#!/usr/bin/env python3
"""Phase 13 SRC-031 WHO+UNICEF 喂养指南合集 — 批量产卡脚本"""
import os

KB = os.path.expanduser("~/Desktop/parenting-kb")
SRC_ID = "SRC-031"
ACCESSED = "2026-05-04"
TODAY = "2026-05-04"

# 段路径映射
SEG_DIRS = {
    "S0": "s0-pregnancy",
    "S1": "s1-newborn",
    "S2": "s2-1to3mo",
    "S3": "s3-3to6mo",
    "S4": "s4-6to9mo",
    "S5": "s5-9to12mo",
    "S6": "s6-12to24mo",
    "S7": "s7-24to36mo",
    "S8": "s8-3to6yr",
}

def indent(text, n=4):
    """缩进多行字符串"""
    pad = " " * n
    return "\n".join(pad + line for line in text.split("\n"))

def safe_quote(s):
    """把内容包成 YAML 双引号字符串,处理内部双引号"""
    s2 = str(s).replace('"', "'")  # 内部 " 替成 ',防 YAML 冲突
    return f'"{s2}"'

def card(card_id, seg, title, hook, why, wtd, fm, ev, refs, related, cit_title, cit_loc, cit_url):
    """生成单张卡片 YAML"""
    wtd_str = "\n".join(f"    - {safe_quote(x)}" for x in wtd)
    refs_str = "\n".join(f"  - {x}" for x in refs) if refs else "  []"
    if related:
        rel_str = "\n" + "\n".join(f"  - {x}" for x in related)
    else:
        rel_str = " []"
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

# === 数据 ===
URL_IYCF = "https://www.who.int/news-room/fact-sheets/detail/infant-and-young-child-feeding"
URL_BFHI = "https://www.who.int/teams/nutrition-and-food-safety/food-and-nutrition-actions-in-health-systems/ten-steps-to-successful-breastfeeding"
URL_CODE = "https://en.wikipedia.org/wiki/International_Code_of_Marketing_of_Breast-milk_Substitutes"
URL_BFHI_WIKI = "https://en.wikipedia.org/wiki/Baby_Friendly_Hospital_Initiative"
URL_CF = "https://www.who.int/health-topics/complementary-feeding"
URL_EBF = "https://www.who.int/tools/elena/interventions/exclusive-breastfeeding"
URL_BF = "https://www.who.int/health-topics/breastfeeding"
URL_HIV = "https://en.wikipedia.org/wiki/Breastfeeding_and_HIV"
URL_LANCET = "https://en.wikipedia.org/wiki/Breastfeeding"
URL_LAM = "https://en.wikipedia.org/wiki/Lactational_amenorrhea"
URL_QA = "https://www.who.int/news-room/questions-and-answers/item/breastfeeding"
URL_GROWTH = "https://www.who.int/tools/child-growth-standards"

cards = []

# ============================================================
# S0 孕期(起 1024) — 5 张
# ============================================================

cards.append(("C-S0-1024", "S0",
    "喂养指南 4 国 1 国际:WHO 收口",
    "国际共识比谁都硬",
    "现库已有 AAP(美) / 鲍秀兰(中) / 松田(日) 三国指南,各国家长立场不同。\n"
    "WHO+UNICEF 是唯一全球医学共识 — 不是某国意见,是国际公共卫生政策。\n"
    "WHO 立场跟 AAP/鲍/松田 部分一致(6 月 EBF / 反产院定时喂奶),部分对立(辅食 6 月 vs AAP 4-6 月 / 持续母乳 2 年 vs 中国'早断')。\n"
    "孕期就要看 WHO 标准 — 选医院 / 选奶粉品牌 / 想喂多久,WHO 给国际答案。",
    [
        "孕期读 WHO 6 月 EBF + 持续 2 年共识",
        "选产院问 BFHI 认证(母婴友好医院倡议)",
        "买奶粉看品牌是否守 Code(国际营销禁令)",
        "决定喂多久不被亲戚施压 — WHO 推荐 ≥ 2 年",
        "中国 EBF 率仍 < 50% — 你不一定要随大流",
    ],
    "只看中国传统(早断 / 早辅食 / 奶粉随便选)→ 错过国际证据 + 受营销绑架。\n"
    "WHO 是目前最强 Tier 1 国际权威,值得知道。",
    "A",
    ["G-ABBR-WHO", "G-ABBR-EBF", "G-ABBR-BFHI", "G-TERM-WHO-Code"],
    ["C-S0-1025", "C-S1-050", "C-S6-1064"],  # 跨派:本卷+AAP+本卷
    "WHO+UNICEF Infant and Young Child Feeding Fact Sheet",
    "fact sheet 总览:WHO 政策合集 + 跟其他国家指南对照",
    URL_IYCF))

cards.append(("C-S0-1025", "S0",
    "选产院:认 BFHI 标志",
    "母婴友好不是噱头",
    "BFHI(Baby-Friendly Hospital Initiative,母婴友好医院倡议)是 WHO+UNICEF 1991 启动,2018 修订的产院实操标准。\n"
    "全球 152+ 国 15,000+ 家医院认证(2011 数据)。中国是早期签署国 — 6,000+ 爱婴医院。\n"
    "BFHI 10 步指出生 1 小时内开奶 / 24 小时同室 / 不定时喂奶 / 不轻易给奶瓶 / 出院衔接。\n"
    "中国数字层级首位但实操参差 — 看到'爱婴医院'牌子≠真按 10 步执行。",
    [
        "选产院问'是否 BFHI 认证 + 何时复评'",
        "问'出生后立即肌肤接触多久'(BFHI 标准 ≥ 1 小时)",
        "问'是否 24 小时同室'(不同室不达标)",
        "问'非医学指征下是否给配方奶'(不应该给)",
        "看到爱婴牌子但实操不到位 → 自己坚持要求",
    ],
    "选了非 BFHI 医院或'纸面 BFHI' → 出生后被定时喂奶 / 母婴分离 / 早期奶瓶,母乳建立失败率高。\n"
    "孕期就该选好,临产换难。",
    "A",
    ["G-ABBR-BFHI", "G-ABBR-WHO"],
    ["C-S0-1024", "C-S1-1002", "C-S1-1004"],
    "Baby-Friendly Hospital Initiative",
    "BFHI 全球认证 + 中国 6000+ 爱婴医院数据 + 10 步骤",
    URL_BFHI_WIKI))

cards.append(("C-S0-1026", "S0",
    "中国奶粉 vs Code:你被营销了",
    "Code 禁的中国都在做",
    "International Code of Marketing of Breast-milk Substitutes(母乳代用品国际营销守则)1981 年第 34 届世卫大会通过。\n"
    "84 国立法实施,中国《婴幼儿配方乳粉广告法》仅部分对接。\n"
    "Code 禁:广告 / 妈妈样品 / 医生礼物 / 医院 promotion / 标签理想化图。\n"
    "中国奶粉品牌(飞鹤 / 雅培 / 惠氏 / 合生元 / 美素佳儿)实操:产院送试用装 / 母婴店推销 / 直播带货 / 跟随奶/增长奶'分阶'营销 — 多数违反 Code。",
    [
        "孕期警惕产院/母婴店 '免费试用装' — 不要拿",
        "奶粉广告(电视/直播)的 '智商 / 抗病' 暗示是 Code 违规",
        "医生送奶粉样品/礼物 → Code 明令禁止",
        "看 Code 全文(WHO 1981)— 知道哪些是营销陷阱",
        "选奶粉看品牌是否在国际 Code 监督名单",
    ],
    "信奶粉广告 → 提前断母乳 + 钱包多花 + 娃缺母乳免疫保护。\n"
    "Code 不是禁配方奶,是禁营销让你买不必要的。",
    "A",
    ["G-TERM-WHO-Code", "G-TERM-formula-marketing", "G-TERM-breastmilk-substitutes"],
    ["C-S0-1024", "C-S1-1009", "C-S1-1011"],
    "International Code of Marketing of Breast-milk Substitutes",
    "Code 1981 通过 + 4 利益方禁令 + 84 国立法 + IBFAN 监测",
    URL_CODE))

cards.append(("C-S0-1027", "S0",
    "全球 EBF 率 44%:谁都没达标",
    "你不是孤独的妈妈",
    "EBF(Exclusive Breastfeeding,纯母乳)0-6 月全球率 44%(2015-2020 WHO 数据)。\n"
    "WHO 2025 目标 ≥ 50% — 全球离目标都还差。\n"
    "中国 EBF 率约 30-40%(估算),低于全球平均。\n"
    "原因:奶粉营销 / 产院定时喂奶 / 工作环境不支持 / 产假短 / 信息错乱。\n"
    "Lancet 2016 系列(Victora 主编):普及 EBF 每年可救 82 万婴儿生命。",
    [
        "EBF 0-6 月不是 '理想化' 是 WHO 全球医学共识",
        "你坚持 EBF 不是 '矫情' — 是国际推荐",
        "中国数字差不要内疚 — 是系统性问题",
        "Lancet 数字记得:82 万婴儿生命 / 年",
        "找母乳支持小组 + 哺乳顾问扶上路",
    ],
    "因为 '别人都加奶粉了' 自责或妥协 → 错过母乳免疫保护 + 妈妈乳腺癌降险机会。\n"
    "全球都在追这个目标,你不是一个人。",
    "A",
    ["G-ABBR-EBF", "G-TERM-Lancet-breastfeeding-series"],
    ["C-S0-1024", "C-S1-1015", "C-S1-1014"],
    "WHO IYCF Fact Sheet + Lancet 2016",
    "全球 EBF 率 44% + Lancet 820k 生命数字 + 中国差距",
    URL_LANCET))

cards.append(("C-S0-1028", "S0",
    "Innocenti 1990:母乳的政治根基",
    "BFHI 起点在意大利",
    "Innocenti Declaration 1990 — UNICEF Florence Innocenti 中心起草,WHO+UNICEF+USAID+SIDA 联合发起的全球母乳喂养政治宣言。\n"
    "1990 原版 4 大目标:① 各国成立母乳协调员 ② BFHI 启动 ③ Code 立法 ④ 立法保护妈妈母乳权利。\n"
    "2005 修订版补充 9 大目标(包括 2025 全球量化指标)。\n"
    "BFHI 1991 启动直接来自 Innocenti 1990。中国签署国之一。\n"
    "[本卡基于 BFHI 间接引用 — Innocenti 全文 WebFetch 失败,见 gaps.md G_WHO_1]",
    [
        "BFHI / Code / 妈妈母乳权 政治根基:Innocenti 1990",
        "母乳喂养不是 '私人选择' — 是国际公共卫生政策",
        "孕期/产假/职场支持 是 Innocenti 国家义务",
        "中国签署 Innocenti — 政府有责任建母乳支持",
        "妈妈知道这背景就敢要求(产假 / 哺乳室 / BFHI 医院)",
    ],
    "把母乳当 '个人事' → 错过国家政策杠杆。\n"
    "Innocenti 是宣言不是建议 — 各国签了就有义务。",
    "B",
    ["G-TERM-Innocenti-Declaration", "G-ABBR-BFHI", "G-TERM-WHO-Code"],
    ["C-S0-1024", "C-S0-1025", "C-S0-1026"],
    "Innocenti Declaration via BFHI Wikipedia (主源 WebFetch 全失败)",
    "1990 Innocenti 是 BFHI 启动政治基础;具体 4+9 目标记 gaps",
    URL_BFHI_WIKI))

# ============================================================
# S1 新生儿(起 1000) — 主战场,18 张
# ============================================================

cards.append(("C-S1-1000", "S1",
    "出生 1 小时内开奶",
    "黄金 1 小时不能错",
    "Early Initiation(出生 1 小时内开奶)— WHO+UNICEF 共同建议。\n"
    "全球只 ~45% 婴儿在出生 1 小时内开奶,中国比例更低。\n"
    "关键作用:① 初乳免疫保护(IgA + lactoferrin + 寡糖)② 妈妈泌乳启动(吸吮 → 泌乳素)③ 母婴 bonding 关键窗。\n"
    "BFHI 第 4 步具体化为'立即且不间断的肌肤接触 + 1 小时内开奶'。\n"
    "中国传统产院:出生立即包裹+测量+称重+洗澡 → 错过 1 小时窗口。",
    [
        "出生立即肌肤接触(skin-to-skin)— 不要先包裹",
        "1 小时内尝试第一次吸吮(就算只 5 分钟)",
        "测量/称重等 → 推到 1 小时后",
        "剖宫产同样:妈妈条件允许就立即接触",
        "产前跟医生提前沟通 — 写入分娩计划",
    ],
    "出生立即被分离测量包裹 → 错过 1 小时窗口 + 初乳免疫保护 + 泌乳启动延迟。\n"
    "黄金 1 小时 only once,不能补。",
    "A",
    ["G-TERM-early-initiation", "G-TERM-skin-to-skin", "G-TERM-colostrum"],
    ["C-S1-1001", "C-S0-1025", "C-S1-051"],
    "BFHI Step 4 + WHO IYCF Fact Sheet",
    "出生 1 小时内开奶 + 立即肌肤接触 + 初乳保护",
    URL_BFHI))

cards.append(("C-S1-1001", "S1",
    "肌肤接触 ≥ 1 小时不间断",
    "不间断三个字关键",
    "BFHI 第 4 步 verbatim:'Facilitate immediate and uninterrupted skin-to-skin contact'。\n"
    "Skin-to-skin(SSC)= 婴儿赤裸贴在妈妈胸口 ≥ 1 小时,直到完成第一次吸吮。\n"
    "效果:① 体温稳定 ② 心率稳定 ③ 血糖稳定 ④ 哭闹减少 ⑤ 母乳启动加速。\n"
    "早产 / 剖宫产 / 妈妈状况允许时同样适用。\n"
    "中国产院常打断:称重 / 洗澡 / 包裹 / 给配方奶 → 都是 BFHI 不允许。",
    [
        "出生立即放妈妈胸口,赤裸贴皮肤",
        "持续 ≥ 1 小时不要打断(测量/称重等等)",
        "等娃自己找到乳头第一次吸吮",
        "剖宫产:爸爸先做 SSC,妈妈状况允许后接力",
        "提前跟产院沟通 — '不间断' 是关键词",
    ],
    "穿着衣服的接触 / 中途打断称重 → SSC 益处大幅打折。\n"
    "Skin-to-skin = 真的 skin-to-skin。",
    "A",
    ["G-TERM-skin-to-skin", "G-ABBR-BFHI"],
    ["C-S1-1000", "C-S1-1002", "C-S1-002"],
    "BFHI Step 4",
    "BFHI 第 4 步:立即且不间断肌肤接触 ≥ 1 小时",
    URL_BFHI))

cards.append(("C-S1-1002", "S1",
    "BFHI 10 步:产院实操圣经",
    "10 步看完心里有底",
    "BFHI(Baby-Friendly Hospital Initiative,母婴友好医院倡议)1991 WHO+UNICEF 启动,2018 修订。\n"
    "10 步分两组:关键管理(1a/1b/1c/2)+ 关键临床(3-10)。\n"
    "关键管理:遵 Code / 书面政策 / 监测系统 / 员工训练。\n"
    "关键临床:产前讨论 / 立即肌肤接触 / 持续支持 / 仅医学指征补充 / 24h 同室 / 反馈信号 / 警告奶瓶 / 出院衔接。\n"
    "全球 152+ 国 15,000+ 家医院 BFHI 认证。中国 6,000+ 爱婴医院。",
    [
        "选产院前看 BFHI 10 步原文",
        "认证医院 ≠ 一定守 — 实操参差",
        "看到偏离 10 步的实操 → 自己坚持",
        "母乳建立期(0-4 周)是 10 步关键期",
        "出院衔接(第 10 步)— 找社区/居家母乳支持",
    ],
    "把 BFHI 当 '认证名号' → 不知道实操标准,被产院流程裹挟。\n"
    "10 步具体化,值得记。",
    "A",
    ["G-TERM-BFHI-10-steps", "G-ABBR-BFHI"],
    ["C-S0-1025", "C-S1-1003", "C-S1-1005"],
    "BFHI 2018 Revised 10 Steps",
    "BFHI 10 步骤完整:关键管理 4 步 + 关键临床 7 步",
    URL_BFHI))

cards.append(("C-S1-1003", "S1",
    "只医学指征才给配方奶",
    "默认不给,这是底线",
    "BFHI 第 6 步 verbatim:'Do not provide breastfed newborns any food or fluids other than breast milk, unless medically indicated.'\n"
    "默认配置:0-4 周纯母乳,不给配方 / 葡萄糖水 / 茶水 / 中药水 / 米汤。\n"
    "可接受医学例外(WHO/UNICEF 2009 Acceptable Medical Reasons):\n"
    "婴儿端:半乳糖血症 / PKU / 极低出生体重 / 严重早产 / 严重高胆。\n"
    "母亲端:HIV+(高资源 + AFASS) / 严重疾病 / 化疗 / 放射药 / 1 型疱疹乳房病灶。\n"
    "中国产院常规给葡萄糖水 / 米粉糊 → 跟 BFHI 第 6 步对立。",
    [
        "0-4 周原则:只母乳,不给任何其他液体/固体",
        "葡萄糖水 / 中药水 / 米汤 → BFHI 不允许",
        "看到产院给非医学指征配方 → 拒绝",
        "真有医学指征(早产 / 严重黄疸)→ 听医生",
        "可接受医学例外清单见 WHO/UNICEF 2009",
    ],
    "默认接受产院 '助消化葡萄糖水' / '没奶先用配方过渡' → 干扰母乳建立 + nipple confusion。\n"
    "默认是不给,医学指征才例外。",
    "A",
    ["G-ABBR-BFHI", "G-TERM-acceptable-medical-reasons", "G-TERM-mixed-feeding"],
    ["C-S1-1002", "C-S1-1006", "C-S1-1012"],
    "BFHI Step 6 + Acceptable Medical Reasons (WHO/UNICEF 2009)",
    "BFHI 第 6 步 + 医学例外清单(WHO/UNICEF 2009 全文 WebFetch 失败,见 gaps G_WHO_2)",
    URL_BFHI))

cards.append(("C-S1-1004", "S1",
    "24 小时同室不分离",
    "Rooming-in 是底线",
    "BFHI 第 7 步:'Enable mothers and babies to remain together 24 hours a day (rooming-in)'。\n"
    "Rooming-in(24 小时同室)= 妈妈和娃整天整夜在同个房间,不分母婴室。\n"
    "效果:① 妈妈识别早期信号(吸吮动作/寻乳)② 按需喂养实操 ③ 减少配方奶补充 ④ 增加 EBF 成功率 ⑤ 母婴 bonding。\n"
    "例外:妈妈或娃需要 NICU / 严重医疗。\n"
    "中国传统产院常规分母婴室,只哺乳时送过来 → 跟 BFHI 第 7 步对立。",
    [
        "选产院问 '24 小时同室还是分母婴室'",
        "分母婴室 → 立刻要求改 24 小时同室",
        "晚上累 → 让爸爸或家人帮换尿布,妈妈休息但娃不分离",
        "看医学指征(NICU)分离是必要的 — 别强求",
        "出院前跟产院明确这点(写入分娩计划)",
    ],
    "接受'母婴室分开睡你休息好'话术 → 错过早期信号识别 + 母乳建立慢。\n"
    "累一点但娃留身边,长远母乳建立更快。",
    "A",
    ["G-TERM-rooming-in", "G-ABBR-BFHI"],
    ["C-S1-1002", "C-S1-1005", "C-S1-1003"],
    "BFHI Step 7",
    "BFHI 第 7 步:24 小时同室 + 母婴 bonding",
    URL_BFHI))

cards.append(("C-S1-1005", "S1",
    "反对定时喂奶 — 看信号",
    "3 小时定时是过时的",
    "BFHI 第 8 步:'Support mothers to recognize and respond to infant feeding cues.'(反对定时喂养,倡导反馈喂养)\n"
    "反馈喂养(responsive feeding)= 看娃信号决定喂,不按时间表。\n"
    "早期信号:唇啜 / 吸吮动作 / 寻乳 / 踢腿 / 警觉。\n"
    "晚期信号:哭(已经过头,饿+情绪 → 难有效吸)。\n"
    "新生儿胃容量小,需 8-12 次/24 小时,不可能 3 小时一次。\n"
    "松田 SRC-024 C-S1-761 也反对中国产院'3 小时定时 + 用枕头支奶瓶'。",
    [
        "看信号喂,不看时间表",
        "8-12 次/天(白天 2-3 小时上限)",
        "夜间最多 4 小时不喂一次",
        "哭已晚 — 早期信号(唇啜)就喂",
        "产院说'3 小时一次' → 违反 BFHI 第 8 步",
    ],
    "按 3 小时定时喂 → 错过早期信号 + 没奶涨给奶瓶补 + 母乳建立慢。\n"
    "Responsive 是 BFHI / AAP / 松田 三方共识。",
    "A",
    ["G-TERM-responsive-feeding", "G-ABBR-BFHI"],
    ["C-S1-1002", "C-S1-050", "C-S1-1016"],  # AAP C-S1-050 + 松田 C-S1-761
    "BFHI Step 8 + 松田 SRC-024 C-S1-761 一致",
    "BFHI 第 8 步:反馈喂养反对定时;跟松田 反产院'3 小时定时' 一致",
    URL_BFHI))

cards.append(("C-S1-1006", "S1",
    "早期奶瓶/奶嘴:慎用警告",
    "母乳建立期是 0-4 周",
    "BFHI 第 9 步:'Counsel mothers on use and risks of bottles, teats, pacifiers.'\n"
    "母乳建立期(0-4 周):奶嘴 / 奶瓶 → nipple confusion(奶头错乱)+ 干扰乳头吸吮模式。\n"
    "AAP / Karp(SRC-005)立场:母乳建立后 3-4 周再用 — 比 BFHI 略松。\n"
    "WHO BFHI 立场更严:能避就避 + 一定要用就告知风险。\n"
    "松田 SRC-024 C-S1-761 跟 BFHI 一致:反产院'用枕头支奶瓶'。",
    [
        "母乳建立 0-4 周尽量不用奶嘴 / 奶瓶",
        "需要用(妈妈不在)→ 用杯子/勺/注射器(spoon/cup feeding)",
        "4 周后母乳稳定再考虑奶嘴",
        "Karp 推 3-4 周用奶嘴防 SIDS — 跟 BFHI 立场略松,自己权衡",
        "一定要用奶瓶 → 选'paced bottle feeding'(节奏类母乳)",
    ],
    "0-4 周用奶嘴/奶瓶 → nipple confusion → 母乳吸吮模式损坏 + 妈妈奶量减少。\n"
    "0-4 周是母乳建立关键期,慎之又慎。",
    "A",
    ["G-TERM-nipple-confusion", "G-ABBR-BFHI"],
    ["C-S1-1002", "C-S1-022", "C-S1-1005"],  # 跨 Karp + BFHI
    "BFHI Step 9 + AAP/Karp 立场对照",
    "BFHI 第 9 步:奶瓶/奶嘴风险告知;比 AAP/Karp 立场更严",
    URL_BFHI))

cards.append(("C-S1-1007", "S1",
    "出院衔接:别孤立无援",
    "出院后才是真考验",
    "BFHI 第 10 步:'Coordinate discharge so that parents and their infants have timely access to ongoing support.'\n"
    "出院衔接:产院 → 社区 / 居家母乳支持 / 哺乳顾问 / 母乳支持小组。\n"
    "母乳建立失败的高峰常在出院后 1-2 周(困难刚来,没人接)。\n"
    "国际母乳协会(La Leche League)/ IBCLC 哺乳顾问 / 妇幼保健所 / 微信母乳群。\n"
    "中国产院出院支持薄弱 — 需要妈妈主动找。",
    [
        "出院前问产院'有没有出院后母乳支持电话/转介'",
        "提前找居家哺乳顾问(IBCLC 资质)",
        "加母乳支持微信群(同月龄 / 同城)",
        "妇幼保健所有母乳门诊 — 出院后 1 周复诊",
        "1-2 周内有任何疑问立刻问 — 别熬",
    ],
    "出院后没人接 + 自己熬 → 喂不上 / 涨奶 / 痛 / 放弃 → 加配方奶 → 母乳率下降。\n"
    "出院前就该铺好支持网。",
    "A",
    ["G-ABBR-BFHI"],
    ["C-S1-1002", "C-S1-1015", "C-S2-1045"],
    "BFHI Step 10",
    "BFHI 第 10 步:出院衔接 + 持续支持",
    URL_BFHI))

cards.append(("C-S1-1008", "S1",
    "EBF 操作定义:连水都不给",
    "ORS+维生素+药 才允",
    "EBF(Exclusive Breastfeeding,纯母乳喂养)WHO 操作定义 verbatim:\n"
    "'No other liquids or solids are given – not even water – with the exception of oral rehydration solution, or drops/syrups of vitamins, minerals or medicines.'\n"
    "允许:① ORS 口服补液(腹泻脱水时)② 维生素/矿物质 滴剂(如维 D)③ 药物。\n"
    "不允许:水 / 葡萄糖水 / 米汤 / 茶水 / 中药水 / 配方奶 / 任何固体。\n"
    "中国传统'要喂水防上火' / 葡萄糖水 → 都打破 EBF 资格。\n"
    "AAP / 鲍秀兰 / 松田 都说 EBF 6 月,但没明确列例外清单 — WHO 是唯一明确给定义的派。",
    [
        "EBF = 只母乳 + 例外清单",
        "维 D 滴剂(母乳娃必补)不打破 EBF",
        "ORS(腹泻脱水)不打破",
        "药物不打破",
        "水 / 葡萄糖水 / 米汤 → 打破 EBF",
    ],
    "给葡萄糖水 / 茶水 / 中药水 → EBF 资格丢失 + 干扰母乳吸吮 + 增加感染风险。\n"
    "操作定义记得:连水都不给。",
    "A",
    ["G-ABBR-EBF", "G-ABBR-WHO"],
    ["C-S1-1003", "C-S0-1024", "C-S2-1044"],
    "WHO ELENA: Exclusive Breastfeeding",
    "EBF 操作定义 verbatim + 例外清单(ORS/维生素/药)",
    URL_EBF))

cards.append(("C-S1-1009", "S1",
    "Code 1981:奶粉营销 4 大禁",
    "妈妈/医生/医院/标签",
    "International Code of Marketing of Breast-milk Substitutes 1981 第 34 届 WHA 通过。\n"
    "4 大利益方禁令(verbatim 引用):\n"
    "① 妈妈端:'All forms of product advertising and promotion are prohibited' + 无样品 + 公司不得直接联系\n"
    "② 医生端:无礼物/财务回扣 + 'samples in no case should be passed on to mothers'\n"
    "③ 医院端:'Promotion of any product is forbidden in a health care facility' + 不得免费/低价提供\n"
    "④ 标签端:'Pictures or text which may idealize the use of infant formula should not be used' + 必须警告污染风险\n"
    "1981 至今 84 国立法实施全部或部分,违规仍广泛(IBFAN/UNICEF/WHO 监测)。",
    [
        "电视/直播奶粉广告(智商/抗病暗示)→ Code 违规",
        "母婴店送试用装 / 满减 → Code 违规",
        "医生送奶粉样品 / 推销品牌 → Code 违规",
        "产院 'Welcome bag' 含奶粉 → Code 违规",
        "标签上'母乳般营养'/可爱婴儿图 → Code 违规",
    ],
    "信中国奶粉广告做选择 → 多花钱 + 提前断母乳 + 智商抗病等暗示无证据。\n"
    "Code 不禁配方奶,禁的是营销让你买不必要的。",
    "A",
    ["G-TERM-WHO-Code", "G-TERM-formula-marketing"],
    ["C-S0-1026", "C-S1-1010", "C-S1-1011"],
    "International Code of Marketing of Breast-milk Substitutes (1981)",
    "Code 4 大利益方禁令 verbatim + 84 国立法实施现状",
    URL_CODE))

cards.append(("C-S1-1010", "S1",
    "Code 涵盖产品:不只配方奶",
    "奶瓶奶嘴都管",
    "Code 涵盖范围(广义 'breast-milk substitutes'):\n"
    "① 配方奶(0-6 月用)\n"
    "② 跟随奶(6-12 月,follow-on formula)\n"
    "③ 增长奶(12 月+,growing-up milk)\n"
    "④ 1 岁内任何乳制品/婴儿食品\n"
    "⑤ 奶瓶 + 奶嘴\n"
    "⑥ 任何'用作部分或全部替代母乳的产品'\n"
    "中国奶粉品牌'1 段 / 2 段 / 3 段 / 4 段'分阶营销 → 暗示不同月龄需要不同奶粉,Code 禁止这种营销。\n"
    "增长奶('儿童奶' / '学步奶' / '4 段')是 Code 重点监管 — WHO 2016 决议加强。",
    [
        "1 段 / 2 段 / 3 段 / 4 段 营销话术 → 知道是 Code 监管对象",
        "'增长奶''学步奶''儿童成长奶' → WHO 2016 加强禁",
        "奶瓶 / 奶嘴 也是 Code 监管 — 不仅配方奶",
        "看广告里 '6 月+' '12 月+' 分阶 → 警惕营销",
        "1 岁后母乳 + 家庭饮食足够,不需要任何'增长奶'",
    ],
    "信奶粉品牌'分阶营养'话术 → 给 1 岁后娃买'4 段奶粉' / '儿童奶'。\n"
    "Code 直接禁止这种营销 — WHO 立场:1 岁后母乳 + 家庭饮食足够。",
    "A",
    ["G-TERM-WHO-Code", "G-TERM-breastmilk-substitutes", "G-TERM-formula-marketing"],
    ["C-S1-1009", "C-S6-1067", "C-S6-1070"],
    "International Code of Marketing — Product Coverage",
    "Code 涵盖配方奶/跟随奶/增长奶/奶瓶/奶嘴 + WHO 2016 决议加强",
    URL_CODE))

cards.append(("C-S1-1011", "S1",
    "中国奶粉:你被 Code 违规营销了",
    "飞鹤雅培惠氏都做",
    "中国奶粉品牌实操:产院送试用装 / 母婴店推销 / 直播带货 / 1-2-3-4 段分阶营销 — 多数违反 Code。\n"
    "中国《婴幼儿配方乳粉广告法》仅部分对接 Code(主要禁 0-6 月配方奶广告),6 月+ 跟随奶/增长奶营销宽松。\n"
    "IBFAN(International Baby Food Action Network)定期发布全球 Code 违规报告 — 中国市场长期上榜。\n"
    "代表性违规:\n"
    "- 产院'Welcome bag'含奶粉(BFHI 第 1a/6 步双重违反)\n"
    "- 直播主播'某某品牌让我家娃聪明'(理想化暗示)\n"
    "- 母婴店买奶粉送奶瓶(交叉营销)\n"
    "- 育儿 KOL 软广(暗示性 endorsement)",
    [
        "产院给 'Welcome bag' 含奶粉 → 拒绝 + 拍照举报",
        "直播带货奶粉 → 知道是 Code 违规",
        "买奶粉送奶瓶 → Code 第 7 章交叉营销禁",
        "KOL 软广夸奶粉 → 警惕(很多没有标注利益关系)",
        "查 IBFAN 中国报告 — 知道哪些品牌违规更严重",
    ],
    "信中国奶粉广告做选择 → 国际标准下都是违规营销。\n"
    "中国家长是这场营销的主战场 — 知道才能防。",
    "B",
    ["G-TERM-WHO-Code", "G-TERM-formula-marketing", "G-TERM-IBFAN"],
    ["C-S0-1026", "C-S1-1009", "C-S1-1010"],
    "International Code Compliance — China Status (估计)",
    "中国奶粉品牌 Code 违规普遍 + 中国法规仅部分对接 + IBFAN 监测",
    URL_CODE))

cards.append(("C-S1-1012", "S1",
    "可接受医学原因清单",
    "AFASS 评估再决定",
    "WHO/UNICEF 2009 联合发布 'Acceptable Medical Reasons for Use of Breast-milk Substitutes' 清单 — 临床医生用,哪些情况(也只在这些情况)可以使用配方奶。\n"
    "婴儿端医学例外:\n"
    "- 半乳糖血症(galactosemia,完全禁母乳)\n"
    "- 苯丙酮尿症(PKU,部分配特殊配方+母乳)\n"
    "- 枫糖尿症(MSUD)\n"
    "- 极低出生体重(<1500g)+ 严重早产(<32 周)\n"
    "- 严重高胆红素血症 / 严重窒息(临时)\n"
    "母亲端医学例外:\n"
    "- HIV+(高资源 + AFASS 满足时,改用配方)\n"
    "- 严重疾病(脓毒症 / 心力衰竭)\n"
    "- 1 型疱疹乳房病灶(临时,病灶愈合后恢复)\n"
    "- 化疗 / 放射性药物 / 部分精神药物\n"
    "[本卡基于 BFHI 第 6 步 + 间接信息 — 完整清单 WebFetch 失败,见 gaps G_WHO_2]",
    [
        "默认 EBF — 例外医学清单很短",
        "婴儿真有半乳糖血症 / PKU → 听医生用特殊配方",
        "妈妈 HIV+ + AFASS → 选配方而不是混合喂养",
        "妈妈短期重病 / 化疗 → 临时停母乳,病好后用 relactation 恢复",
        "'妈妈感冒' / '妈妈奶不够' → 不在医学例外清单",
    ],
    "把'妈妈累 / 奶不够 / 上班不便'当医学例外加配方 → 不符合 WHO 清单 + 母乳率不必要降。\n"
    "医学例外是真的医学,不是借口。",
    "A",
    ["G-TERM-acceptable-medical-reasons", "G-TERM-AFASS", "G-TERM-relactation"],
    ["C-S1-1003", "C-S1-1013", "C-S2-1045"],
    "Acceptable Medical Reasons (WHO/UNICEF 2009) — 间接覆盖",
    "医学例外清单(婴儿+母亲)— 完整清单 gaps G_WHO_2",
    URL_BFHI))

cards.append(("C-S1-1013", "S1",
    "HIV+ 妈妈:ART 时代可母乳",
    "AFASS 决定怎么喂",
    "WHO 2010 修订 — ART 时代立场转变(verbatim):'If replacement feeding is acceptable, feasible, affordable and safe (AFASS), HIV-infected mothers are recommended to use replacement feeding. Otherwise, exclusive breastfeeding is recommended.'\n"
    "AFASS 5 条件:可接受 / 可行 / 可负担 / 可持续 / 安全 — 全部满足才用配方。\n"
    "高资源区(美/欧/中国一线城市)+ AFASS 满足 → 用配方,MTCT 几乎消除。\n"
    "低资源区(撒哈拉)+ AFASS 不全 → EBF + 妈妈服 ART(降低传播率)。\n"
    "关键:不要混合喂养(母乳+配方)— 比纯一种风险更高。\n"
    "中国 PMTCT 指南:HIV+ 妈妈推荐用配方(AFASS 满足),但需个案评估。",
    [
        "HIV+ 妈妈不必然停母乳 — 看 AFASS 评估",
        "AFASS 满足 + 高资源区 → 用配方(MTCT < 1%)",
        "AFASS 不全 → EBF + 抗病毒治疗",
        "绝对不混合喂养 — 任何一边纯",
        "中国 HIV+ 妈妈先到 PMTCT 门诊评估再决定",
    ],
    "把'HIV+'等于'必须配方'→ 老立场,2010 修订改了。\n"
    "AFASS 5 条件评估:有 ART + 有支持环境 + 个案。",
    "A",
    ["G-TERM-HIV-feeding", "G-TERM-AFASS", "G-TERM-mixed-feeding"],
    ["C-S1-1012", "C-S1-1003", "C-S0-1024"],
    "WHO HIV and Infant Feeding Guidelines (2010 ART era)",
    "WHO 2010 ART 时代修订 + AFASS 5 条件 + MTCT 数据",
    URL_HIV))

cards.append(("C-S1-1014", "S1",
    "母乳免疫成分:配方做不到",
    "活的食物vs粉冲的",
    "母乳免疫成分(WHO + Lancet 2016 verbatim):\n"
    "① sIgA(分泌型免疫球蛋白 A):覆盖喉/肺/肠黏膜病原体\n"
    "② lactoferrin(乳铁蛋白):广谱抗病原 + 抗炎\n"
    "③ oligosaccharides(寡糖):喂益生菌 + 防病原黏附\n"
    "④ 抗氧化酶 + 抗炎蛋白 + 生长因子\n"
    "⑤ 妈妈病原暴露后 24-48 小时,母乳含特定抗体\n"
    "Lancet 2016 关键论点:'母乳是活的食物' — 配方奶模拟得到营养，模拟不到免疫保护。\n"
    "WHO:母乳保护胃肠感染 + 降低腹泻/肺炎死亡。",
    [
        "知道母乳免疫成分(IgA/lactoferrin/寡糖)",
        "妈妈感冒 → 母乳含针对性抗体,继续喂保护娃",
        "配方奶'添加 DHA/HMO 仿母乳' → 单点不能模拟全套",
        "活的食物 vs 粉冲 — 配方奶不是同等替代",
        "EBF 6 月免疫保护最强期,值得坚持",
    ],
    "信奶粉广告'添加母乳成分' → 母乳免疫是几百种成分协同,单点添加是营销。\n"
    "母乳是活的,配方是粉冲的。",
    "A",
    ["G-TERM-colostrum", "G-ABBR-EBF", "G-TERM-Lancet-breastfeeding-series"],
    ["C-S0-1027", "C-S1-1015", "C-S1-1000"],
    "Lancet 2016 + WHO Breastfeeding Topic",
    "母乳免疫成分(IgA/lactoferrin/寡糖)+ 'living food'",
    URL_LANCET))

cards.append(("C-S1-1015", "S1",
    "Lancet 2016:82 万生命可救",
    "硬数字记一辈子",
    "Lancet 2016 母乳喂养系列(Cesar Victora 主编)— 母乳证据集大成。\n"
    "核心数字 verbatim:'Increased breastfeeding to near-universal levels in low and middle income countries could prevent approximately 820,000 deaths of children under the age of five annually.'\n"
    "其他关键发现:\n"
    "- 母乳娃 IQ 高 ~3 点(Horta 2015 元分析,中低收入国家更明显)\n"
    "- 母乳妈妈乳腺癌降 6%(每 12 月哺乳)\n"
    "- 卵巢癌 / 2 型糖尿病 / 心血管 / 类风湿 全降\n"
    "- 全球 EBF 普及节省 3000 亿美元/年医疗成本\n"
    "Lancet 2016 跟 WHO 立场互相支撑 — 学术综述+政策共识双背书。",
    [
        "记 82 万婴儿生命/年 — 母乳的硬数字",
        "母乳娃 IQ 高 3 点(中低收入国家更明显)",
        "妈妈乳腺癌每 12 月哺乳降 6%",
        "全球 EBF 节省 3000 亿美元医疗",
        "母乳是公共卫生议题,不是个人偏好",
    ],
    "把母乳当'我自己的事' → 错过这是国际公共卫生关键的认识。\n"
    "Lancet 数字给你坚持的硬证据。",
    "A",
    ["G-TERM-Lancet-breastfeeding-series", "G-PERSON-Victora", "G-PERSON-Horta"],
    ["C-S0-1027", "C-S1-1014", "C-S0-1024"],
    "Lancet 2016 Breastfeeding Series",
    "Lancet 2016 + Horta 2015 IQ + Victora 主编 + 母亲健康益处",
    URL_LANCET))

cards.append(("C-S1-1016", "S1",
    "中国产院定时喂奶差距",
    "BFHI 标签≠真守",
    "中国 6,000+ 爱婴医院数字层级首位,但实操参差。\n"
    "常见'纸面 BFHI'问题:\n"
    "- 出生立即包裹+测量+称重,不等 1 小时肌肤接触\n"
    "- 母婴室分开,只送过来哺乳(违反第 7 步)\n"
    "- 3 小时定时喂奶('护士说该喂了'),不看信号(违反第 8 步)\n"
    "- 'Welcome bag' 含奶粉样品(违反第 1a/6 步双重)\n"
    "- 葡萄糖水 / 米汤 / 助消化(违反第 6 步)\n"
    "- 用枕头支奶瓶喂(松田 SRC-024 反对,跟 BFHI 第 9 步一致)\n"
    "对策:孕期就跟产院/医生对齐,提前写分娩计划。",
    [
        "选产院前问 BFHI 何时复评(过期未评是预警)",
        "产前写分娩计划(立即 SSC / 24h 同室 / 不给配方)",
        "产中坚持 1 小时不间断 SSC + 不离开",
        "看到偏离 BFHI 实操立刻问'按 WHO 标准应该是 X'",
        "出院前确认无 'Welcome bag' 含奶粉",
    ],
    "看到爱婴医院牌子就放心 → 不查实操 → 落入定时喂奶 / 母婴分离陷阱。\n"
    "认证医院 ≠ 真守 10 步。",
    "B",
    ["G-ABBR-BFHI", "G-TERM-BFHI-10-steps"],
    ["C-S0-1025", "C-S1-1004", "C-S1-1005"],
    "BFHI Implementation Status — China",
    "中国 6,000+ 爱婴医院 + 实操参差(估计)",
    URL_BFHI_WIKI))

cards.append(("C-S1-1017", "S1",
    "初乳 colostrum:头 3 天黄金",
    "黄金浓汤别浪费",
    "Colostrum(初乳)= 出生后头 2-5 天分泌的黏稠黄色乳。\n"
    "成分独特:\n"
    "- sIgA 浓度 > 成熟乳 100 倍\n"
    "- lactoferrin 高浓度\n"
    "- 生长因子(EGF / IGF-1) 帮肠道发育\n"
    "- 量极少:出生第 1 天约 5 ml/餐(婴儿胃容量恰好)\n"
    "WHO + BFHI:出生 1 小时内开奶就是为了娃尽早得到初乳。\n"
    "中国传统'初乳脏要挤掉' / '没奶用配方过渡' → 错过初乳免疫黄金窗。",
    [
        "出生头 2-5 天的黄色黏稠乳是初乳,不是 '没奶'",
        "初乳量小但浓度高 — 5 ml 等于配方 50 ml 营养",
        "听到 '初乳脏要挤掉' → 别信(老传统错的)",
        "听到 '没奶用配方过渡' → 也别信(初乳期是正常)",
        "1 小时内开奶 + 频繁吸吮 → 助初乳到成熟乳过渡",
    ],
    "丢初乳或加配方过渡 → 错过 sIgA 100x 浓度免疫黄金窗。\n"
    "初乳是 evolutionary 设计完美的第一份食物。",
    "A",
    ["G-TERM-colostrum", "G-TERM-early-initiation"],
    ["C-S1-1000", "C-S1-1014", "C-S1-1003"],
    "WHO + BFHI on Colostrum",
    "初乳 sIgA 100x 浓度 + 出生头 5 天 + 1 小时内开奶",
    URL_BFHI))

# ============================================================
# S2 1-3 月(起 1044) — 5 张
# ============================================================

cards.append(("C-S2-1044", "S2",
    "按需喂养:看信号不看表",
    "信号才是真闹钟",
    "Responsive feeding(反馈/按需喂养)WHO 立场:1-3 月仍 8-12 次/24 小时。\n"
    "看信号决定喂,不按时间表(BFHI 第 8 步延续)。\n"
    "1-3 月信号变化:\n"
    "- 仍以早期信号为主(唇啜 / 寻乳 / 警觉 / 踢腿)\n"
    "- 哭仍是晚期信号\n"
    "- 'cluster feeding'(群聚喂):某些时段(傍晚)频繁要喂 — 正常,母乳建立期\n"
    "- 1-3 月仍可能 '看似没规律' — 是 normal,不是问题\n"
    "中国传统/老人施压'要规律' → 跟 WHO/AAP/松田 三方共识对立。",
    [
        "1-3 月按需 8-12 次 — 不要强求规律",
        "Cluster feeding(傍晚频繁)是正常",
        "看信号(早期)就喂,哭是晚期",
        "老人 '该喂了' / '别又喂' → 不被绑架",
        "妈妈记 '看娃不看表' 这句话",
    ],
    "强求 3 小时定时 / 4 小时定时 → 错过早期信号 + 母乳奶量调整失败。\n"
    "前 3 月是供需匹配期,频繁吸吮告诉身体奶量。",
    "A",
    ["G-TERM-responsive-feeding", "G-ABBR-EBF"],
    ["C-S1-1005", "C-S1-050", "C-S2-1045"],
    "WHO + BFHI Step 8",
    "WHO 反馈喂养 + 1-3 月按需 + cluster feeding 正常",
    URL_BF))

cards.append(("C-S2-1045", "S2",
    "奶量不够实操:别加奶粉",
    "频繁吸吮才是真解",
    "WHO Q&A 立场:'感觉奶不够'多数是错觉,真不够才需要干预。\n"
    "判断真不够看 4 个客观指标:\n"
    "- 体重曲线持续偏低(WHO Growth Standards 母乳基线)\n"
    "- 24 小时尿布 < 6 块(白天)\n"
    "- 持续黄软便 < 4 次/天(0-6 周)\n"
    "- 表情萎靡 / 哭弱\n"
    "都正常但 '感觉少' → 信号错觉。\n"
    "干预实操(WHO 推荐顺序):\n"
    "① 增加吸吮频次(8-12 → 12-15 次)\n"
    "② 检查衔乳姿势(找哺乳顾问 / IBCLC)\n"
    "③ 双侧轮替吸吮 + 挤压乳房\n"
    "④ 妈妈休息 / 喝水 / 营养\n"
    "⑤ 真奶不够才考虑供应物 / 配方补充(医生指导)",
    [
        "看 4 客观指标(体重/尿布/便/表情)— 不靠'感觉'",
        "感觉少 → 增加吸吮频次(频繁刺激奶量)",
        "找 IBCLC 哺乳顾问检查衔乳",
        "别轻易加奶粉 — 加了奶量进一步降",
        "中国'妈妈奶水不足'话术 → 多数是育儿不良习惯/错觉",
    ],
    "感觉少 → 直接加配方 → 吸吮减少 → 奶量真降 → 加更多配方 → 母乳停。\n"
    "频繁吸吮才是真解,加奶粉是相反操作。",
    "A",
    ["G-ABBR-EBF", "G-TERM-WHO-growth-standards", "G-TERM-galactagogue"],
    ["C-S1-050", "C-S1-1015", "C-S2-1044"],
    "WHO Q&A on Breastfeeding + supply concerns",
    "奶量不够 4 客观指标 + WHO 干预顺序 + 频繁吸吮原理",
    URL_QA))

cards.append(("C-S2-1046", "S2",
    "配方奶安全:70°C 水冲泡",
    "70 度不是巧合",
    "WHO 配方奶安全准备(2007 PIF 指南):\n"
    "① 用 ≥ 70°C 水冲泡(不是开水冲再凉)\n"
    "② 70°C 是杀阪崎肠杆菌(Cronobacter sakazakii)阈值 — 致命婴儿败血症/脑膜炎\n"
    "③ 配方奶不是无菌 — 粉本身可能含病原\n"
    "④ 冲泡后 2 小时内喝完,2 小时内冰箱冷藏 < 24 小时\n"
    "⑤ 装瓶前洗手 + 消毒奶瓶(开水煮 5 min / 蒸汽消毒)\n"
    "⑥ 不要重新加热剩奶(细菌已生长)\n"
    "中国家长常见错误:用 40-50°C '不烫' 水冲(粉里的细菌没被杀)。",
    [
        "用 ≥ 70°C 水冲奶粉 — 别用 40°C 不烫水",
        "冲泡后 2 小时内喝 — 不剩",
        "奶瓶/吸嘴洗 + 开水煮 5 min 消毒(6 月前每天)",
        "粉勺不要塞太满 — 不浓不稀",
        "外出装现冲奶 → 用保温瓶+室温下喂",
    ],
    "用 40-50°C 水冲(说'不烫娃')→ 阪崎杆菌不死 → 致命败血症 / 脑膜炎。\n"
    "70°C 是 WHO 安全阈值,不是巧合。",
    "A",
    ["G-TERM-breastmilk-substitutes"],
    ["C-S2-1045", "C-S1-1003", "C-S1-053"],
    "WHO PIF (Powdered Infant Formula) Safe Preparation 2007",
    "70°C 水 + 阪崎杆菌阈值 + 2 小时内喝完",
    URL_BF))

cards.append(("C-S2-1047", "S2",
    "LAM 哺乳避孕:产后 6 月内",
    "98% 有效但要满 3 条",
    "LAM(Lactational Amenorrhoea Method,哺乳闭经法)— WHO 推荐 4 大产后避孕方法之一。\n"
    "3 条件同时满足才有效(>98%):\n"
    "① 完全母乳(EBF,夜间日间≥4-6 小时一次)\n"
    "② 婴儿 < 6 月\n"
    "③ 月经未恢复(产后 56 天后判)\n"
    "失败率 < 2%(完美使用)。\n"
    "机制:吸吮 → 泌乳素 → 抑制 GnRH → 抑制排卵。\n"
    "任一条件失效 → 立刻找其他避孕方法(月经回 / 6 月到 / 加辅食 → LAM 失效)。\n"
    "中国传统'哺乳期不会怀孕' → 部分对(LAM 满足时)+ 部分错(不满足时常误)。",
    [
        "LAM 3 条件:EBF + < 6 月 + 月经未恢复",
        "三个都满足才 >98% — 任一失效就要换",
        "夜间不喂(让娃睡过夜)→ LAM 失效",
        "加辅食(6 月后)→ LAM 失效",
        "月经回 → 立刻换避孕方法",
    ],
    "信'哺乳期不怀孕'但 3 条件不全 → 意外怀孕。\n"
    "LAM 是有条件的天然避孕,不是哺乳期一定有效。",
    "A",
    ["G-TERM-LAM", "G-ABBR-EBF"],
    ["C-S2-1044", "C-S1-1008", "C-S0-1024"],
    "Lactational Amenorrhea Method (LAM)",
    "LAM 3 条件 + >98% 有效 + 泌乳素机制",
    URL_LAM))

cards.append(("C-S2-1048", "S2",
    "混合喂养风险高于纯",
    "比全母乳全配方都差",
    "WHO + Lancet 2016 立场:混合喂养(母乳+配方)在多数情况下风险高于纯母乳或纯配方。\n"
    "原因:\n"
    "① 配方奶量加 → 母乳吸吮减 → 妈妈奶量真降\n"
    "② 婴儿肠道菌群混乱 — 母乳菌群 vs 配方菌群相互干扰\n"
    "③ 配方奶蛋白不耐(CMPI/CMPA 5%)风险增加\n"
    "④ HIV+ 妈妈混合喂养传播率高于任一纯一种(WHO 2010)\n"
    "⑤ 心理:妈妈对'奶不够'焦虑加重\n"
    "WHO 推荐:能纯母乳就纯;真不够 → 个案评估;HIV+ AFASS → 选纯一种。",
    [
        "默认目标:纯一种(纯母乳优先,真不行纯配方)",
        "'晚上加一顿配方让妈妈休息' → 母乳奶量降",
        "'白天工作配方,晚上母乳' → 母乳奶量被打散",
        "真需要补充 → 用挤奶用杯子/勺(spoon-feeding)而非奶瓶",
        "HIV+ → 必须纯一种,不混合",
    ],
    "信 '混合喂养灵活' → 反而是最差选择(母乳奶量降 + 肠道菌群乱)。\n"
    "WHO 立场:能纯就纯。",
    "B",
    ["G-TERM-mixed-feeding", "G-ABBR-EBF"],
    ["C-S1-1013", "C-S2-1045", "C-S1-1003"],
    "WHO + Lancet 2016 + HIV Feeding Guidelines",
    "混合喂养在多场景下风险高于纯一种 + HIV+ 立场",
    URL_LANCET))

# ============================================================
# S3 3-6 月(起 1042) — 4 张
# ============================================================

cards.append(("C-S3-1042", "S3",
    "辅食 4 月还是 6 月?",
    "WHO 6 月,AAP 4-6 月",
    "辅食时机 — 现库 4 派立场对照(独家维度):\n"
    "① WHO/UNICEF:6 月起(不早也不晚)\n"
    "② AAP(SRC-006):4-6 月,看 readiness 信号(头控/伸手抓/能从勺到喉)\n"
    "③ 鲍秀兰(SRC-009):6 月起\n"
    "④ 松田(SRC-024):5-6 月起,有弹性\n"
    "WHO 立场依据:\n"
    "- 6 月前母乳能量+营养足够\n"
    "- 6 月前肠道未成熟,早期辅食增加感染/过敏风险\n"
    "- 6 月起母乳能量需求超出\n"
    "AAP 立场依据(SRC-006 LEAP 研究):\n"
    "- 早期(4-6 月)引入过敏食物反而预防过敏\n"
    "实操:WHO 是国际基准,AAP 给临床弹性。中国家长可参考 6 月,真早需要(WHO 也允许 4-6 月在 readiness 满足时)看医生。",
    [
        "默认参考 WHO 6 月起",
        "AAP 4-6 月也是合理(看 readiness)",
        "鲍秀兰 6 月,松田 5-6 月,都不早于 4 月",
        "4 月前坚决不给(肠道未成熟)",
        "6 月才开始更稳 — 国际医学共识",
    ],
    "听老人 '4 月加米粉助消化' → 跟 WHO/AAP/鲍/松田 全冲突。\n"
    "4 月前是 'no go zone',6 月是国际基准。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-six-months"],
    ["C-S0-1024", "C-S3-001", "C-S4-1045"],  # 跨 AAP C-S3-001
    "WHO Complementary Feeding + AAP Starting Solid Foods 立场对照",
    "WHO 6 月 vs AAP 4-6 月 vs 鲍秀兰 6 月 vs 松田 5-6 月四派对照",
    URL_CF))

cards.append(("C-S3-1043", "S3",
    "早期辅食:肠道还没准备",
    "4 月前坚决不给",
    "为什么 4 月前不给辅食(WHO + Lancet 2016 + AAP 共识):\n"
    "① 肠道屏障未成熟 — 蛋白分子穿透增加过敏\n"
    "② 肾功能未成熟 — 钠/蛋白负担\n"
    "③ 吞咽-呼吸协调未成熟 — 窒息风险\n"
    "④ 头控未稳 — 不能坐稳吃\n"
    "⑤ 母乳/配方足够 — 不需要额外能量\n"
    "中国传统'4 月加米粉助消化/助睡' → 错的:\n"
    "- 米粉 = 碳水化合物 = 短期饱但消化负担\n"
    "- 4 月前肠道生不出消化酶处理米粉\n"
    "- '助睡眠' 没有证据 — 反而干扰夜醒喂奶。",
    [
        "4 月前坚决不给任何辅食(WHO/AAP/鲍/松田 一致)",
        "'4 月加米粉助消化' 是错的 — 4 月前肠道反而不能消化",
        "米粉助睡眠是误传 — 反而干扰夜醒",
        "听老人/亲戚施压 → 拿 WHO/AAP 立场堵回去",
        "想早开始 → 至少等 4 月 + 看 readiness 信号",
    ],
    "4 月前给米粉 / 蛋黄 / 果汁 → 过敏风险增 + 肠道损伤 + 母乳量被替代下降。\n"
    "肠道是娃的免疫第一道,等 6 月发育好。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-six-months"],
    ["C-S3-1042", "C-S3-001", "C-S0-1024"],
    "WHO + AAP + Lancet 2016 共识",
    "4 月前肠道/肾/吞咽未成熟 + 米粉助消化是误传",
    URL_CF))

cards.append(("C-S3-1044", "S3",
    "提前加米粉是中国通病",
    "WHO 数据:中国差距大",
    "中国家长辅食通病 — 跟 WHO 国际共识差距:\n"
    "- 老人压力 '4 月加米粉助消化' → WHO 4 月前 NO\n"
    "- '米粉助睡眠' → 无证据,WHO/AAP 共识反对\n"
    "- '蛋黄抹嘴 1 月起' → 蛋白过敏风险\n"
    "- '葡萄糖水/果汁' → 1 岁内禁(AAP)+ 干扰母乳(WHO)\n"
    "- '中药/八珍粉' → 安全性无证据,WHO 反对\n"
    "- '让娃尝大人饭菜' → 钠/糖/油负担超婴儿肾肝\n"
    "WHO 立场:0-6 月只母乳/配方;6 月后辅食才开始。",
    [
        "顶住老人压力 — 4 月前不给任何辅食",
        "拿 WHO 6 月共识做盾牌(国际医学共识)",
        "米粉助睡 / 蛋黄抹嘴 / 葡萄糖水 → 都是中国通病不是科学",
        "让娃尝家人饭菜 → 钠糖超标,等 1 岁再说",
        "全家对齐(老公一起堵老人话)",
    ],
    "为家庭和谐让步给老人传统 → WHO 标准下娃可能过敏 + 肠损 + 母乳率降。\n"
    "守住 6 月这条线最重要。",
    "B",
    ["G-ABBR-CF", "G-TERM-WHO-six-months"],
    ["C-S3-1042", "C-S3-1043", "C-S0-1024"],
    "中国辅食通病 (估计) + WHO 立场",
    "中国家长跟 WHO 6 月共识差距 + 老人传统压力",
    URL_CF))

# ============================================================
# S4 6-9 月(起 1045) — 主战场,11 张
# ============================================================

cards.append(("C-S4-1045", "S4",
    "6 月开始辅食 + 持续母乳",
    "辅食是补不是替",
    "WHO 立场(verbatim):'From the age of 6 months, children should begin eating safe and adequate complementary foods while continuing to breastfeed for up to two years of age or beyond.'\n"
    "关键:辅食(complementary feeding)是 '补充' 不是 '替代' 母乳:\n"
    "- 6-12 月母乳供 ≥ 50% 能量\n"
    "- 12-24 月母乳供 ≥ 33% 营养\n"
    "中国/AAP 实操:加辅食 → 母乳量减少。WHO 反对这个换序:辅食 + 母乳并行。\n"
    "顺序建议:先母乳吃饱,再加辅食(避免辅食替代母乳)。",
    [
        "6 月开始加辅食,但母乳不减",
        "顺序:先母乳 (饱) → 再辅食 (尝/学)",
        "辅食 = 补,不是替",
        "6-12 月每天仍 4-6 次母乳",
        "12-24 月仍 3-4 次母乳",
    ],
    "加辅食立刻减母乳次数 → 6-12 月母乳份额从 50% 跌到 30% → 12 月断奶 → 跟 WHO 2 岁立场冲突。\n"
    "辅食是 'in addition to',不是 'replace'。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-six-months", "G-TERM-WHO-two-years"],
    ["C-S3-1042", "C-S4-1046", "C-S5-1037"],
    "WHO Complementary Feeding + Continued Breastfeeding",
    "WHO 6 月辅食起 + 持续母乳 + 6-12m 50% 能量",
    URL_CF))

cards.append(("C-S4-1046", "S4",
    "辅食 4 大支柱:WHO 框架",
    "及时充分安全反馈",
    "WHO 辅食 4 大支柱(four pillars):\n"
    "① 及时性 (Timely)— 6 月开始(不早不晚)\n"
    "② 充分性 (Adequate)— sufficient energy + protein + micronutrients\n"
    "③ 安全性 (Safe)— hygienic preparation + clean utensils + clean hands\n"
    "④ 反馈式 (Responsive)— responsive to child's hunger cues\n"
    "PAHO/WHO 2003 进一步给 10 大原则(全文 WebFetch 失败,见 gaps G_WHO_3)。\n"
    "4 支柱缺一不可 — 中国家长常缺反馈式(逼吃) + 充分性(米粉为主缺铁缺蛋白)。",
    [
        "记 4 支柱:及时(6 月)+ 充分(蛋白铁)+ 安全(卫生)+ 反馈(看信号)",
        "中国传统'米粉为主' → 缺反馈(逼吃) + 充分性(蛋白铁不够)",
        "看 4 支柱自查家里辅食实操",
        "及时性 — 不早不晚 6 月",
        "反馈式 — 看娃信号,不逼吃",
    ],
    "只关注 '吃了多少' → 缺反馈式(逼吃)+ 充分性(米粉低密度)。\n"
    "4 支柱平衡才合 WHO 标准。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles", "G-TERM-responsive-feeding"],
    ["C-S4-1045", "C-S4-1050", "C-S4-1051"],
    "WHO Complementary Feeding 4 Pillars",
    "WHO 4 支柱 + PAHO 10 原则(部分覆盖,gaps G_WHO_3)",
    URL_CF))

cards.append(("C-S4-1047", "S4",
    "6-8 月日 2-3 餐辅食",
    "餐数随月龄递增",
    "WHO 月龄餐数标准:\n"
    "- 6-8 月:辅食日 2-3 餐\n"
    "- 9-11 月:辅食日 3-4 餐\n"
    "- 12-23 月:辅食日 3-4 餐 + 1-2 加餐\n"
    "母乳/配方仍按需(6-12 月 4-6 次/天,12-24 月 3-4 次/天)。\n"
    "总能量 = 母乳 + 辅食。WHO 6-12 月辅食供 ~50% 能量,12-24 月 ~67%。\n"
    "中国传统'1 岁前不要吃太多怕积食' → 跟 WHO 立场对立,反而辅食量不足。",
    [
        "6-8 月:每天 2-3 餐辅食(每餐 2-3 勺起)",
        "9-11 月:每天 3-4 餐辅食",
        "12 月+:3-4 餐 + 1-2 加餐",
        "母乳/配方继续 — 加辅食不替代",
        "辅食量按娃信号(饱了停)",
    ],
    "怕积食给太少辅食 → 6 月后能量缺口 → 生长曲线掉。\n"
    "WHO 量是有依据 — 该吃就吃。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1045", "C-S4-1046", "C-S5-1037"],
    "WHO Complementary Feeding Frequency",
    "WHO 月龄餐数:6-8m 2-3 / 9-11m 3-4 / 12-23m 3-4+1-2",
    URL_CF))

cards.append(("C-S4-1048", "S4",
    "辅食多样性:四大食物组",
    "色彩多营养就齐",
    "WHO 食物多样性(dietary diversity)标准:每日辅食至少含 4 大食物组(共 7 组之中):\n"
    "① 谷物/根茎(米/面/土豆)\n"
    "② 豆类/坚果(豆腐/碎花生酱)\n"
    "③ 奶制品(母乳/配方/酸奶)\n"
    "④ 肉/禽/鱼/动物蛋白\n"
    "⑤ 蛋黄(铁源)\n"
    "⑥ 维A 富含(胡萝卜/南瓜/绿叶菜)\n"
    "⑦ 其他蔬果\n"
    "WHO 数据:全球 6-23 月辅食多样性达标率 < 1/4 — 中国估计也不高。\n"
    "中国通病:米粉/粥为主,蛋白/铁不足。",
    [
        "每日 4+ 食物组 — 看碗里几种颜色",
        "肉/鱼/蛋黄 一定要有(6 月起)",
        "蔬菜不只胡萝卜 — 绿叶/紫色都加",
        "米粉/粥不能为主 — 是碳水占比高蛋白少",
        "记口诀'有色彩有蛋白才算完整餐'",
    ],
    "辅食以米粉/粥为主 → 缺铁缺蛋白 → 6 月后铁性贫血 + 肌肉发育慢。\n"
    "全球 < 1/4 达标,中国家长可以做更好。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1046", "C-S4-1051", "C-S3-006"],  # 跨 AAP C-S3-006 (铁)
    "WHO Dietary Diversity Standard",
    "WHO 4+ 食物组标准 + 全球 < 1/4 达标",
    URL_CF))

cards.append(("C-S4-1049", "S4",
    "辅食质地:6→9→12 月递进",
    "泥糊到家庭饭",
    "WHO 食物质地递进(food consistency):\n"
    "- 6 月:泥状/碎状/半固体(homogeneous puree)\n"
    "- 8 月:可加 finger food(self-feeding 训练)\n"
    "- 12 月:过渡至家庭食物(family foods)— 切碎/煮软\n"
    "原则:'gradually increase food consistency and variety'。\n"
    "AAP 立场(SRC-006 BLW)略一致 — 4-6 月后 finger food / BLW 选项。\n"
    "中国传统'1 岁前都吃稀的'→ 跟 WHO 8 月加 finger food 立场冲突。",
    [
        "6 月:泥糊半固体",
        "8 月:加 finger food(切条让娃自抓)",
        "12 月:家庭食物(切碎煮软,跟随大人桌)",
        "1 岁前 '都吃稀的' 是错的 — 8 月就该练咀嚼",
        "质地慢→快递进,不是一辈子稀",
    ],
    "1 岁前都给稀泥糊 → 错过 8 月咀嚼训练窗 → 后续抗拒固体 + 语言发音影响。\n"
    "8 月 finger food 是关键节点。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1045", "C-S4-1046", "C-S4-001"],  # 跨 AAP BLW
    "WHO Complementary Feeding — Food Consistency",
    "WHO 6→8→12 月质地递进 + finger food 自喂训练",
    URL_CF))

cards.append(("C-S4-1050", "S4",
    "反馈喂养:看娃不强迫",
    "饱不饱娃自己说",
    "Responsive feeding(反馈喂养)WHO 立场延续到辅食期(6 月+):\n"
    "- 看娃饱腹信号(转头/闭嘴/吐出)→ 停\n"
    "- 看饥饿信号(伸手/张嘴/盯食物)→ 喂\n"
    "- 不强迫 / 不奖励 / 不威胁\n"
    "- 让娃决定吃多少(妈妈决定吃什么)— Ellyn Satter 'Division of Responsibility'\n"
    "中国通病:追着喂 / 看动画片喂 / 把'吃完一碗'当目标。\n"
    "WHO 立场:逼吃 → 损害自我饱腹调节 → 长期肥胖 / 挑食风险。",
    [
        "看信号:饱了停(转头/闭嘴/吐)",
        "饿了喂(伸手/张嘴)",
        "不追着喂 / 不看动画片喂",
        "妈妈选食物,娃决定吃多少",
        "今天没吃完不强求,明天可能吃多",
    ],
    "追着喂 + 强迫'吃完才算' → 损害自我饱腹调节 → 长期肥胖 / 厌食 / 挑食。\n"
    "Division of responsibility:你管做,他管吃多少。",
    "A",
    ["G-TERM-responsive-feeding", "G-ABBR-CF"],
    ["C-S4-1046", "C-S2-1044", "C-S6-1066"],
    "WHO Responsive Feeding + Ellyn Satter Division of Responsibility",
    "反馈喂养延续辅食期 + 不强迫 + 自我饱腹调节",
    URL_CF))

cards.append(("C-S4-1051", "S4",
    "含铁辅食优先 6 月起",
    "肉鱼蛋黄第一波",
    "WHO 辅食含铁优先 verbatim:'From 6 months onwards, complementary foods need to be high in iron, e.g. meat, poultry, fish, iron-fortified cereals.'\n"
    "为什么 6 月起首选含铁:\n"
    "- 母乳铁吸收率高但量降(6 月后)\n"
    "- 婴儿出生储铁在 6 月用完\n"
    "- 缺铁 → 缺铁性贫血 → IQ 影响(不可逆)\n"
    "推荐含铁辅食:\n"
    "① 红肉(牛肉泥/猪肉泥)— 血红素铁吸收最好\n"
    "② 禽肉(鸡肉/鸭肉)\n"
    "③ 鱼(三文鱼/鳕鱼)— 兼顾 DHA\n"
    "④ 蛋黄 — 中国传统但需注意过敏\n"
    "⑤ 强化铁米粉 — 方便但单一\n"
    "中国通病:米粉为主 / 怕肉硬不消化 / 蔬菜为主 → 缺铁。",
    [
        "6 月起第一批辅食:含铁优先",
        "肉/鱼/蛋黄/强化铁米粉 — 4 选 2-3",
        "肉别等 8 月 — 6 月起就能吃肉泥",
        "蔬菜/水果 是补充不是主体",
        "12 月做铁缺普查(AAP/WHO 一致)",
    ],
    "辅食以米粉/果蔬为主缺肉 → 6-12 月铁缺贫血 → IQ/动作发育影响。\n"
    "肉/鱼是 6 月起的优先,不是 8 月。",
    "A",
    ["G-ABBR-CF"],
    ["C-S4-1046", "C-S3-006", "C-S4-1048"],  # 跨 AAP C-S3-006
    "WHO + AAP Iron-rich Complementary Foods",
    "WHO 6 月起含铁优先 + 肉/鱼/蛋黄/强化米粉",
    URL_CF))

cards.append(("C-S4-1052", "S4",
    "WHO 生长曲线 vs CDC",
    "母乳基线vs配方基线",
    "WHO Child Growth Standards 2006 vs CDC 2000 Growth Charts 关键区别:\n"
    "WHO 2006:\n"
    "- 6 国 MGRS 研究(巴西/加纳/印度/挪威/阿曼/美国)\n"
    "- 母乳喂养 + 持续 ≥ 12 月样本\n"
    "- '应该长成什么样'(prescriptive)\n"
    "CDC 2000:\n"
    "- 美国数据(以配方喂养为主)\n"
    "- '实际长成什么样'(descriptive)\n"
    "结果差异:\n"
    "- 母乳娃在 CDC 图上偏轻 — 不是不健康,是基线不对\n"
    "- 配方娃 6-12 月在 WHO 图上偏重 — 配方喂养可能过喂\n"
    "中国卫健委 2018 起逐步采用 WHO 标准。",
    [
        "母乳娃 → 看 WHO 图(2006 母乳基线)",
        "配方娃 → 也看 WHO 图(标准更稳)",
        "CDC 图上偏轻不是不健康 — 基线不对",
        "看曲线趋势(自己的轨迹)而不是百分位",
        "中国新版生长图采 WHO 标准",
    ],
    "母乳娃看 CDC 图觉得 '偏轻要加奶粉' → 错的(基线不一致)。\n"
    "看 WHO 图,看自己曲线趋势。",
    "A",
    ["G-TERM-WHO-growth-standards"],
    ["C-S0-1024", "C-S4-1054", "C-S4-1053"],
    "WHO Child Growth Standards 2006 vs CDC 2000",
    "WHO 母乳基线(prescriptive) vs CDC 配方基线(descriptive)",
    URL_GROWTH))

cards.append(("C-S4-1053", "S4",
    "WHO 6 大动作里程碑",
    "独坐扶站爬扶走站走",
    "WHO Child Growth Standards 包括 6 大粗大动作里程碑(gross motor milestones)+ windows of achievement:\n"
    "① 独坐(sitting without support)— 中位 6 月,P3-P97 = 4-9 月\n"
    "② 扶站(standing with assistance)— 中位 7-8 月\n"
    "③ 手膝爬(hands-and-knees crawling)— 中位 9 月(20% 婴儿跳过爬)\n"
    "④ 扶走(walking with assistance)— 中位 10 月\n"
    "⑤ 独站(standing alone)— 中位 12 月\n"
    "⑥ 独走(walking alone)— 中位 13 月,P3-P97 = 9-17 月\n"
    "Windows of achievement = 健康范围,不是 '正常 vs 异常' 二分。\n"
    "跟 CDC LTSAE 9 月里程碑(SRC-001)互补:CDC 4 域里程碑,WHO 给 6 大动作时间窗。",
    [
        "看时间窗(P3-P97),不是中位数",
        "13 月走是中位 — 9 月走也健康,17 月走也健康",
        "20% 娃跳过爬直接走 — 不是异常",
        "出生 6 月 P3 不能独坐 → 看医生",
        "结合 CDC LTSAE 4 域里程碑参考",
    ],
    "看到 '12 月还不会走' 就焦虑加干预 → P3-P97 范围内都是正常。\n"
    "WHO 的时间窗给宽容,但 P3 外要查。",
    "A",
    ["G-TERM-WHO-growth-standards"],
    ["C-S4-1052", "C-S4-1054"],
    "WHO Child Growth Standards — Gross Motor Milestones",
    "WHO 6 大动作里程碑 + windows of achievement P3-P97",
    URL_GROWTH))

cards.append(("C-S4-1054", "S4",
    "母乳娃在 CDC 图偏轻别慌",
    "基线问题,不是体重",
    "中国家长常见困惑:'娃在生长曲线偏轻,要不要加奶粉?'\n"
    "可能是 CDC vs WHO 基线问题,不是真不长:\n"
    "- 母乳娃 6-12 月在 CDC 图上常 P25-P50 → 看似 '中等偏下'\n"
    "- 同娃在 WHO 图上 P50-P75 → 'normal-高'\n"
    "干预决策应基于 WHO 图(母乳基线)+ 趋势(自己的曲线)。\n"
    "Lerner V4 G-TERM-WHO-feeding 已建术语 — 跟综述权威立场一致。\n"
    "实操:中国部分医院仍用 CDC 老图,导致母乳娃被误判'偏轻'加奶粉 → 母乳量降 → 真偏轻 → 自我实现预言。",
    [
        "查娃用的是 WHO 图还是 CDC 老图",
        "母乳娃 → 一定看 WHO 图(2006 母乳基线)",
        "CDC 图 P25 母乳娃 → 在 WHO 图可能 P50-P75",
        "看趋势(自己曲线)比看百分位重要",
        "怀疑医院用错图 → 自己拿 WHO 图复核",
    ],
    "信医生 'CDC 图偏轻要加配方' → 母乳量被替代下降 → 真偏轻。\n"
    "确认是 WHO 图(母乳基线)再做决定。",
    "A",
    ["G-TERM-WHO-growth-standards"],
    ["C-S4-1052", "C-S2-1045"],
    "WHO Growth Standards — China Adoption",
    "WHO 母乳基线 vs CDC 配方基线 + 中国医院图差异",
    URL_GROWTH))

cards.append(("C-S4-1055", "S4",
    "母乳供 50% 能量 6-12 月",
    "辅食一半,母乳一半",
    "WHO 立场(verbatim):'In months 6-12, breastmilk continues to provide up to half or more of a child's nutritional needs.'\n"
    "6-12 月营养构成:\n"
    "- 母乳 ≥ 50% 能量 + 主要免疫保护\n"
    "- 辅食 ≤ 50% 能量 + 主要铁/锌/维 A\n"
    "AAP 立场(SRC-006):6 月推 EBF,12 月起可断 — 早于 WHO 2 年。\n"
    "中国传统'1 岁就该断,母乳没营养'→ 跟 WHO 50% 数字硬冲突。\n"
    "实操:6-12 月每天仍 4-6 次母乳,加辅食后总能量 = 母乳一半 + 辅食一半。",
    [
        "6-12 月母乳 ≥ 50% 能量,辅食 ≤ 50%",
        "每天 4-6 次母乳(辅食后仍喂)",
        "顺序:母乳吃饱后再加辅食",
        "'1 岁该断'/'母乳没营养'是错的",
        "6-12 月母乳免疫仍主要保护",
    ],
    "1 岁前减母乳追求 '辅食为主' → 跟 WHO 50% 数字冲突 → 母乳免疫保护下降 + 妈妈奶量真降。\n"
    "WHO 50% 是硬数据,不是建议。",
    "A",
    ["G-TERM-WHO-six-months", "G-TERM-WHO-two-years"],
    ["C-S4-1045", "C-S5-1038", "C-S6-1064"],
    "WHO Continued Breastfeeding 6-12 months",
    "WHO 6-12m 母乳 ≥ 50% 能量 + 12-24m ≥ 33%",
    URL_BF))

# ============================================================
# S5 9-12 月(起 1037) — 4 张
# ============================================================

cards.append(("C-S5-1037", "S5",
    "9-11 月:辅食 3-4 餐 + 母乳",
    "餐数升,母乳没减",
    "WHO 9-11 月喂养标准:\n"
    "- 辅食:每天 3-4 餐\n"
    "- 母乳:每天 4-6 次(按需)\n"
    "- 食物质地:加 finger food + 半固体\n"
    "- 食物多样性:4+ 食物组(肉/鱼/蛋黄/蔬果/谷物)\n"
    "- 母乳/辅食占比:辅食供能 ~40-50%,母乳 ~50-60%(6-12 月段)\n"
    "中国通病:9-12 月开始 '减母乳',跟 WHO 持续母乳到 2 岁立场冲突。",
    [
        "9-11 月:每天辅食 3-4 餐 + 母乳 4-6 次",
        "母乳次数不主动减 — 让娃自然调整",
        "加 finger food(切条自喂)",
        "食物多样性 — 4+ 食物组",
        "睡前/醒后母乳保留 — 1 岁后仍是核心",
    ],
    "9 月开始减母乳 '准备 1 岁断' → 错过 6-12 月母乳 50% 能量保护。\n"
    "9-11 月仍是母乳主期 — 不是断奶准备。",
    "A",
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1047", "C-S4-1055", "C-S5-1040"],
    "WHO Complementary Feeding 9-11 months",
    "WHO 9-11m 辅食 3-4 餐 + 母乳 4-6 次",
    URL_CF))

cards.append(("C-S5-1038", "S5",
    "Finger food 自喂训练",
    "8 月起让娃自抓",
    "WHO + AAP 共识:8 月起加 finger food(条状/指状)训练自喂。\n"
    "意义:\n"
    "① 训练抓握(pincer grasp 9 月发展)\n"
    "② 训练咀嚼\n"
    "③ 训练自我饱腹调节(看自己吃多少)\n"
    "④ 训练手眼协调\n"
    "⑤ 给娃 agency(自主感)\n"
    "安全:\n"
    "- 切条状不切圆片(防 choking)\n"
    "- 软度:能用拇指捏碎(蒸软南瓜/香蕉/煮软面条)\n"
    "- 一定坐高椅 + 大人在场\n"
    "- 不要分散注意力 + 不强迫\n"
    "中国通病:1 岁前都喂泥糊 + 怕脏不让自抓 → 错过抓握/咀嚼/自我调节训练窗。",
    [
        "8 月起加 finger food(切条状)",
        "切条不切圆片(防 choking)",
        "蒸软南瓜/香蕉/面条/牛油果",
        "坐高椅 + 大人监督 + 别抱着喂",
        "怕脏让娃自抓 vs 怕脏一直喂泥糊 — 选前者",
    ],
    "1 岁前都喂泥糊 → 错过 8-12 月抓握/咀嚼/自我饱腹关键窗。\n"
    "8 月开始加 finger food,不要等 1 岁。",
    "A",
    ["G-ABBR-CF", "G-ABBR-BLW"],
    ["C-S4-001", "C-S4-1049", "C-S5-1037"],
    "WHO + AAP BLW Finger Food",
    "WHO 8 月起 finger food + 抓握训练 + 切条防 choking",
    URL_CF))

cards.append(("C-S5-1039", "S5",
    "1 周岁仍持续母乳",
    "12 月不是断奶分水岭",
    "WHO 立场(verbatim):'continuing to breastfeed for up to 2 years of age or beyond.'\n"
    "12 月不是断奶分水岭 — 是辅食 + 母乳并行的中段。\n"
    "AAP 立场(SRC-006):12 月可断 — 跟 WHO 立场对立(早 1 年)。\n"
    "中国传统'1 岁就该断' → 跟 WHO 直接冲突。\n"
    "12-24 月母乳价值:\n"
    "- 仍供 33% 营养\n"
    "- 免疫保护持续(IgA / lactoferrin 浓度甚至高于 6 月前)\n"
    "- 心理慰藉(进入分离焦虑期)\n"
    "- 妈妈乳腺癌降险(每 12 月哺乳 6%)",
    [
        "12 月不是断奶时间 — 是 WHO 半程标志",
        "AAP 12 月可断 vs WHO 2 年 — 选 WHO",
        "中国'1 岁该断'是传统不是科学",
        "12-24 月母乳供 33% 营养 + 持续免疫",
        "妈妈乳腺癌每 12 月哺乳降 6%",
    ],
    "1 岁强行断 → 跟 WHO 共识冲突 → 错过 12-24 月母乳 33% 营养 + 免疫保护。\n"
    "WHO 推 2 年内继续,不是 1 年。",
    "A",
    ["G-TERM-WHO-two-years"],
    ["C-S4-1055", "C-S6-1064", "C-S6-1067"],
    "WHO Continued Breastfeeding to 2 Years",
    "WHO 12 月不是断奶 + AAP 1 年立场对立 + 中国'早断'传统",
    URL_BF))

cards.append(("C-S5-1040", "S5",
    "12 月转奶粉?WHO 不推",
    "继续母乳是国际标准",
    "中国家长常见决策:'12 月断母乳,转配方或牛奶,加辅食为主'。\n"
    "WHO 立场:不推荐 12 月断母乳 — 推荐持续 ≥ 2 年。\n"
    "如果妈妈不能继续母乳(回工作 / 健康),WHO 推荐:\n"
    "① 优先:挤奶 + 储奶 + 给娃喝(用杯不奶瓶)\n"
    "② 其次:relactation(重新泌乳)+ 找代乳(家庭成员)\n"
    "③ 最后:配方奶(若 < 12 月)/ 全奶(若 ≥ 12 月)\n"
    "12 月+ 不需要 '跟随奶' / '增长奶' — Code 反对(see C-S1-1010)。\n"
    "中国常见误区:12 月断母乳 → 转 '3 段配方奶' / '儿童奶' → 多花钱 + 错过母乳免疫。",
    [
        "12 月不主动断母乳 — WHO 默认 2 年",
        "回工作 → 挤奶 / 储奶 / 杯喂(不奶瓶)",
        "12 月+ 不需要 '跟随奶/增长奶' → Code 禁",
        "12 月+ 牛奶可代配方,但母乳仍优先",
        "'1 岁该转 3 段奶粉' 是奶粉营销话术",
    ],
    "12 月断母乳转 3 段奶粉 → 错过 12-24 月母乳 33% 营养 + 给奶粉公司多花钱(无证据益处)。\n"
    "WHO 立场:12 月不是断奶时间。",
    "B",
    ["G-TERM-WHO-two-years", "G-TERM-formula-marketing", "G-TERM-relactation"],
    ["C-S5-1039", "C-S1-1010", "C-S6-1067"],
    "WHO Continued Breastfeeding + Code on Follow-on/Growing-up Milk",
    "WHO 12 月不断奶 + 跟随/增长奶 Code 禁 + relactation 选项",
    URL_BF))

# ============================================================
# S6 12-24 月(起 1064) — 主战场,7 张
# ============================================================

cards.append(("C-S6-1064", "S6",
    "持续母乳到 2 岁国际共识",
    "全球只 WHO 这么明",
    "WHO 是现库唯一明确推 2 岁内继续母乳的派(其他派 1 岁可断 / 弹性)。\n"
    "WHO verbatim:'continuing to breastfeed for up to 2 years of age or beyond.'\n"
    "现库 4 派对比:\n"
    "- AAP(SRC-006):6 月 EBF + 1 岁可断(可继续不强求)\n"
    "- 鲍秀兰(SRC-009):1 岁可断\n"
    "- 松田(SRC-024):弹性 / 妈妈决定\n"
    "- WHO(SRC-031):≥ 2 岁,'beyond' 可继续\n"
    "依据:\n"
    "- 12-24 月母乳供 33% 营养(硬数据)\n"
    "- 免疫保护持续(IgA / lactoferrin 高浓度)\n"
    "- 妈妈乳腺癌降险(每 12 月哺乳 6%)\n"
    "- 母婴 bonding 心理价值",
    [
        "WHO 推 2 年(国际共识)— 比 AAP/鲍/松田 都长",
        "12-24 月母乳 33% 营养 — 不是 '没营养'",
        "妈妈乳腺癌每 12 月哺乳降 6% — 妈妈受益",
        "选 WHO 长喂 vs AAP 1 年断 — 自己权衡",
        "中国'2 岁内还在喂' 不是 '惯坏',是 WHO 国际标准",
    ],
    "因为 '别人都 1 岁断' 而 1 岁断 → 跟 WHO 国际共识冲突 → 错过 12-24 月营养免疫。\n"
    "WHO 立场不是建议,是公共卫生标准。",
    "A",
    ["G-TERM-WHO-two-years"],
    ["C-S4-1055", "C-S5-1039", "C-S6-1067"],
    "WHO 2-Year Continued Breastfeeding",
    "WHO ≥ 2 年 vs AAP 1 年 vs 中国'早断' 立场对照",
    URL_BF))

cards.append(("C-S6-1065", "S6",
    "12-24 月母乳 33% 营养",
    "硬数字反'没营养'",
    "WHO verbatim:'In months 12-24, breastmilk continues to provide up to one third (33%) of nutritional needs.'\n"
    "中国传统/老人话术'1 岁后母乳没营养' → 直接跟 WHO 33% 硬数字对立。\n"
    "12-24 月母乳成分变化:\n"
    "- 蛋白浓度上升(适应学步儿活动量)\n"
    "- 脂肪浓度仍高\n"
    "- IgA / lactoferrin 浓度甚至高于 6 月前\n"
    "- 寡糖持续(肠道菌群保护)\n"
    "Lancet 2016:12-24 月母乳依然预防腹泻 / 上呼吸道感染 / 中耳炎。",
    [
        "12-24 月母乳供 33% 营养(WHO 硬数字)",
        "'1 岁后没营养' 是错的(免疫成分甚至更高)",
        "12 月后母乳蛋白上升,脂肪仍高",
        "IgA / lactoferrin 12 月+ 浓度高于 6 月前",
        "继续喂保护腹泻/呼吸道/中耳炎",
    ],
    "信'1 岁后没营养'断奶 → 错过 33% 营养 + 持续免疫保护(浓度高于 6 月前)。\n"
    "WHO 数字记得:33% 不是 0%。",
    "A",
    ["G-TERM-WHO-two-years"],
    ["C-S6-1064", "C-S6-1067", "C-S1-1014"],
    "WHO Continued Breastfeeding 12-24 months",
    "WHO 12-24m 33% 营养 + 免疫成分浓度变化",
    URL_BF))

cards.append(("C-S6-1066", "S6",
    "12-23 月:3-4 餐 + 加餐",
    "餐数到顶,加点心",
    "WHO 12-23 月喂养标准:\n"
    "- 辅食:每天 3-4 餐\n"
    "- 加餐(snacks):每天 1-2 次\n"
    "- 母乳:每天 3-4 次(按需)\n"
    "- 食物质地:跟随家庭食物(family foods,切碎煮软)\n"
    "- 食物多样性:5+ 食物组\n"
    "总能量构成:辅食 ~67%,母乳 ~33%。\n"
    "加餐 = 健康零食(水果/酸奶/小块奶酪),不是糖/盐重的零食。",
    [
        "12-23 月:3-4 餐辅食 + 1-2 加餐 + 3-4 次母乳",
        "辅食跟随家庭饮食(切碎煮软)",
        "5+ 食物组(肉/蛋/奶/蔬/果/谷)",
        "加餐 = 水果/酸奶/小块奶酪(不糖盐重)",
        "母乳 33% 营养 — 不是辅食为主就停母乳",
    ],
    "把'1 岁后跟大人吃' = 钠/糖/油大人量 → 学步儿肝肾负担超 + 健康零食被替代为糖盐零食。\n"
    "12-23 月饮食是模仿大人但减量减盐。",
    "A",
    ["G-ABBR-CF"],
    ["C-S6-1064", "C-S6-1065", "C-S5-1037"],
    "WHO Complementary Feeding 12-23 months",
    "WHO 12-23m 3-4 餐 + 1-2 加餐 + 5+ 食物组",
    URL_CF))

cards.append(("C-S6-1067", "S6",
    "中国'早断早好'vs WHO 2 岁",
    "你不是落后是国际",
    "中国传统'早断早好' / '1 岁就该断' / '2 岁还在吃丢人' → 直接跟 WHO ≥ 2 年共识冲突。\n"
    "传统说法 vs WHO 立场:\n"
    "- '1 岁后没营养' → WHO 12-24m 供 33% 营养(C-S6-1065)\n"
    "- '惯坏依赖' → WHO 母婴 bonding 是益处\n"
    "- '影响娃独立' → 没有证据,反而依恋安全 → 长期独立\n"
    "- '影响妈妈身体' → 反:乳腺癌/卵巢癌/2 型糖尿病降险\n"
    "- '老外不喂这么久' → 错的 — 北欧妈妈普遍喂到 2 岁(瑞典 BFHI 全国认证)\n"
    "WHO 立场:2 岁内继续是 normal 不是 abnormal。",
    [
        "1 岁断不是必然 — WHO 推 2 年",
        "亲戚 '太久了/惯坏' 不被绑架",
        "拿 WHO + Lancet 数字回应('33% 营养''乳腺癌降 6%')",
        "瑞典 / 北欧普遍 2 岁 — 不是中国 '落后'",
        "妈妈和娃决定,不被传统/亲戚施压",
    ],
    "因家人/亲戚施压 1 岁断 → 错过 12-24m 33% 营养 + 妈妈乳腺癌降险机会。\n"
    "WHO 立场是国际共识 — 不是西方猎奇。",
    "B",
    ["G-TERM-WHO-two-years"],
    ["C-S6-1064", "C-S6-1065", "C-S0-1024"],
    "WHO Continued Breastfeeding + China Tradition",
    "中国'早断早好' vs WHO 2 年共识 + 北欧普遍",
    URL_BF))

cards.append(("C-S6-1068", "S6",
    "工作妈妈持续母乳实操",
    "挤奶储奶杯喂",
    "WHO 工作场所母乳支持建议:\n"
    "- 带薪产假 ≥ 6 月(中国法律 158 天 ≈ 5 月)\n"
    "- 哺乳室(干净 / 隐私 / 冰箱)\n"
    "- 弹性时间挤奶(每 3-4 小时)\n"
    "- 储奶规则:常温 4 小时 / 冰箱 4 天 / 冷冻 6 月\n"
    "工作妈妈持续母乳实操:\n"
    "① 产假末预存奶(冷冻)\n"
    "② 上班挤奶 2-3 次/天(午餐 + 一次)\n"
    "③ 在家直接喂(早起 / 睡前)\n"
    "④ 让娃白天用杯喝奶(不用奶瓶,防 nipple confusion)\n"
    "中国通病:'回工作 = 断奶' → 错的,可以继续。",
    [
        "回工作 ≠ 断奶 — 挤奶/储奶/杯喂可以",
        "上班挤奶 2-3 次(午餐 + 一次)",
        "储奶规则:常温 4h / 冰 4d / 冻 6m",
        "白天用杯喂(不奶瓶),晚上直接哺乳",
        "找单位哺乳室 + 时间(中国法律有规定)",
    ],
    "回工作直接断 → 错过 6-24 月母乳营养 + 免疫。\n"
    "工作妈妈完全可以持续母乳到 2 岁。",
    "A",
    ["G-TERM-WHO-two-years"],
    ["C-S6-1064", "C-S6-1067", "C-S6-1069"],
    "WHO Workplace Breastfeeding Support",
    "WHO 工作场所支持 + 储奶规则 + 中国 158 天产假",
    URL_QA))

cards.append(("C-S6-1069", "S6",
    "中国 158 天产假 vs WHO 6 月",
    "差 1 个月怎么办",
    "中国法律产假 158 天(约 5 月) — 比 WHO 推荐 ≥ 6 月理想短约 1 月。\n"
    "影响:产假结束(5 月)+ 未到 EBF 6 月目标 → 妈妈两难。\n"
    "WHO 立场对策:\n"
    "① 优先 EBF 6 月 → 产假末挤奶储奶(让娃 5-6 月用杯喝挤的奶)\n"
    "② 工作场所必须有哺乳室 + 弹性时间(中国劳动法支持)\n"
    "③ 产假可申请延长(单位政策 / 病假 / 弹性)\n"
    "④ Relactation(重新泌乳)— 即使中断也可恢复\n"
    "⑤ 配偶/家人帮助(送奶/接送)\n"
    "瑞典 / 北欧产假 ≥ 12 月,中国 5 月差距大但仍可努力。",
    [
        "产假 158 天但目标 EBF 6 月 — 挤奶补 1 月",
        "回工作前 2 周开始预存冷冻奶",
        "上班后挤奶 2-3 次/天",
        "争取工作哺乳室 + 弹性时间",
        "Relactation 是后路 — 即使中断可恢复",
    ],
    "产假结束就放弃 EBF 6 月 → 错过 5-6 月最后 1 月免疫保护期。\n"
    "中国 158 天差 WHO 6 月 1 月 — 努力补上。",
    "B",
    ["G-TERM-WHO-six-months", "G-TERM-relactation"],
    ["C-S6-1068", "C-S6-1064", "C-S2-1045"],
    "WHO 6 Months EBF vs China 158 Days Maternity Leave",
    "WHO 6 月理想 vs 中国 158 天产假 + 工作妈妈对策",
    URL_QA))

cards.append(("C-S6-1070", "S6",
    "增长奶儿童奶 Code 禁",
    "营销话术别上当",
    "中国奶粉品牌 1 岁后营销:'3 段奶粉' / '4 段儿童奶' / '学步成长奶' → WHO Code 重点监管对象。\n"
    "WHO 2016 决议加强对'follow-on formula'(跟随奶 6-12m)和'growing-up milk'(增长奶 12m+)的监管 — 这些产品 Code 早就涵盖。\n"
    "立场:1 岁+ 母乳 + 家庭饮食 + 全奶(若需要)足够 — 不需要任何专门奶粉。\n"
    "中国家长常见误区:\n"
    "- '1 岁后转 3 段奶粉更营养' → 错(配方主营销话术)\n"
    "- '4 段儿童奶补钙' → 全奶(普通奶) + 蔬果就够\n"
    "- '专门学步奶口感更好' → 加糖 + 香精,反而风险高",
    [
        "1 岁后不需要 '3 段 / 4 段' 奶粉",
        "母乳继续 + 家庭饮食 + 全奶(若需)= 足够",
        "'儿童奶' / '学步奶' = Code 禁的营销",
        "看包装'适合 6-12 月' / '适合 12 月+' → 警惕",
        "1 岁后省下奶粉钱 → 买高质量蛋白(肉/鱼/蛋)更值",
    ],
    "信'1 岁转 3 段奶粉''4 段儿童奶补钙'话术 → 多花钱 + 母乳被替代 + WHO Code 营销陷阱。\n"
    "WHO 立场:1 岁+ 不需要专门奶粉。",
    "B",
    ["G-TERM-WHO-Code", "G-TERM-formula-marketing", "G-TERM-breastmilk-substitutes"],
    ["C-S1-1010", "C-S5-1040", "C-S6-1067"],
    "WHO Code + WHO 2016 Follow-on/Growing-up Milk Resolution",
    "WHO Code 涵盖跟随/增长奶 + 中国 1 岁+ 营销陷阱",
    URL_CODE))

# ============================================================
# S7 24-36 月(起 1099) — 3 张
# ============================================================

cards.append(("C-S7-1099", "S7",
    "2 岁是底线不是上限",
    "WHO 写'beyond'是关键",
    "WHO verbatim:'continuing to breastfeed for up to 2 years of age or beyond.'\n"
    "'or beyond' 三个字关键 — 2 岁不是上限,是底线。\n"
    "现实:\n"
    "- 全球母乳中位停止时间(自然离乳)≈ 2.5-7 岁(人类生物学基线,Detwyler 2004)\n"
    "- 北欧 / 部分非洲 / 部分亚洲社会:2-4 岁普遍\n"
    "- 中国/西方都市:多 1-2 岁断 — 文化压力,不是生物学需要\n"
    "继续 2 岁后母乳:\n"
    "- 仍有营养 + 免疫保护(浓度持续高)\n"
    "- 心理慰藉(分离焦虑期)\n"
    "- 母乳哺育期长 → 妈妈乳腺癌降险线性增加",
    [
        "WHO 2 岁是底线不是上限('or beyond')",
        "人类生物学自然离乳 2.5-7 岁",
        "北欧 / 非洲 / 部分亚洲:2-4 岁普遍",
        "继续喂 = 国际正常,中国都市偏短",
        "妈妈乳腺癌降险跟哺乳期长线性相关",
    ],
    "认为 '2 岁后还喂太久' → 是文化偏见,不是生物学/医学根据。\n"
    "WHO 'or beyond' 是大方留白。",
    "B",
    ["G-TERM-WHO-two-years"],
    ["C-S6-1064", "C-S6-1065", "C-S7-1100"],
    "WHO 2 Years 'or Beyond' + Detwyler 2004 Natural Weaning",
    "WHO 'or beyond' 不设上限 + 人类生物学 2.5-7 岁自然离乳",
    URL_BF))

cards.append(("C-S7-1100", "S7",
    "自然离乳 vs 主动断奶",
    "等娃自己说不要",
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
        "妈妈用乳头涂辣椒 / 黄连 → 不推(伤娃心理)",
    ],
    "突然断奶或 '送奶奶家断' → 妈妈乳腺炎 / 娃心理冲击 / 妈妈情绪激素紊乱。\n"
    "WHO 立场:自然或渐进,不强行。",
    "A",
    ["G-TERM-WHO-two-years"],
    ["C-S7-1099", "C-S6-1064"],
    "WHO Weaning Approach (自然 vs 主动)",
    "WHO 默认自然离乳 + 渐进 vs 突然断奶风险",
    URL_QA))

cards.append(("C-S7-1101", "S7",
    "12-36 月跟随家庭饮食",
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
    URL_CF))

# ============================================================
# S8 3-6 岁(起 868) — 1 张
# ============================================================

cards.append(("C-S8-868", "S8",
    "学龄前奶:全奶或母乳",
    "不必专门 4 段奶",
    "WHO 立场:2-6 岁喂奶 — 母乳(若仍喂)或普通全奶/低脂奶足够。\n"
    "不需要任何 'children's formula' / 'growing-up milk' / '4 段儿童奶' — 这些是 WHO Code 禁营销对象。\n"
    "学龄前奶量:\n"
    "- 2-3 岁:全奶(whole milk)~250 ml/天 — 蛋白 + 钙\n"
    "- 4-6 岁:可低脂奶(2%)~250 ml/天\n"
    "中国通病:学龄前喝 '4 段儿童奶' / '学生奶' / '高钙奶' → 多数加糖加香精。",
    [
        "2-6 岁:全奶或母乳,不需要专门奶粉",
        "2-3 岁:全奶 ~250 ml/天",
        "4-6 岁:低脂或全奶都可",
        "'4 段儿童奶' / '高钙奶' → 营销话术",
        "正餐多样化 + 普通奶 = 足够",
    ],
    "信'4 段儿童奶补钙益智' → 多花钱 + 加糖加香精负担。\n"
    "WHO 立场:学龄前普通奶足够。",
    "B",
    ["G-TERM-formula-marketing"],
    ["C-S6-1070", "C-S6-1064"],
    "WHO Pre-school Nutrition + Code on Growing-up Milk",
    "WHO 2-6 岁全奶或母乳 + 不需要专门奶粉",
    URL_CODE))

# === 输出所有卡 ===
print(f"Total cards to write: {len(cards)}")

written = 0
for card_data in cards:
    card_id, seg, title, hook, why, wtd, fm, ev, refs, related, cit_title, cit_loc, cit_url = card_data
    yaml_text = card(card_id, seg, title, hook, why, wtd, fm, ev, refs, related, cit_title, cit_loc, cit_url)
    seg_dir = SEG_DIRS[seg]
    out_path = os.path.join(KB, "30-cards", seg_dir, f"{card_id}.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    written += 1

print(f"Written: {written} cards")
print(f"Phase 13 SRC-031 cards production: DONE")
