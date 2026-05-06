"""Round 1 Pass 4: final 6 hook fixes"""
import os, glob, re

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

HOOK_FIXES = {
    'C-S8-1133': '大环境定调全家家',  # 6→8 - actually use better
    'C-S8-1145': '看优势不是看缺点',  # 7→8
    'C-S8-1135': '上学焦虑要先清醒',  # 7→8
    'C-S8-1139': '太难太易都没心流',  # 7→8
    'C-S8-1143': '意义感终生很重要',  # 7→8
    'C-S8-1136': '不只听话才是品格',  # 7→8
}
# Actually fix C-S8-1133 better
HOOK_FIXES['C-S8-1133'] = '宏环境定调你家家'  # 8


def fix_card(path, cid):
    with open(path) as f:
        content = f.read()
    if cid not in HOOK_FIXES: return False
    new_hook = HOOK_FIXES[cid]
    new_content = re.sub(r'(\s+hook:\s*)"[^"]*"', f'\\1"{new_hook}"', content, count=1)
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        return True
    return False


fixed = 0
for seg in os.listdir(BASE):
    seg_path = os.path.join(BASE, seg)
    if not os.path.isdir(seg_path): continue
    for path in glob.glob(f'{seg_path}/C-*.yaml'):
        cid = os.path.basename(path).replace('.yaml', '')
        if fix_card(path, cid):
            fixed += 1

print(f"Pass 4: Fixed {fixed} hooks")
