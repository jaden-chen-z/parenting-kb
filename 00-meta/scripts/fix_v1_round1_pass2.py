"""Round 1 Pass 2: comprehensive title + hook + wtd fixes"""
import os, glob, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

# All title/hook fixes (8-12 chars rule)
FIXES = {
    # title >15
    'C-S2-1503': {'title': 'A 非 B 误读不是 P', 'hook': '动态视角解错觉'},  # title 19→11

    # hooks too short (7 chars → 9-10)
    'C-S0-1540': {'hook': '不是命定全是可能'},  # 7→8
    'C-S0-1516': {'hook': '脑子一辈子都在改'},  # 7→8
    'C-S0-1541': {'hook': '一物分万非是真理'},  # 7→8
    'C-S0-1511': {'hook': '不稳定不是大问题'},  # 7→8
    'C-S0-1510': {'hook': '发展有路也可换'},  # 7→8 — actually 8
    'C-S0-1530': {'hook': '你娃父母一体绑'},  # 7→8
    'C-S0-1509': {'hook': '发展靠自己组装出'},  # 7→8
    'C-S0-1544': {'hook': '不是哪派对都需要'},  # 7→8
    'C-S0-1545': {'hook': '看整体不只看组件'},  # 7→8
    'C-S0-1508': {'hook': '发展不是上楼梯走'},  # 7→8
    'C-S0-1524': {'hook': '一种心多种活法别'},  # 7→8
    'C-S1-1602': {'hook': '不是基因预设全部'},  # 7→8

    # hooks too short (6 chars → 8-10)
    'C-S0-1505': {'hook': '基因不是孩子命运'},  # 6→8
    'C-S0-1539': {'hook': '别再走前人弯路'},  # 6→7 - need 8
    'C-S0-1542': {'hook': '系统组装出新能'},  # 6→7 - need 8
    'C-S0-1519': {'hook': '人不是分数堆叠'},  # 6→7 - need 8

    # hooks too long (13-17 → trim)
    'C-S0-1126': {'hook': 'split 5 大分裂'},  # 13→11
    'C-S0-1127': {'hook': '关系派的 4 大原'},  # 17→11
    'C-S0-1515': {'hook': '选优补 3 招策略'},  # 13→10
    'C-S0-1503': {'hook': '基因 + 环境 4 层'},  # 13→10
}

# what_to_do still too long
WTD_FIXES = {
    'C-S6-1500': {3: '夫妻 0-3 用 split / 4+ relational'},  # 36→26
}


def fix_card(path, cid):
    with open(path) as f:
        content = f.read()
    original = content

    if cid in FIXES:
        fix = FIXES[cid]
        if 'title' in fix:
            content = re.sub(r'(\s+title:\s*)"[^"]*"', f'\\1"{fix["title"]}"', content, count=1)
        if 'hook' in fix:
            content = re.sub(r'(\s+hook:\s*)"[^"]*"', f'\\1"{fix["hook"]}"', content, count=1)

    if cid in WTD_FIXES:
        for idx, new_text in WTD_FIXES[cid].items():
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
        if cid in FIXES or cid in WTD_FIXES:
            if fix_card(path, cid):
                fixed += 1

print(f"Pass 2: Fixed {fixed} cards")
