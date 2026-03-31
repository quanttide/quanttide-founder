# 子模块自动提交脚本

## 脚本列表

### 1. `commit_submodules.py` - 基础版

基于规则自动生成 commit message。

**用法:**
```bash
# 预览模式（不执行实际变更）
python scripts/commit_submodules.py --dry-run

# 自动提交所有子模块
python scripts/commit_submodules.py

# 仅提交不推送
python scripts/commit_submodules.py --no-push

# 只处理指定的子模块
python scripts/commit_submodules.py --submodule qtadmin

# 跳过确认直接执行
python scripts/commit_submodules.py -y
```

### 2. `commit_submodules_ai.py` - AI 增强版

使用 AI 生成更准确的 commit message（需要配置 API）。

**用法:**
```bash
# 配置 API（可选）
export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="https://api.openai.com/v1"

# 使用 AI 生成 commit message
python scripts/commit_submodules_ai.py

# 没有 API 时自动降级到规则生成
python scripts/commit_submodules_ai.py
```

## 功能特性

- ✅ 自动检测所有子模块的变更
- ✅ 分析变更内容生成 commit message
- ✅ 支持 Conventional Commits 规范
- ✅ 预览模式 (--dry-run)
- ✅ 选择性推送 (--no-push)
- ✅ 过滤指定子模块 (--submodule)
- ✅ 批量确认执行 (-y)

## Commit Message 规范

脚本遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | `feat: add user authentication` |
| `fix` | 修复 bug | `fix: resolve null pointer exception` |
| `docs` | 文档更新 | `docs: update README` |
| `test` | 测试相关 | `test: add unit tests for api` |
| `refactor` | 代码重构 | `refactor: simplify logic` |
| `chore` | 构建/工具 | `chore: update dependencies` |

## 工作流程

1. 扫描所有子模块的 git 状态
2. 检测有变更的子模块
3. 分析变更文件生成 commit message
4. 逐个提交并推送到远程仓库
5. 更新父仓库的子模块引用

## 示例输出

```
📦 发现 8 个子模块

分析：src/qtadmin
  📝 test: add cli integration tests
分析：docs/journal
  📝 docs: update 2024-03 journal entries

共 2 个子模块需要提交

处理：src/qtadmin
  ✓ 已提交：qtadmin
  ✓ 已推送：qtadmin

处理：docs/journal
  ✓ 已提交：journal
  ✓ 已推送：journal

==================================================
✅ 完成：2/2 个子模块

📌 父仓库有待提交的子模块引用更新:
   git commit -m "chore: update 2 submodules"
   git push
```

## 注意事项

- 确保子模块已正确初始化 (`git submodule update --init`)
- 确保有远程仓库的推送权限
- AI 版本需要网络连接和 API 密钥
- 推送超时时间设置为 60 秒
