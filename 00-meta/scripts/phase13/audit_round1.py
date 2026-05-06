#!/usr/bin/env python3
"""Phase 13 Round 1 机器审 — title/hook/wtd/fm/refs/related/cross-school"""
import os, yaml, glob, re

KB = os.path.expanduser("~/Desktop/parenting-kb")

# 收集本次新建的 SRC-031 卡
new_cards = []
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'SRC-031' in content and 'created: 2026-05-04' in content:
            new_cards.append(f)

# 收集所有现有卡(用于 related 验证)
all_card_ids = set()
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        cid = os.path.basename(f).replace('.yaml', '')
        all_card_ids.add(cid)

# 收集所有 glossary IDs
all_glossary = set()
for f in glob.glob(f'{KB}/40-glossary/*.yaml'):
    g_id = os.path.basename(f).replace('.yaml', '')
    all_glossary.add(g_id)

print(f"=== Phase 13 Round 1 机器审 ===")
print(f"SRC-031 cards: {len(new_cards)}")
print(f"All cards: {len(all_card_ids)}")
print(f"All glossary: {len(all_glossary)}")
print()

# 描述型 hook 关键词
DESCRIPTIVE = ['是什么', '说明', '介绍', '概念', '定义', '解释', '描述', '阐述']

# 18+ 派识别 — related_cards 中含这些 ID 模式则视为跨派
SCHOOL_PREFIXES = {
    'AAP': 'C-S[0-9]-(05[0-9]|0[0-2][0-9]|003|004|005|006|007|008)',  # SRC-006 AAP
    'Karp': 'C-S1-(0[0-3][0-9]|22)',  # SRC-005 Karp
    '鲍秀兰': 'C-S[0-9]-(2[0-9]{2}|0[0-9]{2})',  # SRC-009
    '松田': 'C-S[0-9]-7[0-9]{2}',  # SRC-024 松田 ID 700+
    'Brazelton': '',  # SRC-010
    'Bowlby': '',  # SRC-011/013/017
    'Wonder Weeks': '',  # SRC-012
    'Davies': '',  # SRC-014
    'Gopnik': '',  # SRC-015
    'Lillard': '',  # SRC-016
    'Stern': '',  # SRC-018
    'Lansbury': '',  # SRC-019
    'Gerber': '',  # SRC-021/022
    'Pikler': '',  # SRC-026
    'Shonkoff': '',  # SRC-025
    'Lerner V1': 'C-S[0-9]-15[0-9]{2}',  # SRC-030
    'Lerner V2': 'C-S[0-9]-13[0-9]{2}',  # SRC-027
    'Lerner V3': 'C-S[0-9]-14[0-9]{2}',  # SRC-028
    'Lerner V4': 'C-S[0-9]-12[0-9]{2}',  # SRC-029
    'Montessori': '',  # SRC-007/Lillard
}

errors = {
    'title_long': [],
    'hook_wrong': [],
    'wtd_long': [],
    'fm_long': [],
    'descriptive_hook': [],
    'no_glossary': [],
    'broken_glossary': [],
    'no_related': [],
    'broken_related': [],
    'self_ref': [],
    'no_cross_school': [],
}

cards_data = {}
for f in new_cards:
    with open(f, 'r', encoding='utf-8') as fh:
        d = yaml.safe_load(fh)
    cards_data[d['card_id']] = d

for cid, d in cards_data.items():
    front = d.get('front', {})
    back = d.get('back', {})
    title = front.get('title', '')
    hook = front.get('hook', '')

    # title ≤ 15
    if len(title) > 15:
        errors['title_long'].append(f"{cid}: '{title}' ({len(title)} chars)")

    # hook 8-12
    hl = len(hook)
    if hl < 8 or hl > 12:
        errors['hook_wrong'].append(f"{cid}: '{hook}' ({hl} chars)")

    # descriptive hook
    if any(kw in hook for kw in DESCRIPTIVE):
        errors['descriptive_hook'].append(f"{cid}: '{hook}'")

    # what_to_do ≤ 35 each
    wtd = back.get('what_to_do', [])
    for i, item in enumerate(wtd):
        if len(item) > 35:
            errors['wtd_long'].append(f"{cid} wtd[{i}]: '{item[:40]}...' ({len(item)} chars)")

    # failure_mode lines ≤ 80
    fm = back.get('failure_mode', '')
    for line in fm.split('\n'):
        if len(line) > 80:
            errors['fm_long'].append(f"{cid}: '{line[:60]}...' ({len(line)} chars)")

    # glossary_refs
    refs = d.get('glossary_refs', []) or []
    if not refs:
        errors['no_glossary'].append(cid)
    for r in refs:
        if r not in all_glossary:
            errors['broken_glossary'].append(f"{cid}: {r}")

    # related_cards
    related = d.get('related_cards', []) or []
    if not related:
        errors['no_related'].append(cid)
    for r in related:
        if r == cid:
            errors['self_ref'].append(f"{cid}: {r}")
        elif r not in all_card_ids:
            errors['broken_related'].append(f"{cid}: {r}")

    # cross-school check: 至少有 1 张 related 不是本卷 SRC-031 ID(SRC-031 用 1000+)
    src031_pattern = re.compile(r'C-S[0-9]-1[0-9]{3}|C-S8-868')
    cross_count = sum(1 for r in related if not src031_pattern.match(r))
    if cross_count == 0 and related:
        errors['no_cross_school'].append(cid)

# 输出报告
total_errors = sum(len(v) for v in errors.values())
print(f"=== Round 1 总错误数: {total_errors} ===\n")

for cat, issues in errors.items():
    if issues:
        print(f"--- {cat}: {len(issues)} ---")
        for issue in issues[:10]:
            print(f"  {issue}")
        if len(issues) > 10:
            print(f"  ... +{len(issues)-10} more")
        print()
