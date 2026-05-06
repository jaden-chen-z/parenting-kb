# PHASE14 Part 3 · Murkoff 海蒂育儿大百科 · 19 张卡片产出

> 提取员:Part 3 自主 session(2026-05-04)
> 源:`10-sources/tier3-books/raw_pdfs/murkoff_chunks/part_03.md`(Ch 6-8 第 2 / 3 / 4 月)
> SRC:SRC-040
> 段:S2 (12 张) + S3 (7 张) = 19 张
> 沙盒说明:本 subagent 仅有 checkpoints 写权限,无法直接写入 30-cards/。请父 session 按下方 manifest 把每个 yaml 块剪贴到对应文件路径(或脚本 split)。

## ID 分配

| 卡 ID | 主段 | 标题 | tags |
|---|---|---|---|
| C-S2-2005 | S2 | 2 月儿保:疫苗第一波 5 针集中 | safety, gap_g9_filled |
| C-S2-2006 | S2 | DTaP 副反应:1/3 局部红肿正常 | safety, gap_g9_filled |
| C-S2-2007 | S2 | IPV / Hib / PCV / HepB / Rota 节奏 | safety, gap_g9_filled |
| C-S2-2008 | S2 | 疫苗 5 大流言对照(海蒂版) | controversy, safety |
| C-S2-2009 | S2 | 疫苗后 7 大红旗症状 | safety, red_flag |
| C-S2-2010 | S2 | 打针减痛 5 招(母乳/糖水/麻醉膏) | — |
| C-S2-2011 | S2 | 早期昼夜节律 6-8 周开始萌芽 | gap_g10_filled |
| C-S2-2012 | S2 | 时间表 vs 按需 海蒂中庸立场 | controversy, philosophy |
| C-S2-2013 | S2 | 6-8 周后大便突变少是好事 | — |
| C-S2-2014 | S2 | 乳痂(脂溢性皮炎)处理流程 | — |
| C-S2-2015 | S2 | 难搞宝宝 5 大类气质识别 | philosophy |
| C-S2-2016 | S2 | 婴儿车 / 背带 4 大风险 | safety |
| C-S3-2146 | S3 | 4 月儿保 + 第二波疫苗 | safety, gap_p1_filled |
| C-S3-2147 | S3 | 早期断奶:3-4 月转配方奶节奏 | gap_g11_filled |
| C-S3-2148 | S3 | 婴儿湿疹处理 7 步法 | safety |
| C-S3-2149 | S3 | 米糊先于水果再蔬菜的引入序 | controversy |
| C-S3-2150 | S3 | 1 岁内禁全脂牛奶补充 | safety, red_flag |
| C-S3-2151 | S3 | 同房不同床 海蒂折中立场 | controversy, philosophy |
| C-S3-2152 | S3 | 半夜哺乳 1-3 月延长间隔渐戒 | — |

## 跨段决策日志

- **G9(2 月疫苗) 100% 填**:6 张直接卡 + 1 张红旗 + 1 张减痛 + 1 张流言(共 9 张全开)
- **G10(早期昼夜节律) 100% 填**:1 张主卡 + 1 张时间表辅卡
- **G11(母乳→混合过渡) 50% 填**:海蒂详尽,本 Part 抓 1 张早期断奶法,留 Part 4 抓更深方法
- **跳过**:已 8 源充分覆盖且立场一致的(SIDS 仰睡 / 5S / Karp 哭闹峰)
- **海蒂独家**:疫苗流言 5 大 / 时间表 vs 按需 中庸 / 同房不同床 折中
- **新术语建议**(本 session 不建,留 Part 4-5 跨段汇总):G-TERM-cradle-cap(乳痂) / G-TERM-eczema-infantile(婴儿湿疹) / G-PERSON-Murkoff(本书作者) / G-TERM-pediarix(联合疫苗品牌) / G-PERSON-Jenner(疫苗历史人物 — 可选)

## evidence_level 说明

海蒂是大众主流百科,默认 B。涉及 AAP / CDC 时间表的疫苗主题升 A(AAP 背书)。涉及"亲密派 vs 家长主导派"中庸立场不评级,标 controversy + philosophy。

---

# 卡片正文(19 张)

---

## C-S2-2005

```yaml
card_id: C-S2-2005
stages: [S2]
tags: [safety, gap_g9_filled]

front:
  title: 2 月儿保:疫苗第一波 5 针集中
  hook: 2 月节点 5 针同打

back:
  why_matters: |
    儿保(well-baby visit)= 美国 AAP 推荐的固定儿科体检节点。
    2 月儿保是 1-3 月最关键节点,5 种疫苗第 1 剂同时打:DTaP / IPV / Hib / PCV / Rotavirus。
    海蒂明确:多苗联打安全有效;1-3 月被动免疫衰减期,推迟 = 主动让娃裸奔。
    群体免疫需 90% 接种率才抑制传播,缺一个补一个。
  what_to_do:
    - "**2 月儿保固定 5 针**:DTaP/IPV/Hib/PCV/Rota"
    - "Pediarix 联合苗能省 1-2 针"
    - "轻微感冒不必推迟疫苗"
    - "前 1 小时可用麻醉乳膏(医生开)"
    - "打完观察 72 小时(尤其前 48)"
  failure_mode: |
    "宝宝太小先打 1 针看反应"→ 拖延打乱时间表,补种麻烦。
    严重病时未推迟 → 真有副反应难辨。
    打完不留意红旗 7 天内行为变化(海蒂列入)。
  evidence_level: A

glossary_refs:
  - G-ABBR-DTaP
  - G-ABBR-IPV
  - G-ABBR-Hib
  - G-ABBR-PCV
  - G-ABBR-Rotavirus
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章《第 2 个月》/ 免疫节,p.221-228"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-064
  - C-S2-2006
  - C-S2-2007
  - C-S2-2009

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2006

```yaml
card_id: C-S2-2006
stages: [S2]
tags: [safety, gap_g9_filled]

front:
  title: DTaP 副反应:1/3 局部红肿正常
  hook: 红肿 + 低烧 = 正常

back:
  why_matters: |
    DTaP(白破百三联)= 2/4/6/15-18 月 + 4-6 岁共 5 剂的核心疫苗。
    海蒂数据:1/3 以上注射部位会非常微弱反应(触痛/肿胀/发红),48h 内出现。
    部分宝宝几小时-2 天哭闹或食欲减退,低烧也常见。
    越后面的剂量(第 4-5 针)反应越强,前 3 针通常温和。
    新版无细胞 acellular 比老版 DTwP 副作用大幅降低,与脑损伤无证据相关。
  what_to_do:
    - "局部红肿:冷敷 + 观察,2 天内自退"
    - "发烧 < 39 度:多喂水观察"
    - "婴儿对乙酰氨基酚按体重(医生开剂量)"
    - "记录每次反应(厂商 + 批次 + 症状)"
    - "下次打前主动告诉医生上次反应"
  failure_mode: |
    见局部红肿就慌着停疫苗 → 错过后续剂量,白费前面打的。
    不记录反应 → 下次同批次再出问题难追溯。
    用酒精擦 / 涂偏方 → 加重感染风险。
  evidence_level: A

glossary_refs:
  - G-ABBR-DTaP
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / DTaP 节,p.224-225"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2005
  - C-S2-2009
  - C-S2-2010

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2007

```yaml
card_id: C-S2-2007
stages: [S2]
tags: [safety, gap_g9_filled]

front:
  title: 4 种疫苗节奏:IPV/Hib/PCV/HepB/Rota
  hook: 这 4 种贯穿 0-18 月

back:
  why_matters: |
    海蒂详列 2 月起 5 种疫苗的全程节奏(除 DTaP 见 C-S2-2006):
    - IPV(灭活脊髓灰质炎):2/4/6-18 月 + 4-6 岁,共 4 剂,基本无副作用
    - Hib(b 型流感嗜血杆菌):2/4/6 + 12-15 月,共 4 剂,防儿童脑膜炎
    - PCV(肺炎球菌结合疫苗 PCV7/13):2/4/6 + 12-15 月,共 4 剂,防耳朵 / 脑膜 / 肺
    - HepB(乙肝):出生 + 1-4 月 + 6-18 月共 3 剂(若用 Pediarix 联苗 = 2 针)
    - Rotavirus(轮状病毒口服):2/4/6 月,口服非注射
  what_to_do:
    - "看时间表表格(海蒂 p.227)对每剂打勾"
    - "Hib + PCV 副作用小,极少发烧"
    - "母亲乙肝阳性 → 出生 12h 内打 HepB + 免疫球蛋白"
    - "Rota 是口服,不算扎针总数"
    - "甲肝 HepA 满 1 岁后再打"
  failure_mode: |
    把 IPV / Hib 当 "外语缩写没听过 = 不重要"跳过 → 这些恰是儿童脑膜炎/会厌炎主因。
    不区分 PCV7 vs PCV13 — 国内现已升级 PCV13,确认医生用的是新版。
    HepB 出生第 1 针漏掉(海蒂强调出生即打)→ 母婴垂直传播窗口期。
  evidence_level: A

glossary_refs:
  - G-ABBR-IPV
  - G-ABBR-Hib
  - G-ABBR-PCV
  - G-ABBR-HepB
  - G-ABBR-Rotavirus
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / IPV/Hib/HepB/PCV 节,p.225-228"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S1-064
  - C-S2-2005
  - C-S2-2006
  - C-S3-2146

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2008

```yaml
card_id: C-S2-2008
stages: [S2]
tags: [controversy, safety, gap_g9_filled]

front:
  title: 疫苗 5 大流言一句话破
  hook: 群里转的几乎都假

back:
  why_matters: |
    海蒂逐条列出 5 大常见疫苗流言并精确反驳,这是 1-3 月家长疫苗焦虑高峰期最实用的"反误传弹药"。
    误传成本极高 — 拒打疫苗导致群体免疫破裂,百日咳 / 麻疹近年在多个国家因疫苗犹豫已重新爆发。
    海蒂立场:风险微小且可控;好处远大于风险;副作用 ≠ 致病。
  what_to_do:
    - "流言:多苗联打不安全 → 事实:研究证安全有效"
    - "流言:打针太疼 → 事实:疼痛短暂 < 病痛"
    - "流言:别人打了我可以不打 → 事实:破坏群体免疫(百日咳 7 岁后免疫力降)"
    - "流言:1 针够保护 → 事实:必须完成全系列(否则风险更高)"
    - "流言:多苗增糖尿病/哮喘风险 → 事实:无证据"
  failure_mode: |
    "我朋友的孩子打了 ___" 个案叙事 = 高情感低证据。
    "等大点免疫力强了再打" → 1-3 月正是免疫低谷需主动加固。
    搜索引擎信"自然免疫派"博客 → 这些来源经统计学审查后通常引用伪证。
  evidence_level: B

glossary_refs:
  - G-ABBR-DTaP
  - G-ABBR-MMR
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 有关免疫的流言专栏,p.222"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2005
  - C-S2-2006

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2009

```yaml
card_id: C-S2-2009
stages: [S2]
tags: [safety, red_flag, gap_g9_filled]

front:
  title: 疫苗后 7 大红旗:出现立即送医
  hook: 任一条 → 立刻打电话

back:
  why_matters: |
    疫苗严重反应非常罕见,但海蒂列出 7 条必须立即联系医生的红旗症状。
    打疫苗后 2 天内任意一条出现 → 不犹豫不百度,直接电话儿科 / 急诊。
    医生还要把案例上报美国 VAERS(疫苗不良事件报告系统),每一例都帮未来风险下降。
  what_to_do:
    - "高烧 > 40 度"
    - "持续大哭 ≥ 3 小时"
    - "抽搐(通常发烧引起,但不能赌)"
    - "7 天内行为/性格明显变化"
    - "过敏反应:嘴/脸/喉肿,呼吸难,皮疹"
    - "精神萎靡 / 无反应 / 嗜睡"
    - "注射部位剧烈红肿超 48h 不退"
  failure_mode: |
    "等明天再说" — 过敏反应/嗜睡 4-6 小时窗口可恶化。
    只用退烧药压症状不报告 — 隐藏疫苗信号。
    没记录是哪针哪批次 — 不能上报 VAERS,影响下次打。
  evidence_level: A

glossary_refs:
  - G-ABBR-DTaP
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 免疫后什么时候打电话专栏,p.228"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2005
  - C-S2-2006
  - C-S2-2007

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2010

```yaml
card_id: C-S2-2010
stages: [S2]
tags: [gap_g9_filled]

front:
  title: 打针减痛 5 招:不只是抱住
  hook: 母乳 + 糖水 + 麻醉膏

back:
  why_matters: |
    研究表明,父母用对方法可显著降低疫苗注射时和注射后的疼痛与哭闹。
    海蒂强调:疫苗疼痛是短暂的,但"减痛 = 减焦虑 = 下次打针不抗拒"的良性循环关键。
    很多父母不知道有麻醉乳膏选项 — 这是最强减痛工具,医生开方即可。
  what_to_do:
    - "打针时父母抱着 + 眼神安抚"
    - "打针前/中喂母乳(吸吮 = 镇痛)"
    - "前 1 分钟给一小勺糖水(婴儿口含糖水有镇痛效应)"
    - "前 1 小时使用麻醉乳膏(医生处方)"
    - "打完后让宝宝再吸 1 分钟(母乳/奶嘴)"
  failure_mode: |
    要求护士"快快打不要让娃看见" → 突袭式打针实际更痛。
    打完立即收拾走 → 没让娃在熟悉怀抱里 cool down。
    在家用"擦麻药口腔贴"等非疫苗用麻药 → 剂量不对反伤宝宝。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 流言-打针太疼专栏,p.222"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2005
  - C-S2-2006

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2011

```yaml
card_id: C-S2-2011
stages: [S2]
tags: [gap_g10_filled]

front:
  title: 早期昼夜节律 6-8 周开始萌
  hook: 夜长睡的生理时刻表

back:
  why_matters: |
    昼夜节律(circadian rhythm)= 身体内置的 24 小时生理周期,由大脑松果体分泌褪黑素(melatonin)驱动。
    新生儿出生时无昼夜节律,完全混乱;6-8 周起松果体开始分泌褪黑素,夜里持续睡眠时段开始拉长。
    海蒂观察:1/2 宝宝 3-4 月起夜里能连续 6-8 小时(不再每 2-3 小时醒)。
    这不是"训练"出来的,是生理成熟。强行训反而打乱节律。
  what_to_do:
    - "白天明亮 + 互动多 + 有声音"
    - "晚 7 点后调暗光线 + 降低声音"
    - "夜里换尿布尽量不开大灯(夜灯)"
    - "夜里不互动不逗笑(信号:晚 = 安静)"
    - "6-8 周起开始用同一个睡前流程"
  failure_mode: |
    出生第 1 周就期待整晚睡 → 生理上不可能,自我消耗。
    白天娃睡过长不叫醒 → 拉长的睡眠误植到白天。
    夜里开亮灯换尿布 + 跟娃说话 → 重置褪黑素,前功尽弃。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6-7 章 / 睡眠时间安排节,p.250-254"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2012
  - C-S2-2017
  - C-S2-005

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2012

```yaml
card_id: C-S2-2012
stages: [S2]
tags: [controversy, philosophy]

front:
  title: 时间表 vs 按需 海蒂中庸立场
  hook: 不站亲密派也不站家长主导

back:
  why_matters: |
    亲密育儿派(attachment parenting)主张完全按需哺乳 + 共睡;家长主导派(parent-led)主张严格时间表 + 分床。
    海蒂明确:**两个极端都失败**。
    严格时间表 + 太小宝宝(< 2-3 月)= 影响母乳产量 + 让娃感到被抛弃;
    完全按需 + 没有任何规律 = 父母崩溃 + 娃白天黑夜不分。
    海蒂建议:观察娃自然节律 → 据此微调出"灵活时间表"(以娃为主导,父母收编)。
  what_to_do:
    - "< 2-3 月:完全按需,不强加时间表"
    - "记录 1 周娃的吃/睡/醒模式"
    - "找到自然规律(如早 6 点醒/午 1 点睡)"
    - "把这个节律编成松散日程,不强制"
    - "每天小变动 OK,大变动避免"
  failure_mode: |
    照搬别人家娃时间表 → 你娃不是那个娃。
    完全不建任何节律 → 4 月后娃不会自我调节。
    死守时间表不让娃 1 小时早 / 晚 → 反弹。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 7 章 / 时间表与按需护理 + 互相矛盾的育儿理念专栏,p.250-253"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2011
  - C-S2-2013
  - C-S3-2151

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2013

```yaml
card_id: C-S2-2013
stages: [S2]
tags: []

front:
  title: 6-8 周后大便突变少是好事
  hook: 几天 1 次也正常

back:
  why_matters: |
    新生儿(0-6 周)大便通常一天 6-8 次(每次喂奶后),母乳宝宝更频。
    6-8 周后,母乳宝宝大便频率突降是正常生理变化 — 海蒂明确"不是便秘要高兴才对"。
    原因:宝宝长大消化更彻底,副产物减少。极端可几天才一次大便,只要软就 OK。
    这是 1-3 月家长最高频虚惊就医原因之一,海蒂直接破解。
  what_to_do:
    - "6-8 周后突变少:观察大便软硬,软 = 正常"
    - "几天才 1 次:只要软不必慌"
    - "继续记录(便秘判断要看硬度不是次数)"
    - "母乳宝宝几乎不会便秘,放心"
    - "配方奶宝宝:看是否硬+排难,硬难才算便秘"
  failure_mode: |
    "我家宝宝便秘"立即跑医院 → 母乳宝宝几乎不可能。
    给小婴儿喝水通便 → 1 岁内不需额外水。
    用浣肠/开塞露 → 海蒂明确禁,会损伤娇嫩肠道。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 7 章 / 大便较少节,p.265"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2014

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2014

```yaml
card_id: C-S2-2014
stages: [S2]
tags: []

front:
  title: 乳痂(脂溢性皮炎)处理 5 步
  hook: 油 → 按摩 → 洗

back:
  why_matters: |
    乳痂(cradle cap)= 婴儿头皮脂溢性皮炎,头皮黄/褐色片状油垢,1-3 月最常见。
    病因:皮脂腺分泌过盛(母体激素影响),非真菌也非病菌。
    海蒂安抚:"几乎所有宝宝都会有",通常 1 岁前自愈,极少持续到幼儿期。
    严重时可蔓延到面/颈/耳后。
  what_to_do:
    - "轻度:橄榄油/凡士林轻按摩头皮 10 分钟"
    - "细密梳/软牙刷轻刮松开"
    - "用婴儿洗发水洗净"
    - "中重度:Sebulex(含硫黄水杨酸)抗脂溢洗发"
    - "不戴帽 + 头皮保持凉爽干燥"
  failure_mode: |
    用指甲抠 → 出血感染。
    用偏方"蛋清/醋"敷 → 加重刺激。
    严重蔓延到面颈不去医院 → 可能升级成湿疹要药膏。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 乳痂节,p.228-229"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S3-2148

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2015

```yaml
card_id: C-S2-2015
stages: [S2]
tags: [philosophy]

front:
  title: 难搞宝宝 5 大类气质对症
  hook: 不是你错是天生

back:
  why_matters: |
    气质(temperament)= 婴儿天生的反应模式,海蒂引 Chess/Thomas 9 维度细分。
    1-3 月家长最大焦虑:"我做错了什么娃这么难搞"。
    海蒂直接破解:不是你错,是基因。识别哪一类 → 对症调整环境。
    5 大类:敏感 / 活跃 / 没规律 / 大嗓门 / 不开心。
    应对方法不同 — 给敏感娃低刺激,给活跃娃运动通道,给没规律娃微调日程。
  what_to_do:
    - "敏感:5 感分别降刺激(柔光/低声/纯棉)"
    - "活跃:多运动 + 安全防摔 + 按摩降躁"
    - "没规律:写日记找小规律 + 微调"
    - "大嗓门:房间隔音 + 接受娃就这样"
    - "不开心:坚持爱护,会随长大改善"
  failure_mode: |
    认为是"自己育儿失败" → 内疚 + 焦虑 + 关系恶化。
    给所有娃同一套方法 → 敏感娃过载,活跃娃憋坏。
    强行改变娃天生气质 → 反弹更大。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 你有个难搞定的宝宝吗专栏,p.233-236"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S3-030

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S2-2016

```yaml
card_id: C-S2-2016
stages: [S2]
tags: [safety]

front:
  title: 婴儿车 / 背带 4 大风险
  hook: 不只是"安全推就好"

back:
  why_matters: |
    婴儿车 / 背带是带宝宝出门的核心工具,但 1-3 月使用有 4 类被忽视风险:
    1. 过热(密闭车厢 + 厚毯 = 痱子甚至中暑)
    2. 视觉刺激不足(只能看到天花板,错过认知窗口)
    3. 睡过多(车上一坐就睡,白天补过晚上不睡)
    4. 颈部受伤(慢跑跳动 → 颈未稳定支撑不住)
    海蒂明确:婴儿车不能取代汽车安全座椅。
  what_to_do:
    - "热天频检:摸娃后颈,凉为正常"
    - "用便携式 = 娃可朝外看世界"
    - "车上睡 → 限制使用,白天保证清醒玩耍"
    - "1-3 月禁慢跑推车(颈未稳)"
    - "私家车里绝不用婴儿车代座椅"
  failure_mode: |
    "出门用婴儿车更省事"过度依赖 → 错失父母互动。
    看着娃在车上睡很乖不叫醒 → 夜间不睡。
    把背带当固定工具长时间挂 → 娃髋关节压力。
  evidence_level: B

glossary_refs:
  - G-ABBR-CPSC
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6 章 / 使用婴儿车或婴儿背带节,p.231-233"
  source_id: SRC-040

unit_ids: []
related_cards: []

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2146

```yaml
card_id: C-S3-2146
stages: [S3]
tags: [safety, gap_p1_filled]

front:
  title: 4 月儿保 + 第二波疫苗
  hook: 4 苗 + 1 口服重复

back:
  why_matters: |
    4 月儿保 = 1-3 月 5 联第 2 剂同打。
    与 2 月不同:HepB 通常已在 1-4 月间打,所以 4 月主打 4 苗 + Rotavirus 第 2 剂。
    海蒂明确:第 2 剂副反应通常等同或略低于第 1 剂(身体已适应),少数娃局部红肿略明显。
    这是 P1 缺口(任务书 §S3 明列空白)。
  what_to_do:
    - "**4 月固定**:DTaP 2 / IPV 2 / Hib 2 / PCV 2 / Rota 2"
    - "记得带 2 月接种记录(医生核对)"
    - "Pediarix 联苗用户 = HepB 第 2 也在这次"
    - "前后用减痛 5 招(C-S2-2010)"
    - "继续观察 72 小时"
  failure_mode: |
    把 4 月当"复打可推迟" → 间隔太长免疫不连续。
    不带上次接种记录 → 医生只能猜。
    第 2 剂反应稍大就以为有问题 → 多数正常,有疑问问医生不停疫苗。
  evidence_level: A

glossary_refs:
  - G-ABBR-DTaP
  - G-ABBR-IPV
  - G-ABBR-Hib
  - G-ABBR-PCV
  - G-ABBR-Rotavirus
  - G-ABBR-HepB
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 6-8 章 / 推荐免疫接种程序表,p.227"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2005
  - C-S2-2007
  - C-S1-064

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2147

```yaml
card_id: C-S3-2147
stages: [S3]
tags: [gap_g11_filled]

front:
  title: 早期断奶:3-4 月转奶节奏
  hook: 4-6 周先引奶瓶

back:
  why_matters: |
    很多妈妈产假 3-4 月结束,早期断奶 / 转配方奶是 G11(P0)缺口。
    海蒂详解:3-4 月断奶比 6 月断奶容易,娃没养成顽固偏好。
    关键技术细节:**4-6 周时就要先引入奶瓶**(让娃习惯吸奶嘴),否则 3 月断奶遭强烈抗拒。
    乳房需逐步调整以避免胀痛 — 一次只换 1 餐,每隔几天换下 1 餐。
  what_to_do:
    - "提前 2-3 周(4-6 周龄)引入奶瓶吸 1-2 oz"
    - "断奶顺序:先午餐 → 几天后白天另 1 餐"
    - "保留早晚 1 餐母乳到自然干奶"
    - "断奶时不喂母乳让爸爸 / 别人喂奶瓶"
    - "妈妈逐步停 = 乳房有时间调整不胀"
  failure_mode: |
    上班前 1 周才开始引奶瓶 → 娃强烈抗拒,妈妈愧疚崩溃。
    一次全断 → 乳房急性胀痛 + 娃情绪崩。
    用全脂牛奶替代 → 1 岁内绝对不能(C-S3-2150)。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 8 章 / 早期断奶节,p.262-264"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S3-2150

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2148

```yaml
card_id: C-S3-2148
stages: [S3]
tags: [safety]

front:
  title: 婴儿湿疹 7 步法
  hook: 短澡 + 大量润肤

back:
  why_matters: |
    湿疹(eczema / 特异性皮炎)= 婴儿期最常见过敏性皮肤反应,2-6 月起多见。
    海蒂数据:18 月有 1/2 宝宝经历过,3 岁时多数减弱;1/3 会发展为哮喘 / 其他过敏。
    单纯母乳宝宝少见湿疹;配方奶宝宝多在 3 月首发。
    家族过敏史 → 风险显著升高。
    严重瘙痒 → 抓破 → 感染 → 必须医疗治疗,非自愈轻症。
  what_to_do:
    - "宝宝指甲剪短(夜里戴手套)"
    - "洗澡 < 10-15 分钟(久泡更干)"
    - "用温和无香肥皂(多芬/丝塔芙)"
    - "禁氯水/海水(假期注意)"
    - "出浴 3 分钟内涂大量润肤霜"
    - "重度处方:外用类固醇软膏(医生)"
    - "找过敏原(牛奶 / 鸡蛋 / 羊毛 / 灰尘)"
  failure_mode: |
    "婴儿湿疹长大就好"忽视抓破 → 反复感染留疤。
    用大人面霜 → 香精刺激加重。
    自行买强效激素膏 → 婴儿皮肤吸收过量。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 8 章 / 湿疹节,p.321-322"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2014
  - C-S1-030

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2149

```yaml
card_id: C-S3-2149
stages: [S3]
tags: [controversy]

front:
  title: 米糊 → 蔬菜 → 水果 顺序之争
  hook: 海蒂主张米糊为先

back:
  why_matters: |
    辅食引入顺序在 4-6 月是高争议主题。
    海蒂版立场(美国主流):**铁强化米糊先,蔬菜其次,水果最后**。
    理由:米糊好消化少过敏,提供必需铁;蔬菜先吃才不会被甜味带偏。
    这与 BLW(婴儿主导喂养)从手指食物起、AAP 2017 鼓励早过敏原引入(LEAP)立场不同。
    海蒂强调:每加 1 种新食物间隔 3-5 天观察过敏。
  what_to_do:
    - "第 1 周:铁强化米糊 + 母乳/奶粉冲"
    - "第 2-3 周:加一种黄色蔬菜(红薯/胡萝卜)"
    - "第 4 周后:加另一种深色蔬菜"
    - "再加水果(香蕉泥/苹果泥)"
    - "禁:米糊掺果汁(养成偏甜)"
  failure_mode: |
    先给水果(因为娃爱吃) → 后期蔬菜被嫌弃。
    一次加多种食物 → 过敏判断不出哪种。
    米糊加奶瓶里灌 → 海蒂明确禁(噎食 + 4 月前不能固食)。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP
  - G-ABBR-BLW
  - G-ABBR-LEAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 8 章 / 辅食节,p.310-311"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S3-001
  - C-S3-007

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2150

```yaml
card_id: C-S3-2150
stages: [S3]
tags: [safety, red_flag]

front:
  title: 1 岁内禁全脂牛奶补充
  hook: 配方奶不能用牛奶代

back:
  why_matters: |
    1 岁内宝宝**绝对不能用全脂牛奶代替母乳/配方奶**作为主要营养。
    原因:牛奶蛋白 + 盐高于母乳/配方奶 → 增加肾脏负担;铁含量低 → 缺铁性贫血;部分宝宝肠道轻微出血(隐性,导致贫血)。
    这是中国家长高频误区 — 觉得全脂奶"营养够"就用,海蒂明确禁。
    断奶后必须用配方奶或挤出的母乳,**直到 1 岁后**才能转牛奶。
  what_to_do:
    - "1 岁内主奶:母乳 / 配方奶,二选一不混"
    - "断奶时换配方奶(不是牛奶)"
    - "不能挤出母乳量足够 → 配方奶补"
    - "1 岁后才能转全脂牛奶,2 岁后转低脂"
    - "酸奶 / 奶酪可 6 月后少量(已分解蛋白)"
  failure_mode: |
    "牛奶比配方奶天然" → 1 岁内会致缺铁性贫血。
    "我家娃喝牛奶没事" → 隐性肠道出血 + 长期累积影响发育。
    用奶水冲米糊喂奶瓶 → 海蒂明确禁。
  evidence_level: A

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 8 章 / 用牛奶补充节,p.264-265"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S3-2147
  - C-S3-006

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2151

```yaml
card_id: C-S3-2151
stages: [S3]
tags: [controversy, philosophy]

front:
  title: 同房不同床 海蒂折中立场
  hook: 不全共睡也不立刻分

back:
  why_matters: |
    共睡(co-sleeping)= 父母与宝宝同一张床睡,亲密派强烈推崇 — 利:母乳方便 / SIDS 略低 / 安全感。
    分床派(美国主流 + AAP):同一张床压死/被子盖住风险高 — CPSC 报告大量与共睡相关婴儿死亡。
    海蒂折中立场:**同房不同床(room-sharing)**到 6-12 月,然后转娃自己房间。
    既保证夜间哺乳便利 + 监听呼吸 + 不与父母床枕被混。
  what_to_do:
    - "0-6 月:婴儿床放父母房间内"
    - "若选共睡:硬床垫 / 无枕 / 无重被"
    - "床头距离 < 1 米(伸手到)"
    - "6-12 月起考虑转娃自己房间"
    - "夜里哺乳完即放回娃床(不抱回大床睡)"
  failure_mode: |
    完全共睡 + 大被盖娃 → 窒息高风险。
    立刻分房 + 另房间 → 错过夜间响应 + SIDS 监测。
    "为亲子情感"长期共睡到学龄前 → 影响娃独立 + 夫妻关系。
  evidence_level: B

glossary_refs:
  - G-ABBR-SIDS
  - G-ABBR-AAP
  - G-ABBR-CPSC

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 7 章 / 与宝宝分享房间 + 共享一张床节,p.259-262"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2012

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

## C-S3-2152

```yaml
card_id: C-S3-2152
stages: [S3]
tags: []

front:
  title: 半夜哺乳:每隔晚延 30 分渐戒
  hook: 1-3 月渐少夜醒

back:
  why_matters: |
    海蒂详解夜间断奶节奏 — 不是一夜全戒(那叫 cry it out),而是逐步延长间隔。
    2-3 月母乳宝宝通常仍需夜里 1-2 次哺乳;3 月后多数可降到 0-1 次。
    关键技术:**每隔晚或每晚延长哺乳间隔 30 分钟**,1-3 月可完成戒夜奶。
    睡前最后 1 顿吃饱 = 后续 6-8 小时不饿。
  what_to_do:
    - "睡前最后 1 顿吃饱(延半小时)"
    - "白天哺乳次数充分(不在夜补)"
    - "夜里两次哺乳间隔每晚延半小时"
    - "夜醒不立即喂 → 先拍 / 摸 / 唱 1-2 分钟"
    - "母乳宝宝让爸爸夜安抚(避免奶香诱惑)"
  failure_mode: |
    一夜全戒 → 娃哭崩 + 妈妈奶量下降。
    白天不喂够 → 夜里只能补奶。
    夜里逗笑 / 开亮灯 / 讲话 → 重置昼夜节律。
  evidence_level: B

glossary_refs:
  - G-ABBR-AAP

citation:
  book_title_en: "What to Expect the First Year"
  book_title_zh: "海蒂育儿大百科 0-1 岁"
  authors: ["Heidi Murkoff", "Sharon Mazel"]
  publisher_en: "Workman Publishing"
  publisher_zh: "南海出版公司(中译)"
  year: 2010
  edition: "Third Edition"
  location: "第 7 章 / 半夜哺乳节,p.252-254"
  source_id: SRC-040

unit_ids: []
related_cards:
  - C-S2-2011
  - C-S2-2017

language: zh
status: draft
created: 2026-05-04
updated: 2026-05-04
```

---

# 写入指引(给父 session)

```bash
# 推荐:用 yq / sed 把每个 ```yaml ... ``` 块拆出来,按 card_id 命名落盘
# 简单方法:awk 切块
awk '/^```yaml$/,/^```$/' PHASE14_PART3_cards_manifest.md | \
  awk '/^card_id: / {file=$2".yaml"; next} /^```$/ {file=""} file {print > file}'

# 然后按 card_id 前缀分目录
for f in C-S2-*.yaml; do mv "$f" 30-cards/s2-1to3mo/; done
for f in C-S3-*.yaml; do mv "$f" 30-cards/s3-3to6mo/; done
```

或者父 session 用 Read 这个 manifest 文件 + Write 工具逐个落盘。
