# Palette Decision — NSFC 2026 Education 申请书配图（F1–F7 完整版）

## 决策清单（Decision Checklist）

| # | 项 | 结论 |
|---|---|---|
| 1 | Style family | **classic**（盒线风格）→ 用 `academic-figure-prompt` |
| 2 | 命中的硬约束 | ✅ 色盲安全（显式要求）· ✅ **≥4 模块**（framework 5 阶段）· ⚠️ 灰度可分（非"仅黑白"，故不降级为 Print-Safe Gray） |
| 3 | 图类型偏好 | Framework≥4→Nature Blue；Module Detail→Blue Monochrome；Comparison→Purple-Green（**本项目统一覆盖，见下**） |
| 4 | Venue / Domain | venue = None（中文标书）；domain = AI4Education × 新能源工程教育 → 无强制偏好，由模块数规则接管 |
| 5 | Primary / Alternate | **Nature Blue**（主） / **Blue Monochrome**（备） |
| 6 | Hex 来源 | `references/palettes.md` §12 Nature Blue + Semantic Color Binding Contract |
| 7 | 分支 | **scene**（≥4 模块硬约束触发单色规则） |

## 推荐配色：Nature Blue + 2 语义强调色

**一句话理由**：框架 5 模块触发"≥4 模块用单色"硬规则；单一蓝色明度阶梯在去色后仍按明度分离，是"黑白打印可分"这一硬约束下最稳的结构色；再以 2 个色盲安全强调色承载通过/失效语义。

### 主色阶（结构层，1 个色相）

| role | hex | 用途 | 灰度值 |
|---|---|---|---|
| primary | `#1B3A5C` | 输入资源列、核心模态框、主标题 | 52.6 |
| secondary | `#2E6B9E` | 主链阶段 ①–⑤ 骨干模块边框 | 94.6 |
| tertiary | `#5BA0D0` | 子模块、面板浅色填充、独立验证栏底 | 144.8 |
| gray-blue | `#8EAEC4` | 扩展模态/待核验/降级路径（**必配虚线**） | 166.9 |

### 强调色（语义层，2 个色相，用量 ≤10% 面积）

| role | hex | 用途 | 灰度值 |
|---|---|---|---|
| **alert** | `#D95F02` | 失效桶、专业条件错配、惩罚项 $-\mu P(u)$、不入池、退回修改、困难负例标红 | 120.9 |
| **pass** | `#1B9E77` | 三门全通过、正确检索、写入资源单元、交付产出 | 114.4 |

> 用 `#D95F02`（橙）而非纯红 `#D62728`：橙-绿组合对红绿色盲可分，红-绿不可分。**下游 prompt 禁止把 alert 换成纯红。**

### 中性色

| role | hex |
|---|---|
| text | `#333333` |
| fill | `#FFFFFF` |
| section_bg | `#F7F7F7` |
| border | `#CCCCCC` |
| arrow | `#4D4D4D` |

---

## 语义色绑定契约（跨 F1–F7 必须一致）

| 本项目角色 | 契约角色 | hex | 强制附加编码 |
|---|---|---|---|
| 输入资源 / 三类核心模态 | Input / Data | `#1B3A5C` | 实线框 |
| 主链阶段 ①–⑤ / 骨干模块 | Backbone | `#2E6B9E` | 实线框 + 圆角 |
| 扩展模态（代码·案例）/ 待核验队列 / 降级路径 | Frozen | `#8EAEC4` | **虚线框**（必须） |
| 失效 / 错配 / 惩罚 / 不入池 / 退回 | Loss·Feedback | `#D95F02` | **✗ 或 ⚠ 字形**（必须） |
| 通过 / 正确关联 / 输出交付物 | Output | `#1B9E77` | **✓ 字形**（必须） |
| 独立验证栏（专家盲评隔离区） | — | `#5BA0D0` 浅填充 | **虚线隔离墙** |

---

## 可及性说明（已实测，非估算）

按 BT.601 计算全部色值灰度：

```
text #333333    51.0   ← 文字
primary         52.6   ← 深蓝（B&W 下接近文字重量，可接受）
arrow           77.0
secondary       94.6
pass  #1B9E77  114.4  ┐
alert #D95F02  120.9  ┘ Δ=6.5 —— 黑白打印下【不可分】
tertiary       144.8
gray-blue      166.9
border         204.0
```

- ✅ **色盲安全**：蓝色阶梯 + 橙 + 绿，避开红-绿对立；三者在 deuteranopia/protanopia 下均可分。
- ❌ **已发现冲突**：`pass` 与 `alert` 灰度差仅 6.5，**黑白打印时两者会糊成同一灰**。
- ✅ **解法（已写入下游硬约束）**：pass/alert **一律双编码** —— pass = 实线 + ✓；alert = 虚线 + ✗/⚠ + 斜纹填充。任何图中**不得仅靠颜色**区分通过与失效。
- ⚠️ tertiary(144.8) 与 gray-blue(166.9) 灰度差 22，偏紧；故 gray-blue 一律配虚线，靠线型兜底。

---

## 单色统一 vs 分图类型择优（覆盖说明）

`palettes.md` 按图类型本应给 F3–F5 用 Blue Monochrome、F6 用 Purple-Green。**本项目统一覆盖为 Nature Blue**，理由：

1. 7 张图同处一份标书，评审连续翻页，跨图色系跳变（深蓝→紫绿）会显著削弱系统感；
2. Blue Monochrome 与 Nature Blue 同为蓝色阶梯，差异仅在明度，合并无损失；
3. F6 消融矩阵按 Figure Plan 只用符号占位、**不填任何数字**，不需要 Purple-Green 那种类别对比强度。

**备选方案**：若最终排版觉得 Nature Blue 过深过闷，整体切 **Blue Monochrome**（`#1565C0`/`#42A5F5`/`#90CAF9`，中性色同步换 `#212121`/`#F5F8FC`/`#B0BEC5`/`#37474F`），语义强调色与双编码规则不变。

---

## Handoff（供 `academic-figure-prompt` 直接消费）

```yaml
style_family: classic
palette: Nature Blue + semantic accents
primary:    "#1B3A5C"   # Input / 核心模态
secondary:  "#2E6B9E"   # Backbone / 主链阶段
tertiary:   "#5BA0D0"   # 子模块 / 浅填充 / 验证栏底
gray_blue:  "#8EAEC4"   # 扩展模态 / 待核验 / 降级（必虚线）
alert:      "#D95F02"   # 失效 / 错配 / 惩罚（必配 ✗ ⚠）
pass:       "#1B9E77"   # 通过 / 正确 / 输出（必配 ✓）
text:       "#333333"
fill:       "#FFFFFF"
section_bg: "#F7F7F7"
border:     "#CCCCCC"
arrow:      "#4D4D4D"
reason: "framework ≥4 模块触发单色规则；蓝色明度阶梯保证灰度打印可分；2 个色盲安全强调色承载通过/失效语义"
accessibility: colorblind-safe + needs dual encoding (pass vs alert 灰度不可分, 必须 ✓/✗ + 实线/虚线双编码)
chromatic_budget: 3 (blue ramp counted as 1) + neutrals
label_language: zh-CN
forbidden: ["纯红 #D62728", "渐变", "3D 立体", "彩虹面板", "仅用颜色区分通过与失效"]
```
