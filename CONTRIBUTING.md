# 贡献指南

欢迎贡献本项目！

## 项目结构

本项目为 Git 子模块仓库，包含以下子模块：

### 陈述型记忆

- `archive/` - 过去-事件类：工作归档
- `journal/` - 现在-事件类：工作日志
- `report/` - 现在-语义类：工作报告
- `profile/` - 未来-事件类：工作档案
- `essay/` - 未来-语义类：工作札记

### 程序型记忆

- `usercase/` - 判例法：工作案例
- `handbook/` - 习惯法：工作手册
- `specification/` - 成文法：工程标准
- `platform/` - 宪法：技术平台

## 开发环境

### 克隆仓库

```bash
# 克隆主仓库
git clone https://github.com/quanttide/quanttide-founder.git
cd quanttide-founder

# 初始化并更新子模块
git submodule update --init --recursive
```

### 子模块工作流

#### 进入子模块目录

```bash
cd <子模块名>
# 例如：cd journal
```

#### 在子模块中提交和推送

使用 commitizen 生成规范提交：

```bash
# 1. 在子模块中提交（使用 commitizen）
cz commit
# 或简写
cz c

# 2. 推送子模块
git push origin main

# 3. 返回主仓库提交子模块引用更新
cd ..
git add <子模块名>
cz commit -m "chore: update <子模块名> submodule"
git push origin main
```

**Commitizen 基本用法：**
```bash
# 交互式创建规范提交
cz commit

# 自动版本升级 + 生成 CHANGELOG
cz bump
```

**Commit 类型：**

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add user authentication` |
| `fix` | 修复 bug | `fix: resolve null pointer exception` |
| `docs` | 文档更新 | `docs: update README` |
| `test` | 测试相关 | `test: add unit tests for api` |
| `refactor` | 代码重构 | `refactor: simplify logic` |
| `chore` | 构建/工具 | `chore: update dependencies` |

#### 同步子模块远程更新

当子模块在远程有新的提交或版本时，需要在主仓库中同步更新：

```bash
# 同步指定子模块到远程最新
git submodule update --remote <子模块名>
git add <子模块名>
git commit -m "Update <子模块名> submodule"
git push origin main

# 或同步所有子模块到远程最新
git submodule update --remote --merge
git add .
git commit -m "Update all submodules"
git push origin main
```

### 环境变量

#### 维护 .env.example

当 `.env` 发生任何变更时，立即同步更新 `.env.example`：
- 添加新环境变量
- 修改现有变量值
- 删除环境变量

#### 操作流程

1. **临时权限**：Agent 需要临时权限读取 `.env`
2. **保持占位符**：`.env.example` 使用占位符，不包含真实值
   - 例如：`LLM_API_KEY=your_api_key_here`
3. **提交更新**：`.env.example` 需要提交到仓库

#### 子模块

子模块不需要 .env，仅主仓库需要。

#### 子模块打标签

```bash
# 1. 进入子模块目录
cd journal

# 2. 创建并推送标签
git tag <version>
git push origin <version>

# 3. 返回主仓库（仅在主仓库有变更时提交）
cd ..
git add journal
git commit -m "Update journal submodule"
git push origin main
```

#### 子模块发布 Release

```bash
# 1. 确保子模块已推送，包含 CHANGELOG.md

# 2. 创建 Release
gh release create <version> \
  --title "v<version>" \
  --notes-file <子模块名>/CHANGELOG.md \
  --repo quanttide/<子模块仓库名>

# 例如：journal 子模块
gh release create 0.1.0 \
  --title "v0.1.0" \
  --notes-file journal/CHANGELOG.md \
  --repo quanttide/quanttide-journal-of-founder
```

#### 主仓库发布 Release

**重要**：创建 Release 之前必须先更新 CHANGELOG.md

```bash
# 1. 更新 CHANGELOG.md
# - 添加新的版本号和日期
# - 记录本版本的所有变更
# - 遵循 Keep a Changelog 格式
# - 版本格式：## [版本号] - 日期

# 2. 提交 CHANGELOG.md
git add CHANGELOG.md
git commit -m "docs: update CHANGELOG for v<version>"
git push origin main

# 3. 创建 Git 标签
git tag <version>
git push origin <version>

# 4. 创建 Release（使用 --notes-file 引用整个文件）
gh release create <version> \
  --title "v<version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/quanttide-founder
```

**注意**：`gh release create --notes-file CHANGELOG.md` 会引用整个 CHANGELOG.md 文件。
但 Release notes 应该只包含对应版本的内容。如果 CHANGELOG.md 包含多个版本，
创建 Release 后需要手动编辑 Release notes，只保留对应版本的部分。

**推荐的发布流程**：

1. 在 CHANGELOG.md 中添加新版本内容
2. 提交 CHANGELOG.md
3. 创建 Release（此时 Release notes 包含整个文件）
4. 使用 `gh release edit` 更新 Release notes，只保留对应版本：
   ```bash
   # 提取对应版本的 Release notes
   gh release edit <version> --notes "<版本特定内容>" --repo quanttide/quanttide-founder
   ```

**或者使用临时文件**：

```bash
# 1. 提取对应版本内容到临时文件
# 2. 使用临时文件创建 Release
gh release create <version> \
  --title "v<version>" \
  --notes-file /tmp/<version>-release-notes.md \
  --repo quanttide/quanttide-founder
```

#### 常见错误处理

- **子模块标签已存在**：先删除远程标签 `git push origin :refs/tags/<version>`，再重新推送
- **Release 已存在**：先删除 `gh release delete <version> --repo <repo> --yes`，再重新创建
- **推送失败**：检查网络或使用 `--force`（谨慎使用）

## 注意事项

- 子模块是独立仓库，有自己的提交历史和标签
- 主仓库仅记录子模块的引用（commit SHA）
- 发布 Release 应在子模块仓库进行，而非主仓库
- **Release 标题规范**：GitHub Release 标题必须使用 `v` 前缀（如 v0.1.2），保持一致性

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

## 联系方式

如有疑问，可通过 GitHub Issues 联系维护者。
