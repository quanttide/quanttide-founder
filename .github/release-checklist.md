# Release 检查清单

## 预发布检查
- [ ] 所有子模块版本已锁定
- [ ] 通过 CI 测试
- [ ] CHANGELOG.md 版本段已验证
- [ ] 执行过 `npm run build` (如适用)

## Release 创建
```bash
gh release create vX.Y.Z-rc.1 --prerelease --title "vX.Y.Z RC" --notes-file CHANGELOG.md
```

## 最终发布
```bash
gh release edit vX.Y.Z --notes "$(awk '/## vX.Y.Z/{flag=1;next}/## vX.Y.(Z-1)/{flag=0}flag' CHANGELOG.md)"
```
