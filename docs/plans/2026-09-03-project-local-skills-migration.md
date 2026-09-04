# Skills 项目级安装迁移方案

> 实施状态（2026-09-04）：代码与文档迁移已落地。仓库包含 25 个 canonical Skills、50 个双宿主薄入口、同步/检查/审计/归档/恢复脚本及定向回归测试。入口 frontmatter 会保留宿主共同支持的发现字段并过滤历史扩展字段，50 个入口均通过当前 Skill 校验器。只读审计发现当前用户目录有 49 个同名旧副本；为避免影响其他项目，本次未自动归档。Codex / Claude Code 重启后的来源显示仍需由使用者做最终人工确认。

## 通俗解释：究竟发生了什么

- **一句话说明：** 仓库已经保存了自己的 Skills 源码，但用户目前仍要把它们复制到个人目录后，Codex 或 Claude Code 才能发现；这会让不同项目互相污染，也会让旧副本遮住仓库里的新版本。
- **具体场景：** 这像一本书已经放在当前项目的资料柜里，使用者却还要把整本书复印到自己的公共书架。复印件更新不及时后，使用者可能读到旧内容；在另一项目中，同名复印件也仍会出现。
- **对应到本问题：** `skills/` 是项目内的原稿，`~/.agents/skills`、`~/.codex/skills` 和 `~/.claude/skills` 是个人公共书架，Codex 的 `.agents/skills` 与 Claude Code 的 `.claude/skills` 是项目自己的索引入口。
- **改变前后：** 现在克隆仓库后还需执行全局安装，且更新仓库不等于更新已安装副本；改进后只要从本仓库或其子目录启动 Codex/Claude Code，就能发现与当前 Git 版本一致的项目 Skills，不再要求把这 25 个项目自有 Skill 安装到用户主目录。

## 专业判断：问题在哪里

### 已确认的现状

1. 当前仓库在 [`skills/`](../../skills/) 下维护 25 个含 `SKILL.md` 和 `config.yaml` 的项目自有 Skill，`skills/` 应继续作为源码与版本号的单一真相来源。
2. 根级 [`README.md`](../../README.md#L247) 和 [`docs/manual-setup-guide.md`](../manual-setup-guide.md#L200) 仍把 `huangwb8/skills` 的全局安装器作为默认入口，安装目标不受当前仓库边界约束。
3. 仓库目前没有 `.agents/skills/`，已有 `.claude/` 目录也没有 `.claude/skills/`，因此仅有 `skills/` 并不能依靠两种宿主的官方项目发现机制完成加载。
4. OpenAI 官方文档规定，Codex 从当前目录到仓库根目录逐级扫描 `.agents/skills`；Claude Code 官方文档规定，项目 Skill 位于 `.claude/skills`，并从启动目录向仓库根目录扫描。两种宿主的入口目录不同。
5. 同名冲突的行为也不同：Codex 可能同时展示同名 Skill；Claude Code 的个人 Skill 会覆盖项目 Skill。因此只增加项目入口而不处理旧的全局副本，不能保证实际运行的是仓库版本。
6. 活跃代码和文档仍有少量全局路径假设，例如 [`research-idea` 的依赖搜索](../../skills/research-idea/scripts/init_workspace.py#L203)、[`paper-explain-figures` 的命令示例](../../skills/paper-explain-figures/SKILL.md#L113)和 [`research-citation-check` 的兼容搜索](../../skills/research-citation-check/scripts/runtime_utils.py#L147)。历史 CHANGELOG 和旧计划中的路径属于历史记录，不应机械改写。
7. [`research-idea`](../../skills/research-idea/SKILL.md#L66) 还依赖当前仓库未内置的 `parallel-vibe`。这属于外部 Skill 依赖，与“把本项目自有 Skill 改为项目级”是两个层次，必须显式记录，不能假装仓库已经完全自包含。

官方依据：

- [OpenAI：Where Codex loads local skills](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)
- [Claude Code：Where skills live](https://code.claude.com/docs/en/skills#where-skills-live)

### 影响范围

- 新用户：当前仍需额外安装，无法做到克隆即用。
- 维护者：修改 `skills/*` 后，全局副本可能继续执行旧逻辑，容易把“源码已修复”误判成“实际已生效”。
- 多项目用户：ChineseResearchLaTeX 专用 Skill 会出现在不相关仓库中，增加误触发和上下文占用。
- Windows 用户：若直接依赖 Git 符号链接，可能受开发者模式、权限和 `core.symlinks` 设置影响，不符合本仓库的跨平台口径。

## 要达到什么目标

### 完成后的变化

- 从仓库根目录或任意 `projects/*`、`packages/*` 子目录启动 Codex/Claude Code，都能发现本仓库的 25 个项目 Skill。
- `skills/<name>/` 继续是唯一可编辑源码；两个宿主入口不复制业务脚本、资源和长篇 Skill 正文。
- 普通用户不再运行 `curl | bash`、`irm | iex` 或外部 `install-bensz-skills` 来获得本项目自有 Skill。
- 旧全局同名副本能够被只读审计，并由用户显式选择归档；默认流程不删除用户主目录中的任何内容。
- 修改、新增或删除 Skill 后，维护者能用一个确定性命令同步项目入口，并用只读检查防止漏同步。
- 运行时代码优先解析当前仓库中的 Skill；兼容期内若退回全局副本，必须给出可见提示。

### 不在本次处理范围

- 不把所有通用或第三方 Skill 都复制进 ChineseResearchLaTeX。
- 不把项目 Skill 打包成公开插件；当前需求是仓库级工作流，官方也把直接项目目录作为此类场景的合适载体。
- 不自动修改或删除 OpenAI/Claude 的系统 Skill、插件缓存和无关用户 Skill。
- 不重写历史 CHANGELOG、已完成计划或历史测试报告中的旧路径。
- 不改变各 Skill 的写作业务逻辑，除非它确实依赖全局安装路径。

## 推荐架构

保留当前 `skills/` 作为唯一源码，在两个宿主的官方目录中提交“薄入口”：

```text
ChineseResearchLaTeX/
├── skills/                         # 唯一可编辑源码与资源
│   └── nsfc-abstract/
│       ├── SKILL.md
│       ├── config.yaml
│       └── ...
├── .agents/skills/                 # Codex 项目级发现入口
│   └── nsfc-abstract/SKILL.md      # 自动生成的薄入口
├── .claude/skills/                 # Claude Code 项目级发现入口
│   └── nsfc-abstract/SKILL.md      # 自动生成的薄入口
├── scripts/sync_project_skills.py  # 生成与校验入口
└── tests/project-skills/           # 迁移脚本与目录契约测试
```

每个薄入口只承担两件事：

1. 复制源 `SKILL.md` 中宿主共同支持的 frontmatter 字段（`name`、`description`、`metadata`、`allowed-tools`、`license`），过滤只属于历史格式的扩展字段，使入口能通过宿主格式校验。
2. 明确要求宿主完整读取 `skills/<name>/SKILL.md`，以该文件为唯一执行规范，并以它所在目录解析 `scripts/`、`references/`、`assets/` 等相对路径。

薄入口应标记为自动生成，禁止人工维护。这样既满足 Codex/Claude Code 的官方发现路径，又不会生成两套可漂移的业务源码。

### 为什么推荐薄入口，而不是另外两种做法

| 做法 | 结论 | 原因 |
| --- | --- | --- |
| 把 25 个 Skill 完整复制到 `.agents/skills` 和 `.claude/skills` 并提交 | 不推荐 | 三份源码会膨胀仓库，并造成脚本、资源、版本号和文档漂移。 |
| 在两个入口目录中提交符号链接 | 不作为默认方案 | Codex 明确支持符号链接，但 Claude Code 项目 Skill 文档没有给出同等保证；Windows 的 Git 符号链接也存在权限和检出差异。 |
| 提交跨平台薄入口，并自动生成/校验 | 推荐 | 克隆即能被发现，业务源码仍只有一份，普通 Git 文件在 macOS、Linux、Windows 和 WSL 上行为一致。 |

在批量生成 25 个入口前，先选 1 个无外部依赖的 Skill 做 Codex 和 Claude Code 双宿主验证。若任一宿主不能稳定按薄入口读取源文件，则回退为“项目内生成完整镜像”：由同一脚本把 `skills/` 复制到两个隐藏入口，但生成目录不作为人工编辑源，并用摘要校验防漂移。不要退回全局安装，也不要以符号链接作为 Windows 默认方案。

## 改进方向

### 建立项目级发现入口

新增 `scripts/sync_project_skills.py`，自动枚举 `skills/*/SKILL.md`，生成两套薄入口。脚本至少提供：

- `sync`：新增、更新入口；只删除带本脚本管理标记且源 Skill 已不存在的旧入口。
- `check`：只读比较源目录与两个入口，发现缺失、陈旧、额外受管入口或 frontmatter 不一致时返回非零状态。

脚本不得扫描或写入用户主目录。源 Skill 的目录名、frontmatter `name` 和 `config.yaml` 的 `skill_info.name` 应一致；不一致时早失败，不生成模糊入口。

对普通用户而言，这意味着项目随 Git 一起带上自己的能力索引，不必再进行个人级安装。

### 让项目路径成为运行时第一选择

清理活跃文档和代码中的全局路径假设：

- Skill 自身脚本继续优先通过 `Path(__file__).resolve()` 定位自己的资源。
- 跨 Skill 依赖按“当前仓库 `skills/` → `.agents/skills`/`.claude/skills` → 兼容期用户目录”的顺序解析。
- `research-idea` 的 `.` 搜索不能继续误认为 `<仓库根>/<skill>`；应明确支持 `<仓库根>/skills/<skill>`，并对外部 `parallel-vibe` 给出准确诊断。
- `paper-explain-figures`、`research-idea` 等命令示例改成仓库相对入口，移除“系统级安装后”的默认示例。
- 兼容期全局回退只用于不阻断现有用户；一旦实际命中全局副本，应提示其运行迁移审计。

对普通用户而言，这意味着仓库中的修改会直接成为下一次执行所用版本，不会悄悄跑到主目录里的旧脚本。

### 安全迁移旧全局副本

将用户主目录操作与项目入口生成分开，避免普通同步命令意外影响全局环境：

1. 提供只读审计，精确检查本仓库拥有的 25 个名称是否存在于 `~/.agents/skills`、旧版 `~/.codex/skills` 和 `~/.claude/skills`。
2. 默认只报告冲突、实际路径、是否为符号链接以及项目/全局版本差异，不删除内容。
3. 若后续实现归档命令，必须由用户显式传参，把精确命中的项目自有目录移动到带时间戳的备份目录；禁止递归处理整个 `skills` 根目录。
4. 归档清单要支持恢复。外部依赖、系统 Skill、插件 Skill 和未知同名目录均不自动处理。
5. README 说明 Claude Code 的个人同名 Skill 会覆盖项目 Skill，Codex 可能同时显示同名项；因此完成迁移后应重启或刷新宿主并核验实际路径。

对普通用户而言，这意味着旧版本不会被静默删除，迁移失败时也能恢复。

### 显式管理外部 Skill 依赖

项目自有 Skill 与外部通用 Skill 分开管理：

- 第一阶段先把当前 25 个项目自有 Skill 全部项目化。
- 对 `parallel-vibe` 等外部依赖建立清单，标注 `required`、`optional`、来源和受影响的项目 Skill。
- 本次默认不把外部仓库内容复制进源码树。依赖缺失时，相关 Skill 应早失败并准确说明“缺少外部依赖”，但不影响其余项目 Skill。
- 如果最终验收要求“离线克隆后所有 Skill 都可运行、完全不依赖任何用户级 Skill”，再单独决定是固定版本后项目内供应，还是移除该依赖。这个决定会引入上游同步和许可维护成本，不应在本次迁移中默认为已授权。

对普通用户而言，这意味着“项目自带什么”和“还需要什么外部能力”清楚分开，不会出现半安装状态却没有提示。

### 统一文档与维护规则

更新以下现行入口：

- 根级 [`README.md`](../../README.md#L247)：把 Skills 默认用法改为“克隆/更新仓库后从仓库内启动”，删除全局一键安装作为默认路径。
- [`docs/manual-setup-guide.md`](../manual-setup-guide.md#L200)：新增项目发现、同步检查、全局冲突审计和恢复说明；外部全局安装命令若保留，只放入“通用外部 Skill”章节。
- [`skills/README.md`](../../skills/README.md#L1)：说明 `skills/` 是源码，不是宿主直接扫描目录；用户调用仍使用 Skill 名，不直接调用薄入口文件。
- [`AGENTS.md`](../../AGENTS.md#L221)：固定“`skills/` 单一真相 + 两个生成入口 + 禁止全局安装项目自有 Skill”的约定；[`CLAUDE.md`](../../CLAUDE.md#L3) 已引用 `AGENTS.md`，只有出现 Claude Code 专属行为时才补充，避免重复维护核心规则。
- 根级 [`CHANGELOG.md`](../../CHANGELOG.md#L1)：记录默认安装范围变化；只有确实修改运行路径或行为的单个 Skill 才递增 patch 版本并更新自己的 README/CHANGELOG，不为纯生成入口批量虚增 25 个版本号。

文档中的旧计划和历史 CHANGELOG 保留原貌，以免篡改历史；检查规则使用明确排除清单。

## 实施范围与顺序

1. **先做单 Skill 技术验证。** 选择 `nsfc-abstract` 生成两份薄入口，分别从仓库根目录和 `projects/NSFC_Young` 启动 Codex/Claude Code，验证显式调用、隐式匹配、源文件读取和相对资源解析。
2. **建立生成与校验机制。** 落地同步脚本、受管标记、frontmatter 校验和 `tests/project-skills/` 自动化测试，再批量生成全部项目入口。
3. **修正运行时路径。** 全仓扫描活跃的 `SKILL.md`、README、配置和脚本，按项目优先规则修复已确认的全局路径假设；历史材料不改。
4. **梳理外部依赖。** 至少确认 `research-idea → parallel-vibe` 的处理口径，并把必需/可选依赖写入可检查清单。
5. **提供安全迁移。** 先实现只读全局冲突审计；归档/恢复功能只有在测试覆盖精确目标与路径安全后再开放，并保持显式触发。
6. **切换用户文档。** 更新 README、手动指南、AGENTS/CLAUDE 和 CHANGELOG，把项目级加载设为唯一默认路径。
7. **完成双宿主验收。** 在无项目同名全局副本的干净环境及存在旧全局副本的迁移环境中分别验收，然后再宣布全局安装模式退役。

## 如何确认完成

### 自动化验收

- `python3 scripts/sync_project_skills.py check` 返回成功，并确认两个入口各有 25 个受管 Skill。
- 自动化测试覆盖：新增、更新、删除源 Skill；frontmatter 缺失或名称不一致；陈旧入口；未知非受管目录不被删除；路径中含空格；Windows 风格路径处理。
- 在 `tests/project-skills/` 的临时仓库夹具中验证所有写入，测试不得在仓库根目录制造产物。
- 对活跃文件执行路径扫描：除迁移审计的兼容白名单外，不再出现把本项目自有 Skill 默认指向 `~/.agents/skills`、`~/.codex/skills` 或 `~/.claude/skills` 的说明和实现。
- `research-idea` 在项目依赖可用时能定位 `skills/research-topic-extractor` 与 `skills/research-literature-review`；缺少 `parallel-vibe` 时给出明确、非误导的外部依赖错误。

### 人工验收矩阵

| 场景 | Codex | Claude Code |
| --- | --- | --- |
| 从仓库根目录启动 | `/skills` 或 `$` 能看到项目 Skill，路径指向 `.agents/skills` | `/skill-name` 可调用，来源为 `.claude/skills` |
| 从 `projects/NSFC_Young` 启动 | 能沿父目录发现根级项目 Skill | 能沿父目录发现根级项目 Skill |
| 显式调用 `nsfc-abstract` | 完整读取 `skills/nsfc-abstract/SKILL.md` | 完整读取 `skills/nsfc-abstract/SKILL.md` |
| 隐式请求生成 NSFC 摘要 | 按原 description 命中 | 按原 description 命中 |
| 存在旧全局同名副本 | 审计能报告重复项，归档后只剩项目项 | 审计能报告覆盖风险，归档后项目项生效 |
| 修改源 Skill 后忘记同步 | `check` 失败并指出具体 Skill | 同左 |

### 完成标准

- 普通安装说明中不再要求全局安装这 25 个项目自有 Skill。
- 仓库根和子目录中的双宿主发现测试通过。
- `skills/` 仍是唯一业务源码，两个隐藏入口只含受管薄文件。
- 旧全局副本的审计、归档边界和恢复方法有文档、有测试、默认无破坏性。
- 外部依赖没有被误报为项目已内置，也不会拖累无关 Skill。

## 风险与待确认事项

- **最大技术风险是薄入口的跨宿主行为。** 必须先做单 Skill 实机验证；失败时按本方案回退为项目内生成完整镜像，不改变“停止全局安装”的目标。
- **旧全局副本会改变实际优先级。** 在全局冲突未归档前，不能仅凭“项目入口存在”判定迁移完成。
- **完全离线、自包含是更大的目标。** 当前已确认至少有 `parallel-vibe` 外部依赖。本方案默认先完成项目自有 Skill 的本地化；若要求所有外部依赖也随仓库交付，需要追加依赖供应策略。
- **项目级 Skill 只在当前仓库范围生效。** 如果用户把单个 `projects/*` 目录脱离仓库单独复制，根级项目 Skill 不会随之存在；Release 是否需要携带对应入口应按发布资产类型另行决定。
- **不要自动清空用户目录。** 全局迁移只处理精确名称、先审计后归档、保留恢复清单；系统和插件提供的 Skill 永远不由本项目清理。
