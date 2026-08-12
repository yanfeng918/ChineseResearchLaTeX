# CCF-1688 Build Repair Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 让独立目录 `Fund-projects/ccf-1688` 能通过 VS Code 与 NSFC 官方构建脚本稳定生成 `main.pdf`。

**Architecture:** 项目层 wrapper 复用可工作的兄弟项目搜索逻辑，定位同级 `ChineseResearchLaTeX/packages`。共享包层新增仅服务 `type=ccf1688` 的 profile/template，不把公共样式复制回项目；Lua launcher 同时修正 POSIX 编码退出码，避免失败被误报为成功。

**Tech Stack:** Python 3、pytest、Lua/texlua、XeLaTeX、`bensz-nsfc` 公共包。

**Minimal Change Scope:** 仅修改 `Fund-projects/ccf-1688/scripts/`、新增 `Fund-projects/ccf-1688/tests/`，并在 `ChineseResearchLaTeX/packages/bensz-nsfc/` 新增 ccf1688 专属 profile/template、更新 profile 错误提示；不改申请正文、不复制共享字体、不改其它 NSFC profile/template。

**Success Criteria:** wrapper 能发现共享构建脚本；无效构建返回非零状态；`type=ccf1688` 可识别；目标项目生成 5 页 A4 `main.pdf`；现有 General/Local/Young 官方构建全部通过。

**Verification Plan:** 运行目标项目 pytest；运行 `python scripts/nsfc_build.py build --project-dir .`；检查 `pdfinfo main.pdf`；回归 `projects/NSFC_General`、`projects/NSFC_Local`、`projects/NSFC_Young`；用像素对比脚本对比目标输出与既有缓存 PDF。

---

### Task 1: 锁定失败行为

**Files:**
- Create: `/home/yanfeng/fund-writing/Fund-projects/ccf-1688/tests/test_build_pipeline.py`

1. 测试 wrapper 能发现同级 `ChineseResearchLaTeX` 中的 `nsfc_project_tool.py`。
2. 测试 Lua launcher 保留子进程非零退出码。
3. 测试共享包具备 ccf1688 profile/template。
4. 运行 pytest，确认三项在修改前失败。

### Task 2: 修复项目级构建入口

**Files:**
- Modify: `/home/yanfeng/fund-writing/Fund-projects/ccf-1688/scripts/nsfc_build.py`
- Modify: `/home/yanfeng/fund-writing/Fund-projects/ccf-1688/scripts/latex_workshop_build.lua`

1. 从可工作的兄弟项目移植共享仓库搜索逻辑。
2. 解码 texlua 在 POSIX 返回的 wait status，保留真实退出码。
3. 重跑入口相关测试。

### Task 3: 补齐 ccf1688 专属共享模板

**Files:**
- Create: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/packages/bensz-nsfc/profiles/bensz-nsfc-profile-ccf1688.def`
- Create: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/packages/bensz-nsfc/templates/bensz-nsfc-ccf1688.tex`
- Modify: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/packages/bensz-nsfc/bensz-nsfc-core.sty`

1. 新增最窄的 ccf1688 profile。
2. 新增页面、字体、页眉页脚、标题与表格宏实现。
3. 更新支持 profile 的错误提示。
4. 运行目标项目官方构建并检查 5 页 A4 输出。

### Task 4: 视觉与包级回归

**Files:**
- Output only under: `/home/yanfeng/fund-writing/ChineseResearchLaTeX/tests/`
- Output only under: `/home/yanfeng/fund-writing/Fund-projects/ccf-1688/.latex-cache/`

1. 对比新输出与既有缓存 PDF，记录页面和像素差异。
2. 运行 `validate_package.py`。
3. 官方构建 General、Local、Young 三套现有 NSFC 项目。
4. 检查工作区仅包含预期改动与构建产物。
