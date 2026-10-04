# 配图规划

已读取23页文字基线与活动正文，采用Academic Paper Analyzer & Figure Planner规划。共7图：5张核心图和2张设计辅助图；每条真实路线R1/R2/R3各有一张。所有图为拟研究机制或计划，无已有性能图。全图16:9，按正文宽度0.98排版，预计含图27—29页；最终以实际PDF验收。

绘图规则来源：仓库根目录绘图提示词.md。计划配色classic Nature Blue，白底彩边；避免无资料的设备、企业图标和结果曲线。

## F01：长程任务中的上下文约束、证据风险与研究切入点

作用：Arrange nine white cards in three balanced rows of three. The top row is a temporal chain with two solid rightward arrows. A thin brace below that row spans all three risk cards in the middle row: risks can occur throughout the trajectory, not a one-to-one causal mapping of top cards. Each middle risk card points down to its corresponding bottom research card. Bottom cards are visually strongest. Use no pictograms. Preserve generous gutters and leave the top margin blank; no overall title.

落点：`extraTex/1.1.立项依据.tex`，锚点为“本项目的中心科学问题是：”起始的完整段落。比例16:9，预计0.6页。必须要素：任务指令；多步工具交互；环境状态变化；状态遗漏；恢复不确定；额外开销；R1 保真压缩；R2 有效恢复；R3 预算调度。优先级：必需。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F02：ACORE总体框架：状态保留、有效恢复与全开销调度

作用：Use three principal white modules in a left-to-right middle row: R1, R2, R3. A smaller visible-history card above R1 feeds R1 and the archive card below R1 by two separate solid arrows, making archive-before-compression explicit. The archive sends a rightward-then-upward connector into R2. R3 points downward to execution at bottom right. Execution has a dashed outer feedback path returning to visible history. Place the evaluation strip beneath the modules with a connector from execution; keep this distinct from the feedback loop. The final evaluation strip does not feed the method. Keep arrow lanes completely clear of text.

落点：`extraTex/2.1.研究内容.tex`，锚点为“\textbf{总体技术路线。}”起始的完整段落。比例16:9，预计0.6页。必须要素：可见历史；R1 保真压缩；R2 有效恢复；R3 预算调度；原文档案；执行模型；共同评测。优先级：必需。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F03：R1：以未完成动作依赖指导任务状态保真压缩

作用：Use a top horizontal sequence of three large cards with rightward arrows. From value estimation, a clean distribution line branches downward into three equal representation cards across the middle row. Their three downward connectors merge into a wide output card near the bottom center. A small dashed-border ablation card sits below or beside the output, connected by a dashed diagnostic line only. Make the three representation forms equally prominent: they are alternative granularities, not a serial processing sequence. A tiny neutral line divider under each card title provides the visual hierarchy. Do not add metrics, curves, labels about training results, or future observations.

落点：`extraTex/2.1.研究内容.tex`，锚点为“这一分路线输出紧凑状态”起始的完整段落。比例16:9，预计0.6页。必须要素：当前可见信息；提取任务状态；估计保留价值；原文片段；结构化事实；子任务概要；紧凑状态与来源索引；开发阶段消融。优先级：必需。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F04：R2：从动作前提出发的证据卸载、回读与适用性核对

作用：Create a top left-to-right sequence of three white cards. Under the middle locating card, put a separate archive card feeding it upward. Current-applicability checking branches down-right to a verified-evidence card with the exact connector label "满足前提". Its second branch routes down-left to a larger requery card with the exact label "仍不确定". Requery has a dashed feedback arrow returning to applicability checking. A separate arrow from requery leads to the budget-exhaustion termination card. Keep the archive independent of environment requery; do not imply that rereading old bytes updates business state. Use color only for module borders, never red/green traffic signals or icons.

落点：`extraTex/2.1.研究内容.tex`，锚点为“此分路线输出经核对的证据”起始的完整段落。比例16:9，预计0.6页。必须要素：拟执行动作；定位原文片段；核对当前适用性；不可变原文档案；经核对的证据；请求原文或环境重查；资源不足则中止。优先级：必需。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F05：R3：结合恢复反馈和共同资源约束的全开销调度

作用：Use three compact input cards in the top row, each pointing down to one broad controller card. The controller has three distinct downward outgoing arrows toward the lower operation cards. All operation cards point to a wide bottom cost ledger. A dashed outer loop returns the ledger feedback to the remaining-budget card. Keep controller and execution distinct: the controller chooses context operations and the execution model is fixed, not trained here. Do not display a mathematical optimization formula, performance curve, percentages or guaranteed savings. The ledger is descriptive accounting rather than a claim of measured improvement. White backgrounds and restrained blue borders throughout.

落点：`extraTex/2.1.研究内容.tex`，锚点为“三条路线形成可观察的反馈关系：”起始的完整段落。比例16:9，预计0.6页。必须要素：当前工作状态；恢复反馈；剩余预算；规则或轻量控制器；保留 / 压缩；卸载 / 恢复；重查；完整成本记录。优先级：必需。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F06：依赖保留与有效性核验的交叉设计及共同评测条件

作用：Build a large clean two-by-two factorial table in the center, with two column headers and two row headers. The first row is dependency retention off, the second on; the first column is validity checking off, the second on. Cell identifiers must be exactly 00, 01, 10, 11 in reading order. Above it place a single wide shared-conditions strip. Beneath the table place three equal endpoint cards. Use thin gray grid lines with heavier blue outside borders, and white cell fills. Do not use heatmap colors or numerical results. No data-flow arrow is required inside the table because the four cells are comparison groups, not sequential steps.

落点：`extraTex/2.1.研究内容.tex`，锚点为“核心机制实验采用”起始的完整段落。比例16:9，预计0.6页。必须要素：四组共同条件；不核验有效性；核验有效性；不保留依赖；保留依赖；00；01；10；11；主要终点；诊断指标；代价核算。优先级：辅助。科学来源与完整锚点见figure_manifest.json；无数据结论。

## F07：暂定12个月研究安排：开发验证、机制比较、集成与复现

作用：Use five evenly spaced vertical phase cards across a single horizontal timeline. Each phase has its relative-month header in navy, a thin blue divider, and three separate short Chinese task lines. Connect only adjacent phase cards with small rightward arrows along a single level. Beneath all phases place one wide white annotation strip with the tentative-period header and contract qualification. The sequence is a proposed research schedule: do not add completion checkmarks, percentages, approval stamps, or calendar dates. Keep all five cards identical in width and height. Make the annotation as legible as the task labels, with sufficient bottom margin.

落点：`extraTex/2.3.年度研究计划.tex`，锚点为“项目按资料建议采用”起始的完整段落。比例16:9，预计0.6页。必须要素：M1—M2；M3—M5；M6—M8；M9—M10；M11—M12；暂定研究周期。优先级：辅助。科学来源与完整锚点见figure_manifest.json；无数据结论。

插图引导语统一使用完整陈述句，最终图题以figure_manifest.json为准；仅调整图题语法，所有图内标签及科学来源保持一致。
