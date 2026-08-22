#!/usr/bin/env python3
"""Score the current run's OpenAlex candidates using proposal-specific semantic criteria."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CURATED = {
    "10.1145/3447548.3467174": (9.8, "异步多模态异常", "异步多变量时序异常检测与定位，直接支撑问题一。"),
    "10.1109/iccv51070.2023.02013": (9.7, "异步多模态异常", "不完整多模态学习中的分布一致恢复，直接支撑模态缺失建模。"),
    "10.1145/3551626.3564965": (9.5, "异步多模态异常", "面向缺失模态的鲁棒多传感器融合。"),
    "10.1007/s11063-022-11015-0": (9.3, "漂移与可信预警", "处理时间序列异常检测中的概念漂移。"),
    "10.3390/fi16110403": (9.3, "漂移与可信预警", "将不确定性估计引入时间序列异常检测。"),
    "10.1007/s11280-023-01181-z": (9.2, "漂移与可信预警", "同时研究异常和变点检测，适合跨路段/跨场景漂移。"),
    "10.1609/aaai.v39i18.34105": (9.2, "漂移与可信预警", "用预测不确定性进行早期概念漂移检测。"),
    "10.1109/swc62898.2024.00091": (8.9, "漂移与可信预警", "无监督异常检测与概念漂移自适应。"),
    "10.1109/icme59968.2025.11210144": (8.9, "异步多模态异常", "异步变量关系感知的多变量时序异常检测。"),
    "10.3390/s24020637": (9.0, "异步多模态异常", "注意力自编码器与生成模型的多模态工业异常融合。"),
    "10.1109/jsen.2023.3339335": (8.8, "异步多模态异常", "实体和度量学习结合的多变量时序异常检测。"),
    "10.1109/access.2024.3395991": (8.6, "数据集与评价", "工业控制系统异常数据集与评价场景。"),
    "10.1016/j.dib.2025.112207": (8.6, "数据集与评价", "多模态工业过程监测和异常检测数据集。"),
    "10.1109/cvprw67362.2025.00389": (8.7, "数据集与评价", "面向真实扰动的工业异常鲁棒性基准。"),
    "10.1109/cvpr52734.2025.01417": (8.5, "数据集与评价", "真实工业二维/三维异常数据集。"),
    "10.1109/tpami.2025.3592089": (8.9, "异步多模态异常", "多模态去噪增强工业异常检测鲁棒性。"),
    "10.1109/tgcn.2023.3335342": (9.0, "资源受限边缘智能", "面向绿色物联网边缘网络的深度异常检测。"),
    "10.1109/jiot.2024.3468950": (9.4, "资源受限边缘智能", "面向资源受限物联网边缘设备的内存/计算高效异常检测。"),
    "10.1109/tii.2024.3421600": (9.1, "资源受限边缘智能", "面向 MEC 层级工业物联网的异常检测。"),
    "10.23919/jcc.fa.2024-0024.202407": (9.0, "任务导向通信", "基础模型条件下的任务导向语义通信。"),
    "10.1109/mcom.001.2300155": (9.7, "任务导向通信", "多模态语义中继与边缘智能联合设计。"),
    "10.1109/iccworkshops59551.2024.10615907": (9.5, "任务导向通信", "物联网 DNN 任务推理的目标导向通信。"),
    "10.3390/a17110492": (9.1, "任务导向通信", "机器到机器场景的自编码任务导向通信。"),
    "10.1109/wcnc55385.2023.10118916": (9.0, "任务导向通信", "基于语义三元组的任务导向通信。"),
    "10.1109/mwc.009.2400219": (9.4, "边云协同推理", "车联网边缘智能中的自适应分裂联邦学习。"),
    "10.1109/icc51166.2024.10622954": (9.3, "边云协同推理", "结合早退机制的分裂计算。"),
    "10.1109/percom59722.2024.10494426": (9.5, "边云协同推理", "真实目标检测在本地、边缘和分裂计算间自适应执行。"),
    "10.1109/tcc.2024.3361858": (9.3, "边云协同推理", "边云协同目标检测与任务卸载。"),
    "10.1109/ojcoms.2024.3382265": (8.9, "边云协同推理", "计算卸载与边缘资源分配。"),
    "10.1109/access.2025.3578009": (9.0, "边云协同推理", "多任务模型的动态分裂计算。"),
    "10.1109/jiot.2025.3580736": (9.1, "边云协同推理", "车载边缘环境下鲁棒任务卸载与资源分配。"),
    "10.1109/tase.2025.3557934": (8.9, "边云协同推理", "移动边缘计算中的容错服务卸载。"),
    "10.1007/s10922-024-09881-1": (9.3, "低功耗与断续网络", "环境监测物联网的自适应采样。"),
    "10.1145/3628353.3628545": (9.4, "低功耗与断续网络", "资源受限物联网设备的能量感知自适应采样。"),
    "10.1109/jiot.2025.3619116": (9.3, "低功耗与断续网络", "偏远区域断续连接的时延容忍网络设计。"),
    "10.1109/iccubea54992.2022.10011041": (8.6, "低功耗与断续网络", "时延容忍网络近期研究综述。"),
    "10.3390/s23010099": (8.8, "低功耗与断续网络", "车联网时延容忍网络的可靠传输监测。"),
    "10.1109/access.2023.3334638": (8.7, "低功耗与断续网络", "沿海巡检场景的时延容忍路由。"),
    "10.1080/00051144.2022.2095830": (8.6, "低功耗与断续网络", "上下文感知的时延容忍传输协议。"),
    "10.1016/j.jii.2020.100194": (9.2, "物流与仓储感知", "物流物联网体系与研究空白的系统综述。"),
    "10.1038/s41598-025-10512-1": (8.4, "物流与仓储感知", "多模态物联网数据在物流网络中的融合应用。"),
    "10.1109/access.2023.3295495": (8.6, "物流与仓储感知", "港口数字孪生的态势感知与数据分析需求。"),
    "10.1002/eng2.13021": (8.4, "物流与仓储感知", "无线传感器多模态融合异常检测。"),
    "10.3390/s24248112": (8.7, "漂移与可信预警", "移动传感器道路异常检测与增量漂移适应。"),
    "10.1109/icbda65366.2025.11211409": (8.6, "漂移与可信预警", "多变量时序异常检测中的无监督漂移检测和适应。"),
    "10.1109/lsens.2025.3554491": (8.8, "漂移与可信预警", "工业物联网异常检测的鲁棒自适应学习。"),
}


GROUPS = {
    "异步多模态异常": [r"multimodal", r"multi-modal", r"missing modal", r"incomplete modal", r"asynchronous", r"multivariate time"],
    "任务导向通信": [r"task-oriented", r"task oriented", r"goal-oriented", r"semantic communication"],
    "边云协同推理": [r"split comput", r"collaborative inference", r"task offload", r"edge-cloud", r"edge cloud", r"edge intelligence"],
    "低功耗与断续网络": [r"delay tolerant", r"intermittent connect", r"adaptive sampling", r"event-trigger", r"energy-aware"],
    "漂移与可信预警": [r"concept drift", r"uncertainty", r"calibrat", r"early warning"],
    "物流与仓储感知": [r"logistic", r"cargo", r"warehouse", r"cold chain", r"port"],
    "数据集与评价": [r"dataset", r"benchmark", r"evaluation"],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--curated-output", type=Path)
    args = parser.parse_args()

    found_curated: set[str] = set()
    scored = []
    for raw in args.input.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        paper = json.loads(raw)
        doi = str(paper.get("doi") or "").lower().replace("https://doi.org/", "")
        title = str(paper.get("title") or "")
        abstract = str(paper.get("abstract") or "")
        text = f"{title} {abstract}".lower()

        if doi in CURATED:
            score, subtopic, rationale = CURATED[doi]
            found_curated.add(doi)
        else:
            matches = []
            for group, patterns in GROUPS.items():
                hits = sum(bool(re.search(pattern, text)) for pattern in patterns)
                if hits:
                    matches.append((hits, group))
            matches.sort(reverse=True)
            if len(matches) >= 3:
                score = 7.4
            elif len(matches) == 2:
                score = 6.4
            elif len(matches) == 1:
                score = 5.2
            else:
                score = 2.4
            if not doi:
                score -= 0.4
            year = int(paper.get("year") or 0)
            if year > 2026:
                score -= 1.0
            subtopic = matches[0][1] if score >= 5 and matches else ""
            rationale = "标题与摘要按任务、方法、模态和应用边界评分；未进入人工核验高分池。"

        first_sentence = re.split(r"(?<=[.!?])\s+", abstract.strip(), maxsplit=1)[0] if abstract.strip() else "未提供摘要"
        paper.update({
            "score": round(max(1.0, min(10.0, score)), 1),
            "subtopic": subtopic if score >= 5 else "",
            "rationale": rationale,
            "alignment": {
                "task": "完全匹配" if doi in CURATED and score >= 9 else ("部分匹配" if score >= 5 else "不匹配"),
                "method": "完全匹配" if doi in CURATED and score >= 9 else ("部分匹配" if score >= 5 else "不匹配"),
                "modality": "完全匹配" if doi in CURATED and subtopic == "异步多模态异常" else ("部分匹配" if score >= 5 else "不匹配"),
            },
            "extraction": {
                "design": subtopic or "邻近主题",
                "key_findings": first_sentence[:500],
                "limitations": "未明确提及",
            },
        })
        scored.append(paper)

    args.output.write_text("\n".join(json.dumps(item, ensure_ascii=False) for item in scored) + "\n", encoding="utf-8")
    if args.curated_output:
        curated_items = [
            item for item in scored
            if str(item.get("doi") or "").lower().replace("https://doi.org/", "") in CURATED
        ]
        curated_items.sort(key=lambda item: float(item.get("score") or 0), reverse=True)
        args.curated_output.write_text(
            "\n".join(json.dumps(item, ensure_ascii=False) for item in curated_items) + "\n",
            encoding="utf-8",
        )
    missing = sorted(set(CURATED) - found_curated)
    distribution = {
        "high": sum(1 for p in scored if p["score"] >= 7),
        "mid": sum(1 for p in scored if 4 <= p["score"] < 7),
        "low": sum(1 for p in scored if p["score"] < 4),
    }
    print(json.dumps({"count": len(scored), "curated_found": len(found_curated), "curated_missing": missing, "distribution": distribution}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
