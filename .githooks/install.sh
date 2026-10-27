#!/usr/bin/env bash
# 装钩子：有新版 CLI 就交给它，没有就退回直接写配置。
# 卸下：qtfounder git hook uninstall，或逐个仓 git config --unset core.hooksPath。

set -eu

main_root=$(cd "$(dirname "$0")/.." && pwd)
hooks="$main_root/.githooks"

chmod +x "$hooks/pre-commit" "$hooks/post-merge" "$hooks/post-checkout" \
  "$hooks/pre-push" "$hooks/install.sh"

# 旧版 CLI 没有 git hook，--help 会失败，这时走下面的兜底。
if command -v qtfounder >/dev/null 2>&1 && qtfounder git hook --help >/dev/null 2>&1; then
  exec qtfounder git hook install --root "$main_root" --force
fi

git -C "$main_root" config core.hooksPath "$hooks"
git -C "$main_root" submodule foreach --recursive \
  "git config core.hooksPath '$hooks'" >/dev/null || true

echo "闸门已装：$hooks"
