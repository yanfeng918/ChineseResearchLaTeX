# NSFC 参考文献与引用核查报告（草稿：确定性部分）

- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-15-07`

本文件由脚本生成，包含“确定性检查”结果；请在执行 nsfc-ref-alignment skill 时由宿主 AI 补充“语义匹配核查”部分。

---

# NSFC Ref Integrity Report（确定性）

- generated_at: 2026-08-13T15:07:06
- project_root: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education`
- main_tex: `main.tex`
- run_dir: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/.bensz-api/skills/nsfc-ref-alignment/2026-08-13-15-07`

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

## 核验范围与方法

以 `ai_ref_alignment_input.json` 中的 34 个唯一引用为单位，核对引用语句与题名、摘要、DOI 所指主题之间的对应关系；不以文献支持本项目的预期结果。在线自动核验因当前 Python 3.13 环境下的正则表达式兼容性异常未能执行，已使用离线确定性检查并保留该局限。

## 逐组结论

| 正文主题与引用组 | 文献数 | 语义结论 | 处理 |
| --- | ---: | --- | --- |
| 教育知识图谱、课程概念与多模态教育资源 | 9 | 题名和摘要均支持“已有构建、概念组织、课程知识库与异构教育材料统一描述”的概括；正文没有把已有工作夸大为本项目提出的方法。 | 通过 |
| 多模态表示与跨模态检索 | 10 | 综述、视觉语言预训练、图文/视频文本对比学习文献支持“异质性、关联、表示学习和检索”的背景判断。 | 通过；预印本宜在定稿前优先替换为正式发表版本。 |
| 图表理解 | 4 | 图表摘要、图表问答、图表到表格预训练和图表理解综述均对应正文的任务列举；“课程知识和来源位置联合约束不足”是本项目的研究缺口判断，未归因于某一篇文献。 | 通过 |
| 检索增强、事实性与出处核验 | 11 | RAG、FActScore、ARES、MiniCheck、HaluEval 和 ProVe 分别支持外部检索、原子事实、上下文相关性/忠实性、断言核验、幻觉风险、知识图谱出处核验等表述。 | 通过 |
| 开放教育资源质量与能源工程教育 | 3 | 文献直接支持质量保障和工程情境关联的背景判断；没有据此推导学生学习成效。 | 通过 |

## 问题分级

- **P0：0 项。** 34 个引用键均存在，无重复键、缺失键或 DOI 格式错误。
- **P1：2 项。**
  1. 部分条目的 venue 字段仍为 `Unknown`（如 AltCLIP、ChartAssistant、FActScore、ARES、MiniCheck、HaluEval、RAG/多模态 RAG 综述），不影响正文语义，但会降低参考文献排版的规范性；定稿前应按 DOI 补齐正式会议/期刊信息。
  2. 若干视觉语言基础模型和综述目前引用 arXiv 版本；可保留为可追溯文献，但应优先用 DOI/正式会议版本替换，避免正式申请书中过度依赖预印本。
- **P2：1 项。** 离线解析器提示未安装 `bibtexparser`，但本次 34 个已引用条目未发现解析差异；构建时仍应以 BibTeX 输出作为最终检查。

## 最终结论

正文中引用与其支撑的论述相符，未发现“以文献证明本项目预期性能”或“引用不支持其断言”的问题。现阶段可以进入篇幅、文风、质量和编译审查；参考文献元数据规范化列为定稿前的 P1 修订项。
