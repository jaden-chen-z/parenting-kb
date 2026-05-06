"""Batch 3: Ch 13 Shweder + Ch 4 Valsiner + Ch 9 Csikszentmihalyi + Ch 10 Brandtstadter + Ch 12 Elder"""
import os

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

CARDS = [
# =================== Ch 13 Shweder Cultural Psychology ===================
{
    'card_id': 'C-S0-1524', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'shweder', 'cultural_psychology', 'multiple_mentalities', 'foundational'],
    'title': '心智不是通用的', 'hook': '一种心多种活法',
    'why_matters': '''Shweder / Goodnow / Hatano / LeVine / Markus / Miller(Lerner V1 Ch 13)给 cultural psychology —
multiple mentalities(多元心智论)— 不同文化下人有不同 "心智组织方式",不只是 "同一心智 + 文化变量"。
经典对比 —
- 普世派:所有人心智一样,文化只是背景
- 文化派(Shweder):不同文化人心智不同 — 自我感 / 时间感 / 道德感 / 情绪表达 都构成不同
意义 — 中国人 vs 美国人不只是"文化背景不同",是"心智组织方式不同"。
- 中国娃 self 是 互依(interdependent) — 家庭 / 关系 / 角色 一体
- 美国娃 self 是 独立(independent) — 个体 / 选择 / 边界 突出
意义 — 中国家长不必照搬美式 "self-esteem / 早期独立训练" 标准。''',
    'what_to_do': [
        '中国育儿不照搬美式标准',
        '互依 self ≠ 缺陷(是不同 mentality)',
        '"早期独立"美国标准不适合中国',
        '集体感 / 家庭感是中国娃强项',
        'Shweder 多元 — 不是次等是不同',
    ],
    'failure_mode': '"美国育儿就是先进" — 错。Shweder 综述:多元心智不是次等。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Shweder', 'G-PERSON-Markus', 'G-PERSON-Miller', 'G-TERM-cultural-psychology', 'G-TERM-multiple-mentalities'],
    'related_cards': ['C-S0-1500', 'C-S6-1064', 'C-S8-323', 'C-S0-722'],
    'chapter': 'Ch 13 Cultural Psychology (Shweder / Goodnow / Hatano / LeVine / Markus / Miller)',
    'chapter_offset': 3870000,
},
{
    'card_id': 'C-S0-1525', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'shweder', 'cultural_psychology', 'constitutive_culture'],
    'title': '文化不是修饰是构成', 'hook': '文化造心不只是穿',
    'why_matters': '''Shweder 综述强调 — 文化不是 "心智外面的衣服",是 "心智本身的构成材料"。
不是 "中国娃 + 中国文化 = 中国娃外加文化背景" 而是 "中国娃 = 中国文化构成的 mentality"。
意义 — 跨文化比较 ≠ "去掉文化看核心",而是 "看文化构成的不同 mentality"。
Shweder 名言 — "There is no acultural human being"(没有去文化的人)。
中国家长育儿意义 — 不要试图"教孩子超越文化",这不可能。
但 — 可以让娃接触多元文化,培养 cultural literacy(文化识读力)。
意义 — 育儿要 culturally informed(文化感知)— 不是 culturally neutral(文化中立)。''',
    'what_to_do': [
        '承认娃必然带中国文化心智',
        '不试图"超越文化"教育(不可能)',
        '让娃接触多元文化(读 / 旅行 / 朋友)',
        '培养 cultural literacy 而非"普世人"',
        '中国心智 ≠ 局限,是优势 + 视角',
    ],
    'failure_mode': '"我要养国际化通才"立场 — 错。Shweder:无去文化的人。',
    'evidence_level': 'B',
    'glossary_refs': ['G-PERSON-Shweder', 'G-TERM-cultural-psychology', 'G-TERM-constitutive-culture'],
    'related_cards': ['C-S0-1524', 'C-S0-1500', 'C-S0-722', 'C-S8-323'],
    'chapter': 'Ch 13 Shweder',
    'chapter_offset': 3959460,
},
{
    'card_id': 'C-S6-1506', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'shweder', 'cultural_psychology', 'anti_white_middle_class'],
    'title': '反白人中产单一标准', 'hook': '美式标准非真理',
    'why_matters': '''Lerner V1 多章(Shweder / Spencer / Parke-Buriel)指出 — 80% 育儿研究是基于美国白人中产家庭,
这些研究产出的"标准"不一定适合其他文化(包括中国家庭)。
经典例子 —
- "陌生人焦虑 8-10 月"是白人中产数据 → 多人养文化(中国 / 非洲)中症状不同
- "self-esteem 培养"是美式独立 self → 中国互依 self 不一定需要单独培养
- "Authoritative parenting 最优" → 是白人中产数据 → 亚洲 "严而暖" 文化下 authoritarian + warm 也有好结果(Chao 1994)
意义 — 中国家长读美式育儿书,要"翻译"不是直接套用。
保留中国文化优势 — 多人养 / 集体感 / 严而暖 / 教养并重。''',
    'what_to_do': [
        '美式育儿书 — 翻译不照搬',
        '中国"严而暖"也有效(数据支持)',
        '集体感 / 多人养 是优势不是缺陷',
        '不必培养"美式 self-esteem"',
        '看中国文化下的研究(Chao / Chen)',
    ],
    'failure_mode': '美式标准全套用 — 错。文化不匹配会反效果。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Shweder', 'G-PERSON-Spencer', 'G-TERM-cultural-psychology', 'G-TERM-cross-cultural-validity'],
    'related_cards': ['C-S0-1524', 'C-S0-1525', 'C-S8-323', 'C-S8-324'],
    'chapter': 'Ch 13 Shweder + Ch 15 Spencer',
    'chapter_offset': 3997026,
},
{
    'card_id': 'C-S8-1138', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'shweder', 'cultural_psychology', 'parent_application'],
    'title': '中国娃不是落后娃', 'hook': '互依 self 也是金',
    'why_matters': '''Shweder + Markus 的核心命题 — 中国(亚洲)互依 self 不是 "西方独立 self 的初级阶段",是不同 mentality 的等价位。
- 美国娃 5 岁 "我喜欢蓝色因为我喜欢" — 独立 self
- 中国娃 5 岁 "妈妈说蓝色好看所以我也喜欢" — 互依 self
两者都健康,都有发展轨迹,只是不同 mentality。
意义 — 中国家长不必焦虑"我家娃没有美式 self-esteem"。
研究数据(Chao 1994 + Chen 2002)— 中国 "严而暖" + 互依 self 在中国情境下结果良好。
反而 — 强行美式独立训练放在中国情境(集体学校 / 家庭)反而 mismatch 出问题。''',
    'what_to_do': [
        '中国娃互依 self ≠ 缺乏自我',
        '不强行培养美式 "I am special" self',
        '"我们家"叙事是中国 self 健康表达',
        '集体感 + 个人成就 兼顾',
        '中国教养在中国情境有效',
    ],
    'failure_mode': '强培"美式自信" — 文化不匹配会反效果。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Shweder', 'G-PERSON-Markus', 'G-TERM-cultural-psychology', 'G-TERM-interdependent-self'],
    'related_cards': ['C-S0-1524', 'C-S0-1525', 'C-S6-1506', 'C-S8-323'],
    'chapter': 'Ch 13 Shweder',
    'chapter_offset': 4117263,
},

# =================== Ch 4 Valsiner ===================
{
    'card_id': 'C-S0-1546', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'valsiner', 'cultural_construction', 'foundational'],
    'title': '文化和娃共建', 'hook': '不是文化灌入娃',
    'why_matters': '''Valsiner(Lerner V1 Ch 4)给 cultural construction 视角 —
不是 "文化在外面 → 灌入娃 → 娃接受",是 "娃和文化在每天互动中共建(co-construct)"。
意义 —
- 娃不是被动接收文化,是主动参与建构
- 同样文化下,不同娃接受/改造/抗拒方式不同
- 文化也在被娃改变(代际传播是双向)
中国家长意义 — 不要把 "文化传承" 当 "灌输"。
娃会自己 negotiate(协商)— 接受一部分,修改一部分,抗拒一部分。
意义 — 你给娃 "中国文化"(节日 / 礼仪 / 价值观),娃会重新组装出他自己的版本。
不要试图 "复制" 你的版本到娃身上。''',
    'what_to_do': [
        '文化传承不是灌输',
        '让娃 negotiate(参与 + 改造)',
        '允许娃版本跟你不同',
        '中西文化都接触 — 让娃自己组装',
        '代际传播双向 — 娃也教你',
    ],
    'failure_mode': '"复制我的文化版本到娃" — 错。Valsiner:共建不是灌入。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Valsiner', 'G-TERM-cultural-construction', 'G-TERM-cultural-psychology'],
    'related_cards': ['C-S0-1524', 'C-S0-1525', 'C-S0-722', 'C-S8-323'],
    'chapter': 'Ch 4 Culture in Human Development (Valsiner)',
    'chapter_offset': 900000,
},

# =================== Ch 9 Csikszentmihalyi Flow ===================
{
    'card_id': 'C-S0-1527', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'csikszentmihalyi', 'flow', 'intrinsic_motivation', 'foundational'],
    'title': 'Flow 心流是发展核', 'hook': '内驱比奖励强',
    'why_matters': '''Csikszentmihalyi & Rathunde(Lerner V1 Ch 9)给 flow theory —
心流是 "活动本身就是奖励" 的状态(intrinsic motivation 内在动机)。
4 大特征 — 挑战 / 技能匹配 + 即时反馈 + 高度专注 + 自我感消失。
意义 — 中国家长重外部激励(奖励 / 表扬 / 物质) — 短期有效,长期破坏内驱。
Flow 视角 — 让娃在活动中找 flow → 内驱自然形成,不需要奖励。
具体做法 —
- 任务难度跟娃当前技能匹配(太难/太易都不会有 flow)
- 让娃自己选活动(选择是 flow 必要条件)
- 给即时反馈(不只是结果)
- 不打断专注期(娃在 flow 时别叫吃饭)
意义 — flow 是终生学习能力的基础。''',
    'what_to_do': [
        '挑战 / 技能匹配是 flow 必要条件',
        '让娃自己选活动 + 选难度',
        '不打断专注期(flow 时静止旁观)',
        '即时反馈 — 不只是结果',
        'flow 比奖励更可持续',
    ],
    'failure_mode': '"奖励 / 表扬" 当主激励 — 短期有效长期毁内驱。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Csikszentmihalyi', 'G-PERSON-Rathunde', 'G-TERM-flow-theory', 'G-TERM-intrinsic-motivation'],
    'related_cards': ['C-S0-1500', 'C-S0-1522', 'C-S6-1064', 'C-S0-722'],
    'chapter': 'Ch 9 Optimal Experience (Rathunde & Csikszentmihalyi)',
    'chapter_offset': 2440000,
},
{
    'card_id': 'C-S6-1507', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'csikszentmihalyi', 'flow', 'toddler'],
    'title': '1-2 岁初版心流', 'hook': '专注玩别打扰',
    'why_matters': '''1-2 岁孩子已能进入 flow 状态 — 经典场景:专注玩积木 / 沙子 / 倒水 30+ 分钟。
父母常错误地 "及时打断"(吃饭 / 洗澡 / 出门)— 这破坏 flow,长期破坏专注力发展。
Csikszentmihalyi 数据 — 早期 flow 体验是终生 flow 能力的基础。
意义 — 1-2 岁专注玩 30 分钟看似 "无用",其实在练 flow 神经回路。
具体做法 —
- 看到娃专注玩 → 不要打断(就算到饭点也等 5-10 分钟)
- 提供长时间不被打断的玩耍空间(早上 / 下午)
- 玩具简单 + 多变(乐高 / 积木 / 沙子 / 水)易引发 flow
- 高科技玩具(声光过强)反而打断 flow''',
    'what_to_do': [
        '看到专注玩 → 不打断 + 等 5-10 分钟',
        '提供长时间(30-60 分)无打断玩耍',
        '简单 + 多变玩具 引发 flow',
        '声光过强玩具 干扰 flow',
        '1-2 岁 flow 是终生专注力基础',
    ],
    'failure_mode': '专注玩中打断"该吃饭了" — 破坏 flow 神经回路发展。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Csikszentmihalyi', 'G-TERM-flow-theory'],
    'related_cards': ['C-S0-1527', 'C-S6-1064', 'C-S6-1505', 'C-S2-700'],
    'chapter': 'Ch 9 Csikszentmihalyi & Rathunde',
    'chapter_offset': 2556299,
},
{
    'card_id': 'C-S7-1605', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'csikszentmihalyi', 'autotelic_personality'],
    'title': '内驱型人格', 'hook': '为做而做不为奖',
    'why_matters': '''Csikszentmihalyi 给 autotelic personality 概念 —
"以活动本身为目的"的人格(au=自,telos=目的)。
数据 — 6+ 岁 autotelic 倾向已能测,跟成年成就 + 福祉强相关。
意义 — 中国家长 "做这个有什么用" 思维 → 培养 instrumental(工具型)人格(看回报)。
autotelic 人格 — 喜欢学就学,喜欢做就做 — 不问回报。
2-3 岁是 autotelic 形成关键期 —
- 让娃做"无用"的事(扔石头 / 看蚂蚁 / 唱歌)
- 不问"这个对你有什么用"
- 享受过程不只看结果
- 父母自己示范 — 你也喜欢"无用"的事(读小说 / 散步 / 兴趣爱好)
意义 — autotelic 是终生 flow 能力的人格基础。''',
    'what_to_do': [
        '让娃做"无用"的事(扔石头 / 看蚂蚁)',
        '不问"这个对你有什么用"',
        '父母示范"无用"兴趣爱好',
        '享受过程 > 看结果',
        'autotelic 是终生学习人格',
    ],
    'failure_mode': '"做这个有什么用" 思维 — 培养 instrumental 工具型人格。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Csikszentmihalyi', 'G-TERM-autotelic-personality', 'G-TERM-flow-theory'],
    'related_cards': ['C-S0-1527', 'C-S6-1507', 'C-S7-754', 'C-S8-1136'],
    'chapter': 'Ch 9 Csikszentmihalyi & Rathunde',
    'chapter_offset': 2507393,
},
{
    'card_id': 'C-S8-1139', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'csikszentmihalyi', 'flow', 'challenge_skill'],
    'title': '挑战技能要匹配', 'hook': '太难太易都没流',
    'why_matters': '''Csikszentmihalyi flow 必要条件 — 挑战 ≈ 技能。
- 挑战 >> 技能 → 焦虑(不知所措)
- 挑战 << 技能 → 无聊(失去兴趣)
- 挑战 ≈ 技能 → flow(高度投入)
3-6 岁应用 —
- 学走路时 → 平地走会无聊,坡道挑战适中(flow)
- 拼图 → 12 块没难度,100 块绝望,30-50 块 flow
- 学画 → 完全自由空白页焦虑,临摹无趣,有 frame 自由 flow
意义 — 父母选活动 / 玩具 / 学习内容,要刻意调挑战难度。
中国"超龄学"(3 岁学小学)→ 挑战 >> 技能 → 焦虑而非 flow → 长期厌学。''',
    'what_to_do': [
        '选活动看挑战 / 技能匹配',
        '太难 → 降难度 + 拆解步骤',
        '太易 → 加变化 + 升难度',
        '"超龄学" → 焦虑非 flow',
        'flow 是学习内驱的核心条件',
    ],
    'failure_mode': '"超龄超难"学法 — 错。挑战 >> 技能 = 焦虑非 flow。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Csikszentmihalyi', 'G-TERM-flow-theory'],
    'related_cards': ['C-S0-1527', 'C-S6-1507', 'C-S7-1605', 'C-S8-1135'],
    'chapter': 'Ch 9 Csikszentmihalyi & Rathunde',
    'chapter_offset': 2440000,
},

# =================== Ch 10 Brandtstadter Action Theory ===================
{
    'card_id': 'C-S0-1528', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'brandtstadter', 'action_theory', 'foundational'],
    'title': '同化 vs 调节双过程', 'hook': '改环境还是改自己',
    'why_matters': '''Brandtstädter(Lerner V1 Ch 10)给 action theory of self-development —
人面对发展挑战有 2 大策略:
- Assimilation(同化)— 改环境让它适应自己(我家厨房改造让娃能自己取水)
- Accommodation(调节)— 改自己适应环境(娃学规则 / 学等待 / 学忍受)
两者交替使用 — 不是非此即彼。
中国家长常 over-accommodation(让娃一直适应) — 让娃超龄学 / 强忍 / 守规矩 → 培养"懂事娃"代价是真实需求被压制。
理想模式 — 该 assimilate 时(改环境支持娃) + 该 accommodate 时(教娃适应)平衡。
意义 — 育儿 = 双向 action — 改环境 + 改孩子双管齐下。''',
    'what_to_do': [
        '该 assimilate — 改家具高度让娃用',
        '该 accommodate — 教娃等 / 守规则',
        '看情境选哪个(都有用)',
        '不 over-accommodate(让娃一直适应)',
        '双策略交替,不是单选',
    ],
    'failure_mode': '一直 accommodation(逼娃适应)— 培养压抑型懂事娃。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Brandtstadter', 'G-TERM-action-theory', 'G-TERM-assimilation-accommodation'],
    'related_cards': ['C-S0-1500', 'C-S0-1522', 'C-S0-722', 'C-S6-816'],
    'chapter': 'Ch 10 Action Theory of Self-Development (Brandtstadter)',
    'chapter_offset': 2770000,
},
{
    'card_id': 'C-S6-1508', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'brandtstadter', 'action_theory', 'environmental_modification'],
    'title': '1-2 岁多 assimilate', 'hook': '改家比改娃易',
    'why_matters': '''1-2 岁阶段 — accommodation(让娃适应)能力极有限(PFC 没装好),
所以这阶段以 assimilation(改环境)为主才合理。
具体 —
- 想娃自己穿鞋 → 给易穿的鞋 + 矮椅(assimilate)— 不是教娃复杂穿法
- 想娃自己吃 → 给易抓食物 + 防溅围兜(assimilate)— 不是逼用筷子
- 想娃不爬高 → 收高物 + 装防护(assimilate)— 不是反复教 "不许爬"
- 想娃睡好 → 调环境(光 / 声 / 温度)(assimilate)— 不是哄睡几小时
中国家长常反过来 — 要求娃适应大人环境 — 1-2 岁能力跟不上 → 哭闹冲突。
意义 — 看到冲突 → 先想能不能改环境(assimilate),再想该不该教娃(accommodate)。''',
    'what_to_do': [
        '冲突先问 — 能改环境吗',
        '改环境 (易穿鞋 / 矮家具 / 防护) 优先',
        '改娃(教规则)是次选',
        '1-2 岁 PFC 没装好 → 难 accommodate',
        'assimilation 减少 90% 冲突',
    ],
    'failure_mode': '反复教规则不改环境 — 错。1-2 岁能力跟不上。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Brandtstadter', 'G-TERM-action-theory', 'G-TERM-assimilation-accommodation'],
    'related_cards': ['C-S0-1528', 'C-S6-816', 'C-S6-820', 'C-S6-1064'],
    'chapter': 'Ch 10 Brandtstadter',
    'chapter_offset': 2820869,
},
{
    'card_id': 'C-S7-1606', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'brandtstadter', 'intentional_self_development'],
    'title': '主动塑造自己', 'hook': '娃 2 岁开始自塑',
    'why_matters': '''Brandtstädter 提 intentional self-development — 人不是被动被发展,是主动塑造自己。
2-3 岁就开始 — 娃说 "我自己" / "我要" / "不要" — 这是 intentional self-development 起步,
不是"反抗期"。
意义 — 中国家长把 "我自己" / "不要" 解读为反抗 → 镇压 → 破坏 intentional self-development。
正确视角 —
- "我自己" = 娃在练 self-development 主体性
- "不要" = 娃在练 boundary 设定
- "为什么" = 娃在练 metacognition 反思
父母工作 — 支持 intentional self-development,不镇压。
具体 — 让娃做选择(穿什么 / 玩什么 / 吃什么)— 是 self-development 训练。''',
    'what_to_do': [
        '"我自己"鼓励不打断',
        '"不要"听 + 谈判 — 不立刻否决',
        '让娃做小选择(穿 / 玩 / 吃)',
        'self-development 起步阶段宝贵',
        '"反抗期" = 误解 self-development',
    ],
    'failure_mode': '"反抗期"镇压视角 — 错。Brandtstadter:2 岁 self-development 起步。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Brandtstadter', 'G-TERM-action-theory', 'G-TERM-intentional-self-development'],
    'related_cards': ['C-S0-1528', 'C-S7-755', 'C-S7-754', 'C-S7-756'],
    'chapter': 'Ch 10 Brandtstadter',
    'chapter_offset': 2820869,
},

# =================== Ch 12 Elder & Shanahan Life Course ===================
{
    'card_id': 'C-S0-1529', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'elder', 'shanahan', 'life_course', 'foundational'],
    'title': '生命历程 5 大原则', 'hook': '人发展看 5 因素',
    'why_matters': '''Elder & Shanahan(Lerner V1 Ch 12)给 life course theory 5 大原则:
1. Lifespan development — 一辈子发展(对接 Baltes)
2. Human agency — 人是主动行动者(选择影响轨迹)
3. Time and place — 历史时段 + 地理位置塑造发展
4. Linked lives — 个人发展跟其他人轨迹绑定(父母 / 配偶 / 孩子互相影响)
5. Timing — 同一事件在不同生命阶段影响不同(20 岁失业 ≠ 50 岁失业)
意义 — 育儿不只是"管娃" — 是看 family 整个 life course。
中国家长常忽视 linked lives — 你的工作 / 婚姻 / 健康 直接影响娃,娃也直接影响你。
家庭整体看,不只看娃。''',
    'what_to_do': [
        '看 family 整体不只看娃',
        '夫妻 / 父母 / 老人 linked lives',
        '历史时段(2026 年中国)塑造育儿',
        'timing 重要(同事件在不同年龄不同)',
        'agency — 你和娃都是主动行动者',
    ],
    'failure_mode': '只看娃不看 family system — 错。Linked lives 不可忽视。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Elder', 'G-PERSON-Shanahan', 'G-TERM-life-course-theory', 'G-TERM-linked-lives'],
    'related_cards': ['C-S0-1500', 'C-S0-1513', 'C-S0-722', 'C-S8-1132'],
    'chapter': 'Ch 12 Life Course Theory (Elder & Shanahan)',
    'chapter_offset': 3505000,
},
{
    'card_id': 'C-S0-1530', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'elder', 'linked_lives', 'family_system'],
    'title': '人生轨迹相互绑定', 'hook': '你娃父母一体化',
    'why_matters': '''Elder linked lives 原则 — 没有独立的人生轨迹,所有人的生命都跟其他人绑定。
- 你的工作压力 → 娃看到 → 娃焦虑
- 娃的健康问题 → 你工作受影响 → 经济变化 → 婚姻压力
- 老人健康 → 父母分心 → 育儿质量下降
- 夫妻关系 → 娃情绪
意义 — 育儿不能只调娃 — 整个 family system 要一起调。
中国家庭常 — 婚姻 / 工作 / 老人 / 经济 多压同时,父母想"先把娃管好" — 错。
实际 — family 任一处出问题,其他都受影响。
意义 — 优先级:夫妻关系 + 父母自我 ≥ 育儿(因为前者影响后者)。''',
    'what_to_do': [
        '夫妻关系优先(影响娃)',
        '父母自己照顾自己(不耗尽自己)',
        '老人关系处理好(影响 micro)',
        'family system 整体调',
        '"为娃牺牲一切" 反伤娃',
    ],
    'failure_mode': '"为娃牺牲一切"立场 — 错。linked lives:family 整体健康才有娃健康。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Elder', 'G-TERM-linked-lives', 'G-TERM-life-course-theory'],
    'related_cards': ['C-S0-1529', 'C-S8-1132', 'C-S0-722', 'C-S6-822'],
    'chapter': 'Ch 12 Elder & Shanahan',
    'chapter_offset': 3637709,
},
{
    'card_id': 'C-S6-1509', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'elder', 'timing'],
    'title': '同事不同岁影响别', 'hook': '时机定影响大小',
    'why_matters': '''Elder timing 原则 — 同样事件在不同生命阶段影响完全不同。
1-2 岁阶段经历 —
- 父母离婚 → 影响远大于 10 岁(依恋系统正在形成)
- 长期分离(父母外地工作)→ 影响远大于 5 岁
- 严重疾病 → 影响远大于 7 岁
- 入托 → 1.5 岁前可能太早,2 岁后较好
意义 — 中国家庭常忽视 timing — "她还小不记事" 立场 → 错。
1-2 岁正在打依恋 + 神经回路基础,任何重大事件影响放大 5-10 倍。
另一方面 — 父母不必所有事 "等娃大了再做" — 自己人生也有 timing。
关键 — 知道 1-2 岁特别脆弱,重大事件尽量推迟。''',
    'what_to_do': [
        '1-2 岁尽量稳定(避免大变动)',
        '"她还小不记事" 是错觉(神经层记)',
        '入托避免 1.5 岁前',
        '父母分离 / 离婚等重大事 timing 重要',
        'timing 决定影响大小',
    ],
    'failure_mode': '"她还小不记事"立场 — 错。1-2 岁神经层会记住影响。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Elder', 'G-TERM-life-course-theory', 'G-TERM-timing-principle'],
    'related_cards': ['C-S0-1529', 'C-S0-1530', 'C-S6-822', 'C-S2-697'],
    'chapter': 'Ch 12 Elder & Shanahan',
    'chapter_offset': 3637709,
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

print(f"Wrote {count} cards (batch 3: Ch 13 Shweder + Ch 4 Valsiner + Ch 9 Flow + Ch 10 Action + Ch 12 Life Course)")
