# Phase 8 并行第二本 · Magda Gerber RIE 派创始人原典

> 项目代号:parenting-kb · Phase 8 并行第二本(2026-05-03)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读**(按顺序):
> 1. 本文件(PHASE8_GERBER.md)
> 2. `00-meta/checkpoints/checkpoint_PHASE8_GERBER_20260503.md`(本卷产出)
> 3. `00-meta/checkpoints/checkpoint_PHASE8_GERBER_AUDIT_20260503.md`(4 轮独立审 + 漏知识反向覆盖)
> 4. `00-meta/PHASE7_LANSBURY.md`(Lansbury 是本卷推广人,姐妹篇)
> 5. `00-meta/checkpoints/checkpoint_PHASE7_LANSBURY_USER_AUDIT_20260503.md`(用户三审框架)
> 6. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)

---

## 0. 一句话任务

抓 Magda Gerber + Allison Johnson《Your Self-Confident Baby》(John Wiley & Sons, 1998)— RIE 派创始人 1998 原典。
产 **32 张 v3.5 中文 RIE 派创始人卡** + **6 张新术语卡 + 1 张已存在加引用**。
**RIE 派谱系闭环完成**:Pikler(师承)→ Magda Gerber(创始人 SRC-021)→ Janet Lansbury(推广人 SRC-019)。

---

## 1. 选定的书 + 来源

**Magda Gerber & Allison Johnson《Your Self-Confident Baby: How to Encourage Your Child's Natural Abilities — From the Very Start》**

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/gerber_self_confident_baby.md`(488KB,PDF 转 .md) |
| 作者 | Magda Gerber(1910-2007 RIE 创始人,匈牙利裔美国教育家)+ Allison Johnson(合著者) |
| 流派 | Tier 3 / RIE(Resources for Infant Educarers)/ Educaring 哲学 |
| 范围 | 0-24 月(Ch8 末"RIE Doesn't End at Two"延伸到 36 月) |
| 出版 | 原版 1998 英文,John Wiley & Sons |
| ISBN_en | 978-0-471-23104-0 |
| 中译本 | 待考(部分 RIE 教师在国内自译片段) |

### 为什么这本(Phase 8 并行第二本选择)

1. **OCR 已就位** — Lansbury 卷里已确认 `gerber_self_confident_baby.md` 在 raw_pdfs/(488K 字符)
2. **RIE 派闭环** — Lansbury(SRC-019,推广人)+ Magda(SRC-021,创始人)+ Pikler(术语 G-PERSON-Pikler,师承)→ RIE 派完整谱系
3. **8 大原则原版** — Lansbury 在 2014 扩展到 10,本卷给原始 7(实际 1998 列 7 条,而非传说的 8)+ Magda 第一人称(更原汁原味)
4. **Magda 独家章节** — Beverly 案例 / Antaeus tantrum / Red/Yellow/Green / Cause/Consequence / Wants smt-nothing QT — Lansbury 没系统讲
5. **跟 Shonkoff(SRC-020 并行)完全不冲突** — Shonkoff 是综合科学/政策(Tier 1 综述),Gerber 是 RIE 派实操(Tier 3 流派)→ ID 隔离 + 段 ID +200 buffer

---

## 2. 段定义(本次产出实测)

| 段 | 月龄 | 文件夹 | 本次产卡 | ID 起点 |
|---|---|---|---|---|
| S0 | 孕期 | s0-pregnancy | 2 张(C-S0-316..317) | 316(实际 max=116 + 200) |
| S1 | 0-1 月 | s1-newborn | 5 张(C-S1-555..559) | 555(实际 max=355 + 200) |
| S2 | 1-3 月 | s2-1to3mo | 4 张(C-S2-493..496) | 493(实际 max=293 + 200) |
| S3 | 3-6 月 | s3-3to6mo | 3 张(C-S3-499..501) | 499(实际 max=299 + 200) |
| S4 | 6-9 月 | s4-6to9mo | 3 张(C-S4-498..500) | 498(实际 max=298 + 200) |
| S5 | 9-12 月 | s5-9to12mo | 4 张(C-S5-594..597) | 594(实际 max=394 + 200) |
| S6 | 12-24 月 | s6-12to24mo | **8 张**(C-S6-607..614) | 607(实际 max=407 + 200) |
| S7 | 24-36 月 | s7-24to36mo | 3 张(C-S7-552..554) | 552(实际 max=352 + 200) |
| **总计** | | | **32 张**(初版 30 + 漏知识反向覆盖补 2) | |

S6 是本卷最强段(Ch8 占 141K 字符,= 全书 30%),Magda 大部分独家命题(Antaeus / Red-Yellow-Green / Cause-Consequence / 反 Time-out / Lasting Discipline / No 是分离 / Words Give Power)在此。

**ID 隔离策略**(2 session 并行):**+200 buffer**(Shonkoff 用 +50 buffer 起点,我必须更高 buffer 避撞)。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3/4/5/6/7 扩展 + **Phase 7 Lansbury 用户三审教训**。

### 评级 evidence_level(本书标尺)

Magda RIE 1998 立场 = Magda 50+ 年实战(1948 起匈牙利)+ Pikler 师承 + DIP 1972 Stanford + 千+ RIE 班级:
- **A**:与 Tier 1 共识对齐(Magda 跟蒙氏 + Bowlby + AAP + Pikler 临床吻合)
- **B**:Magda 引用 RIE 60+ 年观察 + Pikler 1945 Loczy + DIP 1972 Palo Alto + 自家案例 + 千+ 班级
- **C**:Magda 个人推断(罕见)

实测产出:**A=23(72%) / B=9(28%) / C=0** — A 级 72% **高于 Lansbury 49%**,反映 Magda 跟蒙氏 + Pikler + Bowlby 高度对齐。

---

## 4. 工作流(基于 Phase 7 Lansbury 用户三审教训改进)

### 4.1 章节地图(SRC-021.yaml 已记录)

Magda 8 章传统结构(vs Lansbury 30 章博客合集):
- Ch1 Respect: Key(7 大原则原版,15K)
- Ch2 Birth of RIE(Pikler/Loczy 1945 + DIP 1972,16K)
- Ch3 Newborn Baby(S1 0-1 月巨大段,65K)
- Ch4 Newborn Parents(S0 准父母,23K)
- Ch5 First Months(S2-S4 1-9 月最大段,92K)
- Ch6 Selecting Child Care(选托班,33K — 美国家长场景,本卷不建卡)
- Ch7 Becomes Mobile(S5 9-12 月,77K)
- Ch8 Budding Toddler(S6/S7 12-36 月最大段,141K)

### 4.2 chunk 策略

每章 15-141K 字符,Python `text[start:end]` 切片读取。Ch8(141K)是全书 30%,需多次切片读完。

### 4.3 反向覆盖审计(Phase E 轮 2 实测)

每段产卡完成后,主上下文从原文重列"父母从 RIE 视角必须知道的 N 件事",对比已写卡补漏。

实测漏知识补 **2 张**:
- C-S5-597:Magda 帮宝宝睡的中间路(Ch5 §Help Your Baby Form the Sleeping Habit)— Magda 1998 立场比 Lansbury 2014 更细,引 Ferber method + RIE 元素
- C-S6-614:Words give power 替打咬人(Ch8 §Why It's Important to Talk Feelings)— 中国家长 1.5-2 岁打人/咬人高频痛点

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-021 entry,next_src_id 留 SRC-020 给 Shonkoff session)✅
│   └── tier3-books/notes/
│       └── SRC-021.yaml ✅(新建)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-021 节 + 顶部目录表)
│   ├── s0-pregnancy/      # C-S0-316..317 ✅(2)
│   ├── s1-newborn/        # C-S1-555..559 ✅(5)
│   ├── s2-1to3mo/         # C-S2-493..496 ✅(4)
│   ├── s3-3to6mo/         # C-S3-499..501 ✅(3)
│   ├── s4-6to9mo/         # C-S4-498..500 ✅(3)
│   ├── s5-9to12mo/        # C-S5-594..597 ✅(4,含漏知识补 1)
│   ├── s6-12to24mo/       # C-S6-607..614 ✅(8,含漏知识补 1)
│   └── s7-24to36mo/       # C-S7-552..554 ✅(3)
├── 40-glossary/(6 张新 + 1 张加引用)
│   ├── G-PERSON-Johnson.yaml ✅(新)
│   ├── G-TERM-tantrum-antaeus.yaml ✅(新)⭐
│   ├── G-TERM-red-yellow-green-light.yaml ✅(新)⭐
│   ├── G-TERM-wants-something-quality-time.yaml ✅(新)⭐
│   ├── G-TERM-cause-consequence.yaml ✅(新)
│   ├── G-TERM-selective-intervention.yaml ✅(新)
│   └── G-TERM-educaring.yaml ✅(已被 Shonkoff session 创建,Edit 加 SRC-021/SRC-019 source 引用)
└── 00-meta/
    ├── progress.md ✅(更新 Phase 8 + 累计 633 张)
    ├── PHASE8_GERBER.md ✅(本文件)
    └── checkpoints/
        ├── checkpoint_PHASE8_GERBER_20260503.md ✅(初+二审产出)
        └── checkpoint_PHASE8_GERBER_AUDIT_20260503.md ✅(4 轮独立审 + 漏知识反向覆盖)
```

---

## 6. 完成定义(实测)

- [x] 抓 Magda《Your Self-Confident Baby》全本(8 章,488K)→ SRC-021.yaml + raw .md 已就位
- [x] 产 **32 张新卡**(任务范围 25-32 ✓)
- [x] 新建 **6 张新术语卡 + 1 张加引用**(任务范围 5-7 ✓)
- [x] 漏知识反向覆盖补 2 张(C-S5-597 帮宝宝睡 + C-S6-614 Words give power)
- [x] checkpoint MD 完成(初+二审产出 + 4 轮独立审)
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(用 Edit 单点改避并行覆盖)
- [x] 跨源 related_cards 标连(RIE ↔ Lansbury ↔ Davies ↔ Lillard ↔ Bowlby ↔ Pikler)
- [x] 全部 32 张卡 YAML 验证通过(Python yaml.safe_load)
- [x] 全部 glossary_refs 指向存在的术语卡
- [x] 全部 related_cards 指向存在的知识卡(0 自引用 / 0 占位符)
- [x] **严格审查**:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 学究词残留
- [x] **跨源率 100%**(0 跨源孤岛卡)
- [x] **Lansbury related 100%**(目标 ≥ 50%,创始人 ↔ 推广人对照硬指标)
- [x] **hook 全部抓眼句**(0 描述型,修 2 处:C-S2-493 + C-S6-608)
- [x] **章节 spot-check**(逐章不跳过,补 2 张高价值漏)

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 8 第二本通过。

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 601 张卡 + Shonkoff(SRC-020)并行 session**:ID 隔离 +200 buffer 严格执行
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - Magda vs Lansbury:1998 原典 vs 2014 推广扩展(80%+ 一致)
   - Magda vs Sears 派"亲密育儿":反 → 婴儿不是 helpless,需独立空间(Geralynn 3 周起 30 分钟独玩)
   - Magda vs CIO:反 → 但 1998 引 Ferber method(渐进自我安抚 + 父母先告知合作)
   - Magda vs 主流分散派:反 → 哭是语言,绝不"哄停"
   - Magda vs 高脚椅文化:反 → 小桌小凳哲学(prison vs 自主)
4. ✅ **白话风格**(避免学究腔)— 修 7 处学究词(认知 / 内化 / 机制 / 人格 / 维度)
5. ✅ **跨源主动标连**(32 张卡平均 3.00 个 related_cards,跨源率 100%,Lansbury related 100%)

---

## 8. 工程纪律(并行 Shonkoff session 特别注意)

- 文件 .md 已 OCR(488K,8 章 PDF 转 markdown)
- 主上下文 Python offset 切片读取
- 反向审计每段必做 — 实测补 2 张
- YAML 验证:**`-` 开头条目含 `"` 必须转中文 「」**(否则 YAML parser 误解为 quoted scalar)— 实测 6 张需修
- **本次特别(2 session 并行)**:
  - SRC-021(我)+ SRC-020(Shonkoff,并行 session 进行中)
  - 段 ID +200 buffer(避撞 Shonkoff +50 buffer)
  - **索引文件 Edit 单点改不全文 Write**(否则覆盖 Shonkoff session 更新)
  - **G-TERM-educaring 已被 Shonkoff session 创建** → 用 Edit 加 SRC-021/SRC-019 source 不覆盖
  - **next_src_id 留 SRC-020 给 Shonkoff session**(我 SRC-021 已占用,Shonkoff 完成时改 next_src_id → SRC-022)

---

## 9. 立场对照(本次产出实测)

### 9.1 Magda vs Lansbury(创始人 ↔ 推广人)

跟 Lansbury 60% 重叠(本卷不重建):
- yes space / sportscasting(Magda 命名)/ wait magic word / 不撑坐 / 真物 / 真声音 / Tell first / 哭是语言 / 承认情绪 / 不修复 / 限度温柔 / 不替宝宝做 / 不强迫分享 / 不 train potty / 反 time-out / 反打骂

Magda 独家 40%(本卷必建):
- **7 大基本原则原版**(Ch1)— Lansbury 后扩到 10
- **Wants something / Wants nothing QT**(Ch3)⭐ 二分概念
- **想象巨人国类比**(Ch3)— Tell first 哲学的形象解释
- **7 类设备系统反对**(Ch3)— slings/swings/walkers/bouncers/pacifiers/baby talk/playpen + "zombied out"
- **Spoiled 4 真因**(Ch3)— 重新定义"宠坏 = 应对力被损坏"
- **Magda 8 父母品质矛盾对子**(Ch4)— 全是中道
- **Doula 概念**(Ch4)— 照顾妈妈才能照顾宝宝
- **Selective Intervention 三层级**(Ch2 DIP 1972 命名)
- **6000 次尿布数字**(Ch3 Quality Time)
- **印第安谚语 Tell me/Show me/Involve me**(Ch3)
- **Try a Table & Chair**(Ch7)— 替高脚椅,Magda 标志立场
- **RIE 班香蕉仪式**(Ch7)— 班级实操经典
- **Antaeus tantrum 故事**(Ch8)⭐⭐⭐ 希腊神话比喻
- **Red/Yellow/Green 三灯限度**(Ch8)⭐⭐⭐ Magda 独家命名
- **Cause/Consequence 自然后果**(Ch8)— 替惩罚
- **Lasting Discipline 长在心里**(Ch8 Freud 框架)— 内化哲学(Magda 1998 用 Freud 解释)
- **Beverly 高需求宝宝案例**(Ch2)— DIP 奠基故事(6 月哭闹 → 木板姿 → DIP 学独立)
- **Words Give Power**(Ch8)— 替打咬人的语言哲学
- **Magda 帮宝宝睡中间路**(Ch5)— 1998 立场:不训练但帮形成,引 Ferber method

### 9.2 Magda vs Pikler(学生 ↔ 老师)

Magda 1956 移民美国前在匈牙利师从 Pikler 多年。本卷 Ch2 + Ch5 大量 Pikler 引用(45 次)。
- 自然大动作发展(Pikler 派核心,Magda 全本贯彻)
- 不撑坐 / 不学步车 / 不强教(Pikler-Magda 一致)
- "Hands constitute infant's first connection"(Pikler 引,Magda Ch3 经典段)
- 1945 Loczy 实验(Magda 助 Pikler 训练 infant nurses)
- "Practice makes the master"(德语谚语,Magda 引 Pikler)

### 9.3 Magda vs 中文文化常见误解

| 中文常见误解 | Magda RIE 反驳 | 卡片 ID |
|---|---|---|
| "宝宝小不懂事什么都不会" | 反:出生起当人对待,真声音不娃娃语 | C-S1-556 |
| "硬塞最后一口" | 反:小份 + 信宝宝 + 不强迫(Magda 1998 班级实操)| C-S4-498 |
| "哭就抱+转移" | 反:Listen,不"分散"。哭是语言不是问题 | C-S1-557 |
| "高脚椅看世界" | 反:Magda 派小桌小凳,小人视角 = 尊重 | C-S3-500 |
| "打了就长记性" | 反:打孩子学到打人是 OK 的(模范效应)| C-S6-610 |
| "如厕训练 3 天速成" | 反:98% 4 岁前自学会,强迫制造创伤 | C-S7-552 |
| "扑地哭就是熊" | 反:Antaeus 故事 — 找大地补能,你别打扰 | C-S6-607 |
| "抱多了惯坏" | 反:Magda 重定义"宠坏" = 应对力被损坏(4 真因)| C-S1-559 |
| "不许说不没礼貌" | 反:1-2 岁说不是分离任务,大多数忽略就好 | C-S6-613 |
| "你需要不算需要" | 反:Red/Yellow/Green 三灯,你的需要也算 | C-S6-608 |
| "陪玩才是 quality time" | 反:Wants smt/nothing 二分,日常护理就是 QT | C-S1-555 |
| "我必须永远耐心" | 反:Magda 8 品质都是矛盾对子,做真实不演完美 | C-S0-316 |

---

## 10. 改进建议(给后续 Phase 9 接手)

1. **Pikler《Friedliche Babys》** — Magda 师承原典(1940 德文初版 / 1969 修订)— OCR 已就位 `pikler_friedliche_babys.md`
2. **Ainsworth《Patterns of Attachment》(1978)** — Strange Situation 实证 + 依恋四角(跟 Bowlby + Stern 形成依恋研究三角)
3. **松田道雄《育儿百科》** — OCR 已就位 `matsuda_childcare_encyclopedia.md`,1970s 日本经典(中文家长熟悉)
4. **Brazelton《Touchpoints 3-6》** — 现库 0-3 已有(SRC-010),3-6 续集
5. **WHO Infant Feeding Guideline** — Tier 1 国际公卫
6. **Kohut《How Does Analysis Cure?》** — self psychology 教父(Stern 师承)— 学术性强不推荐
7. **海蒂育儿大百科** — 大众西方主流参考,跟 AAP 重叠

---

## 11. 跟 Phase 7 Lansbury 教训对比

| Phase 7 Lansbury 教训 | Phase 8 Gerber 应对 |
|---|---|
| 内部质量 + 漏知识 + 漏术语 + 用户三审 4 轮独立审 | ✅ 全部跑完,补 2 张漏知识卡 |
| 4 轮独立 spot-check 维度不同(YAML / 反向覆盖 / 术语扫 / 用户三审) | ✅ 维度独立 |
| 漏知识审跟"已建 G-TERM"对照 | ✅ 扫"建了术语没建知识卡"+ 反向 |
| 中国家长高频痛点优先 | ✅ Magda 独家(Antaeus / 三灯 / 自然后果 / Words give power)全建 |
| 并行 session ID 隔离实测 | ✅ +200 buffer 起点,实测 ls 实际占用 |
| 术语数实测 ls | ✅ ls 211 实测(我加 6 新 + 1 加引用 = 总 211 + 6 = 217?— 视 Shonkoff session 实际加多少而定) |
| YAML 引号嵌套陷阱 | ✅ 中文「」替外层 `"`,实测修 6 处 |
| hook 字数 8-12 严格 | ✅ Python 扫 + 修 8 处(7 字 + 13-18 字混合) |
| title ≤ 15 严格 | ✅ Python 扫 0 错 |
| 学究词主动改 | ✅ Python 扫 + 修 7 处(认知 / 内化 / 机制 / 人格 / 维度) |
| 反向覆盖审计每段 + 收官 | ✅ 收官前补 2 张高价值漏卡(Magda sleep + Words give power) |
| 跨源关联手动 | ✅ 32 张卡平均 3.00 个 related,**跨源率 100% + Lansbury related 100%**(目标 ≥ 50% 远超) |
| 章节扫描列全清单 | ✅ 8 章全部 offset 确认 |
| hook 描述型陷阱 | ✅ 修 2 处:C-S2-493(原"心法不是规则清单"含"清单")+ C-S6-608(原"Magda 给的限度坐标系"含"系统/坐标系") |

---

## 12. 工程意外(Phase 8 并行第二本特有)

### 意外 1:2 session 并行 ID 协调
- 启动时 next_src_id = SRC-020(Shonkoff session 还未写)
- **修复**:本卷用 SRC-021 + 不动 next_src_id(让 Shonkoff session 完成时改 → SRC-022)
- **教训**:多 session 并行时不抢同一行(next_src_id 是单行,先写覆盖后者)

### 意外 2:G-TERM-educaring 已被并行 session 创建
- 我以为新建,Write 时报错"已存在"
- 检查 sources: 引用了 SRC-020(Shonkoff session 也建了)
- **修复**:Edit 单点改加 SRC-021 + SRC-019 到 sources(不覆盖,不重写)
- **教训**:并行 session 可能预创建你的术语,Write 前先 ls

### 意外 3:段 ID +200 buffer
- 实际段 max(s0=116 / s1=355 / s2=293 / s3=299 / s4=298 / s5=394 / s6=407 / s7=352)
- 加 200 起:s0=316 / s1=555 / s2=493 / s3=499 / s4=498 / s5=594 / s6=607 / s7=552
- **避开**Shonkoff Phase 8 第一本可能用的 +50 buffer 范围
- 跟 Phase 7 Lansbury 的 +100 buffer 比,本次更保守(2 session 并行风险更大)

### 意外 4:YAML 引号嵌套陷阱(继承 Phase 7)
- 6 处 `- "..."`(中文 `-` 开头条目以英文 `"` 开始)被 YAML parser 当作 quoted scalar
- **修复**:全部改成 `- 「...」`(中文引号),保留可读性 + YAML 安全
- **教训**:中文 `-` 开头条目里有英文术语必须用中文引号,不用英文引号

### 意外 5:hook 字数集中 7 字符(继承 Lansbury / Lillard)
- 8 处 hook 是 7 字(刚好不到 8 字)
- **修复**:Python 批量扫 + Edit 全改 8-12 字
- **教训**:写卡时主动检查 8-12 字 — 7 字符是 Lansbury / Lillard / Gerber 共通陷阱

### 意外 6:学究词残留 7 处
- 认知(2)/ 内化(3)/ 机制(2)/ 人格(1)/ 维度(0)
- **修复后**:0 残留
  - 认知 → 心智 / 懂事
  - 内化 → 长在心里 / 变规矩 / 记心里
  - 机制 → 反应 / 能力
  - 人格 → 性格

### 意外 7:hook 描述型陷阱(继承 Lansbury 用户三审)
- 2 处描述型 hook(含"清单" / "坐标系")
- **修复**:
  - C-S2-493:"心法不是规则清单" → "记 7 条不如懂尊重"
  - C-S6-608:"Magda 给的限度坐标系" → "你的需要也算需要"
- **教训**:hook 必须抓眼,不能描述自己讲的是什么内容

### 意外 8:Magda 7 大原则 vs 文献中的 8/10
- 文献(包括 Lansbury 引用)说 Magda 8 大原则
- Ch1 §Basic Principles 实际只列 7 个(Basic trust / Environment / Uninterrupted Play / Freedom / Active Participant / Observation / Consistency)
- **修复**:卡 + SRC-021 元数据都用 7 大原则原版,标注"Lansbury 后扩展为 10"
- **教训**:不照搬二手文献描述,直接看原文

---

## 13. 未做(留给后续)

| 待办 | 优先级 | 备注 |
|---|---|---|
| 用户审核 32 张卡 | 高 | 推荐 5 张样本(下文) |
| Shonkoff(SRC-020)session 完工后合并 | 中 | 等他们完成时统一更新 source_index 末尾 + INDEX_BY_SOURCE 总数 |
| 补 G-PERSON-Maslow / G-PERSON-Erikson(Magda 引)| 低 | 仅 1-2 卡引用,价值不高 |
| Phase 9 启动(Pikler / Ainsworth 推荐)| 中 | Pikler 是 Magda 师承,本卷大量引用(45 次)|

---

## 14. 用户操作建议

### 推荐审 5 张样本卡(中国家长高频痛点 + Magda 独家)

1. **[C-S6-607 Antaeus 故事:接地起](../30-cards/s6-12to24mo/C-S6-607.yaml)** ⭐⭐⭐ A 级 + Magda 希腊神话比喻 + 替"打骂止哭" — **最独家**
2. **[C-S6-608 红黄绿三灯设限度](../30-cards/s6-12to24mo/C-S6-608.yaml)** ⭐⭐⭐ A 级 + Magda 独家命名 + **"你的需要也算"**(中国密集母职痛点)
3. **[C-S6-614 语言给娃武器替打咬](../30-cards/s6-12to24mo/C-S6-614.yaml)** ⭐⭐ A 级 + 1.5-2 岁打人 / 咬人解药 + 漏知识反向覆盖补
4. **[C-S5-597 Magda 帮宝宝睡的中间路](../30-cards/s5-9to12mo/C-S5-597.yaml)** ⭐⭐ A 级 + Magda 1998 立场 + 漏知识反向覆盖补 + 引 Ferber 但加 RIE 元素
5. **[C-S1-555 想要 vs 不想要 两类陪](../30-cards/s1-newborn/C-S1-555.yaml)** ⭐ A 级 + Magda 独家 QT 二分 + 替"陪玩才是 QT"主流派

### 决定
- Phase 8 并行第二本通过 / 调整 / 重做?
- Phase 9 候选:Pikler 师承原典 / Ainsworth Strange Situation / 松田道雄 / Brazelton 3-6?

---

*v1.0 · 2026-05-03 — Phase 8 Magda Gerber RIE 派创始人 1998 原典完整记录*
*基于 Phase 7 Lansbury 用户三审教训 + 2 session 并行 ID 隔离学到*
*RIE 派完整谱系闭环(Pikler 师承 → Magda 创始人 → Lansbury 推广人),准备 Phase 9 Pikler / Ainsworth / 松田道雄 拓展*
