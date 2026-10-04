# CCNU-EduAgentTrust 最终模板交付验收

交付：[七页可编辑空白申请书](../../projects/NSFC_2026_CCNU-EduAgentTrust_final/main.pdf)、[LaTeX 入口](../../projects/NSFC_2026_CCNU-EduAgentTrust_final/main.tex)、[填写与构建说明](../../projects/NSFC_2026_CCNU-EduAgentTrust_final/README.md)。本报告验收模板排版和填写能力，未填入真实申请人或研究事实。

## 修改层级与理由

- **项目层**：新增 `main.tex`、`extraTex/`、`template.json`、Python wrapper、同名 VS Code 工作区及受管配置、README 和双宿主项目指令。`document_type=open-fund-application` 表达申请书性质，`build_profile=thesis` 明确构建器，覆盖 `NSFC_` 名称推断；不伪造学位元数据。
- **公共包层**：复用现有 `ccnu-open-fund-2026` profile，仅在 `styles/bthesis-style-ccnu-open-fund-2026.tex` 修正封面“课题负责人”的分散对齐。官方五字横坐标为 122.52、145.92、169.32、192.84、216.24 bp；旧实现连排，末字提前约 29.92 bp。这是两个 CCNU 项目共用的固定标签，项目内覆盖会重复公共样式，因此直接修复专属 style。没有修改核心入口、字体 API 或构建脚本。
- **仓库说明层**：更新根级 README、项目导览、公共包 README 和 CHANGELOG；`.gitignore` 放行验收脚本与摘要，光栅图、日志和临时填写副本继续隔离在本测试目录。

本项目与 `Huazhong_template` 的官方基线 SHA-256 相同：`2d7251d3338255a659e58a930c4a6d002c42769f3ad320858185f5b546a1a6aa`。复用既有模板身份即可，未新增同义 profile，也未把整套公共样式复制回项目。

修改公共包前已运行技能的 [回归规划脚本结果](package-regression-plan.json)。规划器按 `thesis-*` 名称匹配，本工作树没有该前缀的项目；因此补充扫描 `projects/` 中真实的 `bensz-thesis` 引用，形成 [实际消费者回归范围](regression-scope.json)，包含目标及四个已有开放课题项目。

## 目标验证

所有命令从本测试目录启动；构建通过 `packages/bensz-thesis/scripts/thesis_project_tool.py`，最终产物位于项目根目录，其余文件隔离到 `.latex-cache/`。

| 验证 | 结果 |
|---|---|
| 官方空白版 build | 成功；7 页；无 LaTeX warning、Error、Overfull/Underfull 或缺字 |
| 与官方基线的页面及文字检查 | 7 页尺寸、方向一致，第 4 页横向；逐页可见字符计数一致，结合全页视觉检查核对原文和顺序；无嵌入图片 |
| 固定表格几何 | 封面、信息表、成员表、预算及意见页的线段数一致，坐标最大误差小于 0.002 bp |
| 封面标签修复 | 五字原点与官方基线最大误差 0.000992 bp |
| 填写副本 | 7 页；封面与信息表共用标题，申请人、首末成员、预算及单位意见均正常显示；B 类圈选正常 |
| 长正文副本 | 12 页；两章末尾标记完整，续页保留标题、版框及连续页码，正文未越框 |
| 固定字段超高 | 按预期失败，输出 `Fixed form cell overflow`；这是专门构造的负向测试，不是交付版错误 |
| VS Code 实际入口 | `texlua → thesis_build.py → thesis_project_tool.py` 构建成功 |
| VS Code 同步检查 | `sync_vscode_configs.py --project NSFC_2026_CCNU-EduAgentTrust_final --check` 通过 |
| 公共包结构校验 | `validate_package.py --skip-compile` 返回 `status=ok` |

可重跑的 [目标验收脚本](verify_delivery.py) 与 [结构、填写和续页结果](verification.json) 一并保留。填写和续页副本未复制参考 PDF，确认排版不依赖基线。最后一次正式交付构建由 VS Code launcher 调用官方入口完成，零错误、零警告。

## 同包项目回归

均在 `regression/` 的项目副本中调用官方构建器，避免覆盖其他项目现有内容与交付文件。结果见 [regression-results.json](regression-results.json)。

| 项目 | 构建和像素回归 |
|---|---|
| `Huazhong_template` | 7 页，零错误、零警告；仅第 1 页发生预期的标签字距变化，第 2–7 页逐像素一致 |
| `NSFC_2026_CIESM-STSR_final` | 4 页，零错误、零警告，与保存的原产物逐像素一致 |
| `NSFC_2026_MineChangeTrust_final` | 13 页，零错误、零警告；控制 CCNU 样式前后版本的两次构建逐像素一致 |
| `NSFC_2027_Mapping_final` | 10 页，零错误、零警告，与保存的原产物逐像素一致 |

中南大学项目的现有预生成 PDF 与当前源码构建结果在第 3 页已有差异。为区分该差异与本次修改，在测试目录冻结两份公共包源码，确认它们**只有 CCNU 样式的本次字距修改不同**，然后对同一中南大学项目副本分别调用原样复制的官方构建器。两份新产物严格 compare 返回 0、逐像素一致，表明本次修改未引入那一页差异；未修改中南大学模板来追平其旧产物。

## 官方 PDF 版式比对与限制

官方 compare 已按 144 DPI 执行，7 页尺寸和方向一致，返回码为 **1**、`identical=false`，详见 [比对摘要](compare-summary.json)。这表示仍有像素差异，不能宣称严格逐像素验收通过。

原生文字、表格线和分页结构完成复核。参考 PDF 的封面 `WPSEMBED2` 等字体与共享宋体、Adobe 黑体/仿宋在字形、字重上不同，WPS 与 XeLaTeX 也有标点及字距差异。封面“课题负责人”的独立位置偏差已修复，余下字体差异没有通过嵌入参考页面掩盖。

完整差异图及 compare 报告保存在本地 `compare/`，可按项目 README 的官方命令重新生成。
