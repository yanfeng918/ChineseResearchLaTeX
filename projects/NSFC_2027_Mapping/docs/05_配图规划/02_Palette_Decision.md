---
document: "视觉逻辑与配色决策 Palette Decision"
stage: "05_figure_plan"
project: "NSFC_2027_Mapping"
skill: "academic-figure-color-expert v1.3.2"
input: "01_Figure_Plan.md 第八节 Palette Handoff"
version: "2026-09-06"
---

# Palette Decision — NSFC 2027 遥感图文检索项目全篇配图

## 一、决策清单（Decision Checklist）

| # | 项 | 结论 |
|---|---|---|
| 1 | Style family | **classic academic**（白底 + 彩色边框 + 扁平矢量）→ 使用 `academic-figure-prompt` |
| 2 | 硬约束是否触发 | **触发 2 条**：①总体框架 ≥4 模块（module_count_framework = 6）②色盲安全未指定即按需要处理；另有项目特有约束——NSFC 评审常灰度打印，需线型/纹理双编码 |
| 3 | 图类型偏好 | Overall Framework（≥4 模块）→ Nature Blue；Module Detail → Blue Monochrome（同蓝色相，可并入 Nature Blue 梯度）；Comparison → 需 1 个强调色 |
| 4 | Venue / domain 偏好 | venue = None（NSFC 申请书，非会议期刊）；domain = 遥感 + 跨模态检索。无 venue 时按 domain + 模块数落到 Nature Blue |
| 5 | Primary / Alternate | **primary: Nature Blue（+ Okabe-Ito 双色语义强调轴）**；**alternate: Okabe-Ito 全色**；纯黑白印刷退路：Print-Safe Gray |
| 6 | Hex 来源 | `academic-figure-color-expert/references/palettes.md` 第 12 号 Nature Blue + 第 1 号 Okabe-Ito |
| 7 | 决策分支 | **scene**（无用户指定配色，无 venue，按硬约束 + 图类型 + 领域推导） |

## 二、推荐方案：Nature Blue 结构色 + Okabe-Ito 三态强调色

**为什么不是纯单色系**：本项目全篇的信息骨架是"三态"（已支持 / 明确冲突 / 未知）。三态是**类别语义**，单色系只能靠明度区分，灰度打印后三态会糊成一片——而三态恰恰是评审必须一眼看懂的东西。因此采用"**结构单色 + 语义三色**"的混合策略：所有流程/模块/容器走 Nature Blue 单色梯度保持克制，**唯一的彩色预算留给三态**。

**为什么不是 Okabe-Ito 全色**：总体框架图 6 个模块，全色会让"哪个颜色重要"失去信号。把蓝色压成结构底噪，绿/橙只在三态处出现，读者的注意力自动落到本项目的核心主张上。

色相计数：蓝（结构，1 个色相族）+ 绿（已支持）+ 橙（明确冲突）= **3 chromatics**，灰蓝（未知）计为 neutral。符合"≤3 彩色 + 中性色"硬规则。

### 主色板 hex

| 角色 | hex | 用途 |
|---|---|---|
| structure_primary | `#1B3A5C` | 顶层容器、科学问题横幅、骨干编码器边框 |
| structure_secondary | `#2E6B9E` | 数据/输入块、二级模块边框 |
| structure_tertiary | `#5BA0D0` | 子项、内部分隔、次要标注 |
| structure_gray | `#8EAEC4` | 未知态、被弱化元素 |
| accent_supported | `#009E73` | **三态-已支持**（Okabe-Ito 绿） |
| accent_conflict | `#D95F02` | **三态-明确冲突**（Okabe-Ito 橙 / Semantic Binding 的 Loss 色） |
| text | `#333333` | 全部正文与标签 |
| fill | `#FFFFFF` | 所有模块填充（无例外） |
| section_bg | `#F7F7F7` | 一级分组面板底 |
| panel_bg_alt | `#F2F6FA` | 二级分组面板底（淡蓝，用于骨干区/评测区区隔） |
| border_neutral | `#CCCCCC` | 无语义的辅助框 |
| arrow | `#4D4D4D` | 前向数据流、监督流 |

### 备选方案（Alternate）

**Okabe-Ito 全色**：`#0072B2` / `#E69F00` / `#009E73` + `#333333` / `#F7F7F7` / `#CCCCCC` / `#4D4D4D`。
适用场景：若最终只做 F2 + F4 两张图（模块数降到 ≤3 层级），或申请人希望图更明快。代价是 6 模块框架图会显得花。

**Print-Safe Gray**：`#000000` / `#333333` / `#666666`。
仅在确认申请书走严格黑白印刷、且愿意完全靠线型 + 纹理区分三态时使用。

## 三、语义色绑定契约（Semantic Color Binding — 12 张图强制统一）

**这是本次配色的核心产物。** 同一角色在 F1—F12 中必须同色同线型，评审看第 3 张图时不需要重新学一遍图例。

| 功能角色 | 边框 hex | 线型 / 纹理 | 出现图 |
|---|---|---|---|
| 数据 / 输入（影像、描述、公开基准） | `#2E6B9E` | 1.5pt 实线，圆角 6px | F1 F2 F4 F5 F6 F7 |
| 骨干 / 预训练编码器（CLIP、RemoteCLIP）**冻结** | `#1B3A5C` | **1.5pt 虚线** + `[Fixed]` 灰色 pill | F6 |
| 适配器 / 可训练部分（PEFT） | `#1B3A5C` | **1.5pt 实线** + `[Tune]` 蓝色 pill | F6 |
| 三态-**已支持** supported | `#009E73` | 1.5pt 实线，无填充纹理 | F2 F4 F5 F6 F8 |
| 三态-**明确冲突** conflicting | `#D95F02` | 1.5pt 实线 + 内部 45° 细斜纹 | F2 F4 F5 F6 F8 |
| 三态-**未知** unknown | `#8EAEC4` | **1.5pt 虚线** + 内部点阵填充 | F2 F4 F5 F6 F8 |
| 前向数据流 | `#4D4D4D` | 1.5pt 实线箭头，4px 箭头 | 全部 |
| 监督 / 约束施加 constrain | `#4D4D4D` | 1.5pt 实线箭头 + 文字标签 `施加约束` | F6 |
| 监督屏蔽 masked | `#8EAEC4` | 1.5pt 虚线箭头，**中段一道短斜杠断开** + 文字标签 `屏蔽监督` | F2 F6 |
| 反馈 / 回流 | `#4D4D4D` | 1.0pt 虚线弧形箭头 + 标签 `错误归因回流` | F4 F7 |
| 本项目主张 | `#009E73` | **2.5pt 加粗实线** + `本项目` 绿色 pill | F2 F3 F6 F9 F11 |
| 已有工作 / 对照基线 | `#CCCCCC` | 1.0pt 实线，文字 `#666666` | F3 F6 F9 |
| 边界 / 诚实声明 | `#8EAEC4` | 1.0pt 虚线框，文字 `#666666` 7pt | F1 F3 F9 F12 |
| 决策节点 | `#1B3A5C` | 菱形，1.5pt 实线 | F10 F11 |
| 里程碑 | `#2E6B9E` | 实心小菱形 ◇ | F10 |

**双编码保证**：三态的每一态都同时由 **色相 + 线型 + 填充纹理** 三重编码。绿=实线无纹理、橙=实线斜纹、灰=虚线点阵。红绿色盲、灰度打印、低分辨率缩略图三种条件下都能区分。

## 四、视觉逻辑（Visual Grammar — 12 张图统一）

配色只解决"用什么颜色"，视觉逻辑解决"读者的眼睛按什么顺序走"。以下六条语法全篇统一。

### 1. 空间语法（方向即语义）
- **左 → 右**：主流程 / 时间推进 / 数据流转。F1 F3 F4 F5 F6 F7 F10 F11 一律左起右止。
- **上 → 下**：抽象层级下降（问题 → 目标 → 内容 → 交付物）。F4 是唯一的四层纵向结构。
- **底部弧线右 → 左**：反馈回流。虚线，走图形最下方，绝不与前向流交叉。
- **右上角**：本项目主张的落位（F9 象限图、F6 臂 c、F2 三态框）。评审的视觉终点固定在这里。

### 2. 层级语法（三级，不做四级）
```
一级：分组面板    #F7F7F7 或 #F2F6FA 淡底 + 1.0pt 同色系深边  ← 只标区域名
二级：模块块      白底 + 1.5pt 语义色边 + 图标 + ≤5 字标题
三级：子项        无边框，纯文字 8pt + 小圆点，或 pill 标签
```
禁止"框中框中框"。需要第四层时改用面板底色分组，不再套框。

### 3. 强调语法（唯一强调轴）
全篇只有一个强调机制：**2.5pt 加粗绿边 + `本项目` pill**。
- 不用阴影、不用发光、不用大字号、不用背景色块做强调。
- 每张图的加粗元素**至多一个**。多了就没有强调。
- 对照/基线一律 1.0pt 灰边 + `#666666` 文字，主动"退后"。

### 4. 图标语法
- 每个二级模块必须有一个视觉锚点，**单色线稿**，用该模块的边框色，16–24px 等效。
- 遥感影像 → `三张叠放的图幅框 + 对角线` ｜ 文本描述 → `三条文本线的文档图标` ｜ 关系三元组 → `两个圆点 + 一条带方向的连线` ｜ 编码器 → `堆叠横条 + 右侧残差弧` ｜ 适配器 → `小方块嵌在大方块角上` ｜ 评测 → `带刻度的量表` ｜ 人工核验 → `双人剪影 + 对勾` ｜ 去重 → `两个重叠圆（韦恩）` ｜ 统计效力 → `小正态曲线`。
- **禁止**：emoji、锁头、火焰、闪电、3D 立体、渐变、彩色填充图标。

### 5. 文字语法
- 模块标题 ≤ 5 字 ｜ 子项 ≤ 3 字 ｜ 箭头标签 ≤ 3 字 ｜ 图上公式至多 1 行核心式。
- 【暂定 …】标记**必须原样出现在图上**，与正文措辞一致——这是本标书的诚实性设计，图上抹掉会造成图文不一致。
- 边界声明用 7pt `#666666`，放图底，不与主流程争夺注意力，但必须存在（F1 F3 F9 F12）。
- 长公式、参数、文献编号 → 一律进 figure caption，不上图。

### 6. 留白语法
- 白底占画布 ≥ 70%。
- 模块间距 ≥ 模块高度的 25%；面板内边距 ≥ 12px 等效。
- 宁可少画一个子项，也不把模块塞满——评审在 A4 上看到的是缩小版。

## 五、无障碍与印刷（Accessibility）

| 检查项 | 结论 |
|---|---|
| 色盲安全 | **是**。`#009E73`（绿）与 `#D95F02`（橙）为 Okabe-Ito 标准安全对，红绿色盲下明度差显著；蓝色族与两者色相距离足够 |
| 灰度打印 | **是**。三态额外由线型（实线/实线+斜纹/虚线）与填充纹理（无/45°斜纹/点阵）区分，去色后仍可判读 |
| 文字对比度 | `#333333` on `#FFFFFF` = 12.6:1 ✅；`#666666` on `#FFFFFF` = 5.7:1 ✅（7pt 边界小字仍达 AA） |
| 彩色文字 | **禁止**。`#D95F02` on white ≈ 3.9:1，未达正文 AA 标准 → 橙色只用于边框与纹理，不用于任何文字 |
| 缩略图可读 | 模块标题 ≤5 字 + 每块一个图标 → A4 半栏缩放后仍可辨模块角色 |
| 单色打印退路 | 若确认纯黑白，切换 Print-Safe Gray，三态改为：实线粗 / 实线细+斜纹 / 虚线+点阵 |

## 六、逐图配色分配

| 图号 | 主结构色 | 出现的语义强调 | 彩色数 | 备注 |
|---|---|---|---|---|
| F1 | `#2E6B9E` + `#5BA0D0` | 仅结局框用 `#D95F02`（"没说"被当成"没有"） | 2 | 背景图不引入三态全色，留悬念给 F2 |
| F2 | `#2E6B9E` | 三态全色（绿/橙/灰）+ `本项目` 绿 pill | 3 | 全篇三态首次亮相，图例必须完整 |
| F3 | `#1B3A5C` 泳道 + `#CCCCCC` 已有工作 | 切入点框 `#009E73` 2.5pt | 2 | 已有工作主动退为灰色 |
| F4 | `#1B3A5C` / `#2E6B9E` / `#5BA0D0` 三级 | 三态标签色点 + 回流虚线 | 3 | 6 模块，靠蓝色梯度分层而非多色 |
| F5 | `#2E6B9E` 主链 | 三态判定框全色 + 硬隔离粗竖线 `#1B3A5C` | 3 | 硬隔离线是本图第二视觉重心 |
| F6 | `#1B3A5C` 骨干（虚线冻结） | 臂 (b) `#D95F02`、臂 (c) `#009E73` 2.5pt、masked 灰虚线 | 3 | 全篇最重要的一张，强调唯一落在臂 (c) |
| F7 | `#2E6B9E` 五维度 | 去重闸口 `#D95F02`、正向出口 `#009E73` | 3 | 五个并列 panel 用同色，靠图标区分 |
| F8 | `#1B3A5C` 中央卡片 | 三证据源用 `#2E6B9E`；三态输出全色；约束框 `#D95F02` 加粗 | 3 | "避免循环论证"的约束框是重点 |
| F9 | 坐标轴 `#4D4D4D`，已有工作 `#CCCCCC`/`#2E6B9E` | 本项目 `#009E73` 2.5pt 落右上 | 2 | 灰色点越多，绿色点越突出 |
| F10 | `#2E6B9E` 任务条 + `#5BA0D0` 次要条 | H1 决策菱形 `#D95F02`，成立/证伪双出边（绿/橙） | 3 | 决策节点是本图唯一强调 |
| F11 | `#1B3A5C` 假说列 | 证伪判据 `#D95F02`，降级路径 `#8EAEC4`，出口框 `#009E73` 2.5pt | 3 | 三行同构，靠列位置而非颜色区分 |
| F12 | `#2E6B9E` 左列 + `#5BA0D0` 右列 | 无强调色；边界条 `#8EAEC4` 虚线 | 1 | 克制处理，避免"炫耀基础"观感 |

## 七、Handoff（交给 academic-figure-prompt）

```
palette: Nature Blue (structure) + Okabe-Ito accents (three-state semantics)
family: classic
primary:    #1B3A5C
secondary:  #2E6B9E
tertiary:   #5BA0D0
gray:       #8EAEC4
accent_supported:  #009E73
accent_conflict:   #D95F02
text:        #333333
fill:        #FFFFFF
section_bg:  #F7F7F7
panel_bg_alt:#F2F6FA
border:      #CCCCCC
arrow:       #4D4D4D
semantic_binding:
  data_input        -> #2E6B9E solid
  backbone_frozen   -> #1B3A5C dashed + [Fixed] pill
  adapter_trainable -> #1B3A5C solid + [Tune] pill
  state_supported   -> #009E73 solid, no hatch
  state_conflict    -> #D95F02 solid + 45-degree hatch
  state_unknown     -> #8EAEC4 dashed + dot fill
  supervision_apply -> #4D4D4D solid arrow
  supervision_mask  -> #8EAEC4 dashed arrow, slashed mid-segment
  feedback_loop     -> #4D4D4D dashed curved arrow
  ours_highlight    -> #009E73 2.5pt bold + "本项目" pill
  baseline_recede   -> #CCCCCC 1.0pt, text #666666
reason: 无 venue；framework 模块数 6（≥4）触发单色规则 → Nature Blue 作结构底色；
        三态是全篇唯一类别语义轴，需灰度可分 → 仅此处启用 Okabe-Ito 绿/橙两个安全色
accessibility: colorblind-safe（Okabe-Ito 安全对）+ 线型/纹理双编码（灰度打印可判读）；
        橙色禁用于文字（对比度 3.9:1 未达 AA）
alternate: Okabe-Ito 全色（图少于 3 张时）；Print-Safe Gray（确认纯黑白印刷时）
```

## 八、Stop

Palette Decision 交付完毕，含语义绑定契约与六条视觉语法。下一步见 `03_Figure_Prompts.md`。
