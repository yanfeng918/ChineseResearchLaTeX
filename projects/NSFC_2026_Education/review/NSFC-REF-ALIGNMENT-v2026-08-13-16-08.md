# NSFC 参考文献与引用核查报告（草稿：确定性部分）

- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-08`

本文件由脚本生成，包含“确定性检查”结果；请在执行 nsfc-ref-alignment skill 时由宿主 AI 补充“语义匹配核查”部分。

---

# NSFC Ref Integrity Report（确定性）

- generated_at: 2026-08-13T16:08:01
- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-08`

## Summary

- tex_files: 17
- bib_files: 1
- total_citations: 34
- unique_cited_bibkeys: 34
- missing_bibkeys: 0
- duplicate_bibkeys: 0
- field_issues: 0
- invalid_doi: 0

## Warnings

- bibtexparser unavailable (No module named 'bibtexparser'); using manual BibTeX parser (best-effort)

## Missing BibKeys（P0）

- （无）

## Duplicate BibKeys（P0/P1）

- （无）

## Bib Field Issues（P1）

- （无）

## DOI Format Issues（P1）

- （无）

## Next Step（AI 语义核查）

本报告仅包含确定性检查结果。请结合 `ai_ref_alignment_input.json` 由宿主 AI 进一步逐条评估“正文表述是否与该文献匹配”，并在 report_dir（默认 `./references/`）输出最终审核报告。

---

## 宿主 AI 语义匹配核查（已完成）

### 核查范围与方法

依据 `.bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-08/ai_ref_alignment_input.json`，逐条读取34个正文引用所在句及其 BibTeX 题名、年份、载体、DOI 和摘要。核查重点为：教育知识组织、多模态表示/检索、图表理解、检索增强与事实核验、教育资源质量和工程教育六组论断是否与相应文献主题一致。此次正文修订未改动正文引用或参考文献条目，故未启用重复在线元数据抓取；上一轮的联网题名核验记录仍保留在 `QC/v202608131515/`。

### 结论

- 总引用34处、唯一 BibTeX 键34个；确定性检查显示缺失键、重复键、字段缺失和 DOI 格式错误均为0。
- 34个引用均与所在论断主题一致：教育知识图谱/课程知识组织文献支撑教育资源的结构化描述；视觉语言、多模态检索、图表理解文献支撑跨模态表示与候选关系构建；RAG、断言核验与幻觉评测文献支撑来源证据和事实一致性讨论；OER 质量与工程教育文献支撑资源内在质量和工程场景关联。
- 未发现“文献领域明显无关”“将方法论文误作教育效果证据”或“以综述文献支撑未经验证的具体性能数字”等 P0/P1 语义错引。

### 仍应注意的文献使用边界

1. BLIP、CLIP、RAG、FActScore 和 ARES 等文献仅用于论证技术组件、表示学习或事实核验的可行性；正文未将其表述为对新能源课程资源质量或学生学习效果的直接实证，当前口径适当。
2. 工程教育与 OER 文献用于说明场景需求和质量维度，不作为本项目模型性能的证据；项目性能主张仍应由立项后的对照、消融、跨来源留出和专家盲评产生。
3. Bib 库中仍有11个未被正文引用的条目。它们不影响本次引用一致性，但若最终不使用，建议在正式提交前从库中删除或补齐其载体字段，以减少参考文献维护噪声。

### 最终等级

- P0：0
- P1：0（仅保留“未引用条目清理”的 P2 维护建议）
- 引用一致性结论：通过。
