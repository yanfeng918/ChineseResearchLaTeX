---
document: "出图规范与 Prompt（F1—F6）"
stage: "05_figure_plan"
project: "NSFC_2027_Mapping"
skill: "academic-figure-prompt v1.5.0"
input: "01_Figure_Plan.md + 02_Palette_Decision.md"
version: "2026-09-06"
---

# Figure Prompts F01—F06

配套：`04_Figure_Prompts_F07-F12.md`（F7—F12）。

## 使用前必读

### 一、CJK 渲染对策

图上文字为中文（申请书最终语种）。当前图像模型渲染汉字仍不稳定，按以下顺序处理：

| 方案 | 做法 | 适用 |
|---|---|---|
| A（推荐） | 直接用本文件的中文 `exact_*` 出图，逐张核对错字，错字处局部重绘或用矢量工具修字 | 文字量少的 F2 F8 F9 |
| B | 把 `exact_*` 换成同义英文短标签出图拿版式，再在 draw.io / Illustrator / PPT 里把英文替换回中文 | 文字量大的 F4 F5 F6 F7 F10 F11 |
| C | 只用 prompt 拿构图草案，最终图在 draw.io 手绘 | 对版式精度要求最高时 |

无论走哪条路：**`【暂定 …】` 标记必须原样出现在最终图上**，与正文措辞一致。

### 二、共用样式（12 张图统一，不在每条 prompt 里重复解释）

```
canvas        : 纯白 #FFFFFF，双栏宽 183mm（F2 F8 F9 F12 可用单栏 89mm）
fills         : 一律白色填充，颜色只上边框
borders       : 容器 1.5pt，分隔 1.0pt，本项目主张 2.5pt，圆角 6px
arrows        : 前向 1.5pt 实线 #4D4D4D（4px 箭头）；反馈 1.0pt 虚线弧形
fonts         : 中文无衬线（思源黑体 / Noto Sans SC）；标题 10pt bold，标签 8pt，注 7pt #666666
icons         : 单色线稿，取所在模块边框色，16–24px 等效
three-state   : 已支持 #009E73 实线无纹理｜明确冲突 #D95F02 实线+45°斜纹｜未知 #8EAEC4 虚线+点阵
negative      : 无 emoji，无锁头/火焰/闪电，无 3D，无渐变，无阴影，无彩色填充图标
```

---

## F1 研究背景与问题提出图

**type** Conceptual Background ｜ **aspect** 16:9 ｜ **落点** 立项依据 1.1 ｜ **优先级** must

### JSON spec

```json
{
  "diagram_type": "Conceptual Background Diagram (problem motivation)",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC / Source Han Sans, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "stage_data": "#2E6B9E solid border, white fill",
      "stage_query": "#2E6B9E solid border, white fill",
      "stage_assumption": "#5BA0D0 solid border, white fill",
      "stage_breakdown": "#2E6B9E solid border on #F7F7F7 tinted panel",
      "outcome": "#D95F02 solid border, white fill",
      "boundary_note": "#8EAEC4 1.0pt dashed border, text #666666"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "icon": "three stacked image frames with a diagonal cross, monochrome line art",
      "exact_title_to_render_inside": "对地观测影像库",
      "exact_text": "规模增长 > 人工判读",
      "flow": "Horizontal arrow pointing RIGHT to 自然语言检索入口"
    },
    {
      "relative_position": "Left Center",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "icon": "magnifying glass over a single text line, monochrome line art",
      "exact_title_to_render_inside": "自然语言检索入口",
      "exact_text": "「河流两侧分布着成排厂房」",
      "secondary_note": "不需波段参数",
      "flow": "Horizontal arrow pointing RIGHT to 隐含前提"
    },
    {
      "relative_position": "Center",
      "shape": "Rounded rectangle, #5BA0D0 1.5pt border, white fill",
      "icon": "question mark glyph inside a thin circle, monochrome line art",
      "exact_title_to_render_inside": "隐含前提",
      "exact_text": "文本描述能充分刻画影像内容",
      "exact_floating_text": "主流方法默认",
      "flow": "Horizontal arrow pointing RIGHT to 前提不成立"
    },
    {
      "relative_position": "Right Center",
      "shape": "Wide panel, #F7F7F7 tinted fill, #2E6B9E 1.5pt border",
      "exact_title_to_render_inside": "前提不成立",
      "internal_content": {
        "layout": "Left half: simplified top-down land-cover sketch; Right half: five caption bars",
        "left": {"exact_label": "一景影像", "detail": "flat outlined shapes: river band, road line, row of factory blocks, farmland patch, aquaculture pond"},
        "right": {"exact_text": "描述1\\n描述2\\n描述3\\n描述4\\n描述5", "detail": "each thin bar carries 2-3 small dots at differing positions", "exact_floating_text": "覆盖差异"}
      },
      "flow": "Horizontal arrow pointing RIGHT to 后果"
    },
    {
      "relative_position": "Far Right",
      "shape": "Rounded rectangle, #D95F02 1.5pt border, white fill",
      "icon": "two diverging arrows splitting from one origin, monochrome line art",
      "exact_title_to_render_inside": "后果",
      "exact_text": "「没说」被当成「没有」\\n中立样本被当作负例惩罚"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Small box, #CCCCCC 1.0pt border, white fill",
      "exact_text": "自然资源调查：耕地与养殖水面相邻"
    },
    {
      "relative_position": "Bottom Center",
      "shape": "Small box, #CCCCCC 1.0pt border, white fill",
      "exact_text": "灾害应急：道路被滑坡截断、下游有居民点"
    },
    {
      "relative_position": "Bottom Strip (below the two业务 boxes)",
      "shape": "#8EAEC4 1.0pt dashed border, no fill",
      "exact_text": "问题动机，非本项目验证范围；验证止于公开学术基准",
      "secondary_note": "7pt #666666"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "The land-cover sketch is flat outlined vector shapes, NOT a photograph or satellite image.",
    "Adhere to typography hierarchy: titles 10pt bold, labels 8pt, notes 7pt grey.",
    "Icons are monochrome thin line art in the block border color.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering, NO gradients, NO shadows.",
    "Canvas is pure white (#FFFFFF)."
  ],
  "caption_note": [
    "业务场景引用自立项依据 1.1，仅用于说明问题价值",
    "RSICD / RSITMD 每幅影像配 5 条描述的构建方式见正文引用 [6][7]"
  ]
}
```

### Image prompt (EN, for GPT-Image-2 / NanoBanana)

```
Flat vector academic conceptual background diagram on a pure white #FFFFFF canvas, explaining why natural-language retrieval of remote sensing imagery rests on an assumption that does not hold.

Horizontal left-to-right progression of four stages linked by solid dark grey #4D4D4D arrows, 1.5pt with 4px heads. Stage 1: rounded rectangle, 1.5pt #2E6B9E border, white fill, icon of three stacked image frames with a diagonal cross, bold title "对地观测影像库", sub-line "规模增长 > 人工判读". Stage 2: same style, magnifying-glass-over-a-text-line icon, title "自然语言检索入口", quoted line "「河流两侧分布着成排厂房」", small grey note "不需波段参数". Stage 3: rounded rectangle with 1.5pt #5BA0D0 border and a thin circled question-mark glyph, title "隐含前提", body "文本描述能充分刻画影像内容", small grey floating tag "主流方法默认". Stage 4 is wider: a panel with #F7F7F7 tinted fill and 1.5pt #2E6B9E border titled "前提不成立"; its left half holds a simplified top-down land-cover sketch drawn as flat outlined shapes only — a river band, a road line, a row of factory blocks, a farmland patch, an aquaculture pond — and its right half holds five thin horizontal bars labelled "描述1" through "描述5", each bar carrying two or three small dots at different positions, with a bracket labelled "覆盖差异".

Far right: an outcome box with 1.5pt #D95F02 border, white fill, an icon of two arrows diverging from one origin, title "后果", text "「没说」被当成「没有」" and second line "中立样本被当作负例惩罚".

Bottom strip: two small white boxes with 1.0pt #CCCCCC borders reading "自然资源调查：耕地与养殖水面相邻" and "灾害应急：道路被滑坡截断、下游有居民点"; beneath them a 1.0pt #8EAEC4 dashed borderless-fill note in 7pt #666666 reading "问题动机，非本项目验证范围；验证止于公开学术基准".

Chinese sans-serif throughout (Noto Sans SC), titles 10pt bold, labels 8pt, notes 7pt grey. White fills with colored borders only, 6px corner radius. The land-cover sketch must be flat vector outlines, never a photograph. No gradients, no shadows, no 3D, no emojis, no lock or fire icons. Aspect ratio 16:9.
```

### Caption 保留内容
业务场景引用自立项依据 1.1，仅用于说明问题价值，不代表本项目验证范围；公开基准每幅影像配 5 条互补描述的构建方式见正文 [6][7]。

---

## F2 描述不完备导致的三态歧义示意图

**type** Problem Illustration / Module Detail ｜ **aspect** 4:3 ｜ **落点** 立项依据 1.3 或内容一开篇 ｜ **优先级** must

> 全篇三态首次亮相，图例必须完整。这张图若只能保留一张，就保它。

### JSON spec

```json
{
  "diagram_type": "Problem Illustration — three-state evidence ambiguity",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "89mm (single column) or 183mm if placed full width",
    "font_family": "Noto Sans SC / Source Han Sans, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "ours_highlight": "2.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid", "masked_arrow": "1.5pt dashed with a short slash across mid-segment"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "image_panel": "#2E6B9E 1.5pt solid border, white fill",
      "caption_bars": "#5BA0D0 1.0pt solid border, white fill",
      "state_supported": "#009E73 1.5pt solid border, white fill, no hatch",
      "state_conflict": "#D95F02 1.5pt solid border, white fill with 45-degree fine hatch",
      "state_unknown": "#8EAEC4 1.5pt dashed border, white fill with fine dot pattern",
      "ours_panel": "#009E73 2.5pt solid border"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid", "masked": "#8EAEC4 dashed, slashed"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left Column",
      "shape": "Five stacked thin bars, #5BA0D0 1.0pt border, white fill",
      "exact_title_to_render_inside": "同图五条描述",
      "exact_text": "D1\\nD2\\nD3\\nD4\\nD5",
      "secondary_note": "覆盖不同地物",
      "flow": "Short arrows pointing RIGHT into the central image panel"
    },
    {
      "relative_position": "Center",
      "shape": "Square panel, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "一景遥感影像",
      "internal_content": {
        "layout": "Flat top-down outlined sketch",
        "elements": "河流 band, 道路 line, 厂房 block row, 耕地 patch, 养殖水面 pond; each labelled with 7pt grey text"
      },
      "flow": "Three arrows fanning RIGHT to the three state boxes"
    },
    {
      "relative_position": "Right Top",
      "shape": "Rounded rectangle, #009E73 1.5pt solid border, white fill",
      "icon": "two dots joined by a directed line, monochrome",
      "exact_title_to_render_inside": "已支持",
      "exact_text": "≥2 条描述独立提及且不矛盾",
      "exact_floating_text": "厂房—沿—河流"
    },
    {
      "relative_position": "Right Middle",
      "shape": "Rounded rectangle, #D95F02 1.5pt solid border, white fill with 45-degree hatch",
      "icon": "two opposing arrows, monochrome",
      "exact_title_to_render_inside": "明确冲突",
      "exact_text": "不同描述给出互斥关系",
      "exact_floating_text": "建筑—在道路左侧 / 右侧"
    },
    {
      "relative_position": "Right Bottom",
      "shape": "Rounded rectangle, #8EAEC4 1.5pt dashed border, white fill with dot pattern",
      "icon": "question mark in a thin square, monochrome",
      "exact_title_to_render_inside": "未知",
      "exact_text": "不可定位 / 不可分辨 / 矛盾无法仲裁",
      "exact_floating_text": "耕地—邻接—养殖水面？"
    },
    {
      "relative_position": "Bottom Left Half",
      "shape": "Panel, #CCCCCC 1.0pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "二值处理（现行）",
      "exact_text": "未提及 → 负例惩罚",
      "flow": "Solid #D95F02 arrow pointing RIGHT into a small box labelled 损失"
    },
    {
      "relative_position": "Bottom Right Half",
      "shape": "Panel, #009E73 2.5pt border, white fill",
      "exact_title_to_render_inside": "三态处理",
      "exact_text": "未知 → 屏蔽监督",
      "exact_floating_text": "本项目",
      "flow": "Dashed #8EAEC4 arrow with a short slash across its mid-segment, pointing RIGHT into a small box labelled 损失"
    },
    {
      "relative_position": "Bottom Strip",
      "shape": "Legend row, no border",
      "exact_text": "已支持=绿实线　明确冲突=橙实线斜纹　未知=灰虚线点阵"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields.",
    "Each of the three states must be distinguishable in GREYSCALE: solid / solid+hatch / dashed+dots.",
    "The masked supervision arrow must be dashed AND visibly interrupted by a short slash in its middle segment.",
    "The remote sensing scene is a flat outlined vector sketch, NOT a photograph.",
    "All boxes use WHITE fill with COLORED BORDERS ONLY; hatch and dot patterns are thin grey-tinted, not solid fills.",
    "Exactly one element carries the 2.5pt bold highlight: the 三态处理 panel.",
    "NO emojis, NO checkmark/cross emoji, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "三态判定的证据来源与适用边界见 F8",
    "屏蔽监督的具体损失构造形式见正文研究内容二"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic problem-illustration diagram on a pure white #FFFFFF canvas, showing why a remote sensing image-text pair can be non-matching for two entirely different reasons.

Three-zone composition. Left column: five thin stacked bars with 1.0pt #5BA0D0 borders labelled "D1" to "D5" under a heading "同图五条描述" and a 7pt grey note "覆盖不同地物"; each bar carries two or three small dots at differing positions, and short solid arrows point right into the centre. Centre: a square panel with 1.5pt #2E6B9E border titled "一景遥感影像", containing a simplified top-down land-cover sketch drawn as flat outlined vector shapes only — a river band, a road line, a row of factory blocks, a farmland patch, an aquaculture pond — each tagged with 7pt grey labels. Three arrows fan out to the right.

Right column, three state boxes stacked vertically, each with an icon and each distinguishable without color: "已支持" with 1.5pt #009E73 solid border, plain white fill, icon of two dots joined by a directed line, body "≥2 条描述独立提及且不矛盾", example "厂房—沿—河流"; "明确冲突" with 1.5pt #D95F02 solid border and fine 45-degree hatch fill, icon of two opposing arrows, body "不同描述给出互斥关系", example "建筑—在道路左侧 / 右侧"; "未知" with 1.5pt #8EAEC4 dashed border and fine dot-pattern fill, icon of a question mark in a thin square, body "不可定位 / 不可分辨 / 矛盾无法仲裁", example "耕地—邻接—养殖水面？".

Bottom band, two side-by-side panels. Left, on #F7F7F7 tint with 1.0pt #CCCCCC border: "二值处理（现行）", "未提及 → 负例惩罚", with a solid #D95F02 arrow into a small box "损失". Right, with a 2.5pt #009E73 bold border and a small green pill "本项目": "三态处理", "未知 → 屏蔽监督", with a dashed #8EAEC4 arrow that is visibly interrupted by a short slash across its middle, pointing into a small box "损失".

Bottom legend line in 7pt grey: "已支持=绿实线　明确冲突=橙实线斜纹　未知=灰虚线点阵".

Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.
```

### Caption 保留内容
三态判定的证据来源与适用边界见图 F8；屏蔽监督的具体损失构造形式见研究内容二。

---

## F3 研究现状三条脉络与本项目切入点

**type** Landscape / Positioning ｜ **aspect** 16:9 ｜ **落点** 立项依据 1.2 末 / 1.3 ｜ **优先级** strong

### JSON spec

```json
{
  "diagram_type": "Research Landscape with three lanes converging to gaps",
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
      "lane_header": "#1B3A5C 1.5pt solid border, white fill",
      "prior_work_node": "#CCCCCC 1.0pt solid border, white fill, text #666666",
      "gap_box": "#D95F02 1.5pt solid border, white fill",
      "entry_point": "#009E73 2.5pt solid border, white fill",
      "lane_bg_a": "#F7F7F7", "lane_bg_b": "#F2F6FA", "lane_bg_c": "#F7F7F7"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Lane (A)",
      "shape": "Horizontal swimlane on #F7F7F7 tint, header box #1B3A5C border",
      "exact_title_to_render_inside": "脉络A：对齐更细",
      "internal_content": {"layout": "Four grey nodes left to right connected by thin arrows",
        "exact_text": "细粒度交互 → 遥感多尺度适配 → 全局—局部对齐 → 视觉语言模型领域适配"},
      "flow": "Arrow pointing RIGHT to 不足①"
    },
    {
      "relative_position": "Middle Lane (B)",
      "shape": "Horizontal swimlane on #F2F6FA tint, header box #1B3A5C border",
      "exact_title_to_render_inside": "脉络B：关系增强",
      "internal_content": {"layout": "Four grey nodes left to right",
        "exact_text": "单模态实体关系 → 伪区域空间通道注意力 → 方向导向嵌入 → 空间感知实体关系"},
      "flow": "Arrow pointing RIGHT to 不足②"
    },
    {
      "relative_position": "Bottom Lane (C)",
      "shape": "Horizontal swimlane on #F7F7F7 tint, header box #1B3A5C border",
      "exact_title_to_render_inside": "脉络C：失配抑制",
      "internal_content": {"layout": "Four grey nodes left to right",
        "exact_text": "部分错配鲁棒学习 → 相似度校正 → 证据深度学习 → 遥感伪匹配对判别"},
      "flow": "Arrow pointing RIGHT to 不足③"
    },
    {
      "relative_position": "Right Column, three stacked boxes",
      "shape": "Rounded rectangles, #D95F02 1.5pt border, white fill",
      "exact_text": "①「未提及」与「真实冲突」混为一谈\\n②关系作增强特征，非可判定证据\\n③评测口径难支撑可归因结论",
      "exact_floating_text": "同出一源：配对关系被当作完备且二值的监督信号",
      "flow": "Three arrows converging RIGHT into 本项目切入点"
    },
    {
      "relative_position": "Far Right",
      "shape": "Rounded rectangle, #009E73 2.5pt border, white fill",
      "icon": "a small wedge entering a stack of layers, monochrome line art",
      "exact_title_to_render_inside": "本项目切入点",
      "exact_text": "把关系证据的可判定状态\\n提升为显式建模变量",
      "exact_floating_text": "本项目"
    },
    {
      "relative_position": "Bottom Strip",
      "shape": "#8EAEC4 1.0pt dashed border, no fill",
      "exact_text": "不主张首次引入空间关系，也不主张首次处理不完备图文对应；两方向均已有成熟工作",
      "secondary_note": "7pt #666666"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Prior-work nodes must visually recede: 1.0pt #CCCCCC borders and #666666 text, no icons.",
    "Exactly one element carries the 2.5pt bold highlight: 本项目切入点.",
    "Lane backgrounds are very light tints only; text stays fully legible.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows, NO citation numbers on figure."
  ],
  "caption_note": [
    "各脉络代表性文献编号见正文 1.2 各小节",
    "泳道内横向次序按方法代际而非严格发表年份（推断，待申请人确认）"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic research-landscape diagram on a pure white #FFFFFF canvas, mapping three lines of prior work onto three unresolved gaps and one entry point.

Three horizontal swimlanes stacked vertically, each occupying the left two-thirds of the canvas. Lane backgrounds alternate very light tints: #F7F7F7, #F2F6FA, #F7F7F7. Each lane opens with a header box, 1.5pt #1B3A5C border, white fill, bold titles "脉络A：对齐更细", "脉络B：关系增强", "脉络C：失配抑制". Inside each lane, four small prior-work nodes run left to right, joined by thin 1.0pt arrows; every node uses a deliberately receding style — 1.0pt #CCCCCC border, white fill, #666666 8pt text, no icons. Lane A nodes read "细粒度交互", "遥感多尺度适配", "全局—局部对齐", "视觉语言模型领域适配". Lane B reads "单模态实体关系", "伪区域空间通道注意力", "方向导向嵌入", "空间感知实体关系". Lane C reads "部分错配鲁棒学习", "相似度校正", "证据深度学习", "遥感伪匹配对判别".

Each lane ends with a solid #4D4D4D arrow pointing right into its own gap box. The three gap boxes stack in a right-hand column, each 1.5pt #D95F02 border, white fill: "①「未提及」与「真实冲突」混为一谈", "②关系作增强特征，非可判定证据", "③评测口径难支撑可归因结论". A thin bracket spans the three boxes with a 7pt grey side note "同出一源：配对关系被当作完备且二值的监督信号".

Three short arrows converge from the gap boxes into a final box at the far right, drawn with a 2.5pt #009E73 bold border and a small green pill "本项目": bold title "本项目切入点", body "把关系证据的可判定状态提升为显式建模变量", with a small monochrome icon of a wedge entering a stack of layers.

Bottom strip: a 1.0pt #8EAEC4 dashed frame with no fill, 7pt #666666 text "不主张首次引入空间关系，也不主张首次处理不完备图文对应；两方向均已有成熟工作".

Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No citation numbers on the figure. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
各脉络代表性文献编号见正文 1.2；泳道内横向次序按方法代际组织，非严格发表年份。

---

## F4 总体研究框架图

**type** Overall Framework ｜ **aspect** 16:9 ｜ **落点** 研究内容 1.5 技术路线（全篇主图）｜ **优先级** must

### JSON spec

```json
{
  "diagram_type": "Overall Research Framework, four-layer vertical with feedback loop",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed curved"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "question_banner": "#1B3A5C 1.5pt solid border, white fill",
      "sublayer_goal": "#2E6B9E 1.5pt solid border, white fill",
      "content_container": "#1B3A5C 1.5pt solid border on #F2F6FA tint",
      "deliverable": "#5BA0D0 1.0pt solid border, white fill",
      "data_entry": "#2E6B9E 1.5pt solid border, white fill",
      "hypothesis": "#5BA0D0 1.0pt solid border, white fill"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid", "feedback_loop": "#4D4D4D dashed curved"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Banner, full width",
      "shape": "Wide rectangle, #1B3A5C 1.5pt border, white fill",
      "exact_title_to_render_inside": "关键科学问题",
      "exact_text": "描述覆盖天然不完备时，如何区分「描述未覆盖」与「实际关系冲突」，\\n使有证据的关系参与约束、不可判定的关系不作监督信号"
    },
    {
      "relative_position": "Second Layer, three equal columns",
      "shape": "Three rectangles, #2E6B9E 1.5pt border, white fill",
      "exact_text": "子问题1 表示层 → 目标G1\\n子问题2 学习层 → 目标G2\\n子问题3 验证层 → 目标G3",
      "internal_content": {
        "col_1_note": "三态可判定、可人工复核",
        "col_2_note": "不牺牲标准召回的前提下降低关系冲突误匹配",
        "col_3_note": "效果可归因于关系建模本身"
      }
    },
    {
      "relative_position": "Third Layer Left",
      "shape": "Large container, #1B3A5C 1.5pt border on #F2F6FA tint",
      "icon": "two dots joined by a directed line, monochrome",
      "exact_title_to_render_inside": "内容一　关系证据三态建模",
      "exact_text": "数据审计 · 实体关系词表 · 三态判定规范",
      "flow": "Horizontal arrow pointing RIGHT to 内容二, arrow label 三态标签"
    },
    {
      "relative_position": "Third Layer Center",
      "shape": "Large container, #1B3A5C 1.5pt border on #F2F6FA tint",
      "icon": "stacked horizontal layers with a curved residual arrow, monochrome",
      "exact_title_to_render_inside": "内容二　关系约束的跨模态匹配",
      "exact_text": "视觉语言编码器 + 参数高效适配 · 三臂对照",
      "flow": "Horizontal arrow pointing RIGHT to 内容三, arrow label 检索模型"
    },
    {
      "relative_position": "Third Layer Right",
      "shape": "Large container, #1B3A5C 1.5pt border on #F2F6FA tint",
      "icon": "a gauge with tick marks, monochrome",
      "exact_title_to_render_inside": "内容三　标准检索与关系挑战联合验证",
      "exact_text": "五维分层评测 · 可归因性控制"
    },
    {
      "relative_position": "Fourth Layer, three columns aligned under contents",
      "shape": "Three boxes, #5BA0D0 1.0pt border, white fill",
      "exact_text": "审计报告 / 关系词表 / 证据字段规范 / 关系挑战子集\\n核心方法 / 训练与推理代码 / 三臂对照与消融\\n评测协议 / 分层结果报告 / 轻量演示与复现材料"
    },
    {
      "relative_position": "Left Vertical Strip",
      "shape": "Tall box, #2E6B9E 1.5pt border, white fill",
      "icon": "three stacked image frames with a diagonal cross, monochrome",
      "exact_title_to_render_inside": "公开数据",
      "exact_text": "RSITMD · RSICD\\n（SkyScript 许可满足时补充）",
      "secondary_note": "审计 + 去重",
      "flow": "Arrow pointing RIGHT into 内容一"
    },
    {
      "relative_position": "Right Vertical Strip",
      "shape": "Tall box, #5BA0D0 1.0pt border, white fill",
      "exact_title_to_render_inside": "三条可证伪假说",
      "exact_text": "H1 现象存在性\\nH2 机制判断\\nH3 可归因性",
      "secondary_note": "均设证伪条件"
    },
    {
      "relative_position": "Bottom, spanning right to left below all layers",
      "shape": "Curved dashed arrow, #4D4D4D 1.0pt",
      "exact_floating_text": "错误归因回流　每年 ≥1 次",
      "flow": "From 内容三 curving LEFT back to both 内容一 and 内容二"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "The dashed feedback arc at the bottom must NOT cross any forward arrow.",
    "Module separation relies on the blue lightness ramp (#1B3A5C / #2E6B9E / #5BA0D0), not on extra hues.",
    "Three-state tokens appear only as three small color dots (green / orange / grey) on the 三态标签 arrow label.",
    "All container boxes use WHITE or very light tint fill with COLORED BORDERS ONLY.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "各内容的详细技术路线分别见 F5 / F6 / F7",
    "目标判据（κ ≥ 0.7【暂定】、mR 不显著下降、等预算对照）见正文研究目标"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic overall-framework diagram on a pure white #FFFFFF canvas, four stacked layers plus a bottom feedback arc, in a restrained navy-blue monochrome scheme.

Top: a full-width banner, 1.5pt #1B3A5C border, white fill, bold label "关键科学问题" and body text "描述覆盖天然不完备时，如何区分「描述未覆盖」与「实际关系冲突」，使有证据的关系参与约束、不可判定的关系不作监督信号".

Second layer: three equal columns, each a rectangle with 1.5pt #2E6B9E border, reading "子问题1 表示层 → 目标G1", "子问题2 学习层 → 目标G2", "子问题3 验证层 → 目标G3", each with a 7pt grey sub-note beneath.

Third layer: three large containers on very light #F2F6FA tint with 1.5pt #1B3A5C borders, connected left to right by solid #4D4D4D arrows whose labels read "三态标签" and "检索模型". Container one: icon of two dots joined by a directed line, title "内容一　关系证据三态建模", body "数据审计 · 实体关系词表 · 三态判定规范". Container two: icon of stacked horizontal layers with a curved residual arrow, title "内容二　关系约束的跨模态匹配", body "视觉语言编码器 + 参数高效适配 · 三臂对照". Container three: icon of a gauge with tick marks, title "内容三　标准检索与关系挑战联合验证", body "五维分层评测 · 可归因性控制". The "三态标签" arrow label carries three tiny dots coloured #009E73, #D95F02 and #8EAEC4.

Fourth layer: three deliverable boxes with 1.0pt #5BA0D0 borders aligned under their containers, listing "审计报告 / 关系词表 / 证据字段规范 / 关系挑战子集", "核心方法 / 训练与推理代码 / 三臂对照与消融", "评测协议 / 分层结果报告 / 轻量演示与复现材料".

Left vertical strip: a tall box, 1.5pt #2E6B9E border, icon of three stacked image frames with a diagonal cross, title "公开数据", body "RSITMD · RSICD（SkyScript 许可满足时补充）", grey note "审计 + 去重", arrow pointing right into 内容一. Right vertical strip: a tall box, 1.0pt #5BA0D0 border, title "三条可证伪假说", body "H1 现象存在性 / H2 机制判断 / H3 可归因性", grey note "均设证伪条件".

Bottom: one long 1.0pt dashed #4D4D4D curved arrow running right to left below every layer, from 内容三 back to 内容一 and 内容二, labelled "错误归因回流　每年 ≥1 次". It must not cross any forward arrow.

Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White or very light tint fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
各内容的详细技术路线分别见图 F5 / F6 / F7；目标判据（κ ≥ 0.7【暂定】、标准 mR 不显著下降、等预算对照下改进成立）见研究目标一节。

---

## F5 技术路线图一：不完备描述条件下的关系证据三态建模

**type** Technical Route ｜ **aspect** 3:2 ｜ **落点** 研究内容一 ｜ **优先级** must

### JSON spec

```json
{
  "diagram_type": "Technical Route — three-state relation evidence modelling",
  "diagram_title_rendering": "None",
  "aspect_ratio": "3:2",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "hard_separator": "2.5pt solid #1B3A5C vertical rule", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "step": "#2E6B9E 1.5pt solid border, white fill",
      "evidence_source": "#5BA0D0 1.0pt solid border, white fill",
      "state_supported": "#009E73 1.5pt solid border, white fill",
      "state_conflict": "#D95F02 1.5pt solid border, white fill with 45-degree hatch",
      "state_unknown": "#8EAEC4 1.5pt dashed border, white fill with dot pattern",
      "hard_separator": "#1B3A5C 2.5pt vertical rule",
      "panel_train": "#F7F7F7", "panel_eval": "#F2F6FA"
    },
    "flow_arrow_colors": {"main_forward_flow": "#4D4D4D solid"}
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Step 1, top left",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "icon": "small vertical bar chart thumbnail, monochrome",
      "exact_title_to_render_inside": "数据审计",
      "exact_text": "分层抽样【暂定 200–400 组】\\n统计同图多描述覆盖差异",
      "flow": "Arrow pointing RIGHT to 实体关系词表"
    },
    {
      "relative_position": "Step 2, top center",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "icon": "a small table grid, monochrome",
      "exact_title_to_render_inside": "实体关系词表",
      "internal_content": {
        "layout": "Three stacked rows",
        "exact_text": "拓扑：相离 / 相邻 / 包含\\n方向：影像坐标系八方位，可归并四方位\\n度量：按地面采样距离归一化的距离分级"
      },
      "secondary_note": "规模【暂定 ≤20 类实体、10 类关系】",
      "flow": "Arrow pointing RIGHT to 三类证据源"
    },
    {
      "relative_position": "Step 3, top right, three sub-columns",
      "shape": "Panel with three boxes, #5BA0D0 1.0pt borders",
      "exact_title_to_render_inside": "三类证据源",
      "internal_content": {
        "col_1": {"exact_header": "同图多描述交叉印证", "exact_text_below_icon": "训练端弱标注"},
        "col_2": {"exact_header": "独立视觉证据", "exact_text_below_icon": "训练端弱标注"},
        "col_3": {"exact_header": "人工核验", "exact_text_below_icon": "评测端唯一合法来源"}
      },
      "flow": "Arrow pointing DOWN to 三态判定"
    },
    {
      "relative_position": "Middle band, three boxes side by side",
      "shape": "Three state boxes with the standard three-state encoding",
      "exact_title_to_render_inside": "三态判定",
      "exact_text": "已支持\\n明确冲突\\n未知",
      "exact_floating_text": "未知不是兜底类别"
    },
    {
      "relative_position": "Middle right, attached note",
      "shape": "Small box, #CCCCCC 1.0pt border, white fill",
      "exact_title_to_render_inside": "坐标系约定",
      "exact_text": "左右上下基于影像坐标系\\n旋转翻转增强同步变换标签\\n不得解释为地理方位"
    },
    {
      "relative_position": "Middle left, attached note",
      "shape": "Small box, #CCCCCC 1.0pt border, white fill",
      "icon": "a small three-row table, monochrome",
      "exact_title_to_render_inside": "分辨率分档",
      "exact_text": "各关系类型按地面采样距离\\n给出适用范围"
    },
    {
      "relative_position": "Bottom, split by a thick vertical rule",
      "shape": "Two panels separated by a 2.5pt #1B3A5C vertical rule labelled 硬性隔离",
      "internal_content": {
        "left_panel": {"shape": "#F7F7F7 tint", "exact_header": "训练端", "exact_text": "允许证据源①②产生的弱标注"},
        "right_panel": {"shape": "#F2F6FA tint", "exact_header": "评测端", "exact_text": "仅接受人工核验标签"}
      },
      "exact_floating_text": "硬性隔离",
      "flow": "Arrow from the right panel pointing RIGHT to 关系挑战子集"
    },
    {
      "relative_position": "Bottom Far Right",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "icon": "small normal distribution curve, monochrome",
      "exact_title_to_render_inside": "关系挑战子集",
      "exact_text": "【暂定 1500–2500 组】",
      "secondary_note": "4 类关系分组 × 3 覆盖度分档，每格【暂定 120–200 组】"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "The thick 2.5pt vertical rule labelled 硬性隔离 is the second visual anchor and must be clearly heavier than every other line.",
    "Keep every 【暂定 …】 string verbatim, including the bracket characters.",
    "Three states keep the global encoding: solid green / solid orange + hatch / dashed grey + dots.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "样本量按统计效力倒推：双侧显著性水平 0.05、检验效能 0.8、中等效应量",
    "三类证据源的适用边界与未知态判据详见 F8"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic technical-route diagram on a pure white #FFFFFF canvas, showing how three-state relation evidence is built from incomplete image captions.

Top row, three steps flowing left to right with solid 1.5pt #4D4D4D arrows. Step 1: rounded rectangle, 1.5pt #2E6B9E border, small monochrome vertical bar-chart thumbnail, title "数据审计", body "分层抽样【暂定 200–400 组】" and "统计同图多描述覆盖差异". Step 2: same border style, small monochrome table-grid icon, title "实体关系词表", three stacked rows "拓扑：相离 / 相邻 / 包含", "方向：影像坐标系八方位，可归并四方位", "度量：按地面采样距离归一化的距离分级", plus a 7pt grey note "规模【暂定 ≤20 类实体、10 类关系】". Step 3: a panel titled "三类证据源" holding three sub-boxes with 1.0pt #5BA0D0 borders, headers "同图多描述交叉印证", "独立视觉证据", "人工核验", each with a small grey pill beneath reading "训练端弱标注", "训练端弱标注", "评测端唯一合法来源".

A downward arrow leads to the middle band: three state boxes side by side using the global encoding — "已支持" with 1.5pt #009E73 solid border and plain fill, "明确冲突" with 1.5pt #D95F02 solid border and fine 45-degree hatch, "未知" with 1.5pt #8EAEC4 dashed border and fine dot fill; a 7pt grey floating note reads "未知不是兜底类别". Flanking notes in 1.0pt #CCCCCC boxes: on the left "分辨率分档 — 各关系类型按地面采样距离给出适用范围" with a small three-row table icon; on the right "坐标系约定 — 左右上下基于影像坐标系；旋转翻转增强同步变换标签；不得解释为地理方位".

Bottom band: two panels separated by one thick 2.5pt #1B3A5C vertical rule, clearly heavier than every other line in the figure, labelled "硬性隔离". Left panel on #F7F7F7 tint: "训练端 — 允许证据源①②产生的弱标注". Right panel on #F2F6FA tint: "评测端 — 仅接受人工核验标签". A solid arrow exits the right panel into a final box with 1.5pt #2E6B9E border and a small monochrome normal-distribution curve icon: title "关系挑战子集", body "【暂定 1500–2500 组】", grey note "4 类关系分组 × 3 覆盖度分档，每格【暂定 120–200 组】".

Reproduce every 【暂定 …】 string verbatim including brackets. Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No gradients, no shadows, no 3D, no emojis. Aspect ratio 3:2.
```

### Caption 保留内容
样本量按统计效力倒推（双侧显著性水平 0.05、检验效能 0.8、中等效应量）；第一年完成审计后依实际效应量重新核定，分层过细时优先合并分档而非降低每格样本量。三类证据源的适用边界与未知态判据详见图 F8。

---

## F6 技术路线图二：三臂对照的关系约束跨模态匹配

**type** Technical Route / Network Architecture ｜ **aspect** 16:9 ｜ **落点** 研究内容二 ｜ **优先级** must

> 全篇最重要的一张。唯一的 2.5pt 加粗落在臂 (c)。

### JSON spec

```json
{
  "diagram_type": "Technical Route — three-arm controlled comparison for relation-constrained cross-modal matching",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Noto Sans SC, sans-serif",
    "font_hierarchy": {"title": "10pt bold", "primary_label": "8pt regular", "secondary_note": "7pt regular #666666"},
    "stroke_hierarchy": {"container_border": "1.5pt solid", "frozen_border": "1.5pt dashed", "ours_highlight": "2.5pt solid", "flow_arrow": "1.5pt solid", "masked_arrow": "1.5pt dashed with a short slash across mid-segment"}
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "input": "#2E6B9E 1.5pt solid border, white fill",
      "backbone_frozen": "#1B3A5C 1.5pt dashed border, white fill, grey pill [Fixed]",
      "adapter_trainable": "#1B3A5C 1.5pt solid border, white fill, blue pill [Tune]",
      "arm_a": "#CCCCCC 1.0pt solid border, white fill, text #666666",
      "arm_b": "#D95F02 1.5pt solid border, white fill",
      "arm_c": "#009E73 2.5pt solid border, white fill, green pill 本项目",
      "backbone_panel": "#F2F6FA"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "#4D4D4D solid",
      "supervision_apply": "#4D4D4D solid, label 施加约束",
      "supervision_mask": "#8EAEC4 dashed with mid-segment slash, label 屏蔽监督"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Far Left, three stacked inputs",
      "shape": "Three small boxes, #2E6B9E 1.5pt border, white fill",
      "exact_text": "遥感影像\\n文本描述\\n三态关系标签",
      "icon": "image-frame icon / document-lines icon / two dots joined by a directed line",
      "secondary_note": "三态标签处显示绿橙灰三色小点",
      "flow": "Arrows pointing RIGHT into 共享骨干"
    },
    {
      "relative_position": "Left Center",
      "shape": "Container panel on #F2F6FA tint, #1B3A5C 1.5pt border",
      "exact_title_to_render_inside": "共享骨干（三臂完全一致）",
      "internal_content": {
        "layout": "Two dashed sub-blocks above one solid sub-block",
        "sub_1": {"exact_header": "图像编码器", "secondary_note": "CLIP / RemoteCLIP", "shape": "dashed border, pill [Fixed]"},
        "sub_2": {"exact_header": "文本编码器", "secondary_note": "CLIP / RemoteCLIP", "shape": "dashed border, pill [Fixed]"},
        "sub_3": {"exact_header": "参数高效适配", "shape": "solid border, pill [Tune]", "icon": "small square nested at the corner of a larger square"}
      },
      "flow": "Three arrows fanning RIGHT to the three arms"
    },
    {
      "relative_position": "Top Banner over the three arms",
      "shape": "Bracket spanning all three arms, no fill",
      "exact_floating_text": "唯一变量：关系信息的处理方式"
    },
    {
      "relative_position": "Right, Arm A (top)",
      "shape": "Rounded rectangle, #CCCCCC 1.0pt border, white fill, text #666666",
      "exact_title_to_render_inside": "臂 (a) 忽略关系",
      "exact_text": "主流全局—局部对齐基线"
    },
    {
      "relative_position": "Right, Arm B (middle)",
      "shape": "Rounded rectangle, #D95F02 1.5pt border, white fill",
      "exact_title_to_render_inside": "臂 (b) 未知作负例",
      "exact_text": "现有失配抑制思路的等价物"
    },
    {
      "relative_position": "Right, Arm C (bottom, largest)",
      "shape": "Rounded rectangle, #009E73 2.5pt border, white fill, green pill 本项目",
      "exact_title_to_render_inside": "臂 (c) 三态区分 + 未知屏蔽",
      "internal_content": {
        "layout": "Three supervision edges",
        "edge_1": {"exact_label": "已支持", "flow": "solid #4D4D4D arrow, label 施加约束"},
        "edge_2": {"exact_label": "明确冲突", "flow": "solid #4D4D4D arrow, label 施加约束"},
        "edge_3": {"exact_label": "未知", "flow": "dashed #8EAEC4 arrow with a short slash across its mid-segment, label 屏蔽监督"}
      },
      "flow": "Arrow pointing DOWN to 三条候选实现"
    },
    {
      "relative_position": "Bottom Right, three branches under Arm C",
      "shape": "Three boxes, #5BA0D0 1.0pt border, white fill",
      "exact_text": "关系证据引导的对齐损失加权\\n关系一致性重排序\\n关系条件下的局部匹配",
      "exact_floating_text": "择一为主线，其余作消融；主线由第一年最小实验选定"
    },
    {
      "relative_position": "Bottom Strip, full width",
      "shape": "Constraint bar, #CCCCCC 1.0pt border, #F7F7F7 fill",
      "exact_text": "对照约束：等骨干 · 等训练预算 · 等数据划分 · 等预处理 · ≥3 随机种子"
    },
    {
      "relative_position": "Bottom Left corner note",
      "shape": "#8EAEC4 1.0pt dashed border, no fill",
      "exact_text": "借用不确定性建模工具，但建模对象是关系命题的可判定性，不是相似度不确定性",
      "secondary_note": "7pt #666666"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Frozen encoders use DASHED borders with a grey [Fixed] pill; the trainable adapter uses a SOLID border with a blue [Tune] pill. No snowflake or fire icons.",
    "The masked supervision arrow must be dashed AND visibly interrupted by a short slash in its middle segment.",
    "Exactly one element carries the 2.5pt bold highlight: 臂 (c).",
    "Arm (a) must visually recede: 1.0pt grey border and #666666 text.",
    "Render text ONLY within designated exact_* fields.",
    "NO emojis, NO lock/fire/lightning icons, NO 3D rendering, NO gradients, NO shadows."
  ],
  "caption_note": [
    "损失函数完整形式、屏蔽比例与超参见正文与补充材料",
    "三臂共享同一骨干、训练预算、数据划分与预处理，唯一变量为关系信息的处理方式"
  ]
}
```

### Image prompt (EN)

```
Flat vector academic architecture diagram on a pure white #FFFFFF canvas, showing a three-arm controlled comparison in which only the handling of relation information varies.

Far left: three small input boxes with 1.5pt #2E6B9E borders stacked vertically — "遥感影像" with a small image-frame icon, "文本描述" with a document-lines icon, "三态关系标签" with an icon of two dots joined by a directed line and three tiny dots coloured #009E73, #D95F02 and #8EAEC4. Solid arrows lead right.

Left centre: a container panel on very light #F2F6FA tint with a 1.5pt #1B3A5C border, titled "共享骨干（三臂完全一致）". Inside it, two sub-blocks drawn with DASHED 1.5pt #1B3A5C borders, each carrying a small grey pill "[Fixed]": "图像编码器" and "文本编码器", both with a 7pt grey note "CLIP / RemoteCLIP" and a small icon of stacked horizontal layers with a curved residual arrow. Below them one sub-block with a SOLID 1.5pt #1B3A5C border and a small blue pill "[Tune]": "参数高效适配", with an icon of a small square nested at the corner of a larger square. Three arrows fan out to the right.

A bracket spans the top of the right region with the floating label "唯一变量：关系信息的处理方式".

Right region, three arms stacked. Arm A, deliberately receding: 1.0pt #CCCCCC border, #666666 text, "臂 (a) 忽略关系", "主流全局—局部对齐基线". Arm B: 1.5pt #D95F02 border, "臂 (b) 未知作负例", "现有失配抑制思路的等价物". Arm C, the largest and the only bold element: 2.5pt #009E73 border with a small green pill "本项目", title "臂 (c) 三态区分 + 未知屏蔽", containing three supervision edges — "已支持" with a solid #4D4D4D arrow labelled "施加约束", "明确冲突" with a solid #4D4D4D arrow labelled "施加约束", and "未知" with a dashed #8EAEC4 arrow that is visibly interrupted by a short slash across its middle, labelled "屏蔽监督".

Below Arm C, three candidate-implementation boxes with 1.0pt #5BA0D0 borders: "关系证据引导的对齐损失加权", "关系一致性重排序", "关系条件下的局部匹配", with a 7pt grey note "择一为主线，其余作消融；主线由第一年最小实验选定".

Full-width bottom bar on #F7F7F7 with 1.0pt #CCCCCC border: "对照约束：等骨干 · 等训练预算 · 等数据划分 · 等预处理 · ≥3 随机种子". Bottom-left dashed #8EAEC4 note in 7pt #666666: "借用不确定性建模工具，但建模对象是关系命题的可判定性，不是相似度不确定性".

Chinese sans-serif, titles 10pt bold, labels 8pt, notes 7pt grey. White fills, colored borders only, 6px radius. No snowflake, lock, fire or lightning icons; frozen status is shown by dashed borders and [Fixed] pills only. No gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.
```

### Caption 保留内容
损失函数完整形式、屏蔽比例与超参见正文；三臂共享同一骨干、训练预算、数据划分与预处理，唯一变量为关系信息的处理方式；关键训练实验不少于 3 个随机种子，报告均值、标准差与置信区间。
