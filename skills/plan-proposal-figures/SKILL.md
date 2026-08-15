---
name: plan-proposal-figures
description: 分析科研或基金项目申报书 PDF，按三个可追溯步骤完成配图规划：先调用 Academic Paper Analyzer & Figure Planner 生成 Figure Plan，再独立审核、修订和复审，最后调用 classic Academic Figure Prompt 为全部审核通过且确需新绘制的图生成 figure spec 与 200–400 词英文 image prompt；全程不生成图像。用于“申报书需要哪些图”“先规划并审核配图”“为整份标书生成所有绘图提示词”等请求；不适用于 pastel/airy 风格、直接生图或只解读已有 Figure。
---

# 申报书配图规划与提示词

## 目标

接收一份申报书，严格按以下顺序交付三个阶段：

1. `Figure Plan`
2. `Figure Plan Review` 与审核后计划
3. 所有获批图项的 `Figure Spec Package`

只规划、审核并写 prompts。禁止调用任何生图后端，禁止创建 PNG、JPG、SVG 等最终图像。

## 依赖

从当前可用 Skill 目录解析并在对应阶段完整读取以下 Skill 及其要求的引用文件：

- `pdf`：读取或 OCR PDF；仅在输入为 PDF 时使用。
- `Academic Paper Analyzer & Figure Planner`：阶段一必须使用。
- `Academic Figure Prompt`：阶段三必须使用。

直接调用上述两个学术配图子 Skill，不调用会继续进入生图阶段的端到端配图 Orchestrator。若任一必需依赖不可用，指出缺失项并停止；不要凭记忆重写其输出契约。

## 输入契约

要求一份可读且未加密的申报书 PDF。用户给出的典型输入为：

```text
/absolute/path/to/proposal/main.pdf
```

按以下顺序处理输入：

1. 验证路径存在、是普通 `.pdf` 文件、可读且能够解密。不要修改源申报书。
2. 若用户未给路径，但当前目录只有一个明确的 `main.pdf`，可使用它，并显式说明该推断；否则只询问申报书 PDF 路径这一项。
3. 对 PDF 优先读取文本层并保留页码边界；文本层缺失或明显不完整时再 OCR，并标注 OCR 风险。
4. 提取标题、申报类型、篇幅/页数、章节结构、图题和已有插图引用。
5. 记录源文件绝对路径、SHA-256、页数、实际分析页、提取方式（`text / OCR / mixed`）和提取警告；不要复制不必要的大体积原文件。
6. 不联网补全申报书未提供的科学内容、结果或个人事实。

信息不足时继续产出保守的阶段性结果，把超出证据的内容标为 `推断` 或 `待确认`。路径无效、PDF 无法解密，或文本层与 OCR 都无法得到标题、研究目标、研究内容中的任何一项时停止。

## 证据规则

- 建立 `evidence_registry`；每条证据记录唯一 `evidence_id`、PDF 页码、章节、证据摘要和提取置信度。
- 为每个节点、边、公式、数值和拟渲染的 `exact_*` 标签记录 `evidence_ids`、`evidence_status: source-explicit | conservative-inference | pending-confirmation` 与 `research_state: proposed | expected | preliminary | established`。
- 不得把 `conservative-inference` 写成原文事实，也不得把拟开展或预期内容画成已验证结果。
- 不编造模块、因果关系、公式、维度、样本量、实验数值、对照组、年度结果或已有基础。
- 先列出现有图及其作用，再规划新增、替换或重绘项。能检查相关 PDF 页面时，使用临时页面栅格做视觉核对；只能读到图题时，把 `existing_asset_relation_confidence` 标为 `low`，不得断言不重复。
- 同一术语、研究内容编号、科学问题编号和指标名称在三个阶段保持一致。
- 本节证据禁令优先于依赖 Skill 中“推断维度”“补 supporting modules”等示例性启发式；缺证据时使用中性几何锚点或阻断图项，不补科学内容。

每份阶段产物只使用以下完整性块：

```yaml
completeness:
  analyzed_materials: []
  output_type: complete | partial | local | skeleton
  high_confidence_information: []
  pending_confirmation: []
  suggested_materials: []
```

## 工作区与交付

需要中间文件时，先读取仓库内 `skills/WORKSPACE.md`（若存在），严格按其中当前契约建立任务工作区：

```text
./.bensz-api/task-<yyyymmdd-hhmm>-<短标签>/
├── README.md
└── plan-proposal-figures/
    ├── input/
    ├── output/
    └── log/
```

创建工作区前，先告诉用户将调用本 Skill、PDF Skill 和两个学术配图子 Skill，以及本轮只生成计划、审核和 prompts。任务名必须含 `yyyymmdd-hhmm`；只在 `input/` 保存路径、哈希、依赖版本和参数快照，不复制原始申报书；草稿与验证日志分别进入 `output/`、`log/`。

正式交付物不放在隐藏工作区：优先写入用户指定目录；未指定时在申报书同级创建 `figure-planning/<yyyymmdd-hhmm>/`，写入 `01-figure-plan.md`、`02-figure-plan-review.md` 和 `03-figure-prompts.md`。目标已存在时不得静默覆盖，追加短后缀。若目标目录不可写，则以 `delivery_mode: inline` 在回复中按相同的三个一级标题完整交付。不要在仓库根目录散落中间文件。

默认连续执行三个阶段，并在回复中明确显示阶段边界。若用户明确要求“只做第一步”或“先停在 Figure Plan”，完成对应阶段后停止。续跑前必须同时匹配源 SHA-256、依赖版本和计划版本；任一不匹配时使受影响的下游阶段失效并重跑，不要复用陈旧产物。

## 阶段一：生成 Figure Plan

读取并遵循 `Academic Paper Analyzer & Figure Planner`，将申报书章节映射为适合基金评审的结构，而不是机械套用论文图数：

- 立项依据、研究现状与核心缺口
- 科学问题、科学假设与研究目标
- 研究内容及其依赖关系
- 总体框架、技术路线与关键机制
- 验证方案、指标、对照与可证伪条件
- 创新点、可行性、研究基础与年度计划

先建立 `section_status`，将每一类标为 `present`、`partial` 或 `absent`。再调用规划器生成建议，并根据申报书页数与正文密度控制图量；不要直接套用论文的 4–12 图经验值。每张图必须回答一个明确的评审问题，装饰性插图不进入计划。

为申报书增加 `figure_form`，再映射到提示词 Skill 支持的受控类型：

| `figure_form` | `figure_type` |
|---|---|
| conceptual framework / research-content map / technical route / study design / timeline | Overall Framework |
| mechanism / key method / subsystem | Module Detail 或 Network Architecture |
| design comparison / condition matrix | Comparison / Ablation |
| evidence chart / measured behavior | Data Behavior |

映射不成立时标记 `unsupported`，不要把教育、社会科学或临床研究设计硬改写成神经网络架构。

使用稳定 ID `F1`、`F2`……，按建议在申报书中的出现顺序编号。把初稿标为 `plan_version: v1`，记录 `source_sha256` 与依赖版本。每个条目至少包含：

| 字段 | 要求 |
|---|---|
| `figure_id` | 稳定 ID |
| `proposed_title` | 中文暂定图名 |
| `target_section` | 建议放置章节与位置 |
| `reviewer_question` | 该图帮助评审回答的唯一问题 |
| `figure_type` | 使用规划器控制类型 |
| `figure_form` | 申报书语义形式及其类型映射 |
| `priority` | `must` / `strong` / `nice` |
| `source_evidence` | 可解析的 `evidence_ids` |
| `core_message` | 一句话结论，不写无法证实的结果 |
| `must_show` | 必须元素列表；逐项记录角色、证据 ID/状态和研究状态 |
| `existing_asset_relation` | `new` / `replace` / `redraw` / `reuse` |
| `proposed_render_action` | `draw_new` / `reuse_existing` / `no_figure` |
| `data_requirement` | 所需数据及 `available / partial / absent` |
| `aspect_ratio` | `16:9` / `3:2` / `4:3` / `1:1` |
| `style_family` | `classic_academic`；其他风格标为不支持 |
| `unknowns` | `待确认` 项；无则写 `none` |

在计划末尾给出：

- 申报书概览与贡献/科学问题摘要
- `domain`、`venue: None` 或申报类型、palette/style family hint，以及可用时的 `module_count_framework`
- 完整性块
- 分章节的图数与作用
- `must / strong / nice` 排序
- 现有图处置清单
- 总图数、预计页面成本和可删减顺序

保存并展示 `01-figure-plan.md` 后再进入阶段二。此阶段不得生成 prompts。

## 阶段二：审核并修订 Figure Plan

以“挑剔的基金评审专家 + 学术图编辑”身份重新读取原始申报书证据。不要把阶段一的理由本身当作证据。若可使用子代理且材料不离开本地环境，优先让一个未参与规划的新子代理执行首轮审核，再由主代理裁决；否则进行一次隔离的第二遍审核。

逐项检查以下质量闸门：

| 维度 | 权重 | 通过标准 |
|---|---:|---|
| 证据忠实 | 25 | 每个科学节点、边、标签、公式和数值可回溯；研究状态正确 |
| 评审价值 | 10 | 每张图回答一个重要评审问题，而非复述正文 |
| 叙事覆盖 | 15 | 科学问题 → 研究内容 → 方法 → 验证形成闭环 |
| 非重复性 | 10 | 图与图、图与已有资产之间没有同义重复 |
| 逻辑一致 | 10 | 编号、术语、箭头方向、输入输出和因果关系一致 |
| 图形适配 | 10 | 内容适合画图；更适合表格或文字的条目已剔除 |
| 可读与篇幅 | 10 | 面板、标签和公式不过载，页面成本与优先级匹配 |
| Prompt 就绪 | 5 | 类型、主题、布局、可见标签和宽高比足够明确 |
| 跨图一致 | 5 | 编号、语义颜色和视觉层级能跨图复用 |

每项无问题得满分；存在未解决 blocker 时该项记 0 并判失败，存在未解决 major 时该项最高为权重的 60%，每个未解决 minor 扣该项权重的 10%。总分达到 85/100、证据忠实达到 23/25、其他每项至少达到权重的 70%，且无未解决 blocker/major，才可判为 `pass`；自动修订并复审后达到同一标准则判为 `pass_with_revisions`。记录 `score_before` 与 `score_after`。可绘制集合为空时不得为过闸而凑图，只需给出有证据支持的“无需新增绘图”结论。

对任意两张图分别计算规范化 `evidence_ids` 集合和 `must_show` 标签集合的 Jaccard 相似度。同一章节、同一图型且任一相似度 ≥ 0.6 时标为候选重复；核心信息相同且两种相似度均 ≥ 0.6 时必须合并或删除。允许“总体框架 + 局部放大”共存，但局部图不得复刻完整总流程。

将问题分为：

- `blocker`：无证据、虚构结果、核心关系不明或无法确定图的主题。
- `major`：关键贡献漏画、明显重复、错误图型、逻辑断裂或严重过载。
- `minor`：标题、顺序、宽高比、标签密度或局部样式可优化。

输出以下内容：

1. 总体结论：`pass`、`pass_with_revisions`、`partial` 或 `replan_required`。
2. 审核矩阵：维度、结论、证据、受影响图项、修改动作。
3. 覆盖矩阵：申报书关键科学问题/研究内容/验证项 → 图 ID；允许写“正文表达更合适”。
4. 问题清单与严重度。
5. 修订日志：新增、合并、删除、降级、改型、改位置和改宽高比。
6. 完整的 `Audited Figure Plan`，标为 `plan_version: reviewed-v2`。每图强制包含 `decision: keep | merge | delete | blocked`、`merged_into`（适用时）、`render_action: draw_new | reuse_existing | no_figure`、`prompt_eligible: true | false`、`blockers`、`unresolved_majors` 和审核后的全部证据字段。

只有同时满足“无 blocker、无 unresolved major、所需数据齐备、classic 风格受支持”的图才可设 `prompt_eligible: true`。直接应用有充分证据的修订，然后真正复审。最多执行初轮审核加两轮“修订 → 复审”（共三次审核）；仍有 blocker 或 major 时把相关图标为 `decision: blocked`，列出所需材料且不得用想象补齐。若其他图合格，总体结论为 `partial`；若无合格图，仍进入阶段三生成空 manifest 和阻断原因。

保存并展示 `02-figure-plan-review.md`。阶段三只用 `Audited Figure Plan` 决定图项集合，但必须按其中锚点回读原 PDF 核验图内文字和科学关系；不得从已被否决的旧条目恢复内容。

## 阶段三：为所有获批图项生成 prompts

审核后图项的唯一选择式为：

```text
decision = keep
AND render_action = draw_new
AND prompt_eligible = true
AND blockers = []
AND unresolved_majors = []
```

对选择集中的每一项按证据锚点回读原 PDF，再分别读取并严格执行 `Academic Figure Prompt`。框架、架构、模块和比较图执行 Steps 1–5，输出 JSON spec + image prompt；纯数据图按其 Step 6 输出 text spec，其中 200–400 词英文 image prompt 本身就是 spec。不得只给一句简略提示词。

在批量生成前建立一次跨图视觉契约：

- 固定申报书术语与缩写表。
- 固定输入、核心方法、监督/约束、输出等语义角色的颜色映射。
- 固定 `style_family: classic_academic`，与 `Academic Figure Prompt` 的能力边界一致。
- 保持图号、研究内容编号、字体层级、箭头语义和状态标记一致。
- 先生成一个全局 Palette Decision 和语义颜色绑定，再原样传给每张图；每张图最多使用该 palette 的 3 个色相。

本 Skill 为 classic-only。若用户明确要求 pastel/airy，在阶段二后标记 `STYLE_FAMILY_MISMATCH` 并停止阶段三；不要强行套用 classic，也不要擅自调用其他提示词 Skill。

每个图项按以下顺序输出：

1. `figure_id`、中文图名、图类型、目标章节和证据锚点。
2. `spec_format: json | text`；JSON spec 包含全部 `exact_*` 文字锁、`aspect_ratio`、物理尺寸与字体、布局块、配色、caption reserve 和负面渲染规则，text spec 遵循纯数据图 fallback。
3. 200–400 词英文 image prompt，完整覆盖八槽结构并以宽高比结尾；`spec_format: text` 时本项即为 text spec，不再伪造 JSON。
4. `prompt_word_count`、palette 名称、使用的 hex 及其决策分支。
5. `caption_reserve`：不应渲染在图内的公式、参数、解释和待确认信息。
6. 完整性块与 `prompt_status: ready | blocked`。

对曲线、柱高、热图、散点位置或显著性等几何形态依赖数值的数据图，只有申报书给出可回溯的真实数据时才生成 prompt；数据缺失即标为 `blocked`。待确认内容只允许进入 `caption_reserve`，不得作为可执行 prompt 的图内占位，并加入 `Do not infer or render missing values`。

若阶段三发现新的证据、数据、风格或可执行性问题，先回退阶段二，更新 `reviewed-v2` 的决定与 `prompt_eligible`，再重算选择集；不得在阶段三单方面改变集合。选择集为空时仍生成 `03-figure-prompts.md`，写入空 manifest、阻断原因和 `image_backend_calls: 0`。

中文申报书默认保留中文 `exact_*` 可见标签；英文 image prompt 逐字锁定这些标签，除非用户明确要求翻译图内文字。

逐图完成以下终检，失败则先修订再交付：

- `spec_format: json` 时 JSON 语法有效，所有可见文字只出现在 `exact_*` 字段。
- `spec_format: text` 仅用于提示词 Skill 允许的纯数据图 fallback。
- 宽高比与审核后计划一致。
- 文本预算、物理尺寸、字体和描边层级满足提示词 Skill 的要求。
- 每个主要模块都有视觉锚点。
- 英文 prompt 为 200–400 词并包含八槽结构。
- 包含 `NO emojis, NO lock/fire/lightning icons, NO 3D rendering` 等负面约束。
- 未重新引入阶段二删除的图项或未证实内容。
- 未推断维度、公式、曲线、数值、科学模块或因果边。
- prompt 集合与上述选择式得到的图项集合完全一致。

将跨图视觉契约、逐图 packages、未生成 prompt 的图项及理由写入 `03-figure-prompts.md`。在文件末尾附 manifest：`figure_id / decision / render_action / prompt_eligible / prompt_status / spec_format / JSON_valid / word_count / style_family`，并验证选择集与 prompt 集合的双向差集为空。记录 `image_backend_calls: 0`。

## 最终停止条件

在以下条件全部满足后停止：

- 三个阶段按顺序完成，或按用户指定阶段停止。
- Figure Plan 的问题已审核并形成可追溯修订。
- 每个审核通过且需要绘制的图都有 Figure Spec Package。
- 每份交付包含完整性块：已分析材料、输出类型、高置信信息、待确认信息、建议补充材料。
- 没有调用图像生成工具，也没有生成最终图片；OCR 或视觉核对产生的临时页栅格不属于生图交付，验证后不交付。

绝不调用 `image_gen`、GPT Image、Gemini/NanoBanana 图像 API、Sensenova、Midjourney 或任何生图脚本；“测试生图”同样禁止。

最终回复只汇报本次实际生成的产物路径（内联时写 `delivery_mode: inline`）、v1 图数、合并/删除/阻塞数量、审核结论、`ready / blocked` 计数和关键待确认项，并明确写出“本次未调用任何图像生成后端”。不要在本 Skill 内继续询问是否开始生图。
