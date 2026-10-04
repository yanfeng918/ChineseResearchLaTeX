# Palette Decision：视觉逻辑与配色

**当前应用范围：** 用户选定F01—F05、F14及F15＋F16合并图，共7张。配色沿用本决策；合并图上排编码三组身份，下排编码两项配对比较，各设图例，避免把不同统计对象混为同一颜色含义。

本决策依据[Figure Plan](Figure_Plan.md)，交给Academic Figure Prompt使用。主选 **classic academic + Nature Blue**；备选 **Blue Monochrome**。分支为scene：总体框架5模块，路线图普遍4模块以上，适合用蓝色明度和形状组织信息。Nature Blue只是配色预设名称，不表示目标期刊为Nature。无用户指定颜色、无风格参考图；按中文科研申请、色觉友好和黑白打印考虑。

## 决策清单

| 项目 | 本次决定 |
|---|---|
| style family | classic，白底、彩色描边、平面矢量；使用Academic Figure Prompt |
| 触发约束 | 多模块框架≥4；默认色觉友好；未来需缩印和黑白阅读 |
| 图型 | 背景/框架/路线/模块统一蓝色；结果图另用三组身份+点形，不用颜色暗示成功 |
| venue/domain | venue=None；实验室开放课题；遥感变化检测与可靠性 |
| 主选 | Nature Blue，来自Color Expert的references/palettes.md |
| 备选 | Blue Monochrome：#1565C0 / #42A5F5 / #90CAF9；整套切换，不混入当前图 |
| 生效分支 | scene；不是用户已确认的审美偏好 |

## 精确颜色与跨图语义

| 角色 | HEX | 图形与解释 |
|---|---|---|
| Primary | #1B3A5C | 核心方法、骨干和主要研究步骤的边框 |
| Secondary | #2E6B9E | 损失、监督、对照和反馈连接 |
| Tertiary | #5BA0D0 | 输入与输出边框；靠形状和标签区分方向 |
| Data/Input | #5BA0D0 | 成对影像框、数据页、矿区标记；标签在左或上 |
| Backbone/Core | #1B3A5C | 特征栈/处理模块；训练权重为实线框并标“[训练]” |
| Loss/Supervision | #2E6B9E | 距离聚合、监督网格；反馈线为虚线 |
| Output/Prediction | #5BA0D0 | 结果掩码、证据文档或曲线轴；输出形状与输入不同 |
| Frozen | #616161 | 灰色虚线框并写“[固定]”；不使用锁头/火焰图标 |
| 正文标签 | #333333 | 所有主要文字用深灰，不能用浅蓝小字 |
| 画布/模块填充 | #FFFFFF | 白色；不以整块彩色填充区分模块 |
| 分组底/中性边框 | #F7F7F7 / #CCCCCC | 分组优先白底细框；浅灰只作中性辅助 |
| 主流程箭头 | #4D4D4D | 实线前向；虚线反馈；点线条件扩展 |

角色映射允许同一色相重复：五种功能不需要五种彩色。Data与Output共享浅蓝，但分别使用输入影像栈和输出掩码/文档；Loss与Backbone通过形状、标签和连线区分。固定状态由灰色、虚线和文字共同编码，不能把所有虚线箭头误认为固定参数。

结果图单独固定实验组身份：无一致性=#616161+方形；全区域=#2E6B9E+圆形；背景位置=#1B3A5C+三角形。三组同等面积、同等线宽；背景组是研究对象，不因此显示为胜者。指标方向由“越高/越低越好”文字明确，下降箭头不等同于改进。图例显式说明当前颜色编码的是实验组，而不是模块角色。

## 视觉逻辑

- F01：双分支概念对照，几何边界变化与外观纹理差异分开，不用真实地图伪造矿区分布。
- F02：五模块研究依赖，居中的三项研究与F03—F05同名；不展开网络层数。
- F03—F05：各自一条可执行研究路线，显示上游输入、输出、核验和下一环节；测试结果无回流训练箭头。
- F06—F12：协议、机制和评价细节，靠分组与连接表达主辅关系；正式未完成的工作标“研究设计”。
- F14—F18/F22：已运行预实验与尚缺证据分开；数值图保留召回损失、跨零区间和NA。
- F19：真实遥感影像与预测保持原像素，不受单色画风约束；彩色只限定新增边框和标记，不洗色，不重绘真实内容。
- F20—F21：条件性外部验证及进度用点线框/“条件性”标记，不装成已经部署或必然发表。

## 可读性与印刷

新绘示意图以白色留白为主（目标≥70%），最多三种蓝色描边加中性色，无渐变/3D/投影。真实科学栅格和定量数据层以保真为先，不为满足留白比例删除像素或数据。深灰文字对白底对比度为12.63:1，高于4.5:1；浅蓝只用作边框，不能承担小字。

优先采用183mm设计画布；F13/F17可用89mm单栏。标题10—12pt，主标签8—9pt，次标签7—8pt，张量/维度6—7pt；容器线1.5pt，分隔线1.0pt。放入当前A4模板时按实际正文宽度重新排布，不能简单整体缩小到字迹不可读。蓝色色阶也不能单独保证类别区分，必须保留形状、线型、中文标签；正式成图后还需实际检查缩印和灰度效果。

## 提示词交接

```json
{
  "style_family": "classic",
  "branch": "scene",
  "venue": null,
  "venue_context": "2026年度实验室开放课题正文",
  "domain": "remote-sensing change detection / mine generalization / reliability assessment",
  "module_count_framework": 5,
  "recommended": "Nature Blue",
  "alternate": "Blue Monochrome",
  "colors": {
    "primary": "#1B3A5C",
    "secondary": "#2E6B9E",
    "tertiary": "#5BA0D0",
    "text": "#333333",
    "fill": "#FFFFFF",
    "section_bg": "#F7F7F7",
    "border": "#CCCCCC",
    "arrow": "#4D4D4D",
    "frozen": "#616161"
  },
  "semantic_binding": {
    "Data": "#5BA0D0",
    "Backbone": "#1B3A5C",
    "Loss": "#2E6B9E",
    "Output": "#5BA0D0",
    "Frozen": "#616161"
  },
  "series_binding": {
    "none": {
      "color": "#616161",
      "marker": "square",
      "exact_label": "无一致性"
    },
    "full": {
      "color": "#2E6B9E",
      "marker": "circle",
      "exact_label": "全区域"
    },
    "background": {
      "color": "#1B3A5C",
      "marker": "triangle",
      "exact_label": "背景位置"
    }
  },
  "text_contrast_on_white": 12.635,
  "generated_images": false
}
```

完整性：已分析21页PDF与22图计划；当前为完整视觉规范，未生成图像；参数以事实来源和具体图注为准。后续可补官方版心尺寸或用户偏好的参考图，但当前采用上述默认方案继续交付全部提示词。
