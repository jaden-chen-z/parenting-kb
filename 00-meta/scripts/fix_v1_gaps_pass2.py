"""Pass 2: hook 字数 + cross-school"""
import os, glob, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

HOOK_FIXES = {
    'C-S0-1550': '不是单一一条路径',  # 6→8
    'C-S0-1551': '信仰怎么慢慢长大',  # 7→8
    'C-S0-1552': '童心是进化的优势',  # 7→8
    'C-S0-1549': '世代差距是真存在',  # 7→8
    'C-S6-1513': '神死命运谁负责',  # 6→7 → fix to 8
}
HOOK_FIXES['C-S6-1513'] = '神死命谁来负责'  # 8

# Replace last related with cross-school
CROSS_SCHOOL = {
    'C-S0-1550': 'C-S0-008',  # AAP general
    'C-S0-1551': 'C-S0-722',  # Lerner V3
    'C-S0-1552': 'C-S0-722',
    'C-S0-1549': 'C-S0-727',  # Lerner V3 Bronfenbrenner
    'C-S6-1513': 'C-S6-1078',  # Lerner V3 Kochanska
    'C-S0-1547': 'C-S0-722',
    'C-S0-1548': 'C-S0-722',
    'C-S0-1553': 'C-S6-1505',  # already might be cross — but ensure
    'C-S8-1146': 'C-S0-727',
}


def fix_card(path, cid):
    with open(path) as f:
        content = f.read()
    original = content

    if cid in HOOK_FIXES:
        new_hook = HOOK_FIXES[cid]
        content = re.sub(r'(\s+hook:\s*)"[^"]*"', f'\\1"{new_hook}"', content, count=1)

    if cid in CROSS_SCHOOL:
        new_ref = CROSS_SCHOOL[cid]
        # Replace last related card
        in_related = False
        last_idx = None
        lines = content.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == 'related_cards:':
                in_related = True
                continue
            if in_related and stripped.startswith('citation:'):
                in_related = False
                continue
            if in_related and stripped.startswith('- '):
                last_idx = i
        if last_idx is not None and new_ref not in '\n'.join(lines):
            indent = lines[last_idx][:len(lines[last_idx]) - len(lines[last_idx].lstrip())]
            lines[last_idx] = f'{indent}- {new_ref}'
            content = '\n'.join(lines)

    if content != original:
        with open(path, 'w') as f:
            f.write(content)
        return True
    return False


fixed = 0
for seg in os.listdir(BASE):
    seg_path = os.path.join(BASE, seg)
    if not os.path.isdir(seg_path): continue
    for path in glob.glob(f'{seg_path}/C-*.yaml'):
        cid = os.path.basename(path).replace('.yaml', '')
        if cid in HOOK_FIXES or cid in CROSS_SCHOOL:
            if fix_card(path, cid):
                fixed += 1

print(f"Pass 2: Fixed {fixed} cards")
