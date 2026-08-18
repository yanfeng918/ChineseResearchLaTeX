# Figure Spec Package — NSFC 2026 Education，F1–F7（完整版）

- 上游：[01-figure-plan.md](01-figure-plan.md) · [02-palette-decision.md](02-palette-decision.md)
- style_family：**classic**（白底 + 彩色描边，非 pastel）
- palette：**Nature Blue + 2 语义强调色**
- **本轮不生图，仅交付 JSON spec + 英文出图 prompt**

## 全局约定（7 张图共用）

```yaml
primary:    "#1B3A5C"   # 输入 / 核心模态
secondary:  "#2E6B9E"   # 主链阶段 / 骨干模块
tertiary:   "#5BA0D0"   # 子模块 / 浅填充
gray_blue:  "#8EAEC4"   # 扩展模态 / 待核验 / 降级（必虚线）
alert:      "#D95F02"   # 失效 / 错配 / 惩罚（必配 ✗ 或 ⚠）
pass:       "#1B9E77"   # 通过 / 正确 / 输出（必配 ✓）
text:       "#333333"   fill: "#FFFFFF"   section_bg: "#F7F7F7"
border:     "#CCCCCC"   arrow: "#4D4D4D"
canvas_width: 183mm     font: Arial / Helvetica 无衬线
font_hierarchy:  title 10-12pt bold · label 8-9pt · note 7-8pt · symbol 6-7pt italic
stroke_hierarchy: container 1.5pt · divider 1.0pt · flow arrow 1.5pt · feedback 1.0pt dashed
label_language: zh-CN（简体中文；数学符号与指标名保留原写法）
```

**七条硬约束（每张图的 prompt 末尾都已写入）**

1. 图内文字**一律简体中文**；`Recall@K`、`MRR`、`VRR`、`Krippendorff's α`、`B0`–`B3` 及数学符号保持原写法。
2. 通过 / 失效**必须双编码**：通过 = 实线 + ✓；失效 = 虚线 + ✗ 或 ⚠ + 斜纹。**不得仅靠颜色区分**（二者灰度差仅 6.5，黑白打印会糊）。
3. 扩展模态（实验代码 / 产业案例）、待核验队列、降级路径**一律虚线 + `#8EAEC4`**。
4. **禁止出现任何具体数值、准确率、样本量结果**——本文档是申请书，无既有实验结果。
5. `alert` 只能用 `#D95F02`（橙），**禁止换成纯红 `#D62728`**（红绿色盲不可分）。
6. 白底 + 彩色描边；无渐变、无 3D、无阴影、无 emoji、无锁 / 火焰 / 闪电装饰图标。
7. 图标为**单色细线**，用所在模块的描边色或深灰，禁止彩色填充图标。

---

# F1 · 项目总体研究框架图

**类型**：Overall Framework ｜ **优先级**：MUST ｜ **aspect_ratio**：16:9
**落位**：`extraTex/1.2.内容目标问题.tex:4`（`\subsubsection{研究内容}` 之后）

## JSON Spec

```json
{
  "diagram_type": "Overall Framework — Multimodal Teaching Resource Construction System",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": {
      "title": "10-12pt bold",
      "primary_label": "8-9pt regular",
      "secondary_note": "7-8pt regular",
      "tensor_shape": "6-7pt italic"
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
    "main_block_color_palette": {
      "input_column": "#1B3A5C 1.5pt solid border, white fill",
      "backbone_stages": "#2E6B9E 1.5pt solid border, white fill",
      "extended_modality": "#8EAEC4 1.2pt DASHED border, white fill",
      "output_column": "#1B9E77 1.5pt solid border, white fill",
      "boundary_note": "#8EAEC4 1.0pt dashed border, #F7F7F7 fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "#4D4D4D 1.5pt solid arrows",
      "extension_flow": "#8EAEC4 1.0pt dashed arrows"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left column container",
      "shape": "Rounded container, #1B3A5C 1.5pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "资源输入",
      "internal_content": {
        "layout": "Four stacked sub-boxes, top three solid, bottom one dashed",
        "row_1": { "exact_text": "课程文本", "icon": "small document with text lines, monochrome line art" },
        "row_2": { "exact_text": "运行曲线", "icon": "small time-series waveform thumbnail, monochrome" },
        "row_3": { "exact_text": "设备结构图", "icon": "small wind-turbine and PV-panel outline icon, monochrome" },
        "row_4": {
          "exact_text": "实验代码 / 产业案例",
          "secondary_note": "[扩展]",
          "shape": "#8EAEC4 1.2pt DASHED border",
          "icon": "small code-bracket icon, monochrome"
        }
      },
      "flow": "Horizontal solid arrow RIGHT to stage ①; row_4 uses a DASHED arrow"
    },
    {
      "relative_position": "Center chain, stage 1 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "① 受控输入",
      "exact_text": "许可 · 脱敏 · 登记",
      "icon": "small clipboard-with-checkmark icon, monochrome line art",
      "flow": "Solid arrow RIGHT to stage ②"
    },
    {
      "relative_position": "Center chain, stage 2 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "② 联合知识约束",
      "exact_text": "产业任务 × 课程知识",
      "exact_floating_text": "创新点一",
      "icon": "small icon of two overlapping circles labelled Kp and Kc, monochrome",
      "secondary_note": "S_kc",
      "flow": "Solid arrow RIGHT to stage ③"
    },
    {
      "relative_position": "Center chain, stage 3 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "③ 跨模态关联",
      "exact_text": "专业属性 + 来源证据",
      "exact_floating_text": "创新点二",
      "icon": "small icon: two rows of dots with crossing connector arrows, monochrome",
      "secondary_note": "R(i,j)",
      "flow": "Solid arrow RIGHT to stage ④"
    },
    {
      "relative_position": "Center chain, stage 4 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "④ 四层门控",
      "exact_text": "内容 · 课程 · 模态 · 证据",
      "exact_floating_text": "创新点三",
      "icon": "small icon: four stacked horizontal bars narrowing downward (funnel of gates), monochrome",
      "secondary_note": "Q(u)",
      "flow": "Solid arrow RIGHT to stage ⑤"
    },
    {
      "relative_position": "Center chain, stage 5 of 5",
      "shape": "Rounded rectangle, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "⑤ 独立验证",
      "exact_text": "专家盲评 · 跨来源留出",
      "icon": "small magnifying-glass over a checklist icon, monochrome",
      "secondary_note": "VRR",
      "flow": "Solid arrow RIGHT to output column"
    },
    {
      "relative_position": "Right column container",
      "shape": "Rounded container, #1B9E77 1.5pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "研究产出",
      "internal_content": {
        "layout": "Five stacked sub-boxes, each with a leading ✓ glyph",
        "row_1": { "exact_text": "资源单元 u=(c,a,m,e,s)" },
        "row_2": { "exact_text": "可追溯资源包" },
        "row_3": { "exact_text": "资源元数据规范" },
        "row_4": { "exact_text": "质量报告" },
        "row_5": { "exact_text": "本地原型" }
      }
    },
    {
      "relative_position": "Bottom full-width strip",
      "shape": "Wide rounded container, #5BA0D0 1.2pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "示范课程模块：新能源数据分析与功率预测",
      "internal_content": {
        "layout": "Four equal-width horizontal cells",
        "column_1": { "exact_text": "运行数据与变量认知" },
        "column_2": { "exact_text": "预处理与可视化" },
        "column_3": { "exact_text": "预测建模与实验" },
        "column_4": { "exact_text": "结果评价与工程案例" }
      }
    },
    {
      "relative_position": "Bottom right corner, below output column",
      "shape": "Small rounded box, #8EAEC4 1.0pt dashed border, #F7F7F7 fill",
      "exact_text": "研究边界\\n不含学生行为数据\\n不做个性化推荐\\n不接入生产平台"
    },
    {
      "relative_position": "Bottom left, outside all containers",
      "shape": "Borderless legend row",
      "exact_text": "实线 = 核心模态 · 主流程    虚线 = 扩展 · 降级    ✓ 通过    ✗ 拒绝"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY.",
    "Extended modality, downgrade paths and pending queues MUST use #8EAEC4 dashed borders.",
    "Pass/fail MUST be dual-encoded: pass = solid border + ✓; fail = dashed border + ✗. Never color alone.",
    "NO numeric values, NO accuracy figures, NO sample sizes anywhere in the figure.",
    "Icons are monochrome thin line art in the block border color. No colored icons.",
    "NO emojis, NO lock/fire/lightning symbols, NO 3D rendering, NO gradients, NO drop shadows.",
    "Canvas is pure white (#FFFFFF)."
  ],
  "caption_note": [
    "完整资源单元定义 u=(c,a,m,e,s) 各分量含义",
    "S_kc、R(i,j)、Q(u)、VRR 完整公式",
    "四个知识模块的详细知识点清单"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic architecture diagram showing the overall research framework of a multimodal teaching-resource construction system for university new-energy courses. All rendered text must be Simplified Chinese.
>
> Horizontal left-to-right composition in three zones. **Left zone**: a light-grey (#F7F7F7) rounded container titled 「资源输入」 with a 1.5pt dark navy #1B3A5C border, holding four stacked white sub-boxes — 「课程文本」 with a small monochrome document icon, 「运行曲线」 with a tiny time-series waveform thumbnail, 「设备结构图」 with a small wind-turbine-and-solar-panel outline icon, and, visually demoted, 「实验代码 / 产业案例」 with a 1.2pt **dashed** #8EAEC4 border, a small code-bracket icon and a tiny grey pill reading 「[扩展]」.
>
> **Center zone**: five equal white rounded rectangles with 1.5pt medium-blue #2E6B9E borders in a horizontal chain, joined by solid 1.5pt dark-grey #4D4D4D arrows — 「① 受控输入」 (clipboard-with-checkmark icon, small grey subtext 「许可 · 脱敏 · 登记」); 「② 联合知识约束」 (two overlapping circles labelled Kp and Kc, subtext 「产业任务 × 课程知识」, italic symbol 「S_kc」); 「③ 跨模态关联」 (two rows of dots with crossing connectors, subtext 「专业属性 + 来源证据」, symbol 「R(i,j)」); 「④ 四层门控」 (four stacked bars narrowing into a funnel, subtext 「内容 · 课程 · 模态 · 证据」, symbol 「Q(u)」); 「⑤ 独立验证」 (magnifier over checklist, subtext 「专家盲评 · 跨来源留出」, symbol 「VRR」). Small orange-free navy tags 「创新点一」「创新点二」「创新点三」 float directly above stages ②③④.
>
> **Right zone**: a container titled 「研究产出」 with a 1.5pt emerald #1B9E77 border holding five white sub-boxes each prefixed by a green ✓ glyph: 「资源单元 u=(c,a,m,e,s)」「可追溯资源包」「资源元数据规范」「质量报告」「本地原型」.
>
> **Bottom**: a full-width pale-blue #5BA0D0 strip titled 「示范课程模块：新能源数据分析与功率预测」 split into four cells — 「运行数据与变量认知」「预处理与可视化」「预测建模与实验」「结果评价与工程案例」. A small dashed grey box at bottom-right reads 「研究边界 / 不含学生行为数据 / 不做个性化推荐 / 不接入生产平台」. A borderless legend at bottom-left: 「实线 = 核心模态 · 主流程　虚线 = 扩展 · 降级　✓ 通过　✗ 拒绝」.
>
> White canvas, white box fills, colored 1.5pt borders only, 4–6px corner radius, monochrome thin-line icons in each block's border color. No numeric values, no gradients, no shadows, no 3D, no emojis. Font Arial: titles 11pt bold, labels 9pt, notes 7.5pt grey. Aspect ratio 16:9.

## 图注预留（不上图）

> 图 1　项目总体研究框架。资源单元 $u=(c,a,m,e,s)$ 中 $c,a,m,e,s$ 分别为课程知识、专业属性、多模态片段及关系、来源位置与质量状态。阶段②的联合知识约束打分 $S_{\mathrm{kc}}$、阶段③的关系评分 $R(i,j)$、阶段④的质量综合 $Q(u)$ 与主指标 VRR 的完整定义见 3.1 节。实验代码与产业案例为扩展模态（虚线），仅在来源许可、格式与解析条件满足时纳入并单独报告。

---

# F2 · 技术路线与实验验证流程图

**类型**：Pipeline（NSFC 技术路线图体裁）｜ **优先级**：MUST ｜ **aspect_ratio**：3:2
**落位**：`extraTex/1.3.方案及可行性.tex:62`（`\subsubsection{技术路线与实验手段}` 之后）

## JSON Spec

```json
{
  "diagram_type": "Technical Route and Experimental Validation Pipeline",
  "diagram_title_rendering": "None",
  "aspect_ratio": "3:2",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "main_chain": "#2E6B9E 1.5pt solid border, white fill",
      "reject_branch": "#D95F02 1.2pt dashed border, white fill",
      "pending_queue": "#8EAEC4 1.2pt dashed border, white fill",
      "control_container": "#1B3A5C 1.5pt border, #F7F7F7 fill",
      "ours_row": "#1B9E77 1.8pt solid border, white fill"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "#4D4D4D 1.5pt solid",
      "exception_branch": "#D95F02 1.0pt dashed",
      "return_loop": "#8EAEC4 1.0pt dashed curved"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top row, five-stage horizontal chain",
      "shape": "Five rounded rectangles, #2E6B9E 1.5pt border, white fill",
      "internal_content": {
        "layout": "Left-to-right chain joined by solid arrows",
        "column_1": { "exact_text": "材料审查", "icon": "small clipboard-with-checkmark icon, monochrome" },
        "column_2": { "exact_text": "单元切分", "icon": "small icon: a block divided by dashed cut lines, monochrome" },
        "column_3": { "exact_text": "跨模态关联", "icon": "small icon: two rows of dots with crossing arrows, monochrome" },
        "column_4": { "exact_text": "四层门控", "icon": "small icon: four stacked narrowing bars, monochrome" },
        "column_5": { "exact_text": "独立验证", "icon": "small magnifier-over-checklist icon, monochrome" }
      }
    },
    {
      "relative_position": "Below 材料审查",
      "shape": "Small box, #D95F02 1.2pt dashed border, white fill",
      "exact_text": "✗ 不入池",
      "exact_floating_text": "未过审查",
      "failure_branch": "Dashed #D95F02 arrow DOWN from 材料审查"
    },
    {
      "relative_position": "Below center, between 跨模态关联 and 四层门控",
      "shape": "Rounded box, #8EAEC4 1.2pt dashed border, white fill",
      "exact_text": "⚠ 人工核验队列",
      "exact_floating_text": "属性或证据不全",
      "flow": "Dashed arrows DOWN from 跨模态关联 and 四层门控; dashed curved arrow back UP to 跨模态关联"
    },
    {
      "relative_position": "Below 四层门控",
      "shape": "Small box, #D95F02 1.2pt dashed border, white fill",
      "exact_text": "✗ 退回修改",
      "exact_floating_text": "严重错误",
      "failure_branch": "Dashed #D95F02 curved arrow looping LEFT back to 单元切分"
    },
    {
      "relative_position": "Right margin, beside 独立验证",
      "shape": "Rounded box, #5BA0D0 1.2pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "数据划分",
      "internal_content": {
        "layout": "Three stacked lines",
        "row_1": { "exact_text": "按知识模块留出" },
        "row_2": { "exact_text": "按来源留出" },
        "row_3": { "exact_text": "按设备类型留出" }
      },
      "secondary_note": "近重复不跨集合"
    },
    {
      "relative_position": "Bottom large container spanning full width",
      "shape": "Wide rounded container, #1B3A5C 1.5pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "统一实验控制",
      "secondary_note": "同一材料 · 同一划分 · 同一人工预算",
      "internal_content": {
        "layout": "Upper row of four method boxes, lower dashed row of five ablation pills",
        "row_1_col_1": { "exact_text": "B0 人工整理" },
        "row_1_col_2": { "exact_text": "B1 通用大模型" },
        "row_1_col_3": { "exact_text": "B2 文本 RAG" },
        "row_1_col_4": { "exact_text": "B3 完整方法", "secondary_note": "[本方法]", "shape": "#1B9E77 1.8pt solid border" },
        "row_2": { "exact_text": "消融：−产业知识　−课程知识　−专业属性　−来源位置　−质量层", "shape": "#8EAEC4 dashed pills" }
      }
    },
    {
      "relative_position": "Very bottom, three side-by-side metric outlets",
      "shape": "Three borderless columns separated by 1.0pt #CCCCCC dividers",
      "internal_content": {
        "column_1": { "exact_header": "构建层", "exact_text": "边界 F1 · 覆盖 · 属性错误率" },
        "column_2": { "exact_header": "关联层", "exact_text": "Recall@K · MRR · 关系 F1 · 来源定位" },
        "column_3": { "exact_header": "质量层", "exact_text": "VRR · 检出率 · 误报率 · 专家盲评" }
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "All boxes WHITE fill with COLORED BORDERS ONLY.",
    "Main forward flow arrows SOLID; all exception, return and pending arrows DASHED.",
    "Reject nodes MUST carry a ✗ glyph; pending nodes MUST carry a ⚠ glyph. Never color alone.",
    "B3 完整方法 is the only emerald-bordered method box, marked with a [本方法] pill.",
    "NO numeric values, NO metric scores anywhere in the figure.",
    "Icons are monochrome thin line art. NO emojis, NO 3D, NO gradients, NO shadows."
  ],
  "caption_note": [
    "B0–B3 各基线的具体设置与训练预算",
    "消融项与三个关键科学问题的对应关系",
    "各层指标的完整定义与统计口径"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic pipeline diagram showing the technical route and experimental validation design of a teaching-resource construction study. All rendered text must be Simplified Chinese.
>
> **Upper two-thirds**: a horizontal five-stage main chain of white rounded rectangles with 1.5pt medium-blue #2E6B9E borders, joined by solid 1.5pt dark-grey arrows — 「材料审查」 (clipboard-with-checkmark icon), 「单元切分」 (a block divided by dashed cut lines), 「跨模态关联」 (two rows of dots with crossing connectors), 「四层门控」 (four stacked narrowing bars), 「独立验证」 (magnifier over checklist).
>
> Three exception branches drop below the chain, all dashed: from 「材料审查」 a dashed orange #D95F02 arrow down to a small dashed orange box 「✗ 不入池」 with a tiny floating label 「未过审查」; from both 「跨模态关联」 and 「四层门控」 dashed grey #8EAEC4 arrows converge into a rounded dashed grey box 「⚠ 人工核验队列」 labelled 「属性或证据不全」, which sends a dashed curved arrow back up to 「跨模态关联」; from 「四层门控」 a dashed orange arrow to 「✗ 退回修改」 labelled 「严重错误」, curving left all the way back to 「单元切分」. In the right margin, a pale-blue #5BA0D0 box titled 「数据划分」 lists 「按知识模块留出」「按来源留出」「按设备类型留出」 with small grey subtext 「近重复不跨集合」.
>
> **Bottom third**: a full-width light-grey container with a 1.5pt dark navy #1B3A5C border titled 「统一实验控制」, subtitle 「同一材料 · 同一划分 · 同一人工预算」. Inside, an upper row of four white method boxes 「B0 人工整理」「B1 通用大模型」「B2 文本 RAG」「B3 完整方法」 — only B3 has a thicker 1.8pt emerald #1B9E77 border and a small 「[本方法]」 pill. Beneath them a row of five dashed grey pills reading 「−产业知识」「−课程知识」「−专业属性」「−来源位置」「−质量层」 preceded by the word 「消融：」.
>
> At the very bottom, three borderless columns divided by 1pt grey rules: 「构建层 / 边界 F1 · 覆盖 · 属性错误率」, 「关联层 / Recall@K · MRR · 关系 F1 · 来源定位」, 「质量层 / VRR · 检出率 · 误报率 · 专家盲评」.
>
> White canvas, white fills, colored borders only, 4–6px radius, monochrome thin-line icons. Absolutely no numeric values or scores. No gradients, shadows, 3D, or emojis. Arial: titles 11pt bold, labels 9pt, notes 7.5pt grey. Aspect ratio 3:2.

## 图注预留（不上图）

> 图 2　技术路线与实验验证流程。主链为正向流程，虚线为异常处置与回退路径。B0 为人工整理，B1 为通用大模型直接构建，B2 为仅文本检索增强生成，B3 为本项目完整方法；消融项 −产业知识、−课程知识对应关键科学问题（1），−专业属性、−来源位置对应问题（2），−质量层对应问题（3）。权重与阈值仅在开发集确定，测试集冻结。

---

# F3 · 创新点一：产业—课程联合知识约束下的资源单元构建

**类型**：Module Detail ｜ **优先级**：MUST ｜ **aspect_ratio**：4:3
**落位**：`extraTex/1.3.方案及可行性.tex:20`（$\mathcal{L}_{\mathrm{unit}}$ 公式之后）或 `1.4.特色与创新.tex:10`

## JSON Spec

```json
{
  "diagram_type": "Module Detail — Joint Industry-Curriculum Knowledge Constraint",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "industry_knowledge": "#1B3A5C 1.5pt solid border, white fill",
      "curriculum_knowledge": "#2E6B9E 1.5pt solid border, white fill",
      "scoring_channels": "#5BA0D0 1.2pt solid border, white fill",
      "pending_queue": "#8EAEC4 1.2pt dashed border, white fill",
      "loss_terms": "#D95F02 1.2pt solid border, white fill"
    },
    "flow_arrow_colors": { "main_forward_flow": "#4D4D4D 1.5pt solid", "pending_flow": "#8EAEC4 1.0pt dashed" }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top left",
      "shape": "Rounded container, #1B3A5C 1.5pt border, white fill",
      "exact_title_to_render_inside": "产业任务知识 Kp",
      "icon": "small gear-and-turbine outline icon, monochrome line art",
      "internal_content": {
        "layout": "Four small stacked label chips",
        "row_1": { "exact_text": "任务" },
        "row_2": { "exact_text": "设备 · 工况" },
        "row_3": { "exact_text": "运行参数" },
        "row_4": { "exact_text": "告警条件" }
      },
      "flow": "Solid arrow DOWN into scoring channel row"
    },
    {
      "relative_position": "Top right",
      "shape": "Rounded container, #2E6B9E 1.5pt border, white fill",
      "exact_title_to_render_inside": "课程知识 Kc",
      "icon": "small open-book with node-graph icon, monochrome line art",
      "internal_content": {
        "layout": "Three small stacked label chips",
        "row_1": { "exact_text": "知识点" },
        "row_2": { "exact_text": "能力目标" },
        "row_3": { "exact_text": "先修关系" }
      },
      "flow": "Solid arrow DOWN into scoring channel row"
    },
    {
      "relative_position": "Upper middle, horizontal row of three",
      "shape": "Three small rounded boxes, #5BA0D0 1.2pt border, white fill",
      "internal_content": {
        "layout": "Three parallel channels converging into a ⊕ node",
        "column_1": { "exact_text": "Sp 产业属性", "secondary_note": "λp" },
        "column_2": { "exact_text": "Sc 课程属性", "secondary_note": "λc" },
        "column_3": { "exact_text": "Spc 术语映射", "secondary_note": "λpc" }
      },
      "flow": "Three solid arrows converge into a small circled ⊕ node labelled 「S_kc」"
    },
    {
      "relative_position": "Middle band, full width",
      "shape": "Six chevron segments in a horizontal chain, #2E6B9E 1.2pt border, white fill",
      "exact_title_to_render_inside": "描述模式",
      "internal_content": {
        "layout": "Six connected chevrons left to right",
        "column_1": { "exact_text": "任务" },
        "column_2": { "exact_text": "对象" },
        "column_3": { "exact_text": "条件" },
        "column_4": { "exact_text": "知识点" },
        "column_5": { "exact_text": "片段" },
        "column_6": { "exact_text": "证据位置" }
      }
    },
    {
      "relative_position": "Lower left, 2x2 grid",
      "shape": "Four small boxes, #D95F02 1.2pt border, white fill",
      "exact_title_to_render_inside": "边界损失",
      "internal_content": {
        "layout": "2x2 grid, each cell has a tiny schematic above its label",
        "row_1_col_1": { "exact_text": "L_cover 遗漏", "icon": "tiny icon: a block with one segment missing" },
        "row_1_col_2": { "exact_text": "L_dup 重复", "icon": "tiny icon: two overlapping identical blocks" },
        "row_2_col_1": { "exact_text": "L_split 过切分", "icon": "tiny icon: one block cut into many thin slivers" },
        "row_2_col_2": { "exact_text": "L_attr 属性错配", "icon": "tiny icon: a block with a mismatched tag" }
      }
    },
    {
      "relative_position": "Lower right, vertical comparison strip",
      "shape": "Four stacked condition rows, #5BA0D0 1.2pt border, white fill; bottom row #1B9E77 1.5pt border",
      "exact_title_to_render_inside": "约束条件对照",
      "internal_content": {
        "layout": "Four rows, each with an arrow pointing right to a shared metric column",
        "row_1": { "exact_text": "无知识" },
        "row_2": { "exact_text": "仅 Kp" },
        "row_3": { "exact_text": "仅 Kc" },
        "row_4": { "exact_text": "联合 Kp + Kc", "secondary_note": "[本方法]" }
      },
      "flow": "Four solid arrows RIGHT into a borderless metric column listing 「边界 F1」「知识覆盖」「属性错误率」"
    },
    {
      "relative_position": "Right margin, detached",
      "shape": "Rounded box, #8EAEC4 1.2pt DASHED border, #F7F7F7 fill",
      "exact_title_to_render_inside": "⚠ 待核验队列",
      "internal_content": {
        "layout": "Three stacked lines",
        "row_1": { "exact_text": "术语异名" },
        "row_2": { "exact_text": "粒度差异" },
        "row_3": { "exact_text": "属性冲突" }
      },
      "flow": "Dashed arrow IN from the ⊕ node"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "All boxes WHITE fill with COLORED BORDERS ONLY.",
    "The pending-verification queue MUST use #8EAEC4 dashed border and a ⚠ glyph.",
    "The 联合 Kp + Kc row is the only emerald-bordered condition, marked [本方法].",
    "NO numeric values, NO metric scores, NO bar heights implying results.",
    "Operators rendered as small circled glyphs ⊕ only. Icons monochrome thin line art.",
    "NO emojis, NO 3D, NO gradients, NO shadows."
  ],
  "caption_note": [
    "S_kc = λp·Sp + λc·Sc + λpc·Spc 完整式与权重取值方式",
    "L_unit = L_cover + α·L_dup + β·L_split + γ·L_attr 完整式",
    "λ 与 α/β/γ 均在开发集确定，测试集冻结"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic module detail diagram showing how industry-task knowledge and curriculum knowledge jointly constrain the construction of teaching resource units. All rendered text must be Simplified Chinese.
>
> **Top row, two knowledge sources side by side**: left, a white rounded container with a 1.5pt dark navy #1B3A5C border titled 「产业任务知识 Kp」 with a small monochrome gear-and-wind-turbine icon, holding four small chips 「任务」「设备 · 工况」「运行参数」「告警条件」; right, a container with a 1.5pt medium blue #2E6B9E border titled 「课程知识 Kc」 with a small open-book-with-node-graph icon, holding chips 「知识点」「能力目标」「先修关系」.
>
> **Upper middle**: solid arrows descend from both containers into three parallel pale-blue #5BA0D0 boxes 「Sp 产业属性」「Sc 课程属性」「Spc 术语映射」, each with a tiny italic weight label 「λp」「λc」「λpc」 beneath. The three converge with solid arrows into a small circled **⊕** node labelled 「S_kc」.
>
> **Middle band**: a full-width horizontal chain of six connected chevron segments titled 「描述模式」, reading left to right 「任务」→「对象」→「条件」→「知识点」→「片段」→「证据位置」, medium blue 1.2pt borders.
>
> **Lower left**: a 2×2 grid titled 「边界损失」 of four white boxes with 1.2pt orange #D95F02 borders, each carrying a tiny monochrome schematic above its label — 「L_cover 遗漏」 (a block with one segment missing), 「L_dup 重复」 (two overlapping identical blocks), 「L_split 过切分」 (one block cut into many thin slivers), 「L_attr 属性错配」 (a block with a mismatched tag).
>
> **Lower right**: a vertical comparison strip titled 「约束条件对照」 with four stacked rows 「无知识」「仅 Kp」「仅 Kc」「联合 Kp + Kc」 — only the last has a 1.5pt emerald #1B9E77 border and a small 「[本方法]」 pill. Four solid arrows point right into a borderless metric column listing 「边界 F1」「知识覆盖」「属性错误率」.
>
> **Right margin, detached**: a dashed grey #8EAEC4 box titled 「⚠ 待核验队列」 listing 「术语异名」「粒度差异」「属性冲突」, fed by a dashed arrow from the ⊕ node.
>
> White canvas, white fills, colored borders only, 4–6px radius. No numeric values, no bar heights implying results. Monochrome thin-line icons. No gradients, shadows, 3D, or emojis. Arial: titles 11pt bold, labels 9pt, symbols 7pt italic. Aspect ratio 4:3.

## 图注预留（不上图）

> 图 3　产业—课程联合知识约束下的资源单元构建（创新点一）。联合打分 $S_{\mathrm{kc}}(d_i,k_j)=\lambda_pS_p+\lambda_cS_c+\lambda_{pc}S_{pc}$，单元边界损失 $\mathcal{L}_{\mathrm{unit}}=\mathcal{L}_{\mathrm{cover}}+\alpha\mathcal{L}_{\mathrm{dup}}+\beta\mathcal{L}_{\mathrm{split}}+\gamma\mathcal{L}_{\mathrm{attr}}$。四种约束条件在同一资源范围、同一数据划分和同一人工复核预算下比较，用于检验联合约束的增量作用及其适用边界。

---

# F4 · 创新点二：跨模态证据关联的三重条件闸门

**类型**：Module Detail ｜ **优先级**：MUST ｜ **aspect_ratio**：4:3
**落位**：`extraTex/1.3.方案及可行性.tex:37`（$R(i,j)$ 公式之后）或 `1.4.特色与创新.tex:14`

## JSON Spec

```json
{
  "diagram_type": "Module Detail — Triple-Gate Cross-Modal Evidence Association",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "encoders": "#1B3A5C 1.5pt solid border, white fill",
      "attribute_tags": "#5BA0D0 1.0pt solid border, white fill",
      "gates": "#2E6B9E 1.5pt solid border, white fill",
      "pass_outlet": "#1B9E77 1.5pt solid border, white fill",
      "fail_buckets": "#D95F02 1.2pt DASHED border, white fill",
      "hard_negatives": "#D95F02 1.2pt dashed border, #F7F7F7 fill"
    },
    "flow_arrow_colors": { "main_forward_flow": "#4D4D4D 1.5pt solid", "reject_flow": "#D95F02 1.0pt dashed" }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top row, four modality encoders",
      "shape": "Four rounded boxes, #1B3A5C 1.5pt border, white fill; the fourth DASHED #8EAEC4",
      "internal_content": {
        "layout": "Four side-by-side encoders, each emitting a short horizontal vector bar plus two attached side tags",
        "column_1": { "exact_text": "文本", "icon": "small document-with-lines icon, monochrome" },
        "column_2": { "exact_text": "运行曲线", "icon": "small time-series waveform thumbnail, monochrome" },
        "column_3": { "exact_text": "设备图", "icon": "small turbine-and-panel outline icon, monochrome" },
        "column_4": { "exact_text": "代码 / 案例", "secondary_note": "[扩展]", "shape": "#8EAEC4 dashed border", "icon": "small code-bracket icon, monochrome" }
      },
      "exact_floating_text": "z 保留属性 A 与来源 e",
      "flow": "Solid arrows DOWN into the contrastive alignment bar"
    },
    {
      "relative_position": "Below encoders, thin full-width bar",
      "shape": "Wide flat rounded bar, #5BA0D0 1.2pt border, white fill",
      "exact_text": "对比学习基础表示",
      "secondary_note": "L_align",
      "icon": "small icon: two rows of dots with one matched pair highlighted, monochrome"
    },
    {
      "relative_position": "Center, three serial gates stacked vertically (CORE VISUAL, largest elements)",
      "shape": "Three large rounded gate boxes, #2E6B9E 1.5pt border, white fill, joined top-to-bottom by solid arrows",
      "internal_content": {
        "layout": "Three vertically serial gates; each gate has a right-side dashed reject exit",
        "row_1": { "exact_title_to_render_inside": "① 语义门", "exact_text": "sim(z_i, z_j)", "secondary_note": "η_s" },
        "row_2": { "exact_title_to_render_inside": "② 专业条件门", "exact_text": "对象 · 变量 · 单位 · 工况 · 时窗", "secondary_note": "C_A　η_a" },
        "row_3": { "exact_title_to_render_inside": "③ 证据位置门", "exact_text": "来源位置 + 关系类别", "secondary_note": "C_E · C_R　η_e η_r" }
      },
      "success_branch": "Solid emerald arrow DOWN from gate ③ to the pass outlet",
      "failure_branch": "Dashed orange arrows RIGHT from gates ② and ③ into the failure buckets"
    },
    {
      "relative_position": "Bottom center, below gate ③",
      "shape": "Rounded box, #1B9E77 1.5pt solid border, white fill",
      "exact_text": "✓ 写入资源单元 u",
      "exact_floating_text": "三门全通过"
    },
    {
      "relative_position": "Right side, two stacked failure buckets",
      "shape": "Two rounded boxes, #D95F02 1.2pt DASHED border, white fill, diagonal hatch fill",
      "internal_content": {
        "row_1": { "exact_text": "✗ 专业条件错配" },
        "row_2": { "exact_text": "✗ 来源不可核查" }
      }
    },
    {
      "relative_position": "Lower right, detached example box",
      "shape": "Rounded box, #D95F02 1.2pt dashed border, #F7F7F7 fill",
      "exact_title_to_render_inside": "困难负例",
      "internal_content": {
        "layout": "Two example rows, each with a small paired-thumbnail sketch and a ✗ glyph",
        "row_1": { "exact_text": "✗ 同为功率曲线\\n采样 15min vs 1h", "icon": "two tiny waveform thumbnails side by side, one denser" },
        "row_2": { "exact_text": "✗ 同一变量\\n单位 kW vs MW", "icon": "two tiny axis-label chips side by side" }
      }
    },
    {
      "relative_position": "Left margin, vertical strip",
      "shape": "Five small pills, #5BA0D0 1.0pt border, white fill",
      "exact_title_to_render_inside": "关系类型",
      "internal_content": {
        "row_1": { "exact_text": "解释" },
        "row_2": { "exact_text": "实例" },
        "row_3": { "exact_text": "计算 · 实验" },
        "row_4": { "exact_text": "对照" },
        "row_5": { "exact_text": "出处支持" }
      }
    },
    {
      "relative_position": "Very bottom, borderless metric row",
      "shape": "Borderless text row separated by 1.0pt #CCCCCC dividers",
      "exact_text": "Recall@1 · Recall@5 　 MRR 　 关系 F1 　 来源定位准确率 　 错配率"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "The three serial gates are the LARGEST elements and must dominate the composition.",
    "Pass path: solid emerald #1B9E77 border + ✓ glyph. Fail path: dashed orange #D95F02 border + ✗ glyph + diagonal hatch. NEVER color alone.",
    "Attribute tags A and source tags e must stay visibly ATTACHED to each encoder output, not merged into the vector bar.",
    "Extended modality 代码/案例 uses #8EAEC4 dashed border with [扩展] pill.",
    "NO numeric values, NO accuracy scores. The hard-negative examples show only unit/frequency labels, never results.",
    "Icons monochrome thin line art. NO emojis, NO 3D, NO gradients, NO shadows."
  ],
  "caption_note": [
    "R(i,j) = η_s·sim + η_a·C_A + η_e·C_E + η_r·C_R 完整式",
    "L_align 对比学习损失完整式与温度参数 τ",
    "五类关系的判定准则与困难负例构造方式"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic module detail diagram showing a triple-gate mechanism that admits a cross-modal association into a teaching resource unit only when semantic similarity, professional conditions and source evidence are all satisfied. All rendered text must be Simplified Chinese.
>
> **Top row**: four modality encoders as white rounded boxes with 1.5pt dark navy #1B3A5C borders — 「文本」 (document icon), 「运行曲线」 (tiny time-series waveform thumbnail), 「设备图」 (turbine-and-panel outline icon), and 「代码 / 案例」 rendered with a 1.2pt **dashed** grey #8EAEC4 border plus a small 「[扩展]」 pill. Each encoder emits a short horizontal vector bar with **two small tags visibly clipped to its side** labelled 「A」 and 「e」, and a floating grey note reads 「z 保留属性 A 与来源 e」. Below them a thin full-width pale-blue bar 「对比学习基础表示」 with an italic 「L_align」.
>
> **Center — the dominant visual**: three large serial gate boxes stacked vertically with 1.5pt medium blue #2E6B9E borders, joined top-to-bottom by solid arrows. 「① 语义门」 with 「sim(z_i, z_j)」 and 「η_s」; 「② 专业条件门」 with 「对象 · 变量 · 单位 · 工况 · 时窗」 and 「C_A　η_a」; 「③ 证据位置门」 with 「来源位置 + 关系类别」 and 「C_E · C_R　η_e η_r」. Gates ② and ③ each shed a **dashed orange** #D95F02 arrow to the right.
>
> **Right side**: two dashed orange boxes with light diagonal hatching — 「✗ 专业条件错配」 and 「✗ 来源不可核查」. Below them a detached dashed orange box titled 「困难负例」 with two rows, each carrying a tiny paired thumbnail and a ✗ — 「同为功率曲线 / 采样 15min vs 1h」 (two waveform thumbnails, one denser) and 「同一变量 / 单位 kW vs MW」 (two axis-label chips).
>
> **Bottom center**: a solid emerald #1B9E77 box 「✓ 写入资源单元 u」 with floating label 「三门全通过」. **Left margin**: five small pale-blue pills titled 「关系类型」 — 「解释」「实例」「计算 · 实验」「对照」「出处支持」. **Very bottom**: a borderless divided row 「Recall@1 · Recall@5　MRR　关系 F1　来源定位准确率　错配率」.
>
> White canvas, white fills, colored borders only, 4–6px radius, monochrome thin-line icons. No numeric values or scores anywhere. No gradients, shadows, 3D, or emojis. Arial: titles 11pt bold, labels 9pt, symbols 7pt italic. Aspect ratio 4:3.

## 图注预留（不上图）

> 图 4　面向专业条件错配的跨模态证据关联（创新点二）。关系评分 $R(i,j)=\eta_s\mathrm{sim}(\boldsymbol{z}_i,\boldsymbol{z}_j)+\eta_aC_A+\eta_eC_E+\eta_rC_R$，其中 $C_A,C_E,C_R$ 分别校验专业属性、来源位置与关系类别。候选关系需同时满足语义相关、专业条件相容和证据位置可核查三项条件方可写入资源单元；仅满足语义相似的候选按失效类型分别记入"专业条件错配"或"来源不可核查"。困难负例以变量、单位、工况和时序错配构造。

---

# F5 · 创新点三：四层质量门控与 VRR 独立效度验证

**类型**：Module Detail ｜ **优先级**：STRONG ｜ **aspect_ratio**：4:3
**落位**：`extraTex/1.3.方案及可行性.tex:55`（VRR 公式之后）或 `1.4.特色与创新.tex:18`

## JSON Spec

```json
{
  "diagram_type": "Module Detail — Four-Layer Quality Gating with Independent Validity Check",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "evidence_precheck": "#5BA0D0 1.2pt solid border, white fill",
      "gate_layers": "#2E6B9E 1.5pt solid border, white fill",
      "penalty": "#D95F02 1.2pt solid border, white fill",
      "pass_outlet": "#1B9E77 1.5pt solid border, white fill",
      "reject_outlet": "#D95F02 1.2pt dashed border, white fill",
      "independent_zone": "#1B3A5C 1.5pt solid border, #F7F7F7 fill"
    },
    "flow_arrow_colors": { "main_forward_flow": "#4D4D4D 1.5pt solid", "manual_check": "#8EAEC4 1.0pt dashed" }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top left",
      "shape": "Rounded box, #5BA0D0 1.2pt border, white fill",
      "exact_title_to_render_inside": "证据支持度",
      "exact_text": "文本 · 其他模态 · 知识关系",
      "secondary_note": "G(a,e)",
      "icon": "small icon: a claim box linked by a line to a source-location pin, monochrome",
      "failure_branch": "Dashed grey arrow RIGHT to 人工核验 when below threshold, labelled 「G < θg」"
    },
    {
      "relative_position": "Top left, beside evidence box",
      "shape": "Small rounded box, #8EAEC4 1.2pt DASHED border, #F7F7F7 fill",
      "exact_text": "⚠ 人工核验"
    },
    {
      "relative_position": "Center left, four vertically stacked gate layers (CORE VISUAL)",
      "shape": "Four stacked rounded bars, #2E6B9E 1.5pt border, white fill, joined by solid downward arrows",
      "exact_title_to_render_inside": "四层质量门控",
      "internal_content": {
        "layout": "Four layers top to bottom, each with a left label, a middle check target and a right weight symbol",
        "row_1": { "exact_text": "内容层 · 事实与参数", "secondary_note": "w_con", "icon": "small magnifier-over-number icon, monochrome" },
        "row_2": { "exact_text": "课程层 · 知识点与目标", "secondary_note": "w_cur", "icon": "small open-book icon, monochrome" },
        "row_3": { "exact_text": "模态层 · 对象与条件", "secondary_note": "w_mod", "icon": "small two-linked-frames icon, monochrome" },
        "row_4": { "exact_text": "证据层 · 原始出处", "secondary_note": "w_evi", "icon": "small location-pin-on-document icon, monochrome" }
      },
      "flow": "Solid arrow DOWN to the decision diamond"
    },
    {
      "relative_position": "Right of the gate stack",
      "shape": "Rounded box, #D95F02 1.2pt border, white fill",
      "exact_title_to_render_inside": "惩罚项",
      "secondary_note": "−μP(u)",
      "internal_content": {
        "row_1": { "exact_text": "参数矛盾" },
        "row_2": { "exact_text": "来源不可追溯" },
        "row_3": { "exact_text": "未授权 · 隐私风险" }
      },
      "flow": "Solid arrow LEFT into the decision diamond"
    },
    {
      "relative_position": "Below gate stack, centered",
      "shape": "Diamond, #1B3A5C 1.5pt border, white fill",
      "exact_text": "Q(u) ≥ θq ?\\n字段完整 · 无严重错误",
      "branch_yes": "Solid emerald arrow DOWN-LEFT to 「✓ 通过」",
      "branch_no": "Dashed orange arrow DOWN-RIGHT to 「✗ 拒绝并留原因」"
    },
    {
      "relative_position": "Bottom left of diamond",
      "shape": "Rounded box, #1B9E77 1.5pt solid border, white fill",
      "exact_text": "✓ 通过 · 进入资源包"
    },
    {
      "relative_position": "Bottom right of diamond",
      "shape": "Rounded box, #D95F02 1.2pt DASHED border, white fill, diagonal hatch",
      "exact_text": "✗ 拒绝并留原因"
    },
    {
      "relative_position": "Bottom center, beneath the pass outlet",
      "shape": "Wide flat bar, #1B9E77 1.5pt border, white fill",
      "exact_text": "主指标 VRR　有效资源单元通过率"
    },
    {
      "relative_position": "Right third, separated by a THICK VERTICAL DASHED WALL",
      "shape": "Tall rounded container, #1B3A5C 1.5pt border, #F7F7F7 fill",
      "exact_title_to_render_inside": "独立效度验证",
      "exact_floating_text": "量表制定者不参与评分 · 评分隐藏方法条件",
      "internal_content": {
        "layout": "Three stacked sub-boxes over a metric footer",
        "row_1": { "exact_text": "专家盲评\\n≥3 名未参与构建教师 · 5 维量表", "icon": "small three-person-outline icon, monochrome" },
        "row_2": { "exact_text": "跨来源留出", "icon": "small split-dataset icon, monochrome" },
        "row_3": { "exact_text": "人工修订时间", "icon": "small stopwatch icon, monochrome" },
        "row_4": { "exact_text": "Krippendorff's α · 错误检出率 · 误报率" }
      },
      "flow": "Solid arrow LEFT from VRR bar crossing the dashed wall, labelled 「比对」"
    },
    {
      "relative_position": "Very bottom, borderless note row",
      "shape": "Borderless small grey text",
      "exact_text": "权重与阈值仅在开发集确定 · 测试集冻结　｜　服务资源验收，不评价学习效果"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "A THICK VERTICAL DASHED WALL must visibly separate the automatic gating zone (left) from the independent validation zone (right). This separation is the semantic core of the figure.",
    "Only ONE arrow may cross the wall, labelled 「比对」.",
    "Pass = solid emerald border + ✓; reject = dashed orange border + ✗ + diagonal hatch. NEVER color alone.",
    "NO numeric values, NO thresholds with numbers, NO scores. θq, θg, w_* remain symbolic.",
    "Icons monochrome thin line art. NO emojis, NO 3D, NO gradients, NO shadows."
  ],
  "caption_note": [
    "G(a,e) = ρt·Gt + ρv·Gv + ρk·Gk 完整式",
    "Q(u) = w_con·q_con + w_cur·q_cur + w_mod·q_mod + w_evi·q_evi − μP(u) 完整式",
    "VRR 指示函数定义与五维专家盲评量表条目"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic module detail diagram showing a four-layer automatic quality gate for teaching resource units, deliberately separated from an independent expert validation zone. All rendered text must be Simplified Chinese.
>
> **Composition: two zones divided by a thick vertical dashed wall running the full height of the figure** — this separation is the semantic core and must be unmistakable.
>
> **Left zone (automatic gating).** Top-left: a pale-blue #5BA0D0 box 「证据支持度」 with subtext 「文本 · 其他模态 · 知识关系」, italic 「G(a,e)」 and a small claim-linked-to-source-pin icon; a dashed grey arrow labelled 「G < θg」 exits right to a small dashed grey box 「⚠ 人工核验」. Below, the dominant element: four stacked rounded bars with 1.5pt medium blue #2E6B9E borders titled 「四层质量门控」, joined by solid downward arrows — 「内容层 · 事实与参数」 (magnifier-over-number icon, 「w_con」), 「课程层 · 知识点与目标」 (open-book icon, 「w_cur」), 「模态层 · 对象与条件」 (two-linked-frames icon, 「w_mod」), 「证据层 · 原始出处」 (location-pin-on-document icon, 「w_evi」). To their right, an orange #D95F02 box 「惩罚项」 with italic 「−μP(u)」 listing 「参数矛盾」「来源不可追溯」「未授权 · 隐私风险」, feeding left into a decision diamond with 1.5pt dark navy border reading 「Q(u) ≥ θq ? / 字段完整 · 无严重错误」. From the diamond a solid emerald arrow goes down-left to 「✓ 通过 · 进入资源包」 (emerald border) and a dashed orange arrow down-right to 「✗ 拒绝并留原因」 (dashed orange border with light diagonal hatching). Beneath, a wide emerald bar 「主指标 VRR　有效资源单元通过率」.
>
> **Right zone (independent validation).** A tall light-grey container with a 1.5pt dark navy border titled 「独立效度验证」, holding 「专家盲评 / ≥3 名未参与构建教师 · 5 维量表」 (three-person-outline icon), 「跨来源留出」 (split-dataset icon), 「人工修订时间」 (stopwatch icon), and a footer line 「Krippendorff's α · 错误检出率 · 误报率」. A floating grey note above reads 「量表制定者不参与评分 · 评分隐藏方法条件」. Exactly **one** solid arrow crosses the dashed wall from the VRR bar, labelled 「比对」.
>
> Bottom borderless grey note: 「权重与阈值仅在开发集确定 · 测试集冻结 ｜ 服务资源验收，不评价学习效果」.
>
> White canvas, white fills, colored borders only, 4–6px radius, monochrome thin-line icons. All thresholds stay symbolic — no numeric values anywhere. No gradients, shadows, 3D, or emojis. Arial: titles 11pt bold, labels 9pt, symbols 7pt italic. Aspect ratio 4:3.

## 图注预留（不上图）

> 图 5　资源内在质量的四层门控与独立效度验证（创新点三）。证据支持度 $G(a,e)=\rho_tG_t+\rho_vG_v+\rho_kG_k$，低于 $\theta_g$ 的断言进入人工核验；四层质量综合 $Q(u)=w_{\mathrm{con}}q_{\mathrm{con}}+w_{\mathrm{cur}}q_{\mathrm{cur}}+w_{\mathrm{mod}}q_{\mathrm{mod}}+w_{\mathrm{evi}}q_{\mathrm{evi}}-\mu P(u)$。虚线墙右侧的专家盲评与左侧自动门控在设计上相互独立：量表制定者不参与正式评分，评分时隐藏方法条件。VRR 仅回答资源单元是否具备进入资源包的内在条件，不回答学生学习效果。

---

# F6 · 对照与消融实验设计矩阵

**类型**：Comparison / Ablation ｜ **优先级**：NICE ｜ **aspect_ratio**：16:9
**落位**：`extraTex/1.3.方案及可行性.tex:67`（技术路线与实验手段末尾）

## JSON Spec

```json
{
  "diagram_type": "Comparison / Ablation Experimental Design Matrix",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "baseline_rows": "#2E6B9E 1.2pt solid border, white fill",
      "ours_row": "#1B9E77 1.8pt solid border, #F7F7F7 fill",
      "ablation_rows": "#8EAEC4 1.2pt DASHED border, white fill",
      "column_headers": "#1B3A5C 1.5pt bottom rule, white fill"
    },
    "flow_arrow_colors": { "mapping_arrow": "#5BA0D0 1.0pt solid with small head" }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top, three column-group headers",
      "shape": "Three header cells with #1B3A5C 1.5pt bottom rules",
      "internal_content": {
        "column_1": { "exact_header": "构建层", "exact_text": "边界 F1 · 覆盖 · 重复 · 属性错误" },
        "column_2": { "exact_header": "关联层", "exact_text": "Recall@K · MRR · 关系 F1 · 来源定位" },
        "column_3": { "exact_header": "质量层", "exact_text": "VRR · 检出率 · 误报率 · 盲评" }
      }
    },
    {
      "relative_position": "Upper block, four baseline rows",
      "shape": "Four row bands, #2E6B9E 1.2pt border, white fill; fourth row #1B9E77 1.8pt border with #F7F7F7 fill",
      "exact_title_to_render_inside": "对照方法",
      "internal_content": {
        "row_1": { "exact_label": "B0 人工整理", "exact_text": "✓  ✓  ✓" },
        "row_2": { "exact_label": "B1 通用大模型", "exact_text": "✓  ✓  ✓" },
        "row_3": { "exact_label": "B2 文本 RAG", "exact_text": "✓  ✓  ✓" },
        "row_4": { "exact_label": "B3 完整方法", "secondary_note": "[本方法]", "exact_text": "✓  ✓  ✓" }
      }
    },
    {
      "relative_position": "Lower block, five ablation rows",
      "shape": "Five row bands, #8EAEC4 1.2pt DASHED border, white fill",
      "exact_title_to_render_inside": "逐项消融",
      "internal_content": {
        "row_1": { "exact_label": "− 产业知识", "exact_text": "✓  ○  ○" },
        "row_2": { "exact_label": "− 课程知识", "exact_text": "✓  ○  ○" },
        "row_3": { "exact_label": "− 专业属性", "exact_text": "○  ✓  ○" },
        "row_4": { "exact_label": "− 来源位置", "exact_text": "○  ✓  ✓" },
        "row_5": { "exact_label": "− 质量层", "exact_text": "○  ○  ✓" }
      }
    },
    {
      "relative_position": "Right margin, three grouped mapping brackets",
      "shape": "Three curly brackets with #5BA0D0 1.0pt arrows pointing right to small labels",
      "internal_content": {
        "row_1": { "exact_text": "→ 关键科学问题（1）", "exact_floating_text": "覆盖 − 产业知识 / − 课程知识" },
        "row_2": { "exact_text": "→ 关键科学问题（2）", "exact_floating_text": "覆盖 − 专业属性 / − 来源位置" },
        "row_3": { "exact_text": "→ 关键科学问题（3）", "exact_floating_text": "覆盖 − 质量层" }
      }
    },
    {
      "relative_position": "Bottom left, legend",
      "shape": "Borderless legend row",
      "exact_text": "✓ 主要观测　○ 次要观测　空 未设置　（单元格不填数值）"
    },
    {
      "relative_position": "Bottom, full-width discipline bar",
      "shape": "Wide flat bar, #8EAEC4 1.0pt dashed border, #F7F7F7 fill",
      "exact_text": "留出策略：知识模块 · 来源 · 设备类型　｜　评分者不参与规则设计 · 评分隐藏方法条件 · 近重复不跨集合"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "CRITICAL: matrix cells contain ONLY the glyphs ✓ ○ or blank. Absolutely NO numbers, NO percentages, NO bar lengths, NO color-graded heat cells. This is an experimental DESIGN matrix, not a results table.",
    "B3 完整方法 is the only emerald-bordered row with light grey fill and a [本方法] pill.",
    "Ablation rows use #8EAEC4 dashed borders to distinguish them from baseline rows.",
    "NO emojis, NO 3D, NO gradients, NO shadows. Flat vector only."
  ],
  "caption_note": [
    "各基线的具体实现与预算设置",
    "消融项与科学问题的逐项对应说明",
    "留出集划分的具体规则"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic comparison diagram showing the experimental **design** matrix (not results) of a teaching-resource construction study. All rendered text must be Simplified Chinese.
>
> A clean tabular layout, nine rows by three column groups, on a white canvas. **Column headers** across the top, each underlined by a 1.5pt dark navy #1B3A5C rule: 「构建层 / 边界 F1 · 覆盖 · 重复 · 属性错误」, 「关联层 / Recall@K · MRR · 关系 F1 · 来源定位」, 「质量层 / VRR · 检出率 · 误报率 · 盲评」.
>
> **Upper block, labelled 「对照方法」**: four horizontal row bands with 1.2pt medium blue #2E6B9E borders and white fill — 「B0 人工整理」, 「B1 通用大模型」, 「B2 文本 RAG」, and 「B3 完整方法」. The B3 row alone carries a thicker 1.8pt emerald #1B9E77 border, a very light grey #F7F7F7 fill and a small 「[本方法]」 pill at its right end.
>
> **Lower block, labelled 「逐项消融」**: five row bands with 1.2pt **dashed** grey #8EAEC4 borders — 「− 产业知识」, 「− 课程知识」, 「− 专业属性」, 「− 来源位置」, 「− 质量层」.
>
> Every matrix cell contains **only** a small glyph: a green ✓, a grey ○, or nothing at all. **No numbers, no percentages, no bar lengths, no heat shading anywhere** — this is a design matrix, not a results table.
>
> **Right margin**: three pale-blue #5BA0D0 curly brackets group the ablation rows and point right with thin arrows to labels 「→ 关键科学问题（1）」 (bracketing − 产业知识 and − 课程知识), 「→ 关键科学问题（2）」 (bracketing − 专业属性 and − 来源位置), 「→ 关键科学问题（3）」 (bracketing − 质量层).
>
> **Bottom left**, a borderless legend: 「✓ 主要观测　○ 次要观测　空 未设置　（单元格不填数值）」. **Bottom**, a full-width flat bar with a 1pt dashed grey border and light grey fill: 「留出策略：知识模块 · 来源 · 设备类型 ｜ 评分者不参与规则设计 · 评分隐藏方法条件 · 近重复不跨集合」.
>
> Generous row spacing, consistent left-aligned row labels, thin 1pt grey column dividers. White fills, colored borders only. No gradients, shadows, 3D, or emojis. Arial: headers 10pt bold, row labels 9pt, glyphs 9pt, notes 7.5pt grey. Aspect ratio 16:9.

## 图注预留（不上图）

> 图 6　对照与消融实验设计矩阵。表中仅标注各条件下的主要与次要观测指标，**不含任何实验结果数值**。B0–B3 在同一资源范围、同一数据划分和同一人工复核预算下比较；五项消融分别对应三个关键科学问题，用于检验各约束成分是否具有可反证的增量作用。测试集按知识模块、材料来源或设备类型留出，近重复材料不跨集合。

---

# F7 · 两年度研究计划与里程碑

**类型**：Timeline / Gantt ｜ **优先级**：NICE ｜ **aspect_ratio**：16:9
**落位**：`extraTex/1.5.研究计划.tex:12`（第二阶段段落之后、`\subsubsection{预期研究结果}` 之前）

## JSON Spec

```json
{
  "diagram_type": "Two-Year Research Plan Timeline with Milestones",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column)",
    "font_family": "Arial, Helvetica, sans-serif",
    "font_hierarchy": { "title": "10-12pt bold", "primary_label": "8-9pt regular", "secondary_note": "7-8pt regular", "tensor_shape": "6-7pt italic" },
    "stroke_hierarchy": { "container_border": "1.5pt solid", "internal_divider": "1.0pt solid", "flow_arrow": "1.5pt solid with 4px head", "feedback_arrow": "1.0pt dashed" }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "stage_one_bars": "#2E6B9E 1.2pt solid border, white fill",
      "stage_two_bars": "#1B3A5C 1.2pt solid border, white fill",
      "milestone": "#1B9E77 1.8pt solid border, white fill",
      "deliverables": "#5BA0D0 1.0pt solid border, #F7F7F7 fill",
      "downgrade_lane": "#8EAEC4 1.2pt DASHED border, #F7F7F7 fill"
    },
    "flow_arrow_colors": { "timeline_axis": "#4D4D4D 1.5pt solid horizontal axis" }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top, horizontal time axis",
      "shape": "Horizontal axis line, #4D4D4D 1.5pt, split into two labelled halves by a vertical divider",
      "internal_content": {
        "column_1": { "exact_header": "第一阶段", "exact_text": "第 1–12 个月" },
        "column_2": { "exact_header": "第二阶段", "exact_text": "第 13–24 个月" }
      },
      "secondary_note": "具体时间节点以立项通知书为准"
    },
    {
      "relative_position": "Upper band, left half, six staggered task bars",
      "shape": "Six horizontal rounded bars, #2E6B9E 1.2pt border, white fill",
      "internal_content": {
        "row_1": { "exact_text": "来源登记与授权审查" },
        "row_2": { "exact_text": "知识结构与单元模式" },
        "row_3": { "exact_text": "三类核心模态解析" },
        "row_4": { "exact_text": "基线 B0 / B1 / B2 搭建" },
        "row_5": { "exact_text": "标注规范制定" },
        "row_6": { "exact_text": "开发集预实验" }
      }
    },
    {
      "relative_position": "Center, at the month-12 boundary",
      "shape": "Large diamond milestone marker, #1B9E77 1.8pt border, white fill",
      "exact_text": "冻结\\n指标 · 划分 · 盲评量表",
      "icon": "small padlock-free anchor icon: a downward pin marker, monochrome"
    },
    {
      "relative_position": "Upper band, right half, six staggered task bars",
      "shape": "Six horizontal rounded bars, #1B3A5C 1.2pt border, white fill",
      "internal_content": {
        "row_1": { "exact_text": "跨模态关联方法完善" },
        "row_2": { "exact_text": "四层质量门控" },
        "row_3": { "exact_text": "对照 · 消融 · 跨来源留出" },
        "row_4": { "exact_text": "独立专家盲评" },
        "row_5": { "exact_text": "分层误差分析" },
        "row_6": { "exact_text": "本地原型迭代" }
      }
    },
    {
      "relative_position": "Middle band, two deliverable panels under each stage",
      "shape": "Two wide flat panels, #5BA0D0 1.0pt border, #F7F7F7 fill",
      "internal_content": {
        "column_1": { "exact_header": "阶段一验收物", "exact_text": "合规清单 · 元数据卡 · 标注规范 · 开发集划分 · 可复现基线" },
        "column_2": { "exact_header": "阶段二验收物", "exact_text": "冻结测试配置 · B0–B3 比较 · 分层误差分析 · 盲评一致性 · 质量报告" }
      }
    },
    {
      "relative_position": "Bottom, full-width dashed lane",
      "shape": "Wide rounded lane, #8EAEC4 1.2pt DASHED border, #F7F7F7 fill",
      "exact_title_to_render_inside": "降级与退出路径",
      "internal_content": {
        "layout": "Four small dashed pills in a row",
        "column_1": { "exact_text": "⚠ 材料退出" },
        "column_2": { "exact_text": "⚠ 约束简化" },
        "column_3": { "exact_text": "⚠ 原型降级为自动初筛—人工复核" },
        "column_4": { "exact_text": "⚠ 负结果如实报告" }
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. All on-figure text is Simplified Chinese.",
    "The month-12 freeze milestone is the single emerald element and must be the visual focal point of the timeline.",
    "The downgrade lane MUST use #8EAEC4 dashed borders with ⚠ glyphs — dual encoding, never color alone.",
    "Task bars carry NO percentage-complete fills and NO numeric durations beyond the two stage labels.",
    "NO emojis, NO 3D, NO gradients, NO shadows. Flat vector only."
  ],
  "caption_note": [
    "各任务的具体交付物与负责分工",
    "阶段性验收的详细条目",
    "项目实施期按两年安排，具体时间节点以立项通知书为准"
  ]
}
```

## Image Prompt（英文，出图用）

> Flat vector academic Gantt-style timeline diagram showing a two-year research plan with a central freeze milestone and an explicit downgrade lane. All rendered text must be Simplified Chinese.
>
> **Top**: a horizontal 1.5pt dark-grey time axis split into two equal halves by a vertical divider, labelled 「第一阶段 / 第 1–12 个月」 on the left and 「第二阶段 / 第 13–24 个月」 on the right, with a small grey note at the far right 「具体时间节点以立项通知书为准」.
>
> **Left half**: six staggered horizontal rounded task bars with 1.2pt medium blue #2E6B9E borders and white fill, each label left-aligned inside its bar — 「来源登记与授权审查」, 「知识结构与单元模式」, 「三类核心模态解析」, 「基线 B0 / B1 / B2 搭建」, 「标注规范制定」, 「开发集预实验」. The bars start at staggered offsets and vary in length to suggest sequencing, but carry no percentage fills and no numeric durations.
>
> **Center, straddling the month-12 boundary**: a large diamond milestone marker with a 1.8pt emerald #1B9E77 border and white fill, containing 「冻结 / 指标 · 划分 · 盲评量表」, with a small monochrome downward pin marker. This is the visual focal point of the whole figure and the only emerald element.
>
> **Right half**: six staggered task bars with 1.2pt dark navy #1B3A5C borders — 「跨模态关联方法完善」, 「四层质量门控」, 「对照 · 消融 · 跨来源留出」, 「独立专家盲评」, 「分层误差分析」, 「本地原型迭代」.
>
> **Middle band**: two wide flat panels with 1pt pale-blue #5BA0D0 borders and very light grey fill, one under each stage — 「阶段一验收物 / 合规清单 · 元数据卡 · 标注规范 · 开发集划分 · 可复现基线」 and 「阶段二验收物 / 冻结测试配置 · B0–B3 比较 · 分层误差分析 · 盲评一致性 · 质量报告」.
>
> **Bottom**: a full-width rounded lane with a 1.2pt **dashed** grey #8EAEC4 border and light grey fill, titled 「降级与退出路径」, holding four small dashed pills each prefixed by a ⚠ glyph — 「材料退出」, 「约束简化」, 「原型降级为自动初筛—人工复核」, 「负结果如实报告」.
>
> White canvas, white bar fills, colored borders only, 4–6px radius, generous vertical rhythm, thin 1pt grey gridlines behind the bars. No gradients, shadows, 3D, or emojis. Arial: stage headers 11pt bold, bar labels 9pt, notes 7.5pt grey. Aspect ratio 16:9.

## 图注预留（不上图）

> 图 7　两年度研究计划与里程碑。第 12 个月的冻结节点标志主要指标、数据划分和专家盲评量表在开发集上确定后不再调整，测试集配置随之冻结。底部虚线泳道为预设的降级与退出路径：材料授权、专家安排或方法增益未达预期时，按该路径压缩规模而不降低来源与合规要求，并如实报告负结果。项目实施期按两年安排，具体时间节点以立项通知书为准。

---

# 交付校验清单

| 校验项 | F1 | F2 | F3 | F4 | F5 | F6 | F7 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 所有可见文字锁在 `exact_*` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| aspect_ratio 与 Figure Plan 一致 | 16:9 | 3:2 | 4:3 | 4:3 | 4:3 | 16:9 | 16:9 |
| `physical_spec_and_typography` 块 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Text Budget（标题 ≤8 汉字） | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 白底 + 彩色描边 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ≤3 色相（蓝阶算 1） | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 每个主模块有图标/视觉锚 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| 通过/失效双编码（✓✗ + 线型） | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 扩展模态虚线降级 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ |
| **零虚构数值** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 负面指令（无 emoji/3D/锁火闪电） | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| caption 预留（公式/参数下沉） | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**F6 无图标**：矩阵类图以网格对齐为视觉锚，加图标反而干扰读表，属有意省略。

## 生图后必须人工核验的三处

1. **中文字形**：`Krippendorff's α`、`Recall@K`、下标 `w_con / q_evi / η_s / λ_pc` 最易被图像模型写错或漏写。
2. **F5 虚线墙**：若模型把左右两区画通或多画一条跨墙箭头，本图的核心论证（自动门控与专家评价相互独立）即失效，必须重出。
3. **F6 单元格**：确认没有任何数字、百分比或热力填充混入——一旦出现即构成虚构实验结果。
