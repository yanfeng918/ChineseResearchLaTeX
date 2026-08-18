# F04 · 资源单元描述模式与联合知识约束图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：资源单元描述模式与联合知识约束图 ｜ **类型**：Research-Object Schema + Constraint Mechanism Diagram
> **状态**：RECOMMENDED ｜ **优先级**：P1 ｜ **长宽比**：4:3

---

## 一、图形目的（Diagram Purpose）

定义本项目的**研究对象本体**——资源单元的字段结构与描述模式；展示产业任务知识与课程知识如何联合约束单元边界；并以"无知识 / 单一知识 / 联合知识"三条件对照说明该约束**可被证伪**。

**一句话结论**：资源单元不是"打了标签的文件"，而是由课程知识、专业属性、多模态片段及关系、来源位置和质量状态五类字段共同定义、并由产业与课程双知识联合约束其边界的可检验对象。

**填补的信息缺口**：总体框架图中"研究内容一"仅有三行标签，无法展开资源单元的字段级结构；技术路线图只给出"切分 → 单元"这一动作，不说明单元内部是什么。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Research-Object Schema and Joint-Constraint Mechanism Diagram",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits; Times italic for the symbols u, c, a, m, e, s",
    "font_hierarchy": {
      "zone_title": "10pt bold",
      "module_title": "9.5pt bold",
      "slot_name": "8.5pt medium",
      "primary_label": "8pt regular",
      "secondary_note": "7pt regular"
    },
    "stroke_hierarchy": {
      "level_1_border": "2.0pt solid",
      "level_2_border": "1.5pt solid",
      "level_3_border": "1.0pt solid",
      "main_flow_arrow": "2.0pt solid with 4px head",
      "subordination_arrow": "1.0pt solid with 3px head",
      "side_note_arrow": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #5BA0D0",
    "main_block_color_palette": {
      "resource_unit_main": "Dark Navy (#1B3A5C) 3.0pt solid border, white fill, 1.5x surrounding whitespace (FOCUS)",
      "constraint_block": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "slot_row": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "knowledge_source_card": "Light Blue (#5BA0D0) 1.0pt solid border, white fill",
      "de_emphasised": "Pale Blue Grey (#8EAEC4) 1.0pt solid border, white fill",
      "band_container": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border"
    },
    "text_colors": {
      "zone_title": "#1B3A5C",
      "module_title": "#1B3A5C",
      "slot_name": "#2E6B9E",
      "body_label": "#333333",
      "de_emphasised_label": "#4D4D4D"
    },
    "flow_arrow_colors": {
      "converging_joint_constraint": "Dark Navy (#1B3A5C) 2.0pt solid, TWO lines merging into ONE before entering the constraint block",
      "main_generation": "Dark Navy (#1B3A5C) 2.0pt solid, filled head",
      "subordination": "Medium Blue (#2E6B9E) 1.0pt solid, thin head",
      "exception_note": "Dark Grey (#4D4D4D) 1.0pt dashed"
    },
    "forbidden_colors": "Do NOT use any warm, red, orange or brown accent anywhere in this figure."
  },
  "layout_and_content_blocks": [
    {
      "id": "ZONE_KNOWLEDGE",
      "relative_position": "Left column, occupies leftmost 22% of canvas width",
      "shape": "Vertical lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "双知识源",
      "internal_content": {
        "layout": "Two light-blue cards stacked vertically, with one dashed conflict note between them",
        "card_industry": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "factory with gear outline, thin grey line art",
          "exact_title_to_render_inside": "产业任务知识",
          "exact_text": "产业任务\\n设备与工况\\n运行参数\\n告警条件"
        },
        "card_course": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "open book outline, thin grey line art",
          "exact_title_to_render_inside": "课程知识",
          "exact_text": "课程知识点\\n能力目标\\n先修关系\\n资源类型"
        },
        "conflict_note": {
          "shape": "Pale Blue Grey (#8EAEC4) 1.0pt dashed border, white fill, placed between the two cards",
          "exact_text": "粒度差异 · 术语异名 · 属性冲突\\n→ 记录候选关系与人工确认状态",
          "typography": "7pt regular, #4D4D4D"
        }
      },
      "flow": "TWO dark navy 2.0pt lines, one from each card, MERGING into a single line that enters ZONE_CONSTRAINT. This converging arrow is the visual signature of joint constraint and appears nowhere else in the figure set."
    },
    {
      "id": "ZONE_CONSTRAINT",
      "relative_position": "Centre column, occupies 28% of canvas width",
      "shape": "Vertical lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "联合约束与边界优化",
      "internal_content": {
        "layout": "Two dark-navy blocks stacked vertically, joined by a downward arrow",
        "block_scoring": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
          "exact_title_to_render_inside": "联合知识约束打分",
          "internal_layout": "Three medium-blue rows",
          "row_1": { "exact_text": "产业属性兼容" },
          "row_2": { "exact_text": "课程属性兼容" },
          "row_3": { "exact_text": "术语映射兼容" },
          "exact_floating_text": "权重于开发集确定"
        },
        "block_boundary": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
          "exact_title_to_render_inside": "单元边界优化目标",
          "internal_layout": "Four medium-blue rows",
          "row_1": { "exact_text": "抑制知识遗漏" },
          "row_2": { "exact_text": "抑制重复" },
          "row_3": { "exact_text": "抑制过度切分" },
          "row_4": { "exact_text": "抑制专业属性错配" }
        }
      },
      "flow": "Thick dark navy arrow pointing RIGHT into ZONE_UNIT"
    },
    {
      "id": "ZONE_UNIT",
      "relative_position": "Right column, occupies rightmost 50% of canvas width — the widest zone",
      "shape": "Vertical lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "资源单元描述模式",
      "internal_content": {
        "layout": "One large FOCUS container holding five horizontal slot rows; a narrow vertical side rail on the right edge; one dashed side note",
        "main_container": {
          "shape": "FOCUS: Dark Navy (#1B3A5C) 3.0pt solid border, white fill, extra whitespace on all four sides",
          "exact_title_to_render_inside": "资源单元 u = (c, a, m, e, s)",
          "title_typography": "Latin letters u c a m e s in Times italic; Chinese in sans-serif",
          "slot_rows": {
            "layout": "Five full-width medium-blue rows, each with a left slot-name cell and a right content cell separated by a 1.0pt divider",
            "row_1": { "exact_slot_name": "c 课程知识", "exact_text": "知识点 · 能力目标 · 先修关系" },
            "row_2": { "exact_slot_name": "a 专业属性", "exact_text": "对象 · 变量 · 单位 · 工况 · 时间窗口" },
            "row_3": { "exact_slot_name": "m 多模态片段及关系", "exact_text": "课程文本 · 运行曲线图表 · 设备结构图", "de_emphasised_line": "扩展：实验代码 · 产业案例" },
            "row_4": { "exact_slot_name": "e 来源位置", "exact_text": "文件 · 版本 · 页或位置 · 许可状态" },
            "row_5": { "exact_slot_name": "s 质量状态", "exact_text": "通过 / 待核验 / 拒绝（保留原因）" }
          }
        },
        "side_rail": {
          "shape": "Narrow vertical Medium Blue (#2E6B9E) 1.5pt border strip on the right edge of the main container",
          "exact_text": "描述模式：任务—对象—条件—知识点—片段—证据位置",
          "typography": "8pt regular, rendered HORIZONTALLY in a narrow multi-line column, never rotated"
        },
        "side_note": {
          "shape": "Pale Blue Grey (#8EAEC4) 1.0pt dashed border, white fill, attached to slot row 2 or 4 by a dashed arrow",
          "exact_text": "无证据属性 → 待核验队列",
          "typography": "7pt regular, #4D4D4D"
        }
      }
    },
    {
      "id": "BAND_CONDITION",
      "relative_position": "Bottom band, FULL canvas width, height <= 18% of canvas",
      "shape": "Full-width horizontal band, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_band_title": "三条件对照",
      "internal_content": {
        "layout": "Three equal-width medium-blue boxes side by side on the left two-thirds, with NO arrows between them, plus one dark-navy metric box on the right third",
        "cond_1": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "exact_text": "无知识约束" },
        "cond_2": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "exact_text": "单一知识约束\\n仅产业知识 / 仅课程知识" },
        "cond_3": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "exact_text": "联合知识约束" },
        "metric_box": {
          "shape": "Dark Navy (#1B3A5C) 1.5pt border, white fill",
          "exact_title_to_render_inside": "检验指标",
          "exact_text": "边界 F1 · 知识覆盖 · 属性错误率"
        },
        "connector": "One thin medium-blue arrow from the group of three condition boxes pointing RIGHT to the metric box. The three condition boxes themselves are NOT connected to each other by any arrow — they are parallel comparison conditions, not a sequence."
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text, including the side rail and lane titles.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. Only lanes and the bottom band may use light grey (#F7F7F7) fill.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E, #5BA0D0, plus neutral greys #8EAEC4, #333333, #4D4D4D, #CCCCCC.",
    "The two knowledge-source cards MUST connect to the constraint block via TWO lines that visibly MERGE into ONE before entering it. This converging arrow is the core visual statement of joint constraint and must be unmistakable.",
    "Exactly ONE focus element: the 资源单元 u = (c, a, m, e, s) container uses a 3.0pt dark navy border with enlarged surrounding whitespace. No other element may be emphasised.",
    "The five slot rows must be full-width, left-aligned, and vertically stacked in the exact order c, a, m, e, s. Each row has a left slot-name cell and a right content cell separated by a thin divider. No slot row may contain more than five content items.",
    "The three condition boxes in the bottom band MUST NOT be connected to each other by arrows. They are parallel comparison conditions; drawing them as a sequence would be a serious misreading.",
    "The Latin symbols u, c, a, m, e, s are rendered in Times italic; all Chinese text is sans-serif. Do NOT render any full equation, loss function, weighting coefficient, or summation.",
    "The 扩展 line inside slot m and the two dashed side notes use pale blue grey #8EAEC4 with 7pt text and must carry the lowest visual weight.",
    "Do NOT expand cross-modal relation scoring, gate logic, quality synthesis, VRR, or any execution sequence — those belong to other figures. Slot s shows only the three state labels.",
    "This figure must NOT read as a database table design. Keep the 描述模式 side rail and the 三条件对照 band prominent so the object reads as a testable scientific construct.",
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

```
A flat 2D vector academic schema diagram for a Chinese research grant proposal, on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: the research object of the project — a "resource unit" for university new-energy course materials — showing its five-field description schema and how industrial-task knowledge and course knowledge jointly constrain its boundary.

Composition: three vertical pale-grey lanes left to right, plus one full-width band at the bottom. The narrow left lane, titled 双知识源, holds two light-blue cards — 产业任务知识 listing 产业任务, 设备与工况, 运行参数, 告警条件, and 课程知识 listing 课程知识点, 能力目标, 先修关系, 资源类型 — with a small dashed pale-grey note between them reading 粒度差异 · 术语异名 · 属性冲突 → 记录候选关系与人工确认状态. From these two cards, two dark-navy lines visibly MERGE into a single line before entering the middle lane: this converging arrow is the central visual statement of the figure. The middle lane, titled 联合约束与边界优化, holds two dark-navy blocks stacked vertically — 联合知识约束打分 with rows 产业属性兼容, 课程属性兼容, 术语映射兼容 and a side note 权重于开发集确定, and 单元边界优化目标 with rows 抑制知识遗漏, 抑制重复, 抑制过度切分, 抑制专业属性错配. A thick arrow points right into the widest right lane, titled 资源单元描述模式, whose centre is the single visual focus: a container with a thick 3pt dark-navy border and generous white space, titled 资源单元 u = (c, a, m, e, s) with the Latin letters in Times italic, holding five full-width medium-blue slot rows in order — c 课程知识, a 专业属性, m 多模态片段及关系, e 来源位置, s 质量状态 — each split by a thin divider into a slot-name cell and a content cell. A narrow vertical rail on its right edge reads 描述模式：任务—对象—条件—知识点—片段—证据位置 in horizontal multi-line text, and a small dashed note reads 无证据属性 → 待核验队列.

The bottom band, titled 三条件对照, holds three parallel medium-blue boxes 无知识约束, 单一知识约束 仅产业知识 / 仅课程知识, 联合知识约束 with absolutely no arrows between them, and one thin arrow from the group to a dark-navy box 检验指标 reading 边界 F1 · 知识覆盖 · 属性错误率.

Supporting modules: sparse monochrome thin-grey line icons — factory with gear, open book.

Visual tone: restrained, scholarly, print-oriented. Material: white fills, coloured borders only, 3pt corner radius, borders 1.0/1.5/2.0/3.0pt. Palette strictly #1B3A5C, #2E6B9E, #5BA0D0 plus neutral greys — no warm, red, orange or brown tones.

Typography: Source Han Sans / Noto Sans CJK SC; lane titles 10pt bold, module titles 9.5pt bold, slot names 8.5pt, labels 8pt, notes 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: any full equation, loss function or coefficient; any relation-scoring, gate logic, VRR or execution sequence; any database-table styling; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 4:3.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 资源单元主体框（焦点）、约束块、边界优化块、检验指标框、汇聚箭头 |
| secondary | `#2E6B9E` | 五槽位行、约束项行、描述模式侧栏、三条件框 |
| tertiary | `#5BA0D0` | 双知识源卡片 |
| gray | `#8EAEC4` | 冲突注记、扩展模态行、待核验队列注记 |
| section_bg | `#F7F7F7` | 三条纵向泳道 + 底部对照带 |
| **禁用** | `#A64B2A` | 本图不含失败语义 |

**唯一焦点**：`资源单元 u = (c, a, m, e, s)` 五槽位主体框（3.0pt 边框 + 1.5× 留白）
**全套唯一汇聚箭头**：Kp + Kc → 联合约束（该形态在 F01–F07 中仅此一处）

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 4 资源单元描述模式与产业—课程知识联合约束。资源单元 $u=(c,a,m,e,s)$ 中，$c$、$a$、$m$、$e$、$s$ 分别表示课程知识、专业属性、多模态片段及关系、来源位置和质量状态。项目对片段与知识节点的匹配采用产业属性、课程属性与术语映射三项兼容性的加权组合，权重在开发集确定；单元边界目标同时约束知识遗漏、重复、过度切分与专业属性错配。通过无知识、单一知识与联合知识三个条件的比较，以边界 F1、知识覆盖与属性错误率检验联合约束的增量作用。
- 联合知识约束打分与单元边界损失的完整数学表达式 → 正文。
- 各权重系数符号与取值范围 → 正文。
- 术语异名与属性冲突的具体处理规则 → 正文。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（object schema + constraint mechanism） |
| 全部模块有标书出处 | ✅ 1.1 / 2.1(1) / 2.3(1) / 3.1 / 4.2 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 4:3 |
| 物理规格与字体块 | ✅ 183mm / 10-9.5-8.5-8-7pt / 1.0-1.5-2.0-3.0pt |
| 有彩色 ≤3 | ✅ 3 种 |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 双知识源图标 + 五槽位表结构锚点 |
| 无空壳模块 | ✅ 每槽位有内容项 |
| 负向约束齐备 | ✅ 含禁公式/禁表设计观感/禁三条件连箭头、NO emojis / NO 3D |
| 与 F02/F03/F05/F06 防重复 | ✅ 明确禁止展开关系评分、门控逻辑、VRR、执行序列 |
| 推断或待确认项 | 无。全部内容可溯源至标书 |
