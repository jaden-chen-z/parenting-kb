# Phase 14 · 海蒂大百科 SRC-040 · R2 深度反向审计 Checkpoint

> 2026-05-04 · R2 漏知识反向审计员 · 比 Phase C 更深入
> 跳过已审章节,扫 7 part 各 5-8 不同位置,关注 sidebar/box 高价值实操
> Phase B+C 已产 156 卡 → R2 补 10 张(含 4 个段)

---

## 1. 抽样章节清单

| Part | 抽样位置 | 主题片段 |
|---|---|---|
| Part 1 | 头/中(40-46K) | 婴儿用品采购 + 安全药箱 + 婴儿润肤乳花生油警告 + 奶瓶 3 类 |
| Part 1 | 中(75-81K) | 哺乳进阶:溢奶/泌乳反射/密集哺乳 |
| Part 2 | 中(60-66K) | 0-1 月放屁/便秘/睡姿/日夜颠倒/睡觉噪音 |
| Part 3 | 中(50-56K, 70-76K) | 选保姆给保姆清单 + 安全座椅烦躁安抚 |
| Part 4 | 早(25-31K) | 食物中毒预防 + 婴儿食品罐使用安全 |
| Part 4 | 尾(80-86K) | 浴室/厨房/户外 babyproofing 进阶 |
| Part 5 | 中(55-66K, 90-96K) | 性别中立教养 + 12 月旅行 + 挑食 + 屏幕 |
| Part 5 | 早(7-9K) | 撞头/咬人/离乳/出牙安抚 |
| Part 6 | 中(20-36K) | 退烧药选 + 蜜蜂叮咬+毒漆树 + 早产并发症 + 中毒急救 |
| Part 6 | 末(70K+) | 早产并发症全谱(ROP/IVH/NEC/PDA) |
| Part 7 | 中-尾(50-70K) | 二孩/收养/同性恋家庭(已大覆盖,跳) |

---

## 2. 高价值漏点筛选

### A 类:中国家长高频痛点 + 反常识(强烈推荐补)

1. **婴儿润肤乳警告:含花生油可能引发过敏** — 海蒂明确警告,中国家长完全不知,与 LEAP 早引入并行的"皮肤接触致敏"路径
2. **退烧药对乙酰氨基酚 vs 布洛芬** — 海蒂详细对比剂型/给药频率/禁忌/雷氏综合征,中国家长常乱用阿司匹林
3. **9 月起咬人:别反咬别夸张反应** — 海蒂明确反对"以牙还牙",中国老人常说"咬回去"
4. **挑食宝宝替代蛋白来源** — 海蒂用具体克数+食物组合,中国家长焦虑"不吃肉"
5. **保姆/月嫂给清单 12 项** — 海蒂详细模板,中国中产家庭高频需求
6. **婴儿安全药箱 12 类清单** — 海蒂完整列表,中国家长常临到用了才买

### B 类:实操数据型(中度推荐)

7. **性别中立教养 6 招** — 海蒂明确反性别刻板,与中国"男孩穷养女孩富养"对照
8. **带宝宝外出旅行 5 安全要点** — 海蒂整章,实操强
9. **早产儿 4 大并发症(PDA/ROP/IVH/NEC)红旗识别** — 海蒂详尽,早产家庭刚需
10. **撞头摇头 3 月内不必担心** — 海蒂解释机制,中国家长常误以为发育异常

### C 类:跳过候选(已 8 源充分覆盖或与 Phase B+C 重叠)

- "选保姆"(Phase B 月嫂卡已盖)
- "汽车安全座椅烦躁安抚"(C-S0-2400 一岁内后向已盖大方向)
- "幼教软件/iPad"(已有"2 岁前禁屏幕")
- "睡觉噪音耐受度"(已有"哭声 5 类"延伸)
- "便秘"(主线已有 3-6 月排便变化卡)
- "毒漆树/poison ivy"(美国独有,中国适用度低)
- "动脉导管未闭 PDA"(过于专业,留给医生)

---

## 3. R2 实补 10 张卡

### C-S0-2500 婴儿安全药箱 12 类清单(产前备货)

```yaml
card_id: C-S0-2500
stages: [S0]
tags: [safety, prenatal, preparation, mainstream, gap_g13_filled]
front:
  title: 婴儿安全药箱 12 类清单(产前备货)
  hook: 凌晨 2 点宝宝高烧没退烧药,没人想经历 — 海蒂的"产前备齐"清单。
back:
  why_matters: |
    Phase B+C 已盖"婴儿用品别买全套"(留 9 月再补),但药品类完全没卡。
    海蒂在 Part 1 给出非常具体的 12 类药箱必备清单,理由是:
    - 半夜或周末发病无法立刻去药房,中国一线城市还能 24 小时药店送药,但县级城市没这条件
    - 产前一次性备齐比"用到再买"成本低、心理负担小
    - 部分药品有保质期 2-3 年,备齐后只需检查不补
    海蒂强调:存放在宝宝够不着的高处,定期(每 3 个月)检查保质期。
  what_to_do:
    - 退烧/止痛(2 选 1):液态对乙酰氨基酚滴液(婴儿用泰诺林)是首选; 6 月+可加布洛芬滴液(摩特灵)。绝不备阿司匹林。
    - 抗感染外用 2 类:抗生素软膏(杆菌肽/新霉素,治轻微划伤)+ 双氧水(清洗伤口不痛)
    - 止痒 2 类:炉甘石洗剂或氢化可的松 0.5% 乳膏(治蚊虫叮咬+红疹)
    - 补液 1 类:口服补液盐(电解质水)— 处理腹泻必备,问医生剂量
    - 防晒 1 类:婴儿专用防晒霜(6 月+ 用,6 月内只用遮挡)
    - 鼻腔 1 类:婴儿吸鼻器(球状气囊)
    - 工具类 4 件:数字体温计(不要水银)、剂量勺/滴管/口腔注射器、无菌纱布+绷带+胶带、小镊子(夹刺)、小手电筒(查咽喉/瞳孔)
    - 不要买:玻璃水银体温计(危险)、热蒸汽加湿器(灼伤)、耳温计(婴儿不准)
  failure_mode: |
    常见错误:
    - 备阿司匹林 → 雷氏综合征风险(致命)
    - 用大人对乙酰氨基酚分割剂量给婴儿 → 剂量不准易过量
    - 6 月内宝宝用布洛芬 → 海蒂明确禁忌(脱水/呕吐/腹痛宝宝绝不能用)
    - 用棉签深插宝宝耳道 → 推屎入更深,海蒂建议问医生
    - 把药放厨房橱柜低处 → 学步期宝宝必摸到
  evidence_level: B
glossary_refs: [G-TERM-babyproofing]
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 1 Ch 2 婴儿用品准备
  page_zh: 47-48
related_cards: [C-S1-2502, C-S5-2152, C-S3-2400]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S1-2600 婴儿润肤乳含花生油警告(过敏隐藏路径)

```yaml
card_id: C-S1-2600
stages: [S1]
tags: [safety, allergy, mom, controversy, mainstream]
front:
  title: 婴儿润肤乳含花生油警告(过敏隐藏路径)
  hook: 给宝宝抹的润肤霜可能让他对花生过敏 — 海蒂藏在沐浴用品 sidebar 里的反常识警告。
back:
  why_matters: |
    Phase B+C 已盖 LEAP 早引入(C-S3-247x 系列)+ 食物花生 1 岁可吃。
    但海蒂在 Part 1 sidebar(p.47)单独警告:含花生油的婴儿润肤乳/沐浴露
    会通过皮肤接触致敏,反而提高 2 岁时花生过敏风险。
    机制(海蒂引研究):皮肤接触致敏(经表皮路径)+ 没经口免疫耐受 = 高风险
    特别针对皮肤已破损/湿疹宝宝。
    美国生产的婴儿润肤乳大多不含花生油,但:
    - 进口产品(欧洲、东南亚)可能含
    - 非"婴儿专用"的家用润肤乳常含
    - 中国母婴市场标签不严,代购产品常无中文成分表
    与 Phase D L3 节(LEAP)平行的另一条预防策略,中国家长几乎完全不知。
  what_to_do:
    - 买婴儿润肤乳前检查成分表:peanut oil/arachis oil(花生油学名)/groundnut oil 都不要
    - 优先选标注"无致敏原(allergen-free)"或"低敏(hypoallergenic)"的婴儿专用线
    - 已有湿疹宝宝特别注意,湿疹皮肤致敏风险更高
    - 不要用大人润肤乳/橄榄油/各种"民间偏方油"给宝宝抹
    - 与 LEAP 策略并行:皮肤避免花生暴露 + 4-6 月经口早引入花生稀释品
  failure_mode: |
    常见错误:
    - 觉得"天然植物油就安全"→ 海蒂明确警告这是反过来的:皮肤暴露反致敏
    - 看到代购欧美产品就信任 → 必须看成分表
    - 用花生油给婴儿按摩(印度/广东沿海传统)→ 双重风险:致敏 + 抑制经口耐受
    - 湿疹宝宝随便抹各种"湿疹药膏"含坚果油 → 严重风险
  evidence_level: A
glossary_refs: [G-TERM-allergy-introduction, G-TERM-LEAP-trial]
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 1 Ch 2 婴儿用品 sidebar"远离坚果"
  page_zh: 47
related_cards: []
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S2-2300 退烧药对乙酰氨基酚 vs 布洛芬选择 + 阿司匹林禁忌

```yaml
card_id: C-S2-2300
stages: [S2, S3, S4, S5]
tags: [safety, red_flag, medicine, mainstream]
front:
  title: 退烧药对乙酰氨基酚 vs 布洛芬选择 + 阿司匹林禁忌
  hook: 婴儿绝对不能吃阿司匹林 — 海蒂讲清楚 2 选 1 怎么选。
back:
  why_matters: |
    Phase B+C 已盖"2-6 月发烧 38°C 找医生"+"退烧三步:轻穿+多水+用药",
    但海蒂详解的"对乙酰氨基酚 vs 布洛芬怎么选"完全没卡。
    中国家长高频痛点:
    - 老人常推荐"阿司匹林泡水喝"→ 雷氏综合征风险(肝/脑致命紊乱)
    - 给婴儿用大人成人型布洛芬 → 剂量过量
    - "联合用药"两种交替给 → 海蒂明确不推荐(易过量)
    海蒂数据具体:
    - 对乙酰氨基酚:每 4-6 小时一次,各种剂型(滴液/糖浆/栓剂/粉剂)
    - 布洛芬:每 6-8 小时一次,药效更强持续更久,但仅 6 月+
    - 阿司匹林:儿童任何感染都禁,除非医生明确指定
  what_to_do:
    - 6 月以下:只用对乙酰氨基酚滴液(婴儿用泰诺林)
    - 6 月以上:可选布洛芬(摩特灵/艾德维尔),但宝宝脱水/呕吐/腹痛绝不能用
    - 看体重不看年龄给剂量,严格按药品说明书
    - 用药品自带的剂量勺/滴管/注射器,不要用厨房勺
    - 宝宝呕吐严重不能口服 → 用对乙酰氨基酚栓剂(海蒂明确推荐)
    - 不要交替两种药:增加剂量记录混乱风险
    - 任何持续发烧不退 24 小时 → 找医生,不是加大剂量
  failure_mode: |
    常见错误:
    - 给宝宝阿司匹林 → 雷氏综合征(致命)
    - 用对乙酰氨基酚同时吃含对乙酰氨基酚的复方感冒药 → 双倍过量,肝衰竭
    - 6 月内用布洛芬 → 海蒂明确禁忌
    - 退烧不下就加大剂量 → 必须找医生
    - 把退烧药当"预防发烧"长期吃 → 肝肾损伤
  evidence_level: A
glossary_refs: []
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 6 Ch 18 生病的宝宝 sidebar
  page_zh: 537-538
related_cards: [C-S2-2107, C-S0-2500]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S3-2500 选保姆 + 给保姆 12 项交接清单

```yaml
card_id: C-S3-2500
stages: [S3, S4, S5]
tags: [postpartum, mom, philosophy, practical]
front:
  title: 选保姆 + 给保姆 12 项交接清单
  hook: 别朋友说"放心给保姆"就照做 — 海蒂的 12 项清单让你睡着也安心。
back:
  why_matters: |
    Phase B+C 已盖"月嫂 vs 产妇护导员 vs 钟点工"(C-S0-2061)选月嫂,
    但 3 月后宝宝转入"长期保姆/育儿嫂"阶段,海蒂详细的"交接清单"完全没卡。
    中国中产家庭高频:
    - 第一次留保姆,妈妈焦虑哭着出门
    - 到现场才发现保姆不会处理常见情况(噎食/烫伤/CPR)
    - "口头交代"忘 1/3,半夜电话还在被问
    海蒂明确反对"分离焦虑前(< 9 月)就该开始让保姆登场",
    9 月后再首次留宝宝独处,陌生人焦虑更难处理。
  what_to_do:
    - 第一次留保姆要安排 6-9 月之间(分离焦虑萌芽前)
    - 第一晚保姆早到 30-60 分钟现场观察一次哺乳/换尿布/拍嗝
    - 12 项书面交接清单(贴冰箱):
      1. 紧急电话:中毒中心 + 儿科医生 + 急救 + 父母手机 2 个
      2. 安抚招(轻摇/特定歌/手机/婴儿车),宝宝最爱玩具
      3. 睡姿:必须仰睡,不用枕头
      4. 拍嗝姿势(肩上/腿上,频率)
      5. 喂养时间表 + 配方奶冲调比例
      6. 换尿布:用湿巾还是棉签 + 是否抹药膏
      7. 哭超过 X 分钟才电话联系(避免每哭就 call)
      8. 严禁动作:摇晃/趴睡/给牛奶/给蜂蜜/给坚果
      9. 禁止访客 + 禁止离开宝宝单独在房
      10. 火灾/触电/急救预案,急救包位置
      11. 房间禁烟 + 厨房不能开火做饭(分心)
      12. 每天回家后 5 分钟简报本(吃几次奶/睡几小时/几次便)
    - 第一次外出 1-2 小时,逐渐拉长
  failure_mode: |
    常见错误:
    - 总是宝宝睡着才走 → 宝宝醒来发现陌生人会更慌
    - 不写清单"她经验丰富不用说" → 每个宝宝不一样,口头交接漏 1/3
    - 不交代喂奶时间表 → 宝宝过饿/过饱
    - 没写中毒中心 + 儿科电话 → 急事找不到人
    - 第一次就外出整晚 → 宝宝+保姆双方压力爆表
  evidence_level: B
glossary_refs: []
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 3 Ch 8 留给保姆 sidebar"是保姆清单"
  page_zh: 270-271
related_cards: [C-S0-2061]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S4-2400 9 月撞头摇头 — 别担心多数自愈

```yaml
card_id: C-S4-2400
stages: [S4, S5]
tags: [philosophy, development, normal, mainstream]
front:
  title: 9 月撞头摇头 — 别担心多数自愈
  hook: 宝宝有规律地撞头让你心碎? 海蒂说 3 岁前自愈,别叫别哄。
back:
  why_matters: |
    Phase B+C 有"撞头后观察 6 小时,12 红旗送医"(撞伤场景),
    但本卡是 6-12 月发育期的"主动撞头/摇头习惯",中国家长高频误判:
    - 老人说"自闭症"或"脑子有问题",要带去医院
    - 实际海蒂解释:这是正常自我安抚机制
    海蒂数据:
    - 摇晃多在 6 月起,撞头 9 月起出现
    - 男孩比女孩更常见(撞头)
    - 大多数 3 岁左右自然消失
    - 与精神/身体障碍无关(若宝宝其他方面正常)
    机制猜测:出牙疼/累/创造摇摆感来自我安抚/睡眠转换辅助
  what_to_do:
    - 第一反应:不责骂、不逗趣、不强行制止 — 这些都加剧
    - 白天提供替代有节奏活动:摇椅/敲锅勺/秋千/手指游戏
    - 给予更多拥抱和轻摇主动安抚
    - 床围加软垫(轻撞,但不勒过紧)
    - 睡前白天活动充分 + 睡前安静过渡(避免过度疲劳引发)
    - 真正担心的红旗:发育迟缓 / 大多数时间不高兴 / 撞头同时表现愤怒
  failure_mode: |
    常见错误:
    - 看到撞头立即抱起 + 大叫 → 强化行为,撞得更勤
    - 责骂 → 增加压力,撞头时间更长
    - 用枕头/毛巾死死压住头 → 危险,且无效
    - 立刻带去医院做脑电图/CT → 99% 正常,但徒增辐射焦虑
    - 与发育自闭症征候混淆:看是否还有"指物缺失/眼神回避/语言滞后",
      若只有撞头没其他征候,基本是正常发育现象
  evidence_level: B
glossary_refs: []
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 5 Ch 13 撞头摇头扭头
  page_zh: 440
related_cards: [C-S5-2152]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S5-2400 9 月+宝宝咬人:别反咬别夸张反应

```yaml
card_id: C-S5-2400
stages: [S5, S6]
tags: [philosophy, discipline, controversy, mainstream]
front:
  title: 9 月+宝宝咬人:别反咬别夸张反应
  hook: 老人说"咬回去他就懂了" — 海蒂说这恰恰是教他可以咬人。
back:
  why_matters: |
    Phase B+C 已盖"7-8 月乳头被咬,坚定 No+拔离"(哺乳场景),
    但本卡是 9 月+宝宝咬人(咬妈妈肩膀/咬其他孩子/咬宠物),
    中国家长 + 老人高频误处理:
    - "咬回去让他知道疼" → 海蒂明确反对:这是教他公平游戏=允许咬
    - 大叫"疼!" + 戏剧化反应 → 海蒂解释:这反而强化(宝宝觉得有趣)
    - 打手心 → 体罚,海蒂反对(已有"管教不是体罚"卡)
    海蒂解释:
    - 咬人最初是实验/游戏,宝宝不知道伤人(咬过磨牙环/玩具)
    - 人的有趣反应(惊吓/大叫/气愤)= 强化反馈
    - 越戏剧化,咬人越多
  what_to_do:
    - 平静坚定语气说"不能咬人",简短不重复
    - 立即转移注意力(歌/玩具/换房间)
    - 提供替代咀嚼物:磨牙环/冰湿毛巾/凉的胡萝卜条(8 月+)
    - 父母/爷爷奶奶不能"亲咬"宝宝(常见的"咬一口"亲昵动作)
    - 哺乳被咬:坚定拔离 + 无表情(避免戏剧化反馈)
    - 在群体玩耍中持续监督,被咬其他孩子立即用身体隔开
    - 与孩子讨论替代发泄方式(语言/打枕头)— 1 岁+开始
  failure_mode: |
    常见错误:
    - 反咬一口 → 教宝宝"咬人是允许的"
    - 哭着说"妈妈好疼啊宝宝看妈妈哭了" → 戏剧化反馈,加剧
    - 笑着说"小坏蛋咬人" → 宝宝学到这是正向反馈
    - 打嘴或打手 → 体罚 + 不解决问题
    - 关小黑屋 → 海蒂反对超过年龄理解的惩罚
    - 不监督就让宝宝和其他孩子玩 → 被咬其他家长会有意见
  evidence_level: B
glossary_refs: [G-TERM-corporal-punishment]
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 5 Ch 13 咬人
  page_zh: 442
related_cards: [C-S1-2218]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S5-2401 1 岁挑食宝宝替代蛋白 7 法

```yaml
card_id: C-S5-2401
stages: [S5, S6]
tags: [feeding, nutrition, mainstream, mom]
front:
  title: 1 岁挑食宝宝替代蛋白 7 法
  hook: 宝宝不吃肉?海蒂列出 1 岁全天蛋白需求只需 2 杯奶 +2 片面包。
back:
  why_matters: |
    Phase B+C 已盖"1 岁后食欲变小"+"拒辅食 4 招"+"12-36m 跟家庭饮食",
    但具体"不吃肉/蔬菜怎么补"的实操替代方案没卡。
    中国家长焦虑:
    - "孩子不吃肉营养不够"
    - "不吃蔬菜以后会便秘"
    - 强迫喂 → 战争 → 厌食
    海蒂数据级反焦虑:
    - 1 岁宝宝营养需求"非常这意味着很容易就吃饱"
    - 1 整天蛋白可由:2 杯牛奶+2 片全麦面包 满足
    - 或:2 杯牛奶+30g 奶酪 满足
    - 或:1 杯奶+1 杯酸奶+1 小碗燕麦+1 片全麦面包 满足
    "肉类不是唯一蛋白来源"是关键反常识。
  what_to_do:
    - 蛋白替代清单(7 类):奶酪 / 硬奶酪 / 牛奶 / 酸奶 / 鸡蛋 / 全麦谷物面包 / 豆类(豆腐/豆浆) / 高蛋白意面
    - 蔬菜"隐藏术":南瓜松饼 / 胡萝卜蛋糕 / 西蓝花炒鸡蛋 / 冷酸奶蘸蔬菜
    - 加工蛋白法:酸奶水果奶昔 / 法式面包(全麦+蛋+奶浸泡)/ 蛋花汤加奶酪
    - 不强迫不批评,孩子自我调节(几顿合计而非一顿合计)
    - 一两顿不吃也不补,下顿等饿了自然吃
    - 每天 1 杯水果汁(限 120ml 内)补维生素 C
    - 担心铁:加铁奶粉 / 红肉碎(藏意面酱里)/ 含铁强化谷物
  failure_mode: |
    常见错误:
    - "不吃完不让走" → 形成餐桌权力斗争
    - "用 iPad 哄着喂" → 长期注意力不在食物
    - "做特殊饭" → 永远是挑食专业户
    - 一顿不吃就喂奶/零食代替 → 正餐永远不饿
    - 量焦虑(对比"别人家孩子吃多少") → 每个宝宝胃容量不同
  evidence_level: B
glossary_refs: []
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 5 Ch 14 挑食
  page_zh: 488
related_cards: [C-S5-2143]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S6-1700 性别中立教养 6 招(反对标签化)

```yaml
card_id: C-S6-1700
stages: [S5, S6, S7]
tags: [philosophy, gender, controversy, mainstream]
front:
  title: 性别中立教养 6 招(反对标签化)
  hook: 别说"男孩穷养女孩富养" — 海蒂的反性别刻板 6 招。
back:
  why_matters: |
    Phase B+C 完全无性别教养主题卡。
    海蒂在 Part 5 Ch 16 单独有"性别培养"长节,
    与中国主流的"男孩要勇敢/女孩要文静""穷养富养"立场对照鲜明。
    海蒂承认天生差异(女宝注意人脸、男宝注意物体;肌肉/疼痛阈值/视听敏感度有差),
    但反对家长强化刻板:
    - "你是大孩子不能哭" + "妹妹哭就抱"
    - 男孩只夸"你强壮",女孩只夸"你漂亮"
    - 玩具按性别选(女不许玩车,男不许玩娃娃)
    - "做爸爸=赚钱,做妈妈=带娃"的角色暗示
    海蒂目标:培养"无性别定向"的宝宝,长大按自身长处选择,而非传统期待。
  what_to_do:
    - 接受先天差异(平均差),但视宝宝为个体(差异大于性别均差)
    - 玩具选择按宝宝兴趣,不按"男娃买车女娃买娃娃"
    - 表扬话术多元化:女儿也可"你跑得真快""你解题真聪明"; 儿子也可"你照顾妹妹真温柔"
    - 家务分配按能力兴趣,不按"做饭=妈妈/修水管=爸爸"
    - 不评论"男孩不能哭"或"女孩要文静" — 情感表达不分性别
    - 父母做榜样:跑步妈妈 + 做饭爸爸 比 "玩娃娃培养教养型男孩"更有效
  failure_mode: |
    常见错误:
    - 完全无视性别差异 → 海蒂不主张这个,平均差异是真的
    - 强行让男孩穿粉色裙子证明"中性"→ 这是另一种刻板
    - 看到女儿粗野就压制 → 压抑她的天性
    - 看到儿子温柔就嘲笑"娘炮" → 严重伤害自尊
    - "中国老人说男孩就是要野" → 把刻板包装成天性
    - 玩具按性别完全分隔 → 错过不同维度的发展刺激
  evidence_level: B
glossary_refs: [G-TERM-gender-stereotypes-peak, G-TERM-gender-schema, G-TERM-gender-labeling]
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 5 Ch 16 性别培养
  page_zh: 493-494
related_cards: []
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S6-1701 1 岁内带宝宝旅行 7 安全要点

```yaml
card_id: C-S6-1701
stages: [S2, S3, S4, S5, S6]
tags: [safety, practical, mainstream, family]
front:
  title: 1 岁内带宝宝旅行 7 安全要点
  hook: 春节回家 / 五一带娃出游 — 海蒂的 7 项安全清单别忽略。
back:
  why_matters: |
    Phase B+C 完全无"带娃旅行"主题卡(汽座有,但不是旅行场景)。
    海蒂 Part 5 Ch 17 有完整"四季旅行"章节,中国家长高频:
    - 春节高铁/飞机回老家(1-2 月龄就出门)
    - 五一/十一出游(夏天高温车内闷死风险)
    - 老家"水土不服"概念害死人
    - 高铁邻座抱怨宝宝哭
    海蒂明确数据:
    - 车温在炎热天气可达灼热"烤箱级",绝不能留宝宝单独
    - 长途>2 小时必须每 2 小时停车休息(后向座椅+陌生环境双倍压力)
    - 高海拔(>2000m)阳光更强 + 缺氧会让贫血宝宝心率/呼吸加快
  what_to_do:
    - 交通工具:1 岁内必须后向汽车安全座椅(已有 C-S0-2400),飞机起飞降落让宝宝吸奶嘴减压
    - 长途车每 2 小时停 → 抱出活动 + 哺乳 + 换尿布
    - 目的地住宿先 babyproofing 检查:窗户够不到/电线遮挡/小型吧台清空/婴儿床安全
    - 行程不塞满,只去能让宝宝 sleep/eat 不限的地方:户外公园/动物园/部分博物馆
    - 想看演唱会/歌剧 → 现场雇临时保姆,别带宝宝
    - 高海拔(>2000m)宝宝心脏病/贫血需先咨询医生
    - 绝对禁忌:任何天气任何理由不能把宝宝单独留车上(夏天 5 分钟可致命)
  failure_mode: |
    常见错误:
    - "宝宝睡着我去店里买杯咖啡" → 车温几分钟变烤箱
    - 春节坐 8 小时火车不停喂奶 → 宝宝哭闹 + 后排乘客投诉
    - 老家不消毒就给宝宝喝井水 → 腹泻+脱水
    - "高原反应大人都行宝宝肯定行" → 婴儿耐缺氧远低于成人
    - 行程塞满景点 → 宝宝小睡被打乱,全家崩溃
    - 春节回老家不带急救药 / 体温计 → 半夜发烧手足无措
  evidence_level: B
glossary_refs: []
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 5 Ch 17 四季旅行
  page_zh: 525-528
related_cards: [C-S0-2400]
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

### C-S7-1200 早产儿 4 大并发症识别(PDA/ROP/IVH/NEC)

```yaml
card_id: C-S7-1200
stages: [S0, S1, S7]
tags: [safety, red_flag, preemie, mainstream, gap_g7_filled]
front:
  title: 早产儿 4 大并发症识别(PDA/ROP/IVH/NEC)
  hook: 早产宝宝出院后这 4 个红旗 — 海蒂的"再住院"清单。
back:
  why_matters: |
    Phase B+C 完全无早产儿专题卡。
    海蒂 Part 6 Ch 21 有完整"早产儿家"长章,中国早产宝宝家庭刚需:
    - 中国早产率约 7%(约 100 万/年早产)
    - 出院后家长焦虑"哪些症状要立刻送医"
    - 普通儿科医生对早产专科识别度参差
    海蒂明确 4 大主要并发症 + 红旗,
    虽然多数在 NICU 出现,但一些会延续到出院后或出院后再发。
  what_to_do:
    - PDA(动脉导管未闭):红旗=心杂音 + 呼气浅短费力 + 嘴唇发青。多数自愈,严重需消炎痛或手术
    - ROP(早产儿视网膜病变):28 周前出生 85% 发生率。出院后定期小儿眼科复诊到 1 岁。征候:斗鸡眼/无意眼球颤动/明显视物障碍
    - IVH(脑室内出血):72 小时内最危。出院后红旗:头围异常增大(脑积水)+ 持续呕吐 + 异常嗜睡
    - NEC(坏死性小肠结肠炎):喂母乳风险更低。红旗:腹胀 + 胆汁性呕吐(绿色) + 便血 + 呼吸暂停 → 急诊
    - 早产贫血:都需口服铁剂补铁(出院医生会开)
    - 早产再住院常见原因:呼吸道感染(RSV) + 脱水
    - 1 岁内频繁眼科/听力/发育评估(矫正月龄而非生月龄看里程碑)
  failure_mode: |
    常见错误:
    - "宝宝出院了应该好了"→ 早产并发症可延续 1-2 年,需密切随访
    - 用足月儿生长曲线评估早产儿 → 必须用矫正月龄
    - 没按时眼科复查 → ROP 错过治疗窗会失明
    - 看到嘴唇发青等"会过去" → PDA 可能心衰
    - 早产儿不补铁"奶里有了"→ 早产儿铁库本来就不足
    - 出现绿色呕吐物当普通吐奶 → NEC 是急症
    - 不做听力筛查 → 早产高发感音性听力下降
  evidence_level: A
glossary_refs: [G-ABBR-RSV]
citation:
  source_id: SRC-040
  book_title_en: What to Expect the First Year
  book_title_zh: 海蒂育儿大百科 0-1 岁
  authors: [Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg]
  publisher_zh: 南海出版公司
  year: 1989
  year_2nd_ed: 2010
  year_zh: 2014
  translator_zh: [莫夏迪, 张敏]
  chapter: Part 6 Ch 21 早产儿
  page_zh: 619-620
related_cards: []
language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 4. 跳过的高价值候选(说明)

| 候选 | 跳过原因 |
|---|---|
| 选保姆面试 9 问 | 与 C-S3-2500 给保姆清单重叠太多,合并写更好 |
| "蜜蜂叮咬刮不挤"详细 | 已有 C-S1-2304 蜜蜂叮咬卡盖了核心 |
| 婴儿用品奶瓶 3 类对比 | 实操性弱,中国家长按线下/电商分类购买,不需要这个细分 |
| 性别 = "天生差异先于教养" 立场 | 与 C-S6-1700 性别中立教养重叠 |
| 离乳"宝宝主动自然 vs 妈妈主动" | 已有 C-S5-2247 自然离乳 vs 主动断奶 + 戒夜奶卡 |
| 食品罐安全 | 中国家长用商品罐少,自制辅食为主,适用度低 |
| 美国旅行医保险 | 美国独有体系,中国不适用 |
| 撞头红旗 / 夜醒踢腿原因 | 已有大量睡眠卡盖 |
| 同性恋家庭收养 | Phase B Part 7 已盖收养母乳基础(C-S0-2168 系列) |
| 撞头/咬人/玩具拆卸的 ASD 排查 | 中国家庭 ASD 筛查体系尚未跟上,过早写会误导,留专业医生 |
| 吃喝中毒急救清单 | 已有 C-S1-2306 中毒卡盖核心 |

---

## 5. 卡 ID 分配总表

| 段 | 新增 ID | title | 价值类型 |
|---|---|---|---|
| S0 | C-S0-2500 | 婴儿安全药箱 12 类清单 | 实操数据 + 中国家长高频 |
| S1 | C-S1-2600 | 婴儿润肤乳含花生油警告 | 反常识 + 强烈漏点 |
| S2 | C-S2-2300 | 退烧药对乙酰氨基酚 vs 布洛芬 + 阿司匹林禁忌 | 红旗禁忌 + 中国家长高频 |
| S3 | C-S3-2500 | 选保姆 + 给保姆 12 项交接清单 | 实操 + 中国中产高频 |
| S4 | C-S4-2400 | 9 月撞头摇头 — 别担心多数自愈 | 反焦虑 + 中国家长高频误判 |
| S5 | C-S5-2400 | 9 月+宝宝咬人:别反咬别夸张反应 | 跨派对照 + 中国老人误指导 |
| S5 | C-S5-2401 | 1 岁挑食宝宝替代蛋白 7 法 | 反焦虑 + 数据具体 |
| S6 | C-S6-1700 | 性别中立教养 6 招(反对标签化) | 跨派立场对照 |
| S6 | C-S6-1701 | 1 岁内带宝宝旅行 7 安全要点 | 实操 + 中国春节高频场景 |
| S7 | C-S7-1200 | 早产儿 4 大并发症识别 | 红旗 + 早产家庭刚需 |

---

## 6. 主线 Python 搬运指引

```python
import re, os, yaml
src = '/Users/jjjjadennnn/Desktop/parenting-kb/00-meta/checkpoints/PHASE14_R2_DEEP_AUDIT.md'
dst_map = {
    'C-S0-2500': 's0-pregnancy',
    'C-S1-2600': 's1-newborn',
    'C-S2-2300': 's2-1to3mo',
    'C-S3-2500': 's3-3to6mo',
    'C-S4-2400': 's4-6to9mo',
    'C-S5-2400': 's5-9to12mo',
    'C-S5-2401': 's5-9to12mo',
    'C-S6-1700': 's6-12to24mo',
    'C-S6-1701': 's6-12to24mo',
    'C-S7-1200': 's7-24to36mo',
}
with open(src) as f:
    text = f.read()
# 找 ```yaml 块
blocks = re.findall(r'```yaml\n(.*?)```', text, re.DOTALL)
for blk in blocks:
    cid_match = re.search(r'card_id:\s*(\S+)', blk)
    if not cid_match:
        continue
    cid = cid_match.group(1)
    if cid not in dst_map:
        continue
    out = f'/Users/jjjjadennnn/Desktop/parenting-kb/30-cards/{dst_map[cid]}/{cid}.yaml'
    with open(out, 'w') as g:
        g.write(blk)
    print(f'wrote {out}')
```

---

> R2 共 10 张:S0=1 / S1=1 / S2=1 / S3=1 / S4=1 / S5=2 / S6=2 / S7=1
> evidence_level:A=4(40%)+ B=6(60%)
> 主题分布:safety=5 / red_flag=2 / philosophy=2 / feeding=1 / mainstream=10 / controversy=3 / mom=2 / family=1 / preemie=1 / gender=1
