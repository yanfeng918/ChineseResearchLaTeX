---
name: nsfc-illustrated-pipeline
description: 当用户要求完成 NSFC 图文全流程、写完标书后自动绘图并插入正文，或继续第二版配图流水线时使用。串联正文写作与核查、逐个 imagegen 生图、可编辑 PPT、逐图 PDF、正文插入和最终验收；支持导入旧 nsfc-full-pipeline 文字进度。不适用于仅写单章、仅画一张图或省级基金。
metadata:
  short-description: NSFC 正文、逐张生图、可编辑 PPT 与插图 PDF 的 23 阶段流程
---

# NSFC 图文全流程

本技能独立于 `nsfc-full-pipeline`。在同一任务中完成正文与图件；Figure Plan、提示词、PNG、PPT 都是中间交接点，主编排器收到有效产物后继续，不把子技能的停止条件当作整项任务结束。

## 入口与范围

先读目标标书的 `AGENTS.md`、`README.md`、`main.tex`、活动正文、BibTeX、事实库、申请人事实文件和已有 `docs/`、`review/`。适用 NSFC 面上、青年、地区项目及其派生目录；用户明确仅写文字时使用原版，不自行扩展到图文流程。

读取 [文字阶段衔接规则](references/text-stages.md)，依据当前阶段再读其中链接的原版章节细则。复用文字写作、事实和评审标准，**本技能的范围、状态入口、绘图和结束规则优先**。不执行原版主入口，不让原版写 `docs/workflow_status.yaml`。

每次新跑或续跑按顺序执行（以下从仓库根写路径；实际验证必须在 `tests/` 子目录）：

```bash
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目> migrate --apply
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目> reconcile --apply
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目> next
```

新断点是 `docs/illustrated_workflow_status.yaml`。首次迁移只读导入原版状态；旧记录指纹不符时定点复核，不按文件存在猜测完成。后续唯一写入者为本技能的主编排器；页级子代理不写主断点或正文。

## 固定执行循环

对 `next` 返回的阶段运行 `begin --stage <完整ID>`，完成实际工作，再运行 `finish --stage <完整ID>`。失败运行 `fail --stage <完整ID> --reason <原因>`，诊断后续跑。所有命令均加 `--project-dir <项目>`，完整接口见 [状态与产物契约](references/state-and-artifacts.md)。

`finish` 失败不能手改状态为完成。`in_progress` 中断后检查调用和产物事实，显式续作或 `finish`，不会仅凭非空文件自动跳过。正文允许合法事实 ID 缺口继续；未写作占位、非法 ID 与布局错误必须修复。无硬事实时可继续画不依赖该事实的背景和流程图。

| ID | 阶段与调用 | 交付/验证 |
|---|---|---|
| 00_layout_resolution | 解析项目类型、正文角色、篇幅及依赖 | 用 `project --from-json` 登记实际布局 |
| 01_topic_extraction | research-topic-extractor；必要时更新项目指南 | 选题与主题 |
| 02_literature_review | research-literature-review | 文献调研、真实 BibTeX |
| 03_scientific_questions | research-idea | 科学问题、假说与创新 |
| 04_research_plan | research-plan | 研究方案与路线 |
| 05_part_one_writing | NSFC 立项依据、研究内容 writer | 活动正文第一部分 |
| 06_research_foundation | nsfc-research-foundation-writer | 可追溯研究基础与条件 |
| 07_other_statements | 本技能依据真实事实填写 | 启用声明与检查报告 |
| 08_reference_alignment | nsfc-ref-alignment | 引用核查 |
| 09_length_control | nsfc-length-aligner | 文字篇幅，预留配图空间 |
| 10_humanization | nsfc-humanization | 去 AI 味，保护事实与标记 |
| 11_qc | nsfc-qc | 质量检查 |
| 12_simulated_review | nsfc-reviewers | 按真实项目类型评审 |
| 13_targeted_repair | 按问题调用相应 writer/检查技能 | P0/P1 定点修复 |
| 14_compile | 本技能 `build --phase text` 调官方入口 | 文字 PDF 基线与编译报告 |
| 15_figure_plan | Academic Paper Analyzer & Figure Planner | Figure Plan、图件清单 |
| 16_figure_prompts | Academic Figure Color Expert → Academic Figure Prompt | 全篇配色、每图 JSON 与 prompt |
| 17_imagegen | **逐个 `$imagegen`，每个 prompt 单独生成一张图** | 串行调用、检查、PNG 与登记 |
| 18_editable_ppt | image-to-editable-ppt | 对象级可编辑 PPT、转换验收 |
| 19_figure_pdf | `export-pdf` | PPT 导出并拆成逐图 PDF |
| 20_insert_figures | `insert --apply`，补插图映射报告 | 正文受管插图、图题、引用 |
| 21_joint_review | 构建、查看插图页、篇幅与相关 QC | 图文检查报告及绑定当前 PDF 的证据 |
| 22_final_compile | 检查当前构建，有变化才再构建 | 最终 `main.pdf` 与编译检查报告 |

每次 `finish` 后继续下一阶段，直至 22 验收完成、用户明确停止，或遇到只有用户/外部状态能解决的阻塞。stage 14 成功后自动进入 15；不以要求无事实缺口的 `body_pipeline_ready` 阻止绘图。

## 配图规则与依赖

读取 [绘图至插入流程](references/figure-stages.md)。绘图规范按本次指令、已指定文件、项目内 `绘图提示词.md`、仓库根同名文件、本技能默认规则的顺序决定；选定外部规则文件后用 `drawing-rules --file <绝对路径>` 登记。

默认核心图：研究背景、总体研究框架、每条真实研究路线各一张图。三条路线对应至少五张核心图。积极规划其他有解释价值的图，在证据和项目页数允许时纳入；不为凑图数创造研究内容。清单分别记录入选和未入选理由，核心图不得静默删除。

stage 00 提前检查以下依赖，缺项集中说明，先完成不受影响的工作：

- 仓库内 `nsfc-full-pipeline` 及其调用的文字技能；脚本复用相邻目录的确定性逻辑。
- 当前宿主能读取的 Figure Planner、Color Expert、Academic Figure Prompt、`image-to-editable-ppt`。
- `$imagegen` 技能及内置 `image_gen` 工具；按宿主发现机制加载，不写死用户目录，不复制系统技能源码。
- `editppt` 与其运行环境、LibreOffice/soffice、中文字体、官方 NSFC 构建链；检查脚本需要 PyYAML、Pillow、PyMuPDF。

## 生图不可省略的约束

按图 ID 顺序读取每图的 JSON 和独立 prompt，逐个调用 `$imagegen` 的内置工具，**一 prompt、一次调用、一张图**。当前图检查并落盘或明确记录失败后再处理下一图；不并发生图，不把多图合成拼图后裁切，不用一个 prompt 的多变体代替不同图件。

实际调用前 `image-start`，调用后实际查看中文、箭头方向、层级、裁切与原文一致性，再复制选定 PNG 到项目 `figures/`，用 `image-record` 登记真实调用标识与检查证据。脚本不会替宿主调用图像模型，也不能证明虚构的调用标识；必须使用本次实际调用记录。

每图默认初绘后最多两轮纠错。失败先诊断，使用 `image-fail` 结束当前尝试；同根因重复失败要先解决根因。仅在根因已修复且需要额外尝试时用 `image-reset --reason` 保留历史后重置。仍失败的图不能计为完成，可以继续后续独立图。正在运行的调用不能因耗时较长就假定失败。

内置模式不要求 API Key；不可用时记录具体问题，只有用户明确选择 CLI/API 回退才执行 `$imagegen` 的回退规范。禁止因配置了第三方服务就自动切换。已有文件默认保留，修订 PNG 在清单中使用带版本的新路径。

## 图文真实性与保护范围

只写活动正文、项目图件和本技能过程材料；不改模板结构、标题、页眉、公共样式或 `extraTex/@config.tex`。默认保留正文的事实 ID、暂定项和引用命令。引用真实可核验，团队、经费、设备和前期结果必须来自事实库。

研究假说、拟开展流程可以画示意图；不得生成假实验照片、假指标、显著性或前期结果。真实数据图用可追溯的数据及绘图代码制作；若与指定 imagegen 路径不兼容，明确该图的科学绘图来源，不能伪造 imagegen 调用登记。此版自动图件登记针对示意 PNG；数据图作为已有科研资产保持原有引用，不纳入伪造生图流水线。

正文插入统一由脚本维护 `% NSFC-ILLUSTRATED BEGIN/END Fxx` 区块（包括引图句、caption、label），不要把正文论证移进区块。脚本把这些块与文字指纹分开，避免纯插图导致文字基线反复重建；原文科学内容变化仍触发文字检查及相关图件复核。

## 最终交付

stage 21 调 `build --phase final`，实际查看最终 PDF 的插图页面，完成图文、篇幅、中文和必要的引用/QC 复核。stage 22 必须对应当前输入；再次改图或正文后先重编译并更新相关验收，不能使用旧 PDF 的报告。

最后运行 `reconcile --apply`、`scan`、`readiness`，汇报：

- 23 阶段的进度与失败原因；主要正文与报告路径。
- Figure Plan、配色、逐图 prompt、PNG、可编辑 PPT、逐图 PDF、最终 `main.pdf`。
- 入选、生成、导出、插入的图件数量，PPT 页数及逐图状态。
- 编译错误与已有/新增 warning，硬事实 ID、图内缺口和暂定项数量。
- `body_pipeline_ready`、`figures_ready`、`illustrated_body_ready`、`submission_ready`。

`submission_ready` 还要求摘要、申请代码、预算、声明和附件都已完成或明确不适用。本技能不自动撰写这些独立组件，不把图文完成说成整份申请书可以提交。
