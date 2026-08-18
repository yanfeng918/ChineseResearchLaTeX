# F03 · 技术路线图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：技术路线图 ｜ **类型**：Technical Route / Execution Pipeline Diagram（含退出、回流与对照带）
> **状态**：MANDATORY ｜ **优先级**：P0 ｜ **长宽比**：16:9

---

## 一、图形目的（Diagram Purpose）

说明本项目**如何实际执行**：五阶段流水线、三类例外处理通道（不入池 / 人工核验 / 退回修改）、B0–B3 对照与五项消融、三层指标产出，以及两年两阶段的时间落位。

**一句话结论**：项目按"材料审查—知识结构与单元切分—跨模态关联—四层门控—独立验证"顺序执行，每阶段设退出或回流通道，权重与阈值仅在开发集确定并在测试集冻结。

**关键约束**：本图使用**动作短语**，与总体研究框架图（名词性概念对位）形态互斥；**不含研究背景、缺口叙事或创新点对位**。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Technical Route Pipeline Diagram with exit, rework and control bands",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits",
    "font_hierarchy": {
      "stage_title": "10pt bold",
      "band_title": "9pt bold",
      "primary_label": "8pt regular",
      "secondary_note": "7pt regular",
      "timeline_label": "7pt regular"
    },
    "stroke_hierarchy": {
      "stage_border": "2.0pt solid",
      "sub_block_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "main_flow_arrow": "2.0pt solid with 4px head",
      "rework_arrow": "1.2pt solid with 3px head",
      "reject_arrow": "1.2pt DASHED with 3px head",
      "auxiliary_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue with restricted warning accent (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #A64B2A (the warning accent REPLACES the usual light blue in this figure)",
    "main_block_color_palette": {
      "stage_container": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "sub_block": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "band_container": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "reject_or_exit_box": "Warm Brick (#A64B2A) 1.5pt DASHED border, white fill",
      "de_emphasised": "Pale Blue Grey (#8EAEC4) 1.0pt solid border, white fill"
    },
    "text_colors": {
      "stage_title": "#1B3A5C",
      "band_title": "#1B3A5C",
      "sub_title": "#2E6B9E",
      "body_label": "#333333",
      "reject_label": "#A64B2A"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Navy (#1B3A5C) 2.0pt solid, filled head",
      "rework_loop": "Dark Grey (#4D4D4D) 1.2pt solid, routed BELOW the pipeline, never crossing a module",
      "reject_exit": "Warm Brick (#A64B2A) 1.2pt DASHED, terminating in a small solid dot",
      "band_to_stage": "Dark Grey (#4D4D4D) 1.0pt dashed"
    },
    "dual_encoding_rule": "Every warm-brick element MUST also use a dashed stroke AND an explicit Chinese label, so the figure remains readable in pure greyscale print."
  },
  "layout_and_content_blocks": [
    {
      "id": "S1",
      "relative_position": "Pipeline stage 1 of 5, far left, upper 55% of canvas",
      "shape": "Rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "S1 材料审查与登记",
      "icon": "clipboard with check mark, thin grey line art",
      "internal_content": {
        "layout": "Three stacked medium-blue sub-blocks",
        "sub_1": { "exact_text": "登记来源 · 许可 · 模态 · 位置 · 敏感信息" },
        "sub_2": { "exact_text": "授权审查与脱敏" },
        "sub_3": { "exact_text": "方法验证资源池 / 课程扩展资源池" }
      },
      "reject_branch": {
        "shape": "Warm Brick (#A64B2A) 1.5pt dashed border, white fill, placed ABOVE the stage",
        "exact_text": "未通过审查 → 不入池",
        "connector": "Short warm-brick dashed arrow pointing UP out of S1, terminating in a small solid dot"
      },
      "flow": "Thick dark navy arrow pointing RIGHT to S2"
    },
    {
      "id": "S2",
      "relative_position": "Pipeline stage 2 of 5",
      "shape": "Rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "S2 知识结构与单元切分",
      "icon": "branching node tree, thin grey line art",
      "internal_content": {
        "layout": "Four stacked medium-blue sub-blocks",
        "sub_1": { "exact_text": "产业任务—课程知识轻量结构" },
        "sub_2": { "exact_text": "候选片段切分" },
        "sub_3": { "exact_text": "联合知识约束打分" },
        "sub_4": { "exact_text": "产出：资源单元" }
      },
      "flow": "Thick dark navy arrow pointing RIGHT to S3"
    },
    {
      "id": "S3",
      "relative_position": "Pipeline stage 3 of 5, centre",
      "shape": "Rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "S3 跨模态候选生成与证据约束关联",
      "icon": "two linked nodes, thin grey line art",
      "internal_content": {
        "layout": "Four stacked medium-blue sub-blocks",
        "sub_1": { "exact_text": "各模态表示提取" },
        "sub_2": { "exact_text": "对比学习获得基础表示" },
        "sub_3": { "exact_text": "专业属性 / 来源位置 / 关系类别校验" },
        "sub_4": { "exact_text": "困难负例：变量 · 单位 · 工况 · 时序错配" }
      },
      "rework_branch": {
        "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill, placed BELOW S3 as a side pocket",
        "exact_text": "属性或证据不全 → 人工核验队列",
        "connector": "Dark grey 1.2pt solid arrow from S3 DOWN into this box, and a matching arrow back UP into S3"
      },
      "flow": "Thick dark navy arrow pointing RIGHT to S4"
    },
    {
      "id": "S4",
      "relative_position": "Pipeline stage 4 of 5",
      "shape": "FOCUS STAGE: rectangular container, Dark Navy (#1B3A5C) 3.0pt solid border, white fill, with 1.5x surrounding whitespace",
      "exact_title_to_render_inside": "S4 四层质量门控",
      "icon": "four stacked horizontal layers, thin grey line art",
      "internal_content": {
        "layout": "Four thin medium-blue horizontal bars stacked vertically, plus one rule line beneath",
        "layer_1": { "exact_label": "内容层" },
        "layer_2": { "exact_label": "课程层" },
        "layer_3": { "exact_label": "模态层" },
        "layer_4": { "exact_label": "证据层" },
        "rule_line": { "exact_text": "任一层严重错误即拒绝并保留原因" }
      },
      "reject_branch": {
        "shape": "Warm Brick (#A64B2A) 1.5pt dashed border, white fill, placed BELOW the pipeline",
        "exact_text": "严重错误单元 → 退回修改",
        "connector": "Warm-brick 1.2pt dashed arrow from S4 DOWN, then a dark grey 1.2pt solid rework arrow routed along the BOTTOM EDGE of the pipeline back to S2. This return path must not cross any module."
      },
      "flow": "Thick dark navy arrow pointing RIGHT to S5"
    },
    {
      "id": "S5",
      "relative_position": "Pipeline stage 5 of 5, far right",
      "shape": "Rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "S5 独立验证与结果报告",
      "icon": "person outline with rating bars, thin grey line art",
      "internal_content": {
        "layout": "Four stacked medium-blue sub-blocks",
        "sub_1": { "exact_text": "按知识模块 / 来源 / 设备类型留出", "secondary_note": "近重复材料不跨集合" },
        "sub_2": { "exact_text": "拟邀请不少于 3 名独立专家盲评", "secondary_note": "不参与构建 · 隐藏方法条件" },
        "sub_3": { "exact_text": "误差分析与错误类型统计" },
        "sub_4": { "exact_text": "产出：资源包 · 元数据 · 质量报告 · 本地原型" }
      }
    },
    {
      "id": "BAND_CONTROL",
      "relative_position": "First full-width band below the pipeline, height <= 12% of canvas",
      "shape": "Full-width horizontal band, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_band_title": "对照与消融设置",
      "internal_content": {
        "layout": "Left half: four baseline chips in a row. Right half: one ablation strip.",
        "baseline_chips": {
          "shape": "Four small Medium Blue (#2E6B9E) 1.5pt border white chips",
          "chip_1": { "exact_label": "B0 人工整理" },
          "chip_2": { "exact_label": "B1 通用大模型" },
          "chip_3": { "exact_label": "B2 仅文本 RAG" },
          "chip_4": { "exact_label": "B3 完整方法" }
        },
        "ablation_strip": {
          "shape": "One wide Medium Blue (#2E6B9E) 1.5pt border white box",
          "exact_title_to_render_inside": "逐项消融",
          "exact_text": "− 产业知识 / − 课程知识 / − 专业属性 / − 来源位置 / − 质量层"
        }
      },
      "connector": "Dark grey 1.0pt dashed arrows rising from this band to S2, S3 and S4, showing that the control settings act on those three stages"
    },
    {
      "id": "BAND_METRIC",
      "relative_position": "Second full-width band, directly below BAND_CONTROL, height <= 13% of canvas",
      "shape": "Full-width horizontal band, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_band_title": "分层指标产出",
      "internal_content": {
        "layout": "Three equal-width medium-blue boxes in one row, each horizontally aligned under the stage that produces it",
        "metric_1": { "exact_title_to_render_inside": "构建层", "exact_text": "边界 F1 · 知识覆盖 · 重复率 · 属性错误率" },
        "metric_2": { "exact_title_to_render_inside": "关联层", "exact_text": "Recall@1 · Recall@5 · MRR · 关系 F1 · 来源定位准确率 · 错配率" },
        "metric_3": { "exact_title_to_render_inside": "质量层", "exact_text": "VRR 主指标 · 错误检出率 · 误报率 · 五维盲评 · Krippendorff's alpha · 人工修订时间" }
      },
      "connector": "Dark grey 1.0pt dashed upward arrows from 构建层 to S2, 关联层 to S3, 质量层 to S4"
    },
    {
      "id": "TIMELINE",
      "relative_position": "Bottom-most single row, full width, height <= 8% of canvas",
      "shape": "One horizontal 1.0pt #CCCCCC line with NO arrowhead, split by one vertical divider at the midpoint",
      "internal_content": {
        "left_segment": {
          "exact_title_to_render_inside": "第 1–12 个月",
          "exact_text": "来源登记与授权审查 · 知识结构与标注规范 · 基线搭建 · 开发集预实验"
        },
        "divider_label": {
          "shape": "Small Dark Navy (#1B3A5C) 1.5pt border white tag straddling the divider",
          "exact_text": "开发集定权重与阈值 → 测试集冻结"
        },
        "right_segment": {
          "exact_title_to_render_inside": "第 13–24 个月",
          "exact_text": "关联方法与四层门控完善 · 冻结测试集上的对照/消融/跨来源留出 · 专家盲评与误差分析 · 原型迭代"
        }
      }
    },
    {
      "id": "FALLBACK_TAG",
      "relative_position": "Bottom-right corner, smallest element",
      "shape": "Pale Blue Grey (#8EAEC4) 1.5pt dashed border, white fill",
      "exact_text": "降级路径：自动初筛—人工复核",
      "typography": "7pt regular, #4D4D4D"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. Only bands may use light grey (#F7F7F7) fill.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E and #A64B2A, plus neutral greys. Do NOT introduce a fourth chromatic colour.",
    "The warm brick colour #A64B2A is RESERVED exclusively for reject, exit and rework-trigger elements. Every such element MUST simultaneously use a dashed stroke and an explicit Chinese label so the figure survives greyscale printing.",
    "Three exception channels must be visually distinct: the S1 exit uses a short dashed arrow terminating in a solid dot; the S3 manual-check pocket uses a solid down-and-back pair of arrows; the S4 rework return is routed along the BOTTOM EDGE of the pipeline back to S2.",
    "All rework and return arrows must be routed BELOW the pipeline and must NEVER cross through any module box.",
    "Exactly ONE focus element: stage S4 四层质量门控 uses a 3.0pt dark navy border with enlarged surrounding whitespace. No other element may be emphasised.",
    "The two bands (对照与消融设置, 分层指标产出) together must occupy no more than 25% of the canvas height. The five-stage pipeline is the dominant element at roughly 55% of canvas height.",
    "The timeline is a plain horizontal line with a midpoint divider. Do NOT draw Gantt bars, calendar grids, milestone diamonds, or any bar-chart element.",
    "Stage S4 shows ONLY four layer names and one rejection rule. Do NOT expand quality scoring, weight synthesis, VRR definition, or expert-validity closure inside it.",
    "Do NOT render any mathematical formula, loss function, or equation. Only the bare metric names listed in exact_* fields are allowed.",
    "Do NOT render any research background narrative, literature gap, innovation point, or scientific-question statement.",
    "Quantities describing future work must keep their 拟邀请 prefix exactly as written.",
    "Icons are monochrome thin grey line art, at most one per stage, no larger than 1.6x the adjacent text height.",
    "NO emojis, NO lock/fire/lightning decorative symbols, NO 3D rendering.",
    "Flat 2D vector infographic style: no gradients, no glow, no glassmorphism, no drop shadows, no bevels, no decorative background patterns, no grid background.",
    "No figure title bar, no caption text, no page number, no watermark, no legend box.",
    "Canvas is pure white (#FFFFFF). White space must occupy at least 70% of the canvas area.",
    "Do NOT depict students, student data, learning behaviour, personalised recommendation, learning-outcome prediction, or any platform/cloud deployment."
  ]
}
```

---

## 三、Image Prompt（English, for image model）

```
A flat 2D vector academic technical-route pipeline diagram for a Chinese research grant proposal, on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: how a project on multimodal teaching-resource construction for university new-energy courses will actually be executed, from material vetting through to independent validation, including the exit, manual-check and rework channels that keep the evidence trustworthy.

Composition: the upper 55% of the canvas is a left-to-right pipeline of five dark-navy 2pt bordered stages joined by thick dark-navy arrows — S1 材料审查与登记, S2 知识结构与单元切分, S3 跨模态候选生成与证据约束关联, S4 四层质量门控, S5 独立验证与结果报告 — each containing three or four medium-blue inner lines. S4 is the single visual focus, drawn with a thicker 3pt border and extra surrounding white space, containing four thin stacked layer bars 内容层, 课程层, 模态层, 证据层 and the rule 任一层严重错误即拒绝并保留原因. Three exception channels are visually distinct: above S1 a warm-brick dashed box 未通过审查 → 不入池 reached by a short dashed arrow ending in a solid dot; below S3 a medium-blue side pocket 属性或证据不全 → 人工核验队列 with a solid down-and-back arrow pair; below S4 a warm-brick dashed box 严重错误单元 → 退回修改 whose return path runs along the bottom edge of the pipeline back to S2 without crossing any module.

Below the pipeline sit two slim full-width pale-grey bands, together no more than a quarter of the canvas height. The first, 对照与消融设置, holds four chips B0 人工整理, B1 通用大模型, B2 仅文本 RAG, B3 完整方法 and a wide 逐项消融 box. The second, 分层指标产出, holds three boxes 构建层, 关联层, 质量层, each connected upward by a thin dashed arrow to the stage that produces it. At the very bottom a plain horizontal line, with no arrowhead and a single midpoint divider, separates 第 1–12 个月 from 第 13–24 个月, with a small navy tag at the divider reading 开发集定权重与阈值 → 测试集冻结.

Supporting modules: sparse monochrome thin-grey line icons — clipboard with check, branching node tree, linked nodes, stacked layers, person with rating bars.

Visual tone: restrained, engineering-clean, print-oriented. Material: white fills, coloured borders only, 3pt corner radius, borders 1.0/1.2/1.5/2.0pt. Palette strictly #1B3A5C, #2E6B9E and #A64B2A plus neutral greys; every warm-brick element is also dashed and labelled.

Typography: Source Han Sans / Noto Sans CJK SC; stage titles 10pt bold, band titles 9pt bold, labels 8pt, notes 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: Gantt bars, calendar grids or milestone diamonds; any formula or equation; any background narrative, literature gap or innovation point; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 16:9.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 五阶段主框、阶段标题、主流箭头、时间轴冻结标签 |
| secondary | `#2E6B9E` | 阶段内子块、基线 chip、消融框、指标框、人工核验口袋 |
| **reject** | `#A64B2A` | **顶替 tertiary**：不入池、退回修改（必配虚线 + 中文标签） |
| gray | `#8EAEC4` | 降级路径角标 |
| arrow | `#4D4D4D` | 回流实线、条带虚线上引 |
| section_bg | `#F7F7F7` | 两条条带 |

**唯一焦点**：S4 四层质量门控（3.0pt 边框 + 1.5× 留白）

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 3 项目技术路线。项目依次完成材料审查与登记、知识结构与单元切分、跨模态候选生成与证据约束关联、四层质量门控与独立验证；未通过审查的材料不入池，属性或证据不全的候选关系进入人工核验队列，存在严重错误的资源单元退回修改。对照设置包括人工整理（B0）、通用大模型（B1）、仅文本检索增强生成（B2）与完整方法（B3），并逐项去除产业知识、课程知识、专业属性、来源位置或质量层。数据按知识模块、来源或设备类型划分，近重复材料不跨集合；权重与阈值仅在开发集确定，测试集冻结。项目实施期按两年安排，具体时间节点以立项通知书为准。
- 全部数学表达式（联合知识约束打分、边界损失、对比学习目标、关系评分、证据支持度、四层质量合成、VRR 定义）→ 正文，不上图。
- 拟构建规模（4 个知识模块、≥300 个资源单元、抽取 120 个盲评单元）→ 图注。
- 风险与应对措施（技术风险、资源与进度风险、质量效度风险）→ 正文。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（execution pipeline） |
| 全部模块有标书出处 | ✅ 3.1 / 3.2 / 3.3 / 5.1 / 2.1 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 16:9 |
| 物理规格与字体块 | ✅ 183mm / 10-9-8-7pt / 1.0-1.2-1.5-2.0pt |
| 有彩色 ≤3 | ✅ 3 种（`#A64B2A` 顶替 `#5BA0D0`） |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 五阶段各 1 图标 |
| 无空壳模块 | ✅ 每阶段 3–4 行 |
| 拒绝元素三重编码 | ✅ 暖色 + 虚线 + 中文标签 |
| 负向约束齐备 | ✅ 含禁甘特图/公式/背景叙事、NO emojis / NO 3D |
| 与 F02 的防混淆约束 | ✅ 使用动作短语 + 阶段编号，与 F02 名词性对位互斥 |
| 与 F06 的防混淆约束 | ✅ S4 仅 4 层名 + 1 条规则，不展开质量合成与效度闭环 |
| 承接被否决的对照矩阵图 | ✅ B0–B3 与五项消融已完整承载于 BAND_CONTROL |
| 推断或待确认项 | 无。全部内容可溯源至标书 |
