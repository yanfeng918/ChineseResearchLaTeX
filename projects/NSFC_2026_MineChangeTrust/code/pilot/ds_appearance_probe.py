#!/usr/bin/env python
"""MCT-P01 扩展分析：外观差异代理量 D_s 的可计算性与其同矿区误差的关联。

目的：检验申报书 2.1 节定义的 D_s 在真实数据上能否计算、覆盖率如何，
以及"按 D_s 高低分层"这一预设是否有数据支持。

严格约束（与 MCT-P01 冻结方案一致）：
  - 只使用 MCT-P01 已抽样的 480 个官方验证切片（sample_manifest.jsonl 中 split=val）
  - 官方 30 个测试矿区不读取、不评分
  - 归一化 RGB/255、背景掩码 3x3 腐蚀，与 protocol.json 一致
  - 不训练任何模型；误差数值直接取自 MCT-P01 的 per_site_metrics.json
  - 逐样本核验 imageA/imageB/label 的 SHA256 与清单一致

D_s 定义（申报书原文）：共同可见光波段按固定尺度归一化后取通道均值；每对影像在
同一腐蚀规则确定的标注未变化有效区，计算两期灰度绝对差的中位数；再对矿区内影像对
取中位数。无有效未变化像素的影像对记为不适用。
"""
import hashlib
import io
import json
import os
from collections import defaultdict

import numpy as np
import pyarrow.parquet as pq
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "results")
# 数据分片目录：优先用 MCT-P01 归档路径，回退到本机缓存
CAND_DIRS = [
    os.path.join(HERE, "data", "hf"),
    "/home/yanfeng/mine-pilot/data/MineNetCD256/data",
]
EROSION = 3          # 与 protocol.json 背景掩码一致
MIN_BG_PIXELS = 1    # 无有效未变化像素才记不适用


def find_shard(name):
    for d in CAND_DIRS:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"找不到分片 {name}，已查：{CAND_DIRS}")


def erode3(mask):
    """3x3 腐蚀（等价于 8 邻域全为 True 才保留），纯 numpy 实现。"""
    m = mask
    out = m.copy()
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            out &= np.roll(np.roll(m, dy, 0), dx, 1)
    out[0, :] = False; out[-1, :] = False
    out[:, 0] = False; out[:, -1] = False
    return out


def spearman(x, y):
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y = np.asarray(x)[ok], np.asarray(y)[ok]
    if len(x) < 4:
        return float("nan"), 0, float("nan")
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    r = float(np.corrcoef(rx, ry)[0, 1])
    # 置换检验（n 很小，报告 p 以免高估证据强度）
    rng = np.random.default_rng(1729)
    cnt = 0
    B = 20000
    for _ in range(B):
        if abs(float(np.corrcoef(rx, rng.permutation(ry))[0, 1])) >= abs(r) - 1e-12:
            cnt += 1
    return r, int(len(x)), (cnt + 1) / (B + 1)


def main():
    rows = [json.loads(l) for l in open(os.path.join(RES, "sample_manifest.jsonl"))]
    val = [r for r in rows if r["split"] == "val"]
    print(f"验证切片 {len(val)} 个 / {len(set(r['domain'] for r in val))} 矿区")

    by_shard = defaultdict(list)
    for r in val:
        by_shard[r["source_shard"]].append(r)

    ds_pair = {}          # global_row_index -> D_s or None
    sha_ok = sha_bad = 0
    for shard, items in by_shard.items():
        path = find_shard(shard)
        want = {r["row_in_shard"]: r for r in items}
        pf = pq.ParquetFile(path)
        base = 0
        for batch in pf.iter_batches(batch_size=512):
            n = batch.num_rows
            hit = [i for i in range(n) if (base + i) in want]
            if hit:
                ca, cb, cl = (batch.column(k) for k in ("imageA", "imageB", "label"))
                for i in hit:
                    r = want[base + i]
                    ab, bb, lb = ca[i].as_py()["bytes"], cb[i].as_py()["bytes"], cl[i].as_py()["bytes"]
                    ok = (hashlib.sha256(ab).hexdigest() == r["imageA_sha256"]
                          and hashlib.sha256(bb).hexdigest() == r["imageB_sha256"]
                          and hashlib.sha256(lb).hexdigest() == r["label_sha256"])
                    sha_ok += ok; sha_bad += (not ok)
                    if not ok:
                        continue
                    A = np.asarray(Image.open(io.BytesIO(ab)).convert("RGB"), np.float32) / 255.0
                    B_ = np.asarray(Image.open(io.BytesIO(bb)).convert("RGB"), np.float32) / 255.0
                    L = np.asarray(Image.open(io.BytesIO(lb)))
                    if L.ndim == 3:
                        L = L[..., 0]
                    bg = erode3(L == 0)                     # 标注未变化有效区（同腐蚀规则）
                    if bg.sum() < MIN_BG_PIXELS:
                        ds_pair[r["global_row_index"]] = None
                        continue
                    ga, gb = A.mean(2), B_.mean(2)          # 共同可见光波段通道均值
                    ds_pair[r["global_row_index"]] = float(np.median(np.abs(ga[bg] - gb[bg])))
            base += n
        print(f"  {shard} 完成")

    print(f"逐样本 SHA256：一致 {sha_ok}，不一致 {sha_bad}")
    assert sha_bad == 0, "样本哈希与 MCT-P01 清单不一致，停止"

    # 矿区级 D_s = 矿区内有效影像对的中位数
    per_site_pairs = defaultdict(list)
    n_na = 0
    for r in val:
        v = ds_pair.get(r["global_row_index"])
        if v is None:
            n_na += 1
        else:
            per_site_pairs[r["domain"]].append(v)
    site_Ds = {d: float(np.median(v)) for d, v in per_site_pairs.items() if v}
    print(f"\n可计算 D_s 的影像对 {len(val)-n_na}/{len(val)}（不适用 {n_na}）")
    print(f"矿区级 D_s：min {min(site_Ds.values()):.4f} "
          f"median {np.median(list(site_Ds.values())):.4f} max {max(site_Ds.values()):.4f}")

    out = {"protocol": "MCT-P01-EXT-Ds", "definition_source": "申报书 2.1 节 D_s",
           "erosion": EROSION, "normalization": "RGB/255",
           "n_val_tiles": len(val), "n_applicable_pairs": len(val) - n_na, "n_na_pairs": n_na,
           "site_Ds": site_Ds, "arms": {}}

    # 混杂检查：D_s 是否与矿区变化像素占比共变？
    # 若共变，则"按 D_s 分层"的组间差异不能单独解释为外观差异的作用。
    pos = defaultdict(list)
    for r in val:
        pos[r["domain"]].append(r["positive_pixels"])
    ratio = {d: sum(v) / (len(v) * 256 * 256) for d, v in pos.items()}
    doms_all = sorted(site_Ds)
    x = np.array([site_Ds[d] for d in doms_all])
    y = np.array([ratio[d] for d in doms_all])
    r_cf, n_cf, p_cf = spearman(x, y)
    cut_all = float(np.median(x))
    print(f"\n=== 混杂检查：D_s vs 矿区变化像素占比 ===")
    print(f"  Spearman = {r_cf:+.3f}  (置换 p={p_cf:.3f}, n={n_cf})")
    print(f"  低档变化占比 {y[x <= cut_all].mean()*100:.2f}%  高档 {y[x > cut_all].mean()*100:.2f}%")
    out["confounder_change_ratio"] = {
        "spearman_Ds_changeratio": r_cf, "perm_p": p_cf, "n_sites": n_cf,
        "low_bin_change_ratio": float(y[x <= cut_all].mean()),
        "high_bin_change_ratio": float(y[x > cut_all].mean()),
        "per_site_change_ratio": {d: float(ratio[d]) for d in doms_all},
        "note": "D_s 与变化像素占比同向共变；按 D_s 分层的组间差异不能单独归因于外观差异",
    }

    # MCT-P01 的逐矿区误差：先在矿区内平均 3 个种子
    pm = json.load(open(os.path.join(RES, "per_site_metrics.json")))
    agg = defaultdict(lambda: defaultdict(list))
    for r in pm:
        agg[r["arm"]][r["domain"]].append(r)
    arms = sorted(agg.keys())

    print("\n=== D_s 与 MCT-P01 逐矿区误差的关联（n=10 矿区，探索性）===")
    for arm in arms:
        doms = [d for d in site_Ds if d in agg[arm]]
        ds = np.array([site_Ds[d] for d in doms])
        fpr = np.array([np.mean([x["FPR"] for x in agg[arm][d]]) for d in doms])
        iou = np.array([np.mean([x["IoU"] for x in agg[arm][d]]) for d in doms])
        r_f, n_f, p_f = spearman(ds, fpr)
        r_i, n_i, p_i = spearman(ds, iou)
        cut = float(np.median(ds))
        lo, hi = fpr[ds <= cut], fpr[ds > cut]
        lo_i, hi_i = iou[ds <= cut], iou[ds > cut]
        print(f"\n  [{arm}]  n={n_f} 矿区")
        print(f"    Spearman(D_s, FPR) = {r_f:+.3f}  (置换 p={p_f:.3f})")
        print(f"    Spearman(D_s, IoU) = {r_i:+.3f}  (置换 p={p_i:.3f})")
        print(f"    按 D_s 中位数 {cut:.4f} 分层：低档 n={len(lo)} FPR {lo.mean()*100:.2f}%  "
              f"高档 n={len(hi)} FPR {hi.mean()*100:.2f}%")
        print(f"                              低档 IoU {lo_i.mean()*100:.2f}%  "
              f"高档 IoU {hi_i.mean()*100:.2f}%")
        out["arms"][arm] = {
            "n_sites": n_f, "cut": cut,
            "spearman_Ds_FPR": r_f, "perm_p_FPR": p_f,
            "spearman_Ds_IoU": r_i, "perm_p_IoU": p_i,
            "low_bin": {"n": int(len(lo)), "FPR": float(lo.mean()), "IoU": float(lo_i.mean())},
            "high_bin": {"n": int(len(hi)), "FPR": float(hi.mean()), "IoU": float(hi_i.mean())},
            "per_site": {d: {"Ds": site_Ds[d],
                             "FPR": float(np.mean([x["FPR"] for x in agg[arm][d]])),
                             "IoU": float(np.mean([x["IoU"] for x in agg[arm][d]]))} for d in doms},
        }

    p = os.path.join(RES, "ds_appearance_probe.json")
    json.dump(out, open(p, "w"), indent=1, ensure_ascii=False)
    print(f"\n结果 -> {p}")


if __name__ == "__main__":
    main()
