# PACT-Agent Figure Palette

决策分支：scene。风格classic，由Academic Figure Color Expert确定，再交Academic Figure Prompt。四模块总体框架触发单色分级规则；基金正文重视中文印刷与灰度可读性，默认兼顾色觉差异。参考图：无；用户未指定hex。

主方案Nature Blue；备选Blue Monochrome（#1565C0 / #42A5F5 / #90CAF9），本次不混用备选。

|角色|色值|双重编码|
|---|---|---|
|输入/数据|#5BA0D0|标题与独立入口框|
|可训练/计算/核心模块|#2E6B9E|实线框、内部结构分隔|
|输出/评价目标|#1B3A5C|较深边框、明确输出标题|
|冻结主干/策略/辅助|#CCCCCC|虚线框与“冻结”文字|
|监督/反馈|#4D4D4D|虚线反馈箭头，主数据流实线|
|文字|#333333|高对比中文无衬线|
|所有填充与画布|#FFFFFF|不使用有色面板、渐变或阴影|

只启用3个蓝色色阶，加中性灰。预设的#8EAEC4在本次不使用，避免增加色阶。冻结与可训练、反馈与前向均有线型和文字区别，灰度下不依赖颜色识别。

Handoff：family=classic；palette=Nature Blue；module_count_framework=4；canvas_width=183mm；font=Noto Sans CJK SC/Arial；heading=11pt、label=9pt、secondary≥8pt；border=1.5pt、divider=1pt；white fill, colored borders only；no 3D/shadow/emoji；每主要块用原生几何分隔或短线作为视觉锚点。正文最终按全宽缩放，实际PDF检查可读性。
