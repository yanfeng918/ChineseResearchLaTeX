# F07 · 研究基础与研究内容支撑对位图 — Figure Prompt Package

> **自足声明**：本文件为独立 prompt 包，下游图像模型无需访问标书 PDF、Figure Plan 或 Visual Logic。
> **图名**：研究基础与研究内容支撑对位图 ｜ **类型**：Capability-to-Task Alignment Diagram
> **状态**：RECOMMENDED ｜ **优先级**：P2（版面允许时采用；页面压力下可整体删除，不影响 F01–F06 完整性）｜ **长宽比**：16:9

---

## 一、图形目的（Diagram Purpose）

证明**可行性与能力对位**：申请人三类前期积累分别支撑三项研究内容的哪一环节，同时以专门的边界带明确区分"已有能力"与"本项目仍需新开展并验证的内容"。

**一句话结论**：三类前期积累在方法与对象层面分别对位三项研究内容，但课程对齐、出处证据与四层质量效度仍是本项目需新开展并验证的部分。

**填补的信息缺口**：F01–F06 均聚焦研究本身，不涉及申请人能力；标书研究基础部分的四路对位陈述被论文清单与项目清单稀释，图示可一次建立"能力—任务"映射。

**最大风险与对策**：本图极易被误读为"前期成果已证明本项目结论"。底部边界带为**强制元素**，不得省略、不得弱化到不可读。

---

## 二、JSON Figure Spec

```json
{
  "diagram_type": "Capability-to-Task Alignment Diagram with Explicit Validation Boundary",
  "diagram_title_rendering": "None",
  "aspect_ratio": "16:9",
  "language_of_rendered_text": "Simplified Chinese (render every exact_* string verbatim, character for character)",
  "physical_spec_and_typography": {
    "canvas_width": "183mm (double column, full text width of an A4 proposal page)",
    "font_family": "Source Han Sans / Noto Sans CJK SC for Chinese; Arial for Latin, journal names and digits",
    "font_hierarchy": {
      "zone_title": "10pt bold",
      "card_title": "9.5pt bold",
      "primary_label": "8pt regular",
      "connector_label": "7.5pt regular",
      "boundary_note": "7pt regular"
    },
    "stroke_hierarchy": {
      "level_1_border": "2.0pt solid",
      "level_2_border": "1.5pt solid",
      "level_3_border": "1.0pt solid",
      "support_arrow": "1.0pt solid with 3px head",
      "shared_condition_arrow": "1.0pt dashed",
      "boundary_border": "1.5pt DASHED"
    }
  },
  "style_and_colors": {
    "background": "Pure white (#FFFFFF)",
    "palette_name": "Nature Blue (classic academic family)",
    "chromatic_budget": "3 chromatics only: #1B3A5C, #2E6B9E, #5BA0D0",
    "main_block_color_palette": {
      "research_content_card": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
      "foundation_card": "Medium Blue (#2E6B9E) 1.5pt solid border, white fill",
      "inner_item": "Light Blue (#5BA0D0) 1.0pt solid border, white fill",
      "connector_label_tag": "Light Blue (#5BA0D0) 1.0pt solid border, white fill, small rectangular tag on the connector line",
      "condition_band": "Light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "boundary_band": "FOCUS: Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill"
    },
    "text_colors": {
      "zone_title": "#1B3A5C",
      "research_content_title": "#1B3A5C",
      "foundation_title": "#2E6B9E",
      "body_label": "#333333",
      "boundary_label": "#4D4D4D"
    },
    "flow_arrow_colors": {
      "capability_support": "Medium Blue (#2E6B9E) 1.0pt solid, thin head",
      "shared_condition": "Dark Grey (#4D4D4D) 1.0pt dashed"
    },
    "forbidden_colors": "Do NOT use any warm, red, orange or brown accent anywhere in this figure."
  },
  "layout_and_content_blocks": [
    {
      "id": "ZONE_FOUNDATION",
      "relative_position": "Left column, occupies leftmost 30% of canvas width",
      "shape": "Vertical group of three medium-blue cards stacked with even spacing",
      "exact_zone_title": "申请人前期积累",
      "internal_content": {
        "card_A": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
          "icon": "line chart with wind turbine, thin grey line art",
          "exact_title_to_render_inside": "A 新能源时序建模与功率预测",
          "inner_items": [
            { "exact_text": "DWT-Former（Energy, 2025）" },
            { "exact_text": "WaveKAN（Neurocomputing, 2026）" },
            { "exact_text": "在研：光伏功率预测项目" }
          ]
        },
        "card_B": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
          "icon": "two linked nodes across image and text, thin grey line art",
          "exact_title_to_render_inside": "B 多模态理解与跨模态关联",
          "inner_items": [
            { "exact_text": "跨模态检索哈希（IEEE SPL, 2026）" },
            { "exact_text": "RSHR+（ESWA, 2026）· RSSR（CVIU, 2026）" },
            { "exact_text": "视觉问答（Machine Learning, 2024）" },
            { "exact_text": "在研：多模态融合技术项目" }
          ]
        },
        "card_C": {
          "shape": "Medium Blue (#2E6B9E) 1.5pt border, white fill",
          "icon": "database with question mark, thin grey line art",
          "exact_title_to_render_inside": "C 知识库研发与课程教学",
          "inner_items": [
            { "exact_text": "智能知识库与问答系统研发" },
            { "exact_text": "人工智能与深度学习课程教学经历" }
          ]
        }
      }
    },
    {
      "id": "ZONE_CONNECTOR",
      "relative_position": "Centre column, occupies 40% of canvas width — reserved almost entirely for connector lines and their labels",
      "shape": "Open area, no container box",
      "exact_zone_title": "支撑环节",
      "internal_content": {
        "layout": "Five thin medium-blue arrows crossing from left cards to right cards, each carrying a small light-blue rectangular label tag at its midpoint. Lines may cross but must be offset to avoid overlap, and no two lines may run parallel in the same colour along the same path.",
        "connector_1": { "from": "card_A", "to": "RC1", "exact_label_tag": "工况与参数属性理解" },
        "connector_2": { "from": "card_A", "to": "RC2", "exact_label_tag": "曲线 · 变量 · 单位 · 时间窗口建模\\n困难负例构造" },
        "connector_3": { "from": "card_B", "to": "RC2", "exact_label_tag": "资源片段表示 · 候选关系生成\\n关系匹配 · 误差分析" },
        "connector_4": { "from": "card_C", "to": "RC1", "exact_label_tag": "来源字段与资源元数据组织" },
        "connector_5": { "from": "card_C", "to": "RC3", "exact_label_tag": "课程表达与专家评价量表设计" }
      }
    },
    {
      "id": "ZONE_CONTENT",
      "relative_position": "Right column, occupies rightmost 30% of canvas width",
      "shape": "Vertical group of three dark-navy cards stacked with even spacing",
      "exact_zone_title": "本项目研究内容",
      "internal_content": {
        "RC1": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
          "exact_title_to_render_inside": "研究内容一",
          "exact_text": "联合知识约束的资源单元构建"
        },
        "RC2": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
          "exact_title_to_render_inside": "研究内容二",
          "exact_text": "专业属性与来源证据约束的跨模态关联"
        },
        "RC3": {
          "shape": "Dark Navy (#1B3A5C) 2.0pt solid border, white fill",
          "exact_title_to_render_inside": "研究内容三",
          "exact_text": "四层资源内在质量验证"
        }
      }
    },
    {
      "id": "BAND_CONDITION",
      "relative_position": "First full-width band below the three columns, height <= 14% of canvas",
      "shape": "Full-width horizontal band, light grey (#F7F7F7) fill, 1.0pt #CCCCCC border",
      "exact_band_title": "实验与团队条件",
      "internal_content": {
        "layout": "Three equal-width light-blue boxes in one row",
        "box_1": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "server rack outline, thin grey line art",
          "exact_title_to_render_inside": "计算条件",
          "exact_text": "NVIDIA A40 × 8\\nRTX 3090 Ti × 6"
        },
        "box_2": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "group of people outline, thin grey line art",
          "exact_title_to_render_inside": "团队",
          "exact_text": "约 10 名研究生\\n资源整理 · 标注 · 训练 · 复核 · 原型实现"
        },
        "box_3": {
          "shape": "Light Blue (#5BA0D0) 1.0pt border, white fill",
          "icon": "single person outline, thin grey line art",
          "exact_title_to_render_inside": "申请人负责",
          "exact_text": "科学问题凝练 · 方案设计\\n合规边界 · 实验质量控制"
        }
      },
      "connector": "Three dark-grey 1.0pt dashed arrows rising from this band to 研究内容一, 研究内容二 and 研究内容三, indicating that these conditions support all three contents"
    },
    {
      "id": "BAND_BOUNDARY",
      "relative_position": "Bottom-most full-width band, height <= 14% of canvas",
      "shape": "Full-width horizontal band, Pale Blue Grey (#8EAEC4) 1.5pt DASHED border, white fill, NO arrows entering or leaving it",
      "exact_band_title": "仍需本项目新开展并验证",
      "internal_content": {
        "layout": "One row of four small pale text chips, plus one full-width note line beneath",
        "chips": {
          "chip_1": { "exact_label": "课程对齐" },
          "chip_2": { "exact_label": "出处证据" },
          "chip_3": { "exact_label": "四层质量效度" },
          "chip_4": { "exact_label": "独立专家盲评与跨来源留出" }
        },
        "note_line": {
          "exact_text": "前期成果不作为本项目假设已成立的证据；课程授权与专家名单在立项后落实。",
          "typography": "7pt regular, #4D4D4D"
        }
      }
    }
  ],
  "RENDERING_RULES_AND_NEGATIVE_PROMPT_INSTRUCTIONS": [
    "Render text ONLY within designated exact_* fields. Render every Chinese string verbatim, character for character, horizontally. Never rotate or vertically stack Chinese text, including column titles.",
    "All container boxes use WHITE (#FFFFFF) fill with COLORED BORDERS ONLY. Only the 实验与团队条件 band may use light grey (#F7F7F7) fill.",
    "Use at most three chromatic colours: #1B3A5C, #2E6B9E, #5BA0D0, plus neutral greys #8EAEC4, #333333, #4D4D4D, #CCCCCC.",
    "MANDATORY ELEMENT: the bottom band 仍需本项目新开展并验证 must be rendered in full, with a dashed pale-grey border and NO arrows entering or leaving it. It must be clearly legible but carry the lowest visual weight on the canvas. Omitting or truncating this band is not acceptable — it prevents the figure from being read as a claim that prior results already prove the project's hypotheses.",
    "The five capability-support arrows may cross, but each must be offset to remain individually traceable. Do NOT draw two same-coloured lines running parallel along the same path. Each arrow carries exactly one small label tag at its midpoint.",
    "Journal names appear only as short parenthetical forms exactly as written. Do NOT render full paper titles, author lists, DOIs, volume or page numbers, project grant numbers, funding amounts, or any student name.",
    "Each foundation card lists at most four inner items. Do NOT expand this figure into a curriculum-vitae style publication list.",
    "Do NOT expand any method mechanism. The research-content cards carry only their titles and a one-line description; the gate logic, field schema, relation scoring and VRR belong to other figures.",
    "Do NOT render any project execution timeline, month, year range, stage number, or Gantt element.",
    "Do NOT render any planned construction scale, expert count, blind-review result, or any other future outcome as if it were achieved. This figure describes existing capability only.",
    "Icons are monochrome thin grey line art, at most one per card or box, no larger than 1.6x the adjacent text height.",
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
A flat 2D vector academic capability-alignment diagram for a Chinese research grant proposal, on a pure white background. All on-figure text is Simplified Chinese and must be reproduced verbatim, horizontally, never rotated.

Core subject: how three strands of the applicant's existing research experience map onto the three research contents of the proposed project — and, equally important, which parts of the project still remain to be newly carried out and validated.

Composition: two facing columns with a wide open middle reserved for connector lines. The left column, titled 申请人前期积累, holds three medium-blue cards: A 新能源时序建模与功率预测 listing DWT-Former（Energy, 2025）, WaveKAN（Neurocomputing, 2026）, 在研：光伏功率预测项目; B 多模态理解与跨模态关联 listing 跨模态检索哈希（IEEE SPL, 2026）, RSHR+（ESWA, 2026）· RSSR（CVIU, 2026）, 视觉问答（Machine Learning, 2024）, 在研：多模态融合技术项目; and C 知识库研发与课程教学 listing 智能知识库与问答系统研发, 人工智能与深度学习课程教学经历. The right column, titled 本项目研究内容, holds three dark-navy cards 研究内容一 联合知识约束的资源单元构建, 研究内容二 专业属性与来源证据约束的跨模态关联, 研究内容三 四层资源内在质量验证.

Five thin medium-blue arrows cross the middle space, each carrying one small light-blue label tag at its midpoint: A to 研究内容一 tagged 工况与参数属性理解; A to 研究内容二 tagged 曲线 · 变量 · 单位 · 时间窗口建模 困难负例构造; B to 研究内容二 tagged 资源片段表示 · 候选关系生成 关系匹配 · 误差分析; C to 研究内容一 tagged 来源字段与资源元数据组织; C to 研究内容三 tagged 课程表达与专家评价量表设计. The lines may cross but each must stay individually traceable through careful offsetting.

Below sits a pale grey band 实验与团队条件 with three light-blue boxes — 计算条件 NVIDIA A40 × 8 RTX 3090 Ti × 6, 团队 约 10 名研究生 资源整理 · 标注 · 训练 · 复核 · 原型实现, and 申请人负责 科学问题凝练 · 方案设计 合规边界 · 实验质量控制 — sending three dashed arrows up to the three research contents. At the very bottom, a mandatory dashed pale-grey band titled 仍需本项目新开展并验证 holds four faint chips 课程对齐, 出处证据, 四层质量效度, 独立专家盲评与跨来源留出, and the note 前期成果不作为本项目假设已成立的证据；课程授权与专家名单在立项后落实. This band has no arrows entering or leaving it and carries the lowest visual weight, yet must remain fully legible.

Supporting modules: sparse monochrome thin-grey line icons — line chart with wind turbine, linked image-text nodes, database with question mark, server rack, group of people, single person.

Visual tone: restrained, factual, print-oriented. Material: white fills, coloured borders only, 3pt corner radius, borders 1.0/1.5/2.0pt. Palette strictly #1B3A5C, #2E6B9E, #5BA0D0 plus neutral greys #8EAEC4, #333333, #4D4D4D — no warm, red, orange or brown tones.

Typography: Source Han Sans / Noto Sans CJK SC; column titles 10pt bold, card titles 9.5pt bold, labels 8pt, connector tags 7.5pt, boundary note 7pt. Canvas width 183mm, white space at least 70%.

Strictly exclude: full paper titles, author lists, DOIs, volume or page numbers, grant numbers, funding amounts, student names; any CV-style publication listing; any method mechanism, gate logic, field schema or VRR; any timeline, month, year range or Gantt element; any planned scale or future result presented as achieved; gradients, glow, 3D, shadows, emojis, decorative backgrounds, title bars, captions, legends; students, learning behaviour, recommendation or platform deployment.

Aspect ratio 16:9.
```

---

## 四、调色板与语义

| 角色 | HEX | 本图用途 |
|------|-----|---------|
| primary | `#1B3A5C` | 右栏三项研究内容卡片、栏标题 |
| secondary | `#2E6B9E` | 左栏三类积累卡片、五条支撑连线 |
| tertiary | `#5BA0D0` | 卡片内条目、连线标签牌、条件带三框 |
| gray | `#8EAEC4` | **底部边界带（强制元素）** |
| arrow | `#4D4D4D` | 条件带虚线上引、边界带文字 |
| section_bg | `#F7F7F7` | 实验与团队条件带 |
| **禁用** | `#A64B2A` | 研究基础图不含失败语义 |

**唯一焦点**：底部「仍需本项目新开展并验证」边界带——注意此处焦点通过**位置与不可省略性**实现，而非视觉加重；该带视觉权重最低但必须完全可读。

---

## 五、Caption Reserve（不上图，留给图注）

- 图注建议：图 7 研究基础与研究内容的支撑对位。申请人在新能源时序建模与功率预测、多模态理解与跨模态关联、知识库研发与课程教学三方面的积累，分别为本项目的资源单元构建、跨模态证据关联与四层质量验证提供工况与参数属性理解、资源片段表示与关系匹配、以及来源字段组织与课程表达等方法基础；现有计算与团队条件可支持对照、消融与本地原型实验。上述基础属于方法与对象层面的衔接，不构成本项目假设已经成立的证据；课程对齐、出处证据与四层质量效度仍需通过消融、独立专家盲评和跨来源留出测试加以验证。
- 论文完整标题、作者列表、卷期页码、DOI → 正文与参考文献。
- 在研项目的资助机构、项目类别、批准号、起止年月、获资助金额 → 正文（（二）3. 正在承担的相关科研项目）。
- 研究生成员姓名与个人任务分工 → 正文。
- 尚缺少的实验条件与拟解决途径 → 正文（（二）2. 工作条件）。

---

## 六、完整性块（Completeness Block）

| 项 | 状态 |
|----|------|
| 图类型 | ✅ 明确（capability-to-task alignment） |
| 全部模块有标书出处 | ✅ （二）1.1 / 1.2 / 1.3 / 1.4 / 2.1 |
| 全部可见文字锁定在 `exact_*` | ✅ |
| aspect_ratio 来自 Figure Plan | ✅ 16:9 |
| 物理规格与字体块 | ✅ 183mm / 10-9.5-8-7.5-7pt / 1.0-1.5-2.0pt |
| 有彩色 ≤3 | ✅ 3 种 |
| 白底 + 彩色边框 | ✅ |
| 每个主要块有图标或视觉锚点 | ✅ 六个图标 |
| 无空壳模块 | ✅ |
| 边界带为强制元素 | ✅ 明确写入 MANDATORY ELEMENT 规则 |
| 隐私与事务信息剔除 | ✅ 禁批准号、经费、学生姓名、论文全称 |
| 未来事实口径 | ✅ 明确禁止将拟构建规模或盲评结果呈现为已达成 |
| 负向约束齐备 | ✅ 含禁简历式罗列/禁时间轴/禁机制展开、NO emojis / NO 3D |
| 与 F02 的防混淆约束 | ✅ F02 为研究设计内部对位，本图为申请人能力对外部对位，无共享模块 |
| 推断或待确认项 | 无。全部内容可溯源至标书（二）1.1–1.4、2.1 |
