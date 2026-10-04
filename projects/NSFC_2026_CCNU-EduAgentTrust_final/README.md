# CCNU 教育智能体开放课题申请书（2026版）

本项目依据所供[官方 PDF](华中师范大学人工智能与教育新形态实验室开放课题项目申请书（2026版）.pdf)，用原生 LaTeX 文字、表格和矢量线重建申请书。实际官方空白表为 **7页**，包含横向成员表；没有整页截图或官方 PDF 嵌入。

| 入口 | 输出 | 用途 |
|---|---|---|
| [main.tex](main.tex) | [main.pdf](main.pdf) | 当前申请书工作稿，含已有申请信息、6张原图和完整被引文献；本轮论证扩写后超出7000字要求 |
| [full.tex](full.tex) | [full.pdf](full.pdf) | 未删节迁移审阅版，供逐段对照；篇幅超过官方上限 |
| [blank.tex](blank.tex) | [blank.pdf](blank.pdf) | 独立7页空白模板，供与官方 PDF 比较 |

## 构建与编辑

在仓库中分别运行，**同一项目的入口必须顺序构建**：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_CCNU-EduAgentTrust_final --tex-file blank.tex
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_CCNU-EduAgentTrust_final --tex-file full.tex
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_CCNU-EduAgentTrust_final
```

也可在项目内运行 `python3 scripts/thesis_build.py build --tex-file main.tex`。需要 Python 3、XeLaTeX、共享 `bensz-fonts` 和含 `ccnu-open-fund-2026` 样式的 `bensz-thesis`。完整仓库使用本地公共包；单项目 wrapper 用 `kpsewhich` 定位已安装包。输出 PDF 在项目根目录，中间文件在 `.latex-cache/`。

VS Code 打开[同名工作区](NSFC_2026_CCNU-EduAgentTrust_final.code-workspace)，LaTeX Workshop 使用 `texlua → thesis_build.py → thesis_project_tool.py`，按当前根入口构建。元数据显式声明 `build_profile=thesis`，与 `NSFC_` 目录前缀无关。不要使用 MineChangeTrust 项目的构建路径。

## 维护位置

课题类型在 `metadata.tex` 中设为 `category={一般课题}`，直接填入左侧单元格；后方 `C.一般课题` 保留原表文字，不加圈框。

| 文件 | 内容 |
|---|---|
| [metadata.tex](extraTex/metadata.tex) | 姓名、单位、联系方式、完整地址、个人经历及申请字段唯一来源 |
| [abstract.tex](extraTex/abstract.tex) | 按摘要组织的中文项目简介（正文211字，含标点）及补充联系信息 |
| [foundation.tex](extraTex/foundation.tex) | 简历、研究条件、3项代表作、4项相关在研项目与组织实施安排 |
| [proposal.tex](extraTex/proposal.tex) | 正式版立项依据、研究内容、方案、创新与计划 |
| [proposal-full.tex](extraTex/proposal-full.tex) | 未删节正文，保留迁移来源和完整论证 |
| [figures/](extraTex/figures/) / [原图](figures/) | 两入口共用的图注、标签、引用句与6张原始矢量PDF |
| [references.tex](references/references.tex) / [myexample.bib](references/myexample.bib) | 按仓库国自然 `gbt7714-nsfc` 样式导出的28条题录及数据库；原第9条 LearnLM 已删除，后续连续编号 |
| [members.tex](extraTex/members.tex) / [budget.tex](extraTex/budget.tex) | 已填7名主要成员及分工；已编制5万元预算，明细见[预算测算](docs/预算测算.md) |
| [填写说明](docs/填写说明.md) | 事实状态、整理口径、来源、待补清单与签章流程 |
| [预实验与教学复核安排](docs/预实验与教学复核安排.md) | 样本覆盖、独立试标、合规性量表及策略冻结的拟实施安排；不代表已有实验结果 |

稳定布局、字体、标题命令、图文共同分页、文献条目间距与字段溢出检查维护在[CCNU专属公共样式](../../packages/bensz-thesis/styles/bthesis-style-ccnu-open-fund-2026.tex)。封面、简表和简历引用同一元数据；工作单位等长字段仅在对应单元格调整字号，正文行距不缩小。官方研究栏目标题只在首页出现，续页保留表框和连续页码。正式提纲使用 `section`，内部 `subsection` 在所属提纲下按1.1、1.2连续编号。

参考文献格式直接由[国自然共享 BST](../../packages/bensz-nsfc/assets/bibtex-style/gbt7714-nsfc.bst)生成；两版共用导出的 `references.tex`，日常构建不需要额外安装国自然包。更新数据库后，可在仓库根目录运行 `python3 tests/ccnu-eduagenttrust-template/20260919-references/render_references.py`，按现有条目顺序重新导出，再顺序构建两版；增删条目时需同步正文引用和题录顺序。

## 验收

2026-09-19补充1.2“国内外研究现状”，按四个研究方向展开贡献、适用范围及其与本项目问题的关系；该节按“汉字＋西文词/数字＋标点”、不计引用标号统计约1580字。原19篇引文已核对，28条题录及其他章节不变。当前PDF为19页，研究栏目连同参考文献和图中文字共10702字，仍超7000字要求；详见[本轮报告](../../tests/ccnu-eduagenttrust-template/20260919-research-status/REPORT.md)及[原始来源核对](../../tests/ccnu-eduagenttrust-template/20260919-research-status/SOURCES.md)。

2026-09-19展开2.3节的三个关键科学问题，润色第3部分的实验设计、统计判据、技术路线及可行性，该轮PDF为18页。研究栏目按“汉字＋西文词/数字＋标点”，计入参考文献与六张图内文字共9289字，超过7000字要求2289字；该轮优先完成所指定两部分的论证改写，未压缩其他章节。修改前同口径为7394字，此前5844字的原生PDF文本统计未包含1550字的图内文字。该工作稿尚需篇幅压缩，见[改写与验收报告](../../tests/ccnu-eduagenttrust-template/20260919-scientific-questions/REPORT.md)。

2026-09-19收紧正式研究稿的图文间距，消除第11页的大块留白，PDF由17页减为16页；正文及六张原图尺寸保持不变，见[分页验收报告](../../tests/ccnu-eduagenttrust-template/20260919-whitespace/REPORT.md)。

2026-09-19按正文复查意见更新正式稿的创新贡献、任务效用指标、样本覆盖与预实验安排，验收见[修订报告](../../tests/ccnu-eduagenttrust-template/20260919-revision/REPORT.md)。正式研究方案以 `proposal.tex` / `main.pdf` 为准；`proposal-full.tex` 保留未删节迁移时的论证供追溯，`full.pdf` 同步共用申请信息及简介。

2026-09-19题录格式调整、原第9条删除及两版构建检查见[本轮验收报告](../../tests/ccnu-eduagenttrust-template/20260919-references/REPORT.md)；成员补全见[成员回填报告](../../tests/ccnu-eduagenttrust-template/20260919-members/REPORT.md)；此前字段与预算补全见[2026-09-18报告](../../tests/ccnu-eduagenttrust-template/20260918-fill/REPORT.md)；模板迁移及公共包回归历史见[前轮报告](../../tests/ccnu-eduagenttrust-template/20260912/REPORT.md)。基线比较使用官方 `compare --tex-file blank.tex`；正文使用文本、字体、坐标和逐页视觉检查；公共包回归按实际包引用覆盖全部5个现有直接消费者，在 `tests/` 副本中构建，保留其他项目已有成果。

```bash
cd tests/ccnu-eduagenttrust-template/20260919-references
python3 verify_references.py
```

空白表与官方页数、方向、栏目和表框一致；WPS原字体与共享字体仍有字形、字重和字距差异，严格像素比较不是完全相同。验收报告分别说明预期变化、残余差异和构建警告。

已按[2026年度正式指南](https://aielab.ccnu.edu.cn/info/1101/6491.htm)填入一般课题5万元、一年期安排，补回民族、邮编及现有成果，完成预算测算。具体起止年月随立项确定；七名研究生成员已按用户资料填入；按用户确认将行政职务填为“无”、申请日期填为2026年9月19日。用户同日确认合作人员尚未确定，保持公开资料和模拟环境先行的方案；教学复核与真实数据授权按研究阶段落实。成员相关在研项目未见于所给资料，仍需核实；签章办理及预算审核见[填写说明](docs/填写说明.md)。
