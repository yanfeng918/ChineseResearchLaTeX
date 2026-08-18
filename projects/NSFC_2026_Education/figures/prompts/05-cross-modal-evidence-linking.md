# F05 · 专业属性与来源证据约束的跨模态关联机制图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：专业属性与来源证据约束的跨模态关联机制图 ｜ **类型**：Mechanism / Decision-Gate Diagram with Failure Taxonomy
> **状态**：RECOMMENDED ｜ **优先级**：P1 ｜ **长宽比**：16:9

---

## 一、图形目的（Diagram Purpose）

说明创新点二的**判定机制**：候选关系必须同时通过语义相关、专业条件相容与证据位置可核查三重检验才能写入资源单元；未通过者被显式归因为三类**可解释的失效类型**，而非笼统的"检索失败"。

**一句话结论**：语义相似只是跨模态关联的必要条件；只有对象、变量、单位、工况、时序相容且来源位置可核查的候选，才构成可支持教学使用的关系。

**填补的信息缺口**：总体框架图中"研究内容二"仅列属性条与关系类型；技术路线图只给出"候选生成 → 校验 → 人工核验回流"的执行位置。三重闸门判定逻辑与失效类型学在两图中均不存在。

**形态强制约束**：本图采用**横向串联的直角闸门条**；四层质量门控图（F06）采用**纵向层栈**。两图流向正交，不得视觉雷同。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Cross-Modal Relation Decision-Gate Mechanism Diagram with Failure Taxonomy",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits; Times italic for the symbols sim, C_A, C_E, C_R",
    "font_hierarchy": {
      "zone_title": "10pt bold",
      "gate_title": "9.5pt bold",
      "primary_label": "8pt regular",
      "secondary_note": "7pt regular"
    },
    "stroke_hierarchy": {
      "gate_border": "2.0pt solid",
      "module_border": "1.5pt solid",
      "lane_border": "1.0pt solid",
      "main_flow_arrow": "2.0pt solid with 4px head",
      "parallel_intake_arrow": "1.0pt solid with 3px head",
      "failure_arrow": "1.2pt DASHED with 3px head",
      "injection_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue with restricted warning accent (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #A64B2A (the warning accent REPLACES the usual light blue in this figure)",
    "main_block_color_palette": {
      "gate_bar": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners (0pt radius)",
      "process_module": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill, 3pt corner radius",
      "modality_lane": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill, 3pt corner radius",
      "de_emphasised_lane": "Pale Blue Grey (#8EAEC4) 1.0pt solid border, white fill",
      "failure_box": "Warm Brick (#A64B2A) 1.5pt DASHED border, white fill",
      "success_box": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "band_container": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border"
    },
    "text_colors": {
      "zone_title": "#1B3A5C",
      "gate_title": "#1B3A5C",
      "module_title": "#2E6B9E",
      "body_label": "#333333",
      "failure_label": "#A64B2A",
      "de_emphasised_label": "#4D4D4D"
    },
    "flow_arrow_colors": {
      "main_decision_flow": "Dark Navy (#1B3A5C) 2.0pt solid, filled head, running left to right through all three gates",
      "modality_intake": "Dark Grey (#4D4D4D) 1.0pt solid, thin head",
      "failure_branch": "Warm Brick (#A64B2A) 1.2pt DASHED, pointing straight DOWN from each gate",
      "negative_injection": "Dark Grey (#4D4D4D) 1.0pt dashed, pointing UP into the gate section",
      "report_link": "Dark Grey (#4D4D4D) 1.0pt dashed, pointing RIGHT to the metric rail"
    },
    "dual_encoding_rule": "Every warm-brick element MUST also use a dashed stroke AND an explicit Chinese label, so the figure remains readable in pure greyscale print."
  },
  "layout_and_content_blocks": [
    {
      "id": "ZONE_INTAKE",
      "relative_position": "Left section, occupies leftmost 24% of canvas width",
      "shape": "Vertical group of four horizontal lanes, converging rightward",
      "exact_zone_title": "多模态输入与属性提取",
      "internal_content": {
        "layout": "Four horizontal modality lanes stacked vertically, each with an icon on the left and a label; the fourth lane is visually de-emphasised. All four feed rightward into one shared extraction bar.",
        "lane_1": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "icon": "document page outline", "exact_label": "课程文本" },
        "lane_2": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "icon": "simplified equipment outline", "exact_label": "设备结构图" },
        "lane_3": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "icon": "line chart", "exact_label": "运行曲线图表" },
        "lane_4": {
          "shape": "Pale Blue Grey (#8EAEC4) 1.0pt border, white fill, LOWEST visual weight",
          "icon": "angle brackets",
          "exact_label": "扩展：实验代码 · 产业案例",
          "typography": "7pt regular, #4D4D4D"
        },
        "extraction_bar": {
          "shape": "One tall Medium Blue (#2E6B9E) 1.5pt border white box spanning the height of all four lanes",
          "exact_title_to_render_inside": "统一属性提取",
          "exact_text": "对象 · 变量 · 单位 · 工况 · 时间窗口 · 来源位置"
        }
      },
      "flow": "Four thin dark-grey arrows, one per lane, pointing RIGHT into the shared extraction bar; then one thick dark navy arrow from the extraction bar RIGHT into ZONE_CANDIDATE"
    },
    {
      "id": "ZONE_CANDIDATE",
      "relative_position": "Left-of-centre, occupies 16% of canvas width",
      "shape": "Two Medium Blue (#2E6B9E) 1.5pt border white boxes stacked vertically",
      "exact_zone_title": "基础表示与候选生成",
      "internal_content": {
        "box_1": {
          "exact_title_to_render_inside": "对比学习获得基础表示",
          "exact_text": "正确配对为正例\\n批内其余为负例",
          "secondary_note": "温度参数 τ"
        },
        "box_2": {
          "exact_title_to_render_inside": "候选关系生成",
          "exact_text": "跨模态候选对"
        }
      },
      "flow": "Thick dark navy arrow pointing RIGHT into ZONE_GATE"
    },
    {
      "id": "ZONE_GATE",
      "relative_position": "Centre-right, occupies 36% of canvas width — the visual focus of the figure",
      "shape": "FOCUS: three tall narrow SQUARE-CORNERED vertical gate bars in a horizontal row, connected by a single thick dark navy arrow running left to right through all three, with 1.5x surrounding whitespace around the whole group",
      "exact_zone_title": "三重条件判定",
      "internal_content": {
        "gate_1": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners, tall and narrow",
          "exact_title_to_render_inside": "闸门一\\n语义相关性",
          "exact_text": "sim",
          "text_typography": "Times italic"
        },
        "gate_2": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners, tall and narrow",
          "exact_title_to_render_inside": "闸门二\\n专业条件相容",
          "exact_text": "对象 · 变量 · 单位\\n工况 · 时序"
        },
        "gate_3": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners, tall and narrow",
          "exact_title_to_render_inside": "闸门三\\n证据位置可核查",
          "exact_text": "来源位置完整"
        },
        "side_gate_relation_type": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill, attached ABOVE the gate row, connected by a short vertical line",
          "exact_title_to_render_inside": "关系类别一致",
          "exact_text": "解释 / 实例 / 计算实验 / 对照 / 出处支持"
        },
        "synthesis_note": {
          "shape": "No border, floating text beneath the gate row",
          "exact_floating_text": "加权评分达阈值且来源完整方可写入"
        }
      },
      "flow": "Thick dark navy arrow continuing RIGHT out of gate three into ZONE_WRITE"
    },
    {
      "id": "ZONE_WRITE",
      "relative_position": "Far right, occupies 14% of canvas width, upper area",
      "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "全部通过",
      "exact_text": "写入资源单元\\n多模态片段及关系 · 来源位置",
      "icon": "check mark inside a rounded square, thin grey line art"
    },
    {
      "id": "BAND_FAILURE",
      "relative_position": "Bottom band, spanning the horizontal extent of ZONE_GATE, height <= 20% of canvas",
      "shape": "Three Warm Brick (#A64B2A) 1.5pt DASHED border white boxes in a row, each STRICTLY vertically aligned under its corresponding gate",
      "exact_band_title": "可解释的失效类型",
      "internal_content": {
        "fail_1": {
          "aligned_under": "闸门一",
          "exact_title_to_render_inside": "语义不相关",
          "exact_text": "一般检索失败"
        },
        "fail_2": {
          "aligned_under": "闸门二",
          "exact_title_to_render_inside": "专业条件错配",
          "exact_text": "语义相似但变量、单位、\\n工况或时序不一致"
        },
        "fail_3": {
          "aligned_under": "闸门三",
          "exact_title_to_render_inside": "来源不可核查",
          "exact_text": "图表存在但出处不可定位"
        }
      },
      "connector": "One warm-brick 1.2pt DASHED arrow pointing straight DOWN from each gate into the failure box directly beneath it. The three arrows must be strictly vertical and parallel."
    },
    {
      "id": "NEGATIVE_POCKET",
      "relative_position": "Bottom-left corner, below ZONE_CANDIDATE",
      "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
      "exact_title_to_render_inside": "困难负例构造",
      "exact_text": "变量错配 · 单位错配 · 工况错配\\n时序错配 · 来源不可核查",
      "connector": "One dark-grey 1.0pt dashed arrow rising UP from this box into the gate section, indicating that hard negatives are injected to test discrimination"
    },
    {
      "id": "METRIC_RAIL",
      "relative_position": "Right edge, narrow vertical rail below ZONE_WRITE",
      "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill, narrow vertical strip",
      "exact_title_to_render_inside": "按关系类型报告",
      "exact_text": "Recall@1\\nRecall@5\\nMRR\\n关系类别 F1\\n来源定位准确率\\n错配率",
      "typography": "8pt regular, rendered HORIZONTALLY as stacked lines, never rotated",
      "connector": "One dark-grey 1.0pt dashed arrow pointing RIGHT from the gate section to this rail"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text, including the metric rail.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E and #A64B2A, plus neutral greys. Do NOT introduce a fourth chromatic colour.",
    "The three decision gates MUST be drawn as tall narrow vertical bars with SQUARE corners (0pt radius), arranged horizontally and pierced by one continuous thick dark navy arrow. Do NOT use diamond decision shapes, do NOT use rounded corners on the gates, and do NOT stack the gates vertically.",
    "All other boxes use 3pt rounded corners. The square-corner treatment is reserved for the gates and is what distinguishes this figure from the four-layer quality-gate figure.",
    "Exactly ONE focus element: the three-gate group uses enlarged surrounding whitespace. No other element may be emphasised.",
    "The three failure boxes MUST be strictly vertically aligned under 闸门一, 闸门二 and 闸门三 respectively, each reached by a straight vertical dashed warm-brick arrow. Misalignment destroys the attribution meaning of the figure and is not acceptable.",
    "The warm brick colour #A64B2A is RESERVED exclusively for the three failure boxes and their arrows. Every such element MUST simultaneously use a dashed stroke and an explicit Chinese label so the figure survives greyscale printing.",
    "The fourth modality lane 扩展：实验代码 · 产业案例 MUST be visually de-emphasised in pale blue grey #8EAEC4 at 7pt, clearly lighter than the three core modality lanes.",
    "The Latin symbol sim is rendered in Times italic. Do NOT render any full equation, weighting coefficient, summation, or softmax expression.",
    "Do NOT expand the resource-unit field schema, the four-layer quality gate, VRR, expert blind review, or any project execution timeline — those belong to other figures.",
    "Icons are monochrome thin grey line art, at most one per lane or box, no larger than 1.6x the adjacent text height.",
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
A flat 2D vector academic mechanism diagram for a Chinese research grant proposal, on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: how a candidate cross-modal relation between course text, equipment diagrams and operating curves is admitted into a resource unit only after passing three successive conditions — semantic relevance, professional-condition compatibility, and verifiable source location — with every failure attributed to an explicit, interpretable type.

Composition: a single left-to-right decision channel. On the left, four stacked horizontal modality lanes — 课程文本, 设备结构图, 运行曲线图表, and a clearly faded pale-grey fourth lane 扩展：实验代码 · 产业案例 — each sending a thin arrow rightward into one tall shared box 统一属性提取 listing 对象 · 变量 · 单位 · 工况 · 时间窗口 · 来源位置. Next, two medium-blue boxes 对比学习获得基础表示 (with 正确配对为正例, 批内其余为负例 and note 温度参数 τ) and 候选关系生成. Then the visual focus: three tall narrow dark-navy gate bars with SQUARE corners standing side by side, pierced by one continuous thick dark-navy arrow — 闸门一 语义相关性 with the italic symbol sim, 闸门二 专业条件相容 listing 对象 · 变量 · 单位 · 工况 · 时序, and 闸门三 证据位置可核查 reading 来源位置完整. Above the gate row a medium-blue box 关系类别一致 lists 解释 / 实例 / 计算实验 / 对照 / 出处支持; beneath the row floats the note 加权评分达阈值且来源完整方可写入. The arrow exits gate three into a dark-navy box 全部通过 reading 写入资源单元 多模态片段及关系 · 来源位置.

Directly below each gate, strictly vertically aligned and reached by a straight vertical warm-brick dashed arrow, sits one dashed warm-brick failure box: 语义不相关 一般检索失败, 专业条件错配 语义相似但变量、单位、工况或时序不一致, and 来源不可核查 图表存在但出处不可定位. In the bottom-left corner a medium-blue box 困难负例构造 listing 变量错配 · 单位错配 · 工况错配 · 时序错配 · 来源不可核查 sends a dashed arrow up into the gate section. On the right edge a narrow rail 按关系类型报告 stacks Recall@1, Recall@5, MRR, 关系类别 F1, 来源定位准确率, 错配率 as horizontal lines.

Supporting modules: sparse monochrome thin-grey line icons — document page, equipment outline, line chart, angle brackets, check mark in a rounded square.

Visual tone: restrained, analytic, print-oriented. Material: white fills, coloured borders only; gates have square corners, everything else 3pt rounded; borders 1.0/1.2/1.5/2.0pt. Palette strictly #1B3A5C, #2E6B9E and #A64B2A plus neutral greys; every warm-brick element is also dashed and labelled.

Typography: Source Han Sans / Noto Sans CJK SC; zone titles 10pt bold, gate titles 9.5pt bold, labels 8pt, notes 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: diamond decision shapes; vertically stacked gates; any full equation or softmax expression; the resource-unit field schema, four-layer quality gate, VRR, expert blind review or project timeline; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 16:9.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 三道闸门条（直角）、"全部通过"框、主判定流箭头 |
| secondary | `#2E6B9E` | 模态泳道、属性提取框、候选生成框、关系类别框、困难负例框、指标侧栏 |
| **reject** | `#A64B2A` | **顶替 tertiary**：三类失效框及其虚线下引箭头 |
| gray | `#8EAEC4` | 第四条扩展模态泳道 |
| arrow | `#4D4D4D` | 模态并行入流、负例注入、指标虚线连接 |

**唯一焦点**：三道判定闸门串联段（1.5× 留白）
**形态标识**：闸门 = 直角（0pt 圆角）；其余元素 = 3pt 圆角。此为与 F06 的强制区分手段。

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 5 专业属性与来源证据约束的跨模态关联机制。项目先以对比学习获得各模态的基础表示并生成候选关系，再对候选关系依次施加语义相关性、专业条件相容性与证据位置可核查性三重判定，并检查关系类别一致性；只有加权评分达到阈值且来源完整的候选，才写入资源单元的多模态片段及关系与来源位置字段。未通过者按失效类型归因为语义不相关、专业条件错配与来源不可核查三类。项目以变量、单位、工况、时序错配和来源不可核查构造困难负例，按关系类型报告 Recall@1、Recall@5、MRR、关系类别 F1、来源定位准确率与错配率。
- 对比学习目标函数与关系评分函数的完整数学表达式及权重符号 → 正文。
- 温度参数 τ 与批大小 B 的具体设置 → 正文。
- 各关系类型的判定细则 → 正文。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（decision-gate mechanism + failure taxonomy） |
| 全部模块有标书出处 | ✅ 1.2 / 1.3 / 2.1(2) / 2.3(2) / 3.1 / 4.3 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 16:9 |
| 物理规格与字体块 | ✅ 183mm / 10-9.5-8-7pt / 1.0-1.2-1.5-2.0pt |
| 有彩色 ≤3 | ✅ 3 种（`#A64B2A` 顶替 `#5BA0D0`） |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 泳道图标 + 直角闸门形态锚点 |
| 无空壳模块 | ✅ |
| 失效元素三重编码 | ✅ 暖色 + 虚线 + 中文标签 |
| 扩展模态弱化 | ✅ `#8EAEC4` + 7pt + "扩展"字样 |
| 负向约束齐备 | ✅ 含禁菱形判定框/禁纵向堆叠/禁公式、NO emojis / NO 3D |
| 与 F06 的防混淆约束 | ✅ 直角横向串联 vs 圆角纵向层栈，流向正交 |
| 推断或待确认项 | 无。全部内容可溯源至标书 |
