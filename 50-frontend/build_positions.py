#!/usr/bin/env python3
"""
build_positions.py — 把 00-meta/conflicts_data/positions.yaml 里的立场对照数据
**文本插入**到对应卡片 YAML 的 back.positions 字段。

为什么用文本插入而非 yaml.load/dump 改写:
- PyYAML 的 dump 不保留 | 块标量、内联列表、双引号、空行等手写格式
- 文本插入只动新增的 positions 块,其他字符 1:1 保留

行为:
- 一张卡同属多议题:多议题 views 自动合并(去重 by school)
- 已有 positions 块 → 替换;未有 → 在 evidence_level: X 行后插入
- 找不到的 card_id 写入错误列表,不中断

用法:
    cd ~/Desktop/parenting-kb/50-frontend
    ../.venv/bin/python build_positions.py            # 真写
    ../.venv/bin/python build_positions.py --dry-run  # 试算
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
POSITIONS_SRC = PROJECT_ROOT / "00-meta" / "conflicts_data" / "positions.yaml"
CARDS_DIR = PROJECT_ROOT / "30-cards"


class IndentDumper(yaml.SafeDumper):
    """让 list 项缩进对齐父键,排版好看。"""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def load_positions():
    """读 positions.yaml,展开为 conflict_id → {issue, cards, views} 的 dict。"""
    if not POSITIONS_SRC.exists():
        sys.exit(f"❌ 找不到 {POSITIONS_SRC}")
    with open(POSITIONS_SRC, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data


def find_card_yaml(card_id):
    """C-S1-013 → 30-cards/s1-newborn/C-S1-013.yaml,找不到返回 None。"""
    matches = list(CARDS_DIR.rglob(f"{card_id}.yaml"))
    if not matches:
        return None
    if len(matches) > 1:
        print(f"⚠️  {card_id} 找到 {len(matches)} 个 yaml,取第一个")
    return matches[0]


def merge_views(existing_views, new_views):
    """同 school 后写覆盖前(允许立场表述演进)。"""
    by_school = {}
    for v in existing_views:
        by_school[v["school"]] = v
    for v in new_views:
        by_school[v["school"]] = v
    return list(by_school.values())


def build_card_positions(card_to_conflicts):
    """同卡多议题 — views 合并;issue 取第一议题(其余作为 conflict_ids 标注备用)。"""
    result = {}
    for card_id, conflicts in card_to_conflicts.items():
        merged_views = []
        first_issue = ""
        conflict_ids = []
        for c in conflicts:
            if not first_issue and c.get("issue"):
                first_issue = c["issue"]
            conflict_ids.append(c["id"])
            merged_views = merge_views(merged_views, c["views"])
        result[card_id] = {
            "issue": first_issue,
            "views": merged_views,
            "_conflict_ids": conflict_ids,  # 仅在打印时显示,不写入卡片
        }
    return result


def render_positions_block(positions, base_indent=2):
    """把 positions dict 渲染成 YAML 文本块,顶层缩进 base_indent 个空格。

    输出形如(base_indent=2):
      positions:
        issue: 包裹 swaddle 该不该用
        views:
          - school: Karp
            source: SRC-003
            stance: 紧裹双臂内
    """
    # 拷贝,去掉内部字段
    clean_pos = {
        "issue": positions["issue"],
        "views": [
            {"school": v["school"], "source": v.get("source", ""), "stance": v["stance"]}
            for v in positions["views"]
        ],
    }
    # views 里去掉空 source(让输出更紧凑)
    for v in clean_pos["views"]:
        if not v["source"]:
            del v["source"]

    raw = yaml.dump(
        {"positions": clean_pos},
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=200,
        Dumper=IndentDumper,
    )
    lines = raw.rstrip("\n").split("\n")
    indented = [(" " * base_indent) + line for line in lines]
    return "\n".join(indented)


# 匹配 back.evidence_level: X 行(X 一般是单字母 A-D,可能带引号)
EVIDENCE_RE = re.compile(r"^(\s+)evidence_level:\s*['\"]?[A-Z][a-z]?['\"]?\s*$", re.MULTILINE)

# 匹配已存在的 positions: 块(以及它的所有子内容)
# 起点:`  positions:` 一行(2 空格缩进)
# 终点:下一个同级或更外层的字段(以 `  word:` 开头但不是 `    ` 开头),或顶层字段(无缩进开头)
POSITIONS_BLOCK_RE = re.compile(
    r"^(  positions:\n(?:    .*\n|\n)*?)(?=^(?:[a-zA-Z_]|  [a-zA-Z_]))",
    re.MULTILINE,
)


def insert_positions(yaml_text, positions):
    """把 positions 块插入或替换进 YAML 文本。返回 (新文本, 状态)。"""
    block = render_positions_block(positions, base_indent=2)

    # 已有 positions 块 → 替换
    existing = POSITIONS_BLOCK_RE.search(yaml_text)
    if existing:
        new_text = yaml_text[: existing.start()] + block + "\n" + yaml_text[existing.end():]
        return new_text, "replaced"

    # 没有 → 在 evidence_level: X 行后插入
    m = EVIDENCE_RE.search(yaml_text)
    if not m:
        return yaml_text, "no evidence_level line"

    insert_at = m.end()
    # m.end() 指向 evidence_level 行末(\n 之前),需要在 \n 之后插入
    # 安全做法:取整行末加 \n 后插
    # m 的内容包含尾部空白(无 \n),所以 yaml_text[m.end()] 应是 '\n' 或 EOF
    if insert_at < len(yaml_text) and yaml_text[insert_at] == "\n":
        insert_at += 1
    new_text = yaml_text[:insert_at] + block + "\n" + yaml_text[insert_at:]
    return new_text, "inserted"


def apply_to_yaml(card_id, positions, dry_run=False):
    yaml_path = find_card_yaml(card_id)
    if not yaml_path:
        return False, f"{card_id}: 找不到 yaml"

    with open(yaml_path, "r", encoding="utf-8") as f:
        text = f.read()

    new_text, status = insert_positions(text, positions)
    if status.startswith("no "):
        return False, f"{card_id}: {status}"

    if new_text == text:
        return True, f"{card_id}: no change"

    if dry_run:
        return True, f"{card_id}: would {status}"

    with open(yaml_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True, f"{card_id}: ✅ {status}"


def main():
    dry_run = "--dry-run" in sys.argv
    src = load_positions()

    card_to_conflicts = defaultdict(list)
    for conflict_id, conflict in src.items():
        cards = conflict.get("cards") or []
        views = conflict.get("views") or []
        issue = conflict.get("issue", "")
        if not cards or not views:
            print(f"⚠️  {conflict_id}: 缺 cards 或 views,跳过")
            continue
        for card_id in cards:
            card_to_conflicts[card_id].append(
                {"issue": issue, "views": views, "id": conflict_id}
            )

    card_positions = build_card_positions(card_to_conflicts)

    print(f"📋 共 {len(src)} 个议题,涉及 {len(card_positions)} 张卡片")
    if dry_run:
        print("(dry-run 模式,不写文件)")

    ok = 0
    errors = []
    changes = defaultdict(int)
    for card_id, positions in card_positions.items():
        success, msg = apply_to_yaml(card_id, positions, dry_run=dry_run)
        if success:
            ok += 1
            for k in ("inserted", "replaced", "no change"):
                if k in msg:
                    changes[k] += 1
        else:
            errors.append(msg)

    print(f"✅ 成功 {ok} / {len(card_positions)}")
    for k, v in changes.items():
        print(f"   {k}: {v}")
    if errors:
        print(f"❌ 失败 {len(errors)}:")
        for e in errors[:20]:
            print(f"   {e}")


if __name__ == "__main__":
    main()
