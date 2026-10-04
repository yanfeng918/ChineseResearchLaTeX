# CIESM 开放基金申请书

本项目使用 `bensz-thesis` 的独立 `ciesm-open-fund` profile/style。`main.tex` 是已填写、含完整研究内容的审阅稿；`blank.tex` 是独立四页空白模板。官方依据为本目录的[四页 PDF](地球系统数值模拟教育部重点实验室开放基金.pdf)，本次会话已确认以它为准。

正式稿可编辑、可构建。2026-09-11 按[模拟评审意见](comments-from-nsfc-reviewers.md)完成一轮定点修改，并补做了[先行试验](../../tests/ciesm-pilot-20260911/REPORT.md)（结论与图 F08/F09 已写入研究基础）。2026-09-19 已依据 [QC 报告](QC/20260919-2043/final/nsfc-qc_report.md)修正考核目标、评价判据、预实验数字、参考文献及图内编号，并依据[参与者资料](../../docs/applicants/00_参与者信息.md)回填 7 名研究生及其任务分工。2026-09-20 按保留语义信息的目标压缩第一部分，正文汉字由 14405 减至 8490（约减少 41%），完整 PDF 由 38 页减至 31 页；公式、引用与配图保留，详见[压缩记录](../../tests/ciesm-application-20260910/compression-20260920/REPORT.md)。按用户明确的口径，3000 字上限仅针对立项依据；当前立项依据为 2440 汉字，按中文逐字、英文及数字按词统计为 2513 字词。F-CIESM-01 实验室合作人尚待落实；不能据此称为可直接提交的定稿。见[填写说明](填写说明.md)与[验收报告](../../tests/ciesm-application-20260910/REPORT.md)。

后续按要求将 2.4“研究方法”与 2.5“技术路线”合并为 **2.4“研究方法与技术路线”**，两节合计汉字由 3154 减至 2630；随后压缩 2.4.4“多层评价与 CIESM 集成验证”（873 → 703 汉字），删除“关键技术”，现“可行性分析”为 2.5。当前研究内容为 3985 汉字（中英文混合口径 4059 字词），完整 PDF 为 29 页；见[合并记录](../../tests/ciesm-application-20260910/merge-methods-route-20260920/REPORT.md)及[评价压缩与删除记录](../../tests/ciesm-application-20260910/compress-evaluation-20260920/REPORT.md)。

## 构建与编辑

从仓库根目录使用官方入口，两个入口顺序构建：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_CIESM-STSR_final --tex-file blank.tex
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_CIESM-STSR_final
```

分别生成 `blank.pdf` 和 `main.pdf`。中间文件及 SyncTeX 位于 `.latex-cache/`，缓存对应最后一次构建。项目内亦可运行 `python3 scripts/thesis_build.py build --tex-file main.tex`。

VS Code 打开 [NSFC_2026_CIESM-STSR_final.code-workspace](NSFC_2026_CIESM-STSR_final.code-workspace)，LaTeX Workshop 通过 `texlua → scripts/thesis_build.py → thesis_project_tool.py` 构建当前入口；`template.json` 显式声明 `build_profile=thesis`，目录前缀不决定产品线。

需要 Python 3、XeLaTeX、Biber、CTeX、TikZ、biblatex、caption、placeins 及仓库中的 `bensz-thesis`、`bensz-fonts`。Biber 与 XeLaTeX 应在 PATH 中。本机已有 Biber，验收时补齐了与 XeLaTeX 相同用户 bin 目录中的可执行入口；未改动公共构建脚本。独立使用项目时须安装包含本次专属样式的包版本。

## 内容入口

| 路径 | 职责 |
|---|---|
| [metadata.tex](extraTex/metadata.tex) | 身份、完整题目、地址与联系方式、履历、日期、摘要表字段的统一来源 |
| [abstract.tex](extraTex/abstract.tex) | 351 字摘要，包含标点；五个关键词在 metadata 中 |
| [report.tex](extraTex/report.tex) | 官方栏目与六份正文的装配，空白和填写入口共用 |
| `extraTex/1.*.tex`、`extraTex/2.*.tex` | 研究正文、工作基础和申请人简介 |
| [myexample.bib](references/myexample.bib) | 29 条引用题录（27 条经 Crossref、2 条经期刊官网核验；完整记录见 `QC/20260919-2043/evidence/`）；著录格式为 GB/T 7714 顺序编码制，与国自然口径一致；通过 Biber 自动更新，勿维护手工 bibitem 副本 |
| [F01-background.pdf](figures/F01-background.pdf) | 2026-09-19 更新的研究问题示意图，补充尺度差距、局地机制、校正后状态与三类验证；PNG 原图见 `figures/F01-background-v2.png`，生成规范见 `docs/figure_specs/F01-background-v2.json`；PDF 封装位图 |
| `figures/F02-*.pdf` 至 `F07-*.pdf` | 沿用原稿的六张 PDF 矢量图 |
| `figures/F08-pilot-error.pdf`、`F09-pilot-aggregation.pdf` | 先行试验产出的两张诊断图，由 `tests/ciesm-pilot-20260911/make_figures.py` 生成 |
| [budget.tex](extraTex/budget.tex) | 填写稿在原八类科目后增列劳务费 1.10 万元（合计 22 人月 × 500 元），设备费为 0，总额 5.00 万元统一引用 metadata；空白稿保留原八类科目 |
| [resource-manifest.json](docs/resource-manifest.json) | 实际源文件、图、标签、引用及哈希清单 |
| `docs/source-only/` | 原稿实际使用但四页 CIESM 表无对应栏目的 NSFC 声明，留存审阅而不混入官方正文 |

正文使用真正的标题命令：官方部分、栏目及内部子标题分别对应 section、subsection、subsubsection，更细内容用 paragraph。每个官方栏目内部从 1.1、2.1 等连续编号，两大部分分别按其官方栏目编号。图号全篇连续，图注随图同页；栏目切换前排完相关浮动图。

封面长课题名称与上下文字同为15.95bp，分两行且每行各有下划线，后续字段整体下移；信息表字段统一使用10.45bp楷体，课题名称、预期成果与关键词按实际文字高度增加行高，利用摘要区留白容纳，并保留高度溢出报错；预期成果左对齐，完整地址在简介正常换行。新增文字超出固定格容量时，应调整公共包的本模板样式，不能裁掉字段或自动缩小字号。主要参考文献使用10.5bp字号、16bp行距，左对齐，编号贴正文左边界，续行与各条文献的作者文本对齐，条目之间不另加空白。字体及字号复查见[检查记录](../../tests/ciesm-application-20260910/font-consistency-20260919/REPORT.md)，文献排版修订见[文献检查记录](../../tests/ciesm-application-20260910/bibliography-layout-20260919/REPORT.md)。

## 官方空白比对

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py compare --project-dir projects/NSFC_2026_CIESM-STSR_final --tex-file blank.tex --baseline-pdf projects/NSFC_2026_CIESM-STSR_final/地球系统数值模拟教育部重点实验室开放基金.pdf --output-dir tests/ciesm-application-20260910/blank-compare --keep-rasters
```

空白入口使用原生文字与表线，不读取或嵌入官方 PDF。官方正文页没有跨页表框、成员表及签章栏，因此不新增其他模板的这些内容。页脚页码随填写正文自然续页。空白比较仍有字体栅格化和细微位置差异，具体数值与公共包全部直接消费者的回归见验收报告。
