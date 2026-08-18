# F01 · 研究背景图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：研究背景图 ｜ **类型**：Motivation / Problem-Formulation Diagram（四段漏斗式论证图）
> **状态**：MANDATORY ｜ **优先级**：P0 ｜ **长宽比**：16:9

---

## 一、图形目的（Diagram Purpose）

说明本项目**为什么必要**：从新疆新能源产业人才需求出发，经课程多模态资源的固有特征与核心矛盾，收束到三条研究缺口与三个科学问题。本图**不含任何方法步骤、模型或指标**。

**一句话结论**：新能源课程的多模态材料不缺数量，缺的是"边界明确、条件正确、出处可查"的可教学使用资源。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Academic Motivation and Problem-Formulation Diagram (four-band funnel)",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits",
    "font_hierarchy": {
      "band_title": "11pt bold",
      "primary_label": "9pt regular",
      "secondary_note": "7.5pt regular",
      "emphasis_line": "10pt bold"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "2.0pt solid with 4px head",
      "mapping_arrow": "1.0pt solid with 3px head"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #5BA0D0",
    "main_block_color_palette": {
      "band_container": "Light grey (#F7F7F7) fill, no border or 1.0pt #CCCCCC border",
      "level_1_box": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "level_2_box": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "level_3_box": "Light Blue (#5BA0D0) 1.0pt solid border, white fill",
      "focus_box": "Dark Navy (#1B3A5C) 3.0pt solid border, white fill, 1.5x surrounding whitespace"
    },
    "text_colors": {
      "band_title": "#1B3A5C",
      "level_2_title": "#2E6B9E",
      "body_label": "#333333"
    },
    "flow_arrow_colors": {
      "band_advance": "Dark Navy (#1B3A5C) 2.0pt solid, filled head",
      "gap_to_question_mapping": "Medium Blue (#2E6B9E) 1.0pt solid, thin head",
      "side_note": "Dark Grey (#4D4D4D) 1.0pt dashed"
    },
    "forbidden_colors": "Do NOT use any warm, red, orange or brown accent anywhere in this figure."
  },
  "layout_and_content_blocks": [
    {
      "id": "BAND_A",
      "relative_position": "Top band, full width, occupies top 16% of canvas",
      "shape": "Full-width horizontal lane, light grey (#F7F7F7) fill",
      "exact_band_title": "现实与产业需求",
      "internal_content": {
        "layout": "Three level-3 boxes in one row, left to right, connected by short right arrows",
        "box_1": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "simplified wind turbine and solar panel outline, thin grey line art",
          "exact_text": "新疆新能源产业"
        },
        "box_2": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "three-person group outline, thin grey line art",
          "exact_text": "需兼具能源工程、数据分析\\n与人工智能素养的人才"
        },
        "box_3": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "academic building outline, thin grey line art",
          "exact_text": "高校新能源课程"
        }
      },
      "flow": "One thick dark navy arrow pointing DOWN from band centre to BAND_B"
    },
    {
      "id": "BAND_B",
      "relative_position": "Second band, full width, occupies 26% of canvas",
      "shape": "Full-width horizontal lane, light grey (#F7F7F7) fill",
      "exact_band_title": "课程多模态资源特征与核心矛盾",
      "internal_content": {
        "layout": "Upper row: five small material chips side by side. Lower centre: one wide emphasis box.",
        "material_chips": {
          "shape": "Five small Light Blue (#5BA0D0) 1.0pt border white boxes of equal width",
          "chip_1": { "icon": "simplified equipment outline", "exact_label": "设备图" },
          "chip_2": { "icon": "line chart", "exact_label": "运行曲线" },
          "chip_3": { "icon": "document page", "exact_label": "数据说明" },
          "chip_4": { "icon": "angle brackets", "exact_label": "实验代码" },
          "chip_5": { "icon": "factory outline", "exact_label": "工程案例" },
          "exact_floating_text": "常以分散文件存在"
        },
        "conflict_box": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill, centred",
          "exact_title_to_render_inside": "自动重组时易出错",
          "exact_text": "变量 · 单位 · 工况 · 图文关系 · 出处"
        },
        "focus_box": {
          "shape": "FOCUS BOX: Dark Navy (#1B3A5C) 3.0pt solid border, white fill, extra whitespace on all four sides",
          "exact_text": "可检索，但不可教学使用"
        }
      },
      "flow": "One thick dark navy arrow pointing DOWN from the focus box to BAND_C"
    },
    {
      "id": "BAND_C",
      "relative_position": "Third band, full width, occupies 34% of canvas",
      "shape": "Full-width horizontal lane, light grey (#F7F7F7) fill",
      "exact_band_title": "现有研究进展与缺口",
      "internal_content": {
        "layout": "Two stacked rows of three columns each. Upper row = current progress cards. Lower row = gap cards. Each gap card sits directly below its progress card.",
        "progress_row": {
          "shape": "Three Medium Blue (#2E6B9E) 1.5pt border white boxes of equal width",
          "card_1": { "exact_title_to_render_inside": "教育知识图谱", "exact_text": "给出概念层级与资源归属" },
          "card_2": { "exact_title_to_render_inside": "跨模态检索与图表理解", "exact_text": "以语义相似为主" },
          "card_3": { "exact_title_to_render_inside": "检索增强与事实核验", "exact_text": "单点事实可核" }
        },
        "gap_row": {
          "shape": "Three Dark Navy (#1B3A5C) 1.5pt border white boxes, aligned one-to-one under the progress cards",
          "gap_1": { "exact_title_to_render_inside": "缺口一", "exact_text": "缺资源单元层面的\\n产业—课程联合约束" },
          "gap_2": { "exact_title_to_render_inside": "缺口二", "exact_text": "变量、单位、工况、时序、来源缺失\\n无法区分检索命中与可教学关系" },
          "gap_3": { "exact_title_to_render_inside": "缺口三", "exact_text": "内容、课程、模态、证据分散评价\\n缺独立效度" }
        },
        "connector": "Short dark grey 1.0pt dashed downward arrow from each progress card to the gap card directly below it, labelled with nothing"
      },
      "flow": "Three separate thin medium-blue arrows, one from each gap card, pointing straight DOWN to the science-question box directly below it. The three arrows are strictly parallel and must NOT cross."
    },
    {
      "id": "BAND_D",
      "relative_position": "Bottom band, full width, occupies bottom 20% of canvas",
      "shape": "Full-width horizontal lane, light grey (#F7F7F7) fill",
      "exact_band_title": "本项目科学问题",
      "internal_content": {
        "layout": "Three equal-width boxes in one row, each vertically aligned with the gap card above it",
        "q_1": {
          "shape": "Dark Navy (#1B3A5C) 1.5pt border, white fill",
          "exact_title_to_render_inside": "科学问题一",
          "exact_text": "联合知识约束为何、\\n在何条件下改善资源单元构建"
        },
        "q_2": {
          "shape": "Dark Navy (#1B3A5C) 1.5pt border, white fill",
          "exact_title_to_render_inside": "科学问题二",
          "exact_text": "专业属性与来源位置如何\\n共同决定跨模态关联正确性"
        },
        "q_3": {
          "shape": "Dark Navy (#1B3A5C) 1.5pt border, white fill",
          "exact_title_to_render_inside": "科学问题三",
          "exact_text": "不依赖学生行为数据的\\n资源内在质量如何获得独立效度"
        }
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. No coloured fills anywhere except the light grey (#F7F7F7) band lanes.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E, #5BA0D0, plus neutral greys.",
    "Adhere to typography hierarchy: band titles 11pt bold, primary labels 9pt, secondary notes 7.5pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, band-advance arrows 2.0pt, mapping arrows 1.0pt.",
    "Exactly ONE focus element: the box reading 可检索，但不可教学使用 uses a 3.0pt dark navy border with enlarged surrounding whitespace. No other element may be emphasised.",
    "The three gap cards and the three science-question boxes MUST be strictly vertically aligned in three parallel columns. The three mapping arrows must not cross.",
    "Icons are monochrome thin grey line art, at most one per box, no larger than 1.6x the adjacent text height.",
    "This figure describes motivation only. Do NOT draw any method step, model name, algorithm, formula, metric, dataset, training pipeline, or technical route element.",
    "Do NOT render any reference numbers, citation brackets, author names, or bibliography markers.",
    "Do NOT use any warm, red, orange, or brown colour anywhere in this figure.",
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

> Copy the block below directly into GPT-Image-2 / NanoBanana / Gemini.

```
A flat 2D vector academic motivation diagram for a Chinese research grant proposal, rendered as a four-band vertical funnel on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: why a research project on multimodal teaching-resource construction for university new-energy courses is necessary — the argument narrows from industrial demand, through the core contradiction of scattered course materials, down to three research gaps and three scientific questions.

Composition: four full-width horizontal lanes stacked top to bottom with pale grey (#F7F7F7) lane backgrounds, connected by thick dark navy downward arrows. Lane 1, titled 现实与产业需求, holds three small light-blue-bordered boxes in a row: 新疆新能源产业, 需兼具能源工程、数据分析与人工智能素养的人才, 高校新能源课程. Lane 2, titled 课程多模态资源特征与核心矛盾, shows an upper strip of five small material chips labelled 设备图, 运行曲线, 数据说明, 实验代码, 工程案例 with the side note 常以分散文件存在, below them a medium-blue box titled 自动重组时易出错 containing 变量 · 单位 · 工况 · 图文关系 · 出处, and beneath it the single visual focus of the whole figure: a box with a thick 3pt dark navy border and generous surrounding white space reading 可检索，但不可教学使用. Lane 3, titled 现有研究进展与缺口, shows an upper row of three medium-blue cards (教育知识图谱, 跨模态检索与图表理解, 检索增强与事实核验) and directly beneath each a dark-navy gap card 缺口一, 缺口二, 缺口三. Lane 4, titled 本项目科学问题, holds three dark-navy boxes 科学问题一, 科学问题二, 科学问题三, each strictly vertically aligned under its gap card, joined by three thin parallel non-crossing arrows.

Supporting modules: sparse monochrome thin-grey line icons only — wind turbine and solar panel, group of people, academic building, equipment outline, line chart, document page, angle brackets, factory outline. One icon maximum per box.

Visual tone: restrained, print-oriented, scholarly. Material: white fills, coloured borders only, 3pt small corner radius, border weights 1.0/1.5/2.0pt. Palette limited to #1B3A5C, #2E6B9E, #5BA0D0 plus neutral greys #333333, #4D4D4D, #CCCCCC — absolutely no warm, red, orange or brown tones.

Typography: Source Han Sans / Noto Sans CJK SC, band titles 11pt bold in #1B3A5C, labels 9pt, notes 7.5pt in #333333. Canvas width 183mm, white space at least 70%.

Strictly exclude: any method step, model name, formula, metric, dataset or technical-route element; any citation numbers; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends, watermarks; any depiction of students, learning behaviour, recommendation, or platform deployment.

Aspect ratio 16:9.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 带标题、缺口卡、科学问题框、带间推进箭头、焦点框 |
| secondary | `#2E6B9E` | 现状卡片、矛盾框、缺口→问题映射箭头 |
| tertiary | `#5BA0D0` | 需求带三框、五类材料 chip |
| text | `#333333` | 正文标签 |
| arrow | `#4D4D4D` | 虚线旁注 |
| section_bg | `#F7F7F7` | 四条泳道底色 |
| **禁用** | `#A64B2A` | 本图不含失败语义，严禁暖色 |

**唯一焦点**：`可检索，但不可教学使用`（3.0pt 深藏青边框 + 1.5× 留白）

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 1 研究背景与科学问题的形成逻辑。新疆新能源产业对复合型人才的需求，要求高校新能源课程的设备图、运行曲线、数据说明、代码与工程案例能够被组织为可教学使用的资源；然而这些材料常以分散文件存在，自动重组时在变量、单位、工况、图文关系与出处上易出错，形成"可检索但不可教学使用"的核心矛盾。现有教育知识图谱、跨模态检索与图表理解、检索增强与事实核验研究分别推进了概念组织、语义匹配与单点事实核查，但仍遗留三条缺口，对应本项目的三个关键科学问题。
- 参考文献编号（[1]–[34]）一律留在正文与图注，不上图。
- 各类方法族的代表性工作名称（BLIP、CLIP、ChartQA、FActScore 等）不上图。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（motivation / problem-formulation） |
| 全部模块有标书出处 | ✅ 1.1 / 1.2 / 1.3 / 1.4 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 16:9 |
| 物理规格与字体块 | ✅ 183mm / 11pt-9pt-7.5pt / 1.0-1.5-2.0pt |
| 有彩色 ≤3 | ✅ 3 种 |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ |
| 无空壳模块 | ✅ |
| 负向约束齐备 | ✅ 含 NO emojis / NO 3D / 无暖色 / 无方法元素 |
| 推断或待确认项 | 无。全部内容可溯源至标书 1.1–1.4 |
