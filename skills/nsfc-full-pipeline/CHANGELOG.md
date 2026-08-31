# Changelog — nsfc-full-pipeline

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [0.3.0] - 2026-08-31

引入 draft-first 缺口策略：缺事实不再阻塞写作，改为按事实 ID 挖空占位并继续，补齐后定点回填。

### Added（新增）

- **`SKILL.md` 新增 `Gap Policy (Draft-First)` 小节**，`config.yaml` 新增 `gap_policy` 节。默认 `run.fill_policy: draft_first`；旧的"缺信息即停"行为保留为 `blocking`，需要时显式设置。
- **两类缺口分离**。可推定项（年度计划月份切分、预期成果数量口径、实验规模、指标阈值、baseline 选择）给合理草稿值并标 `【暂定 …】`，正文完整、不阻塞提交；硬事实（项目批准号、经费额度、已发论文、获奖、平台型号与保障年限、团队成员、国基完成情况、各类声明）只把事实名词挖空为 `【待补 ID：说明】`，绝不填入看起来像真的的值。这条区分是本次改动的安全底线：draft-first 只改变"何时停"，不改变"是否可以编造"。
- **占位标记复用现有事实 ID 体系**（共用层 `F-GEN-*`、项目层专属编号），不另立第三份清单；ID 未登记在事实库时须先建行再引用。标记使用普通 `\textbf{}` 而非新宏，以保证在 Overleaf、独立项目 zip 与任意已装 `bensz-nsfc` 版本下均可编译，且在 PDF 中肉眼可见。
- **新增 `scripts/scan_gaps.py`**：扫描 `extraTex/*.tex` 产出「事实 ID → 出现位置」反向索引，供回填回路定位。除标准库外无依赖，正确跳过 LaTeX 行注释。同时检出两类结构问题——ID 未登记在事实库、整段只有一个占位（后者不是草稿，是伪装成进度的停顿）。支持 `--id` 过滤与 `--json` 输出；有结构问题时返回码为 1，可用作闸门。
- **断点新增 `drafted_with_gaps` 状态与 stage 级 `gaps` 字段**。该状态续跑时不重跑，`gaps` 清空后才可转 `completed`；`blockers` 回归其本义，只用于硬阻塞。
- `evals/evals.json` 由 17 条扩充到 21 条：新增缺事实时挖空续写、有待补即不得声称可提交、按 ID 回填只改局部、缺口未清空时篇幅结论只能暂定四条用例。

### Changed（变更）

- **阻塞点从"写作时"移到"提交前"**。硬阻塞收敛为两处：stage 00 落点/项目类型解析失败（不知道往哪写），stage 01 选题未定（写什么都是编造）。研究基础、工作条件、承担项目、各类声明不再阻塞——它们本就是填空题。相应地，`Stop Conditions` 重写，`Core Principles` 中"缺信息则出问卷并置 need_user_input"改为"默认挖空续写"。
- **阶段 06/07 由停改为挖空续写**；问卷仍然生成，但作为集中补充入口而非阻塞信号。阶段 13 的 `needs_user_fact` 项现在照常应用修复的其余部分，只留事实本身为空。
- **阶段 14 允许带缺口编译**，但编译报告须写明 `【待补 …】` / `【暂定 …】` 数量；`Final Deliverables` 新增未清缺口清单与可提交判定。
- **`Resume Behavior` 补充回填回路**：用户表示已补充事实时，走按 ID 定点回填而非跳到下一个未完成阶段；含 `【待补 …】` 的文件视为已起草，不得推倒重写。
- 下游 skill 加护栏：`nsfc-humanization` 与 `nsfc-length-aligner` 将两类标记纳入逐字保护（压缩时删掉一个 `【待补 …】` 等于让待补事实静默进入投稿稿）；`nsfc-qc` 将缺口单列一类、不计入 P0/P1，但须统计数量并给出可提交判定，真正的未写作占位（`\NSFCBlankPara`、`待填写`）仍按 P0 处理。
- **篇幅结论在缺口清空前一律标注为暂定**。挖空稿偏短且引用偏少，补齐后通常多占 1–2 页；不加这条会陷入"压缩 → 补事实 → 又超 → 再压缩"的来回。`SKILL.md` 阶段 09、`nsfc-length-aligner` 与 `config.yaml` 三处同步固化。

### Verified（验证）

- `scan_gaps.py` 在 `tests/gap-policy-smoke/` 下针对三种情形实测通过：正常名词短语挖空、整段只有占位（正确报错）、ID 未登记（正确报错）；注释行中的标记未被误计。
- 含标记的项目经 `scripts/nsfc_build.py build` 编译无错误，`pdftotext` 确认 `【待补 …】` 与 `【暂定 …】` 均在 PDF 中正常渲染可见。

### Known Issues（已知问题）

- `SKILL.md` 行数继续增长，距 ≤500 行规范更远；缺口策略与阶段细则均待外移到 `references/` 后统一收敛。
- `scan_gaps.py` 仅扫描 `extraTex/*.tex`，未覆盖 `references/*.tex` 与项目自定义正文目录；当前模板下够用。
- 事实 ID 的识别采用通用形态匹配（`F-GEN-03` 这类大写短横格式），事实库中若出现同形态的非 ID 文本会被误纳入已知集合，方向为放宽而非误报。

## [0.2.0] - 2026-08-31

一次完整审核后的修复。所有声明均已对当前仓库真实状态复核。

### Fixed（修复）

- **样例项目 `NSFC_2026_Education` 已不存在**：该项目在 commit `9f46d09`（Remove outdated NSFC project files）中被删除，但 `SKILL.md` 的布局校验表、`config.yaml` 的 `layout.known.five-part.example_projects` 与 `README.md` 仍把它当作 five-part 样例；`README.md` 的快速开始命令更是直接让用户去处理这个不存在的目录。现全部改为真实存在的 `NSFC_Local` / `NSFC_Local_Clean`。
- **`nsfc-proposal-figure-pipeline` 不存在**：`config.yaml` 的 `not_covered` 与 `README.md` 让用户"单独调用"该 skill，但仓库 `skills/`、`~/.claude/skills/`、`~/.codex/skills/` 三处均无此技能，eval 12 还把这个查不到的名字写成了验收标准。现改为：配图不对应任何可调用 skill，由用户自行完成，本编排器不代为规划、不排进阶段、不擅自插图。
- **`project.type` / `grant_type` 声称由 stage 00 解析，但 stage 00 从无此步骤**：`SKILL.md` 的断点模板注释 `resolved by stage 00`、阶段 12 也写 `or the grant type resolved in stage 00`，而 stage 00 的实际流程只解析布局与文件归类。两处默认值又都写死为地区基金，导致在 `NSFC_General` / `NSFC_Young` 上会一路带着地区基金的 `focus` 与专家预期跑完模拟评审。现 stage 00 新增第 5 步显式解析项目类型（用户说明 → 项目 `AGENTS.md`/`README.md` → 目录名，均失败则停下询问，**不回退到地区基金**），阶段 12 的 `grant_type` 与适配性 focus 改为读取 `project.grant_type`，`config.yaml` 中 `simulated_review.grant_type` 置空。
- **地区基金篇幅上限被跨类型套用**：阶段 09 原写"normally 8000 Chinese characters or less"。经核，8000 字只见于 `projects/NSFC_Local/AGENTS.md`，`NSFC_General` 与 `NSFC_Young` 的 `AGENTS.md` 只规定全文 30 页。套用会导致面上/青年标书严重写不够。现 stage 00 新增第 6 步从项目自带 `AGENTS.md` 读出真实预算并记入 `project.length_budget`，阶段 09 改为引用该字段。
- **阶段 13 仍残留 five-part 专用编号**：`chapter inconsistency among 1.1, 1.2, 1.3, 1.4, and 1.5`、`weak 1.1 literature chain`、`plain-prose 1.3` 三处是 v0.1.0 声称已清除的编号硬编码的残留，在 three-part 布局上无意义。现改为按 stage 00 解析出的角色引用。
- **`AGENTS.md` 指代歧义可能污染仓库单一真相来源**：`SKILL.md` 通篇写 `AGENTS.md` 而未区分仓库根与标书项目两份文件，而阶段 01-03 会用 `research-guide-updater` 往"指南文件"里写研究范围。若解析到仓库根 `AGENTS.md`，将破坏整个仓库的开发指令。现在 `Required Initial Reads` 与断点模板的 `guide_file` 处显式限定为标书项目自己的 `AGENTS.md`。
- **布局校验表漏了两个新模板**：补上 `NSFC_General_Clean` 与 `NSFC_Local_Clean`，并说明 `*_Clean` 变体与母模板同布局、只是正文出厂为空。
- 阶段 05 的 `inputs` 补回 `docs/03_科学问题与创新点.md`；阶段 06 的 `outputs` 补上 `docs/05_研究基础素材.md`，使其自产的事实来源文件可被续跑校验。
- `config.yaml` 的 `sub_skills["05_part_one_writing"]` 补上 `SKILL.md` 已声明使用的 `research-plan`。
- 修正 v0.1.0 条目中的笔误：three-part 的 statements 为 `4.1`–`4.4` 与 `4.6`（`4.5.生成式人工智能.tex` 在 `main.tex` 中为注释态），原文误写为 `4.1`–`4.6`。

### Added（新增）

- `SKILL.md` 新增 `Scope` 小节，`config.yaml` 新增 `scope` 节：显式声明适用 `NSFC_General` / `NSFC_General_Clean` / `NSFC_Young` / `NSFC_Local` / `NSFC_Local_Clean`，不适用 `GDNSF_General` / `GDNSF_Regional_Young` / `GXNSF_General`。这三个省级模板的章节体例（立论依据、研究工作基础、实验条件、项目组人员简介、预期研究结果、组织管理措施、其他附件清单）与角色关键词完全不匹配，原先会在 stage 00 以"无法归类"静默卡死；现要求显式说明不适用并建议改用单点 skill。
- `config.yaml` 新增 `grant_type` 节，固化解析顺序、目录名提示、篇幅预算来源与各类型已知预算。
- `evals/evals.json` 由 14 条扩充到 17 条：新增面上项目模拟评审不得套用地区基金口径、省级基金项目须显式声明不适用、`research-guide-updater` 须写项目级而非仓库根 `AGENTS.md` 三条用例；同步修正 eval 4 与 eval 12。

### Changed（变更）

- frontmatter `description` 由英文改为中文，并与同系列 `nsfc-*` skill 的"当用户明确要求…时使用 + ⚠️ 不适用："范式对齐；新增 `metadata`（author / short-description / keywords）。原描述把适用范围写死为 `Regional Science Fund`，而 evals 4/6 恰恰是青年与面上项目用例，触发口径与实际能力不一致。
- `config.yaml` 的 `description` 同步扩展为覆盖面上、青年、地区三类，并补上省级基金的负向约束。
- stage 00 更名为 `Proposal Layout and Grant Type Resolution`，断点文件中同名阶段与 `README.md` 阶段表同步。

### Known Issues（已知问题）

- `SKILL.md` 由 617 行增至 649 行，仍未满足 ≤500 行规范；待把阶段细则外移到 `references/` 后统一收敛。
- `SKILL.md` 正文仍为英文，与项目"默认简体中文"规范不一致，待整体中译（本次仅改 frontmatter）。
- `docs/05_研究基础素材.md` 的编号与阶段编号错位（它是阶段 06 的输入而非阶段 05 的产物），本次未重命名以免影响已有断点文件。
- `skills/README.md` 中 `research-idea` 与 `research-plan` 两个被本编排器调用的子技能同样未登记，超出本次修复范围。

## [0.1.0] - 2026-08-16

首次纳入版本管理。此前该 skill 只有 `SKILL.md` 与 `evals/evals.json`，无版本号、无配置文件、未登记进 `skills/README.md`。

### Added（新增）

- 新增 `config.yaml`：作为版本号唯一真相来源，同时固化项目布局解析规则、断点完成判定口径、参考文献充分性闸门、子 skill 编排表与编译命令。
- 新增 `CHANGELOG.md` 与 `README.md`，补齐项目 Skill 开发规范要求的标准文件。
- `SKILL.md` 新增 `Stage 00: Proposal Layout Resolution`：在任何写作、修复或 QC 阶段之前，从 `main.tex` 的未注释 `\input{extraTex/...}` 解析真实正文文件集合，并按 `part_one` / `foundation` / `statements` 三个角色归类写入断点文件的 `project.body_files`。
- `SKILL.md` 新增 `Workspace Convention` 小节：说明 `docs/` 与 `review/` 属于 `skills/WORKSPACE.md` 定义的正式交付物因而不进任务工作区，而缓存、中间 JSON 与命令日志仍按标准约定隔离。
- 断点结构新增 `project.layout`、`project.body_files` 与 `00_layout_resolution` 阶段。
- `evals/evals.json` 由 3 条扩充到 14 条，沿用原有 schema 未做字段漂移。新增用例覆盖本次修复的每一处行为：three-part / five-part 布局解析（含禁止写入不存在的 `1.2`–`1.5`）、注释态 `\input` 不写入、孤儿文件不计入待办、布局解析失败必须停下询问、占位态文件不得判定为已完成、仓库根与项目内两种编译口径、阶段 06 缺事实时生成问卷、覆盖边界提示（摘要等需单独调用）、模拟评审默认 3 组、参考文献充分性闸门。

### Fixed（修复）

- **正文文件名硬编码导致跨模板静默写错章节**：阶段 05/06/07 原先写死 `1.1`–`1.5`、`2.1`–`2.4`、`3.1`–`3.5`，仅适配 `NSFC_Local` 与 `NSFC_2026_Education`。`NSFC_General` 与 `NSFC_Young` 使用 `1.1`+`2.1`–`2.3`、`3.1`–`3.4`、`4.1`–`4.4`+`4.6` 的另一套编号，两套编号互相重叠，在面上/青年项目上运行会把研究基础写进研究内容的位置且不报错。现全部改为按 stage 00 解析出的角色引用，`SKILL.md` 中已无编号型 `extraTex/N.N.*.tex` 硬编码。
- **编译命令路径不成立**：`python scripts/nsfc_build.py build --project-dir .` 依赖当前工作目录恰好是项目目录，而仓库根 `scripts/` 下并无该脚本。现区分仓库根入口 `packages/bensz-nsfc/scripts/nsfc_project_tool.py` 与项目内 wrapper 两种口径，并显式说明后者的适用前提。
- **续跑阶段完成判定失真**：原判定依据为"声明的输出文件是否存在"，但 `extraTex/*.tex` 在模板中本就存在且带 `\NSFCBlankPara` 占位，会被误判为已完成而跳过写作。现要求输出文件同时非占位态才可判定完成。
- **阶段 06 的 inputs 与 outputs 完全相同**，自引用使该阶段无法表达真实依赖。现输入改为 `docs/05_研究基础素材.md` 与已回填的补充问卷，输出为解析后的 `foundation` 文件集合。
- **`docs/研究基础.md` 无上游产出**：该文件被列为阶段 06 输入但无任何阶段生成。现明确为 `docs/05_研究基础素材.md`，并说明其由用户材料整理而来，作为独立于本阶段输出的事实来源。
- **AIGC 声明未被覆盖**：阶段 07 原始清单遗漏生成式人工智能声明。现要求按解析出的 `statements` 集合逐个处理；若该声明在 `main.tex` 中处于注释态，则不写入并在检查报告中提示用户决定是否启用。
- 修正中英混排残留 `response口径`、`proposal正文`。

### Changed（变更）

- 阶段 12 模拟评审默认 `panel_count` 由 `5` 调整为 `3`，与 `nsfc-reviewers` 自身调优默认值一致；需要更严格时可由用户显式提高到上限 5。
- 压缩断点文件模板：14 个阶段的重复字段改用流式列表表达，模板体积由 209 行降至约 150 行，字段语义不变。
- `SKILL.md` 行数由 625 行变为 617 行：压缩断点模板省下的约 60 行被 stage 00 布局解析、工作区约定与各阶段修正抵消。仍超出项目规范的 500 行上限，待后续将阶段细则外移到 `references/` 后单独收敛。

### Known Issues（已知问题）

- `SKILL.md` 尚未满足 ≤500 行的规范要求。
- 本编排器不覆盖 `nsfc-abstract`、`nsfc-code`、`nsfc-budget` 与配图链路，需用户单独调用；覆盖缺口已在 `config.yaml` 的 `not_covered` 中显式登记。
