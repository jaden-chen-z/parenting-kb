"""V1 SRC-030 glossary generation: G-PERSON theorists + G-TERM frameworks"""
import os

GLOSS_DIR = '/Users/jjjjadennnn/Desktop/parenting-kb/40-glossary'

# ====================== G-PERSON 新建 ======================
# 现有(不重建,补 SRC-030 ref): Bandura / Bronfenbrenner / Damon / Erikson / Lerner / Piaget / Vygotsky
# 新建 G-PERSON 清单(V1 章作者 + 关键理论家)
PERSONS = [
    # Ch 2 元理论
    {'id': 'Overton', 'full_zh': '威利斯·欧弗顿', 'full_en': 'Willis F. Overton',
     'pos': 'Temple University 心理学教授',
     'contrib': 'split vs relational metatheory + 关系发展系统元理论奠基',
     'ch': 'Ch 2', 'hits': '300+', 'school': 'Lerner V1 元理论派'},

    # Ch 3 历史
    {'id': 'Cairns-R', 'full_zh': '罗伯特·凯恩斯', 'full_en': 'Robert B. Cairns',
     'pos': 'University of North Carolina, Chapel Hill 教授',
     'contrib': '发展心理学百年史 + Cairns-Cairns 综述 + 跨学科整合',
     'ch': 'Ch 3', 'hits': '150+', 'school': 'Lerner V1 历史综述派'},
    {'id': 'Cairns-B', 'full_zh': '贝弗利·凯恩斯', 'full_en': 'Beverley D. Cairns',
     'pos': 'University of North Carolina 研究员',
     'contrib': '发展心理学史 + 纵向研究方法 + Cairns-Cairns 共著',
     'ch': 'Ch 3', 'hits': '50+', 'school': 'Lerner V1 历史综述派'},

    # Ch 4 文化
    {'id': 'Valsiner', 'full_zh': '雅安·瓦尔西纳', 'full_en': 'Jaan Valsiner',
     'pos': 'Clark University 心理学教授',
     'contrib': '文化心理学 + cultural construction + 个体-文化共建构',
     'ch': 'Ch 4', 'hits': '200+', 'school': 'Lerner V1 文化心理派'},

    # Ch 5 生物
    {'id': 'Gottlieb', 'full_zh': '吉尔伯特·戈特利布', 'full_en': 'Gilbert Gottlieb',
     'pos': 'Center for Developmental Science, UNC Chapel Hill',
     'contrib': 'probabilistic epigenesis 4 层模型 + 反基因决定论',
     'ch': 'Ch 5', 'hits': '200+', 'school': 'Lerner V1 发展心理生物派'},
    {'id': 'Wahlsten', 'full_zh': '道格拉斯·瓦尔斯滕', 'full_en': 'Douglas Wahlsten',
     'pos': 'University of Windsor 心理学教授',
     'contrib': '行为遗传学 + 反基因决定论 + Gottlieb 共著',
     'ch': 'Ch 5', 'hits': '50+', 'school': 'Lerner V1 行为遗传派'},
    {'id': 'Lickliter', 'full_zh': '罗伯特·利克利特', 'full_en': 'Robert Lickliter',
     'pos': 'Florida International University 心理学教授',
     'contrib': '鸟类胚胎实验 + probabilistic epigenesis 实证 + Gottlieb 共著',
     'ch': 'Ch 5', 'hits': '80+', 'school': 'Lerner V1 发展生物派'},

    # Ch 6 动态系统
    {'id': 'Thelen', 'full_zh': '埃丝特·泰伦', 'full_en': 'Esther Thelen',
     'pos': 'Indiana University 心理学教授(已故)',
     'contrib': 'dynamic systems theory + 婴儿走步研究 + self-organization',
     'ch': 'Ch 6', 'hits': '200+', 'school': 'Lerner V1 动态系统派'},
    {'id': 'Smith-LB', 'full_zh': '琳达·史密斯', 'full_en': 'Linda B. Smith',
     'pos': 'Indiana University 心理学教授',
     'contrib': 'dynamic systems theory + 早期物体认知 + Thelen 共著',
     'ch': 'Ch 6', 'hits': '150+', 'school': 'Lerner V1 动态系统派'},

    # Ch 7 动态技能
    {'id': 'Fischer-K', 'full_zh': '柯特·费雪', 'full_en': 'Kurt W. Fischer',
     'pos': 'Harvard Graduate School of Education',
     'contrib': 'dynamic skill theory + 13 层级技能模型 + variability is signal',
     'ch': 'Ch 7', 'hits': '200+', 'school': 'Lerner V1 动态技能派'},
    {'id': 'Bidell', 'full_zh': '托马斯·比德尔', 'full_en': 'Thomas R. Bidell',
     'pos': 'Boston College 教育学教授',
     'contrib': 'dynamic skill theory + Fischer 共著',
     'ch': 'Ch 7', 'hits': '50+', 'school': 'Lerner V1 动态技能派'},

    # Ch 8 整体
    {'id': 'Magnusson', 'full_zh': '大卫·马格努森', 'full_en': 'David Magnusson',
     'pos': 'Stockholm University 心理学教授',
     'contrib': 'holistic-interactionistic + person-oriented approach + 个体路径',
     'ch': 'Ch 8', 'hits': '180+', 'school': 'Lerner V1 整体派'},
    {'id': 'Stattin', 'full_zh': '哈坎·斯塔丁', 'full_en': 'Håkan Stattin',
     'pos': 'Örebro University 社会学教授',
     'contrib': 'holistic-interactionistic + Magnusson 共著',
     'ch': 'Ch 8', 'hits': '80+', 'school': 'Lerner V1 整体派'},

    # Ch 9 心流
    {'id': 'Csikszentmihalyi', 'full_zh': '米哈里·契克森米哈伊', 'full_en': 'Mihaly Csikszentmihalyi',
     'pos': 'Claremont Graduate University 心理学教授',
     'contrib': 'flow theory(心流)+ optimal experience + autotelic personality',
     'ch': 'Ch 9', 'hits': '150+', 'school': 'Lerner V1 心流派'},
    {'id': 'Rathunde', 'full_zh': '凯文·拉松德', 'full_en': 'Kevin Rathunde',
     'pos': 'University of Utah 家庭研究教授',
     'contrib': 'flow + 内在动机 + Csikszentmihalyi 共著',
     'ch': 'Ch 9', 'hits': '50+', 'school': 'Lerner V1 心流派'},

    # Ch 10 行动
    {'id': 'Brandtstadter', 'full_zh': '约亨·布兰德施泰德', 'full_en': 'Jochen Brandstädter',
     'pos': 'University of Trier 心理学教授',
     'contrib': 'action theory of self-development + assimilation/accommodation 双过程',
     'ch': 'Ch 10', 'hits': '150+', 'school': 'Lerner V1 行动理论派'},

    # Ch 11 生命周期
    {'id': 'Baltes', 'full_zh': '保罗·巴尔特斯', 'full_en': 'Paul B. Baltes',
     'pos': 'Max Planck Institute for Human Development(已故)',
     'contrib': 'lifespan developmental psychology + SOC 模型 + wisdom paradigm',
     'ch': 'Ch 11', 'hits': '250+', 'school': 'Lerner V1 生命周期派'},
    {'id': 'Lindenberger', 'full_zh': '乌尔曼·林登伯格', 'full_en': 'Ulman Lindenberger',
     'pos': 'Max Planck Institute for Human Development 主任',
     'contrib': 'lifespan + 生命周期认知 + Baltes 共著',
     'ch': 'Ch 11', 'hits': '80+', 'school': 'Lerner V1 生命周期派'},
    {'id': 'Staudinger', 'full_zh': '乌苏拉·斯陶丁格', 'full_en': 'Ursula M. Staudinger',
     'pos': 'International University Bremen 教授',
     'contrib': 'wisdom 智慧研究 + lifespan + Baltes 共著',
     'ch': 'Ch 11', 'hits': '100+', 'school': 'Lerner V1 生命周期派'},

    # Ch 12 生命历程
    {'id': 'Elder', 'full_zh': '格伦·埃尔德', 'full_en': 'Glen H. Elder Jr.',
     'pos': 'University of North Carolina Carolina Population Center',
     'contrib': 'life course theory + linked lives + 5 大原则',
     'ch': 'Ch 12', 'hits': '200+', 'school': 'Lerner V1 生命历程派'},
    {'id': 'Shanahan', 'full_zh': '迈克尔·沙纳汉', 'full_en': 'Michael J. Shanahan',
     'pos': 'University of North Carolina Chapel Hill 社会学教授',
     'contrib': 'life course + Elder 共著',
     'ch': 'Ch 12', 'hits': '80+', 'school': 'Lerner V1 生命历程派'},

    # Ch 13 文化心理学
    {'id': 'Shweder', 'full_zh': '理查德·施韦德', 'full_en': 'Richard A. Shweder',
     'pos': 'University of Chicago Committee on Human Development',
     'contrib': 'cultural psychology + multiple mentalities + constitutive culture',
     'ch': 'Ch 13', 'hits': '150+', 'school': 'Lerner V1 文化心理学派'},
    {'id': 'Goodnow', 'full_zh': '杰奎琳·古德诺', 'full_en': 'Jacqueline J. Goodnow',
     'pos': 'University of Sydney 行为科学院',
     'contrib': '父母信念 + 文化心理学 + Shweder 共著',
     'ch': 'Ch 13', 'hits': '50+', 'school': 'Lerner V1 文化心理学派'},
    {'id': 'Hatano', 'full_zh': '波多野谊余夫', 'full_en': 'Giyoo Hatano',
     'pos': 'University of the Air, Chiba City, Japan',
     'contrib': '文化与认知 + 日本文化心理学 + Shweder 共著',
     'ch': 'Ch 13', 'hits': '30+', 'school': 'Lerner V1 文化心理学派'},
    {'id': 'LeVine', 'full_zh': '罗伯特·勒文', 'full_en': 'Robert A. LeVine',
     'pos': 'Harvard Graduate School of Education',
     'contrib': '人类学 + 跨文化育儿 + 早期 culture theory',
     'ch': 'Ch 13', 'hits': '50+', 'school': 'Lerner V1 文化心理学派'},
    {'id': 'Markus', 'full_zh': '黑泽尔·马库斯', 'full_en': 'Hazel R. Markus',
     'pos': 'Stanford University 心理学教授',
     'contrib': '互依 vs 独立 self + 文化 self 派 + Shweder 共著',
     'ch': 'Ch 13', 'hits': '80+', 'school': 'Lerner V1 文化心理学派'},
    {'id': 'Miller', 'full_zh': '佩吉·米勒', 'full_en': 'Peggy J. Miller',
     'pos': 'University of Illinois 演讲传播系',
     'contrib': '叙事 + 文化心理学 + Shweder 共著',
     'ch': 'Ch 13', 'hits': '50+', 'school': 'Lerner V1 文化心理学派'},

    # Ch 14 生态系统(Bronfenbrenner 已建,加 Morris)
    {'id': 'Morris', 'full_zh': '帕梅拉·莫里斯', 'full_en': 'Pamela A. Morris',
     'pos': 'MDRC 研究员',
     'contrib': 'bioecological PPCT 模型 + Bronfenbrenner 共著',
     'ch': 'Ch 14', 'hits': '80+', 'school': 'Lerner V1 生态系统派'},

    # Ch 15 PVEST
    {'id': 'Spencer', 'full_zh': '玛格丽特·斯宾塞', 'full_en': 'Margaret Beale Spencer',
     'pos': 'University of Pennsylvania 心理学教授',
     'contrib': 'PVEST + identity formation + racism in development',
     'ch': 'Ch 15', 'hits': '150+', 'school': 'Lerner V1 PVEST 派'},

    # Ch 16 PYD(Lerner 已建,加 Benson 等)
    {'id': 'Benson', 'full_zh': '彼得·本森', 'full_en': 'Peter L. Benson',
     'pos': 'Search Institute 主任(已故)',
     'contrib': 'asset-based youth development + 40 developmental assets + Lerner 共著',
     'ch': 'Ch 16', 'hits': '50+', 'school': 'Lerner V1 PYD 派'},
    {'id': 'Scales', 'full_zh': '彼得·斯卡尔斯', 'full_en': 'Peter C. Scales',
     'pos': 'Search Institute 资深研究员',
     'contrib': 'developmental assets + thriving + Lerner PYD 共著',
     'ch': 'Ch 16', 'hits': '40+', 'school': 'Lerner V1 PYD 派'},
    {'id': 'Hamilton', 'full_zh': '斯蒂芬·汉密尔顿', 'full_en': 'Stephen F. Hamilton',
     'pos': 'Cornell University 人类发展系',
     'contrib': 'youth development + community-based mentoring',
     'ch': 'Ch 16', 'hits': '30+', 'school': 'Lerner V1 PYD 派'},
    {'id': 'Sesma', 'full_zh': '阿图罗·塞斯马', 'full_en': 'Arturo Sesma Jr.',
     'pos': 'Search Institute 研究员',
     'contrib': 'youth assets research + Lerner PYD 共著',
     'ch': 'Ch 16', 'hits': '30+', 'school': 'Lerner V1 PYD 派'},

    # Ch 17 信仰
    {'id': 'Oser', 'full_zh': '弗里茨·奥泽', 'full_en': 'Fritz K. Oser',
     'pos': 'University of Freiburg 教育学教授',
     'contrib': 'religious development stages + 信仰发展 5 阶段',
     'ch': 'Ch 17', 'hits': '50+', 'school': 'Lerner V1 信仰发展派'},
    {'id': 'Scarlett', 'full_zh': 'W. 乔治·斯卡利特', 'full_en': 'W. George Scarlett',
     'pos': 'Tufts University 儿童发展系',
     'contrib': '宗教发展 + 灵性发展综述 + Oser 共著',
     'ch': 'Ch 17', 'hits': '30+', 'school': 'Lerner V1 信仰发展派'},
    {'id': 'Bucher', 'full_zh': '安东·布赫', 'full_en': 'Anton Bucher',
     'pos': 'University of Salzburg',
     'contrib': '儿童宗教发展 + Oser 共著',
     'ch': 'Ch 17', 'hits': '30+', 'school': 'Lerner V1 信仰发展派'},

    # 其他历史性引用人物
    {'id': 'Werner-H', 'full_zh': '海因茨·维尔纳', 'full_en': 'Heinz Werner',
     'pos': 'Clark University(已故)',
     'contrib': 'orthogenetic principle 正交发展 + 比较心理学奠基',
     'ch': 'Ch 1, 3, 7', 'hits': '100+', 'school': 'Lerner V1 关系发展派(经典)'},
    {'id': 'Wapner', 'full_zh': '西摩·瓦普纳', 'full_en': 'Seymour Wapner',
     'pos': 'Clark University(已故)',
     'contrib': 'holistic developmental approach + Werner 学派',
     'ch': 'Ch 1', 'hits': '30+', 'school': 'Lerner V1 关系发展派'},

    # 引用频次高的其他理论家
    {'id': 'Cole-M', 'full_zh': '迈克尔·科尔', 'full_en': 'Michael Cole',
     'pos': 'University of California, San Diego',
     'contrib': '文化心理学 + Vygotsky 美国引介 + 跨文化认知',
     'ch': 'Ch 4, 13', 'hits': '50+', 'school': 'Lerner V1 文化心理派'},
    {'id': 'Rogoff', 'full_zh': '芭芭拉·罗戈夫', 'full_en': 'Barbara Rogoff',
     'pos': 'University of California, Santa Cruz',
     'contrib': 'sociocultural theory + intent participation + 跨文化学习',
     'ch': 'Ch 4, 13', 'hits': '60+', 'school': 'Lerner V1 文化心理派'},
    {'id': 'Riegel', 'full_zh': '克劳斯·里格尔', 'full_en': 'Klaus F. Riegel',
     'pos': 'University of Michigan(已故)',
     'contrib': 'dialectical psychology + 早期生命周期 + 反阶段论',
     'ch': 'Ch 11', 'hits': '30+', 'school': 'Lerner V1 辩证派'},
]

# ====================== G-TERM 框架术语 ======================
TERMS = [
    # 元理论核心
    {'id': 'split-metatheory', 'name_zh': '分裂元理论', 'name_en': 'split metatheory',
     'desc': 'Overton 提出 — 将世界看成对立二分(基因 vs 环境 / 个体 vs 环境 / 心 vs 身),非此即彼立场。\n中国家长接触的 Karp / 鲍秀兰部分 / 行为训练派属于 split。'},
    {'id': 'relational-metatheory', 'name_zh': '关系元理论', 'name_en': 'relational metatheory',
     'desc': 'Overton 提出 — 当代发展心理学元立场。看两端 mutually constituting(互相塑造),不是非此即彼。\n中国家长接触的 蒙氏 / RIE / Lerner / Bronfenbrenner 派属于 relational。'},
    {'id': 'cartesian-dualism', 'name_zh': '笛卡尔二分论', 'name_en': 'Cartesian dualism',
     'desc': 'Descartes 1640 年代心物二分立场 — 衍生出基因 vs 环境 / 主动 vs 被动 等连串二分。\nLerner V1 整卷主张用 relational metatheory 取代。'},
    {'id': 'relational-developmental-systems', 'name_zh': '关系发展系统', 'name_en': 'relational developmental systems (RDS)',
     'desc': 'Lerner-Overton 综合框架 — 当代发展心理学元统合(2006+):\nrelational metatheory + dynamic systems + bioecological + lifespan + holistic 综合。'},
    {'id': 'developmental-science', 'name_zh': '发展科学', 'name_en': 'developmental science',
     'desc': 'Lerner 倡导名词 — 取代 "developmental psychology" 单一学科。\n是 心理 + 神经 + 遗传 + 社会 + 教育 + 政策 跨学科综合。'},

    # 生物 / epigenesis
    {'id': 'probabilistic-epigenesis', 'name_zh': '概率性表观遗传', 'name_en': 'probabilistic epigenesis',
     'desc': 'Gottlieb 模型 — 4 层(基因 / 神经 / 行为 / 环境)双向互动,反基因决定论。\n基因 ≠ 命运 = 概率而非必然。'},
    {'id': 'canalization', 'name_zh': '渠化', 'name_en': 'canalization',
     'desc': 'Waddington 提出 — 基因像挖了山谷渠道,发展倾向走渠道但环境扰动可改路径。\n深渠道(走 / 说话)环境影响小,浅渠道(兴趣 / 习惯)环境影响大。'},
    {'id': 'anti-genetic-determinism', 'name_zh': '反基因决定论', 'name_en': 'anti-genetic determinism',
     'desc': 'Gottlieb / Lickliter / Wahlsten 立场 — 基因不直接决定行为,4 层双向互动。\n基因测试不能预测命运。'},
    {'id': 'anti-determinism', 'name_zh': '反决定论', 'name_en': 'anti-determinism',
     'desc': 'V1 跨章共识 — 反对基因 / 早期 / 阶段 / 文化 任何形式的"决定论"。\n发展是 probabilistic + 多层 + 双向 + 可塑。'},
    {'id': 'anti-reductionism', 'name_zh': '反还原论', 'name_en': 'anti-reductionism',
     'desc': 'V1 跨章共识 — 反对把复杂系统简化为单组件分析。\n看 multi-level 涌现属性,不能从组件预测系统。'},

    # 动态系统
    {'id': 'dynamic-systems-theory', 'name_zh': '动态系统理论', 'name_en': 'dynamic systems theory (DST)',
     'desc': 'Thelen-Smith 当代发展心理学最有影响力元理论。\n发展是 self-organization + emergence + variability,不是预定阶段。'},
    {'id': 'self-organization', 'name_zh': '自组织', 'name_en': 'self-organization',
     'desc': 'dynamic systems 核心机制 — 多个部件凑合到一起涌现新能力,无中央控制器。\n应用 — 婴儿走步是 self-organize 不是教出来。'},
    {'id': 'emergence', 'name_zh': '涌现', 'name_en': 'emergence',
     'desc': '系统达到一定复杂度后涌现出无法从组件预测的新属性。\n应用 — 走 / 说 / 自我意识 都是涌现,不是预设。'},
    {'id': 'attractors', 'name_zh': '吸引子', 'name_en': 'attractors',
     'desc': 'dynamic systems 里系统倾向"停在"的稳定状态(坐 / 爬 / 站等)。\n看似 "阶段" 是 attractor 短暂稳定。环境改可以转 attractor。'},
    {'id': 'variability-as-signal', 'name_zh': '变异性是信号', 'name_en': 'variability as signal',
     'desc': 'Thelen-Fischer 立场 — 发展中"看似不稳定"是 reorganization 进行中,新能力即将涌现。\n不是问题,是好事。'},
    {'id': 'A-not-B-error', 'name_zh': 'A 非 B 错误', 'name_en': 'A-not-B error',
     'desc': '8-10 月婴儿明明看到玩具藏 B 还找 A — Piaget 解读"无物体永久"。\nThelen-Smith 修正:不是没概念,是 A 杯 attractor 强化结果。'},

    # 动态技能
    {'id': 'dynamic-skill-theory', 'name_zh': '动态技能理论', 'name_en': 'dynamic skill theory',
     'desc': 'Fischer 模型 — 技能发展是 constructive web 网状,不是直线楼梯。\n13 层级 + 跨情境差异 + 反复 reorganize。'},
    {'id': 'constructive-web', 'name_zh': '建构网', 'name_en': 'constructive web',
     'desc': 'Fischer 概念 — 技能发展像织网不是搭楼,多领域多技能各自发展。'},
    {'id': 'skill-reorganization', 'name_zh': '技能重组', 'name_en': 'skill reorganization',
     'desc': 'Fischer 命题 — 看似"退步"是 reorganization 征兆,新能力即将涌现。\n应用 — 18 月娃"原来会现在不会"是好事。'},
    {'id': 'skill-levels', 'name_zh': '技能层级', 'name_en': 'skill levels',
     'desc': 'Fischer 13 层级模型 — 比 Piaget 4 阶段细致 10 倍,每 4-6 月一次重组。'},

    # 整体派
    {'id': 'holistic-person', 'name_zh': '整体人', 'name_en': 'holistic person',
     'desc': 'Magnusson 立场 — 把 person 当整体单位,不是把人拆成"变量"分别测。\n人是模式不是变量。'},
    {'id': 'person-oriented-approach', 'name_zh': '人取向方法', 'name_en': 'person-oriented approach',
     'desc': 'Magnusson 方法学 — 跟 variable-oriented 对立。\n看人的整体动态模式,不只单变量分数。'},
    {'id': 'individual-pathway', 'name_zh': '个体路径', 'name_en': 'individual pathway',
     'desc': 'Magnusson 概念 — 每个人发展轨迹独特,群体均值不代表任何具体个体。'},
    {'id': 'individual-differences', 'name_zh': '个体差异', 'name_en': 'individual differences',
     'desc': 'Magnusson + Brazelton 立场 — 没两个娃一样,养孩子要 fit 这个孩子。'},

    # 心流
    {'id': 'flow-theory', 'name_zh': '心流理论', 'name_en': 'flow theory',
     'desc': 'Csikszentmihalyi 提出 — 活动本身就是奖励的状态(intrinsic motivation)。\n4 大特征:挑战/技能匹配 + 即时反馈 + 高度专注 + 自我感消失。'},
    {'id': 'intrinsic-motivation', 'name_zh': '内在动机', 'name_en': 'intrinsic motivation',
     'desc': 'flow 派核心 — 内在驱动 vs 外在奖励 — 长期更可持续 + 培养更深学习。'},
    {'id': 'autotelic-personality', 'name_zh': '内驱型人格', 'name_en': 'autotelic personality',
     'desc': 'Csikszentmihalyi 概念 — "以活动本身为目的"的人格(au=自,telos=目的)。\n2-3 岁形成关键期。'},

    # 行动理论
    {'id': 'action-theory', 'name_zh': '行动理论', 'name_en': 'action theory of self-development',
     'desc': 'Brandtstädter 框架 — 人是主动塑造自己的行动者,不是被动被发展。'},
    {'id': 'assimilation-accommodation', 'name_zh': '同化 vs 调节', 'name_en': 'assimilation vs accommodation',
     'desc': 'Brandtstädter 双过程 — 改环境(assimilate)还是改自己(accommodate)。\n两者交替,不是非此即彼。'},
    {'id': 'intentional-self-development', 'name_zh': '主动自我发展', 'name_en': 'intentional self-development',
     'desc': 'Brandtstädter 概念 — 2-3 岁起人开始主动塑造自己。\n"我自己 / 我要" 是 ISD 起步,不是反抗期。'},

    # 生命周期
    {'id': 'lifespan-theory', 'name_zh': '生命周期理论', 'name_en': 'lifespan developmental theory',
     'desc': 'Baltes 框架 — 一辈子可塑发展,反早期决定论 + 反关键期论。\n0-3 岁重要但不是唯一,30/50/70 岁都还在发展。'},
    {'id': 'plasticity', 'name_zh': '可塑性', 'name_en': 'plasticity',
     'desc': 'Baltes / Greenough — 神经系统可被经验改变的能力,持续到 70+ 岁(只是程度变低)。'},
    {'id': 'SOC-model', 'name_zh': 'SOC 模型', 'name_en': 'Selection-Optimization-Compensation (SOC)',
     'desc': 'Baltes 提出 — 应对发展挑战 3 大策略:Selection(选)+ Optimization(优)+ Compensation(补)。'},
    {'id': 'wisdom-paradigm', 'name_zh': '智慧范式', 'name_en': 'wisdom paradigm',
     'desc': 'Baltes-Staudinger 智慧 5 维度:深识 / 实操 / 价值 / 不确定性 / 跨情境。\n50+ 岁峰值 ≠ IQ 25 岁峰。'},
    {'id': 'critical-period', 'name_zh': '关键期', 'name_en': 'critical period',
     'desc': '必须的发展窗口(过了就不能)— 真正的关键期很少(视觉 / 语言暴露 / 依恋)。\nBaltes 综述 — 概念被媒体夸大。'},
    {'id': 'sensitive-period', 'name_zh': '敏感期', 'name_en': 'sensitive period',
     'desc': '更易学的发展窗口(但非必须)— 跟关键期不同,可补救。\n语言 / 早教 / 兴趣 都是敏感期不是关键期。'},
    {'id': 'anti-early-education', 'name_zh': '反早教焦虑', 'name_en': 'anti-early-education-anxiety',
     'desc': 'Baltes / Pikler / Davies 立场 — 0-3 早教不必焦虑,陪伴质量 > 课程数量。'},

    # 生命历程
    {'id': 'life-course-theory', 'name_zh': '生命历程理论', 'name_en': 'life course theory',
     'desc': 'Elder & Shanahan 5 大原则:lifespan + agency + time-place + linked lives + timing。'},
    {'id': 'linked-lives', 'name_zh': '人生绑定', 'name_en': 'linked lives',
     'desc': 'Elder 原则 — 没有独立人生轨迹,所有人生命跟其他人绑定。\n夫妻 / 父母 / 老人 / 孩子互相影响。'},
    {'id': 'timing-principle', 'name_zh': '时机原则', 'name_en': 'timing principle',
     'desc': 'Elder 原则 — 同事件在不同生命阶段影响不同。\n1-2 岁经历重大事件影响放大 5-10 倍。'},

    # 生态系统
    {'id': 'bioecological-model', 'name_zh': '生态系统模型', 'name_en': 'bioecological model',
     'desc': 'Bronfenbrenner 5 系统:micro / meso / exo / macro / chrono。'},
    {'id': 'microsystem', 'name_zh': '微观系统', 'name_en': 'microsystem',
     'desc': 'Bronfenbrenner 第 1 层 — 父母 / 同胞 / 老师 直接互动环境。'},
    {'id': 'mesosystem', 'name_zh': '中观系统', 'name_en': 'mesosystem',
     'desc': 'Bronfenbrenner 第 2 层 — 两个 microsystem 之间的关系(家 ↔ 学校)。'},
    {'id': 'exosystem', 'name_zh': '外观系统', 'name_en': 'exosystem',
     'desc': 'Bronfenbrenner 第 3 层 — 父母工作 / 政策 / 媒体 间接影响娃的环境。'},
    {'id': 'macrosystem', 'name_zh': '宏观系统', 'name_en': 'macrosystem',
     'desc': 'Bronfenbrenner 第 4 层 — 文化 / 经济 / 政治 / 价值观。'},
    {'id': 'chronosystem', 'name_zh': '时观系统', 'name_en': 'chronosystem',
     'desc': 'Bronfenbrenner 第 5 层 — 历史时段 + 个人发展时间双重维度。'},
    {'id': 'PPCT-model', 'name_zh': 'PPCT 模型', 'name_en': 'Process-Person-Context-Time (PPCT)',
     'desc': 'Bronfenbrenner 2006 修正版 — 4 维框架:近端互动 + 个体 + 环境 + 时间。'},
    {'id': 'proximal-processes', 'name_zh': '近端互动', 'name_en': 'proximal processes',
     'desc': 'Bronfenbrenner 概念 — 父母跟娃每天反复互动的具体活动是发展引擎。\n超过教育产品 + 专业课 + 设备。'},
    {'id': 'serve-and-return', 'name_zh': '一来一回', 'name_en': 'serve and return',
     'desc': '婴儿发起(声 / 看 / 吐舌)→ 父母回应 — 反复互动循环,proximal process 核心。'},

    # PVEST + identity
    {'id': 'PVEST', 'name_zh': 'PVEST 模型', 'name_en': 'Phenomenological Variant of Ecological Systems Theory',
     'desc': 'Spencer 模型 — 在 Bronfenbrenner 5 系统加 perception + identity 维度。\n5 组件:net vulnerability / stress / coping / identity / outcomes。'},
    {'id': 'identity-formation', 'name_zh': '身份形成', 'name_en': 'identity formation',
     'desc': 'Spencer 命题 — identity 不是天生标签,是孩子主动应对环境的产物。\n父母言行进入娃 identity 建构素材。'},
    {'id': 'racism-in-development', 'name_zh': '发展中的种族主义', 'name_en': 'racism in human development',
     'desc': 'Spencer 立场 — racism / classism / sexism 是直接影响儿童发展的环境变量,不只社会问题。'},

    # PYD
    {'id': 'positive-youth-development', 'name_zh': '积极青少年发展', 'name_en': 'Positive Youth Development (PYD)',
     'desc': 'Lerner 等提出 — asset-based 视角,反 deficit model。\n5C 框架(后扩 6C):Competence / Confidence / Connection / Character / Caring (+ Contribution)。'},
    {'id': '5C-framework', 'name_zh': '5C 框架', 'name_en': '5C framework',
     'desc': 'PYD 核心维度:Competence(能力)/ Confidence(自信)/ Connection(连接)/ Character(品格)/ Caring(关怀)。'},
    {'id': 'asset-based-model', 'name_zh': '资产模型', 'name_en': 'asset-based model',
     'desc': 'Lerner / Benson 立场 — 看孩子优势放大,不是看缺点修补。\n反 deficit-based 视角。'},
    {'id': 'self-efficacy', 'name_zh': '自我效能', 'name_en': 'self-efficacy',
     'desc': 'Bandura 概念 — "我能做 X" 的信念。\n经验积累出来,不是夸出来。PYD Confidence 基础。'},

    # 文化心理学
    {'id': 'cultural-psychology', 'name_zh': '文化心理学', 'name_en': 'cultural psychology',
     'desc': 'Shweder 立场 — 不同文化下人有不同 mentality,不只是 "心智 + 文化变量"。'},
    {'id': 'multiple-mentalities', 'name_zh': '多元心智论', 'name_en': 'multiple mentalities',
     'desc': 'Shweder 命题 — 一个心智多种表达,不是普世单一。\n互依 self ≠ 独立 self 的初级阶段,是不同 mentality。'},
    {'id': 'constitutive-culture', 'name_zh': '构成性文化', 'name_en': 'constitutive culture',
     'desc': 'Shweder 立场 — 文化不是 "心智外的衣服",是 "心智本身的构成材料"。'},
    {'id': 'cultural-construction', 'name_zh': '文化建构', 'name_en': 'cultural construction',
     'desc': 'Valsiner 视角 — 娃和文化每天互动共建构(co-construct),不是文化灌入娃。'},
    {'id': 'interdependent-self', 'name_zh': '互依 self', 'name_en': 'interdependent self',
     'desc': 'Markus 概念 — 东亚 self 强调家庭 / 关系 / 角色一体,跟美国 independent self 对立。'},
    {'id': 'cross-cultural-validity', 'name_zh': '跨文化效度', 'name_en': 'cross-cultural validity',
     'desc': 'Shweder / Spencer 警示 — 80% 育儿研究基于美国白人中产,不一定适合其他文化。'},

    # Werner / 经典
    {'id': 'orthogenetic-principle', 'name_zh': '正交发展原则', 'name_en': 'orthogenetic principle',
     'desc': 'Werner 提出 — 发展是从 globally undifferentiated → differentiated and hierarchically integrated。\n婴儿一切笼统,慢慢分化整合。'},
    {'id': 'three-grand-systems', 'name_zh': '三大派系', 'name_en': 'three grand systems',
     'desc': 'Cairns 综述 — 20 世纪心理学三大派:cognitive-developmentalism + psychoanalysis + learning theory。'},
    {'id': 'history-of-developmental-psych', 'name_zh': '发展心理学史', 'name_en': 'history of developmental psychology',
     'desc': 'Cairns & Cairns Ch 3 综述 — 1931-2006 = 75+ 年发展心理学史。'},

    # 跨章
    {'id': 'continuity-discontinuity', 'name_zh': '连续 vs 不连续', 'name_en': 'continuity vs discontinuity',
     'desc': '跨章争议(Ch 6 vs Ch 11)— 发展是渐进累积还是阶段跳跃。\n当代综合 — 看哪一层(神经 continuity / 行为 discontinuity)。'},
    {'id': 'nature-vs-nurture', 'name_zh': '基因 vs 环境', 'name_en': 'nature vs nurture',
     'desc': '跨章核心(Ch 5 + Ch 2 + Ch 11)— 当代综合:基因 ↔ 环境 双向终生互动,不是 2 选 1。'},
    {'id': 'systems-thinking', 'name_zh': '系统思维', 'name_en': 'systems thinking',
     'desc': '跨章共识(Ch 6 + Ch 8 + Ch 14 + Ch 15)— 整体 ≠ 组件之和。\n看 multi-feedback 不只单线 cause-effect。'},
    {'id': 'embodiment', 'name_zh': '具身化', 'name_en': 'embodiment',
     'desc': 'Overton relational 4 原则之一 — 心智不在脑子里飘,是身体 + 环境一起的。'},
    {'id': 'bidirectional-causality', 'name_zh': '双向因果', 'name_en': 'bidirectional causality',
     'desc': 'Overton relational 原则 — 个体影响环境同时被环境影响,不是单向。'},
    {'id': 'emotion-differentiation', 'name_zh': '情绪分化', 'name_en': 'emotion differentiation',
     'desc': 'Werner 正交原则应用 — 婴儿情绪从笼统兴奋/苦恼,4-6 月开始分化为基本情绪。'},
    {'id': 'object-permanence', 'name_zh': '物体永久', 'name_en': 'object permanence',
     'desc': 'Piaget 经典命题 — 婴儿懂物体看不见也存在。Thelen-Smith 修正:context-dependent 不是固定阶段。'},

    # 信仰
    {'id': 'religious-spiritual-development', 'name_zh': '信仰 / 灵性发展', 'name_en': 'religious / spiritual development',
     'desc': 'Oser-Scarlett-Bucher 综述 — 灵性发展不限宗教,是普世发展维度。'},
]


def write_person(p):
    pid = p['id']
    path = os.path.join(GLOSS_DIR, f'G-PERSON-{pid}.yaml')

    # If file exists, update with SRC-030 reference instead of overwriting
    if os.path.exists(path):
        # Skip — Bronfenbrenner / Vygotsky / Lerner / Damon / Erikson / Bandura / Piaget already exist
        return f'{pid} (existed, skipped)'

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
    with open(path, 'w') as f:
        f.write(yaml_str)
    return pid


def write_term(t):
    tid = t['id']
    path = os.path.join(GLOSS_DIR, f'G-TERM-{tid}.yaml')

    if os.path.exists(path):
        return f'{tid} (existed, skipped)'

    desc_lines = t['desc'].split('\n')
    desc_block = '\n'.join('  ' + line for line in desc_lines)

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
    with open(path, 'w') as f:
        f.write(yaml_str)
    return tid


person_count = 0
person_skipped = 0
for p in PERSONS:
    result = write_person(p)
    if 'skipped' in str(result):
        person_skipped += 1
    else:
        person_count += 1

term_count = 0
term_skipped = 0
for t in TERMS:
    result = write_term(t)
    if 'skipped' in str(result):
        term_skipped += 1
    else:
        term_count += 1

print(f"Wrote {person_count} new G-PERSON ({person_skipped} skipped — already exist)")
print(f"Wrote {term_count} new G-TERM ({term_skipped} skipped — already exist)")
print(f"Total new glossary: {person_count + term_count}")
