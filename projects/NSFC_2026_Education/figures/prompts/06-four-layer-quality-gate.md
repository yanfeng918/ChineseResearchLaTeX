# F06 · 四层资源内在质量门控与独立效度验证图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：四层资源内在质量门控与独立效度验证图 ｜ **类型**：Layered Gate + Independent Validity Closure Diagram
> **状态**：RECOMMENDED ｜ **优先级**：P1 ｜ **长宽比**：4:3

---

## 一、图形目的（Diagram Purpose）

说明创新点三的**质量判定与效度检验机制**：内容、课程、模态、证据四层各自识别不同错误类型，串行否决后合成单元级验收判定与主指标 VRR；其效度由**与自动门控设计相互独立**的专家盲评、跨来源留出与人工修订记录检验。

**一句话结论**：四层门控只回答"资源单元是否具备进入资源包的内在条件"，其可信性来自与门控设计相互独立的专家盲评与跨来源留出，而非模型自身打分。

**填补的信息缺口**：技术路线图中 S4 仅显示四个层名与一条拒绝规则；总体框架图中"研究内容三"仅三行标签。各层检查对象、质量合成、主指标定义与独立效度闭环在两图中均不存在。

**形态强制约束**：本图采用**纵向堆叠的直角层栈**，自上而下；跨模态关联机制图（F05）采用横向串联闸门。两图流向正交，不得视觉雷同。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Four-Layer Quality Gate with Independent Validity Closure Diagram",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits; Times italic for the symbols Q(u), P(u), VRR",
    "font_hierarchy": {
      "zone_title": "10pt bold",
      "layer_name": "9.5pt bold",
      "primary_label": "8pt regular",
      "secondary_note": "7pt regular"
    },
    "stroke_hierarchy": {
      "layer_border": "2.0pt solid",
      "module_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "main_flow_arrow": "2.0pt solid with 4px head",
      "reject_arrow": "1.2pt DASHED with 3px head",
      "comparison_arrow": "1.2pt solid DOUBLE-HEADED",
      "recalibration_arrow": "1.0pt dashed",
      "independence_boundary": "1.5pt DASHED"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue with restricted warning accent (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #A64B2A (the warning accent REPLACES the usual light blue in this figure)",
    "main_block_color_palette": {
      "layer_bar": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners (0pt radius), wide and short",
      "synthesis_block": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, 3pt corner radius",
      "vrr_block": "FOCUS: Dark Navy (#1B3A5C) 3.0pt solid border, white fill, 3pt corner radius, 1.5x surrounding whitespace",
      "module_box": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill, 3pt corner radius",
      "reject_box": "Warm Brick (#A64B2A) 1.5pt DASHED border, white fill",
      "independence_boundary": "Dark Navy (#1B3A5C) 1.5pt DASHED border, no fill — a large enclosing frame",
      "scope_note": "Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill",
      "band_container": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border"
    },
    "text_colors": {
      "zone_title": "#1B3A5C",
      "layer_name": "#1B3A5C",
      "module_title": "#2E6B9E",
      "body_label": "#333333",
      "reject_label": "#A64B2A",
      "de_emphasised_label": "#4D4D4D"
    },
    "flow_arrow_colors": {
      "main_serial_flow": "Dark Navy (#1B3A5C) 2.0pt solid, filled head, running strictly TOP to BOTTOM through the four layers",
      "reject_exit": "Warm Brick (#A64B2A) 1.2pt DASHED, exiting RIGHT from each layer, terminating in a small solid dot",
      "consistency_comparison": "Dark Navy (#1B3A5C) 1.2pt solid DOUBLE-HEADED arrow — the ONLY double-headed arrow permitted in the entire figure set",
      "recalibration": "Dark Grey (#4D4D4D) 1.0pt dashed, curving back upward"
    },
    "dual_encoding_rule": "Every warm-brick element MUST also use a dashed stroke AND an explicit Chinese label, so the figure remains readable in pure greyscale print.",
    "independence_rule": "The automatic-gating side and the expert side use the SAME dark navy colour. Their independence is conveyed ONLY by the dashed enclosing boundary and spatial separation, never by colour difference, so that neither side appears subordinate to the other."
  },
  "layout_and_content_blocks": [
    {
      "id": "ZONE_LAYER_STACK",
      "relative_position": "Top section, centred, occupies top 42% of canvas",
      "shape": "Four wide short SQUARE-CORNERED horizontal bars stacked vertically, joined by one thick dark navy arrow running top to bottom",
      "exact_zone_title": "四层质量门控",
      "internal_content": {
        "layout": "Each bar has a left cell holding the layer name and a right cell holding the check target, separated by a 1.0pt divider",
        "layer_1": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners",
          "exact_layer_name": "内容层",
          "exact_text": "事实与参数正确性"
        },
        "layer_2": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners",
          "exact_layer_name": "课程层",
          "exact_text": "知识点与能力目标对齐"
        },
        "layer_3": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners",
          "exact_layer_name": "模态层",
          "exact_text": "跨模态对象与条件一致"
        },
        "layer_4": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill, SQUARE corners",
          "exact_layer_name": "证据层",
          "exact_text": "原始出处支持关键断言"
        },
        "evidence_side_note": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill, attached to the LEFT of layer_4",
          "exact_title_to_render_inside": "证据支持度",
          "exact_text": "文本支持 · 其他模态支持 · 知识关系支持",
          "secondary_note": "不达阈值 → 人工核验"
        },
        "rule_bar": {
          "shape": "No border, floating text to the right of the stack, aligned with all four reject exits",
          "exact_floating_text": "任一层严重错误即拒绝，并保留拒绝原因"
        }
      },
      "reject_branch": {
        "shape": "One Warm Brick (#A64B2A) 1.5pt DASHED border white box on the right side, receiving all four exits",
        "exact_text": "拒绝并保留原因",
        "connector": "Four short warm-brick 1.2pt DASHED arrows, one exiting RIGHT from each layer bar, all right-aligned, each terminating in a small solid dot before entering the reject box"
      },
      "flow": "One thick dark navy arrow from the bottom of layer_4 pointing DOWN into ZONE_SYNTHESIS"
    },
    {
      "id": "ZONE_SYNTHESIS",
      "relative_position": "Middle section, centred, occupies 22% of canvas",
      "shape": "One Dark Navy (#1B3A5C) 2.0pt border white block, with a three-state output row beneath",
      "exact_zone_title": "单元级判定",
      "internal_content": {
        "synthesis_block": {
          "exact_title_to_render_inside": "四层质量合成 Q(u)",
          "title_typography": "Q(u) in Times italic, Chinese in sans-serif",
          "internal_layout": "Two medium-blue rows",
          "row_1": { "exact_text": "内容 · 课程 · 模态 · 证据 加权" },
          "row_2": { "exact_text": "惩罚项 P(u)：参数矛盾 · 来源不可追溯 · 未授权或隐私风险" }
        },
        "admission_rule": {
          "shape": "No border, floating text",
          "exact_floating_text": "字段完整 ∧ 无严重错误 ∧ 质量分达阈值"
        },
        "output_row": {
          "layout": "Three boxes side by side",
          "out_1": { "shape": "Dark Navy (#1B3A5C) 1.5pt border, white fill", "exact_text": "通过 → 进入资源包" },
          "out_2": { "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill", "exact_text": "待核验 → 人工复核" },
          "out_3": { "shape": "Warm Brick (#A64B2A) 1.5pt DASHED border, white fill", "exact_text": "拒绝 → 保留原因" }
        }
      },
      "flow": "One thick dark navy arrow pointing DOWN-LEFT into the VRR block inside ZONE_CLOSURE"
    },
    {
      "id": "ZONE_CLOSURE",
      "relative_position": "Bottom section, full width, occupies bottom 30% of canvas, split into a LEFT automatic side and a RIGHT expert side",
      "shape": "Horizontal band, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "独立效度验证",
      "internal_content": {
        "left_automatic_side": {
          "vrr_block": {
            "shape": "FOCUS: Dark Navy (#1B3A5C) 3.0pt solid border, white fill, extra whitespace on all sides",
            "exact_title_to_render_inside": "主指标 VRR",
            "title_typography": "VRR in Times italic",
            "exact_text": "有效资源单元通过率\\n四层均通过的单元占比",
            "secondary_note": "权重与阈值仅在开发集确定，测试集冻结"
          }
        },
        "independence_boundary": {
          "shape": "A LARGE Dark Navy (#1B3A5C) 1.5pt DASHED enclosing frame drawn around the ENTIRE right side only, clearly separating it from the left automatic side",
          "exact_boundary_label": "与门控设计相互独立",
          "label_position": "on the top edge of the dashed frame"
        },
        "right_expert_side": {
          "layout": "Three medium-blue boxes stacked vertically inside the dashed independence frame",
          "box_blind_review": {
            "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
            "icon": "person outline with rating bars, thin grey line art",
            "exact_title_to_render_inside": "独立专家盲评",
            "exact_text": "拟邀请不少于 3 名未参与资源构建的教师\\n量表制定者不参与正式评分 · 评分隐藏方法条件",
            "five_dimension_row": {
              "layout": "Five small chips in one row",
              "exact_chips": "内容与事实正确性 | 课程目标对齐性 | 跨模态一致性 | 教学完整性 | 来源可追溯性"
            }
          },
          "box_holdout": {
            "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
            "exact_title_to_render_inside": "跨来源留出测试",
            "exact_text": "按知识模块 / 来源 / 设备类型留出"
          },
          "box_revision": {
            "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
            "exact_title_to_render_inside": "人工修订记录",
            "exact_text": "人工修订时间"
          },
          "sampling_note": {
            "shape": "No border, floating text at the bottom of the frame",
            "exact_floating_text": "拟构建 300 个以上资源单元，拟抽取 120 个用于盲评"
          }
        },
        "comparison_block": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt border, white fill, positioned exactly BETWEEN the left automatic side and the right expert side, straddling the dashed boundary",
          "exact_title_to_render_inside": "一致性比对",
          "exact_text": "Krippendorff's alpha · 错误检出率 · 误报率",
          "connector": "One dark navy 1.2pt solid DOUBLE-HEADED arrow linking the VRR block on the left and the expert side on the right, passing through this comparison block. This is the ONLY double-headed arrow in the figure."
        },
        "recalibration": {
          "connector": "One dark grey 1.0pt dashed arrow curving from the comparison block back UP to the synthesis block",
          "exact_floating_text": "阈值与错误类型重新校准（仅开发集）"
        }
      }
    },
    {
      "id": "SCOPE_NOTE",
      "relative_position": "Bottom-most row, full width, smallest element on the canvas",
      "shape": "Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill",
      "exact_text": "该代理回答资源单元能否进入资源包，不回答学生是否学得更好；不使用学生行为数据。一致性不足时降级为自动初筛—人工复核。",
      "typography": "7pt regular, #4D4D4D, lowest visual weight on the canvas"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. Only the bottom band may use light grey (#F7F7F7) fill.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E and #A64B2A, plus neutral greys. Do NOT introduce a fourth chromatic colour.",
    "The four quality layers MUST be drawn as wide short horizontal bars with SQUARE corners (0pt radius), stacked VERTICALLY top to bottom, pierced by one continuous thick dark navy arrow flowing downward. Do NOT arrange them horizontally and do NOT use rounded corners on the layer bars.",
    "All other boxes use 3pt rounded corners. The vertical square-cornered stack is what distinguishes this figure from the horizontal gate figure elsewhere in the set.",
    "Exactly ONE focus element: the 主指标 VRR block uses a 3.0pt dark navy border with enlarged surrounding whitespace. No other element may be emphasised.",
    "CRITICAL: a LARGE dark navy 1.5pt DASHED frame must enclose the ENTIRE expert side (blind review, holdout test, revision records) and be labelled 与门控设计相互独立 on its top edge. This visual separation is the core scientific argument of the figure and must be unmistakable.",
    "The automatic side and the expert side MUST use the same dark navy colour. Convey their independence only through the dashed boundary and spatial separation, never by making one side lighter, smaller, or subordinate.",
    "Exactly ONE double-headed arrow is permitted in the entire figure: the consistency-comparison link between the VRR block and the expert side. Every other connector is single-headed.",
    "The recalibration arrow MUST carry the label 阈值与错误类型重新校准（仅开发集） exactly as written. Omitting the 仅开发集 qualifier is not acceptable.",
    "The warm brick colour #A64B2A is RESERVED exclusively for rejection elements. Every such element MUST simultaneously use a dashed stroke and an explicit Chinese label so the figure survives greyscale printing.",
    "All four reject exits must leave the layer bars on the RIGHT side, be right-aligned with each other, and terminate in small solid dots.",
    "Quantities describing future work must keep their 拟邀请, 拟构建 and 拟抽取 prefixes exactly as written. Do NOT render them as accomplished facts.",
    "The Latin symbols Q(u), P(u) and VRR are rendered in Times italic. Do NOT render any full equation, summation, indicator function, or weighting coefficient.",
    "Do NOT expand the resource-unit field schema, the cross-modal relation gates, the B0 to B3 baselines, or any project execution timeline — those belong to other figures.",
    "Icons are monochrome thin grey line art, at most one per box, no larger than 1.6x the adjacent text height.",
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

Core subject: a four-layer intrinsic quality gate for teaching resource units, and — crucially — how its validity is established by expert review that is structurally independent of the gate design itself.

Composition: strictly top to bottom. The upper section, titled 四层质量门控, is a vertical stack of four wide short dark-navy bars with SQUARE corners, pierced by one continuous thick downward arrow. Each bar splits into a layer name and a check target: 内容层 事实与参数正确性, 课程层 知识点与能力目标对齐, 模态层 跨模态对象与条件一致, 证据层 原始出处支持关键断言, with a medium-blue side box on the left of the fourth bar reading 证据支持度 文本支持 · 其他模态支持 · 知识关系支持 and the note 不达阈值 → 人工核验. From the right edge of every bar a short warm-brick dashed arrow exits, all right-aligned and ending in small solid dots, into one dashed warm-brick box 拒绝并保留原因, beside the floating rule 任一层严重错误即拒绝，并保留拒绝原因.

The middle section, 单元级判定, holds a dark-navy block 四层质量合成 Q(u) with rows 内容 · 课程 · 模态 · 证据 加权 and 惩罚项 P(u)：参数矛盾 · 来源不可追溯 · 未授权或隐私风险, the floating rule 字段完整 ∧ 无严重错误 ∧ 质量分达阈值, and three output boxes 通过 → 进入资源包, 待核验 → 人工复核, and a dashed warm-brick 拒绝 → 保留原因.

The bottom band, 独立效度验证, splits left and right. On the left is the single visual focus: a block with a thick 3pt border and generous white space reading 主指标 VRR 有效资源单元通过率 四层均通过的单元占比 with the note 权重与阈值仅在开发集确定，测试集冻结. On the right, a LARGE dark-navy DASHED frame labelled 与门控设计相互独立 encloses three medium-blue boxes — 独立专家盲评 (拟邀请不少于 3 名未参与资源构建的教师, 量表制定者不参与正式评分 · 评分隐藏方法条件, plus five chips 内容与事实正确性, 课程目标对齐性, 跨模态一致性, 教学完整性, 来源可追溯性), 跨来源留出测试 按知识模块 / 来源 / 设备类型留出, and 人工修订记录 人工修订时间 — with the note 拟构建 300 个以上资源单元，拟抽取 120 个用于盲评. Straddling the boundary between the two sides sits a dark-navy block 一致性比对 Krippendorff's alpha · 错误检出率 · 误报率, linked by the figure's ONLY double-headed arrow. A dashed arrow curves back up to the synthesis block labelled 阈值与错误类型重新校准（仅开发集）. A tiny dashed pale-grey note runs across the very bottom.

Supporting modules: sparse monochrome thin-grey line icons — person with rating bars.

Visual tone: restrained, rigorous, print-oriented. Material: white fills, coloured borders only; layer bars square-cornered, everything else 3pt rounded; borders 1.0/1.2/1.5/2.0/3.0pt. Palette strictly #1B3A5C, #2E6B9E and #A64B2A plus neutral greys; both sides of the closure use the same navy so neither looks subordinate.

Typography: Source Han Sans / Noto Sans CJK SC; zone titles 10pt bold, layer names 9.5pt bold, labels 8pt, notes 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: horizontal gate arrangements; more than one double-headed arrow; any full equation, summation or indicator function; the resource-unit field schema, cross-modal gates, B0 to B3 baselines or project timeline; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 4:3.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 四层直角层栈、质量合成块、VRR 焦点框、一致性比对块、独立性虚线边界、双向比对箭头 |
| secondary | `#2E6B9E` | 证据支持度侧框、待核验输出、专家盲评/留出/修订三框、五维 chip |
| **reject** | `#A64B2A` | **顶替 tertiary**：四层拒绝出口、拒绝框、拒绝输出（必配虚线 + 中文标签） |
| gray | `#8EAEC4` | 底部适用边界声明 |
| arrow | `#4D4D4D` | 校准回流虚线 |
| section_bg | `#F7F7F7` | 独立效度验证底带 |

**唯一焦点**：`主指标 VRR` 框（3.0pt 边框 + 1.5× 留白）
**形态标识**：四层 = 直角横条纵向堆叠；F05 = 直角竖条横向串联。流向正交。
**全套唯一双向箭头**：VRR ↔ 专家侧的一致性比对（F01–F07 中仅此一处）

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 6 四层资源内在质量门控与独立效度验证。项目对每个资源单元依次施加内容、课程、模态与证据四层质量约束，分别检查事实与参数、知识点与能力目标、跨模态对象与条件、以及原始出处对关键断言的支持；任一层出现严重错误即拒绝并保留原因。通过各层者按加权方式合成单元质量分并计入惩罚项，字段完整、无严重错误且质量分达阈值方可进入资源包，主指标为有效资源单元通过率。自动门控只作筛查，其效度由与规则制定相互独立的专家盲评、跨来源留出测试与人工修订记录检验，并报告 Krippendorff's alpha、错误检出率与误报率。权重与阈值仅在开发集确定，测试集冻结。
- 证据支持度、四层质量合成与 VRR 的完整数学表达式及全部权重符号 → 正文。
- 五维盲评量表的具体条目与评分等级 → 正文或附件。
- 拟构建规模、抽样与专家邀请的落实安排 → 正文（（二）工作条件）。
- 质量效度风险的早期信号与应对措施 → 正文。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（layered gate + validity closure） |
| 全部模块有标书出处 | ✅ 2.1(3) / 2.2 目标三 / 2.3(3) / 3.1 / 4.4 / （二）2.2 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 4:3 |
| 物理规格与字体块 | ✅ 183mm / 10-9.5-8-7pt / 1.0-1.2-1.5-2.0-3.0pt |
| 有彩色 ≤3 | ✅ 3 种（`#A64B2A` 顶替 `#5BA0D0`） |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 直角层栈形态锚点 + 专家图标 |
| 无空壳模块 | ✅ |
| 拒绝元素三重编码 | ✅ 暖色 + 虚线 + 中文标签 |
| 独立性边界为强制元素 | ✅ 粗虚线包围框 + 顶边标注 |
| 未来事实口径 | ✅ 拟邀请 / 拟构建 / 拟抽取 前缀强制保留 |
| "仅开发集"标注 | ✅ 校准回流箭头强制标注 |
| 负向约束齐备 | ✅ 含禁横向布局/禁多个双向箭头/禁公式、NO emojis / NO 3D |
| 与 F05 的防混淆约束 | ✅ 直角横条纵向堆叠（本图，自上而下）vs 直角竖条横向串联（F05，自左向右），流向正交 |
| 与 F03 的防混淆约束 | ✅ F03 的 S4 仅 4 层名 + 1 规则，本图为其机制级放大 |
| 推断或待确认项 | 无。全部内容可溯源至标书 |
