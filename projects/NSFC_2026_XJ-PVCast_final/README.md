# 中国沙漠气象科学研究基金申请书：XJ-PVCast

本项目将既有光伏概率预测与爬坡风险研究正文整理为可编辑的基金申请表。目录名保留 `NSFC_` 前缀，实际属于开放基金申请书，使用 `bensz-thesis` 的独立 `xj-desert-fund-2026` profile；`template.json` 显式声明 `build_profile=thesis`，没有学位论文 `degree`。

`main.tex` 是填写后的申请书入口，输出 `main.pdf`，研究正文按内容自然续页；`blank.tex` 是不加载个人信息的独立空白入口，输出 `blank.pdf`，用于与所供 [官方13页PDF](中国沙漠气象科学研究基金.pdf) 比较。官方封面、填报说明、申请信息简表、六个科研正文栏目、成员分工、预算、推荐与审批、预算说明及两份承诺保留为原生LaTeX文字和表格。

PDF 正文中的文献引用编号可点击跳转到对应参考文献条目，保持黑色文字与原有打印版式。

## 构建和编辑

完整仓库中，需准备XeLaTeX、BibTeX、Python及本仓库版本的 `bensz-fonts` / `bensz-thesis`。以下命令在仓库根目录执行，必须等上一条结束再执行下一条；两个入口共用 `.latex-cache/`，不可并行构建：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_XJ-PVCast_final --tex-file blank.tex
python3 packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/NSFC_2026_XJ-PVCast_final --tex-file main.tex
```

也可在本项目目录使用薄封装，仍转调同一官方构建器：

```bash
python3 scripts/thesis_build.py build --tex-file blank.tex
python3 scripts/thesis_build.py build --tex-file main.tex
```

在VS Code中打开 [NSFC_2026_XJ-PVCast_final.code-workspace](NSFC_2026_XJ-PVCast_final.code-workspace)，LaTeX Workshop通过 `texlua → scripts/latex_workshop_build.lua → scripts/thesis_build.py` 调用官方链路。两个入口可分别编辑和编译，不在同一时间触发构建。中间文件进入 `.latex-cache/`，最终PDF保留在项目根目录。

空白版式比较使用官方入口；测试材料写入仓库 `tests/` 子目录：

```bash
python3 packages/bensz-thesis/scripts/thesis_project_tool.py compare --project-dir projects/NSFC_2026_XJ-PVCast_final --tex-file blank.tex --baseline-pdf projects/NSFC_2026_XJ-PVCast_final/中国沙漠气象科学研究基金.pdf --output-dir tests/xj-pvcast-template/blank-compare
```

比较使用已构建PDF。需要重建时先顺序执行上述构建命令，不同时运行编辑器自动构建和命令行构建。

## 内容入口和修改层级

| 内容 | 维护位置 |
|---|---|
| 姓名、单位、职称、联系方式、完整地址、研究期等统一字段 | [extraTex/metadata.tex](extraTex/metadata.tex)，通过 `\XJField{key}` 引用 |
| 400字内研究摘要、考核指标 | [extraTex/abstract.tex](extraTex/abstract.tex)、[extraTex/assessment.tex](extraTex/assessment.tex) |
| 官方栏目1至6正文 | `extraTex/01-justification.tex` 至 `extraTex/06-foundation.tex` |
| 申请人履历、申报资格和成果归属说明 | `extraTex/applicant-cv.tex`、`extraTex/07-declarations.tex`，均由栏目6输入 |
| PDF插图 | `figures/F02.pdf`、`figures/F03.pdf`、`figures/F05.pdf` 原样用于栏目3；[figures/F04-confirmed.pdf](figures/F04-confirmed.pdf)仅删除原F04中的“暂定”；原F01、F04保留为迁移原件 |
| 图1研究背景与意义 | [figures/background-significance.tex](figures/background-significance.tex)，按用户要求调整，图注与引用在栏目1 |
| 2.1新增研究内容框架图 | [figures/research-content-framework.tex](figures/research-content-framework.tex)，原生TikZ文字和路径，随主入口构建 |
| 参考文献 | [references/myexample.bib](references/myexample.bib) |
| 本项目成员及拟分工 | [extraTex/team-metadata.tex](extraTex/team-metadata.tex)统一字段、[extraTex/members.tex](extraTex/members.tex)组装8人成员表；7名研究生按共用参与者资料回填 |
| 经费金额和计算根据 | [extraTex/budget.tex](extraTex/budget.tex)；已按本次授权填写3.00万元申请预算，申请经费共用metadata字段，尚未获批 |
| 共享标题、表框、固定字段容纳、参考文献间距和分页 | `packages/bensz-thesis/styles/bthesis-style-xj-desert-fund-2026.tex` 及同模板artwork |
| 产品线和构建身份 | [template.json](template.json)、[extraTex/@config.tex](extraTex/@config.tex) |

迁移阶段保留原项目研究段落、4处陈列公式及30个正文引用键；本次在此基础上确定研究设计、计划和预算。原BibTeX库31条记录及全部既有字段保留，2条预印本将已记录的 `citedate` 同值补为新版样式支持的 `urldate`；1条未引用记录不强制列入文献表。F01至F05共5幅矢量PDF原件完整保留，迁移详情及文件校验值见 [资源迁移清单](docs/资源迁移清单.md#L1)。图1已按用户要求调整为原生TikZ“研究背景与意义”，旧F01不再参与正文；本次图5使用仅移除“暂定”字样的 [F04-confirmed.pdf](figures/F04-confirmed.pdf)，原F04保留，其余图示及80%与90%层级不变。

研究方法、技术路线和可行性已移入官方栏目3，研究积累、相关在研项目与简历归入栏目6。栏目标题只在栏目首页出现，续页保留表框与页码。内部采用真正的 `\subsection` / `\subsubsection`，编号按所属栏目连续生成。后续修改不应重新在正文中复制官方栏目全标题，也不应手写子标题编号。

## 本次确定的申请方案

2026年9月20日按用户授权，根据申请人的DWT-Former研究基础、现有8块A40和6块RTX 3090 Ti、7名研究生及2027–2028年期限，确定原稿中的研究参数和申请预算。

- 以1个新疆主场站为主体，目标连续24个月历史记录，最低12个月启动场站方法验证；第2场站和日前预测为取得相应授权、档案后的扩展。
- 每15分钟采样和发布，预测未来15–240分钟；按50%/15%/15%/20%连续划分训练、验证、初始校准及测试段，季节结论限于实际测试月份。
- DWT-Former为主模型，输出19个分位数，报告80%和90%区间，主滚动校准窗口为30天。主爬坡判据为30分钟功率净变化幅度超过装机容量20%，主要终点为未来第60至90分钟的下降爬坡；每次100条轨迹，重点分层至少30个有效日/过程块，事件结论要求30个含事件块，仍结合分块自助置信区间判断。
- 2026年9月21日补全过去60分钟辐照状态分类、跨日过程合并与未知状态回退规则；验证段告警同时约束平均每有效日误报≤1次、误报时间比例≤5%，测试锁定阈值并报告实际负担。
- 7名研究生参与、重点培养2名；完成并投稿论文1篇，交付算法软件1项及数据规范、方法报告、离线原型和使用说明。
- 申请预算3.00万元：业务费1.50万元、劳务费1.20万元、管理费0.30万元，设备费、设备购置费、其他来源及相关其他经费均为0.00万元。

上述内容为本次申报设计，数据授权、成果取得及经费获批状态据实另行记录。详细方法和预算计算根据见 [研究方法](extraTex/03-methods.tex#L1) 与 [填写说明](docs/填写说明与待补清单.md#L1)。

## 正式提交前

已知资料已回填。原课题名29个汉字，未改题；官方研究期与原事实库均为2027年1月至2028年12月。3万元申请预算及分类计算根据已填入，仍须按正式申报流程审核。邮编、邮箱及部分履历维持公开来源待终核状态；签名、盖章、推荐和审批区域按实际流程完成。

本次提供的7名新疆大学研究生均已列入，并按研究任务安排分工；人员表包含申请人共8人，原始证件和联系号码不额外复制到该表。重点培养目标已确定为2名，具体人选、实际投入、本人签名、学历及职称按实际情况核对。

请集中核对 [填写说明与待补清单](docs/填写说明与待补清单.md#L1) 和 [项目事实来源](docs/00_项目事实库.md#L1)。F-XJ-01至F-XJ-08所涉数据授权、NWP档案、人员投入、合作、限项、成果规则、先导证据及审核签章仍按真实材料落实，正式汇总表按要求补齐。

迁移阶段的结构化验收脚本位于仓库 `tests/xj-pvcast-template/`，历史结果见 [模板迁移验收报告](../../tests/xj-pvcast-template/REPORT.md#L1) 和 [2026年9月20日方案确定验证报告](../../tests/xj-pvcast-decisions-20260920/REPORT.md#L1)。本次补实方法判据，精简重复与内部编辑说明，增加管理费用途并处理参考文献跨页孤行；当前构建、页数及一致性检查见 [2026年9月21日质检修正报告](../../tests/xj-pvcast-qc-fix-20260921/REPORT.md#L1)，不沿用历史页数或图位。
