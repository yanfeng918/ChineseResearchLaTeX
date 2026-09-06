# nsfc-illustrated-pipeline — NSFC 图文全流程

面向使用者的指南。版本 **v0.1.0**，以 [config.yaml](config.yaml) 为准；执行规范见 [SKILL.md](SKILL.md)。

这个技能把文字写作、核查和绘图接成一个任务：文字稿编译后继续规划配图、统一配色、逐个调用 `$imagegen`，随后制作可编辑 PPT、导出各图 PDF、插入正文并检查最终版面。

## 快速开始

在 ChineseResearchLaTeX 仓库中打开项目，使用：

```text
请使用 nsfc-illustrated-pipeline 完成 NSFC 标书图文全流程。
输入：projects/NSFC_Young，以及项目中的研究资料和绘图提示词.md。
输出：完整正文、配图、可编辑 PPT、逐图 PDF 和插图后的 main.pdf。
```

文字已经用原版写完时：

```text
使用 nsfc-illustrated-pipeline 继续 projects/我的NSFC项目。
导入原有有效文字进度，完成绘图和正文插入；每个 prompt 单独调用一次 imagegen 生成一张图。
```

新技能名称为 **`nsfc-illustrated-pipeline`**，原来的 `nsfc-full-pipeline` 仍保留。如果当前会话尚未发现新名称，可以直接让 AI 读取仓库中的 `skills/nsfc-illustrated-pipeline/SKILL.md`，或重新打开会话后使用项目入口；无需复制到用户主目录。

## 执行过程

| 部分 | 行为 |
|---|---|
| 文字阶段 00–14 | 布局、选题、文献、研究方案、正文、检查、评审、修复和文字稿编译 |
| 配图阶段 15–17 | Figure Plan、全篇配色、逐图 prompt；按顺序一 prompt 一次 imagegen 调用、一张图 |
| 图件阶段 18–20 | PNG 重建成对象级可编辑 PPT，导出单页 PDF，自动插入图题、编号和正文引用 |
| 验收阶段 21–22 | 查看插图页，复核中文、图文一致性、页数及相关 QC，验收最终 PDF |

三条研究路线默认至少五张核心图：背景、总体框架、三条路线各一张。可增加有解释价值的其他图；实际数量依据正文证据和项目篇幅规则确定。单图失败最多先纠错两轮，失败记录保留，其他独立图继续，整套图件不会被错误标为完成。

## 所需环境

- 完整仓库中的原版文字技能、Python 与官方 NSFC 构建链。
- Figure Planner、Color Expert、Academic Figure Prompt、`image-to-editable-ppt`。
- 宿主 `$imagegen` 及内置绘图工具；默认不需要 API Key，也不会自动切到外部服务。
- `editppt`、LibreOffice/soffice、中文字体，以及 PyYAML、Pillow、PyMuPDF。
- 多页 PPT 重建所需的宿主子代理能力，由转换技能负责页级任务。

工具缺失会在依赖检查中报告。内置绘图不可用时，只有你明确选择 CLI/API 回退才执行该路径。脚本负责状态和文件校验，生图、正文写作、科学与视觉检查由宿主 AI 实际完成。

## 输出与续跑

| 文件 | 内容 |
|---|---|
| `docs/illustrated_workflow_status.yaml` | 新技能独立断点 |
| `docs/figure_source/main.text.pdf` | 配图使用的文字稿基线 |
| `docs/Figure_Plan.md`、`Figure_Palette.md` | 规划和全篇配色 |
| `docs/figure_manifest.json`、`figure_specs/` | 图件落点、逐图规范和 prompt |
| `figures/*.png`、`NSFC-Figures.pptx`、`*.pdf` | 生成图、可编辑 PPT 和逐图 PDF |
| `docs/figure_insertion.md`、`review/` | 插图对应关系和验收报告 |
| `main.pdf` | 插图后的正文 |

新技能只读导入旧 `docs/workflow_status.yaml`，不会修改原版断点。旧阶段必须有有效产物与匹配指纹才能复用；旧记录不完整时要求定点复核。修改 prompt 只使关联图片失效；修改 PPT 会重新验收和导出 PDF，无需重绘 PNG。重复插入会更新原区块，不重复添加图片。

目前 PDF 导出按整本 PPT 进行，因此改一页后会重新导出图件 PDF，但不会重新生成其余 PNG 或重建其余 PPT 页。

## 常见问题

**事实没补齐能继续吗？** 合法待补 ID 可留在正文，背景和已确定路线继续绘制；不会编造实验结果。图内缺失事实也会登记，最终提交状态仍为未就绪。

**PPT 是把 PNG 填进幻灯片吗？** 要重建可编辑文字与主要结构，整页截图或截图叠文字不能通过验收。照片等独立素材可以保留位图。

**完成后能直接提交申请吗？** 图文完成与提交是不同状态。摘要、申请代码、预算、声明和附件仍需要完成或明确不适用；报告会分别给出四级就绪度。

**验证到了什么程度？** 技能入口、状态脚本及隔离回归可本地验证；真实生图和 editppt 页级重建依赖当前宿主与运行环境。测试夹具不作为真实生图或科研内容验收证据。

## 脚本诊断

普通使用优先给出上面的任务提示词。需要查看进度时，从仓库路径调用：

```bash
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目目录> migrate --apply
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目目录> reconcile --apply
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目目录> next
python3 skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py --project-dir <项目目录> readiness
```

详细命令、清单和证据格式见 [状态与产物契约](references/state-and-artifacts.md)。仅运行这些状态命令不会自动产生模型图像；主编排器须按 SKILL 执行实际工作。
