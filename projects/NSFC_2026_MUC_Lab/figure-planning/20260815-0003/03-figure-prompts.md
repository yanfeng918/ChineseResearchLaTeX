# Figure Spec Package — NSFC_2026_MUC_Lab

- `plan_version`: reviewed-v2
- `source_pdf`: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_MUC_Lab/main.pdf`
- `source_sha256`: `5fae172cd362836662f99697a98f04855bc78938c0fb8939208ab82a54a9fa77`
- `style_family`: `classic_academic`
- `project_title_zh`: 场景文字增强的维吾尔语多模态表征融合与跨语言图像理解（用户 2026-08-15 确认）
- `title_on_figure`: false（超过 text budget；仅用于申请书题名与 LaTeX `\caption` 元数据）
- `baseline_codes`: B0=多语 CLIP 零样本；B1=无文字通道；B2=OCR—翻译流水线；完整模型无 B3（用户 2026-08-15 确认；图内不渲染）
- `image_backend_calls`: 0
- 选择式集合：`{F1, F2, F3, F5}`（与 prompt 集合双向差集为空）
- 未生成 prompt：F4、F6（`decision: delete` / `no_figure`）

---

## 跨图视觉契约

### Palette Decision

| 项 | 值 |
|---|---|
| Style family | classic academic（`academic-figure-prompt`；非 pastel） |
| Hard constraint | 框架模块数 ≥ 4 → **Nature Blue** |
| Branch | `scene`（module_count_framework = 5） |
| Alternate | Okabe-Ito |
| Accessibility | colorblind-safe；类别用边框深浅 + 标签双编码 |
| Venue | None（实验室开放课题） |
| Domain | 多模态表征 × 维吾尔语场景文字 × 跨语言图像理解 |

Hex（每图最多 3 个色相 + 中性色）：

- primary `#1B3A5C` / secondary `#2E6B9E` / tertiary `#5BA0D0`
- gray `#8EAEC4` / text `#333333` / fill `#FFFFFF` / section_bg `#F7F7F7` / border `#CCCCCC` / arrow `#4D4D4D`

### 语义角色绑定（四图共用）

| 角色 | 边框 | 用法 |
|---|---|---|
| Input / Data | `#5BA0D0` | 图像、文字区域、描述 |
| Backbone / Fusion | `#1B3A5C` | 缺口、门控 g、问题二列 |
| Output / Eval | `#2E6B9E` | 切入点、评价、sim、创新点二 |
| Frozen / Off | `#8EAEC4` 虚线 | fv/文本冻结、s=0 |
| Loss / Feedback | 虚线箭头 `#4D4D4D` | 不新增第四色相 |

### 术语与缩写锁

| 图内必须原样 | 禁止 |
|---|---|
| 物体外观、场景文字、图中是什么、图中写了什么 | 把已确认全称画进画面 |
| 缺口一/二/三；问题一/二/三；内容一/二/三；创新点一/二 | 创新点三 |
| 创新点仅两条 | 把问题三画成第三条创新 |
| fv, fs, g, s, v, z, h^ug, h^zh | 推断的张量形状 |
| SUST、RUST、Multi30k-Distant、CUTE/MC² 仅文本 | 把 B0/B1/B2 画进画面（对应已确认，仅作文注） |
| 200–400题拟构建 | 已有维语 VQA 库 |

中文 `exact_*` 标签保持中文；英文 prompt 逐字锁定这些字符串。

**B0–B2 对应（仅 caption / 正文表，不进 `exact_*`）**：B0=多语 CLIP 零样本；B1=无文字通道；B2=OCR—翻译流水线；完整模型在第二年、无 B3。

---

## F1  维语场景图的双通道语义与三项研究缺口

- `figure_id`: F1
- 中文图名：维语场景图的双通道语义与三项研究缺口
- 图类型：`Overall Framework`（`conceptual framework`）
- 目标章节：（一）1.4 研究切入点之后、参考文献之前（约 p.3）
- 证据锚点：E01, E02, E13, E14, E15, E16
- `spec_format`: json
- `prompt_word_count`: 311
- palette：Nature Blue；hex `#1B3A5C` / `#2E6B9E` / `#5BA0D0`；branch：`scene`（≥4 modules）
- `prompt_status`: ready

### JSON spec

```json
{
  "diagram_type": "Overall Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt monospace/italic"
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
    "palette_name": "Nature Blue",
    "main_block_color_palette": {
      "input": "Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "core": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "output": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "frozen": "Pale Blue-Gray (#8EAEC4) 1.5pt dashed border, white fill"
    },
    "neutrals": {
      "text": "#333333",
      "fill": "#FFFFFF",
      "section_bg": "#F7F7F7",
      "border": "#CCCCCC",
      "arrow": "#4D4D4D",
      "gray": "#8EAEC4"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) straight solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    },
    "semantic_binding": {
      "Input_Data": "#5BA0D0",
      "Backbone_Fusion": "#1B3A5C",
      "Output_Eval": "#2E6B9E",
      "Frozen": "#8EAEC4 dashed",
      "Loss": "dashed arrow #4D4D4D (no extra hue)"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left, 28% width",
      "shape": "Rounded rectangle, Light Blue (#5BA0D0) 1.5pt border, white fill, 6px radius",
      "exact_label": "双通道",
      "icon": "small image frame icon with diagonal cross, monochrome line art",
      "internal_content": {
        "layout": "Two stacked sub-boxes",
        "row_1": {
          "shape": "white fill, #5BA0D0 1.0pt border",
          "icon": "small filled square, monochrome",
          "exact_text": "物体外观"
        },
        "row_2": {
          "shape": "white fill, #5BA0D0 1.0pt border",
          "icon": "small rectangle with corner markers, monochrome",
          "exact_text": "场景文字"
        }
      },
      "flow": "Two solid arrows RIGHT to center gap stack"
    },
    {
      "relative_position": "Left, below dual-channel box",
      "shape": "Two small pills, #5BA0D0 1.0pt border, white fill",
      "exact_text": "图中是什么",
      "secondary_note": "图中写了什么",
      "caption_note": "Two questions sit as separate pills; second pill exact_text is 图中写了什么"
    },
    {
      "relative_position": "Center, 44% width, top",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 1.5pt border, white fill",
      "exact_title_to_render_inside": "缺口一",
      "exact_text": "检索缺文字通道",
      "secondary_note": "文字当纹理",
      "icon": "small image icon with grey grain overlay, monochrome, not a photo",
      "flow": "Vertical arrow DOWN to 缺口二"
    },
    {
      "relative_position": "Center, middle",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 1.5pt border, white fill",
      "exact_title_to_render_inside": "缺口二",
      "exact_text": "识别≠融合有用",
      "secondary_note": "丢掉物体",
      "icon": "small bounding-box icon only, monochrome",
      "flow": "Vertical arrow DOWN to 缺口三"
    },
    {
      "relative_position": "Center, bottom",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 1.5pt border, white fill",
      "exact_title_to_render_inside": "缺口三",
      "exact_text": "枢纽面向翻译",
      "secondary_note": "OCR后翻译",
      "icon": "small document-to-document arrow icon, monochrome",
      "flow": "Solid arrows RIGHT to entry-point column"
    },
    {
      "relative_position": "Right, 28% width, vertical stack",
      "shape": "Rounded rectangle container, Medium Blue (#2E6B9E) 1.5pt border, white fill, light section_bg #F7F7F7 behind",
      "exact_label": "切入点",
      "internal_content": {
        "layout": "Three stacked step boxes, top to bottom",
        "row_1": {
          "exact_text": "场景文字编码",
          "icon": "small bounding-box icon, monochrome"
        },
        "row_2": {
          "exact_text": "异构融合",
          "icon": "small gate merging two arrows, monochrome"
        },
        "row_3": {
          "exact_text": "跨语言检索与理解评价",
          "icon": "small magnifying-glass over two document icons, monochrome"
        }
      },
      "flow": "Downward solid arrows between the three steps; this column is a pointer only, not a full method pipeline"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([冻结] vs [训练]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values, hidden dimensions, measured metrics, or unstated mappings.",
    "Do not render CLIP/STR layer stacks, street-scene photographs, or a third innovation point."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing a conceptual-gap framework for Uyghur scene-image understanding on a pure white #FFFFFF canvas, 16:9. Natural-scene images contain both object appearance and Uyghur scene text; three existing research paths still cannot treat scene text as a falsifiable third channel for Uyghur–Chinese image understanding.

Horizontal left-to-right composition in three grouped regions on a very light #F7F7F7 section band. Left: a rounded rectangle with 1.5pt light-blue #5BA0D0 border and white fill, a small monochrome image-frame icon, exact_label 双通道. Inside, two stacked sub-boxes: exact_text 物体外观 with a filled-square marker, and exact_text 场景文字 with a bounding-box marker. Directly below, two small pills: exact_text 图中是什么 and exact_text 图中写了什么. Solid dark-grey #4D4D4D arrows run from the left stack into the center.

Center is the largest column: three equal-height rounded rectangles stacked vertically, each with 1.5pt dark-navy #1B3A5C border and white fill. Top: exact_title 缺口一, exact_text 检索缺文字通道, secondary_note 文字当纹理, tiny grain overlay icon (not a photograph). Middle: exact_title 缺口二, exact_text 识别≠融合有用, secondary_note 丢掉物体, bounding-box-only icon. Bottom: exact_title 缺口三, exact_text 枢纽面向翻译, secondary_note OCR后翻译, document-to-document icon. No extra failure-path boxes besides these three.

Right: a medium-blue #2E6B9E 1.5pt container labeled 切入点, three stacked steps with downward arrows: exact_text 场景文字编码, 异构融合, and 跨语言检索与理解评价. This column is a pointer only, not a system pipeline and not a network.

Nature Blue monochrome: dark #1B3A5C, medium #2E6B9E, light #5BA0D0, arrows #4D4D4D, text #333333. All boxes white fill, colored borders only, 6px corner radius, 1.5pt container strokes, 1.0pt dividers. Icons are monochrome thin line art in the block border color. Font: Helvetica/Arial, titles 10–12pt bold, labels 8–9pt, notes 6–7pt. Canvas 183mm wide. Clean grid alignment, no overlapping elements, no gradients, no drop shadows, no 3D. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Do not infer or render missing values, metrics, street photos, or CLIP/STR layer stacks. Exclusion notes stay in the caption, not on the figure. Aspect ratio 16:9.

### caption_reserve

- 不扩展翻译系统、语音、舆情（E04）
- SUST/RUST 与 Multi30k-Distant 不互相替代（E10, E11）
- 式 (1)–(6) 与任何实测指标
- 申请书题名（不进画面）：场景文字增强的维吾尔语多模态表征融合与跨语言图像理解

### completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf text layer at listed evidence pages
    - 02-figure-plan-review.md reviewed-v2
  output_type: complete
  high_confidence_information:
    - Chinese exact_* labels copied from audited must_show
    - Nature Blue hex and 4:3/16:9 from reviewed plan
    - 项目中文全称已由用户确认，不渲染在画面内
  pending_confirmation: []
  suggested_materials: []
```

---

## F2  三项问题、三项内容与两条创新的对应关系

- `figure_id`: F2
- 中文图名：三项问题、三项内容与两条创新的对应关系
- 图类型：`Overall Framework`（`research-content map`）
- 目标章节：（一）2.3 关键科学问题之后、第 3 节之前（约 p.8）
- 证据锚点：E17, E18, E19, E20, E21, E22, E32, E38
- `spec_format`: json
- `prompt_word_count`: 272
- palette：Nature Blue；hex `#1B3A5C` / `#2E6B9E` / `#5BA0D0`；branch：`scene`（≥4 modules）
- `prompt_status`: ready

### JSON spec

```json
{
  "diagram_type": "Overall Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt monospace/italic"
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
    "palette_name": "Nature Blue",
    "main_block_color_palette": {
      "input": "Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "core": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "output": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "frozen": "Pale Blue-Gray (#8EAEC4) 1.5pt dashed border, white fill"
    },
    "neutrals": {
      "text": "#333333",
      "fill": "#FFFFFF",
      "section_bg": "#F7F7F7",
      "border": "#CCCCCC",
      "arrow": "#4D4D4D",
      "gray": "#8EAEC4"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) straight solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    },
    "semantic_binding": {
      "Input_Data": "#5BA0D0",
      "Backbone_Fusion": "#1B3A5C",
      "Output_Eval": "#2E6B9E",
      "Frozen": "#8EAEC4 dashed",
      "Loss": "dashed arrow #4D4D4D (no extra hue)"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top-left, over column 1 only",
      "shape": "Rounded bar, Dark Navy (#1B3A5C) 1.5pt border, white fill",
      "exact_text": "创新点一",
      "icon": "small filled circle marker, monochrome"
    },
    {
      "relative_position": "Top, spanning columns 2 and 3",
      "shape": "Rounded bar, Medium Blue (#2E6B9E) 1.5pt border, white fill",
      "exact_text": "创新点二",
      "secondary_note": "创新点仅两条",
      "icon": "small two-segment bracket, monochrome"
    },
    {
      "relative_position": "Left column",
      "shape": "Rounded rectangle, Light Blue (#5BA0D0) 1.5pt border, white fill",
      "exact_title_to_render_inside": "问题一",
      "exact_text": "第三通道是否有用",
      "internal_content": {
        "row_below": {
          "exact_label": "内容一",
          "exact_text": "维语场景文字编码"
        },
        "product": {
          "exact_text": "s = 0 关闭"
        }
      },
      "icon": "small bounding-box icon, monochrome"
    },
    {
      "relative_position": "Middle column",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 1.5pt border, white fill",
      "exact_title_to_render_inside": "问题二",
      "exact_text": "融合会否互相干扰",
      "internal_content": {
        "row_below": {
          "exact_label": "内容二",
          "exact_text": "门控残差融合"
        }
      },
      "icon": "small gate merging two arrows, monochrome"
    },
    {
      "relative_position": "Right column",
      "shape": "Rounded rectangle, Medium Blue (#2E6B9E) 1.5pt border, white fill",
      "exact_title_to_render_inside": "问题三",
      "exact_text": "枢纽能否服务检索",
      "internal_content": {
        "row_below": {
          "exact_label": "内容三",
          "exact_text": "跨语言检索评价"
        }
      },
      "icon": "small two-document hub with a center image-frame icon, monochrome"
    },
    {
      "relative_position": "Bottom full width",
      "shape": "Three small pills in a row, #CCCCCC 1.0pt border, white fill",
      "exact_text": "去通道不降",
      "secondary_note": "门控双差",
      "exact_floating_text": "翻译不低于枢纽",
      "icon": "small dashed-arrow falsification marker, monochrome"
    },
    {
      "relative_position": "Bottom-right footnote, 6-7pt",
      "shape": "No box, caption-style note still on canvas as exact_text",
      "exact_text": "200–400题拟构建"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([冻结] vs [训练]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values, hidden dimensions, measured metrics, or unstated mappings.",
    "Do not render CLIP/STR layer stacks, street-scene photographs, or a third innovation point."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing a three-column research-content map on a pure white #FFFFFF canvas, 16:9. The map aligns three scientific questions with three research contents and only two innovation points, so the project is not read as another multilingual CLIP system.

Top of the canvas: a short dark-navy #1B3A5C bar sits only above the left column, exact_text 创新点一. A medium-blue #2E6B9E bar spans the middle and right columns, exact_text 创新点二, with a small pill secondary_note 创新点仅两条 and a two-segment bracket icon. Do not draw a third innovation bar.

Below, three equal-width rounded columns. Left, light-blue #5BA0D0 1.5pt border: exact_title 问题一, exact_text 第三通道是否有用, then exact_label 内容一 with exact_text 维语场景文字编码, and a product pill exact_text s = 0 关闭, plus a bounding-box icon. Middle, dark-navy #1B3A5C 1.5pt border: exact_title 问题二, exact_text 融合会否互相干扰, exact_label 内容二, exact_text 门控残差融合, gate-merging icon. Right, medium-blue #2E6B9E 1.5pt border: exact_title 问题三, exact_text 枢纽能否服务检索, exact_label 内容三, exact_text 跨语言检索评价, image-frame hub between two document icons. No baseline-name capsules and no encoder layer stacks inside columns.

Bottom row: three small grey-bordered pills, exact_text 去通道不降, secondary_note 门控双差, exact_floating_text 翻译不低于枢纽. Bottom-right 6–7pt exact_text 200–400题拟构建. No Recall numbers, no 29,000 split sizes, no SCI badge.

Nature Blue: #1B3A5C, #2E6B9E, #5BA0D0, arrows #4D4D4D, text #333333. White fills, colored borders only, 6px radius, 1.5pt outer strokes, 1.0pt inner dividers. Monochrome line-art icons. Font Helvetica/Arial, titles 10–12pt bold, labels 8–9pt, footnote 6–7pt. Canvas 183mm. Clean grid, generous spacing, no gradients, no shadows, no 3D. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Do not infer or render missing values. Full baseline names and ablation lists stay in the caption table, not on the figure. Aspect ratio 16:9.

### caption_reserve

- 三类基线与四消融全称（改正文三线表 / 原 F4）
- Train 29,000 / Val 1,014 / Test 1,000
- H1–H3 假设全文
- SCI / 资源包等产出形态

### completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf text layer at listed evidence pages
    - 02-figure-plan-review.md reviewed-v2
  output_type: complete
  high_confidence_information:
    - Chinese exact_* labels copied from audited must_show
    - Nature Blue hex and 4:3/16:9 from reviewed plan
    - 项目中文全称已由用户确认，不渲染在画面内
  pending_confirmation: []
  suggested_materials: []
```

---

## F3  编码—融合—评价技术路线与三张可检验节点表

- `figure_id`: F3
- 中文图名：编码—融合—评价技术路线与三张可检验节点表
- 图类型：`Overall Framework`（`technical route`）
- 目标章节：（一）3.2 技术路线段末（约 p.9）
- 证据锚点：E18, E20, E28, E29, E31
- `spec_format`: json
- `prompt_word_count`: 300
- palette：Nature Blue；hex `#1B3A5C` / `#2E6B9E` / `#5BA0D0`；branch：`scene`（≥4 modules）
- `prompt_status`: ready

### JSON spec

```json
{
  "diagram_type": "Overall Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt monospace/italic"
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
    "palette_name": "Nature Blue",
    "main_block_color_palette": {
      "input": "Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "core": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "output": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "frozen": "Pale Blue-Gray (#8EAEC4) 1.5pt dashed border, white fill"
    },
    "neutrals": {
      "text": "#333333",
      "fill": "#FFFFFF",
      "section_bg": "#F7F7F7",
      "border": "#CCCCCC",
      "arrow": "#4D4D4D",
      "gray": "#8EAEC4"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) straight solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    },
    "semantic_binding": {
      "Input_Data": "#5BA0D0",
      "Backbone_Fusion": "#1B3A5C",
      "Output_Eval": "#2E6B9E",
      "Frozen": "#8EAEC4 dashed",
      "Loss": "dashed arrow #4D4D4D (no extra hue)"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top row, left third",
      "shape": "Rounded rectangle, Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "编码",
      "exact_text": "SUST 训 fs",
      "secondary_note": "RUST 确认",
      "icon": "small bounding-box icon, monochrome",
      "exact_status": "[训练]",
      "flow": "Solid arrow RIGHT to 融合"
    },
    {
      "relative_position": "Top row, middle third",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "融合",
      "exact_text": "训练 g",
      "secondary_note": "冻结或低学习率",
      "icon": "small gate merging two arrows, monochrome",
      "internal_content": {
        "fv_text": {
          "exact_label": "fv / 文本",
          "exact_status": "[冻结]",
          "shape": "Pale Blue-Gray (#8EAEC4) dashed 1.5pt border, white fill"
        }
      },
      "flow": "Solid arrow RIGHT to 评价"
    },
    {
      "relative_position": "Top row, right third",
      "shape": "Rounded rectangle, Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "评价",
      "exact_text": "Multi30k-Distant",
      "secondary_note": "检索+理解协议",
      "icon": "small magnifying-glass over a document, monochrome",
      "flow": "None to the right"
    },
    {
      "relative_position": "Below 编码",
      "shape": "Small table thumbnail, #1B3A5C 1.0pt border, white fill",
      "exact_title_to_render_inside": "表1",
      "exact_text": "通道是否可用",
      "icon": "small empty 2x2 table grid thumbnail, no numbers, monochrome"
    },
    {
      "relative_position": "Below 评价, left of pair",
      "shape": "Small table thumbnail, #2E6B9E 1.0pt border, white fill",
      "exact_title_to_render_inside": "表2",
      "exact_text": "检索是否提高",
      "icon": "small empty 2x2 table grid thumbnail, no numbers, monochrome"
    },
    {
      "relative_position": "Below 评价, right of pair",
      "shape": "Small table thumbnail, #2E6B9E 1.0pt border, white fill",
      "exact_title_to_render_inside": "表3",
      "exact_text": "去s是否回落",
      "icon": "small empty 2x2 table grid thumbnail, no numbers, monochrome"
    },
    {
      "relative_position": "Bottom dashed feedback from 表1/表2/表3 back to the matching stage",
      "shape": "Dashed curved arrow #4D4D4D",
      "exact_floating_text": "只收缩对应假设",
      "flow": "Dashed feedback; do not rewrite the other two tables"
    },
    {
      "relative_position": "Far-left side path into 融合 only",
      "shape": "Dotted #8EAEC4 1.0pt box, white fill",
      "exact_text": "CUTE/MC² 仅文本",
      "icon": "small document icon, monochrome",
      "flow": "Dotted arrow into text-encoder slot of 融合; no arrow into 评价"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([冻结] vs [训练]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values, hidden dimensions, measured metrics, or unstated mappings.",
    "Do not render CLIP/STR layer stacks, street-scene photographs, or a third innovation point."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing the encoding–fusion–evaluation technical route on a pure white #FFFFFF canvas, 16:9. The route first confirms a Uyghur scene-text encoder, then trains a gated fusion head under frozen or low-learning-rate backbones, then evaluates on Multi30k-Distant; three empty checkpoint tables decide which hypothesis to shrink.

Top row, left to right, three large rounded stages connected by solid dark-grey #4D4D4D arrows. Left, light-blue #5BA0D0 solid border, exact_title 编码, exact_text SUST 训 fs, secondary_note RUST 确认, bounding-box icon, small [训练] pill. Middle, dark-navy #1B3A5C solid border, exact_title 融合, exact_text 训练 g, secondary_note 冻结或低学习率, gate icon; nested dashed pale #8EAEC4 box with exact_label fv / 文本 and [冻结] pill. Right, medium-blue #2E6B9E solid border, exact_title 评价, exact_text Multi30k-Distant, secondary_note 检索+理解协议, magnifying-glass icon. Do not draw CLIP/STR layer stacks inside stages.

Below 编码: a small empty table thumbnail exact_title 表1, exact_text 通道是否可用. Below 评价: two empty table thumbnails exact_title 表2 with exact_text 检索是否提高, and exact_title 表3 with exact_text 去s是否回落. Table grids contain no numbers, bars, or stars. A dashed curved #4D4D4D arrow returns from the tables with exact_floating_text 只收缩对应假设, meaning a failed node shrinks only its own claim.

Far left, a dotted pale box exact_text CUTE/MC² 仅文本 with a document icon and a dotted arrow into the text-encoder slot of 融合 only, never into 评价. No year timeline, no B0–B2 codes, no four-baseline capsules.

Nature Blue: #1B3A5C, #2E6B9E, #5BA0D0, frozen #8EAEC4 dashed, arrows #4D4D4D, text #333333. White fills, colored borders only, 6px radius, 1.5pt solids, 1.0pt dividers, dashed feedback 1.0pt. Monochrome line-art icons. Font Helvetica/Arial, titles 10–12pt bold, labels 8–9pt, pills 7–8pt. Canvas 183mm. Clean grid, no gradients, no shadows, no 3D. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Do not infer or render missing values. Contrast and ablation full names stay in a caption table. Aspect ratio 16:9.

### caption_reserve

- 四对照与四消融全称
- 已确认代号（不进画面）：B0=多语 CLIP 零样本；B1=无文字通道；B2=OCR—翻译流水线；完整模型无 B3
- 「不新造基础模型」散文
- 表内任何数值

### completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf text layer at listed evidence pages
    - 02-figure-plan-review.md reviewed-v2
  output_type: complete
  high_confidence_information:
    - Chinese exact_* labels copied from audited must_show
    - Nature Blue hex and 4:3/16:9 from reviewed plan
    - 项目中文全称已由用户确认，不渲染在画面内
  pending_confirmation: []
  suggested_materials: []
```

---

## F5  可关闭文字通道的门控残差融合与分通道对齐

- `figure_id`: F5
- 中文图名：可关闭文字通道的门控残差融合与分通道对齐
- 图类型：`Module Detail`（`mechanism / key method`）
- 目标章节：（一）3.1 研究方法，式 (2)–(5) 附近（约 p.8）
- 证据锚点：E18, E23, E24, E25, E26, E30
- `spec_format`: json
- `prompt_word_count`: 303
- palette：Nature Blue；hex `#1B3A5C` / `#2E6B9E` / `#5BA0D0`；branch：`scene`（≥4 modules）
- `prompt_status`: ready

### JSON spec

```json
{
  "diagram_type": "Module Detail",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt monospace/italic"
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
    "palette_name": "Nature Blue",
    "main_block_color_palette": {
      "input": "Light Blue (#5BA0D0) 1.5pt solid border, white fill",
      "core": "Dark Navy (#1B3A5C) 1.5pt solid border, white fill",
      "output": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "frozen": "Pale Blue-Gray (#8EAEC4) 1.5pt dashed border, white fill"
    },
    "neutrals": {
      "text": "#333333",
      "fill": "#FFFFFF",
      "section_bg": "#F7F7F7",
      "border": "#CCCCCC",
      "arrow": "#4D4D4D",
      "gray": "#8EAEC4"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) straight solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    },
    "semantic_binding": {
      "Input_Data": "#5BA0D0",
      "Backbone_Fusion": "#1B3A5C",
      "Output_Eval": "#2E6B9E",
      "Frozen": "#8EAEC4 dashed",
      "Loss": "dashed arrow #4D4D4D (no extra hue)"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left column, top",
      "shape": "Rounded rectangle, Light Blue (#5BA0D0) 1.5pt border, white fill",
      "exact_label": "I",
      "icon": "small image frame icon with diagonal cross, monochrome",
      "flow": "Arrow RIGHT to fv"
    },
    {
      "relative_position": "Left column, middle",
      "shape": "Rounded rectangle, Light Blue (#5BA0D0) 1.5pt border, white fill",
      "exact_label": "{tk}",
      "secondary_note": "连写 RTL",
      "icon": "small rectangle with corner markers, monochrome",
      "flow": "Arrow RIGHT to fs"
    },
    {
      "relative_position": "Left column, bottom",
      "shape": "Two stacked pills, Light Blue (#5BA0D0) 1.5pt border, white fill",
      "exact_text": "y^ug",
      "secondary_note": "y^zh",
      "icon": "small document icon, monochrome",
      "flow": "Arrows RIGHT to f_ell"
    },
    {
      "relative_position": "Left-center encoder column",
      "shape": "Three small white boxes, #5BA0D0 1.0pt border",
      "exact_text": "fv → v",
      "exact_floating_text": "fs → s",
      "secondary_note": "fℓ → hℓ",
      "icon": "small stacked feature-map rectangles, monochrome, no internal layers"
    },
    {
      "relative_position": "Beside s",
      "shape": "Small switch pill, #8EAEC4 dashed border, white fill",
      "exact_text": "s = 0",
      "secondary_note": "通道关闭",
      "icon": "small open-gate icon, monochrome"
    },
    {
      "relative_position": "Center large",
      "shape": "Rounded rectangle, Dark Navy (#1B3A5C) 2.0pt border, white fill",
      "exact_title_to_render_inside": "g(v, s)",
      "exact_text": "z=v+α σ(W[v;s])⊙s",
      "icon": "small gate merging a solid appearance arrow with a gated text arrow, monochrome",
      "flow": "Solid arrow RIGHT to sim"
    },
    {
      "relative_position": "Right",
      "shape": "Rounded rectangle, Medium Blue (#2E6B9E) 1.5pt border, white fill",
      "exact_title_to_render_inside": "sim(z, h)",
      "icon": "small cosine-bracket geometric mark, monochrome"
    },
    {
      "relative_position": "Bottom band",
      "shape": "Three dashed-border pills, #2E6B9E 1.0pt dashed, white fill",
      "exact_text": "Lv→t",
      "secondary_note": "Ls→t",
      "exact_floating_text": "Lhub",
      "icon": "small dashed feedback arrows from h and z, monochrome",
      "flow": "Dashed arrows indicating supervision, not extra modules"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([冻结] vs [训练]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values, hidden dimensions, measured metrics, or unstated mappings.",
    "Do not render CLIP/STR layer stacks, street-scene photographs, or a third innovation point."
  ]
}
```

### Image prompt

Flat vector academic module detail diagram showing closable gated-residual fusion for Uyghur scene-text and appearance features on a pure white #FFFFFF canvas, 4:3. Appearance, scene-text regions, and Uyghur/Chinese captions enter separate encoders; the text channel can be zeroed so ablation stays clean; the fused vector is a residual on appearance, not a forced concatenation.

Left column, top to bottom: a light-blue #5BA0D0 box exact_label I with an image-frame icon; a second box exact_label {tk} with secondary_note 连写 RTL and a bounding-box icon; two stacked pills exact_text y^ug and secondary_note y^zh with a document icon. Mid-left, three compact encoder labels only, no layer stacks: exact_text fv → v, exact_floating_text fs → s, secondary_note fℓ → hℓ, each with a tiny stacked-rectangle icon. Beside s, a dashed pale pill exact_text s = 0, secondary_note 通道关闭, open-gate icon.

Center is the largest block, dark-navy #1B3A5C 2.0pt border, exact_title g(v, s), one-line exact_text z=v+α σ(W[v;s])⊙s, gate icon merging a solid appearance arrow with a gated text arrow. A solid #4D4D4D arrow exits right to a medium-blue #2E6B9E box exact_title sim(z, h) with a small cosine geometric mark. Do not print InfoNCE expanded, tau, lambda, W shapes, or hidden dimensions.

Bottom band: three dashed medium-blue pills exact_text Lv→t, secondary_note Ls→t, exact_floating_text Lhub, with dashed supervision arrows only. No concat-versus-InfoNCE comparison boxes, no CLIP/STR internals, no numeric axes.

Nature Blue: #1B3A5C core, #2E6B9E output/loss pills, #5BA0D0 inputs, frozen/off channel #8EAEC4 dashed, arrows #4D4D4D, text #333333. White fills, colored borders only, 4–6px radius, 1.5pt boxes (center 2.0pt), 1.0pt dashed losses. Monochrome line-art icons. Font Helvetica/Arial, titles 10–12pt bold, labels 8–9pt, formula 7–8pt italic. Canvas 183mm. Clean alignment, no gradients, no shadows, no 3D. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Do not infer or render missing values. Full InfoNCE and parameter lists stay in the caption. Aspect ratio 4:3.

### caption_reserve

- 式 (4) 完整 InfoNCE
- τ、批大小、λ 数值、W 尺寸、隐藏维度
- CLIP/STR 层名
- 拼接 / 单 InfoNCE / 门控双对齐的比较句

### completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf text layer at listed evidence pages
    - 02-figure-plan-review.md reviewed-v2
  output_type: complete
  high_confidence_information:
    - Chinese exact_* labels copied from audited must_show
    - Nature Blue hex and 4:3/16:9 from reviewed plan
    - 项目中文全称已由用户确认，不渲染在画面内
  pending_confirmation: []
  suggested_materials: []
```

---

## 未生成 prompt 的图项

| figure_id | decision | render_action | prompt_eligible | prompt_status | 理由 |
|---|---|---|---|---|---|
| F4 | delete | no_figure | false | blocked | 空矩阵宜正文三线表；与路线图验证清单重复 |
| F6 | delete | no_figure | false | blocked | 两年计划正文已清楚；B0–B2/H1–H3 仅点名 |

---

## Manifest

| figure_id | decision | render_action | prompt_eligible | prompt_status | spec_format | JSON_valid | word_count | style_family |
|---|---|---|---|---|---|---|---:|---|
| F1 | keep | draw_new | true | ready | json | true | 311 | classic_academic |
| F2 | keep | draw_new | true | ready | json | true | 272 | classic_academic |
| F3 | keep | draw_new | true | ready | json | true | 300 | classic_academic |
| F5 | keep | draw_new | true | ready | json | true | 303 | classic_academic |
| F4 | delete | no_figure | false | blocked | — | — | — | classic_academic |
| F6 | delete | no_figure | false | blocked | — | — | — | classic_academic |

- 选择集 `{F1,F2,F3,F5}` − prompt 集 `{F1,F2,F3,F5}` = ∅
- prompt 集 − 选择集 = ∅
- `image_backend_calls`: **0**
- 终检：JSON 可解析；可见中文只出现在 `exact_*`；AR 与 reviewed-v2 一致（F1/F2/F3 = 16:9，F5 = 4:3）；未恢复 F4/F6；未推断维度/数值/第三条创新。

