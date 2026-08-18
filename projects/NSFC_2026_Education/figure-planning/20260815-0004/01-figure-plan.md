# Figure Plan v1 — NSFC_2026_Education 申报书配图规划

- `plan_version`: v1
- `source_pdf`: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/main.pdf`
- `source_sha256`: `bfa044d1bc4bd44ab00e9c7b66f2937a0ec0a40cdb137d891ea7708ee0b770b1`
- `pages`: 21（实际分析页 1–21）
- `extraction`: text（`pdftotext -layout`；未 OCR）
- `visual_check`: 页 1、8、9、11 的 72 dpi 临时栅格；均为纯文本页，无插图。临时栅格不交付。
- `extraction_warnings`: 第 1 页正文未印项目题目；题目取自同级 `docs/00_项目基本信息.md`，标为 `待确认`（相对 PDF 正文）。公式行因 PDF 文本层折行，符号以 `extraTex/1.3.方案及可行性.tex` 核验。页 8–9 公式编号 (1)–(8) 为 source-explicit。
- `dependency_versions`:
  - `plan-proposal-figures`: 0.1.0
  - `Academic Paper Analyzer & Figure Planner`: 1.2.0
  - `Academic Figure Prompt`: 1.5.0（本阶段不调用）
- `style_family`: `classic_academic`（本 Skill 仅支持 classic）
- `image_backend_calls`: 0（本阶段禁止 prompts 与生图）

---

## 申报书概览与科学问题摘要

**题目（待确认，PDF 正文未印）**：产业—课程知识联合约束下高校新能源多模态教学资源构建与质量验证研究。

**申报类型（PDF 第 20–21 页 source-explicit）**：新疆教育云技术与资源重点实验室 2026 年度开放课题；正文按国家自然科学基金地区科学基金章节结构撰写。实施期按两年安排。

**对象与边界**：以“新能源数据分析与功率预测”示范课程模块为验证场景，模块内 4 个知识模块（新能源运行数据与变量认知；功率数据预处理与可视化；功率预测建模与实验；结果评价与工程案例）。核心模态为课程文本、运行曲线/图表、设备图/结构图；代码与产业案例为扩展模态。不采集学生数据、不做个性化推荐、不接入生产平台。

**贡献主线（拟开展，非已验证结果）**：

1. 产业任务知识与课程知识的联合约束，改善资源单元边界、覆盖与属性准确性。
2. 专业属性与来源位置共同约束跨模态关联，抑制“语义相似但条件错误”。
3. 内容—课程—模态—证据四层内在质量门控，并与独立专家盲评对照，不依赖学习行为数据。

**资源单元**：\(u=(c,a,m,e,s)\)，分别表示课程知识、专业属性、多模态片段及关系、来源位置、质量状态。

**验证设计（proposed）**：对照 B0 人工整理 / B1 通用大模型 / B2 仅文本 RAG / B3 完整方法；消融产业知识、课程知识、专业属性、来源位置、质量层；跨来源留出；独立专家盲评。主指标为有效资源单元通过率 VRR；关联层报告 Recall@1/5、MRR、关系 F1、来源定位准确率。拟构建规模（4 模块、300+ 单元、抽取 120 盲评）不得画成既有事实。

- `domain`: 高等教育数字化 × 新能源工程教育 × 多模态资源构建与质量验证
- `venue`: None（实验室开放课题 / NSFC 式申请书，非会议期刊）
- `palette / style family hint`: classic academic；框架图模块数 ≥ 4 → 倾向 Nature Blue
- `module_count_framework`: 5（技术路线主阶段：材料审查 → 知识结构与单元切分 → 跨模态关联 → 四层门控 → 独立验证）

论文 4–12 图经验值**不适用**。21 页、第（一）部分建议 8000 字以下、且 PDF 内无插图：规划 3 must + 1 strong + 1 nice + 1 建议改表，总页面成本约 1.9–2.6 页。

---

## section_status

将申报书评审结构映射为规划器章节，而不是论文 Intro/Method/Experiments。

| 申报书评审结构 | 对应 PDF 位置 | 状态 |
|---|---|---|
| 立项依据、研究现状与核心缺口 | §1.1–1.4，p.1–3 | present |
| 科学问题、科学假设与研究目标 | §2.2–2.3，p.6–8 | present |
| 研究内容及其依赖关系 | §2.1，p.6 | present |
| 总体框架、技术路线与关键机制 | §3.1–3.3，p.8–10 | present |
| 验证方案、指标、对照与可证伪条件 | §3.1–3.2、§2.2，p.7–9 | present |
| 创新点、可行性、研究基础与年度计划 | §4、§5、（二）1–2，p.10–18 | present |
| 已测实验结果 / 数据图 | 无 | absent |

---

## 现有图处置清单

### PDF 内插图

| 资产 | 位置 | 作用 | 处置 |
|---|---|---|---|
| PDF Image XObject | `pdfimages -list` 为空 | 无 | 无 reuse / redraw |
| 正文图题 / `\includegraphics` | `extraTex/*.tex` 与 `main.tex` 均无 figure 环境 | 无 | 无 reuse |

`existing_asset_relation_confidence`（相对 PDF）：**high**（文本层完整 + 无 Image XObject + 源 tex 无 figure 环境 + 页 1/8/9/11 栅格为纯文本）。

### 项目目录本地草稿（未嵌入申报书）

以下 PNG 位于 `projects/NSFC_2026_Education/figures/`，生成于 2026-08-14，**不是**申报书插图。历史 `figure-planning/20260814-2338` 误记该目录为空，本轮更正。

| 资产 ID | 文件 | 视觉主题（核对后） | 与拟规划图关系 | 处置 |
|---|---|---|---|---|
| A1 | `fig1-research-background.png` | 需求→分散材料→重组失败→三项缺口→切入点 | 最接近 F1 | `redraw`：可作构图参考，不可直接插入（未入 PDF；标签密度需按 Text Budget 重锁） |
| A2 | `fig2-overall-framework.png` | \(u=(c,a,m,e,s)\) + 三列科学问题 | 最接近 F2 | `redraw`：不可直接插入；草稿描述中出现音频类图标风险，PDF 无“音频”模态 |
| A3 | `fig3-technical-route.png` | 五阶段流水线 + B0–B3 | 最接近 F3 | `redraw`：**blocker 级标签错误**——第 2 阶段写成「联合约束」，正文 §3.2 为「知识结构与单元切分」 |
| A4 | `fig1-overall-framework.png`、`-p1`、`-p2` | 与 A3 同类五阶段流水线 | 与 F3 同义重复 | `no_figure` / 不插入 |
| A5 | `overall-framework.png`、`overall-framework-native-3x2.png` | 更早的框架草稿 | 与 F3 同义重复 | `no_figure` / 不插入 |
| A6 | `research_background.png`、`research_background_v2.png` | 背景→问题→科学问题→目标 五步叙事 | 把 F1 与 F2 叠进一张 | `no_figure`：插入会与 F1/F2 重复 |

`existing_asset_relation_confidence`（相对本地草稿）：**medium**（已读图，但草稿非 PDF 证据；图内个别标签与正文不一致）。

历史规划文档 `docs/core-three-figure-plan-and-prompts.md`、`docs/figure_spec_package.md` 不是申报书插图，**不作为本轮科学证据**。

---

## evidence_registry

每条记录：`evidence_id` / PDF 页 / 章节 / 摘要 / 置信度。

| evidence_id | 页 | 章节 | 摘要 | 置信度 |
|---|---:|---|---|---|
| E01 | 1 | 1.1 | 新疆新能源产业需要能源工程、数据分析与 AI 素养人才；设备图、运行曲线、数据说明、代码与案例常以分散文件存在，自动重组易出现变量、单位、工况、图文关系和出处错误 | high |
| E02 | 1 | 1.1 | 对象为“新能源数据分析与功率预测”示范课程模块；成果为资源包和本地原型；不涉及学生数据、个性化推荐或生产平台接入 | high |
| E03 | 1 | 1.1 | 资源单元由课程知识点/能力目标、专业属性、多模态片段、来源位置和质量状态组成 | high |
| E04 | 1 | 1.1 | 难点在判断曲线与文字是否共享变量和时间窗口、设备图是否支持工况、代码是否对应目标知识点 | high |
| E05 | 1 | 1.1 | 产业资料服务工程任务，课程材料围绕知识点、能力目标和先修关系；直接按主题或相似度汇集易造成“可检索但不可教学使用” | high |
| E06 | 1–2 | 1.2 | 教育知识图谱与多模态教育图谱可统一表示材料，但通常不同时约束产业任务、工程属性、资源片段和出处位置 | high |
| E07 | 2 | 1.2 | 多模态检索与图表理解提供共享表示，但通用相似度不能保证设备对象、变量、单位、工况和时间尺度正确 | high |
| E08 | 2 | 1.2 | 专业教学关系至少含三层：语义相关、对象与条件相容、关键结论可回到原始材料位置 | high |
| E09 | 2 | 1.2 | RAG 与事实核验提供组件基础，尚未给出新能源课程资源中知识、专业条件与出处的联合检验机制 | high |
| E10 | 2 | 1.2 | 内容正确却偏离课程目标、文字与曲线分属不同工况、出处不支撑断言，均影响资源能否进入资源包；提出内容、课程、模态、证据四层质量门控 | high |
| E11 | 2–3 | 1.3 | 三项不足：缺少资源单元层联合约束；跨模态以语义相似为主；四层评价分散且缺少不依赖学生行为、可与专家盲评比较的内在质量效度 | high |
| E12 | 3 | 1.4 | 切入点主线为“联合知识约束—跨模态证据关联—四层质量验证”；对照为人工整理、通用大模型、仅文本 RAG、完整方法；并消融产业知识、课程知识、专业属性、来源约束和质量层；允许负结果 | high |
| E13 | 6 | 2.1 | 两年期最小可行验证；4 个知识模块（运行数据与变量认知；功率数据预处理与可视化；功率预测建模与实验；结果评价与工程案例）；核心模态=课程文本、运行曲线/图表、设备结构图；代码/案例为扩展模态，不作为方法成立前提 | high |
| E14 | 6 | 2.1(1) | 研究内容（1）：建立“任务—对象—条件—知识点—片段—证据位置”描述模式；比较无知识、单一知识和联合知识 | high |
| E15 | 6 | 2.1(2) | 研究内容（2）：提取对象、变量、单位、工况、时间窗口和来源位置；关系类型含解释、实例、计算/实验、对照和出处支持；困难负例为变量/单位/工况/时序错配和来源不可核查 | high |
| E16 | 6 | 2.1(3) | 研究内容（3）：四层门控，任一层严重错误即拒绝；自动门控只作筛查；以专家盲评、跨来源留出和人工修订记录检验效度；只评价能否入包 | high |
| E17 | 6–7 | 2.2 | 总体目标与目标一/二/三，分别对应联合约束、跨模态关联、四层验证；目标二指标含 Recall@1/5、MRR、关系 F1、来源定位准确率 | high |
| E18 | 7 | 2.2 | 拟构建 4 个知识模块、300 个以上单元、抽取 120 个由不少于 3 名未参与构建的专家盲评；阈值在预实验后冻结；**不得表述为既有前期事实** | high |
| E19 | 7–8 | 2.3 | 关键科学问题（1）联合约束何时改善单元构建；（2）专业属性与来源如何决定跨模态正确性；（3）不依赖学生行为的内在质量如何获得独立效度 | high |
| E20 | 8 | 3.1 | 路线：“受控资源输入—联合知识约束—跨模态证据关联—质量门控—独立验证”；\(u=(c,a,m,e,s)\) 为式 (1)；\(\mathcal{K}_c,\mathcal{K}_p\) | high |
| E21 | 8 | 3.1 | 式 (2) \(S_{\mathrm{kc}}\)：产业、课程与术语映射三项加权；在无知识/单一/联合条件下比较 | high |
| E22 | 8 | 3.1 | 式 (3) \(\mathcal{L}_{\mathrm{unit}}\)：覆盖、重复、过度切分、属性错配 | high |
| E23 | 8 | 3.1 | 式 (4) 对比学习 \(\mathcal{L}_{\mathrm{align}}\)，用于基础表示，不是独立网络架构贡献 | high |
| E24 | 8 | 3.1 | 式 (5) \(R(i,j)=\eta_s\mathrm{sim}+\eta_a C_A+\eta_e C_E+\eta_r C_R\)；达阈值且来源完整才写入 | high |
| E25 | 8–9 | 3.1 | 式 (6)(7)(8)：证据支持 \(G\)、四层质量 \(Q\)、主指标 VRR；权重与阈值仅在开发集确定、测试集冻结 | high |
| E26 | 9 | 3.2 | 五阶段：材料审查、知识结构与单元切分、跨模态关联、四层门控、独立验证；未通过审查不入池；属性/证据不全入人工核验；严重错误退回修改 | high |
| E27 | 9 | 3.2 | 对照 B0/B1/B2/B3；逐项去除产业知识、课程知识、专业属性、来源位置或质量层；评分隐藏方法条件 | high |
| E28 | 9 | 3.2 | 构建层：边界 F1、覆盖、重复、属性错误；关联层：Recall@K、MRR、关系 F1、来源定位、错配率；质量层：VRR、检出/误报、五维盲评、修订时间 | high |
| E29 | 9–10 | 3.3 | 可行性降级：收缩知识模块；以文本—图像/图表为主；自动初筛—专家复核；仅用公开许可和自主编写材料 | high |
| E30 | 10–11 | 4 | 三项创新分别对应联合知识、专业条件错配抑制、四层独立效度；系统功能数量和资源包规模不是创新证据 | high |
| E31 | 11–12 | 5.1–5.2 | 第一阶段第 1–12 月、第二阶段第 13–24 月；预期方法、资源包、元数据、本地原型；力争二区 SCI 2 篇（承诺边界已写明） | high |
| E32 | 12–15 | （二）1 | 申请人时序预测、跨模态检索/VQA、知识库与教学经历为 **established** 基础；本项目课程资源构建与四层效度仍为 **proposed** | high |
| E33 | 16–18 | （二）2 | GPU（A40×8、3090 Ti×6）、约 10 名研究生为已具备条件；材料权利登记与正式盲评名单为尚缺 | high |
| E34 | 20–21 | （三）5 | 实际资助背景为实验室开放课题；NSFC 结构用于论证 | high |
| E35 | — | 资产盘点 | PDF 无 Image XObject；`extraTex` 无 figure 环境；页栅格无插图 | high |
| E36 | — | 元数据 | 中文题目见 `docs/00_项目基本信息.md`，PDF 正文未印 | medium |
| E37 | — | 本地草稿 | `figures/` 10 张 PNG 未入 PDF；A3/A4 第 2 阶段标签与 E26 冲突 | high |

公式、节点、边默认 `evidence_status: source-explicit`，`research_state: proposed`（方法与指标）或 `expected`（验收指标），除非标明 `established`。

---

## 分条目 Figure Plan

### F1

| 字段 | 内容 |
|---|---|
| `figure_id` | F1 |
| `proposed_title` | 高校新能源多模态教学资源的双重约束、汇集失败与三项研究缺口 |
| `target_section` | （一）1.4 研究切入点之后、参考文献之前（约 p.3） |
| `reviewer_question` | 现有课程图谱、跨模态检索和事实核验为什么仍不能把分散的新能源材料变成可教学使用的资源单元？ |
| `figure_type` | Overall Framework |
| `figure_form` | conceptual framework → Overall Framework |
| `priority` | must |
| `source_evidence` | E01, E04, E05, E06, E07, E08, E11, E12 |
| `core_message` | 产业任务与课程知识是两类可比较约束；按主题/相似度汇集只能保证可检索，不能保证变量、工况与出处仍可教学使用。 |
| `existing_asset_relation` | redraw（参考 A1，不插入 A6） |
| `proposed_render_action` | draw_new |
| `data_requirement` | 概念结构；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | 题目未印于 PDF；图内不放项目全称长标题 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 产业任务约束：设备 / 工况 / 参数 | 左栏输入约束 | E05, E14 | source-explicit | established（问题陈述） |
| 课程知识约束：知识点 / 能力目标 / 先修 | 左栏输入约束 | E05, E14 | source-explicit | established（问题陈述） |
| 分散材料：文本、运行曲线/图表、设备图 | 输入对象 | E01, E13 | source-explicit | proposed（本项目对象） |
| 扩展模态：代码 / 案例（虚线） | 次要输入 | E13 | source-explicit | proposed |
| 主题/相似度汇集 | 失败机制 | E05 | source-explicit | established（问题陈述） |
| 失败类型：变量/单位/工况/图文/出处错误 | 汇集输出 | E01, E04 | source-explicit | established（问题陈述） |
| 缺口一：缺少单元层联合约束 | 缺口 | E11 | source-explicit | established（文献不足） |
| 缺口二：语义相似 ≠ 专业条件成立 | 缺口 | E07, E08, E11 | source-explicit | established（文献不足） |
| 缺口三：四层质量分散、无独立效度 | 缺口 | E10, E11 | source-explicit | established（文献不足） |
| 判断：可检索 ≠ 可教学使用 | 一句话结论 | E05 | source-explicit | established（问题陈述） |
| 切入点三词：联合知识约束 / 跨模态证据关联 / 四层质量验证 | 右端指向，不展开方法 | E12 | source-explicit | proposed |
| 底栏边界：不涉及学生数据、推荐、生产平台 | 范围 | E02 | source-explicit | proposed |

**禁止入图**：式 (1)–(8)、B0–B3、五阶段流程、VRR 数值、300/120 规模、科学问题编号 Q1–Q3（留给 F2）、音频模态、具体模型名称作为“已被证伪”的对象。

---

### F2

| 字段 | 内容 |
|---|---|
| `figure_id` | F2 |
| `proposed_title` | 资源单元构造、内部关系与内在质量的递进研究框架 |
| `target_section` | （一）2.3 关键科学问题之后、第 3 节之前（约 p.8） |
| `reviewer_question` | 三项科学问题、三项研究内容、三项创新和三类验证证据如何一一对应，而不是功能模块堆砌？ |
| `figure_type` | Overall Framework |
| `figure_form` | research-content map → Overall Framework |
| `priority` | must |
| `source_evidence` | E13, E14, E15, E16, E17, E19, E20, E30 |
| `core_message` | 研究沿“单元构造 → 单元内部关系 → 资源内在质量”递进，三项问题共享受控输入但使用不同对照。 |
| `existing_asset_relation` | redraw（参考 A2） |
| `proposed_render_action` | draw_new |
| `data_requirement` | 结构对应关系；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | none |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 对象：资源单元 \(u=(c,a,m,e,s)\) | 中心对象 | E03, E20 | source-explicit | proposed |
| 示范课程 4 知识模块名称 | 场景 | E13 | source-explicit | proposed |
| 核心模态 vs 扩展模态 | 输入范围 | E13 | source-explicit | proposed |
| 科学问题（1）+ 研究内容（1）+ 创新点一 | 列 1 构造 | E14, E19, E30 | source-explicit | proposed |
| 科学问题（2）+ 研究内容（2）+ 创新点二 | 列 2 关系 | E15, E19, E30 | source-explicit | proposed |
| 科学问题（3）+ 研究内容（3）+ 创新点三 | 列 3 质量 | E16, E19, E30 | source-explicit | proposed |
| 对照提示：无知识 / 单一知识 / 联合知识 | 列 1 可证伪 | E12, E14, E21 | source-explicit | proposed |
| 对照提示：无专业属性 / 无来源位置 | 列 2 可证伪 | E12, E15, E27 | source-explicit | proposed |
| 对照提示：单层质量 vs 四层联合 | 列 3 可证伪 | E12, E16, E27 | source-explicit | proposed |
| 输出：可追溯资源单元 / 资源包 / 本地原型 | 右端产物形态 | E02, E31 | source-explicit | expected |
| 底栏：只评价能否入包，不评价学习效果 | 范围 | E16, E19 | source-explicit | proposed |

**禁止入图**：五阶段操作步骤、公式展开、B0–B3 全名矩阵、音频模态、任何已测曲线或百分比、把 300/120 画成已完成库存。

---

### F3

| 字段 | 内容 |
|---|---|
| `figure_id` | F3 |
| `proposed_title` | 面向可追溯资源单元的五阶段技术路线与独立验证闭环 |
| `target_section` | （一）3.2 技术路线与实验手段段末（约 p.9） |
| `reviewer_question` | 两年实施路径中，材料如何入池、关系如何写入、错误如何退回，以及独立验证如何避免自评分？ |
| `figure_type` | Overall Framework |
| `figure_form` | technical route → Overall Framework |
| `priority` | must |
| `source_evidence` | E20, E26, E27, E28, E29, E16 |
| `core_message` | 路线是带判定分流的闭环：不合规材料不入池，证据不全入人工核验，严重错误退回修改，自动门控只作筛查。 |
| `existing_asset_relation` | redraw（A3/A4 第 2 阶段标签与 E26 冲突，禁止 reuse） |
| `proposed_render_action` | draw_new |
| `data_requirement` | 阶段与分流标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | 五阶段（E26）与式 (1) 叙事五段（E20）用词不完全同一套；图内**强制采用 §3.2 的五阶段名称** |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 阶段 1 材料审查 | 主流程 | E26 | source-explicit | proposed |
| 阶段 2 知识结构与单元切分 | 主流程 | E26 | source-explicit | proposed |
| 阶段 3 跨模态关联 | 主流程 | E26 | source-explicit | proposed |
| 阶段 4 四层门控 | 主流程 | E26 | source-explicit | proposed |
| 阶段 5 独立验证 | 主流程 | E26 | source-explicit | proposed |
| 判定：未通过审查 → 不入池 | 分流 | E26 | source-explicit | proposed |
| 判定：属性或证据不全 → 人工核验 | 分流 | E26 | source-explicit | proposed |
| 判定：严重错误 → 退回修改 | 反馈虚线 | E26 | source-explicit | proposed |
| 核心模态实线 / 扩展模态虚线 | 输入约束 | E13, E26 | source-explicit | proposed |
| 对照胶囊：B0 人工 / B1 通用大模型 / B2 文本 RAG / B3 完整方法 | 验证设计（压缩，不作全矩阵） | E27 | source-explicit | proposed |
| 独立验证：专家盲评、跨来源留出、人工修订记录 | 阶段 5 内容 | E16, E26 | source-explicit | proposed |
| 评分隐藏方法条件 / 评分者不参与规则设计 | 效度约束 | E27 | source-explicit | proposed |
| 降级：自动初筛—专家复核 | 风险路径 | E29 | source-explicit | proposed |

**禁止入图**：把第 2 阶段标成「联合约束」；把 F2 的三列科学问题地图原样复制为另一条流水线；绘制神经网络层栈；填写任何实测指标。

---

### F4

| 字段 | 内容 |
|---|---|
| `figure_id` | F4 |
| `proposed_title` | 对照、消融与分层指标的可证伪实验设计 |
| `target_section` | （一）3.2 与 F3 同节，置于 F3 之后；**默认建议改为正文三线表** |
| `reviewer_question` | 如何用对照和消融分别证伪三项科学问题，而不是只比较“有系统/无系统”？ |
| `figure_type` | Comparison / Ablation |
| `figure_form` | design comparison / condition matrix → Comparison / Ablation |
| `priority` | strong |
| `source_evidence` | E12, E21, E27, E28, E18, E25 |
| `core_message` | 构建、关联、质量三层使用不同对照轴和指标；阈值在开发集冻结，测试集不再改。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | no_figure（图形适配：矩阵更适合三线表；若审核坚持绘图则改为 draw_new） |
| `data_requirement` | 条件与指标名称；`available`。**无实测数值** |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | 验收阈值数值未给出（E18/E25：预实验后冻结）→ 图内不放阈值数字 |

**must_show**（若改表或绘图，内容相同）

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 行：B0 / B1 / B2 / B3 | 方法对照 | E12, E27 | source-explicit | proposed |
| 行：无知识 / 仅产业 / 仅课程 / 联合知识 | 科学问题（1）消融 | E12, E14, E21 | source-explicit | proposed |
| 行：去专业属性 / 去来源位置 | 科学问题（2）消融 | E12, E27 | source-explicit | proposed |
| 行：单层质量 / 四层联合 | 科学问题（3）消融 | E12, E27 | source-explicit | proposed |
| 列：边界 F1、覆盖、重复、属性错误 | 构建层指标 | E28 | source-explicit | expected |
| 列：Recall@1、Recall@5、MRR、关系 F1、来源定位、错配率 | 关联层指标 | E17, E28 | source-explicit | expected |
| 列：VRR、检出/误报、五维盲评、Krippendorff's alpha、修订时间 | 质量层指标 | E18, E25, E28 | source-explicit | expected |
| 标记：测试集指标冻结 / 无填入数值 | 防伪结果 | E18, E25 | source-explicit | proposed |
| Ours 高亮：B3 完整方法 | 比较强调 | E27 | source-explicit | proposed |

**禁止入图**：虚构柱高、热图、显著性星号、样本量单元格中的 300/120 作为已完成 N。空单元格必须保持为空。

**图形适配说明**：F3 已压缩展示 B0–B3 胶囊。完整条件×指标矩阵在 21 页标书中用三线表更省篇幅、更不易被误读为已有结果。阶段二应裁决 `no_figure` 或降为 nice。

---

### F5

| 字段 | 内容 |
|---|---|
| `figure_id` | F5 |
| `proposed_title` | 专业属性与来源位置约束的跨模态关系判定 |
| `target_section` | （一）3.1 跨模态关联段（式 (4)–(5) 附近，约 p.8） |
| `reviewer_question` | 专业属性与来源位置如何把“语义相似”改写成可写入资源单元的关系？ |
| `figure_type` | Module Detail |
| `figure_form` | mechanism / key method → Module Detail |
| `priority` | nice |
| `source_evidence` | E08, E15, E23, E24 |
| `core_message` | 候选关系必须同时满足语义、专业条件和证据位置，才能写入资源单元。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 机制标签与式 (5) 符号；`available` |
| `aspect_ratio` | 4:3 |
| `style_family` | classic_academic |
| `unknowns` | \(\eta\) 权重仅称开发集确定，图内不放具体数值；对比学习只作为基础表示，不展开网络层 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 左：文本 / 设备图 / 运行曲线（代码虚线） | 多模态输入 | E15, E13 | source-explicit | proposed |
| 提取：对象、变量、单位、工况、时间窗口、来源位置 | 属性 | E15 | source-explicit | proposed |
| 基础表示：对比学习（只标“基础表示”，不画层栈） | 前置 | E23 | source-explicit | proposed |
| 四项检查：sim / \(C_A\) / \(C_E\) / \(C_R\) | 核心机制 | E24 | source-explicit | proposed |
| 关系类型：解释、实例、计算/实验、对照、出处支持 | \(C_R\) 内容 | E15 | source-explicit | proposed |
| 困难负例：变量/单位/工况/时序错配、来源不可核查 | 可证伪 | E15 | source-explicit | proposed |
| 写入规则：达阈值且来源完整才写入 | 决策 | E24 | source-explicit | proposed |
| 失败：专业条件错配 / 来源不可核查 | 拒绝分支 | E15, E19 | source-explicit | proposed |

**caption_reserve（不进图）**：式 (4) 完整公式、\(\tau\)、批大小 \(B\)、\(\eta\) 数值、网络维度。

---

### F6

| 字段 | 内容 |
|---|---|
| `figure_id` | F6 |
| `proposed_title` | 两年两阶段研究计划与阶段性验收 |
| `target_section` | （一）5.1 年度研究计划（约 p.11） |
| `reviewer_question` | 两年内先冻结什么、后验证什么，阶段性验收如何与三项科学问题对齐？ |
| `figure_type` | Overall Framework |
| `figure_form` | timeline → Overall Framework |
| `priority` | nice |
| `source_evidence` | E31, E13, E29 |
| `core_message` | 前 12 月完成合规、结构、基线与指标冻结；后 12 月完成对照、消融、盲评与资源包，未达标单元不入包。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | no_figure |
| `data_requirement` | 阶段标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | 具体时间节点以立项通知书为准（E31） |

**图形适配**：两年两阶段用正文或三线表更省篇幅；§5.1 已按月份写清验收口径。本轮建议不绘图。

---

## 优先级排序

| 优先级 | 图 | 评审价值 | v1 建议动作 |
|---|---|---|---|
| must | F1 | 让评审在参考文献前看清“为什么现有方法不够” | draw_new |
| must | F2 | 让三项问题/内容/创新对位，避免被读成系统集成 | draw_new |
| must | F3 | 让实施路径、分流和独立验证可见 | draw_new |
| strong | F4 | 可证伪矩阵；与 F3 胶囊重复风险 | no_figure（改三线表） |
| nice | F5 | 放大式 (5)；公式已在正文 | draw_new |
| nice | F6 | 两年计划正文已清楚 | no_figure |

**不进入计划（unsupported 或无证据）**

| 想法 | 原因 |
|---|---|
| 神经网络架构图 / Transformer 层栈 | 式 (4) 仅为对比学习基础表示，不是贡献模块；硬改写成 Network Architecture 属于 unsupported |
| Data Behavior：VRR 柱、Recall 曲线、消融热图 | 申报书无已测数值；`data_requirement: absent` |
| 学生学习效果 / 平台架构 / 推荐系统 | 明确排除（E02） |
| 研究基础成果墙、GPU 清单图 | 更适合文字；装饰性 |
| 音频模态 | PDF 未列音频；本地草稿若出现音频图标视为虚构 |

---

## 分章节图数与作用

| 章节 | 图 | 作用 |
|---|---|---|
| 立项依据 1.3–1.4 | F1 ×1 | 缺口来源 |
| 内容/目标/问题 2.3 | F2 ×1 | 问题—内容—创新闭环 |
| 方案 3.1 | F5 ×1（nice） | 机制放大 |
| 方案 3.2 | F3 ×1；F4 改表 | 路线闭环；对照矩阵用表 |
| 年度计划 5.1 | F6 不绘图 | 正文已清楚 |
| 创新 / 基础 / 工作条件 | 0 | 正文已对位，不再重复 |

---

## 总图数、页面成本与可删减顺序

- v1 建议**绘制**集合：4（F1/F2/F3 must + F5 nice）
- v1 建议**改表/不画**：F4、F6
- 对 21 页开放课题正文：优先落地 **F1+F2+F3**（约 1.6–2.0 页）
- 预计页面成本：F1 0.55 页；F2 0.55 页；F3 0.60 页；F5 0.40 页；合计约 2.1 页（含 nice）或 1.7 页（仅 must）
- **可删减顺序**：F6（已 no_figure）→ F5 → F4（已建议改表）→ 不得删 F1/F2/F3
- 若第（一）部分已接近篇幅上限：只保留 must 三图

---

## completeness

```yaml
completeness:
  analyzed_materials:
    - /home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_Education/main.pdf (p.1-21, text layer)
    - page rasters p.1, p.8, p.9, p.11 (visual check only)
    - extraTex/1.1.立项依据.tex, extraTex/1.2.内容目标问题.tex, extraTex/1.3.方案及可行性.tex, extraTex/1.4.特色与创新.tex, extraTex/1.5.研究计划.tex
    - figures/*.png (local drafts, not in PDF)
    - docs/00_项目基本信息.md (title only; not used as scientific evidence)
  output_type: complete
  high_confidence_information:
    - PDF 无现有插图
    - 本地草稿存在且部分标签与 §3.2 冲突，必须 redraw 而非 reuse
    - 三项科学问题 / 三项研究内容 / 三项创新
    - 五阶段技术路线名称以 §3.2 为准
    - B0-B3 对照与资源单元 u=(c,a,m,e,s)
    - 明确排除学生数据与生产平台
  pending_confirmation:
    - PDF 正文未印中文题目（E36）
    - 验收阈值具体数值（E18/E25：预实验后冻结）
    - 式 (4) 是否在图中出现（规划为 caption_reserve）
    - F4 最终用图还是三线表（v1 建议表）
  suggested_materials:
    - 若需 Data Behavior 图：提供开发集预实验真实数值后再规划
    - 申请表封面题目的最终打印稿，用于图题统一
```
