# Changelog — nsfc-full-pipeline

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

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

- **正文文件名硬编码导致跨模板静默写错章节**：阶段 05/06/07 原先写死 `1.1`–`1.5`、`2.1`–`2.4`、`3.1`–`3.5`，仅适配 `NSFC_Local` 与 `NSFC_2026_Education`。`NSFC_General` 与 `NSFC_Young` 使用 `1.1`+`2.1`–`2.3`、`3.1`–`3.4`、`4.1`–`4.6` 的另一套编号，两套编号互相重叠，在面上/青年项目上运行会把研究基础写进研究内容的位置且不报错。现全部改为按 stage 00 解析出的角色引用，`SKILL.md` 中已无编号型 `extraTex/N.N.*.tex` 硬编码。
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
