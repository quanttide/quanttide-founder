# AGENTS.md - Agent 工作指南

## 相关文档

- [贡献指南](CONTRIBUTING.md)（**Agent 维护项目必读**）- 子模块工作流、发布流程
- [README](README.md) - 项目简介

---

## 项目概述

元仓库（meta-repo），基于 Git 子模块管理独立文档仓库。

### 子模块

| 子模块 | 仓库 |
|--------|------|
| profile | quanttide-profile-of-founder |
| specification | quanttide-specification-of-founder |
| essay | quanttide-essay-of-founder |
| handbook | quanttide-handbook-of-founder |
| journal | quanttide-journal-of-founder |

### 项目性质

- 非代码仓库：纯文档项目
- 元仓库：仅管理子模块引用
- 独立发布：子模块独立 Release

---

## 构建命令

### 主仓库

无需构建。子模块克隆：

```bash
git clone --recurse-submodules https://github.com/quanttide/quanttide-founder.git
```

### 子模块

详见各子模块 AGENTS.md。通用命令：

```bash
cd <子模块>
jupyter-book build index.md --site
```

---

## 代码规范

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 人机协作

### 核心原则

1. **最小干预**：仅用户明确请求时操作
2. **原子提交**：每次提交独立完整
3. **验证优先**：修改后运行构建验证
4. **独立发布**：子模块独立仓库 Release

### 工作流

1. 理解需求
2. 确定目标（主仓库 vs 子模块）
3. 执行操作
4. 验证结果
5. 提交推送

详细流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 注意事项

- **不要**在主仓库创建 Release
- **不要**直接在 main 分支修改子模块
- 子模块是独立仓库，有自己的提交历史和标签

---

## 维护目标

支持多模块独立演进与统一发布。
