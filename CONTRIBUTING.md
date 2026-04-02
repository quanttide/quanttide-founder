# 贡献指南

## 提交规范

使用 commitizen 生成规范提交：

```bash
cz commit
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

## 人机协作原则

1. **最小干预**：仅用户明确请求时操作
2. **原子提交**：每次提交独立完整
3. **验证优先**：修改后运行构建验证
