# AGENTS.md

## 相关文档

| 文档 | 用途 |
|------|------|
| [README](README.md) | 项目概述、子模块列表 |
| [CONTRIBUTING](CONTRIBUTING.md) | 人机协作、子模块工作流、发布流程、环境变量 |
| [meta/IDENTITY.md](meta/IDENTITY.md) | 仓库自我映射、子模块列表 |
| [meta/SOUL.md](meta/SOUL.md) | AI 自我认知（自维护）|
| [meta/TOOLS.md](meta/TOOLS.md) | 工具清单（自维护）|

---

## 快速索引

| 任务 | 操作位置 |
|------|---------|
| 修改子模块 | CONTRIBUTING > 子模块工作流 |
| 发布 Release | CONTRIBUTING > 主仓库发布 Release |
| 提交变更 | `cz commit` |
| 处理错误 | CONTRIBUTING > 常见错误处理 |
| 更新环境变量 | CONTRIBUTING > 环境变量 |
| 记录日报 | `meta/report/YYYY-MM-DD.md` |

---

## 协作原则

- 最小干预：仅用户明确请求时操作
- 原子提交：每次提交独立完整
- 验证优先：修改后运行构建验证

## 重要提示

- **子模块操作前先 checkout main**：`git checkout main && git pull`
- **读取 .env 需要临时权限**：Agent 无法直接读取 .env
- **自动同步**：.env 变更时同步更新 .env.example
- **Release 标题**：使用 `项目名/vX.Y.Z` 格式（如 cli/v0.0.1-alpha.3）
- **Release notes**：只包含对应版本内容

---

## 如何维护 AGENTS.md

| 类型 | 写在哪里 |
|------|---------|
| 详细说明、工作流步骤 | CONTRIBUTING |
| 给链接、导航索引 | AGENTS.md |

更新时机：新增文档、新增任务类型、重要规则变化时更新；README/CONTRIBUTING 已有的内容不重复。
