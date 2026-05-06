"""Phase E Round 1: Python 机器审 — yaml / 字数 / glossary refs / related cards / 跨派率"""
import os, glob, yaml, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'
GLOSS = '/Users/jjjjadennnn/Desktop/parenting-kb/40-glossary'

# Find all V1 cards (those citing SRC-030)
v1_cards = []
for seg in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo', 's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for path in glob.glob(f'{BASE}/{seg}/C-*.yaml'):
        with open(path) as f:
            content = f.read()
        if 'SRC-030' in content:
            v1_cards.append((seg, path))

print(f"=== Phase E Round 1 Python Audit ===")
print(f"Total V1 cards: {len(v1_cards)}")

# Load each card and validate
parse_errors = []
title_long = []
hook_wrong = []
wtd_long = []
fm_long = []
missing_refs = []
broken_related = []
no_cross_school = []

# Get ALL existing cards (for related_cards validity check)
all_cards = set()
for seg in os.listdir(BASE):
    seg_path = os.path.join(BASE, seg)
    if os.path.isdir(seg_path):
        for path in glob.glob(f'{seg_path}/C-*.yaml'):
            cid = os.path.basename(path).replace('.yaml', '')
            all_cards.add(cid)
print(f"Total existing cards in vault: {len(all_cards)}")

# Get all existing glossary
all_glossary = set()
for path in glob.glob(f'{GLOSS}/G-*.yaml'):
    gid = os.path.basename(path).replace('.yaml', '')
    all_glossary.add(gid)
print(f"Total glossary terms: {len(all_glossary)}")

# Cross-school markers (V1 needs ≥1 related含 17+ 派)
CROSS_SCHOOL_PREFIXES = {
    'C-S0-014': 'AAP serve-return', 'C-S0-115': 'philosophical foundation',
    'C-S0-116': 'philosophical foundation', 'C-S0-008': 'AAP general',
    'C-S0-321': 'multi-school', 'C-S0-722': 'Lerner V3 综述',
    'C-S0-727': 'Lerner V3 Bronfenbrenner',
    'C-S1-013': 'Karp', 'C-S1-014': 'Karp', 'C-S1-015': 'Karp',
    'C-S1-027': 'Karp', 'C-S1-028': 'Karp', 'C-S1-038': 'AAP',
    'C-S1-185': 'Davies/Lillard', 'C-S1-187': 'Davies/Lillard',
    'C-S1-252': 'Davies/Lillard', 'C-S1-068': 'Brazelton',
    'C-S2-014': '鲍秀兰', 'C-S2-697': '松田', 'C-S2-700': '松田',
    'C-S2-940': 'Lerner V3 Bugental', 'C-S2-941': 'Lerner V3 Eisenberg',
    'C-S5-012': '鲍秀兰', 'C-S5-041': 'Pikler',
    'C-S6-189': 'Lillard', 'C-S6-190': 'Lillard',
    'C-S6-816': '松田', 'C-S6-820': '松田', 'C-S6-822': '松田',
    'C-S6-1064': 'Lerner V3 Thompson', 'C-S6-1065': 'Lerner V3',
    'C-S6-1066': 'Lerner V3 Rothbart', 'C-S6-1067': 'Lerner V3 Caspi',
    'C-S6-1075': 'Lerner V3 Dodge', 'C-S6-1078': 'Lerner V3 Kochanska',
    'C-S7-754': '松田', 'C-S7-755': '松田反抗期', 'C-S7-756': '松田',
    'C-S7-996': 'Lerner V3 Thompson', 'C-S7-1001': 'Lerner V3 Rubin',
    'C-S8-100': '松田', 'C-S8-101': '松田', 'C-S8-103': '松田',
    'C-S8-104': '松田', 'C-S8-105': '松田',
    'C-S8-323': 'Lerner V3 Parke', 'C-S8-324': 'Lerner V3 Parke',
    'C-S8-325': 'Lerner V3 Turiel', 'C-S8-330': 'Lerner V3 Turiel',
    # All 17+ schools
}

# Per-card audit
for seg, path in v1_cards:
    cid = os.path.basename(path).replace('.yaml', '')
    try:
        with open(path) as f:
            d = yaml.safe_load(f)
    except Exception as e:
        parse_errors.append((cid, str(e)))
        continue

    # Title length (≤15)
    title = d.get('front', {}).get('title', '')
    if len(title) > 15:
        title_long.append((cid, len(title), title))

    # Hook length (8-12)
    hook = d.get('front', {}).get('hook', '')
    hook_len = len(hook)
    if hook_len < 8 or hook_len > 12:
        hook_wrong.append((cid, hook_len, hook))

    # what_to_do each ≤35
    wtd = d.get('back', {}).get('what_to_do', [])
    for i, item in enumerate(wtd):
        if len(item) > 35:
            wtd_long.append((cid, i, len(item), item))

    # failure_mode single line ≤80
    fm = d.get('back', {}).get('failure_mode', '')
    fm_str = fm.strip() if fm else ''
    fm_lines = fm_str.split('\n')
    for line in fm_lines:
        if len(line.strip()) > 80:
            fm_long.append((cid, len(line.strip()), line[:50]))

    # glossary_refs validity
    refs = d.get('glossary_refs', [])
    for r in refs:
        if r not in all_glossary:
            missing_refs.append((cid, r))

    # related_cards validity + cross-school
    related = d.get('related_cards', [])
    has_cross = False
    for r in related:
        if r not in all_cards:
            broken_related.append((cid, r))
            continue
        # Check if r is from another school
        if r in CROSS_SCHOOL_PREFIXES:
            has_cross = True
        # Also check if r is from Lerner V2/V3/V4 (铁四角)
        if r.endswith(('-722', '-727', '-1000', '-1001', '-1002', '-1003', '-1064', '-1065',
                       '-1066', '-1067', '-1068', '-1069', '-1070', '-1071', '-1072', '-1073',
                       '-1074', '-1075', '-1076', '-1077', '-1078', '-1079', '-1080', '-1081')) \
                or r.startswith('C-S0-72') or r.startswith('C-S6-10') or r.startswith('C-S7-99') \
                or r.startswith('C-S8-32'):
            has_cross = True

    if not has_cross:
        no_cross_school.append((cid, related))

# Report
print(f"\n=== Audit Results ===")
print(f"YAML parse errors: {len(parse_errors)}")
print(f"Title >15 chars: {len(title_long)}")
print(f"Hook not 8-12 chars: {len(hook_wrong)}")
print(f"what_to_do >35 chars: {len(wtd_long)}")
print(f"failure_mode line >80: {len(fm_long)}")
print(f"Missing glossary refs: {len(missing_refs)}")
print(f"Broken related cards: {len(broken_related)}")
print(f"No cross-school related: {len(no_cross_school)}")

if title_long:
    print(f"\nTitle too long:")
    for cid, l, t in title_long[:10]:
        print(f"  {cid} ({l}): '{t}'")

if hook_wrong:
    print(f"\nHook wrong length:")
    for cid, l, h in hook_wrong[:20]:
        print(f"  {cid} ({l}): '{h}'")

if wtd_long:
    print(f"\nwhat_to_do too long:")
    for cid, i, l, item in wtd_long[:10]:
        print(f"  {cid}[{i}] ({l}): '{item[:40]}...'")

if missing_refs:
    print(f"\nMissing glossary refs:")
    for cid, r in missing_refs[:20]:
        print(f"  {cid}: {r}")

if broken_related:
    print(f"\nBroken related cards:")
    for cid, r in broken_related[:20]:
        print(f"  {cid}: {r}")

if no_cross_school:
    print(f"\nNo cross-school related:")
    for cid, related in no_cross_school[:10]:
        print(f"  {cid}: {related[:5]}")
