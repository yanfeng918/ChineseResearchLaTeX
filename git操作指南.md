# Git 操作指南

本文记录本仓库的远程配置、踩过的坑与对应处理方式。内容基于 2026-08-31 的实际排查。

---

## 本仓库的远程配置

```text
仓库级（可以有多个）
  origin    → github.com/yanfeng918/ChineseResearchLaTeX     自己的 fork
  upstream  → github.com/huangwb8/ChineseResearchLaTeX       上游原仓库

分支级（一条分支只能有一个）
  main 的上游追踪 = origin/main
```

查看：

```bash
git remote -v                              # 有哪些远程
git branch -vv                             # 各分支追踪谁
git config --get branch.main.remote        # main 默认推/拉哪个远程
```

---

## Q1：这个仓库有几个远程仓库？

**两个**：`origin`（自己的 fork）和 `upstream`（huangwb8 的原仓库）。

但要分清两层概念，混淆它们是后面所有麻烦的根源：

| 层级 | 含义 | 数量 |
|---|---|---|
| **远程仓库**（remote） | "我知道有这几个地址" | 可以有很多个 |
| **上游追踪**（tracking） | "我这条分支默认跟谁对账" | 一条分支只能有一个 |

`git push origin main` 只是**这一次**推到 origin，**不会改变追踪**。

### 曾经的隐患

排查时发现 `main` 的追踪指向的是 `upstream/main`：

```bash
$ git config --get branch.main.remote
upstream
```

意味着敲**不带参数的 `git push`，目标是 huangwb8 的原仓库**。当时能推成功只是因为显式写了 `origin`；少打这两个字就会去推别人的仓库。大概率被权限拒掉，但不该靠"没权限"来兜底。

其他分支（`XJNSF`、`dev`、`XJNSF-V2`、`2026_Education`）追踪的都是 `origin`，只有 `main` 是历史遗留的例外——大概是先从上游 clone 本地副本、后来才把自己的 fork 接成 `origin` 留下的。

### 已修复

```bash
git branch -u origin/main main
```

---

## Q2：`git push origin main` 报 non-fast-forward

```text
 ! [rejected]        main -> main (non-fast-forward)
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
```

### 别照着提示做

git 这句 "behind" 是**误导**。它只是发现无法 fast-forward，套用了最常见的措辞。真实原因要自己查：

```bash
git fetch origin main
git rev-list --left-right --count origin/main...main    # 左=远端独有  右=本地独有
git merge-base origin/main main                          # 有无共同祖先
```

当时的结果：

```text
origin 独有 1 个，本地独有 794 个
merge-base 无输出  →  ★ 没有共同祖先，两条历史完全无关
```

```text
origin/main   b0d080f  "Initial commit"   只有 1 个提交，只含 LICENSE（2026-08-12 网页建仓时生成）
本地 main     d2e3f46  ...                794 个提交，整个项目
```

**这种情况下 `git pull` 千万别跑**——会把两条无关历史 merge 成畸形的双根提交树，换来的只是一个 LICENSE 文件。

> 排查小坑：`git merge-base A B | xargs git log -1` 在无共同祖先时，`merge-base` 空输出会让 `xargs` 空跑成 `git log -1`，显示的是 HEAD，看着像"有祖先"。判断有无祖先要看返回码，不要看管道末端的输出。

### 处理方式

那个 `Initial commit` 除了 LICENSE 什么都没有，而 LICENSE 在本地 794 个提交里本来就有，丢掉零损失：

```bash
git push --force-with-lease origin main
```

用 `--force-with-lease` 而不是 `-f`：它会先确认远端还停在预期的提交上，期间有别人推过就拒绝。

其他两个备选（当时未采用）：

- `git push origin main:main-full` —— 先推到别的分支留后路
- `git merge --allow-unrelated-histories` —— 能接上，但历史里会留一个双根 merge，为一个已有的 LICENSE 不值得

---

## Q3：force push 之后，main 岂不是有两个远程仓库？

不是。**推送目标**和**追踪目标**是两件事，见 Q1 的两层概念表。

force push 只是把提交送到了 `origin/main`，`main` 的追踪当时仍然指着 `upstream/main`。现在追踪已改为 `origin/main`，两者才统一。

---

## Q4：改完追踪后，`git pull` 从哪里拉？

**从 `origin/main`，也就是自己的 fork。** upstream 不会再被自动碰到。

`git pull` 读的是这两条配置：

```bash
branch.main.remote = origin              # 从哪个远程
branch.main.merge  = refs/heads/main     # 拉那个远程的哪条分支
```

合起来等价于 `git pull origin main`。

改完之后的行为：

| 命令 | 去哪 |
|---|---|
| `git push` | → `yanfeng918/ChineseResearchLaTeX` 的 main |
| `git pull` | ← 同上 |
| `git status` 的 ahead/behind | 对自己的 fork 算 |

日常这个 `git pull` 大多数时候是空跑，因为 `origin/main` 上都是自己推的。**真正有用的场景是在别的机器或 worktree 里推过东西之后。**

---

## 同步上游更新

改完追踪后，同步上游变成一个需要主动做的动作，不会再"顺手就拉进来了"：

```bash
git fetch upstream
git log --oneline main..upstream/main    # 先看人家更新了什么
git merge upstream/main                  # 确认要了再合
```

这正是 fork 工作流该有的样子：**默认走自己的，同步别人的是有意识的决定。**

### merge 还是 rebase

个人科研代码 + worktree + PR 的用法下，一般偏好 `git rebase upstream/main` 保持线性历史：

```bash
git fetch upstream
git rebase upstream/main
```

**但本仓库当前不适用**，原因是：

- 本地已有 794 个提交，与上游分叉很久
- rebase 意味着逐个重放这 794 个提交，冲突要解很多轮
- 这些提交已经推到 `origin`，rebase 会改写全部哈希，其他 worktree 和分支都要跟着善后

所以本仓库同步上游用 **`merge`**。真要动手前先看清楚 `main..upstream/main` 有多少东西，冲突量可能不小。

新开的、提交数少、还没推出去的分支，仍然可以正常用 rebase。

---

## 速查

```bash
# 看清楚现状
git remote -v
git branch -vv
git config --get branch.<分支>.remote

# 推送被拒时，先查清是"落后"还是"无关历史"
git fetch origin <分支>
git rev-list --left-right --count origin/<分支>...<分支>
git merge-base origin/<分支> <分支> && echo 有共同祖先 || echo 无共同祖先

# 改分支追踪
git branch -u origin/<分支> <分支>

# 安全的强推
git push --force-with-lease origin <分支>

# 同步上游
git fetch upstream
git log --oneline main..upstream/main
git merge upstream/main
```

---

## 几条原则

- **push/pull 报错时，先查清状态再动手**。git 的 hint 覆盖的是最常见情形，不一定是当前情形
- **强推一律用 `--force-with-lease`**，不用裸 `-f`
- **`git pull` 在不确定的时候不要跑**。先 `git fetch` 再看差异，确认了再 merge
- **fork 工作流下，分支追踪应指向自己的 fork**，同步上游是显式动作
