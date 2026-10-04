# Academic Figure Prompt Package

**当前选定7图：** F01—F05、F14、F15＋F16合并图。请优先使用[选定版完整提示词](academic-figure-prompts-selected.md)；下文为原22张候选提示词库。合并图另见[JSON](figure_specs/F15_F16.json)与[Prompt](figure_specs/F15_F16.prompt.md)。

依据[Figure Plan](Figure_Plan.md)和[Palette Decision](Figure_Palette.md)生成的22组独立配图规范。每组含可解析JSON和200—400英文词的视觉提示词，图内文字为中文短标签。当前只交付规范，没有生成、修改或插入图片，没有训练/重跑实验。

先查看JSON中的精确文本、连接和source_span，再使用英文brief。结构示意图可在后续明确制图任务中交给图像模型或矢量编辑器；F15/F16/F18是程序绘图规范，F19是真实资产排版规范，不能让图像模型猜测数据或重画科学像素。

统一配色为Nature Blue，主/辅/第三色#1B3A5C / #2E6B9E / #5BA0D0，深灰文字#333333、白底#FFFFFF。容器白色填充，只用彩色描边；冻结和可训练状态以文字及虚/实线双重标识。正式骨干或尚未冻结参数不凭空补充。

| ID | 图名 | JSON | 完整提示词 | 英文词数 | 制作方式 |
|---|---|---|---|---:|---|
| F01 | 研究背景：真实地表变化、外观差异与复核需求 | [规范](figure_specs/F01.json) | [Prompt](figure_specs/F01.prompt.md) | 277 | 结构/设计示意 |
| F02 | 总体研究框架：失效证据—机制检验—复核评价 | [规范](figure_specs/F02.json) | [Prompt](figure_specs/F02.prompt.md) | 282 | 结构/设计示意 |
| F03 | 研究路线一：矿区来源核验与误差诊断 | [规范](figure_specs/F03.json) | [Prompt](figure_specs/F03.prompt.md) | 290 | 结构/设计示意 |
| F04 | 研究路线二：约束区域与负迁移条件检验 | [规范](figure_specs/F04.json) | [Prompt](figure_specs/F04.prompt.md) | 286 | 结构/设计示意 |
| F05 | 研究路线三：校准、错误排序与固定面积复核 | [规范](figure_specs/F05.json) | [Prompt](figure_specs/F05.prompt.md) | 288 | 结构/设计示意 |
| F06 | 数据划分与信息隔离：官方协议、正式设计和测试封存 | [规范](figure_specs/F06.json) | [Prompt](figure_specs/F06.prompt.md) | 290 | 结构/设计示意 |
| F07 | 核心机制：训练背景位置约束与全区域分割监督 | [规范](figure_specs/F07.json) | [Prompt](figure_specs/F07.prompt.md) | 286 | 结构/设计示意 |
| F08 | 可归因对照矩阵：区域、面积、形状、强度与平滑 | [规范](figure_specs/F08.json) | [Prompt](figure_specs/F08.prompt.md) | 283 | 结构/设计示意 |
| F09 | 统计判据：误报改善与小变化召回非劣的联合检验 | [规范](figure_specs/F09.json) | [Prompt](figure_specs/F09.prompt.md) | 288 | 结构/设计示意 |
| F10 | 外观差异代理：计算流程、分层与混杂核查 | [规范](figure_specs/F10.json) | [Prompt](figure_specs/F10.prompt.md) | 263 | 结构/设计示意 |
| F11 | 概率校准与错误排序：两个不同问题 | [规范](figure_specs/F11.json) | [Prompt](figure_specs/F11.prompt.md) | 266 | 结构/设计示意 |
| F12 | 固定预算与等实际面积复核：全图剩余错误的计算 | [规范](figure_specs/F12.json) | [Prompt](figure_specs/F12.prompt.md) | 292 | 结构/设计示意 |
| F13 | 误差类型图谱：背景误报、高置信漏检与标签争议 | [规范](figure_specs/F13.json) | [Prompt](figure_specs/F13.prompt.md) | 264 | 结构/设计示意 |
| F14 | 已完成预实验流程：固定子样本与九模型运行 | [规范](figure_specs/F14.json) | [Prompt](figure_specs/F14.prompt.md) | 277 | 结构/设计示意 |
| F15 | 预实验结果：检测收益与召回代价 | [规范](figure_specs/F15.json) | [Prompt](figure_specs/F15.prompt.md) | 253 | 真实数据程序绘图 |
| F16 | 预实验配对效应：矿区区间与不确定性 | [规范](figure_specs/F16.json) | [Prompt](figure_specs/F16.prompt.md) | 269 | 真实数据程序绘图 |
| F17 | 小变化端点可估计性：从标签定义到NA | [规范](figure_specs/F17.json) | [Prompt](figure_specs/F17.prompt.md) | 275 | 结构/设计示意 |
| F18 | D_s扩展结果：可计算性、误差关联与变化占比混杂 | [规范](figure_specs/F18.json) | [Prompt](figure_specs/F18.prompt.md) | 276 | 真实数据程序绘图 |
| F19 | 固定矿区案例：两期影像、真值与三组预测 | [规范](figure_specs/F19.json) | [Prompt](figure_specs/F19.prompt.md) | 279 | 真实资产排版 |
| F20 | 外部验证与语义边界：MineNetCD、EuroMineNet和铜矿边界 | [规范](figure_specs/F20.json) | [Prompt](figure_specs/F20.prompt.md) | 263 | 结构/设计示意 |
| F21 | 24个月任务进度与冻结节点 | [规范](figure_specs/F21.json) | [Prompt](figure_specs/F21.prompt.md) | 277 | 结构/设计示意 |
| F22 | 已运行轻量孪生网络：多尺度差分与训练损失 | [规范](figure_specs/F22.json) | [Prompt](figure_specs/F22.prompt.md) | 281 | 结构/设计示意 |

## 完整英文提示词

以下逐图列出，可复制使用；严格数据约束以同名JSON为准，JSON不是要求模型打印的图中文字。

### F01｜研究背景：真实地表变化、外观差异与复核需求

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


### F02｜总体研究框架：失效证据—机制检验—复核评价

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


### F03｜研究路线一：矿区来源核验与误差诊断

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


### F04｜研究路线二：约束区域与负迁移条件检验

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


### F05｜研究路线三：校准、错误排序与固定面积复核

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


### F06｜数据划分与信息隔离：官方协议、正式设计和测试封存

类型：Protocol Diagram；16:9；结构/设计示意；英文词数290。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 7 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use three horizontal bands: the published split, the proposed development responsibilities, and the sealed evaluation path. Branch only the original training partition into training and calibration. Keep validation and test partitions aligned with their published origins. Place a vertical boundary before final scoring; both frozen rules and held-out observations enter that scoring panel, with no return edge. A short caption distinguishes these proposed counts from the completed pilot reserve.

Use these anchors in their corresponding spatial blocks: three separate rows of mine tokens; training tokens feeding a model pictogram; calibration tokens beside a single scalar dial; validation tokens and candidate cards; isolated test tokens separated by a vertical boundary; dashed document enclosing final rules; confusion grid receiving predictions and held-out labels.

Render the locked Chinese labels exactly as supplied: “官方划分”; “60／10／30”; “模型训练”; “50 暂定”; “温度拟合”; “10 暂定”; “规则选择”; “测试封存”; “30 暂定”; “全部冻结”; “测试前”; “[固定]”; “最终评分”; “独立评估”; “原训练”; “原验证”; “原测试”; “冻结后”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：官方协议按60/10/30矿区划分。正式主协议拟将原训练部分分出10个独立校准矿区，形成50/10/10/30，仍须归档核验后冻结；MCT-P01仅预留10个训练矿区，未开展温度拟合。

限制：50/10/10/30所有数字标暂定；不将裁切子样本验收画成全量ZIP或官方测试已完成。


### F07｜核心机制：训练背景位置约束与全区域分割监督

类型：Module Detail；4:3；结构/设计示意；英文词数286。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Organize a two-row training graph. The top row carries paired images through shared encoding to change prediction. The lower row introduces training labels only at supervision nodes: one path creates an eroded unchanged mask for feature consistency, and another supervises segmentation across all valid pixels. Use a clear training-only divider. A small detached inference inset repeats only image input, shared encoder and prediction, with no label or mask input.

Use these anchors in their corresponding spatial blocks: two aligned image frames; paired feature-map stacks tied by an equality bracket; binary spatial prediction grid; binary label grid with an eroded interior contour; masked distance cells with an averaging bracket; two-class label grid reaching all valid locations.

Render the locked Chinese labels exactly as supplied: “两期影像”; “共享输入”; “共享编码”; “同一骨干”; “[训练]”; “变化预测”; “全图输出”; “训练标签”; “未变化区”; “背景约束”; “按面积归一”; “分割监督”; “全部有效区”; “特征”; “预测”; “掩码”; “真值”; “训练阶段”; “推理阶段”; “仅训练标签”; “研究设计”; “L = Lseg + λLbg”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：图示为正式研究的功能性损失结构，骨干尚未锁定。分割监督覆盖全部有效区，背景约束在训练标签经腐蚀后的位置计算；空掩码项为零。背景位置特征仍可能受感受野与空间归一化影响。

限制：不编造正式骨干层数、通道数或预训练模块；仅保留一行总损失，完整公式进图注；测试侧没有真值输入。


### F08｜可归因对照矩阵：区域、面积、形状、强度与平滑

类型：Comparison / Ablation；16:9；结构/设计示意；英文词数283。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use an equal-size two-by-three matrix. The first four cells share the same tiny scene and segmentation target, differing only in the constraint overlay. The fifth cell represents sensitivity controls and the sixth holds independent complete comparison methods. Do not connect the cells as sequential network layers. A narrow shared footer records equal backbone, training steps and search budgets without filling every cell with repeated prose.

Use these anchors in their corresponding spatial blocks: empty constraint overlay on a common mask frame; full-frame outlined constraint grid; unchanged-area contour within the same frame; relocated contour with matched area and boundary markers; gradient-length rulers next to an outline smoothing stencil; three separate reference-method cards.

Render the locked Chinese labels exactly as supplied: “无一致性”; “共同监督”; “全区域”; “有效区域”; “背景位置”; “训练标签”; “等面积随机”; “匹配形状”; “强度与平滑”; “敏感性对照”; “完整近邻”; “独立比较”; “FCCDN”; “DonaNet”; “CDDGNet”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：前三组和等面积随机组承担受控比较，进一步记录形状、边界和强度匹配残差；平滑及完整近邻为不同性质的对照。矩阵说明实验设计，不表示这些正式实验均已运行。

限制：不用空白假表表示已测指标；不把完整近邻与仅掩码替换混在一列成绩。


### F09｜统计判据：误报改善与小变化召回非劣的联合检验

类型：Statistical Protocol；4:3；结构/设计示意；英文词数288。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 7 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Build a top row that transforms valid observations into site-level paired intervals. Under it, place two equally sized symbolic endpoint panels feeding a joint decision. Use abstract interval brackets without fabricated numerical outcomes. A clearly separate unavailable-endpoint branch bypasses the decision and ends at NA. Show seed tokens grouped inside site outlines, never as independent resampling units.

Use these anchors in their corresponding spatial blocks: two denominator cards with a validity filter; multiple seed tokens nested inside each site outline; site outlines resampled as whole units; symbolic interval bracket next to an improvement boundary; symbolic interval bracket next to a noninferiority boundary; AND junction leading to two evidence categories; unavailable endpoint card detached from the joint decision.

Render the locked Chinese labels exactly as supplied: “有效端点”; “排除 NA”; “矿区内汇总”; “先均种子”; “矿区重采样”; “配对区间”; “误报改善”; “上界判据”; “召回非劣”; “下界判据”; “联合解释”; “支持／不足”; “不可估计”; “NA”; “端点有效”; “端点为空”; “且”; “证据不足”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：先在每矿区内汇总运行，再对有效矿区配对重采样。背景误报差上界低于−ε且小变化召回差下界高于−δ，才满足联合判据；界值须有独立依据，区间跨零不等于非劣，端点为空不可检验。

限制：ε、δ无具体冻结数值；不能把预实验总体召回替代正式小变化召回；不画虚构的功效曲线。


### F10｜外观差异代理：计算流程、分层与混杂核查

类型：Data Behavior / Protocol；4:3；结构/设计示意；英文词数263。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Place paired observations and the unchanged mask at the left, converging on a two-level aggregation operator. The top continuation creates prespecified appearance strata. Beneath it, use an undirected association bracket to flag changing class proportions, explicitly avoiding a causal arrow from appearance to errors. Link the strata to background false-positive reporting, with IoU interpretation reserved for the caption.

Use these anchors in their corresponding spatial blocks: paired grayscale-channel frames; eroded unchanged outline; nested pair-to-site aggregation brackets; two bins separated by a symbolic threshold; proportion grid beside an association bracket; denominator diagram with false-positive outlines.

Render the locked Chinese labels exactly as supplied: “两期可见光”; “固定尺度”; “未变化掩码”; “标签核验”; “两层中位数”; “影像对→矿区”; “预定分层”; “训练界点”; “变化占比”; “混杂核查”; “背景误报率”; “主要分层指标”; “描述比较”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：D_s由未变化有效区内的两期灰度绝对差中位数、再按矿区取中位数得到。正式分层界点取训练矿区并于测试前冻结；同步报告变化占比，避免用IoU组间差异单独推断外观作用。

限制：本图不绘制因果DAG；预实验扩展采用验证矿区中位数作探索分档，与正式训练界点区分。


### F11｜概率校准与错误排序：两个不同问题

类型：Module Detail；4:3；结构/设计示意；英文词数266。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a forked two-lane comparison. The upper lane evaluates probability calibration, while the lower lane evaluates ranking utility under the same frozen detector. Connect calibrated probabilities to the ranking candidates only as one available input, not as a guaranteed improvement. Keep reliability axes empty because no reliability experiment has been completed. The two output panels have equal visual weight and no superiority badge.

Use these anchors in their corresponding spatial blocks: fixed detector logits beside a save marker; single scalar dial; unpopulated reliability-bin grid; entropy distribution outline and aligned multi-view frames; ranked complete-scene windows.

Render the locked Chinese labels exactly as supplied: “固定预测”; “同一检测器”; “[固定]”; “温度缩放”; “概率尺度”; “校准质量”; “Brier／误差”; “熵与分歧”; “预列候选”; “排序效用”; “剩余 FP／FN”; “校准熵”; “结果待验证”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：温度缩放的校准质量与熵/推理分歧的排序效用分别评估。部分排序定义下温度缩放可能不改顺序，须以固定检测器、同面积剩余错误检验增量。

限制：不填补不存在的ECE、Brier、ROC/AUC或理想下降曲线；窗尺度、视图集合、组合权重仍待验证冻结。


### F12｜固定预算与等实际面积复核：全图剩余错误的计算

类型：Module Detail / Evaluation；16:9；结构/设计示意；英文词数292。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Show a complete scene grid on the left and two accounting tracks on the right. The upper track selects whole windows until the next one would exceed the budget. The lower track truncates the same frozen sequences to a common actual pixel area for sensitivity analysis. Both feed ideal correction and full-scene error accounting. Use neutral hatching to mark selected windows; leave predicted unchanged windows visibly eligible.

Use these anchors in their corresponding spatial blocks: full rectangular lattice with partial boundary windows; parallel ordered strips with different hatch patterns; area accumulator with a stop marker at the next full window; aligned rulers ending at the shortest selected area; selected outline replaced by a ground-truth stencil; two confusion counters over the original full scene.

Render the locked Chinese labels exactly as supplied: “全图窗口”; “含未变化区”; “候选排序”; “同一窗口集”; “预算上限”; “整窗停止”; “共同面积”; “敏感性核对”; “理想纠错”; “仅离线”; “剩余错误”; “全图分母”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：主分析按相同预算上限选择完整窗口，另按各方法实际选中面积的最小值核对等面积结果；末窗像素截取仅用于离线敏感性分析。理想纠错后的FP/FN仍分别除以原全图背景/变化面积。

限制：10%为正式主预算暂定值，写图注；不可把选中区域准确率代替全图剩余错误，不能声称节省人工时间。


### F13｜误差类型图谱：背景误报、高置信漏检与标签争议

类型：Error Taxonomy；4:3；结构/设计示意；英文词数264。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 4 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a two-by-two taxonomy with identical conceptual reference and prediction frames. The upper row illustrates observable error patterns; the lower row lists candidate data-quality explanations that require checking. Avoid drawing a one-to-one causal connection between lower and upper cells. Include a small common legend for reference contours, predictions and uncertain boundaries, using line patterns rather than red-green status colors.

Use these anchors in their corresponding spatial blocks: extra predicted contour outside an unchanged reference boundary; missing predicted contour next to a high-confidence token; slightly offset boundary pair with a measuring bracket; two competing outline annotations.

Render the locked Chinese labels exactly as supplied: “背景误报”; “候选类型”; “高置信漏检”; “覆盖盲区”; “配准差异”; “待核验”; “标签边界”; “概念示意”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 89mm single-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：示意图区分预测误差现象与配准/标注等候选解释。误差原因须由对应影像、标签及专业核验确定，高置信未变化区域同样进入复核候选。

限制：示例为概念示意，不伪装成真实已核验矿区；不把预测漏检全部归因于一致性约束。


### F14｜已完成预实验流程：固定子样本与九模型运行

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


### F15｜预实验结果：检测收益与召回代价

类型：Data Behavior；16:9；真实数据程序绘图；英文词数253。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic data-visualization specification for a programmatically rendered scientific figure. This figure explains the proposal question through 3 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Arrange three matched quantitative panels with the same arm order and distinct marker shapes. Use measured means and sample standard deviations across seeds, keeping each metric on a clearly labeled percentage axis. All three panels must be equally visible; do not enlarge only the favorable false-positive result. Include a compact note that small-change recall is unavailable and different from the overall recall panel.

Use these anchors in their corresponding spatial blocks: data-anchored point-and-error-bar plot panel; data-anchored point-and-error-bar plot panel; data-anchored point-and-error-bar plot panel.

Render the locked Chinese labels exactly as supplied: “变化 IoU”; “越高越好”; “背景误报率”; “越低越好”; “总体召回率”; “无一致性”; “全区域”; “背景位置”; “指标（%）”; “小变化召回 NA”; “预实验结果”; “0”; “10”; “20”; “30”; “40”; “50”; “60”; “70”; “80”; “90”; “100”.

Use the stored numerical payload to render coordinates, intervals and annotations with plotting software. An image model may provide only a non-evidential layout study. Never invent observations, smooth missing data, replace NA with zero, or add significance stars. Preserve adverse effects and confidence intervals crossing zero.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：三个种子的矿区宏平均为：无约束IoU/FPR/总体召回21.08/24.13/67.82%，全区域20.96/26.62/72.65%，背景21.72/23.28/68.55%。误差条为种子样本标准差，不是矿区泛化置信区间。

限制：必须用JSON数值通过绘图库生成，图像模型只能提供版式草案；小变化不可估计不能补零；不加显著性星号。


### F16｜预实验配对效应：矿区区间与不确定性

类型：Data Behavior / Forest Plot；16:9；真实数据程序绘图；英文词数269。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic data-visualization specification for a programmatically rendered scientific figure. This figure explains the proposal question through 4 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Create three coordinated forest panels sharing percentage-point units and a visible zero reference. Each panel contains both background-minus-full and background-minus-none rows, using exact paired-mine intervals from the stored results. Give interval widths enough horizontal room and make the zero line visually neutral. The recall decrease receives the same emphasis as the false-positive decrease. Do not interpret seed standard deviation as an interval.

Use these anchors in their corresponding spatial blocks: paired difference point with horizontal confidence whisker; paired difference point with horizontal confidence whisker; paired difference point with horizontal confidence whisker; two aligned comparison labels and a site-level resampling marker.

Render the locked Chinese labels exactly as supplied: “IoU 差”; “跨零”; “误报率差”; “保留跨零区间”; “总体召回差”; “方向不一”; “比较口径”; “背景减参照”; “背景减全区域”; “背景减无约束”; “差异（百分点）”; “95%矿区区间”; “零参考”; “预实验结果”; “−6”; “−4”; “−2”; “0”; “2”.

Use the stored numerical payload to render coordinates, intervals and annotations with plotting software. An image model may provide only a non-evidential layout study. Never invent observations, smooth missing data, replace NA with zero, or add significance stars. Preserve adverse effects and confidence intervals crossing zero.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：背景减全区域的IoU/FPR/总体召回差分别为+0.760/−3.348/−4.105个百分点，95%矿区配对区间为[−0.057,1.515]/[−4.217,−2.567]/[−6.236,−2.233]。先在矿区内平均种子，再对矿区重采样；结果为探索性。

限制：不能画全指标向好；同时保留背景减无约束区间；不能把总体召回称为小变化召回。


### F17｜小变化端点可估计性：从标签定义到NA

类型：Endpoint Availability；4:3；结构/设计示意；英文词数275。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Separate a conceptual eligibility demonstration from the actual pilot availability count. Show border-touching and interior components as outline examples without pretending they are sampled observations. Follow the pilot rule to an empty eligible tray labeled zero, then to an NA metric card, not a zero-height performance bar. A detached future-design card requests endpoint feasibility checking on original scenes before test rules are frozen.

Use these anchors in their corresponding spatial blocks: binary component outlines with one touching the frame boundary; area ruler and boundary-exclusion stencil; empty eligible-object tray with an explicit zero label; unavailable metric card without a bar or point; separate raw-scene annotation card.

Render the locked Chinese labels exactly as supplied: “标签连通域”; “8连通”; “端点筛选”; “片内／不接边”; “合格对象”; “0”; “不可估计”; “NA”; “正式定义”; “独立冻结”; “预定规则”; “分母为空”; “≤64像素”; “预定定义”; “NA不等于0”; “预实验端点”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 89mm single-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：预实验定义为片内、不接边且面积≤64像素的8连通标签区；480个验证切片中合格对象为0，小变化召回不可估计。正式方案另据开发期原始场景核验小变化定义，不能事后改本次阈值补数。

限制：示意连通域不是实际观察样本；不能由0合格对象推断完整数据集没有小变化。


### F18｜D_s扩展结果：可计算性、误差关联与变化占比混杂

类型：Data Behavior；4:3；真实数据程序绘图；英文词数276。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic data-visualization specification for a programmatically rendered scientific figure. This figure explains the proposal question through 4 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use a two-by-two diagnostic sheet with ten-site scatter plots rather than invented smooth trend curves. The availability panel distinguishes applicable pairs from six unavailable pairs. The lower group comparison labels low and high bins explicitly so their order cannot be reversed. State that the split uses the validation-site median for this exploratory extension, not the training threshold proposed for the formal study. Include the class-proportion association beside the error association.

Use these anchors in their corresponding spatial blocks: two exact availability counts in a proportion strip; ten site-level points on a scatter panel; ten site-level points on a scatter panel; paired mean markers with direct group labels.

Render the locked Chinese labels exactly as supplied: “可计算性”; “474／480”; “D_s 与误报”; “背景组”; “D_s 与占比”; “相关非因果”; “低档／高档”; “探索分档”; “D_s”; “背景误报率（%）”; “变化占比（%）”; “低档”; “高档”; “6对 NA”; “验证中位数”; “预实验结果”; “0”; “0.1”; “0.2”; “0.3”; “10”; “20”; “30”; “40”; “50”.

Use the stored numerical payload to render coordinates, intervals and annotations with plotting software. An image model may provide only a non-evidential layout study. Never invent observations, smooth missing data, replace NA with zero, or add significance stars. Preserve adverse effects and confidence intervals crossing zero.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：474/480对可计算D_s，6对NA；矿区范围0.0915—0.2196。背景组低/高档FPR为19.07/27.49%，变化占比为7.24/13.06%；D_s与变化占比Spearman约0.370、置换p约0.295，仅10矿区，均为探索证据。

限制：此处分档界点来自验证矿区；不伪装为正式训练界点；不将置换p说成已证实因果，实际点坐标只取已存JSON。


### F19｜固定矿区案例：两期影像、真值与三组预测

类型：Qualitative Comparison；4:3；真实资产排版；英文词数279。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Academic qualitative-comparison layout specification for lossless composition of existing scientific assets. This figure explains the proposal question through 3 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Specify a three-row, six-column image plate using only the already archived examples. Rows are the prespecified mines; columns are the two observations, label and three prediction arms. Preserve native pixel content and use equal-sized crops with synchronized framing. Add neutral outlines and column labels around the assets, never artificial restoration, recoloring or newly generated predictions. Existing full comparison artwork may be reused intact if original tile assets are unavailable.

Use these anchors in their corresponding spatial blocks: six source-preserved raster tiles from the fixed first case; six source-preserved raster tiles from the fixed second case; six source-preserved raster tiles from the fixed third case.

Render the locked Chinese labels exactly as supplied: “Brazil_01”; “row 2251”; “Chile_01”; “row 62”; “Congo_01”; “row 1304”; “时相A”; “时相B”; “变化标签”; “无一致性”; “全区域”; “背景位置”; “白色：变化”; “种子17”; “固定案例”.

Assemble the archived source pixels with a layout tool; do not generate, enhance or redraw mine scenes, labels or predictions. Every crop must use identical coordinates across columns. Preserve the fixed case selection and original attribution. If a source asset is missing, leave production pending rather than fabricate its contents.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 4:3.
```

图注保留：采用首次评分前确定的三个验证矿区案例和种子17。三组预测均保留，白色表示变化；图像与标签来自MineNetCD作者数据，CC BY 4.0，预测为本次运行生成。该案例集不代表总体误差发生率。

限制：必须复用真实影像、标签和预测，不调用图像模型重绘科学栅格；局部放大裁切必须各列同坐标；不删除不利案例。


### F20｜外部验证与语义边界：MineNetCD、EuroMineNet和铜矿边界

类型：Dataset Comparison；16:9；结构/设计示意；英文词数263。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Use three equal dataset columns above a shared compatibility check. Distinguish a two-time change task, annual footprint sequences and a static polygon resource through different monochrome anchors. Only compatible aligned tasks feed external validation; static copper boundaries feed case matching rather than change supervision. Do not overlay numerical performance on this conceptual matrix or invent site coordinates.

Use these anchors in their corresponding spatial blocks: paired optical frames beside a binary-change outline; annual footprint outline sequence; single polygon and attribute ledger; separate alignment rulers for bands, resolution and semantics; dotted case-evidence document.

Render the locked Chinese labels exactly as supplied: “MineNetCD”; “两期变化”; “EuroMineNet”; “年度足迹”; “铜矿边界”; “静态属性”; “输入与标签对齐”; “先核验”; “条件性扩展”; “主链完成后”; “案例匹配”; “任务对齐”; “条件性”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：MineNetCD提供主变化任务，EuroMineNet在波段、分辨率及标签对齐后开展内部验证或条件迁移，全球铜矿静态边界只用于可靠匹配的案例属性核对。

限制：不画光学—SAR融合或实时监测；静态边界不能替代变化真值；外部实验尚未完成。


### F21｜24个月任务进度与冻结节点

类型：Research Timeline；16:9；结构/设计示意；英文词数277。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic research diagram. This figure explains the proposal question through 5 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Create a task timeline with proportionate month intervals and small milestone markers, not a chain of equal-size boxes pretending to be durations. Place writing as a thin parallel track beginning during mechanism experiments. Mark first submission as conditional around month twelve, with a reassessment at month fifteen. External validation and real review appear as dotted optional tracks after the core chain closes. Do not draw publication as guaranteed.

Use these anchors in their corresponding spatial blocks: source ledger above a timeline interval; matched-mask pictogram above a timeline interval; fixed model outline above a milestone bracket; paired-interval pictogram above a timeline interval; manuscript revision ledger above a timeline interval.

Render the locked Chinese labels exactly as supplied: “数据与误差”; “1—3月”; “机制与对照”; “4—9月”; “冻结与原型”; “10—12月”; “[固定]”; “评估与扩展”; “13—15月”; “修改与发表”; “16—24月”; “暂定24个月”; “条件首投”; “重新核对”; “同步写作”; “可选扩展”; “研究设计”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：研究期限暂定24个月，自立项批复起计；依次完成数据核验、机制对照、检测器冻结与可靠性评价。首投与发表受结果成熟度和审稿周期影响，资源不足时先保障主链。

限制：没有实际批复起止日期，不写具体年月；不将投稿画成已经满足源刊发表要求。


### F22｜已运行轻量孪生网络：多尺度差分与训练损失

类型：Network Architecture；16:9；结构/设计示意；英文词数281。

本轮不执行制图。与同名JSON一并使用；下文含图内中文精确短标签，数值图交给程序绘图工具。

```text
Flat vector academic architecture diagram. This figure explains the proposal question through 6 grounded visual blocks, while keeping research design separate from measured pilot evidence.

Draw two image branches sharing exactly the same three encoder blocks. At each scale, absolute differences feed a two-stage decoder through nearest upsampling and concatenation, ending in a one-channel prediction. Place training losses below the encoder and output, clearly outside inference flow. Deepest-feature consistency is the arm-dependent path; segmentation supervision is shared. The drawing is explicitly the completed lightweight pilot network, not a newly claimed final architecture.

Use these anchors in their corresponding spatial blocks: two aligned image frames entering shared branches; three scale-specific feature-map outlines joined by a weight-sharing bracket; three pairwise absolute-difference junctions; two aligned decoder outlines with concatenation junctions; single-channel spatial probability grid; full-supervision grid plus deepest-feature mask.

Render the locked Chinese labels exactly as supplied: “两期 RGB”; “256×256×3”; “共享编码”; “16／32／64”; “[训练]”; “多尺度差分”; “逐尺度”; “上采样解码”; “32／16”; “变化概率”; “256×256”; “训练损失”; “三组配置”; “深层特征”; “分割监督”; “预实验网络”; “共享权重”; “256×256×16”; “128×128×32”; “64×64×64”; “已运行预实验”.

Keep conceptual examples explicitly schematic and show conditional research paths without implying completed results. Do not add unreported layers, dimensions, data sources or successes. Training labels must never enter inference or test-driven model selection. Long equations, unresolved thresholds, exact experimental parameters and source citations belong in the external caption, not in module boxes.

Use a pure white #FFFFFF canvas and white module fills with Nature Blue borders: #1B3A5C core, #2E6B9E supervision, #5BA0D0 input/output; #616161 for fixed states. Use #333333 text, #4D4D4D arrows and monochrome line-art anchors. Forward arrows are solid, feedback dashed and optional paths dotted. Keep clean grid alignment, balanced margins and shallow grouping. Use 1.5pt borders and 1.0pt dividers, without gradients, shadows or 3D. Use Noto Sans CJK SC with Arial fallback, titles 10–12pt, primary labels 8–9pt and dimension notes 6–7pt. Design at 183mm double-column width. NO emojis, NO lock/fire/lightning icons, NO 3D rendering. Aspect ratio 16:9.
```

图注保留：已运行网络含共享16/32/64通道编码、多尺度绝对差及32/16通道解码，总参数118,593。各Block为两次卷积/GroupNorm/ReLU；最深层一致性随三组改变，正式研究骨干尚未据此锁定。

限制：网络细节来源为现有代码的只读补充；不得添加Transformer、SAR分支、注意力模块或更深骨干；完整公式和每层尺寸放图注。


## 完整性与制作前检查

已分析当前21页PDF；完整交付22份JSON和22份提示词。每图均绑定物理页码、可见短文本、图注预留、视觉锚点和生产方式。未知正式参数保留于图注，不伪造结果。后续制作时检查字体、缩印、所有连线、图例和真实数据；本轮并未完成图像质量验收，因为尚未生图。
