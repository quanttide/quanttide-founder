# AGENTS.md - Agent 工作指南

## 相关文档

- [贡献指南](CONTRIBUTING.md)（**Agent 维护项目必读**）
- [README](README.md) - 项目简介

> **提示**：Agent 维护项目时应经常参考 [CONTRIBUTING.md](CONTRIBUTING.md) 了解子模块工作流。

---

## 项目概述

本项目是**量潮创始人知识库**的元仓库（meta-repo），基于 Git 子模块管理多个独立文档仓库。

### 子模块列表

| 子模块 | 仓库 | 说明 |
|--------|------|------|
| profile | quanttide-profile-of-founder | 创始人档案 |
| specification | quanttide-specification-of-founder | 标准规范 |
| essay | quanttide-essay-of-founder | 随笔文章 |
| handbook | quanttide-handbook-of-founder | 手册指南 |
| journal | quanttide-journal-of-founder | 日志记录 |

### 项目性质

- **非代码仓库**：纯文档项目，无后端服务
- **元仓库**：仅管理子模块引用，不直接包含内容
- **独立发布**：每个子模块独立仓库、独立 Release

---

## 构建命令

### 主仓库

主仓库无需构建，仅包含子模块引用。

```bash
# 克隆仓库（含子模块）
git clone --recurse-submodules https://github.com/quanttide/quanttide-founder.git

# 或分开执行
git clone https://github.com/quanttide/quanttide-founder.git
git submodule update --init --recursive

# 拉取子模块更新
git submodule update --remote --merge
```

### 子模块构建

各子模块基于 Jupyter Book 构建，构建命令在各自 AGENTS.md 中：

```bash
# 进入子模块
cd <子模块名>

# 构建 HTML
jupyter-book build index.md --site

# 清理构建
jupyter-book clean .
```

---

## 代码规范

### 本仓库

本仓库仅包含配置文件，遵循通用规范：

- `.gitignore` - 使用标准 Python/JupyterBook/OS 忽略规则
- `.gitmodules` - 子模块配置，使用 HTTPS URL
- `CONTRIBUTING.md` - 中文编写，遵循贡献指南

### 子模块文档规范

子模块为 Markdown 文档项目，遵循以下规范：

#### Markdown 风格

- 标题使用中文或英文，**保持一致性**
- 列表使用 `-` 或 `1.` ，**保持统一**
- 代码块标注语言：` ```python `, ` ```bash ` 等
- 链接使用相对路径：`[文字](目录/文件.md)`

#### 文件命名

- 使用小写字母
- 单词间用下划线 `_` 分隔
- 示例：`think/index.md`, `llm_learning.md`

#### 目录结构

```
板块名/
├── index.md        # 板块入口，内容摘要
├── README.md       # 板块说明（可选）
├── 子1.md
└── 子目录主题/
    ├── index.md
    └── 内容.md
```

---

## 人机协作范式

### 核心原则

1. **最小干预**：仅在用户明确请求时操作
2. **原子提交**：每次提交应包含完整且独立的变更
3. **验证优先**：完成修改后验证构建（子模块）
4. **独立发布**：子模块独立仓库，独立 Release

### 工作流程

1. **理解需求**：明确用户的具体任务和范围
2. **确定目标**：判断是修改主仓库还是子模块
3. **执行操作**：按规范进行修改
4. **验证结果**：运行构建验证（子模块）
5. **提交推送**：创建提交并推送到远程

---

## 子模块工作流

### 修改子模块

```bash
# 1. 进入子模块目录
cd journal

# 2. 创建分支
git checkout -b feature/xxx

# 3. 进行修改
# ... 修改内容 ...

# 4. 提交并推送
git add .
git commit -m "commit message"
git push origin feature/xxx

# 5. 返回主仓库更新引用
cd ..
git add journal
git commit -m "Update journal submodule"
git push origin main
```

### 子模块发布 Release

```bash
# 1. 进入子模块，确保 CHANGELOG.md 已更新
cd journal

# 2. 创建标签
git tag <version>
git push origin <version>

# 3. 创建 Release（使用 CHANGELOG 作为 notes）
gh release create <version> \
  --title "Release <version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/quanttide-journal-of-founder

# 4. 返回主仓库（如有变更）
cd ..
git add journal
git commit -m "Update journal submodule"
git push origin main
```

### 常见错误处理

| 错误 | 解决方案 |
|------|----------|
| 子模块标签已存在 | `git push origin :refs/tags/<version>` 删除后重推 |
| Release 已存在 | `gh release delete <version> --repo <repo> --yes` 删除后重建 |
| 推送失败 | 检查网络或 `--force`（谨慎） |
| 子模块 detached HEAD | `git checkout main` 切换分支 |

---

## 版本规范

### 版本号语义

遵循语义化版本（SemVer）：`主版本.次版本.修订号`

### 版本更新规则

| 类型 | 场景 | 示例 |
|------|------|------|
| 修订号 | 错别字修正、格式调整 | 0.0.1 → 0.0.2 |
| 次版本 | 新增内容、新增板块 | 0.0.1 → 0.1.0 |
| 主版本 | 架构调整、板块边界变化 | 0.1.0 → 1.0.0 |

---

## 注意事项

- **不要**在主仓库创建 Release，主仓库仅管理子模块引用
- **不要**直接在 main 分支修改子模块，使用分支工作流
- 子模块是独立仓库，有自己的提交历史和标签
- 更新目录结构后需同步更新 index.md、README.md、_toc.yml 三处（子模块）

---

## 维护目标

构建创始人知识库的协作框架，支持多模块独立演进与统一发布。
