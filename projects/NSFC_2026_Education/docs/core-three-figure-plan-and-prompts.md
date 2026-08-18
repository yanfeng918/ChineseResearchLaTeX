# 三张核心配图：Figure Plan · Palette Decision · Academic Figure Prompt

> 分析对象：`main.pdf`（与 `extraTex/1.1–1.5.tex` 一致）
> 日期：2026-08-14
> 本轮**不生图**。只交付配图规划、跨图视觉逻辑、JSON spec 与英文 image prompt。
> 旧图稿（`figures/research_background_v2.png` 等）仅作反面教材：背景图漏方法、框架图画成流水线。本包按职责重拆。

---

## 一、Figure Plan

### 1. 项目概览

- **题目**：产业—课程知识联合约束下高校新能源多模态教学资源构建与质量验证研究
- **场景**：“新能源数据分析与功率预测”示范课程模块（4 个知识模块）
- **对象**：资源单元 \(u=(c,a,m,e,s)\)
  - \(c\) 课程知识/能力目标；\(a\) 专业属性；\(m\) 多模态片段及关系；\(e\) 来源位置；\(s\) 质量状态
- **核心模态**：课程文本、运行曲线/图表、设备图/结构图
- **扩展模态**：实验代码、产业案例（虚线框；许可/格式/解析满足时才纳入，不作为方法成立前提）
- **三项机制（贡献）**：
  1. 产业任务—课程知识联合约束（构造）
  2. 专业属性与来源证据约束的跨模态关联（关系）
  3. 内容—课程—模态—证据四层内在质量验证（质量）
- **验证**：B0–B3 对照、逐项消融、跨来源留出、独立专家盲评、人工修订记录
- **边界**：只评价资源能否入包；不涉及学生数据、个性化推荐、学习效果或生产平台接入
- **结果状态**：申报书，无已完成实验数值；图中不得暗示既有正结果

### 2. 章节结构与配图映射

| 申报书部分 | 状态 | 配图职责 |
|---|---|---|
| 1.1–1.4 立项依据 | 完整 | Fig. 1 研究背景：双重语境、汇集失败、三类缺口、科学切入 |
| 2.1–2.3 内容/目标/科学问题 | 完整 | Fig. 2 总体框架：对象、三问题递进、验证证据、成果形态 |
| 3.1–3.3 方法/路线/可行性 | 完整 | Fig. 3 技术路线：五阶段、判定分流、反馈、对照与交付 |
| 4 特色与创新 | 完整 | 不单独立图；机制已由 Fig. 2 承载 |
| 5 计划与预期 | 完整 | 不单独立图；交付物由 Fig. 2 右端 / Fig. 3 末端承载 |
| 实验结果 | 不适用 | 无曲线/消融图；指标只作标签，不作已测数值 |

### 3. 总体策略：三图不得同构

三张图回答三个不同问题，禁止画成三版流程图。

| 图号 | 中文图名 | 唯一叙事 | 优先级 | 建议放置 | 图型 | 画幅 |
|---|---|---|---|---|---|---|
| Fig. 1 | 高校新能源多模态教学资源的双重语境、汇集失败与科学切入 | **为什么必须做**：缺口从何而来 | Must | 1.4 切入点之后、参考文献前 | Motivation / Problem-Gap | 16:9 |
| Fig. 2 | 资源单元构造、内部关系与内在质量的递进研究框架 | **研究什么**：问题—机制—证据对应 | Must | 2.3 科学问题之后、第 3 节之前 | Overall Research Framework | 16:9 |
| Fig. 3 | 面向可追溯资源单元的五阶段技术路线与独立验证闭环 | **怎样实施**：步骤、分流、对照、交付 | Must | 3.2 技术路线末、3.3 之前 | Closed-Loop Technical Route | 16:9 |

- 推荐总数：**3**（用户指定核心三图；篇幅上不再加 must 级图）
- 阅读顺序：缺口来源 → 科学对象与机制 → 操作闭环
- `module_count_framework`：**5**（技术路线主阶段；框架图内部为 3 个递进模块）
- palette hint：classic academic（正式申报书，不用 pastel）
- venue：None（开放课题/NSFC 式申请书，非会议期刊）
- domain：新能源工程教育 × 多模态资源构建 × 教育资源质量验证

Strong/Nice（本轮不画，仅备案）：模块细节图（式 2–8）、B0–B3 对照示意、错误类型示意。实验结果图待有数据后再规划。

### 4. Fig. 1 研究背景图

**目的。** 只回答：现有材料为何无法直接重组为可教学资源，以及三项科学问题从哪里产生。不展开方法、公式、基线或五阶段流程。

**布局。** 横向四段因果 + 底栏研究边界：

1. **双重语境与分散资源**
   - 产业任务：设备 · 工况 · 参数
   - 课程教学：知识点 · 能力目标 · 先修
   - 核心资源：文本 / 运行图表 / 设备图
   - 扩展资源：代码/案例（虚线 +「扩展模态」）
2. **现有汇集假设**
   - 中央漏斗：「主题/相似度汇集」
   - 输出：「自动重组」
   - 不把任一具体模型画成已被证伪
3. **三类科学缺口**
   - 单元边界不清（粒度、术语异名、属性冲突）
   - 专业条件错配（变量、单位、工况、时序）
   - 来源证据失联（出处不可定位或不支撑断言）
   - 汇总判断：**可检索 ≠ 可教学使用**
4. **科学切入（问题来源，不是方法展开）**
   - 联合知识约束 → 边界与覆盖
   - 证据约束关联 → 关系正确性
   - 四层质量验证 → 独立效度
   - 目标锚点：五字段资源单元卡
5. **底栏**：仅评价资源内在质量 · 不涉及学生数据、推荐或学习效果

**必须出现的视觉元素**

- 风机/光伏板细线图标 + 课程文档图标（双重语境，非对立色）
- 文档、折线、设备结构缩略、代码括号（多模态；代码虚线）
- 匹配漏斗（主题/相似度汇集）
- 三张断裂配对线缺口卡（无警告 emoji）
- 三张编号切入卡 + 五字段资源单元卡

**图内短标签**

产业任务；课程教学；分散资源；主题/相似度汇集；单元边界不清；专业条件错配；来源证据失联；可检索 ≠ 可教学使用；联合知识约束；证据约束关联；四层质量验证。

**图注保留**：\(u=(c,a,m,e,s)\) 完整定义；「语义相关—条件相容—证据可查」三层关系；扩展模态条件；研究边界。

**禁止**：AI 大脑/云平台/推荐系统；B0–B3/公式/五阶段；把资源质量画成学习效果；产业与课程用对立色。

**证据页**：PDF 立项依据 1.1–1.4（双重约束、相似度汇集失败、三层关系、四层质量、三条不足与切入）。

### 5. Fig. 2 总体研究框架图

**目的。** 回答研究对象是什么、三问题如何递进、每项机制由什么证据检验。这是概念框架，不是软件架构，也不是操作流程。

**布局。** 左输入 + 中央对象与三模块 + 上问题 + 下验证底座 + 右成果：

1. **左：受控输入** — \(\mathcal{D}\)；\(\mathcal{K}_p\)；\(\mathcal{K}_c\)；三类核心模态 + 虚线扩展模态
2. **中上：核心对象** — 资源单元 \(u=(c,a,m,e,s)\) 五字段卡
3. **中：三递进模块（等宽）**
   - ① 构造层：联合知识约束 · H1 · 边界 F1 / 覆盖 / 属性错误
   - ② 关系层：专业属性 + 来源证据 · H2 · Recall@K / MRR / 来源定位
   - ③ 质量层：四层联合验证 · H3 · VRR / 盲评 / 留出
4. **模块上方问题卡**（各 ≤8 字）
   - 联合约束何时有效
   - 属性与出处如何约束
   - 内在质量如何获独立效度
5. **下：共同验证底座** — 同材料/同划分/同人工预算；B0–B3；逐项消融；跨来源留出；专家盲评
6. **右：结果与成果** — 增量作用 · 适用边界/负结果；资源包 · 质量报告 · 本地原型
7. **底注条**：评价入包，不评价学习效果

**必须出现**：Kp/Kc 双节点；五槽单元卡；三张机制卡（双知识映射 / 跨模态匹配 / 四门控条）；每卡上问题、下观测；对照矩阵细线图标；资源包/报告/离线电脑图标。

**禁止**：材料审查、待核验、退回修改等操作步骤；完整公式；三项创新画成互不关联技术堆；上升曲线/奖杯暗示已有正结果。

**证据页**：PDF 2.1–2.3、4.1–4.4、5.2。

### 6. Fig. 3 技术路线图

**目的。** 回答怎样做、何处分流、如何对照并形成可复核结论。背景图和框架图不再重复这些操作细节。

**布局。** 五阶段左→右主流程 + 判定菱形 + 虚线反馈 + 底部实验控制：

1. **① 材料审查** — 公开许可 / 授权 / 自建；来源·许可·脱敏；菱形「合规入池？」；否 → 不入池
2. **② 知识建模** — 任务—对象—条件；知识点—目标—先修；候选切分；粒度/术语/属性冲突入记录
3. **③ 证据关联** — 文本/图表/设备图（实线）+ 代码/案例（虚线）；对象·变量·单位·工况·时序·出处；语义+条件+证据；不全 → 待核验
4. **④ 四层门控** — 内容 / 课程 / 模态 / 证据 2×2；仅作筛查；不通过 → 退回修改（虚线回 ②/③）
5. **⑤ 独立验证** — 开发集定参、测试集冻结；B0–B3、消融、留出、盲评；通过 → 资源包/质量报告/本地原型；机制不支持 → 边界/负结果或「初筛+复核」
6. **底栏实验控制** — 同材料·同划分·同预算；近重复不跨集合；构建层 / 关联层 / 质量层指标标签（无数值）

**必须出现**：审查清单；Kp/Kc 网络；多模态匹配；四道门控条；三个判定菱形；B0–B3 对照条；不入池 / 待核验 / 退回修改三条虚线支路。

**禁止**：把门控画成最终自动验收；从冻结测试回流调参；把代码/案例画成方法成立前提；把 VRR 画成学习效果。

**证据页**：PDF 3.1–3.3。

### 7. 优先级与完整性

| 优先级 | 图 | 理由 |
|---|---|---|
| Must | Fig. 1, 2, 3 | 用户指定；分别覆盖立项、科学问题、实施方案 |
| Strong（本轮不画） | 模块细节 / 对照示意 | 公式与 B0–B3 已由正文承载 |
| Nice（本轮不画） | 错误类型示意 | 有助于审稿理解，但非申报必需 |

**完整性块**

- 已分析材料：`main.pdf` 全文（立项依据至年度计划）；`extraTex/1.1–1.5.tex` 核验公式与术语；旧图稿仅作反面对照
- 当前输出类型：完整（三图规划 + 配色决策 + JSON spec + image prompt）
- 高置信信息：研究对象、三项机制、核心/扩展模态、五阶段路线、对照消融、独立验证、研究边界
- 待确认信息：最终图宽（建议 `0.85\linewidth`）、图号、图注是否写入拟建规模（4 模块 / ≥300 单元 / 120 盲评）、生图模型
- 建议补充材料：生图前若有偏好参考图可只补一张；无参考图可按本包直接生图

---

## 二、Palette Decision（跨三图统一）

### 决策清单

1. **风格族**：classic academic → `academic-figure-prompt`（白底 + 彩色边框；正式申报书，不用 pastel）
2. **硬约束**：色盲友好（默认）；Fig. 3 为 5 阶段 ≥4 模块 → 单色系
3. **图型**：Overall Framework (≥4) → Nature Blue；Motivation 与 Technical Route 共用同一套，避免三图换色
4. **venue / domain**：venue = None；domain = 工程教育 × 多模态系统
5. **主色板 / 备选**：Nature Blue / Okabe-Ito
6. **hex 来源**：`palettes.md` §12 Nature Blue + 语义合同中的稀疏强调色
7. **分支**：`scene`（classic + ≥4 模块 + 克制工程风）

### 主色板

| 角色 | hex | 用途 |
|---|---|---|
| primary | `#1B3A5C` | 深海军蓝：输入、主容器 |
| secondary | `#2E6B9E` | 中蓝：知识/方法模块 |
| tertiary | `#5BA0D0` | 浅蓝：关联/输出结构 |
| gray | `#8EAEC4` | 浅灰蓝：分组底纹 |
| accent-coral | `#D95F02` | 珊瑚橙：缺口/拒绝/错配（稀疏） |
| accent-emerald | `#1B9E77` | 翡翠绿：通过/成果（稀疏） |
| frozen | `#616161` | 石板灰：待核验/基线/扩展模态 |
| text | `#333333` | 文字 |
| fill | `#FFFFFF` | 画布与盒体填充 |
| section_bg | `#F7F7F7` | 区域底纹 |
| border | `#CCCCCC` | 普通边框 |
| arrow | `#4D4D4D` | 主流程实线箭头 |

**备选 Okabe-Ito**：`#0072B2` / `#E69F00` / `#009E73`。仅当某一图必须做强多类对比时启用，仍 ≤3 色相。

### 语义绑定（三图一致）

| 功能角色 | hex | 本申报书含义 |
|---|---|---|
| Input / Data | `#1B3A5C` | 原始资源、模态缩略 |
| Backbone / Knowledge | `#2E6B9E` | Kp、Kc、构造/方法模块 |
| Association | `#5BA0D0` | 跨模态关联、关系层 |
| Loss / Gate / Reject | `#D95F02` | 缺口、门控拒绝、退回 |
| Output / Pass | `#1B9E77` | 入包、成果、通过 |
| Frozen / Pending | `#616161` | 待核验、B0–B2、扩展模态虚线 |

产业知识与课程知识**同属 Backbone**（`#2E6B9E`），用图标/标签区分，不用冷暖对立色。

### 可访问性

- 类别双重编码：颜色 + 线型（实/虚）+ 编号 + 短标签
- 珊瑚/翡翠只出现在判定与成果，不给每个盒子换色
- 文字 `#333333` on `#FFFFFF` ≥ 4.5:1；灰度打印靠深浅与虚实仍可分
- 无渐变、无 3D、无彩色图标、无 emoji

### Handoff（供 prompt 技能）

```
palette: Nature Blue
style_family: classic
primary / secondary / tertiary: #1B3A5C / #2E6B9E / #5BA0D0
accent_reject / accent_pass / frozen: #D95F02 / #1B9E77 / #616161
text / fill / section_bg / border / arrow: #333333 / #FFFFFF / #F7F7F7 / #CCCCCC / #4D4D4D
reason: NSFC-style proposal, ≥4-module framework, colorblind-safe monochrome + sparse pass/fail
accessibility: colorblind-safe; dual-encode; print-friendly
```

---

## 三、Fig. 1 研究背景图 — Figure Spec Package

**中文图名**：高校新能源多模态教学资源的双重语境、汇集失败与科学切入
**类型**：Motivation / Problem-Gap Framework
**palette**：Nature Blue（scene 分支）
**aspect_ratio**：16:9

### JSON spec

```json
{
  "diagram_type": "Motivation / Problem-Gap Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column / NSFC text width)",
    "font_family": "Noto Sans SC / Source Han Sans for Chinese; Arial, Helvetica for Latin",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt italic"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head",
      "feedback_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Col1_Context": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "Col2_Aggregation": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "Col3_Gaps": "Coral (#D95F02) 1.5pt solid border, white fill",
      "Col4_Entry": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "Extended_Modality": "Slate Gray (#616161) 1.5pt dashed border, white fill",
      "Unit_Card": "Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "Boundary_Bar": "section_bg #F7F7F7, 1.0pt #CCCCCC border"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "broken_mismatch": "Coral (#D95F02) dashed broken pairing lines"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left, Column 1",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt border, white fill, 6px radius",
      "exact_title_to_render_inside": "① 双重语境",
      "icon": "small wind-turbine and photovoltaic-panel line icons beside a document icon, monochrome",
      "internal_content": {
        "layout": "Two stacked knowledge cards plus a resource row",
        "row_1": {
          "exact_label": "产业任务",
          "exact_text": "设备 · 工况 · 参数",
          "icon": "small gear-and-plant line icon"
        },
        "row_2": {
          "exact_label": "课程教学",
          "exact_text": "知识点 · 目标 · 先修",
          "icon": "small open-book line icon"
        },
        "row_3": {
          "exact_label": "分散资源",
          "exact_text": "文本  图表  设备图",
          "icon": "document, polyline chart, and device-frame thumbnails, monochrome"
        },
        "row_4": {
          "shape": "dashed #616161",
          "exact_label": "扩展模态",
          "exact_text": "代码 / 案例",
          "icon": "small code-bracket line icon"
        }
      },
      "flow": "Solid dark-grey arrow RIGHT to Column 2",
      "caption_note": "Industry knowledge and course knowledge are joint constraint sources, not opposing camps."
    },
    {
      "relative_position": "Center-Left, Column 2",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "② 现有汇集",
      "icon": "small funnel / matching-filter line icon, monochrome",
      "internal_content": {
        "layout": "Vertical funnel",
        "row_1": {"exact_text": "主题 / 相似度"},
        "row_2": {"exact_label": "自动重组"}
      },
      "secondary_note": "非特定模型",
      "flow": "Solid dark-grey arrow RIGHT to Column 3"
    },
    {
      "relative_position": "Center-Right, Column 3",
      "shape": "Rounded rectangle, #D95F02 1.5pt border, white fill",
      "exact_title_to_render_inside": "③ 三类缺口",
      "icon": "three small cards with broken pairing lines, monochrome coral stroke",
      "internal_content": {
        "layout": "Three stacked gap cards plus a summary bar",
        "row_1": {"exact_label": "单元边界不清", "exact_text": "粒度 · 异名 · 冲突"},
        "row_2": {"exact_label": "专业条件错配", "exact_text": "变量 · 单位 · 工况"},
        "row_3": {"exact_label": "来源证据失联", "exact_text": "出处不可核查"},
        "row_4": {"exact_text": "可检索 ≠ 可教学使用"}
      },
      "flow": "Solid dark-grey arrow RIGHT to Column 4"
    },
    {
      "relative_position": "Far Right, Column 4",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "④ 科学切入",
      "icon": "three numbered entry cards plus a five-slot unit card",
      "internal_content": {
        "layout": "Three numbered rows then unit card",
        "row_1": {"exact_text": "联合知识约束", "secondary_note": "边界与覆盖"},
        "row_2": {"exact_text": "证据约束关联", "secondary_note": "关系正确性"},
        "row_3": {"exact_text": "四层质量验证", "secondary_note": "独立效度"},
        "row_4": {
          "exact_label": "资源单元",
          "exact_text": "u = (c, a, m, e, s)",
          "secondary_note": "五字段"
        }
      }
    },
    {
      "relative_position": "Bottom full-width bar",
      "shape": "Shallow bar, #F7F7F7 fill, #CCCCCC 1.0pt border",
      "exact_text": "仅评价资源内在质量  ·  不涉及学生数据、推荐或学习效果",
      "icon": "small prohibition-slash over a student/click-log icon, thin grey line art"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, notes 7-8pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin line art in the block border color or #4D4D4D. No colored icons.",
    "Extended modality MUST use dashed #616161 border and the pill 扩展模态.",
    "Industry and course cards share #2E6B9E / #1B3A5C family; do NOT use opposing warm/cool camps.",
    "NO emojis, NO lock/fire/lightning icons, NO warning triangles as decoration, NO 3D rendering.",
    "NO AI brain, cloud platform, recommender, classroom, or learning-analytics icons.",
    "NO B0-B3, formulas, five-stage pipeline, or rising KPI curves.",
    "Flat vector: no gradients, no drop shadows, no decorative chrome. Canvas pure white."
  ]
}
```

### Image prompt（约 320 词）

Flat vector academic architecture diagram showing a four-column causal motivation figure for university new-energy multimodal teaching resources, on a pure white #FFFFFF canvas, 16:9.

The figure explains why theme-or-similarity aggregation of scattered course materials fails to produce teachable resource units, and where three scientific questions originate. Horizontal left-to-right flow with four equal-width rounded columns connected by solid dark-grey #4D4D4D arrows; a shallow full-width boundary bar sits under all columns.

Far left, column titled "① 双重语境": two stacked white cards with navy #1B3A5C borders — "产业任务" with a small wind-turbine and photovoltaic line icon and the note "设备 · 工况 · 参数"; "课程教学" with an open-book icon and "知识点 · 目标 · 先修". Below them a resource row labeled "分散资源" with tiny document, polyline-chart, and device-frame thumbnails; a dashed slate-grey #616161 card marked "扩展模态" shows a code-bracket icon and "代码 / 案例".

Center-left, column "② 现有汇集": a funnel icon above the labels "主题 / 相似度" and "自动重组", with a small grey note "非特定模型". Center-right, column "③ 三类缺口" uses coral #D95F02 borders and three stacked cards with broken pairing lines: "单元边界不清", "专业条件错配", "来源证据失联"; a summary strip reads "可检索 ≠ 可教学使用". Far right, column "④ 科学切入" uses medium-blue #2E6B9E borders and three numbered rows — "联合知识约束", "证据约束关联", "四层质量验证" — plus a light-blue #5BA0D0 five-slot card "资源单元" with "u = (c, a, m, e, s)". Bottom bar on #F7F7F7: "仅评价资源内在质量  ·  不涉及学生数据、推荐或学习效果".

Nature Blue palette with sparse coral only on the gap column. White fills, 1.5pt colored borders, 6px corner radius, 1.0pt internal dividers. Monochrome line-art icons, no filled color icons. Clean sans-serif: Chinese in Source Han Sans, Latin in Helvetica; titles 10–12pt bold, labels 8–9pt, notes 7pt grey. No gradients, shadows, 3D, emojis, AI-brain, cloud, or recommender imagery. Parameters and full field definitions stay in the caption, not rendered. Aspect ratio 16:9.

### Caption reserve

- \(u=(c,a,m,e,s)\) 字段定义
- 关系成立的三层：语义相关、条件相容、证据可查
- 代码/案例为扩展模态
- 不涉及学生数据、推荐、学习效果、生产平台

---

## 四、Fig. 2 总体研究框架图 — Figure Spec Package

**中文图名**：资源单元构造、内部关系与内在质量的递进研究框架
**类型**：Overall Research Framework
**palette**：Nature Blue
**aspect_ratio**：16:9

### JSON spec

```json
{
  "diagram_type": "Overall Research Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column / NSFC text width)",
    "font_family": "Noto Sans SC / Source Han Sans for Chinese; Arial, Helvetica for Latin",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt italic"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head",
      "feedback_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Input": "Dark Navy (#1B3A5C) 1.5pt solid, white fill",
      "UnitObject": "Dark Navy (#1B3A5C) 2pt solid, white fill",
      "Module1_Construct": "Medium Blue (#2E6B9E) 1.5pt solid, white fill",
      "Module2_Relation": "Light Blue (#5BA0D0) 1.5pt solid, white fill",
      "Module3_Quality": "Medium Blue (#2E6B9E) 1.5pt solid, white fill",
      "ValidationBase": "section_bg #F7F7F7, #CCCCCC 1.0pt",
      "Output": "Emerald (#1B9E77) 1.5pt solid, white fill",
      "Extended": "Slate Gray (#616161) 1.5pt dashed, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "shared_support": "Dark Grey (#4D4D4D) 1.0pt solid thin connectors downward to validation base"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left column",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt, white fill",
      "exact_title_to_render_inside": "受控输入",
      "icon": "document, polyline, and device-frame thumbnails stacked, monochrome",
      "internal_content": {
        "layout": "Vertical stack",
        "row_1": {"exact_text": "D 原始资源"},
        "row_2": {"exact_text": "Kp 产业知识", "icon": "small node-link graph"},
        "row_3": {"exact_text": "Kc 课程知识", "icon": "small node-link graph"},
        "row_4": {"exact_label": "核心模态", "exact_text": "文本  图表  设备图"},
        "row_5": {"shape": "dashed #616161", "exact_label": "扩展模态", "exact_text": "代码 / 案例"}
      },
      "flow": "Solid arrow RIGHT to resource-unit card"
    },
    {
      "relative_position": "Upper center",
      "shape": "Rounded rectangle, #1B3A5C 2pt, white fill",
      "exact_title_to_render_inside": "资源单元",
      "exact_text": "u = (c, a, m, e, s)",
      "icon": "five small labeled slots in a row, monochrome",
      "internal_content": {
        "layout": "Five equal pills",
        "row_1": {"exact_text": "c 知识   a 属性   m 片段   e 出处   s 状态"}
      },
      "flow": "Solid arrow DOWN into three equal modules"
    },
    {
      "relative_position": "Center row, left module",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt, white fill",
      "exact_title_to_render_inside": "① 构造层",
      "icon": "two nodes Kp and Kc connected by a line, monochrome",
      "internal_content": {
        "row_1": {"exact_label": "联合知识约束"},
        "row_2": {"exact_text": "联合约束何时有效"},
        "row_3": {"exact_text": "无知识 / 仅Kp / 仅Kc / 联合"},
        "row_4": {"exact_text": "边界F1 · 覆盖 · 属性"}
      },
      "flow": "Solid arrow RIGHT to Module 2"
    },
    {
      "relative_position": "Center row, middle module",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt, white fill",
      "exact_title_to_render_inside": "② 关系层",
      "icon": "small cross-modal matching icon: two rows of dots with selective links, plus a broken mismatch line",
      "internal_content": {
        "row_1": {"exact_label": "属性 + 来源证据"},
        "row_2": {"exact_text": "属性与出处如何约束"},
        "row_3": {"exact_text": "语义 · 属性 · 出处"},
        "row_4": {"exact_text": "Recall@K · MRR · 定位"}
      },
      "flow": "Solid arrow RIGHT to Module 3"
    },
    {
      "relative_position": "Center row, right module",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt, white fill",
      "exact_title_to_render_inside": "③ 质量层",
      "icon": "2x2 gate bars labeled as four cells, monochrome",
      "internal_content": {
        "row_1": {"exact_label": "四层联合验证"},
        "row_2": {"exact_text": "内在质量独立效度"},
        "row_3": {"exact_text": "内容  课程  模态  证据"},
        "row_4": {"exact_text": "VRR · 盲评 · 留出"}
      },
      "flow": "Solid arrow RIGHT to output column"
    },
    {
      "relative_position": "Right column",
      "shape": "Rounded rectangle, #1B9E77 1.5pt, white fill",
      "exact_title_to_render_inside": "预期成果",
      "icon": "resource-pack box, report document, and desktop-monitor line icons",
      "internal_content": {
        "row_1": {"exact_text": "资源包 · 质量报告"},
        "row_2": {"exact_text": "本地原型"},
        "row_3": {"exact_text": "增量作用"},
        "row_4": {"exact_text": "适用边界 / 负结果"}
      }
    },
    {
      "relative_position": "Lower full-width base",
      "shape": "Shallow bar, #F7F7F7 fill, #CCCCCC 1.0pt",
      "exact_title_to_render_inside": "共同验证",
      "icon": "small 2x2 comparison matrix, hold-out split, and anonymized score sheet, monochrome",
      "exact_text": "同材料 · 同划分 · 同预算    B0–B3    逐项消融    跨来源留出    专家盲评"
    },
    {
      "relative_position": "Bottom-most caption strip",
      "shape": "Borderless",
      "exact_text": "评价入包，不评价学习效果"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes WHITE fill with COLORED BORDERS ONLY.",
    "This is a conceptual framework, NOT a software pipeline: do not draw review checklists, pending queues, or return-for-revision loops.",
    "Three modules must be equal width, left-to-right progressive, with one scientific question and one metric line each.",
    "Kp and Kc share the knowledge-blue family; do not color them as opposing camps.",
    "Extended modality dashed grey. Output emerald used only on the right results column.",
    "NO trophy, rising sparkline, or checked KPI implying completed positive results.",
    "NO emojis, NO lock/fire/lightning, NO 3D, NO gradients, NO drop shadows.",
    "Icons monochrome line art. Canvas pure white."
  ]
}
```

### Image prompt（约 340 词）

Flat vector academic architecture diagram showing the overall research framework for constructing and validating multimodal teaching resource units, on a pure white #FFFFFF canvas, 16:9.

The diagram is conceptual, not a software pipeline: it maps a controlled object to three progressive scientific mechanisms and a shared evaluation base. Layout: a narrow left input column, an upper-center resource-unit card, a middle row of three equal modules, a right results column, and a full-width validation bar underneath. Solid dark-grey #4D4D4D arrows run left-to-right through the three modules; thin connectors drop from the modules into the validation base. No review-queue or return-loop arrows.

Left column, navy #1B3A5C border, title "受控输入": stacked labels "D 原始资源", "Kp 产业知识" and "Kc 课程知识" each with a tiny node-link icon; a core-modality row with document, polyline, and device-frame thumbnails labeled "文本  图表  设备图"; a dashed slate-grey #616161 card "扩展模态" / "代码 / 案例". Upper center, a thicker navy card "资源单元" shows "u = (c, a, m, e, s)" and five small slots "c 知识   a 属性   m 片段   e 出处   s 状态".

Middle row, three equal rounded modules: ① "构造层" in medium blue #2E6B9E with a Kp–Kc link icon, labels "联合知识约束", "联合约束何时有效", "无知识 / 仅Kp / 仅Kc / 联合", and "边界F1 · 覆盖 · 属性"; ② "关系层" in light blue #5BA0D0 with a selective cross-modal matching icon, labels "属性 + 来源证据", "属性与出处如何约束", "语义 · 属性 · 出处", and "Recall@K · MRR · 定位"; ③ "质量层" in medium blue with a 2×2 gate-bar icon, labels "四层联合验证", "内在质量独立效度", "内容  课程  模态  证据", and "VRR · 盲评 · 留出". Right column, sparse emerald #1B9E77 border, "预期成果": pack / report / monitor icons, "资源包 · 质量报告", "本地原型", "增量作用", "适用边界 / 负结果". Bottom #F7F7F7 bar "共同验证": "同材料 · 同划分 · 同预算    B0–B3    逐项消融    跨来源留出    专家盲评". Tiny strip: "评价入包，不评价学习效果".

Nature Blue monochrome plus one emerald results column. White fills, 1.5pt borders, 6px radii. Sans-serif hierarchy 10–12 / 8–9 / 7pt. No gradients, shadows, 3D, emojis, trophies, or learning-analytics icons. Full formulas stay in the caption. Aspect ratio 16:9.

### Caption reserve

- \(u=(c,a,m,e,s)\) 与式 (2)(5)(7)(8) 的完整定义
- B0 人工、B1 通用大模型、B2 仅文本 RAG、B3 完整方法
- 消融：去产业知识 / 去课程知识 / 去专业属性 / 去来源位置 / 去质量层
- 拟建规模（4 模块、≥300 单元、120 盲评、≥3 名专家）不得画成已有事实
- 权重与阈值在开发集确定、测试集冻结

---

## 五、Fig. 3 技术路线图 — Figure Spec Package

**中文图名**：面向可追溯资源单元的五阶段技术路线与独立验证闭环
**类型**：Closed-Loop Technical Route
**palette**：Nature Blue
**aspect_ratio**：16:9

### JSON spec

```json
{
  "diagram_type": "Closed-Loop Technical Route",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column / NSFC text width)",
    "font_family": "Noto Sans SC / Source Han Sans for Chinese; Arial, Helvetica for Latin",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt italic"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head",
      "feedback_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "S1_Review": "Dark Navy (#1B3A5C) 1.5pt solid, white fill",
      "S2_Knowledge": "Medium Blue (#2E6B9E) 1.5pt solid, white fill",
      "S3_Align": "Light Blue (#5BA0D0) 1.5pt solid, white fill",
      "S4_Gate": "Medium Blue (#2E6B9E) 1.5pt solid, white fill",
      "S5_Validate": "Light Blue (#5BA0D0) 1.5pt solid, white fill",
      "Decision": "thin diamond, #4D4D4D 1.0pt",
      "RejectBranch": "Coral (#D95F02) 1.5pt dashed, white fill",
      "Output": "Emerald (#1B9E77) 1.5pt solid, white fill",
      "ControlBase": "section_bg #F7F7F7, #CCCCCC 1.0pt"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "feedback_loop": "Coral (#D95F02) 1.0pt dashed curved arrows"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top row, stage 1 of 5",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt, white fill",
      "exact_title_to_render_inside": "① 材料审查",
      "icon": "clipboard checklist line icon, monochrome",
      "exact_text": "来源 · 许可 · 脱敏",
      "secondary_note": "公开 / 授权 / 自建",
      "flow": "Solid arrow RIGHT through diamond 合规入池？"
    },
    {
      "relative_position": "Below-left of stage 1 diamond",
      "shape": "Small rounded rectangle, #D95F02 1.5pt dashed, white fill",
      "exact_label": "不入池",
      "branch_no": "Dashed coral arrow DOWN-LEFT from diamond when 否"
    },
    {
      "relative_position": "Top row, stage 2 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt, white fill",
      "exact_title_to_render_inside": "② 知识建模",
      "icon": "Kp–Kc dual node-link icon, monochrome",
      "exact_text": "任务—对象—条件",
      "secondary_note": "切分 · 冲突记录",
      "flow": "Solid arrow RIGHT to stage 3"
    },
    {
      "relative_position": "Top row, stage 3 of 5",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt, white fill",
      "exact_title_to_render_inside": "③ 证据关联",
      "icon": "cross-modal matching matrix with an evidence-anchor pin, monochrome",
      "exact_text": "语义 + 属性 + 出处",
      "secondary_note": "对象·变量·单位·工况",
      "flow": "Solid arrow RIGHT through diamond 关系可写入？"
    },
    {
      "relative_position": "Below stage 3 diamond",
      "shape": "Small rounded rectangle, #616161 1.5pt dashed, white fill",
      "exact_label": "待核验",
      "exact_status": "[待核验]",
      "branch_no": "Dashed grey arrow DOWN to 待核验, then dashed return into stage 3"
    },
    {
      "relative_position": "Top row, stage 4 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt, white fill",
      "exact_title_to_render_inside": "④ 四层门控",
      "icon": "2x2 cells: 内容 课程 模态 证据, monochrome",
      "exact_text": "仅作筛查",
      "flow": "Solid arrow RIGHT through diamond 质量通过？"
    },
    {
      "relative_position": "Below stage 4, feedback",
      "shape": "Small rounded rectangle, #D95F02 1.5pt dashed, white fill",
      "exact_label": "退回修改",
      "failure_branch": "Dashed coral curved arrow from diamond 否 back LEFT toward stages 2–3"
    },
    {
      "relative_position": "Top row, stage 5 of 5",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt, white fill",
      "exact_title_to_render_inside": "⑤ 独立验证",
      "icon": "anonymized score sheet and hold-out split icon, monochrome",
      "exact_text": "测试集冻结",
      "secondary_note": "对照 · 消融 · 盲评",
      "flow": "Solid arrow RIGHT to output card"
    },
    {
      "relative_position": "Far right of stage 5",
      "shape": "Rounded rectangle, #1B9E77 1.5pt, white fill",
      "exact_title_to_render_inside": "交付",
      "icon": "pack box, report, desktop monitor, monochrome",
      "exact_text": "资源包 · 报告 · 原型",
      "secondary_note": "边界 / 负结果"
    },
    {
      "relative_position": "Bottom full-width control bar",
      "shape": "Shallow bar, #F7F7F7 fill, #CCCCCC 1.0pt",
      "exact_title_to_render_inside": "实验控制",
      "icon": "four small baseline pills and three metric groups, monochrome",
      "exact_text": "同材料 · 同划分 · 同预算    B0 人工  B1 大模型  B2 文本RAG  B3 完整法",
      "secondary_note": "构建: 边界F1    关联: Recall@K    质量: VRR"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes WHITE fill with COLORED BORDERS ONLY.",
    "Main forward arrows SOLID #4D4D4D; reject/pending/return arrows DASHED coral or grey.",
    "Three diamonds only: 合规入池？ / 关系可写入？ / 质量通过？ Keep diamond text ≤6 characters plus ？",
    "Automatic gating is screening only; do not draw a green auto-accept stamp as final acceptance.",
    "No arrow from frozen test results back into parameter tuning.",
    "Code/case must not appear as a required core stage; if shown, dashed 扩展模态 only inside stage 3.",
    "NO emojis, NO lock/fire/lightning, NO 3D, NO gradients, NO drop shadows, NO cloud-platform icons.",
    "Do not plot numeric results. Metric names only.",
    "Icons monochrome line art. Canvas pure white."
  ]
}
```

### Image prompt（约 360 词）

Flat vector academic architecture diagram showing a five-stage closed-loop technical route for traceable multimodal teaching-resource units, on a pure white #FFFFFF canvas, 16:9.

Horizontal left-to-right pipeline of five equal-width rounded stages on the upper half, three small decision diamonds on the flow, dashed reject/pending/return branches below the main line, an emerald delivery card at the far right, and a full-width experimental-control bar at the bottom. This figure is operational: it shows steps, gates, and feedback. It must not repeat the scientific-question cards of the framework figure.

Stage ① "材料审查", navy #1B3A5C border, checklist icon, labels "来源 · 许可 · 脱敏" and "公开 / 授权 / 自建". A diamond "合规入池？" sends a solid arrow right on yes and a dashed coral #D95F02 arrow down-left to a small card "不入池". Stage ② "知识建模", medium blue #2E6B9E, Kp–Kc node-link icon, "任务—对象—条件" and "切分 · 冲突记录". Stage ③ "证据关联", light blue #5BA0D0, matching-matrix plus evidence-pin icon, "语义 + 属性 + 出处" and "对象·变量·单位·工况". A diamond "关系可写入？" sends incompletes down a dashed grey arrow to a dashed card "待核验" with a grey "[待核验]" pill, then a dashed return into stage 3. Stage ④ "四层门控", medium blue, 2×2 cells "内容 课程 模态 证据", note "仅作筛查". A diamond "质量通过？" sends failures along a dashed coral curved arrow labeled "退回修改" back toward stages 2–3. Stage ⑤ "独立验证", light blue, score-sheet and hold-out icons, "测试集冻结" and "对照 · 消融 · 盲评". Far right, emerald #1B9E77 card "交付": pack/report/monitor icons, "资源包 · 报告 · 原型" and "边界 / 负结果".

Bottom #F7F7F7 bar "实验控制": "同材料 · 同划分 · 同预算", four pills "B0 人工  B1 大模型  B2 文本RAG  B3 完整法", and three metric groups "构建: 边界F1    关联: Recall@K    质量: VRR" with no numeric values.

Nature Blue borders; coral only on dashed reject/return; emerald only on delivery. White fills, 1.5pt solid main borders, 1.0pt dashed feedback, 6px radii. Sans-serif 10–12 / 8–9 / 7pt. No gradients, shadows, 3D, emojis, auto-accept stamps, cloud platforms, or learning-effect charts. Full equations and metric definitions stay in the caption. Aspect ratio 16:9.

### Caption reserve

- 式 (2)–(8) 与全部权重、阈值
- B0–B3 与五类消融的完整定义
- 分层指标全称（边界 F1、覆盖、重复、属性错误、Recall@1/5、MRR、关系 F1、来源定位、错配率、VRR、检出/误报、Krippendorff’s alpha、修订时间）
- 自动门控只作筛查；专家盲评与规则设计隔离
- 核心/扩展模态条件与许可边界

---

## 六、跨图一致性检查

| 约束 | Fig. 1 | Fig. 2 | Fig. 3 |
|---|---|---|---|
| 叙事 | 为何缺口存在 | 研究什么、如何被检验 | 怎样做、何处分流 |
| 资源单元卡 | 作为目标锚点出现一次 | 作为核心对象放大 | 不重复展开五字段 |
| Kp / Kc | 双重语境，非对立色 | 构造层输入 | 知识建模阶段内部 |
| 四层门控 | 只作为切入名 | 质量层机制卡 | 第④阶段 + 判定菱形 |
| B0–B3 | 不上图 | 验证底座短标签 | 底栏完整四条件 |
| 反馈虚线 | 无 | 无 | 不入池 / 待核验 / 退回 |
| 扩展模态 | 虚线出现 | 虚线出现 | 仅可在第③阶段虚线出现 |
| 学生数据 | 底栏明确排除 | 底条明确排除 | 不上学生/平台图标 |

---

## 七、完整性块（总）

- 已分析材料：`main.pdf` + `extraTex/1.1–1.5.tex`；旧 PNG 仅作职责混淆的反面对照
- 当前输出类型：完整（规划 + 配色 + 三套 JSON spec + 三套 image prompt）
- 高置信信息：对象、三机制、五阶段、对照消融、边界、核心/扩展模态
- 待确认信息：图宽、图号、图注是否写拟建规模、生图模型
- 建议补充材料：无强制参考图；若生图，三张必须按本包同一 Nature Blue 语义绑定一次出齐
- 本轮未生图
