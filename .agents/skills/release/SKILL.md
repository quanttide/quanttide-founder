# release

发布 Git 仓库 Release。

## 触发词

"发布"、"release"、"发版"

## 规则

- 版本号遵循 semver（MAJOR.MINOR.PATCH）
- 发布前确认工作区干净
- Release notes 只包含对应版本内容
- 发布主仓库前确认所有子模块引用是最新的

## 工作流

### 子模块发布 Release

```bash
# 1. 进入子模块目录
cd <子模块路径>

# 2. 确认 CHANGELOG.md 已更新
cat CHANGELOG.md

# 3. 创建并推送标签
git tag <version>
git push origin <version>

# 4. 创建 GitHub Release
gh release create <version> \
  --title "v<version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/<仓库名>
```

### 主仓库发布 Release

```bash
# 1. 确认所有子模块已更新
git submodule update --remote
git status

# 2. 更新 CHANGELOG.md

# 3. 提交 CHANGELOG.md
git add CHANGELOG.md && git commit -m "docs: update CHANGELOG"

# 4. 创建标签并推送
git tag <version> && git push origin <version>

# 5. 创建 GitHub Release
gh release create <version> \
  --title "v<version>" \
  --notes-file CHANGELOG.md \
  --repo quanttide/quanttide-founder
```
