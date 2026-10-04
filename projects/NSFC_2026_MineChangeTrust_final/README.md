# 中南大学实验室开放基金申请书（2026 版）

根据本目录提供的官方 PDF 重建的可填写 LaTeX 模板。`blank.tex` 的空白输出为 13 页，保留封面、填报说明、简表、十四个栏目及签章位置。`main.tex` 装配 `extraTex/` 中的当前研究正文、7 幅原稿插图和现有参考文献，并已填入现有申请人资料、本人简历及研究摘要。回填依据和剩余字段见 [表格回填状态](docs/form-fill-status.md)，预算与审批按实际信息继续完善。

本申请书使用 `bensz-thesis` 的独立 `csu-open-fund-2026` 模板；`template.json` 中的 `build_profile=thesis` 决定构建类型。目录名中的 `NSFC_` 不改变这一选择。本项目不使用学位 `degree` 元数据。

研究设计已结合5万元申请额度与现有条件明确为24个月、18次必要完整训练及最多6次补充训练；拟研究期限为2027年1月至2028年12月，具体日期依批复执行，见 [起止时间依据](docs/project-period.md)。Ds分档、效应判据、随机种子和复核预算等取值见 [研究参数与工作量](docs/parameter-decisions.md)。分位数的实际界点由训练数据计算，历史预实验结果保持原样。

2026-09-21经3组独立模拟评审再次修订，正式稿保持33页：固定特征层与掩码投影，补充工作点敏感性分析，明确各比较的结论边界，优先保障强度对照，并追踪检测后残留错误的可复核性。新规则均为未来研究设计，原预实验数据完整保留；见 [评审与修改报告](../../tests/minechange-review-revise-20260921/comments-from-nsfc-reviewers.md)和 [本轮验收](../../tests/minechange-review-revise-20260921/REPORT.md)。此前NA、有效矿区及随机掩码规则的修订见 [前轮记录](../../tests/minechange-qc-fixes-20260921/REPORT.md)。2026-09-22按申请人要求删除天池英才不确定细项，补充经费办理说明并核对日期、学历、任职和邮箱，见 [提交事实核对表](docs/submission-facts.md)及 [最新验收](../../tests/minechange-submission-details-20260922/REPORT.md)。

## 打开与构建

在 VS Code 中打开 [NSFC_2026_MineChangeTrust_final.code-workspace](NSFC_2026_MineChangeTrust_final.code-workspace)，LaTeX Workshop 会通过项目 wrapper 调用官方构建器。

若打开的是整个仓库，根目录配置会将本项目交给 `thesis` wrapper。首次更新配置后，在命令面板执行 `Developer: Reload Window`，打开本项目 `main.tex` 再构建。若日志先报 `Profile 'csu-open-fund-2026' not found`，随后在中文标点或 `\cite` 附近累计到 `100 errors`，应检查是否仍在直接运行 `xelatex` 并加载旧安装包；正常的整仓库构建配方为 `repository project build (python)`。不要为此删除正文引用。

在完整仓库根目录执行：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_MineChangeTrust_final
```

仅打开本项目时执行：

```bash
python3 scripts/thesis_build.py
```

需要 XeLaTeX，以及包含 `csu-open-fund-2026` profile 的 `bensz-thesis` 和 `bensz-fonts`；正文参考文献还使用 `bensz-nsfc` 提供的 `gbt7714-nsfc.bst`。完整仓库中的官方入口直接使用本地包源码；单独复制项目时须先安装相应公共包。共享字体与 BST 不复制到项目目录。正文输出为 `main.pdf`，空白模板输出为 `blank.pdf`。中间文件与 SyncTeX 保存在 `.latex-cache/`。官方构建器每次清理并重建缓存，因此同一项目的两个入口应顺序构建。

生成用于官方模板对齐的空白版：

```bash
python3 scripts/thesis_build.py build --tex-file blank.tex
```

## 填写位置

| 内容 | 文件 |
|---|---|
| 正文引用的 BibTeX 数据 | [references/myexample.bib](references/myexample.bib) |
| 封面与简表的申请字段、勾选类型、研究期限 | [extraTex/metadata.tex](extraTex/metadata.tex) |
| 主要研究内容及意义（按官方要求限 300 字） | [extraTex/abstract.tex](extraTex/abstract.tex) |
| 一至三：立项依据、研究内容、研究方案 | `extraTex/justification.tex`、`content.tex`、`methods.tex` |
| 四至七：特色创新、执行计划、研究基础、预期成果 | `extraTex/innovation.tex`、`plan.tex`、`foundation.tex`、`outcomes.tex` |
| 八：经费预算 | [extraTex/budget.tex](extraTex/budget.tex) |
| 九：申请者及主要成员、简历 | `extraTex/members.tex`、`biographies.tex`、`biographies-details.tex` |
| 十：两名专家的推荐意见和信息 | `extraTex/recommendation-one.tex`、`recommendation-two.tex`、`recommenders.tex` |
| 十二至十四：单位补充意见、委员会及主任意见 | `extraTex/organization-opinion.tex`、`committee-opinion.tex`、`director-opinion.tex` |

正文引用使用 `\cite{bibkey}` 自动关联文献编号，PDF 中点击编号可跳至对应条目，文献中的 DOI/URL 也可点击访问；链接保持黑色且无边框。文献在立项依据末输出，BibTeX 数据保持在 `references/myexample.bib`。完整清空研究正文时可直接使用 `blank.tex`；若在 `main.tex` 中移除全部引用，也应移除其中的 `\bibliography` 调用。

申请人简历在原成员表内保留学历、工作经历和在研项目，下一页列六篇完整代表作及矿山课题分工。成果目录列出全部作者、年卷期及页码或文章号，题名可点击跳至 DOI；目录为五号字（10.5pt），与正文研究参考文献分开编排。题录、作者身份与未填奖励的依据见 [简历整理说明](docs/biography-sources.md)。

成员表已按申请人指定的参与者资料列入七名新疆大学研究生，连同负责人共八人，工作安排见 [成员与分工](docs/member-assignments.md)。研究生专业沿用当前成员表的“计算机技术”；按申请人要求，保留现有成员简历内容，不扩写逐人简历。学号、证件号码或私人联系方式不写入申请书。

参考文献复用仓库国自然模板的 `gbt7714-nsfc` 样式：顺序编码、作者姓氏及名字首字母、文献类型标识、年卷期页码和已有访问日期及 DOI/URL。文献正文按用户要求采用小五号字（9pt）、14bp 行距，左对齐与悬挂缩进，条目间不加额外空白；这些设置由 CSU 公共样式统一维护。题录仍以原 `.bib` 为准。

通讯地址由 `metadata.tex` 中同一字段供封面与简表使用；简表的窄地址格由 CSU 公共样式按 9bp 字号、11bp 行距换行，保留固定表框与溢出检查。

封面、简表、预算及推荐人字段的单行内容与对应标签共用基线；封面多行内容的末行对齐标签，简表两行地址保持整体居中。成员表各单行共用基线，两行专业等字段以两条基线的中点对齐；不因汉字、数字或邮箱字符形状不同而上下浮动。验收见 [填写位置对齐](../../tests/minechange-cell-alignment-20260920/REPORT.md)。

封面填写内容与固定标签统一为14.05bp，填写区宽338bp，保持原有中轴和基线；当前24字课题名称可完整单行显示。其他页面的字段和正文、参考文献字号沿用各自设置。验收见 [封面字号统一](../../tests/minechange-cover-font-20260922/REPORT.md)。

正文使用7幅矢量PDF：研究背景、总体框架、三条研究路线、预实验流程、预实验结果。2026-09-23按申请人要求，以 `nsfc-illustrated-pipeline` 中的可编辑PPT重建流程将前6幅位图重新绘制为原生文字、形状和连接线；正文引用 `figures/vector/` 下的新版PDF，同目录提供SVG，六页可编辑源为 [NSFC-Figures-vector.pptx](figures/NSFC-Figures-vector.pptx)。原始PDF保留在 `figures/` 便于对照。图7 `F15_F16_pilot_results.pdf` 已为真实数据绘制的矢量图，本次不改数据或文件。图注和 `fig:mct-*` 标签分别位于 `justification.tex`、`content.tex`、`methods.tex`、`foundation.tex`；图与图注仍在同一 `minipage` 中整块分页，前6幅保留原尺寸及顶部12mm裁剪。制作与导出说明见 [矢量图说明](docs/vector-figures.md)，本轮验收见 [矢量重绘验收](../../tests/minechange-vector-20260923/REPORT.md)，图7此前修复见 [间距验收](../../tests/minechange-figure7-spacing-20260920/REPORT.md)。

填写示例：

```latex
\CSUSetup{
  title={课题名称}, applicant={姓名}, organization={工作单位},
  research-type={basic}, organization-type={university}
}
\CSUPeriod{2027}{1}{2028}{12} % 拟申请的24个月期限；具体日期依批复执行
```

`research-type` 可填 `basic`（基础研究）、`applied`（应用研究）；`organization-type` 可填 `university`、`research`、`other`。留空表示未选择。预算 `\CSUBudgetRow{行号}{万元金额}{理由}` 的行号为 0–5，0 为合计；金额不自动求和。当前申请总额为 5.00 万元，简表与预算合计共用 `metadata.tex` 的 `funding` 字段；五项分配依次为0.00、0.00、1.40、1.80、1.80万元，“其它费用”列研究生助研劳务，按累计36人月×500元/人月测算；计算使用现有设备，不安排付费测试，详见 [预算说明](docs/budget-basis.md)。成员 `\CSUMember{行号}{姓名}{性别}{出生年月}{专业}{职称}{分工}` 支持 1–9 行，包含申请者。签章栏留作纸质签署。

封面项目编号由实验室填写。正式填写时请按原始填报说明复核字数、经费、期限和签署要求；模板不会代替申请人确认事实。

## 分页与版式

- 2026-09-22精简研究方法中的重复说明和图3图注，使图3接入第14页；保护下一小节首段，并将图5放在离线复核流程说明之后、补充检测器比较之前。正文与图片字号、实验参数和公式保持不变，正式稿仍33页。验收见 [研究方法分页调整](../../tests/minechange-methods-pagination-20260922/REPORT.md)。
- 一、二、三、六的研究正文按正常 LaTeX 规则自动续页，栏目标题仅在首页显示，续页保留版框，页码连续。
- 正文小标题使用 `\subsection{标题文字}`，由模板自动编号为 `1.1`、`1.2`、`2.1` 等；每个官方栏目重新计数，不在标题文字中手写编号。字号与正文一致并加粗。
- 四/五、七/八在短正文时保持官方合页结构；内容较长时按栏目顺序拆页，研究正文自动续页，标题同样只在各栏目首页显示，经费表另页排放。
- 研究栏目和拆分栏目均只对空内容保留占位；非空正文结束不追加空行，避免满页后出现空白续页。当前验收见 [修订记录](../../tests/minechange-qc-fixes-20260921/REPORT.md)，早期检查快照见 [检查报告](../../tests/minechange-final-check-20260920/REPORT.md)。
- 简表、预算、成员和意见栏保留官方固定空间。内容超高时报错，不缩小整页或裁切正文；这类长材料可在 `main.tex` 中另加附件页。
- 正文可使用段落、列表、公式和普通表格。合页栏目及固定字段中应直接插入 `\includegraphics`、`tabular` 等内容，需要题注可使用 `\captionof`；不要在这些盒子内放置 `figure` / `table` 浮动环境。
- 正文和标签均是原生文字，表格线为矢量。构建不读取参考 PDF，没有 PDF 直通或整页截图。
- 填报说明中的西文引号按原模板使用 Times New Roman；局部西文片段不触发中文标点字体切换，避免“项目编号”两侧引号挤压汉字。核验见 [引号排版修复](../../tests/minechange-instruction-quotes-20260920/REPORT.md)。

## 分层与验收

`main.tex` 负责当前栏目和参考文献装配，`extraTex/` 保存填写数据。`blank.tex` 调用相同的模板接口并传入空白内容，用于长期对齐验收。字体、坐标、表格、续页和溢出检查集中在 [`bthesis-style-csu-open-fund-2026.tex`](../../packages/bensz-thesis/styles/bthesis-style-csu-open-fund-2026.tex)，固定标签及线条位于同目录的 artwork 文件，模板身份在包级 profile 注册。

从仓库的测试子目录执行官方比对，例如在 `tests/minechange-template-20260907/` 中运行：

```bash
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py compare \
  --project-dir ../../projects/NSFC_2026_MineChangeTrust_final \
  --baseline-pdf '../../projects/NSFC_2026_MineChangeTrust_final/附件：2026年中南大学有色金属成矿预测教育部重点实验室开放基金申请书.pdf' \
  --tex-file blank.tex --dpi 144 --keep-rasters --output-dir compare-blank
```

验收记录见 [REPORT.md](../../tests/minechange-template-20260907/REPORT.md)。共享字体中的黑体、仿宋与官方 WPS 字体字形存在细微差异，不能宣称逐像素完全一致。模板保留官方页数、栏目顺序、字体层级和表格坐标。

图片遗漏修复及完整性核验见 [图片迁移验收](../../tests/minechange-figures-20260910/REPORT.md)，包括源文件校验、图号引用、构建记录及含图页面检查。

续页标题去重及包级回归见 [标题验收](../../tests/minechange-headings-20260910/REPORT.md)：七个研究栏目标题各显示一次，正文、图片与版框位置保持不变。

子标题编号及合页/拆页验证见 [子标题验收](../../tests/minechange-subheadings-20260910/REPORT.md)：全文 22 个二级标题按所属栏目自动编号。

个人资料填写与版框检查见 [表格回填验收](../../tests/minechange-personal-info-20260910/REPORT.md)：仅第 1、3、34 页发生变化，其余正文及图片页面与填写前逐像素一致。
