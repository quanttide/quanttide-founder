# Skills

Agent 技能集合，每个 Skill 封装一个高频工作流。

## 使用方法

Agent 会根据用户输入自动匹配 Skill，也可直接调用：

| Skill | 触发词 | 用途 |
|-------|--------|------|
| [git-commit](skills/git-commit/SKILL.md) | "提交"、"commit" | 规范提交 |
| [devops-release](skills/devops-release/SKILL.md) | "发布"、"release" | 发布 Release |
| [devops-audit](skills/devops-audit/SKILL.md) | "审查"、"review" | 流程审查 |
| [git-submodule](skills/git-submodule/SKILL.md) | "子模块"、"submodule" | 子模块管理 |

`meta-classify`、`language-govern`、`think-reflect`、`product-collect`、`product-organize` 五条随 `qtfounder` CLI 发布，正文在 `apps/qtfounder/src/cli/skills/`，装在 `~/.agents/skills/`，本目录不再保留。

## 目录结构

```
.agents/
└── skills/
    ├── git-commit/
    │   ├── SKILL.md
    │   ├── scripts/
    │   ├── references/
    │   └── assets/
    ├── devops-release/
    │   ├── SKILL.md
    │   ├── scripts/
    │   ├── references/
    │   └── assets/
    └── git-submodule/
        ├── SKILL.md
        ├── scripts/
        ├── references/
        └── assets/
```

每个 Skill 包含 `SKILL.md`（YAML Frontmatter + Markdown 正文）和可选的 `scripts/`、`references/`、`assets/` 目录。

## 新建 Skill

```bash
mkdir -p .agents/skills/<name>
# 编辑 .agents/skills/<name>/SKILL.md
```

详见 [CONTRIBUTING.md](../CONTRIBUTING.md)。
