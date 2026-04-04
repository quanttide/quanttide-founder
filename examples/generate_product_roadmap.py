#!/usr/bin/env python3
"""
从产品日志生成产品路线图

读取 docs/journal/product/ 下的日志文件，
按 ## 产品名 拆分并聚合，每个产品输出一个路线图文件。

用法:
    python examples/generate_product_roadmap.py              # 处理 product 标识
    python examples/generate_product_roadmap.py think        # 处理 think 标识
"""

import re
import sys
from datetime import datetime
from pathlib import Path

JOURNAL_BASE = Path("docs/journal")
ROADMAP_BASE = Path("docs/roadmap")


def load_journal(slug: str) -> list[dict]:
    """加载指定标识符下的所有日志文件"""
    journal_dir = JOURNAL_BASE / slug
    if not journal_dir.exists():
        print(f"错误: 找不到 {journal_dir}")
        sys.exit(1)

    entries = []
    for f in sorted(journal_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        entries.append({"date": f.stem, "file": f.name, "content": content})
    return entries


def split_by_product(content: str, date: str) -> list[dict]:
    """按 ## 标题拆分内容，返回 [{product, section, date}]"""
    sections = re.split(r"^## (.+)$", content, flags=re.MULTILINE)
    results = []
    i = 1
    while i < len(sections) - 1:
        name = sections[i].strip()
        body = sections[i + 1].strip()
        if name and body:
            results.append({"product": name, "section": body, "date": date})
        i += 2
    return results


def aggregate_products(entries: list[dict]) -> dict[str, list[dict]]:
    """按产品名聚合所有条目"""
    products = {}
    for entry in entries:
        items = split_by_product(entry["content"], entry["date"])
        for item in items:
            name = item["product"]
            if name not in products:
                products[name] = []
            products[name].append(item)
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
        lines.append(item["section"])
        lines.append("")

    return "\n".join(lines)


def main():
    slug = (
        sys.argv[1]
        if len(sys.argv) > 1 and not sys.argv[1].startswith("--")
        else "product"
    )

    entries = load_journal(slug)
    print(f"加载 {len(entries)} 个日志文件")

    products = aggregate_products(entries)
    print(f"识别到 {len(products)} 个产品: {', '.join(products.keys())}")

    ROADMAP_BASE.mkdir(parents=True, exist_ok=True)

    for name, items in products.items():
        output = ROADMAP_BASE / f"{slugify(name)}.md"
        content = build_roadmap(name, items)
        output.write_text(content, encoding="utf-8")
        print(f"  输出: {output}")

    print(f"\n完成! 共生成 {len(products)} 个文件到 {ROADMAP_BASE}/")


if __name__ == "__main__":
    main()
