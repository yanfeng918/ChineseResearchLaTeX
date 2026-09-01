---
name: nsfc-full-pipeline
description: 当用户明确要求“跑 NSFC 标书全流程”“从头写完整标书”“继续/续跑标书写作流程”或“按 QC/模拟评审结果自动修改标书”时使用。适用于 ChineseResearchLaTeX 仓库内的国家自然科学基金面上、青年、地区项目，按 00–14 共 15 个阶段编排正文写作、检查、评审、定点修复与编译；使用可迁移断点实现可靠续跑，默认 draft-first：缺硬事实时以事实 ID 挖空并继续，仅在布局、项目类型或选题无法确定时阻塞。⚠️ 不适用：单章节写作、一次性只读质检、省级或地方科学基金项目。
metadata:
  author: Bensz Conan
  short-description: NSFC 正文 15 阶段编排、draft-first 与可靠断点续跑
  keywords:
    - nsfc-full-pipeline
    - NSFC 标书全流程
    - draft-first
    - 断点续跑
---

# NSFC 标书全流程

## 目标与边界

本技能编排 ChineseResearchLaTeX 中 NSFC 面上、青年和地区项目的正文流程。它覆盖选题、文献、科学问题、研究方案、正文、引用、篇幅、去 AI 味、QC、模拟评审、P0/P1 修复与编译。

“全流程”指 `main.tex` 引用的正文链路，不自动生成摘要、申请代码、预算说明、声明附件或配图。最终必须分别报告：

- `body_pipeline_ready`：正文 15 阶段是否完成；
- `submission_ready`：正文完成且摘要、申请代码、预算、声明和附件均已完成或明确不适用。

不得把前者表述成“整份申请书可以提交”。

正式交付写入项目自身的 `docs/`、`review/`、`extraTex/` 和 `main.pdf`。检索缓存、中间 JSON 与命令日志放入统一的 `.bensz-api/task-.../nsfc-full-pipeline/` 临时工作区。

## 必须遵守的规则

1. 先读项目级 `AGENTS.md`，不得用仓库根规则替代项目的篇幅与章节规则。
2. `main.tex` 中未注释的 `\input` / `\include` 是正文文件唯一真相来源；不得编辑孤儿文件、注释态章节或 `extraTex/@config.tex`。
3. 不改模板结构、公共样式、页眉、字体和章节标题；只修改项目正文、事实资料、过程文档与评审报告。
4. 不编造批准号、经费、论文、奖项、设备、团队、前期结果或声明。draft-first 只改变何时停，不降低事实标准。
5. 引用必须真实可核验；缺文献时继续检索或记录缺失主题，不得虚构 BibTeX。
6. `\NSFCBlankPara`、`待填写` 等是未写作占位；`【待补 ID：说明】` 是已写但待回填的硬事实缺口，两者不得混淆。
7. 所有阶段状态通过脚本原子更新，不凭文件存在或模型记忆宣告完成。

## 首轮读取

每次新跑或续跑都先读取：

- 项目 `AGENTS.md`、`README.md`、`main.tex`；
- `docs/workflow_status.yaml`（若存在）；
- `docs/00_项目基本信息.md`、`docs/00_项目事实库.md`（若存在）；
- 断点中声明的 `applicant_profile_file`；
- `references/myexample.bib`；
- `main.tex` 实际引用的正文文件；
- 与当前阶段有关的已有 `docs/`、`review/` 产物。

随后完整读取 [references/checkpoint-and-gap-policy.md](references/checkpoint-and-gap-policy.md)，并按当前阶段完整读取：

- stage 00–07：[references/stages-00-07.md](references/stages-00-07.md)
- stage 08–14：[references/stages-08-14.md](references/stages-08-14.md)

## 每次运行的固定入口

从仓库根目录执行，`<project-dir>` 替换为标书目录：

```bash
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> migrate --apply
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> reconcile --apply
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> next
```

不得跳过迁移与对账：旧断点需要补齐 schema，`in_progress` 需要按产物指纹恢复，`main.tex` 变化需要让 stage 00 失效，正文缺口需要从真实文件反向同步。

执行每个阶段前后分别运行：

```bash
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> begin --stage <stage-id>

# 完成该阶段的实际工作

python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> finish --stage <stage-id>
```

`finish` 未通过时修复产物或状态，不能手工把阶段改成 `completed`。

## 15 个阶段

| ID | 阶段 | 主要产物/动作 | 子技能 |
|---|---|---|---|
| 00 | 布局与项目类型解析 | `project.layout`、`grant_type`、正文角色映射、篇幅预算 | 本技能 |
| 01 | 选题与研究主题 | `docs/01_选题与研究主题.md` | `research-topic-extractor`、`research-guide-updater` |
| 02 | 文献调研 | `docs/02_文献调研/`、真实 BibTeX | `research-literature-review`、`research-guide-updater` |
| 03 | 科学问题与创新点 | `docs/03_科学问题与创新点.md` | `research-idea`、`research-guide-updater` |
| 04 | 研究方案与技术路线 | `docs/04_研究方案与技术路线.md` | `research-plan` |
| 05 | 第一部分正文 | stage 00 解析出的 `part_one` 文件 | 对应 NSFC writer、`research-plan` |
| 06 | 研究基础与工作条件 | stage 00 解析出的 `foundation` 文件 | `nsfc-research-foundation-writer` |
| 07 | 其他说明 | stage 00 解析出的 `statements` 文件与检查报告 | 本技能 |
| 08 | 引用一致性核查 | `review/引用一致性审核报告.md` | `nsfc-ref-alignment` |
| 09 | 篇幅对齐 | `review/篇幅控制报告.md` | `nsfc-length-aligner` |
| 10 | 去 AI 味 | `review/去AI味修改报告.md` | `nsfc-humanization` |
| 11 | QC | `review/质量控制报告.md` | `nsfc-qc` |
| 12 | 模拟专家评审 | `review/模拟专家评审_全稿.md` | `nsfc-reviewers` |
| 13 | P0/P1 定点修复 | 修复清单与 `review/P0P1定点修复报告.md` | 按问题回调相关技能 |
| 14 | 编译 | `main.pdf`、`review/编译检查报告.md` | 官方构建入口 |

按顺序推进，除非断点表明阶段已 `completed`、`drafted_with_gaps` 或 `skipped`。`drafted_with_gaps` 不重写；先继续后续阶段，事实补齐时再按 ID 定点回填。

## Draft-first 缺口处理

缺信息时先分类：

- 可推定项：给合理草稿值并标 `【暂定 …】`；不得伪装成用户确认值。
- 硬事实：只挖掉名词短语，写成 `\textbf{【待补 F-GEN-03：批准号与起止年份】}`；ID 必须来自申请人事实文件或项目事实库。

正文句子与论证链必须尽量写完整，不得用一个占位符代替整段。集中更新相应信息补充问卷，但继续推进；stage 05–07 由状态脚本根据真实标记置为 `drafted_with_gaps`。

只有以下情况暂停并向用户提一个合并后的问题：

- stage 00 无法确定正文落点、项目类型或篇幅口径；
- stage 01 无法确定研究主题，继续写会使整篇内容成为臆造；
- 路径越界、资料冲突或工具故障使当前阶段无法安全推进。

补事实后运行 `reconcile --apply`，按 ID 仅修改命中句；正文或 BibTeX 变化后重跑受影响的引用、篇幅、QC 或评审阶段。

## 文献与写作闸门

文献充分性按学科适配，不把 CS/AI 数量阈值强加给所有领域。通用要求是：关键论断有高质量、真实且语义匹配的来源，近年进展与奠基工作覆盖合理。CS/AI 默认量化参考见阶段文档。

stage 05 写作必须形成闭环：价值与必要性 → 现状与缺口 → 科学问题/假说 → 研究目标与内容 → 方案与可行性 → 创新与计划。stage 06 只使用可追溯事实；stage 07 对每项声明给真实肯定或否定句，未知事实挖空，不得整节留白。

## 检查、评审与修复

stage 08–12 依次完成引用、篇幅、人味、QC 与模拟评审。任何改写都必须逐字保护 `【待补 …】`、`【暂定 …】` 和引用命令。

stage 13 建立问题矩阵并分类：

- `auto_fix`：证据充分、范围明确，可直接定点修复；
- `needs_user_fact`：用既有事实 ID 挖空或保留，不停下重写整节；
- `defer_or_reject`：与资助额度、研究边界或用户目标冲突，记录理由。

优先修 P0/P1；每轮修复后只重跑受影响的 stage 08–12。若仍有可安全自动修复的 P0/P1，继续有限范围迭代；若剩余项需要用户事实或策略选择，记录后进入 stage 14，不假装修复完成。stage 13 不编译。

## 编译与最终判定

stage 14 使用官方入口：

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build \
  --project-dir <project-dir>
```

若从项目目录运行，则使用项目自带 wrapper：

```bash
python scripts/nsfc_build.py build --project-dir .
```

编译必须零错误；warning 要说明是已有还是新增。最终运行：

```bash
python skills/nsfc-full-pipeline/scripts/scan_gaps.py \
  --project-dir <project-dir> --json
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> reconcile --apply
python skills/nsfc-full-pipeline/scripts/pipeline_state.py \
  --project-dir <project-dir> readiness
```

最终汇报必须列出：完成阶段、正文改动、报告与 PDF 路径、编译结果、剩余硬事实 ID、暂定项数量、`body_pipeline_ready`、`submission_ready` 及尚缺的申请书组件。
