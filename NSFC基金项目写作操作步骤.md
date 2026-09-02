# 开一份新 NSFC 标书：操作步骤

> 面向 `NSFC_General_Clean`（面上/青年，three-part 布局）。地区项目把模板换成 `NSFC_Local_Clean` 即可，章节编号是另一套，见 [nsfc-writing-workflow-guide.md](docs/nsfc-writing-workflow-guide.md) 第七节。
>
> 本文只讲**怎么起跑一份标书**。模板安装、编译原理、改哪些 `.tex` 见 [docs/nsfc-usage-guide.md](docs/nsfc-usage-guide.md)；写作流程的完整规则见 [docs/nsfc-writing-workflow-guide.md](docs/nsfc-writing-workflow-guide.md)。

---

## ⚠️ 先看这条

**`NSFC_General_Clean` 是 `create_project.py` 的源模板，不是工作目录。**

直接在里面写，题目、团队、事实库会留在模板里，以后每次 `create_project.py --template NSFC_General_Clean` 都会把上一个项目的内容带进新项目。这个坑真实发生过，记录在 [nsfc-writing-workflow-guide.md:276-278](docs/nsfc-writing-workflow-guide.md#L276-L278)。

模板的 `docs/` 只应有三个骨架文件：`00_项目事实库.md`、`workflow_status.yaml`、`README.md`。

所以第 1 步先复制出去。如果确实要在 Clean 里写，后面步骤把路径换掉即可，其余完全一样。

---

## 第 1 步：建项目

```bash
cd /home/yanfeng/fund-writing/ChineseResearchLaTeX
python3 scripts/create_project.py --template NSFC_General_Clean --name NSFC_2027_你的项目名
```

名字必须以 `NSFC_` 开头，否则 VS Code 同步脚本认不出它是 NSFC 项目。脚本会拒绝覆盖已有项目、排除 PDF 与 LaTeX 中间产物、重新生成同名 VS Code 工作区，失败时回滚本次新建目录。

下文所有 `<项目>` 都指 `projects/NSFC_2027_你的项目名`。

| 模板 | 适用 | 布局 |
|---|---|---|
| `NSFC_General_Clean` | 面上、青年 | three-part（`1.1` + `2.1`–`2.3` + `3.1`–`3.4`） |
| `NSFC_Local_Clean` | 地区 | five-part（`1.1`–`1.5` + `2.1`–`2.4` + `3.1`–`3.5`） |

## 第 2 步：让 `nsfc-full-pipeline` 能触发（一次性）

这个编排器装在了 `~/.codex/skills/`，**没装到 `~/.claude/skills/`**，所以在 Claude Code 里按名字调不出来：

```bash
cp -a skills/nsfc-full-pipeline ~/.claude/skills/
```

不想装也行——起跑时改说「读取 `skills/nsfc-full-pipeline/SKILL.md` 后处理 …」，效果一样。

## 第 3 步：共用层——通常不用动

[docs/applicants/yan-feng.md](docs/applicants/yan-feng.md) 已填好：身份、履历、科研项目 `P-H*`/`P-V*`、代表作 `O-*`、科研条件、跨项目待补事实 `F-GEN-*`。新项目的 `workflow_status.yaml` 里 `applicant_profile_file` 已指向它。

**履历、论文、在研项目不要抄进项目事实库。** 共用层改一处，全项目生效。论文发表了、拿了新项目，只改这一份文件。

换申请人时才需要新建 `docs/applicants/<slug>.md`，照 `yan-feng.md` 的结构写。

## 第 4 步：填项目事实库

编辑 `<项目>/docs/00_项目事实库.md`，逐节替换 `<...>` 占位，删掉用不到的小节。frontmatter 里 `project:` 和 `applicant_profile:` 的 slug 记得改。

**这几项必须填**，否则 stage 01 会停（选题未定是仅有的两个硬阻塞之一）：

| 小节 | 必填 |
|---|---|
| 一、申报目标 | 申报类别（面上）、申报方向、建议经费、执行期、申请截止 |
| 三、研究边界 | **中文题目、研究对象、应用场景、明确禁止扩展的方向** |
| 五、团队 | 逐人「姓名—角色—负责模块」；通讯录和学生名单不自动算成员 |
| 六、数据与条件 | 只写本项目特有的数据/样本/场地，通用算力见共用层 |

每条都要标状态：

| 状态 | AI 的行为 |
|---|---|
| `已确认` | 直接写入正文，不再询问 |
| `公开来源待终核` | 可作草稿素材，提交前需复核 |
| `待本人确认` | 不得推断为既成事实 |
| `明确暂无` | 可用真实、保守的否定表述 |

**回答"没有""不适用"也是有效的事实决定**，标成 `明确暂无`，同一轮任务就不会反复追问。

不要把身份证号、学号、私人手机号写进任何事实库文件。

## 第 5 步：改断点文件的 3 个空字段

`<项目>/docs/workflow_status.yaml` 里只有这三个是空的：

```yaml
project:
  type: NSFC_General
  grant_type: 面上项目
  length_budget: "正文 ≤30 页"
```

其余已经对了，不要改：`layout: three-part`、`fill_policy: draft_first`、`proposal_path`、`body_dir`、`bib_file`、两个事实源路径。

`stages` 段由流程自动维护，手工别动。

## 第 6 步：起跑

```text
请使用 nsfc-full-pipeline 处理 projects/NSFC_2027_你的项目名，从头跑全流程。
```

按 00–14 阶段串联：选题 → 文献调研 → 科学问题 → 研究方案 → 第一部分正文 → 研究基础与工作条件 → 其他说明 → 引用核查 → 篇幅对齐 → 去 AI 味 → QC → 模拟评审 → P0/P1 定点修复 → 编译。

断点写在 `workflow_status.yaml`，中断后说「继续」就续跑，不会推倒重来。

评审后自动改稿：

```text
根据模拟评审报告修复 P0/P1 问题
```

**想自己控制节奏**，就按顺序逐个触发：`research-topic-extractor` → `research-literature-review` → `research-idea` → `research-plan` → `nsfc-justification-writer` → `nsfc-research-content-writer` → `nsfc-research-foundation-writer` → `nsfc-ref-alignment` → `nsfc-length-aligner` → `nsfc-humanization` → `nsfc-qc` → `nsfc-reviewers`。

## 第 7 步：查缺口 → 补齐 → 定点回填

缺事实默认不停（`draft_first`），挖个带编号的坑继续写：

| 缺什么 | 标记 |
|---|---|
| **可推定**：年度计划月份、成果数量口径、实验规模、指标阈值 | `\textbf{【暂定 …】}`，正文写完整，不阻塞提交 |
| **硬事实**：批准号、经费额度、论文、获奖、平台型号、团队成员、国基完成情况、各类声明 | `\textbf{【待补 ID：说明】}`，句子写完整，只挖掉事实本身 |

看还欠什么：

```bash
python3 skills/nsfc-full-pipeline/scripts/scan_gaps.py --project-dir projects/NSFC_2027_你的项目名
```

加 `--id F-GEN-03` 只看某一条。

补完后直接说「我补充了 F-GEN-03」或「补充完了」，AI 会重读事实库找出状态变成 `已确认`/`明确暂无` 的条目，**只改那几句**，不重写整节。

确认为 `明确暂无` 也算补齐——占位换成 `无相关情况。`，不是换成另一个占位。

## 第 8 步：编译

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir projects/NSFC_2027_你的项目名
```

`bensz-nsfc` 已装在 `~/texmf/`。链路是 `xelatex → bibtex → xelatex → xelatex`，中间文件进 `.latex-cache/`，根目录只留 `main.pdf`。

改完 `.tex` 不重新编译，PDF 不会变。

## 第 9 步：编排器不覆盖的，单独调

| 环节 | 技能 |
|---|---|
| 中英文摘要（**申请书必填**） | `nsfc-abstract` |
| 申请代码推荐 | `nsfc-code` |
| 预算说明书 | `nsfc-budget` |

配图不在 `nsfc-full-pipeline` 内，正文定稿后单独走一遍，见第 10 步。

## 第 10 步：配图

**时机**：正文定稿、`【待补 …】` 清空之后。图会改变页数，所以必须排在篇幅对齐之前的最后一环——出完图还要回头重跑一次篇幅检查。

### 10.0 前置检查（一次性）

| 项 | 检查 |
|---|---|
| `academic-figure-*` 四个技能 | `~/.claude/skills/` 与 `~/.agents/skills/` 都有，[绘图提示词.md](绘图提示词.md) 里的绝对路径有效 |
| `auto-draw-plot` 出图凭据 | 需要 `~/.bensz-skills/config/remote.env`，**缺了前三步照跑、到出图才失败** |
| `image-to-editable-ppt` | 只装在 `~/.codex/skills/`，Claude Code 里按名字调不出来 |

```bash
# 出图凭据（二选一，看买的是哪个）
mkdir -p ~/.bensz-skills/config
cat > ~/.bensz-skills/config/remote.env <<'EOF'
OPENAI_BASE_URL=https://<你的>.benszresearch.com/v1
OPENAI_API_KEY=<key>
OPENAI_IMAGE_MODEL=gpt-image-2
# 或 Gemini 路线：GEMINI_BASE_URL / GEMINI_API / GEMINI_MODEL
EOF
chmod 600 ~/.bensz-skills/config/remote.env

# 让 PPT 技能在 Claude Code 里可用
cp -a ~/.codex/skills/image-to-editable-ppt ~/.claude/skills/
```

### 10.1 先算页面余量，再定图数

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir projects/<项目>
pdfinfo projects/<项目>/main.pdf | grep Pages
```

一张 `width=0.8\linewidth` 的图连 caption 约占 **1/3 页**，5 张（背景 + 框架 + 3 条技术路线）≈ **2 页**。

正文上限 30 页。**不要指望"先插图再压"**——NSFC 前三部分是硬结构，`\clearpage` 把页面余量藏起来了，压缩常常一页都省不下来。余量不够就先砍图数或改用 `0.6\linewidth`。

### 10.2 出图（一个会话串行跑完）

```text
1. academic-paper-analyzer-figure-planner  → 读 main.pdf，只出 Figure Plan，不出图
2. academic-figure-color-expert            → 只调一次，锁定一套 hex（含色盲安全校验）
3. academic-figure-prompt                  → 逐图生成 prompt，每个都塞同一份 hex + 同一套字号/线宽
4. auto-draw-plot                          → 出图到 figures/*.png
```

**`color-expert` 只调用一次**，产出的 hex 表全图复用。逐图配色会让 5 张图长得像 5 篇不同的论文。

已经明确知道要哪几张图时，不必用 `academic-figure-workflow-orchestrator`，它那层路由是多余的。

### 10.3 过一遍可编辑 PPT——这步是纠错，不是美化

**AI 生图的中文几乎必然出错**（错字、断字、术语走形）。这才是必须过 PPT 的真正原因。

```text
使用 ~/.claude/skills/image-to-editable-ppt/SKILL.md，
把 projects/<项目>/figures/ 下的 PNG 转成可编辑 PPT
```

在 PPT 里把文字全部改对，然后**直接导出 PDF**。

### 10.4 落地 `figures/`

| 图的情况 | 做法 | 结果 |
|---|---|---|
| 走了 PPT 修字的 | PPT 直接导出 PDF | **矢量**，文字可选中、无锯齿、体积小 |
| 纯示意、无中文、不用改 | 用下面的脚本把 PNG 封装成 PDF | 像素不变，但避免 `xdvipdfmx` 每次编译重新压缩 |

优先走矢量那条。封装脚本在项目根目录跑（同 [图像格式转为PPT格式.md](图像格式转为PPT格式.md)）：

```bash
cd projects/<项目>
mkdir -p .latex-cache/figure-pdf-wrap
pdftex_bin="$(kpsewhich -var-value=SELFAUTOLOC)/pdftex"
for png in figures/*.png; do
  stem="$(basename "${png%.png}")"
  "$pdftex_bin" -interaction=batchmode -halt-on-error \
    -output-directory=.latex-cache/figure-pdf-wrap -jobname="$stem" \
    "\pdfximage{$png}\setbox0=\hbox{\pdfrefximage\pdflastximage}\pdfpagewidth=\wd0\pdfpageheight=\ht0\hoffset=-1in\voffset=-1in\shipout\box0\end"
  cp ".latex-cache/figure-pdf-wrap/$stem.pdf" "figures/$stem.pdf"
done
```

**换了 PNG 就要重新生成同名 PDF**，否则正文里还是旧图。

### 10.5 插入正文 + 收尾

three-part 布局的落点：

| 图 | 落点 |
|---|---|
| 研究背景图 | `extraTex/1.1.立项依据.tex` 现状分析之后 |
| 总体研究框架图 | `extraTex/2.1.研究内容.tex` 「总体技术路线」段落之后 |
| 3 条技术路线图 | 同文件，各自分项技术路线之下 |

模板规范的写法：

```latex
\begin{figure}[!th]
    \begin{center}
        \includegraphics[width=0.8\linewidth]{figures/fig1-framework.pdf}
        \caption{总体研究框架}
        \label{fig:framework}
    \end{center}
\end{figure}
```

正文里用 `图~\ref{fig:framework}` 引用。**插了图不在正文提它**，评审会认为是凑版面。

收尾：

```bash
python packages/bensz-nsfc/scripts/nsfc_project_tool.py build --project-dir projects/<项目>
pdfinfo projects/<项目>/main.pdf | grep Pages   # 对比 10.1 的页数
```

然后重跑 `nsfc-length-aligner`（页数变了，之前的篇幅结论作废）和 `nsfc-qc`。

### 可直接粘贴的 prompt

```text
读取 projects/<项目>/main.pdf。

第一步：用 academic-paper-analyzer-figure-planner 出 Figure Plan，先不要生图。
至少包含：1 张研究背景图、1 张总体研究框架图、3 张技术路线图（三条研究路线各一张）。
同时告诉我当前正文页数和距 30 页上限的余量，以及这些图预计占几页。

第二步：用 academic-figure-color-expert 一次性锁定全套配色，输出 hex 表。
这套配色对全部图生效，不要逐图重新配。

第三步：用 academic-figure-prompt 逐图生成 prompt，每个 prompt 里都写入第二步的 hex，
并统一字号层级与线宽。

第四步：用 auto-draw-plot 出图，存到 projects/<项目>/figures/。

图里中文可能出错，出图后停下等我确认，我要过一遍可编辑 PPT 改字。
```

---

## 两条别忘的硬规则

1. **只要正文里还有 `【待补 …】`，这稿就不能提交。** 阻塞点没消失，只是从"写作时"挪到了"提交前"。
2. **缺口清空前，篇幅结论只能算暂定。** 挖空稿偏短，补完真实项目和论文常多占 1–2 页；这时候信"还有余量"，补完就得回头再压。

## AI 老是问已经给过的信息？

多半是三个原因之一：

1. `docs/workflow_status.yaml` 不存在——没有断点，每次从头跑
2. 事实散在多份文档里没进事实库，或者没标 `已确认`
3. 同一事实在两份文档里说法不一致，AI 只能停下来问

对策：把事实收敛进两层事实库，冲突的当场裁定并写明口径。
