# NSFC 图文流程验证

所有命令在本目录运行；临时项目、虚拟环境、PDF、PPT 和预览留在本目录并由 Git 忽略。

确定性回归：

```bash
python3 -B -m unittest discover -s . -p 'test_pipeline.py' -v
```

需要 PyYAML、Pillow、PyMuPDF。覆盖只读迁移、事实缺口、递归活动正文、路径越界、串行一图一调用、重试、单图失效、幂等插入、标签冲突及最终构建失效。

真实转换/构建集成额外需要 python-pptx、LibreOffice 和仓库官方 NSFC 构建环境：

```bash
python3 -m venv --system-site-packages .venv
.venv/bin/python -m pip install python-pptx
.venv/bin/python -B smoke_integration.py
```

此测试使用合成 PNG 和原生对象 PPT，实际执行 LibreOffice 导出、逐页拆分、正文插入及官方 XeLaTeX 构建，并检查更换图件后的就绪度失效；产物在 `_artifacts/`。图像/检查报告中的成功字段是测试夹具，不代表真实 imagegen 调用或 editppt 重建通过。真实模型生成和转换技能的页级质量应在运行具体标书任务时另行验收。

2026-09-06 验证结果：15 项回归通过；五图 PPT 导出及官方构建通过，文字夹具 1 页、插图后 2 页，零编译错误，无新增 LaTeX warning。基线已有未使用 figure caption 设置、包声明名称和缺少 recorder 文件警告；插图后前者消失，其余两项仍为已有警告。已查看两页最终预览，中文和图件均显示。技能结构校验与 52 个双宿主入口一致性检查通过。
