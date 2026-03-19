# 文档一致性检查脚本

## 概述

检查主仓库中 .gitmodules 和文档中的路径引用是否一致。

## 检查项

### 1. .gitmodules 路径检查

- 验证所有子模块路径是否存在
- 检查子模块 URL 是否可访问

### 2. 文档路径引用检查

- README.md 中的目录结构
- meta/ 下的相对引用
- AGENTS.md 中的路径规范

### 3. 子模块列表完整性

- .gitmodules 中的模块数量
- meta/profile/submodule.md 中的列表
- 实际目录数量

## 输出

```bash
# 一致性报告
检查项          状态    详情
.gitmodules    ✅     11 个子模块
README.md      ✅     路径已更新
submodule.md   ⚠️     缺少 1 个引用
```

## 实现位置

- **阶段一（摸索）**：`meta/roadmap/doc-check.md`
- **阶段二（thera）**：`src/thera/scripts/doc-check.py`
