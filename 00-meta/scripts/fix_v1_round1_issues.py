"""Fix Round 1 issues: title, hook, wtd, broken related, cross-school"""
import os, glob, yaml, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

# === Fix 1: Title >15 ===
TITLE_FIXES = {
    'C-S0-1500': 'B 氏 5 系统模型',  # was: Bronfenbrenner 5 系统 (19)
    'C-S6-1508': '1-2 岁多改环境',  # was: 1-2 岁多 assimilate (17)
    'C-S0-1532': 'PVEST 风险身份模型',  # length 14 - actually need to check
}

# === Fix 2: Hook 8-12 chars (currently <8 or >12) ===
HOOK_FIXES = {
    'C-S0-1501': '过程人环境时间 4 维',  # was 7 → 11
    'C-S0-1517': '老了智慧反而长大',  # 7 → 9
    'C-S0-1537': '认知精分行为 3 派',  # 7 → 10
    'C-S0-1126': 'split 派 5 大分裂',  # 14 → 12
    'C-S0-1527': '内驱力比奖励更强',  # 6 → 9
    'C-S0-1546': '不是文化灌入娃心',  # 7 → 9
    'C-S0-1513': '老了也能再发展啊',  # 7 → 9
    'C-S0-1128': '笛卡尔留下的大坑',  # 7 → 9
    'C-S0-1535': '不是单一心理学派',  # 7 → 9
    'C-S0-1543': '都对得看是哪一层',  # 6 → 9
    'C-S0-1538': '从笼统到精分化期',  # 7 → 9
    'C-S3-1646': '从混乱到清晰分化',  # 6 → 9
    'C-S6-1507': '专注玩耍千万别打扰',  # 6 → 10
    'C-S6-1508': '改家比改娃简单多',  # 6 → 9
    'C-S6-1505': '资产视角不是赤字',  # 6 → 9
    'C-S7-1602': '关系比能力更重要',  # 7 → 9
    'C-S7-1609': '社交体能也是能力',  # 7 → 9
    'C-S8-1144': '不是套不是反搬',  # 6 → 8
    'C-S8-1132': '上班压力会溅到娃',  # 7 → 9
    'C-S8-1142': '社会偏见会进童心',  # 7 → 9
    'C-S0-1532': '种族阶层入生态层',  # 7 → 9
}

# === Fix 3: what_to_do >35 chars ===
WTD_FIXES = {
    'C-S0-1501': {1: 'Person 看气质 — 配 Chess 适配'},  # 36 → 25
    'C-S0-1128': {3: '蒙氏 prepared env 是 relational 派', 4: 'Brazelton 个性化 = relational 派'},  # 47, 37 → ~30
    'C-S0-1125': {2: 'relational 派书:蒙氏 / RIE / Lerner'},  # 48 → 32
    'C-S6-1500': {3: '夫妻分工 — 0-3 用 split / 4+ 用 relational'},  # 44 → 30
    'C-S8-631': {3: '中国家庭 — split 给底线 + relational 给气质'},  # 49 → 30
}

# === Fix 4: Broken related cards ===
RELATED_FIXES = {
    'C-S0-1127': {'C-S0-321': 'C-S0-727'},  # 321 doesn't exist, replace with 727 (Lerner V3 Bronfenbrenner)
    'C-S5-1643': {'C-S5-041': 'C-S5-012'},  # 041 doesn't exist, replace with 012 (鲍秀兰把屎把尿)
}

# === Fix 5: Add cross-school related (replace one V1-internal with cross-school) ===
# Cards that need 1 cross-school added (replace last V1 ref with cross-school)
CROSS_SCHOOL_ADDS = {
    'C-S0-1540': 'C-S0-008',     # Add AAP general
    'C-S0-1536': 'C-S0-014',     # Add AAP serve-return
    'C-S0-1511': 'C-S0-722',     # Lerner V3 综述
    'C-S0-1545': 'C-S0-722',     # Lerner V3
    'C-S0-1542': 'C-S0-722',     # Lerner V3
    'C-S4-1644': 'C-S2-700',     # 松田
    'C-S6-1512': 'C-S6-1078',    # Lerner V3 Kochanska 良知
    'C-S6-1503': 'C-S6-189',     # Lillard 蒙氏
    'C-S8-1139': 'C-S6-816',     # 松田撒娇斥责
    'C-S8-1140': 'C-S7-755',     # 松田反 反抗期
}


def fix_card(path, cid):
    with open(path) as f:
        content = f.read()
    original = content

    # Fix title
    if cid in TITLE_FIXES:
        new_title = TITLE_FIXES[cid]
        content = re.sub(r'(\s+title:\s*)"[^"]*"', f'\\1"{new_title}"', content, count=1)

    # Fix hook
    if cid in HOOK_FIXES:
        new_hook = HOOK_FIXES[cid]
        content = re.sub(r'(\s+hook:\s*)"[^"]*"', f'\\1"{new_hook}"', content, count=1)

    # Fix what_to_do (replace specific items)
    if cid in WTD_FIXES:
        for idx, new_text in WTD_FIXES[cid].items():
            # Find what_to_do block, replace nth item
            in_wtd = False
            wtd_idx = 0
            new_lines = []
            for line in content.split('\n'):
                stripped = line.strip()
                if stripped == 'what_to_do:':
                    in_wtd = True
                    new_lines.append(line)
                    continue
                if in_wtd and (stripped.startswith('failure_mode:') or stripped.startswith('evidence_level:')):
                    in_wtd = False

                if in_wtd and stripped.startswith('- "'):
                    if wtd_idx == idx:
                        indent = line[:len(line) - len(line.lstrip())]
                        new_lines.append(f'{indent}- "{new_text}"')
                    else:
                        new_lines.append(line)
                    wtd_idx += 1
                else:
                    new_lines.append(line)
            content = '\n'.join(new_lines)

    # Fix broken related
    if cid in RELATED_FIXES:
        for old_ref, new_ref in RELATED_FIXES[cid].items():
            content = content.replace(f'  - {old_ref}\n', f'  - {new_ref}\n')

    # Add cross-school: replace last related with cross-school version
    if cid in CROSS_SCHOOL_ADDS:
        new_ref = CROSS_SCHOOL_ADDS[cid]
        # Find related_cards block, replace LAST item
        in_related = False
        last_related_idx = None
        lines = content.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == 'related_cards:':
                in_related = True
                continue
            if in_related and (stripped.startswith('citation:') or stripped == ''):
                if stripped.startswith('citation:'):
                    in_related = False
                continue
            if in_related and stripped.startswith('- '):
                last_related_idx = i

        if last_related_idx is not None:
            indent = lines[last_related_idx][:len(lines[last_related_idx]) - len(lines[last_related_idx].lstrip())]
            lines[last_related_idx] = f'{indent}- {new_ref}'
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
        if cid in TITLE_FIXES or cid in HOOK_FIXES or cid in WTD_FIXES or cid in RELATED_FIXES or cid in CROSS_SCHOOL_ADDS:
            if fix_card(path, cid):
                fixed += 1

print(f"Fixed {fixed} cards (title/hook/wtd/related/cross-school)")
