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
| [product-clarify](skills/product-clarify/SKILL.md) | "记一次澄清"、返工信号 | 记录需求差、立规则 |
| [product-requirement](skills/product-requirement/SKILL.md) | "归档需求"、"汇总澄清账本"、"清缓存" | 按主题归入 `product/requirement/`，归档后清本地缓存 |
| [meta-category](skills/meta-category/SKILL.md) | "这条该放哪"、"日志到洞察"、"日志到路线图"、"日志到意图" | 判类、从日志分诊到各层、按类写入 |

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
