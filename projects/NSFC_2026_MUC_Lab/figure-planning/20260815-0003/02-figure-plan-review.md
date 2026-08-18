# Figure Plan Review — NSFC_2026_MUC_Lab

- `plan_version`: reviewed-v2
- `source_pdf`: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_MUC_Lab/main.pdf`
- `source_sha256`: `5fae172cd362836662f99697a98f04855bc78938c0fb8939208ab82a54a9fa77`
- `reviewer`: 未参与规划的独立子代理首轮 + 主代理裁决与复审
- `review_rounds`: 初轮审核 + 1 次修订复审（未用满第二轮）
- `style_family`: `classic_academic`
- `project_title_zh`: 场景文字增强的维吾尔语多模态表征融合与跨语言图像理解（用户 2026-08-15 确认；图内不渲染全称）
- `baseline_codes_confirmed`: B0=多语 CLIP 零样本；B1=无文字通道；B2=OCR—翻译流水线；完整模型无 B3（用户 2026-08-15 确认；图内不渲染代号）
- `image_backend_calls`: 0

---

## 1. 总体结论

**`pass_with_revisions`**

| | 分 |
|---|---:|
| `score_before` | 72.5 / 100 |
| `score_after` | 93 / 100 |
| 证据忠实 after | 25 / 25 |
| 未解决 blocker | 无 |
| 未解决 major | 无 |

首轮因篇幅过载、F5 优先级倒置、F3/F4 复刻验证清单、F4 空矩阵图型、F6 不适配等 major 未过闸。修订后绘制集为 **F1 + F2 + F3 + F5**（3 must + 1 strong）；F4、F6 改为正文表/文字。科学主线未推倒。

独立首轮详见工作区日志；本文件为裁决后的可执行计划。阶段三只使用下文 `Audited Figure Plan`。

---

## 2. 审核矩阵

计分规则：无问题得满分；未解决 blocker 该项 0；未解决 major 该项最高为权重 60%；每个未解决 minor 扣该项权重 10%。

| 维度 | 权重 | before | after | 结论 | 证据 | 受影响图 | 修改动作 |
|---|---:|---:|---:|---|---|---|---|
| 证据忠实 | 25 | 22.5 | 25 | 通过 | 节点/公式可回溯；无实测、无「5 个百分点」、无第三条创新。已修正 F1 数据事实状态、删除 R@1 列、F2 顶栏不再挂 E29 | F1, F2, F4 | 改状态；删除 F4；F2 顶栏只用 E17 |
| 评审价值 | 10 | 6 | 10 | 通过 | 评审要看：为何 CLIP/STR/枢纽不够（p.1–3）、式 (2) 如何可关闭（p.8）、三张表如何证伪（p.9） | F5, F2, F6 | F5→must；F2→strong；F6 不出图 |
| 叙事覆盖 | 15 | 9 | 15 | 通过 | 缺口 F1 → 问题/内容/创新 F2 → 门控 F5 → 三节点 F3 | F2, F3, F5 | must 含 F1+F5+F3 |
| 非重复性 | 10 | 6 | 10 | 通过 | F3 八胶囊与 F4 八行核心相同（p.9 同一段）；字面 Jaccard 漏检 | F1, F3, F4 | F3 删胶囊；F4 改表；F1 失败并入缺口 |
| 逻辑一致 | 10 | 8 | 10 | 通过 | B0–B2 仅 p.10 点名；对照「无文字通道」与消融「去 s」PDF 未等同 | F3, F4 | 年份/B0–B2 不进 F3；对照清单只留正文表 |
| 图形适配 | 10 | 6 | 9 | 通过（1 minor） | F4 空矩阵宜表；F6 宜文；F1 控制类型仍映射 Overall Framework | F4, F6, F1 | F4/F6→`no_figure`；F1 保持映射但按概念缺口画 |
| 可读与篇幅 | 10 | 6 | 9 | 通过（1 minor） | 15 页含约 3 页文献；修订后 4 图约 1.8 页；单图 must_show ≤8 | 全部 | 删除 F4/F6；瘦身 F1/F2/F3 |
| Prompt 就绪 | 5 | 4.5 | 5 | 通过 | 瘦身后类型/主题/布局/AR/可见标签唯一 | F1, F3 | 先改结构再允许 prompt |
| 跨图一致 | 5 | 4.5 | 5 | 通过 | 符号 \(f_v,f_s,g,s,z\) 一致；语义色在阶段三契约中固定 | 全部 | 统一术语表，不新增模块 |

`score_before` = 72.5。`score_after` = 25+10+15+10+10+9+9+5+5 = **93**。

图形适配与篇幅各留 1 个未解决 minor：F1 的受控类型名仍为 Overall Framework（Skill 映射表强制）；F2 作为 strong 第 4 图，若第（一）部超页则改为三线表。均未达 major。

---

## 3. 覆盖矩阵

| 申报书节点 | 修订后 | 说明 |
|---|---|---|
| 问题一 | F2 列1；F5 \(s=\mathbf{0}\)；F3 节点表1+3 | 闭环 |
| 问题二 | F2 列2；F5 式 (2) | F5 为必须图示 |
| 问题三 | F2 列3（共享创新点二）；F3 节点表2 | 不画第三条创新 |
| 内容一 | F2 列1；F3 阶段1；F5 \(f_s\) | |
| 内容二 | F2 列2；F5 中心；F3 阶段2 | |
| 内容三 | F2 列3；F3 阶段3 | 指标名称正文/F2 底栏 |
| 创新点一 | F2 列1 顶栏 | F1 不再重复创新点名称 |
| 创新点二 | F2 跨列 2–3 顶栏，标明「仅两条」 | |
| 四对照 | **正文三线表**（原 F4） | 图中不再铺八行 |
| 四消融 | **正文三线表**（原 F4） | |
| 式 (2) 门控 | **F5** | 禁止层栈 |
| 三张节点表 | **F3** | |
| 200–400 拟构建 | F2 一处图注 | 禁止画成 VQA 库 |
| 排除边界（翻译/语音/舆情） | F1 图注 / 正文 | 不占主面板 |
| CUTE/MC² 仅文本 | F3 分流虚线 | |
| 不新造 VLM | 正文更合适 | F3 不再单列 |
| 新能源/教学区分 | 正文更合适 | |
| 两年计划 / B0–B2 / H1–H3 | 正文更合适（原 F6） | 代号不展开 |

---

## 4. 问题清单（初轮 → 裁决）

### Blocker
无。

### Major（初轮；修订后关闭）

1. **篇幅/图数** → 删除 F4、F6；绘制集 4 图。关闭。
2. **F5 优先级倒置** → 升 must。关闭。
3. **F3 与 F4 协议复刻** → 删除 F4；F3 去掉对照/消融胶囊。关闭。
4. **F4 图型错误** → `decision: delete`，`no_figure`。关闭。
5. **F1 严重过载** → must_show 压到 6 项；失败路径并入缺口。关闭。
6. **F6 不适配** → `decision: delete`。关闭。

### Minor（修订后残留）

1. F1 受控 `figure_type` 仍为 Overall Framework（映射表强制）；画成概念缺口图，不画系统管道。不阻塞 prompt。
2. F2 为第 4 图；若第（一）部超页，优先改为三线表。当前仍 `draw_new`。
3. 「无文字通道」对照与「去 \(s\)」消融是否同一设置：PDF 未声明。图内不画二者连线；只在正文表分行列出。已随 F4 删除从画面消失。

已关闭的初轮 minor：F1 数据状态、R@1 列、E29 挂载、F3 注入 B0–B2、F5 拼接旁注、创新点二无「仅两条」字样。

---

## 5. Jaccard（初轮）与重复裁决

`source_evidence` 字面 Jaccard 均 &lt; 0.3，**漏检** F3/F4。对照/消融子集归一化后 F3 胶囊 vs F4 八行 **J=1.0**。规则「同章同型」因图型不同不强制合并，但核心信息相同，按 major 重复处理：**删除 F4**。

F5 相对 F3 证据/标签 Jaccard 均低，保留「总路线 + 机制放大」。F5 不得复刻三阶段与三张表。

修订后绘制集两两：F1 缺口 vs F2 对应图 vs F3 路线 vs F5 门控，核心信息不同。

---

## 6. 修订日志

| 动作 | 对象 | 内容 |
|---|---|---|
| 删除 | F4 | 对照×指标空矩阵改为 §3.2 正文三线表；不生成 prompt |
| 删除 | F6 | 两年计划留 §5.1 正文；B0–B2、H1–H3 保持未展开 |
| 升格 | F5 | `priority: must`；唯一承载式 (2) 与 \(s=\mathbf{0}\) |
| 降级 | F2 | `priority: strong`；创新点二跨列 2–3，图内写「创新点仅两条」 |
| 瘦身 | F1 | 6 个 must_show；失败并入缺口；排除边界与数据不替代进 caption_reserve |
| 瘦身 | F3 | 只留三阶段 + 三节点表 + 失败收缩 + CUTE/MC² 分流；删八胶囊与年份栏 |
| 瘦身 | F5 | 去掉拼接/单 InfoNCE 旁注（改 caption_reserve）；不画层栈 |
| 改状态 | F1 | 「SUST/RUST 与 Multi30k-Distant 不互相替代」→ `established`（数据事实，图注） |
| 改证据 | F2 | 顶栏不再使用 E29；公开数据约束用 E17 |
| 改位置 | F5 | 紧挨 §3.1 式 (2)；F2 在 §2.3 后；F3 在 §3.2 末 |
| 不新增 | — | 禁止层栈、Data Behavior、街景拼贴、第三条创新、H1–H3 全文、B0–B2 映射、任何数值 |

---

## 7. Audited Figure Plan（reviewed-v2）

全局字段同 v1，除非下文明示覆盖。`module_count_framework`: 5。`palette hint`: Nature Blue。

### F1

| 字段 | 内容 |
|---|---|
| `figure_id` | F1 |
| `decision` | keep |
| `merged_into` | — |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `proposed_title` | 维语场景图的双通道语义与三项研究缺口 |
| `target_section` | （一）1.4 研究切入点之后、参考文献之前（约 p.3） |
| `reviewer_question` | 现有多语 CLIP、维语 STR 和视觉枢纽翻译为什么仍不能回答「图中写了什么是否有助于维—汉图像理解」？ |
| `figure_type` | Overall Framework |
| `figure_form` | conceptual framework → Overall Framework |
| `priority` | must |
| `source_evidence` | E01, E02, E13, E14, E15, E16 |
| `core_message` | 维语场景图同时有物体外观和场景文字；缺文字通道、停在识别、按翻译验收，都无法把文字写成可消融的理解贡献。 |
| `existing_asset_relation` | new |
| `data_requirement` | 概念结构；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | none（题目已确认；图内仍不放全称） |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 双通道：物体外观 / 场景文字 | 输入分解 | E01, E02 | source-explicit | established（问题陈述） |
| 两问：图中是什么 / 图中写了什么 | 评审锚点 | E13 | source-explicit | established（问题陈述） |
| 缺口一：检索缺维语文字通道 | 缺口（内含「文字当纹理」） | E03, E07, E13 | source-explicit | established（文献不足） |
| 缺口二：识别正确 ≠ 融合有用 | 缺口（内含 STR 丢掉物体） | E03, E08, E14 | source-explicit | established（文献不足） |
| 缺口三：枢纽面向翻译，缺检索消融 | 缺口（内含 OCR→翻译累积） | E08, E10, E15 | source-explicit | established（文献不足） |
| 切入点三词：场景文字编码 / 异构融合 / 跨语言检索与理解评价 | 右端指向 | E16 | source-explicit | proposed |

**caption_reserve**：不扩展翻译系统、语音、舆情（E04）；SUST/RUST 与 Multi30k-Distant 不互相替代（E10, E11，`established`）；式 (1)–(6)；任何实测指标。

---

### F2

| 字段 | 内容 |
|---|---|
| `figure_id` | F2 |
| `decision` | keep |
| `merged_into` | — |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `proposed_title` | 三项问题、三项内容与两条创新的对应关系 |
| `target_section` | （一）2.3 关键科学问题之后、第 3 节之前（约 p.8） |
| `reviewer_question` | 三项科学问题、三项研究内容与两条创新如何对应，而不是「再做一个多语 CLIP」？ |
| `figure_type` | Overall Framework |
| `figure_form` | research-content map → Overall Framework |
| `priority` | strong |
| `source_evidence` | E17, E18, E19, E20, E21, E22, E32, E38 |
| `core_message` | 研究沿「文字通道是否有用 → 如何融合而不干扰 → 枢纽能否服务检索」递进；创新点只有两条，问题三并入创新点二的评价。 |
| `existing_asset_relation` | new |
| `data_requirement` | 结构对应关系；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | H1–H3 不进图 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 列 1：问题一 + 内容一 | 第三通道 | E18, E22 | source-explicit | proposed |
| 列 1 顶栏：创新点一 | 创新（仅此列） | E32 | source-explicit | proposed |
| 列 2：问题二 + 内容二 | 门控融合 | E19, E22 | source-explicit | proposed |
| 列 3：问题三 + 内容三 | 检索评价 | E20, E22 | source-explicit | proposed |
| 跨列 2–3 顶栏：创新点二（图内须出现「创新点仅两条」） | 创新共享 | E32 | source-explicit | proposed |
| 列 1 产物：\(s\)；无文字 \(s=\mathbf{0}\) | 开关 | E18 | source-explicit | proposed |
| 底栏证伪：去通道不降 / 门控双差 / 翻译不低于枢纽 | 可证伪 | E22 | source-explicit | proposed |
| 图注：200–400 题为拟构建，非已有 VQA 库 | 防伪 | E21, E38 | source-explicit | proposed |

**caption_reserve**：三类基线全称与四消融（改正文表）；Train 29,000 等划分数字；输出形态「SCI/资源包」。

---

### F3

| 字段 | 内容 |
|---|---|
| `figure_id` | F3 |
| `decision` | keep |
| `merged_into` | — |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `proposed_title` | 编码—融合—评价技术路线与三张可检验节点表 |
| `target_section` | （一）3.2 技术路线段末（约 p.9） |
| `reviewer_question` | 文字编码器何时可用、融合何时训练、哪三张表决定假设收缩？ |
| `figure_type` | Overall Framework |
| `figure_form` | technical route → Overall Framework |
| `priority` | must |
| `source_evidence` | E18, E20, E28, E29, E31 |
| `core_message` | 先确认 \(f_s\)，再训练 \(g\)，最后用三张表分别检验通道、检索与消融；失败只收缩对应假设。 |
| `existing_asset_relation` | new |
| `data_requirement` | 阶段与节点标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | B0–B2 已确认对应，本图仍不画代号 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 阶段 1 编码：SUST 训 \(f_s\)，RUST 确认 | 主流程 | E18, E28 | source-explicit | proposed |
| 阶段 2 融合：冻结或低学习率适配 \(f_v\)/文本编码器，训练 \(g\) | 主流程 | E28 | source-explicit | proposed |
| 阶段 3 评价：Multi30k-Distant 检索 + 理解协议 | 主流程 | E20, E28 | source-explicit | proposed |
| 节点表 1：RUST 文字通道是否可用 | 检验 | E28 | source-explicit | proposed |
| 节点表 2：跨语言检索是否提高 | 检验 | E28 | source-explicit | proposed |
| 节点表 3：去掉 \(s\) 后主指标是否回落 | 检验 | E28 | source-explicit | proposed |
| 失败分流：只收缩对应假设，不改写另外两张表口径 | 反馈虚线 | E28, E31 | source-explicit | proposed |
| 数据分流：CUTE/MC² 只进文本编码器，不进图像测试 | 约束 | E20, E29 | source-explicit | proposed |

**caption_reserve**：四对照与四消融全称（正文表）；年份与 B0–B2；「不新造基础模型」散文。

---

### F4

| 字段 | 内容 |
|---|---|
| `figure_id` | F4 |
| `decision` | delete |
| `merged_into` | 正文三线表（§3.2） |
| `render_action` | no_figure |
| `prompt_eligible` | false |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `priority` | —（已删除） |
| `reason` | 无实测的空矩阵更适合表格；与瘦身前提议的 F3 胶囊核心信息相同 |

---

### F5

| 字段 | 内容 |
|---|---|
| `figure_id` | F5 |
| `decision` | keep |
| `merged_into` | — |
| `render_action` | draw_new |
| `prompt_eligible` | true |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `proposed_title` | 可关闭文字通道的门控残差融合与分通道对齐 |
| `target_section` | （一）3.1 研究方法，式 (2)–(5) 附近（约 p.8） |
| `reviewer_question` | 外观、连写维文与维/汉描述如何进入同一表征，又如何被单独关掉以做干净消融？ |
| `figure_type` | Module Detail |
| `figure_form` | mechanism / key method → Module Detail |
| `priority` | must |
| `source_evidence` | E18, E23, E24, E25, E26, E30 |
| `core_message` | \(s=\mathbf{0}\) 即关闭文字通道；\(z\) 是对外观的门控残差；外观—文本与文字—文本分开对齐，枢纽损失经 \(z\) 对齐双语描述。 |
| `existing_asset_relation` | new |
| `data_requirement` | 机制标签与式 (1)(2) 符号；`available` |
| `aspect_ratio` | 4:3 |
| `style_family` | classic_academic |
| `unknowns` | \(\alpha,\lambda,\tau,W\) 数值与隐藏维度未给出 → 不进图 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 图像 \(I\) | 输入 | E23 | source-explicit | proposed |
| 文字区域 \(\{t_k\}\) | 输入 | E23 | source-explicit | proposed |
| \(y^{\mathrm{ug}}\) / \(y^{\mathrm{zh}}\) | 输入 | E23 | source-explicit | proposed |
| \(f_v \rightarrow v\)；\(f_s \rightarrow s\)；\(f_\ell \rightarrow h^{\ell}\) | 编码器（只标符号） | E23 | source-explicit | proposed |
| 无文字：\(s=\mathbf{0}\)，通道关闭 | 开关 | E18, E23 | source-explicit | proposed |
| \(z=v+\alpha\sigma(W[v;s])\odot s\) | 核心机制 | E24 | source-explicit | proposed |
| \(\mathrm{sim}(z,h)\) | 输出打分 | E25 | source-explicit | proposed |
| \(\mathcal{L}_{v\rightarrow t}\) / \(\mathcal{L}_{s\rightarrow t}\) / \(\mathcal{L}_{\mathrm{hub}}\) | 监督 | E26 | source-explicit | proposed |

**caption_reserve**：式 (4) 完整 InfoNCE；\(\tau\)、批大小、\(\lambda\) 数值、\(W\) 尺寸；CLIP/STR 层名；拼接/单 InfoNCE 比较句（正文已有）；连写/从右向左作为 \(f_s\) 旁注可保留 ≤2 词「连写 RTL」，更长解释进 caption。

---

### F6

| 字段 | 内容 |
|---|---|
| `figure_id` | F6 |
| `decision` | delete |
| `merged_into` | §5.1 正文 |
| `render_action` | no_figure |
| `prompt_eligible` | false |
| `blockers` | [] |
| `unresolved_majors` | [] |
| `priority` | —（已删除） |
| `reason` | 两年两阶段正文已按时间写清；B0–B2 与 H1–H3 仅点名，不宜画成验收灯 |

---

## 8. 修订后优先级与页面成本

| 优先级 | 图 | 决策 |
|---|---|---|
| must | F1 | keep / draw_new / prompt_eligible |
| must | F5 | keep / draw_new / prompt_eligible |
| must | F3 | keep / draw_new / prompt_eligible |
| strong | F2 | keep / draw_new / prompt_eligible |
| — | F4, F6 | delete / no_figure |

预计页面成本：F1 0.45 + F2 0.45 + F5 0.45 + F3 0.50 ≈ **1.85 页**。若超页，删减顺序：F2（改三线表）→ 不得删 F1/F5/F3。

阶段三选择式集合：`{F1, F2, F3, F5}`。

---

## completeness

```yaml
completeness:
  analyzed_materials:
    - main.pdf p.1-15 text layer
    - 01-figure-plan.md v1
    - extraTex/1.3.方案及可行性.tex (symbol checksum only)
    - independent subagent first-pass review
  output_type: complete
  high_confidence_information:
    - 无现有插图
    - 中文题目全称已由用户确认
    - B0–B2 与四对照对应已由用户确认（图内不画代号）
    - 三项问题 / 三项内容 / 两条创新
    - 式 (2) 门控残差与 s=0
    - 三张节点表与「失败只收缩假设」
  pending_confirmation:
    - H1–H3 假设全文（不进图）
    - 若第（一）部超页，F2 是否改为表
  suggested_materials:
    - 若恢复 Data Behavior：真实预实验数值
```
