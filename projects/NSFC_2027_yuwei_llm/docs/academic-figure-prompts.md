# Academic Figure Prompt Package

本文件对应 [Figure_Plan.md](Figure_Plan.md) 的 F1--F13。本轮只生成提示词与结构规格，不生成图片。

## 全局 Palette Decision

- **约束**：NSFC 申请书；NLP/LLM 数据机制；需兼顾屏幕与灰度打印；默认要求色盲友好；每幅图不超过 3 个彩色通道；F3--F13 均含 4 个以上模块。
- **style family**：Classic academic，使用 `Academic Figure Prompt`；不采用 pastel/airy 风格。
- **决策分支**：`scene`。F1--F2 为双来源概念对照，采用 **Okabe-Ito**；F3--F13 触发“≥4 模块”硬约束，采用 **Nature Blue**。
- **Okabe-Ito 主方案**：primary `#0072B2`，secondary `#E69F00`，tertiary `#009E73`，text `#333333`，fill `#FFFFFF`，section background `#F7F7F7`，border `#CCCCCC`，arrow `#4D4D4D`。备选：Nature Blue。
- **Nature Blue 主方案**：primary `#1B3A5C`，secondary `#2E6B9E`，tertiary `#5BA0D0`，frozen/auxiliary `#8EAEC4`，text `#333333`，fill `#FFFFFF`，section background `#F7F7F7`，border `#CCCCCC`，arrow `#4D4D4D`。备选：ML TopConf Colorblind（`#0173B2/#DE8F05/#029E73`）。
- **跨图语义绑定**：数据/输入=`#5BA0D0`（F1--F2 为 `#0072B2`）；核心模型/共同参考=`#1B3A5C`；干预/分析=`#2E6B9E`；结构缺陷概念=`#E69F00`；非冗余支持概念=`#009E73`；冻结/辅助=`#8EAEC4` 虚线；失败/反馈=`#4D4D4D` 点线或斜线纹理；输出用双线框或右向结论卡再编码。
- **可访问性**：所有类别同时使用颜色、形状、线型和文字标签；不以红绿对立单独传递结论；白底文字对比度不低于 4.5:1；灰度打印仍可通过实线/虚线/点线、圆角框/菱形/六边形区分。

### Palette handoff：F1--F2

```text
palette: Okabe-Ito
primary / secondary / tertiary: #0072B2 / #E69F00 / #009E73
text / fill / section_bg / border / arrow: #333333 / #FFFFFF / #F7F7F7 / #CCCCCC / #4D4D4D
reason: 双来源概念对照只有两条核心路径，需要色盲安全的离散区分。
accessibility: colorblind-safe；同时使用三角/圆形、实线/虚线和文字标签。
```

### Palette handoff：F3--F13

```text
palette: Nature Blue
primary / secondary / tertiary: #1B3A5C / #2E6B9E / #5BA0D0
text / fill / section_bg / border / arrow: #333333 / #FFFFFF / #F7F7F7 / #CCCCCC / #4D4D4D
reason: 每图包含四个以上模块，单色明度层级比多色模块更稳健、更适合申报书打印。
accessibility: colorblind-safe and grayscale-friendly；冻结/失败/可选状态另用虚线、点线、斜线纹理。
```

---

## F1 同一低分下的两类中文语料及过滤悖论

**类型**：Research Background / Conceptual Comparison  
**色板**：Okabe-Ito；备选 Nature Blue  
**caption reserve**：静态质量分只用于定位样本；低熟悉不等于结构破损；图中散点和分数带均为概念示意，不表示实测结果。

### JSON figure spec

```json
{
  "diagram_type": "Academic Research Background Conceptual Comparison",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {
    "palette": "Okabe-Ito",
    "background": "White #FFFFFF",
    "input_data": "Blue #0072B2",
    "structural_defect": "Orange #E69F00",
    "semantic_support": "Green #009E73",
    "text": "#333333",
    "arrow": "#4D4D4D"
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far left, upper lane",
      "shape": "Rounded rectangle, #E69F00 solid border, white fill",
      "exact_title_to_render_inside": "结构破损文本",
      "exact_text": "错序｜截断｜断裂",
      "icon": "small broken paragraph thumbnail with displaced text lines, monochrome line art",
      "flow": "Solid arrow right to 双重评分"
    },
    {
      "relative_position": "Far left, lower lane",
      "shape": "Rounded rectangle, #009E73 solid border, white fill",
      "exact_title_to_render_inside": "完整低熟悉语体",
      "exact_text": "网络｜地域｜异体",
      "icon": "small intact document with continuous text lines and a rare-expression marker, monochrome line art",
      "flow": "Solid arrow right to 双重评分"
    },
    {
      "relative_position": "Center left",
      "shape": "Two vertically stacked rounded boxes, #0072B2 borders, white fill",
      "exact_title_to_render_inside": "双重评分",
      "exact_text": "困惑度型\n规范性型",
      "icon": "two small gauge-and-classifier line icons",
      "flow": "Solid arrow right to 低分重叠区"
    },
    {
      "relative_position": "Center",
      "shape": "Lens-shaped overlap panel, #0072B2 border, very light grey section background",
      "exact_title_to_render_inside": "低分重叠区",
      "exact_text": "同分异源",
      "icon": "small conceptual scatterplot with orange triangles and green circles overlapping inside a shaded vertical band",
      "flow": "Solid arrow right to 统一过滤"
    },
    {
      "relative_position": "Center right",
      "shape": "Funnel outline, #4D4D4D border, white fill",
      "exact_title_to_render_inside": "统一过滤",
      "exact_text": "单一阈值",
      "icon": "simple filter funnel, monochrome line art",
      "flow": "Two diverging arrows right"
    },
    {
      "relative_position": "Far right, upper outcome",
      "shape": "Rounded result card, #E69F00 double border, white fill",
      "exact_title_to_render_inside": "结构噪声减少",
      "exact_text": "更新更对齐",
      "icon": "two gradient arrows becoming more parallel, monochrome line art"
    },
    {
      "relative_position": "Far right, lower outcome",
      "shape": "Rounded result card, #009E73 dashed border, white fill",
      "exact_title_to_render_inside": "语义支持收缩",
      "exact_text": "语体｜实体｜长尾",
      "icon": "coverage network losing peripheral nodes, monochrome line art"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Borderless annotation band",
      "exact_floating_text": "相近低分 ≠ 相同效用",
      "caption_note": "Conceptual diagram only; no empirical score values or outcome magnitudes are rendered."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE #FFFFFF fill with COLORED BORDERS ONLY.",
    "Use titles 10-12pt bold, labels 8-9pt, notes 6-8pt.",
    "Use 1.5pt container borders, 1.0pt dividers, and 1.5pt arrows.",
    "Icons are monochrome thin line art; no filled color icons.",
    "Use both color and shape to distinguish the two source types.",
    "Do not render numeric axes, fabricated scores, effects, or significance marks.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients, NO decorative shadows, NO photorealism.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic conceptual comparison diagram showing why two kinds of Chinese pretraining text can receive similar low-quality representations yet have different training utility. Use a pure white canvas and a horizontal left-to-right narrative with two parallel input lanes. In the upper lane, render a white rounded card with an orange #E69F00 border labeled exactly “结构破损文本”, containing “错序｜截断｜断裂” and a tiny broken-paragraph thumbnail. In the lower lane, render a green #009E73 bordered card labeled “完整低熟悉语体”, containing “网络｜地域｜异体” and an intact-document thumbnail.

Both lanes feed into a blue #0072B2 double scorer labeled “双重评分”, with two compact rows “困惑度型” and “规范性型”. Next, show a small conceptual scatterplot labeled “低分重叠区”: orange triangles and green circles overlap inside one shaded vertical band, with “同分异源” centered in the band. Do not show numeric axes or empirical values. A neutral funnel labeled “统一过滤” and “单一阈值” then splits into two outcomes: an orange double-border card “结构噪声减少 / 更新更对齐” with two increasingly parallel gradient arrows, and a green dashed-border card “语义支持收缩 / 语体｜实体｜长尾” with a coverage network losing peripheral nodes. Add the exact bottom statement “相近低分 ≠ 相同效用”.

Use Helvetica or Arial, 10–12 pt bold titles, 8–9 pt labels, 1.5 pt borders, dark-grey #4D4D4D arrows, white box fills, and monochrome thin-line icons. Keep alignment strict and whitespace generous. Use color plus triangle/circle shapes for accessibility. No gradients, fabricated results, shadows, emojis, decorative icons, or 3D effects. Aspect ratio 16:9.

---

## F2 低质量表征效用异质性的双路径假设

**类型**：Scientific Mechanism Hypothesis  
**色板**：Okabe-Ito；备选 Nature Blue  
**caption reserve**：结构路径与支持路径是两套不同估计量；模型知识状态仅作为支持路径的预注册边界条件；任何一路均允许被负对照否定。

### JSON figure spec

```json
{
  "diagram_type": "Scientific Dual-Path Mechanism Hypothesis",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {
    "palette": "Okabe-Ito",
    "background": "#FFFFFF",
    "common_representation": "#0072B2",
    "structure_path": "#E69F00",
    "support_path": "#009E73",
    "neutral": "#4D4D4D"
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top center",
      "shape": "Wide rounded rectangle, #0072B2 double border, white fill",
      "exact_title_to_render_inside": "相近低质量表征",
      "exact_text": "表面同分",
      "icon": "two converging score gauges, monochrome line art",
      "flow": "Two solid arrows split downward into left and right lanes"
    },
    {
      "relative_position": "Middle left lane",
      "shape": "Large pale grouping panel with #E69F00 heading rule",
      "exact_title_to_render_inside": "结构缺陷路径",
      "internal_content": {
        "layout": "Three connected white cards",
        "step_1": {"exact_text": "结构破损", "icon": "broken paragraph thumbnail"},
        "step_2": {"exact_text": "低对齐更新", "icon": "misaligned vector arrows"},
        "step_3": {"exact_text": "通用能力", "exact_secondary_note": "知识保持", "icon": "document-and-brain line icon"}
      }
    },
    {
      "relative_position": "Bottom left under structure lane",
      "shape": "Two small counterfactual cards, orange solid and grey dashed borders",
      "exact_title_to_render_inside": "恢复与负对照",
      "exact_text": "原文恢复｜sham",
      "icon": "reversible arrow beside matched-operation symbol"
    },
    {
      "relative_position": "Middle right lane",
      "shape": "Large pale grouping panel with #009E73 heading rule",
      "exact_title_to_render_inside": "语义支持路径",
      "internal_content": {
        "layout": "Three connected white cards",
        "step_1": {"exact_text": "完整低熟悉语体", "icon": "intact rare-text document"},
        "step_2": {"exact_text": "非冗余更新", "icon": "coverage network with distinct nodes"},
        "step_3": {"exact_text": "语体长尾能力", "icon": "branching knowledge tree"}
      }
    },
    {
      "relative_position": "Bottom right under support lane",
      "shape": "Three small counterfactual cards with green solid, grey dashed, and dotted borders",
      "exact_title_to_render_inside": "补回与伪补回",
      "exact_text": "非冗余｜窄支持｜主流",
      "icon": "three coverage grids of broad, narrow, and unrelated support"
    },
    {
      "relative_position": "Far right lower side",
      "shape": "Hexagonal moderator node, #0072B2 dashed border, white fill",
      "exact_title_to_render_inside": "知识状态",
      "exact_text": "共同 checkpoint",
      "icon": "small stacked model layers and checkpoint marker",
      "flow": "Dashed arrow only to 语义支持路径"
    },
    {
      "relative_position": "Center vertical divider",
      "shape": "Thin grey divider with a compact label",
      "exact_floating_text": "两估计量不比较"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Borderless conclusion band",
      "exact_floating_text": "恢复成立｜负对照通过｜能力响应",
      "caption_note": "Each path is independently falsifiable; failure of one path does not rescue it through post-hoc state dependence."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE #FFFFFF fill with COLORED BORDERS ONLY.",
    "Keep the two lanes visually symmetric but causally separate.",
    "Use solid arrows for hypothesized flow and dashed arrows for moderation or negative control.",
    "Icons are monochrome thin line art.",
    "Do not draw measured effect sizes, p-values, or empirical curves.",
    "Do not connect 知识状态 to the structure lane.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic mechanism hypothesis diagram showing the dual-path explanation for heterogeneous utility of low-quality representations in Chinese pretraining data. Place a wide blue #0072B2 double-border card at the top center labeled exactly “相近低质量表征” with the secondary text “表面同分” and two converging score-gauge icons. Split downward into two balanced but causally separate lanes.

The left orange #E69F00 lane is titled “结构缺陷路径”. Arrange three white cards in sequence: “结构破损” with a broken-paragraph thumbnail, “低对齐更新” with two misaligned gradient arrows, and “通用能力” with the note “知识保持” and a document-brain icon. Beneath it, show “恢复与负对照” with the exact labels “原文恢复｜sham”, using a solid reversible arrow for recovery and a dashed matched-operation symbol for sham.

The right green #009E73 lane is titled “语义支持路径”. Arrange three cards: “完整低熟悉语体” with an intact rare-expression document, “非冗余更新” with a diverse coverage network, and “语体长尾能力” with a branching knowledge tree. Beneath it, show “补回与伪补回” and “非冗余｜窄支持｜主流” as three distinct coverage grids. Add a blue dashed hexagon “知识状态 / 共同 checkpoint” at the lower right, with a dashed moderator arrow only into the support lane. Between the lanes place “两估计量不比较”; at the bottom place “恢复成立｜负对照通过｜能力响应”.

Use clean Arial/Helvetica, 10–12 pt titles, 8–9 pt labels, 1.5 pt colored borders, white fills, dark-grey arrows, consistent monochrome line icons, and strict grid alignment. Do not render data values, p-values, gradients, shadows, emojis, decorative icons, or 3D elements. Aspect ratio 16:9.

---

## F3 三项研究内容与双路径证据闭环

**类型**：Overall Framework  
**色板**：Nature Blue；备选 ML TopConf Colorblind  
**caption reserve**：研究内容一形成样本层，研究内容二、三并行识别两条路径；来源 A 用于确认，来源 B 仅复核冻结的存活对比；外部边界不再单列为第四项内容。

### JSON figure spec

```json
{
  "diagram_type": "Scientific Overall Research Framework",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {
    "palette": "Nature Blue",
    "background": "#FFFFFF",
    "core": "#1B3A5C",
    "process": "#2E6B9E",
    "data": "#5BA0D0",
    "frozen": "#8EAEC4",
    "text": "#333333",
    "arrow": "#4D4D4D"
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top left",
      "shape": "Two database cylinders, #5BA0D0 borders, white fill",
      "exact_title_to_render_inside": "双来源语料",
      "exact_text": "来源 A｜来源 B",
      "icon": "two small database cylinders with separate provenance tags",
      "flow": "Solid arrow right to 数据治理"
    },
    {
      "relative_position": "Top center-left",
      "shape": "Rounded rectangle, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "数据治理",
      "exact_text": "许可｜去重｜索引",
      "icon": "data card and four-level index tree, monochrome line art",
      "flow": "Solid arrow right to 同分样本层"
    },
    {
      "relative_position": "Top center",
      "shape": "Rounded rectangle, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "同分样本层",
      "exact_text": "双评分｜盲标",
      "exact_floating_text": "研究内容一",
      "icon": "overlap scatterplot and two annotator silhouettes, monochrome",
      "flow": "Solid arrow down to 六臂反事实"
    },
    {
      "relative_position": "Center",
      "shape": "Wide fan-out container, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "六臂反事实",
      "exact_text": "A0｜A1｜A2｜A3｜A4｜A5",
      "icon": "six compact document cards radiating from one shared data pool",
      "flow": "Two solid arrows down into left and right mechanism lanes"
    },
    {
      "relative_position": "Lower left lane",
      "shape": "Large rounded grouping panel, #2E6B9E solid border, white fill",
      "exact_title_to_render_inside": "结构缺陷路径",
      "exact_text": "恢复｜破损｜sham",
      "exact_floating_text": "研究内容二",
      "icon": "three document states connected by reversible arrows",
      "flow": "Solid arrow right to 来源 A 训练"
    },
    {
      "relative_position": "Lower right lane",
      "shape": "Large rounded grouping panel, #5BA0D0 solid border, white fill",
      "exact_title_to_render_inside": "语义支持路径",
      "exact_text": "主流｜非冗余｜窄支持",
      "exact_floating_text": "研究内容三",
      "icon": "three coverage networks with unrelated, broad, and narrow support",
      "flow": "Solid arrow left-to-center to 来源 A 训练"
    },
    {
      "relative_position": "Bottom center-left",
      "shape": "Rounded rectangle, #1B3A5C solid border, white fill",
      "exact_title_to_render_inside": "来源 A 训练",
      "exact_text": "共同 checkpoint\n成对种子",
      "icon": "stacked transformer layers with paired seed markers",
      "flow": "Solid arrow right to 双终点评价"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Rounded rectangle, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "双终点评价",
      "exact_text": "梯度对齐｜独立能力",
      "icon": "gradient-angle thumbnail beside two evaluation cards",
      "flow": "Solid arrow right to 联合判定"
    },
    {
      "relative_position": "Bottom center-right",
      "shape": "Diamond decision node, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "联合判定",
      "exact_text": "优效｜等效",
      "icon": "confidence interval bars and equivalence band",
      "flow": "Solid arrow right to 冻结复核; dashed arrows down to 分支停止"
    },
    {
      "relative_position": "Far bottom right",
      "shape": "Rounded rectangle, #8EAEC4 dashed border, white fill",
      "exact_title_to_render_inside": "来源 B 复核",
      "exact_text": "冻结协议",
      "icon": "sealed checklist entering a second database",
      "flow": "Solid arrow right/down to 边界结论"
    },
    {
      "relative_position": "Far right vertical result panel",
      "shape": "Three stacked output cards, #1B3A5C/#2E6B9E/#8EAEC4 borders, white fill",
      "exact_title_to_render_inside": "外部边界",
      "exact_text": "直接运输\n条件校准\n拒绝外推",
      "icon": "small boundary map with three zones"
    },
    {
      "relative_position": "Bottom margin",
      "shape": "Borderless annotation band",
      "exact_floating_text": "闸门失败仅停止对应分支",
      "caption_note": "Source and register names remain generic until license and independent-token audit are frozen."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE #FFFFFF fill with Nature Blue colored borders only.",
    "Use three horizontal tiers: data, mechanisms, evidence and transport.",
    "Main forward flow arrows are solid #4D4D4D; stopping branches are dashed.",
    "Frozen protocol and Source B use dashed #8EAEC4 borders.",
    "Icons are monochrome thin line art.",
    "Do not imply Source B tunes thresholds or validates sham and narrow-support specificity again.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic architecture diagram showing three linked research contents and a dual-path evidence loop for low-quality Chinese pretraining data. Use a pure white canvas and three horizontal tiers. Mark the top data tier as “研究内容一”; connect “双来源语料 / 来源 A｜来源 B” to “数据治理 / 许可｜去重｜索引”, then to a dark-navy double-border card “同分样本层 / 双评分｜盲标”. Add database, data-card, four-level index, overlap-scatter, and two-annotator line icons.

From the sample layer, flow downward into a central fan-out box “六臂反事实 / A0｜A1｜A2｜A3｜A4｜A5”. Split into two parallel mechanism lanes explicitly tagged “研究内容二” and “研究内容三”: left “结构缺陷路径 / 恢复｜破损｜sham” with three document-state thumbnails, and right “语义支持路径 / 主流｜非冗余｜窄支持” with three coverage-network thumbnails. Both lanes converge into “来源 A 训练 / 共同 checkpoint / 成对种子”, illustrated by stacked transformer layers and paired markers.

In the bottom evidence tier, connect Source A training to “双终点评价 / 梯度对齐｜独立能力”, then a diamond “联合判定 / 优效｜等效”. Successful branches enter a dashed pale-blue card “来源 B 复核 / 冻结协议”, followed by a vertical result panel “外部边界” containing “直接运输”, “条件校准”, and “拒绝外推”. Dashed downward branches from failed gates end at the exact note “闸门失败仅停止对应分支”.

Use Nature Blue: #1B3A5C for core and decisions, #2E6B9E for processes, #5BA0D0 for data, #8EAEC4 dashed for frozen elements, and #4D4D4D arrows. All boxes have white fills, 1.5 pt borders, short Chinese labels, and monochrome line icons. No gradients, shadows, emojis, decorative symbols, or 3D. Aspect ratio 16:9.

---

## F4 路线一：同分异源样本层构建

**类型**：Technical Route / Data Pipeline  
**色板**：Nature Blue；备选 ML TopConf Colorblind  
**caption reserve**：来源名称、确认性语体和阈值待第一年度冻结；若双评分重叠或人工一致性验收失败，则不进入中心命题检验。

### JSON figure spec

```json
{
  "diagram_type": "Technical Route for Identifiable Sample-Layer Construction",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Far left",
      "shape": "Two database cylinders, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "候选公开语料",
      "exact_text": "来源 A｜来源 B",
      "icon": "two separated database cylinders with provenance tags",
      "flow": "Solid arrow right"
    },
    {
      "relative_position": "Left center",
      "shape": "Rounded rectangle, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "治理与审计",
      "exact_text": "许可｜版本｜隐私\n规范化｜去重｜编码",
      "icon": "data card with checklist and deduplication nodes",
      "flow": "Solid arrow right"
    },
    {
      "relative_position": "Center left",
      "shape": "Four-layer stacked index, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "四层索引",
      "exact_text": "来源\n语体\n主题实体\n重复簇",
      "icon": "stacked filing layers with branching keys",
      "flow": "Solid arrow right then split into two parallel lanes"
    },
    {
      "relative_position": "Upper middle lane",
      "shape": "Two adjacent rounded cards, #2E6B9E borders, white fill",
      "exact_title_to_render_inside": "异质质量表征",
      "exact_text": "困惑度型｜规范性型",
      "icon": "gauge and classifier line icons",
      "flow": "Solid arrow right to 汇合"
    },
    {
      "relative_position": "Lower middle lane",
      "shape": "Rounded rectangle, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "双人盲标",
      "exact_text": "结构｜语义｜事实｜语体",
      "icon": "two annotator silhouettes examining document cards",
      "flow": "Solid arrow right to 汇合"
    },
    {
      "relative_position": "Center right",
      "shape": "Lens-shaped merge card, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "同分异源样本层",
      "exact_text": "重叠｜匹配｜隔离",
      "icon": "overlap scatter thumbnail with two shape-coded sample classes",
      "flow": "Solid arrow right to 验收闸门"
    },
    {
      "relative_position": "Right center",
      "shape": "Diamond, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "验收闸门",
      "exact_text": "追溯｜一致\n保持｜重叠｜平衡",
      "icon": "five compact geometric check markers",
      "branch_yes": "Solid arrow right to 实验输入",
      "branch_no": "Dashed arrow down to 返工或终止"
    },
    {
      "relative_position": "Far right upper",
      "shape": "Two separated output trays, #2E6B9E and #5BA0D0 solid borders, white fill",
      "exact_title_to_render_inside": "互斥目标集合",
      "exact_text": "结构目标集｜支持目标集",
      "icon": "two non-overlapping document trays",
      "flow": "Solid arrow down to 六臂生成器"
    },
    {
      "relative_position": "Far right lower",
      "shape": "Rounded rectangle, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "六臂生成器",
      "exact_text": "A0｜A1｜A2\nA3｜A4｜A5",
      "icon": "six deterministic output cards"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Dashed grey return card",
      "exact_title_to_render_inside": "返工或终止",
      "exact_text": "不读取能力结果",
      "caption_note": "Formal source names, register definitions, and thresholds are pending audit and pilot freezing."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "Show scoring and blind annotation as parallel independent lanes.",
    "Use shape coding in the overlap thumbnail; do not show empirical coordinates.",
    "The structure and support target trays must not overlap.",
    "The failure branch is dashed and returns to protocol revision, never to performance tuning.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic data-pipeline diagram showing the technical route for constructing an identifiable “同分异源” sample layer from public Chinese corpora. Use a strict left-to-right flow on a white canvas. Begin with two separate database cylinders labeled “候选公开语料 / 来源 A｜来源 B”. Connect them to “治理与审计”, containing the exact compact rows “许可｜版本｜隐私” and “规范化｜去重｜编码”, with data-card, checklist, and deduplication line icons. Continue to a four-layer stacked index labeled “四层索引” with “来源 / 语体 / 主题实体 / 重复簇”.

Split into two independent middle lanes. The upper lane is “异质质量表征 / 困惑度型｜规范性型”, anchored by a gauge and classifier. The lower lane is “双人盲标 / 结构｜语义｜事实｜语体”, anchored by two annotators examining documents. Merge both lanes into a dark-navy double-border lens “同分异源样本层 / 重叠｜匹配｜隔离”, including a tiny conceptual overlap scatterplot with triangles and circles but no numeric axes.

Flow into a diamond “验收闸门” containing “追溯｜一致 / 保持｜重叠｜平衡”. The solid success branch produces two visibly separated trays “互斥目标集合 / 结构目标集｜支持目标集”, then a double-border “六臂生成器 / A0｜A1｜A2 / A3｜A4｜A5”. The dashed failure branch goes downward to “返工或终止 / 不读取能力结果”.

Use Nature Blue borders: #1B3A5C core, #2E6B9E process, #5BA0D0 data, #8EAEC4 auxiliary, with dark-grey #4D4D4D arrows. White fills only, 1.5 pt outlines, Arial/Helvetica labels, monochrome line icons, and clear spacing. Keep every arrow unambiguous and preserve visible separation between independent data subsets. No fabricated source names, scores, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F5 路线二：结构缺陷削减、动力学与来源边界

**类型**：Technical Route / Counterfactual Experiment  
**色板**：Nature Blue；备选 Blue Monochrome  
**caption reserve**：A0/A1/A2 共用同一破损前体；训练运行是推断单位；来源 A 完成处理特异性检验后，仅冻结 A0--A1 进入来源 B；正式阈值待预注册冻结。

### JSON figure spec

```json
{
  "diagram_type": "Technical Route for Structural-Defect Counterfactual Experiment",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Top left",
      "shape": "Rounded document card, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "结构完整原文",
      "exact_text": "统一背景池",
      "icon": "intact paragraph thumbnail with ordered lines",
      "flow": "Solid arrow right to 可逆破损"
    },
    {
      "relative_position": "Top center-left",
      "shape": "Rounded document card, #2E6B9E double border, white fill",
      "exact_title_to_render_inside": "共同破损前体",
      "exact_text": "错序｜截断｜断裂",
      "icon": "same paragraph with displaced, clipped, and disconnected lines",
      "flow": "Three solid arrows downward to A0, A1, A2"
    },
    {
      "relative_position": "Middle left column",
      "shape": "Rounded card, #1B3A5C solid border, white fill",
      "exact_title_to_render_inside": "A0 精确恢复",
      "exact_text": "逆操作",
      "icon": "reversible arrow returning paragraph lines to original order",
      "flow": "Solid arrow right to 平衡审计"
    },
    {
      "relative_position": "Middle center column",
      "shape": "Rounded card, #2E6B9E solid border, white fill",
      "exact_title_to_render_inside": "A1 保留破损",
      "exact_text": "无恢复",
      "icon": "broken paragraph thumbnail",
      "flow": "Solid arrow right to 平衡审计"
    },
    {
      "relative_position": "Middle right column",
      "shape": "Rounded card, #8EAEC4 dashed border, white fill",
      "exact_title_to_render_inside": "A2 等量 sham",
      "exact_text": "不恢复结构",
      "icon": "matched editing marks that leave paragraph structure broken",
      "flow": "Solid arrow right to 平衡审计"
    },
    {
      "relative_position": "Center right",
      "shape": "Vertical balance panel, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "平衡审计",
      "exact_text": "token｜packing\n来源｜主题｜预算",
      "icon": "balance scale with equal document and token stacks",
      "flow": "Solid arrow down to 成对训练"
    },
    {
      "relative_position": "Bottom left-center",
      "shape": "Rounded rectangle, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "来源 A 成对训练",
      "exact_text": "共同 checkpoint\n六个主种子",
      "icon": "stacked transformer layers branching into six paired run markers",
      "flow": "Solid arrow right to 双证据读出"
    },
    {
      "relative_position": "Bottom center-right",
      "shape": "Two adjacent output cards, #2E6B9E and #5BA0D0 borders, white fill",
      "exact_title_to_render_inside": "双证据读出",
      "exact_text": "梯度对齐｜通用能力",
      "icon": "gradient angle and independent evaluation sheet",
      "flow": "Solid arrow right to 结构判定"
    },
    {
      "relative_position": "Bottom right",
      "shape": "Diamond decision node, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "结构判定",
      "exact_text": "A0>A1\nA0>A2\nA1≈A2",
      "icon": "two superiority interval bars and one equivalence band",
      "branch_yes": "Solid arrow to 来源 B 冻结复核",
      "branch_no": "Dashed arrow to 停止结构路径"
    },
    {
      "relative_position": "Far right continuation",
      "shape": "Dashed rounded card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "来源 B 冻结复核",
      "exact_text": "A0−A1｜方向区间",
      "icon": "sealed checklist entering a second database",
      "flow": "Solid arrow to 来源边界",
      "caption_note": "Source B receives the frozen A0-A1 contrast only; source admission, manipulation validity, interval precision, and direction are checked in order."
    },
    {
      "relative_position": "Far right lower",
      "shape": "Four compact status cards with solid, double, dotted, and hatched borders",
      "exact_title_to_render_inside": "来源边界",
      "exact_text": "直接运输｜条件校准\n证据不足｜拒绝外推",
      "icon": "four bounded zones beside a confidence interval",
      "caption_note": "Exact thresholds are frozen before unblinding; checkpoint and token observations do not increase the number of inferential units."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "A0, A1, and A2 must visibly originate from the same damaged precursor.",
    "Use a dashed border only for sham and dashed arrows only for stopping branches.",
    "Display paired run markers rather than treating checkpoints as replicates.",
    "Icons are monochrome thin line art.",
    "Do not render empirical outcomes, p-values, or unfrozen numeric thresholds.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic counterfactual technical-route diagram showing how structural-defect reduction and recovery specificity are tested in Chinese pretraining data. Use two tiers on a pure white canvas. At the top left, show “结构完整原文 / 统一背景池” as an ordered paragraph card. A solid arrow creates a dark-blue double-border “共同破损前体 / 错序｜截断｜断裂” with visibly displaced, clipped, and disconnected text lines. From this single common precursor, fan out into exactly three aligned cards: “A0 精确恢复 / 逆操作” with a reversible arrow restoring the original paragraph; “A1 保留破损 / 无恢复” with the broken paragraph unchanged; and “A2 等量 sham / 不恢复结构” with matched editing marks and a dashed pale-blue border.

All three arms converge into “平衡审计”, displaying the compact rows “token｜packing” and “来源｜主题｜预算”, anchored by a balance scale with equal token stacks. Flow downward to “来源 A 成对训练 / 共同 checkpoint / 六个主种子”, illustrated by one transformer checkpoint branching into six paired run markers. Continue into two evidence cards under “双证据读出”: “梯度对齐” with a vector-angle icon and “通用能力” with an independent evaluation sheet.

Finish the Source A stage at a double-border diamond “结构判定” containing the exact lines “A0>A1”, “A0>A2”, and “A1≈A2”. A dashed failure arrow leads to “停止结构路径”. The solid success branch enters a dashed card “来源 B 冻结复核 / A0−A1｜方向区间”, shown as a sealed checklist entering a second database. End with “来源边界” and the four compact outcomes “直接运输｜条件校准 / 证据不足｜拒绝外推”, using solid, double, dotted, and hatched borders rather than outcome colors.

Use Nature Blue borders: #1B3A5C for common reference and decisions, #2E6B9E for interventions, #5BA0D0 for inputs and outputs, #8EAEC4 dashed for sham, and #4D4D4D arrows. White fills only, 1.5 pt outlines, short Arial/Helvetica labels, and monochrome line icons. No empirical values, p-values, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F6 路线三：非冗余语义支持及状态—来源—尺度边界

**类型**：Technical Route / Counterfactual Experiment  
**色板**：Nature Blue；备选 ML TopConf Colorblind  
**caption reserve**：A0/A3/A4/A5 基于同一待移除集合；非冗余广度以来源、主题/实体和去重簇定义；主路径通过后才依次检验状态、来源和尺度边界。

### JSON figure spec

```json
{
  "diagram_type": "Technical Route for Nonredundant Semantic-Support Counterfactual Experiment",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Top left",
      "shape": "Large rounded data card, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "目标中文语体",
      "exact_text": "固定移除集合",
      "icon": "document cluster with one highlighted subset",
      "flow": "Four solid arrows fan out to A0, A3, A4, A5"
    },
    {
      "relative_position": "Upper middle, column 1",
      "shape": "Rounded card, #1B3A5C solid border, white fill",
      "exact_title_to_render_inside": "A0 完整参考",
      "exact_text": "保留原支持",
      "icon": "broad coverage network with diverse nodes"
    },
    {
      "relative_position": "Upper middle, column 2",
      "shape": "Rounded card, #8EAEC4 dashed border, white fill",
      "exact_title_to_render_inside": "A3 主流补回",
      "exact_text": "等 token",
      "icon": "target cluster removed and replaced by unrelated mainstream cards"
    },
    {
      "relative_position": "Upper middle, column 3",
      "shape": "Rounded card, #2E6B9E double border, white fill",
      "exact_title_to_render_inside": "A4 非冗余补回",
      "exact_text": "同语体广支持",
      "icon": "same-register network with many non-overlapping topic and entity nodes"
    },
    {
      "relative_position": "Upper middle, column 4",
      "shape": "Rounded card, #5BA0D0 dotted border, white fill",
      "exact_title_to_render_inside": "A5 窄支持补回",
      "exact_text": "同语体重复",
      "icon": "same-register network with repeated nodes in one narrow cluster"
    },
    {
      "relative_position": "Center full width",
      "shape": "Thin horizontal constraint band, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "共同约束",
      "exact_text": "背景池｜token｜长度｜质量分｜曝光",
      "icon": "five equal balance markers",
      "flow": "Solid arrow down to 来源 A 成对训练"
    },
    {
      "relative_position": "Bottom left-center",
      "shape": "Rounded rectangle, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "来源 A 成对训练",
      "exact_text": "共同 checkpoint\n六个主种子",
      "icon": "one model checkpoint branching into paired run markers",
      "flow": "Solid arrow right to 双证据读出"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Two adjacent cards, #2E6B9E and #5BA0D0 borders, white fill",
      "exact_title_to_render_inside": "双证据读出",
      "exact_text": "目标梯度对齐\n语体长尾能力",
      "icon": "vector angle beside branching knowledge tree",
      "flow": "Solid arrow right to 支持判定"
    },
    {
      "relative_position": "Bottom center-right",
      "shape": "Diamond, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "支持判定",
      "exact_text": "A0>A3\nA4>A3\nA4>A5\nA4≈A0",
      "icon": "three superiority bars and one equivalence band",
      "flow": "Solid arrow right to 结论分级"
    },
    {
      "relative_position": "Far right",
      "shape": "Four stacked output cards with solid, double, dashed, and dotted borders",
      "exact_title_to_render_inside": "结论分级",
      "exact_text": "完整恢复\n部分恢复\n语体曝光\n路径不成立",
      "icon": "four-level evidence ladder"
    },
    {
      "relative_position": "Bottom inset",
      "shape": "Three connected dashed mini-panels, #8EAEC4 borders, white fill",
      "exact_title_to_render_inside": "条件边界",
      "exact_text": "状态：双 checkpoint\n来源：B 冻结复核\n尺度：同 tokenizer",
      "icon": "training trajectory with two branch points, second database, and two model stacks of different height",
      "flow": "Dashed conditional sequence from 状态 to 来源 to 尺度",
      "caption_note": "State and Source B checks occur only after the Source A support path passes. Larger-model replication occurs only if at least one path maintains direction in Source B."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "A0, A3, A4, and A5 must originate from the same highlighted removal set.",
    "Distinguish broad nonredundant support from narrow repeated support by network topology as well as border style.",
    "The state, source, and scale boundary inset is dashed and secondary, never a rescue loop.",
    "Icons are monochrome thin line art.",
    "Do not render empirical values, p-values, or unfrozen equivalence margins.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic counterfactual technical-route diagram showing how nonredundant semantic-support loss is distinguished from mere register exposure in Chinese pretraining data. Start at the upper left with “目标中文语体 / 固定移除集合”, illustrated by a document cluster with one highlighted subset. Fan out from that identical subset into four aligned white cards: “A0 完整参考 / 保留原支持” with a broad diverse network; “A3 主流补回 / 等 token” with the target cluster replaced by unrelated mainstream cards and a dashed border; “A4 非冗余补回 / 同语体广支持” with many non-overlapping topic and entity nodes and a double border; and “A5 窄支持补回 / 同语体重复” with repeated nodes concentrated in one cluster and a dotted border.

Below all four arms, place a full-width constraint band “共同约束 / 背景池｜token｜长度｜质量分｜曝光” with five equal balance markers. Continue to “来源 A 成对训练 / 共同 checkpoint / 六个主种子”, then “双证据读出” with the exact two lines “目标梯度对齐” and “语体长尾能力”, using a vector-angle icon and branching knowledge tree.

End at a decision diamond “支持判定” containing “A0>A3”, “A4>A3”, “A4>A5”, and “A4≈A0”. Connect to a four-level result stack “结论分级” with “完整恢复 / 部分恢复 / 语体曝光 / 路径不成立”. Along the bottom, add three connected dashed mini-panels under “条件边界”: “状态：双 checkpoint” with two predefined branch points, “来源：B 冻结复核” with a second database receiving A4−A3, and “尺度：同 tokenizer” with two model stacks of different height. Make the scale panel reachable only after at least one path keeps its direction in Source B; no dashed branch may loop back to rescue the main path.

Use Nature Blue: #1B3A5C core, #2E6B9E intervention, #5BA0D0 data, #8EAEC4 frozen/secondary, #4D4D4D arrows. White fills, 1.5 pt outlines, Arial/Helvetica, monochrome line icons. No fabricated outcomes, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F7 双路径共享的冻结外部复核

**类型**：External Validation Decision Flow  
**色板**：Nature Blue；备选 ML TopConf Colorblind  
**caption reserve**：本图是研究内容二、三共享的边界检验子流程，不是第四项研究内容；来源 B 只运输来源 A 已存活且已冻结的主对比。

### JSON figure spec

```json
{
  "diagram_type": "Scientific External-Validation and Transport Decision Flow",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Far left",
      "shape": "Rounded rectangle, #1B3A5C solid border, white fill",
      "exact_title_to_render_inside": "来源 A 存活路径",
      "exact_text": "结构｜支持",
      "icon": "two path lines passing a gate",
      "flow": "Solid arrow right"
    },
    {
      "relative_position": "Left center",
      "shape": "Tall dashed container, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "冻结协议包",
      "exact_text": "处理规则\n主终点\n效应方向\n预测区间\n统计代码",
      "icon": "sealed checklist with five short rows",
      "flow": "Solid arrow right to 来源 B 四臂"
    },
    {
      "relative_position": "Center left",
      "shape": "Four compact cards, #5BA0D0 borders, white fill",
      "exact_title_to_render_inside": "来源 B 四臂",
      "exact_text": "完整｜破损\n主流｜非冗余",
      "icon": "second database feeding four compact run cards",
      "flow": "Solid arrow right into four-stage gate"
    },
    {
      "relative_position": "Center to center-right",
      "shape": "Four sequential diamond gates, alternating #1B3A5C and #2E6B9E borders",
      "exact_title_to_render_inside": "四级检查",
      "exact_text": "来源准入\n操纵验收\n区间精度\n方向区间",
      "icon": "four progressively narrower gate frames",
      "flow": "Solid arrows through all gates; dashed failure branches downward"
    },
    {
      "relative_position": "Lower row under first gate",
      "shape": "Dashed output card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "不可复核",
      "exact_text": "准入或操纵失败",
      "icon": "closed boundary line"
    },
    {
      "relative_position": "Lower row under precision gate",
      "shape": "Dotted output card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "证据不足",
      "exact_text": "区间过宽",
      "icon": "wide confidence interval crossing a reference band"
    },
    {
      "relative_position": "Right center",
      "shape": "Small process card, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "一次固定校准",
      "exact_text": "预算不变",
      "icon": "single wrench-like geometric adjustment marker, not a decorative icon",
      "flow": "Solid arrow to final decision; no feedback to threshold selection"
    },
    {
      "relative_position": "Far right",
      "shape": "Three stacked result cards with solid, double, and hatched borders",
      "exact_title_to_render_inside": "运输边界",
      "exact_text": "直接运输\n条件校准\n拒绝外推",
      "icon": "map divided into three bounded zones"
    },
    {
      "relative_position": "Top right inset",
      "shape": "Small dashed optional card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "尺度探索",
      "exact_text": "至少一路保持方向",
      "icon": "two model stacks of different height",
      "flow": "Dashed incoming arrow only from successful transport branch",
      "caption_note": "Larger-model exploration is cancelled if both paths fail to maintain direction in Source B."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "Keep the four checks sequential and visually non-circular.",
    "Failure branches are dashed and terminate in explicit evidence states.",
    "Do not draw Source B feeding back into threshold, register, endpoint, or code selection.",
    "The scale-exploration inset is conditional and secondary.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic decision-flow diagram showing external transport under a frozen protocol rather than a second tuning environment. Use a horizontal left-to-right flow on a pure white canvas. Begin with “来源 A 存活路径 / 结构｜支持”, illustrated by two path lines passing a gate. Connect it to a tall dashed pale-blue container “冻结协议包” with exactly five short rows: “处理规则”, “主终点”, “效应方向”, “预测区间”, and “统计代码”. Use a sealed checklist as the visual anchor, without a lock icon.

The frozen package enters “来源 B 四臂 / 完整｜破损 / 主流｜非冗余”, shown as a second database feeding four compact run cards. Next, draw four sequential diamond gates under the shared heading “四级检查”: “来源准入”, “操纵验收”, “区间精度”, and “方向区间”. Solid arrows continue right only after each gate passes. Dashed failure branches from the first two gates terminate at “不可复核 / 准入或操纵失败”; the precision gate can terminate at “证据不足 / 区间过宽”, with a wide interval crossing a reference band.

After the direction-and-interval gate, show one compact process card “一次固定校准 / 预算不变”, with no arrow returning to threshold or endpoint selection. The final vertical panel “运输边界” contains “直接运输”, “条件校准”, and “拒绝外推”, distinguished by solid, double, and hatched borders. Add a small dashed top-right inset “尺度探索 / 至少一路保持方向”, reachable only from a successful Source B branch.

Use Nature Blue: #1B3A5C decisions, #2E6B9E processes, #5BA0D0 data, #8EAEC4 frozen or uncertain states, and #4D4D4D arrows. White fills only, 1.5 pt borders, Arial/Helvetica, monochrome line icons. No feedback tuning loop, gradients, shadows, emojis, lock/fire/lightning icons, or 3D. Aspect ratio 16:9.

---

## F8 六臂反事实实验与预注册主对比

**类型**：Comparison / Experimental Design  
**色板**：Nature Blue；备选 Print-Safe Gray  
**caption reserve**：A0 的结构目标和支持目标来自互不重叠文档集合；共同参考不意味着两条路径的估计量可直接比较；所有臂共享背景池与训练预算。

### JSON figure spec

```json
{
  "diagram_type": "Academic Six-Arm Counterfactual Experimental Design",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Far left center",
      "shape": "Large data-pool cylinder, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "共同背景池",
      "exact_text": "等 token｜等预算",
      "icon": "database cylinder with equal token stacks",
      "flow": "Two solid arrows to upper and lower comparison groups"
    },
    {
      "relative_position": "Upper group",
      "shape": "Wide grouping panel, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "结构路径",
      "internal_content": {
        "layout": "Three equal-width cards",
        "arm_0": {"exact_text": "A0 精确恢复", "icon": "ordered paragraph"},
        "arm_1": {"exact_text": "A1 保留破损", "icon": "broken paragraph"},
        "arm_2": {"exact_text": "A2 等量 sham", "icon": "matched edits without recovery"}
      }
    },
    {
      "relative_position": "Above upper group",
      "shape": "Two curved comparison brackets",
      "exact_floating_text": "A0−A1｜A0−A2",
      "exact_secondary_note": "A1≈A2",
      "icon": "two superiority bars and one equivalence band"
    },
    {
      "relative_position": "Lower group",
      "shape": "Wide grouping panel, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "支持路径",
      "internal_content": {
        "layout": "Four equal-width cards",
        "arm_0": {"exact_text": "A0 完整参考", "icon": "broad original coverage"},
        "arm_3": {"exact_text": "A3 主流补回", "icon": "unrelated mainstream cards"},
        "arm_4": {"exact_text": "A4 非冗余补回", "icon": "broad same-register network"},
        "arm_5": {"exact_text": "A5 窄支持补回", "icon": "repeated narrow cluster"}
      }
    },
    {
      "relative_position": "Below lower group",
      "shape": "Four compact comparison brackets",
      "exact_floating_text": "A0−A3｜A4−A3｜A4−A5｜A4≈A0",
      "icon": "three superiority bars and one equivalence band"
    },
    {
      "relative_position": "Center vertical divider",
      "shape": "Thick grey separation rule with two non-overlap tray icons",
      "exact_floating_text": "目标文档集合互不重叠"
    },
    {
      "relative_position": "Far right",
      "shape": "Two stacked output cards, #1B3A5C and #2E6B9E borders, white fill",
      "exact_title_to_render_inside": "预注册终点",
      "exact_text": "通用知识\n语体长尾",
      "icon": "two independent evaluation sheets"
    },
    {
      "relative_position": "Bottom center",
      "shape": "Borderless emphasis band",
      "exact_floating_text": "共同参考 ≠ 路径估计量直接比较",
      "caption_note": "This diagram can replace the existing six-arm text table. A0 is shown in both groups only as a shared reference definition, not as duplicated treatment data."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "Keep the upper structural group and lower support group visibly separated.",
    "A0 may appear in both groups as a reference label, but add the non-overlap statement prominently.",
    "Use brackets and interval icons rather than directional causal arrows between the two path estimands.",
    "Icons are monochrome thin line art.",
    "Do not show empirical effect sizes, p-values, or fabricated outcomes.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic comparison diagram showing a six-arm counterfactual experimental design with two separate estimand families. On the far left, place a data-pool cylinder “共同背景池 / 等 token｜等预算”, with two arrows feeding an upper structural group and a lower support group. The upper white panel is titled “结构路径” and contains three equal cards: “A0 精确恢复” with an ordered paragraph, “A1 保留破损” with a broken paragraph, and “A2 等量 sham” with matched edits that do not restore structure. Above the cards, draw two comparison brackets labeled exactly “A0−A1｜A0−A2”, plus a compact equivalence note “A1≈A2”.

The lower panel is titled “支持路径” and contains four equal cards: “A0 完整参考” with broad original support, “A3 主流补回” with unrelated mainstream documents, “A4 非冗余补回” with a broad same-register network, and “A5 窄支持补回” with a repeated narrow cluster. Under the panel, draw compact brackets labeled “A0−A3｜A4−A3｜A4−A5｜A4≈A0”.

Separate the groups using a strong neutral divider and two non-overlapping tray icons labeled “目标文档集合互不重叠”. On the right, show “预注册终点” with two stacked output cards “通用知识” and “语体长尾”. At the bottom, emphasize the exact statement “共同参考 ≠ 路径估计量直接比较”.

Use Nature Blue: #1B3A5C for references and endpoints, #2E6B9E for the structure group, #5BA0D0 for the support group, #8EAEC4 for secondary comparisons, and #4D4D4D lines. White fills, 1.5 pt borders, Arial/Helvetica, monochrome icons, and dual coding by border patterns and network topology. No effect values, p-values, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F9 能力定向梯度对齐的候选动力学证据链

**类型**：Module Detail  
**色板**：Nature Blue；备选 Blue Monochrome  
**caption reserve**：主读出为末层低秩投影后、单位 token 归一化的梯度余弦；完整公式、投影维度、checkpoint 位置及 probe 规则在冻结清单中，不在图内展开。

### JSON figure spec

```json
{
  "diagram_type": "Academic Module Detail for Capability-Directed Gradient Alignment",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "89mm (single column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Upper left",
      "shape": "Rounded data card, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "处理语料 probe",
      "exact_text": "单位 token",
      "icon": "small token sequence and batch grid",
      "flow": "Solid arrow right to 末层投影"
    },
    {
      "relative_position": "Lower left",
      "shape": "Rounded data card, #5BA0D0 double border, white fill",
      "exact_title_to_render_inside": "独立能力诊断集",
      "exact_text": "完全隔离",
      "icon": "separate evaluation sheet and document set",
      "flow": "Solid arrow right to 末层投影"
    },
    {
      "relative_position": "Center left",
      "shape": "Tall model block, #1B3A5C dashed border, white fill",
      "exact_title_to_render_inside": "固定 checkpoint",
      "exact_text": "末层低秩投影",
      "icon": "stacked transformer layers with the last layer highlighted",
      "flow": "Two solid arrows right to 梯度向量"
    },
    {
      "relative_position": "Center",
      "shape": "Large circular vector-angle panel, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "能力定向梯度对齐",
      "exact_text": "cos(g处理, g能力)",
      "icon": "two vectors from one origin with a clearly marked angle arc",
      "flow": "Solid arrow right to 时间证据链"
    },
    {
      "relative_position": "Right vertical chain",
      "shape": "Four vertically connected small cards, alternating #1B3A5C and #2E6B9E borders",
      "exact_title_to_render_inside": "四项联合证据",
      "exact_text": "处理改变读出\n读出先于能力\n恢复共同逆转\n留出预测增益",
      "icon": "four-node time-ordered chain",
      "flow": "Solid arrow down to 候选机制"
    },
    {
      "relative_position": "Bottom right",
      "shape": "Rounded output card, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "候选动力学机制",
      "exact_text": "非完整中介",
      "icon": "bounded causal-chain icon with a caution divider"
    },
    {
      "relative_position": "Bottom left inset",
      "shape": "Small dotted auxiliary panel, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "次级指标",
      "exact_text": "损失｜有效秩\n裁剪率｜遗忘率",
      "icon": "four tiny diagnostic charts",
      "flow": "Dotted side arrow to sensitivity note only",
      "caption_note": "Secondary metrics cannot replace the primary alignment readout."
    },
    {
      "relative_position": "Top margin",
      "shape": "Small dashed manifest strip",
      "exact_floating_text": "checkpoint｜probe｜规则｜归一化：预先冻结"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "Keep treatment probe and capability diagnostic set visually isolated before they enter the fixed checkpoint.",
    "Show only the one-line cosine notation; place full formula and dimensions in the caption.",
    "Use a time-ordered four-node chain, not a generic mediation triangle.",
    "Secondary metrics use dotted borders and never replace the main flow.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic module-detail diagram explaining capability-directed gradient alignment as a bounded candidate dynamical mechanism. Use a pure white 4:3 canvas. On the left, place two clearly isolated data cards: upper “处理语料 probe / 单位 token” with a small token-sequence and batch-grid icon, and lower “独立能力诊断集 / 完全隔离” with a separate evaluation sheet. Both feed into a tall dashed dark-navy block “固定 checkpoint / 末层低秩投影”, illustrated by stacked transformer layers with only the final layer highlighted.

At the center, draw a large circular vector panel titled “能力定向梯度对齐”. Show two arrows from the same origin, one representing the treatment gradient and one the independent capability gradient, with a clean angle arc between them. Render only the compact expression “cos(g处理, g能力)” and no full derivation. Across the top, add a dashed manifest strip with the exact text “checkpoint｜probe｜规则｜归一化：预先冻结”.

To the right, create a time-ordered four-node chain under “四项联合证据”: “处理改变读出”, “读出先于能力”, “恢复共同逆转”, and “留出预测增益”. The chain ends at a double-border result card “候选动力学机制 / 非完整中介”. At the bottom left, place a dotted auxiliary panel “次级指标” with “损失｜有效秩 / 裁剪率｜遗忘率” and four tiny diagnostic thumbnails; connect it only to a sensitivity note, not to the main decision chain.

Use Nature Blue #1B3A5C, #2E6B9E, #5BA0D0, auxiliary #8EAEC4, and dark-grey #4D4D4D arrows. White fills, 1.5 pt outlines, Arial/Helvetica labels, monochrome icons. No empirical values, long formulas, gradients, shadows, emojis, or 3D. Aspect ratio 4:3.

---

## F10 双路径联合判定与可证伪决策树

**类型**：Statistical Decision Flow  
**色板**：Nature Blue；备选 Print-Safe Gray  
**caption reserve**：最小实践意义阈值和等效界值在揭盲前冻结；正式检验为六个配对区组的单侧精确符号翻转检验；图中不显示尚未冻结的具体界值。

### JSON figure spec

```json
{
  "diagram_type": "Academic Statistical Decision Tree for Two Independently Falsifiable Paths",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Top center",
      "shape": "Wide header strip, #1B3A5C double border, white fill",
      "exact_title_to_render_inside": "两路径独立反证",
      "exact_text": "各自单侧 α=0.025｜无路径间门控",
      "icon": "one input splitting into two independent decision lanes",
      "flow": "Two solid arrows down"
    },
    {
      "relative_position": "Left lane",
      "shape": "Large rounded grouping panel, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "结构路径",
      "internal_content": {
        "layout": "Two sequential superiority gates and one manipulation note",
        "gate_1": {"exact_text": "A0−A1 下界过阈值", "icon": "one-sided lower confidence bound above a vertical threshold"},
        "gate_2": {"exact_text": "A0−A2 下界过阈值", "icon": "one-sided lower confidence bound above a vertical threshold"},
        "note": {"exact_text": "A1≈A2 操纵预期", "icon": "interval inside equivalence band"}
      },
      "branch_yes": "Solid arrow to 确认结构路径",
      "branch_no": "Dashed arrow to 不确认完整路径"
    },
    {
      "relative_position": "Right lane",
      "shape": "Large rounded grouping panel, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "支持路径",
      "internal_content": {
        "layout": "Three superiority gates followed by one equivalence gate",
        "gate_1": {"exact_text": "A0−A3 下界过阈值", "icon": "one-sided lower bound"},
        "gate_2": {"exact_text": "A4−A3 下界过阈值", "icon": "one-sided lower bound"},
        "gate_3": {"exact_text": "A4−A5 下界过阈值", "icon": "one-sided lower bound"},
        "gate_4": {"exact_text": "A4−A0 落入等效界", "icon": "two-sided interval inside equivalence band"}
      },
      "branch_yes": "Solid arrow to 确认支持路径",
      "branch_no": "Dashed arrow to 部分恢复或不成立"
    },
    {
      "relative_position": "Bottom left and right outcomes",
      "shape": "Four result cards with solid, double, dotted, and hatched borders",
      "exact_title_to_render_inside": "证据结论",
      "exact_text": "路径确认｜部分支持\n证据不足｜路径反证",
      "icon": "four-level evidence ladder"
    },
    {
      "relative_position": "Bottom center-left inset",
      "shape": "Dashed resource decision card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "功效不足",
      "exact_text": "转移可选预算\n增加配对种子\n仍不足则区间估计",
      "icon": "resource bar moving from optional branch to paired-run markers"
    },
    {
      "relative_position": "Bottom center-right inset",
      "shape": "Dotted mechanism downgrade card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "动力学读出失败",
      "exact_text": "保留总效应\n删除机制解释",
      "icon": "causal-chain line ending while an effect interval remains"
    },
    {
      "relative_position": "Bottom margin",
      "shape": "Borderless note",
      "exact_floating_text": "任一必要条件失败 → 不确认完整路径",
      "caption_note": "All superiority gates use one-sided 97.5% randomization-inversion lower confidence bounds; A4-A0 uses a two-sided 95% equivalence interval."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE fill with Nature Blue borders only.",
    "Keep the two path lanes independent; no gate crosses between lanes.",
    "Use interval glyphs without fabricated numeric thresholds.",
    "All required gates within a path use an intersection rule, not a voting rule.",
    "Failure branches are dashed and terminate in explicit downgraded conclusions.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic statistical decision tree showing two independently falsifiable research paths. At the top center, place a wide double-border header “两路径独立反证” with the exact line “各自单侧 α=0.025｜无路径间门控”. Split into two independent vertical lanes with no cross-links.

The left lane is titled “结构路径”. Show two required superiority gates in sequence: “A0−A1 下界过阈值” and “A0−A2 下界过阈值”, each illustrated by a one-sided lower confidence bound lying beyond an unlabeled practical threshold. Add a secondary note “A1≈A2 操纵预期” with an interval inside an equivalence band. A solid pass branch leads to “确认结构路径”; any failed required gate uses a dashed branch to “不确认完整路径”.

The right lane is titled “支持路径”. Show three required superiority gates—“A0−A3 下界过阈值”, “A4−A3 下界过阈值”, and “A4−A5 下界过阈值”—followed by “A4−A0 落入等效界” with a two-sided interval inside a shaded equivalence band. Its pass branch leads to “确认支持路径”; failed gates lead to “部分恢复或不成立”.

Across the bottom, show “证据结论” with “路径确认｜部分支持 / 证据不足｜路径反证”. Add two dashed secondary cards: “功效不足 / 转移可选预算 / 增加配对种子 / 仍不足则区间估计”, and “动力学读出失败 / 保留总效应 / 删除机制解释”. Emphasize “任一必要条件失败 → 不确认完整路径”.

Use Nature Blue #1B3A5C, #2E6B9E, #5BA0D0, auxiliary #8EAEC4, and grey #4D4D4D arrows. White fills, 1.5 pt borders, short Arial/Helvetica labels. Align every interval glyph to a shared horizontal baseline, and use border patterns to keep all four evidence conclusions distinguishable in grayscale. Do not show numeric thresholds, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F11 四年任务—里程碑—资源配置图

**类型**：Timeline / Research Roadmap  
**色板**：Nature Blue；备选 Blue Monochrome  
**caption reserve**：执行年度的具体起止年月以当年指南和批准通知为准；27.4B token 是上限预算；第四年状态/尺度探索为条件触发项；A100 未落实且不计入稳定条件。

### JSON figure spec

```json
{
  "diagram_type": "Academic Four-Year Research Timeline and Resource Roadmap",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Top horizontal axis",
      "shape": "Four equal timeline columns separated by 1.0pt dividers",
      "exact_floating_text": "第一年｜第二年｜第三年｜第四年"
    },
    {
      "relative_position": "Column 1",
      "shape": "Rounded task card, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "操作定义与先导",
      "exact_text": "许可审计\n双评分盲标\n六臂生成\n6×0.10B",
      "icon": "data card, annotators, and six small run cards",
      "flow": "Solid arrow to milestone diamond"
    },
    {
      "relative_position": "Column 2",
      "shape": "Rounded task card, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "来源 A 确认",
      "exact_text": "六臂×六种子\n单次 0.40B\n双路径判定",
      "icon": "one checkpoint branching to paired runs and two path intervals",
      "flow": "Solid arrow to milestone diamond"
    },
    {
      "relative_position": "Column 3",
      "shape": "Rounded task card, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "来源 B 复核",
      "exact_text": "四臂×六种子\n单次 0.40B\n冻结运输",
      "icon": "sealed protocol entering a second database",
      "flow": "Solid arrow to milestone diamond"
    },
    {
      "relative_position": "Column 4",
      "shape": "Rounded optional task card, #8EAEC4 dashed border, white fill",
      "exact_title_to_render_inside": "边界探索与凝练",
      "exact_text": "状态｜尺度\n可选 ≤2.8B\n成果整合",
      "icon": "two checkpoint branches, two model sizes, and report stack",
      "flow": "Dashed incoming arrow from Year 3 pass gate"
    },
    {
      "relative_position": "Middle milestone row",
      "shape": "Four diamond nodes, #1B3A5C borders, white fill",
      "exact_title_to_render_inside": "年度闸门",
      "exact_text": "操纵通过\n路径存活\n运输判定\n边界结论",
      "icon": "four milestone diamonds connected by a solid timeline"
    },
    {
      "relative_position": "Bottom resource row",
      "shape": "Three aligned resource bands, blue borders and white fill",
      "exact_title_to_render_inside": "资源配置",
      "exact_text": "A40：同构训练\n3090 Ti：评分评测\n总上限约 27.4B token",
      "icon": "GPU board, scoring gauge, and token-budget bar"
    },
    {
      "relative_position": "Bottom right note",
      "shape": "Dotted neutral note card",
      "exact_text": "继续｜收缩｜停止",
      "caption_note": "Optional Year 4 tasks are cancelled first when a path gate fails or measured resources are insufficient."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All cards use WHITE fill with Nature Blue borders only.",
    "Use four equal-width year columns and align tasks, milestones, and resource bands.",
    "Year 4 is visually conditional with a dashed border and dashed incoming arrow.",
    "Do not show calendar dates or imply that A100 resources are available.",
    "Use resource bars as budget allocations, not empirical progress bars.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic four-year research roadmap combining tasks, milestones, and resource allocation. Use a pure white canvas divided into four equal columns labeled exactly “第一年｜第二年｜第三年｜第四年”. In Year 1, show “操作定义与先导” with the short rows “许可审计”, “双评分盲标”, “六臂生成”, and “6×0.10B”; use data-card, annotator, and six-run thumbnails. In Year 2, show “来源 A 确认” with “六臂×六种子”, “单次 0.40B”, and “双路径判定”, anchored by a common checkpoint and paired-run markers. In Year 3, show “来源 B 复核” with “四臂×六种子”, “单次 0.40B”, and “冻结运输”, anchored by a sealed protocol entering a second database. In Year 4, use a dashed pale-blue card “边界探索与凝练” with “状态｜尺度”, “可选 ≤2.8B”, and “成果整合”; its incoming arrow must be dashed and conditional on the Year 3 gate.

Across the middle, connect four milestone diamonds under “年度闸门”: “操纵通过”, “路径存活”, “运输判定”, and “边界结论”. Along the bottom, place one full-width resource band “资源配置” with “A40：同构训练”, “3090 Ti：评分评测”, and “总上限约 27.4B token”, illustrated by a GPU board, scoring gauge, and token budget bar. Add a small dotted note “继续｜收缩｜停止”.

Use Nature Blue #1B3A5C for milestones, #2E6B9E for validation, #5BA0D0 for early data work, #8EAEC4 dashed for optional work, and #4D4D4D arrows. White fills, 1.5 pt borders, Arial/Helvetica labels, and monochrome line icons. Keep milestone diamonds aligned. Do not render dates, A100 availability, empirical progress, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F12 风险信号、替代路线与降级交付地图

**类型**：Risk Matrix / Decision Map  
**色板**：Nature Blue；备选 Print-Safe Gray  
**caption reserve**：五类风险及处置均来自申报书研究基础 1.4；失败分支保留可回答的科学问题，不通过追加来源、阈值或模型追逐同向结果。

### JSON figure spec

```json
{
  "diagram_type": "Academic Risk Signal, Mitigation, and Downgraded-Deliverable Matrix",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {"palette": "Nature Blue", "background": "#FFFFFF", "core": "#1B3A5C", "process": "#2E6B9E", "data": "#5BA0D0", "frozen": "#8EAEC4", "text": "#333333", "arrow": "#4D4D4D"},
  "layout_and_content_blocks": [
    {
      "relative_position": "Top header row",
      "shape": "Three column headers with #1B3A5C lower rules",
      "exact_floating_text": "早期信号｜处置动作｜降级交付"
    },
    {
      "relative_position": "Row 1",
      "shape": "Three-cell horizontal lane, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "技术操纵",
      "exact_text": "重叠或配平失败｜重设 sham｜失配审计",
      "icon": "overlap scatter, matched-edit symbol, and audit report"
    },
    {
      "relative_position": "Row 2",
      "shape": "Three-cell horizontal lane, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "统计识别",
      "exact_text": "效应小于方差｜增加配对种子｜区间估计",
      "icon": "wide interval, paired markers, and interval report"
    },
    {
      "relative_position": "Row 3",
      "shape": "Three-cell horizontal lane, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "进度合规",
      "exact_text": "许可或标注滞后｜收缩可核验子集｜来源 A 闭环",
      "icon": "license sheet, smaller verified data tray, and closed-loop report"
    },
    {
      "relative_position": "Row 4",
      "shape": "Three-cell horizontal lane, #2E6B9E border, white fill",
      "exact_title_to_render_inside": "计算资源",
      "exact_text": "吞吐或存储不足｜取消可选探索｜下调统一 token",
      "icon": "throughput gauge, crossed optional branch without X symbol, and reduced equal token bars"
    },
    {
      "relative_position": "Row 5",
      "shape": "Three-cell horizontal lane, #8EAEC4 dashed border, white fill",
      "exact_title_to_render_inside": "外部效度",
      "exact_text": "来源 B 复核失败｜区分失败类型｜运输边界图",
      "icon": "second database, four-way classification tree, and bounded map"
    },
    {
      "relative_position": "Far right vertical band",
      "shape": "Vertical stepped bracket, #1B3A5C solid line",
      "exact_title_to_render_inside": "保留科学问题",
      "exact_text": "总效应\n失败机制\n适用边界",
      "icon": "three report folders on descending steps"
    },
    {
      "relative_position": "Bottom emphasis band",
      "shape": "Borderless wide note",
      "exact_floating_text": "不追加来源｜不移动阈值｜不追逐正结果",
      "caption_note": "Failure states are pre-specified scientific outcomes rather than generic project failure."
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All cells use WHITE fill with Nature Blue borders only.",
    "Use a five-row by three-stage matrix with consistent column alignment.",
    "Color indicates workflow role, not risk severity.",
    "Use line patterns and icons to preserve meaning in grayscale.",
    "Do not use red-green traffic-light encoding or alarming decorative symbols.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
```

### Image prompt

Flat vector academic risk matrix showing how early warning signals lead to predefined mitigation and scientifically meaningful downgraded deliverables. Use a pure white canvas with a five-row by three-stage matrix. Across the top, render exactly “早期信号｜处置动作｜降级交付”. Each row has a short title at the left and three aligned content cells.

Row 1, “技术操纵”: “重叠或配平失败｜重设 sham｜失配审计”, with an overlap scatter, matched-edit symbol, and audit report. Row 2, “统计识别”: “效应小于方差｜增加配对种子｜区间估计”, with a wide interval, paired-run markers, and an interval report. Row 3, “进度合规”: “许可或标注滞后｜收缩可核验子集｜来源 A 闭环”, with a license sheet, a smaller verified data tray, and a closed-loop report. Row 4, “计算资源”: “吞吐或存储不足｜取消可选探索｜下调统一 token”, with a throughput gauge, a faded optional branch, and equally reduced token bars. Row 5, “外部效度”: “来源 B 复核失败｜区分失败类型｜运输边界图”, with a second database, a four-way classification tree, and a bounded map.

At the far right, add a stepped bracket titled “保留科学问题” with “总效应 / 失败机制 / 适用边界” represented by three report folders. Across the bottom, emphasize “不追加来源｜不移动阈值｜不追逐正结果”.

Use Nature Blue #1B3A5C, #2E6B9E, #5BA0D0, dashed #8EAEC4, and dark-grey #4D4D4D. Color indicates workflow role, not severity; use border patterns and icons for grayscale accessibility. White fills, 1.5 pt outlines, Arial/Helvetica labels, monochrome line icons. No red-green traffic lights, alarm symbols, gradients, shadows, emojis, or 3D. Aspect ratio 16:9.

---

## F13 公开数据结构操纵预实验

**类型**：Data Behavior + Validation
**色板**：Nature Blue；备选 ML TopConf Colorblind
**caption reserve**：结果来自 ChineseWebText2.0 公开测试集和固定版本 Qwen2.5-0.5B；预实验只证明数据/模型可访问、扰动可计算及恢复/sham 可核查，不是继续预训练、能力终点或机制证据。

### JSON figure spec

~~~json
{
  "diagram_type": "Academic Preliminary Experiment Data Behavior and Validation Figure",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {"title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt monospace/italic"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {
    "palette": "Nature Blue",
    "background": "#FFFFFF",
    "core": "#1B3A5C",
    "process": "#2E6B9E",
    "data": "#5BA0D0",
    "frozen": "#8EAEC4",
    "text": "#333333",
    "arrow": "#4D4D4D"
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far left",
      "shape": "Vertical funnel panel, #5BA0D0 border, white fill",
      "exact_title_to_render_inside": "公开数据筛选",
      "exact_text": "原始 1,000\n合格 122\n标定 30\n评估 50",
      "icon": "database cylinder flowing through a four-stage sample funnel",
      "flow": "Solid arrow right to 冻结设置"
    },
    {
      "relative_position": "Upper center-left",
      "shape": "Dashed setup card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "冻结设置",
      "exact_text": "Qwen2.5-0.5B\n块宽 128 字",
      "icon": "small stacked transformer layers beside a fixed-width text block",
      "flow": "Solid arrow right to 五种状态",
      "caption_note": "Dataset: ChineseWebText2.0 public test split; fixed random seed 20270906; no sample triggered 1,024-token truncation."
    },
    {
      "relative_position": "Center large panel",
      "shape": "Wide chart panel, #1B3A5C border, white fill",
      "exact_title_to_render_inside": "中位 causal-LM loss",
      "exact_axis_label_y": "loss",
      "exact_text": "原文 3.101\n繁体 3.049\n扰动 3.379\n恢复 3.101\nsham 3.368",
      "icon": "five aligned lollipop markers with distinct circle, square, triangle, diamond, and cross shapes",
      "flow": "Solid arrow right to 操纵验证"
    },
    {
      "relative_position": "Right upper results",
      "shape": "Three stacked validation cards, #2E6B9E borders, white fill",
      "exact_title_to_render_inside": "操纵验证",
      "exact_text": "扰动差 0.211\n95% CI 0.180–0.276\n恢复率 100%\nsham 非恢复 100%",
      "icon": "paired-difference interval, closed recovery loop, and broken sham return arrow"
    },
    {
      "relative_position": "Right lower result",
      "shape": "Dotted auxiliary card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "交叉检查",
      "exact_text": "第二评分器同方向\n无 1,024-token 截断",
      "icon": "second scoring gauge beside an unclipped token sequence"
    },
    {
      "relative_position": "Bottom center-left",
      "shape": "Hatched caution card, #8EAEC4 border, white fill",
      "exact_title_to_render_inside": "同分条件未满足",
      "exact_text": "重叠率 0.66\n成对差 0.303\n95% CI 0.220–0.360",
      "icon": "two partially overlapping distributions with separated paired markers",
      "caption_note": "Traditional-character conversion changed token counts; this pilot does not establish static-score equivalence."
    },
    {
      "relative_position": "Bottom full-width evidence boundary",
      "shape": "Two-column conclusion band, #1B3A5C solid divider, white fill",
      "exact_title_to_render_inside": "证据边界",
      "exact_text": "已证明：可访问｜可计算｜可恢复\n未证明：继续预训练｜能力效应｜因果机制",
      "icon": "three checked geometric nodes separated from three open geometric nodes"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All boxes use WHITE #FFFFFF fill with Nature Blue colored borders only.",
    "Render the five observed median losses exactly as supplied; do not interpolate or invent error bars for them.",
    "Use shape, line style, and labels in addition to color for all five text states.",
    "The confidence interval belongs only to the paired disturbance-minus-original median difference.",
    "Keep established findings and unestablished claims in visibly separate columns.",
    "Icons are monochrome thin line art.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering.",
    "NO gradients or decorative shadows.",
    "Canvas is pure white #FFFFFF."
  ]
}
~~~

### Image prompt

Flat vector academic data-behavior and validation figure presenting a real public-data preliminary experiment for structural text manipulation. Use a pure white canvas with a left-to-right evidence flow. On the far left, draw a vertical sample funnel titled exactly “公开数据筛选”, with “原始 1,000”, “合格 122”, “标定 30”, and “评估 50”. Connect it to a dashed setup card “冻结设置” containing “Qwen2.5-0.5B” and “块宽 128 字”, anchored by a small transformer stack and a fixed-width text block.

The largest center panel is titled “中位 causal-LM loss”. Show five aligned lollipop markers on one shared vertical loss axis, using distinct shapes as well as one Nature Blue lightness ramp. Render the exact labels and values: “原文 3.101”, “繁体 3.049”, “扰动 3.379”, “恢复 3.101”, and “sham 3.368”. Do not invent uncertainty bars for these five medians. On the upper right, show “操纵验证” with “扰动差 0.211”, “95% CI 0.180–0.276”, “恢复率 100%”, and “sham 非恢复 100%”, using a paired-difference interval, a closed recovery loop, and a broken sham-return arrow. Below it, add “交叉检查 / 第二评分器同方向 / 无 1,024-token 截断”.

Place a hatched caution card below the plot: “同分条件未满足 / 重叠率 0.66 / 成对差 0.303 / 95% CI 0.220–0.360”. Across the bottom, use a two-column band “证据边界”: left “已证明：可访问｜可计算｜可恢复”; right “未证明：继续预训练｜能力效应｜因果机制”.

Use Nature Blue #1B3A5C, #2E6B9E, #5BA0D0, auxiliary #8EAEC4, text #333333, and arrows #4D4D4D. White fills, 1.5 pt borders, Arial/Helvetica, and monochrome line icons. No fabricated values, gradients, shadows, emojis, decorative symbols, or 3D. Aspect ratio 16:9.

---

## Prompt Package 完整性

- **已分析材料**：`projects/NSFC_2027_yuwei_llm/main.pdf` 全部 27 页；同时核对对应 LaTeX 源文段以避免 PDF 抽取断行造成误读。
- **当前输出类型**：完整 Figure Plan 对应的 13 组 classic academic JSON specs 与英文 image prompts；未执行生图。
- **高置信信息**：双路径逻辑、三条核心技术路线、六臂定义、主对比、能力定向梯度对齐、统计判据、外部复核、预实验真实结果和年度资源上限。
- **待确认信息**：来源 A/B 正式名称、确认性与稳健性语体、具体约 1B 开源基座、能力终点名称、实践阈值/等效界值及最终落稿图数。
- **建议补充材料**：生图前优先确认最终采用 F1--F6 全套还是从 F7--F13 中替换/增补；确认后可在同一视觉系统下逐图生成并做文字重排。
