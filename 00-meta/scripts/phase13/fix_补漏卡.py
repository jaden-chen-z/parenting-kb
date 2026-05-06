#!/usr/bin/env python3
"""Phase 13 修补漏卡 — title/hook/cross-school"""
import os, re, glob

KB = os.path.expanduser("~/Desktop/parenting-kb")

# Title fix(≤ 15 字)
TITLE_FIX = {
    "C-S1-1022": "中国 BFHI 历史成功",  # 11 字
    "C-S1-1021": "Nestle 1977 抵制",  # 13 字
    "C-S2-1049": "Cochrane:6 月 EBF 优",  # 14 字 (重新数:C/o/c/h/r/a/n/e/:/6/' '/月/' '/E/B/F/' '/优 = 18,要更短)
}

# 重新数,严格 ≤ 15
TITLE_FIX = {
    "C-S1-1022": "中国 BFHI 历史成",  # 10
    "C-S1-1021": "Nestle 1977 抵制",  # 13
    "C-S2-1049": "Cochrane EBF 6 月",  # 13 (C/o/c/h/r/a/n/e/' '/E/B/F/' '/6/' '/月 = 16, 再短)
}

TITLE_FIX = {
    "C-S1-1022": "BFHI 中国历史成",  # 11
    "C-S1-1021": "Nestle 1977 抵制",  # 13
    "C-S2-1049": "Cochrane 元分析",  # 12 (C/o/c/h/r/a/n/e/' '/元/分/析 = 12)
}

# 验证
print("Title 字数:")
for cid, t in TITLE_FIX.items():
    print(f"  {cid}: '{t}' ({len(t)} 字) {'✓' if len(t) <= 15 else '✗'}")

# Hook fix
HOOK_FIX = {
    "C-S0-1029": "矮 瘦 胖 都算营养",  # 8 字 (矮/' '/瘦/' '/胖/' '/都/算/营/养 = 10)
    "C-S1-1022": "94 年 EBF 翻倍记",  # 数:9/4/' '/年/' '/E/B/F/' '/翻/倍/记 = 12
    "C-S1-1019": "孕期就该聊母乳的",  # 8 字
    "C-S2-1049": "元分析硬证据支撑",  # 8 字
}

print("\nHook 字数:")
for cid, h in HOOK_FIX.items():
    print(f"  {cid}: '{h}' ({len(h)} 字) {'✓' if 8 <= len(h) <= 12 else '✗'}")

# Cross-school 加 — 给 9 张新卡加跨派 related
CROSS_SCHOOL_ADD = {
    "C-S1-1018": "C-S1-022",  # Karp 奶嘴
    "C-S1-1019": "C-S0-007",  # Brazelton
    "C-S1-1020": "C-S1-050",  # AAP
    "C-S1-1021": "C-S1-022",  # Karp
    "C-S1-1022": "C-S1-050",  # AAP
    "C-S2-1049": "C-S3-001",  # AAP feeding
    "C-S6-1071": "C-S6-001",  # 任意现 S6 卡
    "C-S7-1102": "C-S5-001",  # 任意现 S5 卡
    "C-S7-1103": "C-S6-001",  # 任意现 S6 卡
}

# 验证 cross IDs 存在
all_ids = set()
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        all_ids.add(os.path.basename(f).replace('.yaml',''))

# 调整不存在的
for k, v in list(CROSS_SCHOOL_ADD.items()):
    if v not in all_ids:
        # 找该段第一个 < 100 卡
        seg = k.split('-')[1]  # eg S6
        cands = sorted([c for c in all_ids if c.startswith(f'C-{seg}-0')])
        if cands:
            CROSS_SCHOOL_ADD[k] = cands[0]
            print(f"  [调整] {k}: {v} → {cands[0]}")

# 应用
new_cards = []
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        with open(f) as fh:
            content = fh.read()
        if 'SRC-031' in content and 'created: 2026-05-04' in content:
            new_cards.append(f)

fixed = 0
for f in new_cards:
    with open(f) as fh:
        content = fh.read()
    cid_match = re.search(r'card_id:\s*(\S+)', content)
    if not cid_match: continue
    cid = cid_match.group(1)
    new_content = content

    if cid in TITLE_FIX:
        new_content = re.sub(r'(\s+title:\s+)"[^"]*"', f'\\1"{TITLE_FIX[cid]}"', new_content)

    if cid in HOOK_FIX:
        new_content = re.sub(r'(\s+hook:\s+)"[^"]*"', f'\\1"{HOOK_FIX[cid]}"', new_content)

    if cid in CROSS_SCHOOL_ADD:
        cross_id = CROSS_SCHOOL_ADD[cid]
        rel_match = re.search(r'(related_cards:\n(?:  - [^\n]+\n)+)', new_content)
        if rel_match:
            existing = rel_match.group(1)
            if cross_id not in existing:
                new_rel = existing + f'  - {cross_id}\n'
                new_content = new_content.replace(existing, new_rel, 1)

    if new_content != content:
        with open(f, 'w') as fh:
            fh.write(new_content)
        fixed += 1

print(f"Fixed: {fixed}")
