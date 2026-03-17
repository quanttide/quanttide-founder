# 元数据

本文件是 quanttide-founder 仓库的自我映射，定义了本仓库的元理论、结构规范和项目状态。

## 客体介绍

**quanttide-founder** 是量潮创始人工作文档的元仓库（Meta Repository），通过 Git 子模块管理多个独立的知识库。

### 仓库定位

- **性质**：元仓库（Meta Repository）
- **功能**：集中管理创始人工作文档的各个知识库
- **管理方式**：Git 子模块（Submodule）
- **维护方式**：AI 自动维护

### 核心价值

1. **知识结构化**：通过记忆分类框架将知识系统化
2. **模块化管理**：各子模块独立开发、独立发布
3. **版本追踪**：清晰的版本管理和发布记录
4. **自动化维护**：AI 辅助维护元数据和文档

## 核心框架

### 记忆建模

本仓库采用记忆分类框架作为元理论，定义了组织知识管理的认知基础。

- **陈述型记忆 - 九宫格模型**：将知识按时间（过去/现在/未来）和类型（事件/语义/自我）分类
- **程序型记忆五层体系**：从工作论文到工作章程的五层结构

详见 [记忆建模](./profile/memory.md)

### 仓库结构

本仓库遵循统一的元认知规范，定义了子模块的标准文件结构。

- **标准文件**：README.md、CONTRIBUTING.md、AGENTS.md、CHANGELOG.md
- **元数据目录**：meta/（含 SOUL.md、IDENTITY.md）

详见 [仓库结构](./profile/repo.md)

## 项目状态

### 子模块列表

本仓库包含以下子模块：

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
| **tutorial** | `./tutorial/` | 过去-语义类 | 基础教程 |

详见 [子模块列表](./profile/submodule.md)

### Release 列表

各子模块的最新 Release 信息：

| 子模块 | 仓库 | 最新 Release | Release 日期 |
|--------|------|-------------|-------------|
| **archive** | quanttide-archive-of-founder | [v0.1.0](https://github.com/quanttide/quanttide-archive-of-founder/releases/tag/v0.1.0) | 2026-03-17 |
| **essay** | quanttide-essay-of-founder | [0.0.2](https://github.com/quanttide/quanttide-essay-of-founder/releases/tag/0.0.2) | 2026-03-13 |
| **handbook** | quanttide-handbook-of-founder | [v0.1.0](https://github.com/quanttide/quanttide-handbook-of-founder/releases/tag/v0.1.0) | 2026-03-17 |
| **journal** | quanttide-journal-of-founder | [0.1.2](https://github.com/quanttide/quanttide-journal-of-founder/releases/tag/0.1.2) | 2026-03-13 |
| **profile** | quanttide-profile-of-founder | [v0.2.4](https://github.com/quanttide/quanttide-profile-of-founder/releases/tag/v0.2.4) | 2026-03-17 |
| **specification** | quanttide-specification-of-founder | [0.0.1](https://github.com/quanttide/quanttide-specification-of-founder/releases/tag/0.0.1) | 2026-03-13 |

详见 [Release 列表](./profile/release.md)

## 版本约定

- 各子模块独立版本管理
- 主仓库不设版本，仅追踪子模块引用
- Meta 目录由 AI 自动维护

## 更新日志

详细更新记录见 [journal](./journal/) 目录，按日期命名。

- [2026-03-16](./journal/2026-03-16.md)
- [2026-03-15](./journal/2026-03-15.md)
- [2026-03-14](./journal/2026-03-14.md)
