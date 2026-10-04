# diQiuShuzhi 模板交付验收

验收日期：2026-09-06。目标为 `projects/diQiuShuzhi/`，基线为用户提供的 `地球系统数值模拟教育部重点实验室开放基金.pdf`。

## 结果

默认生成可编辑的四页空白申请书，官方 PDF 不参与编译。最终 XeLaTeX 日志无错误、缺字、Overfull、Underfull 或 warning。正文可正常续页，页脚总页数动态更新；固定填写框溢出时明确报错。已检查四页空白输出及填写测试的封面、信息表、预算表图像。

| 验证 | 结果 |
|---|---|
| 官方 `thesis_project_tool.py build` | 通过，4 页，595.3 × 841.9 bp |
| 项目 VS Code `texlua → thesis_build.py → 官方工具` | 通过，产出 `main.pdf` 与缓存内 SyncTeX |
| 官方 `compare`，144 dpi | 4 页尺寸一致，存在细微像素差异，非逐像素相等 |
| 逐页去除空白后的字符多重集 | 与官方 PDF 完全一致；信息表填写区的文本提取顺序不同，不影响版面 |
| 输出图片对象 | 0；文字和框线均为原生 LaTeX 重建 |
| 填写与续页测试 | 通过，9 页；24 段正文完整，金额、英文/数字、斜杠和总页码正确，预算长说明增高行高 |
| 超长填写字段 | 官方构建返回失败，未产生正式 `main.pdf`，没有静默裁剪 |
| VS Code 配置回归与现有构建器测试 | 11 项通过 |
| 公共包文件结构校验 | `validate_package.py --skip-compile` 通过 |

## 修改层级与原因

公共包层新增 `ciesm-open-fund` 专属 profile/style，并登记结构校验清单。字体直接使用 `bensz-fonts` 既有资源。现有学校 profile 没有开放基金表单能力；若把封面、信息表、预算表和页脚实现全部放在项目中，会使项目承担稳定样式实现，因此通过本包已有的 profile/style 扩展点接入。未修改既有 13 套学校模板的样式、profile 和公共 `.sty` 核心；修改前保存的 32 份原样式、profile、核心及配套文件的 SHA-256 全部保持一致。

项目层新增 `main.tex`、元信息、摘要、六份正文、预算填写入口、只读官方 PDF 引用、说明与薄 wrapper。`template.json` 使用 `document_type=open-fund-application` 和 `build_profile=thesis`，没有把基金申请书登记成学位论文。默认不填入个人信息或虚构科研内容。

仓库脚本层为 `sync_vscode_configs.py` 增加元数据类型解析。无标准目录前缀时可以声明已有 `build_profile`，仍优先沿用旧目录前缀，错误的元数据明确报错；这样新目录可持续同步标准 VS Code 配置。README、项目指令与 CHANGELOG 同步说明该入口；根级 CLAUDE.md 通过 `@./AGENTS.md` 引用核心指令，无需复制修改。

## 视觉差异

数据见 [visual-metrics.json](visual-metrics.json)。两份 PDF 由官方 compare 以 144 dpi 光栅化，灰度小于 200 的像素计为墨迹；“1 bp 内覆盖”指另一份图在 2 像素邻域内存在墨迹，不是像素相等率。

| 页 | 不同灰度像素占整页 | 官方墨迹在 1 bp 内被输出覆盖 | 输出墨迹在 1 bp 内被官方覆盖 |
|---|---:|---:|---:|
| 封面 | 0.989% | 100.000% | 100.000% |
| 信息表 | 0.701% | 99.231% | 99.158% |
| 报告正文 | 0.627% | 99.929% | 99.929% |
| 预算表 | 0.597% | 98.375% | 100.000% |

残余差异包括 WPS 与 XeLaTeX 的字距、字体描边和抗锯齿，出生日期空白字段的位置，以及部分框线交点和线宽的细微差异。页面数量、主要位置、提纲换行、表格尺寸、灰色预算背景与页脚已按官方 PDF 对齐。官方 compare 如实报告 `identical=false`，不将白色背景占比误称为模板匹配率。

## 公共包回归范围

修改包层前运行技能的 `plan_package_regression.py`，原始结果保存在 [regression-plan.json](regression-plan.json)。当前工作区没有任何 `projects/thesis-*`，初始扫描也没有现存 `bensz-thesis` 使用者；不能把 README 中已不存在的学校示例说成已完成编译回归。

实施期间其他会话新增了 `Huazhong_template`、其专属 profile，并修改公共构建器（`-recorder` 与最后一趟退出码检查）。本任务保留这些修改，复核后对当前真实同包使用者补做回归：

- `diQiuShuzhi`：本项目官方 build、官方基线 compare、9 页填写与溢出测试。
- `Huazhong_template`：在本测试目录复制其完整源码快照，用官方入口构建通过，7 页，无 warning；与复制时保存的该项目 `main.pdf` 进行官方 144 dpi compare，逐像素一致（`identical=true`）。未修改它的正文、样式或正式产物。
- 所有原有学校 profile/style 和公共核心：文件哈希保持一致。缺少的学校示例未重建，也未宣称已编译。

## 复核命令

以下命令均在 `tests/diqiushuzhi-template/` 下执行，测试产物保存在此目录或 `_artifacts/`，不在仓库根目录运行测试。

```bash
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir ../../projects/diQiuShuzhi
python3 ../../packages/bensz-thesis/scripts/thesis_project_tool.py compare --project-dir ../../projects/diQiuShuzhi --baseline-pdf ../../projects/diQiuShuzhi/地球系统数值模拟教育部重点实验室开放基金.pdf --output-dir compare --keep-rasters
python3 verify_editability.py
python3 ../../scripts/sync_vscode_configs.py --check --project diQiuShuzhi --project Huazhong_template
python3 ../../packages/bensz-thesis/scripts/validate_package.py --skip-compile
python3 -m pytest -q test_vscode_profile.py ../../scripts/test_sync_vscode_configs.py ../../scripts/test_thesis_project_tool.py --basetemp=_artifacts/pytest -o cache_dir=_artifacts/pytest-cache
```

现有构建器测试依赖 `pypdf`；本环境缺少该依赖，安装到本测试目录的 `_artifacts/python-deps/` 后以 `PYTHONPATH=_artifacts/python-deps` 执行 pytest，未修改系统 Python 环境。填写测试另需 PyMuPDF。

## 使用限制

本次交付模板源码与 PDF，不包含真实申请材料。封面与信息表保留官方单页固定框，过长字段需精简；预算备注可自动换行，但整表须留在一页内。摘要 400 字、第一部分 3000 字、关键词最多五个及预算加总由填写者检查。独立项目使用须安装包含此新 profile 的公共包源码版本；未制作或发布 Release/Overleaf 压缩包。
