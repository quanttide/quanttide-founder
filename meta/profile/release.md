# Release 列表

本文件记录 quanttide-founder 仓库及其子模块的最新 Release 信息。

## 主仓库 Release

| 仓库 | 最新 Release | Release 日期 |
|------|-------------|-------------|
| **quanttide-founder** | [0.1.0](https://github.com/quanttide/quanttide-founder/releases/tag/0.1.0) | 2026-03-17 |

## 子模块 Release 列表

| 子模块 | 仓库 | 最新 Release | Release 日期 |
|--------|------|-------------|-------------|
| **archive** | quanttide-archive-of-founder | [v0.1.0](https://github.com/quanttide/quanttide-archive-of-founder/releases/tag/v0.1.0) | 2026-03-17 |
| **essay** | quanttide-essay-of-founder | [0.0.2](https://github.com/quanttide/quanttide-essay-of-founder/releases/tag/0.0.2) | 2026-03-13 |
| **handbook** | quanttide-handbook-of-founder | [v0.1.0](https://github.com/quanttide/quanttide-handbook-of-founder/releases/tag/v0.1.0) | 2026-03-17 |
| **journal** | quanttide-journal-of-founder | [0.1.2](https://github.com/quanttide/quanttide-journal-of-founder/releases/tag/0.1.2) | 2026-03-13 |
| **profile** | quanttide-profile-of-founder | [v0.2.4](https://github.com/quanttide/quanttide-profile-of-founder/releases/tag/v0.2.4) | 2026-03-17 |
| **specification** | quanttide-specification-of-founder | [0.0.1](https://github.com/quanttide/quanttide-specification-of-founder/releases/tag/0.0.1) | 2026-03-13 |

## 版本约定

- 各子模块独立版本管理
- 主仓库版本通过 Git 标签管理
- Meta 目录由 AI 自动维护

## Release 流程规范

### 版本管理原则
- **版本标签**：使用 Git 标签管理版本（格式：0.1.0）
- **Release Notes**：遵循 Keep a Changelog 格式
- **元数据更新**：发布后更新 `meta/profile/release.md` 和 `meta/IDENTITY.md`

### 版本控制原则
- **正式发布**：使用正式 Release 而非草稿
- **版本规范**：遵循语义化版本控制规范
- **清理维护**：定期清理不必要的 Release
