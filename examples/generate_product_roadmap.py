#!/usr/bin/env python3
"""
从产品日志生成产品路线图

读取 docs/journal/product/ 下的产品日志文件，
使用本地 ollama (qwen2.5-coder:3b) 分析并生成产品路线图，
输出到 docs/roadmap/product/ 目录。

用法:
    python examples/generate_product_roadmap.py              # 生成完整路线图
    python examples/generate_product_roadmap.py --output docs/roadmap/product/custom.md
"""

import json
import sys
from datetime import datetime
from pathlib import Path

JOURNAL_DIR = Path("docs/journal/product")
DEFAULT_OUTPUT = Path("docs/roadmap/product/roadmap.md")
OLLAMA_MODEL = "qwen2.5-coder:3b"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"


def load_journals() -> list[dict]:
    """加载所有产品日志文件"""
    journals = []
    if not JOURNAL_DIR.exists():
        print(f"错误: 找不到 {JOURNAL_DIR}")
        sys.exit(1)

    for f in sorted(JOURNAL_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        journals.append({"date": f.stem, "file": f.name, "content": content})

    return journals


def call_ollama(prompt: str, system: str, model: str = OLLAMA_MODEL) -> str:
    """调用本地 ollama API"""
    import urllib.request
    import urllib.error

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


def generate_roadmap(journals: list[dict]) -> str:
    """生成产品路线图"""
    journals_text = ""
    for j in journals:
        journals_text += f"### {j['date']} ({j['file']})\n\n{j['content']}\n\n"

    system_prompt = """你是一位产品战略分析师。请根据以下产品日志，生成一份结构化的产品路线图。

输出 Markdown 格式，包含以下部分：

## 产品全景

按产品线/模块组织，每个产品包含：
- 定位与愿景
- 核心功能清单
- 当前状态（探索/验证/开发/成熟）

## 功能规划

按优先级排列的功能项，每项包含：
- 功能名称
- 所属产品
- 优先级（P0/P1/P2）
- 状态（待探索/待验证/开发中/已完成）
- 来源日志日期

## 技术债务与修复

从日志中提取的 bug 修复、技术债务项。

## 下一步行动

按紧急性和重要性排列的近期行动计划。

重要约束：
- 只基于日志中明确提到的内容，不要臆测
- 保留原始表述的关键信息
- 标注每条信息的来源日期"""

    prompt = f"请根据以下产品日志生成路线图：\n\n{journals_text}"

    print("正在生成产品路线图...")
    return call_ollama(prompt, system_prompt)


def main():
    output = DEFAULT_OUTPUT
    for arg in sys.argv[1:]:
        if arg.startswith("--output="):
            output = Path(arg.split("=", 1)[1])
        elif arg.startswith("--output"):
            idx = sys.argv.index(arg)
            if idx + 1 < len(sys.argv):
                output = Path(sys.argv[idx + 1])

    journals = load_journals()
    print(f"加载 {len(journals)} 个产品日志文件")

    roadmap = generate_roadmap(journals)

    output.parent.mkdir(parents=True, exist_ok=True)

    header = f"""# 产品路线图

> 基于 {len(journals)} 个产品日志文件生成
> 生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}
> 数据来源: {JOURNAL_DIR}

---

"""

    full_report = header + roadmap

    output.write_text(full_report, encoding="utf-8")
    print(f"\n路线图已输出: {output}")


if __name__ == "__main__":
    main()
