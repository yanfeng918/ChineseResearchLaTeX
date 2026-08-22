# 引用核验建议（手动补齐 BibTeX）

说明：本工具不会自动联网补齐引用，但会生成一段“可直接复制”的提示词，帮助你（或任意 BibTeX 工具/助手）完成核验与补齐。


## DOI 缺失的条目（.bib 有该 key，但缺 doi 字段，建议补齐以便可核验）

- geifman2017selective
- guo2017calibration
- rubanova2019latentode

## 可直接复制的提示词（用于核验与补齐）
```
请帮我核验并补齐参考文献条目：
目标项目：.
任务：核验并补齐参考文献条目，确保不出现幻觉引用。
需要补 DOI 的 bibkey：
geifman2017selective, guo2017calibration, rubanova2019latentode
说明：这些 key 在 .bib 存在，但缺 doi 字段；请在不杜撰的前提下补齐 doi（如无法确定，请明确提示需要我提供 DOI/链接）。
输出：更新项目 references/*.bib（或你认为合适的 .bib），并给出每条的题目/作者/年份/期刊/DOI 核验结果；无法核验的条目请标注“待核验”。
```
