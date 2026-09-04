# 手动配置指南

本文档面向不使用 AI 自然语言安装、需要精确控制安装路径、镜像、版本与编译参数的高级用户，汇总本仓库及配套 skills 的全部手动命令。普通用户优先回到 [README](../README.md) 使用「自然语言安装」方式，让 Claude Code / OpenAI Codex 自动完成。

> 依赖配置 Python 3 环境

---

## LaTeX 公共包安装

对应 README 入口：[LaTeX 包安装](../README.md#latex-包安装) 的「推荐：让 AI 自然语言安装」。

本项目 [`packages/`](https://github.com/huangwb8/ChineseResearchLaTeX/tree/main/packages) 目录维护了以下可安装的 LaTeX 公共包，支持指定 1 个或多个包安装：

| 包名 | 说明 |
|------|------|
| `bensz-fonts` | 共享字体基础包——集中托管字体资产并提供统一字体 API |
| `bensz-nsfc` | NSFC 公共包——三套国自然模板的共享样式基础 |
| `bensz-paper` | SCI 论文公共包——支持 PDF / DOCX 双输出 |
| `bensz-thesis` | 毕业论文公共包——支持硕士/博士论文模板、DOCX 初稿导出与像素级验收脚本 |
| `bensz-cv` | 学术简历公共包——支持中英文简历模板与像素级验收脚本 |

### 远程硬编码安装

> 💡 `--ref` 参数支持版本 tag（如 `v4.0.1`）或分支名（如 `main`），默认为 `main`。
> 💡 如果当前网络无法访问 GitHub，也可以直接改用 Gitee 镜像里的同一份安装脚本。
> 💡 若使用 Gitee 脚本地址，安装命令里也建议显式带上 `--mirror gitee`，这样包体下载会一并走 Gitee。

直接远程下载安装脚本并执行：

安装器会优先自动探测 `kpsewhich`、`mktexlsr`、`texhash`、`initexmf` 的实际位置，并兼容 macOS / Linux / Windows 常见的 TeX Live / MiKTeX 安装目录。若你的 TeX 没有加入 `PATH`，或希望安装到自定义 texmf 树，可显式追加 `--texmfhome <路径>`。

**macOS / Linux / WSL：**

```bash
# 默认安装所有公共包
curl -fsSL https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py \
  | python3 - install

# 安装多个包
curl -fsSL https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py \
  | python3 - install --packages bensz-nsfc,bensz-paper,bensz-thesis,bensz-cv

# 中国大陆可显式切换到 Gitee 镜像下载包体
curl -fsSL https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py \
  | python3 - install --packages bensz-cv --mirror gitee

# 如果目标版本和已安装版本一致，安装器会自动跳过；需要覆盖时显式加 --force
curl -fsSL https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py \
  | python3 - install --force

# 如果连 GitHub 上的安装脚本也无法访问，可直接改用 Gitee 镜像脚本
curl -fsSL https://gitee.com/huangwb8/ChineseResearchLaTeX/raw/main/scripts/install.py \
  | python3 - install --mirror gitee
```

**Windows PowerShell：**

```powershell
(Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py' `
  -UseBasicParsing).Content | python - install

# 如果 GitHub 无法访问，可直接改用 Gitee 镜像脚本
(Invoke-WebRequest -Uri 'https://gitee.com/huangwb8/ChineseResearchLaTeX/raw/main/scripts/install.py' `
  -UseBasicParsing).Content | python - install --mirror gitee
```

如果你的 Windows 安装了官方 Python Launcher，也可以把上面的 `python -` 换成 `py -3 -`。若直接提示 `No installed python found!`，通常说明当前机器没有可用的 `py` 启动器，或 Python 尚未正确安装到命令行环境。

如需显式覆盖安装目录，可参考：

```powershell
(Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py' `
  -UseBasicParsing).Content | python - install --texmfhome "$HOME\\texmf"
```

查看所有支持的包：

```bash
curl -fsSL https://raw.githubusercontent.com/huangwb8/ChineseResearchLaTeX/main/scripts/install.py \
  | python3 - list

# GitHub 不通时可改用 Gitee 镜像脚本
curl -fsSL https://gitee.com/huangwb8/ChineseResearchLaTeX/raw/main/scripts/install.py \
  | python3 - list
```

### 本地硬编码安装

> 💡 `--ref` 参数支持版本 tag（如 `v4.0.1`）或分支名（如 `main`），默认为 `main`。

适用于已将仓库克隆到本地的场景。首先克隆仓库：

```bash
# GitHub 源站
git clone https://github.com/huangwb8/ChineseResearchLaTeX.git
cd ChineseResearchLaTeX
```

如果 GitHub 无法访问，也可改为：

```bash
git clone https://gitee.com/huangwb8/ChineseResearchLaTeX.git
cd ChineseResearchLaTeX
```

然后在**仓库根目录**执行：

```bash
# 默认安装所有公共包
python3 scripts/install.py install

# 安装多个包
python3 scripts/install.py install --packages bensz-nsfc,bensz-paper,bensz-thesis,bensz-cv

# 单独安装共享字体基础包
python3 scripts/install.py install --packages bensz-fonts

# 如果目标版本和已安装版本一致，会自动跳过；需要覆盖时显式加 --force
python3 scripts/install.py install --force

# 使用 Gitee 镜像下载包体
python3 scripts/install.py install --packages bensz-paper --mirror gitee

# 查看所有支持的包
python3 scripts/install.py list
```

其中 `bensz-nsfc`、`bensz-paper`、`bensz-thesis`、`bensz-cv` 现都带包级版本管理/激活能力；普通用户仍建议优先走根级统一安装器，如需直接切换或回退某个公共包版本，可再调用各包自己的安装器，例如：

```bash
python packages/bensz-paper/scripts/package/install.py install --ref main
python packages/bensz-paper/scripts/package/install.py rollback
python packages/bensz-thesis/scripts/package/install.py check
python packages/bensz-cv/scripts/package/install.py use --ref v4.0.0
```

这些包级安装器的缓存与状态文件现统一收口到 `~/.ChineseResearchLaTeX/<package>/`，例如 `~/.ChineseResearchLaTeX/bensz-paper/`，避免在用户主目录散落多个顶级隐藏目录。

---

## LaTeX 模板编译

对应 README 入口：[LaTeX 模板编译](../README.md#latex-模板编译) 的自然语言描述。

可以手动在 VSCode 里编译，也可以使用统一的 Python 渲染器生成 PDF。

### NSFC 模板

适用于 `projects/NSFC_*`：

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir projects/NSFC_Young
```

### SCI 论文模板

适用于 `projects/paper-*`，支持 PDF + DOCX 双输出：

- 正文默认维护在 `extraTex/**/*.tex`；DOCX 导出只在运行期临时生成 Markdown，不再保存第二份正文源文件
- DOCX 后处理会为 Pandoc 默认表格补上稳定可见的横向边框；示例项目 `paper-sci-01` 当前已切到更接近 `CCS/paper` 的 Vancouver/JITC 参考文献口径，并进一步按当前 LaTeX profile 统一 Word 侧的标题、作者与参考文献关键样式
- DOCX 数学公式会经 HTML5 + MathML 中间态落成 Word 原生公式对象，避免 `$\\gamma$` 这类源码形式直接泄漏到投稿文档
- 若项目未声明参考文献命令，构建链会自动跳过 `biber` 与 citeproc，适合 `paper-coverletter-01` 这类投稿信项目
- `count-words` 支持对一个或多个 `.tex` 做可见字数统计；若传入 `main.tex`，会递归跟随 `\input` / `\include` 链，并自动忽略 LaTeX 命令名、引用 keys 与数学公式源码

```bash
python packages/bensz-paper/scripts/paper_project_tool.py build --project-dir projects/paper-sci-01
python packages/bensz-paper/scripts/paper_project_tool.py build --project-dir projects/paper-coverletter-01
python packages/bensz-paper/scripts/paper_project_tool.py count-words projects/paper-sci-01/extraTex/body/introduction.tex projects/paper-sci-01/extraTex/body/results.tex
```

### 学位论文 / 博士后研究报告模板

适用于 `projects/thesis-*`：

- 每个 thesis 项目都应在 `packages/bensz-thesis/` 中拥有独立的 `template/profile/style`；`thesis-smu-postdoc` 现已独立于 `thesis-smu-master`，仅共享同一公共包基础设施
- 可通过 `docx` 子命令从同一份 LaTeX 源导出可编辑 Word draft；复杂表格、算法、代码块、TikZ 或 PDF 专属构造会在 `.latex-cache/docx/main_docx_quality_report.md` 中提示人工复核，学校 Word 样式建议配合 `--reference-doc` 使用

```bash
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-nju-master
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-nju-master --tex-file baseline.tex
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-nju-master --tex-file editable.tex
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-sysu-doctor
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-ucas-doctor
python packages/bensz-thesis/scripts/thesis_project_tool.py build --project-dir projects/thesis-smu-postdoc
python packages/bensz-thesis/scripts/thesis_project_tool.py docx --project-dir projects/thesis-smu-master
```

### 简历模板

适用于 `projects/cv-*`，支持中英文 PDF 双输出与像素级比较：

```bash
python packages/bensz-cv/scripts/cv_project_tool.py build --project-dir projects/cv-01 --variant all
```

---

## Skills 项目级加载与迁移

对应 README 入口：[Skills](../README.md#-skills)。本仓库自有 Skills 随 Git 版本一起交付，不再要求安装到 `~/.agents/skills`、`~/.codex/skills` 或 `~/.claude/skills`。

### 普通使用

克隆或更新仓库后，直接从仓库根目录或其子目录启动 Codex / Claude Code。宿主分别读取已提交的 `.agents/skills/` 与 `.claude/skills/` 薄入口，再转到 `skills/<name>/SKILL.md` 的 canonical 指令和资源。

不要直接修改两个隐藏入口目录；它们由脚本生成。

### 维护入口

```bash
# 修改、新增或删除 skills/* 后，同步两个宿主入口
python3 scripts/sync_project_skills.py sync

# 提交前只读检查；发现缺失或漂移时返回非零状态
python3 scripts/sync_project_skills.py check
```

同步器会校验目录名与 `SKILL.md` frontmatter 的 `name`；存在 `config.yaml` 时，也会校验其中的 `skill_info.name`。生成入口只保留宿主共同支持的 frontmatter 字段，避免 canonical Skill 中的历史扩展字段阻断发现。它只会清理带生成标记的陈旧入口，不会删除自定义目录。

### 审计旧全局副本

```bash
# 只读列出与当前项目 25 个 Skills 同名的用户级副本
python3 scripts/sync_project_skills.py audit-global

# 机器可读输出
python3 scripts/sync_project_skills.py audit-global --json
```

审计不会修改用户主目录。若确认旧副本不再被其他项目使用，可显式归档：

```bash
# 只移动精确同名目录/符号链接，并生成可恢复 manifest
python3 scripts/sync_project_skills.py archive-global --apply
```

归档默认位于 `~/.ChineseResearchLaTeX/skill-backups/<时间戳>/`。需要回退时使用归档命令打印出的 manifest：

```bash
python3 scripts/sync_project_skills.py restore-global \
  --manifest ~/.ChineseResearchLaTeX/skill-backups/<时间戳>/manifest.json \
  --apply
```

恢复操作遇到已有目标时会拒绝覆盖。归档与恢复都只接受当前项目拥有的精确 Skill 名，不处理第三方、系统或插件 Skill。

用户级同名副本仍存在时，Codex 可能显示重复项，Claude Code 也可能优先使用个人副本。完成归档后重启或刷新宿主，并核对实际 Skill 来源是否位于当前仓库。

### 外部 Skill 依赖

本仓库未内置的依赖单独登记在 [`skills/external-dependencies.yaml`](../skills/external-dependencies.yaml)。当前 `parallel-vibe` 是 `research-idea` 的必需依赖，也是 `nsfc-reviewers`、`nsfc-qc` 的可选增强依赖；本次迁移不会替用户自动安装或删除它。
