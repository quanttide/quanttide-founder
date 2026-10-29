# 协作与贡献指南

## Skill 概览

本项目将高频工作流封装为 Skill，位于 `.agents/skills/` 目录：

| Skill | 用途 | 触发词 |
|-------|------|--------|
| [git-commit](.agents/skills/git-commit/SKILL.md) | 规范提交 | "提交"、"commit" |
| [devops-release](.agents/skills/devops-release/SKILL.md) | 发布 Release | "发布"、"release" |
| [git-submodule](.agents/skills/git-submodule/SKILL.md) | 子模块管理 | "子模块"、"submodule" |
| [devops-audit](.agents/skills/devops-audit/SKILL.md) | 流程审查 | "审查"、"review" |
| [product-organize](apps/qtfounder/src/cli/skills/product-organize/SKILL.md) | 需求归档与清缓存 | "归档需求"、"汇总澄清记录"、"清缓存" |
| [write-express](apps/qtfounder/src/cli/skills/write-express/SKILL.md) | 表达改写 | "改写"、"太密"、"像口号" |
| [docs-format](apps/qtfounder/src/cli/skills/docs-format/SKILL.md) | 正式文档格式规范 | "格式"、"排版"、"正式文档" |

`design-review`、`docs-format`、`execute-collect`、`meta-classify`、`language-govern`、`think-reflect`、`product-collect`、`product-organize`、`write-express` 九条随 `qtfounder` CLI 发布，正文在 `apps/qtfounder/src/cli/skills/`，装在 `~/.agents/skills/`，不在本仓维护。

每个 Skill 的 `SKILL.md` 包含：触发词、规则、工作流步骤。

## 使用 Skill

Agent 会根据用户输入的触发词自动匹配对应的 Skill 并执行。

## 维护 Skill

### 新建 Skill

```bash
mkdir -p .agents/skills/<name>
# 创建 .agents/skills/<name>/SKILL.md
```

SKILL.md 模板：

```markdown
# <name>

简要描述功能。

## 触发词

"关键词1"、"关键词2"

## 规则

- 必须遵守的约束

## 工作流

### 步骤名称

```bash
具体命令
```
```

### 修改 Skill

直接编辑 `.agents/skills/<name>/SKILL.md`，提交变更即可。

### 删除 Skill

```bash
rm -rf .agents/skills/<name>
```

## 提交规范

提交信息遵循 Conventional Commits 格式：

```bash
git commit -m "<type>: <description>"
```

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复 bug |
| `docs` | 文档更新 |
| `test` | 测试相关 |
| `refactor` | 代码重构 |
| `chore` | 构建/工具 |

### 提交纪律

- 子模块提交并推送后，主仓库随即提交子模块指针更新，不积压
- 验证通过再提交；提交即推送，main 更新会触发站点部署
- 一次提交只做一件事，提交后回报 GitHub 提交链接

### 写入闸门

提交前跑一遍语言审计，只拦这一笔新引入的用词错误；HEAD 里已经有的算存量，放行。

- 装一次：`qtfounder git hook install`，装到主仓与各子模块；CLI 还没装时用 `.githooks/install.sh` 兜底，卸下用 `qtfounder git hook uninstall`
- 查漂移：`qtfounder git hook status`，有就退 1
- 同步子模块：`post-merge` 与 `post-checkout` 把子模块对齐到父仓指针记录的提交，不拉远程最新；拉最新仍用 `git submodule update --remote`
- 挡断指针：`pre-push` 跑 `qtfounder git submodule check --pushed`，子模块没推或指针不在远端就拦下
- 格式不管：列表、加粗、表格由体检报告定期报，不在提交时挡人；挡多了只会逼人用 `--no-verify`
- 嫌疑不拦，目录级的体裁要求也不拦，后者归人判
- 确属误判，`git commit --no-verify` 放行这一次，别当常规

## 记忆集划分与提炼

`data/context` 的记忆按主题域分集（详见 `data/context/AGENTS.md`）。集与集之间有**提炼关系**，不是并列：

- **default（创业与个人主线）只保留 `journal/` 与 `profile/`**——时间线 + 个人特征两层，不放 roadmap / insight / intention。
- **work（工作主线）从 default 提炼**：工作相关的主体（业务、组织、平台、AI 协作）归 `work/` 的各层。
- **write（写作主线）同理**：保留 `journal/` 与 `profile/`（创作动机 / 创作方法 / 创作困境），另有 `history/`、`library/` 放作品与素材。
- **提炼不丢内容**：从 default 收进 work 的各条按主题落位；重复的合并，独有的保留。

## 规范与执行的分工

手册（`docs/handbook`）与案例集（`docs/gallery`）不按「抽象 / 具体」分，按**判断与执行**分：

- **手册只留判断与边界**：为什么这么定、规则是什么、什么情况下不适用。不写可执行步骤，不贴完整命令序列。读者是人，读它是为了决策
- **可执行的流程一律进案例集 `work/`**：一个重复做的动作收成一个 work，文件内自带前置、命令、参数、校验与常见偏差，读它就能跑完
- **work 是工具的扩展单元**：主命令行保持干净，新增能力优先写成 work 定义，而不是写插件或新子命令；写完一个 work，工具就多一项能力
- **因此 work 必须自足**：前置（安装与认证）、用到的参数、失败现象与处置都在本篇内写全，不依赖别处
- **案例集内两种文体分目录**：`media/` 一类是判例（遇到过什么、当时怎么处理），`work/` 是工作流（这样跑就得到结果）
- 手册与 work 的关系是「定规则 / 照着跑」，不是互相链接：同一条事实同时像规则又像步骤时，步骤归 work，规则抽成一行留在手册
- work 的写法按任务蓝图执行：散文管命令与取舍，块管步骤、验收标准、偏差与边界

## 子模块边界

- 子模块之间**不互相引用**：正文、链接、相对路径、`myst.yml` 导航都不指向其它子模块的文件
- 相邻内容是各自写自足的一篇：用到的前置、命令、参数在本篇内写全，不复述对方
- 内容迁移按「移走不留副本」，来源侧删除；迁移记录只写在 CHANGELOG 里说明「从哪一类资产迁来」，正文不写对方仓的文件路径
- 理由：子模块单独发布、单独被引用，跨仓相对链接在网页上会断；两处都写同一个事实，就是两个真源

## 发布规范

- 子模块先发布，主仓库后发布；主仓库发布前确认所有子模块引用最新
- 子模块操作前先 checkout main：`git checkout main && git pull`

详细流程见 [devops-release](.agents/skills/devops-release/SKILL.md)。

## 创始人第二大脑：功能与边界

创始人第二大脑（`data/context`）的定位是**个人感受与源头的提纯层**：日志中唯一不可替代的内容是个人的情绪、边界体验与状态收束，这是蒸馏个人档案的最纯原料。工作想法与公司事务随处可读，混入会稀释信号——日志里的饮食规则即验收标准：AI 开始读不出重点时，就该提纯。

| 主体 | 内容 | 归宿 |
|------|------|------|
| 个人 | 感受、边界体验、状态收束、日志管理元规则 | `data/context` 的 `default/` 集 |
| 创作 | 叙事日志与创作档案 | `data/context` 的 `write/` 集；存量 write 归档在 `quanttide-write` 仓库 `data/archive/` |
| 滁州公司 | 公司启用、业务市场、品牌策略、资产组织 | `roadriver-tech` 仓库 `data/journal/` |
| 工作 | 系统治理、工具链、组织结构、职业定义、AI 观点解读 | `quanttide-work` 仓库 `data/context/quanttide-founder/` |
| 游戏 | 游戏日志与设计档案 | `quanttide-work` 仓库 `data/context/quanttide-founder/game/` |

运作逻辑（对应元目标「从依赖个人到依赖规则」）：

1. **个人孵化**：个人空间只产生源头（感受与问题），保持单人交互的轻量与独立可发版。
2. **溢出度量**：迁出量即个人向组织的资源溢出量，是可观测的贡献指标。
3. **提交组织**：成熟想法按主体迁入对应组织仓库，成为可交付资产（收复领土、驱逐他者）。
4. **规则化分流**：判断与流程固化在 `data/context/default/README.md` 与各 Skill 中，由 AI 自主执行，创始人一对一投入递减。

## 人机协作原则

1. **最小干预**：仅在用户明确请求时操作；不主动创建文件（除非必要）；优先编辑现有文件；目录变更需与作者商议，能不更改尽量不更改
2. **原子提交**：每次提交独立完整；不提交不完整的更改；验证后再提交
3. **验证优先**：修改后运行构建验证；前端文件操作后必须验证；确保更改符合预期
4. **安全第一**：不创建可能被恶意使用的代码；检测安全漏洞并报告；遵循 OWASP 最佳实践
5. **脚本归实验室**：一次性脚本默认写进 `examples/quanttide-founder-lab/examples/`，不写 `/tmp`，也不散在主仓根。脚本是工作经验的载体，丢进临时目录就等于没发生。文件头写清怎么跑、怎么算对，用完不删。

## 输出规范

- 不使用 emoji（除非用户明确请求）；输出简洁，适合 CLI 显示；使用 MyST Markdown
- 非财务语境不用记账类术语（记账、账目、两笔账）；写「记录」「事项」「衡量标准」
- 文件路径用 `code` 格式，每个引用独立、不合并，可选包含行号
- 代码示例用 fenced code blocks，包含语言标识符，保持简洁

### 文字体检

`qtfounder audit` 把文字与文档审计汇总成一份能给人读的报告，每期只说一处，改完再出下一期。缺省看整个仓，契约里的 exclude 会跳过流水、归档与示例；给目录参数就只看那几个。
