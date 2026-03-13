# QuantTide Founder

元仓库（meta-repo），基于 Git 子模块管理独立文档仓库。

## 子模块

| 子模块 | 仓库 |
|--------|------|
| profile | quanttide-profile-of-founder |
| specification | quanttide-specification-of-founder |
| essay | quanttide-essay-of-founder |
| handbook | quanttide-handbook-of-founder |
| journal | quanttide-journal-of-founder |

## 项目性质

- 非代码仓库：纯文档项目
- 元仓库：仅管理子模块引用
- 独立发布：子模块独立 Release

## 构建

主仓库无需构建。克隆：

```bash
git clone --recurse-submodules https://github.com/quanttide/quanttide-founder.git
```

子模块构建命令见各子模块 AGENTS.md。
