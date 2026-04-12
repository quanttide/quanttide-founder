# Skills

Agent 技能集合，每个 Skill 封装一个高频工作流。

## 使用方法

Agent 会根据用户输入自动匹配 Skill，也可直接调用：

| Skill | 触发词 | 用途 |
|-------|--------|------|
| [devops-commit](skills/devops-commit/SKILL.md) | "提交"、"commit" | 规范提交 |
| [devops-release](skills/devops-release/SKILL.md) | "发布"、"release" | 发布 Release |
| [devops-submodule](skills/devops-submodule/SKILL.md) | "子模块"、"submodule" | 子模块管理 |

## 目录结构

```
.agents/
└── skills/
    ├── devops-commit/       # 规范提交
    ├── devops-release/      # 发布 Release
    └── devops-submodule/    # 子模块管理
```

每个 Skill 目录包含 `SKILL.md`，定义触发词、规则和工作流步骤。

## 新建 Skill

```bash
mkdir -p .agents/skills/<name>
# 编辑 .agents/skills/<name>/SKILL.md
```

详见 [CONTRIBUTING.md](../CONTRIBUTING.md)。
