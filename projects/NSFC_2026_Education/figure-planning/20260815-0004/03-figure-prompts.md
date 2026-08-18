# Figure Spec Package — NSFC_2026_Education（阶段三）

- `plan_version`: reviewed-v2（独立审核回写后；原 03 已失效重跑）
- `source_sha256`: `bfa044d1bc4bd44ab00e9c7b66f2937a0ec0a40cdb137d891ea7708ee0b770b1`
- `style_family`: `classic_academic`
- `selection_rule`: `decision=keep AND render_action=draw_new AND prompt_eligible=true AND blockers=[] AND unresolved_majors=[]`
- `selected_figures`: [F1, F2, F3, F5]
- `image_backend_calls`: 0
- `dependency_versions`: Academic Figure Prompt 1.5.0；Academic Figure Color Expert 1.3.2

本文件只交付 JSON spec 与英文 image prompt。禁止生图。中文 `exact_*` 标签按申报书原文锁定，英文 prompt 逐字保留这些中文，不翻译图内文字。

---

## 跨图视觉契约

### 术语与缩写（全图统一）

| 图内可见写法 | 含义 | 不得改写为 |
|---|---|---|
| 资源单元 | 教学资源单元 | 知识点包、学习对象 |
| \(u=(c,a,m,e,s)\) | 式 (1) | 五元组其他字母 |
| \(c\) / \(a\) / \(m\) / \(e\) / \(s\) | 课程知识 / 专业属性 / 片段及关系 / 来源位置 / 质量状态 | 随意英文全称 |
| \(\mathcal{K}_p\) / \(\mathcal{K}_c\) | 产业任务知识 / 课程知识 | 产业图谱、课标 |
| B0 人工 / B1 大模型 / B2 文本RAG / B3 完整方法 | 对照 | GPT、ChatGPT、SOTA |
| VRR | 有效资源单元通过率（只出名称） | 任何百分数 |
| 内容 / 课程 / 模态 / 证据 | 四层门控 | 正确性/时效性等误译 |
| 材料审查 / 知识结构与单元切分 / 跨模态关联 / 四层门控 / 独立验证 | §3.2 五阶段 | 「联合约束」作为第 2 阶段 |

### Palette Decision（全局，原样传给每张图）

```
style_family: classic_academic
skill: academic-figure-prompt
palette: Nature Blue
branch: scene  # hard constraint: framework ≥4 modules (F3 五阶段)
alternate: Blue Monochrome
accessibility: colorblind-safe; dual-encode with label + line style
primary:   #1B3A5C
secondary: #2E6B9E
tertiary:  #5BA0D0
gray:      #8EAEC4
text:      #333333
fill:      #FFFFFF
section_bg:#F7F7F7
border:    #CCCCCC
arrow:     #4D4D4D
```

每图最多 3 个色相：`#1B3A5C` / `#2E6B9E` / `#5BA0D0`，其余为中性灰与白。

### 语义颜色绑定（映射到 Nature Blue，不外加珊瑚/薄荷绿）

| 功能角色 | 边框色 | 线型 |
|---|---|---|
| Input / Data | `#5BA0D0` | 实线 |
| Backbone / Core method | `#1B3A5C` | 实线 |
| Constraint / Gate / Supervision | `#2E6B9E` | 实线 |
| Output / Target | `#1B3A5C` | 实线 |
| Extension / optional | `#8EAEC4` | 虚线 |
| Reject / 不入池 / 退回 | `#2E6B9E` | 虚线 + 文字，不加第四色相 |

### 共享渲染规则

- 白底、白填充、彩色描边；4–6 px 圆角；无渐变、无投影、无 3D。
- 主流程实线箭头 `#4D4D4D` 1.5 pt；反馈/扩展/不入池虚线 1.0 pt。
- 字体 Helvetica/Arial：title 10–12 pt bold，label 8–9 pt，note 6–7 pt。
- 图标：单色细线，置于块内标题旁；禁止 emoji、锁/火/闪电。
- 画布：F1/F3 为 183 mm 宽、16:9；F2 为 183 mm 宽、3:2；F5 为 183 mm 宽、4:3。
- 不推断缺失数值；公式长式、权重、300/120、阈值进 caption_reserve。

---

## F1 — 高校新能源多模态教学资源的双重约束、汇集失败与三项研究缺口

- `figure_id`: F1
- 中文图名：高校新能源多模态教学资源的双重约束、汇集失败与三项研究缺口
- `figure_type`: Overall Framework
- 目标章节：（一）1.4 之后、参考文献之前
- 证据锚点：E01, E02, E04, E05, E07, E08, E10, E11, E12（PDF p.1–3）
- `spec_format`: json
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
    "section_bg": "#F7F7F7",
    "main_block_color_palette": {
      "Input": "Light blue (#5BA0D0) 1.5pt solid border, white fill",
      "FailureMechanism": "Medium blue (#2E6B9E) 1.5pt solid border, white fill",
      "Gap": "Dark navy (#1B3A5C) 2pt solid border, white fill",
      "Entry": "Dark navy (#1B3A5C) 1.0pt dashed border, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left, Upper",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "产业任务约束",
      "exact_text": "设备名称 / 运行参数 / 告警条件",
      "icon": "small industrial equipment outline, monochrome line art",
      "flow": "Solid arrow RIGHT to 分散材料"
    },
    {
      "relative_position": "Far Left, Lower",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "课程知识约束",
      "exact_text": "知识点 / 能力目标 / 先修",
      "icon": "small document-with-list outline, monochrome line art",
      "flow": "Solid arrow RIGHT to 分散材料"
    },
    {
      "relative_position": "Left-Center",
      "shape": "Rounded container, #5BA0D0 1.5pt solid border, white fill, light #F7F7F7 interior band",
      "exact_title_to_render_inside": "分散材料",
      "internal_content": {
        "layout": "Three stacked equal-width white sub-boxes",
        "row_1": {
          "exact_label": "文本",
          "icon": "small document icon, monochrome line art"
        },
        "row_2": {
          "exact_label": "运行曲线",
          "icon": "small time-series waveform thumbnail, monochrome"
        },
        "row_3": {
          "exact_label": "设备图",
          "icon": "small image frame icon with diagonal cross, monochrome line art"
        }
      },
      "secondary_note": "多源异构",
      "flow": "Solid arrow RIGHT to 主题/相似度汇集"
    },
    {
      "relative_position": "Center",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "主题/相似度汇集",
      "icon": "two unlinked rectangles as a broken-chain geometric marker, monochrome",
      "exact_floating_text": "可检索但不可教学使用",
      "flow": "Solid arrow DOWN to failure pills, then RIGHT to 现有研究不足"
    },
    {
      "relative_position": "Center, below 主题/相似度汇集",
      "shape": "Five small rounded pills, #2E6B9E 1.0pt border, white fill, in one horizontal row",
      "exact_text": "变量",
      "internal_content": {
        "layout": "Five pills left to right",
        "pill_2": {"exact_text": "单位"},
        "pill_3": {"exact_text": "工况"},
        "pill_4": {"exact_text": "图文"},
        "pill_5": {"exact_text": "出处"}
      }
    },
    {
      "relative_position": "Right",
      "shape": "Rounded rectangle, #1B3A5C 2pt solid border, white fill",
      "exact_title_to_render_inside": "现有研究不足",
      "icon": "three stacked short bars, monochrome line art",
      "internal_content": {
        "layout": "Three left-aligned numbered lines",
        "row_1": {"exact_text": "1 缺单元层联合约束"},
        "row_2": {"exact_text": "2 语义相似 ≠ 可教关系"},
        "row_3": {"exact_text": "3 缺独立质量效度"}
      }
    },
    {
      "relative_position": "Bottom Center",
      "shape": "Wide thin bar, #1B3A5C 1.5pt solid border, white fill",
      "exact_text": "可检索 ≠ 可教学使用"
    },
    {
      "relative_position": "Bottom Right",
      "shape": "Rounded rectangle, #1B3A5C 1.0pt dashed border, white fill",
      "exact_title_to_render_inside": "研究切入",
      "internal_content": {
        "layout": "Three dark-navy pills connected by short solid arrows, left to right",
        "pill_1": {"exact_text": "联合知识约束"},
        "pill_2": {"exact_text": "跨模态证据关联"},
        "pill_3": {"exact_text": "四层质量验证"}
      },
      "secondary_note": "不展开方法"
    },
    {
      "relative_position": "Bottom Left footer",
      "shape": "Borderless",
      "exact_text": "不含学生数据 / 推荐 / 生产接入"
    },
    {
      "relative_position": "Bottom legend",
      "shape": "Borderless",
      "exact_label": "实线",
      "exact_floating_text": "问题叙事"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([Fixed] vs [Tune]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values.",
    "Do not render equations (1)-(8), B0-B3 names, VRR numbers, 300/120 counts, audio modality, or neural-network layer stacks."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing a conceptual overall framework of why scattered university new-energy teaching files cannot be auto-assembled into teachable resource units, on a pure white #FFFFFF canvas, 16:9. Industry-task constraints and curriculum-knowledge constraints act as two comparable filters; aggregating files by topic or similarity yields units that are retrievable but not teachable.

Composition is a single horizontal left-to-right narrative on a pale #F7F7F7 band, four panels aligned on one baseline with generous gaps and no overlapping. Far left: two stacked rounded rectangles with 1.5pt #5BA0D0 borders and white fill. Upper box title 「产业任务约束」 in 10-12pt bold, secondary line 「设备名称 / 运行参数 / 告警条件」, small industrial-equipment outline icon. Lower box title 「课程知识约束」, secondary line 「知识点 / 能力目标 / 先修」, small document-with-list icon. Two solid #4D4D4D arrows enter a taller left-center container titled 「分散材料」 holding three inner white sub-boxes in a vertical stack, not box-in-box beyond one level: 「文本」 with a document icon, 「运行曲线」 with a tiny time-series waveform thumbnail, 「设备图」 with an image-frame icon; a 7pt note 「多源异构」 sits under the stack. A solid arrow continues into a center #2E6B9E box titled 「主题/相似度汇集」 with a broken-chain geometric marker (two unlinked rectangles). Directly beneath, five small pills in one row read 「变量」「单位」「工况」「图文」「出处」. A solid arrow leads to the rightmost #1B3A5C 2pt box titled 「现有研究不足」 with a three-bar icon and three lines 「1 缺单元层联合约束」「2 语义相似 ≠ 可教关系」「3 缺独立质量效度」. A wide bottom-center bar reads 「可检索 ≠ 可教学使用」. Bottom-right dashed enclosure titled 「研究切入」 holds three pills 「联合知识约束」→「跨模态证据关联」→「四层质量验证」 and a tiny note 「不展开方法」. Footer left: 「不含学生数据 / 推荐 / 生产接入」. Legend: solid arrow = 「问题叙事」.

Nature Blue monochrome only: dark #1B3A5C, medium #2E6B9E, light #5BA0D0, arrows #4D4D4D. White fills, colored borders, 4-6px corners, 1.5pt containers, 1.0pt dividers. Canvas 183 mm. Helvetica/Arial. Thin 1.5px outlines, muted palette, labels readable at thumbnail size, clean grid alignment, no overlapping. NO emojis, NO lock/fire/lightning icons, NO 3D rendering, no gradients, no drop shadows. Do not infer or render missing values, formulas, B0-B3, VRR numbers, 300/120, audio, or network layers. Aspect ratio 16:9.

- `prompt_word_count`: 335
- palette: Nature Blue；hex `#1B3A5C` `#2E6B9E` `#5BA0D0`；branch: scene ≥4 modules
- `caption_reserve`: 项目全称；式 (1)–(8)；B0–B3；VRR 定义；300/120；四个知识模块全称；代码/案例扩展模态（本图不单列）
- `JSON_valid`: true

```yaml
completeness:
  analyzed_materials: [main.pdf p.1-3, reviewed-v2 F1]
  output_type: complete
  high_confidence_information: [双重约束, 三项缺口, 切入点三词, 排除边界]
  pending_confirmation: [PDF 未印题目]
  suggested_materials: [封面题目打印稿]
```

---

## F2 — 资源单元构造、内部关系与内在质量的递进研究框架

- `figure_id`: F2
- 中文图名：资源单元构造、内部关系与内在质量的递进研究框架
- `figure_type`: Overall Framework
- 目标章节：（一）2.3 之后、第 3 节之前
- 证据锚点：E03, E14, E15, E16, E19, E30（PDF p.6–11）
- `spec_format`: json
- `prompt_status`: ready

### JSON spec

```json
{
  "diagram_type": "Overall Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "3:2",
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
    "section_bg": "#F7F7F7",
    "main_block_color_palette": {
      "Object": "Dark navy (#1B3A5C) 2pt solid border, white fill",
      "Column": "Medium blue (#2E6B9E) 1.5pt solid border, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Center",
      "shape": "Rounded rectangle, #1B3A5C 2pt solid border, white fill",
      "exact_title_to_render_inside": "资源单元",
      "exact_text": "u = (c, a, m, e, s)",
      "icon": "small five-slot horizontal tuple bar, monochrome line art",
      "internal_content": {
        "layout": "Five tiny labelled slots under the formula",
        "slot_c": {"exact_label": "c 知识"},
        "slot_a": {"exact_label": "a 属性"},
        "slot_m": {"exact_label": "m 片段"},
        "slot_e": {"exact_label": "e 出处"},
        "slot_s": {"exact_label": "s 状态"}
      },
      "flow": "Three solid arrows DOWN into the three columns"
    },
    {
      "relative_position": "Middle Left column",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "① 单元构造",
      "icon": "two small linked circles labelled Kp and Kc, monochrome line art",
      "internal_content": {
        "layout": "Vertical stack",
        "row_1": {"exact_text": "问题一 联合约束何时有效"},
        "row_2": {"exact_text": "内容一 联合知识构建"},
        "row_3": {"exact_text": "创新一"},
        "row_4": {"exact_text": "无知识 / 仅产业 / 仅课程 / 联合"}
      },
      "flow": "Solid arrow RIGHT to column 2"
    },
    {
      "relative_position": "Middle Center column",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "② 单元内部关系",
      "icon": "four-node X-linked graph icon, monochrome line art",
      "internal_content": {
        "layout": "Vertical stack",
        "row_1": {"exact_text": "问题二 属性与出处如何约束"},
        "row_2": {"exact_text": "内容二 跨模态关联"},
        "row_3": {"exact_text": "创新二"},
        "row_4": {"exact_text": "无专业属性 / 无来源位置"}
      },
      "flow": "Solid arrow RIGHT to column 3"
    },
    {
      "relative_position": "Middle Right column",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "③ 资源内在质量",
      "icon": "2x2 grid of four small squares, monochrome line art",
      "internal_content": {
        "layout": "Vertical stack",
        "row_1": {"exact_text": "问题三 内在质量独立效度"},
        "row_2": {"exact_text": "内容三 四层验证"},
        "row_3": {"exact_text": "创新三"},
        "row_4": {"exact_text": "单层质量 / 四层联合"}
      },
      "flow": "Solid arrows DOWN from all three columns to footer"
    },
    {
      "relative_position": "Bottom footer",
      "shape": "Dashed wide bar, #1B3A5C 1.0pt dashed border, white fill",
      "exact_text": "评价入包，不评价学习效果"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([Fixed] vs [Tune]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values.",
    "Do not render the four knowledge-module full names, equations (2)-(8), B0-B3 full matrix, audio icons, or measured percentages."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing a research-content overall framework that maps three scientific questions onto three research tasks and three innovations around one resource unit, on a pure white #FFFFFF canvas, 3:2. Unit construction, intra-unit relations, and intrinsic quality form a progressive chain that shares one object but uses different contrasts.

Top center: a dark-navy #1B3A5C rounded rectangle titled 「资源单元」 with the single formula line 「u = (c, a, m, e, s)」, a five-slot tuple icon, and five 6-7pt slots 「c 知识」「a 属性」「m 片段」「e 出处」「s 状态」. Three solid #4D4D4D arrows drop into three equal-width columns with #2E6B9E 1.5pt borders, white fill, 6px corners, aligned on one grid. Left column titled 「① 单元构造」 with two linked circles Kp–Kc and lines 「问题一 联合约束何时有效」「内容一 联合知识构建」「创新一」「无知识 / 仅产业 / 仅课程 / 联合」. Center column titled 「② 单元内部关系」 with a four-node X-graph icon and 「问题二 属性与出处如何约束」「内容二 跨模态关联」「创新二」「无专业属性 / 无来源位置」. Right column titled 「③ 资源内在质量」 with a 2x2 four-square icon and 「问题三 内在质量独立效度」「内容三 四层验证」「创新三」「单层质量 / 四层联合」. Short solid arrows connect the three columns left to right. A dashed footer bar reads 「评价入包，不评价学习效果」. Do not draw a separate input-modality wall, four knowledge-module names, resource-package icons, or local-prototype boxes.

Nature Blue: #1B3A5C #2E6B9E #5BA0D0, arrows #4D4D4D. White fills, colored borders only, canvas 183 mm, Helvetica/Arial 10-12pt titles and 8-9pt labels, 1.5pt strokes. Clean grid, no overlapping, no nested boxes beyond one container. NO emojis, NO lock/fire/lightning icons, NO 3D rendering, no gradients, no shadows. Do not infer or render missing values, module full names, B0-B3 matrices, audio, layer stacks, or any measured scores. Aspect ratio 3:2.

- `prompt_word_count`: 259
- palette: Nature Blue；hex `#1B3A5C` `#2E6B9E` `#5BA0D0`；branch: scene ≥4 modules
- `caption_reserve`: 四个知识模块全称；受控输入模态墙；资源包 / 本地原型；式 (2)–(8)；B0–B3；300/120；创新点长标题
- `JSON_valid`: true

```yaml
completeness:
  analyzed_materials: [main.pdf p.6-11, reviewed-v2 F2]
  output_type: complete
  high_confidence_information: [三列对位, u 五元组, 四档知识对照]
  pending_confirmation: []
  suggested_materials: []
```

---

## F3 — 面向可追溯资源单元的五阶段技术路线与独立验证闭环

- `figure_id`: F3
- 中文图名：面向可追溯资源单元的五阶段技术路线与独立验证闭环
- `figure_type`: Overall Framework
- 目标章节：（一）3.2 段末
- 证据锚点：E13, E16, E26, E27（PDF p.9）；阶段名**只**用 §3.2；E29 仅进 caption
- `spec_format`: json
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
    "section_bg": "#F7F7F7",
    "main_block_color_palette": {
      "Input": "Light blue (#5BA0D0) 1.5pt solid border, white fill",
      "Stage": "Dark navy (#1B3A5C) 1.5pt solid border, white fill",
      "Gate": "Medium blue (#2E6B9E) 1.5pt solid border, white fill",
      "Reject": "Medium blue (#2E6B9E) 1.0pt dashed border, white fill",
      "Output": "Dark navy (#1B3A5C) 1.5pt solid border, white fill",
      "Extension": "Gray (#8EAEC4) 1.0pt dashed border, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left, vertical stack",
      "shape": "Four stacked rounded rectangles; first three #5BA0D0 solid, fourth #8EAEC4 dashed, white fill",
      "internal_content": {
        "layout": "Vertical stack labelled 输入",
        "row_1": {"exact_label": "课程文本", "icon": "small document icon, monochrome line art"},
        "row_2": {"exact_label": "运行图表", "icon": "small time-series waveform thumbnail, monochrome"},
        "row_3": {"exact_label": "设备图", "icon": "small image frame icon with diagonal cross, monochrome line art"},
                    "row_4": {"exact_label": "代码/案例", "secondary_note": "扩展", "icon": "small code-brackets outline, monochrome line art"}
      },
      "flow": "Solid arrows RIGHT into stage 1"
    },
    {
      "relative_position": "Top row, stage 1",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "1 材料审查",
      "exact_text": "许可 · 脱敏",
      "icon": "small clipboard-with-check outline, monochrome line art",
      "failure_branch": "Dashed arrow DOWN to 不入池",
      "flow": "Solid arrow RIGHT to stage 2"
    },
    {
      "relative_position": "Below stage 1",
      "shape": "Rounded rectangle, #2E6B9E 1.0pt dashed border, white fill",
      "exact_label": "不入池"
    },
    {
      "relative_position": "Top row, stage 2",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "2 知识结构与单元切分",
      "exact_text": "Kp + Kc",
      "icon": "two linked circles, monochrome line art",
      "flow": "Solid arrow RIGHT to stage 3"
    },
    {
      "relative_position": "Top row, stage 3",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "3 跨模态关联",
      "exact_text": "属性 + 出处",
      "icon": "four-node X-linked graph icon, monochrome line art",
      "failure_branch": "Dashed arrow DOWN to 人工核验",
      "flow": "Solid arrow RIGHT to stage 4"
    },
    {
      "relative_position": "Below stage 3",
      "shape": "Rounded rectangle, #2E6B9E 1.0pt dashed border, white fill",
      "exact_label": "人工核验",
      "flow": "Dashed arrow UP-RIGHT back toward stage 4"
    },
    {
      "relative_position": "Top row, stage 4",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "4 四层门控",
      "exact_text": "仅筛查",
      "icon": "2x2 grid of four small squares, monochrome line art",
      "internal_content": {
        "layout": "2x2 labels",
        "cell_1": {"exact_label": "内容"},
        "cell_2": {"exact_label": "课程"},
        "cell_3": {"exact_label": "模态"},
        "cell_4": {"exact_label": "证据"}
      },
      "flow": "Solid arrow RIGHT to stage 5"
    },
    {
      "relative_position": "Top row, stage 5",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "5 独立验证",
      "exact_text": "盲评 · 留出",
      "secondary_note": "隐藏方法条件",
      "icon": "small magnifying-glass over a checklist, monochrome line art",
      "failure_branch": "Dashed curved arrow LEFT-DOWN labelled 退回修改, landing at stage 2",
      "flow": "Solid arrow RIGHT to output"
    },
    {
      "relative_position": "Far Right",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "资源单元",
      "exact_text": "u = (c, a, m, e, s)",
      "icon": "small five-slot tuple bar, monochrome line art"
    },
    {
      "relative_position": "Bottom legend",
      "shape": "Borderless",
      "exact_floating_text": "实线 = 主流程；虚线 = 扩展 / 退回 / 不入池"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([Fixed] vs [Tune]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values.",
    "Stage 2 title MUST be exactly 知识结构与单元切分. NEVER render 联合约束 as the stage-2 title.",
    "Do not render B0-B3 capsules, ablation bars, or 自动初筛—专家复核 as a sixth pipeline stage.",
    "Do not render neural-network layer stacks, audio, filled metric bars, or any numeric VRR/Recall values."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing the five-stage technical route and independent-validation loop for building traceable teaching resource units, on a pure white #FFFFFF canvas, 16:9. Materials enter a gated pipeline: failed review never enters the pool, incomplete evidence goes to human checks, severe errors return for revision, and automatic gating is screening only.

Left column: four stacked input boxes. Solid #5BA0D0 boxes 「课程文本」 (document icon), 「运行图表」 (waveform thumbnail), 「设备图」 (image-frame icon); dashed #8EAEC4 box 「代码/案例」 with note 「扩展」. Solid #4D4D4D arrows enter a top row of five equal-width stage boxes. Stage 1 dark-navy box 「1 材料审查」 with clipboard icon and 「许可 · 脱敏」; a dashed arrow drops to a dashed box 「不入池」. Stage 2 dark-navy box MUST read exactly 「2 知识结构与单元切分」 with two linked circles and 「Kp + Kc」 — never retitle this stage as 联合约束. Stage 3 medium-blue box 「3 跨模态关联」 with X-graph icon and 「属性 + 出处」; a dashed arrow drops to 「人工核验」, which dashed-returns toward stage 4. Stage 4 medium-blue box 「4 四层门控」 with a 2x2 grid labelled 「内容」「课程」「模态」「证据」 and note 「仅筛查」. Stage 5 dark-navy box 「5 独立验证」 with magnifying-glass-over-checklist icon, 「盲评 · 留出」, and 「隐藏方法条件」. A dashed curved arrow labelled 「退回修改」 runs from stage 5 back to stage 2. Right: one output box titled 「资源单元」 with 「u = (c, a, m, e, s)」. Legend: 「实线 = 主流程；虚线 = 扩展 / 退回 / 不入池」. Do not draw B0–B3 capsules, an experiment-control bar, or any sixth fallback stage.

Nature Blue #1B3A5C #2E6B9E #5BA0D0, arrows #4D4D4D, canvas 183 mm, Helvetica/Arial, 1.5pt solid forward arrows, 1.0pt dashed feedback. White fills, 4-6px corners, clean alignment, no overlapping. NO emojis, NO lock/fire/lightning icons, NO 3D rendering, no gradients, no shadows. Do not infer or render missing values, metric numbers, audio, or layer stacks. Aspect ratio 16:9.

- `prompt_word_count`: 295
- palette: Nature Blue；hex `#1B3A5C` `#2E6B9E` `#5BA0D0`；branch: scene ≥4 modules
- `caption_reserve`: B0–B3 与消融（三线表）；「若自动门控与专家评价一致性不足，则自动初筛—专家复核」；式 (1)–(8) 全式；η/λ/θ 数值；300/120；E20 叙事五词不得替换阶段名
- `JSON_valid`: true

```yaml
completeness:
  analyzed_materials: [main.pdf p.9-10, extraTex/1.3.方案及可行性.tex, reviewed-v2 F3]
  output_type: complete
  high_confidence_information: [§3.2 五阶段原文, 三分流, 隐藏方法条件]
  pending_confirmation: []
  suggested_materials: []
```

---

## F5 — 专业属性与来源位置约束的跨模态关系判定

- `figure_id`: F5
- 中文图名：专业属性与来源位置约束的跨模态关系判定
- `figure_type`: Module Detail
- 目标章节：（一）3.1 式 (4)–(5) 附近
- 证据锚点：E08, E13, E15, E19, E23, E24（PDF p.2, p.6, p.8）
- `spec_format`: json
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
    "section_bg": "#F7F7F7",
    "main_block_color_palette": {
      "Input": "Light blue (#5BA0D0) 1.5pt solid border, white fill",
      "Core": "Dark navy (#1B3A5C) 2pt solid border, white fill",
      "Check": "Medium blue (#2E6B9E) 1.5pt solid border, white fill",
      "Reject": "Medium blue (#2E6B9E) 1.0pt dashed border, white fill",
      "Extension": "Gray (#8EAEC4) 1.0pt dashed border, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) solid arrows",
      "feedback_loop": "Dark Grey (#4D4D4D) dashed curved arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left column",
      "shape": "Three solid #5BA0D0 boxes plus one dashed #8EAEC4 box, white fill",
      "internal_content": {
        "layout": "Vertical stack",
        "row_1": {"exact_label": "文本", "icon": "small document icon, monochrome line art"},
        "row_2": {"exact_label": "设备图", "icon": "small image frame icon with diagonal cross, monochrome line art"},
        "row_3": {"exact_label": "运行曲线", "icon": "small time-series waveform thumbnail, monochrome"},
        "row_4": {"exact_label": "代码", "secondary_note": "扩展"}
      },
      "flow": "Solid arrows RIGHT into 属性提取"
    },
    {
      "relative_position": "Left-center strip",
      "shape": "Tall thin rounded rectangle, #5BA0D0 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "属性提取",
      "icon": "small tagged-field list icon, monochrome line art",
      "internal_content": {
        "layout": "Six stacked short labels",
        "row_1": {"exact_label": "对象"},
        "row_2": {"exact_label": "变量"},
        "row_3": {"exact_label": "单位"},
        "row_4": {"exact_label": "工况"},
        "row_5": {"exact_label": "时间窗口"},
        "row_6": {"exact_label": "来源位置"}
      },
      "flow": "Solid arrow RIGHT into core scoring block"
    },
    {
      "relative_position": "Upper center, small",
      "shape": "Small rounded rectangle, #8EAEC4 1.0pt dashed border, white fill",
      "exact_title_to_render_inside": "基础表示",
      "secondary_note": "对比学习",
      "icon": "small two-arrow alignment mark, monochrome line art, NOT a layer stack"
    },
    {
      "relative_position": "Center (largest block)",
      "shape": "Large rounded rectangle, #1B3A5C 2pt solid border, white fill",
      "exact_title_to_render_inside": "关系评分 R(i,j)",
      "exact_text": "sim + CA + CE + CR",
      "icon": "four parallel check-bars merging to one score node, monochrome line art",
      "internal_content": {
        "layout": "Four stacked check rows",
        "row_1": {"exact_text": "sim 语义"},
        "row_2": {"exact_text": "CA 专业属性"},
        "row_3": {"exact_text": "CE 来源位置"},
        "row_4": {"exact_text": "CR 关系类别"}
      },
      "flow": "Solid arrow RIGHT to decision diamond"
    },
    {
      "relative_position": "Right, decision",
      "shape": "Diamond, #2E6B9E 1.5pt solid border, white fill",
      "exact_text": "达阈值且来源完整",
      "branch_yes": "Solid arrow RIGHT to 写入资源单元",
      "branch_no": "Dashed arrow DOWN to reject box"
    },
    {
      "relative_position": "Far Right",
      "shape": "Rounded rectangle, #1B3A5C 1.5pt solid border, white fill",
      "exact_title_to_render_inside": "写入资源单元",
      "icon": "small inbox/tray outline, monochrome line art"
    },
    {
      "relative_position": "Right Lower",
      "shape": "Rounded rectangle, #2E6B9E 1.0pt dashed border, white fill",
      "exact_title_to_render_inside": "拒绝",
      "internal_content": {
        "layout": "Two lines",
        "row_1": {"exact_text": "专业条件错配"},
        "row_2": {"exact_text": "来源不可核查"}
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Adhere to typography hierarchy: titles 10-12pt bold, labels 8-9pt, tensor shapes 6-7pt.",
    "Adhere to stroke hierarchy: containers 1.5pt, dividers 1.0pt, arrows 1.5pt.",
    "Icons are monochrome thin grey line art. No colored icons.",
    "Weight status MUST use dashed/solid borders or subtle pill tags ([Fixed] vs [Tune]).",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "Feedback loop arrows are DASHED. Main forward flow arrows are SOLID.",
    "Flat vector style: no gradients, no 3D, no decorative shadows.",
    "Canvas is pure white (#FFFFFF).",
    "Do not infer or render missing values.",
    "Do not render Transformer/CNN layer stacks, audio modality, eta/tau numbers, full equation (4), or the five-stage technical route from F3."
  ]
}
```

### Image prompt

Flat vector academic module detail diagram showing how professional attributes and source locations turn semantic similarity into a writable cross-modal relation, on a pure white #FFFFFF canvas, 4:3. A candidate pair is written into the resource unit only when semantic similarity, attribute compatibility, source support, and relation type all pass.

Left-to-center-to-right mechanism, not a five-stage pipeline. Left: three solid #5BA0D0 boxes 「文本」 (document icon), 「设备图」 (image-frame icon), 「运行曲线」 (waveform thumbnail), and one dashed grey box 「代码」 with note 「扩展」. They feed a tall strip titled 「属性提取」 listing 「对象」「变量」「单位」「工况」「时间窗口」「来源位置」 with a tagged-field icon. A small dashed box above the core reads 「基础表示」 and 「对比学习」, using a two-arrow alignment mark — no neural layer stack. The large central #1B3A5C box is titled 「关系评分 R(i,j)」 with one core line 「sim + CA + CE + CR」 and four check rows 「sim 语义」「CA 专业属性」「CE 来源位置」「CR 关系类别」, plus a four-bar-merging-to-node icon. A diamond on the right reads 「达阈值且来源完整」: solid yes-arrow to 「写入资源单元」 (inbox icon); dashed no-arrow to 「拒绝」 containing 「专业条件错配」 and 「来源不可核查」. Do not draw a five-pill relation-type bar or a hard-negative example strip; those stay in the caption. Sparse math only: the short R(i,j) token line; full formulas stay off-figure.

Nature Blue #1B3A5C #2E6B9E #5BA0D0, arrows #4D4D4D, canvas 183 mm, Helvetica/Arial, titles 10-12pt, labels 8-9pt, 1.5pt borders, 4px corners, white fills. Clean alignment, no overlapping, no extra pipeline copied from the technical-route figure. NO emojis, NO lock/fire/lightning icons, NO 3D rendering, no gradients, no shadows. Do not infer or render missing values, eta/tau numbers, audio, or network layers. Aspect ratio 4:3.

- `prompt_word_count`: 257
- palette: Nature Blue；hex `#1B3A5C` `#2E6B9E` `#5BA0D0`；branch: scene ≥4 modules（Module Detail 的 alternate 为 Blue Monochrome，本套为跨图一致固定 Nature Blue）
- `caption_reserve`: 五种关系类型（解释、实例、计算/实验、对照、出处支持）；困难负例展开；式 (4) 全式；\(B,\tau,\eta\) 数值；网络维度；五阶段路线
- `JSON_valid`: true

```yaml
completeness:
  analyzed_materials: [main.pdf p.6 p.8, extraTex/1.3.方案及可行性.tex eq (5), reviewed-v2 F5]
  output_type: complete
  high_confidence_information: [四项检查, 写入/拒绝分流]
  pending_confirmation: [eta 数值不进图]
  suggested_materials: []
```

---

## 未生成 prompt 的图项

| figure_id | decision | render_action | prompt_eligible | 理由 |
|---|---|---|---|---|
| F4 | delete | no_figure | false | 对照×指标矩阵改为正文三线表；无实测数值 |
| F6 | delete | no_figure | false | 两年计划正文已清楚，绘图评审价值不足 |

无 Data Behavior prompt：申报书无已测曲线/柱高/热图数据。

---

## Manifest

| figure_id | decision | render_action | prompt_eligible | prompt_status | spec_format | JSON_valid | word_count | style_family |
|---|---|---|---|---|---|---|---:|---|
| F1 | keep | draw_new | true | ready | json | true | 335 | classic_academic |
| F2 | keep | draw_new | true | ready | json | true | 259 | classic_academic |
| F3 | keep | draw_new | true | ready | json | true | 295 | classic_academic |
| F4 | delete | no_figure | false | blocked | — | — | — | classic_academic |
| F5 | keep | draw_new | true | ready | json | true | 257 | classic_academic |
| F6 | delete | no_figure | false | blocked | — | — | — | classic_academic |

双向差集：选择集 {F1,F2,F3,F5} 与 prompt 集合 {F1,F2,F3,F5} 均为空差。

`image_backend_calls`: **0**

---

## completeness（阶段三总块）

```yaml
completeness:
  analyzed_materials:
    - reviewed-v2 Audited Figure Plan
    - main.pdf p.1-3, p.6-11 (re-read for exact labels)
    - extraTex/1.3.方案及可行性.tex (eq 1 and 5)
  output_type: complete
  high_confidence_information:
    - 4 ready JSON+prompt packages
    - F4/F6 blocked from prompts by design
    - Nature Blue global palette
  pending_confirmation:
    - PDF 未印中文题目
    - 独立子代理若补提 major，下游需失效重跑
  suggested_materials:
    - 封面题目打印稿
```
