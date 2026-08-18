# NSFC 参考文献与引用核查报告（草稿：确定性部分）

- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-15-29`

本文件由脚本生成，包含“确定性检查”结果；请在执行 nsfc-ref-alignment skill 时由宿主 AI 补充“语义匹配核查”部分。

---

# NSFC Ref Integrity Report（确定性）

- generated_at: 2026-08-13T15:29:04
- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-15-29`

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

# AI 语义匹配核查（人工补充）

34 个引用分别覆盖教育知识图谱与课程资源组织、多模态表示与检索、图表理解、检索增强与事实核验、出处核验、开放教育资源质量及能源工程教育。逐组核对题名、摘要、DOI 元数据和正文语句后，未发现“文献不支持正文断言”“以文献证明本项目预期性能”或错引问题。

- **P0：0 项。** 引用键、DOI 和最小 BibTeX 字段完整。
- **P1：已处理。** 已为正文所引用的会议论文补齐 venue 字段；仍有少数预印本条目，定稿前可优先替换为同一工作的正式发表版本。
- **局限：** 在线自动核验因当前 Python 3.13 的正则兼容问题不可用；其确定性检查已成功运行，题名和语义核查由本次人工复核与 QC 的联网元数据证据补足。

结论：引用质量可以通过本轮核验；后续只需在提交前复核预印本的正式版本替换，不需要重写立项依据的文献链。
