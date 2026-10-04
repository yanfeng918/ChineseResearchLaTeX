# XJ-PVCast 全套学术图配色决策

适用范围：研究背景、总体研究框架及三个研究内容技术路线，共五张核心图。以中文申请书最终约155 mm宽的插图为验收对象；本文件固定跨图视觉角色，不替代逐图内容规范。日期：2026-09-19。

## 决策与依据

- 风格家族：**classic academic**，白底、白填充、彩色边框、平面矢量结构。
- 主配色：**Nature Blue**。决策分支为`scene`：总体与路线图均有不少于四个主要模块，优先同色系，减少颜色分类负担。
- 备选：**Print-Safe Gray**，仅在整套改为纯黑白印刷时整体切换，不逐图混用。
- 场景：气象与光伏预测的小额科研基金申请书，并非特定会议海报。默认兼顾色觉差异及灰度打印。
- 参考图：未指定；根据当前正文及经典学术流程图要求建立规则。
- 主要约束：最多三种有彩色加中性色；本套实际只启用两种蓝色，所有模块白填充，白色面积不低于70%，建议不低于85%。

色值来自 Academic Figure Color Expert 的 Nature Blue 与 Print-Safe Gray 预设；字体与几何尺寸依本项目中文印刷宽度调整。

## 色值与语义绑定

| 配色字段 | 色值 | 本套用途 |
|---|---|---|
| primary | `#1B3A5C` | 核心模型、方法操作的边框 |
| secondary | `#2E6B9E` | 数据输入及预测输出的边框 |
| tertiary | `#5BA0D0` | 预设备用，本套默认不启用；不作小字或关键边界 |
| text | `#333333` | 全部中文、数字、数学标签 |
| fill / canvas | `#FFFFFF` | 画布与所有模块填充 |
| section_bg | `#F7F7F7` | 可选的大区分组底色；禁止叠加有彩色底块 |
| border | `#CCCCCC` | 无语义的辅助分隔线，不承载类别识别 |
| arrow / anchor | `#4D4D4D` | 箭头、几何锚点、示意曲线 |
| neutral_status | `#616161` | 校验、监督、状态标记 |

| 功能角色 | 固定颜色 | 第二识别通道 |
|---|---|---|
| Data / Input：观测、功率、历史误差 | `#2E6B9E` | 直角矩形，左上小型空心表格 |
| Backbone / Core：尺度处理、分位模型、秩重排 | `#1B3A5C` | 小圆角矩形，三条水平线或简化层叠矩形 |
| Loss / Supervision / Feedback：评分、覆盖诊断、到达标签反馈 | `#616161` | 独立诊断区域，小刻度线或端点区间锚点；反馈箭头虚线 |
| Output / Prediction：分位网格、区间、事件概率、告警记录 | `#2E6B9E` | 矩形加一条内侧底线，并写明输出名称 |
| Frozen / Fixed：确有正文依据的固定状态 | `#616161` | 状态文字及虚线外框；本项目未声明冻结网络，不添加冻结模型 |

输入与输出共享中蓝，以位置、标签和输出内侧底线区分；颜色不随F01—F05或C1—C3换义。图中不需要的角色直接省略。数据“拟获取”、参数“待确认”与模型“冻结”不同，前两者必须用明确中文表达，不借颜色暗示已经落实。

## 155 mm中文排版与线条

所有字号均指插入正文后、宽155 mm时的实际字号，不能按大画布字号缩小后交付。

| 元素 | 规范 |
|---|---|
| 中文字体 | 思源黑体 / Noto Sans CJK SC，英文可用Arial；中文标点与字形完整 |
| 分区标题 | 11–12 pt，半粗体 |
| 主要标签 | 9.5–10.5 pt，常规或半粗体 |
| 次要标签 | 8.5–9 pt；不足空间先删次要文字，不再缩小 |
| 模块标题 | 通常4–8个汉字；每框最多两行正文，每行宜不超过10–12个汉字 |
| 容器 / 主箭头 | 1.5 pt；箭头头部约1.2 mm；连线不穿文字 |
| 内部分隔 / 几何锚点 | 1.0 pt；锚点约4–6 mm，可由原生线、矩形、圆组成 |
| 次要反馈箭头 | 1.0 pt虚线；主流程实线；旁路的含义须有文字 |
| 圆角与留白 | 圆角约1–1.5 mm；模块内边距至少2 mm，图外安全边距至少3 mm |

整图题名与长公式放在LaTeX图题/图注中。图片内保留短分区名，避免同时重复大标题、图号和图注。纯白模块不得使用渐变、阴影、立体效果或彩色文字。

## 五图共享的视觉锚点

| 图别 | 建议锚点 | 避免的表达 |
|---|---|---|
| F01 研究背景 | 短折线、两端点、区间括号 | 真实地图、天气照片、虚构性能曲线 |
| F02 总体框架 | 三个水平条组、分支连线、输出底线 | 把区间诊断支路串成事件分布校准保证 |
| F03 内容一路线 | 可用时间轴、小表格、两级尺度折线 | 用太阳/云/沙尘复杂插画代替数据来源 |
| F04 内容二路线 | 分位数短线、时间窗口、区间端点 | 无依据的神经网络层数、已保证的覆盖率 |
| F05 内容三路线 | 同列样本表、行配对连线、简短比较标签 | 预设“本方法最佳”的色块、得分或胜负标记 |

每个主要模块至少有一个小锚点，统一深灰细线。优先使用PPT原生矩形、直线、折线、空心圆、端点括号；不需要复杂语义图标、照片或必须再次生成才能复原的素材。示意样本与折线只解释结构，注明“结构示意”或“非实测”。

## 可访问性与灰度要求

按标准相对亮度计算：`#333333`对白对比度12.63:1，对`#F7F7F7`为11.79:1；深蓝对白11.63:1，中蓝对白5.66:1，深灰箭头8.45:1。小字统一深灰，满足至少4.5:1。备用浅蓝对白仅2.84:1，因此不承担关键边框、曲线或文字；`#CCCCCC`也只作冗余分隔。

同边际三组比较使用相同框大小、边框色和线宽，靠完整短标签及配对结构区分，不把某组预先标为胜者。灰度打印后仍应能靠文字、几何和箭头方向理解全部关系。以上为配色与对比度检查；最终成图仍须在155 mm尺寸检查中文、灰度与线条，不将本规范视为实际成图验收记录。

## 可复制交接块

```yaml
style_family: classic_academic
decision_branch: scene
palette: Nature Blue
alternate: Print-Safe Gray
primary: '#1B3A5C'
secondary: '#2E6B9E'
tertiary: '#5BA0D0' # reserved; inactive in the five-figure set
active_chromatic_colors: ['#1B3A5C', '#2E6B9E']
text: '#333333'
fill: '#FFFFFF'
canvas: '#FFFFFF'
section_bg: '#F7F7F7'
border: '#CCCCCC' # nonessential separators only
arrow: '#4D4D4D'
anchor: '#4D4D4D'
neutral_status: '#616161'
final_width_mm: 155
font_family: Noto Sans CJK SC, Source Han Sans SC, Arial
font_pt: {title: 11.5, primary: 10, secondary: 9}
stroke_pt: {container: 1.5, divider: 1, forward: 1.5, feedback: 1}
accessibility: colorblind-conscious; mandatory text-and-shape dual encoding
visual_anchors: native rectangles, tables, polylines, open circles, endpoint brackets
reason: multi-module Chinese scientific diagrams, readable in print and reproducible as editable PPT
```

若采用黑白备选，整套同时映射：核心`#000000`，输入/输出`#333333`，监督/固定`#666666`，文字`#333333`，箭头`#4D4D4D`；几何与文字语义保持不变。

规范来源：[Color Expert](</home/yanfeng/.agents/skills/academic-figure-color-expert/SKILL.md>)、[配色预设](</home/yanfeng/.agents/skills/academic-figure-color-expert/references/palettes.md>)、[Academic Figure Prompt](</home/yanfeng/.agents/skills/academic-figure-prompt/SKILL.md>)、[根绘图要求](../../../绘图提示词.md)。
