#!/usr/bin/env python3
"""
自动提交所有子模块的变更并生成 commit message

用法:
    python scripts/commit_submodules.py [--dry-run] [--no-push] [--message-prefix]

功能:
    1. 遍历所有子模块
    2. 检测有变更的子模块
    3. 分析变更内容生成 commit message
    4. 自动提交并推送到远程
    5. 更新父仓库的子模块引用
"""

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class SubmoduleChange:
    """子模块变更信息"""
    path: str
    status: str  # M = modified, U = untracked, A = added
    files_changed: list[str]
    commit_message: str


def run_git_command(cmd: list[str], cwd: Optional[Path] = None) -> tuple[int, str, str]:
    """运行 git 命令，返回 (returncode, stdout, stderr)"""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=30
    )
    return result.returncode, result.stdout, result.stderr


def get_submodule_paths() -> list[str]:
    """获取所有子模块路径"""
    _, output, _ = run_git_command(["git", "config", "--file", ".gitmodules", "--get-regexp", "path"])
    paths = []
    for line in output.strip().split("\n"):
        if line:
            parts = line.split()
            if len(parts) >= 2:
                paths.append(parts[1])
    return paths


def check_submodule_status(submodule_path: Path) -> tuple[bool, list[str]]:
    """
    检查子模块状态
    返回：(has_changes, changed_files)
    """
    if not submodule_path.exists():
        return False, []
    
    # 检查 git 状态
    returncode, stdout, _ = run_git_command(
        ["git", "status", "--porcelain"],
        cwd=submodule_path
    )
    
    if returncode != 0:
        # 可能不是 git 仓库
        return False, []
    
    changed_files = []
    for line in stdout.strip().split("\n"):
        if line.strip():
            # 解析状态行
            status = line[:2].strip()
            filename = line[3:] if len(line) > 3 else ""
            if filename:
                changed_files.append(f"{status}:{filename}")
    
    return len(changed_files) > 0, changed_files


def analyze_changes(submodule_path: Path, changed_files: list[str]) -> str:
    """分析变更并生成 commit message"""
    # 获取变更类型
    added = [f for f in changed_files if f.startswith("A ") or f.startswith("??")]
    modified = [f for f in changed_files if f.startswith("M ") or f.startswith(" M")]
    deleted = [f for f in changed_files if f.startswith("D ") or f.startswith(" D")]
    
    # 获取文件扩展名统计
    extensions = {}
    for f in changed_files:
        filename = f.split(":", 1)[1] if ":" in f else f
        ext = Path(filename).suffix.lower()
        extensions[ext] = extensions.get(ext, 0) + 1
    
    # 生成 commit message
    parts = []
    
    # 根据变更的文件类型生成前缀
    if ".py" in extensions:
        prefix = "feat" if any("test" in f for f in changed_files) else "fix"
        if any("test" in f for f in changed_files):
            prefix = "test"
        elif any("doc" in f.lower() for f in changed_files):
            prefix = "docs"
        elif any("refactor" in f.lower() for f in changed_files):
            prefix = "refactor"
    elif ".md" in extensions:
        prefix = "docs"
    else:
        prefix = "chore"
    
    # 生成简短描述
    if added and not modified and not deleted:
        action = "add"
    elif deleted and not added and not modified:
        action = "remove"
    elif modified:
        action = "update"
    else:
        action = "change"
    
    # 根据文件类型生成描述
    if ".py" in extensions:
        subject = "python files"
    elif ".md" in extensions:
        subject = "documentation"
    elif ".json" in extensions:
        subject = "configuration"
    elif ".yaml" in extensions or ".yml" in extensions:
        subject = "workflow files"
    else:
        subject = "files"
    
    # 如果有特定目录，加入目录名
    dirs = set()
    for f in changed_files:
        filename = f.split(":", 1)[1] if ":" in f else f
        parent = str(Path(filename).parent)
        if parent and parent != ".":
            dirs.add(parent.split("/")[0])
    
    if dirs:
        dir_list = sorted(dirs)
        if len(dir_list) == 1:
            subject = f"{dir_list[0]}: {subject}"
        elif len(dir_list) <= 3:
            subject = f"{', '.join(dir_list)}: {subject}"
        else:
            subject = f"multiple dirs: {subject}"
    
    # 生成完整的 commit message
    commit_msg = f"{prefix}: {action} {subject}"
    
    # 添加详细变更列表（如果文件不多）
    if len(changed_files) <= 10:
        commit_msg += "\n\nChanged files:\n"
        for f in changed_files:
            commit_msg += f"  - {f}\n"
    
    return commit_msg.strip()


def commit_submodule(
    submodule_path: Path,
    commit_message: str,
    dry_run: bool = False,
    push: bool = True
) -> bool:
    """提交子模块变更"""
    if dry_run:
        print(f"[DRY-RUN] 提交 {submodule_path}: {commit_message.split(chr(10))[0]}")
        return True
    
    # git add
    returncode, _, stderr = run_git_command(
        ["git", "add", "-A"],
        cwd=submodule_path
    )
    if returncode != 0:
        print(f"  错误：git add 失败 - {stderr}")
        return False
    
    # git commit
    returncode, _, stderr = run_git_command(
        ["git", "commit", "-m", commit_message],
        cwd=submodule_path
    )
    if returncode != 0:
        if "nothing to commit" in stderr:
            print(f"  跳过：{submodule_path} 无变更")
            return True
        print(f"  错误：git commit 失败 - {stderr}")
        return False
    
    print(f"  已提交：{submodule_path}")
    
    # git push
    if push:
        returncode, _, stderr = run_git_command(
            ["git", "push", "origin", "HEAD"],
            cwd=submodule_path
        )
        if returncode != 0:
            print(f"  警告：git push 失败 - {stderr}")
            return True  # 提交成功，推送失败也算部分成功
        print(f"  已推送：{submodule_path}")
    
    return True


def update_parent_submodule_reference(submodule_path: str, push: bool = True) -> bool:
    """更新父仓库中的子模块引用"""
    # git add 子模块
    returncode, _, stderr = run_git_command(
        ["git", "add", submodule_path]
    )
    if returncode != 0:
        print(f"  错误：父仓库 git add 失败 - {stderr}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="自动提交所有子模块的变更"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式，不执行实际变更"
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="仅提交不推送"
    )
    parser.add_argument(
        "--message-prefix",
        type=str,
        default="",
        help="commit message 前缀"
    )
    parser.add_argument(
        "--submodule",
        type=str,
        default="",
        help="只处理指定的子模块"
    )
    
    args = parser.parse_args()
    
    # 获取项目根目录
    project_root = Path.cwd()
    
    # 获取所有子模块路径
    submodule_paths = get_submodule_paths()
    
    if args.submodule:
        submodule_paths = [p for p in submodule_paths if args.submodule in p]
    
    if not submodule_paths:
        print("未找到子模块")
        sys.exit(0)
    
    print(f"发现 {len(submodule_paths)} 个子模块")
    print()
    
    # 检查每个子模块的状态
    changes: list[SubmoduleChange] = []
    
    for path in submodule_paths:
        submodule_path = project_root / path
        has_changes, changed_files = check_submodule_status(submodule_path)
        
        if has_changes:
            commit_message = analyze_changes(submodule_path, changed_files)
            if args.message_prefix:
                commit_message = f"{args.message_prefix}: {commit_message}"
            
            changes.append(SubmoduleChange(
                path=path,
                status="M",
                files_changed=changed_files,
                commit_message=commit_message
            ))
            print(f"发现变更：{path}")
            for f in changed_files[:5]:  # 只显示前 5 个
                print(f"    {f}")
            if len(changed_files) > 5:
                print(f"    ... 还有 {len(changed_files) - 5} 个文件")
            print()
    
    if not changes:
        print("所有子模块都是最新的，没有需要提交的变更")
        sys.exit(0)
    
    print(f"\n共 {len(changes)} 个子模块需要提交\n")
    
    if not args.dry_run:
        confirm = input("确认提交这些变更？[y/N]: ")
        if confirm.lower() != "y":
            print("已取消")
            sys.exit(0)
    
    # 提交每个子模块
    success_count = 0
    for change in changes:
        submodule_path = project_root / change.path
        print(f"处理：{change.path}")
        
        if commit_submodule(
            submodule_path,
            change.commit_message,
            dry_run=args.dry_run,
            push=not args.no_push
        ):
            success_count += 1
            
            # 更新父仓库的子模块引用
            if not args.dry_run:
                update_parent_submodule_reference(
                    change.path,
                    push=not args.no_push
                )
    
    print(f"\n完成：{success_count}/{len(changes)} 个子模块提交成功")
    
    if not args.dry_run and success_count > 0:
        print("\n父仓库中的变更：")
        print("  运行 'git status' 查看子模块引用更新")
        print(f"  运行 'git commit -m \"chore: update submodules\"' 提交父仓库")


if __name__ == "__main__":
    main()
