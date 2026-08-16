# 课题二申报书 — 跨境物流智能感知与弱网环境通信技术研发

自治区重点研发科技专项（现代物流领域）**课题二独立申报书**的 LaTeX 工程。
版式复刻自治区科技厅官方 Word 申报书表格，输出 14 页 A4 PDF。

- **申报单位**：新疆边疆宾馆有限责任公司（国有企业牵头）
- **协作单位**：新疆大学、新疆财经大学
- **实施年限**：2027 年 1 月—2029 年 12 月
- **经费**：总投入 510 万元（地方财政 170 万 + 企业自筹 340 万）

> 本工程与 `projects/NSFC_*` 国家自然科学基金产品线无关，不依赖 `bensz-nsfc` 公共包。

---

## 快速开始

### 编译

```bash
xelatex -interaction=nonstopmode -halt-on-error -output-directory=.latex-cache main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=.latex-cache main.tex
cp .latex-cache/main.pdf ./main.pdf
```

两次编译即可（无参考文献，不需要 bibtex）。**不要**使用 `code/nsfc_build.py`，那是 NSFC 产品线脚本。

正常产出：14 页 A4（595.28 × 841.89 pt）。

### 修改内容

**只编辑 [content.tex](content.tex)。** 全部正文由该文件中的 22 个宏定义，例如：

```latex
\newcommand{\PriorWorkContent}{%
申报单位前期任务承担情况……
}
```

宏名与官方表格栏目的对应关系见 [AGENTS.md](AGENTS.md) 第三节。

---

## 文件结构

```
main.tex                    入口（8 行）
application-template.sty    版式定义，勿改
sections/form-pages.tex     官方 14 页固定表格，绝对 bp 坐标，勿改
content.tex                 ★ 唯一需要编辑的文件
docs/                       材料与写作基线
main.pdf                    产出
```

`application-template.sty` 用 tikz 绝对坐标复刻官方表格框线，正文以
`\parbox` 定位在固定坐标上，字号 14.17bp、行距 18.12bp、fandol 字体。
改动版式文件会破坏与官方表格的像素级对齐。

### 遗留文件

`main-nsfc-template.tex.bak`、`extraTex/`、`references/`、`figures/`、`code/`、
`scripts/`、`template/` 是迁移前 NSFC 模板的残留，**已不参与编译**，保留以备回退。

---

## 写作约束（重要）

### 框高才是真正的字数上限

官方表格标注的字数限制**不等于**实际可容纳字数。例如"科研条件支撑状况"标注限 500 字，
但版面框高仅 196bp，约 346 字。所有栏目的实测容量见 [AGENTS.md](AGENTS.md) 第三节。

每个 `\par` 会因末行不满浪费约半行，段落越多有效容量越小。

### 溢出不会报错，必须单独校验

固定框模板中文字溢出**不产生任何 LaTeX 警告**——编译"成功"不代表版面正确。
改完 `content.tex` 后必须执行：

```bash
pdftotext -bbox-layout main.pdf /tmp/bbox.html
```

比对各栏框底坐标与框内文字最大 `yMax`。也可目视抽查：

```bash
pdftoppm -f 10 -l 10 -r 100 -png main.pdf /tmp/chk
```

### 内容红线

- 不虚构专利、软件、论文名称及作者、发明人、权属份额
- 除四项硬指标外不新增数值承诺
- 项目级预期性指标须注明属项目级，不写成课题二单独承诺
- 材料不足的栏目宁可留空，不编造

---

## 当前状态

22 个内容栏全部已填写。已通过校验：**14 页 A4、编译零警告、22/22 栏文字全部在框内**。

详细分析、材料清单和待确认事项见 [docs/00_项目基本信息.md](docs/00_项目基本信息.md)；
待核定事项见 [AGENTS.md](AGENTS.md) 第七节。
