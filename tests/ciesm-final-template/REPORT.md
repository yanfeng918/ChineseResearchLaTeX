# CIESM-STSR final 模板验收

日期：2026-09-07。项目：`projects/NSFC_2026_CIESM-STSR_final/`。本次交付可编辑的四页空白申请书，未填入真实申报内容。

## 实现与分层

- **项目层**：新增 LaTeX 主入口、元信息、摘要、六份正文填写文件、预算表、项目说明、薄 wrapper，以及与目录同名的 VS Code 工作区。元数据显式声明 `build_profile=thesis` 和 `template=ciesm-open-fund`。
- **公共包层**：复用现有 `packages/bensz-thesis` 中的 `ciesm-open-fund` profile/style，以及 `bensz-fonts` 字体。新官方 PDF 的 SHA-256 与上一轮基线完全一致，因此无须新增或复制样式。profile、style、官方构建器在本轮前后的 SHA-256 均一致；包内仅更新 README 中的现行项目链接。
- **配置与文档层**：使用当前同步器已有的“显式 `build_profile` 优先于目录名前缀”规则，生成 thesis 构建配置。本轮没有修改同步器实现；根级 README、projects 导览、AGENTS 和包 README 的旧入口链接改为新路径。根级 CLAUDE.md 自动引用 AGENTS.md。

虽然目录名包含 `NSFC_`，实际文档仍为实验室开放基金申请书；构建采用 `thesis_project_tool.py`。未改写邻近项目 `NSFC_2026_CIESM-STSR` 的已有研究稿。

## 验证结果

| 检查 | 结果 |
|---|---|
| 官方 build | 通过，4 页，595.3 × 841.9 bp |
| `texlua → 项目 wrapper → 官方工具` | 通过；PDF 位于项目根，缓存与 SyncTeX 位于 `.latex-cache/` |
| 最终编译日志 | 无错误、warning、缺字、Overfull 或 Underfull |
| VS Code 同步 `--check` | 三个受管文件全部一致，使用 `scripts/thesis_build.py` |
| 填写与自动续页 | 通过，9 页，24 段测试正文完整，页脚总页数正确 |
| 金额、英文、斜杠与预算换行 | 通过；超长字段触发构建失败，不静默裁剪 |
| 配置与现有构建脚本测试 | 12 项通过，包含显式声明覆盖 NSFC 前缀及旧项目回退规则 |
| 官方 PDF 字符核对 | 逐页忽略空白后的字符多重集完全一致 |
| 原生可编辑输出 | 4 页均无图片对象；填写测试在不复制官方 PDF 的条件下构建成功 |
| 与上一轮已验收模板比较 | 144 dpi 灰度图逐页完全一致 |

官方 `compare` 已执行，四页尺寸一致，报告为 `identical=false`，返回码 1 表示存在像素差异。与 WPS 官方 PDF 的不同灰度像素分别占整页 **0.989%、0.701%、0.627%、0.597%**；残余差异为字距、描边、框线及出生日期空白字段位置等，与上一轮已验收版保持一致。该百分比是全页像素差异统计，不是模板匹配率。四页输出已逐页目视检查。

原始基线 SHA-256：`f9170bb2d850fcbe987529398ea131ad6994fb987a20898037fb11956720d013`。结构化结果见 [verification.json](verification.json)。

本轮未修改公共包运行时代码，因此不触发全部学校模板重新编译；以运行时文件哈希不变、目标项目实际构建和与既有验收输出逐像素一致确认复用行为。包层回归计划工具的只读结果保存于本地 `reference-regression-plan.json`，其中按目录前缀匹配的学校项目列表为空，不代表本轮验证了不存在的学校示例。

## 复核方式

在 `tests/ciesm-final-template/` 下执行，测试文件和产物均隔离于 `tests/`：

```bash
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir ../../projects/NSFC_2026_CIESM-STSR_final
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py compare --project-dir ../../projects/NSFC_2026_CIESM-STSR_final --baseline-pdf ../../projects/NSFC_2026_CIESM-STSR_final/地球系统数值模拟教育部重点实验室开放基金.pdf --output-dir compare --keep-rasters
python3 verify_editability.py
python3 ../../scripts/sync_vscode_configs.py --check --project NSFC_2026_CIESM-STSR_final
```

填写回归复用 `tests/diqiushuzhi-template/verify_editability.py`，输入和所有新输出都指向本轮目录。pytest 使用上一轮隔离安装的 `pypdf` 依赖：

```bash
PYTHONPATH=../diqiushuzhi-template/_artifacts/python-deps python3 -m pytest -q ../diqiushuzhi-template/test_vscode_profile.py ../../scripts/test_sync_vscode_configs.py ../../scripts/test_thesis_project_tool.py --basetemp=_artifacts/pytest -o cache_dir=_artifacts/pytest-cache
```

## 填写限制

摘要不超过 400 字，第一部分不超过 3000 字，关键词最多五个，预算总额需与各科目核对。上述语义约束由填写者确认；固定字段或单页预算表超过可用空间时模板会报错。正文可自动跨页，填写后不再限定四页。详细编辑位置见[项目 README](../../projects/NSFC_2026_CIESM-STSR_final/README.md)。
