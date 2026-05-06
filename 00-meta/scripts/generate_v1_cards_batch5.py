"""Batch 5: 段位填充 (s1, s3, s4, s5) + s7 增补"""
import os

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'

CARDS = [
# =================== s1 0-1 月 ===================
{
    'card_id': 'C-S1-1602', 'seg': 's1-newborn', 'stages': ['S1'],
    'tags': ['relationships', 'lerner_v1', 'thelen', 'self_organization', 'newborn'],
    'title': '新生儿能力是涌现', 'hook': '不是基因预设的',
    'why_matters': '''新生儿看似 "本能" 的能力(吸吮 / 抓握 / 视觉追踪)— Thelen-Smith 视角:
不是 "先天预设" 直接出来,是基因 + 子宫环境 + 出生过程 共同 self-organize 涌现。
意义 — 看似 "天生本能" 的吸吮 / 抓握 也是动态系统涌现 — 早产儿这些能力可能延后 2-3 周,因为系统组装条件晚到位。
中国家长意义 — 不要拿 "新生儿应该会 X" 月龄表焦虑早产 / 弱小宝宝。
每个新生儿的能力 emergence 时间不同,跟基因 + 子宫 + 出生 + 出生后头几天经验 一起塑造。
父母工作 — 提供身体接触 + 喂养 + 安静 → 让 self-organize 顺畅完成。''',
    'what_to_do': [
        '不焦虑"新生儿应该会 X"',
        '早产儿能力 emergence 延后属正常',
        '提供身体接触 + 喂养 + 安静',
        'self-organization 需要时间',
        '能力涌现是组装出来的',
    ],
    'failure_mode': '"新生儿就该会 X" 月龄表焦虑 — 错。能力是涌现不是预设。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-TERM-self-organization', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S0-1509', 'C-S0-722', 'C-S1-038'],
    'chapter': 'Ch 6 Thelen & Smith + 新生儿应用',
    'chapter_offset': 1440888,
},

# =================== s3 3-6 月 ===================
{
    'card_id': 'C-S3-1646', 'seg': 's3-3to6mo', 'stages': ['S3'],
    'tags': ['emotional', 'lerner_v1', 'thelen', 'fischer', 'emotion_emergence'],
    'title': '情绪是 4 月开始分化', 'hook': '从混乱到清晰',
    'why_matters': '''4-6 月是情绪 differentiation(分化)关键阶段 —
- 出生:globally aroused(笼统兴奋 / 苦恼)
- 4 月:开始分化 — 高兴 / 害怕 / 生气 / 惊讶 (基本情绪显现)
- 6 月:对人 vs 物 反应不同(社会情绪起步)
Werner 正交原则 + Fischer dynamic skill + Thelen self-organization 三视角合一 —
情绪不是预设,是涌现 — 4 月这个分化是系统重组的成果。
意义 — 中国家长这阶段常 "这娃哭笑都不一样了 不知道为啥" — 是 differentiation 在进行。
父母工作 —
- 帮娃命名情绪("你好像有点生气")
- 不压制情绪表达(让 differentiation 完成)
- 反应与情绪匹配(不要总是同一个反应)''',
    'what_to_do': [
        '帮娃命名情绪 — 高兴 / 难过 / 生气 / 害怕',
        '不压制情绪表达',
        '反应跟情绪匹配(不千篇一律)',
        '4-6 月是情绪 differentiation 关键',
        '看到分化 — 庆祝不焦虑',
    ],
    'failure_mode': '看娃情绪复杂"难带"焦虑 — 错。是 differentiation 进步标志。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Werner-H', 'G-PERSON-Fischer-K', 'G-TERM-emotion-differentiation', 'G-TERM-orthogenetic-principle'],
    'related_cards': ['C-S0-1538', 'C-S0-1542', 'C-S3-942', 'C-S0-725'],
    'chapter': 'Ch 7 Fischer + Ch 3 Werner reference',
    'chapter_offset': 1707604,
},

# =================== s4 6-9 月 ===================
{
    'card_id': 'C-S4-1644', 'seg': 's4-6to9mo', 'stages': ['S4'],
    'tags': ['cognitive', 'lerner_v1', 'thelen', 'object_permanence', 'piaget_revised'],
    'title': '物体永久不是阶段', 'hook': '不是突然懂的',
    'why_matters': '''6-9 月物体永久(object permanence)— Piaget 经典命题"8 月才有"被 Thelen-Smith dynamic systems 修正。
- Piaget — 8 月固定阶段(此前没有)
- 现代综述(via V1 Ch 6) — 物体永久能力是 emergent + context-dependent —
  - 情境支持高(熟悉环境 / 短延迟 / 简单藏)→ 4 月就能见
  - 情境支持低(陌生 / 长延迟 / 复杂藏)→ 12 月还会失败
- 不是 "懂 / 不懂" 二分,是 "在不同情境下有不同表现"
意义 — 中国家长不必焦虑 "我家 8 月还认不出物体藏哪是不是落后"。
- 在简单情境下你家娃可能 4 月就有物体永久
- 在复杂情境下到 12 月 + 还可能失败
- 都是正常 dynamic 表现,不是阶段问题''',
    'what_to_do': [
        '不焦虑"几月有物体永久"',
        '简单情境(熟悉 / 短藏)— 早能见',
        '复杂情境 — 晚能见',
        '不是阶段是动态能力',
        'Piaget 月龄表过简化',
    ],
    'failure_mode': '拿"8 月物体永久"标准焦虑 — 错。Thelen 修正:context-dependent。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-PERSON-Piaget', 'G-TERM-object-permanence', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S2-1503', 'C-S0-1542', 'C-S4-944'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},

# =================== s5 9-12 月 ===================
{
    'card_id': 'C-S5-1643', 'seg': 's5-9to12mo', 'stages': ['S5'],
    'tags': ['gross_motor', 'lerner_v1', 'thelen', 'walking', 'dynamic_systems'],
    'title': '走步靠组装非月龄', 'hook': '9-18 月都正常',
    'why_matters': '''9-12 月开始进入走步发展段 — Thelen dynamic systems 视角:
走步不是月龄解锁,是 4 个部件 self-organize 涌现:
1. 腿肌肉强度(支撑体重)
2. 平衡感(前庭 + 视觉空间)
3. 神经 motor cortex 成熟
4. 内在动机(想去某地)
4 个部件凑齐时间不同 — 不同娃 9 月到 18 月范围都正常。
Adolph 数据(Lerner V2)— 同月龄学走能力差异极大。
意义 — 中国家长 "12 月不走是不是有问题" 焦虑 → V1 + V2 综述:9-18 月范围,无需担心。
干预只在 18 月仍未尝试走或单侧使用异常时考虑。''',
    'what_to_do': [
        '9-18 月走都正常',
        '不强求"几月学会"',
        '不学步车(干扰 self-organize)',
        '提供安全空间 + 跌倒缓冲',
        '17-18 月仍未尝试 → 看医生',
    ],
    'failure_mode': '"12 月不走" 焦虑 — 错。9-18 月范围正常。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-TERM-dynamic-systems-theory', 'G-TERM-self-organization'],
    'related_cards': ['C-S0-1508', 'C-S2-1502', 'C-S5-012', 'C-S5-041'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},

# =================== s7 增补 ===================
{
    'card_id': 'C-S7-1607', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'caring'],
    'title': '同理心 5C 的 caring', 'hook': '关怀是 PYD 维度',
    'why_matters': '''Lerner PYD 5C 中 Caring(关怀)— 同理 + 利他 — 是发展维度,不是天生有/没有。
2-3 岁是关键发展期 —
- 24 月 — instrumental helping(帮够不到的东西)
- 30 月 — 共情情绪(看别人哭也难过)
- 36 月 — 主动安慰(给安慰物 / 拍手 / 抱)
意义 — 中国家长常 "她还小不懂" 跳过教 caring — 错。
Eisenberg 综述 + Lerner PYD 一致:caring 在 2-3 岁开始,父母示范 + 反思 + 鼓励是发展引擎。
做法 —
- 父母示范 caring(对老人 / 对邻居 / 对宠物)
- 让娃参与照顾(浇花 / 喂宠物 / 给奶奶递东西)
- 看到娃 caring 行为 — 描述不评价("你给奶奶递水真贴心")
- 不强迫(强迫的不是 caring 是表演)''',
    'what_to_do': [
        '父母示范 caring(对老人 / 邻居 / 宠物)',
        '让娃参与照顾(浇花 / 喂宠物)',
        '描述不评价 — "你给奶奶递水真贴心"',
        '不强迫(强迫的不是 caring)',
        'PYD 5C 维度 — 长期培养',
    ],
    'failure_mode': '"她还小不懂"跳过 caring 培养 — 错。2-3 岁是关键期。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1522', 'C-S6-1505', 'C-S7-1602', 'C-S2-941'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
},
{
    'card_id': 'C-S7-1608', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'confidence'],
    'title': '自信不是夸出来', 'hook': '能做的事多自信',
    'why_matters': '''Lerner PYD 5C 中 Confidence(自信)— 不是夸出来,是 "我能做 X" 经验积累出来。
中国家长 confidence 误区 —
- 误区 1 — 反复夸"你真棒"(美式) → 但娃没做啥实事 → 表面自信内里空
- 误区 2 — 反复批评 → 自信被压
- 正确 — 让娃做能完成的事 + 描述他做的(不评价)
2-3 岁 confidence 培养 —
- 让娃自己穿鞋(就算慢)
- 让娃自己吃饭(就算撒)
- 让娃自己选衣服(就算搭配怪)
- 让娃自己擦桌子(就算擦不干净)
关键 — "他做的" 经验积累 = 自信根。
"你真棒" 是水中花 — Bandura 自我效能理论(via Lerner)同立场。''',
    'what_to_do': [
        '让娃做能完成的事(就算慢 / 撒)',
        '描述行为 — 不空夸"你真棒"',
        '"他做的"积累 = 自信根',
        '不剥夺尝试机会(怕慢 / 怕乱)',
        'Bandura 自我效能立场',
    ],
    'failure_mode': '"你真棒"反复夸 — 培养表面自信内里空虚。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-PERSON-Bandura', 'G-TERM-positive-youth-development', 'G-TERM-self-efficacy'],
    'related_cards': ['C-S0-1522', 'C-S7-1602', 'C-S7-754', 'C-S7-1606'],
    'chapter': 'Ch 16 Lerner PYD + Bandura ref',
    'chapter_offset': 4891805,
},
{
    'card_id': 'C-S7-1609', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'competence'],
    'title': '能力是多维不只学业', 'hook': '社交体能也是能',
    'why_matters': '''Lerner PYD 5C 中 Competence(能力)— 学业 / 社交 / 体能 / 艺术 / 自调 多维度,不只学业。
中国家长常 — 2-3 岁就开始 学业 competence(数 / 字 / 双语) → 单维 → 后期失衡。
PYD 平衡视角 —
- 学业能力(认字 / 数 / 概念)— 这阶段适度
- 社交能力(交友 / 谈判 / 共享)— 这阶段重要(同伴互动多)
- 体能(爬 / 跑 / 跳 / 平衡)— 这阶段必须
- 艺术(画 / 唱 / 跳)— 这阶段易培养
- 自我调节(等 / 转移 / 选择)— 这阶段开始
意义 — 5 维度都要,不要 1 维独大。
具体 — 每周回顾 — 这周 5 维度娃各发展了什么?哪维度最弱?下周怎么补?''',
    'what_to_do': [
        '5 维度同步看(每周回顾)',
        '学业能力适度,不独大',
        '社交能力 — 多 playgroup',
        '体能 — 户外 1+ 小时/天',
        '自我调节 — 鼓励选择 + 等待',
    ],
    'failure_mode': '学业能力独大(2-3 岁就读认字)— 错。PYD 视角:5 维平衡。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-5C-framework'],
    'related_cards': ['C-S0-1522', 'C-S7-1607', 'C-S7-1608', 'C-S7-754'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
},
{
    'card_id': 'C-S7-1610', 'seg': 's7-24to36mo', 'stages': ['S7'],
    'tags': ['philosophy', 'lerner_v1', 'spencer', 'identity_2_3'],
    'title': '2-3 岁身份起步', 'hook': '我是 X 开始建',
    'why_matters': '''Spencer PVEST 应用到 2-3 岁 — identity 形成起步阶段。
2-3 岁娃开始有 — "我是 X 的人" 早期叙事:
- "我是哥哥 / 姐姐"(家庭角色)
- "我是 X 班的"(早教 / 托班归属)
- "我喜欢 X"(兴趣身份)
- "我会 X"(能力身份)
意义 — 父母这阶段的言行进入娃 identity 建构素材。
- 反复说"你就是个慢孩子" → 进入 identity → 成"我是慢的"
- 反复说"你能办到" → 进入 identity → 成"我能办到"
具体做法 —
- 注意自己反复用的"标签语"
- 描述行为不评价人(行为可改 标签固化)
- 让娃接触多元角色(避免单一身份)
- 鼓励"我是 X" 多元化叙事(我是哥哥 + 我喜欢车 + 我会跑)''',
    'what_to_do': [
        '注意反复用的"标签语"',
        '描述行为不评价人',
        '让娃接触多元角色',
        '鼓励 identity 多元叙事',
        '父母言行 = identity 建构素材',
    ],
    'failure_mode': '反复贴标签(她就是 X)— 进入 identity 长期固化。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Spencer', 'G-TERM-PVEST', 'G-TERM-identity-formation'],
    'related_cards': ['C-S0-1532', 'C-S6-1510', 'C-S6-1066', 'C-S7-996'],
    'chapter': 'Ch 15 Spencer PVEST',
    'chapter_offset': 4551844,
},

# =================== s2 增补 ===================
{
    'card_id': 'C-S2-1505', 'seg': 's2-1to3mo', 'stages': ['S2'],
    'tags': ['relationships', 'lerner_v1', 'bronfenbrenner', 'proximal_processes', 'newborn'],
    'title': '近端互动从 2 月起', 'hook': '日常陪伴是引擎',
    'why_matters': '''Bronfenbrenner proximal processes 在 1-3 月开始进入"高效期" —
婴儿开始能够 social referencing(看你脸读情绪),
Serve & return(serve & return)互动质量决定神经发展。
- 婴儿"发起"(发出声 / 看你 / 吐舌)= serve
- 你"回应"(回声 / 看回去 / 吐舌)= return
- 反复 serve-return 循环 = proximal process 核心
中国家庭多人养情境下 — proximal process 数量足够,但质量参差(不同看护人反应度不同)。
关键 — 主要看护人(妈 / 奶奶 / 阿姨)中至少 1 个反应度高 + 一致 → 婴儿大脑 wiring 健康。
意义 — 不需要"专门陪玩",日常喂 / 抱 / 哄 / 换尿布时的反应度就是 proximal process。''',
    'what_to_do': [
        '婴儿 serve(声 / 看 / 吐舌) → 你 return',
        '日常喂 / 抱 / 哄 / 换尿布反应度高',
        '不需要"专门陪玩"',
        '主要看护人反应度高 + 一致',
        '近端互动 = 神经发展引擎',
    ],
    'failure_mode': '婴儿哭闹冷静处理"不能宠" — 错。Serve-return 缺失影响神经 wiring。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-proximal-processes', 'G-TERM-serve-and-return'],
    'related_cards': ['C-S0-1500', 'C-S0-1502', 'C-S2-1500', 'C-S0-014'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4361274,
},

# =================== s8 增补 ===================
{
    'card_id': 'C-S8-1145', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'lerner', 'PYD', 'asset_based'],
    'title': '资产视角看孩子', 'hook': '看优势不是看缺',
    'why_matters': '''Lerner PYD 核心立场转变 — 从 deficit-based 转 asset-based 育儿视角。
deficit 视角 — "我家娃数学差 / 不爱社交 / 不爱阅读 / 没耐性 / 内向" → 拼命补缺。
asset 视角 — "我家娃有 X 优势 / 兴趣 / 关系 / 强项" → 放大 + 衍生。
3-6 岁这阶段父母容易陷 deficit 视角 — 因为入学焦虑放大了缺点感知。
PYD 数据 — asset-based 育儿的孩子:
- 自尊更高(因为感到有价值)
- 学习更主动(优势带学习)
- 关系更好(被看到优势)
- 长期成就更高(asset 自然衍生其他能力)
意义 — 父母视角从"我家娃差什么"换成"我家娃强什么 + 怎么放大",
这一换是 PYD 育儿的关键转变。''',
    'what_to_do': [
        '每天找娃 1 个优势(具体)',
        '不在缺点上反复 nag',
        '"她最近 X 进步了"叙事',
        '优势带学习(用强项学新)',
        'asset > deficit 育儿视角',
    ],
    'failure_mode': '"她数学差 / 不爱社交"立场长期 nag — 培养自卑根。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lerner', 'G-TERM-positive-youth-development', 'G-TERM-asset-based-model'],
    'related_cards': ['C-S0-1522', 'C-S6-1505', 'C-S8-1136', 'C-S8-323'],
    'chapter': 'Ch 16 Lerner PYD',
    'chapter_offset': 4891805,
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

print(f"Wrote {count} cards (batch 5: 段位填充 s1/s3/s4/s5 + s7/s2/s8 增补)")
