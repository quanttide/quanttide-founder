#!/usr/bin/env bash
# 把写入闸门装到主仓与所有已初始化的子模块。
# 卸下：git config --unset core.hooksPath（主仓与子模块各跑一次）

set -eu

main_root=$(cd "$(dirname "$0")/.." && pwd)
hooks="$main_root/.githooks"

chmod +x "$hooks/pre-commit" "$hooks/install.sh"

git -C "$main_root" config core.hooksPath "$hooks"
git -C "$main_root" submodule foreach --recursive \
  "git config core.hooksPath '$hooks'" >/dev/null || true

echo "闸门已装：$hooks"
