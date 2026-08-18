# NSFC 参考文献与引用核查报告（草稿：确定性部分）

- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-21`

本文件由脚本生成，包含“确定性检查”结果；请在执行 nsfc-ref-alignment skill 时由宿主 AI 补充“语义匹配核查”部分。

---

# NSFC Ref Integrity Report（确定性）

- generated_at: 2026-08-13T16:21:58
- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-21`

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

## 宿主 AI 语义匹配核查（已完成）

依据 .bensz-api/skills/nsfc-ref-alignment/2026-08-13-16-21/ai_ref_alignment_input.json，逐条核查34处正文引用所在句及其题名、年份、载体、DOI和摘要。教育知识组织文献用于异构资源的结构化描述；多模态、检索和图表理解文献用于表示与关系构建；RAG、事实核验和幻觉评测文献用于来源证据与断言支持；OER质量与工程教育文献用于质量维度和工程场景需求。

- 缺失键、重复键、字段问题和 DOI 格式错误均为0。
- 34个引用与其论断主题一致，未发现领域明显无关、张冠李戴、将技术组件论文误作教育效果证据或以综述支持具体性能数字的 P0/P1 风险。
- 本轮只压缩了背景与方法表述，未改动引用键或BibTeX；此前联网题名核验结果继续适用。

P0：0；P1：0。Bib库尚有11个未引用条目，建议最终提交前清理或补齐其载体字段，列为P2维护项。引用一致性结论：通过。
上述语义核查已完成，本报告为最终引用一致性审核结果。
