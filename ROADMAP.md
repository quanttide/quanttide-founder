# Roadmap v0.2.x

本文件记录 quanttide-founder 仓库的未来版本规划。

## 维护类

- **src/qtadmin 分类归档**：整理旧代码不影响开发
  - 从 `src/qtadmin` 提取过时代码模块
  - 归档到 `docs/archive/qtadmin/` 方便参考
  - 保持 `src/qtadmin` 核心代码清晰

## 探索类

### scripts → thera → qtadmin → qtcloud 生命周期

| 步骤 | 状态 | 说明 |
|------|------|------|
| 1. AI 从 meta 元认知摸索需要的脚本到 `scripts/` | ✅ 已验证 | doc_check.py, submodule_sync.py |
| 2. 人类识别后写到 `src/thera/` | ✅ 已验证 | 2026-03-20 迁移完成 |
| 3. 识别功能和价值，分类到 `src/qtadmin/` | ⏳ 待进行 | - |
| 4. 计划成熟后正式固定到 qtcloud-* 系列项目 | ⏳ 待进行 | - |

### 下一步目标

**持续优化 meta 结构，让它可以产出更多更好的 scripts**

- 优化 meta 目录结构，提高 AI 摸索效率
- 积累更多脚本需求到 `meta/roadmap/scripts/`
- 建立脚本质量评估标准

### 探索目标：显性化分类标准

将隐性的问题领域识别显性化，形成可执行的判断依据：

1. **问题领域识别**：从脚本需求中抽象出领域概念
   - 例如：doc_check.py, submodule_sync.py → 数字资产治理
2. **工程方法论识别**：从实践中总结方法论
   - 例如：scripts-to-thera 演进 → 软件工程
3. **分类标准积累**：建立问题领域目录，持续积累识别经验
