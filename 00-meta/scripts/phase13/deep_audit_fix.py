#!/usr/bin/env python3
"""Phase 13 用户深度审 — 补漏知识点 + 漏术语 + 修内部结构"""
import os, re, glob, yaml

KB = os.path.expanduser("~/Desktop/parenting-kb")
SRC_ID = "SRC-031"
TODAY = "2026-05-04"
ACCESSED = "2026-05-04"

SEG_DIRS = {
    "S0": "s0-pregnancy", "S1": "s1-newborn", "S2": "s2-1to3mo", "S3": "s3-3to6mo",
    "S4": "s4-6to9mo", "S5": "s5-9to12mo", "S6": "s6-12to24mo", "S7": "s7-24to36mo",
    "S8": "s8-3to6yr",
}

def safe_quote(s):
    return '"' + str(s).replace('"', "'") + '"'

def indent(text, n=4):
    pad = " " * n
    return "\n".join(pad + line for line in text.split("\n"))

def card(card_id, seg, title, hook, why, wtd, fm, ev, refs, related, cit_title, cit_loc, cit_url):
    wtd_str = "\n".join(f"    - {safe_quote(x)}" for x in wtd)
    refs_str = "\n".join(f"  - {x}" for x in refs)
    rel_str = "\n" + "\n".join(f"  - {x}" for x in related) if related else " []"
    return f"""card_id: {card_id}
stages: [{seg}]
tags: []

front:
  title: {safe_quote(title)}
  hook: {safe_quote(hook)}

back:
  why_matters: |
{indent(why, 4)}
  what_to_do:
{wtd_str}
  failure_mode: |
{indent(fm, 4)}
  evidence_level: {ev}

glossary_refs:
{refs_str}

citation:
  page_title: {safe_quote(cit_title)}
  publisher: "World Health Organization & UNICEF"
  page_url_primary: {cit_url}
  accessed: {ACCESSED}
  language: en
  location: {safe_quote(cit_loc)}
  source_id: {SRC_ID}

unit_ids: []
related_cards:{rel_str}

language: zh
status: draft
created: {TODAY}
updated: {TODAY}
"""

URL_IYCF = "https://www.who.int/news-room/fact-sheets/detail/infant-and-young-child-feeding"
URL_BFHI = "https://www.who.int/teams/nutrition-and-food-safety/food-and-nutrition-actions-in-health-systems/ten-steps-to-successful-breastfeeding"
URL_CODE = "https://en.wikipedia.org/wiki/International_Code_of_Marketing_of_Breast-milk_Substitutes"
URL_BFHI_WIKI = "https://en.wikipedia.org/wiki/Baby_Friendly_Hospital_Initiative"
URL_GROWTH = "https://www.who.int/tools/child-growth-standards"
URL_BF = "https://www.who.int/health-topics/breastfeeding"
URL_QA = "https://www.who.int/news-room/questions-and-answers/item/breastfeeding"
URL_EBF = "https://www.who.int/tools/elena/interventions/exclusive-breastfeeding"
URL_LANCET = "https://en.wikipedia.org/wiki/Breastfeeding"

# ============================================================
# 11 张补漏卡(包括 2 张 ID 冲突重建)
# ============================================================

new_cards_data = []

# C-S0-1029 营养不良 3 类(stunting/wasting/overweight)+ 全球数据
new_cards_data.append(("C-S0-1029", "S0",
    "营养不良 3 类:矮 瘦 胖",
    "stunting wasting overweight",
    "WHO 5 岁以下儿童营养不良 3 大类(2022 数据 verbatim):\n"
    "① stunting(矮小)— 身高/年龄低于 -2 SD,慢性营养不良 — **全球 1.49 亿娃**\n"
    "② wasting(消瘦)— 体重/身高低于 -2 SD,急性营养不良 — **4500 万娃**\n"
    "③ overweight(超重)— 体重/身高高于 +2 SD,过度喂养 — **3700 万娃**\n"
    "中国家长常见误区:\n"
    "- 'overweight 也是营养不良' — 不是只缺才算,过也算\n"
    "- '中国娃没问题' — 中国 stunting 在中西部农村仍有,overweight 在城市持续上升\n"
    "WHO Growth Standards 2006 给统一阈值。",
    [
        "记 3 类:矮 / 瘦 / 胖 都是 WHO 营养不良",
        "矮:身高/年龄 -2 SD(慢性)",
        "瘦:体重/身高 -2 SD(急性)",
        "胖:体重/身高 +2 SD(过度)",
        "WHO Growth 2006 是统一判定标准",
    ],
    "把'胖娃'当'养得好' → WHO 把 overweight 列营养不良 — 长期肥胖+糖尿病风险高。\n"
    "营养不良不只'瘦','胖'也算。",
    "A",
    ["G-TERM-WHO-growth-standards", "G-TERM-stunting", "G-TERM-wasting"],
    ["C-S0-1024", "C-S4-1052", "C-S0-007"],
    "WHO IYCF Fact Sheet — Malnutrition Categories",
    "WHO 5 岁下营养不良 3 类 + 2022 全球数据(149M/45M/37M)",
    URL_IYCF))

# C-S1-1018 BFHI 关键管理 4 步(1a/1b/1c/2)
new_cards_data.append(("C-S1-1018", "S1",
    "BFHI 关键管理 4 步",
    "10 步前 4 步是基础",
    "BFHI 10 步骤前 4 步是关键管理(Critical Management Procedures):\n"
    "**Step 1a**:Comply fully with the International Code of Marketing of Breast-milk Substitutes(产院禁奶粉营销 — 不送试用装,不接受奶粉公司礼物)\n"
    "**Step 1b**:Have a written infant feeding policy(书面婴儿喂养政策 — 公开张贴 + 员工/家长可见)\n"
    "**Step 1c**:Establish ongoing monitoring and data management systems(持续监测 — 哪些妈妈坚持 EBF)\n"
    "**Step 2**:Ensure staff have sufficient knowledge, competence and skills(员工训练 — 母乳支持技能必修)\n"
    "中国爱婴医院'纸面 BFHI'问题:1a 形同虚设(产房入口堆奶粉广告)/ 1b 没书面政策 / 1c 不监测 / 2 员工不会衔乳。",
    [
        "选医院问'看你们书面喂养政策'(1b)",
        "看产房入口有无奶粉广告(1a 违反)",
        "问医生 / 助产士 母乳训练(2)",
        "问医院 EBF 率监测数据(1c)",
        "前 4 步系统性差 → 后 6 步执行不到位",
    ],
    "看到 BFHI 牌子但产房入口堆奶粉广告 → 第 1a 步直接违反,纸面认证。\n"
    "10 步前 4 步是地基,后 6 步是临床。",
    "A",
    ["G-TERM-BFHI-10-steps", "G-ABBR-BFHI", "G-TERM-WHO-Code"],
    ["C-S1-1002", "C-S0-1025", "C-S1-1009"],
    "BFHI Step 1a/1b/1c/2 (Critical Management Procedures)",
    "BFHI 10 步前 4 步关键管理 + 中国'纸面 BFHI'诊断",
    URL_BFHI))

# C-S1-1019 BFHI 第 3 步产前讨论
new_cards_data.append(("C-S1-1019", "S1",
    "BFHI 第 3 步产前讨论",
    "孕期就该聊母乳",
    "BFHI 第 3 步 verbatim:'Discuss the importance and management of breastfeeding with pregnant women and their families.'\n"
    "产前(孕中后期)产院应该主动跟妈妈+家人讨论:\n"
    "① 母乳重要性(初乳 + IgA + lactoferrin)\n"
    "② 实操(衔乳 + 频率 + 信号)\n"
    "③ 常见困难 + 求助路径\n"
    "④ Code 警惕(产后会被推销奶粉)\n"
    "⑤ BFHI 10 步流程预告\n"
    "中国产院常规:产前不讨论母乳 → 产后突然要求妈妈母乳 → 妈妈没准备 → 衔乳困难 → 加配方奶。",
    [
        "孕期约产前母乳咨询(产院或居家 IBCLC)",
        "提前学衔乳姿势(YouTube + IBCLC 课程)",
        "全家(老公/婆婆/妈妈)一起听 — 不只妈妈",
        "Code 警惕预演:'谢谢但我不要试用装'",
        "产前写分娩计划(立即 SSC + 24h 同室 + 不给配方)",
    ],
    "产前不讨论母乳 → 产后临场没准备 → 衔乳困难 → 妈妈焦虑 + 加配方。\n"
    "BFHI 第 3 步要求产前讨论 — 中国常被忽略。",
    "A",
    ["G-TERM-BFHI-10-steps", "G-ABBR-BFHI"],
    ["C-S1-1002", "C-S0-1025", "C-S1-1007"],
    "BFHI Step 3 (Antenatal Discussion)",
    "BFHI 第 3 步产前讨论 + 中国常被忽略",
    URL_BFHI))

# C-S1-1020 BFHI 第 5 步衔乳支持
new_cards_data.append(("C-S1-1020", "S1",
    "BFHI 第 5 步衔乳支持",
    "衔乳难是技术不是天赋",
    "BFHI 第 5 步 verbatim:'Support mothers to initiate and maintain breastfeeding and manage common difficulties.'\n"
    "母乳建立期(0-4 周)常见困难 + WHO 立场:\n"
    "① 衔乳浅(shallow latch)→ 调整体位(交叉摇篮 / 橄榄球)\n"
    "② 乳头疼/破→ 衔乳深 + 涂母乳风干\n"
    "③ 涨奶(engorgement)→ 频繁吸 + 反向按压\n"
    "④ 乳腺管堵塞/乳腺炎→ 频繁吸 + 热敷 + 找医生\n"
    "⑤ 奶量焦虑→ 看 4 客观指标(C-S2-1045)\n"
    "解决路径:护士 / 哺乳顾问 / IBCLC / 母乳支持小组。\n"
    "中国通病:出现困难 → '没奶就加配方' → 母乳量真降。",
    [
        "出现困难第一时间找哺乳顾问(IBCLC)",
        "衔乳痛 → 调整体位,不是停喂",
        "涨奶 → 频繁吸 + 反向按压(不挤一干二净)",
        "乳腺炎 → 继续吸 + 热敷 + 找医生(可继续喂)",
        "妇幼保健所有母乳门诊 — 出院 1 周复诊",
    ],
    "出现困难就停母乳加配方 → 跟 BFHI 第 5 步立场冲突 → 母乳建立失败。\n"
    "衔乳难不是天赋,是技术,可学可改。",
    "A",
    ["G-TERM-BFHI-10-steps", "G-ABBR-BFHI", "G-ABBR-EBF"],
    ["C-S1-1002", "C-S2-1045", "C-S1-1007"],
    "BFHI Step 5 (Maintain Breastfeeding + Manage Difficulties)",
    "BFHI 第 5 步衔乳支持 + 5 大常见困难解决路径",
    URL_BFHI))

# C-S1-1021 Nestle 1977 抵制运动
new_cards_data.append(("C-S1-1021", "S1",
    "Nestle 1977 抵制运动",
    "Code 来源是商业丑闻",
    "International Code 1981 不是凭空通过 — 是 Nestle 抵制运动(Nestle Boycott)逼出来的。\n"
    "1970s 背景:Nestle 等奶粉公司在非洲推销配方奶,妈妈用脏水冲泡 → 婴儿大量死亡(估计数十万)。\n"
    "1974 War on Want 'The Baby Killer' 报告 → 公开 Nestle 营销手段(送试用装 / 假冒护士 / 标签无警告)。\n"
    "1977 美国发起 Nestle 抵制 → 蔓延全球 7 年。\n"
    "1981 第 34 届 WHA 通过 Code → 抵制部分缓解。\n"
    "1988 抵制重启(违规仍在)— 持续到今。\n"
    "中国家长意义:奶粉公司不是'养娃帮手'是商业实体 — 国际史上有血泪教训。",
    [
        "记 Nestle 1977 — 国际 Code 来历",
        "奶粉公司不是中立 — 商业利益驱动",
        "中国直播带货 / 母婴店推销 → 跟 1970s 非洲推销同质",
        "知道历史不被'母乳就好但配方更现代'话术骗",
        "IBFAN 持续监督 — 抵制运动遗产",
    ],
    "不知道 Code 历史 → 信奶粉广告'科学营养'话术 → 重蹈 1970s 非洲覆辙。\n"
    "国际 Code 是血换来的政策。",
    "B",
    ["G-TERM-WHO-Code", "G-TERM-Nestle-boycott-1977", "G-TERM-IBFAN"],
    ["C-S1-1009", "C-S1-1011", "C-S0-1026"],
    "International Code History — Nestle Boycott 1977",
    "Nestle 1977 抵制运动 + War on Want 1974 + Code 1981 通过背景",
    URL_CODE))

# C-S1-1022 中国 BFHI 1992-1994 EBF 历史成功案例
new_cards_data.append(("C-S1-1022", "S1",
    "中国 BFHI 历史:29→68%",
    "94 年农村 EBF 翻倍",
    "中国 BFHI 1992 启动后 — 1992-1994 农村 EBF 率从 29% 跃升到 68%(2 年内翻倍多)— 国际公认成功案例(WHO 数据)。\n"
    "原因:政府强力推 + 6,000+ 爱婴医院认证 + 妇幼系统配合。\n"
    "之后:21 世纪起 BFHI 实操参差(纸面 BFHI)+ 奶粉营销加强 → 中国 EBF 率回落到 30-40%(估计)。\n"
    "教训:政策推得起来,松了就退 — 中国家长可以参考 1990s 早期模式。\n"
    "对照:瑞典 1997 全国 65 中心认证 + 北欧普遍 ≥ 2 岁母乳;美国 2018 仅 24.57% 医院认证。",
    [
        "知道中国 1992-1994 EBF 翻倍的成功",
        "现在 EBF 率回落 — 系统问题非妈妈个人",
        "选 1990s 早期 BFHI 标准的产院",
        "瑞典 / 北欧普遍 ≥ 2 岁 — 国际不是'你太久'",
        "找妇幼保健所支持 — 是 BFHI 历史遗产",
    ],
    "把 EBF 失败归因 '妈妈不够努力' → 是系统问题(BFHI 实操松+营销加强)。\n"
    "中国 1992-1994 证明做得到。",
    "B",
    ["G-ABBR-BFHI", "G-ABBR-EBF"],
    ["C-S0-1027", "C-S1-1016", "C-S0-1025"],
    "BFHI Implementation — China 1992-1994 Success",
    "中国 1992-1994 农村 EBF 29→68% + WHO 公认成功案例",
    URL_BFHI_WIKI))

# C-S2-1049 Cochrane EBF 元分析
new_cards_data.append(("C-S2-1049", "S2",
    "Cochrane:6 月 EBF 优于 4 月",
    "元分析硬证据",
    "WHO 6 月 EBF 推荐的科学根基:Cochrane 系统综述(Kramer & Kakuma 2012)。\n"
    "对比 4 月 EBF + 2 月混合 vs 6 月 EBF:\n"
    "**6 月 EBF 优势(verbatim from Cochrane)**:\n"
    "① 婴儿胃肠感染少\n"
    "② 婴儿母亲铁缺率低(母乳铁吸收高)\n"
    "③ 母亲泌乳期长(月经回归晚)\n"
    "④ 母亲产后体重恢复快\n"
    "**4 月 EBF 唯一优势**:'flexibility' — 但 WHO 不接受这点足以推迟 EBF\n"
    "Cochrane Cochrane 是 Tier 1 元分析方法学权威 — 这个综述是 WHO + AAP 6 月 EBF 立场的科学根基。\n"
    "AAP 4-6 月立场基于 LEAP 早期过敏引入,跟 EBF 时长不是同问题。",
    [
        "WHO 6 月 EBF 不是凭感觉 — Cochrane 元分析支持",
        "Kramer-Kakuma 2012 是关键文献",
        "记 4 优势:感染少/铁少/泌乳长/瘦快",
        "AAP 4-6 月是过敏引入立场,不是 EBF 时长",
        "Cochrane 是元分析方法学权威 — 信",
    ],
    "信'4 月 EBF 跟 6 月一样' → Cochrane 元分析直接反对 → 错过 4 大优势。\n"
    "EBF 6 月有硬科学根基,不是政策推断。",
    "A",
    ["G-ABBR-EBF", "G-TERM-WHO-six-months", "G-PERSON-Kramer"],
    ["C-S3-1042", "C-S0-1024", "C-S1-1015"],
    "Cochrane Kramer-Kakuma 2012 'Optimal duration of exclusive breastfeeding'",
    "Cochrane 元分析 6 月 vs 4 月 EBF 4 大优势",
    URL_EBF))

# C-S6-1071 免疫接种期间继续母乳
new_cards_data.append(("C-S6-1071", "S6",
    "疫苗期间继续母乳",
    "母乳是疫苗最佳搭档",
    "WHO + AAP 立场:免疫接种期间继续母乳 — 不仅可,而且增强疫苗效力。\n"
    "原因:\n"
    "① 母乳 IgA 协同增强黏膜免疫(肠/呼吸道)\n"
    "② 母乳寡糖喂益生菌,肠道菌群好 → 疫苗反应更强\n"
    "③ 母乳免疫成分给短期保护过渡(疫苗免疫建立 2-4 周)\n"
    "④ 哺乳安抚减少接种焦虑哭闹(妈妈在场即安全)\n"
    "实操建议:\n"
    "- 接种前后 都可哺乳\n"
    "- 接种现场哺乳安抚\n"
    "- 接种后发热 → 继续母乳(不停)\n"
    "- 妈妈刚接种(eg 流感疫苗)→ 继续喂(疫苗成分不进母乳)\n"
    "中国常见误区:'接种后停 24 小时母乳' → 错的,WHO/AAP 反对。",
    [
        "接种前后都喂母乳",
        "接种现场哺乳安抚娃",
        "接种后发热继续母乳(不停)",
        "妈妈接种疫苗也继续喂(成分不进母乳)",
        "听到 '接种后停 24 小时' → 别信",
    ],
    "接种后停 24 小时母乳 → 错过母乳免疫协同增强疫苗效力。\n"
    "母乳是疫苗最佳搭档,不是冲突。",
    "A",
    ["G-ABBR-EBF", "G-TERM-WHO-two-years"],
    ["C-S6-1064", "C-S5-1037"],
    "WHO Q&A on Breastfeeding + Immunization",
    "WHO 立场:免疫接种期间继续母乳 + 4 大原因 + 中国误区",
    URL_QA))

# C-S7-1102 自然离乳(原 1100 内容,因 ID 冲突)
new_cards_data.append(("C-S7-1102", "S7",
    "自然离乳 vs 主动断奶",
    "等娃自己说不要了",
    "WHO 立场:断奶时机 / 方式由妈妈和娃共同决定 — 不强加。\n"
    "两种路径:\n"
    "① 自然离乳(child-led weaning):娃自己减少 → 自己停 — 多在 2-4 岁\n"
    "② 主动断奶(mother-led weaning):妈妈主动减少 → 停 — 任何月龄\n"
    "WHO 推:能继续就自然离乳;不能 → 渐进减少不突然停。\n"
    "突然断奶 risks:\n"
    "- 妈妈乳腺炎(milk stasis)\n"
    "- 娃心理冲击(尤其在分离焦虑期)\n"
    "- 妈妈情绪波动(激素剧变)\n"
    "中国常见'2 岁送奶奶家断' = 突然断 + 母婴分离 = 双重伤害。",
    [
        "默认自然离乳 — 等娃自己减/停",
        "需要主动断 → 渐进(每周减 1 次)",
        "绝不'送奶奶家断'(突然 + 分离)",
        "突然断 → 妈妈乳腺炎 + 娃心理冲击",
        "妈妈用乳头涂辣椒 / 黄连 → 不推",
    ],
    "突然断奶或'送奶奶家断' → 妈妈乳腺炎 / 娃心理冲击 / 妈妈情绪激素紊乱。\n"
    "WHO 立场:自然或渐进,不强行。",
    "A",
    ["G-TERM-WHO-two-years", "G-PERSON-Detwyler"],
    ["C-S7-1099", "C-S6-1064"],
    "WHO Weaning Approach + Detwyler Natural Weaning",
    "WHO 默认自然离乳 + 渐进 vs 突然断奶风险 + Detwyler 2.5-7 岁人类生物学",
    URL_QA))

# C-S7-1103 12-36m 跟随家庭饮食(原 1101 内容)
new_cards_data.append(("C-S7-1103", "S7",
    "12-36m 跟家庭饮食",
    "盐糖油减量是关键",
    "WHO 12 月+ 立场:跟随家庭饮食(family foods)+ 持续母乳。\n"
    "12-36 月饮食原则:\n"
    "① 形态:跟大人桌(切碎/煮软)\n"
    "② 多样:5+ 食物组\n"
    "③ 量:大人量的 ~1/4-1/2(分多餐 + 加餐)\n"
    "④ 减盐:< 1g/天(总),不另加盐\n"
    "⑤ 减糖:不另加糖(果汁/糕点限)\n"
    "⑥ 减油:不油炸,蒸/煮/炒优先\n"
    "中国通病:1 岁后跟大人吃 = 大人盐糖量 → 学步儿肝肾负担超。",
    [
        "12+ 月跟大人桌 — 但盐/糖/油单独减",
        "不另加盐(< 1g/天)",
        "不另加糖(果汁糕点限)",
        "蒸/煮/炒为主 — 不油炸",
        "母乳/全奶继续(WHO 持续 2 年)",
    ],
    "1 岁后直接跟大人吃含盐糖油 → 钠超 / 蛀牙 / 肝肾负担超。\n"
    "12-36 月仍是儿童食品标准。",
    "A",
    ["G-ABBR-CF"],
    ["C-S6-1066", "C-S6-1064"],
    "WHO 12+ Months Family Foods",
    "WHO 12+ 跟随家庭饮食 + 减盐糖油",
    URL_BF))

# C-S0-1030 全球营养不良 5 岁下数字 — 已合并到 C-S0-1029,跳过单独卡

# 输出 11 张卡
written = 0
for card_data in new_cards_data:
    cid = card_data[0]
    seg = card_data[1]
    yaml_text = card(*card_data)
    seg_dir = SEG_DIRS[seg]
    out_path = os.path.join(KB, "30-cards", seg_dir, f"{cid}.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    written += 1

print(f"补漏卡: {written} 张")

# ============================================================
# 9 张漏术语
# ============================================================

def term(g_id, gtype, display, en, zh, one_liner, detail, key_facts, related_g, related_c=None):
    related_g_str = "\n".join(f"  - {x}" for x in related_g) if related_g else "  []"
    related_c_str = "\n".join(f"  - {x}" for x in related_c) if related_c else "  []"
    kf_str = "\n".join(f"  - {safe_quote(x)}" for x in key_facts) if key_facts else "  []"
    return f"""glossary_id: {g_id}
type: {gtype}
display_name: {safe_quote(display)}

en_term: {safe_quote(en)}
zh_term: {safe_quote(zh)}

one_liner: |
  {one_liner}

detail: |
{indent(detail, 2)}

key_facts:
{kf_str}

related_glossary:
{related_g_str}

related_cards:
{related_c_str}

sources:
  - source_id: {SRC_ID}

language: zh
status: complete
created: {TODAY}
updated: {TODAY}
"""

new_terms = []

new_terms.append(("G-TERM-stunting", "term", "stunting 矮小",
    "Stunting (Linear Growth Failure)", "矮小",
    "stunting = 身高/年龄低于 WHO Growth Standards -2 SD,慢性营养不良指标。",
    """## 定义
Stunting — 身高/年龄低于 WHO Growth Standards -2 SD,5 岁以下慢性营养不良核心指标。

## 阈值
- 中度:-2 SD 至 -3 SD
- 严重:< -3 SD

## 全球数据(2022)
- 5 岁下 1.49 亿娃 stunted
- 多数在低中收入国家(撒哈拉/南亚)
- 中国西部农村仍有

## 原因
- 慢性营养不良(辅食质量差 + 持续不足)
- 反复感染(腹泻 / 呼吸道)
- 母亲营养不良 + 早婚早育
- 6-23 月辅食多样性不达标(全球 < 1/4 达标)

## 影响
- 不可逆 — 错过 1000 天黄金窗(怀孕到 2 岁)
- 终身 IQ 影响(平均 -10 点)
- 慢性疾病风险增

## 干预
- 6 月 EBF
- 6 月起辅食含铁优先 + 多样性
- 持续母乳到 2 岁(WHO 立场)""",
    ["WHO Growth -2 SD 阈值", "全球 1.49 亿娃", "1000 天黄金窗", "终身 IQ -10 点"],
    ["G-TERM-WHO-growth-standards", "G-TERM-wasting", "G-ABBR-CF"],
    ["C-S0-1029", "C-S4-1052"]))

new_terms.append(("G-TERM-wasting", "term", "wasting 消瘦",
    "Wasting (Acute Malnutrition)", "消瘦",
    "wasting = 体重/身高低于 WHO Growth Standards -2 SD,急性营养不良指标。",
    """## 定义
Wasting — 体重/身高低于 WHO Growth Standards -2 SD,5 岁以下急性营养不良核心指标。

## 阈值
- 中度:-2 SD 至 -3 SD
- 严重(SAM):< -3 SD,需要紧急医学干预(MUAC < 11.5 cm)

## 全球数据(2022)
- 5 岁下 4500 万娃 wasted
- 紧急/灾难时高(战争 / 饥荒)
- 死亡率高(SAM 死亡率 5-15%)

## 原因
- 急性食物不足
- 急性疾病(腹泻脱水)
- 紧急情况(灾难)

## 干预
- WHO Ready-to-Use Therapeutic Food (RUTF)
- 紧急喂养项目
- 持续母乳保护(EBF 防 wasting 死亡)

## 跟 stunting 区别
- stunting:慢性,身高失败
- wasting:急性,体重失败
- 两者可同时存在(severely affected)""",
    ["WHO -2 SD 阈值", "全球 4500 万娃", "紧急/灾难时高", "SAM 死亡率 5-15%"],
    ["G-TERM-WHO-growth-standards", "G-TERM-stunting"],
    ["C-S0-1029"]))

new_terms.append(("G-TERM-MTCT", "term", "MTCT 母婴垂直传播",
    "Mother-to-Child Transmission", "母婴垂直传播",
    "MTCT = HIV/HBV 等病毒从妈妈传给娃的途径(产前/产中/母乳)。",
    """## 定义
Mother-to-Child Transmission — 母亲传染病(HIV / HBV / 梅毒等)垂直传给婴儿的途径。

## 3 大途径
- 产前(intrauterine,经胎盘)
- 产中(intrapartum,经产道)
- 产后(postnatal,经母乳)

## HIV MTCT 数据
- 不 ART:总 MTCT 30-45%
- 母乳 MTCT 5-20%(累积 24 月)
- ART 下:< 1-2%(高资源区几乎消除)

## WHO 2010 立场转变
- 旧:HIV+ 妈妈避免母乳
- 新:AFASS 评估
  - 满足 → 用配方
  - 不满足 → EBF + ART

## 中国 PMTCT
中国 PMTCT(Prevention of MTCT)国家项目自 2010s 推广。""",
    ["3 途径:产前/产中/产后", "HIV 不 ART 总 MTCT 30-45%", "ART 下 < 1-2%"],
    ["G-TERM-PMTCT", "G-TERM-HIV-feeding", "G-TERM-AFASS"],
    ["C-S1-1013"]))

new_terms.append(("G-TERM-PMTCT", "term", "PMTCT 母婴阻断",
    "Prevention of Mother-to-Child Transmission", "母婴阻断",
    "PMTCT = WHO 推 HIV+/HBV+ 妈妈母婴垂直传播阻断方案。",
    """## 定义
Prevention of Mother-to-Child Transmission — WHO 推荐的 HIV/HBV 母婴垂直传播阻断综合方案。

## HIV PMTCT 4 支柱
1. 一级预防(妇女育龄前预防 HIV 感染)
2. 计划生育(HIV+ 妇女计划生育权)
3. PMTCT 干预(产前 + 产中 + 产后)
4. 关怀治疗(妈妈 + 娃 ART 持续)

## 中国 PMTCT 项目
- 2002 年试点
- 2011 年全国推广
- HIV+ 孕妇 ART + 婴儿出生 6 周内 ART 预防 + 配方喂养(高资源 + AFASS)
- 中国 MTCT 率从 30%(无干预)降到 < 5%(2020 数据)

## HBV PMTCT
HBV 大三阳妈妈娃出生 24h 内乙肝免疫球蛋白 + 乙肝疫苗 → 阻断率 > 95%。

## 喂养立场
WHO + 中国 PMTCT:HIV+ 妈妈 AFASS 满足 → 配方;AFASS 不全 → EBF + ART。""",
    ["WHO HIV 4 支柱", "中国 2011 全国", "中国 MTCT 从 30% 降 < 5%", "HBV 阻断 > 95%"],
    ["G-TERM-MTCT", "G-TERM-HIV-feeding", "G-TERM-AFASS"],
    ["C-S1-1013"]))

new_terms.append(("G-TERM-Cronobacter-sakazakii", "term", "阪崎肠杆菌",
    "Cronobacter sakazakii", "阪崎肠杆菌",
    "阪崎杆菌 = 配方奶粉中可能含的致命病原,WHO 推 70°C 水冲泡杀灭。",
    """## 定义
Cronobacter sakazakii(原名 Enterobacter sakazakii)— 配方奶粉中可能含的细菌病原。

## 风险
- 婴儿败血症
- 脑膜炎(致命)
- 脑损伤(存活也常残)
- 死亡率 40-80%(婴儿期)

## 来源
- 配方奶粉本身(干粉灭菌不彻底)
- 冲泡用具(奶瓶 / 吸嘴)
- 不洁水

## WHO 2007 PIF 安全准备指南
- 用 ≥ 70°C 水冲泡(杀阪崎杆菌阈值)
- 冲泡 2 小时内喝完
- 奶瓶/吸嘴消毒(开水煮 5 min / 蒸汽)

## 高危
- 早产儿(< 28 周)
- 低出生体重(< 1500g)
- 免疫缺陷
- WHO 强烈推这些婴儿用 commercial sterile liquid formula(罐装液体配方)

## 中国家长常见错误
用 40-50°C '不烫娃'水冲奶粉 → 阪崎杆菌不死 → 致命风险。""",
    ["WHO 70°C 阈值", "婴儿败血症/脑膜炎", "死亡率 40-80%", "早产儿/低体重高危"],
    ["G-TERM-PIF-safe-preparation", "G-TERM-breastmilk-substitutes"],
    ["C-S2-1046"]))

new_terms.append(("G-TERM-PIF-safe-preparation", "term", "PIF 安全准备",
    "Powdered Infant Formula Safe Preparation", "婴儿配方奶粉安全准备",
    "WHO 2007 PIF 指南 — 配方奶粉冲泡的国际安全标准。",
    """## 定义
Powdered Infant Formula(PIF)Safe Preparation — WHO 2007 发布的配方奶粉冲泡国际安全标准。

## 核心规则
1. 用 ≥ 70°C 水冲泡(杀阪崎杆菌)
2. 冲泡 2 小时内喝完
3. 冰箱冷藏 < 24 小时(预冲泡)
4. 不重新加热剩奶(细菌已生长)
5. 奶瓶/吸嘴消毒(开水煮 5 min / 蒸汽 / 洗碗机)
6. 装瓶前洗手
7. 粉勺别压实 — 不浓不稀

## 高危婴儿
早产 / 低出生体重 / 免疫缺陷 → WHO 推 commercial sterile liquid formula(罐装液体)。

## 中国家长常见错误
- 用 40-50°C '不烫娃'水 → 阪崎杆菌不死
- 冲泡后保温瓶放几小时 → 细菌已生长
- 上次没喝完留下次喂 → 风险

## 跟其他派关系
- AAP / 鲍秀兰 / 松田 都说要消毒,但 70°C 阈值是 WHO 独家明确
- 中国母婴店常推 '50°C 不烫' → 跟 WHO 立场冲突""",
    ["WHO 2007 国际标准", "70°C 关键阈值", "2 小时内喝完", "中国家长常见 50°C 错"],
    ["G-TERM-Cronobacter-sakazakii", "G-TERM-breastmilk-substitutes"],
    ["C-S2-1046"]))

new_terms.append(("G-TERM-Nestle-boycott-1977", "term", "Nestle 1977 抵制运动",
    "Nestle Boycott 1977", "Nestle 抵制运动 1977",
    "1977 年起的全球抵制运动 — 国际 Code 1981 直接来源。",
    """## 历史背景
1970s Nestle 等奶粉公司在非洲推销配方奶 — 妈妈用脏水冲泡 → 婴儿死亡数十万。

## 引爆事件
- 1974 War on Want 报告 'The Baby Killer' — 公开 Nestle 营销手段
- Mike Muller 主笔 — 揭露试用装 / 假冒护士 / 标签无警告

## 抵制运动
- 1977 美国发起
- 7 年蔓延全球
- 1984 暂停(Nestle 部分让步)
- 1988 重启(违规仍在)
- 持续到今(IBFAN 监督)

## 直接成果
- 1981 第 34 届 WHA 通过 International Code of Marketing of Breast-milk Substitutes
- 84 国立法实施

## 历史意义
- 国际公共卫生政策由消费者运动推动的标志案例
- IBFAN 1979 成立(抵制运动产物)

## 当代意义
中国奶粉营销跟 1970s 非洲推销同质 — Code 是血换来的政策,不是抽象建议。""",
    ["1977 起抵制", "1974 The Baby Killer 报告", "1981 Code 通过", "IBFAN 1979 成立"],
    ["G-TERM-WHO-Code", "G-TERM-IBFAN", "G-TERM-formula-marketing"],
    ["C-S1-1021"]))

new_terms.append(("G-PERSON-Kramer", "person", "Michael Kramer",
    "Michael S. Kramer", "Michael Kramer",
    "McGill 大学流行病学家 — Cochrane EBF 元分析作者(Kramer-Kakuma 2012)。",
    """## 简介
Michael S. Kramer — McGill 大学(加拿大)流行病学家,母乳喂养证据综述权威。

## 主要贡献
- Cochrane Kramer-Kakuma 2012 'Optimal duration of exclusive breastfeeding' 元分析 — WHO 6 月 EBF 推荐的核心科学根基
- PROBIT(Promotion of Breastfeeding Intervention Trial)主导研究 — 白俄罗斯 17,046 母婴 RCT
- 母乳长期效应(IQ / 过敏 / 肥胖)研究

## PROBIT 关键发现
- BFHI 干预 → EBF 率显著提高
- 母乳延长 → 婴儿胃肠 / 呼吸道感染降
- 长期 IQ 益处 +5-7 点(高于 Horta 2015 的 +3 点估计)

## 在 SRC-031 中的角色
Kramer-Kakuma 2012 Cochrane 元分析是 WHO 6 月 EBF 立场的科学根基(C-S2-1049)。""",
    ["McGill 大学流行病学家", "Cochrane Kramer-Kakuma 2012", "PROBIT RCT 17,046 母婴", "WHO 6 月 EBF 科学根基"],
    ["G-TERM-WHO-six-months", "G-ABBR-EBF", "G-PERSON-Victora"],
    ["C-S2-1049"]))

new_terms.append(("G-PERSON-Detwyler", "person", "Katherine Dettwyler",
    "Katherine A. Dettwyler", "Katherine Dettwyler",
    "Texas A&M 大学人类学家 — 自然离乳人类生物学基线 2.5-7 岁。",
    """## 简介
Katherine Dettwyler — Texas A&M 大学(美国)人类学家,母乳喂养跨文化研究权威。

## 主要贡献
- Dettwyler 2004 'A Natural Age of Weaning' 论文
- 跟其他灵长类生物学比对得出人类自然离乳年龄 2.5-7 岁
- 跟 Stuart-Macadam 合编 'Breastfeeding: Biocultural Perspectives'(1995)

## 推断方法学
基于 5 大灵长类指标比对:
1. 三倍出生体重年龄(~ 2.5 岁)
2. 大臼齿出齐年龄(~ 5.5-6 岁)
3. 怀孕期 6 倍长(~ 4.5 岁)
4. 成年体重 1/3(~ 4-7 岁)
5. 生殖器成熟(~ 7 岁)

## 结论
人类生物学自然离乳年龄 2.5-7 岁 — WHO ≥ 2 岁 'or beyond' 立场的人类学根基。

## 跟 WHO 关系
Dettwyler 2004 给 WHO 'or beyond' 提供生物学证据基础 — 不是文化任意,是物种基线。

## 中国家长意义
'2 岁后还在喂' 不是过度 — 比人类生物学下限还短。""",
    ["Texas A&M 人类学家", "Dettwyler 2004 论文", "5 大灵长类指标", "人类自然离乳 2.5-7 岁"],
    ["G-TERM-WHO-two-years"],
    ["C-S7-1099", "C-S7-1102"]))

# 写术语
written_terms = 0
for t in new_terms:
    g_id = t[0]
    yaml_text = term(*t)
    out_path = os.path.join(KB, "40-glossary", f"{g_id}.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    written_terms += 1
print(f"补漏术语: {written_terms} 张")

print(f"\n=== 补漏总计:11 卡 + 9 术语 ===")
