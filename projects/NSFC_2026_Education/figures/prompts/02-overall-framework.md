# F02 · 总体研究框架图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：总体研究框架图 ｜ **类型**：Overall Research Framework Diagram（概念对位型，非流程图）
> **状态**：MANDATORY ｜ **优先级**：P0 ｜ **长宽比**：16:9

---

## 一、图形目的（Diagram Purpose）

说明本项目**研究什么、三项研究内容在概念上如何互相支撑**，并展示"研究内容 ↔ 科学问题 ↔ 研究目标 ↔ 创新点"的四重对位与横贯三项内容的统一验证体系。

**一句话结论**：三项研究内容沿"资源单元怎么建—单元内关系怎么判—单元质量怎么验"层层递进，共享受控输入与统一验证体系，各自锚定一个可证伪的科学问题。

**关键约束**：本图是**概念结构图**，全部使用名词性标题，**严禁出现任何动作序列词、时间节点或执行步骤**（那属于技术路线图）。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Overall Research Framework Diagram (conceptual alignment, not a process flow)",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin and digits",
    "font_hierarchy": {
      "zone_title": "11pt bold",
      "module_title": "10pt bold",
      "sub_title": "8.5pt medium",
      "primary_label": "8pt regular",
      "secondary_note": "7pt regular"
    },
    "stroke_hierarchy": {
      "level_1_border": "2.0pt solid",
      "level_2_border": "1.5pt solid",
      "level_3_border": "1.0pt solid",
      "main_chain_arrow": "2.0pt solid with 4px head",
      "alignment_arrow": "1.0pt solid with 3px head",
      "shared_effect_line": "1.0pt dashed"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #5BA0D0",
    "main_block_color_palette": {
      "research_content_module": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "sub_block": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "input_material": "Light Blue (#5BA0D0) 1.0pt solid border, white fill",
      "de_emphasised": "Pale Blue Grey (#8EAEC4) 1.0pt solid border, white fill",
      "zone_lane": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "scope_note": "Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill"
    },
    "text_colors": {
      "zone_title": "#1B3A5C",
      "module_title": "#1B3A5C",
      "sub_title": "#2E6B9E",
      "body_label": "#333333",
      "de_emphasised_label": "#4D4D4D"
    },
    "flow_arrow_colors": {
      "main_chain": "Dark Navy (#1B3A5C) 2.0pt solid, filled head",
      "alignment_mapping": "Medium Blue (#2E6B9E) 1.0pt solid, thin head",
      "shared_validation": "Dark Grey (#4D4D4D) 1.0pt dashed, thin head"
    },
    "forbidden_colors": "Do NOT use any warm, red, orange or brown accent anywhere in this figure."
  },
  "layout_and_content_blocks": [
    {
      "id": "ZONE_INPUT",
      "relative_position": "Left column, occupies leftmost 17% of canvas width, vertically spanning the main chain row",
      "shape": "Vertical lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "受控资源输入",
      "internal_content": {
        "layout": "Four stacked light-blue boxes",
        "box_1": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "shield with check mark, thin grey line art",
          "exact_text": "公开许可 · 明确授权 · 自主编写"
        },
        "box_2": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "academic building outline",
          "exact_text": "示范课程模块\\n新能源数据分析与功率预测"
        },
        "box_3": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "exact_title_to_render_inside": "拟构建 4 个知识模块",
          "exact_text": "运行数据与变量认知\\n预处理与可视化\\n预测建模与实验\\n结果评价与工程案例"
        },
        "box_4": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill, with one de-emphasised inner line",
          "exact_title_to_render_inside": "核心模态",
          "exact_text": "课程文本 · 运行曲线图表 · 设备结构图",
          "exact_floating_text_de_emphasised": "扩展模态：实验代码 · 产业案例（单独报告）"
        }
      },
      "flow": "One thick dark navy arrow pointing RIGHT into RC1"
    },
    {
      "id": "RC1",
      "relative_position": "Main chain, first of three, centre-left, occupies 20% of canvas width",
      "shape": "Large rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "研究内容一\\n产业任务—课程知识联合约束的资源单元构建",
      "corner_tag": { "shape": "Small Medium Blue (#2E6B9E) 1.0pt border tag at top-right corner", "exact_label": "创新点一" },
      "icon": "two converging arrows merging into one, thin grey line art",
      "internal_content": {
        "layout": "Three stacked medium-blue sub-blocks, maximum three lines total",
        "sub_1": { "exact_text": "产业任务知识 + 课程知识" },
        "sub_2": { "exact_text": "任务—对象—条件—知识点—片段—证据位置" },
        "sub_3": { "exact_text": "对照：无知识 / 单一知识 / 联合知识" }
      },
      "flow": "Thick dark navy arrow pointing RIGHT to RC2"
    },
    {
      "id": "RC2",
      "relative_position": "Main chain, second of three, centre, occupies 20% of canvas width",
      "shape": "Large rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "研究内容二\\n专业属性与来源证据约束的跨模态资源关联",
      "corner_tag": { "shape": "Small Medium Blue (#2E6B9E) 1.0pt border tag at top-right corner", "exact_label": "创新点二" },
      "icon": "two linked nodes with a verification tick, thin grey line art",
      "internal_content": {
        "layout": "Three stacked medium-blue sub-blocks, maximum three lines total",
        "sub_1": { "exact_text": "对象 · 变量 · 单位 · 工况 · 时间窗口 · 来源位置" },
        "sub_2": { "exact_text": "关系类型：解释 / 实例 / 计算实验 / 对照 / 出处支持" },
        "sub_3": { "exact_text": "准入：语义 ∧ 专业条件 ∧ 证据位置" }
      },
      "flow": "Thick dark navy arrow pointing RIGHT to RC3"
    },
    {
      "id": "RC3",
      "relative_position": "Main chain, third of three, centre-right, occupies 20% of canvas width",
      "shape": "Large rectangular container, Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "exact_title_to_render_inside": "研究内容三\\n资源内在质量的四层联合验证",
      "corner_tag": { "shape": "Small Medium Blue (#2E6B9E) 1.0pt border tag at top-right corner", "exact_label": "创新点三" },
      "icon": "four stacked horizontal layers with a gate, thin grey line art",
      "internal_content": {
        "layout": "Three stacked medium-blue sub-blocks, maximum three lines total",
        "sub_1": { "exact_text": "四层门控：内容 · 课程 · 模态 · 证据" },
        "sub_2": { "exact_text": "任一层严重错误即拒绝" },
        "sub_3": { "exact_text": "主指标：有效资源单元通过率 VRR" }
      },
      "flow": "Thick dark navy arrow pointing RIGHT into ZONE_GOAL"
    },
    {
      "id": "BAND_QUESTION",
      "relative_position": "Directly below the main chain, spanning the same horizontal extent as RC1 to RC3",
      "shape": "Horizontal lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "关键科学问题",
      "internal_content": {
        "layout": "Three equal-width medium-blue boxes, each strictly vertically aligned under RC1, RC2 and RC3 respectively",
        "q_1": { "exact_title_to_render_inside": "科学问题一", "exact_text": "联合知识约束的增量作用与适用边界" },
        "q_2": { "exact_title_to_render_inside": "科学问题二", "exact_text": "专业属性与来源位置对关联正确性的共同决定机制" },
        "q_3": { "exact_title_to_render_inside": "科学问题三", "exact_text": "不依赖学生行为数据的资源内在质量独立效度" }
      },
      "connector": "One thin medium-blue vertical double-ended-free arrow from each research-content module DOWN to its aligned question box. Three parallel lines, no crossing."
    },
    {
      "id": "ZONE_GOAL",
      "relative_position": "Right column, occupies rightmost 17% of canvas width, vertically spanning the main chain row",
      "shape": "Vertical lane, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_zone_title": "研究目标",
      "internal_content": {
        "layout": "One dark-navy overall-goal box on top, three medium-blue sub-goal boxes stacked below",
        "overall": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt border, white fill",
          "exact_title_to_render_inside": "总体目标",
          "exact_text": "揭示三类约束对资源构建质量的作用机制\\n形成可验证、可追溯的构建与质控方法"
        },
        "goal_1": { "shape": "Medium Blue (#2E6B9E) 1.5pt border", "exact_title_to_render_inside": "目标一", "exact_text": "边界 F1 · 知识覆盖 · 属性一致性" },
        "goal_2": { "shape": "Medium Blue (#2E6B9E) 1.5pt border", "exact_title_to_render_inside": "目标二", "exact_text": "Recall@1 · Recall@5 · MRR\\n关系 F1 · 来源定位准确率" },
        "goal_3": { "shape": "Medium Blue (#2E6B9E) 1.5pt border", "exact_title_to_render_inside": "目标三", "exact_text": "VRR 主指标 · 五维专家盲评\\nKrippendorff's alpha · 人工修订时间" }
      },
      "connector": "Three thin medium-blue horizontal arrows from RC1, RC2, RC3 to 目标一, 目标二, 目标三 respectively. Draw these along the upper edge so they do not collide with the main chain arrows."
    },
    {
      "id": "BAND_VALIDATION",
      "relative_position": "Bottom band, FULL canvas width, spanning underneath the input lane, the question band and the goal lane",
      "shape": "Full-width horizontal band, light grey (#F7F7F7) fill, Dark Navy (#1B3A5C) 1.5pt solid border",
      "exact_zone_title": "统一验证体系",
      "internal_content": {
        "layout": "Six equal-width medium-blue chips in a single row",
        "chip_1": { "exact_label": "受控输入与统一标注" },
        "chip_2": { "exact_label": "B0–B3 对照" },
        "chip_3": { "exact_label": "逐项消融" },
        "chip_4": { "exact_label": "跨来源留出" },
        "chip_5": { "exact_label": "独立专家盲评" },
        "chip_6": { "exact_label": "负结果如实报告与边界界定" }
      },
      "connector": "Three dark-grey 1.0pt DASHED arrows rising from this band up to RC1, RC2 and RC3, indicating that the validation system acts on all three research contents simultaneously. This band must read as spanning all three, NOT as a downstream stage of RC3."
    },
    {
      "id": "SCOPE_NOTE",
      "relative_position": "Bottom-right corner, smallest element on the canvas, below or beside the validation band",
      "shape": "Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill",
      "exact_text": "研究范围不含：学生画像 · 学习行为分析 · 个性化推荐 · 学习效果预测 · 生产平台接入",
      "typography": "7pt regular, #4D4D4D, lowest visual weight on the canvas"
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text, including lane titles.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. Only lanes and bands may use light grey (#F7F7F7) fill.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E, #5BA0D0, plus neutral greys #8EAEC4, #333333, #4D4D4D, #CCCCCC.",
    "This is a CONCEPTUAL ALIGNMENT diagram, not a process flow. Use noun-phrase titles only. Do NOT render any action verb, ordinal step number, stage label, month, year, timeline, or Gantt element.",
    "The 统一验证体系 band MUST span the full canvas width and connect upward to all three research-content modules with dashed arrows. It must NOT be drawn as a downstream stage after 研究内容三.",
    "The three science-question boxes MUST be strictly vertically aligned under 研究内容一, 研究内容二 and 研究内容三 respectively. The three alignment arrows must be parallel and must not cross.",
    "Each research-content module contains at most three inner text lines. Do not expand any internal mechanism, gate logic, scoring function, or field schema — those belong to other figures.",
    "The visual focus is the three-module main chain AS A GROUP, achieved through its uniform 2.0pt borders and the thick connecting arrows. Exactly ONE focus is permitted: do NOT single out any individual module, question box, goal box or band with a heavier border, larger type, coloured fill, or extra emphasis of any kind. The three research-content modules must be visually identical in weight and size.",
    "The 扩展模态 line and the 研究范围不含 note use pale blue grey #8EAEC4 with 7pt text and must carry the lowest visual weight on the canvas.",
    "Quantities that describe future work must keep their 拟构建 prefix exactly as written.",
    "Icons are monochrome thin grey line art, at most one per research-content module, no larger than 1.6x the adjacent text height.",
    "Do NOT render any mathematical formula, loss function, weight symbol, or equation. Only the bare metric names listed in exact_* fields are allowed.",
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
A flat 2D vector academic research-framework diagram for a Chinese research grant proposal, on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: the conceptual structure of a project on constructing and quality-controlling multimodal teaching resources for university new-energy courses — three research contents form one progressive chain, each anchored to a scientific question, a research goal and an innovation point, all sharing one unified validation system.

Composition: a horizontal three-stage main chain across the centre. On the far left, a pale grey vertical lane titled 受控资源输入 holds four light-blue boxes: 公开许可 · 明确授权 · 自主编写; 示范课程模块 新能源数据分析与功率预测; 拟构建 4 个知识模块 with four sub-lines; and 核心模态 课程文本 · 运行曲线图表 · 设备结构图 with a visually faded line 扩展模态：实验代码 · 产业案例（单独报告）. The chain itself is three large dark-navy 2pt bordered containers joined by thick dark-navy right arrows, titled 研究内容一 产业任务—课程知识联合约束的资源单元构建, 研究内容二 专业属性与来源证据约束的跨模态资源关联, and 研究内容三 资源内在质量的四层联合验证, each with a small corner tag 创新点一 / 创新点二 / 创新点三 and at most three inner medium-blue lines. Directly beneath, a pale grey band titled 关键科学问题 holds three boxes 科学问题一, 科学问题二, 科学问题三, each strictly vertically aligned under its research content and joined by thin parallel non-crossing arrows. On the far right, a pale grey vertical lane titled 研究目标 holds a dark-navy 总体目标 box above three medium-blue boxes 目标一, 目标二, 目标三. Across the entire bottom, a full-width band titled 统一验证体系 holds six chips — 受控输入与统一标注, B0–B3 对照, 逐项消融, 跨来源留出, 独立专家盲评, 负结果如实报告与边界界定 — and sends three dashed arrows upward to all three research contents, so it clearly spans them rather than following the third one. A tiny dashed pale-grey note sits in the bottom-right corner.

Supporting modules: sparse monochrome thin-grey line icons — converging arrows, linked nodes with a tick, stacked gate layers, shield with check, academic building.

Visual tone: restrained, scholarly, print-oriented. Material: white fills, coloured borders only, 3pt corner radius, borders 1.0/1.5/2.0pt. Palette strictly #1B3A5C, #2E6B9E, #5BA0D0 plus neutral greys #8EAEC4, #333333, #4D4D4D — no warm, red, orange or brown tones.

Typography: Source Han Sans / Noto Sans CJK SC; lane titles 11pt bold, module titles 10pt bold, labels 8pt, faded notes 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: action verbs, step numbers, timelines, Gantt bars, months or years; any formula or equation; any internal gate logic or field schema; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 16:9.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 三项研究内容主框、总体目标框、主链箭头、验证体系带边框 |
| secondary | `#2E6B9E` | 子块、科学问题框、目标一二三、创新点角标、对位箭头 |
| tertiary | `#5BA0D0` | 输入区素材框 |
| gray | `#8EAEC4` | 扩展模态行、研究范围声明框 |
| arrow | `#4D4D4D` | 验证体系虚线上引箭头 |
| section_bg | `#F7F7F7` | 输入/问题/目标/验证四条泳道与条带 |
| **禁用** | `#A64B2A` | 本图不含失败语义 |

**唯一焦点**：RC1→RC2→RC3 主链整体（作为一个视觉组，靠 2.0pt 边框与主链粗箭头形成，不额外加粗单个模块）

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 2 项目总体研究框架。项目以受控资源输入为起点，围绕"新能源数据分析与功率预测"示范课程模块，依次开展产业任务—课程知识联合约束的资源单元构建、专业属性与来源证据约束的跨模态资源关联、以及资源内在质量的四层联合验证；三项研究内容分别锚定一个关键科学问题与一项研究目标，并共享受控输入与统一标注、B0–B3 对照、逐项消融、跨来源留出与独立专家盲评构成的统一验证体系。
- 资源单元五元组的完整定义 $u=(c,a,m,e,s)$ 及各字段含义 → 图注或 F04。
- 联合知识约束打分、关系评分、四层质量合成与 VRR 的完整数学表达式 → 图注或正文，不上图。
- B0/B1/B2/B3 的具体含义（人工整理 / 通用大模型 / 仅文本 RAG / 完整方法）→ 图注。
- 拟构建规模（≥300 个资源单元、抽取 120 个盲评单元、≥3 名专家）→ 图注，不上图。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（conceptual framework，非流程图） |
| 全部模块有标书出处 | ✅ 2.1 / 2.2 / 2.3 / 3.1 / 4.2–4.4 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 16:9 |
| 物理规格与字体块 | ✅ 183mm / 11-10-8.5-8-7pt / 1.0-1.5-2.0pt |
| 有彩色 ≤3 | ✅ 3 种（+ 中性 `#8EAEC4`） |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 三项研究内容各 1 图标 |
| 无空壳模块 | ✅ 每模块 3 行内容 |
| 负向约束齐备 | ✅ 含禁动作词/时间轴/公式、NO emojis / NO 3D |
| 与 F03 的防混淆约束 | ✅ 明确禁止动作词、步骤号、时间节点 |
| 推断或待确认项 | 无。全部内容可溯源至标书 |
