#!/usr/bin/env python3
"""
记忆卡片画像报告

读取 data/cards/ 下的所有记忆卡片，按四种记忆类型分别总结，
刻画作者的认知特征、知识体系、自我认知和行为模式。

输出到 data/report/profile.md

用法:
    python scripts/generate_profile_report.py
    python scripts/generate_profile_report.py --output data/report/custom.md
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import urllib.request
import urllib.error

CARDS_DIR = Path("data/cards")
DEFAULT_OUTPUT = Path("data/report/profile.md")
OLLAMA_MODEL = "qwen2.5-coder:3b"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"

CATEGORY_PROFILES = {
    "episodic": {
        "title": "事件记忆画像",
        "desc": "作者经历过的重要事件、决策时刻、关键转折点",
        "prompt": """你是一位心理分析师。请根据以下事件记忆卡片，分析作者的经历特征。

分析维度：
1. 关注焦点：作者最关心什么类型的事情？
2. 决策风格：作者如何做决策？有什么特点？
3. 行为模式：从事件中可以观察到什么重复出现的行为？
4. 关键转折：哪些事件标志着重要的认知或行为转变？

输出 Markdown 格式的分析报告，200-400 字。""",
    },
    "semantic": {
        "title": "语义记忆画像",
        "desc": "作者掌握的知识、概念、规则和客观认知",
        "prompt": """你是一位知识分析师。请根据以下语义记忆卡片，分析作者的知识体系。

分析维度：
1. 知识结构：作者的知识分布在哪些领域？
2. 认知深度：作者对哪些概念有深入理解？
3. 知识偏好：作者倾向于什么类型的知识？（技术/管理/哲学/...）
4. 知识盲区：从卡片中可以推断出哪些知识缺口？

输出 Markdown 格式的分析报告，200-400 字。""",
    },
    "self": {
        "title": "自我记忆画像",
        "desc": "作者的自我认知、价值观、情感反思和身份认同",
        "prompt": """你是一位人格分析师。请根据以下自我记忆卡片，分析作者的自我认知和人格特征。

分析维度：
1. 核心信念：作者最深层的价值观和信念是什么？
2. 自我期待：作者想成为什么样的人？
3. 内在冲突：作者面临哪些内在张力或矛盾？
4. 成长轨迹：从自我反思中可以看出怎样的成长路径？

输出 Markdown 格式的分析报告，200-400 字。""",
    },
    "procedural": {
        "title": "程序性记忆画像",
        "desc": "作者的方法论、工作流程、技能和问题解决模式",
        "prompt": """你是一位方法论分析师。请根据以下程序性记忆卡片，分析作者的工作方法和技能特征。

分析维度：
1. 工作风格：作者偏好什么样的工作方式？
2. 问题解决：作者面对问题时的典型应对策略是什么？
3. 技能分布：作者在哪些方面有方法论积累？
4. 效率模式：作者如何提升自己的效率？

输出 Markdown 格式的分析报告，200-400 字。""",
    },
}


def load_cards() -> dict[str, list[dict]]:
    """加载所有卡片，按类别分组"""
    cards_by_cat = {}
    for cat in CATEGORY_PROFILES:
        cat_dir = CARDS_DIR / cat
        if not cat_dir.exists():
            cards_by_cat[cat] = []
            continue
        cards = []
        for f in sorted(cat_dir.glob("*.json")):
            data = json.loads(f.read_text(encoding="utf-8"))
            cards.append(data)
        cards_by_cat[cat] = cards
    return cards_by_cat


def call_ollama(prompt: str, system: str, model: str = OLLAMA_MODEL) -> str:
    """调用本地 ollama"""
    data = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "system": system,
            "stream": False,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        f"{OLLAMA_BASE_URL}/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("response", "")
    except Exception as e:
        return f"[调用失败: {e}]"


def build_cards_text(cards: list[dict]) -> str:
    """将卡片列表转为文本"""
    lines = []
    for i, card in enumerate(cards, 1):
        lines.append(f"卡片{i}: [{card.get('tense', '?')}] {card['title']}")
        lines.append(f"  {card.get('description', '')}")
        lines.append("")
    return "\n".join(lines)


def generate_profile(cards_by_cat: dict[str, list[dict]]) -> str:
    """生成画像报告"""
    sections = []

    for cat, info in CATEGORY_PROFILES.items():
        cards = cards_by_cat.get(cat, [])
        if not cards:
            sections.append(f"## {info['title']}\n\n（无数据）\n")
            continue

        cards_text = build_cards_text(cards)
        prompt = f"请分析以下{info['title']}卡片，刻画作者的特征：\n\n{cards_text}"

        print(f"  分析: {info['title']} ({len(cards)} 张卡片)")
        analysis = call_ollama(prompt, info["prompt"])

        sections.append(f"## {info['title']}\n\n{info['desc']}\n\n{analysis}\n")

    return "\n".join(sections)


def generate_summary(cards_by_cat: dict[str, list[dict]]) -> str:
    """生成综合总结"""
    all_cards = []
    for cards in cards_by_cat.values():
        all_cards.extend(cards)

    if not all_cards:
        return ""

    summary_prompt = f"""你是一位综合分析师。请根据以下四种记忆类型的分析结果，给出对作者的整体画像。

分析维度：
1. 核心特质：用 3-5 个关键词概括作者的核心特征
2. 认知模式：作者的思维方式和认知习惯
3. 成长方向：作者正在向什么方向进化？
4. 潜在风险：可能存在什么盲点或风险？
5. 一句话画像：用一句话概括这个人

输出 Markdown 格式，300-500 字。"""

    # 先汇总各类型卡片数量
    stats_lines = []
    for cat, cards in cards_by_cat.items():
        stats_lines.append(f"- {cat}: {len(cards)} 张卡片")
        for card in cards:
            stats_lines.append(f"  - [{card.get('tense', '?')}] {card['title']}")

    prompt = f"请根据以下记忆卡片数据，给出对作者的整体画像：\n\n" + "\n".join(
        stats_lines
    )

    print("  生成综合画像...")
    return call_ollama(prompt, summary_prompt)


def main():
    output = DEFAULT_OUTPUT
    for arg in sys.argv[1:]:
        if arg.startswith("--output="):
            output = Path(arg.split("=", 1)[1])
        elif arg.startswith("--output"):
            idx = sys.argv.index(arg)
            if idx + 1 < len(sys.argv):
                output = Path(sys.argv[idx + 1])

    if not CARDS_DIR.exists():
        print(f"错误: 找不到 {CARDS_DIR}")
        print("请先运行 parse_think_cards.py")
        sys.exit(1)

    cards_by_cat = load_cards()
    total = sum(len(v) for v in cards_by_cat.values())
    print(f"加载 {total} 张卡片")

    output.parent.mkdir(parents=True, exist_ok=True)

    profile = generate_profile(cards_by_cat)
    summary = generate_summary(cards_by_cat)

    report = f"""# 作者画像报告

> 基于 {total} 张记忆卡片，来源于 {len(list(CARDS_DIR.glob("*/*.json")))} 个 think 日志文件
> 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}

## 卡片统计

| 记忆类型 | 数量 |
|---------|------|
"""
    for cat, cards in cards_by_cat.items():
        report += f"| {cat} | {len(cards)} |\n"

    report += f"""
---

{profile}

---

## 综合画像

{summary}
"""

    output.write_text(report, encoding="utf-8")
    print(f"\n报告已输出: {output}")


if __name__ == "__main__":
    main()
