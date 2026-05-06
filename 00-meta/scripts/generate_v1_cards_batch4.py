"""Batch 4: Ch 1 Lerner + Ch 3 Cairns + Ch 15 Spencer + Ch 17 Oser + cross-chapter themes"""
import os

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

CARDS = [
# =================== Ch 1 Lerner Developmental Science ===================
{
    'card_id': 'C-S0-1535', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'developmental_science', 'foundational'],
    'title': '发展科学新框架', 'hook': '不是单一心理学',
    'why_matters': '''Lerner(Lerner V1 Ch 1)给当代发展心理学新名字 — developmental science(发展科学)。
不是 "developmental psychology" 单一学科,是 多学科合体:
- 心理学 + 神经科学 + 遗传学 + 社会学 + 人类学 + 教育学 + 政策科学
- 共识方法 — relational developmental systems
- 共识价值 — 应用导向(从研究到政策到实操)
意义 — 育儿不能只看心理学,要看跨学科证据综合。
中国家长意义 —
- 单看 一本心理学书 → 视角窄
- 多看 心理学 + 神经科学 + 教育学 + 社会学 综合 → 视角立体
- 警惕 "纯心理学" 立场单一专家
意义 — Lerner V1 整本书就是 "developmental science" 的多视角综合示范。''',
    'what_to_do': [
        '不只看心理学一种视角',
        '神经 / 遗传 / 社会 / 教育多视角',
        '警惕单一专家立场',
        '应用导向 — 实操才是检验',
        'developmental science > 单学科',
    ],
    'failure_mode': '只信一个学科一个专家 — 错。当代视角是跨学科。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-developmental-science', 'G-TERM-relational-developmental-systems'],
    'related_cards': ['C-S0-1500', 'C-S0-1503', 'C-S0-722', 'C-S0-008'],
    'chapter': 'Ch 1 Developmental Science (Lerner)',
    'chapter_offset': 52000,
},
{
    'card_id': 'C-S0-1536', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'overton', 'relational_developmental_systems'],
    'title': '关系发展系统总框', 'hook': 'V1 的统一答案',
    'why_matters': '''Lerner V1 全卷的最终答案 — relational developmental systems(关系发展系统)是当代元理论统合。
组成 —
- relational metatheory(Overton)— 关系思维取代二分思维
- developmental systems(Gottlieb / Lerner)— 多层次互动取代单因
- contextualism(Lerner)— 个体 ↔ 环境双向取代单向
- dynamic systems(Thelen-Smith)— self-organization 取代预定阶段
- holistic-interactionistic(Magnusson)— 整体人取代变量人
- bioecological(Bronfenbrenner)— 5 层环境取代单一环境
- lifespan(Baltes)— 全程发展取代关键期
意义 — 这套框架是 2006 后儿童心理学的"主流共识",中国家长理解这套框架,
看任何育儿书都有了"地图"。''',
    'what_to_do': [
        '记住 7 大元理论关键名词',
        '看任何育儿书 — 用 RDS 框架定位',
        'split 派 vs RDS 派 — 一眼看出',
        '中国当代育儿应用 RDS 框架',
        'Lerner V1 是"框架地图"',
    ],
    'failure_mode': '不学元框架 — 永远在"哪派对"焦虑里。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-PERSON-Overton', 'G-TERM-relational-developmental-systems'],
    'related_cards': ['C-S0-1125', 'C-S0-1500', 'C-S0-1535', 'C-S0-1503'],
    'chapter': 'Ch 1 Lerner Developmental Science + 跨卷综合',
    'chapter_offset': 52000,
},

# =================== Ch 3 Cairns History of Developmental Psychology ===================
{
    'card_id': 'C-S0-1537', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cairns', 'history', 'three_grand_systems'],
    'title': '心理学 3 大派', 'hook': '认知精分行为派',
    'why_matters': '''Cairns & Cairns(Lerner V1 Ch 3)给发展心理学百年史 —
20 世纪主流是 "three grand systems" 三大派:
- Cognitive-developmentalism(认知派)— Piaget / Vygotsky
- Psychoanalysis(精神分析派)— Freud / Erikson / Bowlby
- Learning theory(学习理论派)— Skinner / Bandura
中国家长接触的育儿书都属于这 3 派之一(或衍生):
- 蒙氏 / 早教 / Gopnik = 认知派
- Bowlby / Stern / Ainsworth = 精神分析派(扩展为依恋派)
- 行为训练 / Brazelton 部分 / 强化奖励 = 学习理论派
意义 — 知道一本书是哪派,你就知道它的盲点(每派都有偏)。
当代综合派(Lerner / Bronfenbrenner / dynamic systems)= 3 派融合 + 跨学科。''',
    'what_to_do': [
        '认出每本书属于哪派',
        '知道每派的盲点(都有)',
        '认知派偏 — 忽视情绪 + 关系',
        '精分派偏 — 忽视行为 + 学习',
        '学习派偏 — 忽视主动 + 关系',
        '当代综合派 — 三派融合',
    ],
    'failure_mode': '不分派别 — 看一本书就当真理。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Cairns-R', 'G-PERSON-Cairns-B', 'G-TERM-three-grand-systems', 'G-TERM-history-of-developmental-psych'],
    'related_cards': ['C-S0-1125', 'C-S0-1535', 'C-S0-1536', 'C-S0-722'],
    'chapter': 'Ch 3 Making of Developmental Psychology (Cairns & Cairns)',
    'chapter_offset': 490000,
},
{
    'card_id': 'C-S0-1538', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cairns', 'werner', 'orthogenetic'],
    'title': 'Werner 正交发展原则', 'hook': '从笼统到精分化',
    'why_matters': '''Werner orthogenetic principle(正交发展原则)是发展心理学奠基命题之一(via Cairns Ch 3)—
发展是从 globally undifferentiated → differentiated and hierarchically integrated。
- 全球未分化(婴儿)→ 分化 + 层级整合(成熟)
- 婴儿一切感受混在一起 → 慢慢分出各种情绪 / 概念 / 关系
- 婴儿动作笼统 → 慢慢分出精细动作
应用 —
- 情绪 — 6 月笼统兴奋 / 苦恼 → 12 月分出兴奋 / 害怕 / 生气 → 24 月分出嫉妒 / 内疚 / 自豪
- 概念 — 1 岁 "动物" 笼统 → 3 岁 分 狗 / 猫 / 鸟
- 自我 — 1 岁笼统 "我" → 3 岁分 "学习的我 / 玩的我 / 妹妹的哥"
意义 — 中国家长不期望 1 岁娃有 3 岁的精细分化能力。
分化是发展的 mark,不是天生有的。''',
    'what_to_do': [
        '不期望婴儿有精细分化能力',
        '情绪 / 概念 / 自我 都从笼统开始',
        '随发展自然分化',
        '逼分化 (反复教 概念) 不一定有效',
        'Werner 原则解释发展轨迹',
    ],
    'failure_mode': '逼婴儿"懂细节" — 错。Werner:发展是从笼统到分化的过程。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Werner-H', 'G-PERSON-Cairns-R', 'G-TERM-orthogenetic-principle'],
    'related_cards': ['C-S0-1537', 'C-S0-1500', 'C-S0-722', 'C-S2-697'],
    'chapter': 'Ch 3 Cairns + Ch 1 Werner reference',
    'chapter_offset': 689728,
},
{
    'card_id': 'C-S0-1539', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cairns', 'history', '75_years'],
    'title': '心理学 75 年史教训', 'hook': '别再走老弯路',
    'why_matters': '''Cairns Ch 3 综合 1931-2006 = 75+ 年发展心理学史。
3 个核心教训给当代家长 —
1. **每代主流都被推翻** — 1930 年代 nativism / 1950 年代 behaviorism / 1960 年代 cognitivism / 1990 年代 dynamic systems → 别死信当下"科学"
2. **极端立场都错** — 全基因决定 / 全环境决定 / 全先天 / 全后天 — 后被实证全部推翻
3. **综合是答案** — 当代 RDS 是综合 + 跨学科 + 多层
意义 — 中国家长接触的"最新科学" 50 年后可能被推翻 — 别全信。
读历史让你 — 拒绝极端立场 + 接受不确定性 + 综合多视角。''',
    'what_to_do': [
        '拒绝极端立场(全基因 / 全环境)',
        '当代"科学"50 年后未必正确',
        '综合 + 多视角 安全',
        '不确定性是常态',
        '历史教训 = 别迷信单一权威',
    ],
    'failure_mode': '迷信"最新研究"的单一立场 — 历史教训:多被推翻。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Cairns-R', 'G-PERSON-Cairns-B', 'G-TERM-history-of-developmental-psych'],
    'related_cards': ['C-S0-1537', 'C-S0-1538', 'C-S0-1535', 'C-S0-722'],
    'chapter': 'Ch 3 Cairns 75-year history',
    'chapter_offset': 880825,
},

# =================== Ch 15 Spencer PVEST ===================
{
    'card_id': 'C-S0-1532', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'spencer', 'PVEST', 'identity'],
    'title': 'PVEST 风险身份模', 'hook': '种族阶层入生态',
    'why_matters': '''Spencer(Lerner V1 Ch 15)给 PVEST(Phenomenological Variant of Ecological Systems Theory) —
在 Bronfenbrenner 5 系统基础上加入 perception(主观感知) + identity(身份建构) 维度。
5 组件:
1. Net vulnerability(净脆弱)— 风险 - 资源
2. Net stress(净压力)— 实际压力 - 支持
3. Reactive coping(应对反应)— 适应/不适应方式
4. Emergent identity(涌现身份)— 通过应对形成身份
5. Coping outcomes(应对结果)— 长期适应/不适应
意义 — Bronfenbrenner 给环境结构,Spencer 加 "孩子怎么主观体验环境 + 形成身份" 维度。
应用 — 中国 "外地人" / "城乡 gap" / "二胎" 等身份问题用 PVEST 分析。
不只看客观环境,看孩子主观感受 + 身份形成。''',
    'what_to_do': [
        '看娃主观感受 — 不只客观环境',
        '身份形成是主动应对的产物',
        '"风险"分析要扣资源(净脆弱)',
        '中国"身份"压力(户口 / 城乡 / 二胎)用 PVEST',
        'identity 是 coping 出来的',
    ],
    'failure_mode': '只看客观环境不看孩子主观感受 — 错。PVEST 强调 phenomenology。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Spencer', 'G-TERM-PVEST', 'G-TERM-bioecological-model'],
    'related_cards': ['C-S0-1500', 'C-S0-1501', 'C-S0-722', 'C-S6-1064'],
    'chapter': 'Ch 15 PVEST (Spencer)',
    'chapter_offset': 4540000,
},
{
    'card_id': 'C-S6-1510', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'spencer', 'identity_formation'],
    'title': '身份从应对中长', 'hook': '不是天生的标签',
    'why_matters': '''Spencer PVEST 关键命题 — identity(身份)不是天生标签,是孩子主动应对环境的产物。
1-2 岁还没明确"身份"概念,但身份的根从这阶段开始 —
- 通过反复经验 — 形成"我是 X 的人"叙事
- 通过应对挑战 — 形成"我能 / 我不能"自我效能
- 通过被对待 — 形成"我值得 / 不值得"价值感
意义 — 中国家长贴标签("我家娃就是内向 / 害羞 / 慢热") → 进入娃身份建构 → 长期固化。
反向用 PVEST — 不贴标签,描述行为("今天她在 playground 试了新滑梯")。
让娃从应对中自然涌现 identity,不是被父母标签锁定。''',
    'what_to_do': [
        '不贴"她就是 X"标签',
        '描述行为 — 不评价人',
        '让娃自然涌现身份',
        '"应对挑战" 经验积累 = 自我效能',
        'identity 是应对出来的不是天生',
    ],
    'failure_mode': '"她就是内向"标签 — 锁定娃 identity 长期固化。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Spencer', 'G-TERM-PVEST', 'G-TERM-identity-formation'],
    'related_cards': ['C-S0-1532', 'C-S6-1066', 'C-S6-1067', 'C-S6-1505'],
    'chapter': 'Ch 15 Spencer PVEST',
    'chapter_offset': 4551844,
},
{
    'card_id': 'C-S8-1142', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'spencer', 'racism', 'social_pressure'],
    'title': '种族阶层影响发展', 'hook': '社会偏见进童心',
    'why_matters': '''Spencer Ch 15 强调 — racism / classism / sexism 不只是 "社会问题",是直接影响儿童发展的环境变量。
中国家庭情境下对应 —
- 户口歧视(外地学校 / 城乡待遇)
- 性别偏见(男孩 vs 女孩对待)
- 学校阶层(普通 vs 重点)
- 家长身份(白领 vs 蓝领)
- 长相 / 体重 / 口音歧视
3-6 岁孩子开始感知这些 — 不直接说,但影响 identity 形成。
意义 — 父母不能等到孩子 "懂事了再说" — 3-6 岁就要 —
- 帮孩子识别歧视(不让孩子内化"我不行")
- 解释社会不公(适合年龄的语言)
- 培养应对策略(不接受 + 不传染)
- 父母示范不歧视他人(言行一致)''',
    'what_to_do': [
        '帮娃识别歧视(不让内化)',
        '解释社会不公 — 适合年龄的语言',
        '培养应对策略(不接受 / 不传染)',
        '父母示范不歧视他人',
        '种族 / 性别 / 阶层 议题不回避',
    ],
    'failure_mode': '"等懂事了再说" — 错。3-6 岁已经在内化偏见。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Spencer', 'G-TERM-PVEST', 'G-TERM-racism-in-development'],
    'related_cards': ['C-S0-1532', 'C-S6-1510', 'C-S8-323', 'C-S8-324'],
    'chapter': 'Ch 15 Spencer PVEST',
    'chapter_offset': 4829838,
},

# =================== Ch 17 Oser Religious/Spiritual Development ===================
{
    'card_id': 'C-S6-1511', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'oser', 'religious_development', 'spirituality'],
    'title': '信仰发展也有阶段', 'hook': '信仰小时即萌芽',
    'why_matters': '''Oser / Scarlett / Bucher(Lerner V1 Ch 17)给 religious/spiritual development 综述。
信仰发展不只 "宗教信仰",是 "对意义 / 超越 / 价值 的体验" — 包括无宗教家庭。
1-2 岁开始的灵性发展征兆 —
- 对自然的好奇 + 敬畏(看星星 / 大海 / 大树)
- 对死亡的早期感知(看到死蝉 / 死宠物)
- 对"为什么"的追问(超越具体答案)
意义 — 中国父母常 "孩子还小不懂" 跳过这话题 — 错过灵性发展窗口。
建议 —
- 自然敬畏 — 多带户外 / 看天 / 看夜空
- 死亡话题 — 不回避(看到死蝉可以谈)
- 神秘感受 — 接纳不解释
意义 — 灵性 ≠ 宗教 = 对意义的体验,是 wellbeing 重要维度。''',
    'what_to_do': [
        '多带户外培养自然敬畏',
        '不回避死亡话题(适当年龄)',
        '神秘感受 — 接纳不解释',
        '"为什么" 追问 — 容纳不完美答案',
        '灵性 ≠ 宗教 = 意义感',
    ],
    'failure_mode': '"小不懂"跳过灵性话题 — 错过早期发展窗口。',
    'evidence_level': 'B',
    'glossary_refs': ['G-PERSON-Oser', 'G-TERM-religious-spiritual-development'],
    'related_cards': ['C-S6-1064', 'C-S6-1505', 'C-S0-1517', 'C-S6-820'],
    'chapter': 'Ch 17 Religious/Spiritual Development (Oser / Scarlett / Bucher)',
    'chapter_offset': 5105000,
},
{
    'card_id': 'C-S8-1143', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'oser', 'spirituality', 'meaning'],
    'title': '灵性不限于宗教', 'hook': '意义感终生重要',
    'why_matters': '''Oser Ch 17 综述 — spiritual development 不限于宗教信仰,是普世发展维度。
3-6 岁阶段的灵性发展任务 —
- 意义建构 — "我是谁 / 我为什么在这" 早期版
- 关系超越 — "我跟家人 / 自然 / 宇宙 的连接"
- 价值内化 — "什么重要 / 什么不重要"
- 死亡好奇 — "活的 vs 死的 / 永远 vs 暂时"
中国非宗教家庭也能培养灵性 —
- 通过自然(山 / 海 / 星空)
- 通过艺术(音乐 / 绘画 / 诗)
- 通过传统(节日 / 祖辈故事)
- 通过哲学讨论(适合年龄)
数据 — 灵性高的成年人 wellbeing 显著高 → 0-6 岁是基础期。''',
    'what_to_do': [
        '自然敬畏 — 户外 / 星空 / 海',
        '艺术体验 — 音乐 / 绘画 / 诗',
        '传统连接 — 节日 / 祖辈 / 家族',
        '哲学讨论 — 适合年龄的"为什么"',
        '灵性 = wellbeing 维度 不只宗教',
    ],
    'failure_mode': '"我家不信教没灵性" — 错。灵性是意义感不限宗教。',
    'evidence_level': 'B',
    'glossary_refs': ['G-PERSON-Oser', 'G-TERM-religious-spiritual-development'],
    'related_cards': ['C-S6-1511', 'C-S0-1517', 'C-S8-1136', 'C-S8-105'],
    'chapter': 'Ch 17 Oser',
    'chapter_offset': 5159842,
},

# =================== 跨章主题独立卡(必须独立化) ===================
{
    'card_id': 'C-S0-1540', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'determinism', 'foundational'],
    'title': '决定论 vs 概率论', 'hook': '不是命定是可能',
    'why_matters': '''跨章命题(Ch 5 Gottlieb + Ch 11 Baltes + Ch 6 Thelen)— 反 determinism 是 V1 元理论共识。
- 基因 determinism — Gottlieb 反(probabilistic epigenesis)
- 阶段 determinism — Thelen 反(dynamic emergence)
- 早期 determinism — Baltes 反(lifespan plasticity)
- 文化 determinism — Shweder 改(共建非灌入)
共识 — 发展是 probabilistic(概率性)不是 deterministic(决定性)。
意义 —
- "天生 X" 错(基因不决定)
- "过了关键期就完了" 错(早期不决定)
- "这阶段就是反抗期" 错(阶段不决定)
- "中国娃就是 X" 错(文化不决定)
反之 — 一切都是概率 + 多层 + 双向 + 可塑。''',
    'what_to_do': [
        '"决定论" 立场全部警惕',
        '基因 / 早期 / 阶段 / 文化 都不决定',
        'probabilistic 视角 = 多种可能',
        '行动改变概率 — 不是命运',
        '反 determinism = V1 元共识',
    ],
    'failure_mode': '任何"X 决定 Y"立场 — V1 全部反对。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Gottlieb', 'G-PERSON-Baltes', 'G-PERSON-Thelen', 'G-TERM-anti-determinism', 'G-TERM-probabilistic-epigenesis'],
    'related_cards': ['C-S0-1503', 'C-S0-1513', 'C-S0-1508', 'C-S0-1524'],
    'chapter': 'Ch 5 + Ch 11 + Ch 6 + Ch 13(跨章命题)',
    'chapter_offset': 1140000,
},
{
    'card_id': 'C-S0-1541', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'reductionism', 'anti'],
    'title': '反还原论批判', 'hook': '一物分万非真理',
    'why_matters': '''跨章共识(Ch 2 Overton + Ch 5 Gottlieb + Ch 8 Magnusson)— 反 reductionism(还原论)。
什么是 reductionism — 把复杂系统简化为更简单组件,再单独分析。
- 把 "孩子" 简化为 "脑" — 还原到神经
- 把 "脑" 简化为 "基因表达" — 还原到分子
- 把 "孩子情绪" 简化为 "化学反应" — 还原到生化
V1 综述明确反对 — 还原论会丢失系统层级的涌现属性。
意义 —
- 中国家长 "孩子情绪问题 = 缺锌 / 缺铁 / 缺维生素" 立场 = 还原论
- "孩子学不进 = 智力低" = 还原论
- "孩子打人 = 性格坏" = 还原论
反 — 看 multi-level + 关系 + 系统层级。''',
    'what_to_do': [
        '不简化复杂为单因',
        '"缺 X 补 X" 是还原立场',
        '看 multi-level(基因 / 神经 / 行为 / 环境)',
        '系统涌现属性不能从组件预测',
        '反 reductionism = V1 共识',
    ],
    'failure_mode': '"X 问题就是 Y 简单原因" — V1 反 reductionism 立场。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Overton', 'G-PERSON-Gottlieb', 'G-PERSON-Magnusson', 'G-TERM-anti-reductionism', 'G-TERM-relational-metatheory'],
    'related_cards': ['C-S0-1125', 'C-S0-1503', 'C-S0-1519', 'C-S0-722'],
    'chapter': 'Ch 2 + Ch 5 + Ch 8(跨章命题)',
    'chapter_offset': 145000,
},
{
    'card_id': 'C-S0-1542', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'emergence', 'foundational'],
    'title': '涌现论是发展核心', 'hook': '系统组装出新',
    'why_matters': '''跨章命题(Ch 6 Thelen + Ch 7 Fischer + Ch 11 Baltes)— emergence(涌现)是发展核心机制。
什么是 emergence — 系统达到一定复杂度后,涌现出无法从组件预测的新属性。
经典例子 —
- 走步能力 = 腿 + 重力 + 神经 + 平衡 + 动机 涌现(Thelen)
- 语言能力 = 听力 + 模仿 + 互动 + 意图 涌现
- 自我意识 = 反思 + 镜像 + 关系 涌现
意义 — 你不能"教"涌现,只能"创造条件"等涌现。
中国家长意义 —
- "教走" / "教说话" / "教情商" 是错位心态
- 应是 — 提供条件 + 等系统 self-organize
- 看到能力涌现 — 庆祝不是奖励(已经够了)
意义 — emergence 视角让你放下"教"的焦虑,改为"等"的耐心。''',
    'what_to_do': [
        '"教技能" 错位 — 应"创造条件"',
        '提供环境 / 时间 / 安全 → 等涌现',
        '看到涌现 — 庆祝不奖励',
        '"教"的焦虑放下',
        'emergence 视角 = 育儿耐心根',
    ],
    'failure_mode': '"教技能"心态 — 干扰 self-organize 涌现过程。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Fischer-K', 'G-TERM-emergence', 'G-TERM-self-organization'],
    'related_cards': ['C-S0-1508', 'C-S0-1509', 'C-S0-1512', 'C-S2-1502'],
    'chapter': 'Ch 6 + Ch 7 + Ch 11(跨章命题)',
    'chapter_offset': 1395000,
},
{
    'card_id': 'C-S0-1543', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'continuity_discontinuity'],
    'title': '连续 vs 不连续', 'hook': '都对要看哪层',
    'why_matters': '''跨章经典争议(Ch 6 vs Ch 11 vs Ch 7)— continuity(连续)vs discontinuity(不连续)。
- continuity 派(Baltes)— 发展是渐进累积,不是跳跃
- discontinuity 派(Piaget)— 发展是阶段跳跃
- 当代综合 — 看哪一层
  - 神经层级(细胞数 / 突触修剪)= continuity 渐进
  - 行为层级(走 / 说 / 写)= discontinuity 跳跃涌现
  - 认知层级(物体永久 / 守恒)= 半 continuity 半 discontinuity
意义 — 中国家长经常二选一立场("发展是连续的" 或"阶段跳跃"),都太简化。
当代视角 — 不同层级不同性质,父母要分层看。
- 长期累积(语言 / 阅读)= continuity → 每天积累
- 关键涌现(走 / 说话 / 自我意识)= discontinuity → 等 + 庆祝
意义 — 双视角让你既有耐心(看 continuity)又有期待(看 discontinuity)。''',
    'what_to_do': [
        '区分哪一层 continuity 哪一层 discontinuity',
        '语言阅读 — continuity 每天积累',
        '走说话 — discontinuity 等涌现',
        '不二选一 — 双视角并用',
        '层级不同性质不同',
    ],
    'failure_mode': '只看 continuity (急于积累) 或只看 discontinuity (干等) — 错。双视角并用。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Baltes', 'G-PERSON-Piaget', 'G-PERSON-Thelen', 'G-TERM-continuity-discontinuity'],
    'related_cards': ['C-S0-1508', 'C-S0-1513', 'C-S0-1542', 'C-S0-722'],
    'chapter': 'Ch 6 + Ch 11 + Ch 7(跨章命题)',
    'chapter_offset': 1395000,
},
{
    'card_id': 'C-S0-1544', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'nature_nurture', 'modern_synthesis'],
    'title': '基因 vs 环境综合', 'hook': '不是哪派对都需',
    'why_matters': '''跨章核心(Ch 5 Gottlieb + Ch 2 Overton + Ch 11 Baltes)— nature vs nurture 当代综合。
20 世纪争 — 基因派 vs 环境派 互相否定。
21 世纪综合 — 基因 ↔ 环境 双向终生互动:
- 基因表达受环境调控(epigenetics)
- 环境影响通过基因表达发生
- 行为既改基因表达也改环境
- 4 层(基因 / 神经 / 行为 / 环境)互相塑造(Gottlieb)
意义 — 中国家长 "天生 vs 教育" 二选一立场过时。
当代立场 — 不能简单分配 X% 基因 + Y% 环境,因为两者持续互动塑造。
"双胞胎研究"显示 50% 基因贡献 — 但这不是"基因决定 50%",是"在当前环境中估算的相关性"。
环境改变,这个 50% 可以变。''',
    'what_to_do': [
        '"基因 vs 环境" 二选一立场过时',
        '基因 ↔ 环境 双向终生互动',
        '50% 数据 ≠ 基因决定 50%',
        '环境改 → 50% 可改',
        '当代综合 = nature × nurture',
    ],
    'failure_mode': '"基因占 X% 环境占 Y%" 立场 — 误读双胞胎数据。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Gottlieb', 'G-PERSON-Overton', 'G-TERM-nature-vs-nurture', 'G-TERM-probabilistic-epigenesis'],
    'related_cards': ['C-S0-1503', 'C-S0-1125', 'C-S0-1540', 'C-S0-722'],
    'chapter': 'Ch 5 + Ch 2 + Ch 11(跨章命题)',
    'chapter_offset': 1140000,
},
{
    'card_id': 'C-S0-1545', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'systems_thinking'],
    'title': '系统观必备视角', 'hook': '看整体不只组件',
    'why_matters': '''跨章共识(Ch 6 + Ch 8 + Ch 14 + Ch 15)— systems thinking 是当代核心元视角。
核心命题 — 整体 ≠ 组件之和(emergence + interaction)。
4 派系统观:
- Dynamic systems(Thelen)— 时间维度系统
- Holistic person(Magnusson)— 个体内部系统
- Bioecological(Bronfenbrenner)— 个体 ↔ 环境系统
- PVEST(Spencer)— 主观 + 身份系统
意义 — 中国家长习惯线性思维 — "做 X → 得 Y"。
系统思维 — "做 X → 多个反馈环路 → 多种可能 Y"。
经典例子 —
- 给娃报奥数 → 期望 数学好 → 实际可能引发 数学厌恶 / 自信下降 / 时间没了 / 关系紧张
- 给娃多自由 → 期望 自主 → 实际可能引发 焦虑 / 不知所措 / 选择困难
意义 — 任何育儿决定都是系统决定,看多反馈环路,不只单线 cause-effect。''',
    'what_to_do': [
        '任何决定 — 想 3+ 反馈环路',
        '"做 X 得 Y" 线性思维警惕',
        '看 multi-feedback 不只单线',
        '系统思维 = 减少意外后果',
        '4 派系统观全部学一遍',
    ],
    'failure_mode': '线性思维 — "做 X 必得 Y" — 漏掉系统反馈环路。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Magnusson', 'G-PERSON-Bronfenbrenner', 'G-PERSON-Spencer', 'G-TERM-systems-thinking'],
    'related_cards': ['C-S0-1500', 'C-S0-1508', 'C-S0-1519', 'C-S0-1532'],
    'chapter': 'Ch 6 + Ch 8 + Ch 14 + Ch 15(跨章命题)',
    'chapter_offset': 4275000,
},
{
    'card_id': 'C-S6-1512', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'individual_vs_universal'],
    'title': '个体差异 vs 普世', 'hook': '都重要但分情境',
    'why_matters': '''跨章经典张力(Ch 8 Magnusson + Ch 13 Shweder + Ch 11 Baltes)—
个体差异 vs 普世规律 平衡。
- 个体差异(Magnusson)— 没两个娃一样
- 普世规律(Baltes 早期)— 所有娃都遵循 X 发展
- 文化差异(Shweder)— 不同文化娃路径不同
当代综合 —
- 普世(走 / 说 / 依恋形成)— 大方向一致
- 个体(气质 / 兴趣 / 路径)— 个体差异巨大
- 文化(self / 道德 / 时间感)— 文化差异显著
意义 — 中国家长两端都掉 —
- 偏普世 — 拿"标准发展表"焦虑你家娃
- 偏个体 — 完全不参考标准
正确视角 — 普世大方向 + 个体路径 + 文化情境 三者综合看。''',
    'what_to_do': [
        '普世大方向 — 参考',
        '个体路径 — 主体',
        '文化情境 — 不忽视',
        '三者综合看,不二选一',
        '"标准娃" 错觉警惕',
    ],
    'failure_mode': '只看普世(标准表)或只看个体(完全相对) — 都错。三者综合。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Magnusson', 'G-PERSON-Shweder', 'G-PERSON-Baltes', 'G-TERM-individual-differences', 'G-TERM-cultural-psychology'],
    'related_cards': ['C-S0-1519', 'C-S0-1524', 'C-S0-1513', 'C-S6-1504'],
    'chapter': 'Ch 8 + Ch 13 + Ch 11(跨章命题)',
    'chapter_offset': 2105000,
},

# =================== Spencer 增补 + PYD 中国应用 ===================
{
    'card_id': 'C-S8-1144', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'cross_chapter', 'culture_individual_co_construction'],
    'title': '文化-个人共建构', 'hook': '不是套不是反',
    'why_matters': '''跨章共识(Ch 4 Valsiner + Ch 13 Shweder + Ch 1 Lerner)— 文化-个人是共建构关系。
不是 — 文化在外 → 灌入娃(传统观)
也不是 — 娃完全自主 → 文化是限制(西方个人主义观)
而是 — 娃和文化每天互动 → 共同建构出娃的 mentality + 文化的更新版本
意义 — 中国家长对 "文化传承" 常 2 极:
- 极保守 — "祖辈怎么养就怎么养"(灌入)
- 极反传统 — "我家不要中国传统这些套子"(反弹)
当代视角 — 让娃 negotiate(协商)文化:接受一部分,改造一部分,加新版本。
具体 —
- 跟娃讨论传统(为啥过节 / 拜祖)
- 容忍娃版本不同(她不想拜祖也行)
- 让娃接触多元(不只中国文化)
- 看娃 5 年后自己的版本''',
    'what_to_do': [
        '不强行传承(也不彻底反)',
        '让娃 negotiate 文化',
        '接受娃版本跟你不同',
        '多元接触 — 中国 + 西方 + 其他',
        '5 年后看娃版本',
    ],
    'failure_mode': '"祖辈怎么养就怎么" 或 "全反传统" — 都错。共建构是中道。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Valsiner', 'G-PERSON-Shweder', 'G-PERSON-Lerner', 'G-TERM-cultural-construction', 'G-TERM-cultural-psychology'],
    'related_cards': ['C-S0-1524', 'C-S0-1525', 'C-S0-1546', 'C-S8-323'],
    'chapter': 'Ch 4 + Ch 13 + Ch 1(跨章命题)',
    'chapter_offset': 900000,
},
{
    'card_id': 'C-S8-1140', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'brandtstadter', 'self_other_change'],
    'title': '改环境 vs 改自己', 'hook': '5 岁该练双策略',
    'why_matters': '''Brandtstadter 双过程在 5 岁开始能教 —
让娃自己决定 — 这件事我改环境(assimilate)还是改自己(accommodate)?
经典场景 —
- 学校规则我不喜欢(午睡时间)— 改环境(跟老师沟通)还是改自己(学会接受)?
- 朋友惹我 — 改环境(换朋友)还是改自己(沟通修复)?
- 我做不到某事 — 改环境(找帮助)还是改自己(练)?
意义 — 培养 agency 意识 — 娃知道自己有 2 个策略,不是被动。
中国家庭常 — 一律 accommodate(适应规则)→ 培养顺从娃,不培养 agency。
应支持双策略,让娃自己选择 — 这是 PYD competence + character 培养基础。
具体 — 跟 5+ 岁娃讨论 "这事咱们能改环境吗?如果不能咱们怎么自己适应?"''',
    'what_to_do': [
        '5+ 岁讨论"改环境 vs 改自己"',
        '不一律让娃 accommodate',
        'agency 是双策略意识',
        'assimilate 也教(沟通 / 求助 / 改环境)',
        'PYD competence 基础',
    ],
    'failure_mode': '一律"你要适应"立场 — 培养顺从娃缺 agency。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Brandtstadter', 'G-TERM-action-theory', 'G-TERM-assimilation-accommodation'],
    'related_cards': ['C-S0-1528', 'C-S6-1508', 'C-S7-1606', 'C-S8-1136'],
    'chapter': 'Ch 10 Brandtstadter',
    'chapter_offset': 2820869,
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

print(f"Wrote {count} cards (batch 4: Ch 1 Lerner + Ch 3 Cairns + Ch 15 Spencer + Ch 17 Oser + cross-chapter)")
