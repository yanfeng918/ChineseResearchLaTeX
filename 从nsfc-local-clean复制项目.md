新目录名建议保持 NSFC_ 前缀，否则 VS Code 同步脚本无法识别其为 NSFC 项目。

new_project=NSFC_MyProject

cp -a projects/NSFC_Local "projects/$new_project"

python packages/bensz-nsfc/scripts/nsfc_project_tool.py clean \
  --project-dir "projects/$new_project" \
  --remove-pdf

rm "projects/$new_project/NSFC_Local.code-workspace"

python scripts/sync_vscode_configs.py \
  --project "$new_project"

二、构建了一个脚本：


python scripts/create_project.py \
  --template NSFC_Local_Clean  \
  --name NSFC_2027_Silk_Road_Smart_Logistic_v3

脚本会：
    拒绝覆盖已有项目
    排除 .latex-cache、PDF 和 LaTeX 中间文件
    重新生成同名 VS Code 工作区
    失败时回滚本次新建目录

