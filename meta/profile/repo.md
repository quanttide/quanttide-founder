# 仓库结构

本文件记录 quanttide-founder 仓库的结构规范。

## 元认知规范（仓库级）

**仓库级标准文件规范**：`handbook/asset/repo.md`

定义了子模块的标准文件结构：
- README.md - 项目概述
- CONTRIBUTING.md - 贡献指南
- AGENTS.md - Agent 导航
- CHANGELOG.md - 版本历史
- meta/ - 元数据目录（含 SOUL.md、IDENTITY.md）

## 元数据管理原则

### 元数据重构原则
- **职责分离**：将详细信息移到专门文件，主文件保留导航功能
- **引用机制**：通过链接引用详细内容，避免信息冗余
- **结构化组织**：按功能分类组织文件，提高可维护性

### 文件职责分离
- `meta/IDENTITY.md`：负责导航和客体介绍
- `meta/profile/*.md`：负责技术细节的详细说明
