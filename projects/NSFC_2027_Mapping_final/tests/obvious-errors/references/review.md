# 参考文献明显错误检查

检查日期：2026-09-22。只读检查正文、BibTeX 与既有 bbl；没有修改正文、题录、PDF，没有构建。

## 结论

未发现缺失引用键、重复条目或重大题录错配。48 条文献均有正文引用，共 143 处；47 个 DOI 中 46 个通过 Crossref 注册元数据核对题名、作者、年份、卷期与页码，另 1 个中文期刊 DOI 由期刊官方页面核对；无 DOI 的 CLIP 由 PMLR 官方题录核对。Crossref 对两条中文文献返回英文姓名或英文题名，已用期刊官方页面核对，不属于正文题录错误。

## 确定的小问题

- **SCAN 的会议论文集名误用丛书名**（确定性：高；严重度：低）。`references/myexample.bib:334` 的 `booktitle` 仅为 `Lecture Notes in Computer Science`。该字段应填写具体论文集 `Computer Vision – ECCV 2018`；LNCS 是系列名。Springer 官方还列出卷 11208、出版者 Springer、出版地 Cham。当前 `.latex-cache/main.bbl:121` 确实只排出了丛书名，读者无法直接从参考文献看出 ECCV 2018。证据：[Springer 官方题录](https://link.springer.com/chapter/10.1007/978-3-030-01225-0_13)。此问题不影响正文对 SCAN 堆叠交叉注意力的描述，也不构成假文献。

## 重要的未核验边界

- **ESRN 的方法重叠仍未完成全文核验**：`extraTex/proposal.tex:330`、`:365` 已明示此边界。DOI 题名、作者、页码已通过 Crossref 核对；ACM 正文访问仍返回 403。不能据此判断文献不存在，也不能声称已排除与本项目三态设计的方法重叠。来源：[ACM 出版页](https://dl.acm.org/doi/10.1145/3731715.3733434)、[Crossref 注册元数据](https://api.crossref.org/works/10.1145/3731715.3733434)。这是原文已承认的查新待办，不是本轮发现的事实错误。
- 本轮是明显错误筛查和题录核对，没有逐篇重新阅读全部 48 篇全文。

## 补充的官方证据

- `wuhui2026rsitr`：Crossref 返回 404，但期刊官网存在对应文献，题名、六名作者与 DOI 一致；英文页列出收稿 2026-02-13、录用 2026-04-09、在线出版 2026-04-28，支持当前年份 2026。中文导航出现的 2025 不足以推翻这些明确日期。[期刊英文页](https://jeit.ac.cn/en/article/doi/10.11999/JEIT260189)、[期刊中文页](https://jeit.ac.cn/cn/article/doi/10.11999/JEIT260189?viewType=HTML)。本轮通过网页搜索返回的官方页面内容读取；直接打开受 403 限制。
- `radford2021clip`：题名、作者、2021、卷 139、8748–8763、PMLR 一致，官方 BibTeX 没有 DOI 字段。[PMLR 官方题录](https://proceedings.mlr.press/v139/radford21a.html)。
- `lishutao2025alignment`：[遥感学报官方页面](https://www.ygxb.ac.cn/cn/article/doi/10.11834/jrs.20254457)，29(6):1551–1565，2025。
- `zhengxiangtao2025crossmodal`：[遥感学报官方页面](https://www.ygxb.ac.cn/en/article/doi/10.11834/jrs.20255125/)，29(6):1566–1586，2025；官方引文同时提供中文题名与中文作者。
- `cglsa2026`：[MDPI 官方页面](https://www.mdpi.com/2072-4292/18/14/2335)，2026-07-13 出版，18(14):2335，题名与两名作者一致。
- `pmpguard2026`：[AAAI 官方页面](https://ojs.aaai.org/index.php/AAAI/article/view/37767)，2026-03-14 出版，40(10):8197–8205，题名与四名作者一致。

机器可读证据见 `crossref-evidence.json`；初次限流响应保存在成功重试条目的 `first_attempt`，未将限流/404 自动判为假文献。
