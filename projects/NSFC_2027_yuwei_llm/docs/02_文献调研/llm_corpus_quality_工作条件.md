# 工作条件
- 主题: 中文预训练语料质量与训练效用的耦合机制和可迁移评价
- 档位: basic
- 目标字数: 3000–6000（可覆盖）
- 目标参考文献: 30–60（可覆盖）
- 最高原则: 不可偷懒/短视，需说明不确定性处理。

## ⚠️ 内容分离原则（防止 AI 流程泄露）

**重要**：本文件用于记录 AI 工作流程和方法学信息。
综述正文（{主题}_review.tex）必须完全聚焦领域知识，不应出现任何以下内容：
- ❌ '本综述基于 X 条初检文献、去重后 Y 条、最终保留 Z 篇'
- ❌ '方法学上，本综述按照检索→去重→评分→选文→写作的管线执行'
- ❌ 任何提及'检索'、'去重'、'相关性评分'、'选文'、'字数预算'等元操作的描述

这些方法学信息应记录在本文件的相应章节（Search Log、Relevance Scoring & Selection 等），
而**不是**放在综述正文中。目标是让读者感受不到这是 AI 生成的综述。

---

## Search Plan
- 以预训练数据质量、数据选择、数据价值、混合优化、去重与污染、规模律、中文语料和学习动力学为 10 组英文查询。
- 主检索源为 OpenAlex，外部补充核验优先使用 ACL Anthology、arXiv 与论文官方页面。
- 时间重点覆盖 2021--2026 年，同时保留规模律、训练数据抽取等必要奠基工作。
## Search Log
- 10 组查询共返回 499 条记录，查询内合并后 415 条。
- 详细日志：`output/artifacts/search_log_llm_corpus_quality.json`。
## Dedup
- 依据 DOI、题名相似度与年份窗口去重，415 条合并为 406 条，跨 DOI 合并 9 条。
- 映射：`output/artifacts/dedupe_map_llm_corpus_quality.json`。
## Relevance Scoring & Selection
- 按任务、方法和模态对题名与摘要逐条语义审查；优先保留直接研究预训练数据质量、选择、混合、数据价值、去重或外部效度的工作。
- 评分分布：高分 46 条、中分 36 条、低分 324 条。低分比例高源于宽查询返回了大量医学、视觉和一般数据科学文献，未为追求形式分布而抬高相关性。
- 最终选入 45 条，摘要覆盖率 100\%。
- **⚠️ 评分分布异常警告（如适用）**：
  - 如果所有文献评分均为 1.0（保底评分），说明评分机制失效
  - 可能原因：中文主题导致脚本评分无法提取有效 token（v3.6 及更早版本）
  - 建议：使用 AI 评分（v3.7+）或将主题转为英文
- 评分文件路径：`output/artifacts/scored_papers_{主题}.jsonl`
## Data Extraction Table（数据抽取表）
- 数据抽取表路径：`output/reference/data_extraction_table.md`
- 包含每篇文献的 Score、Subtopic、DOI、Year、Title、Venue、Design、Key findings、Limitations
## Review Structure
- 语料质量的概念分解；质量筛选与语料治理；数据价值与学习动力学；数据混合、规模律与训练效用；中文语料与跨域迁移；讨论、展望与结论。
## Validation
- 待 `validate_counts.py`、`validate_review_tex.py` 与导出阶段自动回填。
