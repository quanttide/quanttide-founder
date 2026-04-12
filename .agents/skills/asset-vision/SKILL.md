---
name: asset-vision
description: 从 roadmap 和 context 子仓库中识别、提取、移动愿景类文档到 vision 子仓库。基于文档内容的抽象程度和面向未来的特性判断是否属于愿景。
---

# asset-vision

从 `docs/roadmap` 和 `docs/context` 中识别并移动愿景类文档到 `docs/vision`。

## 判断原则

### 属于 vision 的特征
- 抽象的、方向性的、指导性的思考
- 面向未来，讨论"为什么做"和"最终成为什么"
- 创始人个人哲学、价值观、战略愿景
- 教育愿景、运营价值观、组织哲学等

### 属于 roadmap 的特征
- 具体的、可执行的、有时间线的规划
- 讨论"做什么"、"怎么做"、"何时做"
- 产品路线图、组织制度、基础设施规划

### 属于 context 的特征
- 具体参考材料、技术架构
- 认知科学参考、工具使用指南
- 具体的技术实现思路

## 工作流

### 1. 扫描文档

```bash
# 查看 roadmap 所有文件
git -C docs/roadmap ls-files

# 查看 context 所有文件
git -C docs/context ls-files

# 查看 vision 已有结构
git -C docs/vision ls-files
```

### 2. 阅读判断

对每个文件执行以下判断：

```
if 内容包含: 愿景/哲学/价值观/战略方向/身份认同/面向未来的思考:
    → 属于 vision
elif 内容包含: 产品规划/时间表/组织架构/基础设施/具体实践:
    → 属于 roadmap 或 context
```

### 3. 执行移动

```bash
# 创建目标目录
mkdir -p docs/vision/<category>

# 复制文件
cp docs/<source>/<path> docs/vision/<path>

# 从源删除
rm docs/<source>/<path>

# 清理空目录
rmdir docs/<source>/<parent_dir> 2>/dev/null
```

### 4. 提交变更

```bash
# 提交 vision 子仓库
git -C docs/vision add -A
git -C docs/vision commit -m "feat: add <description> docs"

# 提交 source 子仓库
git -C docs/<source> add -A
git -C docs/<source> checkout main
git -C docs/<source> pull
# 如果 detached HEAD，合并提交
git -C docs/<source> merge <commit-hash>

# 提交主仓库
git add docs/vision docs/<source>
git commit -m "chore: move <description> from <source> to vision"
git push --recurse-submodules=on-demand
```
