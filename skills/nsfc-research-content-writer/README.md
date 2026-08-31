# nsfc-research-content-writer

用于 NSFC 标书正文 `（二）研究内容` 的写作/重构，并**同时编排**「特色与创新」与「年度研究计划」。

目标是形成“研究内容 → 技术路线 → 创新点 → 年度计划”的一致闭环。写入落点从 `main.tex` 按角色解析，适配面上/青年（三段式）与地区（五段式）两种章节编号。

## 参数（建议显式提供）

- `project_root`：标书项目根目录（如 `projects/NSFC_Young`）
- `output_mode`（默认 `apply`）
  - `preview`：只按角色输出可复制的 LaTeX 草稿，不写文件
  - `apply`：仅写入落点解析得出的角色文件（三段式 3 份，五段式 4 份），不触碰其他文件

## 推荐用法（Prompt 模板）

```
请使用 nsfc-research-content-writer：
project_root：projects/NSFC_Young
信息表：请按 skills/nsfc-research-content-writer/references/info_form.md 提供
输出：落点从 main.tex 按角色解析（勿按 extraTex/2.*.tex 编号 glob 选文件）
output_mode：apply（默认）/ preview（只预览不写入）
研究类型：基础研究 / 应用研究（用于选择更贴合的组织框架；不确定时按“问题→目标→内容→路线→验证”通用主线组织）
篇幅目标（推荐）：研究内容 12–15 页（含图表），纯文字约 12000–15000 字；以“页数控制”为主，不要以字数为导向
额外要求：子目标编号 S1–S4；每个子目标必须写清 指标+对照+数据来源；创新点与年度计划标注回溯到对应 Sx（正文中改用自然语言）
技术路线：先总体路线（起点/主链/各研究内容落位/依赖关系/目标闭合），再分项路线（每项研究内容一条，含输入/方法与关键步骤/输出/验证口径/衔接），条数与序号须与研究内容严格对应
禁止改动：不要改 main.tex、extraTex/@config.tex、任何 .cls/.sty
```

## 写入落点：按角色解析（不按编号）

NSFC 模板不共用一套章节编号，而且编号互相重叠：

| 布局 | 项目 | 研究内容 | 特色与创新 | 年度计划 | 方案及可行性 |
|---|---|---|---|---|---|
| 三段式 | `NSFC_General`、`NSFC_General_Clean`、`NSFC_Young` | `2.1.研究内容` | `2.2.特色与创新` | `2.3.年度研究计划` | 无（技术路线并入研究内容） |
| 五段式 | `NSFC_Local`、`NSFC_Local_Clean` | `1.2.内容目标问题` | `1.4.特色与创新` | `1.5.研究计划` | `1.3.方案及可行性` |

在五段式项目上，`extraTex/2.*.tex` 匹配到的其实是 `2.1.研究基础` / `2.2.工作条件` / `2.3.承担项目`——按编号写会把研究内容写进研究基础**且编译不报错**。所以本技能强制先读 `main.tex` 里未被注释的 `\input{extraTex/...}`，按角色关键词归类出真实文件，解析不出就停下来问你。

**技术路线落点随布局变化**：三段式并入研究内容；五段式写入独立的 `1.3.方案及可行性`。

## 技术路线：总—分结构（强制）

技术路线与研究内容脱节是这一章最常见的扣分点——评审看不出"哪条路线在解决哪项研究内容"。本技能强制按两层写：

**（总）总体技术路线**：1–2 段 + 技术路线图。写清起点输入 → 关键环节主链 → 每项研究内容落在哪一环 → 环节间是串行依赖还是并行推进 → 整条链跑通后如何达成总目标。**不能把研究内容标题复述一遍就算总体路线。**

**（分）分项技术路线**：每项研究内容对应且仅对应一条，标题写明"面向研究内容 X"。每条覆盖五要素：

| 要素 | 作用 |
|---|---|
| 输入 | 数据/材料/前序产物从哪来 |
| 方法与关键步骤 | 具体做什么、分几步（不只堆方法名） |
| 输出 | 产出什么可交付、可度量的结果 |
| 验证口径 | 对照/基线、消融、外部验证、统计、泄漏防控 |
| 衔接 | 产出给谁用；末端环节说明如何汇入总目标 |

**数量硬约束**：分路线条数 = 研究内容项数，序号严格对应。不允许缺口（有内容无路线）或孤儿（有路线无内容）。

写完会用"研究内容 ↔ 分路线"映射表逐项核对数量、序号、术语、依赖闭合四件事。详见 `references/technical_route_structure.md`。

## 篇幅与图表（写作提醒）

- 研究内容推荐页数：12–15 页（含图表），约占标书总页数（≤28 页）的 50%
- 研究内容推荐字数：12000–15000 字（纯文字部分）
- 评审标准已从“字数控制”转向“页数控制”，建议先按页数规划结构，再用图表提质
- 技术路线图建议放在研究内容开头，并与总体技术路线段落相互印证；图中模块命名要与正文研究内容名称一致
- 参考：`skills/nsfc-research-content-writer/references/page_budget.md`

## 推荐工作流（先预览再写入）

1. `output_mode=preview` 按角色生成草稿（用于审阅口径与结构）
   - 可参考 `skills/nsfc-research-content-writer/references/output_skeletons.md` 的最小结构骨架快速起草
2. 人工确认后切换 `output_mode=apply` 写入落点解析得出的角色文件

## 验收自检

- 按 `skills/nsfc-research-content-writer/references/dod_checklist.md` 快速自检（重点看落点是否按角色解析、技术路线总分两层齐全且与研究内容逐项对应、创新点可回溯、年度计划覆盖 S1–S4）
- 可选脚本自检（只读）：`python3 skills/nsfc-research-content-writer/scripts/check_project_outputs.py --project-root projects/NSFC_Young`
  - 更严格（将“首次/领先”等绝对化措辞视为错误）：`python3 skills/nsfc-research-content-writer/scripts/check_project_outputs.py --project-root projects/NSFC_Young --fail-on-risk-phrases`
  - 一键执行（先校验 skill 再自检输出）：`python3 skills/nsfc-research-content-writer/scripts/run_checks.py --project-root projects/NSFC_Young --fail-on-risk-phrases`

## 开发者：一致性校验与可追溯测试会话

- 校验（必需）：`python3 skills/nsfc-research-content-writer/scripts/validate_skill.py`
- 创建 A/B 轮会话骨架（在本 skill 目录下执行）：
  - A轮：`python3 scripts/create_test_session.py --kind a --id vYYYYMMDDHHMM --create-plan`
  - B轮：`python3 scripts/create_test_session.py --kind b --id vYYYYMMDDHHMM --create-plan`
