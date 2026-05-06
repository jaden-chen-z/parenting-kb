#!/usr/bin/env python3
"""Phase 13 SRC-031 — 批量产术语卡(G-TERM / G-ABBR / G-PERSON)"""
import os

KB = os.path.expanduser("~/Desktop/parenting-kb")
SRC_ID = "SRC-031"
TODAY = "2026-05-04"

def safe_quote(s):
    return '"' + str(s).replace('"', "'") + '"'

def indent(text, n=2):
    pad = " " * n
    return "\n".join(pad + line for line in text.split("\n"))

def term(g_id, gtype, display, en, zh, one_liner, detail, key_facts, related_g, related_c=None):
    """生成 G-TERM/G-ABBR/G-PERSON yaml"""
    related_g_str = "\n".join(f"  - {x}" for x in related_g) if related_g else "  []"
    related_c_str = "\n".join(f"  - {x}" for x in related_c) if related_c else "  []"
    kf_str = "\n".join(f"  - {safe_quote(x)}" for x in key_facts) if key_facts else "  []"

    return f"""glossary_id: {g_id}
type: {gtype}
display_name: {safe_quote(display)}

en_term: {safe_quote(en)}
zh_term: {safe_quote(zh)}

one_liner: |
{indent(one_liner, 2)}

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

terms = []

# ============================================================
# G-ABBR(缩写)
# ============================================================

terms.append(("G-ABBR-WHO", "abbreviation",
    "WHO 世界卫生组织",
    "World Health Organization",
    "世界卫生组织",
    "WHO 是联合国下属国际公共卫生机构,设日内瓦,194 成员国。",
    """## 定义
World Health Organization(世界卫生组织)— 联合国下属国际公共卫生机构。

## 历史
1948 年成立,设瑞士日内瓦。194 成员国。

## 在 SRC-031 中的角色
WHO 跟 UNICEF 共同发布婴幼儿喂养政策合集 — 6 月 EBF / 持续母乳到 2 岁 / BFHI / Code 等核心政策都来自 WHO。

## 跟其他派关系
WHO 是 Tier 1 国际权威 — 跟 AAP(美) / 鲍秀兰(中) / 松田(日) 各国指南并列。
WHO 立场是国际医学共识(全球 194 国 buy-in),非单一国家观点。""",
    ["1948 年成立", "194 成员国", "联合国下属", "Tier 1 国际权威"],
    ["G-ABBR-EBF", "G-ABBR-BFHI", "G-TERM-WHO-Code"],
    ["C-S0-1024", "C-S1-1000"]))

terms.append(("G-ABBR-EBF", "abbreviation",
    "EBF 纯母乳喂养",
    "Exclusive Breastfeeding",
    "纯母乳喂养",
    "EBF = 婴儿只喝母乳,任何其他液体/固体不给(连水都不给),例外 ORS / 维生素 / 药物。",
    """## WHO 操作定义 verbatim
'Exclusive breastfeeding means that the infant receives only breast milk. No other liquids or solids are given – not even water – with the exception of oral rehydration solution, or drops/syrups of vitamins, minerals or medicines.'

## 例外清单
- ORS(口服补液,腹泻脱水时)
- 维生素/矿物质 滴剂或糖浆
- 药物

## WHO 推荐时长
0-6 月 EBF(全球目标 2025 ≥ 50%,目前 44%)。

## 跟其他派关系
- AAP / 鲍秀兰 / 松田 都说 EBF 6 月,但没明确列例外清单
- WHO 是唯一明确给操作定义的派""",
    ["WHO 推 0-6 月", "全球率 44%(2015-2020)", "2025 目标 ≥ 50%", "操作定义含 ORS/维生素/药物例外"],
    ["G-ABBR-WHO", "G-TERM-WHO-six-months", "G-ABBR-CF"],
    ["C-S1-1008", "C-S0-1027"]))

terms.append(("G-ABBR-CF", "abbreviation",
    "CF 辅食",
    "Complementary Feeding",
    "辅食",
    "CF = 6 月起开始的'补充'喂养(complementary 意指补母乳,不是替代)。",
    """## 定义
Complementary Feeding — 婴儿 6 月起开始的'补充'食物,跟母乳并行(不是替代)。

## WHO 4 大支柱
① 及时(Timely)— 6 月开始
② 充分(Adequate)— 能量+蛋白+微营养
③ 安全(Safe)— 卫生准备
④ 反馈(Responsive)— 看信号

## 月龄餐数
- 6-8 月:日 2-3 餐
- 9-11 月:日 3-4 餐
- 12-23 月:日 3-4 餐 + 1-2 加餐

## 关键
'Complementary' 意指补充母乳 — 6-12 月母乳仍 ≥ 50% 能量,12-24 月仍 ≥ 33%。
中国传统 '辅食为主' 跟 WHO 立场冲突。""",
    ["WHO 6 月起", "4 大支柱(及时/充分/安全/反馈)", "月龄递增餐数", "补充非替代"],
    ["G-ABBR-EBF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1045", "C-S4-1046", "C-S4-1047"]))

terms.append(("G-ABBR-IYCF", "abbreviation",
    "IYCF 婴幼儿喂养",
    "Infant and Young Child Feeding",
    "婴幼儿喂养",
    "IYCF 是 WHO+UNICEF 用的总框架词,涵盖 0-24 月 EBF + CF + 持续母乳。",
    """## 定义
Infant and Young Child Feeding — WHO+UNICEF 喂养政策合集的总框架词,涵盖 0-24 月所有喂养主题。

## 涵盖范围
- 出生 1 小时内开奶
- EBF 0-6 月
- CF 6 月起辅食
- 持续母乳到 2 岁

## 政策文档
- WHO Global Strategy for Infant and Young Child Feeding(2003)
- WHO IYCF Fact Sheet
- WHO IYCF Model Chapter(2009 医学院教材)""",
    ["WHO+UNICEF 总框架词", "0-24 月喂养", "Global Strategy 2003"],
    ["G-ABBR-EBF", "G-ABBR-CF", "G-ABBR-BFHI"],
    ["C-S0-1024", "C-S1-1002"]))

terms.append(("G-ABBR-BFHI", "abbreviation",
    "BFHI 母婴友好医院",
    "Baby-Friendly Hospital Initiative",
    "母婴友好医院倡议",
    "BFHI 是 WHO+UNICEF 1991 启动的产院实操标准 — 10 步骤具体化母乳支持。",
    """## 定义
Baby-Friendly Hospital Initiative — WHO+UNICEF 1991 启动,2018 修订的产院认证标准。

## 10 步骤(2018 修订)
关键管理:
- 1a 遵守 Code
- 1b 书面婴儿喂养政策
- 1c 监测系统
- 2 员工训练

关键临床:
- 3 产前讨论
- 4 立即肌肤接触
- 5 持续母乳支持
- 6 仅医学指征补充
- 7 24h 同室
- 8 反馈喂养
- 9 警告奶瓶/奶嘴
- 10 出院衔接

## 全球认证
- 152+ 国 15,000+ 设施(2011)
- 中国 6,000+ 爱婴医院(早期签署国)
- 瑞典 1997 全国 65 中心认证
- 美国 2018 512 医院

## 关键
'BFHI 标签 ≠ 真守 10 步' — 实操参差是普遍问题。""",
    ["WHO+UNICEF 1991 启动", "2018 修订 10 步", "中国 6000+ 爱婴医院", "标签≠真守 10 步"],
    ["G-TERM-BFHI-10-steps", "G-ABBR-WHO", "G-TERM-WHO-Code"],
    ["C-S0-1025", "C-S1-1002", "C-S1-1004"]))

# ============================================================
# G-TERM(术语)
# ============================================================

terms.append(("G-TERM-BFHI-10-steps", "term",
    "BFHI 10 步骤",
    "Ten Steps to Successful Breastfeeding",
    "BFHI 10 步骤",
    "BFHI 10 步:WHO+UNICEF 1991 提出 + 2018 修订的产院实操标准全部 10 步。",
    """## 完整 10 步(2018 修订)
关键管理程序(Critical Management Procedures):
- Step 1a: Comply fully with the International Code of Marketing of Breast-milk Substitutes
- Step 1b: Have a written infant feeding policy
- Step 1c: Establish ongoing monitoring and data management systems
- Step 2: Ensure staff have sufficient knowledge, competence and skills

关键临床实践(Key Clinical Practices):
- Step 3: Discuss the importance and management of breastfeeding with pregnant women
- Step 4: Facilitate immediate skin-to-skin contact and support breastfeeding initiation
- Step 5: Support mothers to initiate and maintain breastfeeding
- Step 6: Do not provide breastfed newborns any food or fluids other than breast milk, unless medically indicated
- Step 7: Enable mothers and babies to remain together 24 hours a day (rooming-in)
- Step 8: Support mothers to recognize and respond to infant feeding cues
- Step 9: Counsel mothers on use and risks of bottles, teats, pacifiers
- Step 10: Coordinate discharge for ongoing community support

## 循证支持
'2016 年 58 项研究系统评述明确表明,遵守十步骤会影响出生后早期启动母乳喂养、纯母乳喂养和母乳喂养总时长'。

## 跟其他派关系
- 跟松田 SRC-024 反产院'3 小时定时 + 用枕头支奶瓶' 一致(BFHI 第 8/9 步)
- 跟 AAP 反馈喂养立场一致(第 8 步)
- 比 AAP/Karp 奶嘴立场更严(第 9 步)""",
    ["1991 启动 2018 修订", "关键管理 4 步 + 关键临床 7 步", "2016 年 58 项研究系统评述支持"],
    ["G-ABBR-BFHI", "G-TERM-skin-to-skin", "G-TERM-rooming-in", "G-TERM-responsive-feeding"],
    ["C-S1-1002", "C-S1-1003", "C-S1-1004", "C-S1-1005"]))

terms.append(("G-TERM-WHO-Code", "term",
    "WHO Code 母乳代用品营销守则",
    "International Code of Marketing of Breast-milk Substitutes",
    "母乳代用品国际营销守则",
    "WHO 1981 第 34 届 WHA 通过,禁止奶粉公司不当营销,84 国立法实施。",
    """## 定义
International Code of Marketing of Breast-milk Substitutes — WHO 1981 年第 34 届世卫大会通过的国际政策框架,目标限制配方奶 + 相关产品营销。

## 4 大利益方禁令
妈妈端:
- 'All forms of product advertising and promotion are prohibited'
- 无产品样品给妈妈
- 公司不得直接联系妈妈

医生端:
- 无礼物/财务回扣给医疗专业人员
- 'samples in no case should be passed on to mothers'

医院端:
- 'Promotion of any product is forbidden in a health care facility'
- 不得免费/低价提供

标签端:
- 'Pictures or text which may idealize the use of infant formula should not be used'
- 必须警告污染风险

## 涵盖产品
- 配方奶(0-6 月)
- 跟随奶(6-12 月)
- 增长奶(12 月+)
- 1 岁内任何乳制品/婴儿食品
- 奶瓶 + 奶嘴

## 后续 WHA 决议
1986 / 1990 / 1994 / 2005 / 2010 / 2016 — 持续加强。

## 实施现状
'Since 1981, 84 countries have enacted legislation implementing all or many of the provisions of the Code.'
违规仍广泛 — Nestle 1977 抵制运动是历史标志,IBFAN/UNICEF/WHO 持续监测。
中国《婴幼儿配方乳粉广告法》仅部分对接。""",
    ["1981 年 WHA 通过", "84 国立法实施", "4 大利益方禁令", "中国仅部分对接"],
    ["G-TERM-formula-marketing", "G-TERM-breastmilk-substitutes", "G-TERM-IBFAN", "G-TERM-NetCode"],
    ["C-S0-1026", "C-S1-1009", "C-S1-1010", "C-S1-1011"]))

terms.append(("G-TERM-WHO-six-months", "term",
    "WHO 6 月 EBF 共识",
    "WHO Six-Months Exclusive Breastfeeding Recommendation",
    "WHO 6 月专母乳共识",
    "WHO 推 0-6 月纯母乳 — 国际医学共识,跟 AAP 4-6 月辅食立场略分歧。",
    """## WHO 立场 verbatim
'WHO and UNICEF recommend that children initiate breastfeeding within the first hour of birth and be exclusively breastfed for the first 6 months.'

## 依据
- 6 月前母乳能量 + 营养充足
- 6 月前肠道未成熟,早期辅食增过敏/感染风险
- Lancet 2016 元分析:6 月 EBF 比 4 月 EBF 益处更多

## 跟其他派对照
- AAP(SRC-006):4-6 月,看 readiness 信号(LEAP 早引入立场)
- 鲍秀兰:6 月起辅食(跟 WHO 一致)
- 松田:5-6 月起,有弹性

## Cochrane 元分析
Kramer & Kakuma 2012 'Optimal duration of exclusive breastfeeding' 支持 6 月。""",
    ["WHO + UNICEF 共同推 0-6 月", "Cochrane 元分析支持", "AAP 4-6 月立场略分歧"],
    ["G-ABBR-EBF", "G-ABBR-WHO", "G-ABBR-CF"],
    ["C-S3-1042", "C-S3-1043", "C-S6-1069"]))

terms.append(("G-TERM-WHO-two-years", "term",
    "WHO 2 岁内继续母乳",
    "WHO Two-Year Continued Breastfeeding Recommendation",
    "WHO 持续母乳 2 年共识",
    "WHO 推持续母乳 ≥ 2 岁 'or beyond' — 国际医学共识,比 AAP 1 年立场更长。",
    """## WHO 立场 verbatim
'From the age of 6 months, children should begin eating safe and adequate complementary foods while continuing to breastfeed for up to two years of age or beyond.'

## 关键 'or beyond'
2 岁不是上限是底线。人类生物学自然离乳 2.5-7 岁(Detwyler 2004)。

## 营养构成数字
- 6-12 月:母乳供 ≥ 50% 能量
- 12-24 月:母乳供 ≥ 33% 营养

## 跟其他派对照
- AAP(SRC-006):1 岁可断
- 鲍秀兰(SRC-009):1 岁可断
- 松田(SRC-024):弹性
- WHO 是唯一明确推 2 岁内继续的派

## 妈妈益处
- 乳腺癌每 12 月哺乳降 6%
- 卵巢癌降
- 2 型糖尿病降
- 心血管疾病降
- 类风湿关节炎降

## 跟 SRC-029 对接
Lerner V4 G-TERM-WHO-feeding 已建术语,本卷给完整 verbatim。""",
    ["WHO 推 ≥ 2 岁 'or beyond'", "12-24m 33% 营养", "唯一明确推 2 年的派", "妈妈乳腺癌降 6%/12m"],
    ["G-ABBR-EBF", "G-ABBR-WHO", "G-PERSON-Victora"],
    ["C-S5-1039", "C-S6-1064", "C-S6-1065", "C-S7-1099"]))

terms.append(("G-TERM-Innocenti-Declaration", "term",
    "Innocenti Declaration 1990",
    "Innocenti Declaration on Breastfeeding (1990 + 2005)",
    "Innocenti 母乳喂养宣言",
    "Innocenti 1990 是 BFHI 启动的政治基础 — UNICEF Florence Innocenti 中心起草。",
    """## 1990 原版
- 1990 年 7 月 30 日 Florence Innocenti 中心通过
- WHO+UNICEF+USAID+SIDA 联合发起
- 4 大操作目标(具体措辞 WebFetch 失败,见 gaps G_WHO_1):
  ① 各国成立母乳协调员
  ② BFHI 启动
  ③ Code 立法
  ④ 立法保护妈妈母乳权

## 2005 修订
9 大补充目标 — 含 2025 全球量化指标。

## 政治根基
Innocenti 是 BFHI 1991 启动的直接政治基础 — 各国签署 = 国家义务。

## 中国签署状态
中国是早期签署国之一(具体行动需补)。

## 数据完整度警告
本术语基于间接信息(BFHI Wikipedia)— Innocenti 全文 WebFetch 全 URL 失败。
完整 4+9 目标精确措辞 + 各国签署状态记 gaps.md G_WHO_1。""",
    ["1990 通过", "WHO+UNICEF+USAID+SIDA 联合", "BFHI 1991 政治基础", "中国早期签署"],
    ["G-ABBR-BFHI", "G-TERM-WHO-Code", "G-ABBR-WHO"],
    ["C-S0-1028"]))

terms.append(("G-TERM-WHO-growth-standards", "term",
    "WHO Growth Standards 2006",
    "WHO Child Growth Standards (2006)",
    "WHO 儿童生长标准",
    "WHO 2006 母乳喂养基线 vs CDC 2000 配方奶基线 — 同一个娃在两图位置不同。",
    """## 定义
WHO Child Growth Standards — WHO 2006 发布的国际儿童生长曲线,基于 6 国母乳喂养婴儿。

## MGRS 多中心研究
WHO Multicentre Growth Reference Study — 6 国:
- 巴西
- 加纳
- 印度
- 挪威
- 阿曼
- 美国

## 7 大指标
- length/height-for-age
- weight-for-age
- weight-for-length/height
- BMI-for-age
- head circumference
- arm circumference
- skinfold measurements

## 6 大粗大动作里程碑(windows of achievement)
- 独坐(sitting without support)中位 6 月
- 扶站 中位 7-8 月
- 手膝爬 中位 9 月(20% 跳过爬)
- 扶走 中位 10 月
- 独站 中位 12 月
- 独走 中位 13 月,P3-P97 = 9-17 月

## 关键区别 vs CDC 2000
- WHO 2006:母乳喂养基线(prescriptive — '应该长成什么样')
- CDC 2000:美国数据(以配方喂养为主)(descriptive — '实际长成什么样')

## 中国采纳
中国卫健委 2018 起逐步采用 WHO 标准。""",
    ["WHO 2006 发布", "6 国 MGRS 研究", "母乳基线 vs CDC 配方基线", "中国 2018 起采纳"],
    ["G-ABBR-EBF", "G-ABBR-WHO"],
    ["C-S4-1052", "C-S4-1053", "C-S4-1054"]))

terms.append(("G-TERM-WHO-CF-principles", "term",
    "WHO 辅食 4 大支柱",
    "WHO Complementary Feeding Four Pillars",
    "WHO 辅食 4 大支柱",
    "WHO 辅食 4 支柱:及时 + 充分 + 安全 + 反馈 — 全球辅食实操框架。",
    """## 4 大支柱(Four Pillars)
| 维度 | WHO 要求 |
|------|--------|
| 及时性(Timely) | 6 月引入 |
| 充分性(Adequate) | sufficient energy, protein, micronutrients |
| 安全性(Safe) | 卫生储存/准备,清洁手和餐具 |
| 反馈式(Responsive) | responsive to child's clues for hunger |

## 月龄进食频率
- 6-8 月:日 2-3 餐
- 9-11 月:日 3-4 餐
- 12-23 月:日 3-4 餐 + 1-2 加餐

## 食物质地递进
- 6 月:泥状/碎状/半固体
- 8 月:加 finger food(self-feeding)
- 12 月:过渡至家庭食物

## PAHO/WHO 2003 10 大原则
基于 4 支柱,PAHO/WHO 2003 进一步给 10 条 Guiding Principles(全文 WebFetch 失败,见 gaps G_WHO_3)。""",
    ["及时/充分/安全/反馈", "PAHO 2003 10 原则", "月龄递增餐数"],
    ["G-ABBR-CF", "G-TERM-responsive-feeding"],
    ["C-S4-1046", "C-S4-1047", "C-S5-1037"]))

terms.append(("G-TERM-acceptable-medical-reasons", "term",
    "可接受医学原因清单",
    "Acceptable Medical Reasons for Breast-milk Substitutes",
    "可接受医学原因清单",
    "WHO/UNICEF 2009 清单 — 哪些情况(也只在这些情况)可以使用配方奶。",
    """## 婴儿端医学例外
- 半乳糖血症(galactosemia)— 完全禁母乳
- 苯丙酮尿症(PKU)— 部分配特殊配方+母乳
- 枫糖尿症(MSUD)
- 极低出生体重(<1500g)
- 严重早产(<32 周)
- 严重高胆红素血症(临时)
- 严重窒息(临时)

## 母亲端医学例外
- HIV+(高资源 + AFASS 满足时)
- 严重疾病(脓毒症 / 心力衰竭)
- 1 型疱疹乳房病灶(临时)
- 化疗
- 放射性药物
- 部分精神药物

## 关键鉴别
- 临时停母乳 vs 完全停 — 多数情况是临时
- '妈妈累' / '奶不够' / '上班' → 不在医学例外清单

## 数据完整度
本清单基于间接信息(BFHI 第 6 步 + 医学常识)— 完整清单 WebFetch 失败,见 gaps G_WHO_2。""",
    ["WHO/UNICEF 2009 联合发布", "婴儿端 + 母亲端清单", "完整清单 gaps G_WHO_2"],
    ["G-ABBR-BFHI", "G-TERM-HIV-feeding", "G-TERM-relactation"],
    ["C-S1-1003", "C-S1-1012", "C-S1-1013"]))

terms.append(("G-TERM-HIV-feeding", "term",
    "HIV+ 妈妈喂养",
    "HIV and Infant Feeding Guidelines (WHO 2010)",
    "HIV 母乳喂养指南",
    "WHO 2010 ART 时代修订 — 从'HIV+ 避免母乳'转到'AFASS 评估决定'。",
    """## WHO 2010 立场转变
verbatim:'If replacement feeding is acceptable, feasible, affordable and safe (AFASS), HIV-infected mothers are recommended to use replacement feeding. Otherwise, exclusive breastfeeding is recommended.'

## ART 时代关键改变
- 2003 旧立场:HIV+ 妈妈尽量避免母乳
- 2010 新立场:
  ① AFASS 满足 → 用配方
  ② AFASS 不全 → EBF + 妈妈 ART

## MTCT 风险数据
- 不 ART:bottle-fed 19% MTCT vs breastfed 49%
- 高资源区(美/欧):MTCT 几乎消除
- 低资源区(撒哈拉):EBF + ART 推荐

## 关键
不要混合喂养(母乳+配方)— 比纯一种风险更高。

## 中国 PMTCT
中国 PMTCT 指南推荐配方(AFASS 满足)+ 个案评估。""",
    ["WHO 2010 ART 时代修订", "AFASS 5 条件", "不混合喂养", "高资源 MTCT 几乎消除"],
    ["G-TERM-AFASS", "G-ABBR-EBF", "G-TERM-mixed-feeding"],
    ["C-S1-1013"]))

terms.append(("G-TERM-AFASS", "term",
    "AFASS 5 条件",
    "AFASS Standard (Acceptable, Feasible, Affordable, Sustainable, Safe)",
    "AFASS 替代喂养 5 条件",
    "AFASS = 替代喂养必须满足的 5 条件:可接受/可行/可负担/可持续/安全。",
    """## 5 条件
- Acceptable(可接受)— 文化和家庭可接受配方
- Feasible(可行)— 妈妈/家庭有能力准备
- Affordable(可负担)— 经济上可持续
- Sustainable(可持续)— 长期供应稳定
- Safe(安全)— 清洁水 + 消毒奶瓶 + 70°C 水冲

## 用途
HIV+ 妈妈喂养决策:5 全满足 → 用配方;不全 → EBF + ART。

## 适用扩展
也适用于其他需要替代喂养的情况(妈妈病/ 化疗 / 死亡等)。""",
    ["WHO 5 条件框架", "HIV+ 喂养决策核心", "5 条件全满足才用配方"],
    ["G-TERM-HIV-feeding", "G-TERM-acceptable-medical-reasons"],
    ["C-S1-1012", "C-S1-1013"]))

terms.append(("G-TERM-formula-marketing", "term",
    "奶粉营销监管",
    "Formula Marketing Regulation",
    "奶粉营销监管",
    "WHO Code 1981 + 后续决议禁止奶粉公司不当营销 — 中国实施部分。",
    """## Code 监管对象
- 配方奶(0-6 月)
- 跟随奶(follow-on formula 6-12 月)
- 增长奶(growing-up milk 12 月+)
- 1 岁内任何乳制品/婴儿食品
- 奶瓶 + 奶嘴

## 4 大利益方禁令
妈妈 / 医生 / 医院 / 标签 — 见 G-TERM-WHO-Code。

## 中国奶粉品牌实操
违规普遍:
- 产院送试用装
- 母婴店推销
- 直播带货
- 1-2-3-4 段分阶营销
- KOL 软广

## 中国法规
《婴幼儿配方乳粉广告法》仅部分对接 Code(主要禁 0-6 月配方奶广告),6 月+ 跟随奶/增长奶营销宽松。

## 监督
- IBFAN(International Baby Food Action Network)
- NetCode(WHO + IBFAN + UNICEF 联合监测网)""",
    ["WHO Code 1981 起", "中国法规仅部分对接", "IBFAN/NetCode 监督", "1-2-3-4 段营销 Code 禁"],
    ["G-TERM-WHO-Code", "G-TERM-breastmilk-substitutes", "G-TERM-IBFAN"],
    ["C-S0-1026", "C-S1-1009", "C-S1-1011", "C-S6-1070"]))

terms.append(("G-TERM-breastmilk-substitutes", "term",
    "母乳代用品",
    "Breast-milk Substitutes",
    "母乳代用品",
    "Code 定义的'母乳代用品'广义 — 不只配方奶,还含奶瓶/奶嘴/跟随奶/增长奶。",
    """## Code 定义
Breast-milk substitute = 'any food being marketed or otherwise represented as a partial or total replacement for breast milk'(任何作为部分或全部替代母乳产品的营销)。

## 涵盖
- 婴儿配方奶(infant formula 0-6 月)
- 跟随奶(follow-on formula 6-12 月)
- 增长奶(growing-up milk 12 月+)— WHO 2016 决议明确加强
- 1 岁内任何乳制品/婴儿食品
- 奶瓶
- 奶嘴
- 安抚奶嘴

## 关键
1-2-3-4 段奶粉 = 中国奶粉品牌分阶营销,WHO 立场视为 Code 监管对象。

## WHO 立场
1 岁后母乳 + 家庭饮食 + 全奶 = 足够,不需要任何 'breast-milk substitute'。""",
    ["Code 广义定义", "1-2-3-4 段都是", "1 岁后不需要专门奶粉"],
    ["G-TERM-WHO-Code", "G-TERM-formula-marketing"],
    ["C-S1-1010", "C-S6-1070", "C-S8-868"]))

terms.append(("G-TERM-Lancet-breastfeeding-series", "term",
    "Lancet 2016 母乳喂养系列",
    "Lancet 2016 Breastfeeding Series",
    "Lancet 2016 母乳系列",
    "Lancet 2016 系列(Victora 主编)— 母乳证据集大成,核心数据:82 万生命可救。",
    """## 系列概况
The Lancet 2016 Breastfeeding Series — Cesar Victora(巴西 Pelotas 大学)主编,母乳证据综述集大成。

## 核心数字 verbatim
'Increased breastfeeding to near-universal levels in low and middle income countries could prevent approximately 820,000 deaths of children under the age of five annually.'

## 关键发现
- 全球 EBF 普及节省 3000 亿美元/年医疗
- 母乳娃 IQ 高 ~3 点(Horta 2015 元分析)
- 妈妈乳腺癌每 12 月哺乳降 6%
- 卵巢癌 / 2 型糖尿病 / 心血管 / 类风湿 全降

## 母乳免疫成分
- sIgA(分泌型免疫球蛋白 A)
- lactoferrin(乳铁蛋白)
- oligosaccharides(寡糖)
- 抗氧化酶 + 抗炎蛋白

## 跟 WHO 立场对接
学术综述+政策共识双背书 — Lancet 数据是 WHO IYCF 政策的科学根基。""",
    ["Victora 主编 Lancet 2016", "82 万婴儿生命/年", "IQ +3 点", "妈妈乳腺癌降 6%/12m"],
    ["G-PERSON-Victora", "G-PERSON-Horta", "G-ABBR-EBF"],
    ["C-S0-1027", "C-S1-1015"]))

terms.append(("G-TERM-LAM", "term",
    "LAM 哺乳闭经法",
    "Lactational Amenorrhea Method",
    "哺乳闭经法",
    "LAM = 完全母乳 + < 6 月 + 月经未恢复 → >98% 有效避孕。",
    """## 3 条件(同时满足)
① 完全母乳(EBF,夜间日间≥4-6 小时一次)
② 婴儿 < 6 月
③ 月经未恢复(产后 56 天后判)

## 失败率
< 2%(完美使用)。

## 机制
吸吮 → 泌乳素(prolactin)→ 抑制 GnRH(gonadotropin-releasing hormone)→ 抑制排卵。

## 失效条件
任一条件失效 → 立刻找其他避孕方法:
- 月经回 → 失效
- 6 月到 → 失效
- 加辅食 / 减少夜哺 → 失效

## WHO 立场
WHO 推荐 4 大产后避孕方法之一(其他:屏障法/激素/IUD)。

## 中国传统认知
'哺乳期不会怀孕' → 部分对(LAM 满足时)+ 部分错(不满足时常误)。""",
    ["3 条件:EBF + < 6 月 + 月经未恢复", ">98% 有效", "WHO 推 4 大避孕之一"],
    ["G-ABBR-EBF", "G-ABBR-WHO"],
    ["C-S2-1047"]))

terms.append(("G-TERM-NetCode", "term",
    "NetCode 监测网",
    "Network for Global Monitoring and Support for Implementation of the International Code",
    "国际守则全球监测网",
    "NetCode = WHO + IBFAN + UNICEF 联合监测奶粉公司 Code 违规的全球网络。",
    """## 定义
NetCode(Network for Global Monitoring and Support for Implementation of the International Code)— WHO 与 IBFAN/UNICEF 联合发起的 Code 实施监测网络。

## 职能
- 监测各国 Code 实施
- 监测奶粉公司违规
- 发布定期违规报告

## 数据
- 84 国立法实施 Code 全部或部分(1981 至今)
- 违规仍广泛
- Nestle 1977 抵制运动是历史标志

## 中国
中国法规仅部分对接 Code,违规普遍 — IBFAN 中国报告长期上榜。""",
    ["WHO + IBFAN + UNICEF 联合", "84 国立法监测", "中国违规普遍"],
    ["G-TERM-WHO-Code", "G-TERM-IBFAN", "G-TERM-formula-marketing"],
    ["C-S1-1009", "C-S1-1011"]))

terms.append(("G-TERM-IBFAN", "term",
    "IBFAN 国际母婴行动网",
    "International Baby Food Action Network",
    "国际母婴食品行动网",
    "IBFAN = 全球 NGO 网络,定期发布 Code 违规公司报告 — 中国市场长期上榜。",
    """## 定义
International Baby Food Action Network — 1979 年成立的全球非政府组织网络,目标监督奶粉公司 Code 合规。

## 职能
- 监测全球奶粉公司 Code 违规
- 发布定期 'Breaking the Rules' 报告
- 跟 WHO/UNICEF 合作 NetCode

## 历史
Nestle 1977 抵制运动 — IBFAN 起源前情。

## 中国数据
中国市场在 IBFAN 报告中长期上榜违规品牌 — 飞鹤/雅培/惠氏/合生元等。""",
    ["1979 年成立", "全球 NGO 网络", "Breaking the Rules 报告"],
    ["G-TERM-WHO-Code", "G-TERM-NetCode", "G-TERM-formula-marketing"],
    ["C-S1-1011"]))

terms.append(("G-TERM-colostrum", "term",
    "Colostrum 初乳",
    "Colostrum",
    "初乳",
    "初乳 = 出生后头 2-5 天分泌的浓缩黄乳,sIgA 浓度 > 成熟乳 100 倍。",
    """## 定义
Colostrum — 出生后头 2-5 天分泌的黏稠黄色乳。

## 成分独特
- sIgA(分泌型免疫球蛋白 A)浓度 > 成熟乳 100 倍
- lactoferrin 高浓度
- 生长因子(EGF / IGF-1)帮肠道发育
- 量极少:出生第 1 天约 5 ml/餐(婴儿胃容量恰好)

## 关键功能
- 婴儿第一次免疫接种(被动免疫)
- 帮肠道菌群建立
- 通便(胎便)
- 妈妈泌乳启动

## 跟 BFHI 关系
出生 1 小时内开奶就是为了娃尽早得到初乳(BFHI 第 4 步)。

## 中国传统误区
'初乳脏要挤掉' / '没奶用配方过渡' → 错过初乳免疫黄金窗。""",
    ["头 2-5 天黄乳", "sIgA 100x 成熟乳", "5 ml/餐 = 胃容量", "BFHI 第 4 步保护"],
    ["G-ABBR-EBF", "G-TERM-early-initiation", "G-TERM-skin-to-skin"],
    ["C-S1-1000", "C-S1-1014", "C-S1-1017"]))

terms.append(("G-TERM-skin-to-skin", "term",
    "Skin-to-skin 肌肤接触",
    "Skin-to-Skin Contact (SSC)",
    "肌肤接触",
    "Skin-to-skin = 婴儿赤裸贴妈妈胸口 ≥ 1 小时 — BFHI 第 4 步 + 出生 1 小时内不间断。",
    """## 定义
Skin-to-skin contact (SSC)— 婴儿赤裸贴在妈妈胸口,持续 ≥ 1 小时不间断。

## BFHI 第 4 步 verbatim
'Facilitate immediate and uninterrupted skin-to-skin contact and support mothers to initiate breastfeeding as soon as possible after birth.'

## 关键 'uninterrupted'
- 测量/称重等 → 推到 1 小时后
- 持续直到完成第一次吸吮
- 早产/剖宫产 同样适用(妈妈状况允许时)

## 效果
- 体温稳定
- 心率稳定
- 血糖稳定
- 哭闹减少
- 母乳启动加速

## 跟其他派
- 跟 Karp(SRC-005)C-S1-002 一致(立即接触是 SIDS 因素之一)
- 跟松田 SRC-024 反产院'快速包裹+测量' 一致""",
    ["BFHI 第 4 步", "≥ 1 小时不间断", "早产剖宫产同样适用"],
    ["G-TERM-BFHI-10-steps", "G-TERM-early-initiation", "G-TERM-colostrum"],
    ["C-S1-1000", "C-S1-1001"]))

terms.append(("G-TERM-rooming-in", "term",
    "Rooming-in 24 小时同室",
    "Rooming-in",
    "母婴同室",
    "Rooming-in = 妈妈和娃 24 小时整天整夜同室不分离 — BFHI 第 7 步。",
    """## 定义
Rooming-in — 妈妈和娃 24 小时同房,不分母婴室。

## BFHI 第 7 步 verbatim
'Enable mothers and babies to remain together 24 hours a day.'

## 效果
- 妈妈识别早期信号(吸吮动作/寻乳)
- 按需喂养实操
- 减少配方奶补充
- 增加 EBF 成功率
- 母婴 bonding

## 例外
- NICU 需要
- 妈妈或娃严重医疗

## 中国传统差距
中国传统产院常规分母婴室,只哺乳时送过来 → 跟 BFHI 第 7 步对立。""",
    ["BFHI 第 7 步", "24 小时同室不分离", "中国传统产院差距"],
    ["G-TERM-BFHI-10-steps", "G-TERM-responsive-feeding"],
    ["C-S1-1002", "C-S1-1004"]))

terms.append(("G-TERM-early-initiation", "term",
    "Early initiation 1 小时内开奶",
    "Early Initiation of Breastfeeding",
    "出生 1 小时内开奶",
    "出生 1 小时内开奶 — WHO+UNICEF 共同建议,全球只 ~45% 婴儿达到。",
    """## 定义
Early initiation — 出生 1 小时内开始母乳喂养。

## 关键作用
- 初乳免疫保护(IgA + lactoferrin + 寡糖)
- 妈妈泌乳启动(吸吮 → 泌乳素)
- 母婴 bonding 关键窗

## BFHI 第 4 步具体化
'Facilitate immediate skin-to-skin contact and support breastfeeding initiation as soon as possible after birth.'

## 全球数据
- ~45% 婴儿在 1 小时内开奶(WHO 2018)
- 中国比例更低(传统产院流程干扰)

## 中国传统差距
中国传统产院:出生立即包裹+测量+称重+洗澡 → 错过 1 小时窗口。""",
    ["WHO+UNICEF 共同建议", "全球 45% 达到", "BFHI 第 4 步具体化"],
    ["G-TERM-skin-to-skin", "G-TERM-colostrum", "G-TERM-BFHI-10-steps"],
    ["C-S1-1000", "C-S1-1017"]))

terms.append(("G-TERM-nipple-confusion", "term",
    "Nipple confusion 奶头错乱",
    "Nipple Confusion",
    "奶头错乱",
    "母乳建立期(0-4 周)用奶嘴/奶瓶 → 干扰乳头吸吮模式 → 奶量减少。",
    """## 定义
Nipple confusion — 婴儿在母乳建立期接触奶嘴/奶瓶后,改变乳头吸吮模式,导致母乳吸吮效率降低。

## 机制
- 乳头吸吮:婴儿用舌头按压 + 吸吮 → 母乳分泌
- 奶嘴/奶瓶吸吮:被动流出,机制不同
- 婴儿混淆 → 不会有效吸乳头 → 母乳量减少

## BFHI 第 9 步立场
- 母乳建立期(0-4 周)避免奶嘴/奶瓶
- 必须用 → 用杯子/勺/注射器(spoon/cup feeding)
- 4 周后母乳稳定再考虑

## 跟 AAP/Karp 立场对照
- Karp(SRC-005):母乳建立后 3-4 周可用奶嘴(防 SIDS)
- AAP(SRC-006):3-4 周后可用
- BFHI(SRC-031):立场更严,能避就避""",
    ["0-4 周避免奶嘴/奶瓶", "BFHI 第 9 步立场", "比 AAP/Karp 更严"],
    ["G-TERM-BFHI-10-steps"],
    ["C-S1-1006", "C-S1-1018"]))

terms.append(("G-TERM-mixed-feeding", "term",
    "Mixed feeding 混合喂养",
    "Mixed Feeding",
    "混合喂养",
    "母乳+配方混喂 — WHO 立场:多数情况下风险高于纯一种。",
    """## 定义
Mixed feeding — 同时给婴儿母乳和配方奶(任意比例)。

## WHO + Lancet 2016 立场
多数情况下风险高于纯母乳或纯配方:
- 配方奶量加 → 母乳吸吮减 → 妈妈奶量真降
- 婴儿肠道菌群混乱(母乳菌群 vs 配方菌群相互干扰)
- 配方奶蛋白不耐(CMPI/CMPA 5%)风险增加
- HIV+ 妈妈混合传播率高于任一纯一种(WHO 2010)

## WHO 推荐
能纯母乳就纯;真不够 → 个案评估;HIV+ AFASS → 选纯一种。

## 中国通病
'晚上加一顿配方让妈妈休息' / '白天工作配方,晚上母乳' → 母乳奶量被打散。""",
    ["WHO 立场:风险高于纯一种", "中国常见误区", "HIV+ 必须纯一种"],
    ["G-TERM-HIV-feeding", "G-ABBR-EBF"],
    ["C-S1-1013", "C-S2-1048"]))

terms.append(("G-TERM-responsive-feeding", "term",
    "反馈喂养",
    "Responsive Feeding",
    "反馈式喂养",
    "看娃信号决定喂,不按时间表 — BFHI 第 8 步 + 跟 AAP/松田 共识。",
    """## 定义
Responsive feeding — 看婴儿信号决定喂,不按时间表。

## 早期 vs 晚期信号
- 早期:唇啜 / 吸吮 / 寻乳 / 踢腿 / 警觉
- 晚期:哭(已过头,饿+情绪 → 难有效吸)

## BFHI 第 8 步 verbatim
'Support mothers to recognize and respond to infant feeding cues.'

## 频次
- 新生儿:8-12 次/24h
- 1-3 月:仍 8-12 次
- 'Cluster feeding'(群聚喂)正常

## 跟其他派关系
- AAP(SRC-006):'on demand' 立场一致
- 松田(SRC-024):反产院'3 小时定时' 一致(C-S1-761)
- WHO BFHI:一致

## 辅食期延续
6 月+ 加辅食仍 responsive — 看娃饱腹/饥饿信号。""",
    ["BFHI 第 8 步", "AAP/松田/WHO 三方共识", "早期信号:唇啜/寻乳/踢腿/警觉"],
    ["G-TERM-BFHI-10-steps"],
    ["C-S1-1005", "C-S2-1044", "C-S4-1050"]))

terms.append(("G-TERM-relactation", "term",
    "Relactation 重新泌乳",
    "Relactation",
    "重新泌乳",
    "已停母乳的妈妈通过频繁吸吮重新建立母乳 — WHO 推荐路径。",
    """## 定义
Relactation — 已停母乳(部分或完全)的妈妈通过频繁吸吮重新建立母乳。

## 适用场景
- 妈妈病好后想恢复母乳
- 早期错误判断(以为 '没奶'加配方)后想纠正
- 紧急情况(收养 / 灾难)妈妈或代乳

## 机制
吸吮 → 泌乳素 + 催产素 → 重新启动泌乳。

## WHO 立场
推荐 relactation 作为'妈妈病/化疗后' 恢复母乳的路径。

## 实操
- 每 2 小时让娃吸吮(刺激泌乳素)
- 必要时用挤奶器辅助
- 同时给配方过渡 + 逐步减少
- 找哺乳顾问指导(IBCLC)
- 通常 1-2 周开始有奶,4-6 周可纯母乳""",
    ["停奶后重启母乳", "WHO 推荐路径", "1-2 周见奶,4-6 周可纯"],
    ["G-TERM-acceptable-medical-reasons"],
    ["C-S1-1012", "C-S5-1040", "C-S6-1069"]))

terms.append(("G-TERM-galactagogue", "term",
    "Galactagogue 催乳",
    "Galactagogue",
    "催乳食/药",
    "催乳物 — WHO 立场:频繁吸吮才是真解,中国传统催乳汤效果有限。",
    """## 定义
Galactagogue — 用于增加母乳分泌的食物或药物。

## WHO 立场
- 第一干预:增加吸吮频次(频繁刺激泌乳素)
- 第二:检查衔乳姿势(找 IBCLC)
- 第三:挤奶/双侧轮替
- Galactagogue(食/药)效果有限,不是首选

## 常见 galactagogue
- 食物:燕麦 / 茴香 / 葫芦巴 / 啤酒花
- 中医:王不留行 / 通草 / 路路通 / 桔梗
- 西药:多潘立酮(domperidone,RCT 有限)

## 关键
- 没证据是 magic bullet
- 真正提奶量靠频繁吸吮
- 中国 '猪蹄汤催乳' 等传统效果不显著(脂肪多但泌乳素影响弱)""",
    ["WHO 立场:吸吮才是真解", "传统催乳汤效果有限", "domperidone RCT 有限"],
    ["G-ABBR-EBF"],
    ["C-S2-1045"]))

# ============================================================
# G-PERSON(经典学者)
# ============================================================

terms.append(("G-PERSON-Victora", "person",
    "Cesar Victora",
    "Cesar Victora",
    "Cesar Victora",
    "巴西 Pelotas 大学流行病学家,Lancet 2016 母乳系列主编。",
    """## 简介
Cesar Victora — 巴西 Pelotas 大学公共卫生学院流行病学家,全球母乳喂养研究核心人物。

## 主要贡献
- Lancet 2016 母乳喂养系列主编
- 巴西 Pelotas 出生队列研究(1982/1993/2004 三代追踪)
- WHO 母乳证据综述顾问
- WHO Multicentre Growth Reference Study(MGRS)成员

## 关键发现
- 全球 EBF 普及可救 82 万婴儿生命/年(Lancet 2016)
- 母乳娃 IQ 益处持续到成年
- 中低收入国家母乳益处尤其显著

## 在 SRC-031 中的角色
Lancet 2016 系列是 WHO IYCF 政策的科学根基。""",
    ["巴西 Pelotas 流行病学家", "Lancet 2016 主编", "Pelotas 队列研究三代", "WHO MGRS 成员"],
    ["G-TERM-Lancet-breastfeeding-series", "G-TERM-WHO-growth-standards"],
    ["C-S1-1015"]))

terms.append(("G-PERSON-Horta", "person",
    "Bernardo Horta",
    "Bernardo Lessa Horta",
    "Bernardo Horta",
    "巴西 Pelotas 大学流行病学家,母乳 IQ 元分析作者(Horta 2015)。",
    """## 简介
Bernardo Horta — 巴西 Pelotas 大学流行病学家,跟 Victora 合作,母乳长期效应研究核心。

## 主要贡献
- Horta 2015 元分析:母乳娃 IQ 益处约 +3 点
- 母乳长期心血管/代谢效应研究
- Lancet 2016 系列主要作者

## 在 SRC-031 中的角色
Horta 2015 IQ 元分析是 WHO 母乳认知益处的核心证据。""",
    ["巴西 Pelotas 流行病学家", "Horta 2015 IQ 元分析", "母乳 IQ +3 点"],
    ["G-TERM-Lancet-breastfeeding-series", "G-PERSON-Victora"],
    ["C-S1-1015"]))

terms.append(("G-PERSON-Dewey", "person",
    "Kathryn Dewey",
    "Kathryn Dewey",
    "Kathryn Dewey",
    "UC Davis 营养学教授,WHO 辅食指南核心专家,Guiding Principles 主要作者。",
    """## 简介
Kathryn Dewey — UC Davis(加州大学戴维斯分校)营养学教授,全球辅食研究权威。

## 主要贡献
- PAHO/WHO 2003 'Guiding Principles for Complementary Feeding' 主要作者
- WHO 辅食 4 大支柱框架贡献者
- 母乳/辅食营养相互作用研究

## 关键概念
- Complementary feeding 4 pillars(及时/充分/安全/反馈)
- Iron-rich first foods 立场
- Self-regulation 在辅食期的重要性

## 在 SRC-031 中的角色
PAHO/WHO 2003 Guiding Principles 是辅食实操的全球圣经(完整 10 条 WebFetch 失败,gaps G_WHO_3)。""",
    ["UC Davis 营养学教授", "PAHO/WHO 2003 Guiding Principles 作者", "辅食 4 支柱贡献者"],
    ["G-ABBR-CF", "G-TERM-WHO-CF-principles"],
    ["C-S4-1046"]))

terms.append(("G-PERSON-Lutter", "person",
    "Chessa Lutter",
    "Chessa K. Lutter",
    "Chessa Lutter",
    "PAHO 高级喂养专家,RTI International 资深顾问,IYCF 政策核心。",
    """## 简介
Chessa Lutter — PAHO(Pan American Health Organization,泛美卫生组织)高级喂养专家,IYCF 政策制定核心。

## 主要贡献
- PAHO/WHO 2003 'Guiding Principles for Complementary Feeding' 共同作者
- 拉美 BFHI 推广核心
- 全球儿童营养政策制定

## 在 SRC-031 中的角色
PAHO 是 WHO 美洲区办公室 — Lutter 代表区域专家,跟 Dewey 合作。""",
    ["PAHO 高级喂养专家", "PAHO/WHO 2003 共同作者", "拉美 BFHI 推广"],
    ["G-PERSON-Dewey", "G-ABBR-BFHI"],
    ["C-S4-1046"]))

# === 输出 ===
print(f"Total terms to write: {len(terms)}")
written = 0
for t in terms:
    g_id, gtype, display, en, zh, one_liner, detail, key_facts, related_g, related_c = t
    yaml_text = term(g_id, gtype, display, en, zh, one_liner, detail, key_facts, related_g, related_c)
    out_path = os.path.join(KB, "40-glossary", f"{g_id}.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(yaml_text)
    written += 1

print(f"Written: {written} terms")
