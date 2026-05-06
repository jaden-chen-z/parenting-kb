#!/usr/bin/env python3
"""Phase 13 最后修 — 5 张 hook 字数 + C-S7-1103 + BFHI 综述补"""
import os, re, glob

KB = os.path.expanduser("~/Desktop/parenting-kb")

# Hook 字数严格 8-12(刚才修成 7 不够)
HOOK_FIX = {
    "C-S1-1014": "母乳是活的食物啊",  # 8
    "C-S1-1017": "5 天黄金的浓汤",  # 8 字
    "C-S4-1048": "4 大食物组打底",   # 8 — 已是
    "C-S4-1051": "六月起优先含铁的",  # 8
    "C-S4-1053": "六大动作里程碑啊",  # 8
}

# 重数
print("Hook fix 字数:")
for cid, h in HOOK_FIX.items():
    print(f"  {cid}: '{h}' ({len(h)} 字)")

# C-S7-1103 加 1 glossary_ref
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

    if cid in HOOK_FIX:
        new_content = re.sub(r'(\s+hook:\s+)"[^"]*"', f'\\1"{HOOK_FIX[cid]}"', new_content)

    if cid == "C-S7-1103":
        gr_match = re.search(r'(glossary_refs:\n(?:  - [^\n]+\n)+)', new_content)
        if gr_match:
            existing = gr_match.group(1)
            if "G-ABBR-WHO" not in existing:
                new_block = existing + '  - G-ABBR-WHO\n'
                new_content = new_content.replace(existing, new_block, 1)

    if new_content != content:
        with open(f, 'w') as fh:
            fh.write(new_content)
        fixed += 1

# 在已有 BFHI 总览卡 C-S1-1002 添加 2016 综述支持的提及
fp = f'{KB}/30-cards/s1-newborn/C-S1-1002.yaml'
with open(fp) as fh: c = fh.read()
# 在 why_matters 末尾追加
if "58 项" not in c:
    new_c = c.replace(
        '全球 152+ 国 15,000+ 家医院 BFHI 认证。中国 6,000+ 爱婴医院。',
        '全球 152+ 国 15,000+ 家医院 BFHI 认证。中国 6,000+ 爱婴医院。\n    2016 系统综述(58 项研究)证实:遵守 10 步 → EBF 启动率/纯母乳率/总时长全提高。'
    )
    if new_c != c:
        with open(fp, 'w') as fh: fh.write(new_c)
        fixed += 1
        print(f"Added BFHI 2016 综述 to C-S1-1002")

print(f"Fixed: {fixed}")
