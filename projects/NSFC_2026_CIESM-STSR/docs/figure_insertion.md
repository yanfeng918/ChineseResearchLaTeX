# 正文插图映射

7 图由主技能 insert --apply 按唯一原文锚点写入受管块。仅修改活动正文 1.1、2.1；原文件备份保存在 docs/figure_source/backups。正文引图句、稳定标签、图题和 PDF 路径与清单一致，最终页数 24 页。最终复核修正了自动引图句的重复句号，未改变原文科学内容或图件。

|ID/图号|正文文件|标签|最终 PDF 页码|逐图 PDF|图题|
|---|---|---|---|---|---|
|F01/图1|extraTex/1.1.立项依据.tex|fig:background|2|figures/F01-background.pdf|复杂地形下的跨尺度重建问题。网格为结构示意，虚线表示增强场向选定大尺度状态的回聚合检查|
|F02/图2|extraTex/2.1.研究内容.tex|fig:framework|7|figures/F02-framework.pdf|四项研究内容及训练与应用关系。参考资料内开展配对训练，真实CIESM进入独立应用；方法反馈不使用测试集调参|
|F03/图3|extraTex/2.1.研究内容.tex|fig:data|10|figures/F03-data.pdf|数据构建与样本隔离路线。两类资料分别组织；训练、验证、测试是共同划分约定，不表示资料来源与集合的一一对应|
|F04/图4|extraTex/2.1.研究内容.tex|fig:reconstruction|11|figures/F04-reconstruction.pdf|多变量时空重建与等信息对照。共享表征连接四类专用输出，随机残差为条件性扩展，独立基线保持同信息和总预算|
|F05/图5|extraTex/2.1.研究内容.tex|fig:constraints|13|figures/F05-constraints.pdf|显式一致性与经验约束的作用区分。聚合、非负和变量定义条件逐项检查，数值一致性与独立样本收益分别评价|
|F06/图6|extraTex/2.1.研究内容.tex|fig:integration|15|figures/F06-integration.pdf|CIESM集成与应用证据路线。公开兼容性、实验室联调、实际应用与接收均按真实记录确认，图示为拟开展流程|
|F07/图7|extraTex/2.1.研究内容.tex|fig:evaluation|17|figures/F07-evaluation.pdf|公平消融与两类验证证据。矩阵表示四种拟比较配置；两类资料使用各自评价口径，结论同时检查非退化及不确定性|

唯一原文段落锚点详见 figure_manifest.json 的 anchor；完整页面渲染与实际编号解析见 tests/nsfc-ciesm-stsr-illustrated/final-page-renders 和 insertion-final-map.json。图号与页码均从本次 main.aux 解析，并在当前 main.pdf 中逐页目视核对。
