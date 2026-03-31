#!/usr/bin/env python3
"""
使用 AI 自动生成子模块 commit message

用法:
    python scripts/commit_submodules_ai.py [--dry-run] [--no-push]

依赖:
    - 需要配置 OPENAI_API_KEY 或使用其他兼容的 API
"""

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class SubmoduleChange:
    """子模块变更信息"""
    path: str
    files_changed: list[str]
    diff_summary: str
    commit_message: str


def run_git_command(cmd: list[str], cwd: Optional[Path] = None, timeout: int = 30) -> tuple[int, str, str]:
    """运行 git 命令"""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout
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
    """检查子模块状态"""
    if not submodule_path.exists():
        return False, []
    
    returncode, stdout, _ = run_git_command(
        ["git", "status", "--porcelain"],
        cwd=submodule_path
    )
    
    if returncode != 0:
        return False, []
    
    changed_files = []
    for line in stdout.strip().split("\n"):
        if line.strip():
            changed_files.append(line.strip())
    
    return len(changed_files) > 0, changed_files


def get_diff_summary(submodule_path: Path, max_lines: int = 100) -> str:
    """获取变更摘要"""
    # 获取 staged 和 unstaged 的 diff
    _, staged, _ = run_git_command(["git", "diff", "--cached", "--stat"], cwd=submodule_path)
    _, unstaged, _ = run_git_command(["git", "diff", "--stat"], cwd=submodule_path)
    
    summary = []
    if staged.strip():
        summary.append("Staged changes:")
        summary.append(staged.strip())
    if unstaged.strip():
        summary.append("Unstaged changes:")
        summary.append(unstaged.strip())
    
    return "\n".join(summary)[:max_lines * 100]  # 限制长度


def generate_commit_message_with_ai(
    submodule_path: str,
    files_changed: list[str],
    diff_summary: str
) -> str:
    """使用 AI 生成 commit message"""
    
    # 尝试使用 OpenAI API
    api_key = os.environ.get("OPENAI_API_KEY")
    api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    if not api_key:
        # 降级到规则生成
        return generate_commit_message_rules(submodule_path, files_changed)
    
    try:
        import requests
        
        prompt = f"""分析以下 git 变更并生成符合 Conventional Commits 规范的 commit message：

子模块路径：{submodule_path}
变更文件：
{chr(10).join(f'  - {f}' for f in files_changed[:20])}

变更摘要：
{diff_summary[:500]}

要求：
1. 使用 Conventional Commits 格式：<type>: <description>
2. type 从以下选择：feat, fix, docs, style, refactor, test, chore
3. description 简洁明了，不超过 50 字符
4. 如果变更复杂，添加空行后跟详细说明

只返回 commit message，不要其他内容。"""

        response = requests.post(
            f"{api_base}/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "你是一个专业的软件工程师，擅长编写清晰准确的 git commit message。"},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 200,
                "temperature": 0.3
            },
            timeout=30
        )
        
        if response.status_code == 200:
            message = response.json()["choices"][0]["message"]["content"].strip()
            # 清理可能的 markdown 格式
            message = message.replace("```", "").strip()
            return message
    except Exception as e:
        print(f"  AI 生成失败：{e}，降级到规则生成")
    
    return generate_commit_message_rules(submodule_path, files_changed)


def generate_commit_message_rules(submodule_path: str, files_changed: list[str]) -> str:
    """基于规则生成 commit message"""
    # 分析文件类型
    py_files = [f for f in files_changed if ".py" in f]
    md_files = [f for f in files_changed if ".md" in f]
    test_files = [f for f in files_changed if "test" in f.lower()]
    doc_files = [f for f in files_changed if "doc" in f.lower() or "readme" in f.lower()]
    config_files = [f for f in files_changed if any(ext in f for ext in [".json", ".yaml", ".yml", ".toml"])]
    
    # 确定类型
    if test_files:
        commit_type = "test"
    elif doc_files or (md_files and not py_files):
        commit_type = "docs"
    elif any("refactor" in f.lower() for f in files_changed):
        commit_type = "refactor"
    elif py_files:
        commit_type = "feat"
    elif config_files:
        commit_type = "chore"
    else:
        commit_type = "chore"
    
    # 生成描述
    dirs = set()
    for f in files_changed:
        parts = f.split()
        filename = parts[1] if len(parts) > 1 else parts[0]
        filename = filename.lstrip("?MADRCU")
        parent = str(Path(filename).parent)
        if parent and parent != ".":
            dirs.add(parent.split("/")[0])
    
    if dirs:
        dir_list = sorted(dirs)
        if len(dir_list) == 1:
            subject = dir_list[0]
        elif len(dir_list) <= 3:
            subject = ", ".join(dir_list)
        else:
            subject = "multiple directories"
    else:
        subject = "files"
    
    # 确定动作
    added = [f for f in files_changed if f.startswith("A") or f.startswith("??")]
    if added and len(added) == len(files_changed):
        action = "add"
    elif any("delete" in f.lower() or "remove" in f.lower() for f in files_changed):
        action = "remove"
    else:
        action = "update"
    
    return f"{commit_type}: {action} {subject}"


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
            return True
        print(f"  错误：git commit 失败 - {stderr}")
        return False
    
    print(f"  ✓ 已提交：{submodule_path.name}")
    
    # git push
    if push:
        returncode, output, stderr = run_git_command(
            ["git", "push", "origin", "HEAD"],
            cwd=submodule_path,
            timeout=60
        )
        if returncode != 0:
            print(f"  ⚠ 推送失败：{stderr.strip()}")
            return True
        print(f"  ✓ 已推送：{submodule_path.name}")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description="使用 AI 自动提交子模块变更并生成 commit message",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                      # 自动提交所有子模块
  %(prog)s --dry-run            # 预览模式
  %(prog)s --no-push            # 仅提交不推送
  %(prog)s --submodule qtadmin  # 只处理 qtadmin

环境变量:
  OPENAI_API_KEY      OpenAI API 密钥（可选，用于 AI 生成 commit message）
  OPENAI_API_BASE     OpenAI API 基础 URL（可选）
        """
    )
    parser.add_argument("--dry-run", action="store_true", help="预览模式")
    parser.add_argument("--no-push", action="store_true", help="仅提交不推送")
    parser.add_argument("--submodule", type=str, default="", help="只处理指定的子模块")
    parser.add_argument("--yes", "-y", action="store_true", help="跳过确认")
    
    args = parser.parse_args()
    
    project_root = Path.cwd()
    submodule_paths = get_submodule_paths()
    
    if args.submodule:
        submodule_paths = [p for p in submodule_paths if args.submodule in p]
    
    if not submodule_paths:
        print("未找到子模块")
        sys.exit(0)
    
    print(f"📦 发现 {len(submodule_paths)} 个子模块\n")
    
    # 检查变更
    changes: list[SubmoduleChange] = []
    
    for path in submodule_paths:
        submodule_path = project_root / path
        has_changes, changed_files = check_submodule_status(submodule_path)
        
        if has_changes:
            diff_summary = get_diff_summary(submodule_path)
            
            # 生成 commit message
            print(f"分析：{path}")
            commit_message = generate_commit_message_with_ai(
                path, changed_files, diff_summary
            )
            
            changes.append(SubmoduleChange(
                path=path,
                files_changed=changed_files,
                diff_summary=diff_summary,
                commit_message=commit_message
            ))
            print(f"  📝 {commit_message.split(chr(10))[0]}")
    
    if not changes:
        print("\n✅ 所有子模块都是最新的")
        sys.exit(0)
    
    print(f"\n共 {len(changes)} 个子模块需要提交\n")
    
    if not args.dry_run and not args.yes:
        confirm = input("确认提交？[y/N]: ")
        if confirm.lower() != "y":
            print("已取消")
            sys.exit(0)
    
    # 提交
    success_count = 0
    for change in changes:
        submodule_path = project_root / change.path
        print(f"\n处理：{change.path}")
        
        if commit_submodule(
            submodule_path,
            change.commit_message,
            dry_run=args.dry_run,
            push=not args.no_push
        ):
            success_count += 1
            
            # 更新父仓库引用
            if not args.dry_run:
                run_git_command(["git", "add", change.path])
    
    print(f"\n{'='*50}")
    print(f"✅ 完成：{success_count}/{len(changes)} 个子模块")
    
    if not args.dry_run and success_count > 0:
        print(f"\n📌 父仓库有待提交的子模块引用更新:")
        print(f"   git commit -m \"chore: update {success_count} submodules\"")
        print(f"   git push")


if __name__ == "__main__":
    main()
