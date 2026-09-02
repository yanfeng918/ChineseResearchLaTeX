# 新建项目

## 纯手工版本

新目录名建议保持 NSFC_ 前缀，否则 VS Code 同步脚本无法识别其为 NSFC 项目。

new_project=NSFC_MyProject

cp -a projects/NSFC_Local "projects/$new_project"

python packages/bensz-nsfc/scripts/nsfc_project_tool.py clean \
  --project-dir "projects/$new_project" \
  --remove-pdf

rm "projects/$new_project/NSFC_Local.code-workspace"

python scripts/sync_vscode_configs.py \
  --project "$new_project"

## 构建了一个脚本：

python scripts/create_project.py \
  --template NSFC_Local_Clean  \
  --name NSFC_2027_Silk_Road_Smart_Logistic_v3

脚本会：
    拒绝覆盖已有项目
    排除 .latex-cache、PDF 和 LaTeX 中间文件
    重新生成同名 VS Code 工作区
    失败时回滚本次新建目录


# 启动项目

----------------------------------------
基于projects/NSFC_General_Clean/docs中的信息，
请使用 nsfc-full-pipeline 处理 projects/NSFC_General_Clean这个项目，从头跑全流程。

----------------------------------------
请使用 nsfc-full-pipeline 处理 projects/你的项目，从头跑全流程。


# 把官方模板落成 LaTeX 项目


请使用 make-latex-model skill，把我提供的官方基金模板落成一个新的 LaTeX 项目。
目标项目：projects/NSFC\_2026\_Education\_final
参考模板：projects/NSFC\_2026\_Education\_final/template.pdf
目标：根据当前 ChineseResearchLaTeX 的真实分层，把这套模板调到可交付状态；如果问题属于共享样式，请优先改 packages/bensz-thesis，而不是只改项目层。
输出：直接修改代码并用官方构建入口验证；最后告诉我你改到了哪一层、为什么这样改。



# 最后，把NSFC格式的申报书转换为指定格式申报书：


场景 1：旧 NSFC 标书迁到当前项目
请使用 transfer-old-latex-to-new skill。
目标：把我这份旧 NSFC 标书正文迁移到当前仓库合适的 NSFC 项目里。
输入：
- 旧项目目录：/path/to/old-nsfc
- 目标模板参考：projects/NSFC_Young
要求：
- 只迁移正文与参考文献
- 不要修改模板样式和项目骨架
- 如果当前模板缺少承载位点，只报告，不要偷改模板



现在NSFC_2026_CCF_1688_Yuanbao2这个基金已经按照国自然写好了，
现在需要把这个项目下面的内容迁移到CCF-1688这个项目下面中，
latex的模板不一样，把需要的内容从
NSFC_2026_CCF_1688_Yuanbao2中迁移到这个项目中


## 当时使用了DeepSeek的接口操作：
现在文件夹里面有4个文件，你现在需要把任务申报书 .PDF 版本导入到重大科技专项申报书.doc，该对应的一定要对应起来。（38分钟）

但是，公式没有和原文的pdf对应，想办法使用公式编辑器还是什么方式？（43分钟）







