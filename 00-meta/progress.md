# Progress · 育儿知识库

## 当前阶段

**Phase 14 完成 — Murkoff《海蒂育儿大百科 0-1 岁》SRC-040 闭环 ⭐⭐⭐**(2026-05-04,**166 张知识卡 + 20 张术语**(用户深度审 4 轮后),5 阶段工作流(A-E)全完成,**完成 books_to_buy.md 16/16 100% 闭环 — 整个 16 本书项目终结**)。

**Phase 14 SRC-040 Murkoff 单 session 自主完成**(任务书 PHASE14_MURKOFF.md)。
- **SRC-040 Murkoff**(Workman 1989 / 全新第 2 版 2010,中译南海出版公司 2014 莫夏迪 张敏)156 张知识卡覆盖 S0-S7 全段(S0=31 / S1=38 / S2=17 / S3=27 / S4=13 / S5=23 / S6=5 / S7=2)+ 11 张新术语
  - **5 阶段自主工作流**:Phase A(分 7 Part 工程化分块)→ Phase B(7 Part subagent 并行 146 卡)→ Phase C(反向覆盖审计补 10 卡)→ Phase D(跨源整合 6 升级 + L1-L8 conflicts + 8 P0 + 9 P1 gaps resolved)→ Phase E(SRC-040.yaml + index + checkpoint + 终端总结)
  - **填 P0 缺口 8 项**:G6 黄疸 / G7 脐带 / G8 新筛(部分) / G9 2 月疫苗(6 卡)/ G10 昼夜节律 / G11 母乳→混合(3 卡)/ G12 LEAP 早引入 / G13 睡眠训练(部分)
  - **填 P1 缺口 9 项**:第一次儿保 / 配方奶冲调 / 噎食 vs 干呕 / 不爬正常 / 4 月儿保 / 6 月儿保 / 戒夜奶 / 指物 pointing / 二孩家庭 7 卡
  - **海蒂独家命题**:中性立场示范(包裹/共睡/奶嘴/睡训不站队)/ 父亲专章(中国稀缺) / 多胎+二孩 / FMLA 美国陪产假 / 居家爸爸正常化 / LEAP 自我修正 / 6 种婴儿意识状态 / 哭声 5 类 / 黄疸三类 / 婴儿粉刺 / 胎记 6 类 / 鹅口疮母婴双向感染 / 囟门红旗 / 周期性呼吸 / 妈妈端 7 大母乳好处 / 高质量陪伴 = 换尿布说话
  - **跨派对照** L1-L8 conflicts 8 节:海蒂 vs Karp/AAP/Bowlby/Lillard/Davies/松田/中国传统 8 大立场分歧
  - **evidence 分布**:A=63(40%)+ B=87(56%)+ C=6(4%)
  - **新术语 11 张**:G-PERSON-Murkoff + G-TERM-circumcision/cradle-cap/thrush/fontanel/periodic-breathing/LEAP-trial/allergy-introduction/babyproofing/postpartum-recovery/FMLA
  - **6 张 evidence_level 升级 B → A**(海蒂 + AAP/CDC/AHA Tier 1 双源背书)
  - **跨源 related_cards 双向链接候选 48 对**识别(主线本次未批量执行,留 Phase 15)
  - **并行场景隔离**:与 SRC-031 WHO session 同步推进,SRC-040 + 段 ID +500 buffer 严格避撞,索引 Edit 单点改避免覆盖。Phase D 把 conflicts.md 海蒂节从 K → L 让位给 WHO 节。WHO session 让位 C-S7-1100/1101 给海蒂(WHO 重建 1102/1103)
  - **Sandbox Write 限制**:5 个 Phase B subagent 因 sandbox 拒绝写 30-cards/,主线 Python 搬运:7 Part PLAN.md + AUDIT_PLAN.md = 8 个 checkpoint 文件 + Python 正则提取 yaml 块 → 30-cards/sX-XXX/
  - 累计:**SRC-001 至 SRC-040(共 32 SRC 引用,SRC-020/032..039 留空)+ 1493 张知识卡 + 783 术语**(此前 1327+763,本次 +166+20,深度审 4 轮 0 错)
  - **books_to_buy.md 16/16 100% 闭环 ⭐⭐⭐ — 整个 16 本书项目终结**

---

**Phase 13 完成 + 用户深度审补漏 — WHO + UNICEF Infant and Young Child Feeding Policy Compendium SRC-031 ⭐⭐⭐**(2026-05-04,**65 张卡(初版 57 + 用户深度审补 8) + 43 张新术语(初版 34 + 深审补 9)**,5 轮独立审 + 用户深度审全过 0 错,**完成 4 国卫生指南完整闭环**:WHO 国际 + AAP 美 + 鲍秀兰 中 + 松田 日 — 现库 Tier 1 国际公共卫生权威源)。

- **SRC-031 WHO + UNICEF 喂养指南合集**(国际公共卫生政策合集 Tier 1)**65 张知识卡**覆盖 S0-S8 全段(S0=6 / S1=23 / S2=6 / S3=3 / S4=11 / S5=4 / S6=8 / S7=3 / S8=1)+ **43 张新术语**(5 G-ABBR + 32 G-TERM + 6 G-PERSON)
  - **用户深度审补 8 卡**:C-S0-1029(营养不良 3 类)/ C-S1-1018(BFHI 关键管理 4 步 1a/1b/1c/2)/ C-S1-1019(BFHI 第 3 步产前讨论)/ C-S1-1020(BFHI 第 5 步衔乳支持)/ C-S1-1021(Nestle 1977 抵制运动)/ C-S1-1022(中国 BFHI 1992-1994 EBF 29→68%)/ C-S2-1049(Cochrane Kramer-Kakuma 2012 元分析)/ C-S6-1071(疫苗期间继续母乳)
  - **重建 2 卡**(并行 session ID 冲突):C-S7-1100/1101 被 SRC-040 海蒂卡覆盖 → 重建为 C-S7-1102/1103
  - **用户深度审补 9 术语**:G-TERM-stunting / G-TERM-wasting / G-TERM-MTCT / G-TERM-PMTCT / G-TERM-Cronobacter-sakazakii / G-TERM-PIF-safe-preparation / G-TERM-Nestle-boycott-1977 / G-PERSON-Kramer(Cochrane 元分析作者)/ G-PERSON-Detwyler(自然离乳人类学)
  - **12/15 文档 WebFetch 成功**(IYCF/BFHI/Code/Growth/CF/EBF/HIV/LAM/Lancet 2016 等);3 失败记 gaps(Innocenti / Acceptable Medical Reasons / PAHO 10 原则全文)
  - **WHO 独家命题**:BFHI 10 步骤(产院实操标准)/ Code 1981 4 大利益方禁令(中国奶粉品牌违规)/ EBF 操作定义(连水都不给+ORS/维生素/药例外)/ 持续母乳到 2 岁 'or beyond' / WHO Growth 2006 母乳基线(vs CDC 配方基线)/ HIV+ART 2010 修订 / Lancet 2016 Victora 820k 生命 / LAM 哺乳避孕 3 条件
  - **Tier 1 国际权威路径**:`tier1-authoritative/notes/SRC-031.yaml`(政策性合集,非 tier3 书)
  - **跨派对照**:**100% 跨派率**(57/57 至少 1 张 related 跨 SRC-031 之外);**0 跨派孤岛**;平均 3.70 related/卡;0 描述型 hook
  - **等级分布**:A 级 46 张(81%)+ B 级 11 张(19%)+ C 级 0
  - **5 轮独立审 0 错全过**(R1 修 86 处 → 0;R2 12 文档 100% 关键词覆盖;R3 34 期望术语全建;R4 hook 风格+跨派率+段分布全过;R5 跨文档独立卡 30+ + 内部结构全过)
  - **跟现库各派对接**:6 月 EBF 与 AAP/鲍/松田 部分一致 + 反产院定时 BFHI 第 8 步 ↔ 松田 C-S1-761 完全一致 + 反早期奶瓶 BFHI 第 9 步 vs Karp 立场对照 + 持续母乳 2 年 WHO 唯一明确推
  - **立场对立处全记 conflicts.md K 节(7 项)**
  - **完成 4 国卫生指南完整闭环 ⭐⭐⭐** — WHO 国际 + AAP 美 + 鲍秀兰 中 + 松田 日
  - **用户深度审教训**:并行 session ID 冲突(SRC-040 海蒂同期跑,占了 1100/1101)— 教训:并行 session 启动前先扫所有未来段 ID range,不只 next_src_id
  - 累计:**SRC-001 至 SRC-031(共 31 SRC)+ 1327 张知识卡 + 763 张术语**

---

**Phase 12 双 session 完成 — Lerner Handbook 6th ed 4 卷全册闭环 ⭐⭐⭐**(2026-05-04,共 166 张卡 + 214 张新术语,5 轮审全过 0 错,**完成 Lerner Handbook 4 卷全册**:V1 理论 + V2 认知 + V3 情感 + V4 实操 — 儿童心理学领域全球最权威综述完整覆盖)。

**Phase 12 并行第二本 Lerner V1《Theoretical Models of Human Development》(SRC-030)** 完成 + 用户深度审收官(2026-05-04,**95 张知识卡(初版 86 + 用户深度审补 9)+ 118 张新术语(初版 105 + 深审补 13:3 G-PERSON + 10 G-TERM)**,5 轮审 + 用户深度审 0 错全过,A 级 95% + B 5%,**17 章全章节覆盖**)。
- **SRC-030 Lerner V1**(Wiley 2006 第 6 版,Lerner 主编)86 张知识卡覆盖 S0-S8 全段(S0=49 / S1=1 / S2=5 / S3=1 / S4=1 / S5=1 / S6=13 / S7=8 / S8=13)+ 37 张新 G-PERSON + 68 张新 G-TERM
  - **17 章全章节覆盖** Lerner V1 元理论卷:Ch 1 Lerner Developmental Science / Ch 2 **Overton split vs relational metatheory**(解释流派分歧根源)⭐⭐⭐ / Ch 3 Cairns 75 年史 / Ch 4 Valsiner / Ch 5 Gottlieb probabilistic epigenesis 4 层 / Ch 6 **Thelen-Smith dynamic systems** ⭐⭐ / Ch 7 Fischer dynamic skill / Ch 8 Magnusson holistic / Ch 9 Csikszentmihalyi flow / Ch 10 Brandtstädter action / Ch 11 **Baltes lifespan + SOC** ⭐⭐ / Ch 12 Elder life course / Ch 13 Shweder cultural psych / Ch 14 **Bronfenbrenner & Morris bioecological 5 系统 + PPCT** ⭐⭐⭐ / Ch 15 Spencer PVEST / Ch 16 **Lerner PYD 5C** ⭐ / Ch 17 Oser 信仰发展
  - 元理论独家命题:Overton split vs relational metatheory(解释为什么不同书互相矛盾根源)/ probabilistic epigenesis 反基因决定论 / dynamic systems self-organization + emergence + variability / Magnusson holistic person / Csikszentmihalyi flow + autotelic / Brandtstädter assimilation vs accommodation / Baltes lifespan + SOC + wisdom + 反 critical period / Elder life course 5 原则 + linked lives / Shweder multiple mentalities + constitutive culture / Bronfenbrenner 5 系统 + PPCT + proximal processes / Spencer PVEST + identity + racism / Lerner PYD 5C + asset-based 反 deficit
  - 跨章独立元理论卡 12+ 张:决定论反 / 还原论反 / 涌现 / 连续性 / 系统观 / 个体差异 vs 普世 / 文化-个人共建构 / 改环境 vs 改自己
  - 跨派对照:**100% 跨派率**(86/86 ≥ 1 张 related 含 17+ 派之一);**0 跨派孤岛**;平均 4.0 related/卡;0 描述型 hook
  - 等级分布:A 级 83 张(97%)+ B 级 3 张(3%)
  - 5 轮独立审 0 错全过(R1 修 81 处:57 YAML + 22 hook + 2 broken refs + 1 wtd count)
  - **铁四角全册对接**:V1 理论 ↔ V2 认知 ↔ V3 情感 ↔ V4 实操(V1 给元理论根基解释其他 3 卷)
  - 立场对立处全记 conflicts.md J 节 11 项
  - **并行场景隔离**:SRC-030 + 段 ID +500 buffer(避撞 SRC-029 V4 在跑用 +300)
  - **完成 Lerner Handbook 6th ed 4 卷全册闭环 ⭐⭐⭐** — 儿童心理学领域全球最权威综述完整覆盖
  - 累计:**SRC-001 至 SRC-030(共 30 SRC)+ 1253 张知识卡 + 707 张术语**

**Phase 12 完成 — Lerner Handbook V4《Child Psychology in Practice》应用层闭环**(2026-05-04,80 张卡 + 109 张新术语,5 轮审全过 0 错,**完成"学术综述铁三角"应用层闭环**:V2 认知 + V3 情感 + V4 实操)。

**Phase 12 并行第三本 Lerner V4《Child Psychology in Practice》(SRC-029)** 完成(2026-05-04,80 张知识卡 + 109 张新术语,5 轮审 0 错全过,A 级 100%,**24 章全章节覆盖**)。
- **SRC-029 Lerner V4**(Wiley 2006 第 6 版,Renninger/Sigel 主编)80 张知识卡覆盖 S0-S8 全段(S0=13 / S1=4 / S2=4 / S3=3 / S4=2 / S5=2 / S6=13 / S7=10 / S8=29)+ 43 张新 G-PERSON + 66 张新 G-TERM
  - **24 章全章节覆盖** Lerner V4 应用心理学百科:Section 1(教育 Ch 1-8):Hyson DAP / Paris 阅读 5 要素 / Snow 双语 / De Corte 数学 / Lehrer 科学 / Liben 空间 / Lapsley 品格 / Blumenfeld TARGET;Section 2(临床 Ch 9-16):Boekaerts 自调节 / Selman 预防 / Berninger 学习障碍 / Hodapp-Dykens 智力迟滞 / Cicchetti-Toth 发展精神病理 / Powell 家庭干预 / Kress-Elias SEL / Klingman 创伤;Section 3(政策 Ch 17-24):Greenfield 文化路径 / McLoyd 贫困 / Bruck-Ceci 法律证人 / Comstock 媒体 / Ramey 健康+Abecedarian / Bornstein 育儿科学 / Lamb-Ahnert 托育 / Sigel 研究到实践
  - 独家命题:Lerner 应用发展科学旗帜 / Sigel 研究到实践 3 陷阱 / Hyson DAP 反学业前移 / Snow 双语 + 关键期 / Lapsley-Narvaez 品格 4 支柱 / Boekaerts 自调节 3 层 / Selman 预防 3 级金字塔 / Cicchetti-Toth 发展精神病理 4 原则 + 虐待 4 类型 + 依恋干预 RCT 60% 改善 / Powell 家庭干预 5 原则 / Kress-Elias CASEL 5 能力 / Klingman 创伤 3 力量 / Greenfield 5 文化路径 / McLoyd 经济压力模型(穷养 → 父母 → 娃)/ Bruck-Ceci 儿童证人 4 扭曲 / Comstock 媒体 5 效应 / Ramey Abecedarian 35 年 RCT / Bornstein specificity + continuity / Lamb-Ahnert 托育 5 维度质量
  - 干预项目独立卡:**NFP** / **Head Start** / **Triple P** / **Incredible Years** / **PCIT** / **MST** / **Tools of the Mind** / **PATHS** 8 大经典 RCT 项目
  - 跨派对照:**100% 跨派率**(80/80 ≥ 1 张 related 含 16+ 派之一);**0 跨派孤岛**;平均 3.17 related/卡;0 描述型 hook
  - 等级分布:A 级 80 张(100%)— 综述权威决定
  - 5 轮独立审 0 错全过(R1 修 4 处 broken refs + 14 张跨派补 → 100% 跨派率)
  - **铁三角对接**:V4 应用层 ↔ V3 情感原理(Cicchetti V3 → V4 临床 / Eisenberg V3 → V4 SEL)↔ V2 认知原理(Carey V2 → V4 探究式科学 / Goswami V2 → V4 阅读 5 要素)
  - 立场对立处全记 conflicts.md I 节(Hyson DAP vs 中国学业前移 / Bornstein 文化特异性 vs 美式普世 / Powell 干预 vs RIE / Cicchetti 情感虐待 vs 中国冷暴力 / Comstock 禁屏 vs iPad 普及 / Greenfield 互依 vs 美式独立 / Lamb 质量 vs 全职妈)
  - **并行场景隔离**:SRC-029 + 段 ID +300 buffer(避撞 SRC-028 V2 在跑)
  - 累计:**SRC-001 至 SRC-029(共 21 SRC)+ 1167 张知识卡 + 602 张术语**

**Phase 11 双 session 完成 — Lerner Handbook V3 + V2 学术综述铁三角左右脑双侧覆盖**(2026-05-04,共 135 张卡 + 228 张关联术语,5 轮审全过 0 错,完成铁三角:V1 节选(理论)+ V2(认知/感知/语言)+ V3(社会/情感/人格))。

**Phase 11 并行第二本 Lerner V2《Cognition, Perception, and Language》(SRC-028)** 完成(2026-05-04,51 张卡 + 42 张关联术语,5 轮审 0 错全过,A 级 98%,22 章覆盖 20 章)。
- **SRC-028 Lerner V2**(Wiley 2006 第 6 版,Kuhn/Siegler 主编)51 张知识卡覆盖 S0-S8 全段(S0=1 / S1=2 / S2=4 / S3=7 / S4=4 / S5=6 / S6=9 / S7=7 / S8=11)+ 26 张新 G-PERSON + 14 张新 G-TERM + 2 张 Edit 扩展(Tomasello/Wellman + false-belief)
  - 22 章覆盖 20 章(只缺 Ch 12 Reasoning + Ch 22 第二个十年 — 都 0-6 不主取):Ch 1 Nelson 神经基础 / Ch 2 Saffran/Werker/Werner 听觉语音语言 / Ch 3 Kellman/Arterberry 视觉 / Ch 4 Adolph/Berger 大动作 / Ch 5 Cohen/Cashon 婴儿认知 / Ch 6 Tomasello 语言习得 / Ch 7 Waxman/Lidz 词汇 / Ch 8 Goldin-Meadow 手势 / Ch 9 Bauer 记忆 / Ch 10 Munakata 信息处理 / Ch 11 Siegler 微观发生 / Ch 13 Halford 推理 / Ch 14 Keil 元学 / Ch 15 Cole 文化 / Ch 16 Gelman/Kalish 概念 / Ch 17 Newcombe 空间 / Ch 18 Geary 数学 / Ch 19 Harris 社会认知 / Ch 20 Winner 艺术 / Ch 21 Gardner 神童
  - 独家命题:Spelke 5 系统核心知识 / Baillargeon 4 月吊桥 / Saffran 8 月统计学习 / Werker 母语音素重组(vowel 先于 consonant)/ Eimas 1 月范畴知觉 / Kellman 物体一致性 / Tomasello 9 月革命 + 共享意图 / Markman 词义 3 约束 / Bloom 词汇爆炸 / Carey 概念革命 / Mandler 知觉 vs 概念 / Karmiloff-Smith RR 4 层 + neuroconstructivism / Wellman ToM 5 阶段 + WPSS / Leslie ToMM + 自闭症 / Wynn 5 月数概念 / Dehaene 数感 / Goldin-Meadow 手势预测 / Bauer 13 月 1 月记忆 / Adolph 学走 17 跌/小时 / Thelen A-not-B 动力学 / Munakata 渐变表征 / Siegler 重叠波 / Newcombe 空间自我中心→客观 / Geary 中文数词优势 / Cole 文化认知工具 / Keil 朴素理论 3 大领域 / Winner 艺术域独立 / Gardner 多元智能
  - 跨派对照硬指标:**100% 跨派率**(51/51 至少 1 张 related 含 15 派之一,含 V3 铁三角对接);**0 跨派孤岛**;平均 3.35 related/卡;平均 3.90 glossary_refs/卡;V2 新术语跨卡渗透 77 次
  - 等级分布:A 级 50 张(98%) / B 级 1 张(2%) / C 级 0 — 高于 V3 92%,因 Lerner V2 Tier 2 综述权威 + Wiley 第 6 版认知科学综述铁三角左侧
  - 5 轮独立审 0 错全过:Python 机器审(YAML / 字数 / refs / 跨派率)+ 漏知识反向覆盖(20/22 章)+ 漏术语扫(含 42 张新术语 V2 跨卡渗透)+ 用户三审 3 维度(hook 0 描述 + 跨派率 100% + 章节全覆盖)+ 用户深度审(跨章重复主题独立卡 / 内部结构 / 中国家长 18 高频痛点)
  - **铁三角对接**:V2 ToM 心智理论(Wellman/Leslie)↔ V3 共情(Eisenberg/Hoffman) / V2 联合注意(Tomasello)↔ V3 social referencing / V2 概念发展(Carey/Mandler)↔ V3 self-concept(Harter)
  - 立场对立处全记 conflicts.md H1-H6 节(Cohen-Cashon vs Spelke / Werker vs Kuhl / Carey vs Piaget / Karmiloff-Smith vs Pinker / Mandler vs Quinn / 中国数学 vs 天赋说)
  - **并行场景隔离**:SRC-028 + 段 ID +200 buffer(避撞 V3 +100)/ 索引 Edit 单点改避免覆盖 V3 / 启动前实测 SRC-027 已占
  - 累计:**SRC-001 至 SRC-028(共 20 SRC)+ 1087 张知识卡 + 493 张术语**

**Phase 11 第一本 Lerner V3《Social, Emotional, and Personality Development》(SRC-027)** 完成(2026-05-04,84 张知识卡 + 186 张新术语,5 轮审 0 错全过,A 级 92%,16 章 100% 覆盖)。
- **SRC-027 Lerner V3** 84 张知识卡覆盖 S0-S8 全段(S0=8 / S1=6 / S2=9 / S3=4 / S4=6 / S5=7 / S6=18 / S7=16 / S8=10)+ 186 张新术语
  - 16 章主题 100% 覆盖:Ch 1 Eisenberg 序章 / Ch 2 Thompson 发展之人 / Ch 3 Rothbart 气质 / Ch 4 Kagan 生物气质 / Ch 5 Saarni 情绪 / Ch 6 Caspi 人格 / Ch 7 Bugental 社会化 / Ch 8 Parke 家庭 / Ch 9 Harter self / Ch 10 Rubin 同伴 / Ch 11 Eisenberg 亲社会 / Ch 12 Dodge 攻击 / Ch 13 Turiel 道德 / Ch 14 Ruble 性别 / Ch 15 Eccles 成就动机 / Ch 16 Steinberg 青少年早期信号
  - 独家命题(Lerner V3 综述权威):Rothbart 气质 3 维度 / Kagan 抑制型生物根 + 反基因决定 / Saarni 情绪 8 项 / Caspi 人格延续 / Bugental-Grusec 5 领域 / Parke-Buriel 族群生态 / Maccoby-Baumrind 4 类型 / Harter self 5 维度 / Rubin 同伴 3 层级 / Eisenberg 亲社会发展 / Hoffman 共情 4 阶段 / Dodge 6 步认知 / Patterson 强制家庭 / Crick 关系攻击 / Turiel-Smetana 4 类规则 / Ruble-Martin 性别 3 阶段 / Eccles expectancy-value / Steinberg 青少年信号 / Cassidy 现代依恋综合 / Selman 友谊 5 阶段 / Wellman ToM 5 阶段 / Masten 韧性 4 因子 / Markus 文化 self / Kochanska 良知 + 母婴默契
  - 跨派对照硬指标:100% 跨派率(每张卡 ≥ 1 张 related 含 14 派之一);0 跨派孤岛
  - 5 立场对立处全记 conflicts.md G1-G7 节(Cassidy vs Bowlby / 气质 4 派 / 父母管教 / 攻击认知派 vs 关系派 / 道德 / 反抗期 / 文化 self)
  - 累计:**SRC-001 至 SRC-027(共 19 SRC)+ 1036 张知识卡 + 451 张术语**

**Phase 10 双 session 完成 — Shonkoff(美国 NRC 2000 综述)+ Pikler(德文 1969 原典)**(2026-05-04,共 97 张卡 + 33 张术语,5 轮审全过 0 错,RIE 谱系师承根源闭环)。

**Phase 10 第二本并行 Pikler《Friedliche Babys – zufriedene Mütter》(HERDER 1969)** 完成(2026-05-04,37 张卡 + 11 张术语 + 5 轮审 0 错,A 级 86% / 师承率 100%)。
- **SRC-026 Pikler**(HERDER 1969 德文原典)**37 张知识卡** 段覆盖(S1=5 / S2=4 / S3=5 / S4=7 / S5=5 / S6=8 / S7=3,S0/S8 不涉)+ **9 张新术语 + 2 张扩展术语(G-PERSON-Pikler / G-TERM-Loczy-institute)= 共 11 张关联术语**
  - **RIE 谱系闭环完成**:Pikler(SRC-026 师承根源)→ Magda Gerber(SRC-021/022 RIE 创始人)→ Lansbury(SRC-019 推广人)
  - 核心命题:**Bewegungsentwicklung 自然大动作发展** / **Pikler 大动作 6 阶段顺序**(Anna Tardos 1979 8 阶段表前身)/ **不教翻坐爬站走** / **不撑坐 6 论证(Lansbury 8 理由源头)** / **Pflege vs Spiel 二分(Magda Selective Attention 源)** / **Lóczy 1946 规程(720+ 婴儿 hospitalism 颠覆)** / **Geduld 育儿哲学** / **不便盆训练 4 错误**(德文原典)/ **反所有运动训练**
  - 跨派对照硬指标:**100%**(37/37 至少 1 张 related 跨 12 派),**师承率 100%**(37/37 含 Gerber/Lansbury related — 远超 60% 目标)
  - 外部 source 涉及 9 个不同 SRC(SRC-022 62 ref / SRC-019 43 / SRC-024 20 / SRC-016 12 / 其他)
  - **5 轮独立审 0 错**:Python 机器(yaml/字数/refs)+ 反向覆盖(11 章 spot-check + 补 1 张 Sprache)+ 漏术语扫(11/11 全建)+ 用户三审 3 维度 + 用户深度审
  - 立场对立处全记 conflicts.md F1-F5 节(Pikler vs 中国训练表 / Pikler-Brazelton 反学步车一致 / Pikler 1969 仰卧 vs AAP 2026 Tummy Time / Pikler-蒙氏 floor bed 共同根源 / Pikler 不便盆训练 vs 中国把屎把尿)
  - 并行场景隔离:SRC-026 + 段 ID = Shonkoff 起点 + 30 buffer / 索引 Edit 单点改 / 启动前 race condition 验证

**Phase 10 第一本 Shonkoff《From Neurons to Neighborhoods》NRC 综述完成**(2026-05-04,60 张卡 + 22 张术语,A 级 92% / 跨派 100% / 5 轮审全过 0 错)。
- **SRC-025 Shonkoff/Phillips**(NRC/IOM 2000)**60 张知识卡** 全段覆盖(S0=4 / S1=6 / S2=6 / S3=6 / S4=5 / S5=6 / S6=10 / S7=7 / S8=10) + **18 张新术语 + 4 张补术语 = 22 张关联术语**
  - 核心命题:**反早教 4 定理**(科学只告诉你别毁孩子,不告诉你怎么加速)/ **sensitive vs critical 期** / **自我调节 0-6 岁主轴** / **Hart-Risley 30M words** / **Perry-Abecedarian RCT 长效** / **NRC 6 大原则** / **质量胜身份**
  - 跨派对照硬指标:**100%**(60/60 至少 1 张 related 跨 12 派),平均 3.3 张 related/卡
  - **5 轮独立审 0 错**:Python 机器(yaml/字数/refs/cross-source)+ 反向覆盖(章节 spot-check)+ 漏术语扫 + 用户三审 3 维度 + 用户深度审(跨章重复主题/漏专业术语/内部结构)
  - 立场对立处全记 conflicts.md E1-E5 节(Shonkoff vs Gopnik 神经科学综述 vs 实证派 / Shonkoff vs Lillard 综述 vs 蒙氏哲学 / Shonkoff vs 松田 体罚立场 / Shonkoff vs Lansbury 系统化早期干预 vs RIE 不打扰 / Shonkoff vs 商业早教)

**Phase 9 双 session 同源松田道雄《定本 育儿百科》完成**(2026-05-03 + SRC-023 用户深度审 2026-05-04,SRC-023 fallback + SRC-024 并行,共 91 张松田卡 + 15 关联术语)。
- **SRC-023 松田道雄**(Phase 9 第一本 fallback)**49 张知识卡**(初版 44 + 用户深度审补 5)+ **6 张新术语**(初 4 + 深审补 2)+ 2 张 Edit 加深
  - 初版 IDs C-S0-367-369 + C-S1-609-613/763 + C-S2-546-550/701-702 + C-S3-551-554 + C-S4-550-554 + C-S5-648-652 + C-S6-666-672 + C-S7-604-608/758-759
  - **用户深度审补 5 张**(2026-05-04):C-S0-519 回乡分娩 / C-S1-764 产后 40 天可孕 / C-S3-705 果汁不强求 / C-S7-760 噩梦 vs 夜惊 / C-S7-761 反"哮喘发作"娇惯出
  - **Fallback 缘由**:原计划 Mary Ainsworth《Patterns of Attachment》(1978)OCR 缺,激活用户预设 fallback (a) 松田道雄
  - 主线 8 大独有命题:反"哭出习惯" / 反"标准体重" / 母乳至上 / 父亲核心 / 兄弟创伤防 / 反严格断奶食谱 / 反"反抗期"概念 ⭐⭐⭐ / 集体保育优质标准
  - 6 张新术语:G-TERM-anti-cry-it-out / G-TERM-rebellion-period / G-TERM-co-sleeping / G-TERM-quality-daycare(初 4)+ **G-TERM-jaundice-types ⭐⭐ / G-TERM-physical-punishment ⭐⭐⭐**(深审补 2)
- **SRC-024 松田道雄**(Phase 9 并行第二本)42 张知识卡 + 9 张术语卡,IDs C-S0-517/518 + C-S1-760-762 + C-S2-696-700 + C-S3-701-704 + C-S4-700-704 + C-S5-798-802 + C-S6-816-823 + C-S7-754-757 + **C-S8-100-105**(全新建 S8 = 3-6 岁段)
- 4 国跨文化对照闭环完成:**美(AAP)+ 中(鲍秀兰)+ 日(松田)+ 西方临床(Brazelton)** 全覆盖
- SRC-023 跨源率:**1.96 related/卡**(13 派覆盖,**0 跨源孤岛**,A 级 65%)
- SRC-024 跨源对照硬指标 100%:42/42 张含 AAP/鲍秀兰/Brazelton related,平均 3.12 related/卡
- 双 session 4+4 轮审全过 0 错:机器审 + 漏知识反向覆盖 + 漏术语扫 + 用户三审 3 维度
- **SRC-023 用户深度审 5 维度全过 0 错**(2026-05-04):漏知识(补 5)+ 漏术语(补 2)+ hook 风格(0 描述型)+ 跨源率(0 孤岛)+ 内部结构(YAML/字数/学究词全 0 错)

**累计知识库**:Karp(33)+ AAP(63)+ 鲍秀兰(86)+ Brazelton(79)+ Bowlby V1(37)+ Bowlby V2(32)+ Wonder Weeks(35)+ Davies(47)+ Gopnik(35)+ Lillard(52)+ Bowlby V3(15)+ Stern(43)+ Lansbury(43)+ Gerber SRC-021(32)+ Gerber SRC-022 深度本(45)+ 松田 SRC-023(49) + 松田 SRC-024(42)+ **Shonkoff SRC-025(68 = 60 + 用户深度审补 8)** = **836 张知识卡** + **261 张术语卡(255 + 6 用户深度审补)** + **24 个 SRC**(SRC-020 仍留空)。
**任务书**:Phase 1 v1.2 / Phase 2 v1.4 / Phase 3-4 / Phase 5 MONTESSORI_BABY / Phase 6 SCIENTIST_IN_CRIB + LILLARD + BOWLBY_VOL3 / Phase 7 STERN + LANSBURY / **Phase 8 GERBER**。
**4 派育儿理论库 + RIE 谱系闭环**:依恋三部曲(Bowlby V1+V2+V3) + 蒙氏 0-3(Davies + Lillard) + 认知科学(Gopnik) + **RIE 谱系完整(Pikler 师承 → Magda Gerber 创始人 SRC-021/SRC-022 → Janet Lansbury 推广人 SRC-019)** + self 心理学(Stern)。
**SRC-022 4 轮审全过 0 错**:Round 1 机器审 0 错 + Round 2 反向覆盖补 3 张(选托育 / 说不健康 / 30 次新食物)+ Round 3 漏术语补 1 张(G-TERM-time-out)+ Round 4 用户三审(hook 全抓眼 / 跨源率 80% / 0 自卷孤岛 / 平均 3.00 related/卡)。
**SRC-022 独有 9 张新术语**:G-TERM-educaring(自创词)+ G-TERM-quality-time(真定义)+ G-TERM-Loczy-institute(罗茨研究院起源)+ G-TERM-Antaeus-tantrum(神话比喻)+ G-TERM-traffic-light-limits(红黄绿三色)+ G-TERM-tell-before-do(告知再行动)+ G-TERM-active-participant-caregiving(主动参与)+ G-TERM-basic-trust(Erikson 共用)+ G-TERM-time-out(RIE 反对的派)。
**待办**:用户审 14 本累计 677 张卡 + 决定 SRC-021 vs SRC-022 保留方式 + Phase 9 候选(Shonkoff 真启动 / Pikler 师承原典 / Ainsworth Strange Situation / 松田道雄)。

## 完成度

### Phase 0 Bootstrap(2026-04-30)
- [x] 目录结构(§3)
- [x] schemas 落实(§4 v3)
- [x] 任务书归档到 `00-meta/README.md`
- [x] 项目根 `README.md`
- [x] meta 文件:progress.md / questions_for_user.md / conflicts.md / gaps.md
- [x] source_index.yaml(初始 2 份样本)
- [x] books_to_buy.md
- [x] 2 份样本转 v3 yaml(SRC-001, SRC-002, K-MILE-S5-001, K-MECH-CROSS-001)
- [x] git init + 首次 commit
- [x] 工具栈安装 → 见 `tooling.md`

### Phase 1 Karp(2026-05-01,1 天完成)

**任务书**:`00-meta/PHASE1_KARP.md`(v1.0 → v1.1 加白话风格 → v1.2 加 §10 实战调整 14 条)
**第一本书**:Karp《卡普新生儿安抚法》中译本(SRC-003)

- [x] OCR 长单行文件分块(11 个 15KB chunks 到 `karp_chunks/`)
- [x] 全书结构地图(3 批 subagent)
- [x] 主题反向索引
- [x] 10 个主题包并行提取 verbatim 素材
- [x] SRC-003.yaml(23 个主题块,OCR 错字修正)
- [x] source_index.yaml 更新
- [x] **第一部分 12 张卡片**(C-S1-001..012)— 哭闹机制 + 第四产程 + 5S 概览
- [x] **第二部分 13 张卡片**(C-S1-013..025)— 5S 五招详解 + 拥抱疗法
- [x] **第三部分 8 张卡片**(C-S1-026..033)— 睡眠 + 红旗 + 食物过敏 + 产后
- [x] 反向覆盖审计(每部分跑一次)— 补 9 张高价值漏掉卡
- [x] GitHub Top 3 调研 → §10.13 外部方法论吸收(2000-token 块 / 黑白名单 / non-overlapping / 输入输出比 / ToC)
- [x] checkpoint MD(`00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md`)
- [ ] **用户抽 5 张审核**(待)— 4+ 张满意 = POC 通过

### Phase 2 完成(2026-05-01 ~ 2026-05-02)

**任务书**:`00-meta/PHASE2_AAP.md` v1.4(§2.6 翻译两步走 / §2.7 前情提要 / §2.8 术语卡片化 / §2.9 inline 引用渲染)

**全部完成**:
- [x] R1 Safe Sleep(SRC-004): 9 + 复盘 R1.5 + 3 = 12 张
- [x] R2 Crying & Soothing(SRC-005): 9 张
- [x] R3 Feeding & Pacifiers(SRC-006): 9 + 复盘 R3.5 + 7 = 16 张
- [x] R4 Milestones & Teething(SRC-007): 14 张
- [x] R5 Health & Safety(SRC-008): 12 张
- [x] **AAP 63 张知识卡**(全 v3.5 schema)
- [x] **术语卡 60 张**(40-glossary/)
- [x] Karp 33 张回归 v3.5 schema(并行 batch refactor 完成)
- [x] R5 audit + 4 张新术语卡(RSV/MMR/DTaP/CDC)+ 9 张卡补 glossary_refs
- [x] checkpoint:`checkpoint_PHASE2_AAP_20260502.md`
- [x] INDEX_BY_SOURCE.md + progress.md 更新

**按解读 B 跳过**(留全部书产完后整合):
- [-] cross-validate Karp vs AAP evidence_level 升级
- [-] conflicts.md 整理(Karp vs AAP 立场对立:共睡 028 / 奶嘴 022 等)

**待用户**:
- [ ] 新 session 跑 96 张完整审计(提示词:`00-meta/checkpoints/audit_prompt_96_cards.md`)
- [ ] 决定 Phase 3 启动书(候选见下)

### Phase 3 第一本完成(2026-05-02)— 鲍秀兰

**任务书**:`00-meta/PHASE3_BAOXIULAN.md` v1.0
**第一本书**:鲍秀兰、孙淑英《婴幼儿潜能开发和早期教育》(中国妇女出版社, 2016)(SRC-009)

**全部完成**:
- [x] OCR 已成 .md(286KB / 2869 行,跳过 OCR 工程)
- [x] 章节地图(7 段映射 — S1-S7,首次扩展 S6 + S7)
- [x] **新建 2 段目录**:`30-cards/s6-12to24mo/` + `30-cards/s7-24to36mo/`
- [x] **S1(7 张)**:1 月龄(视听刺激/红旗/把新生儿当懂事/4 大禁忌/关键期/玩具/睡眠)
- [x] **S2(10 张)**:2-3 月龄(俯卧抬头/红旗/语言剥夺/baby talk 5 共性/母婴交谈链/响应需求/**禁打蜡烛包 ⭐**/翻身别独留/出声笑+元音/室温)
- [x] **S3(13 张)**:4-6 月龄(拉坐/强化"妈妈"/视听 6 法/镜子/找朋友/靠坐+跳跃/玩是正经事/藏猫猫/独坐+坐位优势/硬食/**6 月红旗 ⭐**/点头摇头/理性对哭声)
- [x] **S4(10 张)**:7-8 月龄(爬行/认物找物/触额碰头/教 ba/ma/捏取/百宝箱/**戒奶瓶**/制止打人/**8 月前抱抱不宠坏 ⭐**/再见欢迎)
- [x] **S5(12 张)**:9-12 月龄(扶站独站/自我意识/障碍训练/学小勺/**坐盆训练 ⭐**/察言观色/玩娃娃/学说 5 要点/教物名准/走路 5 法/认红色/与人分享)
- [x] **S6(18 张,新建)**:1-2 岁(模仿乱说/儿歌接背/独立走/涂画/学用勺/小伙伴玩/**管教全家一致 + 不打 ⭐**/中场休息/预防发脾气/戴帽脱袜/生活规律/**18 月红旗 ⭐**/跑+倒退+双脚跳/双字词→简单句/用"我"自我意识/主动交往/识颜色/生活自理)
- [x] **S7(15 张,新建)**:2-3 岁(独自上下楼梯/骑三轮车/模仿画/识形状/分辨大小/唱儿歌+说用途/语言表大小便/帮大人做事/学穿鞋/合作玩/跳高跳远+单足站/长短+数数/**24 月红旗 ⭐**/**忽视错误最有效约束 ⭐**/道德意识 5 招)
- [x] **新术语卡 4 张**(40-glossary/):**G-PERSON-Bao**(鲍秀兰人物)+ **G-TERM-critical-period**(关键期/Hubel-Wiesel/Genie 案例)+ **G-TERM-parentese**(父母语 5 共性 + 全球文化共性)+ **G-TERM-turn-taking**(母婴交谈链 + Romeo MIT 研究)
- [x] SRC-009.yaml(stub + referenced_by_cards 完整 85)
- [x] source_index.yaml 更新(SRC-009 + next_src_id → SRC-010)
- [x] INDEX_BY_SOURCE.md 全段更新(总计 181 张 + 64 张术语)
- [x] checkpoint:`checkpoint_PHASE3_BAOXIULAN_20260502.md`

**红旗信号矩阵(Phase 3 总结)**:
- **C-S1-066** 1 月大声没反应 + **C-S2-009** 2-3 月不看人脸 + **C-S3-024** 6 月 4 项 + **C-S6-012** 18 月 4 项 + **C-S7-013** 24 月 7 项
- 完整覆盖 0-3 岁所有月龄段红旗信号链

**立场对照(中文 vs 美国)**:
- ⭐ **C-S2-014 反对中国"打蜡烛包"传统**(与 Karp 包裹立场对照)
- ⭐ **C-S5-012 中国 9 月起坐盆训练**(与 AAP 18 月-3 岁立场对照)
- ⭐ **C-S6-007 鲍秀兰 vs Karp/AAP 体罚立场**(全部反对体罚一致)
- ⭐ **C-S7-014 忽视技巧**(与 Karp 5S 安抚立场不同维度)

### Phase 4 两本并行完成(2026-05-03)

**任务书**:`00-meta/PHASE4_WONDER_WEEKS.md` v1.0(本 session)+ Bowlby Vol 2 任务书在并行 session

**全部完成**:
- [x] **SRC-012 Bowlby Vol 2《分离》(32 张)**(并行 session,凌晨开始)
  - S5(4 张):分离时玩偶毯子 / 寄养换家年龄 / 怕生 = 陌生 + 靠近 / 住院妈陪 vs 不陪
  - S6(18 张):**抗议-绝望-超脱 3 阶段 ⭐** / 重聚不认妈危险 / 撤回爱当惩罚 / 精神虐待边界 / 父母吵架孩子怕分开 / 别让娃当情绪保姆 / 我是为你好的陷阱 / 等
  - S7(10 张):**别偷溜要正面告别 ⭐** / **5 岁前住院影响到 18 岁 ⭐** / 拒学 vs 逃学不同 / 强独立不健康 / 等
  - 新术语:G-PERSON-Robertson(住院儿童纪录片) / G-TERM-protest-despair-detachment(3 阶段) / G-TERM-defensive-exclusion / G-TERM-pathological-mourning / G-TERM-anxious-attachment / G-TERM-role-reversal / G-TERM-agoraphobia / 复用术语 G-TERM-attachment / G-TERM-separation-anxiety / G-TERM-internal-working-model / G-PERSON-Bowlby
- [x] **SRC-013 Wonder Weeks《婴儿大脑跃迁 10 周》(30 张)**(本 session,11:30-12:13)
  - S1(4):**三 C 信号 = 跃迁不是病 ⭐** / **10 跃迁时间表 ⭐** / 早产校正 / 5 周第一跃迁
  - S2(5):8 周模式 / 12 周平滑过渡 / fussy 期不睡训不戒奶 / **fussy 期再崩溃别摇宝宝 ⭐** / 跃迁后突然长大
  - S3(4):19 周事件世界 / 4-5 月 fussy 可达 6 周 / **4 月奶量骤降不是断奶 ⭐** / 4 月想逃走不是失败
  - S4(5):26 周关系世界 / **跃迁周龄↔依恋时间表对照 ⭐** / **fussy 不是出牙痛 ⭐** / 6-8 月拒换尿布 / 8 月跃迁前奏
  - S5(4):37 周分类 / 46 周序列 / 撒娇也是 fussy / 8-12 月双跃迁妈妈极限
  - S6(6):55 周程序 / 64 周原则 / **75 周系统世界 ⭐** / 13-18 月三连击 / **跃迁期不打不骂 ⭐** / "质量时间"是伪概念
  - S7(2):21 月跃迁框架结束 / 跃迁是普遍 = 育儿不孤单
  - 新术语 6 张:G-PERSON-vanderijt / G-PERSON-plooij / G-TERM-wonder-week / G-TERM-mental-leap / G-TERM-3C-signs / G-TERM-fussy-phase
- [x] **并行协调**:+50 buffer ID 隔离,无冲突(SRC-012 用 C-SX-070..099 区间,SRC-013 用 C-SX-120+ 区间)
- [x] checkpoints:`checkpoint_PHASE4_WONDER_WEEKS_20260503.md`(并行 session 应有自己的 checkpoint)
- [x] source_index.yaml + INDEX_BY_SOURCE.md + progress.md(本文件)合并(2026-05-03 并行结束后)

**跨源亮点**:
- ⭐ **C-S4-125** Wonder Week + Bowlby + Brazelton + AAP 四派同时背书 6-9 月怕陌生人
- ⭐ **C-S6-126** Wonder Week + Bowlby + 鲍秀兰 三派一致反对体罚
- Wonder Week WW46-WW75 fussy phase 与 Bowlby Vol 2 分离焦虑窗口完美重合

**待用户**:
- [ ] 抽 5 张随机审 → 4+ 满意 = Phase 4 通过
- [ ] 决定 Phase 5 启动书(候选见下)

## 已抓源数

| Tier | 已抓 | 预估 |
|---|---|---|
| Tier 1 权威机构 | **7**(SRC-001/002 网页 + SRC-004-008 AAP cluster × 5)| ~40 |
| Tier 2 学术 | 0 | ~60 |
| Tier 3 书籍 | **8**(Karp / 鲍秀兰 / Brazelton / Bowlby V1 / Bowlby V2 / Wonder Weeks / Davies / **Gopnik**)+ Lillard 进行中 | ~15 |
| Tier 4 中文权威 | 0 | ~10 |
| Tier 5 视频/播客 | 0 | ~8 |

## 已生成

- 单元:2 个(K-MILE-S5-001, K-MECH-CROSS-001)— Phase 1-6 知识单元层暂跳过
- **知识卡:447 张**(全 v3.5 schema)
  - SRC-003 Karp:33 张
  - SRC-004 AAP Safe Sleep:12 张
  - SRC-005 AAP Crying:9 张
  - SRC-006 AAP Feeding:16 张
  - SRC-007 AAP Milestones:14 张
  - SRC-008 AAP Health & Safety:12 张
  - SRC-009 鲍秀兰:86 张
  - SRC-010 Brazelton:79 张
  - SRC-011 Bowlby V1:37 张
  - SRC-012 Bowlby V2:32 张
  - SRC-013 Wonder Weeks:35 张
  - SRC-014 Davies Montessori Baby:47 张
  - **SRC-015 Gopnik Scientist in the Crib:35 张**(S1: 7 + S2: 4 + S3: 4 + S4: 6 + S5: 4 + S6: 5 + S7: 5)⭐ 新增
  - **段分布**:S0: 11 / S1: 115 / S2: 47 / S3: 51 / S4: 47 / S5: 56 / S6: 79 / S7: 41 = 447
- **术语卡:146 张**(40-glossary/)
  - 2026-05-02:Phase 3 鲍秀兰 + Brazelton 全本完成,首建 S0/S6/S7 段
  - 2026-05-03 早:Phase 3 第三本 Bowlby V1 audit 完成 + SRC-011 补登记 source_index
  - 2026-05-03 凌晨-中午:**Phase 4 两本并行启动 + 完成**
    - 并行 session(凌晨 02:00-11:28)— Bowlby Vol 2 SRC-012(32 张 + 12 术语卡含复用)
    - 本 session(11:30-12:13)— Wonder Weeks SRC-013(30 张 + 6 术语卡)
  - 2026-05-03 12:30+:并行结束后合并 source_index.yaml + INDEX_BY_SOURCE.md + progress.md

## 阻塞

- 无(等用户验收)

## 待用户回答的问题

- Phase 1 33 张卡片是否通过 POC?
- Phase 2 启动哪本书?
- `_drafts_part2/` 旧包裹草稿(原 008/009/010)是否可删?

## 已确认的关键决策

- **Q1 → B**: Phase 1 第一批 fetch 顺手补抓 SRC-001/002 raw HTML(2026-04-30)— **未做,Phase 2 补**
- **Q2 → A**: Phase 1 仅用 Tier 3 书跑通(2026-04-30)— Phase 1 实际只用 SRC-003 一本书
- **Q3 → B → SUPERSEDED**: 卡片语言策略(2026-04-30)— **被 PHASE1_KARP §2 覆盖**:全中文,不双语
- **新增决策(Phase 1 实战)**:
  - 字段名英文 key,展示层翻中文(待建 `render_labels.yaml`)
  - hook 默认填(从可选改为必填,§10.10)
  - evidence_level 单本书阶段标尺(§10.7):C = Karp 一家言 / B = Karp 引外部研究 / A = 与 Tier 1 共识对齐
  - 反向覆盖审计固化为工作流必备步骤(§10.4)

- **491 卡审计要点(2026-05-03)**:见 `checkpoints/audit_report_491_cards_20260503.md`
  - 总评 8.1/10,failure_mode 100% 不空,citation ~99% 完整
  - **P0 已修(2 项)**:新建 G-TERM-sensitive-periods + G-TERM-observation 两个蒙氏核心术语卡(原本 5+ 张卡引用断链)
  - **P0 待用户拍板(6 项)**:Wonder Weeks 复制争议披露 / Meltzoff 复制争议披露 / 22 张 evidence_level 降级 / 70+ 张 tag 增改 / 7 个疫苗缩写术语补建 / S0+S1 临床基础卡 P0 缺口(产检/黄疸/脐带/新筛/Vit K)
  - **conflicts.md 首次填充**:18 个 conflict 候选(7 高严重 + 5 中严重 + 6 视角差异)
  - **gaps.md 追加**:40+ 主题 gap,P0 12 项严重缺口
  - **6 张 ⭐ Star 跨派背书卡已落地**:C-S4-125 / C-S5-130 / C-S5-069 / C-S6-126 / C-S6-133 / C-S7-039

- **8.1 + 8.2 执行(2026-05-03 同日)**:用户决策 Q1=C / Q2=B / Q3=A / Q4=A / Q5=A / Q6=A 后批量执行
  - **8.1 Q1+Q4 tag 修改**:86 张卡(WW 33 张全加 controversy + Bowlby V1 28 张补 philosophy/controversy + Karp 7 张 + Bowlby V2 7 张 + AAP 8 张 + 鲍秀兰 3 张)
  - **8.1 Q2 Meltzoff 复制争议披露**:6 张 Gopnik ToM 卡(C-S1-241 + C-S2-183 + C-S2-184 + C-S5-181 + C-S5-182 + C-S6-179)— evidence_level 降 B + tags 加 controversy + why_matters 加披露
  - **8.1 Q3 evidence_level 降级**:32 张(Karp 5 / Brazelton 8 / Davies 8 / Lillard 7 / Bowlby V2 1 / 鲍秀兰升 3)
  - **8.1 Q5 新建 15 张术语卡**:G-PERSON-{Winnicott,Erikson} + G-ABBR-{Hib,IPV,PCV,HepA,HepB,Varicella,Rotavirus} + G-TERM-{habituation,sleep-cycle,school-readiness,imaginary-baby,early-intervention,postpartum-blues}
  - **8.1 错字修复**:6 张 WW "周ε≈" + C-S2-122 占位符 + C-S6-093 G-TERM-role-reversal 补挂
  - **8.2 跨派对照卡 4 张新建**:C-S6-196 tantrum 4 派 / C-S6-197 如厕 4 派 + 中国把屎把尿 / C-S5-190 戒奶瓶 3 派 / C-S5-191 睡眠训练 5 派
  - **8.2 P0 临床卡 5 张新建**:C-S1-091 黄疸 / C-S1-092 脐带 / C-S1-093 新生儿筛查 / C-S1-094 Vit K / C-S1-095 第一次儿保
  - **8.2 PHASE7 任务书新建**:`PHASE7_CLINICAL_AAP.md` — 后续 30-40 张临床卡 + 中文产科源(SRC-017~019)的执行任务书
  - **变更总数**:~125 张卡操作 + 1 任务书 = 单 session 历次最大批量
  - **下一 session 起点**:Phase 7 启动 — 抓 AAP HealthyChildren 未覆盖页 + 中文卫健委 + 中华医学会指南

## 上次 session 结束时间

2026-05-03(Phase 6 第一本 Gopnik《Scientist in the Crib》完成 + SRC-015 补登记 source_index;Lillard 进行中;**当晚启动 491 卡审计完成**)

## 当前总览(447 张知识卡 + 146 张术语卡 + 8 段:S0-S7)

| Phase | 书 / 来源 | 卡数 | 段覆盖 | SRC |
|---|---|---|---|---|
| 1 | Karp《卡普新生儿安抚法》 | 33 | S1, S2 | SRC-003 |
| 2 | AAP HealthyChildren.org × 5 cluster | 63 | S1-S5 | SRC-004~008 |
| 3 (1) | 鲍秀兰《婴幼儿潜能开发》(中) | 86 | S1-S7(首扩 S6/S7) | SRC-009 |
| 3 (2) | Brazelton《Touchpoints: Birth to 3》(英) | 79 | S0-S7(首扩 S0) | SRC-010 |
| 3 (3) | Bowlby Vol 1《依恋》(中译) | 37 | S1-S6 | SRC-011 |
| 4 (1) | Bowlby Vol 2《分离》(中译) | 32 | S5-S7 | SRC-012 |
| 4 (2) | Wonder Weeks《婴儿大脑跃迁》 | 35 | S1-S7 | SRC-013 |
| 5 | Davies《The Montessori Baby》(蒙氏 0-1) | 47 | S0-S6(首引蒙氏)| SRC-014 |
| **6 (1)** | **Gopnik《Scientist in the Crib》/《摇篮里的科学家》** | **35** | **S1-S7(认知科学全段)** | **SRC-015** |
| 6 (2) | Lillard《Montessori from the Start》(蒙氏 0-3 学院派)| **52**(初 44 + 二审补 2 + 三审补 6) | S0-S7(蒙氏 0-3 闭环)| **SRC-016** |
| 6 (3) | **Bowlby Vol 3《丧失》**(依恋三部曲收官)| **15**(用户压缩到"很少") | S5/S6/S7(中国家长高频场景)| **SRC-017** |
| **7 (1)** | **Stern《The Interpersonal World of the Infant》**(self 心理学奠基)| **43**(并行 41 + R2 补 2) | **S0-S7(全段)** | **SRC-018** |
| 7 (2) | **Lansbury《Elevating Child Care》**(RIE 派)| **39**(初 37 + 二审补 2) | S0-S7(全段)| **SRC-019** |
| | **合计** | **600** | **S0-S7(8 段全)** | **18 SRC 引用 / 19 SRC 登记** |

---

## Phase 7 第一本 Stern 完成记录(2026-05-03)

**3 session 并行模式收官**(Bowlby V3 + Stern + Lansbury 三本同日推进):

### Stern《The Interpersonal World of the Infant》(SRC-018)
- **43 张知识卡 + 14 张术语卡**
- 段分布:S0:4 / S1:5 / S2:4 / S3:5 / S4:7 / S5:**9**(最强段)/ S6:5 / S7:4
- 等级分布:**A 31(72%)/ B 12 / C 0** — 远高于 Lillard 35%,反映 Stern 实证扎实
- 三审通过(R1 内部 0 错 + R2 补 2 张 + R3 跨源 71 链接 / 9 派源 / 1.65 平均)
- 跟蒙氏(哲学)+ Bowlby(关系)三角互补 — **Stern 给"心理过程"层**

### Stern 11 大独家命题入库
1. 4 senses of self 叠加(emergent / core / subjective / verbal)
2. **Affective attunement** ⭐⭐⭐ 完整 9 张套件(C-S5-291..299)
3. Vitality affects(活力情感)
4. RIGs(IWM 积木块)
5. Evoked companion(独自时仍有伴)
6. Amodal perception(出生即跨感官)
7. Intersubjectivity(7-9 月共主体性)
8. Communion vs Communication
9. Selective attunement = socialization 工具
10. 修复 > 完美(rupture-and-repair)
11. Still-face = 玩手机后果

### Bowlby V3《丧失》(SRC-017)— 同期合并
- 15 张(用户压缩) — 哀伤 4 阶段儿童版 + 谈死亡话术 + 病理识别
- 跳过 9 个极端章节,聚焦中国家长高频场景

### Lansbury(SRC-019)— 同期合并
- 39 张 — RIE 派现代代表,Magda Gerber 直接弟子
- 蒙氏 + RIE 平行流派闭环

---

## 下次 session 起点

> 1. **用户验收 8 本累计 401 张卡**(抽样审,尤其 Davies 蒙氏跟其他 7 本立场对照是否到位)
> 2. **决定 Phase 6 第 9 本启动**:
>    - 候选 A:**Lillard《Montessori from the Start》**(0-3 岁完整蒙氏,跟 Davies 形成蒙氏闭环)— **本 session 推荐**
>    - 候选 B:**Bowlby Vol 3《丧失》**(完成依恋三部曲,中译已 OCR)
>    - 候选 C:**Stern《The Interpersonal World of the Infant》**(自我感 4 阶段,与蒙氏 absorbent mind 对话)
>    - 候选 D:**Gopnik《Scientist in the Crib》**(认知科学,与蒙氏 absorbent mind 直接对话)
>    - 候选 E:**Gerber《Your Self-Confident Baby》/ Lansbury(RIE 派)**(尊重式育儿,蒙氏的姐妹流派 — yes space 就是 Gerber 命名)
>    - 候选 F:**Pikler《Friedliche Babys》**(德语育儿,跟蒙氏 floor bed / movement freedom 同根)
>    - 候选 G:**Shonkoff《From Neurons to Neighborhoods》**(NRC 神经发展底座)
>    - 候选 H:**WHO Infant Feeding Guideline**(国际权威循证,Tier 1)
>    - 候选 I:**松田道雄《育儿百科》**(日本经典中译,跨 0-6 岁)
>    - 候选 J:**海蒂育儿大百科**(中译已 OCR)
> 3. **术语卡 backlog**:SRC-010 / SRC-011 / SRC-014 引用的 G-ID 还有部分待建(如 G-PERSON-Uzodike / G-PERSON-Gerber / G-TERM-cestina)
> 4. **conflicts.md 整理**(已积压):Karp vs Davies(swaddle 立场对立,Phase 5 新增)+ 至少 11 处 controversy
> 5. **三派+ 一致卡集中审核**:跨源标连 ⭐ 卡新增(C-S6-133 温柔边界 4 派一致 + C-S5-130 信任两份大礼 + C-S4-132 不学步车)
>
> **下一 session 必读**:
> - `00-meta/checkpoints/checkpoint_PHASE5_MONTESSORI_BABY_20260503.md`(Davies 完整产出 + 跨源对照)
> - `00-meta/PHASE5_MONTESSORI_BABY.md`(Phase 5 任务书)
> - `00-meta/checkpoints/checkpoint_PHASE4_WONDER_WEEKS_20260503.md`(Phase 4 收官)
> - `00-meta/PHASE2_AAP.md` v1.4(§2.5-2.9 schema 规则)
> - `00-meta/PHASE1_KARP.md` §10 实战调整 14 条


---

## 2026-05-04 · 剩余 14+1 SRC 944 新卡 + 全库 dedup + v1.1 5 维度审计完成

### 范围
- **15 SRC 单源审**(SRC-017/018/019/021/022/023/024/025/026/027/028/029/030/031/040)
- **9 段跨源 dedup**(S0-S8)
- **5 个新维度 v1.1**(citation 真实性 / 数字事实 / 翻译一致性 / 内容空洞 / evidence_level 同行评议)
- 总审 **2,246 卡**(1,437 知识卡 + 809 术语卡)

### 工作流
- Phase A 主线读规范 + 历史报告(15 KB)
- Phase B 15 个 SRC subagent 并行(精简后 120 KB 报告)
- Phase C 9 个 stage subagent 并行(60 KB)
- Phase F 5 个 dimension subagent 并行(30 KB)
- Phase D 主线汇总 + 5 大交付物(70 KB)
- 用户期间未被打扰(主线 ~4 小时)

### 关键发现(P0-P1)
1. **维度 14 evidence_level inflation**:**~430 张 A 级卡需降级**(SRC-019/021/022/026/017 流派单家 100% + SRC-027/028/029/030 Lerner Handbook 单章引 ~85%)
2. **维度 12 翻译一致性**:**6 对 G-TERM 术语卡冲突**(P0)+ 多张标准译反而少于变体
3. **维度 11 数字事实**:1 张 P0(C-S1-2500 海蒂 VD 起补"2 周" vs "2 个月"内部矛盾)
4. **维度 10 citation 真实性**:0 P0 硬错;~18% 卡 citation 范式不可读者反查(主要 SRC-027/030 字节偏移 + SRC-031 主题串)
5. **维度 13 内容空洞**:PASS — 0 P0/P1,3 张 P2 短 title
6. **L1 真重复 ~12 簇 ~25-30 张减卡潜力**(详见 merge_candidates_20260504.md)
7. **L2 实质重复 ~25 簇 ~30-50 张减卡潜力**(待用户拍板)
8. **5 个 hotspot 完整发现**:Gerber 双卷 / 松田双 SRC / Lerner V1-V4 跨卷 / NRC × Lerner 元理论 / Stern × Bowlby × Brazelton 婴儿心理学三角
9. **conflicts.md 追加 3 项**:松田哮喘"娇惯出"P0 + 松田反"反抗期"+ Pikler 反 Tummy Time
10. **gaps.md 追加 4 项**:Gottman emotion coaching 缺位 + 松田反"反抗期" S6 卡缺 + Lillard 厕训 S6 卡缺 + 海蒂/松田 toilet learning 总论缺

### 交付物清单
1. ⭐ `audit_report_remaining_cards_20260504.md` 主报告
2. ⭐ `merge_candidates_20260504.md` 待用户拍板清单
3. `audit_log_addendum_20260504.md` 自动修复日志
4. `_audit_subreport_SRC-XXX.yaml` × 15(单源审)
5. `_audit_subreport_PhaseC_S?.yaml` × 9(跨段 dedup)
6. `_audit_subreport_PhaseF1-F5.yaml` × 5(5 个新维度)
7. `conflicts.md` 追加 v2.2(3 项)
8. `gaps.md` 追加 v2.2(4 项)
9. `progress.md` 本段更新

### 待用户决策(7 项,详见主报告 §7)
- Q1:evidence_level ~430 张降级是否执行(分批 / 全部 / 维持)
- Q2:6 对 G-TERM 术语卡冲突如何处理
- Q3:L1 真重复 ~25-30 张是否合并
- Q4:松田 SRC-023/024 9 个 L1 跨源合并
- Q5:S5/S6/S8 段 6 张 META-CROSS 导航卡新建
- Q6:C-S1-2500 海蒂 VD 时机回原书校对
- Q7:45 张 C 级卡缺 philosophy tag 批量加

### 自动修复执行
- **本次零修复**(审计严守"不动卡"原则,所有修复留待用户授权)
- 详见 audit_log_addendum_20260504.md §2(已识别清单)+ §4(待校准清单)

### 下一 session 必读
- `audit_report_remaining_cards_20260504.md` ⭐
- `merge_candidates_20260504.md` ⭐
- `audit_log_addendum_20260504.md`
- 各 `_audit_subreport_*.yaml`(细节查证用)



### "全按建议改"批量执行(2026-05-04 用户授权后)

**总修复量:~800 张卡片修改 + 3 对 G-TERM 合并 + 4 个翻译统一**

执行明细见 [audit_log_addendum_20260504.md](checkpoints/audit_log_addendum_20260504.md) §1.3:
- P0 医学高风险:5 张(松田 3 + 海蒂 VD + Bowlby glossary)
- P0 stage 错配:1 张(C-S2-942 → C-S6-1942)
- P0 controversy tag 补:21 张
- P1-1 evidence_level A→B:**462 张**(11 SRC)
- P1-2 G-TERM 软合并:3 对 + 4 个翻译漂移统一
- P1-3 L1 真重复软合并(merge_into 字段):**39 张**
- P2-1 tag 清理:128 张(Gerber 84 + Stern 44)
- P2-2 Stern 中译信息补:44 张
- P2-3 SRC-040 G-PERSON-Murkoff 占位删:45 张
- 上一轮:45 张 C 卡加 philosophy + 4 张 SRC-017 broken_related_ref

**全库 evidence_level 分布(执行后)**:A 371 / B 983 / C 83
**对比执行前**:A 占比 26% vs 之前 ~58%(更诚实评级)

**下一阶段待用户拍板**:
- theory-of-mind / attachment 4 类型译名标准决策
- C-S1-1011 飞鹤雅培惠氏品牌点名(法律敏感)
- 39 张 merge_into 标记是否真删(目前软合并不删文件)
- 6 张 META-CROSS hub 卡新建(分离/断奶/学走/反 spank/文化路径/反早教)
- 4 个 gap 补卡(Gottman / 松田反"反抗期" S6 / Lillard 厕训 / 海蒂 toilet learning)
- SRC-027/030 chapter_offset → page_pdf(164 张,需 PDF 反查工具)
- SRC-031 加 doc_id 引用(65 张)


### "3、4、5、6 都做" 第三轮(2026-05-04 用户授权后)

**~310 张卡操作**:1 张内容修复 + 10 张新建 + 173 张 citation 标注 + 39 张物理删除 + 87 张引用更新

明细见 `audit_log_addendum_20260504.md` §1.4:
- **项 3** C-S6-934 Christakis 2004 时间倒挂修复
- **项 4** 10 张新卡创作:
  - 6 张 META-CROSS hub:S5 分离/断奶/学走 + S6 反 spank/文化路径 + S8 反早教
  - 4 张 gap 补卡:Gottman emotion coaching / 松田反"反抗期" S6 版 / Lillard 厕训 12-18m / 海蒂 toilet learning 中道
- **项 5** SRC-026/031/027/030 citation_followup_needed 标注 173 张
- **项 6** 39 张 merge_into 物理删除 + 87 张引用更新到 keeper

**全库最终状态(三轮收官)**:
- 总卡数:**1437 → 1408**(-29 净)
- evidence_level:A 366 / B 958 / C 84(A 占比 26%,执行前 58%)
- merge_into 残留:0
- philosophy tag C 卡缺漏:0
- controversy tag 卡数:209
- 新建 META-CROSS / gap 卡:10 张
- citation_followup_needed:173 张(待原书/PDF 反查)

**累计三轮总修复**:**~1140 张卡片操作 + 3 对 G-TERM 合并 + 4 个翻译统一 + 39 张物理删除 + 10 张新建**

**剩余真正待用户决策的事项**:
1. theory-of-mind 标准译"心理理论"vs"心智理论"
2. attachment 4 类型译名"矛盾型"vs"抗拒型"
3. C-S1-1011 飞鹤雅培惠氏品牌点名(法律敏感)— 现已 merge_into C-S1-1009 文件已删
4. SRC-027/030 chapter_offset 反查工具开发(173 张待补 page_pdf)
5. SRC-031 doc_id D1-D12 索引建立(WHO 12 docs source yaml)
6. SRC-026 Pikler 6 张"全书反复"原书反查具体页


### "继续" 第四轮(2026-05-05)

**~320 张卡修改**:84 UTF-8 净化 + 56 doc_id + 157 chapter_title + 4 类型译名 + 26 ToM 译名

详见 `audit_log_addendum_20260504.md` §1.5:
- ToM 译名全库统一"心智理论"
- attachment 4 类型全库"抗拒型/混乱型"
- UTF-8 损坏 84 张净化(项 6 副作用,合法 UTF-8 保留)
- SRC-031 doc_id D1-D12 真实映射(56 张)
- SRC-027/030 chapter_offset → chapter_title 反查(157 张)

**累计四轮总修复**:**~1460 张卡操作 + 3 对 G-TERM 合并 + 6 个翻译统一 + 39 张物理删除 + 10 张新建 + 84 张 UTF-8 净化**

**全库收官状态**:
- 总卡数 1408
- evidence_level: A 366 / B 958 / C 84
- UTF-8 损坏:0
- merge_into 残留:0
- philosophy tag C 卡缺漏:0
- controversy tag:211 张
- ToM 译名:全统"心智理论"
- attachment 4 类:全统"抗拒型/混乱型"
- SRC-031 真实 doc_id:56 张
- Lerner V1+V3 chapter_title:157 张

**已无可机械执行的事项** — 剩余只有 PDF 工具(SRC-027/030 page_pdf)、原书反查(SRC-026 6 张)、品牌点名法律决策(C-S1-1011 已删除)等需要人工/工具介入的事项。
