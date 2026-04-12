# 贡献指南

## 提交规范

提交信息遵循 Conventional Commits 格式：

```bash
git commit -m "<type>: <description>"
```

**Commit 类型：**

| 类型 | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复 bug |
| `docs` | 文档更新 |
| `test` | 测试相关 |
| `refactor` | 代码重构 |
| `chore` | 构建/工具 |

## 发布流程

### 子模块发布 Release

```bash
# 1. 进入子模块目录
cd <子模块名>

# 2. 创建并推送标签
git tag <version>
git push origin <version>

# 3. 创建 Release
gh release create <version> \
  --title "v<version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/<仓库名>
```

### 主仓库发布 Release

```bash
# 1. 更新 CHANGELOG.md
# 2. 提交 CHANGELOG.md
git add CHANGELOG.md && git commit -m "docs: update CHANGELOG"

# 3. 创建标签并推送
git tag <version> && git push origin <version>

# 4. 创建 Release
gh release create <version> \
  --title "v<version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/quanttide-founder
```

## Git Submodule 维护

### 添加子模块

- 新仓库必须先有至少一次提交（不能是空仓库），否则 `git submodule add` 会失败
- 添加后需要手动 `git add` 子模块引用再提交主仓库

```bash
git submodule add <url> <path>
git add <path>
git commit -m "feat: add <name> submodule"
```

### 移除子模块

```bash
# 1. 取消初始化
git submodule deinit -f <path>

# 2. 从 Git 中移除
git rm -f <path>

# 3. （可选）删除云端仓库
gh repo delete <owner>/<repo> --yes
```

- `.gitmodules` 会自动更新
- `.git/config` 中的历史配置不会自动清理，需要手动清理避免警告

### 更新子模块

```bash
# 更新所有子模块到最新
git submodule update --remote

# 更新指定子模块
git submodule update --remote <path>
```

- 子模块可能进入 detached HEAD 状态，此时提交会丢失。切换回 main 分支后再操作更安全
- 网络问题（TLS 握手失败、502）会中断更新，通常与代理有关

### 提交变更

子模块变更分两层：

1. **子仓库内部**：在子仓库目录下 `git add` 和 `git commit`
2. **主仓库**：`git add <submodule-path>` 记录子模块的 commit hash

推送：

```bash
# 一次性推送所有子仓库和主仓库
git push --recurse-submodules=on-demand

# 若子仓库落后，需先单独推送
git -C <path> push
```

### 合并冲突处理

- 子模块冲突不能简单 `rebase`，推荐 `merge`
- 冲突类型及解决：

| 冲突类型 | 解决方式 |
|----------|----------|
| `.gitmodules` 内容冲突 | 手动编辑文件解决 |
| 子模块 commit hash 冲突 | 进入子模块合并，然后 `git add <path>` |
| 删除/修改冲突 | 按需保留或删除 |

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `non-fast-forward` 推送失败 | 子仓库落后远端 | 先 `git pull` 再 `push` |
| `locally modified submodule` | 子模块有未提交变更 | 先在子仓库提交 |
| `no merge base` | 两边历史分叉 | 进入子模块找到共同祖先 |
| detached HEAD 提交丢失 | 在分离头指针上提交 | 切换到 main 分支重新提交 |
| `.gitmodules` 重复配置警告 | `.git/config` 残留旧配置 | `git config --remove-section submodule.<name>` 清理 |

## 人机协作原则

1. **最小干预**：仅用户明确请求时操作
2. **原子提交**：每次提交独立完整
3. **验证优先**：修改后运行构建验证
