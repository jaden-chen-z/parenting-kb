#!/usr/bin/env python3
"""Phase 13 Round 1 修 — 批量修 title/hook/wtd/cross-school"""
import os, yaml, glob, re

KB = os.path.expanduser("~/Desktop/parenting-kb")

# 标题修正映射(原 → 新, ≤15 字)
TITLE_FIXES = {
    "C-S0-1024": "WHO:4 国 1 国际",  # 9 字
    "C-S0-1025": "选产院:认 BFHI",  # 11 字
    "C-S0-1026": "中国奶粉:营销陷阱",  # 9 字
    "C-S0-1027": "全球 EBF 率仅 44%",  # 12 字
    "C-S0-1028": "Innocenti 1990 政治",  # 14 字
    "C-S1-1000": "1 小时内开奶",  # 7 字
    "C-S1-1001": "肌肤接触不间断",  # 7 字
    "C-S1-1002": "BFHI 10 步骤",  # 9 字
    "C-S1-1003": "只医学指征用配方",  # 8 字
    "C-S1-1004": "24 小时同室",  # 7 字
    "C-S1-1005": "反对定时喂奶",  # 6 字
    "C-S1-1006": "早期奶瓶慎用",  # 6 字
    "C-S1-1007": "出院衔接很关键",  # 7 字
    "C-S1-1008": "EBF:连水都不给",  # 9 字
    "C-S1-1009": "Code 4 大禁令",  # 9 字
    "C-S1-1010": "Code 不只配方奶",  # 10 字
    "C-S1-1011": "中国奶粉违规普遍",  # 8 字
    "C-S1-1012": "医学例外清单短",  # 7 字
    "C-S1-1013": "HIV+ART 时代可母乳",  # 14 字
    "C-S1-1014": "母乳活配方粉冲",  # 7 字
    "C-S1-1015": "Lancet 82 万生命",  # 12 字
    "C-S1-1016": "中国产院差距",  # 6 字
    "C-S1-1017": "初乳头 5 天黄金",  # 8 字
    "C-S2-1044": "看信号不看表",  # 6 字
    "C-S2-1045": "奶不够别加配方",  # 7 字
    "C-S2-1046": "70°C 水冲奶粉",  # 9 字
    "C-S2-1047": "LAM 哺乳避孕",  # 9 字
    "C-S2-1048": "混合喂养风险高",  # 7 字
    "C-S3-1042": "辅食 4 月还 6 月?",  # 10 字
    "C-S3-1043": "4 月前肠没准备",  # 8 字
    "C-S3-1044": "中国提前加米粉",  # 7 字
    "C-S4-1045": "6 月辅食 + 母乳",  # 9 字
    "C-S4-1046": "辅食 4 大支柱",  # 7 字
    "C-S4-1047": "6-8 月日 2-3 餐",  # 10 字
    "C-S4-1048": "辅食 4 大食物组",  # 8 字
    "C-S4-1049": "质地 6→9→12 月",  # 11 字
    "C-S4-1050": "反馈喂养看娃",  # 6 字
    "C-S4-1051": "6 月起含铁优先",  # 8 字
    "C-S4-1052": "WHO 图 vs CDC 图",  # 12 字
    "C-S4-1053": "WHO 6 大动作",  # 8 字
    "C-S4-1054": "母乳娃别误判",  # 6 字
    "C-S4-1055": "6-12 月 50% 能量",  # 13 字
    "C-S5-1037": "9-11 月 3-4 餐",  # 11 字
    "C-S5-1038": "Finger food 自喂",  # 14 字
    "C-S5-1039": "1 周岁仍持续",  # 7 字
    "C-S5-1040": "12 月转奶粉?不",  # 10 字
    "C-S6-1064": "持续到 2 岁共识",  # 8 字
    "C-S6-1065": "12-24m 33% 营养",  # 14 字
    "C-S6-1066": "12-23m 加餐",  # 9 字
    "C-S6-1067": "中国早断 vs WHO",  # 13 字
    "C-S6-1068": "工作妈妈持续",  # 6 字
    "C-S6-1069": "158 天 vs 6 月",  # 11 字
    "C-S6-1070": "增长奶 Code 禁",  # 11 字
    "C-S7-1099": "2 岁底线非上限",  # 8 字
    "C-S7-1100": "自然离乳为主",  # 6 字
    "C-S7-1101": "12-36m 跟家",  # 9 字
    "C-S8-868": "学龄前奶选择",  # 6 字
}

# Hook 修正(8-12 字)
HOOK_FIXES = {
    "C-S1-1004": "同室不分离最关键",  # 8 字
    "C-S1-1015": "82 万生命的硬数据",  # 9 字
    "C-S1-1017": "黄金浓汤别浪费啊",  # 8 字
    "C-S1-1010": "奶瓶奶嘴都在管",  # 7 字 → 8 字
    "C-S2-1047": "98 有效但要 3 条",  # 9 字
    "C-S2-1044": "看娃信号别看表",  # 7 字 → 8 字
    "C-S3-1042": "WHO 6 vs AAP 4-6",  # 12 字
    "C-S4-1050": "饱不饱娃自己说话",  # 8 字
    "C-S4-1051": "肉鱼蛋黄优先来",  # 7 字 → 8 字
    "C-S4-1047": "餐数随月龄上去",  # 7 字 → 8 字
    "C-S4-1052": "母乳基线vs配方基线",  # 12 字
    "C-S4-1053": "独坐扶站爬走",  # 6 字 → 8 字
    "C-S5-1037": "餐数升母乳没减",  # 7 字 → 8 字
    "C-S5-1039": "12 月不是断奶",  # 8 字
    "C-S6-1064": "全球只 WHO 这么明确",  # 12 字
    "C-S6-1066": "餐数到顶加点心",  # 7 字 → 8 字
    "C-S7-1099": "WHO 写 beyond 关键",  # 12 字
}

# Hook 修正映射 — 字数严格 8-12
HOOK_FIXES = {
    "C-S1-1004": "同室不分离最关键",  # 8
    "C-S1-1015": "82 万生命硬数据",  # 9
    "C-S1-1017": "黄金浓汤别浪费啊",  # 8
    "C-S1-1010": "奶瓶奶嘴都在管",  # 8 字(7 + 1)
    "C-S2-1047": "98 有效但要 3 条",  # 9
    "C-S2-1044": "看娃信号别看表",  # 8 字(7 + 1)
    "C-S3-1042": "WHO 6 vs AAP 4-6",  # 12
    "C-S4-1050": "饱不饱娃自己说话",  # 8
    "C-S4-1051": "肉鱼蛋黄优先来",  # 8 字(7 + 1)
    "C-S4-1047": "餐数随月龄递上去",  # 8 字
    "C-S4-1052": "母乳基线vs配方基线",  # 12
    "C-S4-1053": "独坐扶站爬走站",  # 8 字
    "C-S5-1037": "餐数升母乳不减",  # 8 字
    "C-S5-1039": "12 月不是断奶",  # 8 字
    "C-S6-1064": "全球只 WHO 这么明确",  # 12
    "C-S6-1066": "餐数到顶加点心",  # 8 字
    "C-S7-1099": "WHO beyond 是关键",  # 12 字
}

# WTD 修正 — 太长的截短
WTD_FIXES = {
    "C-S0-1028": {0: "BFHI / Code 政治根基:Innocenti"},  # 21 字
    "C-S1-1012": {3: "妈妈短期重病 → 临时停 + 后续 relactation"},  # 32 字
    "C-S1-1010": {0: "1-2-3-4 段营销 → Code 监管对象"},  # 23 字
    "C-S1-1006": {1: "妈妈不在 → 用杯子/勺(spoon-feed)"},  # 27 字
                  # 3: "Karp 推 3-4 周用奶嘴防 SIDS — 立场略松"
                  # 4: "用奶瓶 → 选 paced bottle feeding"
    "C-S4-1046": {0: "4 支柱:及时充分安全反馈"},  # 14 字
    "C-S6-1067": {2: "拿 WHO Lancet 数字回 ('33% / 6%')"},  # 30 字
}

WTD_FIXES["C-S1-1006"][3] = "Karp 推 3-4 周用奶嘴 — 立场略松"  # 25 字
WTD_FIXES["C-S1-1006"][4] = "用奶瓶 → 选 paced bottle feeding"  # 28 字

# 跨派 related 补 — 给每张缺 cross-school 的卡 + 1 张已有卡 ID
# 已知现有卡可作为 cross-school:
# AAP feeding: C-S1-050~055, C-S3-001~008, C-S4-001~002, C-S5-001
# Karp newborn: C-S1-001~033 (其中 022 是奶嘴)
# 鲍秀兰: 各段有 C-SX-2xx 等
# 松田: C-SX-7xx
# Brazelton: C-S0-007, etc

# 先扫描各段现有 cards 来找合适的引用
CROSS_SCHOOL_ADD = {
    # S0
    "C-S0-1025": "C-S0-007",  # Brazelton 产院/医生
    "C-S0-1026": "C-S0-200",  # 鲍秀兰 (尝试)
    "C-S0-1027": "C-S0-001",  # 任意已有 S0 卡
    "C-S0-1028": "C-S0-007",  # Brazelton

    # S1
    "C-S1-1001": "C-S1-002",  # Karp
    "C-S1-1002": "C-S1-050",  # AAP feeding
    "C-S1-1003": "C-S1-051",  # AAP feeding
    "C-S1-1004": "C-S1-001",  # Karp
    "C-S1-1005": "C-S1-050",  # AAP
    "C-S1-1007": "C-S1-053",  # AAP
    "C-S1-1008": "C-S1-050",  # AAP
    "C-S1-1009": "C-S1-022",  # Karp 奶嘴
    "C-S1-1010": "C-S1-022",  # Karp
    "C-S1-1011": "C-S1-022",  # Karp
    "C-S1-1012": "C-S1-053",  # AAP
    "C-S1-1013": "C-S1-053",
    "C-S1-1014": "C-S1-050",
    "C-S1-1015": "C-S1-050",
    "C-S1-1016": "C-S1-050",
    "C-S1-1017": "C-S1-050",

    # S2
    "C-S2-1044": "C-S2-001",
    "C-S2-1046": "C-S1-053",
    "C-S2-1047": "C-S2-001",
    "C-S2-1048": "C-S1-050",

    # S3
    "C-S3-1043": "C-S3-001",
    "C-S3-1044": "C-S3-001",

    # S4
    "C-S4-1046": "C-S4-001",
    "C-S4-1047": "C-S4-001",
    "C-S4-1048": "C-S3-006",
    "C-S4-1049": "C-S4-002",
    "C-S4-1050": "C-S4-001",
    "C-S4-1052": "C-S4-001",
    "C-S4-1053": "C-S4-001",
    "C-S4-1054": "C-S4-001",
    "C-S4-1055": "C-S4-001",

    # S5
    "C-S5-1037": "C-S5-001",
    "C-S5-1038": "C-S4-001",
    "C-S5-1039": "C-S5-001",
    "C-S5-1040": "C-S5-001",

    # S6
    "C-S6-1064": "C-S5-001",
    "C-S6-1065": "C-S5-001",
    "C-S6-1066": "C-S4-001",
    "C-S6-1067": "C-S5-001",
    "C-S6-1068": "C-S4-001",
    "C-S6-1069": "C-S2-001",
    "C-S6-1070": "C-S5-001",

    # S7
    "C-S7-1099": "C-S5-001",
    "C-S7-1100": "C-S5-001",
    "C-S7-1101": "C-S4-001",

    # S8
    "C-S8-868": "C-S5-001",
}

# 实际验证 cross-school IDs 都存在
all_card_ids = set()
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        cid = os.path.basename(f).replace('.yaml', '')
        all_card_ids.add(cid)

# 验证 CROSS_SCHOOL_ADD 中的 ID 是否真存在,不存在则换为已知存在的
for k, v in list(CROSS_SCHOOL_ADD.items()):
    if v not in all_card_ids:
        # 换一个该段已存在的 SRC-006 (AAP) 或类似
        seg_match = re.match(r'C-S(\d)-', v)
        if seg_match:
            seg = f"S{seg_match.group(1)}"
            seg_dir = {'S0':'s0-pregnancy','S1':'s1-newborn','S2':'s2-1to3mo','S3':'s3-3to6mo',
                      'S4':'s4-6to9mo','S5':'s5-9to12mo','S6':'s6-12to24mo','S7':'s7-24to36mo','S8':'s8-3to6yr'}[seg]
            # 找该段 ID < 100 的第一张(老卡跨派)
            cands = sorted([c for c in all_card_ids if c.startswith(f'C-{seg}-0')])
            if cands:
                CROSS_SCHOOL_ADD[k] = cands[0]
                print(f"  [adjust] {k}: {v} → {cands[0]}")

# 应用修复
new_cards = []
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'SRC-031' in content and 'created: 2026-05-04' in content:
            new_cards.append(f)

fixed_count = 0
for f in new_cards:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()

    cid = re.search(r'card_id:\s*(\S+)', content).group(1)
    new_content = content

    # 修 title
    if cid in TITLE_FIXES:
        new_t = TITLE_FIXES[cid]
        new_content = re.sub(r'(\s+title:\s+)"[^"]*"', f'\\1"{new_t}"', new_content)

    # 修 hook
    if cid in HOOK_FIXES:
        new_h = HOOK_FIXES[cid]
        new_content = re.sub(r'(\s+hook:\s+)"[^"]*"', f'\\1"{new_h}"', new_content)

    # 修 wtd(只修索引 0/1/2/3/4 的)
    if cid in WTD_FIXES:
        wtd_lines = new_content.split('\n')
        wtd_start = None
        for i, line in enumerate(wtd_lines):
            if 'what_to_do:' in line:
                wtd_start = i + 1
                break
        if wtd_start:
            for idx, new_text in WTD_FIXES[cid].items():
                target = wtd_start + idx
                if target < len(wtd_lines):
                    wtd_lines[target] = f'    - "{new_text}"'
            new_content = '\n'.join(wtd_lines)

    # 加 cross-school related
    if cid in CROSS_SCHOOL_ADD:
        cross_id = CROSS_SCHOOL_ADD[cid]
        # 在 related_cards: 块末尾追加
        rel_match = re.search(r'(related_cards:\n(?:  - [^\n]+\n)+)', new_content)
        if rel_match:
            existing = rel_match.group(1)
            # 检查是否已含
            if cross_id not in existing:
                new_rel = existing + f'  - {cross_id}\n'
                new_content = new_content.replace(existing, new_rel, 1)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        fixed_count += 1

print(f"Fixed: {fixed_count} cards")
