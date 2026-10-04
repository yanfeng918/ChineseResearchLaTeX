# 测绘实验室开放基金模板验收

验收日期：2026-09-07。目标：[NSFC_2027_Mapping_final](../../projects/NSFC_2027_Mapping_final/README.md)。参考为用户提供的《测绘科学与工程自然资源部重点实验室.pdf》，WPS 导出的 **2026 版**，共 10 页，第 4 页横向。

## 修改层级及理由

- **公共包**：在 `packages/bensz-thesis` 注册 `casm-open-fund-2026`，独立 style 管理字体、页眉页脚、横向页、填写接口、固定区域高度检查及流式正文；artwork 保存官方标签与矢量表格坐标。这是新增稳定模板能力，单在项目中实现会把样式实现下沉到正文层，因此按仓库标准落到公共包。未修改 thesis 核心装配、共享字体或官方构建逻辑。同步包清单、结构校验与说明。
- **项目**：新增主入口、`extraTex` 填写文件、开放课题元数据、Python wrapper、VS Code 工作区与 Lua launcher、使用说明。未迁移其它目录内已有标书正文，未虚构申请信息。
- **公共脚本**：`scripts/sync_vscode_configs.py` 优先读取显式 `build_profile`，未声明时仍按目录前缀推断，解决本项目 `NSFC_` 前缀错误选择 NSFC 构建器的问题。同步现有测试、脚本文档和项目指令。

所有源文字与表格为原生 LaTeX 文字/矢量线；构建不读取参考 PDF，也没有从 PDF 抽取字体并复制到项目。`bensz-fonts` 已有字体按共享 API 加载。

## 目标验证

| 验证 | 结果 |
|---|---|
| 官方 `thesis_project_tool.py build` | 成功，10 页，零错误、零 warning、零 overfull/underfull |
| 页面与文本 | 10 页尺寸均与参考一致；第 4 页横向；正文页码连续 1–8 |
| 文字完整性 | 逐页去空白后字符计数一致，未发现字符缺失或新增；保留原稿中的重复编号 |
| 实际填写 | 姓名、邮箱、中英课题名、首末成员行、合计与 15 项预算可写入并检索 |
| 长正文 | 添加 80 段测试正文后输出 20 页；正文终点仍在 PDF 中，多页重复章节框及页码，零 warning |
| 固定区域超长输入 | 官方构建非零退出，报告 `Fixed form cell overflow` |
| 非法成员行 | 第 11 行被拒绝，官方构建非零退出 |
| 无参考 PDF 的副本 | 填写副本与 launcher 副本均成功构建 |
| VS Code 实际入口 | `texlua → thesis_build.py → thesis_project_tool.py` 构建成功 |
| 同步配置与包结构 | 目标配置 `--check`、包 `--skip-compile` 均通过；配置推断 8 项 pytest 通过 |

复现：在本目录运行 `python3 verify_template.py`。测试正文、日志、栅格图、包快照均留在本目录的隔离子目录，不写入仓库根目录。

## 与官方 PDF 的版式比较

已执行官方 compare，144 DPI，参考与输出均为 10 页且尺寸一致。**`identical=false`，严格逐像素比较的退出码为 1；这不是完全像素一致的结果。**

逐页差异像素占页面面积约 0.79%–4.23%，仅用于定位差异，不能当成版式质量评分。完整指标见 [visual-metrics.json](visual-metrics.json)，原始比较报告在本地 `official-compare/compare-report.json`，逐页差异图在 `official-compare/diff/`。

已目视检查封面、填报说明、基本信息、横向成员表、预算、研究正文、承诺与意见页。主要残余差异：共享包的 Adobe 黑体/仿宋与 WPS 的 SimHei/FangSong 字形不同；字号舍入和抗锯齿不同；正文提示及承诺中的英文按 LaTeX 段落重新断行，承诺英文比原稿多占一行，但未挤压签字区。表格外框、横向页与章节分页保持参考结构。

原稿的“二〇二六年制”、2026 年度条款、2026-11-01 至 2027-10-31 研究期限均保留；成员表第 9 行原编号为“8”，最后两章均为“七”，未擅自修正。目标目录名中的 2027 不代表采用未提供的 2027 版官方模板。

## 同包回归

修改公共包前已运行技能要求的回归规划脚本，计划见 [regression-plan.json](regression-plan.json)。脚本的 `thesis-*` 前缀规则没有命中现存项目，已按真实加载 `bensz-thesis` 的项目补齐范围。

共享工作区内其它模板也在发生修改，个别磁盘 PDF 一度滞后于源码，因此最终回归使用同一源码快照的两份包：完整包，以及仅移除本任务新增 CASM profile/style/artwork 的控制包。两组均通过官方构建入口，比较同一项目的输出；这样可以单独检验本次新增模板的影响。

| 现存项目 | 页数 | 构建 warning | 完整包 / 控制包 compare |
|---|---:|---:|---|
| Huazhong_template | 7 | 0 | 逐像素一致 |
| NSFC_2026_CCNU-EduAgentTrust_final | 7 | 0 | 逐像素一致 |
| NSFC_2026_MineChangeTrust_final | 13 | 0 | 逐像素一致 |
| NSFC_2026_CIESM-STSR_final | 26 | 12 条既有诊断，新引入 0 | 逐像素一致 |

CIESM 在执行期间从空白模板进入正文写作，冻结时为 26 页；两组均出现相同的 4 条 overfull 与 8 条缺字诊断（ñ、ë、Á），属于该项目的原有字体/正文问题，本任务未新增。此前 4 页空白版本已另行完成零警告回归。

结果见 [verification-results.json](verification-results.json)。上述结论限定于冻结时的源码；本次未修改其它项目正文或样式。
