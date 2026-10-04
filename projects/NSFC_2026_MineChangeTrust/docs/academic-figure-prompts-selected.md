# Academic Figure Prompt：选定7图

**当前执行状态：选定7图已插入正文，main.pdf为25页。** 本文下方“未生图/未插图”等措辞为规划阶段记录，实际交付以[正文插图记录](figure_insertion.md)为准。第7图按真实JSON重绘。

当前范围由用户选定：F01—F05、F14、合并后的F15＋F16。图内中文短标签，英文视觉提示词；每图配套JSON。未生图，未修改PDF。

| 正文图号 | 规划ID | 图名 | 比例 |
|---|---|---|---|
| 图1 | F01 | 研究背景：真实地表变化、外观差异与复核需求 | 16:9 |
| 图2 | F02 | 总体研究框架：失效证据—机制检验—复核评价 | 16:9 |
| 图3 | F03 | 研究路线一：矿区来源核验与误差诊断 | 16:9 |
| 图4 | F04 | 研究路线二：约束区域与负迁移条件检验 | 16:9 |
| 图5 | F05 | 研究路线三：校准、错误排序与固定面积复核 | 16:9 |
| 图6 | F14 | 已完成预实验流程：固定子样本与九模型运行 | 16:9 |
| 图7 | F15_F16 | 预实验结果与矿区配对效应：检测收益、召回代价及不确定性 | 4:3 |

图7为4:3的2×3组合图，其余为16:9。统一采用既有[配色方案](Figure_Palette.md)。详细目的和来源见[Figure Plan](Figure_Plan.md)。

## 图1 · F01｜研究背景：真实地表变化、外观差异与复核需求

类型：Research Background；16:9；结构/设计示意；英文词数277。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a left-to-right motivation storyboard. Split the paired mine observations into two vertically aligned conceptual alternatives, then reconverge them at prediction errors and bounded review. Keep the two alternatives equally prominent. A changed boundary is geometric; appearance differences use neutral hatching without moving that boundary. These mini-scenes are conceptual line drawings, never photographs or geolocated observations.

Use these anchors in their corresponding spatial blocks: contour drawing of an open-pit terrace and an adjacent vegetation patch; paired abstract outlines with one changed boundary; identical contours with different neutral hatch densities; two equal mask grids, one with extra outlines and one with missing outlines; magnifier above a complete window grid.

Render the locked Chinese labels exactly as supplied: “矿山地表”; “两期观测”; “真实变化”; “边界改变”; “外观差异”; “边界不变”; “误报与漏检”; “需区分”; “可信复核”; “有限面积”; “概念示意”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：矿山两期影像同时包含地物边界变化和观测外观差异。图示说明两类差异可能引起误报或漏检，以及有限复核面积下识别错误的研究需求；所有场景均为概念示意。

限制：不画污染等级、沉降预警、实时事件、已建成新疆示范区；不把外观差异直接画成已证实的误差原因。

[对应JSON规范](figure_specs/F01.json)

## 图2 · F02｜总体研究框架：失效证据—机制检验—复核评价

类型：Overall Framework；16:9；结构/设计示意；英文词数282。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic architecture diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Arrange five major blocks in one horizontal chain. The middle three correspond exactly to the three research contents, with the same names used in their dedicated route figures. Label the handoff from diagnosis as verified samples and strata, and the next handoff as a frozen detector. Below the chain, reserve a thin detached strip for conditional external validation; it is not a sixth core module. Do not depict a deployed monitoring platform.

Use these anchors in their corresponding spatial blocks: paired image frames with a small source ledger; magnifier above a confusion grid; feature maps beside a binary mask; fixed model outline beside a ranked window grid; document with a split effect marker.

Render the locked Chinese labels exactly as supplied: “公开影像”; “标签／矿区”; “误差诊断”; “内容一”; “区域约束”; “内容二”; “复核评价”; “内容三”; “[固定]”; “条件与反例”; “矿区证据”; “核验与分层”; “冻结检测器”; “外部验证（条件性）”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：总体框架包含公开输入、误差诊断、区域约束检验、冻结检测器的复核评价及矿区证据输出五个主模块。配准或标签问题占主导时先返回质量诊断；外部验证为有条件扩展。

限制：内容二是待检验机制，输出允许无增量和反例；内容三不向检测器回传训练梯度。

[对应JSON规范](figure_specs/F02.json)

## 图3 · F03｜研究路线一：矿区来源核验与误差诊断

类型：Technical Route；16:9；结构/设计示意；英文词数290。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 7 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Make a main horizontal audit sequence ending in a decision diamond. The upper continuation exports verified samples and strata to route two. The lower branch handles registration or label ambiguity first and loops back to error inspection using a dashed diagnostic arrow. Show source ancestry as connected documents rather than fabricated geographic coordinates. Baseline diagnostics use development mines; do not route held-out test labels into the branch decision.

Use these anchors in their corresponding spatial blocks: three connected ledger sheets for mine, scene and tile; non-overlapping groups of small site tokens; shared neural feature-map pictogram; confusion grid with a magnifier; diamond with two clearly separated outgoing paths; two output ledgers linked by a bracket; offset contour pair with an inspection marker.

Render the locked Chinese labels exactly as supplied: “来源核验”; “矿区—场景”; “独立划分”; “按矿区”; “基线复现”; “训练／验证”; “误差核验”; “分层抽查”; “机制相关？”; “先诊断”; “样本与分层”; “进入路线二”; “质量诊断”; “配准／标签”; “相关”; “质量主导”; “复核”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：路线一核对矿区、原始影像和切片的来源，完成按矿区隔离的开发期复现与误差抽查。仅当主要误差与拟检验机制相关时向路线二输出样本及分层规则。

限制：不把官方划分标成已发现泄漏；无坐标证据不画实际矿区空间分布；测试标签不参与开发决策。

[对应JSON规范](figure_specs/F03.json)

## 图4 · F04｜研究路线二：约束区域与负迁移条件检验

类型：Technical Route；16:9；结构/设计示意；英文词数286。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a controlled-comparison layout with two middle lanes. One lane shows the four same-backbone constraints, while the other records matched controls and exploratory mechanism diagnostics. Bring both lanes into the joint endpoint gate, then export a selected and frozen detector together with limitations. Use equal panel sizes for every comparison arm. The mechanism lane must not imply that a larger effect has already been observed.

Use these anchors in their corresponding spatial blocks: verified paired image frames and a strata ledger; four aligned mask grids with identical outer dimensions; matched-area masks beside equal-length comparison rulers; mask replacement sequence and two gradient vectors; two endpoint cards entering an AND junction; fixed model outline next to a failure-case ledger.

Render the locked Chinese labels exactly as supplied: “核验样本”; “路线一输出”; “同骨干对照”; “四组约束”; “替代解释”; “强度／平滑”; “机制诊断”; “污染／近邻”; “联合判据”; “误报／召回”; “冻结与反例”; “交给路线三”; “辅助解释”; “开发期确定”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：路线二以同骨干背景约束对全图约束为主比较，联合评价误报改善与小变化召回非劣；随机、强度和平滑对照检查替代解释，污染和近邻替换提供辅助诊断。

限制：FCCDN、DonaNet、CDDGNet不是网络串联组件；正式四组不等同于已经完成的三组预实验；不画成功勾号。

[对应JSON规范](figure_specs/F04.json)

## 图5 · F05｜研究路线三：校准、错误排序与固定面积复核

类型：Technical Route；16:9；结构/设计示意；英文词数288。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Draw a frozen detector at the left and two separate development lanes in the middle. Independent calibration mines fit temperature once; validation mines choose among prelisted score rules without refitting temperature. Merge these outputs only at full-scene window ranking. Show ideal correction and remaining errors on the main right-hand path, with real reviewer assessment in a detached dotted extension. No arrows may return from test scoring to training, calibration or selection.

Use these anchors in their corresponding spatial blocks: dashed model outline with a save marker; single temperature dial and calibration-bin grid; small candidate-score cards beside a selector; complete window grid including unchanged predictions; two counters represented by outlined bars; person-free magnifier and a time ledger.

Render the locked Chinese labels exactly as supplied: “冻结检测器”; “参数固定”; “[固定]”; “独立校准”; “只拟合 T”; “验证选择”; “固定规则”; “全图排序”; “同面积预算”; “剩余错误”; “FP／FN”; “真实复核”; “条件扩展”; “概率”; “规则”; “理想纠错”; “条件具备”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：路线三在同一冻结检测器上分别完成温度拟合、验证规则选择和全图窗口排序，以全图剩余FP/FN及真实变化覆盖评价固定面积下的理想纠错上限；真实人员复核另需核验。

限制：不能画成温度缩放必然改变排序；复核窗口必须包含预测未变化区；没有已测节省工时。

[对应JSON规范](figure_specs/F05.json)

## 图6 · F14｜已完成预实验流程：固定子样本与九模型运行

类型：Experimental Setup；16:9；结构/设计示意；英文词数277。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a five-stage horizontal provenance chain with a detached reserve strip beneath it. The first stage contains exactly four shard icons. Sampling shows separate training and validation trays, then a three-by-three run matrix, nine saved final models and ten-mine scoring. The bottom reserve strip is deliberately unconnected to model fitting. Clearly mark the figure as completed pilot evidence, while keeping official test evaluation outside the chain.

Use these anchors in their corresponding spatial blocks: four compact source documents; site tokens feeding two sample trays; three identical model frames with different masks; nine saved model markers; ten site cards with integer confusion counts; detached reserve tokens and test tokens.

Render the locked Chinese labels exactly as supplied: “公开分片”; “四分片校验”; “固定抽样”; “1188／480”; “同种子对照”; “三组×三种子”; “固定末轮”; “12轮／0.5”; “[固定]”; “验证评分”; “90行统计”; “保留与封存”; “未作校准”; “统一评分”; “50训练矿区”; “10验证矿区”; “10保留矿区”; “30测试矿区”; “未读取”; “已运行预实验”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：MCT-P01核验四分片，按固定规则抽取50训练矿区1,188片和10验证矿区480片；三组各三个种子、固定12轮和阈值0.5，九模型保存后统一验证。10个保留训练矿区未用于校准，官方测试未读。

限制：四分片验收不等于完整ZIP验收；不画正式四组全部完成；训练纯耗时约558秒与下载/验证耗时分开。

[对应JSON规范](figure_specs/F14.json)

## 图7 · F15_F16｜预实验结果与矿区配对效应：检测收益、召回代价及不确定性

选定版图7；合并F15和F16；4:3；183mm；真实数据程序绘图规范；英文词数294。本轮不绘图。

```text
Flat vector academic data visualization specification for a programmatically rendered combined point and forest plot. The figure explains measured detection performance and paired mine uncertainty from the same nine archived pilot models.

Arrange six equally sized panels in two rows and three columns. Left, middle and right columns represent change IoU, background false-positive rate and overall recall. In the upper row, place the three experimental arms in a consistent order and show measured means with sample standard deviations across three seed-level mine averages. In the lower row, show background-minus-full and background-minus-none as horizontal point estimates with their complete paired-mine bootstrap intervals. Keep a neutral zero line, retain adverse recall effects, and show intervals crossing zero without winner badges. No flow arrows connect the rows.

Use points and whiskers as the visual anchor in every panel. Lock column titles and difference labels to “变化 IoU”, “背景误报率”, “总体召回率”, “IoU 差”, “误报率差”, and “总体召回差”. Panel tags are “(a)” through “(f)”. Row labels are “均值±种子SD” and “差值及95%区间”; axes use “指标（%）” above and “差异（百分点）” below. Upper categories are “无一致性”, “全区域”, “背景位置”; lower categories are “背景减全区域” and “背景减无约束”. Use separate legends titled “实验组” and “配对比较”. Add “预实验结果” and the footer “小变化召回：NA”. Render numeric ticks exactly from the paired JSON specification.

Keep the layout aligned and restrained, with white #FFFFFF fills, Nature Blue outlines, 1.5pt borders and 1.0pt dividers. Upper series use grey #616161 squares, blue #2E6B9E circles and navy #1B3A5C triangles; lower comparisons use the blue circle and navy triangle with their own legend. Text is #333333. Coordinates must come from the archived JSON payload; never synthesize measurements or convert unavailable endpoints into zero. Full protocols and statistical interpretations belong in the external caption.

Use Noto Sans CJK SC with Arial for Latin labels, titles 10–12pt, primary labels 8–9pt, and secondary notes 7–8pt. Design at 183mm width with sufficient space for both rows. NO emojis, NO lock/fire/lightning icons, NO 3D rendering; no gradients or shadows. Aspect ratio 4:3.
```

图注预留：

- MCT-P01采用50个训练矿区的1,188片和10个验证矿区的480片，三组各运行种子17、29、43；官方测试未读取。
- 上排为三个种子的矿区宏平均及种子样本标准差，单位为%；下排先在每矿区内平均种子，再对十个矿区进行配对重采样，表示95%区间，单位为百分点。两类误差条不可互换。
- 背景减全区域的IoU、FPR、总体召回差分别约为+0.760、−3.348、−4.105个百分点，对应95%区间为[−0.057,1.515]、[−4.217,−2.567]、[−6.236,−2.233]；背景减无约束的三项区间均跨零。保留全部六项比较，不宣称联合优势已获支持。
- 预定小变化端点在480片中没有合格对象，记NA；它不等于零召回，也不能被总体召回替代。
- 上排色形表示实验组，下排色形表示比较对象；分别标注图例。完整数值、协议和解释保留在外部图注。

[对应JSON规范](figure_specs/F15_F16.json)

完整性：选定7图的规范和提示词齐全；合并图四份数据载荷与原始结果一致。物理页码、实验统计口径和未知参数边界沿用已核验来源。实际成图的字体、线条和缩印检查留待制图后执行。
