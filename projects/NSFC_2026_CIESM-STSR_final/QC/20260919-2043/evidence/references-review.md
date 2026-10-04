# 参考文献只读核验（2026-09-19）

实际入口为 `references/myexample.bib`；从当前 `.latex-cache/main.aux` 提取 29 个不同引用 key，与 29 条 bib 记录逐一对应。未发现缺 key 或未引用条目。

## 确证问题

1. **Hao2015Oasis 年卷不匹配（P2）**：`references/myexample.bib:286` 使用 2015，但著录卷期页为 8(2):172–183。正式卷期为 2016 年 4 月，出版社建议引文也使用 2016；2015-12-09 是在线先发日期。应统一为 2016, 8(2):172–183，引用 key 可保持不变。[出版社页面](https://link.springer.com/article/10.1007/s40333-015-0060-x)。
2. **Bischoff2024Unpaired 卷期、文章号缺失（P2）**：`references/myexample.bib:113` 只保留刊名、年、DOI。正式记录可补为 *Artificial Intelligence for the Earth Systems*, 2024, **3(2):e230039**。[作者机构保存的正式期刊 PDF](https://clima.caltech.edu/wp-content/uploads/2024/06/aies-AIES-D-23-0039.1.pdf)、[期刊条目](https://journals.ametsoc.org/view/journals/aies/3/2/AIES-D-23-0039.1.xml)。Crossref 自身遗漏卷期，已用 PDF 与目录补证。

## 核验覆盖

- 27/29 条成功读取 Crossref DOI 注册元数据，核对标题、作者、期刊/会议、年卷期页或文章号；除上述日期口径外，已填字段经归一后未发现错配。DeepSD 的 Crossref 把副标题单独存储，合并后与 bib 一致，不是标题错误。
- `Hersbach2020ERA5` 与 `Geiss2022` 的 Crossref 接口遭遇 HTTP 429，改用[Wiley 官网](https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.3803)与[GMD 官网](https://gmd.copernicus.org/articles/15/6677/2022/)核对基本元数据。ERA5 核对主要作者及年卷期页，未自动逐名核对完整作者序列；Geiss 三位作者已完整核对。
- `Pretrain2026` 确有正式出版记录：2026-07-01，*Geoscientific Model Development*, 19(12):5781–5804，DOI `10.5194/gmd-19-5781-2026`。当前题名、作者、年卷期页一致。[期刊官网](https://gmd.copernicus.org/articles/19/5781/2026/index.html)。
- 本轮未发现假 DOI、DOI 对应另一篇文章、错误题名或实际卷页错配。上述结论属于元数据核查，不等同于已核对所有引文的科学论据。

仅新增本核验目录中的证据文件，未修改申请书 tex/bib/PDF。原始 Crossref 记录见 `references-crossref.json`；逐条检查与发现见 `references-review.json`。
