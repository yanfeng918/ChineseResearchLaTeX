# 文字阶段衔接

00–07 的科学写作细则复用 [原版 stages-00-07.md](../../nsfc-full-pipeline/references/stages-00-07.md)；08–13 复用 [原版 stages-08-14.md](../../nsfc-full-pipeline/references/stages-08-14.md) 中的检查、评审与修复部分。执行到相应阶段时完整读取对应文档。

这些文档只提供章节职责和事实标准。本技能的主 SKILL 与以下差异决定执行方式：

- 所有状态操作都调用本技能 `scripts/pipeline_state.py`；不调用原版状态 CLI，不写原版断点。
- 原版“配图不覆盖”“14 编译后最终汇报”等边界在此不生效；14 是文字稿基线，完成后自动绘图。
- 09 的篇幅结论在插图前为文字阶段结论，21 必须对插图后实际版面复核。
- 14 使用本技能 `build --phase text` 调用仓库官方构建器；它额外保存 `docs/figure_source/main.text.pdf` 和构建指纹。
- 事实 ID 与暂定项按原规则保护。补齐事实后使用本技能 `scan` 和 `reconcile`；扫描器从本技能断点读取事实源，递归检查真正加载的正文。
- 合法硬事实缺口不阻止背景、框架和已确定路线出图；图内依赖缺失事实时在图件清单的 `gap_ids` 中登记，避免被 PNG 隐藏。

stage 00 由 AI 从真实文件判断项目类别、布局与篇幅，用 `project --from-json` 登记以下结构（路径示例必须替换为当前活动正文）：

```json
{
  "type": "NSFC_General",
  "grant_type": "面上项目",
  "layout": "three-part",
  "length_budget": "以本项目 AGENTS.md 为准，全文不超过30页",
  "body_files": {
    "part_one": ["extraTex/1.1.立项依据.tex", "extraTex/2.1.研究内容.tex", "extraTex/2.2.特色与创新.tex", "extraTex/2.3.年度研究计划.tex"],
    "foundation": ["extraTex/3.1.研究基础.tex", "extraTex/3.2.工作条件.tex", "extraTex/3.3.承担项目情况.tex", "extraTex/3.4.完成国基项目情况.tex"],
    "statements": ["extraTex/4.1.不同类型国基情况.tex", "extraTex/4.2.同年单位不一致.tex", "extraTex/4.3.承担中单位不一致.tex", "extraTex/4.4.不同专业技术职务的申请.tex", "extraTex/4.6.其他.tex"]
  },
  "project_fact_file": "docs/00_项目事实库.md"
}
```

申请人共用事实文件可通过 `applicant_profile_file` 指定项目外只读文件。不要把整个用户目录当作事实源。角色映射必须覆盖活动正文，文件不能重复或越界；动态宏加载无法确定时先解决解析问题。
