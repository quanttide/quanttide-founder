# 如何使用和维护 Skill

## Skill 概览

本项目将高频工作流封装为 Skill，位于 `.agents/skills/` 目录：

| Skill | 用途 | 触发词 |
|-------|------|--------|
| [devops-commit](.agents/skills/devops-commit/SKILL.md) | 规范提交 | "提交"、"commit" |
| [devops-release](.agents/skills/devops-release/SKILL.md) | 发布 Release | "发布"、"release" |
| [devops-submodule](.agents/skills/devops-submodule/SKILL.md) | 子模块管理 | "子模块"、"submodule" |

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

## 人机协作原则

1. **最小干预**：仅用户明确请求时操作
2. **原子提交**：每次提交独立完整
3. **验证优先**：修改后运行构建验证
