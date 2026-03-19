# CHANGELOG

本文件记录 quanttide-founder 仓库的所有重要变更。

## 格式

基于 [Keep a Changelog](https://keepachangelog.com/) 格式：
- `Added`：新增功能
- `Changed`：变更现有功能
- `Deprecated`：即将移除的功能
- `Removed`：已移除的功能
- `Fixed`：Bug 修复
- `Security`：安全相关变更

**工作流程**：创建 Release 之前必须先更新此文件。

---

## [0.1.3] - 2026-03-19

### Changed

- **工作论文修改记忆定义**：
  - 基础教程 → 工作教程：产教融合体系的枢纽，内外部教学和培训的主要资料
  - 发展蓝图 → 工作蓝图：更聚焦于当下的具体问题
  - 发展历程 → 工作历程：更聚焦于具体视角

- **meta vs tutorial 读写规范**：明确 meta 目录给 AI 读，tutorial 子模块给人读

---

## [0.1.2] - 2026-03-18

### Added

- **meta/AGENTS.md**：AI 自我认知文档，由 AI 自维护
- **meta/TOOLS.md**：工具清单，记录项目中使用的开发工具
- **meta/journal/**：工作日志目录，记录 meta 目录的日常变更
  - `meta/journal/README.md`：日志说明和规范
  - `meta/journal/2026-03-18.md`：工作日志
- **meta/tutorial/**：使用指南目录，包含教程和分类哲学
  - `meta/tutorial/index.md`：如何使用创始人的第二大脑指南
  - `meta/tutorial/category.md`：范畴论为基础的分类和命名哲学教程
- **范畴论教程**：从本体论到范畴论的分类哲学教程

### Changed

- **meta 目录重构**：
  - 将 `meta/brochure/company.md` 移到 `meta/tutorial/index.md`
  - 更新 `meta/IDENTITY.md` 目录结构
  - 更新 `meta/README.md` 结构和说明
  - 添加 `meta/journal/` 和 `meta/tutorial/` 到记忆分层模型

- **CHANGELOG 工作流**：
  - 恢复 CHANGELOG.md
  - 标题改为大写（CHANGELOG）
  - 更新 AGENTS.md 和 CONTRIBUTING.md 中的 CHANGELOG 工作流程
  - 明确 Release notes 应该只包含对应版本的内容

- **GitHub Release 清理**：
  - 删除旧版本 Release（v0.0.2, v0.0.1）
  - 更新 0.1.0 和 0.1.1 Release notes 为标准格式
  - 只保留 0.1.0 和 0.1.1 两个 Release

- **子模块更新**：
  - archive: 提交 97cf161，新增 journal/code 和 journal/default
  - journal: 提交 c24fca7，重构 code 目录，添加 code/README.md

### Removed

- **meta/brochure/company.md**：已移到 `meta/tutorial/index.md`

### Fixed

- **CHANGELOG.md**：恢复并更新 Changelog 文件
- **GitHub Release**：修复 0.1.0 Release notes 包含整个 CHANGELOG.md 的问题

---



---

## [0.1.1] - 2026-03-17

### Added

- **meta/brochure/**：宣传册目录
  - `meta/brochure/index.md`：项目宣传册（感性化介绍项目价值和愿景）
  - `meta/brochure/company.md`：内部使用指南（量潮科技成员使用指南）
- **meta/journal/**：工作日志目录
  - `meta/journal/2026-03-17.md`：原始事件记录（按时间线）
- **meta/report/**：工作报告目录
  - 记日报/总结（按记忆分类：事件记忆、语义记忆、自我记忆）
- **meta/bylaw/report.md`：元报告章程（定义报告规范）
- **meta/bylaw/profile.md`：Profile 维护章程
- **meta/bylaw/bylaw.md`：元章程和人机分工

### Changed

- **目录结构重构**：
  - 分离原始事件记录和日报总结
  - `meta/bylaw/journal.md` → `meta/bylaw/report.md`

- **人机分工明确**：
  - bylaw：人类主导制定，AI 总结
  - handbook：AI 主导整理，人类验收
  - profile/journal：AI 自动维护

- **记忆分层模型**：
  - bylaw（最高优先级）→ handbook → profile → report（基础优先级）

### Removed

- **CHANGELOG.md**：已删除（内容已分散到各文件，现已恢复）
- **旧版本标签 v0.0.2**：已删除

---

## [0.1.0] - 2026-03-17

### Added

- **元数据重构**：将详细信息移到 `meta/profile/` 目录
  - `meta/profile/submodule.md`：子模块列表
  - `meta/profile/release.md`：Release 列表
  - `meta/profile/memory.md`：记忆建模知识
  - `meta/profile/repo.md`：仓库结构规范

- **客体介绍**：重构 `meta/IDENTITY.md` 为客体介绍文档
  - 仓库定位和核心价值
  - 核心框架概要
  - 项目状态展示

### Changed

- **子模块更新**：
  - archive: v0.1.0 (2026-03-17)
  - handbook: v0.1.0 (2026-03-17)
  - profile: v0.2.4 (2026-03-17)

- **文档重构**：
  - 将子模块信息移到 `meta/profile/submodule.md`
  - 将 Release 信息移到 `meta/profile/release.md`
  - 将记忆建模知识移到 `meta/profile/memory.md`
  - 将仓库结构知识移到 `meta/profile/repo.md`

### Fixed

- **CHANGELOG.md**：恢复并更新 Changelog 文件
