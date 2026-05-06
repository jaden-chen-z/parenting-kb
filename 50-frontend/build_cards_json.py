#!/usr/bin/env python3
"""
build_cards_json.py — 把 30-cards/*/C-*.yaml 全部转成一个 cards.json
让前端 fetch 加载,而不是 hardcoded。

用法:
    cd ~/Desktop/parenting-kb/50-frontend
    ../.venv/bin/python build_cards_json.py
    # 或: python3 build_cards_json.py(若已装 pyyaml)

每次卡片数据变更后,重跑此脚本刷新 cards.json。
"""

import yaml
import json
import re
import datetime
from pathlib import Path
from collections import defaultdict


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = PROJECT_ROOT / "30-cards"
GLOSSARY_DIR = PROJECT_ROOT / "40-glossary"
OUTPUT = Path(__file__).resolve().parent / "cards.json"
GLOSSARY_OUTPUT = Path(__file__).resolve().parent / "glossary.json"

# 段 ID → 中文显示名
STAGE_NAMES = {
    "S0": "孕期",
    "S1": "0–1 月",
    "S2": "1–3 月",
    "S3": "3–6 月",
    "S4": "6–9 月",
    "S5": "9–12 月",
    "S6": "12–24 月",
    "S7": "24–36 月",
    "S8": "3–6 岁",
}

# 段 ID → 副标题(英文)
STAGE_EN = {
    "S0": "PRENATAL",
    "S1": "NEWBORN",
    "S2": "SOCIAL BUD",
    "S3": "SENSE · ROLL",
    "S4": "EXPLORE · SIT",
    "S5": "CRAWL · STAND",
    "S6": "WALK · WORDS",
    "S7": "SELF · EXPRESS",
    "S8": "EARLY CHILD",
}

# tag 优先级(从高到低)— 卡片有多 tag 时取第一个匹配的作为前端 tag 显示
TAG_PRIORITY = ["red_flag", "safety", "controversy", "philosophy"]


def split_lede_body(text):
    """把 why_matters 的多行文本拆成 lede(一句话) + body[](后续段落)。

    策略:
    1. 优先按段落空行拆;
    2. 单段文本按 Chinese 句号 。 拆,首句作 lede,余下分组成 body 段落;
    3. 极短文本(<60 字)整体作 lede,body 为空。
    """
    if not text:
        return "", []
    text = text.strip()

    # 段落级拆分(空行分段)
    paragraphs = [
        p.strip().replace("\n", " ").replace("  ", " ")
        for p in re.split(r"\n\s*\n", text)
        if p.strip()
    ]

    if len(paragraphs) >= 2:
        return paragraphs[0], paragraphs[1:]

    # 单段:按 。 拆
    single = paragraphs[0] if paragraphs else text.replace("\n", " ").strip()

    # 极短整体作 lede
    if len(single) < 60:
        return single, []

    # 拆句子(保留 。)
    sentences = re.split(r"(?<=。)", single)
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= 1:
        return single, []
    if len(sentences) == 2:
        return sentences[0], [sentences[1]]

    # 多句子:首 1 句作 lede,余下每 2-3 句一段
    lede = sentences[0]
    rest = sentences[1:]
    body = []
    chunk = []
    for s in rest:
        chunk.append(s)
        if len(chunk) >= 2:
            body.append("".join(chunk))
            chunk = []
    if chunk:
        body.append("".join(chunk))
    return lede, body


def pick_tag(tags):
    """从 tags[] 选一个最重要的作为前端单 tag,大写。"""
    if not tags:
        return ""
    for t in TAG_PRIORITY:
        if t in tags:
            return t.upper()
    return tags[0].upper().replace("-", "_")


def authors_to_str(authors):
    """authors[] → 字符串(逗号分隔)。"""
    if not authors:
        return ""
    if isinstance(authors, list):
        return ", ".join(str(a) for a in authors)
    return str(authors)


def normalize_text(text):
    """折叠多行块标量为单行(保持可读)。"""
    if text is None:
        return ""
    text = str(text).replace("\n", " ").strip()
    return re.sub(r"\s+", " ", text)


def convert_card(yaml_data, global_idx):
    """把一张 yaml 卡片转成前端 schema。"""
    stages = yaml_data.get("stages") or []
    primary_stage = stages[0] if stages else "S?"

    back = yaml_data.get("back") or {}
    why_matters = back.get("why_matters", "") or ""
    lede, body = split_lede_body(why_matters)

    what = back.get("what_to_do") or []
    if isinstance(what, str):
        what = [what]
    what = [normalize_text(w) for w in what if w]

    fail = back.get("failure_mode", "") or ""
    fail = normalize_text(fail)

    # 立场冲突版块:多派立场对照(可选,仅冲突卡片有)
    # YAML schema:
    #   back.positions:
    #     issue: "议题(短句)"
    #     views:
    #       - school: "派别名"           # 必填
    #         source: "SRC-XXX"          # 选,显示在派别名右侧
    #         stance: "立场描述"           # 必填,一句话表态
    positions = back.get("positions") or None
    if positions:
        views = positions.get("views") or []
        positions = {
            "issue": normalize_text(positions.get("issue", "")),
            "views": [
                {
                    "school": str(v.get("school", "") or "").strip(),
                    "source": str(v.get("source", "") or "").strip(),
                    "stance": normalize_text(v.get("stance", "")),
                }
                for v in views
                if v and v.get("school") and v.get("stance")
            ],
        }
        if not positions["views"]:
            positions = None

    citation = yaml_data.get("citation") or {}

    front = yaml_data.get("front") or {}

    card_back = {
        "lede": lede,
        "body": body,
        "what": what,
        "fail": fail,
        "evidence": back.get("evidence_level", "B"),
    }
    if positions:
        card_back["positions"] = positions

    return {
        "card_id": yaml_data.get("card_id", ""),
        "stage": primary_stage,
        "stageName": STAGE_NAMES.get(primary_stage, primary_stage),
        "tag": pick_tag(yaml_data.get("tags") or []),
        "no": global_idx + 1,
        "front": {
            "title": str(front.get("title", "") or "").strip(),
            "hook": str(front.get("hook", "") or "").strip(),
        },
        "back": card_back,
        "citation": {
            "book_zh": (
                citation.get("book_title_zh")
                or citation.get("book_title_en")
                or ""
            ),
            "authors": authors_to_str(citation.get("authors")),
            "location": str(citation.get("location") or ""),
            "source_id": citation.get("source_id") or "",
        },
        "related_cards": yaml_data.get("related_cards") or [],
        "glossary_refs": yaml_data.get("glossary_refs") or [],
    }


def convert_glossary(yaml_data):
    """精简术语 yaml 给前端用 — 只留 popup 展示需要的字段。"""
    rel_cards = yaml_data.get("related_cards") or []
    if isinstance(rel_cards, list):
        # 去掉 yaml 里 # 注释、空值
        rel_cards = [str(x).strip() for x in rel_cards if x]
    else:
        rel_cards = []
    rel_glossary = yaml_data.get("related_glossary") or []
    if isinstance(rel_glossary, list):
        rel_glossary = [str(x).strip() for x in rel_glossary if x]
    else:
        rel_glossary = []
    # aliases:别名列表 — 卡片正文中扫的额外搜索词
    # 用途:让"5S"(简写)能匹配到 "5S 安抚法" 词条 / "DDH" 匹配到 "髋发育不良" 等
    aliases = yaml_data.get("aliases") or []
    if isinstance(aliases, list):
        aliases = [str(x).strip() for x in aliases if x and str(x).strip()]
    else:
        aliases = []
    return {
        "glossary_id": yaml_data.get("glossary_id", ""),
        "type": yaml_data.get("type", "term") or "term",
        "display_name": (yaml_data.get("display_name") or "").strip(),
        "full_name_en": (yaml_data.get("full_name_en") or "").strip(),
        "full_name_zh": (yaml_data.get("full_name_zh") or "").strip(),
        "one_liner": (yaml_data.get("one_liner") or "").strip(),
        "aliases": aliases,
        "related_cards": rel_cards,
        "related_glossary": rel_glossary,
    }


def build_glossary():
    """扫 40-glossary/G-*.yaml,生成 glossary.json。"""
    yaml_files = sorted(GLOSSARY_DIR.glob("G-*.yaml"))
    print(f"📚 扫到 {len(yaml_files)} 个术语 yaml...")
    items = []
    errors = []
    for f in yaml_files:
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = yaml.safe_load(fp)
            if not data or not data.get("glossary_id"):
                errors.append(f"{f.name}: 缺 glossary_id")
                continue
            items.append(convert_glossary(data))
        except yaml.YAMLError as e:
            errors.append(f"{f.name}: YAML 解析失败 {e}")
        except Exception as e:
            errors.append(f"{f.name}: {e}")

    output = {
        "meta": {
            "total": len(items),
            "generated_at": datetime.datetime.now().isoformat(),
            "errors": errors,
        },
        "items": items,
    }
    with open(GLOSSARY_OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, separators=(",", ":"))
    size_kb = GLOSSARY_OUTPUT.stat().st_size // 1024
    print(f"✅ 写入 {GLOSSARY_OUTPUT.name}")
    print(f"   {len(items)} 个术语 / 文件 {size_kb} KB")
    if errors:
        print(f"   ⚠️  {len(errors)} 个错误:")
        for e in errors[:5]:
            print(f"   {e}")
        if len(errors) > 5:
            print(f"   ...还有 {len(errors) - 5}")


def main():
    cards_by_stage = defaultdict(list)
    all_cards = []
    errors = []

    yaml_files = sorted(CARDS_DIR.glob("s*-*/C-S*-*.yaml"))
    print(f"📂 扫到 {len(yaml_files)} 张知识卡 yaml...")

    for yaml_file in yaml_files:
        try:
            with open(yaml_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if not data or not data.get("card_id"):
                errors.append(f"{yaml_file.name}: 缺 card_id")
                continue
            card = convert_card(data, len(all_cards))
            all_cards.append(card)
            cards_by_stage[card["stage"]].append(card["card_id"])
        except yaml.YAMLError as e:
            errors.append(f"{yaml_file.name}: YAML 解析失败 {e}")
        except Exception as e:
            errors.append(f"{yaml_file.name}: {e}")

    # 段内重新编号(no 从 1 起,每段独立)
    stage_indices = defaultdict(int)
    for c in all_cards:
        stage_indices[c["stage"]] += 1
        c["noInStage"] = stage_indices[c["stage"]]
        c["totalInStage"] = 0  # 占位,下面填
    stage_totals = {s: stage_indices[s] for s in stage_indices}
    for c in all_cards:
        c["totalInStage"] = stage_totals.get(c["stage"], 0)

    output = {
        "meta": {
            "total": len(all_cards),
            "stages_total": {s: len(cards_by_stage[s]) for s in sorted(cards_by_stage.keys())},
            "generated_at": datetime.datetime.now().isoformat(),
            "errors": errors,
        },
        "stages": [
            {
                "id": s,
                "name": STAGE_NAMES.get(s, s),
                "en": STAGE_EN.get(s, ""),
                "count": len(cards_by_stage[s]),
            }
            for s in sorted(cards_by_stage.keys())
        ],
        "cards": all_cards,
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = OUTPUT.stat().st_size // 1024
    print(f"✅ 写入 {OUTPUT.name}")
    print(f"   {len(all_cards)} 张知识卡 / 跨 {len(cards_by_stage)} 段")
    for s in sorted(cards_by_stage):
        name = STAGE_NAMES.get(s, s)
        print(f"   {s} {name:>10}: {len(cards_by_stage[s]):>4} 张")
    print(f"   文件大小: {size_kb} KB")
    if errors:
        print(f"\n⚠️  解析失败 {len(errors)} 张:")
        for e in errors[:10]:
            print(f"   {e}")
        if len(errors) > 10:
            print(f"   ...还有 {len(errors) - 10} 个错误未列出")


if __name__ == "__main__":
    main()
    build_glossary()
