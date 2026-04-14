---
name: devops-release
description: 发布 Git 仓库 Release，支持子模块和主仓库两种发布流程。创建 tag、推送远端、生成 GitHub Release。
---

# devops-release

发布 Git 仓库 Release。

## 规则

- 版本号遵循 semver（MAJOR.MINOR.PATCH）
- 发布前确认工作区干净
- Release notes 只包含对应版本内容
- 发布主仓库前确认所有子模块引用是最新的

## 工作流

### 预发布检查
- [ ] 所有子模块版本已锁定
- [ ] 通过 CI 测试
- [ ] CHANGELOG.md 版本段已验证
- [ ] 执行过 `npm run build` (如适用)

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
# 1. 创建预发布版本（可选）
gh release create vX.Y.Z-rc.1 --prerelease --title "vX.Y.Z RC" --notes-file CHANGELOG.md

# 2. 确认所有子模块已更新
git submodule update --remote
git status

# 3. 更新 CHANGELOG.md

# 4. 提交 CHANGELOG.md
git add CHANGELOG.md && git commit -m "docs: update CHANGELOG"

# 5. 创建标签并推送
git tag <version> && git push origin <version>

# 6. 创建 GitHub Release
gh release create <version> \
  --title "v<version>" \
  --notes "$(awk '/## vX.Y.Z/{flag=1;next}/## vX.Y.(Z-1)/{flag=0}flag' CHANGELOG.md)" \
  --repo quanttide/quanttide-founder
```
