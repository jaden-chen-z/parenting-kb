#!/usr/bin/env python3
"""Phase 13 Round 1 Pass 3 — hook 美化(去 '啊' 后缀)"""
import os, re, glob

KB = os.path.expanduser("~/Desktop/parenting-kb")

# 去掉之前的 '啊' 后缀,换成更自然的 8 字 hook
HOOK_FIX = {
    "C-S1-1010": "奶瓶奶嘴都监管的",  # 8
    "C-S2-1044": "看娃信号别看时表",  # 8
    "C-S4-1051": "肉鱼蛋黄优先吃",  # 7 → 加字 "肉鱼蛋黄优先做的" 8
    "C-S4-1048": "色彩多营养就齐了",  # 8
    "C-S4-1049": "泥糊渐进到家庭饭",  # 8
    "C-S4-1045": "辅食是补不是替代",  # 8
    "C-S4-1053": "独坐扶站爬扶走的",  # 8
    "C-S5-1037": "餐数升而母乳不减",  # 8
    "C-S6-1068": "挤奶储奶用杯子喂",  # 8
    "C-S6-1066": "餐数到顶加些点心",  # 8
    "C-S5-1038": "8 月起让娃自己抓",  # 8
    "C-S7-1099": "WHO beyond 是关键",  # 12
    # 剩 2 个 7 字
    "C-S6-1070": "营销话术莫上当",  # 7 → 8 字 "营销话术不要上当"
    "C-S7-1100": "等娃说不要喝奶",  # 7 → 8 字
}

# 重数确保 8-12
HOOK_FIX = {
    "C-S1-1010": "奶瓶奶嘴都管的呀",  # 8
    "C-S2-1044": "看娃信号别看时表",  # 8
    "C-S4-1051": "肉鱼蛋黄优先做的",  # 8
    "C-S4-1048": "色彩多营养就齐了",  # 8
    "C-S4-1049": "泥糊渐进到家庭饭",  # 8
    "C-S4-1045": "辅食是补不是替代",  # 8
    "C-S4-1053": "独坐扶站爬扶走的",  # 8
    "C-S5-1037": "餐数升母乳没减少",  # 8
    "C-S6-1068": "挤奶储奶用杯子喂",  # 8
    "C-S6-1066": "餐数到顶加些点心",  # 8
    "C-S5-1038": "8 月起让娃自己抓",  # 8
    "C-S7-1099": "WHO beyond 是关键",  # 12
    "C-S6-1070": "营销话术不要上当",  # 8
    "C-S7-1100": "等娃自己说不要了",  # 8
}

# 验证字数
print("Hook 字数验证:")
for cid, h in HOOK_FIX.items():
    n = len(h)
    ok = "✓" if 8 <= n <= 12 else "✗"
    print(f"  {ok} {cid}: '{h}' ({n})")

# 应用
new_cards = []
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'SRC-031' in content and 'created: 2026-05-04' in content:
            new_cards.append(f)

fixed = 0
for f in new_cards:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    cid = re.search(r'card_id:\s*(\S+)', content).group(1)
    if cid in HOOK_FIX:
        new_content = re.sub(r'(\s+hook:\s+)"[^"]*"', f'\\1"{HOOK_FIX[cid]}"', content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(new_content)
            fixed += 1

print(f"\nFixed: {fixed}")
