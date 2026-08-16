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

1. 先读 `docs/00_项目基本信息.md` 了解项目身份、材料与待确认事项
2. 用户提出写作需求 → 用 `Read` 读取 `content.tex`，定位对应的内容宏
3. 查 AGENTS.md 第三节确认该栏目的**框高容量**（不是官方标注字数）
4. 只修改 `content.tex`；不得改动 `sections/form-pages.tex` 与 `application-template.sty`
5. 编译两次 xelatex，然后**必做溢出校验**——固定框溢出不报警告，编译成功不代表版面正确

### 溢出校验命令

```bash
pdftotext -bbox-layout main.pdf /tmp/bbox.html   # 比对框底坐标与文字 yMax
pdftoppm -f 10 -l 10 -r 100 -png main.pdf /tmp/chk   # 目视抽查
```

### 注意

- 本项目**不是**国家自然科学基金，`nsfc-*` 系列 skill 的整章生成能力大多不适用，
  且带国自然文体预设；可用的是 `nsfc-length-aligner`、`nsfc-humanization`、`nsfc-qc`
- 不要使用 `code/nsfc_build.py` 编译
- `docs/8.9课题二申报书-合并-v6.docx` 是 0 字节空文件，勿引用

### 默认语言

始终用**简体中文**与用户交流并撰写申报书内容。
