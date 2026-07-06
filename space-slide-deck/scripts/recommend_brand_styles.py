#!/usr/bin/env python3
"""Recommend brand design systems for slide deck content.

Reads source content from a file path or stdin and returns five matched-but-random
options plus one deterministic smart match.
"""

import argparse
import hashlib
import json
import random
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REGISTRY = SCRIPT_DIR.parent / "references" / "brand-style-registry.json"

KEYWORD_TAGS = {
    "ai": ["ai", "agent", "model", "llm", "gpt", "claude", "人工智能", "模型", "智能体", "大模型", "自动化"],
    "agent": ["agent", "agents", "mcp", "workflow", "automation", "智能体", "工作流", "自动化", "编排"],
    "developer": ["developer", "api", "code", "sdk", "github", "cli", "开发者", "代码", "接口", "编程", "开源"],
    "devops": ["devops", "deploy", "cloud", "infra", "observability", "security", "部署", "云", "基础设施", "安全", "监控"],
    "knowledge": ["knowledge", "docs", "note", "obsidian", "wiki", "学习", "知识", "笔记", "文档", "教程", "方法论"],
    "productivity": ["productivity", "calendar", "email", "效率", "生产力", "日程", "邮件", "个人系统"],
    "saas": ["saas", "product", "dashboard", "metrics", "产品", "指标", "看板", "数据", "商业化"],
    "growth": ["growth", "marketing", "sales", "crm", "launch", "增长", "营销", "销售", "发布", "获客"],
    "finance": ["finance", "payment", "pricing", "crypto", "trading", "金融", "支付", "定价", "加密", "交易"],
    "consumer": ["consumer", "community", "social", "app", "用户", "社区", "消费", "应用"],
    "creative": ["design", "creative", "media", "video", "music", "podcast", "设计", "创意", "视频", "音乐", "播客"],
    "premium": ["premium", "executive", "luxury", "hardware", "高端", "发布会", "硬件", "旗舰", "奢侈"],
    "research": ["research", "academic", "paper", "science", "enterprise", "研究", "论文", "科学", "企业", "治理"],
    "mobility": ["car", "vehicle", "mobility", "travel", "space", "汽车", "出行", "旅行", "航天"],
}


def load_registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def normalize(text):
    return text.lower()


def infer_tags(text):
    lowered = normalize(text)
    tags = set()
    for tag, keywords in KEYWORD_TAGS.items():
        if any(keyword.lower() in lowered for keyword in keywords):
            tags.add(tag)
    return tags


def score_entry(entry, text, inferred_tags):
    lowered = normalize(text)
    score = 0

    entry_tags = set(entry.get("tags", []))
    score += 4 * len(entry_tags & inferred_tags)

    category = entry.get("category", "")
    if category in inferred_tags:
        score += 3

    for alias in entry.get("aliases", []):
        if alias.lower() in lowered:
            score += 12

    for tag in entry_tags:
        if re.search(rf"\b{re.escape(tag.lower())}\b", lowered):
            score += 2

    # General deck defaults: prioritize legible design systems for weak signals.
    if not inferred_tags and entry["slug"] in {"claude", "notion", "apple", "stripe", "linear.app", "vercel"}:
        score += 2

    return score


def recommend(text, count=5):
    registry = load_registry()
    inferred_tags = infer_tags(text)
    scored = []
    for entry in registry:
        score = score_entry(entry, text, inferred_tags)
        scored.append((score, entry))

    scored.sort(key=lambda item: (-item[0], item[1]["slug"]))
    smart_match = scored[0][1]

    strong_pool = [entry for score, entry in scored if score == scored[0][0] or score >= max(1, scored[0][0] - 4)]
    if len(strong_pool) < count:
        positive = [(score, entry) for score, entry in scored if score > 0]
        threshold = max(1, scored[0][0] // 2)
        strong_pool = [entry for score, entry in positive if score >= threshold]
    if len(strong_pool) < count:
        strong_pool = [entry for score, entry in scored if score > 0][: max(count, 12)]
    if len(strong_pool) < count:
        strong_pool = [entry for _, entry in scored[:12]]

    seed = int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:12], 16)
    rng = random.Random(seed)
    pool = strong_pool[:]
    rng.shuffle(pool)

    options = []
    seen = set()
    for entry in pool:
        if entry["slug"] == smart_match["slug"]:
            continue
        if entry["slug"] in seen:
            continue
        options.append(entry)
        seen.add(entry["slug"])
        if len(options) == count:
            break

    if len(options) < count:
        for _, entry in scored:
            if entry["slug"] == smart_match["slug"] or entry["slug"] in seen:
                continue
            options.append(entry)
            seen.add(entry["slug"])
            if len(options) == count:
                break

    return {
        "inferred_tags": sorted(inferred_tags),
        "recommendations": options,
        "smart_match": smart_match,
    }


def format_markdown(result):
    lines = []
    tags = ", ".join(result["inferred_tags"]) or "general"
    lines.append(f"内容信号：{tags}")
    lines.append("")
    lines.append("推荐 5 种匹配风格：")
    for i, entry in enumerate(result["recommendations"], 1):
        lines.append(f"{i}. `{entry['slug']}` - {entry['description']}")
    smart = result["smart_match"]
    lines.append(f"6. `智能匹配` - 使用 `{smart['slug']}`：{smart['description']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Recommend brand design systems for slide decks.")
    parser.add_argument("source", nargs="?", help="Path to source content. Reads stdin when omitted.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    args = parser.parse_args()

    if args.source:
        text = Path(args.source).read_text(encoding="utf-8")
    else:
        import sys
        text = sys.stdin.read()

    result = recommend(text)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_markdown(result))


if __name__ == "__main__":
    main()
