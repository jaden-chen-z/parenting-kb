# Phase 14 SRC-040 海蒂 Part 1 提取员产出 (2026-05-04)

> **关键阻塞**:本 subagent 的 Write 沙盒只允许 `00-meta/checkpoints/`,无法直接写入 `30-cards/s0-pregnancy/` 与 `30-cards/s1-newborn/`。
> 主线请用本文件中的完整 YAML 全量落盘到对应路径(每张卡一个文件,文件名 = card_id)。
> 卡片 YAML 已按 v3.5 schema + PHASE2 §2.7 前情提要 + 字数无上限规则编写。

---

## 决策摘要(返回给主线的 JSON)

```json
{
  "part": 1,
  "cards_count": 17,
  "cards": [
    {"id":"C-S0-2053","title":"包皮环切术:利弊都不重,自己拍","stage":"S0","level":"A","tags":["controversy","safety"]},
    {"id":"C-S0-2054","title":"产前面谈选儿科医生 7 问清单","stage":"S0","level":"B","tags":[]},
    {"id":"C-S0-2055","title":"独立 vs 合伙 vs 团体诊所","stage":"S0","level":"C","tags":[]},
    {"id":"C-S0-2056","title":"母乳还是配方:权衡而非道德题","stage":"S0","level":"B","tags":["philosophy"]},
    {"id":"C-S0-2057","title":"真正不能母乳的 7 种情况","stage":"S0","level":"A","tags":["safety","red_flag"]},
    {"id":"C-S0-2058","title":"收养妈妈也能母乳喂养","stage":"S0","level":"B","tags":[]},
    {"id":"C-S0-2059","title":"婴儿用品别买全套,留 9 月再补","stage":"S0","level":"C","tags":[]},
    {"id":"C-S0-2060","title":"婴儿衣服直接买大码","stage":"S0","level":"C","tags":[]},
    {"id":"C-S0-2061","title":"月嫂 vs 产妇护导员 vs 钟点工","stage":"S0","level":"C","tags":[]},
    {"id":"C-S0-2062","title":"祖父母首次到访先约边界","stage":"S0","level":"C","tags":["philosophy","controversy"]},
    {"id":"C-S0-2063","title":"乳房产前不需任何'锻炼'","stage":"S0","level":"A","tags":["safety"]},
    {"id":"C-S0-2064","title":"乳头内陷孕期就评估","stage":"S0","level":"B","tags":[]},
    {"id":"C-S0-2065","title":"纸尿裤 vs 棉布尿布:没赢家","stage":"S0","level":"B","tags":[]},
    {"id":"C-S0-2066","title":"宠物迎新生儿:孕期就训练","stage":"S0","level":"B","tags":["safety","red_flag"]},
    {"id":"C-S1-2102","title":"母乳的妈妈端 7 大好处","stage":"S1","level":"A","tags":[]},
    {"id":"C-S1-2103","title":"母乳频喂 vs 配方久饱:正常","stage":"S1","level":"B","tags":[]},
    {"id":"C-S1-2104","title":"决定不喂母乳:别内疚","stage":"S1","level":"C","tags":["philosophy"]}
  ],
  "gaps_filled": [],
  "cross_links_made": [
    "C-S0-2054 ↔ C-S0-007 (Brazelton 选医生哲学)",
    "C-S0-2056 ↔ C-S1-1003 (BFHI 第 6 步)",
    "C-S0-2057 ↔ C-S1-1013 (HIV+AFASS)",
    "C-S0-2057 ↔ C-S0-005 (孕期用药)",
    "C-S0-2059 ↔ C-S0-009 (待产物品采购)",
    "C-S0-2062 ↔ C-S0-003 (祖父母参与)",
    "C-S0-2065 ↔ C-S1-006 (尿布/换尿布)",
    "C-S1-2102 ↔ C-S1-050 (AAP 母乳起步)",
    "C-S1-2103 ↔ C-S1-050 (AAP 频喂立场)"
  ],
  "new_glossary_cards": [],
  "skipped_topics": [
    "母乳预防 SIDS — 已 SRC-004 充分覆盖",
    "母乳的宝宝端好处(免疫/智商/牙齿) — 已 SRC-006/SRC-031 充分覆盖",
    "戒烟保护宝宝 — 已 C-S0-006/C-S0-367/C-S0-518 覆盖",
    "起名字原则 — 文化偏向太强,无证据增量",
    "母乳建立期奶嘴慎用 — 已 C-S1-1006 覆盖",
    "返工继续母乳 — 已 C-S1-095/C-S1-1012 覆盖",
    "选医生'医疗之家'哲学 — 已 C-S0-007 覆盖,本次只补'产前面谈清单'操作面"
  ],
  "decisions_log": "1) 海蒂 Ch1 角色转变/事业回归/丧失信心 → C 级编辑观点,无证据增量,跳过。 2) 海蒂母乳 11 大好处中,免疫/SIDS/智商已被 AAP/Karp/WHO 反复覆盖,只取'妈妈端 7 大好处'(子宫复旧/避孕/乳腺癌)做整合卡。 3) 包皮环切术是 P0 缺口,必填,标 A 级因引用 AAP 1999 立场。 4) 选医生分两张:C-S0-007 是哲学,本次 C-S0-2054 是产前面谈操作清单(互补不重)。 5) 月嫂决策表是中国家长高频痛点,海蒂虽美国背景但分类框架可借鉴,标 C 级。"
}
```

---

## 卡片 1 / C-S0-2053 · 包皮环切术决策

```yaml
card_id: C-S0-2053
stages: [S0]
tags: [controversy, safety]

front:
  title: 包皮环切术:利弊都不重,自己拍
  hook: AAP 不推也不反

back:
  why_matters: |
    包皮环切术(circumcision)= 切掉阴茎包皮的小手术,一般出生后 24 小时做。
    美国 1980 年代 80% 男婴做,现在降到 50% 出头。AAP 1999 年立场:有医学好处但不强到要列为常规。
    好处:略降尿道感染、阴茎癌、艾滋病传染风险(绝对值都很低)。
    坏处:出血/感染极少但有;做了不可逆。
    海蒂的判断:利弊分量都不重,父母按宗教/审美/文化/现实自己定即可,没"对错"答案。
  what_to_do:
    - 决定权在你和配偶,不必听亲戚施压
    - 做的话:产后 20-24 小时后做,不在产房
    - 做的话必须用局部麻醉(AAP 推荐,别裸做)
    - 不做的话:2 岁后教孩子翻洗包皮即可
    - 别让没经验的医生 / 宗教执行人操作
  failure_mode: |
    把它当"必做"或"必拒"都是误解 — AAP 中立意味着没标准答案。
    新生儿不打麻醉硬做 → 有证据显示宝宝心率/血压/皮质醇升高,孩子真的疼。
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
  location: "第 1 章 临产前的准备 · 包皮环切术"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 2 / C-S0-2054 · 产前面谈选儿科医生 7 问清单

```yaml
card_id: C-S0-2054
stages: [S0]
tags: []

front:
  title: 产前面谈选儿科医生 7 问清单
  hook: 怀孕 7-8 月预约见面

back:
  why_matters: |
    产前面谈(prenatal interview)= 怀孕 7-8 月时主动约目标儿科医生面谈一次,免费或低费,看理念合不合再签。
    海蒂强调:别等宝宝出生才挑医生 — 早产或急诊时你就没空慢慢面试了。
    Brazelton 也说"医患关系是治疗关系"(见 C-S0-007),早建立才有信任。
    7 个高优先级议题:母乳支持、提前出院、包皮环切、素食、预防医学、抗生素使用、辅助疗法。
  what_to_do:
    - 怀孕 7-8 月预约 1-2 个候选医生面谈
    - 必问:'对母乳支持到什么程度?'
    - 必问:'需要时能开抗生素到什么阈值?'
    - 看候诊室氛围:玩具新不新 / 前台耐不耐心
    - 问急诊处理流程:打电话 vs 直接去医院
    - 选合伙诊所要确认能否固定看一个人
  failure_mode: |
    出生后才挑医生 → 急诊时只能找替班 / 病历没建。
    只看证书不看理念 → 母乳期发现医生劝你转配方就晚了。
  evidence_level: B

glossary_refs:
  - G-PERSON-Brazelton

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
  location: "第 1 章 临产前的准备 · 选择合适的医生 · 产前面谈"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-007    # Brazelton 医患关系哲学(本卡是其操作清单)
  - C-S0-001    # Brazelton 早建立信任

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 3 / C-S0-2055 · 独立 vs 合伙 vs 团体诊所

```yaml
card_id: C-S0-2055
stages: [S0]
tags: []

front:
  title: 独立 vs 合伙 vs 团体诊所
  hook: 一对一 vs 24 小时随叫

back:
  why_matters: |
    儿科诊所有 3 种行医方式:独立医生(1 人)、合伙(2 人)、团体(3+ 人)。
    海蒂的判断:没有最好的,只有最适合的 — 一对一关系强但休假找替班;团体 24 小时随叫但每次见不同人。
    中国家长容易陷入"一定要找最有名的"误区,忽视了"能否每次见同一人"和"能否半夜联系上"是更日常的指标。
  what_to_do:
    - 想要紧密一对一关系 → 选独立医生
    - 怕医生休假没人接班 → 选合伙(2 人)
    - 想 24 小时随叫 → 选团体(3-5 人)
    - 选合伙/团体必问:'每次能预约同一医生吗?'
    - 团体诊所:接受'半数时间见副手'再签
  failure_mode: |
    选了团体诊所却以为'每次都能见到主治医生' → 副手/护士接诊时焦虑。
    选了独立医生却没问'休假谁接班'→ 关键时刻找不到人。
  evidence_level: C

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
  location: "第 1 章 临产前的准备 · 哪种行医方式最完美"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-2054

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 4 / C-S0-2056 · 母乳还是配方:权衡而非道德题

```yaml
card_id: C-S0-2056
stages: [S0]
tags: [philosophy]

front:
  title: 母乳还是配方:权衡而非道德题
  hook: 1 个月也比没喂强

back:
  why_matters: |
    母乳 vs 配方决定不止"科学"还有"感觉"。海蒂的中庸立场:不应让"母乳最好"压力等同"非母乳就失败"。
    多数权威(WHO/AAP)默认推母乳是因群体收益,但单家庭决策还要看妈妈状态、工作、心理。
    海蒂建议:即使最初想配方也试 6 周再决定;即使最初想纯母乳也别用全人格压自己。
    几周母乳 ≠ 没喂,初乳期 + 1 月母乳就有显著免疫好处 — 别因为做不到 6 月而 0 月。
  what_to_do:
    - 不确定 → 先试母乳 1 个月,有底再换
    - 想配方 → 至少试 6 周确认自己感受
    - 短期母乳也算数:1 周初乳即有价值
    - 别让其他人的选择决定你的
    - 决定后不回头,别在两种间反复纠结
  failure_mode: |
    把'母乳=好妈妈'内化 → 奶不够时崩溃自责,影响产后心理。
    把'配方=放弃'对立 → 错过试一试的机会。
    最危险:在两种间反复犹豫,反而两种都做不好。
  evidence_level: B

glossary_refs:
  - G-TERM-mixed-feeding

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
  location: "第 1 章 给宝宝喂奶 · 做出决定"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-1003   # BFHI 默认不给配方
  - C-S1-1006   # 母乳建立期慎用奶瓶
  - C-S1-050    # AAP 母乳起步

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 5 / C-S0-2057 · 真正不能母乳的 7 种情况

```yaml
card_id: C-S0-2057
stages: [S0]
tags: [safety, red_flag]

front:
  title: 真正不能母乳的 7 种情况
  hook: 其余都能母乳

back:
  why_matters: |
    母乳禁忌(contraindications to breastfeeding)= 母乳真正会伤宝宝的少数医学情况。
    中国家长常被错误"建议"停母乳:感冒、轻微吃药、剖腹产 — 这些都不是禁忌。
    真禁忌很少:母亲严重传染病(未控 TB、未治 HIV、化疗放疗期)、宝宝先天代谢病(PKU、半乳糖血症)。
    青霉素、产后抗生素、乳腺炎期间可以继续喂(WHO 与 AAP 一致)。
    多数药物哺乳期可调整剂型 — 用药前必问医生"哺乳期方案"。
  what_to_do:
    - 妈妈端禁忌:未治 HIV / 未控 TB / 化疗 / 锂剂 / 抗甲状腺
    - 妈妈滥用药/酒精 → 不能母乳(可恢复后再开始)
    - 宝宝端禁忌:PKU(配特殊配方)/ 半乳糖血症
    - 普通感冒 / 流感 → 继续喂(抗体反而保护宝宝)
    - 用任何新药前先问医生"哺乳兼容性"
  failure_mode: |
    把'妈妈感冒了得停母乳'当真 → 抗体走不进宝宝,反而失去保护。
    一概'吃任何药就停' → 错过母乳期,且很多药其实兼容。
    HIV+ 时代变了:见 C-S1-1013 AFASS 评估,不再一刀切。
  evidence_level: A

glossary_refs:
  - G-TERM-acceptable-medical-reasons

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
  location: "第 1 章 给宝宝喂奶 · 如果你无法母乳喂养"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-1013   # WHO HIV AFASS 修订
  - C-S1-1003   # BFHI 第 6 步医学指征
  - C-S0-005    # 孕期/哺乳期用药

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 6 / C-S0-2058 · 收养妈妈也能母乳喂养

```yaml
card_id: C-S0-2058
stages: [S0]
tags: []

front:
  title: 收养妈妈也能母乳喂养
  hook: 没怀孕也能产奶

back:
  why_matters: |
    诱导泌乳(induced lactation)= 没生过孩子的妈妈通过药物 + 频繁吸吮启动乳腺产奶。
    很多人不知道:收养孩子的妈妈、伴侣不哺乳的同性家庭都能尝试。
    通常需要:孕前 2-3 个月开始用催乳药 + 吸奶器、宝宝到家后频繁亲喂、配方奶辅助。
    全母乳很少能实现,但部分母乳 + 配方搭配是可行的常规方案。
    海蒂建议:决定前先咨询哺乳顾问 (lactation consultant),别自己摸索。
  what_to_do:
    - 收养前 2-3 月找哺乳顾问做诱导计划
    - 抱养后即立刻多次亲喂(频率 > 量)
    - 用辅助哺乳器(SNS)边喂配方边吸吮
    - 不指望全母乳,部分母乳就有价值
    - 接受亲喂主要是亲密体验,不是营养主源
  failure_mode: |
    以为"没生过孩子就完全没奶" → 错过尝试的机会。
    要求自己必须"全母乳" → 失败就完全放弃,失去亲喂亲密。
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
  location: "第 1 章 给宝宝喂奶 · 收养宝宝和母乳喂养"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 7 / C-S0-2059 · 婴儿用品别买全套

```yaml
card_id: C-S0-2059
stages: [S0]
tags: []

front:
  title: 婴儿用品别买全套,留 9 月再补
  hook: 一半东西用不到就尺寸不合

back:
  why_matters: |
    商场推销的"婴儿全套清单"= 50+ 件商品打包,营销目的远大于实用。
    海蒂的核心建议:把购物清单当"参考"不当"必买" — 每个宝宝需求不同,你也会收到大量礼物。
    亲友送的 0-3 月衣服、洗澡椅、玩具会塞满半个家;你买的反而很多用不上。
    建议策略:先列清单 → 等亲友送 → 收到后剩下的再买 → 大部分买 6-9 月码,少买 3 月码。
    主要是因为:宝宝长得太快,3 月码穿 4 周就废了。
  what_to_do:
    - 先列"清单",别先买全套
    - 收到亲友礼物后再补不足的
    - 衣服主要买 6-9 月码,少买 3 月码
    - 不买:洗澡椅 / 床铃 / 婴儿椅 / 复杂玩具
    - 季节衣按预产期挪到下季买
  failure_mode: |
    出生前买齐 50 件 → 一半因为礼物重了,一半因为尺寸过了。
    买太多 0-3 月衣服 → 宝宝 3 周就长出去,标签都没拆。
  evidence_level: C

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
  location: "第 2 章 婴儿用品采购 · 总原则"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-009    # 待产物品
  - C-S0-013    # 婴儿用品

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 8 / C-S0-2060 · 婴儿衣服直接买大码

```yaml
card_id: C-S0-2060
stages: [S0]
tags: []

front:
  title: 婴儿衣服直接买大码
  hook: 6-12 月码最实用

back:
  why_matters: |
    婴儿衣服尺码标"月龄"是建议值,各品牌偏差大 — 有的 6 月款只够 4 月穿,有的 6 月款能穿到 9 月。
    海蒂建议:没把握时买大码,理由有 3:
    (1) 衣服洗后会缩水,棉质尤其;
    (2) 宝宝长得比衣服快;
    (3) 大点的衣服可以卷起袖子,小了的衣服只能扔。
    标签注明"6 月"=约 7-10 千克,但中国宝宝可能 4 月就到。
    一个例外:贴身内衣需要正合身,买大了会皱褶磨皮肤。
  what_to_do:
    - 主要买 6-9 月码,卷袖子穿
    - 买前查品牌实际尺寸,别只看标签月龄
    - 棉质衣服按标签往上加 1 码
    - 季末清仓便宜不要买:可能等不到下季就过码
    - 贴身内衣例外:正合身买
  failure_mode: |
    严格按标签买 → 3 周宝宝穿上"3 月码",马上就紧。
    清仓时买未来季节的 → 到时候宝宝已经长出去。
  evidence_level: C

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
  location: "第 2 章 婴儿用品采购 · 宝宝的衣柜"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-2059

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 9 / C-S0-2061 · 月嫂 vs 产妇护导员 vs 钟点工

```yaml
card_id: C-S0-2061
stages: [S0]
tags: []

front:
  title: 月嫂 vs 产妇护导员 vs 钟点工
  hook: 看你想接管什么

back:
  why_matters: |
    产后帮手 3 类:全天保姆/月嫂(管宝宝)、产妇护导员 doula(教妈妈+做饭)、钟点工(只做家务)。
    海蒂的核心提醒:别盲目雇月嫂 — 母乳喂养时月嫂作用有限(她不能喂奶),钟点工反而更解放你。
    选错原因常见:以为"月嫂能教你"但有的月嫂主导欲强反而压制新手;以为"全天住家更省心"但 24 小时陌生人在家很不舒服。
    决策核心问:你想要"接管照看"还是"教你照看"还是"分担家务"?
  what_to_do:
    - 想全天替你带宝宝 + 配方喂养 → 月嫂
    - 想学母乳 + 做饭 + 不接管 → 产妇护导员
    - 母乳喂养 + 想自己带 → 钟点工(只做家务)
    - 面试必问:'你愿意从旁辅导还是主导?'
    - 雇前查肺结核 + 心肺复苏 + 安全培训证
  failure_mode: |
    母乳喂养 + 雇月嫂 → 大部分时间她无事做,反而干扰母婴磨合。
    主导型月嫂入家 → 新手父母彻底失能,月嫂走后崩溃。
  evidence_level: C

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
  location: "第 1 章 临产前的准备 · 保姆或产妇护导员"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 10 / C-S0-2062 · 祖父母首次到访先约边界

```yaml
card_id: C-S0-2062
stages: [S0]
tags: [philosophy, controversy]

front:
  title: 祖父母首次到访先约边界
  hook: 头几周三人单独最重要

back:
  why_matters: |
    祖父母到访问题(grandparents arrival)= 中国家庭的首大冲突点 — 老人通常想立即"接管",新手父母想"先磨合"。
    海蒂的立场:头几周三人独处对建立亲密关系和育儿信心最关键 — 老人晚到几周更好。
    建议直接说:"几周后宝宝有反应了再来,那时更有趣" — 既不伤感情又设好边界。
    老人短期受伤但抱孙后会原谅;新手父母如果一开始没建立"我是父母"的主体感,后续 18 年都难纠正。
    例外:你确实需要帮忙(剖腹产、双胞胎)→ 提前邀,但定好"协助 ≠ 接管"。
  what_to_do:
    - 怀孕 8 月就跟双方父母明确表达"先三人独处几周"
    - 用"几周后宝宝更可爱"婉拒立即到访
    - 你确实想老人帮 → 提前定"做哪些 / 不做哪些"
    - 到访后冲突:不发火,坚定重申主导权在你
    - 让爸爸出面跟自己父母谈最有效
  failure_mode: |
    没设边界 → 老人入家就接管,你彻底失能,母乳/作息/育儿观全乱。
    完全拒绝老人 → 关系裂痕 + 你独自累垮。
    老人坚持"我们当年这么带大你的" → 用"现在标准变了"(如禁趴睡)反驳。
  evidence_level: C

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
  location: "第 1 章 临产前的准备 · 祖父母 / 公婆"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-003    # 祖父母参与
  - C-S0-014    # 中国 4-2-1 祖辈格局

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 11 / C-S0-2063 · 乳房产前不需任何"锻炼"

```yaml
card_id: C-S0-2063
stages: [S0]
tags: [safety]

front:
  title: 乳房产前不需任何"锻炼"
  hook: 越折腾越糟

back:
  why_matters: |
    民间流传"产前锻炼乳头"= 用酒精擦/毛刷刷/按摩/吸奶器 — 海蒂明确说全部错,弊大于利。
    乳头本就为哺乳设计,不需任何"准备"。错误"锻炼"反而:
    (1) 酒精/金缕梅 → 乳头干裂;
    (2) 肥皂洗 → 破坏天然保护油;
    (3) 按摩/吸奶器 → 触发宫缩,严重时早产 + 引发乳腺炎。
    孕晚期(28 周后)肥皂都不要碰乳头。
    真正能做的是"心理准备" — 看书/学知识/找哺乳顾问,而不是物理锻炼。
  what_to_do:
    - 孕晚期不用任何特殊产品擦乳头
    - 不要按摩 / 揉捏 / 用吸奶器试挤
    - 别用酒精 / 金缕梅 / 含香料润肤露
    - 洗澡时清水冲即可,28 周后避肥皂
    - 心理准备:看母乳书 + 联系哺乳顾问
  failure_mode: |
    听老人/网帖建议"提前锻炼" → 乳头开裂、宫缩早产。
    用吸奶器试挤初乳 → 浪费宝贵初乳 + 触发宫缩。
    用肥皂彻底清洗 → 破坏天然抑菌油,反而易感染。
  evidence_level: A

glossary_refs:
  - G-TERM-colostrum

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
  location: "第 1 章 临产前的准备 · 让乳房做好母乳喂养的准备"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 12 / C-S0-2064 · 乳头内陷孕期就评估

```yaml
card_id: C-S0-2064
stages: [S0]
tags: []

front:
  title: 乳头内陷孕期就评估
  hook: 多数能哺乳

back:
  why_matters: |
    乳头内陷(inverted nipple)= 用手指挤压乳晕时乳头不凸出反而缩回乳房。
    民间误以为"内陷乳头不能哺乳"— 错。海蒂引研究:多数内陷乳头不需任何处理就可哺乳成功。
    评估方法:遇冷或挤压乳晕,乳头能凸出 = 不算内陷;持续缩回 = 真内陷。
    真内陷处理:孕期戴乳头保护罩(nipple shield/breast shell),用无痛压力慢慢拉出。
    缺点:罩子显眼会让人感到尴尬,可能出汗起疹 — 多数情况其实不必用。
  what_to_do:
    - 孕中期自检:挤压乳晕看乳头反应
    - 真内陷 → 咨询医生是否需要保护罩
    - 不要自己强拉 / 按摩 / 抠
    - 哺乳期需要时用辅助衔乳工具
    - 接受多数内陷乳头根本不需要处理
  failure_mode: |
    听人说"内陷不能哺乳"放弃尝试 → 错过机会。
    没评估就买保护罩 → 没必要 + 不舒服。
    自己用力按摩抠 → 触发宫缩。
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
  location: "第 1 章 临产前的准备 · 让乳房做好母乳喂养的准备 · 乳头保护罩"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-2063

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 13 / C-S0-2065 · 纸尿裤 vs 棉布尿布

```yaml
card_id: C-S0-2065
stages: [S0]
tags: []

front:
  title: 纸尿裤 vs 棉布尿布:没赢家
  hook: 看你最在意什么

back:
  why_matters: |
    一次性纸尿裤 vs 棉布尿布的"环保 vs 便利"争议 — 海蒂的判断:都没绝对赢家,只看你最在意什么。
    纸尿裤优势:换得快、夜间睡得长、不漏尿。劣势:太干 → 父母不勤换 → 反而起尿布疹;让宝宝感觉舒服 → 学如厕更晚。
    棉布尿布优势:可重用、宝宝感不适会激励训便。劣势:必须配防水裤 → 不透气反而易尿布疹;频换更累;洗护耗水电。
    海蒂主流策略:头几月在家用棉布,外出/夜间用纸尿裤;不强求一种。
    中国家长容易陷入"环保焦虑"或"省钱焦虑",其实日常便利更重要。
  what_to_do:
    - 不必选一种 → 在家棉布 + 外出纸尿裤
    - 纸尿裤要勤换:不靠"湿了才换"判断
    - 用棉布 → 必备透气防水裤,夜间双层
    - 起尿布疹换品牌 / 换种类即可
    - 别陷入"哪种更环保"的辩论,行动更重要
  failure_mode: |
    纸尿裤太干懒得换 → 宝宝长时间湿在里面 → 严重尿布疹。
    全棉布坚持 → 累垮 + 妈妈睡不好(夜间频醒换)。
    买高价"有机"棉布 → 没证据更环保 + 经济压力。
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
  location: "第 1 章 临产前的准备 · 使用哪种尿布"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 14 / C-S0-2066 · 宠物迎新生儿:孕期就训练

```yaml
card_id: C-S0-2066
stages: [S0]
tags: [safety, red_flag]

front:
  title: 宠物迎新生儿:孕期就训练
  hook: 别等出院才介绍

back:
  why_matters: |
    宠物迎新生儿(pet introduction)= 家有狗/猫的孕妇必修课。
    海蒂强调:被当"独子"养的宠物突然让位很容易嫉妒甚至攻击宝宝。攻击案例多发于"事先没准备"的家庭。
    狗的风险:扑跳 / 守食 / 咬挑衅;猫的风险:跳进婴儿床压住宝宝口鼻、抓伤。
    准备核心:宠物新身份过渡(从"独子"到"哥姐") + 婴儿气味提前接触 + 边界训练。
    不要等出院才介绍 — 那时宠物完全没心理准备,反应难控。
  what_to_do:
    - 孕期送狗去基本服从训练班
    - 邀请有娃朋友来家 / 用婴儿娃娃做道具排练
    - 婴儿房门口装栏杆,不让宠物入内
    - 出院前让爸爸把宝宝旧衣服带回家给宠物闻
    - 喂奶时摸狗,推车出门带狗 — 让它感觉没被替代
    - 任何攻击迹象立即隔离 / 严肃训斥
  failure_mode: |
    出院当天才介绍 → 宠物震惊 + 嫉妒 + 攻击概率最高。
    宝宝出生后冷落宠物 → 宠物把负面情绪转嫁宝宝。
    "我家狗温和不会咬" → 压力下任何狗都可能咬。
    猫睡进婴儿床 → 压住口鼻引发窒息,需安装床帐。
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
  location: "第 1 章 临产前的准备 · 让宠物做好准备"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 15 / C-S1-2102 · 母乳的妈妈端 7 大好处

```yaml
card_id: C-S1-2102
stages: [S1]
tags: []

front:
  title: 母乳的妈妈端 7 大好处
  hook: 不只对宝宝好

back:
  why_matters: |
    "母乳好处"讨论几乎全聚焦宝宝,海蒂提醒:对妈妈的好处一样实在。
    7 大妈妈端好处:
    (1) 子宫复旧更快(吸吮触发宫缩),
    (2) 减少恶露 = 失血少,
    (3) 每天多耗 500 卡 → 帮助减孕期重,
    (4) 哺乳激素抑制排卵 → 自然避孕(不100%可靠,见 C-S0-1027),
    (5) 子宫癌 / 卵巢癌 / 绝经前乳腺癌风险下降,
    (6) 风湿性关节炎 + 骨质疏松风险下降,
    (7) 强制频繁短休 → 产后身体被迫修养。
    当作"做不了母乳就失败"看是错的;当作"额外好处"激励持续就对。
  what_to_do:
    - 把妈妈端好处写下来,情绪低时看
    - 哺乳间隔躺下 = 身体修养时间,别用来做家务
    - 别因为"想瘦"少吃 → 哺乳额外耗 500 卡
    - 自然避孕不可靠 → 6 周后查产后避孕方案
    - 哺乳期定期乳房自检
  failure_mode: |
    只看宝宝端好处 → 自己累垮时找不到坚持的支点。
    误以为"哺乳期不会怀孕" → 6 周内可能就排卵了(见 C-S0-1027)。
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
  location: "第 1 章 给宝宝喂奶 · 有利于母乳喂养的事实 · 对父母来说,母乳喂养的好处"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-050    # AAP 母乳起步
  - C-S1-1013   # WHO HIV+AFASS

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 16 / C-S1-2103 · 母乳频喂 vs 配方久饱:正常

```yaml
card_id: C-S1-2103
stages: [S1]
tags: []

front:
  title: 母乳频喂 vs 配方久饱:正常
  hook: 不是奶不够

back:
  why_matters: |
    新手妈妈最焦虑误判:"母乳宝宝怎么 1.5 小时又要吃,是不是奶不够?"
    海蒂明确:母乳消化快(液态、酶辅助),配方奶在胃里形成橡胶状凝乳,消化慢 → 母乳宝宝就是该频喂。
    AAP 立场:每天 8-12 次(白天 2-3h 一次)是正常,而不是"该 4h 一次"。
    判断"够不够"看的是:每天 6-8 次湿尿布 + 每周增重稳定,而不是"宝宝不哭就是饱"或"间隔短就是饿"。
    频繁吃也是宝宝主动调奶量的方式 — 越吸越多,妈妈越休息越少。
  what_to_do:
    - 母乳宝宝 1.5-3h 一次都正常,不必焦虑
    - 看尿布数(每天 6-8 块湿)+ 每周增重判断够不够
    - 别用"配方间隔 4h"的标准衡量母乳
    - 不要混合喂养"补一瓶" → 反而打乱供需
    - 真担心 → 找哺乳顾问或医生评估,不自我判断
  failure_mode: |
    用"配方间隔"标准衡量母乳 → 误以为奶不够 → 急转配方。
    "宝宝刚吃完又哭" 立刻补配方 → 减少吸吮 → 妈妈奶量真的下降 → 自我应验。
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
  location: "第 1 章 给宝宝喂奶 · 有利于配方奶喂养的事实 · 宝宝饱足感持续时间"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-050    # AAP 母乳起步 8-12 次
  - C-S1-1003   # BFHI 第 6 步默认不给配方

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 卡片 17 / C-S1-2104 · 决定不喂母乳:别内疚

```yaml
card_id: C-S1-2104
stages: [S1]
tags: [philosophy]

front:
  title: 决定不喂母乳:别内疚
  hook: 配方奶宝宝也健康

back:
  why_matters: |
    母乳/配方决策的最大隐藏代价:做配方妈妈的"罪疚感"。
    海蒂明确说:如果母乳让你不快乐,深情递上的奶瓶比勉强递上的乳房好 — 宝宝能感觉到妈妈的不安。
    无数健康宝宝是配方喂养长大的;现代配方奶营养足够支撑 0-12 月。
    配方妈妈不必每次喂奶都说"对不起"或刻意低调。决定后就坚持,别在两种间反复纠结。
    这是"心理负担成本" 议题,不是"营养"议题 — 别让"不母乳就失败"的话术绑架。
  what_to_do:
    - 决定后坚定:不再纠结"是不是该再试母乳"
    - 用奶瓶喂时 = 创造同样亲密机会(肌肤接触 / 目光 / 抱姿)
    - 让爸爸 / 祖辈分担喂养,你休息
    - 拒绝"母乳道德绑架":你的决定不需别人同意
    - 关注宝宝增重和发展,不关注"该不该母乳"
  failure_mode: |
    长期内疚 → 影响产后心理,反而损害母婴关系。
    在母乳/配方间反复 → 两种都做不好,妈妈崩溃。
    用配方时刻意"补偿"(例如冷漠喂奶) → 失去亲喂亲密的机会。
  evidence_level: C

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
  location: "第 1 章 给宝宝喂奶 · 做出决定 · 如果你决定不采用母乳"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S0-2056   # 决策权衡
  - C-S1-1013   # WHO HIV AFASS(也是不"母乳=好"的去道德化)

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## 落盘指令(给主线)

请把上面 17 个 yaml 块各自落到下面对应路径(文件名 = card_id):

```
30-cards/s0-pregnancy/C-S0-2053.yaml
30-cards/s0-pregnancy/C-S0-2054.yaml
30-cards/s0-pregnancy/C-S0-2055.yaml
30-cards/s0-pregnancy/C-S0-2056.yaml
30-cards/s0-pregnancy/C-S0-2057.yaml
30-cards/s0-pregnancy/C-S0-2058.yaml
30-cards/s0-pregnancy/C-S0-2059.yaml
30-cards/s0-pregnancy/C-S0-2060.yaml
30-cards/s0-pregnancy/C-S0-2061.yaml
30-cards/s0-pregnancy/C-S0-2062.yaml
30-cards/s0-pregnancy/C-S0-2063.yaml
30-cards/s0-pregnancy/C-S0-2064.yaml
30-cards/s0-pregnancy/C-S0-2065.yaml
30-cards/s0-pregnancy/C-S0-2066.yaml
30-cards/s1-newborn/C-S1-2102.yaml
30-cards/s1-newborn/C-S1-2103.yaml
30-cards/s1-newborn/C-S1-2104.yaml
```

不需新建术语卡 — 都引用已有 glossary。

源文件主要内容已提取本 Part 增量。Part 1 仍有少量内容(选医生中段、保险类型、双胞胎收养特殊场景)价值低或与现有卡覆盖重叠,已跳过。
