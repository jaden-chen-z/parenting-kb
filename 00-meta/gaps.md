# 找不到的内容

> 抓不到 / 付费墙挡住 / 中译版找不到的源,记录在这。

---

## G1:SRC-001 / SRC-002 raw HTML 缺失

**Status: 已计划修复 — Phase 1 第一批 fetch 任务**

**背景**:附录 B 的 2 份样本 yaml 是 verbatim 整理版,但没有保留对应的 raw HTML 文件。

**影响**:source yaml 中 `local_file: null`,审计追溯路径不完整(虽然 URL 能再访问到当前版本,但页面可能更新)。

**处理**:Q1 已确认方案 B —— Phase 1 启动时顺手补抓。

**对应源**:
- SRC-001 https://www.cdc.gov/act-early/milestones/9-months.html → 落地到 `10-sources/tier1-authoritative/raw/cdc_ltsae_9months.html`
- SRC-002 https://developingchild.harvard.edu/key-concept/serve-and-return/ → 落地到 `10-sources/tier1-authoritative/raw/harvard_serve_and_return.html`

**抓取后回填**:source yaml 的 `local_file` + `file_size_bytes` + 必要时 `metadata.last_reviewed`

---

## G2:Harvard "5 Steps for Brain-Building Serve and Return" PDF 待抓

**背景**:K-MECH-CROSS-001 的 `actions` 字段当前是基于 SR 概念的二手概述,**未** verbatim 自 5 Steps PDF。

**影响**:落地动作未达 verbatim 标准,Phase 1 必须补。

**待抓 URL**:
- https://harvardcenter.wpenginepowered.com/wp-content/uploads/2017/06/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf

**处理**:Phase 1 第一批 fetch 任务。

---

# 491 卡审计追加(2026-05-03)

> 来源:`00-meta/checkpoints/audit_report_491_cards_20260503.md` §3
> 跨 8 段 + 10 源 subagent 审计共发现 40+ 主题 gap,以下按段 + 严重度组织。

## P0 严重缺口(12 项)— 中国家长高频痛点,知识库无法应对真实场景

### G3 · S0 段 · 产检窗口
- **缺**:NT / 大排畸 / 糖耐 / B 群链 / 抗 D 注射 / 时间表
- **现状**:S0 段 14 张卡里 0 张涉及循证医学产检节点(SRC-010 Brazelton + SRC-014 Davies + SRC-016 Lillard 三源都不是产科文献)
- **影响**:这是 S0 段最大临床盲区
- **建议来源**:中文产科指南 / ACOG / WHO 产前保健

### G4 · S0 段 · 待产包 + 分娩计划 + 无痛分娩决策
- **缺**:临产 2 周操作清单 + 分娩计划模板 + 无痛分娩 Q&A
- **现状**:0 卡
- **建议来源**:Penny Simkin《The Birth Partner》/ 鲍秀兰孕产篇

### G5 · S0 段 · 妊娠并发症识别
- **缺**:妊高 / 妊糖 / 胎位异常 / 先兆早产 安全底线
- **现状**:0 卡(完全无医学风险预警)
- **建议来源**:ACOG 指南 / 中国妇产科教科书

### G6 · S1 段 · 新生儿黄疸 ✅ 已 resolved by 海蒂 SRC-040 C-S1-2203 (黄疸三类对比表)
- **缺**:生理性 vs 病理性区分 / 蓝光治疗指征 / 母乳性黄疸
- **现状**:0 卡
- **影响**:0-1 月最常见就医原因之一
- **建议来源**:SRC-008 AAP H&S / 鲍秀兰

### G7 · S1 段 · 脐带护理 + 残端脱落 ✅ 已 resolved by 海蒂 SRC-040 C-S1-2204 (脐带护理新立场) + C-S1-2221 (脐疝)
- **缺**:消毒方法 / 感染识别 / 脱落时间表
- **现状**:0 卡(产后第一周高频问题)
- **建议来源**:SRC-008 AAP

### G8 · S1 段 · 新生儿筛查 ✅ 部分 resolved by 海蒂 SRC-040 C-S1-2223 (听力) + C-S1-2202 (包皮)
- **缺**:足底血(PKU/CH/G6PD)/ CCHD 心脏 / 听力筛查不止迟发型
- **现状**:仅 C-S1-066 鲍秀兰覆盖了"听力筛查迟发型",其他新筛全部空白
- **建议来源**:SRC-008 AAP H&S

### G9 · S2 段 · 2 月儿保 + 第一波疫苗 ✅ 已 resolved by 海蒂 SRC-040 C-S2-2005..2010 (6 张) + C-S2-2105..2107 (退烧)
- **缺**:DTaP / Hib / IPV / PCV / HepB / Rotavirus 时间表 + 接种反应处理 + 中国一类苗 vs 美国 AAP 时间表对照
- **现状**:0 卡
- **影响**:1-3 月家长**最高频问的实操问题**(疫苗发热怎么办 / 自费 vs 免费选哪种 / 有点感冒能打吗)
- **建议来源**:AAP Red Book + 中国 CDC 免疫规划

### G10 · S2 段 · 早期昼夜节律萌芽 ✅ 已 resolved by 海蒂 SRC-040 C-S2-2011 (6-8 周 melatonin)
- **缺**:melatonin 6-8 周分泌 + 晚长睡形成的生理时间表
- **现状**:任务书 §2 S2 主题清单**明确列出**,52 张卡完全没有
- **建议来源**:AAP / Mindell 睡眠书 / Weissbluth Healthy Sleep Habits

### G11 · S3 段 · 母乳→混合喂养过渡 ✅ 已 resolved by 海蒂 SRC-040 C-S3-2147/2246/2247 (3 张:转奶节奏 + 拒奶瓶 + 直接学杯)
- **缺**:配方奶选购 / 一天混几次 / 怎样追奶 / 妈妈上班后挤奶
- **现状**:任务书 §2 S3 主题清单**明确列出**,56 张卡完全无覆盖
- **影响**:中文家长(产假 3-6 月结束高峰)的最大刚需,严重失重
- **建议来源**:La Leche League / WHO 母乳手册 / SRC-014 Davies Ch7

### G12 · S4 段 · 过敏原引入(LEAP 早暴露) ✅ 已 resolved by 海蒂 SRC-040 C-S3-2248/2249 (海蒂 2010 vs 2014 自我修正)
- **缺**:花生 / 鸡蛋 / 牛奶 / 鱼虾 6 月起早引入降低过敏风险
- **现状**:任务书明列,S4 段完全无独立卡;LEAP 试验 / AAP 2017 指南早引入花生是关键科学,C-S4-001(BLW)未触及
- **建议来源**:SRC-006 AAP Feeding

### G13 · S5 段 · 睡眠训练抉择(extinction / Ferber / no-cry / fading) ✅ 部分 resolved by 海蒂 SRC-040 C-S3-2258 (Ferber/改良) + C-S5-2152 (温和派)
- **缺**:跨派对比 — Lillard 关门睡 vs Davies 反训 vs Brazelton 温和拍背 vs AAP 6 月+ vs Bowlby 反对 vs Karp 5S 持续
- **现状**:6 派立场分散在多张单卡,**0 张跨派对比卡**
- **影响**:中国家长 9-12 月最高频痛点之一
- **建议来源**:综合 6 派立场 + Karp + Ferber + Sears + Mindell

### G14 · S6/S7 段 · 24 月 M-CHAT 自闭症筛查
- **缺**:AAP 推荐 18 月 + 24 月 M-CHAT 标准化筛查工具
- **现状**:0 卡(只有 C-S7-013 鲍秀兰 24 月红旗本土清单)
- **影响**:错过 24 月窗口可能延误自闭症早期识别
- **建议来源**:AAP Bright Futures + M-CHAT 筛查表

---

## P1 重要缺口(15+ 项)

### S0 段
- 产前抑郁筛查(EPDS / PHQ-9)
- 月子文化 vs 产后恢复循证对照
- 母乳喂养准备(乳房护理 / 泵奶器 / 哺乳姿势 / 初乳概念)

### S1 段
- 维生素 K 注射(出生后)
- 第一次儿保(3-5 天 / 2 周 / 1 月节点)
- PURPLE 完整框架(只有 C-S1-178 提"三 C")
- 原始反射全套(rooting/sucking/palmar/stepping/Babinski 系统卡)
- 配方奶冲调安全(水温 / 比例 / 储存)

### S2 段
- 被动免疫下降(母传 IgG 衰减曲线 + 为什么 2-6 月免疫低谷)
- 1-3 月配方奶量 + 间隔表 + 混喂节奏
- 大小便监测(6-8 周 poop 频率突降是正常)
- 浴疹 / 痱子 / 湿疹 / 脂溢性皮炎起点
- 喂养间隔(按需 vs 按时)跨源对照

### S3 段
- 4 月儿保 + 第二波疫苗
- 翻身后床上安全升级(脱包裹之外的环境清单)

### S4 段
- 噎食(choking)vs 干呕(gagging)区分
- "不爬也正常"AAP 立场(对冲鲍秀兰"缺爬有害"焦虑)
- 6 月儿保 + 第三波疫苗
- 9 月儿保 + ASQ 发育筛查
- babbling 辅音重复(Brazelton / Davies 视角缺)

### S5 段
- **指物 pointing / 意图性沟通**(任务书明列"语言能力最强预测因子")
- 戒夜奶时机
- 精细动作精度(钳取小物 / release / 堆塔)
- 物体永久性巩固阶段(A-not-B → 完整对象追踪)
- "母乳 1 岁后是否继续"立场对比

### S6 段
- 18 月儿保 + 第四波疫苗(中国本土疫苗)
- picky eating 全程指南(Brazelton 2 张 + 蒙氏立场缺)
- 牙刷训练 / 第一颗乳牙护理 / 龋齿预防
- 二孩家庭(老大反应 / 退化 / 嫉妒)
- 与祖父母教养不一致(中国独特困境)
- 想象游戏 / 假装游戏 / pretend play 萌芽
- 双语家庭策略 18-24 月词汇爆发

### S7 段
- 词汇爆炸 + 句子语法(SVO 主谓宾)
- 三岁的反叛("threes are worse than twos" 中国主流认知)
- 完整如厕训练方法论(分步 SOP)
- 36 月发育里程碑全检
- 第二胎适应(老大反应)
- 入园前的社交准备(2-4 周提前练习)

---

## P2 优化缺口(10+ 项)

- S0:准爸爸产前心理与角色重塑(非"挡门"维度)
- S0:胎儿期感官发育精确时间表(听 / 视 / 触 / 嗅 / 味)
- S0:产前依恋形成 / Bowlby 系统在 S0 完全空
- S0:高龄妊娠 / 多胎 / 辅助生殖特殊场景
- S1:胎记 / 蒙古斑 / 婴儿粉刺识别
- S1:体温警戒线分场景(腋温/肛温/耳温区分)
- S2:眼神交流 / mutual gaze 发育时间表
- S2:妈妈产后恢复(2-3 月 42 天复查 / 盆底 / 性生活回归 / 月经恢复)
- S3:DHA / EPA 补充 + 鱼油 vs 海藻油
- S3:secure base 萌芽实操 / Ainsworth 4 类入门
- S4:拍嗝 vs 不拍嗝(6-9 月是否还需要)
- S5:扩展辅食形态(块状 → 半固体 → 颗粒进阶)
- S5:tantrum 前兆识别 + 提前干预
- S6:1-2 岁睡眠总指南(夜醒 / 转单睡 / 戒夜奶)
- S6:18 月分离焦虑第二峰值实操
- S6:1-2 岁意外伤害预防 / babyproofing 升级
- S6:中国传统育儿对比(把屎把尿 / 老人喂饭追喂 / 中国式"礼貌")
- S7:幼儿园选择标准(蒙氏 vs 中式 vs 双语)
- S7:屏幕时间 2-3 岁界限
- S7:三角关系 / 父亲角色(2-3 岁 oedipal phase)

---

## 流派覆盖 gap

- 🟡 **RIE**:无独立 source(只在 Davies/Lillard 卡内引用 yes space / tarry time)— 建议抓 Gerber《Your Self-Confident Baby》
- 🟡 **Pikler**:无独立 source(只在 Davies/Lillard 卡内引用 floor bed / freedom of movement)— 建议抓 Pikler《Friedliche Babys》

---

## 术语词典 gap(2 个 P0 已修)

✅ 本次审计已新建:
- G-TERM-sensitive-periods(蒙氏核心,5+ 卡引用断链已修)
- G-TERM-observation(蒙氏方法论起点,4+ 卡引用断链已修)

待补:
- G-PERSON-Winnicott(Brazelton 多卡引用)
- G-PERSON-Erikson(Brazelton 多卡引用)
- G-PERSON-Ainsworth(Bowlby V1 12 卡缺)
- G-PERSON-Bruner(Gopnik C-S1-243)
- G-PERSON-Spelke(Gopnik 多卡)
- G-PERSON-Field(Gopnik C-S2-183)
- G-PERSON-Gerber(蒙氏 / Davies / Lillard yes space 来源)
- G-PERSON-Montessori(蒙氏理论原典作者)
- G-ABBR-Hib / G-ABBR-IPV / G-ABBR-PCV / G-ABBR-HepA / G-ABBR-HepB / G-ABBR-Varicella / G-ABBR-Rotavirus(疫苗高频)
- G-TERM-habituation(Brazelton 多卡)
- G-TERM-sleep-cycle(Brazelton 多卡)
- G-TERM-school-readiness(Brazelton 多卡)
- G-TERM-imaginary-baby(Brazelton 多卡)
- G-TERM-early-intervention(Brazelton)
- G-TERM-postpartum-blues(区分 PPD)
- G-TERM-medical-home / managed-care / call-hour / therapeutic-relationship(C-S0-007 一卡占 4 个孤儿)

---

*v2.0 — 491 卡审计追加。*

---

# Phase 13 SRC-031 WHO+UNICEF 喂养指南合集 WebFetch 失败记(2026-05-04)

## G_WHO_1:Innocenti Declaration 1990 + 2005 全文

**背景**:Innocenti Declaration 1990(BFHI 启动政治基础)+ 2005 补充版,UNICEF Florence Innocenti 中心起草。

**尝试 URLs**:
- https://www.unicef.org/innocenti-declaration-1990 — 403
- https://www.unicef.org/nutrition/innocenti-declaration — 404
- https://www.unicef.org/innocenti — 403
- https://www.unicef-irc.org/research/innocenti-declaration/ — redirect 失败
- https://en.wikipedia.org/wiki/Innocenti_Declaration — 404
- https://en.wikipedia.org/wiki/Innocenti_Declaration_on_the_Protection,_Promotion_and_Support_of_Breastfeeding — 404

**目前覆盖**:高层 framing 通过 BFHI Wikipedia 间接捕获(1990 Innocenti 是 BFHI 启动的政治基础)。

**缺失**:
- 1990 原版 4 大操作目标精确措辞(BFHI / Code 立法 / 国家协调员 / 立法保护)
- 2005 补充 9 大目标(2025 全球量化指标)
- 各国签署状态(中国是否签)

**处理**:跳过 Innocenti 独立卡,在 SRC-031 综述卡 + Code 卡里间接引用。

---

## G_WHO_2:Acceptable Medical Reasons for Breast-milk Substitutes (WHO/UNICEF 2009)

**背景**:WHO/UNICEF 2009 联合发布,临床医生用清单 — 哪些情况下可以(也只在这些情况)使用配方奶。

**尝试 URLs**:
- https://www.who.int/publications/i/item/WHO-NMH-NHD-09.01 — 404

**目前覆盖**:BFHI 第 6 步 "unless medically indicated" 间接覆盖。

**缺失**:
- 婴儿端清单:半乳糖血症 / 苯丙酮尿症 / 枫糖尿症 / 极低出生体重(<1500g)/ 早产(<32 周)/ 严重窒息 / 严重高胆红素血症
- 母亲端清单:HIV(高资源区 + AFASS 满足时)/ 严重疾病(脓毒症 / 心力衰竭) / 1 型疱疹乳房病灶 / 化疗 / 放射性药物 / 精神药物中部分类
- 临时停母乳 vs 完全停的鉴别

**处理**:在 HIV+ 卡 + Acceptable Reasons 综述卡里覆盖框架,具体清单作为后续补强。

---

## G_WHO_3:PAHO/WHO Guiding Principles for Complementary Feeding (2003) 10 大原则全文

**背景**:PAHO/WHO 2003 发布,辅食 10 大指导原则(全球辅食实操圣经)。

**尝试 URLs**:
- https://www.paho.org/hq/dmdocuments/2009/principlescompfeeding.pdf — 404
- https://en.wikipedia.org/wiki/Complementary_feeding — 404

**目前覆盖**:WHO Complementary Feeding 主页拿到 4 支柱 + 月龄餐数(D6 文档)。

**缺失**:
- 10 条原则精确措辞(及时性 / 充分性 / 安全性 / 反馈式 之上还有 6 条:多样性 / 频次 / 食物质地 / 母乳延续 / 维生素强化 / 卫生)
- 中国家长辅食实操对接

**处理**:核心 4 支柱 + 月龄餐数已在 D6 / SRC-031 中,具体 10 条记 gap 待后续补 PDF。

---

*v2.1 — Phase 13 SRC-031 WHO 失败记(2026-05-04)。*



---

# v2.2 追加 · 2026-05-04 审计 · 4 项新缺口

> 来自 `audit_report_remaining_cards_20260504.md` Phase C 跨段 dedup 发现的主题缺位。

## G_AUDIT_2026_05_04_001 · Gottman emotion coaching 派完全缺位

**段位**:S6 / S7 / S8 普遍

**缺**:Gottman emotion coaching 5 步法(Aware / Recognize / Validate / Help label / Set limits)是 SEL 教养主流,但本知识库:
- SRC-019 Lansbury / SRC-021/022 Gerber 都引"接受感受 + 限度行为"但没直点 Gottman
- SRC-027 V3 Saarni 4 类情绪应对 vs Gottman 5 步法不是同一框架
- SRC-029 V4 CASEL 5 能力 vs Gottman emotion coaching 是平行框架

**严重度**:P1

**建议来源**:Gottman《The Heart of Parenting》/ Gottman-Declaire 1997 / Lerner V4 Ch15 SEL 章引

**处理**:补 1 卡(C-S7-NEW-GOTTMAN)说明 5 步法 + 跟现有 RIE/CASEL 框架对照

---

## G_AUDIT_2026_05_04_002 · 松田"反 反抗期 标签"独立卡缺

**段位**:S6 / S7

**缺**:任务书提及松田 §387 反"反抗期"立场,但 S6 段未见独立卡(C-S6-669 接近但只讲"躺地哭")— Phase C S6 hotspot 2 明确发现。

**现状**:C-S7-604(SRC-023 §387)在 S7 段已有,但 S6(12-24 月)缺一张同立场卡

**严重度**:P2

**处理**:从 C-S7-604 派生 1 卡到 S6 段,或 C-S6-1079(Erikson autonomy)加松田对照立场段

---

## G_AUDIT_2026_05_04_003 · Lillard 蒙氏 toilet training 12-18 月时机未独立成卡

**段位**:S6

**缺**:Lillard SRC-016 蒙氏立场 12-18 月敏感期(任务书 conflicts.md A4 明列)— 在 S7-MC-01 4 派对照中提到但 S6 无独立卡

**严重度**:P2

**处理**:补 C-S6-NEW-LILLARD-POTTY,展开 Lillard 12-18 月敏感期 + 蒙氏小马桶哲学

---

## G_AUDIT_2026_05_04_004 · 海蒂 / 松田 toilet training 视角未独立成卡

**段位**:S7 / S6

**缺**:海蒂《育儿大百科》对 toilet training 的中道立场 + 松田 §366 把屎把尿对照(S6 卡 C-S6-823 偏向操作 1.5 岁夏天撤尿布,无总论)

**严重度**:P2

**处理**:补 海蒂 toilet training 总论卡(C-S7-NEW-HEIDI-POTTY)+ 松田 toilet learning 总论卡

---

*v2.2 完。本次审计共追加 4 项主题缺口,均为 P1-P2 优先级,Gottman emotion coaching 派最大(覆盖 S6-S8 全段)。*
