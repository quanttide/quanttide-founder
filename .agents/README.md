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
| [archive-to-domain](skills/archive-to-domain/SKILL.md) | "移交"、"领域归档" | 归档站资源移交领域 archive |
| [default-to-domain](skills/default-to-domain/SKILL.md) | "从 default 到领域" | default 内容移交领域资产仓 |
| [code-clarify](skills/code-clarify/SKILL.md) | "记一次澄清"、"汇总澄清账本"、返工信号 | 记录需求差、立规则，并按主题汇总到 `code/intent/` |
| [journal-to-profile](skills/journal-to-profile/SKILL.md) | "日志到档案" | 从日志蒸馏档案 |
| [journal-to-roadmap](skills/journal-to-roadmap/SKILL.md) | "日志到路线图" | 从日志蒸馏方向层路线图 |
| [journal-to-insight](skills/journal-to-insight/SKILL.md) | "日志到洞察" | 从日志提炼认知洞察 |
| [journal-to-intention](skills/journal-to-intention/SKILL.md) | "日志到意图" | 从日志提取人机协作意图 |

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
