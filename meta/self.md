# Self - 自我映射

本文件是整个仓库的自我映射，反映当前项目状态。

## 项目概述

**quanttide-founder** 是量潮创始人工作文档的元仓库（Meta Repository），通过 Git 子模块管理多个独立的知识库。

## 子模块列表

| 子模块 | 路径 | 描述 | 当前版本 |
|--------|------|------|----------|
| **essay** | `./essay/` | 随笔 - 个人思考和想法的记录 | 0.0.1 |
| **handbook** | `./handbook/` | 手册 - 工作流程和规范文档 | v0.0.2 |
| **journal** | `./journal/` | 日志 - 日常记录和事件记忆 | 0.1.1 |
| **profile** | `./profile/` | 档案 - 工作和知识档案 | 0.2.3 |
| **specification** | `./specification/` | 标准 - 规范和定义文档 | 0.0.1 |

## 目录结构

```
quanttide-founder/
├── essay/          # 随笔模块
├── handbook/       # 手册模块  
├── journal/        # 日志模块
├── profile/        # 档案模块
├── specification/  # 标准模块
├── meta/           # 元信息（自我映射）
├── AGENTS.md       # Agent 工作指南
├── CONTRIBUTING.md # 贡献指南
└── README.md       # 项目说明
```

## 元信息

- [meta/metadata.md](./metadata.md) - 子模块 Release 状态
- [meta/AGENTS.md](./AGENTS.md) - Meta Agent 指南
- [meta/README.md](./README.md) - Meta 目录说明
- [meta/CONTRIBUTING.md](./CONTRIBUTING.md) - Meta 贡献指南

## 版本约定

- 各子模块独立版本管理
- 主仓库不设版本，仅追踪子模块引用
- Meta 目录由 AI 自动维护
