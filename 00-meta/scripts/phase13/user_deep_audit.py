#!/usr/bin/env python3
"""Phase 13 SRC-031 用户深度审 — 内部结构 + 漏知识点 + 漏术语"""
import os, yaml, glob, re, collections

KB = os.path.expanduser("~/Desktop/parenting-kb")

new_cards = []
for sd in ['s0-pregnancy', 's1-newborn', 's2-1to3mo', 's3-3to6mo', 's4-6to9mo',
           's5-9to12mo', 's6-12to24mo', 's7-24to36mo', 's8-3to6yr']:
    for f in glob.glob(f'{KB}/30-cards/{sd}/*.yaml'):
        with open(f) as fh:
            content = fh.read()
        if 'SRC-031' in content and 'created: 2026-05-04' in content:
            new_cards.append(f)

cards_data = {}
for f in new_cards:
    with open(f) as fh:
        d = yaml.safe_load(fh)
    cards_data[d['card_id']] = (f, d)

print(f"=== 深度审 SRC-031 {len(cards_data)} 卡 ===\n")

# ============================================================
# 维度 1:内部结构问题
# ============================================================
print("=== 维度 1:内部结构 ===\n")

issues = collections.defaultdict(list)

for cid, (f, d) in sorted(cards_data.items()):
    front = d['front']
    back = d['back']
    title = front.get('title', '')
    hook = front.get('hook', '')
    why = back.get('why_matters', '')
    wtd = back.get('what_to_do', [])
    fm = back.get('failure_mode', '')

    # H1: hook 是否真"抓眼"(语气)
    # 描述型:含"是什么/介绍/概念"
    # 平淡型:陈述事实但没引发好奇/警觉
    # 真抓眼:口号式 / 警示性 / 反直觉
    if hook.endswith(("的", "啊", "呀", "了", "嘛")):
        if any(x in hook for x in ["都", "不", "是", "需"]):
            pass  # 仍可
        else:
            issues['hook_too_passive'].append(f"{cid}: '{hook}'")

    # H2: why_matters 是否有前情提要(头 1-2 句给定义/背景)
    # 检查 why_matters 是否以专业词起头但没解释
    why_lines = [l.strip() for l in why.split("\n") if l.strip()]
    if why_lines:
        first_line = why_lines[0]
        # 含英文术语/缩写但没解释
        if re.search(r'\b[A-Z]{2,}\b', first_line) and len(first_line) < 40:
            # eg "WHO + UNICEF 是唯一全球医学共识" — 假设知道 WHO
            if '=' not in first_line and '是' not in first_line and ':' not in first_line:
                issues['why_no_intro'].append(f"{cid}: '{first_line[:50]}'")

    # H3: what_to_do 数量 3-5
    if len(wtd) < 3:
        issues['wtd_too_few'].append(f"{cid}: only {len(wtd)} items")
    elif len(wtd) > 5:
        issues['wtd_too_many'].append(f"{cid}: {len(wtd)} items")

    # H4: failure_mode 完整(2 句 — 后果 + 警示)
    fm_lines = [l for l in fm.split("\n") if l.strip()]
    if len(fm_lines) < 2:
        issues['fm_only_1_line'].append(f"{cid}: '{fm[:60]}'")

    # H5: glossary_refs 数量(应 ≥ 2 — 一般 WHO 卡多概念)
    refs = d.get('glossary_refs', []) or []
    if len(refs) < 2:
        issues['glossary_refs_thin'].append(f"{cid}: {len(refs)} refs")

    # H6: related_cards ≥ 2(且 ≥ 1 跨派)
    related = d.get('related_cards', []) or []
    if len(related) < 2:
        issues['related_thin'].append(f"{cid}: {len(related)} related")

# 输出
total_int_issues = sum(len(v) for v in issues.values())
print(f"内部结构问题: {total_int_issues}\n")
for cat, lst in issues.items():
    if lst:
        print(f"--- {cat}: {len(lst)} ---")
        for x in lst[:5]:
            print(f"  {x}")
        if len(lst) > 5:
            print(f"  ... +{len(lst)-5} more")
        print()

# ============================================================
# 维度 2:漏知识点(对照 12 文档关键命题)
# ============================================================
print("\n=== 维度 2:漏知识点(对照 12 WHO 文档)===\n")

# 关键命题清单 — 跟卡片内容比对
KEY_PROPOSITIONS = {
    # D1 IYCF Fact Sheet
    "营养不良 3 类(stunting/wasting/overweight)": ["stunting", "wasting", "overweight", "矮小", "消瘦", "超重"],
    "全球 5 岁下 149M stunted/45M wasted/37M overweight": ["149", "45M", "37M", "1.49 亿", "4500 万", "3700 万"],
    "辅食多样性达标率 < 1/4(6-23m)": ["1/4", "四分之一", "less than a fourth"],

    # D2 BFHI
    "BFHI 第 1a 步遵守 Code": ["第 1a", "1a", "Code 遵守", "Step 1a"],
    "BFHI 第 1b/1c 步书面政策+监测": ["1b", "1c", "书面政策", "监测系统"],
    "BFHI 第 2 步员工训练": ["第 2 步", "Step 2", "员工训练", "knowledge"],
    "BFHI 第 3 步产前讨论": ["第 3 步", "Step 3", "产前讨论"],
    "BFHI 第 5 步衔乳困难处理": ["第 5 步", "Step 5", "衔乳困难", "maintain"],
    "BFHI 2016 系统综述支持(58 项研究)": ["58 项", "58 studies", "2016 综述"],

    # D3 Code
    "Nestle 1977 抵制运动": ["Nestle", "雀巢", "1977", "boycott", "抵制"],
    "Code 后续 WHA 决议": ["WHA 决议", "1986", "1990", "1994", "2005", "2010", "2016"],
    "WHO 2016 决议加强增长奶监管": ["2016 决议", "growing-up", "增长奶 加强"],

    # D4 BFHI Status
    "中国 1992-1994 农村 EBF 29% → 68%": ["29%", "68%", "1992", "1994", "rural"],
    "瑞典 1997 全国 65 中心认证": ["瑞典", "65", "1997"],
    "美国 2018 512 医院 24.57%": ["美国 2018", "512", "24.57"],

    # D5 Growth Standards
    "营养不良 SD 阈值(-2 SD stunting / -3 SD severe)": ["-2 SD", "-3 SD", "标准差", "stunting threshold"],

    # D6 CF
    "1 岁前禁:蜂蜜 / 全牛奶 / 盐糖 / 添加糖": ["蜂蜜", "1 岁前", "全牛奶", "盐", "糖", "1 岁前禁"],
    "卫生:洗手 + 餐具消毒 + 安全食物存储": ["洗手", "餐具消毒", "食物存储"],

    # D7 ELENA EBF
    "Cochrane Kramer-Kakuma 2012 EBF 元分析": ["Cochrane", "Kramer", "Kakuma"],

    # D8 BF Topic
    "母乳储存规则(常温 4h / 冰箱 4d / 冷冻 6m)": ["常温 4", "冰箱 4", "冷冻 6", "4 小时", "4 天", "6 月"],

    # D9 HIV
    "中国 PMTCT 指南": ["PMTCT", "中国 HIV"],
    "MTCT 数字(不 ART 19% bottle vs 49% breast)": ["19%", "49%", "MTCT"],

    # D10 Lancet 2016
    "全球 EBF 节省 3000 亿美元医疗": ["3000 亿", "$300 billion", "医疗成本"],

    # D11 LAM
    "LAM 失败率 < 2%": ["失败率", "< 2%", "2 percent"],

    # D12 Q&A
    "储奶规则(室温 4h / 冰箱 4d / 冻 6m)": ["储奶规则", "保存", "室温 4 小时"],
    "免疫接种期间继续母乳": ["免疫接种", "vaccination"],
}

# 拼合所有卡片内容
all_content = ""
for cid, (f, d) in cards_data.items():
    all_content += " " + d['front'].get('title', '')
    all_content += " " + d['front'].get('hook', '')
    all_content += " " + d['back'].get('why_matters', '')
    for w in d['back'].get('what_to_do', []):
        all_content += " " + w
    all_content += " " + d['back'].get('failure_mode', '')

missing_props = []
for prop, kws in KEY_PROPOSITIONS.items():
    found = any(kw in all_content for kw in kws)
    if not found:
        missing_props.append(prop)

print(f"漏知识点: {len(missing_props)}")
for p in missing_props:
    print(f"  ✗ {p}")

# ============================================================
# 维度 3:漏术语
# ============================================================
print("\n=== 维度 3:漏术语 ===\n")

# 基于 WHO 内容应该建但没建的术语
EXPECTED_NEW_TERMS = {
    "G-TERM-stunting": "stunting 矮小(WHO 营养不良核心概念,5 岁下 1.49 亿)",
    "G-TERM-wasting": "wasting 消瘦(WHO 营养不良核心,5 岁下 4500 万)",
    "G-TERM-MTCT": "Mother-to-Child Transmission 母婴垂直传播(HIV 卡用到)",
    "G-TERM-PMTCT": "Prevention of MTCT 母婴阻断(中国 PMTCT 项目)",
    "G-TERM-Cronobacter-sakazakii": "阪崎肠杆菌(70°C 水冲奶粉对应病原)",
    "G-TERM-PIF-safe-preparation": "Powdered Infant Formula 安全准备(WHO 2007)",
    "G-TERM-Nestle-boycott-1977": "Nestle 抵制运动 1977(Code 历史标志)",
    "G-PERSON-Kramer": "Michael Kramer(Cochrane EBF 元分析作者)",
    "G-PERSON-Detwyler": "Katherine Dettwyler(自然离乳 2.5-7 岁人类生物学)",
}

all_glossary = set()
for f in glob.glob(f'{KB}/40-glossary/*.yaml'):
    g_id = os.path.basename(f).replace('.yaml', '')
    all_glossary.add(g_id)

missing_terms = []
for term, desc in EXPECTED_NEW_TERMS.items():
    if term not in all_glossary:
        missing_terms.append((term, desc))

print(f"漏术语: {len(missing_terms)}")
for t, d in missing_terms:
    print(f"  ✗ {t} — {d}")

print("\n=== 总结 ===")
print(f"内部结构问题:{total_int_issues}")
print(f"漏知识点:{len(missing_props)}")
print(f"漏术语:{len(missing_terms)}")
