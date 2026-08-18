# Figure Plan v1 — NSFC_2026_MUC_Lab 申报书配图规划

- `plan_version`: v1
- `source_pdf`: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_MUC_Lab/main.pdf`
- `source_sha256`: `5fae172cd362836662f99697a98f04855bc78938c0fb8939208ab82a54a9fa77`
- `pages`: 15（实际分析页 1–15）
- `extraction`: text（`pdftotext -layout`；未 OCR）
- `project_title_zh`: 场景文字增强的维吾尔语多模态表征融合与跨语言图像理解（用户 2026-08-15 确认；图内不渲染全称）
- `extraction_warnings`:
  - 第 1 页正文仍未印项目题目；全称已由用户确认，不再标为 `待确认`。图内因 text budget 仍不放全称，仅用于封面/题名与图题元数据。
  - 第 4–6 页为英文参考文献，无配图信息。
  - 式 (1)–(6) 因 PDF 文本层折行，符号以 `extraTex/1.3.方案及可行性.tex` 核验，不据此补充 PDF 未出现的科学内容。
  - 年度计划出现 `B0–B2`、可行性出现 `H1–H3`。`B0–B2` 与四对照的逐项对应已由用户 2026-08-15 确认（见下表），图内仍只用 §3.2 中文全称、不画代号。`H1–H3` 假设全文仍未展开。
- `dependency_versions`:
  - `plan-proposal-figures`: 0.1.0
  - `Academic Paper Analyzer & Figure Planner`: 1.2.0
  - `Academic Figure Prompt`: 1.5.0
- `style_family`: `classic_academic`（本 Skill 仅支持 classic）
- `image_backend_calls`: 0（本阶段禁止 prompts 与生图）

---

## 申报书概览与科学问题摘要

**题目（用户确认）**：场景文字增强的维吾尔语多模态表征融合与跨语言图像理解。PDF 第 15 页 source-explicit 的对象表述为「维吾尔语场景文字与维—汉图像理解」；正文未印全称不影响已确认题名。

**申报类型（PDF 第 1、9–11、15 页 source-explicit）**：教育部重点实验室「民族语言多模态提取融合」方向开放课题；正文按国家自然科学基金地区科学基金章节结构撰写。实施期两年（2027.01–2028.12）；预算 5 万元。不是国家自然科学基金项目。

**对象与边界**：自然场景图像同时包含物体外观与维吾尔语场景文字（路牌、招牌、海报）。对象收敛到维—汉图文；不扩展为通用民汉翻译系统、语音交互或舆情治理。主评测用公开数据 SUST/RUST 与 Multi30k-Distant；CUTE 与 MC² 仅更新文本编码器。拟建 200–400 题理解协议不得画成已有大规模维语 VQA 基准。

**贡献主线（拟开展，非已验证结果）**：

1. 把维吾尔语场景文字作为可关闭的第三视觉语言通道，而不是停在识别准确率。
2. 外观、文字与维/汉描述分通道编码，用门控残差融合，避免文字噪声覆盖物体语义。
3. 以共享图像为枢纽做汉↔维互检索，主指标为 Recall@K / MRR；翻译流水线只作对照。

**可证伪口径（proposed）**：若去掉文字通道后主指标不下降，或 OCR—翻译流水线全面不低于视觉枢纽，则收缩主张。对照顺序：多语 CLIP 零样本、无文字通道、OCR—翻译流水线、完整模型。消融顺序：去 \(s\)、去门控、去 \(\mathcal{L}_{s\rightarrow t}\)、去 \(\mathcal{L}_{\mathrm{hub}}\)。

**B0–B2 对应（用户 2026-08-15 确认；图内不渲染代号）**

| 代号 | 对照全称 | 年度 |
|---|---|---|
| B0 | 多语 CLIP 零样本 | 第一年 |
| B1 | 无文字通道 | 第一年 |
| B2 | OCR—翻译流水线 | 第一年 |
| — | 完整模型 | 第二年；正文无 B3 |

- `domain`: 多模态表征学习 × 维吾尔语场景文字 × 低资源跨语言图像理解
- `venue`: None（实验室开放课题 / NSFC 式申请书，非会议期刊）
- `palette / style family hint`: classic academic；框架模块数 ≥ 4 → 倾向 Nature Blue
- `module_count_framework`: 5（外观编码 \(f_v\)、文字编码 \(f_s\)、文本编码 \(f_\ell\)、门控融合 \(g\)、检索评价）

---

## section_status

将申报书评审结构映射为规划器章节，而不是论文 Intro/Method/Experiments。

| 申报书评审结构 | 对应 PDF 位置 | 状态 |
|---|---|---|
| 立项依据、研究现状与核心缺口 | §1.1–1.4，p.1–3 | present |
| 科学问题、科学假设与研究目标 | §2.2–2.3，p.7–8 | present（H1–H3 仅点名，假设正文未展开） |
| 研究内容及其依赖关系 | §2.1，p.7 | present |
| 总体框架、技术路线与关键机制 | §3.1–3.4，p.8–9 | present |
| 验证方案、指标、对照与可证伪条件 | §3.2–3.5、§2.2，p.7–9 | present |
| 创新点、可行性、研究基础与年度计划 | §4、§5、（二）1–2，p.9–12 | present（创新点为两条，不是三条） |
| 已测实验结果 / 数据图 | 无 | absent |

论文 4–12 图经验值**不适用**。15 页申请书中约 3 页为参考文献，第（一）部分宜控在 5000–7000 字：规划 3 must + 1 strong + 2 nice，优先落地 must 三图；可删减顺序见文末。

---

## 现有图处置清单

| 资产 | 位置 | 作用 | 处置 |
|---|---|---|---|
| PDF 内插图 | `pdfimages -list` 为空；正文无图题、无 `\includegraphics` | 无 | 无 reuse / redraw |
| `projects/NSFC_2026_MUC_Lab/figures/` | 仅 `.gitkeep` | 无 | 无 reuse |
| `docs/03_科学问题与创新点.md` | 非申报书插图；含 PDF 未写的「5 个百分点」等阈值 | 仅作旁证，**不作为本轮证据** | 图内禁止写入该文档独有数值 |

`existing_asset_relation_confidence`: **high**（文本层完整 + 无 Image XObject + 源 tex 无 figure 环境）。未做整本页栅格；因无图题、无图像对象，不将“不重复”建立在未见页面上。临时页栅格不属于交付物。

---

## evidence_registry

每条记录：`evidence_id` / PDF 页 / 章节 / 摘要 / 置信度。

| evidence_id | 页 | 章节 | 摘要 | 置信度 |
|---|---:|---|---|---|
| E01 | 1 | 1.1 | 民族地区自然场景图像同时包含物体外观和场景文字；路牌、招牌、海报上的维吾尔语既标识地点与商户，也构成图像语义 | high |
| E02 | 1 | 1.1 | 现有视觉—语言模型主要在英/中图文对上训练，倾向回答「图中是什么」，对黏着语、从右向左、连写变体丰富的维语场景文字缺乏稳定编码 | high |
| E03 | 1 | 1.1 | 只做跨模态检索则文字被当成纹理；只做场景文字识别则丢掉物体与场景上下文 | high |
| E04 | 1 | 1.1 | 面向实验室「民族语言多模态提取融合」；把维语场景文字作为独立视觉语言通道，与外观、维/汉描述一并编码；对象收敛到维—汉图文；不扩展为通用民汉翻译、语音交互或舆情治理 | high |
| E05 | 1 | 1.1 | 外观、文字区域与双语描述的粒度、噪声和脚本方向不同，直接拼接或单一对比损失易互相干扰；跨语言检索需支持汉查询维图、维查询汉图 | high |
| E06 | 1 | 1.1 | 「第三通道是否有用」写成可消融、可证伪；两年期不适合大规模预训练或在线系统；若文字通道只提高 OCR、不提高汉↔维检索，则收缩主张 | high |
| E07 | 2 | 1.2 | CLIP/ALIGN/SigLIP 等训练数据以自然描述为主，图像文字通常不被单独建模；两类错误：招牌当纹理，或用英/中先验猜图意；CLIP 零样本只作对照 | high |
| E08 | 2 | 1.2 | STR 输出字符串，图像理解需要可与外观相加或门控的连续向量；OCR 后翻译再检索会在三级累积错误，且无法做去掉文字通道的干净消融 | high |
| E09 | 2 | 1.2 | TextVQA/ST-VQA/OCR-VQA 表明答案写在图里时必须读字；OCR-free 数据仍集中英/中印刷体，不能外推到维语连写招牌 | high |
| E10 | 2–3 | 1.2 | 多语 CLIP 很少以维语为主测语言；视觉枢纽在句对稀缺时用共享图像约束潜空间；Multi30k-Distant 任务是翻译不是场景文字增强理解；本项目改用 Recall@K 与 MRR；Multi30k 图像很少是新疆街景招牌，RUST 仍用于检验文字通道，二者不互相替代 | high |
| E11 | 3 | 1.2 | SUST 60 万合成词级图、RUST 4000 张新疆实景图，验收仍是识别准确率；MC² 维语网页单语、CUTE 中维藏英语料；CUTE 含机翻，只适合文本预训练；商业平行库不进入数据清单 | high |
| E12 | 3 | 1.2 | 申请人已有知识增强 VQA、空间共注意力、遥感 VQA 与跨模态检索基础；本项目迁移到维语场景文字与维—汉图文，不重复新能源预测或教学资源构建 | high |
| E13 | 3 | 1.3 | 不足一：图文检索缺少维语场景文字通道，无法区分「图中是什么」与「图中写了什么」；多语 CLIP 零样本会高估资源语言先验 | high |
| E14 | 3 | 1.3 | 不足二：维语 STR 停在识别准确率；识别正确不等于融合有用；错误文字向量可能损害物体检索 | high |
| E15 | 3 | 1.3 | 不足三：视觉枢纽与 Multi30k-Distant 面向翻译；缺少以 Recall@K、MRR 和去掉文字通道消融为主的验收；拟建 200–400 题只是辅助协议，主结论必须落在公开检索划分上 | high |
| E16 | 3 | 1.4 | 主线「场景文字编码—异构融合—跨语言检索与理解评价」；SUST/RUST 得区域特征；分通道编码和门控融合；Multi30k-Distant 汉↔维互检索；对照为多语 CLIP 零样本、无文字通道对比学习、OCR 后翻译再检索 | high |
| E17 | 7 | 2.1 | 三项研究内容一一对应，均在公开数据上完成，不依赖未授权采集 | high |
| E18 | 7 | 2.1(1) | 内容一：SUST 训练/适配词级场景文字编码器，RUST 测试；得到可供融合的文字区域特征 \(s\)；无文字图像令 \(s=\mathbf{0}\) 并关闭通道；RUST 识别准确率为中间指标，非主验收 | high |
| E19 | 7 | 2.1(2) | 内容二：\(f_v,f_s\) 与维/汉文本编码器得 \(v,s,h^{\mathrm{ug}},h^{\mathrm{zh}}\)；融合头 \(g(v,s)\) 门控残差；外观—文本与文字—文本分开对齐；比较简单拼接、单 InfoNCE 与门控双对齐 | high |
| E20 | 7 | 2.1(3) | 内容三：I2T/T2I 及汉查询—维描述、维查询—汉描述的 Recall@K 与 MRR；拟建 200–400 题理解协议；翻译流水线只作对照，不以 BLEU 为主指标；CUTE 与 MC² 仅用于文本编码器继续预训练；不把再训练通用多语 VLM 列作研究内容 | high |
| E21 | 7 | 2.2 | 总体目标：可复现方法，并在公开基准上证明或证伪其对维—汉跨语言图像理解的贡献。具体目标：(1) RUST 上编码器可用且去掉通道后 Recall@5 下降可观测；(2) Multi30k-Distant 上完整模型汉↔维 Recall@5 高于无文字通道与 OCR—翻译流水线；(3) 完成 200–400 题并报告准确率，不表述为已有大规模维语 VQA 库；(4) 支撑 1 篇中科院三区及以上 SCI，实验室第一单位 | high |
| E22 | 7–8 | 2.3 | 问题一：场景文字能否成为稳定第三通道；消融后若不下降则拒绝普遍有用。问题二：外观、连写维文与维/汉描述如何融合而不互相干扰；若门控在物体检索和文字相关检索上同时差于单通道，则拒绝必须复杂融合。问题三：共享图像作枢纽能否改善汉↔维互检索；若翻译流水线全面不低于视觉枢纽，则把枢纽降为辅助模块 | high |
| E23 | 8 | 3.1 | 式 (1)：\(v=f_v(I)\)，\(s=f_s(\{t_k\})\)，\(h^{\ell}=f_{\ell}(y^{\ell})\)，\(\ell\in\{\mathrm{ug},\mathrm{zh}\}\)；无文字时 \(s=\mathbf{0}\) | high |
| E24 | 8 | 3.1 | 式 (2)：\(z=g(v,s)=v+\alpha\,\sigma(W[v;s])\odot s\)；\(\sigma\) 为 Sigmoid，\(\alpha\) 可学习或验证集选择 | high |
| E25 | 8 | 3.1 | 式 (3)：余弦相似度 \(\mathrm{sim}(z,h)\) | high |
| E26 | 8 | 3.1 | 式 (4)(5)：分通道 InfoNCE \(\mathcal{L}_{v\rightarrow t}\)；\(\mathcal{L}_{s\rightarrow t}\) 同构；\(\mathcal{L}=\mathcal{L}_{v\rightarrow t}+\lambda_s\mathcal{L}_{s\rightarrow t}+\lambda_{\mathrm{hub}}\mathcal{L}_{\mathrm{hub}}\)；\(\mathcal{L}_{\mathrm{hub}}\) 将同一图像上 \(h^{\mathrm{ug}}\) 与 \(h^{\mathrm{zh}}\) 通过 \(z\) 对齐；\(\lambda\) 在验证集选择 | high |
| E27 | 8 | 3.1 | 式 (6)：\(\mathrm{R@}K\) 与 MRR；\(r_i\) 为正确匹配秩；理解任务报告准确率 | high |
| E28 | 9 | 3.2 | 路线「编码—融合—评价」：SUST 得 \(f_s\)，RUST 确认可用；冻结或低学习率适配 \(f_v\) 与文本编码器，训练 \(g\) 与对齐损失；Multi30k-Distant 单语与跨语言检索 + 理解协议。对照顺序：多语 CLIP 零样本、无文字通道、OCR—翻译流水线、完整模型。消融顺序：去 \(s\)、去门控、去 \(\mathcal{L}_{s\rightarrow t}\)、去 \(\mathcal{L}_{\mathrm{hub}}\)。三张表节点：RUST 文字通道是否可用；跨语言检索是否提高；去掉 \(s\) 后主指标是否回落。失败只收缩对应假设 | high |
| E29 | 9 | 3.3 | Multi30k-Distant Train 29,000 / Val 1,014 / Test 1,000；SUST 训 \(f_s\)，RUST 按作者划分测试；CUTE/MC² 不进入图像测试；理解题在测试集编写且不用训练集描述原句；不从随机初始化训练大型 VLM | high |
| E30 | 9 | 3.4 | 关键技术：连写、从右向左脚本的维语场景文字区域编码；分通道对齐与门控融合；以图像为枢纽的汉—维互检索协议及与翻译流水线的公平对照 | high |
| E31 | 9 | 3.5 | 理论/数据/条件可行；风险为图像许可、RUST 与 Multi30k 域差、5 万元算力上限；应对为合法子集、不把 OCR 准确率解释为检索增益、只训练融合头与轻量适配。若 H1–H3 被证伪，收缩为「文字通道仅对文字主导图像有效」或「枢纽不优于翻译流水线」 | high |
| E32 | 9–10 | 4 | 创新点一：场景文字作为跨语言图像理解的第三通道，验收看去掉文字通道后 Recall@5 或准确率是否下降。创新点二：低资源维—汉条件下的分通道融合与视觉枢纽评价；若枢纽不优于翻译则如实降级。创新点只有两条 | high |
| E33 | 10 | 5.1 | 第一年 2027.01–12：合规审查、SUST/RUST、无文字通道基线与 OCR—翻译流水线、Recall@K/MRR/消融脚本；确认 \(f_s\) 可用并得到 B0–B2 可复现分数。第二年 2028.01–12：门控融合与视觉枢纽、Multi30k-Distant 检索、200–400 题与专家核对、SCI 投稿；完成 H1–H3 检验 | high |
| E34 | 10–11 | 5.2–5.3 | 预期：方法协议 + 完整模型/三类基线/四项消融 + 三区 SCI 1 篇（实验室第一单位）。不承诺专利、平台或学生数据。预算劳务费 3.5 万、业务费 1.5 万 | high |
| E35 | 11–12 | （二）1 | 申请人颜丰；VQA/检索积累为 established；新能源/遥感指标不构成本课题结果；约 10 名研究生；天池英才对象为产业集群，与本课题不同 | high |
| E36 | 12 | （二）2 | 已具备 GPU 与公开数据来源；缺少现成维语融合代码、本地 Multi30k-Distant 对齐副本、200–400 题题面；融合代码在开源 CLIP/STR 上适配，不新造基础模型 | high |
| E37 | 13 | （二）3 | 在研天池英才、光伏预测、博士后 VQA、横向知识库；与本课题对象或考核不同 | high |
| E38 | 15 | （三）5 | 电子版文件名「2026 年开放课题申请-新疆大学-颜丰-副教授」；理解评测题为拟构建协议，不是已经发布的大规模维语 VQA 基准 | high |
| E39 | — | 资产盘点 | PDF 无 Image XObject；`extraTex` 无 figure 环境；`figures/` 仅 `.gitkeep` | high |
| E40 | — | 元数据 | 中文题目「场景文字增强的维吾尔语多模态表征融合与跨语言图像理解」由用户 2026-08-15 确认；PDF 正文仍未印全称 | high |

| E41 | — | 用户确认 | B0=多语 CLIP 零样本，B1=无文字通道，B2=OCR—翻译流水线；完整模型在第二年、无 B3。图内不渲染这些代号 | high |

公式、节点、边默认 `evidence_status: source-explicit`，`research_state: proposed`（方法与指标）或 `expected`（验收指标名称），除非标明 `established`（问题陈述、文献不足、已有论文基础）。`H1–H3` 与问题一至三的逐项对应仍为 `conservative-inference`。`B0–B2` 对应已由用户确认（E41），但图内仍不画代号。

---

## 分条目 Figure Plan

### F1

| 字段 | 内容 |
|---|---|
| `figure_id` | F1 |
| `proposed_title` | 维语场景图的双通道语义、「读图/读字」失败与三项研究缺口 |
| `target_section` | （一）1.4 研究切入点之后、参考文献之前（约 p.3） |
| `reviewer_question` | 现有多语 CLIP、维语 STR 和视觉枢纽翻译为什么仍不能回答「图中写了什么是否有助于维—汉图像理解」？ |
| `figure_type` | Overall Framework |
| `figure_form` | conceptual framework → Overall Framework |
| `priority` | must |
| `source_evidence` | E01, E02, E03, E07, E08, E10, E13, E14, E15, E16 |
| `core_message` | 维语场景图同时有物体外观和场景文字；按纹理检索、按字符串识别、按翻译枢纽，都无法把文字通道写成可消融的理解贡献。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 概念结构；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | none（题目已确认；图内仍不放全称长标题） |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 输入对象：路牌 / 招牌 / 海报 | 场景 | E01 | source-explicit | established（问题陈述） |
| 双通道：物体外观 / 场景文字 | 输入分解 | E01, E02 | source-explicit | established（问题陈述） |
| 两问：图中是什么 / 图中写了什么 | 评审锚点 | E13 | source-explicit | established（问题陈述） |
| 失败一：文字当纹理 | 现有路径 | E03, E07 | source-explicit | established（文献不足） |
| 失败二：只做 STR，丢掉物体 | 现有路径 | E03, E08, E14 | source-explicit | established（文献不足） |
| 失败三：OCR→翻译→检索，三级累积 | 现有路径 | E08 | source-explicit | established（文献不足） |
| 缺口一：检索缺维语文字通道 | 缺口 | E13 | source-explicit | established（文献不足） |
| 缺口二：识别≠融合有用 | 缺口 | E14 | source-explicit | established（文献不足） |
| 缺口三：枢纽面向翻译，缺检索消融 | 缺口 | E10, E15 | source-explicit | established（文献不足） |
| 数据不替代：SUST/RUST vs Multi30k-Distant | 边界 | E10, E11 | source-explicit | proposed |
| 切入点三词：场景文字编码 / 异构融合 / 跨语言检索与理解评价 | 右端指向，不展开方法 | E16 | source-explicit | proposed |
| 底栏：不扩展翻译系统、语音、舆情 | 范围 | E04 | source-explicit | proposed |

**禁止入图**：式 (1)–(6)、完整模型层栈、B0–B2 代号、200–400 题规模画成已有基准、任何实测 Recall/准确率、`docs/03` 中的 5 个百分点阈值。

---

### F2

| 字段 | 内容 |
|---|---|
| `figure_id` | F2 |
| `proposed_title` | 第三通道、异构融合与视觉枢纽的三项研究内容对应图 |
| `target_section` | （一）2.3 关键科学问题之后、第 3 节之前（约 p.8） |
| `reviewer_question` | 三项科学问题、三项研究内容与两条创新如何对应，而不是「再做一个多语 CLIP」？ |
| `figure_type` | Overall Framework |
| `figure_form` | research-content map → Overall Framework |
| `priority` | must |
| `source_evidence` | E17, E18, E19, E20, E21, E22, E32 |
| `core_message` | 研究沿「文字通道是否有用 → 如何融合而不干扰 → 枢纽能否服务检索」递进；创新点只有两条，问题三并入创新点二的评价。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 结构对应关系；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | H1–H3 与问题一至三的代号对应为 `conservative-inference`；图内用「问题一/二/三」，不写未展开的假设全文 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 共享输入：公开数据，未授权采集不进入 | 顶栏 | E17, E29 | source-explicit | proposed |
| 列 1：问题一 + 内容一 + 创新点一 | 第三通道 | E18, E22, E32 | source-explicit | proposed |
| 列 2：问题二 + 内容二 + 创新点二（融合半侧） | 门控融合 | E19, E22, E32 | source-explicit | proposed |
| 列 3：问题三 + 内容三 + 创新点二（枢纽评价半侧） | 检索评价 | E20, E22, E32 | source-explicit | proposed |
| 内容一输出：文字区域特征 \(s\)；无文字 \(s=\mathbf{0}\) | 列 1 产物 | E18 | source-explicit | proposed |
| 内容二比较：简单拼接 / 单 InfoNCE / 门控双对齐 | 列 2 可证伪 | E19 | source-explicit | proposed |
| 内容三主指标：Recall@K、MRR；理解准确率为辅 | 列 3 指标 | E20, E21, E27 | source-explicit | expected |
| 证伪提示：去通道不降 / 门控双差 / 翻译不低于枢纽 | 底栏可证伪 | E22 | source-explicit | proposed |
| 共享对照：三类基线 + 完整模型（名称级，不展开矩阵） | 底栏 | E16, E20, E28 | source-explicit | proposed |
| 输出形态：可复现方法 / 检索消融表 / 拟建理解协议 | 右端 | E21, E34, E38 | source-explicit | expected |
| 标注：200–400 题为拟构建，非已有 VQA 库 | 防伪 | E15, E21, E38 | source-explicit | proposed |

**禁止入图**：第三条创新点、五阶段操作步骤、公式展开、编码器内部层栈、把 60 万/4000/29,000 画成已完成实验库存、任何已测曲线。

---

### F3

| 字段 | 内容 |
|---|---|
| `figure_id` | F3 |
| `proposed_title` | 编码—融合—评价技术路线与三张可检验节点表 |
| `target_section` | （一）3.2 技术路线段末（约 p.9） |
| `reviewer_question` | 两年路径中，文字编码器何时可用、融合何时训练、哪三张表决定假设收缩？ |
| `figure_type` | Overall Framework |
| `figure_form` | technical route → Overall Framework |
| `priority` | must |
| `source_evidence` | E18, E28, E29, E31, E33, E36 |
| `core_message` | 路线是带冻结与轻量适配的闭环：先确认 \(f_s\)，再训练 \(g\)，最后用三张表分别检验通道、检索与消融；失败只收缩对应假设。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 阶段与节点标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | B0–B2 已确认对应，本图仍只用对照全称、不画代号 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 阶段 1 编码：SUST 训 \(f_s\)，RUST 确认 | 主流程 | E18, E28 | source-explicit | proposed |
| 阶段 2 融合：冻结或低学习率适配 \(f_v\)/文本编码器，训练 \(g\) | 主流程 | E28, E36 | source-explicit | proposed |
| 阶段 3 评价：Multi30k-Distant 检索 + 理解协议 | 主流程 | E20, E28 | source-explicit | proposed |
| 权重状态：\(f_v\)/文本编码器冻结或低学习率；\(g\) 可训练 | 状态 | E28, E31 | source-explicit | proposed |
| 节点表 1：RUST 文字通道是否可用 | 检验 | E28 | source-explicit | proposed |
| 节点表 2：跨语言检索是否提高 | 检验 | E28 | source-explicit | proposed |
| 节点表 3：去掉 \(s\) 后主指标是否回落 | 检验 | E28 | source-explicit | proposed |
| 对照胶囊（压缩）：多语 CLIP 零样本 / 无文字通道 / OCR—翻译 / 完整模型 | 验证设计 | E28 | source-explicit | proposed |
| 消融胶囊（压缩）：去 \(s\) / 去门控 / 去 \(\mathcal{L}_{s\rightarrow t}\) / 去 \(\mathcal{L}_{\mathrm{hub}}\) | 验证设计 | E28 | source-explicit | proposed |
| 失败分流：只收缩对应假设，不改写另外两张表口径 | 反馈虚线 | E28, E31 | source-explicit | proposed |
| 数据分流：CUTE/MC² 只进文本编码器，不进图像测试 | 约束 | E20, E29 | source-explicit | proposed |
| 不新造基础模型 / 不随机初始化大型 VLM | 范围 | E29, E36 | source-explicit | proposed |

**禁止入图**：把 F2 三列科学问题地图原样复制为流水线；绘制 CLIP/STR 网络层栈；填写任何实测指标；把域差风险画成已经消除。

---

### F4

| 字段 | 内容 |
|---|---|
| `figure_id` | F4 |
| `proposed_title` | 对照、消融与主/辅指标的可证伪实验设计 |
| `target_section` | （一）3.2 与 F3 同节，置于 F3 之后；若篇幅不足则降为正文表 |
| `reviewer_question` | 如何用对照和消融分别证伪三项科学问题，而不是只比较「有模型/无模型」？ |
| `figure_type` | Comparison / Ablation |
| `figure_form` | design comparison / condition matrix → Comparison / Ablation |
| `priority` | strong |
| `source_evidence` | E16, E21, E22, E27, E28, E34 |
| `core_message` | 四对照回答「完整模型是否优于既有路径」；四消融分别对应通道、门控、文字对齐与枢纽；主指标是检索，OCR 准确率只是中间量。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 条件与指标名称；`available`。**无实测数值** |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | 单元格必须留空；行名用对照全称，不用 B0–B2 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 行：多语 CLIP 零样本 | 方法对照 | E16, E28 | source-explicit | proposed |
| 行：无文字通道 | 方法对照 | E16, E28 | source-explicit | proposed |
| 行：OCR—翻译流水线 | 方法对照 | E16, E28 | source-explicit | proposed |
| 行：完整模型（ours 高亮） | 方法对照 | E28 | source-explicit | proposed |
| 行：去 \(s\) | 问题一消融 | E22, E28 | source-explicit | proposed |
| 行：去门控 | 问题二消融 | E22, E28 | source-explicit | proposed |
| 行：去 \(\mathcal{L}_{s\rightarrow t}\) | 问题二消融 | E28 | source-explicit | proposed |
| 行：去 \(\mathcal{L}_{\mathrm{hub}}\) | 问题三消融 | E22, E28 | source-explicit | proposed |
| 列：Recall@1 / Recall@5 / MRR | 主指标 | E21, E27 | source-explicit | expected |
| 列：RUST 识别准确率 | 中间指标，非主验收 | E18 | source-explicit | expected |
| 列：理解准确率 | 辅助协议 | E20, E21, E27 | source-explicit | expected |
| 标记：无填入数值 / 不把 OCR 解释为检索增益 | 防伪 | E06, E31 | source-explicit | proposed |
| 标记：200–400 题为拟构建 | 防伪 | E15, E38 | source-explicit | proposed |

**禁止入图**：虚构柱高、热图、显著性星号、样本量单元格中的 60 万/4000/29,000 作为已完成 N、BLEU 主列。

---

### F5

| 字段 | 内容 |
|---|---|
| `figure_id` | F5 |
| `proposed_title` | 可关闭文字通道的门控残差融合与分通道对齐 |
| `target_section` | （一）3.1 研究方法，式 (2)–(5) 附近（约 p.8） |
| `reviewer_question` | 外观、连写维文与维/汉描述如何进入同一表征，又如何被单独关掉以做干净消融？ |
| `figure_type` | Module Detail |
| `figure_form` | mechanism / key method → Module Detail |
| `priority` | strong |
| `source_evidence` | E05, E19, E23, E24, E25, E26, E30 |
| `core_message` | \(s=\mathbf{0}\) 即关闭文字通道；\(z\) 是对外观的门控残差，不是强制拼接；外观—文本与文字—文本分开对齐，枢纽损失经 \(z\) 对齐双语描述。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 机制标签与式 (1)(2) 符号；`available` |
| `aspect_ratio` | 4:3 |
| `style_family` | classic_academic |
| `unknowns` | \(\alpha,\lambda_s,\lambda_{\mathrm{hub}},\tau,W\) 的具体数值未给出；网络维度未给出 → 图内不放数值与张量形状 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 左上：图像 \(I\) | 输入 | E23 | source-explicit | proposed |
| 左中：文字区域 \(\{t_k\}\) | 输入 | E23 | source-explicit | proposed |
| 左下：\(y^{\mathrm{ug}}\) / \(y^{\mathrm{zh}}\) | 输入 | E23 | source-explicit | proposed |
| \(f_v \rightarrow v\)；\(f_s \rightarrow s\)；\(f_\ell \rightarrow h^{\ell}\) | 编码器（只标符号，不画层） | E23 | source-explicit | proposed |
| 无文字：\(s=\mathbf{0}\)，通道关闭 | 开关 | E18, E23 | source-explicit | proposed |
| 中心：\(z=v+\alpha\sigma(W[v;s])\odot s\) | 核心机制 | E24 | source-explicit | proposed |
| 检索：\(\mathrm{sim}(z,h)\) | 输出打分 | E25 | source-explicit | proposed |
| 损失：\(\mathcal{L}_{v\rightarrow t}\) / \(\mathcal{L}_{s\rightarrow t}\) / \(\mathcal{L}_{\mathrm{hub}}\) | 监督 | E26 | source-explicit | proposed |
| 比较旁注：拼接 / 单 InfoNCE / 门控双对齐 | 可证伪 | E19 | source-explicit | proposed |
| 脚本约束：连写、从右向左（标注，不画字体渲染） | 文字编码器约束 | E02, E30 | source-explicit | proposed |

**caption_reserve（不进图）**：式 (4) 完整 InfoNCE、\(\tau\)、批大小、\(\lambda\) 数值、\(W\) 尺寸、CLIP/STR 内部层名、任何隐藏维度。

---

### F6

| 字段 | 内容 |
|---|---|
| `figure_id` | F6 |
| `proposed_title` | 两年两阶段研究计划与阶段性验收 |
| `target_section` | （一）5.1 年度研究计划（约 p.10） |
| `reviewer_question` | 两年内先冻结什么、后验证什么，阶段性验收如何对齐三项科学问题？ |
| `figure_type` | Overall Framework |
| `figure_form` | timeline → Overall Framework |
| `priority` | nice |
| `source_evidence` | E33, E34, E31 |
| `core_message` | 2027 年确认 \(f_s\) 并得到三类基线可复现分数；2028 年完成门控、枢纽、检索与理解协议，并检验 H1–H3。 |
| `existing_asset_relation` | new |
| `proposed_render_action` | draw_new |
| `data_requirement` | 阶段标签；`available` |
| `aspect_ratio` | 16:9 |
| `style_family` | classic_academic |
| `unknowns` | B0–B2 已确认对应但仍不进图；H1–H3 假设全文仍未展开 |

**must_show**

| 元素 | 角色 | evidence_ids | evidence_status | research_state |
|---|---|---|---|---|
| 第一年 2027.01–12：合规、SUST/RUST、无文字通道与 OCR—翻译、评测脚本 | 阶段 | E33 | source-explicit | proposed |
| 第一年验收：\(f_s\) 可用 + B0–B2 分数 | 节点 | E33 | source-explicit | expected |
| 第二年 2028.01–12：门控融合、视觉枢纽、Multi30k-Distant、200–400 题、SCI | 阶段 | E33 | source-explicit | proposed |
| 第二年验收：H1–H3 检验 | 节点 | E33, E31 | source-explicit | expected |
| 负结果边界：文字通道仅对文字主导图像有效 / 枢纽不优于翻译 | 退出 | E31 | source-explicit | proposed |

**图形适配风险**：两年两阶段正文已按时间写清，用三线表更省篇幅。审核阶段可改为 `no_figure`。

---

## 优先级排序

| 优先级 | 图 | 评审价值 |
|---|---|---|
| must | F1 | 让评审在参考文献前看清「为什么 CLIP/STR/翻译枢纽都不够」 |
| must | F2 | 让三项问题/三项内容/两条创新对位，避免被读成系统集成或第三条创新 |
| must | F3 | 让编码—融合—评价与三张表节点可见 |
| strong | F5 | 放大可关闭通道的门控残差；公式已在正文，但消融接口需要看见 |
| strong | F4 | 让可证伪设计一眼可读；若与 F3 胶囊重复则降为表 |
| nice | F6 | 两年计划正文已清楚 |

**不进入计划（unsupported 或无证据）**

| 想法 | 原因 |
|---|---|
| CLIP / STR / Transformer 层栈 Network Architecture | 贡献是门控融合与评价协议，不是新骨干；硬改写属于 unsupported |
| Data Behavior：Recall 曲线、消融热图、t-SNE | 申报书无已测数值；`data_requirement: absent` |
| 维文书法/街景照片拼贴 | 装饰性；无授权实景图可放入申请书 |
| 研究基础成果墙、GPU 清单、经费饼图 | 更适合文字；装饰性 |
| 民汉翻译系统 / 语音 / 舆情 / 教学资源架构 | 明确排除（E04, E12） |

---

## 分章节图数与作用

| 章节 | 图 | 作用 |
|---|---|---|
| 立项依据 1.3–1.4 | F1 ×1 | 缺口来源 |
| 内容/目标/问题 2.3 | F2 ×1 | 问题—内容—创新闭环 |
| 方案 3.1 | F5 ×1（strong） | 机制放大 |
| 方案 3.2 | F3 ×1 + F4 ×1（strong） | 路线与可证伪矩阵 |
| 年度计划 5.1 | F6 ×1（nice） | 时间 |
| 创新 / 基础 / 工作条件 | 0 | 正文已对位，不再重复 |

---

## 总图数、页面成本与可删减顺序

- 建议绘制集合：6（3 must / 2 strong / 1 nice）
- 对 15 页开放课题正文（含约 3 页文献）：优先落地 **F1+F2+F3**（约 1.6–2.0 页）
- 预计页面成本：F1 0.50 页；F2 0.55 页；F3 0.55 页；F4 0.50 页；F5 0.45 页；F6 0.35 页；合计约 2.9 页（全画）或 1.6 页（仅 must）
- **可删减顺序**：F6 → F4（改为三线表）→ F5（改回公式+短文）→ 不得删 F1/F2/F3
- 若第（一）部分已接近篇幅上限：只保留 must 三图

---

## completeness

```yaml
completeness:
  analyzed_materials:
    - /home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2026_MUC_Lab/main.pdf (p.1-15, text layer)
    - extraTex/1.3.方案及可行性.tex (formula checksum only)
    - docs/00_项目基本信息.md (title only; not used as scientific evidence)
  output_type: complete
  high_confidence_information:
    - 无现有插图
    - 中文题目全称已由用户确认
    - B0–B2 与四对照对应已由用户确认（图内不画代号）
    - 三项科学问题 / 三项研究内容 / 两条创新
    - 技术路线「编码—融合—评价」与四对照、四消融
    - 式 (1)–(6) 符号与门控残差
    - 明确排除翻译系统、语音、舆情；200–400 题为拟构建
  pending_confirmation:
    - H1–H3 假设正文（PDF 仅点名）
    - α、λ、τ、隐藏维度等数值（未给出）
  suggested_materials:
    - 若需 Data Behavior 图：提供开发集预实验真实数值后再规划
    - 若需与旧 PNG 对齐：提供 figures/ 下现有文件（当前为空）
```
