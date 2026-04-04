#!/usr/bin/env python3
"""
从产品日志生成产品路线图

读取 docs/journal/<slug>/<product>/ 下的日志文件，
每个产品输出一个路线图文件到 docs/roadmap/<slug>/。

用法:
    python examples/generate_product_roadmap.py              # 处理 product 标识
    python examples/generate_product_roadmap.py think        # 处理 think 标识
"""

import re
import sys
from pathlib import Path

JOURNAL_BASE = Path("docs/journal")
ROADMAP_BASE = Path("docs/roadmap")


def load_journal(slug: str) -> dict[str, list[dict]]:
    """加载指定标识符下所有产品的日志文件，返回 {product: [{date, file, content}]}"""
    journal_dir = JOURNAL_BASE / slug
    if not journal_dir.exists():
        print(f"错误: 找不到 {journal_dir}")
        sys.exit(1)

    products = {}
    for d in sorted(journal_dir.iterdir()):
        if not d.is_dir():
            continue
        product_name = d.name
        entries = []
        for f in sorted(d.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            entries.append({"date": f.stem, "file": f.name, "content": content})
        if entries:
            products[product_name] = entries
    return products


def slugify(name: str) -> str:
    """产品名转文件名"""
    return re.sub(r"[^\w\u4e00-\u9fff-]", "_", name)


def build_roadmap(product_name: str, items: list[dict]) -> str:
    """构建产品路线图（规则驱动，不调用 LLM）"""
    lines = [f"# {product_name}", ""]

    for item in items:
        lines.append(f"## {item['date']}")
        lines.append("")
        lines.append(item["content"])
        lines.append("")

    return "\n".join(lines)


def main():
    slug = (
        sys.argv[1]
        if len(sys.argv) > 1 and not sys.argv[1].startswith("--")
        else "product"
    )

    products = load_journal(slug)
    print(f"识别到 {len(products)} 个产品: {', '.join(products.keys())}")

    output_dir = ROADMAP_BASE / slug
    output_dir.mkdir(parents=True, exist_ok=True)

    for name, items in products.items():
        output = output_dir / f"{slugify(name)}.md"
        content = build_roadmap(name, items)
        output.write_text(content, encoding="utf-8")
        print(f"  输出: {output}")

    print(f"\n完成! 共生成 {len(products)} 个文件到 {output_dir}/")


if __name__ == "__main__":
    main()
