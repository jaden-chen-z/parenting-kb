# Phase 14 SRC-040 Heidi 反向覆盖审计 (Phase C)

**日期**: 2026-05-04
**审计员**: Phase C subagent (反向覆盖审计)
**Phase B 已产**: 146 张海蒂卡(s0=30 / s1=31 / s2=16 / s3=26 / s4=13 / s5=23 / s6=5 / s7=2)
**Phase C 决定补**: 10 张

---

## 1. 抽样章节清单

按 part_01..07 各做 3 段抽样(头部 / 中部 / 尾部)+ 27 个高价值关键词主题搜索:

| Part | 主题域 | 抽样侧重 |
|---|---|---|
| part_01 | 孕产准备 / 母乳 / 配方 / 婴儿用品 / 选医生 | 母乳 vs 配方权衡(已覆盖)、初乳、乳头护理、婴儿监视器、奶嘴/奶瓶、安全座椅 |
| part_02 | 新生儿期 / 哺乳实操 / 维生素 / 哺乳问题 | 维生素 D、铁补充、洗澡、日夜颠倒、肠绞痛、牛奶过敏、乳头混淆 |
| part_03 | 1-3 月 / 语言交流 / 第三月喂养 | 儿语、外语、按摩、便秘、心杂音、撞头/扭头 |
| part_04 | 4-6 月辅食 / 翻身 / 浴缸 | 安全喂养、辅食卫生、洗澡安全、过敏原引入(已覆盖)、手指食物 |
| part_05 | 7-9 月精细动作 / 季节性安全 | 拍手游戏、夏季水中毒、防蚊、戏水安全 |
| part_06 | 10-12 月感冒/流感 / 早产儿 / 特殊需要 | 感冒红旗(已覆盖)、流感疫苗(已覆盖)、早产儿喂养、特殊需要儿 |
| part_07 | 妈妈恢复 / 爸爸专章 / 二胎 / 收养 | 凯格尔(已覆盖)、产后体型、永久避孕、收养祖父母 |

**抽样关键词搜索**(确认源覆盖+ Phase B 是否已产):
- ✅ 已 Phase B 覆盖: 黄疸 / PURPLE 哭(C-S1-178 鲍秀兰 + 已有海蒂卡)/ 包皮环切 / 母乳储存 / 哺乳期避孕 / 父亲产后抑郁 / 大便颜色 / CPR / 撞头 / 烫伤 / 选医生 / 包裹 / 共睡 / 月嫂
- ❌ 海蒂源**有详细论述但 Phase B 漏掉**: 维生素 D / 铁 / 婴儿按摩 / 肠绞痛(海蒂版)/ 偏头颅预防 / 乳头疼痛 / 涨奶 / 出生一小时初乳 / 乳腺炎 / 安全座椅后向朝向 / 哺乳禁忌物 / 婴儿背带袋鼠护理 / 哺乳期咖啡因 / 浴缸排水恐惧

---

## 2. 漏掉但应补的清单 + 决策

| # | 漏掉主题 | 段 | 海蒂源覆盖度 | 跨源现状 | 决策 | 理由 |
|---|---|---|---|---|---|---|
| 1 | 母乳宝宝从出生 2 周补 VD 400 IU | S1 | part_02 重点专栏 | ❌ S1 完全无 VD 卡(C-S1-095 抚触 / C-S2-1341 是其他维生素)| **补** | gaps.md P0 类高频问题,海蒂明确给出 AAP 方案 |
| 2 | 4-6 月起补铁的判断 | S3 | part_02+part_03 | ❌ S3 无独立铁卡 | **补** | 海蒂明确"4-6 月铁库耗尽",中国家长高度焦虑铁缺乏的关键节点 |
| 3 | 婴儿按摩 7 大好处 + 5 步法 | S2 | part_03 整章 | ❌ 0 张按摩主题卡(grep "按摩"无独立卡)| **补** | 海蒂罕见地把按摩放专章,跨派(早产儿研究)有效性证据级别高 |
| 4 | 肠绞痛海蒂版安抚清单(5S 之外的 8 招)| S1 | part_01+part_02 | ✅ Karp 5S 已覆盖,❌ 海蒂额外维度无 | **补** | 海蒂列了"白噪音/换姿势/换喂养人/草药茴香水/试戒咖啡因"等 Karp 之外的招数,跨派对照价值 |
| 5 | 偏头颅(扁头综合征)预防 + 修复 | S1 | part_02@24367 头型/part_05@7175 | ❌ 0 张(只有撞头红旗卡)| **补** | 仰睡时代独有问题,海蒂给"清醒时多变换体位 + tummy time + 头部变化方向"操作 |
| 6 | 安全座椅 1 岁前必须后向 | S0 | part_01@2645 显眼专栏 | ❌ S0 育儿装备卡只覆盖"婴儿用品别买全套",安全座椅朝向无 | **补** | 美国 AAP 强烈底线,中国家长普遍把后向当 6 月就翻 |
| 7 | 乳头疼痛 + 皲裂 7 步处理 | S1 | part_01@71xxx | ❌ 已有"哺乳新妈妈"卡未涉及,跨源 Davies/AAP 也不细 | **补** | 母乳第一周最高离乳率原因,实操级清单 |
| 8 | 涨奶/堵奶/乳腺炎三阶梯识别 | S1 | part_01+part_07 | ❌ 0 卡(grep 全库无)| **补** | 海蒂区分三阶段症状+处理,跨源完全空白 |
| 9 | 哺乳期 5 类禁忌(尼古丁/酒精/咖啡因/草药/特定药物)| S1 | part_01@90277 | ❌ 已覆盖"真正不能母乳的 7 种情况"是疾病维度,饮食/烟酒/咖啡因维度无 | **补** | 中国哺乳妈妈高频疑问("哺乳能喝奶茶吗")|
| 10 | 婴儿背带袋鼠护理(babywearing) | S1 | part_01@57002 | ❌ 0 张背带主题卡 | **补** | 海蒂罕见用"袋鼠/有袋动物"框架推 babywearing,与肠绞痛安抚强关联 |

---

## 3. 跳过的高价值候选 + 理由

| 候选 | 跳过理由 |
|---|---|
| 出生黄金一小时 / 早接触 / 初乳重要性 | SRC-031 WHO BFHI 段已强覆盖(早接触+初乳是 BFHI 第 4 步) |
| 哺乳姿势 4 种(摇篮/橄榄球/侧卧/交叉)| 跨派太普及,Davies + AAP + WHO 均有,海蒂版仅图示无独家 |
| 乳头混淆 6 周前不引入奶瓶 | 已有 C-S1-2xxx "母乳娃拒奶瓶 6 周前就该练"反向覆盖 |
| 婴儿生长曲线判读 | 跨源已多次覆盖(SRC-008 AAP H&S / 鲍秀兰),海蒂无新增 |
| 心杂音绝大多数无害 | 单一议题适合疾病百科卡,海蒂只 2 句话不够独立成卡 |
| 婴儿监视器选购 | 装备类已有"婴儿用品别买全套",此为子项不必单卡 |
| 浴缸排水恐惧/水温 49°C | 安全细节,可并入未来 babyproofing 大卡,单卡价值低 |
| 蜂蜜 1 岁前禁 | 海蒂明确,**但跨源 SRC-006 AAP Feeding 已强覆盖**,且不是海蒂独家 |
| 果汁稀释/拒喂果汁 | 与上同理,AAP 主导立场 |
| 永久避孕(输卵管/输精管)| 偏离育儿核心,产后避孕已有黄体酮卡覆盖最常用方案 |
| 收养祖父母态度 | 边缘人群议题,适合特殊家庭专题不补主线 |
| 早产儿全套护理 | part_06 整章但有专书 SRC 覆盖更深,Heidi 大众百科版本不增量 |

---

## 4. 实际补卡 10 张

| ID | Title | Stage | Tags |
|---|---|---|---|
| C-S1-2500 | 母乳宝宝从 2 周起补 VD 400 IU | S1 | safety |
| C-S3-2400 | 铁库 4-6 月耗尽,饮食铁主补 | S3 | safety |
| C-S2-2200 | 婴儿按摩 7 大好处 + 5 步法 | S2 | - |
| C-S1-2501 | 肠绞痛安抚 8 招(5S 之外) | S1 | controversy |
| C-S1-2502 | 偏头颅预防:醒着多变体位 + 头方向轮换 | S1 | safety |
| C-S0-2400 | 1 岁内汽车安全座椅必须后向 | S0 | safety, red_flag |
| C-S1-2503 | 乳头疼痛/皲裂 7 步处理 | S1 | - |
| C-S1-2504 | 涨奶 → 堵奶 → 乳腺炎 三阶梯识别 | S1 | safety, red_flag |
| C-S1-2505 | 哺乳期 5 类禁忌:烟/酒/咖/草药/某药 | S1 | safety |
| C-S1-2506 | 婴儿背带袋鼠护理 5 益处 | S1 | - |

---

## 5. 卡片正文(主线 Python 搬到目标目录)

```yaml
card_id: C-S1-2500
stages: [S1]
tags: [safety]

front:
  title: 母乳宝宝从 2 周起补 VD 400 IU
  hook: 配方娃日量 450 克奶不用补

back:
  why_matters: |
    维生素 D 是骨骼发育必需,缺乏直接造成佝偻病。
    宝宝靠晒太阳合成 VD,但防晒衣 + 防晒霜 + 冬季长 + 北方城市,大部分宝宝晒不够。
    白皮肤宝宝每周晒 15 分钟、深色皮肤更长才达标 — 现实里很难持续达到。
    母乳本身 VD 含量极低(妈妈再怎么吃都补不上),所以 AAP 建议**纯/混母乳宝宝从出生头 2 个月起就开始补 VD**。
    配方奶里通常已强化 VD,**每天喝 ≥ 450 克配方奶的宝宝不用额外补**(补多反而中毒)。
  what_to_do:
    - 纯/混母乳宝宝:出生 2 周内开始,每日 400 IU 滴剂滴口腔
    - 混合喂养:算配方奶量,每日不到 450 克 → 仍按 400 IU 补
    - 配方奶 ≥ 450 克/日 → 不补,过量风险高
    - 选液体型滴剂(常含 A+C+D 三联),不用胶囊
    - 持续补到 1 岁后转全脂奶时再评估
  failure_mode: |
    "晒太阳就够"是误区 — 都市生活、防晒习惯、季节都让晒太阳达标率极低。
    给配方娃额外补 VD → VD 中毒(高钙血症 / 肾损伤)。
  evidence_level: A

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 6 章 第 1 个月 · 补充剂的意义 · 维生素 D 专栏"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S3-2400
stages: [S3]
tags: [safety]

front:
  title: 铁库 4-6 月耗尽,饮食铁主补
  hook: 母乳娃 6 月后必须配铁辅食

back:
  why_matters: |
    缺铁不是小事 — 头 18 个月缺铁会造成不可逆的神经发育和行为问题。
    足月宝宝在妈妈肚子里囤了一定量铁,但**4-6 月这批储备就耗完了**。
    分两路:
    1) 配方奶娃:加铁配方奶持续供应,通常不用单独补
    2) 母乳娃:母乳铁含量低,**6 月起靠辅食补铁**(铁强化米粉、肉泥、含铁绿叶蔬菜)
    早产儿 / 出生体重低的宝宝是例外,医生会开口服铁补充液。
    海蒂明确:**正常足月宝宝别自行买铁补充液**,过量风险高,饮食路径足够。
  what_to_do:
    - 母乳娃:6 月辅食起加铁强化米粉作为第一口固体
    - 餐内加肉泥(红肉铁吸收率最高)+ 蛋黄(8 月起)
    - 同餐配维生素 C 食物(柑橘 / 西兰花 / 红椒)→ 提升铁吸收
    - 配方奶娃:坚持加铁配方奶,辅食铁是锦上添花
    - 6/9/12 月儿保查 Hb,异常再加补充剂
  failure_mode: |
    家长怕宝宝缺铁自购铁补充液 → 海蒂反对,胃肠不适且过量有毒。
    迷信"红枣红糖红米"补铁 — 植物铁吸收率仅 2-5%,远不如肉泥。
    辅食只给米糊 + 蔬菜泥不加肉,6-9 月最容易缺铁。
  evidence_level: A

glossary_refs: []

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 6 章 补充剂的意义 · 铁元素专栏 + 第 9 章 黑便讨论"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S2-2200
stages: [S2]
tags: []

front:
  title: 婴儿按摩 7 大好处 + 5 步法
  hook: 早产儿研究证据,健康娃同样受益

back:
  why_matters: |
    婴儿按摩不再是玄学,早产儿临床研究证实:按摩组**入睡更快、呼吸更顺、更机灵**。
    扩展到健康宝宝同样有效。海蒂列出 7 大效益:
    1) 增强免疫 2) 强化肌肉发育 3) 刺激生长 4) 缓解肠痉挛
    5) 改善出牙痛 6) 促进睡眠 7) 减压(宝宝也有压力)
    额外赠品:**家长按摩时也减压,被证实可缓解产后抑郁症状**。
    充满爱意的触摸还能减少宝宝攻击行为,长期亲子关系投资。
  what_to_do:
    - 选你和宝宝都放松的时间(洗完澡后/游戏前最佳),关电话
    - 房间 ≥ 24°C(宝宝脱衣只穿尿布),灯光调暗
    - 用婴儿专用按摩油(冷压植物油,不用花生油 — 致敏)
    - 顺序:腿 → 脚 → 腹(顺时针)→ 胸 → 手臂 → 背 → 头
    - 按摩力度像揉面团,宝宝表情拒绝就停;每次 10-15 分钟
  failure_mode: |
    饥饿/刚吃饱时按摩 → 宝宝抗拒或吐奶。
    用花生油等坚果油 → 增加 2 岁前花生过敏风险(海蒂明确警示)。
    把按摩当治病(发烧/急性病)硬做 → 拖延就医。
  evidence_level: B

glossary_refs: []

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 8 章 第 3 个月 · 婴儿按摩专章"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2501
stages: [S1]
tags: [controversy]

front:
  title: 肠绞痛安抚 8 招(5S 之外)
  hook: Karp 5S + 海蒂额外维度

back:
  why_matters: |
    Karp 5S(包裹/侧卧/嘘声/摇晃/吸吮)是肠绞痛安抚的金标准 — 但**不是每个宝宝都对 5S 全部买账**。
    海蒂提供 5S 之外的备选维度,让父母在"哭了 1 小时还在哭"时多 8 招可试:
    其中**戒咖啡因**对部分母乳宝宝立竿见影,**茴香水/草药** AAP 中立但海蒂列入,需警惕。
  what_to_do:
    - 妈妈戒咖啡因 1 周看变化(母乳娃高度敏感)
    - 换喂养人:让爸爸/外婆抱,有时换味道有效
    - 白噪音(吹风机/吸尘器/白噪音 App),持续 5-10 分钟
    - 婴儿背带 babywearing 边走边轻拍(C-S1-2506 关联)
    - 换姿势:飞机抱、趴在大人前臂、蹬腿动作
    - 户外散步:温度变化和环境刺激常奏效
    - 温水澡 + 之后腹部按摩(顺时针)
    - 牛奶蛋白排查:连续 2 周避所有奶制品(母乳妈妈或换水解奶粉),复评
  failure_mode: |
    试 1 招 5 分钟没效就换 → 海蒂强调每招至少坚持 10 分钟。
    用茴香水 / 益生菌等"偏方"不告知医生 → 部分草药对婴儿肝有毒。
    肠绞痛全归因牛奶蛋白过敏 → 真过敏率不到 1%,别盲目换奶粉。
    哭超 3 小时还安抚不下来 + 发烧/呕吐 → 不是绞痛,送医。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 7 章 第 2 个月 · 肠痉挛专题"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2502
stages: [S1]
tags: [safety]

front:
  title: 偏头颅预防:醒着多变体位 + 头方向轮换
  hook: 仰睡时代的副产品,清醒时主动救

back:
  why_matters: |
    AAP 仰睡防 SIDS 拯救了无数婴儿,**但副作用是宝宝后脑/侧脑被压成扁/偏的概率上升**。
    海蒂明确:**轻中度偏头颅自己不会修复**,但发现早 + 主动干预多数能改善;严重要戴矫形头盔。
    关键窗口:**0-4 月**颅骨可塑性最强,4 月之后干预效果递减。
    根本原理:仰睡 + 推车 + 提篮 + 抱姿都让一个固定面持续受压。
  what_to_do:
    - 仰睡仍然坚持(SIDS 第一原则不动摇)
    - **每天清醒至少 30 分钟 tummy time**,分多次累计
    - 抱姿/喂奶左右轮换(每次换边,别永远习惯一边)
    - 婴儿床头位置每周左右调一次(让宝宝看人/光的角度变)
    - 推车/汽车座椅别长时间(单次 < 90 分钟)
    - 4 月仍明显偏 → 找儿科评估,必要时戴矫形头盔(6-12 月效果最好)
  failure_mode: |
    觉得"长大自己就圆了"等到 6 月才行动 → 颅骨可塑窗口已晚。
    为防偏头让宝宝侧睡或趴睡 → SIDS 风险倍增,绝对禁。
    无差别让宝宝睡定型枕 → 海蒂 + AAP 都明确反对,枕头 = SIDS 凶手。
  evidence_level: B

glossary_refs:
  - G-ABBR-SIDS
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 5 章 新生儿护理 · 头型问题 + 第 11 章 撞头摇头扭头"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S0-2400
stages: [S0]
tags: [safety, red_flag]

front:
  title: 1 岁内汽车安全座椅必须后向
  hook: 美国 AAP 死命令,中国家长普遍违规

back:
  why_matters: |
    海蒂在第二版前言把"1 岁前必须后向安全座椅"列为**最重大的更新指南**之一,与"仰睡防 SIDS"并列。
    原理:婴儿头部相对身体大、颈部肌肉弱,正面碰撞时**前向座椅会让头部猛甩,颈椎易折**;后向座椅让宝宝整个背部分散冲击力,生还率提升 5 倍。
    AAP 最新建议:**至少到 2 岁,理想到座椅体重上限**(很多座椅可后向到 18 公斤,够用到 4 岁)。
    后排中央位置 > 后排两侧 > 副驾(绝对禁,气囊弹出会致命)。
  what_to_do:
    - 出院第一程:后向安装在后排中央,角度 45 度
    - **绝不**为了能看脸把座椅转前向(可买后视镜挂前座椅背)
    - 1 岁前不要换前向(海蒂底线),AAP 推到 2 岁后
    - 副驾驶气囊未关 → 任何朝向都不能放儿童
    - 座椅二手别用(撞过的有微裂),自己买新的
    - 安装后晃动 < 2.5 cm 才算合格
  failure_mode: |
    "宝宝哭闹要看见我才行"→ 转前向,撞车致命率倍增。
    把宝宝放副驾大人怀里 → 副驾气囊弹出 = 致命武器。
    冬天厚衣服直接绑安全座椅 → 安全带松紧不准,撞击时宝宝飞出。
    出门只 5 分钟没装座椅 → 90% 致命事故离家 5 公里内。
  evidence_level: A

glossary_refs:
  - G-ABBR-AAP
  - G-ABBR-SIDS

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第二版前言 + 第 2 章 婴儿装备 · 汽车安全座椅"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2503
stages: [S1]
tags: []

front:
  title: 乳头疼痛/皲裂 7 步处理
  hook: 第一周离乳率最高的元凶

back:
  why_matters: |
    乳头疼痛是产后第一周妈妈放弃母乳的**头号原因**(海蒂数据)。
    根本原因 90% 是**含接姿势不对**(只含乳头没含乳晕)。
    痛 = 信号灯,不是"忍忍就好"。皲裂 = 真伤,继续硬喂会感染演变乳腺炎(C-S1-2504 关联)。
    海蒂强调:**先调含接，调好后疼痛 24-48 小时缓解;调不好就找哺乳顾问**。
  what_to_do:
    - 调含接:宝宝嘴张大如打哈欠时塞入,乳晕含进至少 2.5 cm
    - 喂完后:挤几滴自己的母乳涂乳头(天然抗菌,自然风干)
    - 用纯羊毛脂(Lanolin)厚涂,不用洗就能喂下顿
    - 哺乳前热敷 + 哺乳间冷敷(冷冻圆白菜叶贴胸有效)
    - 换哺乳姿势:皲裂面避开宝宝下颚(用橄榄球抱替交叉)
    - 每次哺乳从**不痛**那一边开始(疼侧已激活泌乳)
    - 用乳头保护罩仅是过渡,长期会减少奶量
  failure_mode: |
    疼忍着继续 → 24 小时内皲裂出血 → 1 周乳腺炎。
    用肥皂/酒精消毒乳头 → 洗掉天然保护脂,加重皲裂。
    呕吐物带血以为宝宝出血 → 其实是吸到妈妈伤口的血,先排查自己乳头。
    皲裂 + 发烧 → 已是乳腺炎,立即就医(看 C-S1-2504)。
  evidence_level: B

glossary_refs: []

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 3 章 母乳喂养 · 乳头疼痛专题"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2504
stages: [S1]
tags: [safety, red_flag]

front:
  title: 涨奶 → 堵奶 → 乳腺炎 三阶梯识别
  hook: 越早处理越简单

back:
  why_matters: |
    哺乳前 2 周妈妈最常遇到的乳房问题三阶梯:涨奶(engorgement)→ 局部堵奶(plugged duct)→ 乳腺炎(mastitis)。
    分阶梯识别 + 对症处理是关键 — **早期热敷 + 多喂 90% 自愈,拖到乳腺炎要抗生素**,2% 演成乳腺脓肿要手术。
    海蒂区分症状:涨 = 全乳房硬、对称;堵 = 局部硬块、皮肤正常;乳腺炎 = 红/热/痛 + 发烧 ≥ 38°C + 类流感肌肉酸痛。
  what_to_do:
    - 涨奶:多喂 + 喂前热敷 + 喂后冷敷,2-3 天自然平衡
    - 堵奶:喂时用宝宝下巴对准硬块、按摩从硬块往乳头方向推,每次喂这一侧
    - 乳腺炎红旗(任一项即就医):一侧红肿热痛 / 发烧 ≥ 38°C / 全身酸痛 / 硬块 24 小时不消
    - 乳腺炎处理:**继续哺乳**(细菌不会感染宝宝,反而帮你排空)+ 抗生素 10-14 天 + 大量休息
    - 卷心菜冷敷叶贴胸 20 分钟可缓解涨痛
    - 乳头保护罩出门别忘记戴(吸湿垫频繁换)
  failure_mode: |
    涨奶停喂"让奶散了" → 越积越严重,72 小时演堵奶。
    乳腺炎停喂宝宝 → 错!继续喂才能排空脓液,停喂 = 加重。
    硬块 24 小时不消 + 发烧 → 不是堵奶是乳腺炎,自服抗生素错(剂量/时长不对)。
    乳房脓肿不切开排脓自我吸收 → 不可能,延误成败血症。
  evidence_level: A

glossary_refs: []

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 3 章 母乳喂养 · 涨奶/堵奶/乳腺炎专题 + 第 23 章 产后恢复"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2505
stages: [S1]
tags: [safety]

front:
  title: 哺乳期 5 类禁忌:烟/酒/咖/草药/某药
  hook: "能喝奶茶吗"高频问题底线

back:
  why_matters: |
    哺乳妈妈饮食比孕期宽松,**但仍有 5 类硬底线**(海蒂明确):
    1) **尼古丁**:>1 包/天 → 减奶量 + 宝宝焦躁;长期影响未知但肯定无好处
    2) **酒精**:可偶尔(每天 ≤ 1 杯啤酒/红酒),且要喂奶后 2 小时再喝
    3) **咖啡因**:200 mg/天上限(约 2 杯美式),宝宝代谢咖啡因极慢,会累积
    4) **草药/中药**:大多数无安全数据,胡芦巴(下奶)有血压心率影响
    5) **特定药物**:抗癌药、含锂的、麦角胺(治偏头痛)、放射性药物绝禁
    家庭小药柜常见的青霉素/对乙酰氨基酚/感冒药多数安全,但开新药一律先咨询。
  what_to_do:
    - 喝酒 → 喂奶后立即喝 1 杯,等 2 小时再下次喂(肝代谢)
    - 戒不掉烟 → 至少喂奶 1 小时后再吸,别在宝宝旁边吸
    - 咖啡 ≤ 2 杯/日,下午 4 点后避免(影响宝宝夜睡)
    - 中药 / 凉茶 / 月子草药 → 让中医师告诉哺乳期是否能服(不要自服)
    - 看任何科 → 主动告知"哺乳期",医生会换药
    - 网查"L1-L5 哺乳安全等级"(LactMed 数据库)
  failure_mode: |
    "1 杯奶茶没事"喝 3 杯 → 咖啡因累积宝宝整夜哭闹。
    "中药天然安全"吃下奶汤 → 胡芦巴影响哺乳妈妈血压。
    哺乳期发烧自服强力感冒药 → 多数含伪麻黄碱(回奶)+ 镇静剂(宝宝嗜睡)。
    放射检查不告知"哺乳" → 部分造影剂需暂停哺乳 24 小时。
  evidence_level: A

glossary_refs: []

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 3 章 母乳喂养 · 避免摄入的食物 + 药物章节"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

```yaml
card_id: C-S1-2506
stages: [S1]
tags: []

front:
  title: 婴儿背带袋鼠护理 5 益处
  hook: 几千年人类智慧,现代证据加持

back:
  why_matters: |
    "穿宝宝出门"(babywearing)不是新潮 — 几千年来有袋动物和大多数人类文化都这么干。
    海蒂列出 5 大益处:
    1) **方便**:父母腾手做事(做饭/带老大)
    2) **宝宝舒适**:被抱+体温+心跳=宫内环境复刻
    3) **父母快乐**:亲密接触刺激催产素,降低产后焦虑
    4) **减肠绞痛**:背带里直立位 + 节奏感 = 黄金安抚(C-S1-2501 关联)
    5) **促进发育**:宝宝看世界视角丰富,语言输入更多
    海蒂提醒区分类型:新生儿用包裹式/环式("自然胎位"),坐稳后才能用前向背架。
  what_to_do:
    - 0-4 月:包裹式(Wrap)或环式(Ring sling),宝宝面朝里贴胸
    - 4-6 月:前向背带(SSC 软结构),仍面朝里
    - 6 月后(能稳定坐):面朝外或背后
    - 安全口诀"TICKS":Tight 紧 / In view 看见脸 / Close enough to kiss 能吻到 / Keep chin off chest 下巴抬起 / Supported back 背部支撑
    - 单次背 ≤ 2 小时,中间放下活动
    - 宝宝睡着 → 立即检查呼吸道(下巴别贴胸)
  failure_mode: |
    背带太松 + 宝宝下巴贴胸 → 气道阻塞窒息(背带类 SIDS 实有案例)。
    新生儿用前向硬背架 → 颈部不能撑头部,易窒息。
    背着做剧烈运动/骑车/烹饪热油 → 宝宝撞伤/烫伤风险。
    觉得"包裹式总安全"忘 TICKS → 仍可窒息。
  evidence_level: B

glossary_refs:
  - G-ABBR-SIDS

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1岁"
  authors:
    - Heidi Murkoff
    - Sandee Hathaway
    - Arlene Eisenberg
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(新经典发行)"
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh:
    - 莫夏迪
    - 张敏
  location: "第 2 章 婴儿装备 · 婴儿背带或吊忽专题"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 6. 主线 Python 搬运脚本(供主线执行)

```python
import re, os
plan = '/Users/jjjjadennnn/Desktop/parenting-kb/00-meta/checkpoints/PHASE14_AUDIT_PLAN.md'
with open(plan) as f: text = f.read()
blocks = re.findall(r'```yaml\n(.*?)```', text, re.DOTALL)
stage_dirs = {
    'S0': 's0-pregnancy', 'S1': 's1-newborn', 'S2': 's2-1to3mo',
    'S3': 's3-3to6mo', 'S4': 's4-6to9mo', 'S5': 's5-9to12mo',
    'S6': 's6-12to24mo', 'S7': 's7-24to36mo',
}
base = '/Users/jjjjadennnn/Desktop/parenting-kb/30-cards'
for b in blocks:
    cid = re.search(r'card_id:\s*(C-S\d-\d+)', b).group(1)
    stage = re.search(r'stages:\s*\[(S\d)\]', b).group(1)
    out = f'{base}/{stage_dirs[stage]}/{cid}.yaml'
    with open(out, 'w') as fo: fo.write(b.rstrip() + '\n')
    print(f'wrote {out}')
```

---

## 7. 总结

- 抽样了 part_01..07 各 3 段 + 27 个高价值关键词
- 识别 22 个**漏掉**主题候选,最终决定**补 10 张、跳 12 张**
- 跳的 12 张要么跨源已强覆盖、要么海蒂无独家增量、要么主题边缘
- 补的 10 张全部是**海蒂独家详解 + Phase B 漏掉 + 中国家长高频痛点**(VD/铁/按摩/肠绞痛 8 招/偏头颅/后向座椅/乳头疼/乳腺炎三阶梯/哺乳禁忌/babywearing)
- 全部按 v3.5 schema, source_id="SRC-040", citation 沿用 Phase B 格式, failure_mode 必填
- 卡 ID 严格按 buffer:S0=2400, S1=2500-2506, S2=2200, S3=2400 全部 Phase B 之外

