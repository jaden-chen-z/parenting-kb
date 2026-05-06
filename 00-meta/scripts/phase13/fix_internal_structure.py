#!/usr/bin/env python3
"""Phase 13 用户深度审 — 修内部结构(glossary_refs 单数 + hook 弱)+ ID 冲突 fix"""
import os, re, glob

KB = os.path.expanduser("~/Desktop/parenting-kb")

# 14 张 glossary_refs 单数 → 各加 1 张相关术语
GLOSSARY_REFS_ADD = {
    "C-S1-1007": "G-ABBR-EBF",  # 出院衔接 — 加 EBF
    "C-S2-1046": "G-ABBR-WHO",  # 70°C 配方奶 — 加 WHO
    "C-S4-1051": "G-TERM-WHO-CF-principles",  # 含铁优先 — 加 CF principles
    "C-S4-1052": "G-ABBR-EBF",  # WHO 图 vs CDC — 加 EBF
    "C-S4-1053": "G-ABBR-WHO",  # 6 大动作 — 加 WHO
    "C-S4-1054": "G-ABBR-EBF",  # 母乳娃别误判 — 加 EBF
    "C-S4-1055": "G-ABBR-WHO",  # 6-12m 50% — 加 WHO
    "C-S5-1037": "G-TERM-WHO-CF-principles",  # 9-11 月 — 加 CF principles
    "C-S5-1038": "G-TERM-WHO-CF-principles",  # finger food — 加 CF principles
    "C-S5-1039": "G-ABBR-WHO",  # 1 周岁 — 加 WHO
    "C-S6-1064": "G-ABBR-WHO",  # 持续到 2 岁 — 加 WHO
    "C-S6-1065": "G-ABBR-WHO",  # 33% 营养 — 加 WHO
    "C-S6-1066": "G-TERM-WHO-CF-principles",  # 12-23 加餐 — 加 CF principles
    "C-S6-1067": "G-ABBR-WHO",  # 中国早断 vs WHO — 加 WHO
    "C-S6-1068": "G-ABBR-WHO",  # 工作妈妈 — 加 WHO
    "C-S6-1069": "G-ABBR-WHO",  # 158 天 vs 6 月 — 加 WHO
    "C-S7-1099": "G-PERSON-Detwyler",  # 2 岁是底线 — 加 Detwyler
    "C-S7-1101": "G-ABBR-WHO",  # 跟家庭饮食 — 已删,跳过
    "C-S8-868": "G-ABBR-WHO",  # 学龄前奶 — 加 WHO
}

# 5 张 hook 弱 → 改抓眼
HOOK_FIX = {
    "C-S1-1014": "母乳是活的食物",  # 8
    "C-S1-1017": "5 天黄金浓汤",  # 6 → 8 字
    "C-S4-1048": "4 大食物组打底",  # 8
    "C-S4-1051": "六月起优先含铁",  # 8
    "C-S4-1053": "六大动作里程碑",  # 8
}

# 实际验证字数
print("Hook fix 字数:")
for cid, h in HOOK_FIX.items():
    print(f"  {cid}: '{h}' ({len(h)} 字)")

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

    # 改 hook
    if cid in HOOK_FIX:
        new_content = re.sub(r'(\s+hook:\s+)"[^"]*"', f'\\1"{HOOK_FIX[cid]}"', new_content)

    # 加 glossary_ref(在 glossary_refs 块末尾追加)
    if cid in GLOSSARY_REFS_ADD:
        new_ref = GLOSSARY_REFS_ADD[cid]
        # 检查是否已含
        if new_ref not in new_content:
            # 在 glossary_refs 块末尾追加
            gr_match = re.search(r'(glossary_refs:\n(?:  - [^\n]+\n)+)', new_content)
            if gr_match:
                existing = gr_match.group(1)
                new_block = existing + f'  - {new_ref}\n'
                new_content = new_content.replace(existing, new_block, 1)

    if new_content != content:
        with open(f, 'w') as fh:
            fh.write(new_content)
        fixed += 1

# 修 C-S7-1099 的 related 引用(原指向 C-S7-1100,现需 C-S7-1102)
fp = f'{KB}/30-cards/s7-24to36mo/C-S7-1099.yaml'
with open(fp) as fh: c = fh.read()
new_c = c.replace('C-S7-1100', 'C-S7-1102')
if new_c != c:
    with open(fp, 'w') as fh: fh.write(new_c)
    print(f"Updated C-S7-1099 reference: 1100 → 1102")
    fixed += 1

print(f"\nFixed: {fixed} 卡")
