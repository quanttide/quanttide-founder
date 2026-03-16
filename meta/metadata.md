# 元数据

本文件是 quanttide-founder 仓库的自我映射，包含项目状态和子模块信息。

## 核心框架（事实源）

**记忆分类框架**是本项目的元理论，定义了组织知识管理的认知基础。

### 陈述型记忆 - 九宫格模型

| | 事件类 | 语义类 | 自我类 |
|------|--------|--------|--------|
| **过去** | Archive（工作归档） | Tutorial（基础教程） | History（发展历程） |
| **现在** | Journal（工作日志） | Report（工作报告） | Brochure（宣传册） |
| **未来** | Profile（工作档案） | Essay（工作札记） | Roadmap（发展蓝图） |

### 程序型记忆五层体系

| 层次 | 英文名称 | 中文名称 | 法律隐喻 | 说明 |
|------|----------|----------|----------|------|
| 5 | Paper | 工作论文 | 立法原理 | 系统总结归纳基本原理与方法论，无直接约束力 |
| 4 | Usecase | 工作案例 | 精选判例 | 来源于具体实践案例的积累与复用 |
| 3 | Handbook | 工作手册 | 权威汇编 | 对实践和原理的系统化整理 |
| 2 | Specification | 工程标准 | 程序性法律 | 系统性程序规范，具有约束力 |
| 1 | Bylaw | 工作章程 | 宪法 | 规定基本原则与权责划分 |

**事实源**：`paper/meta/memory.md`

## 项目概述

**quanttide-founder** 是量潮创始人工作文档的元仓库（Meta Repository），通过 Git 子模块管理多个独立的知识库。

## 子模块列表

| 子模块 | 路径 | 定位 | 描述 |
|--------|------|------|------|
| **archive** | `./archive/` | 过去-事件类 | 工作归档 |
| **essay** | `./essay/` | 未来-语义类 | 工作札记 |
| **handbook** | `./handbook/` | 程序型-习惯法 | 工作手册 |
| **journal** | `./journal/` | 现在-事件类 | 工作日志 |
| **paper** | `./paper/` | 程序型-权威法理 | 工作论文 |
| **platform** | `./platform/` | 程序型-宪法 | 技术平台 |
| **profile** | `./profile/` | 未来-事件类 | 工作档案 |
| **report** | `./report/` | 现在-语义类 | 工作报告 |
| **specification** | `./specification/` | 程序型-成文法 | 工程标准 |
| **usercase** | `./usercase/` | 程序型-判例法 | 工作案例 |

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
├── archive/         # 过去-事件类：工作归档
├── essay/          # 未来-语义类：工作札记
├── handbook/       # 程序型-习惯法：工作手册
├── journal/        # 现在-事件类：工作日志
├── paper/          # 程序型-权威法理：工作论文
├── platform/       # 程序型-宪法：技术平台
├── profile/        # 未来-事件类：工作档案
├── report/         # 现在-语义类：工作报告
├── specification/  # 程序型-成文法：工程标准
├── usercase/       # 程序型-判例法：工作案例
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

### 2026-03-16

- 添加 paper 子模块（工作论文）
- 更新元数据：添加核心框架（记忆分类框架）事实源
- 更新子模块列表：按九宫格和程序型记忆分类
- 更新目录结构

### 2026-03-15

- journal: 添加 knowledge/self UUID，episode 添加 date 字段
- journal: 更新 execute 日志文件

### 2026-03-14

- essay: 创建 Release v0.0.1
- journal: 删除 Draft Release 0.1.0
- specification: 创建 Release 0.0.1
