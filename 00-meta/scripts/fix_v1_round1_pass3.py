"""Round 1 Pass 3: extend remaining short hooks to 8+ chars"""
import os, glob, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

# All remaining 6-7 char hooks → 8-9 chars
HOOK_FIXES = {
    'C-S0-1510': '发展有路也是可换',  # 7→8
    'C-S0-1530': '你娃父母人生绑定',  # 7→8
    'C-S0-1539': '别再走前人的弯路',  # 7→8
    'C-S0-1542': '系统组装出新能力',  # 7→8
    'C-S0-1519': '人不是分数的堆叠',  # 7→8
    'C-S2-1505': '日常陪伴就是引擎',  # 7→8
    'C-S2-1503': '动态视角解 P 错觉',  # 7→8
    'C-S4-1644': '不是突然就懂的事',  # 6→8
    'C-S6-1510': '身份不是天生标签',  # 7→8
    'C-S6-1506': '美式标准非是真理',  # 7→8
    'C-S6-1511': '信仰小时候就萌芽',  # 7→8
    'C-S6-1504': '没有两个娃是一样',  # 6→8
    'C-S6-1512': '都重要但要分情境',  # 7→8
    'C-S6-1509': '时机决定影响大小',  # 7→8
    'C-S6-1502': '细颗粒度看发展期',  # 7→8
    'C-S6-1503': '不抢早就真没了吗',  # 7→8
    'C-S7-1603': '统计骗人个体才真',  # 7→8
    'C-S7-1605': '为做而做不为奖励',  # 7→8
    'C-S7-1608': '能做的事多了自信',  # 7→8
    'C-S8-1144': '不是死套不是全反',  # 7→8
}


def fix_card(path, cid):
    with open(path) as f:
        content = f.read()
    original = content

    if cid in HOOK_FIXES:
        new_hook = HOOK_FIXES[cid]
        content = re.sub(r'(\s+hook:\s*)"[^"]*"', f'\\1"{new_hook}"', content, count=1)

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
        if cid in HOOK_FIXES:
            if fix_card(path, cid):
                fixed += 1

print(f"Pass 3: Fixed {fixed} hooks")
