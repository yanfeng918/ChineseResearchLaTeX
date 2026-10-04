---
document: "配图规划索引"
stage: "05_figure_plan"
project: "NSFC_2027_Mapping"
version: "2026-09-06"
---

# 05 配图规划

来源：`main.pdf`（2026-09-05 编译版）+ `docs/04_研究方案与技术路线.md`。全程只读标书，未修改任何 `extraTex/*.tex`，未插图，未生成图像。

| 文件 | 内容 | 产出技能 |
|---|---|---|
| [01_Figure_Plan.md](01_Figure_Plan.md) | 12 张图的规划：章节映射、优先级、比例、必现视觉元素、完整性块、落地组合建议 | academic-paper-analyzer-figure-planner v1.2.0 |
| [02_Palette_Decision.md](02_Palette_Decision.md) | 配色决策、语义色绑定契约、六条视觉语法、无障碍与灰度打印、逐图配色分配 | academic-figure-color-expert v1.3.2 |
| [03_Figure_Prompts_F01-F06.md](03_Figure_Prompts_F01-F06.md) | F1—F6 的 JSON spec + 英文出图 prompt + caption 保留内容；含 CJK 渲染对策与共用样式 | academic-figure-prompt v1.5.0 |
| [04_Figure_Prompts_F07-F12.md](04_Figure_Prompts_F07-F12.md) | F7—F12 的 JSON spec + 英文出图 prompt + caption 保留内容；含出图后全局检查清单 | academic-figure-prompt v1.5.0 |
| **[05_最终选图.md](05_最终选图.md)** | **决定稿：正文实际收录的 7 张、篇幅账、LaTeX 插入片段、落选理由与替换选项** | — |

## 12 张图速览（★ = 正文收录）

| 图号 | 中文图名 | 类型 | 比例 | 收录 |
|---|---|---|---|---|
| F1 | 研究背景与问题提出图 | Conceptual Background | 16:9 | — |
| **F2** | 描述不完备导致的三态歧义示意图 | Problem Illustration | 4:3 | ★ |
| F3 | 研究现状三条脉络与本项目切入点 | Landscape / Positioning | 16:9 | — |
| **F4** | 总体研究框架图 | Overall Framework | 16:9 | ★ |
| **F5** | 技术路线图一：关系证据三态建模 | Technical Route | 3:2 | ★ |
| **F6** | 技术路线图二：三臂对照的关系约束匹配 | Technical Route / Network Arch | 16:9 | ★ |
| **F7** | 技术路线图三：分层验证与可归因性控制 | Technical Route / Eval Protocol | 16:9 | ★ |
| F8 | 三态判定的三类证据源与适用边界 | Module Detail | 4:3 | 备选 A |
| **F9** | 与最相关工作的差异定位图 | Comparison | 3:2 | ★ |
| F10 | 年度研究计划与里程碑 | Timeline / Gantt | 16:9 | 备选 B |
| **F11** | 假说—证伪判据—降级路径 | Decision Flow | 16:9 | ★ |
| F12 | 申请人积累与项目需求对位图 | Mapping | 4:3 | — |

## 最终选图

正文收录 **7 张：F2、F4、F5、F6、F7、F9、F11**。落点、宽度、篇幅账、LaTeX 插入片段、
落选理由与两个替换选项见 **[05_最终选图.md](05_最终选图.md)**。

关键约束：当前正文 29 页（上限 30），7 张图约占 3.0–3.3 页，**需先腾出 2.0–2.5 页正文**。
未收录的 5 张仍保留完整 prompt，可用于答辩、汇报与后续论文。

## 出图前需申请人确认的三件事

1. **图上文字语种**——中文（渲染风险高）/ 英文出版式再回填中文 / 直接 draw.io 手绘，见 `03_Figure_Prompts_F01-F06.md` 开头的 CJK 渲染对策。
2. **F9 两轴命名**——「关系语义的处理」×「失配的处理」为本规划提出的表述（推断），正文只给了文字差异说明。
3. **第 7 张是否维持 F11**——两个等成本替换：F8（若更担心"三态怎么判"的可行性质疑）、F10（若担心证伪路径图让评审不安）。见 `05_最终选图.md` 第六节。

## 边界说明

- 本目录只做规划与 prompt，不生成图像、不修改标书正文、不向 `figures/` 写入任何文件。
- 所有 `【暂定 …】` 数值与正文保持同一措辞；正文这些标记变更时，需回到本目录同步。
