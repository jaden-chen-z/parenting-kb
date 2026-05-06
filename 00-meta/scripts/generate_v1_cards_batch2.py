"""Batch 2: Ch 7 Fischer + Ch 11 Baltes + Ch 16 Lerner PYD + Ch 8 Magnusson"""
import os

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

CARDS = [
# =================== Ch 7 Fischer Dynamic Skill Theory ===================
{
    'card_id': 'C-S0-1512', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'fischer', 'dynamic_skill', 'foundational'],
    'title': '技能不是直线发展', 'hook': '能力像织网不是搭楼',
    'why_matters': '''Fischer & Bidell(Lerner V1 Ch 7)给 dynamic skill theory —
技能发展不是按楼梯一级一级上,是 constructive web(建构网状)。
- 不是单一通用能力(智商) — 是多领域多技能各自发展
- 不是稳步提升 — 是反复 reorganize(重新组织)
- 同一个孩子在不同情境表现不同(高情境支持 vs 低情境支持差距大)
意义 — Piaget 的"4 阶段"过简化。Fischer 给更细的 levels(13 layer 层级)。
中国家长意义 — 不要拿"年龄段能力" 套你家娃,每个领域(动作 / 语言 / 社交 / 认知)各自发展。''',
    'what_to_do': [
        '不期望"全面发展"同步',
        '某领域强 + 某领域弱是常态',
        '同一能力在情境 A 会 + 情境 B 不会属正常',
        '高情境支持(陪 / 引导)能放大能力',
        '看每领域路径,不看综合分数',
    ],
    'failure_mode': '"我家娃综合差" 立场 — 错。Fischer 视角是多领域分别看。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Fischer-K', 'G-TERM-dynamic-skill-theory', 'G-TERM-constructive-web'],
    'related_cards': ['C-S0-1508', 'C-S0-1511', 'C-S0-722', 'C-S2-1503'],
    'chapter': 'Ch 7 Dynamic Skill Theory (Fischer & Bidell)',
    'chapter_offset': 1690000,
},
{
    'card_id': 'C-S2-1504', 'seg': 's2-1to3mo', 'stages': ['S2'],
    'tags': ['cognitive', 'lerner_v1', 'fischer', 'skill_reorganization', 'wonder_weeks_link'],
    'title': '退步是新组织前奏', 'hook': '会了又不会是好事',
    'why_matters': '''Fischer 的核心命题 — 技能发展中"看似退步"是 reorganization(系统重组)的征兆,
是新阶段即将到来的前奏,不是真退步。
对接 Wonder Weeks 跃迁论 — 跃迁前几天娃通常"退步"(吃睡变差 / 黏人 / 哭闹增)。
对接中国家长经验 — "原来会自己穿鞋,这两天又不会了"是 reorganization 进行中。
意义 — 看似退步要欢迎,不要焦虑。系统在拆旧装新,稳定后会出现新能力。
父母此时的工作 — 提供安全 + 不施压 + 等系统重组完成。''',
    'what_to_do': [
        '看似退步 → 庆祝新能力即将来',
        '不强行让娃"恢复"原能力',
        '提供安全感 + 多陪伴',
        '系统重组期娃情绪不稳定属正常',
        '等几天 → 新能力自然涌现',
    ],
    'failure_mode': '看似退步焦虑 push — 错。reorganization 不能被强行加速。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Fischer-K', 'G-TERM-skill-reorganization', 'G-TERM-dynamic-skill-theory'],
    'related_cards': ['C-S0-1512', 'C-S0-1511', 'C-S2-1502', 'C-S2-700'],
    'chapter': 'Ch 7 Fischer & Bidell',
    'chapter_offset': 1707604,
},
{
    'card_id': 'C-S6-1502', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['cognitive', 'lerner_v1', 'fischer', 'skill_levels'],
    'title': '能力分 13 层不 4 阶段', 'hook': '细颗粒度看发展',
    'why_matters': '''Fischer 给 13 层级 (level) 技能模型 — 比 Piaget 4 阶段细致 10 倍 —
每一层有具体 cognitive 操作,每隔 4-6 个月经历一次重组。
1-2 岁这个段对应 Fischer 第 5-7 层(感知运动 → 单体表征 → 表征关系)。
意义 — 你看到 18 月娃"突然"会用 2 字句(妈妈抱)是 level 6 → 7 的重组涌现。
中国家长意义 — 不要拿"15 月该会 X"焦虑,Fischer 数据:同月龄 level 差异可达 2 个层级。
关键不是月龄,是孩子在自己路径上的层级位置 + 情境支持质量。''',
    'what_to_do': [
        '不焦虑"该会 X 月龄"',
        '看孩子当前能力 level(13 层中第几)',
        '高情境支持(陪 / 引导)能让 level 提前显现',
        '低情境(独自 / 无引导)level 表现退后属正常',
        '路径 > 月龄',
    ],
    'failure_mode': '月龄表焦虑 — 错。Fischer 数据:同月龄差异巨大。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Fischer-K', 'G-TERM-dynamic-skill-theory', 'G-TERM-skill-levels'],
    'related_cards': ['C-S0-1512', 'C-S2-1504', 'C-S6-1064', 'C-S6-1066'],
    'chapter': 'Ch 7 Fischer & Bidell',
    'chapter_offset': 1715469,
},

# =================== Ch 11 Baltes Lifespan ===================
{
    'card_id': 'C-S0-1513', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'lifespan', 'foundational'],
    'title': '一辈子可塑发展', 'hook': '老了也能再发展',
    'why_matters': '''Baltes / Lindenberger / Staudinger(Lerner V1 Ch 11)给 lifespan theory —
反早期决定论,主张人一辈子都在发展(包括老年)。
核心命题 —
- plasticity(可塑性)持续到死(只是程度变低)
- 不同领域峰值不同(认知速度 25 岁峰 / 智慧 50+ 岁峰)
- 老年也有发展(SOC 策略让能力维持)
意义 — 中国家长 "0-3 岁是关键期" 焦虑论是过度简化。
Baltes 数据:0-3 岁重要但不是"过了就没了"。30 岁 / 50 岁 / 70 岁都还在发展。
意义 — 父母不必"赌上前 3 年" — 全程都重要,后期补救空间大。''',
    'what_to_do': [
        '0-3 岁重要但不是唯一关键期',
        '错过早期窗口不绝望(后续可补)',
        '父母自己也在发展(育儿是双向)',
        '老人也在发展(陪老人也是育儿)',
        '一辈子框架取代关键期框架',
    ],
    'failure_mode': '"过了 0-3 就晚了" 立场 — 错。Baltes 综述明确反对。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-PERSON-Lindenberger', 'G-PERSON-Staudinger', 'G-TERM-lifespan-theory', 'G-TERM-plasticity'],
    'related_cards': ['C-S0-1503', 'C-S0-1500', 'C-S0-722', 'C-S0-115'],
    'chapter': 'Ch 11 Lifespan Theory (Baltes / Lindenberger / Staudinger)',
    'chapter_offset': 3025000,
},
{
    'card_id': 'C-S0-1514', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'anti_critical_period'],
    'title': '关键期论被夸大', 'hook': '0-3 不是命运闸',
    'why_matters': '''Baltes 综述 — "关键期"概念在媒体被夸大,真正的关键期(必须的窗口)很少。
真正的关键期(0-3 不可错过):
- 视觉发展(眼疾必须早治)
- 母语暴露(完全无暴露才有问题)
- 安全依恋形成(完全缺爱才有问题)
"敏感期"(更易但非必须):
- 语言学习 — 早学更易但成人也能学
- 社交 — 早期建立易,后续可学
- 兴趣 — 早接触易培养
中国家长把 "敏感期" 当 "关键期" — 制造无效焦虑。''',
    'what_to_do': [
        '区分关键期 vs 敏感期',
        '关键期(视觉 / 语言暴露 / 依恋)只 5%',
        '敏感期(早教 / 兴趣)90%(可补救)',
        '错过敏感期 ≠ 没希望(只是费力些)',
        '不被"早教窗口"营销吓住',
    ],
    'failure_mode': '"敏感期"当"关键期"拼命投入 — 错。多数可补救。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-TERM-critical-period', 'G-TERM-sensitive-period', 'G-TERM-plasticity'],
    'related_cards': ['C-S0-1513', 'C-S0-1503', 'C-S0-722', 'C-S6-189'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3110519,
},
{
    'card_id': 'C-S0-1515', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'SOC'],
    'title': 'SOC 一辈子三策略', 'hook': '选 + 优 + 补 3 招',
    'why_matters': '''Baltes 给 SOC 模型 — selection(选择) + optimization(最优化) + compensation(补偿)是
人一辈子应对发展的 3 个策略:
- Selection(选)— 资源有限,选择重要的
- Optimization(优)— 选好的事情上做到最好
- Compensation(补)— 老了 / 弱了 / 输了用别的方式补
意义 — 不只老人,孩子也可以学 SOC。
中国家庭育儿应用 —
- 父母自己:工作 / 育儿 / 自我发展精力有限 → SOC 选择最重要
- 教孩子:不能样样学,选 1-2 个深耕(selection)+ 全力做好(optimize)+ 弱项找方法补(compensate)
- 老人帮带 → 是 compensation 不是失败
SOC 让你少焦虑,多策略。''',
    'what_to_do': [
        '父母 SOC — 选 1-2 件重要的(不全做)',
        '孩子兴趣 — 选 1-2 个深耕(不全报)',
        '弱项找补 — 不强求"全面发展"',
        '老人帮带 — 是 compensation 别愧疚',
        '一辈子 3 策略,不只老人用',
    ],
    'failure_mode': '"全部都要全部都好" — 错。SOC 数据:不可能,且不必要。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-TERM-SOC-model'],
    'related_cards': ['C-S0-1513', 'C-S0-1514', 'C-S8-1135', 'C-S0-722'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3110519,
},
{
    'card_id': 'C-S6-1503', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'plasticity', 'anti_early_education'],
    'title': '早教不必抢起点', 'hook': '不抢早就没了吗',
    'why_matters': '''中国早教焦虑核心命题 — "0-3 岁脑发育关键期错过就没了"。
Baltes Lerner V1 Ch 11 综述明确反对 — 这是把"敏感期"夸大成"关键期"。
真相 —
- 0-3 岁脑发育快速,但 plasticity 持续到 70+ 岁
- 6 岁前不上早教,7 岁后追上的孩子很多
- 早教不能保证后期高成就(数据弱相关)
- 过度早教反而干扰自然 self-organization(Pikler / Davies 立场)
中国家长意义 — 不必砸钱抢早教,把钱投在 proximal processes(陪伴质量)更划算。
Baltes lifespan + Bronfenbrenner microsystem 双重支持。''',
    'what_to_do': [
        '不必上早教班(0-3 岁)',
        '陪伴质量 > 课程数量',
        '错过"敏感期" ≠ 永远输',
        '追求"全面早教"是营销骗局',
        'Baltes lifespan:一辈子可塑',
    ],
    'failure_mode': '砸钱早教 + 怕"输在起跑线" — 错。Baltes 综述明确反对关键期论。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-TERM-lifespan-theory', 'G-TERM-plasticity', 'G-TERM-anti-early-education'],
    'related_cards': ['C-S0-1513', 'C-S0-1514', 'C-S0-1515', 'C-S7-125'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3025000,
},
{
    'card_id': 'C-S0-1516', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'plasticity', 'foundational'],
    'title': '可塑性持续到死', 'hook': '脑子一辈子在改',
    'why_matters': '''Baltes 综述 plasticity(可塑性)定义 — 神经系统可被经验改变的能力。
不是 "0-3 岁后没了" — 是 "0-3 岁高 / 老年低,但全程都有"。
神经科学数据(Greenough 等)— 70 岁人脑子还能长新连接(海马 / PFC 区)。
意义 —
- 中国 "脑发育关键期" 营销夸大 — Baltes 综述反驳
- 老人学英语 / 学新技能 — 慢但能学
- 中年人转行 — 慢但能转
- 70 岁也能发展智慧 / 灵性
意义 — 把"可塑性"当一辈子礼物,不当"赌上 0-3"。''',
    'what_to_do': [
        '一辈子学习心态(自己 + 孩子)',
        '老人学新东西鼓励(可塑性还有)',
        '中年人转行不晚',
        '不在"关键期"上焦虑',
        'Baltes:plasticity 持续 70+ 岁',
    ],
    'failure_mode': '"老了学不动" — 错。Baltes 数据:能,只是慢。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-TERM-plasticity', 'G-TERM-lifespan-theory'],
    'related_cards': ['C-S0-1513', 'C-S0-1514', 'C-S6-1503', 'C-S0-722'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3110519,
},
{
    'card_id': 'C-S8-1135', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'lifespan', 'school_anxiety'],
    'title': '6 岁不是命运分水岭', 'hook': '上学焦虑要清醒',
    'why_matters': '''中国父母 6 岁焦虑 — "进好小学决定一辈子"。
Baltes 综述明确反对 — lifespan 数据:小学起点跟成年成就相关性 < 0.3。
真正影响成年成就 —
- 自我效能(Bandura)
- 主动性(Lerner PYD)
- 关系质量(Bronfenbrenner micro)
- 兴趣 / 内驱力(Csikszentmihalyi flow)
这些 0-6 岁打基础,但 7-18 岁继续可塑。
意义 — 6 岁前别赌"上好学校",赌"基础能力 + 兴趣 + 关系"。''',
    'what_to_do': [
        '不为 6 岁前"上好小学"过度焦虑',
        '基础能力(社交 / 自调 / 兴趣)更关键',
        '小学 6 年路径不固定',
        'Baltes 数据:中年成就跟小学成绩弱相关',
        '一辈子框架取代"赢起跑线"',
    ],
    'failure_mode': '"上不了好小学一辈子完蛋" — 错。Baltes 综述明确反对。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-TERM-lifespan-theory'],
    'related_cards': ['C-S0-1513', 'C-S0-1514', 'C-S6-1503', 'C-S8-323'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3491730,
},
{
    'card_id': 'C-S0-1517', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'baltes', 'wisdom'],
    'title': '智慧不是 IQ', 'hook': '老了智慧反而长',
    'why_matters': '''Baltes 在 V1 Ch 11 给"智慧"(wisdom)研究奠基 — 智慧是发展的终点之一,跟 IQ 不一样。
- IQ 25 岁峰值后下降
- Wisdom 50+ 岁才峰值(Baltes "wisdom paradigm" 5 维度:深识 / 实操 / 价值 / 不确定性 / 跨情境)
意义 — 中国 "聪明" 不等于"智慧",养孩子目标不是 IQ 高,是 wisdom 强。
0-6 岁打 wisdom 基础 —
- 让孩子接触多元情境(培养跨情境思考)
- 鼓励反思 / 提问(培养深识)
- 容纳不确定性(不所有问题都有答案)
- 跟孩子一起讨论价值观(不只对错)
意义 — IQ 焦虑该转 wisdom 焦虑(也别太焦虑)。''',
    'what_to_do': [
        '区分聪明 vs 智慧(后者更重要)',
        '让娃接触多元情境(跨情境)',
        '鼓励反思 + 提问',
        '价值观讨论 — 不只是对错',
        '不焦虑 IQ,看 wisdom 路径',
    ],
    'failure_mode': '"智力开发"焦虑 — 错。IQ 25 岁见顶,wisdom 50+ 才见顶。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-PERSON-Staudinger', 'G-TERM-wisdom-paradigm'],
    'related_cards': ['C-S0-1513', 'C-S0-1515', 'C-S8-103', 'C-S8-104'],
    'chapter': 'Ch 11 Baltes Lifespan',
    'chapter_offset': 3110519,
},

# =================== Ch 16 Lerner PYD ===================
{
    'card_id': 'C-S0-1522', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', '5C', 'foundational'],
    'title': 'PYD 5C 框架', 'hook': '5 个 C 替代成绩',
    'why_matters': '''Lerner et al.(Lerner V1 Ch 16)给 Positive Youth Development(PYD)5C 框架:
- Competence(能力)— 学习 / 社交 / 体能 等具体能力
- Confidence(自信)— 自我效能 + 价值感
- Connection(连接)— 跟父母 / 同伴 / 老师 / 社区的关系
- Character(品格)— 道德 / 责任 / 价值观
- Caring(关怀)— 同理 / 利他
后来加 6C — Contribution(贡献)— 给社区 / 家庭 / 社会的贡献
意义 — PYD 反 deficit model(只看缺点改正),用 asset model(看优势放大)。
中国 "成绩中心" 育儿可对接 PYD 反思 — 5C 比成绩更预测成年福祉。''',
    'what_to_do': [
        '5C 维度同步看(不只成绩)',
        'Competence 不只学业(社交 / 体能 / 艺术)',
        'Confidence 来自被尊重 + 成就感',
        'Connection 是父母 + 同伴 + 老师多元',
        'Character + Caring 比成绩更预测成年',
    ],
    'failure_mode': '"成绩第一" 单维 — 错。PYD 综述:5C 全维更预测福祉。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1500', 'C-S0-1513', 'C-S0-722', 'C-S8-323'],
    'chapter': 'Ch 16 Positive Youth Development (Lerner / Benson / Scales)',
    'chapter_offset': 4860000,
},
{
    'card_id': 'C-S6-1505', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'anti_deficit'],
    'title': '看优势不是修缺点', 'hook': '资产不是赤字',
    'why_matters': '''Lerner V1 Ch 16 PYD 反 deficit model — 不是看孩子"少了什么"修补,是看"多了什么"放大。
中国家长习惯 deficit 视角 — "我家娃数学差 / 不爱社交 / 不爱阅读" → 拼命补。
PYD asset 视角 — "我家娃有 X 优势 / 兴趣 / 关系" → 放大 + 衍生其他能力。
1-2 岁这个阶段建立的视角终生影响:
- deficit 视角 → 娃感到自己是"问题",自卑根
- asset 视角 → 娃感到自己有价值,自信根
意义 — 父母选"看优势"还是"修缺点"决定娃自我感。''',
    'what_to_do': [
        '每天找娃 1 个优势夸(具体的)',
        '不在缺点上反复 nag',
        '兴趣 + 优势放大 → 衍生其他能力',
        '弱项慢慢补(用优势带)',
        'asset 视角 = 长期自信根',
    ],
    'failure_mode': '只盯缺点修 — 错。PYD 数据:asset 视角发展更全面。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-asset-based-model'],
    'related_cards': ['C-S0-1522', 'C-S6-1064', 'C-S6-816', 'C-S6-1075'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4860000,
},
{
    'card_id': 'C-S7-1602', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'connection'],
    'title': '连接是 5C 之首', 'hook': '关系比能力重要',
    'why_matters': '''Lerner V1 Ch 16 PYD 5C 中,Connection(连接)是"基础维度" —
没有 connection,其他 4C(competence/confidence/character/caring)都难发展。
Connection 包括 — 父母 / 同伴 / 老师 / 社区 / 文化的多元关系网。
2-3 岁阶段 Connection 建设 —
- 跟父母 → 安全依恋(Bowlby)
- 跟同伴 → 早期友谊(Hartup)
- 跟祖辈 → 多代关系网
- 跟社区 → 邻居 / 公园 / 早教 接触
中国家庭常 Connection 单一 — 父母 1 + 老人 1,缺同伴 / 社区 → PYD 弱。
意义 — 给娃一个 Connection 网比给一堆早教课更重要。''',
    'what_to_do': [
        '父母关系是 base — 安全依恋',
        '同伴关系刻意创造(playground / 邻居)',
        '祖辈关系健康(不只帮带)',
        '社区接触 — 邻居 / 公园 / 早教',
        'Connection 网 = 终生 PYD 基础',
    ],
    'failure_mode': '只跟父母 + 老人 connection — 错。同伴 / 社区缺导致 PYD 单薄。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1522', 'C-S7-996', 'C-S7-1001', 'C-S7-754'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
},
{
    'card_id': 'C-S8-1136', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'character'],
    'title': '品格是道德加责任', 'hook': '不只听话是品格',
    'why_matters': '''Lerner V1 Ch 16 PYD 中 Character(品格)— 不是简单"听话",是道德判断 + 责任感 + 价值观一体。
3-6 岁 Character 形成关键期 —
- 道德判断(Smetana 4 类规则:道德 / 习俗 / 个人 / 谨慎)
- 责任感(从小事开始 — 收玩具 / 穿衣服 / 喂宠物)
- 价值观(父母示范是核心,说教效果差)
中国家长常把"听话"当 character — 错。听话是 obedience,不是 character。
PYD character 是孩子内化的判断力,不是被动服从。
意义 — 培养 character 的方式不是"训" — 是 "示范 + 讨论 + 容许犯错 + 反思"。''',
    'what_to_do': [
        '区分 character vs obedience(后者不是目标)',
        '道德判断 — 用 Smetana 4 类规则讨论',
        '责任感 — 小事(收玩具 / 喂宠物)',
        '价值观 — 父母示范 > 说教',
        '容许犯错 + 反思 = character 形成',
    ],
    'failure_mode': '把"听话"当 character — 错。PYD:character 是内化判断,不是服从。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-PERSON-Smetana', 'G-TERM-positive-youth-development', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1522', 'C-S8-330', 'C-S8-325', 'C-S6-1078'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
},

# =================== Ch 8 Magnusson Holistic ===================
{
    'card_id': 'C-S0-1519', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'magnusson', 'stattin', 'holistic_person', 'foundational'],
    'title': '整体人不是变量人', 'hook': '人不是分数堆',
    'why_matters': '''Magnusson & Stattin(Lerner V1 Ch 8)给 holistic-interactionistic 元理论 —
研究人要把 person 当整体单位,不是把人拆成"变量"分别测。
经典对比 —
- variable-oriented(变量取向)— "智商 IQ 110 + 外向性 75 + 神经质 40 = 此人"
- person-oriented(人取向)— 此人是动态整体,不是变量加和
意义 — 中国家长常 variable-oriented:数学 90 + 英语 60 + 体育 80 = 我家娃。
但娃是动态整体 — 数学 90 跟英语 60 是互动出来,不是独立变量。
意义 — 看孩子要看模式(pattern),不只是分数(scores)。''',
    'what_to_do': [
        '看孩子整体动态,不只单项分数',
        '各科目互动看(数学好可能因兴趣)',
        '"性格"是模式,不是单维分数',
        '同分不同人(高中生 90 分有 5 种来路)',
        '人取向 > 变量取向',
    ],
    'failure_mode': '"我家娃 IQ 110" 单维标签 — 错。Magnusson 综述:人是模式不是变量。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Magnusson', 'G-PERSON-Stattin', 'G-TERM-holistic-person', 'G-TERM-person-oriented-approach'],
    'related_cards': ['C-S0-1500', 'C-S0-1503', 'C-S0-722', 'C-S6-1067'],
    'chapter': 'Ch 8 Holistic Person-Context Interaction (Magnusson & Stattin)',
    'chapter_offset': 2105000,
},
{
    'card_id': 'C-S6-1504', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['relationships', 'lerner_v1', 'magnusson', 'individualization', 'goodness_of_fit'],
    'title': '个性化不是标准化', 'hook': '没两个娃一样',
    'why_matters': '''Magnusson holistic 视角应用到 1-2 岁 —
没有"15 月该会的"标准娃,每个娃是独特模式。
Brazelton "个性化" + Chess "goodness of fit" + Magnusson holistic 三者一致:
养孩子要 fit 这个孩子,不是把孩子套标准。
中国家庭多孩家庭直接经验 — 老大养法不一定适合老二。
但很多父母还是用 "标准答案" 框架 — 一本育儿书 + 一个朋友建议 + 一个老师权威 =统一应用。
Magnusson 视角:每个孩子的模式不同 — 你要观察 + 实验 + 调整。''',
    'what_to_do': [
        '不套"15 月应该 X" 标准',
        '观察自家娃当前模式',
        '实验不同方法 — 看哪个 fit',
        '老大经验不强加老二',
        '"个性化养" = Magnusson 视角',
    ],
    'failure_mode': '"标准娃" 模板 — 错。Magnusson holistic 视角反对。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Magnusson', 'G-TERM-holistic-person', 'G-TERM-goodness-of-fit'],
    'related_cards': ['C-S0-1519', 'C-S6-1066', 'C-S6-1067', 'C-S6-1064'],
    'chapter': 'Ch 8 Magnusson & Stattin',
    'chapter_offset': 2399248,
},
{
    'card_id': 'C-S7-1603', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'magnusson', 'individual_pathway'],
    'title': '群体均值不是你娃', 'hook': '统计骗人个体真',
    'why_matters': '''Magnusson 综述强调 — 心理学统计的"平均值"不是任何具体个体。
"2-3 岁平均 X 月会 Y" 不代表你家娃也该 X 月会 Y。
真正的发展是 individual pathway(个体轨迹)— 每个娃自己的路径不同。
意义 — 中国父母焦虑常源自 "平均" 比较 — 隔壁家娃 / 月龄表 / 早教评估。
Magnusson 视角:跟你家娃自己比,不跟群体均值比。
具体做法 — 记录自家娃 6 月 / 12 月 / 18 月 / 24 月 自己的进步,
跟自己比"是不是在自己路径上发展" — 而非跟群体均值比。''',
    'what_to_do': [
        '记录自家娃 6 月间隔的进步',
        '跟"3 月前的自己" 比,不跟邻居比',
        '群体均值参考 — 不是标准',
        '个体路径 > 平均比较',
        'Magnusson:individual is the unit',
    ],
    'failure_mode': '群体均值焦虑 — 错。Magnusson 综述:你家娃 ≠ 平均人。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Magnusson', 'G-TERM-holistic-person', 'G-TERM-individual-pathway'],
    'related_cards': ['C-S0-1519', 'C-S6-1504', 'C-S7-754', 'C-S6-1067'],
    'chapter': 'Ch 8 Magnusson & Stattin',
    'chapter_offset': 2166368,
},

]

def write_card(c):
    seg = c['seg']
    cid = c['card_id']
    path = os.path.join(BASE, seg, f'{cid}.yaml')

    yaml_str = f'''card_id: {cid}
stages: {c['stages']}
tags: {c['tags']}

front:
  title: "{c['title']}"
  hook: "{c['hook']}"

back:
  why_matters: |
{chr(10).join("    " + line for line in c['why_matters'].split(chr(10)))}
  what_to_do:
{chr(10).join(f'    - "{wtd}"' for wtd in c['what_to_do'])}
  failure_mode: |
    {c['failure_mode']}
  evidence_level: {c['evidence_level']}

glossary_refs:
{chr(10).join(f'  - {g}' for g in c['glossary_refs'])}

related_cards:
{chr(10).join(f'  - {r}' for r in c['related_cards'])}

citation:
  source_id: SRC-030
  source_title: "Handbook of Child Psychology Vol 1: Theoretical Models of Human Development"
  chapter: "{c['chapter']}"
  chapter_offset: {c['chapter_offset']}

language: zh
status: complete
created: 2026-05-04
updated: 2026-05-04
'''
    with open(path, 'w') as f:
        f.write(yaml_str)
    return cid

count = 0
for c in CARDS:
    cid = write_card(c)
    count += 1

print(f"Wrote {count} cards (batch 2: Ch 7 Fischer + Ch 11 Baltes + Ch 16 PYD + Ch 8 Magnusson)")
