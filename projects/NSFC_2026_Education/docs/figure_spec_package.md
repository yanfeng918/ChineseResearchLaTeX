# NSFC 2026 教育方向申报书 — 配色与图规格包（Figure Spec Package）

> 生成日期：2026-08-14
> 关联技能：`academic-figure-color-expert`（配色决策）、`academic-figure-prompt`（JSON 图规格 + 图像提示词，classic 风格族）
> 上游输入：Figure Plan（8 图：4 must / 2 strong / 2 nice）

---

## 0. Palette Decision（配色决策，color-expert 输出契约）

### 0.1 决策清单

1. **风格族**：classic（经典学术 box-border；NSFC 正式申报书，拒绝 pastel 柔彩）
2. **硬约束命中**：色盲友好（默认必须）；F1/F2/F6 等 ≥4 模块 → 单色系规则
3. **图型偏好**：Framework(≥4) → Nature Blue；Module Detail → Blue Monochrome（与 Nature Blue 同族）；Comparison → 灰底 + 单一强调色；Data/Motivation → 双态对比色
4. **venue / domain**：NSFC 地区科学基金申请书（非论文 venue，记 None）；多模态学习 / 教育资源构建 / 新能源工程教育
5. **primary / alternate**：Nature Blue（主）/ Okabe-Ito（备）
6. **hex 来源**：`academic-figure-color-expert/references/palettes.md` §12 Nature Blue + 语义强调色
7. **决策分支**：`scene`（classic 家族 + ≥4 模块硬约束 + 工程科技克制风）

### 0.2 主色板（跨图一致，全文只用这一套）

| 角色 | hex | 用途 |
|------|-----|------|
| primary | `#1B3A5C` | 深海军蓝：输入/数据、容器主边框 |
| secondary | `#2E6B9E` | 中蓝：知识/方法模块 |
| tertiary | `#5BA0D0` | 浅蓝：关联/输出模块 |
| gray | `#8EAEC4` | 浅灰蓝：分组底纹、分隔 |
| accent-coral | `#D95F02` | 珊瑚橙：质量门控/拒绝/错误/错配（稀疏使用） |
| accent-emerald | `#1B9E77` | 翡翠绿：通过/输出/正确关联（稀疏使用） |
| frozen | `#616161` | 石板灰：待核验/冻结/基线 |
| text | `#333333` | 正文文字 |
| fill | `#FFFFFF` | 画布/盒体填充 |
| section_bg | `#F7F7F7` | 区域分组底纹 |
| border | `#CCCCCC` | 普通边框 |
| arrow | `#4D4D4D` | 箭头/连线 |

**备选色板（Alternate）**：Okabe-Ito —— primary `#0072B2`、secondary `#E69F00`、tertiary `#009E73`、text `#333333`、fill `#FFFFFF`、section_bg `#F7F7F7`、border `#CCCCCC`、arrow `#4D4D4D`。仅在需要更强多色区分（如 F2 动机图多材料对比）时启用，且仍 ≤3 色。

### 0.3 语义色绑定（Semantic Color Binding，跨图统一）

| 功能角色 | 绑定 hex | 本申报书含义 |
|----------|----------|--------------|
| Input / Data | `#1B3A5C` | 输入材料、资源片段、数据模态 |
| Backbone / Knowledge | `#2E6B9E` | 产业知识 Kp、课程知识 Kc、方法模块 |
| Association | `#5BA0D0` | 跨模态关联、关系评分、来源位置 |
| Loss / Gate / Reject | `#D95F02` | 质量门控、拒绝、错配、错误类型 |
| Output / Pass | `#1B9E77` | 资源包、通过、正确关联、VRR |
| Frozen / Pending | `#616161` | 待核验队列、基线 B0–B2、消融项 |

### 0.4 可访问性与原因

- **色盲友好**：蓝/珊瑚/绿在 deuteranopia/protanopia 下可区分；所有类别**双重编码**（颜色 + 图标/线型/虚实边框/pill 标签），不单靠色相。
- **黑白打印**：主色板为单色系 + 2 强调色，灰度打印后仍以深浅/虚实区分。
- **对比度**：文字 `#333333` on `#FFFFFF` ≥ 4.5:1。
- **原因**：正式申报书要求克制专业；F1 等框架图 ≥4 模块，单色系减少视觉噪音；工程/科技领域适配 Nature Blue。

### 0.5 通用渲染规则（所有图共用）

- 画布纯白 `#FFFFFF`；盒体白底 + 彩色边框，绝不上色填充盒体。
- 文字**仅**出现在 exact_* 字段指定位置；模块标题 ≤5 词，步骤标签 ≤2 词主 + ≤2 词副。
- 容器边框 1.5pt 实线、内部分隔 1.0pt、主线箭头 1.5pt（4px 箭头）、反馈/回环箭头 1.0pt 虚线。
- 图标一律单色细线（用所在块边框色或深灰），禁止彩色图标、emoji、锁/火焰/闪电装饰、3D 渲染。
- 冻结/待核验状态用**虚线边框 + [待核验] pill**，非 emoji。
- 扁平矢量：无渐变、无投影、无 3D；中文用思源黑体/微软雅黑，英文数字用 Helvetica/Arial，公式用 Times italic。
- 中文标注尽量 ≤8 字/行；长公式、参数、指标定义进 **图注（caption）**，不上图。
- 画布宽度：NSFC A4 单栏正文约 140 mm（适配 89mm/183mm 期刊口径）；图宽 0.8\linewidth 排版。

---

## 1. F1 总体研究框架（must · Overall Framework · 16:9）

**中文图名**：总体研究框架与技术路线
**放置**：2.1 研究内容开头 或 3.2 技术路线；`\label{fig:overall-framework}`
**配色**：Nature Blue + 语义强调（见 §0）

### 1.1 JSON 图规格

```json
{
  "diagram_type": "End-to-end research framework with validation loop",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin), Times italic (formula)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt",
      "tensor_shape": "7pt"
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
      "Input_Materials": "#1B3A5C 2px solid border, white fill",
      "License_Review": "#1B3A5C 2px solid border, white fill",
      "Joint_Knowledge": "#2E6B9E 2px solid border, white fill",
      "Cross_Modal": "#5BA0D0 2px solid border, white fill",
      "Resource_Unit": "#2E6B9E 2px solid border, white fill",
      "Quality_Gate": "#D95F02 2px solid border, white fill",
      "Output_Pack": "#1B9E77 2px solid border, white fill",
      "Validation_Bar": "#616161 1px solid border, white fill",
      "Innovation_Callouts": "#D95F02 text only"
    },
    "flow_arrow_colors": {
      "main_forward_flow": "Dark Grey (#4D4D4D) straight solid arrows",
      "manual_review_loop": "Dark Grey (#4D4D4D) dashed curved arrow from Quality Gate back to License Review",
      "validation_flow": "Dark Grey (#4D4D4D) thin arrows to bottom validation bar"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Left",
      "shape": "Rounded rectangle, #1B3A5C 2px solid border, white fill",
      "exact_title_to_render_inside": "输入材料",
      "exact_label": "公开/授权/自建",
      "icon": "four small thumbnails: document text lines, image frame, waveform curve, code brackets, monochrome line art",
      "secondary_note": "文本·设备图·运行曲线·代码/案例",
      "flow": "Horizontal arrow RIGHT to License Review"
    },
    {
      "relative_position": "Top Left-Center",
      "shape": "Rounded rectangle, #1B3A5C 2px solid border, white fill",
      "exact_title_to_render_inside": "来源登记\n授权审查",
      "icon": "thin shield with check mark, monochrome line art",
      "secondary_note": "许可·版本·脱敏",
      "flow": "Horizontal arrow RIGHT to Joint Knowledge"
    },
    {
      "relative_position": "Top Center",
      "shape": "Rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "联合知识约束",
      "icon": "two overlapping circles labeled Kp and Kc, monochrome line art",
      "internal_content": {
        "layout": "two small stacked pills",
        "pill_1": {"exact_text": "产业知识 Kp", "secondary_note": "任务·设备·工况"},
        "pill_2": {"exact_text": "课程知识 Kc", "secondary_note": "知识点·能力目标·先修"}
      },
      "exact_floating_text": "创新点①",
      "flow": "Horizontal arrow RIGHT to Cross-Modal"
    },
    {
      "relative_position": "Top Center-Right",
      "shape": "Rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "跨模态证据关联",
      "icon": "two rows of dots with crossing thin arrows (matching), monochrome line art",
      "internal_content": {
        "layout": "two small stacked pills",
        "pill_1": {"exact_text": "专业属性 Ai", "secondary_note": "对象·变量·单位·工况·时序"},
        "pill_2": {"exact_text": "来源位置 ei", "secondary_note": "可核查出处"}
      },
      "exact_floating_text": "创新点②",
      "flow": "Horizontal arrow RIGHT to Resource Unit"
    },
    {
      "relative_position": "Top Right",
      "shape": "Rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "资源单元",
      "exact_text": "u = (c,a,m,e,s)",
      "secondary_note": "课程·属性·片段·证据·状态",
      "icon": "small card with five field slots, monochrome line art",
      "flow": "Horizontal arrow RIGHT to Quality Gate"
    },
    {
      "relative_position": "Top Far Right",
      "shape": "Rounded rectangle, #D95F02 2px solid border, white fill",
      "exact_title_to_render_inside": "四层质量门控",
      "exact_text": "内容·课程·模态·证据",
      "icon": "four horizontal gate bars of decreasing height, monochrome line art",
      "exact_floating_text": "创新点③",
      "flow": "Horizontal arrow RIGHT to Output Pack; dashed loop DOWN to manual review then back to License Review"
    },
    {
      "relative_position": "Top Far Right End",
      "shape": "Rounded rectangle, #1B9E77 2px solid border, white fill",
      "exact_title_to_render_inside": "可追溯资源包\n本地原型",
      "icon": "small package box with trace link icon, monochrome line art",
      "secondary_note": "离线验证·不含学生数据",
      "flow": "Thin arrows DOWN to Validation Bar"
    },
    {
      "relative_position": "Bottom",
      "shape": "Wide panel, #F7F7F7 fill with #8EAEC4 1px border",
      "exact_title_to_render_inside": "验证",
      "exact_text": "B0 人工整理  B1 通用大模型  B2 文本RAG  B3 完整方法",
      "exact_floating_text": "逐项消融 | 独立专家盲评 | 跨来源留出 | VRR 主指标",
      "icon": "small bar-chart thumbnail and checkmark pair, monochrome line art"
    }
  ],
  "caption_note": [
    "图注：公开/授权/自建资源经来源登记与授权审查后，依次经产业任务—课程知识联合约束、专业属性与来源证据约束的跨模态关联构建资源单元 u=(c,a,m,e,s)，再经内容、课程、模态、证据四层质量门控输出可追溯资源包与本地原型。",
    "验证：B0 人工整理、B1 通用大模型直接构建、B2 仅文本检索增强生成与 B3 完整方法对照，并逐项消融产业知识、课程知识、专业属性、来源位置与四层质量各层；主指标为有效资源单元通过率 VRR，辅以 Recall@1/5、MRR、关系 F1、来源定位、五维专家盲评、Krippendorff's alpha 与人工修订时间。",
    "创新点①②③分别对应该图中联合知识约束、跨模态证据关联与四层质量门控三个模块。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings above verbatim; do not rephrase or translate them.",
    "All boxes: white (#FFFFFF) fill with colored borders ONLY; canvas pure white.",
    "Main forward flow solid dark grey arrows; manual-review loop dashed.",
    "Icons monochrome thin line art in the block border color.",
    "NO emojis, NO 3D, NO gradients, NO shadows, NO decorative elements.",
    "Flat vector style, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 1.2 图像提示词（English, generation-ready）

Flat vector academic architecture diagram showing the overall research framework of a university renewable-energy multimodal teaching-resource construction system on a pure white #FFFFFF canvas, 16:9. One horizontal left-to-right pipeline of seven rounded rectangles (white fill, colored 2px borders, 6px corner radius) connected by solid dark grey #4D4D4D arrows.

Stage 1, dark navy #1B3A5C border, titled "输入材料" with four small monochrome thumbnails inside: document text lines, image frame, waveform curve, code brackets; small subtitle "公开/授权/自建". Stage 2, same navy border, "来源登记 授权审查" with a thin shield-with-check icon. Stage 3, medium blue #2E6B9E border, "联合知识约束" containing two small pills "产业知识 Kp" and "课程知识 Kc", with a small orange text callout "创新点①" above. Stage 4, light blue #5BA0D0 border, "跨模态证据关联" with a matching-lines icon and two pills "专业属性 Ai" and "来源位置 ei", callout "创新点②". Stage 5, medium blue border, "资源单元" with the formula "u=(c,a,m,e,s)" in Times italic and a five-slot card icon. Stage 6, coral #D95F02 border, "四层质量门控" with a four-bar gate icon and the line "内容·课程·模态·证据", callout "创新点③"; a dashed dark-grey loop curves from its bottom back to stage 2 labelled by a small pill "人工核验". Stage 7, emerald #1B9E77 border, "可追溯资源包 本地原型" with a small package icon.

Bottom validation panel on a very light grey #F7F7F7 strip: the row "B0 人工整理  B1 通用大模型  B2 文本RAG  B3 完整方法" with a small bar-chart thumbnail, and below it the smaller line "逐项消融 | 独立专家盲评 | 跨来源留出 | VRR 主指标". Thin arrows drop from stages 6 and 7 into this strip. All Chinese labels rendered verbatim; text dark grey #333333, Helvetica-style sans-serif, module titles bold 12pt, secondary notes 8pt. Flat vector, no gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.

---

## 2. F2 研究背景与问题动机（strong · Motivation / Data Behavior · 16:9）

**中文图名**：研究背景：分散资源与自动重组的错误类型
**放置**：1.1 研究背景与意义；`\label{fig:research-background}`
**配色**：Nature Blue + 珊瑚（错配）/ 翡翠（正确）双态

### 2.1 JSON 图规格

```json
{
  "diagram_type": "Problem motivation diagram with correct vs mismatched examples",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Scattered_Materials": "#1B3A5C 2px solid border, white fill",
      "Correct_Link": "#1B9E77 2px solid border, white fill",
      "Wrong_Link": "#D95F02 2px solid border, white fill",
      "No_Provenance": "#616161 2px dashed border, white fill",
      "Punchline": "#1B3A5C text only"
    },
    "flow_arrow_colors": {
      "down": "Dark Grey (#4D4D4D) thin arrows",
      "correct": "#1B9E77 solid thin arrow",
      "wrong": "#D95F02 solid thin arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top",
      "shape": "One row of five equal rounded rectangles, #1B3A5C 2px border, white fill",
      "exact_title_to_render_inside": "同一知识点：分散材料",
      "icon": "row of five small thumbnails: text lines, waveform curve, image frame, code brackets, industry case tag, monochrome line art",
      "secondary_note": "讲义 · 运行曲线 · 设备图 · 代码 · 案例",
      "flow": "Thin arrows DOWN to the two example rows"
    },
    {
      "relative_position": "Middle Left",
      "shape": "Rounded rectangle, #1B9E77 2px solid border, white fill",
      "exact_title_to_render_inside": "正确关联",
      "exact_text": "曲线与文字共享变量与时间窗口",
      "exact_floating_text": "✓ 可进入资源包",
      "icon": "small checkmark inside a circle, monochrome line art",
      "secondary_note": "工况一致 · 出处可查"
    },
    {
      "relative_position": "Middle Right",
      "shape": "Rounded rectangle, #D95F02 2px solid border, white fill",
      "exact_title_to_render_inside": "专业条件错配",
      "exact_text": "语义相似但变量/单位/工况不一致",
      "exact_floating_text": "✗ 拒绝",
      "icon": "small cross inside a circle, monochrome line art",
      "secondary_note": "相似≠可用"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Rounded rectangle, #616161 2px dashed border, white fill",
      "exact_title_to_render_inside": "来源不可核查",
      "exact_text": "图表存在但出处不可定位",
      "exact_floating_text": "✗ 待核验",
      "icon": "small question-mark tag icon, monochrome line art"
    },
    {
      "relative_position": "Bottom",
      "shape": "No box, centered text",
      "exact_text": "可检索，但不可教学使用",
      "secondary_note": "资源单元边界·关系条件·证据支持为可检验对象"
    }
  ],
  "caption_note": [
    "图注：同一知识点的讲义文本、运行曲线、设备图、代码与产业案例常以分散文件存在，自动重组时可能出现专业条件错配（变量、单位、工况、时序不一致）或来源不可核查等错误，导致资源‘可检索但不可教学使用’。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings above verbatim; keep ✓ and ✗ as thin line-art glyphs, not emojis.",
    "All boxes white fill with colored borders; canvas pure white.",
    "Icons monochrome thin line art only.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 2.2 图像提示词（English, generation-ready）

Flat vector academic problem-motivation diagram on a pure white #FFFFFF canvas, 16:9, explaining why scattered multimodal teaching materials fail automatic reassembly for a renewable-energy course.

Top row: a single group box with dark navy #1B3A5C border titled "同一知识点：分散材料", containing five equal small thumbnails in monochrome line art — text lines, waveform curve, image frame, code brackets, and an industry-case tag — with the subtitle "讲义 · 运行曲线 · 设备图 · 代码 · 案例" beneath. Three thin dark-grey arrows drop from this row into three outcome rows below.

Outcome one (middle left): rounded rectangle with emerald #1B9E77 border titled "正确关联", body text "曲线与文字共享变量与时间窗口", a thin circle-check line-art glyph, and a green pill "✓ 可进入资源包". Outcome two (middle right): rounded rectangle with coral #D95F02 border titled "专业条件错配", body text "语义相似但变量/单位/工况不一致", a circle-cross glyph, and a coral pill "✗ 拒绝". Outcome three (bottom left): dashed grey #616161 border rectangle titled "来源不可核查", body text "图表存在但出处不可定位", question-mark tag icon, grey pill "✗ 待核验".

Bottom center, no box, a bold dark-navy sentence "可检索，但不可教学使用" with a smaller grey note "资源单元边界·关系条件·证据支持为可检验对象". All Chinese text rendered verbatim, dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.

---

## 3. F3 联合知识约束模块（must · Module Detail · 4:3）

**中文图名**：模块一：产业任务—课程知识联合约束
**放置**：3.1 研究方法（对应公式 2/3）；`\label{fig:joint-knowledge}`
**配色**：Nature Blue + 珊瑚（冲突）/ 翡翠（通过）

### 3.1 JSON 图规格

```json
{
  "diagram_type": "Module detail diagram of joint industry-course knowledge constraint",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin), Times italic (formula)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt",
      "tensor_shape": "7pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Industry_Knowledge": "#2E6B9E 2px solid border, white fill",
      "Course_Knowledge": "#2E6B9E 2px solid border, white fill",
      "Joint_Score": "#1B3A5C 2px solid border, white fill",
      "Boundary_Loss": "#5BA0D0 2px solid border, white fill",
      "Pending_Queue": "#616161 2px dashed border, white fill",
      "Four_Conditions": "#8EAEC4 1px border pills, white fill"
    },
    "flow_arrow_colors": {
      "forward": "Dark Grey (#4D4D4D) solid arrows",
      "conflict": "#D95F02 thin dashed arrows into pending queue"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Left",
      "shape": "Rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "产业任务知识 Kp",
      "exact_text": "任务 · 设备 · 工况",
      "secondary_note": "变量·单位·时序",
      "icon": "small factory-gear icon, monochrome line art",
      "flow": "Arrow RIGHT into Joint Score"
    },
    {
      "relative_position": "Top Right",
      "shape": "Rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "课程知识 Kc",
      "exact_text": "知识点 · 能力目标 · 先修关系",
      "icon": "small open-book icon, monochrome line art",
      "flow": "Arrow LEFT into Joint Score"
    },
    {
      "relative_position": "Center",
      "shape": "Rounded rectangle, #1B3A5C 2px solid border, white fill",
      "exact_title_to_render_inside": "联合评分",
      "exact_text": "S_kc = λp·Sp + λc·Sc + λpc·Spc",
      "icon": "two overlapping circles with a scale symbol, monochrome line art",
      "secondary_note": "产业属性·课程属性·术语映射",
      "flow": "Arrow RIGHT into Boundary Loss"
    },
    {
      "relative_position": "Right",
      "shape": "Rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "单元边界四项约束",
      "exact_text": "覆盖 Lcover · 重复 Ldup · 过度切分 Lsplit · 属性错配 Lattr",
      "icon": "four small rule lines with endpoints, monochrome line art",
      "flow": "Thin arrows DOWN to Four Conditions"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Rounded rectangle, #616161 2px dashed border, white fill",
      "exact_title_to_render_inside": "待核验队列",
      "exact_text": "粒度差异 · 术语异名 · 属性冲突",
      "icon": "small hourglass icon, monochrome line art",
      "secondary_note": "[待核验]"
    },
    {
      "relative_position": "Bottom Center",
      "shape": "Row of four equal pills, #8EAEC4 1px border, white fill",
      "exact_title_to_render_inside": "四条件比较",
      "exact_text": "无知识 | 仅产业 | 仅课程 | 联合约束",
      "exact_floating_text": "联合约束高亮 #1B3A5C 加粗边框",
      "icon": "small comparison scale icon, monochrome line art"
    }
  ],
  "caption_note": [
    "公式注：S_kc(di,kj)=λp·Sp(di,kj;Kp)+λc·Sc(di,kj;Kc)+λpc·Spc(di,kj)，λ 为开发集权重。",
    "单元边界损失：Lunit=Lcover+α·Ldup+β·Lsplit+γ·Lattr，分别惩罚知识遗漏、重复、过度切分与专业属性错配。",
    "在无知识、仅产业知识、仅课程知识与联合约束四种条件下比较单元边界 F1、知识覆盖与属性错误率，检验科学问题一。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings and the one-line formula verbatim; formula in Times italic.",
    "All boxes white fill with colored borders; canvas pure white.",
    "Icons monochrome thin line art in block border color.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 3.2 图像提示词（English, generation-ready）

Flat vector academic module-detail diagram of the joint industry-course knowledge constraint module on a pure white #FFFFFF canvas, 4:3.

Top left: rounded rectangle with medium-blue #2E6B9E border titled "产业任务知识 Kp", body "任务 · 设备 · 工况", small grey note "变量·单位·时序", and a small monochrome gear icon; a solid dark-grey arrow points right. Top right: rounded rectangle with the same medium-blue border titled "课程知识 Kc", body "知识点 · 能力目标 · 先修关系", small open-book line-art icon; an arrow points left. Both converge into a central rounded rectangle with dark-navy #1B3A5C border titled "联合评分", containing the one-line formula "S_kc = λp·Sp + λc·Sc + λpc·Spc" in Times italic, a two-circle overlap icon, and the note "产业属性·课程属性·术语映射". A right arrow leads to a light-blue #5BA0D0 rectangle titled "单元边界四项约束" with the body "覆盖 Lcover · 重复 Ldup · 过度切分 Lsplit · 属性错配 Lattr" and four rule-line icons.

Bottom left: dashed grey #616161 rectangle titled "待核验队列" with body "粒度差异 · 术语异名 · 属性冲突", an hourglass icon and a grey "[待核验]" pill; two thin coral #D95F02 dashed arrows drop from the knowledge boxes into it. Bottom center: a row of four equal pills "无知识 | 仅产业 | 仅课程 | 联合约束" with the last pill "联合约束" given a thicker dark-navy border to highlight it. All Chinese text rendered verbatim in dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.

---

## 4. F4 跨模态证据关联模块（must · Module Detail · 4:3）

**中文图名**：模块二：专业属性与来源证据约束的跨模态关联
**放置**：3.1 研究方法（对应公式 4/5）；`\label{fig:cross-modal}`
**配色**：Nature Blue + 珊瑚（错配类型）

### 4.1 JSON 图规格

```json
{
  "diagram_type": "Module detail diagram of attribute- and provenance-constrained cross-modal association",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin), Times italic (formula)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt",
      "tensor_shape": "7pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid with 4px head"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Multimodal_Input": "#1B3A5C 2px solid border, white fill",
      "Encoder": "#5BA0D0 2px solid border, white fill",
      "Attribute_Provenance": "#5BA0D0 2px solid border, white fill",
      "Relation_Score": "#1B3A5C 2px solid border, white fill",
      "Write_Unit": "#1B9E77 2px solid border, white fill",
      "Error_Types": "#D95F02 1.5px dashed border pills, white fill"
    },
    "flow_arrow_colors": {
      "forward": "Dark Grey (#4D4D4D) solid arrows",
      "reject": "#D95F02 thin dashed arrow to Error Types"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top",
      "shape": "Wide rounded rectangle, #1B3A5C 2px solid border, white fill",
      "exact_title_to_render_inside": "多模态输入",
      "exact_text": "文本 · 设备图 · 运行曲线 · 代码/案例",
      "icon": "row of four small thumbnails: text lines, image frame, waveform, code brackets, monochrome line art",
      "flow": "Arrow DOWN into Encoder"
    },
    {
      "relative_position": "Center Left",
      "shape": "Rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "编码与对齐",
      "exact_text": "z_i  →  对比学习 L_align",
      "icon": "two rows of dots with thin matching arrows, monochrome line art",
      "secondary_note": "公式见图注",
      "flow": "Arrow RIGHT into Relation Score"
    },
    {
      "relative_position": "Center Right",
      "shape": "Rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "属性与证据抽取",
      "exact_text": "专业属性 Ai · 来源位置 ei",
      "icon": "small tag with location pin, monochrome line art",
      "secondary_note": "对象·变量·单位·工况·时间窗口",
      "flow": "Arrow LEFT into Relation Score"
    },
    {
      "relative_position": "Center Bottom",
      "shape": "Rounded rectangle, #1B3A5C 2px solid border, white fill",
      "exact_title_to_render_inside": "联合评分",
      "exact_text": "R(i,j) = ηs·sim + ηa·CA + ηe·CE + ηr·CR",
      "icon": "small gate symbol with threshold line, monochrome line art",
      "secondary_note": "阈值+证据完整方可写入",
      "flow": "Arrow RIGHT into Write Unit; thin coral dashed arrow DOWN to Error Types"
    },
    {
      "relative_position": "Bottom Right",
      "shape": "Rounded rectangle, #1B9E77 2px solid border, white fill",
      "exact_title_to_render_inside": "写入资源单元",
      "exact_text": "关系类型 · 专业条件 · 证据可查",
      "icon": "small check-in-database icon, monochrome line art"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Row of small pills, #D95F02 1.5px dashed border, white fill",
      "exact_title_to_render_inside": "困难负例：错误类型",
      "exact_text": "变量错配 · 单位错配 · 工况错配 · 时序错配 · 来源不可核查",
      "icon": "small alert-triangle line-art icon"
    }
  ],
  "caption_note": [
    "公式注：Lalign=−(1/B)Σ log[exp(sim(zi,zi+)/τ) / Σj exp(sim(zi,zj)/τ)]（对比学习基础表示）。",
    "候选关系评分 R(i,j)=ηs·sim(zi,zj)+ηa·CA(Ai,Aj)+ηe·CE(ei,ej)+ηr·CR(i,j)，CA/CE/CR 分别检查专业属性、来源位置与关系类别。",
    "仅语义相似不足以保证正确：按关系类型报告 Recall@1/5、MRR、关系 F1、来源定位准确率与专业条件错配率，检验科学问题二。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings and the one-line formulas verbatim; formulas in Times italic.",
    "All boxes white fill with colored borders; canvas pure white.",
    "Icons monochrome thin line art only.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 4.2 图像提示词（English, generation-ready）

Flat vector academic module-detail diagram of attribute- and provenance-constrained cross-modal association on a pure white #FFFFFF canvas, 4:3.

Top: a wide rounded rectangle with dark-navy #1B3A5C border titled "多模态输入", containing four small monochrome thumbnails (text lines, image frame, waveform, code brackets) and the body "文本 · 设备图 · 运行曲线 · 代码/案例". A solid dark-grey arrow drops to the center.

Center left: rounded rectangle with light-blue #5BA0D0 border titled "编码与对齐", body "z_i  →  对比学习 L_align" with a two-rows-of-dots matching icon and the note "公式见图注". Center right: rounded rectangle, same light-blue border, titled "属性与证据抽取", body "专业属性 Ai · 来源位置 ei", small tag-with-pin icon, note "对象·变量·单位·工况·时间窗口". Both feed into a central dark-navy #1B3A5C rectangle titled "联合评分" containing the Times-italic formula "R(i,j) = ηs·sim + ηa·CA + ηe·CE + ηr·CR", a gate-with-threshold icon, and the note "阈值+证据完整方可写入".

From the score block, a solid emerald #1B9E77-bordered arrow points right into a rectangle titled "写入资源单元" with body "关系类型 · 专业条件 · 证据可查" and a check-in-database icon. A thin coral #D95F02 dashed arrow drops down to a row of dashed coral pills titled "困难负例：错误类型" containing "变量错配 · 单位错配 · 工况错配 · 时序错配 · 来源不可核查" with a small alert-triangle icon. All Chinese text rendered verbatim in dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt, formulas in Times italic. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.

---

## 5. F5 四层质量门控模块（must · Module Detail · 4:3）

**中文图名**：模块三：资源内在质量四层门控与独立验证
**放置**：3.1 研究方法（对应公式 6/7/8）；`\label{fig:quality-gate}`
**配色**：Nature Blue + 珊瑚（拒绝）/ 翡翠（通过）

### 5.1 JSON 图规格

```json
{
  "diagram_type": "Module detail diagram of four-layer quality gate with independent validation loop",
  "diagram_title_rendering": "None",
  "aspect_ratio": "4:3",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin), Times italic (formula)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt",
      "tensor_shape": "7pt"
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
      "Resource_Unit_In": "#2E6B9E 2px solid border, white fill",
      "Evidence_Score": "#5BA0D0 2px solid border, white fill",
      "Four_Layers": "#1B3A5C 2px solid border, white fill",
      "Reject": "#D95F02 2px solid border, white fill",
      "Pass_VRR": "#1B9E77 2px solid border, white fill",
      "Validation_Loop": "#616161 1px dashed border, white fill"
    },
    "flow_arrow_colors": {
      "forward": "Dark Grey (#4D4D4D) solid arrows",
      "reject": "#D95F02 dashed arrow",
      "pass": "#1B9E77 solid arrow"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Left",
      "shape": "Rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "资源单元输入",
      "exact_text": "关键断言集合 A(u)",
      "icon": "small card with assertion lines, monochrome line art",
      "flow": "Arrow RIGHT into Evidence Score"
    },
    {
      "relative_position": "Top Right",
      "shape": "Rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "证据支持度",
      "exact_text": "G(a,e) = ρt·Gt + ρv·Gv + ρk·Gk",
      "icon": "small chain-link icon, monochrome line art",
      "secondary_note": "文本·模态·知识关系支持",
      "flow": "Arrow DOWN into Four Layers"
    },
    {
      "relative_position": "Center",
      "shape": "Vertical stack of four equal bands inside one container, #1B3A5C 2px border, white fill",
      "exact_title_to_render_inside": "四层质量门控",
      "internal_content": {
        "layout": "four stacked bands with internal 1.0pt dividers",
        "band_1": {"exact_text": "内容层 q_con", "secondary_note": "事实/参数"},
        "band_2": {"exact_text": "课程层 q_cur", "secondary_note": "知识点/能力目标"},
        "band_3": {"exact_text": "模态层 q_mod", "secondary_note": "跨模态对象条件"},
        "band_4": {"exact_text": "证据层 q_evi", "secondary_note": "原始出处"}
      },
      "icon": "four horizontal gate bars, monochrome line art",
      "flow": "DOWN branches: left coral dashed to Reject; right emerald solid to Pass_VRR"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Rounded rectangle, #D95F02 2px solid border, white fill",
      "exact_title_to_render_inside": "拒绝",
      "exact_text": "任一层严重错误 · 保留原因",
      "icon": "small crossed-circle icon, monochrome line art",
      "secondary_note": "进入人工核验"
    },
    {
      "relative_position": "Bottom Right",
      "shape": "Rounded rectangle, #1B9E77 2px solid border, white fill",
      "exact_title_to_render_inside": "通过 → VRR 计入",
      "exact_text": "字段完整 · 无严重错误",
      "icon": "small checkmark-in-circle icon, monochrome line art"
    },
    {
      "relative_position": "Very Bottom",
      "shape": "Wide panel, #616161 1px dashed border, white fill",
      "exact_title_to_render_inside": "独立验证",
      "exact_text": "五维专家盲评 · Krippendorff α · 跨来源留出 · 人工修订",
      "icon": "small eye and scale icons, monochrome line art",
      "secondary_note": "自动初筛 → 人工复核"
    }
  ],
  "caption_note": [
    "公式注：G(a,e)=ρt·Gt(a,e)+ρv·Gv(a,e)+ρk·Gk(a,e)，不满足 G≥θg 的断言进入人工核验。",
    "综合质量 Q(u)=wcon·qcon+wcur·qcur+wmod·qmod+wevi·qevi−μ·P(u)，P 为严重错误惩罚（参数矛盾、来源不可追溯、未授权/隐私风险）。",
    "主指标 VRR=Σ I[qcon,qcur,qmod,qevi 均合格]/|U|；与五维专家盲评（内容正确性、课程目标对齐、跨模态一致、教学完整、来源可追溯）、Krippendorff's alpha、错误检出/误报率、人工修订时间共同报告，检验科学问题三。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings and the one-line formula verbatim; formula in Times italic.",
    "All boxes white fill with colored borders; canvas pure white.",
    "Icons monochrome thin line art only.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 5.2 图像提示词（English, generation-ready）

Flat vector academic module-detail diagram of the four-layer resource quality gate on a pure white #FFFFFF canvas, 4:3.

Top left: rounded rectangle with medium-blue #2E6B9E border titled "资源单元输入", body "关键断言集合 A(u)", small card-with-lines icon, arrow pointing right into a light-blue #5BA0D0 rectangle titled "证据支持度" containing the Times-italic formula "G(a,e) = ρt·Gt + ρv·Gv + ρk·Gk", a chain-link icon, and the note "文本·模态·知识关系支持". A solid dark-grey arrow drops into the central gate.

Center: one tall rounded container with dark-navy #1B3A5C border titled "四层质量门控", internally divided by thin 1.0pt lines into four equal horizontal bands: "内容层 q_con  (事实/参数)", "课程层 q_cur  (知识点/能力目标)", "模态层 q_mod  (跨模态对象条件)", "证据层 q_evi  (原始出处)"; a four-bar gate icon sits at its right edge. From the bottom of the gate two arrows diverge: a coral #D95F02 dashed arrow to the lower-left rectangle "拒绝" (body "任一层严重错误 · 保留原因", crossed-circle icon, note "进入人工核验"), and an emerald #1B9E77 solid arrow to the lower-right rectangle "通过 → VRR 计入" (body "字段完整 · 无严重错误", checkmark-circle icon).

Very bottom: a wide panel with dashed grey #616161 border titled "独立验证" containing the row "五维专家盲评 · Krippendorff α · 跨来源留出 · 人工修订", small eye and scale line-art icons, and the note "自动初筛 → 人工复核". All Chinese text rendered verbatim in dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt, formulas in Times italic. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 4:3.

---

## 6. F6 实验设计与对照消融矩阵（strong · Comparison / Ablation · 16:9）

**中文图名**：实验设计：B0–B3 对照与逐项消融
**放置**：3.2 技术路线与实验手段；`\label{fig:experiment-matrix}`
**配色**：灰底基线 + 单一强调（完整方法高亮）

### 6.1 JSON 图规格

```json
{
  "diagram_type": "Comparison-ablation matrix of baselines and full method",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Baseline_Cell": "#CCCCCC 1px solid border, white fill",
      "Ours_Cell": "#1B3A5C 2.5px solid border, white fill",
      "Row_Header": "#8EAEC4 1px solid border, #F7F7F7 fill",
      "Ablation_Panel": "#616161 1px dashed border, white fill",
      "Split_Panel": "#F7F7F7 fill, #8EAEC4 1px border"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top Left",
      "shape": "Row header cell, #F7F7F7 fill with #8EAEC4 1px border",
      "exact_text": "指标层 / 方法",
      "icon": "small corner-table icon, monochrome line art"
    },
    {
      "relative_position": "Top Row",
      "shape": "Four equal column header cells, #F7F7F7 fill, #8EAEC4 1px border",
      "exact_text": "B0 人工整理 | B1 通用大模型 | B2 文本RAG | B3 完整方法",
      "exact_floating_text": "B3 列 #1B3A5C 2.5px 加粗边框 + [完整方法] pill"
    },
    {
      "relative_position": "Middle Rows",
      "shape": "3 x 4 grid of equal cells; baseline cells #CCCCCC 1px border, ours column #1B3A5C 2.5px border",
      "exact_text": "构建层：边界F1·覆盖·属性错误",
      "exact_floating_text": "关联层：Recall@1/5·MRR·关系F1·错配率",
      "secondary_note": "质量层：VRR·误报/漏报·盲评·修订时间",
      "icon": "small metric-dashboard icons: bar chart, curve, gauge, monochrome line art"
    },
    {
      "relative_position": "Bottom Left",
      "shape": "Rounded rectangle, #616161 1px dashed border, white fill",
      "exact_title_to_render_inside": "逐项消融",
      "exact_text": "去产业知识 · 去课程知识 · 去专业属性 · 去来源位置 · 去质量层",
      "icon": "small split-remove icon, monochrome line art"
    },
    {
      "relative_position": "Bottom Right",
      "shape": "Rounded rectangle, #F7F7F7 fill with #8EAEC4 1px border",
      "exact_title_to_render_inside": "测试划分",
      "exact_text": "知识模块留出 · 设备类型留出 · 材料来源留出",
      "icon": "small three-slice pie icon, monochrome line art"
    }
  ],
  "caption_note": [
    "图注：构建层报告边界 F1、知识覆盖、重复与属性错误；关联层报告 Recall@1/5、MRR、关系 F1、来源定位与错配率；质量层报告 VRR、错误检出/误报、五维专家盲评与人工修订时间。",
    "完整方法 B3 由产业—课程联合知识约束、专业属性与来源证据跨模态关联、四层质量门控构成；B0–B2 分别为人工整理、通用大模型直接构建与仅文本检索增强生成。",
    "消融逐项去除产业知识、课程知识、专业属性、来源位置与四层质量各层；测试集按知识模块、设备类型或材料来源留出，近重复材料不跨集合。指标为拟验证项，阈值在开发集预实验后冻结。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings above verbatim.",
    "Baseline cells thin grey border; only the B3/ours column gets the thick navy border and a pill.",
    "All cells white fill; canvas pure white; icons monochrome line art.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 6.2 图像提示词（English, generation-ready）

Flat vector academic comparison matrix on a pure white #FFFFFF canvas, 16:9, contrasting four construction pipelines for a multimodal teaching-resource system.

Top-left corner cell and four top column-header cells on a very light grey #F7F7F7 strip with thin #8EAEC4 borders: the corner cell reads "指标层 / 方法", and the four headers read "B0 人工整理", "B1 通用大模型", "B2 文本RAG", "B3 完整方法". Below, a 3-by-4 grid of equal white cells with thin grey #CCCCCC borders; the B3 column is highlighted with a thick dark-navy #1B3A5C 2.5px border and a small navy pill "[完整方法]". Row labels on the left are "构建层", "关联层", "质量层", and the cell contents read respectively "边界F1·覆盖·属性错误", "Recall@1/5·MRR·关系F1·错配率", "VRR·误报/漏报·盲评·修订时间", each with a small monochrome dashboard icon (bar chart, curve, gauge). The cell text describes the metrics to be reported, not numeric results.

Bottom left: a dashed grey #616161 panel titled "逐项消融" containing "去产业知识 · 去课程知识 · 去专业属性 · 去来源位置 · 去质量层" with a small split-remove icon. Bottom right: a light-grey panel titled "测试划分" containing "知识模块留出 · 设备类型留出 · 材料来源留出" with a small three-slice pie icon. All Chinese text rendered verbatim in dark grey #333333 sans-serif, headers bold 12pt, cell text 9-10pt, notes 8pt. Flat vector, thin outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.

---

## 7. F7 年度研究计划甘特（nice · Timeline · 16:9）

**中文图名**：两年期研究计划
**放置**：5.1 年度研究计划；`\label{fig:research-plan}`
**配色**：Nature Blue 两阶段色 + 里程碑标记

### 7.1 JSON 图规格

```json
{
  "diagram_type": "Two-year research plan Gantt timeline",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Phase1": "#2E6B9E 2px solid border, white fill",
      "Phase2": "#5BA0D0 2px solid border, white fill",
      "Milestone": "#1B3A5C small diamond markers",
      "Axis": "#CCCCCC thin axis line"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Top",
      "shape": "Horizontal 24-month axis with month ticks, #CCCCCC thin line",
      "exact_text": "第1月 — 第12月 — 第24月",
      "secondary_note": "M1  M6  M12  M18  M24"
    },
    {
      "relative_position": "Middle Top",
      "shape": "Wide rounded rectangle, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "第一阶段（1–12月）",
      "exact_text": "来源登记·授权审查 · 知识结构与单元切分 · 三类核心模态解析 · 基线构建 · 预实验 · 冻结指标",
      "icon": "small checklist icon, monochrome line art",
      "secondary_note": "验收：合规清单·元数据卡·标注规范·开发集划分"
    },
    {
      "relative_position": "Middle Bottom",
      "shape": "Wide rounded rectangle, #5BA0D0 2px solid border, white fill",
      "exact_title_to_render_inside": "第二阶段（13–24月）",
      "exact_text": "跨模态关联完善 · 四层质量门控 · 测试集对照消融 · 专家盲评 · 原型迭代",
      "icon": "small magnifier icon, monochrome line art",
      "secondary_note": "验收：冻结配置·B0–B3·消融·盲评一致性·质量报告"
    },
    {
      "relative_position": "Bottom",
      "shape": "Row of small diamond markers with labels, #1B3A5C",
      "exact_text": "阶段验收点",
      "exact_floating_text": "具体时间节点以立项通知书为准",
      "icon": "small diamond outline markers, monochrome line art"
    }
  ],
  "caption_note": [
    "图注：项目按两年期安排，第一阶段完成材料合规、知识结构、解析流程、基线与预实验并冻结主要指标；第二阶段完成跨模态关联、四层门控、对照消融、独立专家盲评与本地原型迭代。",
    "阶段性验收以材料合规清单、资源元数据卡、标注规范、冻结测试配置、B0–B3 比较、模块消融、误差分析、专家盲评一致性与资源质量报告为主；若跨来源验证或盲评未支持预设机制，形成边界与负结果说明。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings above verbatim.",
    "Timeline axis thin grey; two phase bars with white fill and colored borders; diamond markers small.",
    "Icons monochrome line art only.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 7.2 图像提示词（English, generation-ready）

Flat vector academic Gantt-style timeline of a two-year research plan on a pure white #FFFFFF canvas, 16:9.

Top: a thin grey #CCCCCC horizontal axis spanning 24 months with tick marks and labels "第1月", "第12月", "第24月" and smaller grey ticks "M1 M6 M12 M18 M24". Below it, two wide horizontal rounded rectangles stacked:

Phase one bar (upper) with medium-blue #2E6B9E 2px border, white fill, title "第一阶段（1–12月）", body "来源登记·授权审查 · 知识结构与单元切分 · 三类核心模态解析 · 基线构建 · 预实验 · 冻结指标", a small monochrome checklist icon, and the small grey note "验收：合规清单·元数据卡·标注规范·开发集划分". Phase two bar (lower) with light-blue #5BA0D0 2px border, title "第二阶段（13–24月）", body "跨模态关联完善 · 四层质量门控 · 测试集对照消融 · 专家盲评 · 原型迭代", a small magnifier icon, and note "验收：冻结配置·B0–B3·消融·盲评一致性·质量报告". Both bars are aligned to the month axis — phase one spanning months 1–12, phase two spanning months 13–24.

Bottom: three or four small dark-navy #1B3A5C diamond outline markers on the axis labelled "阶段验收点", and a tiny grey note "具体时间节点以立项通知书为准". All Chinese text rendered verbatim in dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.

---

## 8. F8 研究基础衔接图（nice · Framework · 16:9）

**中文图名**：研究基础与研究内容的衔接
**放置**：2.1 研究基础；`\label{fig:foundation-mapping}`
**配色**：Nature Blue + 灰（既有成果）

### 8.1 JSON 图规格

```json
{
  "diagram_type": "Foundation-to-research-content mapping diagram",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "physical_spec_and_typography": {
    "canvas_width": "140mm (NSFC A4 single column)",
    "font_family": "Source Han Sans CN / Microsoft YaHei (Chinese), Helvetica (Latin)",
    "font_hierarchy": {
      "title": "12pt bold",
      "primary_label": "10pt",
      "secondary_note": "8pt"
    },
    "stroke_hierarchy": {
      "container_border": "1.5pt solid",
      "internal_divider": "1.0pt solid",
      "flow_arrow": "1.5pt solid"
    }
  },
  "style_and_colors": {
    "background": "White (#FFFFFF)",
    "main_block_color_palette": {
      "Existing_Work": "#616161 1.5px solid border, white fill",
      "Bridge": "#8EAEC4 thin arrows",
      "Research_Content": "#2E6B9E 2px solid border, white fill"
    }
  },
  "layout_and_content_blocks": [
    {
      "relative_position": "Left Column",
      "shape": "Three stacked rounded rectangles, #616161 1.5px solid border, white fill",
      "exact_title_to_render_inside": "既有积累",
      "internal_content": {
        "layout": "three stacked boxes",
        "box_1": {"exact_text": "时序预测", "secondary_note": "DWT-Former · WaveKAN"},
        "box_2": {"exact_text": "多模态检索与VQA", "secondary_note": "FFMH · RSHR+ · RSSR"},
        "box_3": {"exact_text": "知识库与教学经历", "secondary_note": "元数据·来源·课程表达"}
      },
      "icon": "small icons: waveform, image-frame, database, monochrome line art",
      "flow": "Three thin grey arrows RIGHT into Bridge"
    },
    {
      "relative_position": "Center",
      "shape": "No box; thin #8EAEC4 arrows with small labels",
      "exact_floating_text": "方法衔接：曲线/变量/工况建模 | 跨模态表示/关系匹配 | 来源组织/课程设计",
      "icon": "three small connecting arrows, monochrome line art"
    },
    {
      "relative_position": "Right Column",
      "shape": "Three stacked rounded rectangles, #2E6B9E 2px solid border, white fill",
      "exact_title_to_render_inside": "研究内容",
      "internal_content": {
        "layout": "three stacked boxes",
        "box_1": {"exact_text": "① 联合知识约束", "secondary_note": "资源单元构建"},
        "box_2": {"exact_text": "② 跨模态证据关联", "secondary_note": "专业属性·来源位置"},
        "box_3": {"exact_text": "③ 四层质量验证", "secondary_note": "VRR·盲评·留出"}
      },
      "icon": "small icons: two-circle, matching-lines, four-bars, monochrome line art"
    },
    {
      "relative_position": "Bottom",
      "shape": "No box, centered small grey text",
      "exact_text": "方法衔接，非既有结论",
      "secondary_note": "联合/消融/盲评/留出仍需立项后验证"
    }
  ],
  "caption_note": [
    "图注：申请人既有研究在新能源时序建模（DWT-Former、WaveKAN）、多模态检索与视觉问答（FFMH、RSHR+、RSSR 等）和智能知识库/教学经历三方面的积累，为曲线与工况属性建模、跨模态表示与关系匹配、元数据与课程表达提供方法衔接；本图表示方法衔接关系，不将拟构建资源规模或验证结果表述为既有事实。"
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render the Chinese strings above verbatim.",
    "Left column grey borders (existing work), right column blue borders (research content), center thin arrows only.",
    "Icons monochrome line art only.",
    "NO emojis, NO 3D, NO gradients, NO decorative shadows.",
    "Flat vector, clean sans-serif labels, no text outside exact_* fields."
  ]
}
```

### 8.2 图像提示词（English, generation-ready）

Flat vector academic mapping diagram on a pure white #FFFFFF canvas, 16:9, connecting the applicant's existing research foundations to the three research contents.

Left column: three stacked rounded rectangles with thin grey #616161 borders, titled "既有积累", containing "时序预测 (DWT-Former · WaveKAN)", "多模态检索与VQA (FFMH · RSHR+ · RSSR)", "知识库与教学经历 (元数据·来源·课程表达)", each with a small monochrome line-art icon (waveform, image frame, database). Three thin grey #8EAEC4 arrows point right into a center corridor with the small label "方法衔接：曲线/变量/工况建模 | 跨模态表示/关系匹配 | 来源组织/课程设计" and three small connecting arrow icons.

Right column: three stacked rounded rectangles with medium-blue #2E6B9E 2px borders, titled "研究内容", containing "① 联合知识约束 (资源单元构建)", "② 跨模态证据关联 (专业属性·来源位置)", "③ 四层质量验证 (VRR·盲评·留出)", each with a matching monochrome icon (two overlapping circles, matching dot rows, four gate bars). Each left foundation box maps to the corresponding right content box via a thin arrow.

Bottom center, small grey text: "方法衔接，非既有结论" with a lighter note "联合/消融/盲评/留出仍需立项后验证". All Chinese text rendered verbatim in dark grey #333333 sans-serif, titles bold 12pt, body 10pt, notes 8pt. Flat vector, thin 1.5-2px outlines, white fills, no gradients, no shadows, no 3D, no emojis. Aspect ratio 16:9.

---

## 9. 完整性块与下一步

### 9.1 完整性块

```
- 已分析材料: main.pdf 全文、extraTex 章节结构、docs/03 与 docs/04、Figure Plan（8 图）
- 当前输出类型: 完整（配色决策 + 8 张图 JSON 规格 + 图像提示词，classic 风格族）
- 高置信信息: 三方法模块（公式 2–8）、B0–B3 对照与消融、四层门控、五维盲评、
              两年计划、研究基础成果清单
- 待确认信息: ① 申报系统图数/页数限制；② 中文标注在图像模型上的渲染准确性
              （需生成后人工核对 exact_* 文案）；③ 是否需要对 F2/F6/F7/F8 之外的
              图也全部成图，还是先出 4 张 must
- 建议补充材料: ① 若已有目标风格参考图，交给 color-expert 对齐；② 申报系统对
              图片数量与分辨率的硬性要求
```

### 9.2 推荐成图顺序

F1（总体框架）→ F3 → F4 → F5（三个方法模块）→ F6（实验矩阵）→ F2（动机图）→ F7（计划甘特）→ F8（基础衔接）。

每张图生成后：① 核对图上中文字符与 exact_* 一致；② 若模型渲染中文出错，改用"图上英文短标签 + 图注中文全称"的降级方案；③ 接入 `main.tex`：

```latex
\begin{figure}[!th]
    \begin{center}
        \includegraphics[width=0.85\linewidth]{figures/figX-name.png}
        \caption{...中文图注...}
        \label{fig:xxx}
    \end{center}
\end{figure}
```

### 9.3 后续链路

- 配色若有调整（如改为 Okabe-Ito 或需要更柔和的副色）→ 回到 `academic-figure-color-expert` 重新出决策。
- 若用户想要 pastel/airy 风格 → 转 `academic-figure-prompt-pastel`（P1/P2/P3），本包 classic 规格作废。
- 生图阶段：逐张调用 imagegen 能力，生成后按 §9.2 核对与接入。
