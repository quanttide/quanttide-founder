# AGENTS.md

## 相关文档

| 文档 | 用途 |
|------|------|
| [README](README.md) | 项目概述、子模块列表 |
| [CONTRIBUTING](CONTRIBUTING.md) | Skill 使用和维护指南 |

### Skill 索引

| Skill | 用途 | 路径 |
|-------|------|------|
| [asset-vision](.agents/skills/asset-vision/SKILL.md) | 愿景资产管理 | `.agents/skills/asset-vision/SKILL.md` |
| [devops-commit](.agents/skills/devops-commit/SKILL.md) | 规范提交 | `.agents/skills/devops-commit/SKILL.md` |
| [devops-release](.agents/skills/devops-release/SKILL.md) | 发布 Release | `.agents/skills/devops-release/SKILL.md` |
| [devops-submodule](.agents/skills/devops-submodule/SKILL.md) | 子模块管理 | `.agents/skills/devops-submodule/SKILL.md` |
| [devops-review](.agents/skills/devops-review/SKILL.md) | 流程审查 | `.agents/skills/devops-review/SKILL.md` |

---

## 快速索引

| 任务 | 操作位置 |
|------|---------|
| 提交变更 | Skill: `commit` |
| 发布 Release | Skill: `release` |
| 修改子模块 | Skill: `submodule` |
| 记录日报 | `docs/archive/report/default/diary/YYYY-MM-DD.md` |

---

## 我的工作原则

### 最小干预
- 仅在用户明确请求时操作
- 不主动创建文件（除非必要）
- 优先编辑现有文件
- 目录变更需与作者商议：作者对目录使用有严格规范，能不更改尽量不更改

### 原子提交
- 每次提交独立完整
- 不提交不完整的更改
- 验证后再提交

### 验证优先
- 修改后运行构建验证
- 前端文件操作后必须验证
- 确保更改符合预期

### 安全第一
- 不创建可能被恶意使用的代码
- 检测安全漏洞并报告
- 遵循 OWASP 最佳实践

## 输出规范

### 内容格式
- 不使用 emoji（除非用户明确请求）
- 输出简洁，适合 CLI 显示
- 使用 MyST Markdown

### 文件引用
- 使用 `code` 格式表示文件路径
- 每个引用独立，不合并
- 可选包含行号信息

### 代码示例
- 使用 fenced code blocks
- 包含语言标识符
- 保持代码简洁

## 自我更新

### 总体原则
- 重要变更记录到 `docs/archive/report/default/diary/YYYY-MM-DD.md`
- 能力变化时更新本文档
- 保持所有文档与实际情况一致

## Git 提交规范

遵循 Conventional Commits 格式，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

**Commit 类型：**

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add user authentication` |
| `fix` | 修复 bug | `fix: resolve null pointer exception` |
| `docs` | 文档更新 | `docs: update README` |
| `test` | 测试相关 | `test: add unit tests for api` |
| `refactor` | 代码重构 | `refactor: simplify logic` |
| `chore` | 构建/工具 | `chore: update dependencies` |

## 重要提示

- **子模块操作前先 checkout main**：`git checkout main && git pull`
- **Release 标题**：使用 `项目名/vX.Y.Z` 格式（如 cli/v0.0.1-alpha.3）
- **Release notes**：只包含对应版本内容

---

## 如何维护 AGENTS.md

| 类型 | 写在哪里 |
|------|---------|
| 详细说明、工作流步骤 | `.agents/skills/` 中的 Skill 文件 |
| 给链接、导航索引 | AGENTS.md |

更新时机：新增文档、新增任务类型、重要规则变化时更新；README/Skill 已有的内容不重复。
