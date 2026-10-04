---
document: "出图规范与 Prompt（F7—F12）"
stage: "05_figure_plan"
project: "NSFC_2027_Mapping"
skill: "academic-figure-prompt v1.5.0"
input: "01_Figure_Plan.md + 02_Palette_Decision.md"
version: "2026-09-06"
---

# Figure Prompts F07—F12

共用样式、CJK 渲染对策见 `03_Figure_Prompts_F01-F06.md` 开头「使用前必读」，本文件不重复。

---

## F7 技术路线图三：标准检索与关系挑战的联合验证

**type** Technical Route / Eval Protocol ｜ **aspect** 16:9 ｜ **落点** 研究内容三 ｜ **优先级** must

### JSON spec

```json
{
  "diagram_type": "Technical Route — stratified evaluation protocol with attribution control",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "gate_border": "1.5pt solid #D95F02", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid", "feedback_arrow": "1.0pt dashed curved"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "input_model": "#1B3A5C 1.5pt solid border, white fill",
      "eval_dimension": "#2E6B9E 1.5pt solid border, white fill",
      "dedup_gate": "#D95F02 1.5pt solid border, white fill",
      "control_bar": "#5BA0D0 1.0pt solid border, #F7F7F7 fill",
      "exit_positive": "#009E73 1.5pt solid border, white fill",
      "exit_negative": "#8EAEC4 1.5pt dashed border, white fill",
      "eval_panel_bg": "#F2F6FA"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid", "feedback_loop": "#4D4D4D dashed curved"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left",
      "shape": "Tall box, #1B3A5C 1.5pt border, white fill",
      "icon": "stacked horizontal layers with a curved residual arrow, monochrome",
      "exact_title_to_render_inside": "三臂检索模型",
      "exact_text": "来自内容二",
      "flow": "Arrows fanning RIGHT into the five evaluation dimensions"
    },
    {
      "relative_position": "Center, five columns on a #F2F6FA panel",
      "shape": "Five boxes, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "分层评测五维",
      "internal_content": {
        "col_1": {"exact_header": "标准检索", "icon": "gauge with tick marks", "exact_text": "RSITMD · RSICD 双向\\n原始划分与协议\\nR@1 / R@5 / R@10 · mR"},
        "col_2": {"exact_header": "关系挑战", "icon": "two dots joined by a directed line", "exact_text": "人工核验子集\\n关系冲突误匹配率\\n关系判别准确率"},
        "col_3": {"exact_header": "覆盖度稳健性", "icon": "small stepped bar chart", "exact_text": "按描述覆盖程度分档\\n区分真实自然样本\\n与人工扰动样本"},
        "col_4": {"exact_header": "迁移", "icon": "two overlapping circles (Venn)", "exact_text": "同域比较\\n目标域未参训迁移\\n真正数据独立测试"},
        "col_5": {"exact_header": "效率", "icon": "stopwatch outline", "exact_text": "可训练参数量\\n训练开销\\n索引与查询耗时"}
      }
    },
    {
      "relative_position": "Attached above column 4 as a gate",
      "shape": "Small box, #D95F02 1.5pt border, white fill",
      "exact_title_to_render_inside": "去重闸口",
      "exact_text": "原图 + 近重复 + 同源切片联合去重",
      "secondary_note": "不以数据集名不同即认定独立"
    },
    {
      "relative_position": "Attached beside column 2 as a warning note",
      "shape": "#8EAEC4 1.0pt dashed border, no fill",
      "exact_text": "与标准结果分开报告；改动真值后不与原论文数字直接比较",
      "secondary_note": "7pt #666666"
    },
    {
      "relative_position": "Attached beneath column 5",
      "shape": "No border, 7pt grey text",
      "exact_text": "注明硬件、图库规模与批大小"
    },
    {
      "relative_position": "Bottom Bar, full width",
      "shape": "Control bar, #5BA0D0 1.0pt border, #F7F7F7 fill, three equal cells",
      "exact_title_to_render_inside": "可归因性控制",
      "exact_text": "等参数量与等训练步数对照\\n近重复与同源切片去重\\n三级测试分别定义分别报告"
    },
    {
      "relative_position": "Far Right Top",
      "shape": "Rounded rectangle, #009E73 1.5pt border, white fill",
      "exact_title_to_render_inside": "正向出口",
      "exact_text": "性能变化可归因于关系建模本身"
    },
    {
      "relative_position": "Far Right Bottom",
      "shape": "Rounded rectangle, #8EAEC4 1.5pt dashed border, white fill",
      "exact_title_to_render_inside": "反向出口",
      "exact_text": "等预算下改进消失 → 如实报告负结果\\n贡献收敛到评测协议与失效模式刻画"
    },
    {
      "relative_position": "Bottom, curved dashed arrow running right to left",
      "shape": "Curved dashed arrow, #4D4D4D 1.0pt",
      "exact_floating_text": "错误归因回流 → 内容一 / 内容二"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "The five evaluation columns share one border color; they are distinguished by their icons and headers, not by five different hues.",
    "The 去重闸口 box is the only orange element in the upper half and must read as a gate placed on the path into 迁移.",
    "The dashed feedback arc must not cross any forward arrow.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "各指标定义式与统计检验方法见正文",
    "同域比较 / 迁移测试 / 数据独立测试的定义边界见研究内容三"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic evaluation-protocol diagram on a pure white #FFFFFF canvas, showing how a retrieval improvement is attributed to relation modelling rather than to capacity, budget or data leakage.

Far left: a tall box with 1.5pt #1B3A5C border and an icon of stacked horizontal layers with a curved residual arrow, title "三臂检索模型", note "来自内容二". Solid 1.5pt #4D4D4D arrows fan right.

Centre: a wide panel on very light #F2F6FA tint holding five equal columns, all sharing the same 1.5pt #2E6B9E border so that they are distinguished by icon and header rather than by hue. Column 1, gauge-with-tick-marks icon, header "标准检索", body "RSITMD · RSICD 双向 / 原始划分与协议 / R@1 · R@5 · R@10 · mR". Column 2, icon of two dots joined by a directed line, header "关系挑战", body "人工核验子集 / 关系冲突误匹配率 / 关系判别准确率". Column 3, small stepped bar-chart icon, header "覆盖度稳健性", body "按描述覆盖程度分档 / 区分真实自然样本与人工扰动样本". Column 4, two-overlapping-circles Venn icon, header "迁移", body "同域比较 / 目标域未参训迁移 / 真正数据独立测试". Column 5, stopwatch-outline icon, header "效率", body "可训练参数量 / 训练开销 / 索引与查询耗时", with a 7pt grey line beneath "注明硬件、图库规模与批大小".

Sitting on the path into column 4, the only orange element in the upper half: a gate box with 1.5pt #D95F02 border, title "去重闸口", body "原图 + 近重复 + 同源切片联合去重", grey note "不以数据集名不同即认定独立". Beside column 2, a 1.0pt #8EAEC4 dashed note in 7pt #666666: "与标准结果分开报告；改动真值后不与原论文数字直接比较".

Full-width bottom bar on #F7F7F7 with 1.0pt #5BA0D0 border, split into three cells under the heading "可归因性控制": "等参数量与等训练步数对照", "近重复与同源切片去重", "三级测试分别定义分别报告".

Far right, two exits stacked. Upper, 1.5pt #009E73 solid border: "正向出口 — 性能变化可归因于关系建模本身". Lower, 1.5pt #8EAEC4 dashed border: "反向出口 — 等预算下改进消失 → 如实报告负结果；贡献收敛到评测协议与失效模式刻画".

Along the bottom, one 1.0pt dashed #4D4D4D curved arrow running right to left, labelled "错误归因回流 → 内容一 / 内容二", never crossing a forward arrow.

Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
各指标定义式与显著性检验方法见正文；同域比较、目标域未参与训练的迁移测试、真正数据独立的测试三者分别定义并分别报告。

---

## F8 三态判定的三类证据源与适用边界

**type** Module Detail ｜ **aspect** 4:3 ｜ **落点** 研究内容一（关键技术 1）｜ **优先级** strong

### JSON spec

```json
{
  "diagram_type": "Module Detail — evidence sources and admissibility boundaries for three-state adjudication",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "89mm (single column) or 183mm if placed full width",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "constraint_highlight": "2.5pt solid #D95F02", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "triple_card": "#1B3A5C 1.5pt solid border, white fill",
      "evidence_source": "#2E6B9E 1.5pt solid border, white fill",
      "constraint_box": "#D95F02 2.5pt solid border, white fill",
      "state_supported": "#009E73 1.5pt solid border, white fill",
      "state_conflict": "#D95F02 1.5pt solid border, white fill with 45-degree hatch",
      "state_unknown": "#8EAEC4 1.5pt dashed border, white fill with dot pattern"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Center",
      "shape": "Card, #1B3A5C 1.5pt border, white fill, internal 1.0pt dividers",
      "icon": "two dots joined by a directed line, monochrome",
      "exact_title_to_render_inside": "关系三元组记录",
      "exact_text": "〈实体A, 关系, 实体B〉",
      "internal_content": {
        "layout": "Four field rows",
        "exact_text": "证据来源\\n置信度\\n判定人\\n分辨率档"
      },
      "flow": "Arrow pointing DOWN to the three state boxes"
    },
    {
      "relative_position": "Left, feeding into center",
      "shape": "Box, #2E6B9E 1.5pt border, white fill, grey pill 训练端弱标注",
      "icon": "five thin stacked caption bars, monochrome",
      "exact_title_to_render_inside": "① 同图多描述交叉印证",
      "exact_text": "≥2 条独立提及且不矛盾 → 已支持候选\\n互斥关系 → 明确冲突候选\\n仅 1 条提及 → 不升级",
      "secondary_note": "不引入外部模型",
      "flow": "Arrow pointing RIGHT into 关系三元组记录"
    },
    {
      "relative_position": "Top, feeding into center",
      "shape": "Box, #2E6B9E 1.5pt border, white fill, grey pill 训练端弱标注",
      "icon": "bounding box with corner markers, monochrome",
      "exact_title_to_render_inside": "② 独立视觉证据",
      "exact_text": "开放词汇检测 / 分割仅提供实体位置与范围\\n关系由确定性几何规则判定",
      "secondary_note": "外接框重叠 · 质心相对位置 · 归一化距离",
      "flow": "Arrow pointing DOWN into 关系三元组记录"
    },
    {
      "relative_position": "Attached to block ②",
      "shape": "Box, #D95F02 2.5pt border, white fill",
      "exact_text": "外部模型只定位实体，关系不由模型直接输出；\\n与被评测模型不共享骨干与训练数据 → 避免循环论证"
    },
    {
      "relative_position": "Right, feeding into center",
      "shape": "Box, #2E6B9E 1.5pt border, white fill, green pill 评测端唯一合法来源",
      "icon": "two person outlines with a tick, monochrome",
      "exact_title_to_render_inside": "③ 人工核验",
      "exact_text": "双人独立标注 + 第三人仲裁\\n报告标注者间一致性",
      "secondary_note": "Cohen's κ ≥ 0.7【暂定】",
      "flow": "Arrow pointing LEFT into 关系三元组记录"
    },
    {
      "relative_position": "Bottom, three boxes side by side",
      "shape": "Three state boxes with the standard three-state encoding",
      "exact_text": "已支持\\n明确冲突\\n未知"
    },
    {
      "relative_position": "Bottom, attached under 未知",
      "shape": "Box, #8EAEC4 1.5pt dashed border, white fill with dot pattern",
      "exact_title_to_render_inside": "未知的三条判据",
      "exact_text": "实体无法可靠定位\\n关系在该地面采样距离下不可分辨\\n各证据源矛盾且无法仲裁",
      "exact_floating_text": "未知不是兜底类别"
    },
    {
      "relative_position": "Bottom Right corner",
      "shape": "Small box, #CCCCCC 1.0pt border, white fill",
      "icon": "small axes with an image frame, monochrome",
      "exact_title_to_render_inside": "坐标系约定",
      "exact_text": "左右上下基于影像坐标系\\n旋转翻转增强同步变换标签\\n不得解释为地理方位"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "The 2.5pt #D95F02 constraint box attached to evidence source ② is the single visual anchor of this figure.",
    "Admissibility pills must be visible on all three sources: two grey 训练端弱标注 pills and one green 评测端唯一合法来源 pill.",
    "Three states keep the global encoding: solid green / solid orange + hatch / dashed grey + dots.",
    "Keep 【暂定】 verbatim including brackets.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "几何规则的具体阈值按分辨率分档给出，见正文",
    "训练集允许证据源①②的弱标注，独立评测样本只接受来源③"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic module-detail diagram on a pure white #FFFFFF canvas, showing where the evidence for a spatial-relation triple may legitimately come from.

Centre: a record card with 1.5pt #1B3A5C border, white fill and thin 1.0pt internal dividers, icon of two dots joined by a directed line, title "关系三元组记录", headline "〈实体A, 关系, 实体B〉", and four field rows "证据来源", "置信度", "判定人", "分辨率档".

Three evidence sources feed the card from left, top and right, each a box with 1.5pt #2E6B9E border and an admissibility pill. Left, grey pill "训练端弱标注", icon of five thin stacked caption bars, title "① 同图多描述交叉印证", body "≥2 条独立提及且不矛盾 → 已支持候选 / 互斥关系 → 明确冲突候选 / 仅 1 条提及 → 不升级", 7pt grey note "不引入外部模型". Top, grey pill "训练端弱标注", icon of a bounding box with corner markers, title "② 独立视觉证据", body "开放词汇检测 / 分割仅提供实体位置与范围；关系由确定性几何规则判定", grey note "外接框重叠 · 质心相对位置 · 归一化距离". Right, green pill "评测端唯一合法来源", icon of two person outlines with a tick, title "③ 人工核验", body "双人独立标注 + 第三人仲裁；报告标注者间一致性", grey note "Cohen's κ ≥ 0.7【暂定】".

Attached to source ②, and forming the single visual anchor of the whole figure, a box with a heavy 2.5pt #D95F02 border reading "外部模型只定位实体，关系不由模型直接输出；与被评测模型不共享骨干与训练数据 → 避免循环论证".

Bottom: an arrow from the card leads down to three state boxes side by side using the global encoding — "已支持" 1.5pt #009E73 solid plain fill, "明确冲突" 1.5pt #D95F02 solid with fine 45-degree hatch, "未知" 1.5pt #8EAEC4 dashed with fine dot fill. Beneath "未知", a dashed dot-filled box titled "未知的三条判据" listing "实体无法可靠定位 / 关系在该地面采样距离下不可分辨 / 各证据源矛盾且无法仲裁", with a 7pt grey floating note "未知不是兜底类别". Bottom-right corner, a small 1.0pt #CCCCCC box with a small axes-and-image-frame icon: "坐标系约定 — 左右上下基于影像坐标系；旋转翻转增强同步变换标签；不得解释为地理方位".

Reproduce 【暂定】 verbatim including brackets. Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.
```

### Caption 保留内容
几何规则的具体阈值按分辨率分档给出；训练集允许证据源①②产生的弱标注，独立评测样本只接受来源③的人工核验标签。

---

## F9 与最相关工作的差异定位图

**type** Comparison ｜ **aspect** 3:2 ｜ **落点** 特色与创新 / 差异说明 ｜ **优先级** strong（已入选最终 7 张）

> 两轴命名为本规划提出的表述（推断），需申请人确认后再出图。
> 比例由 1:1 改为 3:2（决定见 `05_最终选图.md` 第三节）：两轴是序数类别而非等尺度度量轴，无需正方形画布；改后在 `0.72\linewidth` 下占页 37.1%，比 1:1 省约 0.5 页且节点更宽松。

### JSON spec

```json
{
  "diagram_type": "Two-axis positioning map against most related work",
  "diagram_title_rendering": "None",
  "aspect_ratio": "3:2",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column), rendered at 0.72 text width in the proposal",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"axis": "1.5pt solid #4D4D4D", "container_border": "1.0pt solid", "ours_highlight": "2.5pt solid", "gridline": "0.5pt dashed #CCCCCC"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "prior_generic": "#CCCCCC 1.0pt solid border, white fill, text #666666",
      "prior_relation": "#2E6B9E 1.0pt solid border, white fill",
      "prior_mismatch": "#2E6B9E 1.0pt solid border, white fill",
      "ours": "#009E73 2.5pt solid border, white fill, green pill 本项目",
      "side_note": "#8EAEC4 1.0pt dashed border, no fill"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "X axis, bottom",
      "shape": "Horizontal axis, 1.5pt #4D4D4D with arrowhead right",
      "exact_label": "关系语义的处理",
      "exact_text": "不建模　→　关系增强表示　→　关系证据状态判定"
    },
    {
      "relative_position": "Y axis, left",
      "shape": "Vertical axis, 1.5pt #4D4D4D with arrowhead up",
      "exact_label": "失配的处理",
      "exact_text": "不区分成因　→　按失配强度加权　→　区分成因并屏蔽不可判定"
    },
    {
      "relative_position": "Lower Left quadrant",
      "shape": "Small grey nodes, #CCCCCC 1.0pt border, text #666666",
      "exact_text": "对比预训练视觉语言模型\\n遥感领域适配模型"
    },
    {
      "relative_position": "Lower Center",
      "shape": "Small grey node, #CCCCCC 1.0pt border, text #666666",
      "exact_text": "全局—局部对齐 / 多尺度细粒度匹配"
    },
    {
      "relative_position": "Middle Column (x = 关系增强表示)",
      "shape": "Blue nodes, #2E6B9E 1.0pt border, white fill",
      "exact_text": "单模态实体关系特征学习\\n伪区域空间—通道注意力\\n方向导向视觉语义嵌入\\n外部知识增强检索\\n空间感知实体关系探索"
    },
    {
      "relative_position": "Upper Left (y = 按失配强度加权)",
      "shape": "Blue nodes, #2E6B9E 1.0pt border, white fill",
      "exact_text": "部分错配鲁棒学习\\n相似度一致性纠正\\n三分法噪声对应\\n遥感伪匹配对判别"
    },
    {
      "relative_position": "Upper Right corner",
      "shape": "Box, #009E73 2.5pt border, white fill, green pill 本项目",
      "icon": "two dots joined by a directed line with a small state tag, monochrome",
      "exact_title_to_render_inside": "本项目",
      "exact_text": "关系证据可判定状态\\n作为一等建模对象\\n未知态不参与监督"
    },
    {
      "relative_position": "Right margin, outside the axes",
      "shape": "#8EAEC4 1.0pt dashed border, no fill",
      "exact_title_to_render_inside": "不在本图两轴上",
      "exact_text": "不确定性 / 证据建模工作\\n建模对象是相似度或表示的不确定性\\n技术手段可借用，问题定义不同"
    },
    {
      "relative_position": "Bottom Strip",
      "shape": "No border, 7pt #666666",
      "exact_text": "不主张首次引入空间关系，也不主张首次处理不完备图文对应"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Prior work nodes must be small, unlabelled by citation number, and visually quieter than the ours node.",
    "Exactly one element carries the 2.5pt bold highlight: 本项目, positioned in the upper right.",
    "Gridlines are 0.5pt dashed light grey; do not fill quadrants with background color.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "各节点对应文献编号见正文 1.10 与最相关工作的差异说明",
    "两轴命名为图示表述，正文以文字形式给出差异"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic two-axis positioning map on a pure white #FFFFFF canvas, placing this project against the most closely related lines of work.

A horizontal axis along the bottom, 1.5pt #4D4D4D with an arrowhead pointing right, labelled "关系语义的处理" with three tick labels "不建模", "关系增强表示", "关系证据状态判定". A vertical axis on the left, same weight with an arrowhead pointing up, labelled "失配的处理" with three tick labels "不区分成因", "按失配强度加权", "区分成因并屏蔽不可判定". Faint 0.5pt dashed #CCCCCC gridlines divide the plane; quadrants are left unfilled.

Prior-work nodes are small rounded boxes and are deliberately quiet, carrying no citation numbers. In the lower-left region, two grey nodes with 1.0pt #CCCCCC borders and #666666 text: "对比预训练视觉语言模型" and "遥感领域适配模型". Lower centre, one more grey node: "全局—局部对齐 / 多尺度细粒度匹配". In the middle column, five nodes with 1.0pt #2E6B9E borders: "单模态实体关系特征学习", "伪区域空间—通道注意力", "方向导向视觉语义嵌入", "外部知识增强检索", "空间感知实体关系探索". In the upper-left region, four nodes with 1.0pt #2E6B9E borders: "部分错配鲁棒学习", "相似度一致性纠正", "三分法噪声对应", "遥感伪匹配对判别".

In the upper-right corner, the single bold element of the figure: a box with a 2.5pt #009E73 border, a small green pill "本项目", a monochrome icon of two dots joined by a directed line carrying a small state tag, title "本项目" and body "关系证据可判定状态作为一等建模对象；未知态不参与监督".

Outside the plotting area, in the right margin, a 1.0pt #8EAEC4 dashed frame with no fill, titled "不在本图两轴上", body "不确定性 / 证据建模工作：建模对象是相似度或表示的不确定性；技术手段可借用，问题定义不同".

Bottom strip, borderless 7pt #666666 text: "不主张首次引入空间关系，也不主张首次处理不完备图文对应".

Chinese sans-serif, titles 10pt bold, node labels 8pt, notes 7pt grey. White fills, colored borders only, 4px radius on nodes. No gradients, no shadows, no 3D, no emojis. Aspect ratio 3:2.
```

### Caption 保留内容
各节点对应文献编号见正文 1.10；两轴命名为图示表述，正文以文字形式给出逐项差异。

---

## F10 年度研究计划与里程碑

**type** Timeline / Gantt ｜ **aspect** 16:9 ｜ **落点** 年度研究计划 ｜ **优先级** strong

### JSON spec

```json
{
  "diagram_type": "Four-year Gantt timeline with a decision node",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "task_bar": "1.0pt solid", "decision_node": "1.5pt solid diamond", "gridline": "0.5pt dashed #CCCCCC"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "task_primary": "#2E6B9E 1.0pt solid border, white fill",
      "task_secondary": "#5BA0D0 1.0pt solid border, white fill",
      "decision_node": "#D95F02 1.5pt solid border, diamond, white fill",
      "milestone": "#2E6B9E filled small diamond",
      "branch_pass": "#009E73 1.5pt solid arrow",
      "branch_fail": "#D95F02 1.5pt dashed arrow",
      "lane_bg_odd": "#F7F7F7", "lane_bg_even": "#FFFFFF"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top axis",
      "shape": "Horizontal time axis divided into four equal segments by 0.5pt dashed gridlines",
      "exact_text": "2027　│　2028　│　2029　│　2030"
    },
    {
      "relative_position": "Lane 1",
      "shape": "Swimlane on #F7F7F7 tint, row header box #1B3A5C 1.5pt border",
      "exact_title_to_render_inside": "内容一",
      "exact_text": "数据获取与许可确认 · 去重与固定划分 · 分层抽样审计【暂定 200–400 组】\\n关系挑战子集标注与一致性仲裁【暂定 1500–2500 组】\\n规范 v2 回流修订"
    },
    {
      "relative_position": "Lane 2",
      "shape": "Swimlane on white, row header box #1B3A5C 1.5pt border",
      "exact_title_to_render_inside": "内容二",
      "exact_text": "基线复现 · 最小实验选主线\\n主线方法实现 · 三臂对照 · 屏蔽比例消融\\n方法完善"
    },
    {
      "relative_position": "Lane 3",
      "shape": "Swimlane on #F7F7F7 tint, row header box #1B3A5C 1.5pt border",
      "exact_title_to_render_inside": "内容三",
      "exact_text": "错误归因（H1 检验）\\n标准检索主实验\\n等预算对照（H3）· 去重后迁移 · 覆盖度分档 · 效率评测\\n评测协议定稿"
    },
    {
      "relative_position": "Lane 4",
      "shape": "Swimlane on white, row header box #1B3A5C 1.5pt border",
      "exact_title_to_render_inside": "论文与开放材料",
      "exact_text": "投出第 1 篇论文【暂定】\\n投出第 2 篇论文【暂定】\\n复现材料整理 · 轻量检索演示 · 许可范围内派生标注与索引发布 · 结题"
    },
    {
      "relative_position": "End of year 1, spanning lanes",
      "shape": "Diamond, #D95F02 1.5pt border, white fill",
      "exact_title_to_render_inside": "H1 检验",
      "exact_text": "描述不完备是否为重要误差来源",
      "branch_yes": "Solid #009E73 arrow labelled 成立 → 按原定推进",
      "branch_no": "Dashed #D95F02 arrow labelled 证伪 → 调整内容一定位乃至题目"
    },
    {
      "relative_position": "Milestone markers on lane ends",
      "shape": "Small filled #2E6B9E diamonds with 7pt labels",
      "exact_text": "关系规范 v1\\n三臂对照结果\\nH2 / H3 检验结论\\n协议定稿与结题"
    },
    {
      "relative_position": "Bottom Strip",
      "shape": "No border, 7pt #666666",
      "exact_text": "【暂定】月份划分与工作量分配为计划安排，将根据实际进展调整"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "The H1 decision diamond at the end of year 1 is the only strongly emphasised element and must have two visibly different out-edges: a solid green pass edge and a dashed orange falsified edge.",
    "Task bars share one blue family; do not assign a different hue per lane.",
    "Keep every 【暂定 …】 string verbatim including brackets.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "阶段目标与交付物清单见正文年度研究计划各年条目",
    "执行期 2027.01—2030.12，共 4 年"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic Gantt timeline on a pure white #FFFFFF canvas, covering a four-year research plan with one explicit decision node.

Top: a horizontal time axis divided into four equal segments by 0.5pt dashed #CCCCCC gridlines, labelled "2027", "2028", "2029", "2030".

Four horizontal swimlanes below, alternating #F7F7F7 tint and white backgrounds. Each lane opens with a row header box, 1.5pt #1B3A5C border: "内容一", "内容二", "内容三", "论文与开放材料". Task bars inside the lanes are rounded rectangles with 1.0pt borders in a single blue family — #2E6B9E for primary tasks, #5BA0D0 for secondary — never a different hue per lane, with 8pt labels placed inside or immediately above each bar.

Lane 内容一 bars: "数据获取与许可确认", "去重与固定划分", "分层抽样审计【暂定 200–400 组】" in year 1; "关系挑战子集标注与一致性仲裁【暂定 1500–2500 组】" spanning year 2; "规范 v2 回流修订" in year 3. Lane 内容二: "基线复现" and "最小实验选主线" in year 1; "主线方法实现", "三臂对照", "屏蔽比例消融" in year 2; "方法完善" in year 3. Lane 内容三: "错误归因（H1 检验）" in year 1; "标准检索主实验" in year 2; "等预算对照（H3）", "去重后迁移", "覆盖度分档", "效率评测" in year 3; "评测协议定稿" in year 4. Lane 论文与开放材料: "投出第 1 篇论文【暂定】" in year 2; "投出第 2 篇论文【暂定】" in year 3; "复现材料整理", "轻量检索演示", "许可范围内派生标注与索引发布", "结题" in year 4.

At the end of year 1, spanning the lanes, the single strongly emphasised element: a diamond with a 1.5pt #D95F02 border and white fill, label "H1 检验", sub-line "描述不完备是否为重要误差来源", with two visibly different out-edges — a solid #009E73 arrow labelled "成立 → 按原定推进" and a dashed #D95F02 arrow labelled "证伪 → 调整内容一定位乃至题目".

Small filled #2E6B9E diamond milestone markers sit at lane ends with 7pt labels: "关系规范 v1", "三臂对照结果", "H2 / H3 检验结论", "协议定稿与结题".

Bottom strip, borderless 7pt #666666: "【暂定】月份划分与工作量分配为计划安排，将根据实际进展调整".

Reproduce every 【暂定 …】 string verbatim including brackets. Chinese sans-serif, headers 10pt bold, bar labels 8pt, notes 7pt grey. White fills, colored borders only, 4px radius on bars. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
各年度阶段目标与交付物清单见正文年度研究计划；执行期 2027.01—2030.12，共 4 年。

---

## F11 假说—证伪判据—降级路径图

**type** Decision Flow ｜ **aspect** 16:9 ｜ **落点** 研究风险与应对措施 ｜ **优先级** strong

### JSON spec

```json
{
  "diagram_type": "Decision flow — hypotheses, falsification criteria and fallback paths",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "ours_highlight": "2.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "hypothesis": "#1B3A5C 1.5pt solid border, white fill",
      "checkpoint": "#2E6B9E 1.5pt solid border, white fill",
      "falsification": "#D95F02 1.5pt solid border, white fill",
      "fallback": "#8EAEC4 1.5pt dashed border, white fill",
      "principle": "#009E73 2.5pt solid border, white fill",
      "side_risk": "#5BA0D0 1.0pt solid border, white fill",
      "row_bg_odd": "#F7F7F7"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Column headers",
      "shape": "No border, 8pt bold",
      "exact_text": "假说　→　检验时点　→　证伪判据　→　降级路径"
    },
    {
      "relative_position": "Row 1",
      "shape": "Four boxes left to right on #F7F7F7 tint",
      "exact_text": "H1 现象存在性\\n第一年错误归因\\n该类错误占比 <【暂定 10%】，或无法与细粒度语义不足、同类场景近似稳定区分\\n收敛为「关系冲突识别」单一目标，或转向覆盖度稳健性；调整内容一定位乃至题目"
    },
    {
      "relative_position": "Row 2",
      "shape": "Four boxes left to right on white",
      "exact_text": "H2 机制判断\\n第二至三年三臂对照\\n三态相对二值无可复现差异，或标准 mR 显著下降\\n贡献收敛到评测协议与失效模式刻画"
    },
    {
      "relative_position": "Row 3",
      "shape": "Four boxes left to right on #F7F7F7 tint",
      "exact_text": "H3 可归因性\\n第三年等预算对照\\n改进可由骨干容量或训练预算解释\\n如实报告负结果"
    },
    {
      "relative_position": "Left Vertical Strip",
      "shape": "Tall box, #5BA0D0 1.0pt border, white fill, four internal rows",
      "exact_title_to_render_inside": "其它风险与早期信号",
      "exact_text": "查新结论变化：最相关工作全文未取得 → 申报前取得并逐项对照\\n标注一致性不足：第二年 κ 值 → 收缩词表至高一致性子集\\n数据许可限制：第一年确认 → 交付索引与构建脚本\\n自动抽取三元组噪声：第一年审计 → 训练端降权，评测端全人工核验"
    },
    {
      "relative_position": "Far Right, spanning all three rows",
      "shape": "Tall box, #009E73 2.5pt border, white fill",
      "icon": "a balance scale outline, monochrome",
      "exact_title_to_render_inside": "统一原则",
      "exact_text": "不通过改动评测口径或抽样方式\\n维持既定结论"
    },
    {
      "relative_position": "Bottom Strip",
      "shape": "No border, 7pt #666666",
      "exact_text": "H1—H3 任一被证伪，均如实报告并调整定位；可被否定正是其作为科学问题的标志"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Three rows are structurally identical; they are distinguished by row position and alternating tint, not by different hues.",
    "Fallback boxes use dashed grey borders to read as contingency rather than as plan.",
    "Exactly one element carries the 2.5pt bold highlight: 统一原则.",
    "Keep 【暂定 10%】 verbatim including brackets.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "各风险的完整应对文字见正文研究风险与应对措施",
    "H1 检验前置到第一年，正是为了使调整成本可控"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic decision-flow diagram on a pure white #FFFFFF canvas, laying out three falsifiable hypotheses together with their falsification criteria and fallback paths.

A four-column grid occupying the centre and right of the canvas, with borderless 8pt bold column headers reading "假说", "检验时点", "证伪判据", "降级路径", separated by short solid #4D4D4D arrows.

Three structurally identical rows, distinguished only by position and by alternating #F7F7F7 and white row tints, never by different hues. Row 1: hypothesis box with 1.5pt #1B3A5C border "H1 现象存在性"; checkpoint box with 1.5pt #2E6B9E border "第一年错误归因"; falsification box with 1.5pt #D95F02 border "该类错误占比 <【暂定 10%】，或无法与细粒度语义不足、同类场景近似稳定区分"; fallback box with 1.5pt #8EAEC4 dashed border "收敛为「关系冲突识别」单一目标，或转向覆盖度稳健性；调整内容一定位乃至题目". Row 2: "H2 机制判断"; "第二至三年三臂对照"; "三态相对二值无可复现差异，或标准 mR 显著下降"; "贡献收敛到评测协议与失效模式刻画". Row 3: "H3 可归因性"; "第三年等预算对照"; "改进可由骨干容量或训练预算解释"; "如实报告负结果".

Left vertical strip: a tall box with 1.0pt #5BA0D0 border titled "其它风险与早期信号", four internal rows separated by 1.0pt dividers: "查新结论变化：最相关工作全文未取得 → 申报前取得并逐项对照", "标注一致性不足：第二年 κ 值 → 收缩词表至高一致性子集", "数据许可限制：第一年确认 → 交付索引与构建脚本", "自动抽取三元组噪声：第一年审计 → 训练端降权，评测端全人工核验".

Far right, spanning all three rows and the only bold element in the figure: a tall box with a 2.5pt #009E73 border, a monochrome balance-scale outline icon, title "统一原则", body "不通过改动评测口径或抽样方式维持既定结论".

Bottom strip, borderless 7pt #666666 text: "H1—H3 任一被证伪，均如实报告并调整定位；可被否定正是其作为科学问题的标志".

Reproduce 【暂定 10%】 verbatim including brackets. Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. Dashed borders on fallback boxes so they read as contingency rather than plan. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
各风险的完整应对文字见正文研究风险与应对措施；H1 检验前置到第一年，正是为了使调整成本可控。

---

## F12 申请人积累与项目需求对位图

**type** Mapping ｜ **aspect** 4:3 ｜ **落点** 研究基础与可行性分析 ｜ **优先级** nice

> 可选处理：若担心评审观感，可只保留左右对位 + 算力条，把底部边界条留在正文（正文已如实写明，不构成隐瞒）。

### JSON spec

```json
{
  "diagram_type": "Capability-to-requirement mapping",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "89mm (single column) or 183mm if placed full width",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "mapping_line": "1.5pt solid", "boundary_border": "1.0pt dashed"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "accumulation": "#2E6B9E 1.5pt solid border, white fill",
      "requirement": "#5BA0D0 1.5pt solid border, white fill",
      "compute": "#CCCCCC 1.0pt solid border, #F7F7F7 fill",
      "boundary": "#8EAEC4 1.0pt dashed border, no fill, text #666666"
    },
    "flow_arrow_colors": {"mapping": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left Column, three stacked boxes",
      "shape": "Three boxes, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "已有研究积累",
      "internal_content": {
        "box_1": {"exact_header": "跨模态检索的表征与匹配", "icon": "two rows of dots with crossing lines", "exact_text": "特征融合与解耦的跨模态哈希检索\\n双分支特征融合多语义对齐哈希"},
        "box_2": {"exact_header": "遥感语义与空间结构理解", "icon": "three stacked image frames with a diagonal cross", "exact_text": "渐进式视觉校准与结构化状态空间推理\\n知识迁移与深度空间建模"},
        "box_3": {"exact_header": "多模态表征与空间关系", "icon": "two dots joined by a directed line", "exact_text": "多层次视觉表征增强的知识感知图像理解\\n空间位置关系协同注意力"}
      }
    },
    {
      "relative_position": "Right Column, three stacked boxes",
      "shape": "Three boxes, #5BA0D0 1.5pt border, white fill",
      "exact_title_to_render_inside": "项目所需能力",
      "internal_content": {
        "box_1": {"exact_header": "内容一所需", "exact_text": "判断关系在遥感影像上是否可辨认"},
        "box_2": {"exact_header": "内容二所需", "exact_text": "关系证据如何进入对齐或重排序目标"},
        "box_3": {"exact_header": "内容三所需", "exact_text": "分层评测、等预算对照与消融组织"}
      }
    },
    {
      "relative_position": "Between the two columns",
      "shape": "Crossing mapping lines, 1.5pt solid #4D4D4D",
      "exact_floating_text": "遥感理解 → 内容一\\n跨模态检索 → 内容二\\n空间关系建模 → 内容一 + 内容二"
    },
    {
      "relative_position": "Bottom Bar",
      "shape": "Bar, #CCCCCC 1.0pt border, #F7F7F7 fill",
      "icon": "small server rack outline, monochrome",
      "exact_title_to_render_inside": "计算条件",
      "exact_text": "NVIDIA A40 × 8　·　RTX 3090 Ti × 6",
      "secondary_note": "已确认可稳定使用"
    },
    {
      "relative_position": "Bottom Strip, below the compute bar",
      "shape": "#8EAEC4 1.0pt dashed border, no fill, text #666666",
      "exact_title_to_render_inside": "前期基础边界",
      "exact_text": "尚无可直接复用的项目级数据、代码、模型配置、评价脚本或消融日志\\n公开数据集仅完成获取入口核验，尚未下载与逐样本验证"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "This figure carries NO accent highlight; keep it in the blue family only.",
    "Mapping lines must visibly cross, showing that accumulation two feeds requirement one.",
    "Do not print journal names, impact factors, author order or publication years on the figure.",
    "The boundary note uses dashed grey border and #666666 text and must not be visually emphasised.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "代表性成果的期刊、年份与作者贡献见正文研究基础",
    "连线映射为归纳结果，非正文原句"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic mapping diagram on a pure white #FFFFFF canvas, connecting three existing lines of the applicant's work to the three capability requirements of the proposed project. Restrained, single blue family, no accent color anywhere.

Left column, heading "已有研究积累", three stacked boxes with 1.5pt #2E6B9E borders and white fill. Box 1: icon of two rows of dots with crossing lines, header "跨模态检索的表征与匹配", body "特征融合与解耦的跨模态哈希检索 / 双分支特征融合多语义对齐哈希". Box 2: icon of three stacked image frames with a diagonal cross, header "遥感语义与空间结构理解", body "渐进式视觉校准与结构化状态空间推理 / 知识迁移与深度空间建模". Box 3: icon of two dots joined by a directed line, header "多模态表征与空间关系", body "多层次视觉表征增强的知识感知图像理解 / 空间位置关系协同注意力".

Right column, heading "项目所需能力", three stacked boxes with 1.5pt #5BA0D0 borders. Box 1: header "内容一所需", body "判断关系在遥感影像上是否可辨认". Box 2: header "内容二所需", body "关系证据如何进入对齐或重排序目标". Box 3: header "内容三所需", body "分层评测、等预算对照与消融组织".

Between the columns, 1.5pt solid #4D4D4D mapping lines that visibly cross: accumulation box 2 connects to requirement box 1, accumulation box 1 connects to requirement box 2, and accumulation box 3 forks to both requirement box 1 and requirement box 2. Small 7pt grey labels ride the lines: "遥感理解 → 内容一", "跨模态检索 → 内容二", "空间关系建模 → 内容一 + 内容二".

Bottom bar on #F7F7F7 with 1.0pt #CCCCCC border and a small monochrome server-rack outline icon: title "计算条件", body "NVIDIA A40 × 8　·　RTX 3090 Ti × 6", grey note "已确认可稳定使用".

Beneath it, a quiet 1.0pt #8EAEC4 dashed frame with no fill and #666666 text, deliberately not emphasised: title "前期基础边界", body "尚无可直接复用的项目级数据、代码、模型配置、评价脚本或消融日志；公开数据集仅完成获取入口核验，尚未下载与逐样本验证".

Do not print journal names, impact factors, author order or publication years anywhere on the figure. Chinese sans-serif, headings 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.
```

### Caption 保留内容
代表性成果的期刊、年份与作者贡献见正文研究基础；连线映射为归纳结果，非正文原句。

---

## 全局检查清单（12 张图出图后逐项核对）

- [ ] 每个可见字符串都来自 `exact_*` 字段，没有模型自行添加的文字
- [ ] `aspect_ratio` 与 Figure Plan 一致
- [ ] `【暂定 …】` 标记原样保留，与正文措辞一致
- [ ] 文字预算：模块标题 ≤5 字、子项 ≤3 字、箭头标签 ≤3 字
- [ ] 白底 + 彩色边框，无彩色填充（斜纹/点阵除外，且为浅灰调）
- [ ] 每张图彩色数 ≤3（见 `02_Palette_Decision.md` 第六节逐图分配）
- [ ] 每张图至多一个 2.5pt 加粗强调元素
- [ ] 每个二级模块都有单色线稿图标，无空壳
- [ ] 冻结/可训练用虚线框 + `[Fixed]` / 实线框 + `[Tune]`，无雪花/火焰图标
- [ ] 三态在灰度下仍可区分（实线 / 实线+斜纹 / 虚线+点阵）
- [ ] 屏蔽监督箭头虚线且中段有断开斜杠
- [ ] 反馈虚线弧不与任何前向箭头交叉
- [ ] 无 emoji、无锁头/火焰/闪电、无 3D、无渐变、无阴影
- [ ] 长公式、参数、文献编号已移入 caption
- [ ] 图上无期刊名、影响因子、作者排序（F12）
