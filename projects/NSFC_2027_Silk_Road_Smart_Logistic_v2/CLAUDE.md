# 自治区重点研发专项 课题二申报书 - Claude Code 适配

## 核心指令

@./AGENTS.md

---

## Claude Code 特定说明

### 文件引用规范

在 Claude Code 中引用文件时，使用 markdown 链接语法：

- **文件**：`[content.tex](content.tex)`
- **特定行**：`[content.tex:70](content.tex#L70)`
- **行范围**：`[content.tex:70-95](content.tex#L70-L95)`

### 任务管理

- 多栏目写作任务使用 TodoWrite 工具跟踪进度
- 完成每个栏目后及时标记 completed

### 推荐工作流

1. 先读 `docs/00_项目基本信息.md` 了解项目身份、材料与待确认事项；
   选题、术语、研究边界与查新缺口见 `docs/01_选题与研究主题.md`
2. 用户提出写作需求 → 用 `Read` 读取 `content.tex`，定位对应的内容宏
3. 查 AGENTS.md 第三节确认该栏目的**框高容量**（不是官方标注字数）；
   若改动涉及研究内容，先查第一节的 3 项结构与强关联纽带约束
4. 只修改 `content.tex`；不得改动 `sections/form-pages.tex` 与 `application-template.sty`
5. 编译两次 xelatex，然后**必做溢出校验**——固定框溢出不报警告，编译成功不代表版面正确；
   且**坐标法单用会漏报**，须与尾句存在性检查并用（见下）

### 溢出校验命令

两项检查缺一不可。只跑坐标法会漏掉"内容被静默丢弃"这一最严重的情况：

```bash
pdftotext -bbox-layout main.pdf /tmp/bbox.html   # ① 比对框底坐标与文字 yMax
pdftoppm -f 10 -l 10 -r 100 -png main.pdf /tmp/chk   # ③ 目视抽查
```

② 尾句存在性检查：取每个宏正文**末 10 字符**，确认其出现在 `pdftotext main.pdf -` 的输出中。
缺失即为内容丢失（必修）；存在但越过框底则仅为出框（内容完整，可按需修）。
用 `Bash` 跑一段 Python 一次性遍历 22 个宏，比逐栏目视快得多。

### 注意

- 本项目**不是**国家自然科学基金，`nsfc-*` 系列 skill 的整章生成能力大多不适用，
  且带国自然文体预设；可用的是 `nsfc-length-aligner`、`nsfc-humanization`、`nsfc-qc`
- 不要使用 `code/nsfc_build.py` 编译
- `docs/8.9课题二申报书-合并-v6.docx` 是 0 字节空文件，勿引用

### 默认语言

始终用**简体中文**与用户交流并撰写申报书内容。
