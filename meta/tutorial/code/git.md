# Git 人机协作指南

如何指导 AI 做 Git 操作，以及如何检查 AI 的工作。

## 指导 AI

### 给出明确目标

- "更新所有子模块"
- "提交并推送这次修改"
- "解决这个冲突"

### 提供必要信息

- 告诉 AI 你修改了哪些文件
- 指定提交信息的内容
- 说明是否需要使用代理

### 分步骤进行

- 复杂操作拆成多步
- 每步确认结果后再继续
- 避免一次性给太多任务

## 检查 AI 的工作

### 提交前

- `git status`：确认 AI 修改了正确的文件
- `git diff`：确认修改内容符合预期

### 提交后

- `git log --oneline -1`：确认提交信息正确
- `git ls-remote origin main`：确认推送成功

### 子模块操作后

子模块容易出错，必须额外检查：

1. 进入子模块检查：
   ```bash
   cd <子模块目录>
   git log --oneline -1
   git ls-remote origin main
   ```

2. 返回主仓库检查：
   ```bash
   cd ..
   git diff <子模块目录>
   ```

## 验证链接

每次提交推送后，打开 GitHub 检查：

- 主仓库：`https://github.com/quanttide/quanttide-founder`
- 子模块：`https://github.com/quanttide/quanttide-<子模块名>-of-founder`

确认修改内容已同步到远程。

## 常见问题

### AI 推送失败

告诉 AI："使用代理重试"，或者自己执行：
```bash
export https_proxy=http://127.0.0.1:7897
git push
```

### 子模块分离头指针

告诉 AI："先切换到 main 分支"，然后重新操作。

### 冲突

告诉 AI："解决冲突后继续"，或者自己手动解决。
