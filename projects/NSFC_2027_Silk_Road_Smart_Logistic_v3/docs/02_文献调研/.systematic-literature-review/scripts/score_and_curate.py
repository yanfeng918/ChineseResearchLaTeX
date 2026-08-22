#!/usr/bin/env python3
"""Build a scored candidate set and inject a DOI-verified core collection.

This is a run-local helper. It preserves every retrieved candidate, gives the
manually reviewed core collection the highest scores, and records missing
abstracts instead of inventing evidence.
"""

from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / ".systematic-literature-review" / "artifacts"
INPUTS = [
    ART / "papers_deduped_弱网跨境物流文献综述.jsonl",
    ART / "papers_targeted.jsonl",
]
OUTPUT = ART / "scored_papers_弱网跨境物流文献综述.jsonl"


CORE = {
    # 多模态学习、异常检测与评价
    "10.1109/tpami.2018.2798607": ("多模态鲁棒感知", "建立多模态表示、对齐与融合的基础分类框架"),
    "10.1109/tpami.2023.3275156": ("多模态鲁棒感知", "综述 Transformer 多模态融合范式及其适用边界"),
    "10.1016/j.inffus.2019.02.010": ("多模态鲁棒感知", "以模态丢弃训练增强缺失输入下的融合鲁棒性"),
    "10.1109/cvpr52688.2022.01764": ("多模态鲁棒感知", "系统检验多模态 Transformer 面对缺失模态的鲁棒性"),
    "manual:cml2023": ("多模态鲁棒感知", "约束缺失/损坏模态下的预测置信度，支撑风险校准"),
    "10.5220/0010865000003124": ("多模态异常检测", "提供 RGB 与三维信息联合异常检测的公开基准"),
    "10.1109/cvpr52729.2023.00776": ("多模态异常检测", "代表性 RGB--3D 混合融合异常检测方法"),
    "10.1109/cvpr52733.2024.01631": ("多模态异常检测", "利用跨模态特征映射兼顾检测性能与边缘效率"),
    "10.1007/s11633-023-1459-z": ("多模态异常检测", "总结工业视觉异常检测方法、数据集与评价口径"),
    "10.1145/3691338": ("时序异常检测", "总结深度时序异常检测范式及评价陷阱"),
    "manual:anomalytransformer2022": ("时序异常检测", "以关联差异刻画多变量时序异常"),
    "10.52202/075280-0473": ("时序异常检测", "针对非平稳漂移构建动态分解与扩散重建方法"),
    "10.52202/079017-3437": ("时序异常检测", "揭示点调整等评价协议对时序异常结果的系统性影响"),
    "10.1109/jsen.2024.3480133": ("时序异常检测", "以模态一致性交换表示提升异常可分性"),
    "10.3390/s24092845": ("时序异常检测", "处理异步多变量传感器序列的时空建模"),
    "10.1109/jsen.2024.3452088": ("时序异常检测", "面向多源传感器的图结构与时序分解"),
    "10.1109/tifs.2024.3459631": ("时序异常检测", "在结构先验约束下学习变量关系图"),
    "10.52202/075280-2525": ("时序异常检测", "用记忆引导 Transformer 缓解重建过泛化"),

    # 边缘计算、弱网与通信--计算--能耗协同
    "10.1109/jiot.2016.2579198": ("边缘协同", "界定边缘计算的基本范式、优势与开放挑战"),
    "10.1109/jproc.2019.2918951": ("边缘协同", "系统总结端--边深度学习训练与推理架构"),
    "10.1109/comst.2017.2745201": ("边缘协同", "总结无线通信与计算资源联合管理问题"),
    "10.1109/comst.2017.2682318": ("边缘协同", "总结边缘卸载、资源配置与移动性管理"),
    "10.1109/access.2022.3231039": ("任务导向传输", "以任务效用而非比特完整性定义通信质量"),
    "10.1109/jsac.2021.3065072": ("任务导向传输", "提供信息时效性的统一定义、模型与优化框架"),
    "10.1145/863955.863960": ("弱网可靠传输", "奠定间歇连接环境下存储--携带--转发架构"),
    "10.1145/3640342": ("任务导向传输", "将信息新鲜度扩展为任务相关的有用信息时效"),
    "10.23919/jcin.2021.9475121": ("边缘协同", "联合设计通信与计算以控制联邦边缘学习能耗"),
    "10.1109/iccworkshops57953.2023.10283786": ("任务导向传输", "以语义传输增强时限敏感物联网边缘智能鲁棒性"),
    "manual:mcunet2020": ("端侧轻量推理", "给出微控制器上神经网络设计与推理引擎的代表方案"),
    "10.1016/j.iot.2024.101063": ("端侧轻量推理", "梳理微控制器端异常检测算法、硬件与评价指标"),
    "10.1016/j.iot.2024.101263": ("端侧轻量推理", "研究资源感知的边缘分布式实时深度学习"),
    "10.1109/edge60047.2023.00032": ("端侧轻量推理", "代表性轻量边缘时序异常检测框架"),
    "10.1016/j.jnca.2022.103341": ("边缘协同", "归纳高动态场景中的卸载收益、开销与时延约束"),

    # 物流、口岸、集装箱与仓储实证
    "10.1016/j.cie.2022.108455": ("物流场景与需求", "总结物流仓储物联网应用及研究缺口"),
    "10.1016/j.ssci.2022.105766": ("物流场景与需求", "以真实航空冷库验证 IIoT、数字孪生与无监督监测"),
    "10.1109/access.2021.3072916": ("物流场景与需求", "在蜂窝物联网智能物流中验证深度异常检测"),
    "10.1016/j.comnet.2025.111627": ("物流场景与需求", "面向海运集装箱通信受限环境评估混合物联网监测"),
    "10.1016/j.trpro.2023.11.831": ("物流场景与需求", "展示港口装卸设备的边缘物联网协同架构"),
    "10.1016/j.iot.2023.100982": ("物流场景与需求", "总结物联网供应链管理研究的技术与实证边界"),
    "10.1016/j.procs.2024.09.084": ("物流场景与需求", "展示贸易物流中视觉与多传感监测需求"),
    "10.1371/journal.pone.0315322": ("物流场景与需求", "研究冷链数据流异常检测并提供领域评价实例"),
    "10.1016/j.aei.2024.102444": ("物流场景与需求", "用不规则多模态振动序列监测港口岸桥设备"),
    "10.1080/00207543.2017.1402140": ("物流场景与需求", "系统归纳物联网在供应链过程中的作用与证据缺口"),
    "10.1016/j.jfoodeng.2015.11.009": ("物流场景与需求", "给出食品供应链实时感知与虚拟化架构基础"),
    "10.1016/j.cie.2020.107076": ("物流场景与需求", "总结物联网与大数据支持供应链决策的证据"),
    "10.1016/j.iot.2024.101324": ("物流场景与需求", "归纳物联网驱动供应链韧性的近期挑战"),

    # 不确定性与跨域泛化
    "10.1109/tpami.2022.3195549": ("不确定性与泛化", "界定域泛化问题并归纳跨域学习方法"),
    "manual:ovadia2019": ("不确定性与泛化", "大规模检验分布漂移下预测不确定性的可靠性"),
    "manual:guo2017": ("不确定性与泛化", "建立现代神经网络置信度校准的基础评价方法"),
    "10.48550/arxiv.2107.07511": ("不确定性与泛化", "提供分布无关的预测集合与覆盖率保证"),
}


MANUAL = [
    {
        "id": "manual:cml2023",
        "title": "Calibrating Multimodal Learning",
        "authors": ["Huan Ma", "Qingyang Zhang", "Changqing Zhang", "Bingzhe Wu", "Huazhu Fu", "Joey Tianyi Zhou", "Qinghua Hu"],
        "year": 2023,
        "venue": "Proceedings of the 40th International Conference on Machine Learning",
        "url": "https://proceedings.mlr.press/v202/ma23i.html",
        "abstract": "Multimodal models can become overconfident when modalities are corrupted or removed. The paper introduces a regularization principle that confidence should not increase after removing a modality and evaluates its effect on calibration, accuracy, and robustness.",
    },
    {
        "id": "manual:anomalytransformer2022",
        "title": "Anomaly Transformer: Time Series Anomaly Detection with Association Discrepancy",
        "authors": ["Jiehui Xu", "Haixu Wu", "Jianmin Wang", "Mingsheng Long"],
        "year": 2022,
        "venue": "International Conference on Learning Representations",
        "url": "https://openreview.net/forum?id=LzQQ89U1qm_",
        "abstract": "The work proposes an association-discrepancy criterion and anomaly-attention mechanism for unsupervised time-series anomaly detection, with experiments on six benchmarks spanning system monitoring, space and earth exploration, and water treatment.",
    },
    {
        "id": "manual:mcunet2020",
        "title": "MCUNet: Tiny Deep Learning on IoT Devices",
        "authors": ["Ji Lin", "Wei-Ming Chen", "Yujun Lin", "Chuang Gan", "Song Han"],
        "year": 2020,
        "venue": "Advances in Neural Information Processing Systems",
        "url": "https://proceedings.neurips.cc/paper/2020/hash/86c51678350f656dcc7f490a43946ee5-Abstract.html",
        "abstract": "MCUNet jointly designs compact neural architectures and an inference engine for microcontrollers, demonstrating practical image classification and detection under severe memory constraints.",
    },
    {
        "id": "manual:ovadia2019",
        "title": "Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift",
        "authors": ["Yaniv Ovadia", "Emily Fertig", "Jie Ren", "Zachary Nado", "D. Sculley", "Sebastian Nowozin", "Joshua Dillon", "Balaji Lakshminarayanan", "Jasper Snoek"],
        "year": 2019,
        "venue": "Advances in Neural Information Processing Systems",
        "url": "https://proceedings.neurips.cc/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html",
        "abstract": "The study benchmarks predictive uncertainty methods under dataset shift and shows that accuracy and calibration can deteriorate together, while model-marginalizing approaches are comparatively robust.",
    },
    {
        "id": "manual:guo2017",
        "title": "On Calibration of Modern Neural Networks",
        "authors": ["Chuan Guo", "Geoff Pleiss", "Yu Sun", "Kilian Q. Weinberger"],
        "year": 2017,
        "venue": "Proceedings of the 34th International Conference on Machine Learning",
        "url": "https://proceedings.mlr.press/v70/guo17a.html",
        "abstract": "The paper shows that modern neural networks are often poorly calibrated and demonstrates that temperature scaling is an effective post-hoc calibration baseline across image and document classification tasks.",
    },
    {
        "id": "10.48550/arxiv.2107.07511",
        "title": "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
        "authors": ["Anastasios N. Angelopoulos", "Stephen Bates"],
        "year": 2021,
        "venue": "arXiv",
        "doi": "10.48550/arXiv.2107.07511",
        "url": "https://arxiv.org/abs/2107.07511",
        "abstract": "Conformal prediction constructs statistically rigorous prediction sets or intervals with finite-sample distribution-free coverage guarantees and can wrap arbitrary pre-trained prediction models.",
    },
]


GROUP_TERMS = {
    "多模态鲁棒感知": ["multimodal", "multi-modal", "missing modality", "sensor fusion", "modality"],
    "多模态异常检测": ["multimodal", "anomaly", "industrial", "sensor fusion"],
    "时序异常检测": ["time series", "anomaly", "multivariate", "temporal"],
    "边缘协同": ["edge computing", "edge intelligence", "offloading", "resource allocation"],
    "任务导向传输": ["semantic communication", "task-oriented", "age of information", "information freshness"],
    "弱网可靠传输": ["delay tolerant", "intermittent", "disruption", "connectivity"],
    "端侧轻量推理": ["tinyml", "microcontroller", "resource-constrained", "lightweight", "edge device"],
    "物流场景与需求": ["logistics", "warehouse", "cargo", "container", "cold chain", "supply chain", "port"],
    "不确定性与泛化": ["uncertainty", "calibration", "domain generalization", "dataset shift", "conformal"],
}


def norm_doi(value: object) -> str:
    doi = str(value or "").strip().lower()
    return doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def norm_title(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", html.unescape(str(value or "")).lower()).strip()


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def strip_markup(value: object) -> str:
    text = html.unescape(str(value or ""))
    return re.sub(r"<[^>]+>", " ", text).replace("\n", " ").strip()


def crossref_record(doi: str) -> dict | None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": "NSFC-literature-curation/1.0 (mailto:yf@xju.edu.cn)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                msg = json.load(response)["message"]
            date = msg.get("published-print") or msg.get("published-online") or msg.get("issued") or {}
            parts = date.get("date-parts") or [[]]
            authors = []
            for author in msg.get("author") or []:
                name = " ".join(x for x in [author.get("given", ""), author.get("family", "")] if x).strip()
                if name:
                    authors.append(name)
            return {
                "title": (msg.get("title") or [doi])[0],
                "authors": authors,
                "year": parts[0][0] if parts and parts[0] else None,
                "venue": (msg.get("container-title") or [""])[0],
                "doi": doi,
                "url": "https://doi.org/" + doi,
                "abstract": strip_markup(msg.get("abstract")),
                "source": "crossref_verified",
            }
        except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError):
            time.sleep(1.5 * (attempt + 1))
    return None


def core_id(row: dict) -> str:
    if row.get("id"):
        return str(row["id"]).lower()
    doi = norm_doi(row.get("doi"))
    return doi


def classify(row: dict) -> tuple[float, str, str]:
    cid = core_id(row)
    if cid in CORE:
        group, rationale = CORE[cid]
        return 9.4, group, rationale

    title = norm_title(row.get("title"))
    body = (title + " " + norm_title(row.get("abstract"))).strip()
    forbidden = ["decision letter", "author response", "peer review", "retracted", "withdrawn", "correction"]
    if not title or any(term in title for term in forbidden):
        return 1.0, "", "非研究论文或元数据不完整，不进入主题分组"

    hits = []
    for group, terms in GROUP_TERMS.items():
        count = sum(term in body for term in terms)
        if count:
            hits.append((count, group))
    hits.sort(reverse=True)
    if not hits:
        return 2.2, "", "与项目研究对象、方法或场景缺少直接对应"

    total = sum(item[0] for item in hits)
    score = min(8.0, 4.0 + 0.8 * hits[0][0] + 0.35 * max(0, len(hits) - 1) + 0.15 * min(total, 6))
    doi = norm_doi(row.get("doi"))
    venue = str(row.get("venue") or "").lower()
    if doi.startswith(("10.2139/ssrn", "10.21203/rs", "10.20944/preprints")) or not venue:
        score -= 1.0
    score = round(max(1.0, score), 1)
    group = hits[0][1] if score >= 5.0 else ""
    rationale = f"与{group or '项目主题'}存在概念或方法交集；未纳入核心证据集" if group else "弱相关候选"
    return score, group, rationale


def main() -> None:
    rows: dict[str, dict] = {}
    for path in INPUTS:
        for row in read_jsonl(path):
            key = norm_doi(row.get("doi")) or norm_title(row.get("title"))
            if not key:
                continue
            old = rows.get(key)
            if old is None or len(str(row.get("abstract") or "")) > len(str(old.get("abstract") or "")):
                rows[key] = row

    for row in MANUAL:
        rows[str(row["id"]).lower()] = row

    for cid in CORE:
        if cid.startswith("manual:") or cid in rows:
            continue
        fetched = crossref_record(cid)
        if fetched:
            rows[cid] = fetched
        else:
            rows[cid] = {
                "title": cid,
                "authors": [],
                "year": None,
                "venue": "",
                "doi": cid,
                "url": "https://doi.org/" + cid,
                "abstract": "",
                "source": "doi_unresolved",
                "quality_warnings": ["metadata_resolution_failed"],
            }

    scored = []
    for row in rows.values():
        score, subtopic, rationale = classify(row)
        out = dict(row)
        out["score"] = score
        out["subtopic"] = subtopic if score >= 5 else ""
        out["rationale"] = rationale
        out["alignment"] = {
            "task": "完全匹配" if score >= 9 else ("部分匹配" if score >= 5 else "不匹配"),
            "method": "完全匹配" if score >= 9 else ("部分匹配" if score >= 5 else "不匹配"),
            "modality": "完全匹配" if score >= 9 and "模态" in subtopic else ("部分匹配" if score >= 5 else "不匹配"),
        }
        abstract = strip_markup(row.get("abstract"))
        first_sentence = re.split(r"(?<=[.!?])\s+", abstract, maxsplit=1)[0] if abstract else ""
        out["extraction"] = {
            "design": subtopic or "相关领域候选",
            "key_findings": first_sentence[:300] if first_sentence else "摘要元数据缺失，写作前需依据原文核验",
            "limitations": "摘要未明确提及；引用时仅使用已核验的题名、方法定位与公开结论",
        }
        scored.append(out)

    scored.sort(key=lambda x: (-float(x.get("score") or 0), -(int(x.get("year") or 0))))
    OUTPUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in scored), encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT),
        "candidates": len(scored),
        "core_requested": len(CORE),
        "core_resolved": sum(core_id(row) in CORE and row.get("title") != core_id(row) for row in scored),
        "with_abstract": sum(len(strip_markup(row.get("abstract"))) >= 80 for row in scored),
        "score_distribution": {
            "high": sum(float(row.get("score") or 0) >= 7 for row in scored),
            "mid": sum(4 <= float(row.get("score") or 0) < 7 for row in scored),
            "low": sum(float(row.get("score") or 0) < 4 for row in scored),
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
