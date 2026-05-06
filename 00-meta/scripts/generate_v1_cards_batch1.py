"""Phase 12 V1 SRC-030 batch card generator — produces YAML cards from structured data.
All IDs use 1500+ buffer to avoid V4 collision.
"""
import os, yaml

BASE = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'
COMMON = {
    'language': 'zh',
    'status': 'complete',
    'created': '2026-05-04',
    'updated': '2026-05-04',
}

# Each card defined as a dict — no need for individual Write calls
CARDS = [

# =================== Ch 14 Bronfenbrenner Bioecological ===================
{
    'card_id': 'C-S0-1500', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'bronfenbrenner', 'bioecological', '5_systems', 'foundational'],
    'title': 'Bronfenbrenner 5 系统', 'hook': '5 层环境塑造孩子',
    'why_matters': '''Bronfenbrenner & Morris(Lerner V1 Ch 14)给当代发展心理学最权威的环境模型 —
bioecological 5 系统(2006 第 6 版完整版,从 1979 持续修订):
1. microsystem(微观)— 父母 / 同胞 / 老师 直接互动
2. mesosystem(中观)— 家 ↔ 学校 / 家 ↔ 邻居 settings 之间
3. exosystem(外观)— 父母工作 / 政策 / 媒体 间接影响
4. macrosystem(宏观)— 文化 / 经济 / 政治 价值观
5. chronosystem(时观)— 历史变迁 / 个人发展时间
中国父母常只看 micro(家)和 macro(文化),漏 meso(家 ↔ 学校协调)和 exo(父母工作压力外溢)。
完整 5 层视角让你看到孩子问题的根源不止一层。''',
    'what_to_do': [
        '孩子学校问题先看 mesosystem(家 ↔ 学校沟通)',
        '父母焦虑外溢看 exosystem(工作压力)',
        '中国式育儿冲突看 macrosystem(文化变迁)',
        '不要只调 microsystem(管孩子) — 多层同时',
        '5 层都健康 → 孩子问题大多消失',
    ],
    'failure_mode': '只盯 micro 层(管孩子) — 错。问题常在 meso/exo/macro 多层共振。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-bioecological-model', 'G-TERM-microsystem', 'G-TERM-mesosystem', 'G-TERM-exosystem', 'G-TERM-macrosystem', 'G-TERM-chronosystem'],
    'related_cards': ['C-S0-727', 'C-S0-1125', 'C-S6-1064', 'C-S8-323'],
    'chapter': 'Ch 14 Bioecological Model (Bronfenbrenner & Morris)',
    'chapter_offset': 4275000,
},
{
    'card_id': 'C-S0-1501', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'bronfenbrenner', 'PPCT', 'foundational'],
    'title': 'PPCT 4 维框架', 'hook': '过程人环境时间',
    'why_matters': '''Bronfenbrenner 2006 修正版 — 不只是 5 层环境,还多 PPCT 4 维:
- Process(过程)— 近端日常互动是发展引擎(每天爸妈跟娃说话 / 玩耍 / 吃饭)
- Person(人)— 娃自己的气质 / 资源 / 能力 加入互动
- Context(环境)— 5 层环境(microsystem 起)
- Time(时间)— 历史时段 + 个人时间双重
中国父母常只看 Person 一维(我家娃天生 X),忽略 Process 一维(每天的近端互动质量)。
PPCT 框架告诉你 — 发展靠"近端日常互动 × 孩子能力 × 多层环境 × 时间"4 个轴。''',
    'what_to_do': [
        'Process 是核心 — 每天 1 小时高质量陪伴 > 1 周末',
        'Person 看气质 — 配 Chess goodness-of-fit',
        'Context 看 5 层 — 不只家',
        'Time 看历史 — 你 80 后育儿 ≠ 60 后',
        'PPCT 4 维同步看,缺一维就片面',
    ],
    'failure_mode': '只看 Person(我家娃就这样) — 错。Process 和 Context 决定 50%+。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-PPCT-model', 'G-TERM-proximal-processes'],
    'related_cards': ['C-S0-1500', 'C-S0-1125', 'C-S2-940', 'C-S6-1066'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4361672,
},
{
    'card_id': 'C-S0-1502', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'bronfenbrenner', 'proximal_processes', 'foundational'],
    'title': '近端互动是发展引擎', 'hook': '日常陪伴比啥都重要',
    'why_matters': '''Bronfenbrenner 提 proximal processes(近端互动)— 真正驱动发展的是:
父母跟娃每天反复互动的具体活动(读书 / 吃饭 / 玩耍 / 散步 / 谈话)。
不是教育产品,不是专业课,不是设备 — 是日常重复的"足够好"互动。
中国父母常以为 "高级教具 + 名师 + 双语早教 = 好发展" — 错。
Bronfenbrenner 数据:proximal process 质量是发展第一变量,远超教学技术。
意义 — 你每天 1 小时高质量陪伴(蹲下听 / 一起做饭 / 一起读书) > 1 万元早教班。''',
    'what_to_do': [
        '每天 1 小时不被打断的陪伴时间(关手机)',
        '吃饭一起 + 散步一起 + 睡前读书一起',
        '近端互动里反复出现"轮替"(serve & return)',
        '不需要昂贵教具 — 日用品就够',
        '亲子互动质量 > 任何外部资源',
    ],
    'failure_mode': '把娃送早教班自己玩手机 — 错。Proximal process 缺失再多课弥补不了。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-proximal-processes', 'G-TERM-PPCT-model'],
    'related_cards': ['C-S0-1500', 'C-S0-1501', 'C-S0-014', 'C-S2-940'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4361274,
},
{
    'card_id': 'C-S2-1500', 'seg': 's2-1to3mo', 'stages': ['S2'],
    'tags': ['relationships', 'lerner_v1', 'bronfenbrenner', 'microsystem'],
    'title': '微观 = 你跟娃日常', 'hook': '家就是发展实验室',
    'why_matters': '''Bronfenbrenner microsystem 在 1-3 月这个阶段特别关键 —
婴儿 99% 时间在 microsystem(家 + 主要看护人)里。
microsystem 质量 = 你跟娃日常互动的"频率 × 时长 × 反应度 × 情感色调"4 维。
Lerner V1 综述强调 — 这个阶段的 microsystem 质量预测后期社会情绪发展。
但中国家庭常 microsystem 多人同时介入(爸 + 妈 + 爷 + 奶 + 阿姨)— 不一定是坏事 —
关键是几个看护人之间是 mesosystem(协调一致)还是冲突(规则不一)。''',
    'what_to_do': [
        '主要看护人 1-2 个(婴儿期减少混乱)',
        '看护人之间规则统一(meso 健康)',
        '抱 / 喂 / 哄 反应度高(serve & return)',
        '哭就回应不会"惯坏"',
        '微观日常互动 = 发展核心',
    ],
    'failure_mode': '微观看护人 5+ 个轮换规则不一 — 微观质量低,娃焦虑增。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-microsystem', 'G-TERM-proximal-processes'],
    'related_cards': ['C-S0-1500', 'C-S0-1502', 'C-S2-697', 'C-S2-940'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4361343,
},
{
    'card_id': 'C-S6-1501', 'seg': 's6-12to24mo', 'stages': ['S6'],
    'tags': ['relationships', 'lerner_v1', 'bronfenbrenner', 'mesosystem'],
    'title': '中观 = 家学校协调', 'hook': '环境之间也在打架',
    'why_matters': '''Bronfenbrenner mesosystem 在 1-2 岁开始变重要 — 因为娃开始进入第二个 microsystem(早教 / 托班 / 奶奶家)。
mesosystem = 两个 microsystem 之间的关系(家 ↔ 早教 / 家 ↔ 奶奶家)。
关键变量 — 两边规矩是否一致 / 沟通是否顺畅 / 价值观是否兼容。
中国家庭最常 meso 失调:父母 vs 老人(吃饭穿衣管教标准不同)→ 娃来回切换学说谎 / 焦虑 / 走极端。
Lerner V1 数据:meso 失调是 1-3 岁问题行为的主因之一。''',
    'what_to_do': [
        '家和奶奶家规矩商量统一(吃饭 / 屏幕 / 睡眠)',
        '家和早教沟通同步(教学方式 / 行为标准)',
        '不要让娃在两套规矩间切换',
        '主要看护人对齐 1-2 周开个家庭会',
        'meso 协调 = 减少娃焦虑根源',
    ],
    'failure_mode': '家管严奶奶家放养 — 娃学会两面三刀 + 焦虑增。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-mesosystem'],
    'related_cards': ['C-S0-1500', 'C-S0-1501', 'C-S6-1064', 'C-S6-816'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4483850,
},
{
    'card_id': 'C-S8-1132', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['relationships', 'lerner_v1', 'bronfenbrenner', 'exosystem'],
    'title': '外观 = 父母工作影响', 'hook': '上班压力溅到娃',
    'why_matters': '''Bronfenbrenner exosystem 是父母工作 / 政策 / 社区资源 等娃不直接接触但影响娃的层。
最典型 — 父母工作压力外溢:996 / 加班 / 出差 → 父母回家暴躁 / 缺席 / 焦虑 → 娃直接受影响。
Lerner V1 综述指出 — exo 经常是被父母忽视的层(我工作跟孩子没关系吧?)— 错,影响巨大。
中国家长 6 岁前常 exo 失调 → 娃察觉到家长状态差 → 行为出问题(谓之"不听话")。
解决办法不在管娃,在调 exo(父母工作平衡 / 育儿假 / 家庭支持)。''',
    'what_to_do': [
        '父母工作压力 → 不带回家(下楼喘 5 分再进门)',
        '出差期 → 提前告知 + 视频联系',
        '父母情绪先调 exo 再管娃',
        '如可能 — 减少加班 / 调岗 / 育儿假',
        'exo 调整经常比管娃更有效',
    ],
    'failure_mode': '工作压力外溢 + 怪娃"不听话" — 错。问题在 exo 层不在 micro。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-exosystem'],
    'related_cards': ['C-S0-1500', 'C-S6-1501', 'C-S6-822', 'C-S8-323'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4483850,
},
{
    'card_id': 'C-S8-1133', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'bronfenbrenner', 'macrosystem', 'culture'],
    'title': '宏观 = 文化经济政治', 'hook': '大环境定调家',
    'why_matters': '''Bronfenbrenner macrosystem = 文化 / 价值观 / 经济结构 / 政治制度。
中国 0-6 岁家庭面对的 macrosystem 张力:
- 高竞争文化 vs 反内卷新观念
- 经济压力(房贷 / 教育 / 医疗) vs 二胎政策
- 集体主义 vs 个人主义价值观
- 应试教育 vs 素质教育摆动
macro 不是父母能改的 — 但能"看见" → 减少自我归罪。
意义 — 你的育儿焦虑很大一部分是 macro 引起的,不是你不会带娃。
Lerner V1:macro 决定中观和微观的可能性边界。''',
    'what_to_do': [
        '看到 macro → 减少"我做不好"自责',
        '加入支持社群(对抗 macro 孤立)',
        '选学校时考虑 macro 趋势(应试 vs 素质)',
        '跟伴侣 / 老人讨论 macro 差异',
        'macro 不能改但能选择回应方式',
    ],
    'failure_mode': '把所有焦虑归到自己身上 — 错。macro 是 50% 焦虑源,不是你的问题。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-macrosystem'],
    'related_cards': ['C-S0-1500', 'C-S8-1132', 'C-S8-323', 'C-S8-1138'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4483850,
},
{
    'card_id': 'C-S8-1134', 'seg': 's8-3to6yr', 'stages': ['S8'],
    'tags': ['philosophy', 'lerner_v1', 'bronfenbrenner', 'chronosystem', 'historical_time'],
    'title': '时观 = 历史时间维', 'hook': '你不是你妈那一代',
    'why_matters': '''Bronfenbrenner chronosystem = 历史时段 + 个人时间双重维度。
你在 2026 年养孩子 ≠ 你妈在 1995 年养你 — 完全不同的 macrosystem。
- 网络渗透:你娃出生即数字原住民
- 信息爆炸:你能查到 1000 个育儿建议(也焦虑 1000 倍)
- 经济压力:房价 + 教育成本 ≠ 90 年代
- 双职工成常态
chronosystem 视角让你 — 不要照搬上一代经验(你妈说"我那时候你怎么怎么")。
Lerner V1:历史时段决定育儿"可能空间" — 同样 4 岁,2026 年和 1985 年 macro 不同,做法可以不一样。''',
    'what_to_do': [
        '警惕"我那时候 X 怎么不也好好的"',
        '当代育儿挑战和历史不同 — 别直接套老经验',
        '同时不要彻底否定老经验(共睡 / 多人养有传统优势)',
        '区分什么是历史性的什么是普世的',
        'chronosystem 视角 → 选择性继承 / 选择性更新',
    ],
    'failure_mode': '老人/夫妻 chronosystem 视角不同 → 育儿吵架 — 看见就好。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Bronfenbrenner', 'G-TERM-chronosystem'],
    'related_cards': ['C-S0-1500', 'C-S8-1133', 'C-S8-323', 'C-S8-324'],
    'chapter': 'Ch 14 Bronfenbrenner & Morris',
    'chapter_offset': 4483850,
},

# =================== Ch 5 Gottlieb Probabilistic Epigenesis ===================
{
    'card_id': 'C-S0-1503', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'gottlieb', 'probabilistic_epigenesis', 'foundational'],
    'title': '基因不决定 4 层互动', 'hook': '基因 + 环境 4 层塑造',
    'why_matters': '''Gottlieb / Wahlsten / Lickliter(Lerner V1 Ch 5)给当代权威反基因决定论模型 —
probabilistic epigenesis(概率性表观遗传)4 层双向互动:
1. genetic activity(基因活动)
2. neural activity(神经活动)
3. behavior(行为)
4. environment(环境)
4 层之间是 ↑↓ 双向因果,不是单向"基因决定行为"。
意义 — 你不能说"这孩子天生 X"。基因表达受环境影响,环境影响行为,行为影响神经,神经又调基因表达。
中国家长"我家娃天生 X"立场是过时(20 世纪中前期)的 preformist 立场。
当代综述:基因 ≠ 命运 = 概率而非必然。''',
    'what_to_do': [
        '不说"天生" — 说"目前倾向"',
        '改环境 → 改行为 → 影响神经发展',
        '坏脾气娃 5-10 年 environment 改变可能转',
        '基因测试不能预测命运(只是概率)',
        '"环境一辈子可改"是 V1 共识立场',
    ],
    'failure_mode': '"基因决定" 立场 — 错。Gottlieb 综述明确反对,4 层双向。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Gottlieb', 'G-PERSON-Wahlsten', 'G-PERSON-Lickliter', 'G-TERM-probabilistic-epigenesis', 'G-TERM-canalization'],
    'related_cards': ['C-S0-1125', 'C-S0-1500', 'C-S0-722', 'C-S0-008'],
    'chapter': 'Ch 5 Significance of Biology (Gottlieb / Wahlsten / Lickliter)',
    'chapter_offset': 1140000,
},
{
    'card_id': 'C-S0-1504', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'gottlieb', 'canalization', 'waddington'],
    'title': '渠化 = 路径有但不固', 'hook': '基因画路环境定走',
    'why_matters': '''Waddington 的 canalization(渠化)是 epigenesis 的核心比喻 —
基因像在山谷里挖了几条"渠道"(发展路径),孩子的发展 tend to fall into 这些渠道。
但 — 环境扰动可以让发展轨迹脱离渠道,进入另一条。
意义 —
- "深渠道"(强 canalization)= 几乎所有娃都走这条,环境影响小(eg 走路 / 说话)
- "浅渠道"(弱 canalization)= 环境影响大(eg 阅读偏好 / 性格)
中国家长意义 — 哪些发展是"深渠道"(随便都行),哪些是"浅渠道"(投入有效),分清就不焦虑。''',
    'what_to_do': [
        '深渠道(走路 / 说话 / 长牙) — 不需要 push',
        '浅渠道(读书习惯 / 兴趣) — 投入有效',
        '气质大方向 = 深渠道 / 表达方式 = 浅渠道',
        '不在深渠道上"加速"(浪费精力)',
        '在浅渠道上"加投入"(投入回报高)',
    ],
    'failure_mode': '把所有发展都当浅渠道猛投入 — 错。深渠道你 push 也没用。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Gottlieb', 'G-TERM-canalization', 'G-TERM-probabilistic-epigenesis'],
    'related_cards': ['C-S0-1503', 'C-S0-1500', 'C-S0-722', 'C-S2-697'],
    'chapter': 'Ch 5 Gottlieb / Wahlsten / Lickliter',
    'chapter_offset': 1179582,
},
{
    'card_id': 'C-S0-1505', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'gottlieb', 'anti_genetic_determinism'],
    'title': '基因测试不能预测', 'hook': '基因不是命运',
    'why_matters': '''Gottlieb V1 Ch 5 综述明确指出 — 基因测试 / GWAS / 多基因风险评分等
不能预测个人发展结果,因为 4 层互动(基因 / 神经 / 行为 / 环境)是 probabilistic 不是 deterministic。
中国家长越来越多接触基因测试营销 — "你家娃天赋是 X / 易得 Y"等。
V1 立场 — 这些预测最多解释 5-15% 的变异,远不能定个人。
另外 — 基因表达本身受环境影响(epigenetics),所以"测出来"的不是固定的,是当下状态。
意义 — 不要被基因报告唬住,环境干预总是有空间。''',
    'what_to_do': [
        '基因测试报告看 — 不当圣经',
        '"高风险"≠ 一定得病(只是概率)',
        '"低天赋"≠ 没希望(环境可改 50%+)',
        '钱花在 environment 改善 > 花在基因测试',
        '基因 ↔ 环境双向终生',
    ],
    'failure_mode': '基因测试结果决定育儿方向 — 错。误解 V1 综述立场。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Gottlieb', 'G-TERM-probabilistic-epigenesis', 'G-TERM-anti-genetic-determinism'],
    'related_cards': ['C-S0-1503', 'C-S0-1504', 'C-S0-722', 'C-S0-008'],
    'chapter': 'Ch 5 Gottlieb / Wahlsten / Lickliter',
    'chapter_offset': 1231253,
},
{
    'card_id': 'C-S0-1506', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'gottlieb', 'lickliter', 'animal_research'],
    'title': '鸭子实验证明环境', 'hook': '基因 + 蛋内学会的',
    'why_matters': '''Lickliter 的经典实验 — 鸭子在蛋里会学习自己物种的叫声(母鸭子叫)。
但如果在孵化前几天给鸭蛋播放鸡叫,孵出的小鸭跟着鸡跑(印记错乱)。
意义 — 看似"先天本能"的物种识别,其实是"基因 + 出生前环境"互动出来。
迁移到人类 —
- 母语习得不是 100% 先天,是基因 + 妈妈说话出生前听到一起
- "天生听话/不听话"不是基因,是出生前 + 出生后环境一起塑造
- 即使基因相同(双胞胎),环境一改,行为差异立刻显现
中国家长意义 — "天生 X"立场极脆弱,环境影响远比想象大。''',
    'what_to_do': [
        '不要轻易归因"天生"',
        '出生前环境(母亲压力 / 营养 / 情绪)就在塑造娃',
        '出生后头 3 年环境 = 行为基础',
        'Lickliter 数据支持:基因表达受环境直接影响',
        '环境改 = 行为可改(不限月龄)',
    ],
    'failure_mode': '基因决定立场 — 错。Lickliter 鸟类实验明确反驳。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Lickliter', 'G-PERSON-Gottlieb', 'G-TERM-probabilistic-epigenesis'],
    'related_cards': ['C-S0-1503', 'C-S0-1504', 'C-S0-1505', 'C-S0-722'],
    'chapter': 'Ch 5 Gottlieb / Wahlsten / Lickliter',
    'chapter_offset': 1377472,
},
{
    'card_id': 'C-S0-1507', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'equifinality', 'multifinality', 'foundational'],
    'title': '同终点 vs 同起点', 'hook': '殊途同归同途殊归',
    'why_matters': '''发展心理学双向性原则:
- equifinality(同终点) — 不同起点 / 路径可达到同一发展结果(条条大路通罗马)
- multifinality(同起点) — 同样起点不同环境到不同结果(同娘养不同娃)
意义 —
- equifinality:多种育儿方式都能养出健康娃 — 不必追求"唯一正确"
- multifinality:同样基因 / 家庭环境,孩子不同 — 不要责怪自己没"复制"老大成功
Lerner V1 综述把双向性当核心原则 — 不是 X 必然导致 Y,而是 X-Y 关系是概率的。
中国家长意义 — 二胎"同样养"不同娃属正常(multifinality);
不必学某派才能养好(equifinality)。''',
    'what_to_do': [
        '老大老二不同 → multifinality 正常',
        '不必追求"唯一对的方法" → equifinality',
        '同养出大儿子 ≠ 同样会养出小女儿',
        '邻居娃养法 ≠ 一定适合你家',
        '看大方向(健康发展),不强求路径',
    ],
    'failure_mode': '"我老大这样养就行老二肯定也行" — 错,multifinality 警告。',
    'evidence_level': 'A',
    'glossary_refs': ['G-TERM-equifinality', 'G-TERM-multifinality', 'G-TERM-probabilistic-epigenesis'],
    'related_cards': ['C-S0-1503', 'C-S0-1504', 'C-S0-722', 'C-S6-1067'],
    'chapter': 'Ch 5 Gottlieb / Wahlsten / Lickliter + Ch 6 Thelen-Smith',
    'chapter_offset': 1140000,
},

# =================== Ch 6 Thelen-Smith Dynamic Systems ===================
{
    'card_id': 'C-S0-1508', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'thelen', 'smith_lb', 'dynamic_systems', 'foundational'],
    'title': '动态系统理论', 'hook': '发展不是上楼梯',
    'why_matters': '''Thelen & Smith(Lerner V1 Ch 6)给当代发展心理学最有影响力的元理论 —
dynamic systems theory(动态系统论)。
核心 — 发展不是按图纸上楼梯,是 self-organization(自组织)涌现出来的。
对比经典 Piaget 阶段论 —
- Piaget:阶段是预定的(感知运动 → 前操作 → 具体操作 → 形式操作)
- Thelen-Smith:阶段是涌现的,看似有阶段是 attractor 状态短暂稳定
意义 — 你看到娃"突然会某个东西"不是按月龄解锁,是动态系统多个部件凑合到一起 self-organize 出来。
不能拿月龄强行 push(没到 self-organize 条件,你 push 也不会出现)。''',
    'what_to_do': [
        '不按"几个月该会 X"焦虑',
        '看娃自己尝试 + 多个部件准备',
        '提供环境支持,不强行教',
        '看似"突然会" = 动态自组织',
        '看似"退步" = 系统重组中(下一步前奏)',
    ],
    'failure_mode': '"该会 X 月龄" 焦虑 push — 错。动态系统视角是不强行。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-TERM-dynamic-systems-theory', 'G-TERM-self-organization'],
    'related_cards': ['C-S0-1500', 'C-S0-1503', 'C-S0-722', 'C-S2-700'],
    'chapter': 'Ch 6 Dynamic Systems Theories (Thelen & Smith)',
    'chapter_offset': 1395000,
},
{
    'card_id': 'C-S0-1509', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'thelen', 'self_organization'],
    'title': '自组织 = 自发涌现', 'hook': '发展靠自己组装',
    'why_matters': '''self-organization(自组织)是 dynamic systems 核心机制 —
没有"中央控制器"(没有基因蓝图全程指挥),没有"教练 push",
是多个部件(神经 / 肌肉 / 感官 / 环境)在某个时刻凑到一起,涌现出新的能力。
经典例子:婴儿走步不是大脑下"走"的命令,是腿肌肉强度 + 平衡感 + 视觉空间感 + 动机 4 个部件凑合时涌现。
意义 — 中国家长热衷"教技能"(教爬 / 教坐 / 教走) — 但这些都是 self-organize 出来,不是教出来。
Pikler / RIE 派的实操对接 V1 元理论 — 不教翻坐爬站走,提供环境让娃自己 self-organize。''',
    'what_to_do': [
        '不教翻坐爬站走 — 让娃自己 organize',
        '提供环境(空间 / 安全 / 时间)',
        '观察娃的尝试,不打断',
        '看到"突然会" = self-organization 完成',
        '失败时不强行帮 — 让系统继续 organize',
    ],
    'failure_mode': '"教技能" 心态 — 错。self-organize 不是教出来,是组装出来。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-TERM-self-organization', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S0-722', 'C-S2-1502', 'C-S3-941'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},
{
    'card_id': 'C-S0-1510', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'thelen', 'attractors'],
    'title': '吸引子 = 偏好状态', 'hook': '发展有路但可换',
    'why_matters': '''dynamic systems 里 attractors(吸引子)是系统倾向"停在"的几个稳定状态。
比如 — 婴儿在坐姿 / 爬姿 / 站姿是几个 attractor,系统在转换时不稳定(看似"乱"),稳定后看似"会了"。
发展意义 — 看似"阶段"是 attractor 状态短暂稳定。
attractor 不是预定的 — 环境改变可以创造新 attractor 或消除旧 attractor。
中国家长意义 — 孩子的"性格"也是 attractor(动态稳定状态),不是固定的本质。
环境一改,attractor 可以转移。"内向小孩"在新环境可能转活泼 — 不是装的,是 attractor 转移。''',
    'what_to_do': [
        '"性格"是 attractor 不是本质',
        '换环境可以转 attractor(转学校 / 搬家)',
        '"突然变了"是 attractor 重组',
        '不固化"娃就是 X"标签',
        '看动态趋势 > 看静态截面',
    ],
    'failure_mode': '把娃当固定本质 — 错。attractor 视角是动态的。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-TERM-attractors', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S0-1509', 'C-S6-1066', 'C-S6-1067'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},
{
    'card_id': 'C-S0-1511', 'seg': 's0-pregnancy', 'stages': ['S0'],
    'tags': ['philosophy', 'lerner_v1', 'thelen', 'fischer', 'variability'],
    'title': '变异性是发展信号', 'hook': '不稳定不是问题',
    'why_matters': '''Thelen-Smith 和 Fischer 都强调 — variability(变异性)是发展的核心信号,不是噪音。
当孩子在某领域(eg 走路 / 说话 / 情绪管理)显得"不稳定"(一会会一会不会),
不是问题 — 是系统正在 reorganize 进入新的 attractor。
高变异 = 系统在过渡期 = 新能力即将涌现。
低变异 = 系统在稳定期 = 当前能力已固化。
意义 — 中国家长看到娃"反复"(今天会自己穿鞋明天又不会),
立马焦虑"是不是退步" — 错。Thelen-Fischer 综述明确:变异是好事。''',
    'what_to_do': [
        '看到"忽会忽不会" → 不是问题是过渡',
        '稳定一段后突然"乱" → 系统重组中',
        '高变异期更需耐心(下一个稳定即将来)',
        '不强行求"稳定"(那是固化不是发展)',
        '变异 = 发展信号 = 好事',
    ],
    'failure_mode': '"反复" 焦虑当退步 — 错。Thelen 综述:variability 是 signal。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Fischer-K', 'G-TERM-variability-as-signal', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S0-1509', 'C-S0-1510', 'C-S0-1512'],
    'chapter': 'Ch 6 Thelen-Smith + Ch 7 Fischer',
    'chapter_offset': 1440888,
},
{
    'card_id': 'C-S2-1502', 'seg': 's2-1to3mo', 'stages': ['S2'],
    'tags': ['gross_motor', 'lerner_v1', 'thelen', 'self_organization', 'pikler_alignment'],
    'title': '走步是组装出来的', 'hook': '不是教会的是涌现',
    'why_matters': '''Thelen 的经典研究 — 婴儿 1-2 月有"走步反射"(stepping reflex),3-4 月就消失了 —
传统解释:皮层成熟抑制了原始反射。
Thelen 反驳 — 不是反射消失,是腿变胖了(肌肉力跟不上重量)。
证据:把婴儿放到水里(浮力减小重量)— 走步动作回来了。
意义 — 走步能力是动态系统(肌肉 + 重力 + 神经 + 平衡 + 动机)合成,不是大脑发育解锁。
意义 — 中国家长"教走"心态完全错位 — 走步是 self-organize,不需要"教"。
Pikler / RIE 派的实操(不教翻坐爬站走)= V1 元理论的具体应用。''',
    'what_to_do': [
        '不教走 — 给空间 / 时间让娃自己尝试',
        '不要学步车(干扰 self-organize)',
        '观察"几月走"范围 9-18 月都正常',
        '走得早 ≠ 智力高(组装早而已)',
        '走得晚 ≠ 落后(组装条件还没成)',
    ],
    'failure_mode': '"教走" + 学步车 — 干扰自然 self-organization。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-TERM-self-organization', 'G-TERM-dynamic-systems-theory'],
    'related_cards': ['C-S0-1508', 'C-S0-1509', 'C-S2-700', 'C-S5-012'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},
{
    'card_id': 'C-S2-1503', 'seg': 's2-1to3mo', 'stages': ['S2'],
    'tags': ['gross_motor', 'lerner_v1', 'thelen', 'A_not_B'],
    'title': 'A-not-B 不是 Piaget 错', 'hook': '动态视角解错觉',
    'why_matters': '''Piaget 经典 A-not-B error — 8-10 月婴儿明明看到玩具藏在 B 杯,还是去找 A 杯。
Piaget 解释 — 没有"物体永久性"概念。
Thelen-Smith 反驳 — 不是没概念,是动态系统强化了 A 杯的"伸手 attractor"(之前几次找 A 都成功)。
当延迟伸手时间 / 改变姿势 / 减少之前 A 找次数 — A-not-B error 消失。
意义 — Piaget 阶段论很多"概念"其实是动态系统的副产品。
中国家长意义 — 不要拿 Piaget 月龄表给孩子贴标签("我家 8 月还有 A-not-B 是不是落后")。
动态视角:能力随情境变化,不是固定阶段。''',
    'what_to_do': [
        '不拿 Piaget 月龄表当圣经',
        '"概念有没有"看情境(不同情境表现不同)',
        '能力 emergent — 不是预定阶段',
        '8 月找错杯不是"概念"问题是 attractor',
        '动态视角看每一次表现',
    ],
    'failure_mode': 'Piaget 阶段论严格用 — 当代综述视角已超越。',
    'evidence_level': 'A',
    'glossary_refs': ['G-PERSON-Thelen', 'G-PERSON-Smith-LB', 'G-PERSON-Piaget', 'G-TERM-dynamic-systems-theory', 'G-TERM-A-not-B-error'],
    'related_cards': ['C-S0-1508', 'C-S2-1502', 'C-S0-1509', 'C-S2-700'],
    'chapter': 'Ch 6 Thelen & Smith',
    'chapter_offset': 1440888,
},

]

# Write all cards
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

print(f"Wrote {count} cards (batch 1: Ch 14 Bronfenbrenner + Ch 5 Gottlieb + Ch 6 Thelen-Smith)")
print(f"IDs: {[c['card_id'] for c in CARDS]}")
