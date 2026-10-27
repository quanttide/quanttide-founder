# AGENTS.md

不要过度思考：直接动手，做必要的最小改动，不发散不铺开。变更一律提交并推送（子模块逐层指针一并更新），不必逐次确认。

## 相关文档

| 文档 | 用途 |
|------|------|
| [README](README.md) | 项目概述、子模块列表 |
| [CONTRIBUTING](CONTRIBUTING.md) | 工作原则、输出规范、第二大脑功能与边界、Skill 使用维护、版本契约 |
| [习惯](docs/gallery/meta/property.md) | 标识、文档模板、变更与语言上的个人偏好（id 用 uuid，name 做机器可读标识） |

## 快速索引

| 任务 | 操作位置 |
|------|---------|
| 装/查 Git 钩子 | `qtfounder git hook install` / `status` |
| 查子模块指针 | `qtfounder git submodule check` |
| 提交变更 | Skill: `git-commit`（规范见 CONTRIBUTING） |
| 发布 Release | Skill: `devops-release` |
| 修改子模块 | Skill: `git-submodule` |
| 流程审查 | Skill: `devops-audit` |
| 记录日报 | `data/context/default/YYYY-MM-DD.md`（当天放集根，更早日志在 `data/context/default/journal/`） |
| 记一次澄清 / 立规则 | Skill: `product-collect`（调 `qtfounder product clarify`） |
| 归档需求 / 清缓存 | Skill: `product-organize`（用 `product organize` 读聚类，写 `data/profile` 的 `product/`，再 `product clear`） |
| 归档旧日志 | 手动迁入 `data/journal/<域>/<YYYY-MM>/YYYY-MM-DD.md` |
| 看文字体检 | `qtfounder audit`（每期只说一处） |
| 改写表达 | Skill: `write-express`（先跑 `qtfounder write`，再按定义、步骤、边界、验收重排） |
| 查 Skill 命名 | `qtfounder agent skill lint <目录>`（范围-动词、触发时机、标题） |
| 判断该放哪 | `qtfounder meta classify <文件>`（Skill: `meta-classify`） |
| 清一批禁用词 | Skill: `language-govern`（清单见 `data/roadmap/language/governance.md`） |
| 写一次性脚本 | `examples/quanttide-founder-lab/examples/`，不写临时目录 |
| 装 Skill 到系统位置 | `qtfounder agent skill install`（缺省 `~/.agents/skills`；只装某个仓加 `--root`，`check` 查差异） |

`meta-classify`、`language-govern`、`think-reflect`、`product-collect`、`product-organize`、`write-express` 六条随 `qtfounder` 发布，正文在 `apps/qtfounder/src/cli/skills/`，装在 `~/.agents/skills/`；本仓 `.agents/skills/` 不再保留这六条。

## 如何维护 AGENTS.md

| 类型 | 写在哪里 |
|------|---------|
| 详细说明、工作流步骤 | `.agents/skills/` 中的 Skill 文件 |
| 协作原则、输出规范、背景理解、版本契约 | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 给链接、导航索引 | AGENTS.md |

更新时机：新增文档、新增任务类型、重要规则变化时更新；README/Skill/CONTRIBUTING 已有的内容不重复。
