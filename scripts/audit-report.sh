#!/usr/bin/env bash
# 文字体检：把各仓的文字与文档审计汇总成一份能读的报告。
#
# 每期只说一处最值得改的。挑法是一个词、一条规则：改一次能带走很多处。
# 完整清单不铺开，改完这一处再出下一期。
#
# 用法：scripts/audit-report.sh [目录...]        缺省看整个仓，契约里的 exclude 会跳过流水、归档与示例

set -u

main_root=$(cd "$(dirname "$0")/.." && pwd)
lang_rules="$main_root/apps/qtfounder/src/cli/src/language/default-contract.toml"
docs_rules="$main_root/apps/qtfounder/src/cli/src/docs/default-contract.toml"

if [ "$#" -gt 0 ]; then
  roots=("$@")
else
  roots=(.)
fi

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

scanned=0
suspects=0
: >"$tmpdir/errors"

for root in "${roots[@]}"; do
  [ -d "$root" ] || continue
  for audit in language docs; do
    if [ "$audit" = language ]; then
      rules="$lang_rules"
    else
      rules="$docs_rules"
    fi
    [ -f "$rules" ] || continue

    out=$(qtfounder "$audit" "$root" --rules "$rules" --json 2>/dev/null) || true
    [ -n "$out" ] || continue

    n=$(printf '%s\n' "$out" | sed -n 's/.*"scanned_files": *\([0-9]*\).*/\1/p' | head -1)
    if [ "$audit" = language ]; then
      scanned=$((scanned + ${n:-0}))
    fi

    s=$(printf '%s\n' "$out" | grep -c '"severity":"suspect"' || true)
    suspects=$((suspects + ${s:-0}))

    errs=$(printf '%s\n' "$out" | grep '"severity":"error"' | grep -v '"verdict":"mention"')
    [ -n "$errs" ] || continue
    printf '%s\n' "$errs" \
      | sed -n 's/.*"kind":"\([^"]*\)".*"path":"\([^"]*\)".*"advice":"\([^"]*\)".*/\1|\3|\2/p' \
      >>"$tmpdir/errors"
  done
done

printf '量潮创始人 · 文字体检\n\n'
printf '这次看了 %s 篇文档。\n\n' "$scanned"

total=$(wc -l <"$tmpdir/errors" | tr -d ' ')
if [ "$total" -eq 0 ]; then
  printf '没查出问题。\n'
  exit 0
fi

ranking=$(cut -d'|' -f1,2 "$tmpdir/errors" | sort | uniq -c | sort -rn)
# 术语优先：读者要先翻译才能懂的词，比格式小事更值得先改。
pool="$tmpdir/errors"
banned=$(grep -c '^banned|' "$tmpdir/errors" || true)
if [ "${banned:-0}" -gt 0 ]; then
  pool="$tmpdir/banned"
  grep '^banned|' "$tmpdir/errors" >"$pool"
  ranking=$(cut -d'|' -f1,2 "$pool" | sort | uniq -c | sort -rn)
fi
top=$(printf '%s\n' "$ranking" | head -1)
count=$(printf '%s' "$top" | awk '{print $1}')
key=$(printf '%s' "$top" | sed 's/^ *[0-9]\+ *//')
advice=${key#*|}
files=$(grep -F "$key|" "$pool" | cut -d'|' -f3 | sort -u | wc -l | tr -d ' ')
kinds=$(cut -d'|' -f1,2 "$tmpdir/errors" | sort -u | wc -l | tr -d ' ')

word=$(printf '%s' "$advice" | sed -n 's/^「\([^」]*\)」.*/\1/p')
rest=$(printf '%s' "$advice" | sed -n 's/.*→ *//p' | sed 's/：/——/')

if [ -n "$word" ]; then
  printf '这一期先改一处：「%s」\n\n' "$word"
  printf '它出现 %s 次，落在 %s 篇里。\n\n' "$count" "$files"
  printf '怎么改：把「%s」换成 %s。\n\n' "$word" "$rest"
else
  printf '这一期先改一处：%s\n\n' "$advice"
  printf '它出现 %s 次，落在 %s 篇里。\n\n' "$count" "$files"
fi

if [ "$kinds" -gt 1 ]; then
  printf '另有 %s 类这次不列，改完这一处再看。\n' "$((kinds - 1))"
fi

if [ "$suspects" -gt 0 ]; then
  printf '机器拿不准的有 %s 处，这类归人判，不进这份报告。\n' "$suspects"
fi
