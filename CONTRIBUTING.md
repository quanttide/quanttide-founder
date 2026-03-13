# 贡献指南

欢迎贡献本项目！

## 项目结构

本项目为 Git 子模块仓库，包含以下子模块：

- `essay/` - 随笔板块
- `handbook/` - 手册板块
- `journal/` - 日志板块
- `profile/` - 档案板块
- `specification/` - 标准板块

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

```bash
# 1. 在子模块中提交
git add .
git commit -m "commit message"

# 2. 推送子模块
git push origin main

# 3. 返回主仓库提交子模块引用更新
cd ..
git add <子模块名>
git commit -m "Update <子模块名> submodule"
git push origin main
```

### 环境变量

#### 维护 .env.example

当 `.env` 有变更时，同步更新 `.env.example`：

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
  --title "Release <version>" \
  --notes-file <子模块名>/CHANGELOG.md \
  --repo quanttide/<子模块仓库名>

# 例如：journal 子模块
gh release create 0.1.0 \
  --title "Release 0.1.0" \
  --notes-file journal/CHANGELOG.md \
  --repo quanttide/quanttide-journal-of-founder
```

#### 常见错误处理

- **子模块标签已存在**：先删除远程标签 `git push origin :refs/tags/<version>`，再重新推送
- **Release 已存在**：先删除 `gh release delete <version> --repo <repo> --yes`，再重新创建
- **推送失败**：检查网络或使用 `--force`（谨慎使用）

## 注意事项

- 子模块是独立仓库，有自己的提交历史和标签
- 主仓库仅记录子模块的引用（commit SHA）
- 发布 Release 应在子模块仓库进行，而非主仓库

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
