# nsfc-justification-writer 脚本

脚本只承担确定性边界：目标文件存在性、路径白名单、引用 key、字数统计、备份、diff 和回滚。逻辑、术语、论证维度、可读性等语义判断与正文改写由宿主 AI/用户完成。

## 推荐流程

1. 用户指定目标文件，或配置中声明 `targets.justification_tex`；不明确时只读追踪 `main.tex` 的唯一候选。
2. AI 输出完整正文提案，运行 `preview` 生成 unified diff。
3. 用户确认目标和 diff 后，才使用写入入口；写入前自动备份，写入后可用 `diff/rollback` 复核。

```bash
python skills/nsfc-justification-writer/scripts/run.py preview \
  --project-root projects/NSFC_Young \
  --proposal-file /tmp/proposal.tex
```

`preview` 不解析标题、不写入文件；如果新增/删除行包含章节、环境、引用入口或配置命令，会提示人工确认。

## 独立工具

```bash
python skills/nsfc-justification-writer/scripts/run.py refs --project-root projects/NSFC_Young
python skills/nsfc-justification-writer/scripts/run.py wordcount --project-root projects/NSFC_Young
python skills/nsfc-justification-writer/scripts/run.py diagnose --project-root projects/NSFC_Young
python skills/nsfc-justification-writer/scripts/run.py coach --project-root projects/NSFC_Young --stage auto
```

`diagnose/coach/review` 的结果是建议，不以固定小节数、开篇关键词或页数阈值阻断写作。逻辑、术语、论证维度和专业可读性由宿主 AI 自主规划并复核；措辞中的吹牛式、绝对化和无依据夸大表述由宿主 AI 按 `references/boastful_expression_guidelines.md` 复核，Python 不维护固定短语表。需要时可在配置 `constraints` 中显式启用独立预警。

## legacy 兼容入口

```bash
python skills/nsfc-justification-writer/scripts/run.py apply-section \
  --project-root projects/NSFC_Young \
  --title "国内外研究现状" \
  --body-file /tmp/new_body.txt
```

该命令仍按 `\\subsubsection` 标题替换正文，仅用于迁移旧项目；它不会成为新项目默认工作流。标题未命中时不要改正文来适配检查器，应改用 `preview` 并明确正文范围。

## 版本管理与验证

```bash
python skills/nsfc-justification-writer/scripts/run.py list-runs
python skills/nsfc-justification-writer/scripts/run.py diff --project-root projects/NSFC_Young --run-id <run_id>
python skills/nsfc-justification-writer/scripts/run.py rollback --project-root projects/NSFC_Young --run-id <run_id> --yes
python skills/nsfc-justification-writer/scripts/run.py validate-config
```
