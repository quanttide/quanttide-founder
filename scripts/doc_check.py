#!/usr/bin/env python3
"""
文档一致性检查脚本

检查主仓库中 .gitmodules 和文档中的路径引用是否一致。
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def check_gitmodules():
    """检查 .gitmodules 中的子模块路径是否存在"""
    gitmodules_path = REPO_ROOT / ".gitmodules"
    if not gitmodules_path.exists():
        return False, "文件不存在"
    
    modules = {}
    with open(gitmodules_path) as f:
        content = f.read()
        for match in re.finditer(r'path\s*=\s*(.+)', content):
            path = match.group(1).strip()
            modules[path] = (REPO_ROOT / path).exists()
    
    all_exist = all(modules.values())
    details = f"{len(modules)} 个子模块"
    missing = [p for p, e in modules.items() if not e]
    if missing:
        details += f", 缺失: {', '.join(missing)}"
    return all_exist, details


def check_readme_paths():
    """检查 README.md 中的路径是否存在"""
    readme_path = REPO_ROOT / "README.md"
    if not readme_path.exists():
        return False, "文件不存在"
    
    with open(readme_path) as f:
        content = f.read()
    
    paths = re.findall(r'`([\w/.-]+)/`', content)
    missing = []
    for path in paths:
        full_path = REPO_ROOT / path
        if not full_path.exists() and path not in ['AGENTS.md', 'CONTRIBUTING.md', 'README.md', 'CHANGELOG.md', 'ROADMAP.md']:
            missing.append(path)
    
    all_exist = len(missing) == 0
    details = f"{len(paths)} 个路径" if all_exist else f"缺失: {', '.join(missing)}"
    return all_exist, details


def check_submodule_list():
    """检查 submodule.md 中的列表是否完整"""
    submodule_md = REPO_ROOT / "meta" / "profile" / "submodule.md"
    if not submodule_md.exists():
        return False, "文件不存在"
    
    with open(submodule_md) as f:
        content = f.read()
    
    listed_paths = set(re.findall(r'`([^`]+)/`', content))
    
    gitmodules_path = REPO_ROOT / ".gitmodules"
    if gitmodules_path.exists():
        with open(gitmodules_path) as f:
            git_content = f.read()
        git_paths = re.findall(r'path\s*=\s*(.+)', git_content)
        git_modules = set(p.strip() for p in git_paths)
        
        missing = git_modules - listed_paths
        all_match = len(missing) == 0
        details = f"{len(listed_paths)} 个路径" if all_match else f"缺少: {', '.join(missing)}"
        return all_match, details
    
    return False, "无法读取 .gitmodules"


def main():
    print("=" * 60)
    print("文档一致性检查")
    print("=" * 60)
    print()
    
    checks = [
        (".gitmodules", check_gitmodules),
        ("README.md", check_readme_paths),
        ("submodule.md", check_submodule_list),
    ]
    
    results = []
    for name, check_func in checks:
        status, details = check_func()
        symbol = "✅" if status else "⚠️"
        results.append((name, status, details))
        print(f"{symbol} {name:20s} {details}")
    
    print()
    print("=" * 60)
    all_pass = all(r[1] for r in results)
    if all_pass:
        print("✅ 所有检查通过")
    else:
        print("⚠️ 存在不一致，请检查")
    print("=" * 60)
    
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
