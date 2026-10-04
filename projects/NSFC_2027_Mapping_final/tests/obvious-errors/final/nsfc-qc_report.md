# 当前申请书明显错误核查

核查时间：2026-09-22T23:35:56+08:00。对象：NSFC_2027_Mapping_final 当前46页 main.pdf。

**执行摘要**

确认两处直接错误：图1的“覆差差异”错字；参考文献[11]把LNCS丛书名填成具体会议论文集名。另有天池英才项目材料未同步、邮编来源冲突和研究空白表述过强三处需处理。未发现预算合计、主要样本量、实验次数或年度安排的明显矛盾。

**范围与只读声明**

按本项目2026版开放基金模板检查，不套用NSFC项目的页数上限或栏目要求。检查主文件、实际输入的14份TeX、48条文献题录、12幅实际插图、已有事实缺口记录及当前PDF。逐一查看全部插图，抽查封面、信息、成员、预算、文献与后置表格页面，并读取全文文本与最终构建日志。未修改TeX、BibTeX、PNG或PDF，未重新编译。

**硬性问题（P0）**

未确认P0级重大数值矛盾、缺失引用键或无法阅读/跳转的工程错误。该结论不等于正式申请材料已经齐备。

**重要问题（P1）**

**F01：图1竖排文字错字**

位置：[proposal.tex:13](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/extraTex/proposal.tex:13)；PDF第6页。

竖排标签实际写成“覆差差异”。

建议：将第二字“差”改为“盖”，得到“覆盖差异”；只改图中文字。

[放大像素证据](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/tests/obvious-errors/figures/figure01-vertical-label.png)

**F02：天池英才项目具体任务与最新事实库未同步**

位置：[extraTex/foundation.tex](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/extraTex/foundation.tex:148)；PDF第41页。

正文写“依据为项目任务书”并列具体负责内容，第150行进一步断言研究数据、评测和成果边界；共享事实库 docs/applicants/yan-feng.md 第84行于2026-09-22记录无可供核对的具体任务/成果材料，并撤下具体分工和已核对任务书表述。

建议：保留已经确认的名称、金额、期限与主持身份；具体分工及边界补充材料后再写，或改为拟遵守的原则。不能据此认定项目本身不存在。

最新事实来源：[共用申请人事实库](/home/yanfeng/fund-writing/ChineseResearchLaTeX/docs/applicants/yan-feng.md:84)。

**F03：地址与邮编存在新旧校区口径冲突**

位置：[extraTex/metadata.tex](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/extraTex/metadata.tex:19)；PDF第3页。

华瑞街777号使用830046；学校校区地址列表和研究生招生学院联系表将博达校区/计算机学院列为830017。学院页脚仍列830046，因此保留来源冲突说明。

建议：按实际收件地点核对；如为博达校区华瑞街777号，应优先采用校级及学院联系表的830017口径。

来源：[官方来源1](https://www.xju.edu.cn/zzjg1.htm)；[官方来源2](https://yz.xju.edu.cn/lianxiwomen/erjixueyuan/)；[官方来源3](https://it.xju.edu.cn/xygk/xyjj.htm)。

**次要问题（P2）**

**F04：SCAN参考文献的论文集名误用丛书名**

位置：[references/myexample.bib](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/references/myexample.bib:334)；PDF第14页。

参考文献[11]的booktitle只有Lecture Notes in Computer Science，漏了具体论文集Computer Vision – ECCV 2018。

建议：booktitle改为具体论文集名，LNCS放series，并按官方题录补卷11208、Springer和Cham。

来源：[Springer官方题录](https://link.springer.com/chapter/10.1007/978-3-030-01225-0_13)。

**F05：未完成方法查新，却提前断言研究空白**

位置：[extraTex/proposal.tex](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/extraTex/proposal.tex:75)；PDF第10页。

第75行使用“仍未被正面处理”，第365行却明确未取得最相关ESRN的可靠摘要和全文，尚无法判断方法重叠。

建议：改成需要进一步检验的具体问题；完成全文对照前不要断言既有工作尚未正面处理。

**引用核查清单**

48条文献题录均取得证据：46条Crossref注册元数据、1条JEIT官方页面、1条PMLR官方题录。没有缺失键、重复条目或未引用条目；143处引用链接和48个文献目标均通过PDF注释与可见编号校验。题录核验不表示逐篇全文查新，也不表示全部引文语义已重新核对。

完整证据：[文献检查简报](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/tests/obvious-errors/references/review.md)；[元数据证据JSON](/home/yanfeng/fund-writing/ChineseResearchLaTeX/projects/NSFC_2027_Mapping_final/tests/obvious-errors/references/crossref-evidence.json)。

LaTeX最终日志无警告、无越界或松散行框。BibTeX仍有已有的CLIP出版地字段缺失提示；PMLR官方题录没有该字段，本轮不将此提示判为假引，也不建议虚构地名。

**篇幅与结构分布**

| 内容 | 汉字数（预检口径） | 说明 |
|---|---:|---|
| 摘要 | 284 | 非空白可见字符约311，未见超出400字的明显问题 |
| 立项依据与研究内容 | 12432 | 含研究方案、创新和年度安排 |
| 研究基础与条件 | 4207 | 含个人/成员简介及在研项目 |
| PDF | 46页 | 参考文献位于物理第13—17页，12幅插图 |

未依据目录名中的2027判定2026年度、期限为错；供给的官方模板即为2026版。成员表原始编号重复“8”、末尾栏目编号沿用官方模板，不作为本轮新增错误。自动预检对UTF8、OMX、CasmResearch等源码名称的缩写警报已人工排除，不计入问题数。

**事实缺口与可提交判断**

正文未发现显式的“【待补 ID】”或“【暂定】”标记；以下事实缺口均已有记录或需要申请人材料，单列，不按未写正文占位计入P0/P1：

- **G01 主要成员教育与研究简历不足**：模板要求学历与研究工作简历，当前7人主要只有在读身份和拟定分工；需本人提供经历和成果，不能代编。（extraTex/foundation.tex:96,119-139）

- **G02 正在承担项目的列示范围需要核对**：当前列3项；教师官网另列2026年度光伏预测项目、2026.06-2026.10智能知识库项目及其他参与项目。栏目原文没有仅限相关项目的限定，当前小标题自行限定为相关项目。应按申报基准日、实际在研状态与本表要求核实完整清单，不能把共用资料中“本次申请”的筛选决定自动套用至本项目。（extraTex/foundation.tex:141-170） [学院教师页](https://it.xju.edu.cn/info/1144/3131.htm)。

- **G03 申请人奖励情况待本人确认**：未提供奖励材料，不应自行填无奖励。（extraTex/foundation.tex:96,112-116）

- **G04 ESRN方法重叠尚未完成全文核验**：题录真实性已通过；全文仍受访问限制。属于查新缺口，不是虚假文献。（extraTex/proposal.tex:365）

- **G05 预审计与试标尚未实施**：正文明确安排在执行期开展，没有虚称已完成；不能单独以未开展预实验认定不能申报。（extraTex/foundation.tex:35,75-83）

当前稿技术上可阅读和跳转；正式提交前应修正确定错误、处理事实冲突、补足模板要求的成员简介并完成签章手续。审核方意见栏空白、无高级职称申请人适用的推荐意见栏目不能一概作为当前申请人的正文缺项。没有以未开展预实验作为单独否决项。

**建议的最小修改路线**

1. 修正图1的一个错字与SCAN的具体论文集字段。
2. 核实天池英才项目可保留的事实、通讯邮编与在研项目完整清单。
3. 补充成员简历/奖励信息，将“仍未被正面处理”收敛为待检验问题。
4. 修改后沿官方thesis入口重编译，复核引用跳转、分页和新增警告。

**附录：复现与限制**

使用仓库nsfc-qc只读预检，并以三个独立子任务核查研究逻辑、全部配图和引用题录；未调用parallel-vibe批量代理脚本，现有协作工具已提供独立并行核查。文献证据来自Crossref、期刊及出版方；地址和项目资料对照学校/学院官网。公开网页与共享事实库出现分歧的内容保留不确定性，不据此认定申请人事实不实。

验证文件：nsfc-qc_metrics.json、nsfc-qc_findings.json、validation.json；其他证据位于本报告的上级目录。源码及PDF哈希复核：全部保持不变。
