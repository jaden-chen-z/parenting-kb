"""人工深度审 — 补漏 9 卡 + 3 术语"""
import os

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'
GLOSS = '/Users/jjjjadennnn/Desktop/parenting-kb/40-glossary'

# === 3 张漏的 G-PERSON ===
PERSONS = [
    {'id': 'Greenough', 'full_zh': '威廉·格里诺', 'full_en': 'William T. Greenough',
     'pos': 'University of Illinois 心理学教授',
     'contrib': 'experience-expectant vs experience-dependent 突触分类 + 终生神经可塑性实证',
     'ch': 'Ch 11 (via Baltes)', 'hits': '50+', 'school': 'Lerner V1 神经可塑性派'},
    {'id': 'Fowler', 'full_zh': '詹姆斯·福勒', 'full_en': 'James W. Fowler',
     'pos': 'Emory University 神学院教授(已故)',
     'contrib': '信仰发展 6 阶段(stages of faith)— 全人类信仰认知发展奠基',
     'ch': 'Ch 17', 'hits': '36', 'school': 'Lerner V1 信仰发展派'},
    {'id': 'Baldwin-JM', 'full_zh': '詹姆斯·M·鲍德温', 'full_en': 'James Mark Baldwin',
     'pos': 'Princeton / Johns Hopkins 心理学教授(已故 1934)',
     'contrib': 'genetic logic 发展逻辑 + Baldwin effect + 早期发展心理学奠基(Piaget 直接师承)',
     'ch': 'Ch 4 (via Valsiner)', 'hits': '38', 'school': 'Lerner V1 历史奠基派'},
]

def write_person(p):
    pid = p['id']
    path = os.path.join(GLOSS, f'G-PERSON-{pid}.yaml')
    if os.path.exists(path): return f'{pid} (existed)'
    yaml_str = f'''glossary_id: G-PERSON-{pid}
type: person
display_name: "{pid}({p['full_zh']})"

full_name_en: "{p['full_en']}"
full_name_zh: "{p['full_zh']}"

position: |
  {p['pos']}

contribution: |
  {p['contrib']}

one_liner: |
  {p['full_zh']} — {p['contrib']}

key_facts:
  - "本卷章节:{p['ch']}"
  - "Lerner V1 命中:{p['hits']} 次"
  - "学派:{p['school']}"

related_glossary: []
related_cards: []

sources:
  - source_id: SRC-030
    chapter: "{p['ch']}"

language: zh
status: complete
created: 2026-05-04
updated: 2026-05-04
'''
    with open(path, 'w') as f: f.write(yaml_str)
    return pid


# === 6 张新 G-TERM(对应漏的命题) ===
TERMS = [
    {'id': 'genetic-logic', 'name_zh': '发展逻辑', 'name_en': 'genetic logic (Baldwin)',
     'desc': 'Baldwin 1906 提出 — 心理发展的逻辑分析方法,认为发展是质变 + 阶段重组,不是量变累积。\nPiaget 直接师承 Baldwin,Vygotsky 也受影响。'},
    {'id': 'helix-development', 'name_zh': '螺旋发展', 'name_en': 'helix / spiral development',
     'desc': 'Valsiner 模型 — 发展像螺旋上升,不是直线也不是圆周。\n时间不可逆 + 状态似而非同 + 持续涌现新结构。'},
    {'id': 'neoteny', 'name_zh': '幼态延续', 'name_en': 'neoteny',
     'desc': 'Csikszentmihalyi 借生物学概念 — 人保留幼年特性进入成年(玩 / 好奇 / 学习能力)。\n人类是动物界 neoteny 最强物种,这是 flow 能力的进化基础。'},
    {'id': 'thriving', 'name_zh': '繁荣发展', 'name_en': 'thriving',
     'desc': 'Lerner PYD 概念 — 5C(后扩 6C)之上的整体状态 — 个体跟环境互动产生最优发展。\n不只是"没问题",是"积极发展"。'},
    {'id': 'developmental-assets', 'name_zh': '发展资产', 'name_en': 'developmental assets',
     'desc': 'Search Institute (Benson) 提出 40 项 — 内部 (commitment to learning / positive values / etc)+ 外部 (support / boundaries / constructive use of time / empowerment)资产。'},
    {'id': 'fowler-faith-stages', 'name_zh': 'Fowler 信仰 6 阶段', 'name_en': 'Fowler stages of faith',
     'desc': 'Fowler 1981 经典 — 信仰发展 6 阶段(intuitive-projective / mythic-literal / synthetic-conventional / individuative-reflective / conjunctive / universalizing)。'},
    {'id': 'oser-religious-judgment', 'name_zh': 'Oser 信仰判断 5 阶段', 'name_en': 'Oser religious judgment stages',
     'desc': 'Oser 提出 — 5 阶段儿童如何理解神 / 命运 / 责任(orientation deus ex machina → autonomy 自主 → deism 神在内 → mediated 中介 → unconditional 无条件)。'},
    {'id': 'cohort-effects', 'name_zh': '世代效应', 'name_en': 'cohort effects',
     'desc': 'Elder & Shanahan 概念 — 同时代出生的人受历史时段塑造 (大萧条 / 战争 / 经济危机)— 影响超越个人选择。'},
    {'id': 'oakland-growth-study', 'name_zh': '奥克兰成长研究', 'name_en': 'Oakland Growth Study (Elder)',
     'desc': 'Elder 经典数据源 — 1929 大萧条期 167 名儿童终生跟踪。\n证明历史时段(大萧条)对儿童发展影响因家庭经济状态而异 — 中产家庭逆境反而培养 resilience。'},
    {'id': 'developmental-trajectories', 'name_zh': '发展轨迹', 'name_en': 'developmental trajectories',
     'desc': 'Elder 概念 — 个人的人生路径 — 由历史时段 + 家庭背景 + 个人选择 + linked lives 共同塑造。\n不是单一线,有 multiple trajectories(教育 / 职业 / 家庭 / 健康)。'},
]

def write_term(t):
    tid = t['id']
    path = os.path.join(GLOSS, f'G-TERM-{tid}.yaml')
    if os.path.exists(path): return f'{tid} (existed)'
    desc_lines = t['desc'].split('\n')
    desc_block = '\n'.join('  ' + l for l in desc_lines)
    yaml_str = f'''glossary_id: G-TERM-{tid}
type: term
display_name: "{t['name_zh']} / {t['name_en']}"

name_en: "{t['name_en']}"
name_zh: "{t['name_zh']}"

description: |
{desc_block}

one_liner: |
  {t['name_zh']}({t['name_en']})— {desc_lines[0]}

key_facts:
  - "Lerner V1 元理论卷核心术语"
  - "学派:Lerner V1 综述派"

related_glossary: []
related_cards: []

sources:
  - source_id: SRC-030

language: zh
status: complete
created: 2026-05-04
updated: 2026-05-04
'''
    with open(path, 'w') as f: f.write(yaml_str)
    return tid


# === 9 张漏卡 ===
CARDS = [
# Ch 4 Valsiner: Baldwin + helix
{
    'card_id': 'C-S0-1547', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'valsiner', 'baldwin', 'genetic_logic', 'foundational'],
    'title': 'Baldwin 发展逻辑奠基', 'hook': '心理发展不是堆积',
    'why_matters': '''Valsiner(Lerner V1 Ch 4)指出 — James Mark Baldwin 1906 发展心理学奠基人(直接师承 Piaget)。
Baldwin "genetic logic" 立场 — 心理发展不是量的累积,是质的重组。
- 反"积累论"(empiricism 经验派 — 学得多就发展)
- 反"成熟论"(nativism 先天派 — 时间到了就会)
- 主"重组论"— 发展是阶段间的质变重组
意义 — 中国家长 "学得越早越好"立场是 Baldwin 反对的累积论。
Baldwin 视角:学的内容跟孩子当前结构匹配,才能引发重组(等于 ZPD Vygotsky 的源头)。
不是越早越多越好,是恰到好处的"撞击"促进重组。''',
    'what_to_do': [
        '不"累积"早教 — 看孩子结构准备',
        '"撞击"匹配当前结构 = 学习高效',
        '反"学得多就发展"流行立场',
        '阶段重组需要时间和空间',
        'Baldwin = 现代发展心理学奠基',
    ],
    'failure_mode': '"灌入式早教"立场 — 错。Baldwin 视角:发展是重组不是累积。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Valsiner', 'G-PERSON-Baldwin-JM', 'G-PERSON-Piaget', 'G-TERM-genetic-logic'],
    'related_cards': ['C-S0-1546', 'C-S0-1503', 'C-S0-722', 'C-S0-1125'],
    'chapter': 'Ch 4 Valsiner (Baldwin reference)',
    'chapter_offset': 1050000,
},
{
    'card_id': 'C-S0-1548', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'valsiner', 'helix_development', 'time_irreversibility'],
    'title': '螺旋发展非循环', 'hook': '不会回到过去状态',
    'why_matters': '''Valsiner Ch 4 给"helix"螺旋模型 — 发展不是直线也不是循环。
"看似回到过去状态"(eg 退步 / 退行)实际不是回到 — 是螺旋上升中相似但更高位置。
原因 — 时间不可逆(irreversibility),每个新状态都是独特的。
意义 — 中国家长 "她又退回去了"立场是循环论错觉。
- 5 岁的"分离焦虑"≠ 1 岁的分离焦虑(更高级版本,认知更复杂)
- 7 岁的"叛逆"≠ 2 岁的叛逆(autonomy 期 vs identity 期)
- 老人"回归童心"≠ 真童心(经历过完整人生的人玩耍是不同质的)
意义 — 看似退步要看高位含义 — 螺旋上升中的低点,不是真退。''',
    'what_to_do': [
        '"她又退回去了" → 看是不是螺旋上升的相似点',
        '不同年龄分离焦虑性质不同',
        '不同年龄叛逆性质不同',
        '时间不可逆 — 不会真回到过去',
        '螺旋视角 = 看高位不只看表象',
    ],
    'failure_mode': '"循环论"看发展(回到过去) — 错。螺旋上升每个状态独特。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Valsiner', 'G-TERM-helix-development', 'G-TERM-emergence'],
    'related_cards': ['C-S0-1546', 'C-S0-1547', 'C-S2-1504', 'C-S0-1542'],
    'chapter': 'Ch 4 Valsiner',
    'chapter_offset': 1050000,
},

# Ch 12 Elder: Oakland Great Depression + cohort effects
{
    'card_id': 'C-S0-1549', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'elder', 'cohort_effects', 'great_depression'],
    'title': '大时代塑造小孩子', 'hook': '世代差距是真的',
    'why_matters': '''Elder Ch 12 经典数据源 — Oakland Growth Study 1929 大萧条期 167 名儿童终生跟踪 + Berkeley Guidance Study 1928。
关键发现:
- 中产家庭遇大萧条 → 父母经济压力 → 但娃发展出 resilience(被迫早熟 + 责任感)
- 工薪家庭遇大萧条 → 父母情绪崩 → 娃发展受损
- 同样"经济危机" → 不同家庭背景下儿童轨迹完全不同
意义 — 中国家长意义 —
- 经济压力本身不是育儿杀手 — 父母怎么应对才是
- "穷养"不一定差 — 看家庭情绪稳定 + 是否给娃责任感
- "富养"不一定好 — 看父母是否传递价值观
- 时段(80 后 vs 90 后 vs 00 后育儿)— 历史塑造差异巨大
意义 — 不能孤立看孩子,看 family 处于哪个历史时段 + 怎么应对。''',
    'what_to_do': [
        '经济压力 — 父母情绪稳定才是关键',
        '"穷养"不必焦虑 — 看家庭情绪 + 责任感',
        '"富养"不必傲 — 看价值观传递',
        '理解世代差异(80 后 ≠ 00 后育儿)',
        'family 处境 + 应对方式 = 关键',
    ],
    'failure_mode': '只盯个人努力不看历史时段 — 错。Elder 数据:cohort 决定 50%+。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Elder', 'G-TERM-cohort-effects', 'G-TERM-oakland-growth-study', 'G-TERM-life-course-theory'],
    'related_cards': ['C-S0-1529', 'C-S0-1530', 'C-S8-1133', 'C-S8-1134'],
    'chapter': 'Ch 12 Elder & Shanahan',
    'chapter_offset': 3637709,
},
{
    'card_id': 'C-S0-1550', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'elder', 'trajectories', 'multiple_pathways'],
    'title': '人生有多条轨迹', 'hook': '不是单一路径',
    'why_matters': '''Elder 概念 — 人不是单一发展路径,是 multiple trajectories(多重轨迹)同时进行:
- 教育 trajectory(从入园到毕业)
- 职业 trajectory(从工作到退休)
- 家庭 trajectory(单身 → 婚 → 育 → 老)
- 健康 trajectory(从健康到老化)
- 关系 trajectory(朋友 / 同事 / 邻居网络变化)
- 灵性 trajectory(信仰 / 价值观演化)
意义 — 中国家长常 "教育 trajectory 唯一"立场 → 把娃发展简化成"上好学校"单线。
Elder 视角 — 看 6+ 条轨迹综合 — 教育只是其中一条。
- 学业差但社交好 → 教育轨迹弱 / 关系轨迹强 = 人生未必差
- 学业好但孤独 → 教育强 / 关系弱 = 一条腿走路
- 健康差(过劳 / 焦虑) → 健康轨迹下行 → 长期所有轨迹下行
意义 — 多轨迹视角让你不焦虑单一路径,看综合发展。''',
    'what_to_do': [
        '不只看教育 trajectory(就 1 条)',
        '同时看健康 / 关系 / 灵性 / 兴趣',
        '某条强可补另一条弱',
        '"学业好就行" 立场过简',
        '6+ 条轨迹综合看人生',
    ],
    'failure_mode': '"教育 trajectory 唯一" 立场 — 错。Elder 视角:多轨迹综合。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Elder', 'G-TERM-developmental-trajectories', 'G-TERM-life-course-theory'],
    'related_cards': ['C-S0-1529', 'C-S0-1530', 'C-S0-1549', 'C-S0-1522'],
    'chapter': 'Ch 12 Elder & Shanahan',
    'chapter_offset': 3637709,
},

# Ch 17 Oser: Fowler stages + Oser religious judgment
{
    'card_id': 'C-S0-1551', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'oser', 'fowler', 'faith_stages'],
    'title': 'Fowler 信仰 6 阶段', 'hook': '信仰怎么慢慢长',
    'why_matters': '''Fowler 1981 经典 — 信仰发展 6 阶段(via Oser Ch 17):
1. **intuitive-projective**(3-7 岁)— 直觉投射,神是大力量(像超人)
2. **mythic-literal**(7-12 岁)— 神话字面理解,故事即真理
3. **synthetic-conventional**(青春期)— 综合常规,跟随群体信仰
4. **individuative-reflective**(青年期)— 个人反思,质疑常规
5. **conjunctive**(中年期)— 综合矛盾 + 接纳神秘
6. **universalizing**(罕见)— 普世意识,超越教派
意义 — 中国非宗教家庭也适用(Fowler 不限于宗教,是"意义系统")。
中国父母对接 —
- 3-7 岁娃问"妈妈,人死了去哪" — 直觉投射阶段,简单回答
- 7-12 岁娃信"故事就是这样" — 字面理解,容许 + 不嘲笑
- 青春期质疑你的价值观 — 个人反思阶段,平等讨论''',
    'what_to_do': [
        '3-7 岁 — 简单具体回答关于神 / 死亡',
        '7-12 岁 — 容许字面理解,不强行抽象',
        '青春期 — 质疑是健康发展',
        '不限于宗教 — 任何意义系统',
        'Fowler 6 阶段 = 终生信仰发展',
    ],
    'failure_mode': '"信仰是大人事" 立场 — 错。Fowler:3-7 岁就开始。',
    'evidence_level': 'B',
    'glossary_refs': ['G-PERSON-Fowler', 'G-PERSON-Oser', 'G-TERM-fowler-faith-stages', 'G-TERM-religious-spiritual-development'],
    'related_cards': ['C-S6-1511', 'C-S8-1143', 'C-S0-1517', 'C-S8-1136'],
    'chapter': 'Ch 17 Oser (Fowler reference)',
    'chapter_offset': 5172633,
},
{
    'card_id': 'C-S6-1513', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['philosophy', 'lerner_v1', 'oser', 'religious_judgment'],
    'title': 'Oser 信仰 5 阶段', 'hook': '神死命谁负责',
    'why_matters': '''Oser 自己 5 阶段模型(信仰判断,不只 Fowler 信仰内容)— 儿童如何理解神 / 命运 / 责任:
1. **deus ex machina**(早期)— 神像万能开关,出事祈祷神来救
2. **autonomy**(8-10 岁)— 神跟人事分开,自己负责
3. **deism**(青春期)— 神是抽象原则,内化在我心
4. **mediated**(青年)— 神跟人通过他人 / 关系作用
5. **unconditional**(成熟)— 无条件信任,不依赖物理证据
1-2 岁 起步 —
- 听到祖辈祈祷 / 拜祖
- 问"为什么人会死"
- 看到自然(花谢 / 月亮 / 星星)有敬畏感
意义 — 不是教信仰,是接纳娃的灵性提问。
中国家长意义 — 老人拜祖父母可参与 — 是娃 deus ex machina 阶段的自然体验。''',
    'what_to_do': [
        '老人祈祷 / 拜祖 — 让娃自然体验',
        '"为什么死"问题 — 简单诚实回答',
        '自然敬畏 — 多带户外',
        '不灌输也不阻止',
        'Oser 5 阶段 = 信仰判断发展',
    ],
    'failure_mode': '"小孩不懂这些" 跳过 — 错。1-2 岁灵性体验是奠基。',
    'evidence_level': 'B',
    'glossary_refs': ['G-PERSON-Oser', 'G-TERM-oser-religious-judgment', 'G-TERM-religious-spiritual-development'],
    'related_cards': ['C-S6-1511', 'C-S0-1551', 'C-S8-1143', 'C-S0-1517'],
    'chapter': 'Ch 17 Oser',
    'chapter_offset': 5159842,
},

# Ch 9 Csikszentmihalyi: neoteny
{
    'card_id': 'C-S0-1552', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'csikszentmihalyi', 'neoteny', 'lifelong_play'],
    'title': '人是终生玩家物种', 'hook': '童心是进化优势',
    'why_matters': '''Csikszentmihalyi(Ch 9)借生物学 neoteny 概念 — 人是动物界 neoteny 最强物种。
neoteny = 保留幼年特性进入成年(玩 / 好奇 / 学习能力)。
意义 —
- 黑猩猩 5 岁 + 就 "成年化",失去玩 / 探索动力
- 人 5 岁 50 岁 都能玩 / 学 / 好奇 — 这是进化优势
- 老人有童心 — 不是退化,是 neoteny 完整保留
- 父母自己也要保 neoteny — 跟娃一起玩是双向收益
中国家长意义 — "成熟"不是去除童心,是把童心 + 责任结合。
- 不必教娃"早成熟"(剥夺 neoteny = 剥夺学习能力)
- 父母自己保童心(跟娃一起好奇 / 玩 / 学)
- 老人保童心 — 鼓励别压制
意义 — neoteny 是 flow + 终生学习能力的根基。''',
    'what_to_do': [
        '不教娃"早成熟" — 保 neoteny',
        '父母自己保童心(跟娃一起玩)',
        '老人有童心鼓励别压',
        '"成熟" = 童心 + 责任',
        'neoteny = 终生学习根基',
    ],
    'failure_mode': '"教娃早成熟" 立场 — 剥夺 neoteny = 剥夺学习能力。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Csikszentmihalyi', 'G-TERM-neoteny', 'G-TERM-flow-theory'],
    'related_cards': ['C-S0-1527', 'C-S0-1517', 'C-S6-1507', 'C-S0-1513'],
    'chapter': 'Ch 9 Csikszentmihalyi & Rathunde',
    'chapter_offset': 2507393,
},

# Ch 16 Lerner PYD: thriving + developmental assets
{
    'card_id': 'C-S0-1553', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'thriving'],
    'title': '繁荣发展不只 5C', 'hook': '5C 之上的整体感',
    'why_matters': '''Lerner Ch 16 提 thriving(繁荣发展)— 是 5C(后扩 6C)之上的整体状态。
thriving = 个体跟环境互动产生最优发展。
不只是 "没问题 / 不犯错",是积极发展 + 贡献:
- Competence(能力)→ 实际用出来
- Confidence(自信)→ 不怯于尝试
- Connection(连接)→ 多元关系网
- Character(品格)→ 内化价值观
- Caring(关怀)→ 主动付出
- Contribution(贡献)→ 给社区 / 家 / 社会
意义 — 中国家长 "不犯错就行" / "成绩好就行" 立场是 deficit/单维 vs thriving 整体视角。
thriving 视角让你看 — 娃整体状态(身心灵 + 关系 + 贡献)是不是积极发展?
不是某一维度高分。
意义 — thriving 是 PYD 的目标,不是 average,不是 excellent,是 holistically positive。''',
    'what_to_do': [
        'thriving 看整体不看单维',
        '6C 同时发展才是 thriving',
        '"不犯错就行" 立场放下',
        '"成绩好就行" 立场放下',
        'thriving = PYD 终极目标',
    ],
    'failure_mode': '"不犯错就行" 立场 — 错。PYD 视角:thriving 是积极发展。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-thriving', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1522', 'C-S6-1505', 'C-S8-1136', 'C-S0-722'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
},
{
    'card_id': 'C-S8-1146', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'benson', 'developmental_assets'],
    'title': 'Search 40 项发展资产', 'hook': '内 + 外资产清单',
    'why_matters': '''Benson(Search Institute,via Lerner Ch 16)给 40 项 developmental assets —
分内部(20)+ 外部(20)资产:

**外部资产**:
- Support(家庭支持 / 邻居 / 学校 / 父母参与)
- Empowerment(被重视 / 安全感 / 资源 / 服务社区)
- Boundaries(家庭 / 学校 / 邻居 边界 + 成人榜样)
- Constructive Use of Time(创造性活动 / 青年项目 / 信仰社区 / 居家时间)

**内部资产**:
- Commitment to Learning(成就动机 / 阅读 / 学习参与)
- Positive Values(关怀 / 平等 / 诚实 / 责任)
- Social Competencies(规划 / 同理 / 决策 / 文化能力)
- Positive Identity(个人力量 / 自尊 / 目的感 / 未来观)

意义 — 中国父母看清单 — 你家娃有哪些资产已建?哪些缺?
数据 — 高 30+ 资产的青少年:risky behavior 大幅下降 + 学业 + 关系全面好。''',
    'what_to_do': [
        '清单逐项看 — 我家娃有哪些资产',
        '40 项中目标 30+(高 thriving)',
        '外部资产先建(支持 / 边界)',
        '内部资产 = 长期目标',
        'asset 视角 = 替代成绩中心',
    ],
    'failure_mode': '"成绩中心" 立场 — 错。40 项 assets 数据:多维平衡更预测福祉。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Benson', 'G-PERSON-Lerner', 'G-TERM-developmental-assets', 'G-TERM-positive-youth-development'],
    'related_cards': ['C-S0-1522', 'C-S0-1553', 'C-S8-1145', 'C-S8-323'],
    'chapter': 'Ch 16 Lerner PYD (Benson assets)',
    'chapter_offset': 4860000,
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
    with open(path, 'w') as f: f.write(yaml_str)
    return cid


# Write all
person_count = sum(1 for p in PERSONS if 'existed' not in str(write_person(p)))
term_count = sum(1 for t in TERMS if 'existed' not in str(write_term(t)))
card_count = sum(1 for c in CARDS if write_card(c))

print(f"Wrote {person_count} new G-PERSON")
print(f"Wrote {term_count} new G-TERM")
print(f"Wrote {card_count} new cards")
