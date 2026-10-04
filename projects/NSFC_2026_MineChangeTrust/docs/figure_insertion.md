# 正文插图记录

已插入选定的7张图，正文编译为25页。前6张为用户提供PNG的无损PDF封装，第7张依据已归档JSON重绘为矢量统计图。原始7张PNG均保留，校验值未改变。

| 图号 | 规划ID | 正文页 | 引用文件 |
|---|---|---|---|
| 1 | F01 | 2 | [F01_research_background.pdf](../figures/F01_research_background.pdf) |
| 2 | F02 | 8 | [F02_overall_framework.pdf](../figures/F02_overall_framework.pdf) |
| 3 | F03 | 11 | [F03_route_diagnosis.pdf](../figures/F03_route_diagnosis.pdf) |
| 4 | F04 | 14 | [F04_route_constraint.pdf](../figures/F04_route_constraint.pdf) |
| 5 | F05 | 15 | [F05_route_reliability.pdf](../figures/F05_route_reliability.pdf) |
| 6 | F14 | 19 | [F14_pilot_workflow.pdf](../figures/F14_pilot_workflow.pdf) |
| 7 | F15_F16 | 20 | [F15_F16_pilot_results.pdf](../figures/F15_F16_pilot_results.pdf) |

图片自带的标题区只在LaTeX排版时以顶部12mm裁切隐藏，原PDF保留完整图片。正文使用自动编号、图注及交叉引用；未改动公共包和项目版式配置。

第7张原PNG中的多项测量与归档不一致，因此未将其作为统计结果插入。例如三组IoU应为21.08%、20.96%、21.72%；相对无约束的三项配对区间均跨零。插入版本从aggregate_metrics.json与paired_site_contrasts.json读取坐标，并用seed_macro_metrics.json核对均值与种子标准差，未重跑训练。图6矿区卡片数字在图注中明确为汇总方式示意。

上排误差条为种子样本标准差，下排为先按矿区平均种子、再按矿区配对重采样的95%区间；小变化召回保持NA。

可复现入口：

```bash
python3 projects/NSFC_2026_MineChangeTrust/scripts/prepare_figures.py
python3 packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir projects/NSFC_2026_MineChangeTrust
```

准备脚本使用PyMuPDF、Matplotlib、NumPy及本机Noto Sans CJK或思源黑体；六张示意PDF保留原始栅格，统计图保存矢量内容。完整来源、哈希和实际坐标见[inserted_figures.json](../figures/inserted_figures.json)。

验证：7个插图路径有效，图号1—7和引用已解析；6张无损封装逐像素校验；9个均值/标准差及6项配对区间核对通过；7个插图页已目视检查。没有新增编译警告，已有字体替代、包名/recorder及参考文献Underfull警告与插图前一致。
