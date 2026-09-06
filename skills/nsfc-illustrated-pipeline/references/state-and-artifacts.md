# 状态与产物契约

脚本为 `skills/nsfc-illustrated-pipeline/scripts/pipeline_state.py`。所有命令均以 `--project-dir <项目目录>` 指定同一项目；完整参数通过 `--help` 查看。运行前加载本技能 config，状态文件与图件文件名由配置确定。

## 命令

| 命令 | 用途 |
|---|---|
| `migrate [--apply]` | 初始化新断点，只读导入原版文字进度；默认预览 |
| `project --from-json <文件>` | 登记 AI 从真实正文确定的布局和事实文件 |
| `drawing-rules --file <文件>` | 保存用户绘图规则路径 |
| `reconcile [--apply]` / `next` | 校准真实产物，获取下一阶段 |
| `begin --stage <ID>` / `finish --stage <ID>` | 开始/验收阶段；新绘图阶段按顺序执行 |
| `fail --stage <ID> --reason <原因>` | 如实登记阶段失败 |
| `image-start --figure F01 [--prompt <文件>]` | 登记串行调用、实际 prompt 和本次输入 |
| `image-record --figure F01 --call-id <实际ID> --evidence <文件>` | 核验新 PNG，绑定一次独立调用 |
| `image-fail --reason <原因>` | 结束已确认失败的图像调用 |
| `image-reset --figure F01 --reason <已修复根因>` | 保留历史后允许额外尝试，不重置进行中的调用 |
| `deck-record --evidence <文件>` | 结构检查并登记当前 PPT 与 PNG 来源 |
| `export-pdf` | 从当前 PPT 导出各图 PDF |
| `insert [--apply]` | 预览或幂等插入图题、图片和正文引用 |
| `build --phase text` / `build --phase final` | 官方构建、基线保存、最终输入/PDF 指纹 |
| `scan` / `readiness` | 事实缺口和四级就绪度 |
| `submission --item <项> --status <状态> --reason <证据>` | 登记独立申请书组件状态 |

状态 schema 3 使用独立文件 `docs/illustrated_workflow_status.yaml`，包含旧 00–14、新 15–22、逐图调用与验收、构建和提交清单。只读导入记录来源哈希；不修改原版 `docs/workflow_status.yaml`，不把本技能断点传给原版迁移脚本。

状态只通过上述入口原子写回。AI 可以写科学内容、图件清单、prompt 和真实验收报告，但不能直接写阶段状态/调用记录。中断后的 `in_progress` 保留为进行中，核实工具结果后显式记录或恢复；文件非空不等于实际调用完成。

## 图件清单

`docs/figure_manifest.json` 的顶层字段为 `route_ids` 和 `figures`。以下展示一个入选条目的字段；实际清单必须包含背景、框架和每条路线，不能直接将单条示例当完整清单：

```json
{
  "route_ids": ["R1", "R2", "R3"],
  "figures": [
    {
      "id": "F01", "kind": "background", "required": true, "selected": true,
      "source_file": "extraTex/1.1.立项依据.tex",
      "source_excerpt": "从当前正文复制的一段科学内容，必须真实命中原文。",
      "anchor": "从当前正文复制的唯一完整段落，图插在该段落后。",
      "spec": "docs/figure_specs/F01.json", "prompt": "docs/figure_specs/F01.prompt.md",
      "png": "figures/F01-background.png", "pdf": "figures/F01-background.pdf",
      "caption": "研究背景与关键科学问题", "label": "fig:background", "width": 0.9,
      "gap_ids": []
    }
  ]
}
```

`kind` 核心类型是 `background`、`framework`、`route`；路线条目加 `route_id` 对应真实路线；可选示意图用 `optional`。未入选条目有 `id`、`selected:false`、`required:false`、`reason` 即可。每个入选条目有独立 prompt/spec/png/pdf 路径，caption 为普通中文文本，由脚本转义成安全 LaTeX。

`source_excerpt` 和 `anchor` 必须命中受管插图之外的当前正文。正文变化时按科学含义复核，不为了通过脚本而只更新原文片段。图件输入指纹绑定来源片段、prompt、spec、配色与 gap_ids；只改插入宽度、caption、最终 PDF 不会强制重新 imagegen。

## 验收证据

JSON 证据由实际检查后生成，建议放在 `review/figures/`。布尔值必须是 JSON 的 `true/false`，缺项或检查未通过不能填 true。脚本核验格式和文件指纹，真实性由执行者对实际图件检查负责。

PNG 证据：

```json
{"passed": true, "checks": {"chinese": true, "direction": true, "hierarchy": true, "crop": true, "source_consistency": true}, "notes": "记录实际检查结果及修正内容"}
```

PPT 汇总证据：

```json
{"passed": true, "checks": {"editable_objects": true, "text_fidelity": true, "page_mapping": true, "editppt_validation": true}, "notes": "记录 editppt 工作区、各页 validation 与最终 finalize 的真实结果"}
```

图文联合证据固定为 `review/图文联合检查证据.json`：

```json
{
  "passed": true,
  "checks": {"page_limit": true, "legibility": true, "no_crop": true, "references": true, "source_consistency": true, "qc": true},
  "input_sha256": "本次 build --phase final 返回的 input",
  "pdf_sha256": "本次 build --phase final 返回的 output",
  "figure_pages": {"F01": [2], "F02": [4], "F03": [5], "F04": [6], "F05": [7]},
  "notes": "记录实际版面、warning、暂定项和未解决问题"
}
```

页码从 1 开始，必须逐图查看，不可照抄示例。有科学或版面问题时 checks 对应项为 false，先修复再验收。合法待补事实不假装已经补齐；最终就绪度还检查正文缺口和图件 gap_ids。

## 变更与恢复

- 文字指纹排除完整受管插图块；原文、项目规则或事实源变化会使相关文字阶段失效。
- 插图基线 PDF 保存在 `docs/figure_source/`；最终 `main.pdf` 独立更新，插图不会反复触发基线变化。
- PNG 内容或 prompt/spec 改变使该图的 image 验收失效；其他图仍可复用。
- PPT 修改需要重新 `deck-record` 和导出 PDF；不需要重新生成 PNG。
- 未登记或被用户替换的同名 PDF 不覆盖。已登记的本技能产物更新前保存备份。
- 受管块重复、锚点不唯一、目标为孤儿文件或路径越界时拒绝写入，不猜测应删除哪段正文。
- 最终构建指纹包括递归 TeX、引用图片、BibTeX；有 recorder 文件时额外包括其中真实读入的包、字体资源。宏计算图像路径等静态解析不支持的布局需先由执行者明确解析，不能把这种项目误报为已就绪。

正式产物在项目 docs/review/figures/extraTex。任务工作区从断点 `run.workspace` 获取；LaTeX 中间文件隔离在 `.latex-cache/`。本技能脚本不是无需 AI 的全自动生图程序，它负责让宿主 AI 的执行和交付可核查、可恢复。
