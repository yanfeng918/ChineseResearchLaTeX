# 申请书插图的矢量重绘

本次按申请人2026年9月23日“使用 nsfc-illustrated-pipeline 中的 skill 把图像改写矢量图”的要求，复用其中的可编辑PPT重建、PDF导出、正文插入和联合检查流程。范围为现有插图转换，不重跑选题、正文写作或图像生成。

## 原始图件与处理范围

| 正文图号 | 文件标识 | 原始构成 | 本次处理 |
|---|---|---|---|
| 1 | F01_research_background | 单幅位图封装的PDF | 原生文字、边界及流程结构 |
| 2 | F02_overall_framework | 单幅位图封装的PDF | 原生文字、模块及连接线 |
| 3 | F03_route_diagnosis | 单幅位图封装的PDF | 原生流程、判断和诊断回路 |
| 4 | F04_route_constraint | 单幅位图封装的PDF | 四组对照、开发选择与正式评价 |
| 5 | F05_route_reliability | 单幅位图封装的PDF | 校准、验证选择、排序与复核 |
| 6 | F14_pilot_workflow | 单幅位图封装的PDF | 真实预实验流程和汇总方式 |
| 7 | F15_F16_pilot_results | Matplotlib原生矢量PDF | 保留原始文件、数据及误差线 |

用户要求全矢量改写，故六张示意图采用可编辑文字与原生形状；原有装饰性纹理及图标整理为几何示意。该要求优先于转换技能默认以位图分离复杂图标的保真策略。图7基于实测数据，不能用生成图像重新猜测数值。

## 交付与复用

- `figures/NSFC-Figures-vector.pptx`：六页可编辑图件，顺序与上表前六项一致。
- `figures/vector/*.pdf`：正文引用的单图矢量PDF。
- `figures/vector/*.svg`：可移植矢量副本，字形转路径，编辑文字可使用PPT。
- `figures/vector/source/*.json`：逐页对象清单，坐标与可编辑内容来源。
- 原始六张PDF留在 `figures/`，可用于对照；现有图7继续原位引用。
- 完整重建工作区及真实CLI验收记录位于 `tests/minechange-vector-20260923/editppt/`，汇总见同级 `REPORT.md`。

修改PPT后，从仓库的测试子目录调用导出脚本，再按官方入口构建申请书：

```bash
python3 ../../projects/NSFC_2026_MineChangeTrust_final/scripts/export_vector_figures.py --work-dir ./export
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir ../../projects/NSFC_2026_MineChangeTrust_final
```

导出脚本检查PPT恰好六页，拒绝含位图的PDF页。单图画布保留原PDF尺寸，顶部留空以兼容现有12mm裁剪，不在图内重复放置正文图题。字体与边框采用统一层级，使用Noto Sans CJK SC及蓝灰配色。

## 科学内容约束

当前正文优先于早期绘图提示词。图2–5为拟开展的研究设计，不表示已完成实验或已取得性能增益；测试数据不反馈开发选择。图4区分开发期选定冻结与正式联合评价；图5的固定温度单向用于验证得分，验证不得反向重拟温度。图6保留三组、三个种子、12轮和0.5阈值等既有事实，以“9模型×10矿区＝90行记录”替代虚构具体计数。正文仅相应更新图注和图件路径。
