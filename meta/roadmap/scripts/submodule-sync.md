# 子模块同步脚本

## 概述

自动检测子模块远程更新，生成变更摘要，支持选择性同步。

## 功能

### 1. 检测远程更新

```bash
python scripts/submodule_sync.py --check
```

输出：
```
检测到 3 个子模块有更新：
  docs/journal     376cd5e → 7c38b48 (5 commits)
  docs/tutorial   2abda62 → c278c69 (2 commits)
  src/thera       0f22233 → 1a2b3c4 (1 commit)
```

### 2. 查看变更

```bash
python scripts/submodule_sync.py --diff <子模块>
```

### 3. 选择性同步

```bash
python scripts/submodule_sync.py --sync docs/journal,docs/tutorial
```

### 4. 全部同步

```bash
python scripts/submodule_sync.py --sync-all
```

## 实现

```python
import subprocess
import re
from pathlib import Path

def get_remote_commits():
    """获取所有子模块的远程最新提交"""
    result = subprocess.run(
        ["git submodule foreach", "git fetch --dry-run"],
        capture_output=True, text=True
    )
    # 解析输出，提取有更新的子模块

def sync_submodule(path, verbose=False):
    """同步指定子模块"""
    subprocess.run(["git", " submodule", "update", "--remote", "--merge", path])

def main():
    # 支持 --check, --diff, --sync, --sync-all 参数
```

## 演进路径

- **阶段一（摸索）**：`meta/roadmap/scripts/submodule-sync.md`
- **阶段二（thera）**：写入 `src/thera/scripts/submodule_sync.py`
- **阶段三（qtadmin）**：分类到 `src/qtadmin/scripts/`
- **阶段四（qtcloud）**：成熟后成为独立项目
