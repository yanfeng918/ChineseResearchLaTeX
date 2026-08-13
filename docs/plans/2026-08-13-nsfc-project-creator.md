# NSFC Project Creator Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 新增一个可从 `projects/NSFC_*` 模板安全创建干净项目副本的命令行脚本。

**Architecture:** 在根级 `scripts/` 增加独立 Python CLI，负责校验简单项目名、复制模板并过滤 LaTeX 构建产物，随后复用现有 `sync_vscode_configs.py` 生成与新目录同名的工作区配置。实现保持 NSFC 项目层薄封装，不改动 `bensz-nsfc` 公共包。

**Tech Stack:** Python 3 标准库、pytest、现有 VS Code 配置同步器。

**Minimal Change Scope:** 新增 `scripts/create_project.py` 和 `tests/bensz-nsfc/create-project/` 回归测试；仅同步更新根级 `README.md`、`projects/README.md` 与 `CHANGELOG.md`。不修改现有模板正文、公共包源码或用户已有项目。

**Success Criteria:** 命令能从 `NSFC_Local` 或 `NSFC_Local_Clean` 创建 `NSFC_*` 新目录；不复制 `.latex-cache`、PDF、旧工作区文件或常见 LaTeX 中间文件；生成正确的新工作区文件；对非法名称、缺失模板和已存在目标安全失败。

**Verification Plan:** 运行 `pytest tests/bensz-nsfc/create-project/test_create_project.py -v`，再运行 `python scripts/create_project.py --help` 和现有 `scripts/test_sync_vscode_configs.py` 回归测试。

---

### Task 1: 定义项目创建行为

**Files:**
- Create: `tests/bensz-nsfc/create-project/test_create_project.py`

1. 编写覆盖干净复制、VS Code 同步、非法名称、目标冲突和缺失模板的失败测试。
2. 运行目标 pytest，确认因 `scripts/create_project.py` 尚不存在而失败。

### Task 2: 实现最小 CLI

**Files:**
- Create: `scripts/create_project.py`

1. 实现参数解析、路径校验、过滤复制与失败回滚。
2. 调用现有 VS Code 同步函数生成 `<新项目名>.code-workspace`。
3. 运行目标 pytest，确认全部通过并按测试保护做必要重构。

### Task 3: 文档与回归验证

**Files:**
- Modify: `README.md`
- Modify: `projects/README.md`
- Modify: `CHANGELOG.md`

1. 记录推荐命令、默认模板和过滤规则。
2. 运行目标测试、VS Code 同步测试与 CLI 帮助检查。
3. 检查 Git diff，确保没有生成测试项目或构建产物。
