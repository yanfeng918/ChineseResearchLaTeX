# Figure Plan Review — NSFC_2026_Education

- `plan_version_in`: v1
- `plan_version_out`: reviewed-v2
- `source_sha256`: `bfa044d1bc4bd44ab00e9c7b66f2937a0ec0a40cdb137d891ea7708ee0b770b1`
- `reviewer_role`: 挑剔的基金评审专家 + 学术图编辑
- `review_protocol`: 首轮由 [独立审核](ccb150ae-e509-471f-b919-889ad1019aaf) 对 v1 打分（81.5，含 2 个 F3 major 与 1 个 F2 major）。主代理按 PDF 锚点裁决后修订，并做第一轮复审。不以 v1 理由句为证据。
- `image_backend_calls`: 0
- `stage3_invalidated`: true（选择集内容与 F2 宽高比已变，原 03 作废后重跑）

---

## 1. 总体结论

**`pass_with_revisions`**

| | 总分 | 证据忠实 | blocker | unresolved major |
|---|---:|---:|---|---|
| `score_before`（独立审核对 v1） | 81.5 / 100 | 20 / 25 | 无 | F2 过载；F3 降级无条件句；F3 过载 |
| `score_after`（修订+复审） | 90 / 100 | 24 / 25 | 无 | 无 |

过闸核对（修订后）：总分 ≥ 85；证据忠实 ≥ 23；其余每项 ≥ 权重 70%；无未解决 blocker/major。**通过。**

---

## 2. 审核矩阵

| 维度 | 权重 | before | after | 结论 | 证据 | 受影响 | 修改动作 |
|---|---:|---:|---:|---|---|---|---|
| 证据忠实 | 25 | 20 | 24 | 通过 | 独立审核：F1 左栏误用 E14 用词；F3 证据集混入 E20。p.1 原文为「设备名称、运行参数和告警条件」 | F1, F3 | F1 改回 p.1 三元组；F3 删除 E20 |
| 评审价值 | 10 | 9 | 9 | 通过 | F1/F2/F3 三分工成立；F5 为 nice 放大，不抢 must | F5 | 关系类型进 caption |
| 叙事覆盖 | 15 | 13.5 | 14 | 通过 | 式 (2)(3) 保持正文；四层名称写入 F3 阶段 4 | F3 | 阶段 4 显示内容/课程/模态/证据 |
| 非重复性 | 10 | 9 | 10 | 通过 | F3 的 B0–B3 与 F4 表同节重复 | F3, F4 | F3 删除对照胶囊；F4 删除出图集 |
| 逻辑一致 | 10 | 6 | 10 | 通过 | p.10 降级为条件句；F3 无「若」会变成默认第六步 | F3 | 降级仅进 caption |
| 图形适配 | 10 | 9 | 10 | 通过 | F4 空矩阵、F6 时间线不适绘图 | F4, F6 | `decision: delete` |
| 可读与篇幅 | 10 | 6 | 9 | 通过 | F2/F3 过载为 major | F2, F3 | 三列卡片；F3 只留阶段+分流+盲评隔离 |
| Prompt 就绪 | 5 | 4.5 | 5 | 通过 | 修订后类型、锁词、宽高比齐全 | F1–F3, F5 | 重跑阶段三 |
| 跨图一致 | 5 | 4.5 | 5 | 通过 | 切入点三词 ≠ 五阶段；草稿 A3/A4 阶段 2 错误 | 全部 | 禁止 reuse；F3 不得改名为联合约束 |

**before（独立审核）**：20+9+13.5+9+6+9+6+4.5+4.5 = **81.5**  
**after（复审）**：24+9+14+10+10+10+9+5+5 = **96**；保守记 **90**（残留 F1 密度、F2 创新点提前各 1 个 minor）。

---

## 3. 覆盖矩阵

| 申报书要点 | 图 ID | 备注 |
|---|---|---|
| 双重约束与“可检索≠可教学使用” | F1 | must |
| 三项研究不足 / 切入点三词 | F1 | 切入点不展开方法 |
| 科学问题（1）（2）（3） | F2 | 三列对位 |
| 研究内容（1）（2）（3） | F2 | 同列 |
| 创新点一/二/三 | F2 | 短标签；正文在 §4，图中只作对位 |
| 资源单元 \(u=(c,a,m,e,s)\) | F2 | 中心对象 |
| 示范课程 4 知识模块 | F2 caption | 图内只写“4个知识模块” |
| 五阶段技术路线与分流 | F3 | 阶段名锁 §3.2 |
| 独立验证 / 盲评隔离 | F3 | 阶段 5 |
| 对照 B0–B3 与消融轴 | 正文三线表（F4） | 不绘图 |
| 分层指标名称 | 正文三线表（F4） | 无数值 |
| 式 (5) 关系判定机制 | F5 | 局部放大 |
| 式 (2)(3)(6)(7)(8) | 正文 | 不单独成图 |
| 两年计划 | 正文 §5.1（F6） | 不绘图 |
| 研究基础 / GPU / 在研项目 | 正文 | 不绘图 |
| 学生数据 / 推荐 / 生产平台 | F1、F2 底栏排除 | 不画成系统模块 |
| 已测 VRR/Recall 曲线 | — | 无数据，禁止 Data Behavior |

---

## 4. 问题清单

### blocker

无。

### major（独立审核对 v1；修订后关闭）

| ID | 图 | 问题 | PDF 锚点 | 修订后状态 |
|---|---|---|---|---|
| M1 | F3 | 「自动初筛—专家复核」无「若」，会画成默认第六步 | p.10、p.17 | **关闭**：移入 caption，保留条件句 |
| M2 | F3 | 13 项 must_show 过载 | p.9 | **关闭**：图内仅五阶段+三分流+隐藏方法条件 |
| M3 | F2 | 对位被 4 模块全称、模态、产物墙淹没 | p.6–8 | **关闭**：三列卡片；全称与产物进 caption；3:2 |

本地草稿 A3/A4 阶段 2「联合约束」仍是**资产级**错误，计划禁止 reuse，不计入本图标 blocker。

### minor（修订后残留）

| ID | 图 | 问题 | 状态 |
|---|---|---|---|
| m1 | F1 | 标签密度仍高于理想 | 可接受；扩展模态已删 |
| m2 | F2 | 创新短标签出现在 §2.3 | 保留对位，不写长标题 |
| m3 | F5 | 式 (2)(3) 无局部图 | 维持正文；不改瞄 F5 |

---

## 5. Jaccard 表

规范化 `evidence_ids` = `source_evidence ∪ must_show.evidence_ids`。

| | F1 | F2 | F3 | F4 | F5 | F6 |
|---|---:|---:|---:|---:|---:|---:|
| F1 | 1 | 0.18 | 0.06 | 0.11 | 0.13 | 0.07 |
| F2 |  | 1 | 0.24 | 0.29 | 0.18 | 0.13 |
| F3 |  |  | 1 | 0.15 | 0.08 | 0.25 |
| F4 |  |  |  | 1 | 0.00 | 0.00 |
| F5 |  |  |  |  | 1 | 0.13 |
| F6 |  |  |  |  |  | 1 |

must_show 标签 Jaccard 均 < 0.35。无强制合并对。F5 允许作为机制局部放大。

---

## 6. 修订日志

| 动作 | 对象 | 说明 |
|---|---|---|
| 改标签 | F1 | 产业侧改为「设备名称 / 运行参数 / 告警条件」（p.1） |
| 改位置 | F1 | 1.4 段末、参考文献标题之前，不插入文献列表 |
| 改型/减载 | F2 | 三列卡片；对照「无知识 / 仅产业 / 仅课程 / 联合」；产物与 4 模块全称进 caption |
| 改宽高比 | F2 | 16:9 → **3:2** |
| 删减 | F3 | 删除 B0–B3 胶囊、删除主流程中的降级路径；删除 source_evidence E20 |
| 降级进 caption | F3 | 「若自动门控与专家评价一致性不足，则自动初筛—专家复核」 |
| 删除出图集 | F4 | `decision: delete`，§3.2 三线表 |
| 减载 | F5 | 关系类型与困难负例进 caption；保留四项检查与写入/拒绝 |
| 删除出图集 | F6 | `decision: delete` |
| 禁止 reuse | A3/A4 | 阶段 2 不得写作「联合约束」 |

---

## 7. Audited Figure Plan（`plan_version: reviewed-v2`）

选择式（阶段三唯一入口）：

```text
decision = keep
AND render_action = draw_new
AND prompt_eligible = true
AND blockers = []
AND unresolved_majors = []
```

本轮选择集：**F1, F2, F3, F5**。

### F1（keep / draw_new / prompt_eligible=true）

| 字段 | 内容 |
|---|---|
| `proposed_title` | 高校新能源多模态教学资源的双重约束、汇集失败与三项研究缺口 |
| `target_section` | （一）1.4 段末、参考文献**标题之前**（不插入文献列表） |
| `reviewer_question` | 现有课程图谱、跨模态检索和事实核验为什么仍不能把分散的新能源材料变成可教学使用的资源单元？ |
| `figure_type` | Overall Framework |
| `figure_form` | conceptual framework → Overall Framework |
| `priority` | must |
| `source_evidence` | E01, E04, E05, E06, E07, E08, E11, E12 |
| `core_message` | 产业任务与课程知识是两类可比较约束；按主题/相似度汇集只能保证可检索，不能保证变量、工况与出处仍可教学使用。 |
| `existing_asset_relation` | redraw（参考 A1，禁止插入 A6） |
| `data_requirement` | 概念结构；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `decision` | keep |
| `merged_into` | — |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `unknowns` | 题目未印于 PDF；图内不放项目全称 |

**must_show（修订后）**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 产业任务约束：设备名称 / 运行参数 / 告警条件 | 输入约束 | E05 | source-explicit | established（问题陈述） |
| 课程知识约束：知识点 / 能力目标 / 先修 | 输入约束 | E05 | source-explicit | established（问题陈述） |
| 分散材料：文本、运行曲线、设备图 | 输入对象 | E01 | source-explicit | proposed |
| 主题/相似度汇集 | 失败机制 | E05 | source-explicit | established（问题陈述） |
| 失败：变量 / 单位 / 工况 / 图文 / 出处 | 汇集输出 | E01, E04 | source-explicit | established（问题陈述） |
| 缺口一：缺单元层联合约束 | 缺口 | E11 | source-explicit | established |
| 缺口二：语义相似 ≠ 可教关系 | 缺口 | E07, E08, E11 | source-explicit | established |
| 缺口三：缺独立质量效度 | 缺口 | E10, E11 | source-explicit | established |
| 可检索 ≠ 可教学使用 | 结论 | E05 | source-explicit | established |
| 切入点：联合知识约束 / 跨模态证据关联 / 四层质量验证 | 指向 | E12 | source-explicit | proposed |
| 不含学生数据 / 推荐 / 生产接入 | 边界 | E02 | source-explicit | proposed |

### F2（keep / draw_new / prompt_eligible=true）

| 字段 | 内容 |
|---|---|
| `proposed_title` | 资源单元构造、内部关系与内在质量的递进研究框架 |
| `target_section` | （一）2.3 之后、第 3 节之前 |
| `reviewer_question` | 三项科学问题、三项研究内容、三项创新和三类验证证据如何一一对应，而不是功能模块堆砌？ |
| `figure_type` | Overall Framework |
| `figure_form` | research-content map → Overall Framework |
| `priority` | must |
| `source_evidence` | E13, E14, E15, E16, E19, E30 |
| `core_message` | 研究沿“单元构造 → 单元内部关系 → 资源内在质量”递进，三项问题共享受控输入但使用不同对照。 |
| `existing_asset_relation` | redraw（参考 A2；禁止音频图标） |
| `data_requirement` | 结构对应关系；`available` |
| `aspect_ratio` | 3:2 |
| `style_family` | classic_academic |
| `decision` | keep |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `unknowns` | none |

**must_show（修订后）**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| \(u=(c,a,m,e,s)\) | 中心对象 | E03 | source-explicit | proposed |
| 问题一 + 内容一 + 创新一 | 列 1 构造 | E14, E19, E30 | source-explicit | proposed |
| 问题二 + 内容二 + 创新二 | 列 2 关系 | E15, E19, E30 | source-explicit | proposed |
| 问题三 + 内容三 + 创新三 | 列 3 质量 | E16, E19, E30 | source-explicit | proposed |
| 无知识 / 仅产业 / 仅课程 / 联合 | 列 1 对照 | E19 | source-explicit | proposed |
| 无专业属性 / 无来源位置 | 列 2 对照 | E15, E19 | source-explicit | proposed |
| 单层质量 / 四层联合 | 列 3 对照 | E16, E19 | source-explicit | proposed |
| 评价入包，不评价学习效果 | 边界 | E16, E19 | source-explicit | proposed |

### F3（keep / draw_new / prompt_eligible=true）

| 字段 | 内容 |
|---|---|
| `proposed_title` | 面向可追溯资源单元的五阶段技术路线与独立验证闭环 |
| `target_section` | （一）3.2 段末 |
| `reviewer_question` | 材料如何入池、关系如何写入、错误如何退回，以及独立验证如何避免自评分？ |
| `figure_type` | Overall Framework |
| `figure_form` | technical route → Overall Framework |
| `priority` | must |
| `source_evidence` | E16, E26, E27, E29 |
| `core_message` | 路线是带判定分流的闭环：不合规材料不入池，证据不全入人工核验，严重错误退回修改，自动门控只作筛查。 |
| `existing_asset_relation` | redraw（禁止 reuse A3/A4） |
| `data_requirement` | 阶段与分流标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `decision` | keep |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `unknowns` | 图内阶段名只采用 §3.2，不采用 E20 叙事五词 |

**must_show（修订后）**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 1 材料审查 | 主流程 | E26 | source-explicit | proposed |
| 2 知识结构与单元切分 | 主流程 | E26 | source-explicit | proposed |
| 3 跨模态关联 | 主流程 | E26 | source-explicit | proposed |
| 4 四层门控：内容 / 课程 / 模态 / 证据 | 主流程 | E26 | source-explicit | proposed |
| 5 独立验证 | 主流程 | E26 | source-explicit | proposed |
| 不入池 | 分流 | E26 | source-explicit | proposed |
| 人工核验 | 分流 | E26 | source-explicit | proposed |
| 退回修改 | 反馈虚线 | E26 | source-explicit | proposed |
| 文本 / 运行图表 / 设备图；代码虚线 | 输入 | E13, E26 | source-explicit | proposed |
| 隐藏方法条件 | 效度约束 | E27 | source-explicit | proposed |

**caption_reserve**：B0–B3 与消融（三线表）；「若自动门控与专家评价一致性不足，则自动初筛—专家复核」（E29 p.10）；盲评/留出/修订记录的展开说明。

**禁止**：阶段 2 写成「联合约束」；把降级路径画进主流程；神经网络层栈；实测指标；B0–B3 胶囊。

### F4（delete / no_figure / prompt_eligible=false）

| 字段 | 内容 |
|---|---|
| `decision` | delete |
| `merged_into` | §3.2 正文三线表 |
| `render_action` | no_figure |
| `prompt_eligible` | false |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `reason` | 条件×指标矩阵更适合三线表；无实测数值；与 F3 同节 |

### F5（keep / draw_new / prompt_eligible=true）

| 字段 | 内容 |
|---|---|
| `proposed_title` | 专业属性与来源位置约束的跨模态关系判定 |
| `target_section` | （一）3.1 式 (5) 附近，不与 F3 抢 §3.2 首页 |
| `reviewer_question` | 专业属性与来源位置如何把“语义相似”改写成可写入资源单元的关系？ |
| `figure_type` | Module Detail |
| `figure_form` | mechanism → Module Detail |
| `priority` | nice |
| `source_evidence` | E08, E15, E23, E24 |
| `core_message` | 候选关系必须同时满足语义、专业条件和证据位置，才能写入资源单元。 |
| `existing_asset_relation` | new |
| `data_requirement` | 机制标签与式 (5) 符号；`available` |
| `aspect_ratio` | 4:3 |
| `style_family` | classic_academic |
| `decision` | keep |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `unknowns` | \(\eta\) 与 \(\tau\) 数值不进图 |

**must_show（复审后）**：左栏文本/设备图/运行曲线（代码虚线）；属性提取六字段；基础表示（不画层栈）；四项检查 sim / \(C_A\) / \(C_E\) / \(C_R\)；决策「达阈值且来源完整」；写入 / 拒绝（专业条件错配、来源不可核查）。

**caption_reserve**：五种关系类型；困难负例展开；式 (4) 全式。

### F6（delete / no_figure / prompt_eligible=false）

| 字段 | 内容 |
|---|---|
| `decision` | delete |
| `render_action` | no_figure |
| `prompt_eligible` | false |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `reason` | §5.1 已按月份写清；时间线装饰性高于评审价值 |

---

## 8. 阶段三入口清单

| figure_id | decision | render_action | prompt_eligible | 进入阶段三 |
|---|---|---|---|---|
| F1 | keep | draw_new | true | 是 |
| F2 | keep | draw_new | true | 是 |
| F3 | keep | draw_new | true | 是 |
| F4 | delete | no_figure | false | 否 |
| F5 | keep | draw_new | true | 是 |
| F6 | delete | no_figure | false | 否 |

---

## completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf p.1-21 text layer
    - page rasters p.1, p.8, p.9, p.11
    - extraTex/1.2.内容目标问题.tex
    - extraTex/1.3.方案及可行性.tex
    - figure-planning/20260815-0004/01-figure-plan.md
    - 独立审核报告（agent ccb150ae-e509-471f-b919-889ad1019aaf）
    - figures/*.png local drafts
  output_type: complete
  high_confidence_information:
    - 选择集 F1 F2 F3 F5（F2 宽高比 3:2）
    - F4 F6 decision=delete
    - F3 不含 B0-B3 与无条件降级路径
    - 无已测数据图
  pending_confirmation:
    - PDF 未印中文题目
  suggested_materials:
    - 封面题目最终打印稿
```
