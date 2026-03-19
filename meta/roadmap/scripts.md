# Scripts 迭代计划

本文件记录 AI 从元认知出发摸索的脚本需求，遵循 scripts → thera → qtadmin → qtcloud 的生命周期。

## 阶段一：Scripts（AI 摸索期）

AI 在 meta 中记录自己需要的工具设想。

### 1. 子模块同步脚本

**问题**：每次手动执行 `git submodule update --remote --merge` 繁琐。

**设想**：
- 自动检测哪些子模块有远程更新
- 生成变更摘要
- 支持选择性同步

**位置**：`meta/roadmap/scripts/submodule-sync.md`

### 2. CHANGELOG 生成脚本

**问题**：手动维护 CHANGELOG 容易遗漏。

**设想**：
- 从 git log 自动提取 commit message
- 按子模块分类
- 生成符合 Keep a Changelog 格式的草稿

**位置**：`meta/roadmap/scripts/changelog-gen.md`

### 3. 版本发布脚本

**问题**：发布流程步骤多（更新 CHANGELOG → commit → tag → push → release）。

**设想**：
- 交互式引导发布流程
- 自动验证 CHANGELOG 格式
- 自动创建 tag 和 release

**位置**：`meta/roadmap/scripts/release.md`

### 4. 文档一致性检查

**问题**：目录结构变更后容易遗漏更新引用。

**设想**：
- 检查 .gitmodules 和文档中的路径引用是否一致
- 检查子模块列表是否完整
- 生成不一致报告

**位置**：`meta/roadmap/scripts/doc-check.md`

## 阶段二：Thera（人类识别期）

人类识别脚本价值后，写入 src/thera。

## 阶段三：Qtadmin（价值分类期）

识别脚本功能和价值，分类管理。

## 阶段四：Qtcloud（正式固定期）

成熟后成为 qtcloud 系列项目。
