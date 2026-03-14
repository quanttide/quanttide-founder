# 元数据

本文件是 quanttide-founder 仓库的自我映射，包含项目状态和子模块信息。

## 项目概述

**quanttide-founder** 是量潮创始人工作文档的元仓库（Meta Repository），通过 Git 子模块管理多个独立的知识库。

## 子模块列表

| 子模块 | 路径 | 描述 | 当前版本 |
|--------|------|------|----------|
| **essay** | `./essay/` | 随笔 - 个人思考和想法的记录 | 0.0.1 |
| **handbook** | `./handbook/` | 手册 - 工作流程和规范文档 | v0.0.2 |
| **journal** | `./journal/` | 日志 - 日常记录和事件记忆 | 0.1.2 |
| **profile** | `./profile/` | 档案 - 工作和知识档案 | 0.2.3 |
| **specification** | `./specification/` | 标准 - 规范和定义文档 | 0.0.1 |

## 子模块 Release 列表

| 子模块 | 仓库 | 最新 Release | Release 日期 |
|--------|------|-------------|-------------|
| **essay** | quanttide-essay-of-founder | [v0.0.1](https://github.com/quanttide/quanttide-essay-of-founder/releases/tag/v0.0.1) | 2026-03-14 |
| **handbook** | quanttide-handbook-of-founder | [v0.0.2](https://github.com/quanttide/quanttide-handbook-of-founder/releases/tag/v0.0.2) | 2026-03-13 |
| **journal** | quanttide-journal-of-founder | [0.1.2](https://github.com/quanttide/quanttide-journal-of-founder/releases/tag/0.1.2) | 2026-03-15 |
| **profile** | quanttide-profile-of-founder | [0.2.3](https://github.com/quanttide/quanttide-profile-of-founder/releases/tag/0.2.3) | 2026-03-07 |
| **specification** | quanttide-specification-of-founder | [0.0.1](https://github.com/quanttide/quanttide-specification-of-founder/releases/tag/0.0.1) | 2026-03-14 |

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

## 版本约定

- 各子模块独立版本管理
- 主仓库不设版本，仅追踪子模块引用
- Meta 目录由 AI 自动维护

## 更新日志

### 2026-03-15

- journal: 添加 knowledge/self UUID，episode 添加 date 字段
- journal: 更新 execute 日志文件

### 2026-03-14

- essay: 创建 Release v0.0.1
- journal: 删除 Draft Release 0.1.0
- specification: 创建 Release 0.0.1
