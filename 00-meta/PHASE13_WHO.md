# Phase 13 任务书 · SRC-031 WHO + UNICEF Infant and Young Child Feeding Policy Compendium

> 完成日期:2026-05-04
> 项目:parenting-kb
> 完成状态:✅ 5 轮独立审 0 错全过

---

## 0. 一句话任务

抓 WHO + UNICEF 婴幼儿喂养政策合集(IYCF / BFHI / Code / Growth / CF / EBF / HIV / LAM / Lancet 2016 等),产 **57 张中文 v3.5 知识卡** + **34 张新术语**,**完成 4 国卫生指南闭环**(WHO 国际 + AAP 美 + 鲍秀兰 中 + 松田 日)。

---

## 1. 选定的源 + 来源

**SRC-031 — 多文档合集**:
- WHO IYCF Fact Sheet
- BFHI 10 Steps (2018 修订)
- International Code of Marketing 1981
- WHO Child Growth Standards 2006
- WHO Complementary Feeding 4 Pillars
- WHO ELENA Exclusive Breastfeeding
- WHO Q&A on Breastfeeding
- HIV and Infant Feeding (2010 ART era)
- Lancet 2016 Breastfeeding Series (Victora 主编)
- Lactational Amenorrhea Method (LAM)
- BFHI Wikipedia (实施现状)

**Tier 1** 国际公共卫生权威 — 文件路径:`10-sources/tier1-authoritative/notes/SRC-031.yaml`(政策性合集,非 tier3 书)。

---

## 2. 选这本作为 Phase 13 的理由

### 2.1 现库缺失维度填补
现库已有 AAP(SRC-006 美) + 鲍秀兰(SRC-009 中) + 松田(SRC-024 日)三国指南。**WHO 是唯一全球医学共识**(国际公共卫生政策),完成 4 国 1 国际闭环。

### 2.2 政策性独家维度
- **BFHI 10 步骤**:现库无任何来源讲产院实操标准 — 中国 6,000+ 爱婴医院实操差距独家维度
- **Code 1981 营销禁令**:现库无来源讲奶粉公司监管 — 中国奶粉品牌违规普遍是中国家长高频痛点
- **WHO Growth Standards 2006 母乳基线**:vs CDC 2000 配方基线 — 母乳娃别误判
- **持续母乳到 2 岁 'or beyond'**:WHO 是唯一明确推 ≥ 2 年的派
- **HIV+ 妈妈 2010 ART 时代**:现库唯一覆盖
- **Lancet 2016 系列**:Victora 主编,820k 生命硬数据

---

## 3. 卡片规范

完全继承 v3.5 schema(PHASE2_AAP §2.5-2.9):
- 全中文白话风格
- title ≤ 15 字 / hook 8-12 字 / what_to_do 每条 ≤ 35 字 / failure_mode ≤ 80 字
- glossary_refs ≥ 1 / related_cards ≥ 2(其中 ≥ 1 跨 SRC-031 之外)
- citation 必填(URL + accessed + source_id)

**ID 规则**:段 ID +100 buffer(单 session)
- S0:1024 / S1:1000 / S2:1044 / S3:1042 / S4:1045 / S5:1037 / S6:1064 / S7:1099 / S8:868

---

## 4. WebFetch 结果

| 文档 | URL | 状态 |
|---|---|---|
| D1 IYCF Fact Sheet | who.int/news-room/fact-sheets/detail/infant-and-young-child-feeding | ✓ |
| D2 BFHI 10 Steps | who.int/teams/.../ten-steps-to-successful-breastfeeding | ✓ |
| D3 Code (Wikipedia fallback) | en.wikipedia.org/.../International_Code... | ✓ |
| D4 BFHI Status (Wikipedia) | en.wikipedia.org/wiki/Baby_Friendly_Hospital_Initiative | ✓ |
| D5 Growth Standards | who.int/tools/child-growth-standards | ✓ partial |
| D6 Complementary Feeding | who.int/health-topics/complementary-feeding | ✓ |
| D7 ELENA EBF | who.int/tools/elena/interventions/exclusive-breastfeeding | ✓ partial |
| D8 BF Topic | who.int/health-topics/breastfeeding | ✓ |
| D9 HIV Feeding (Wikipedia) | en.wikipedia.org/wiki/Breastfeeding_and_HIV | ✓ |
| D10 Lancet 2016 (Wikipedia) | en.wikipedia.org/wiki/Breastfeeding | ✓ |
| D11 LAM (Wikipedia) | en.wikipedia.org/wiki/Lactational_amenorrhea | ✓ |
| D12 Q&A | who.int/news-room/questions-and-answers/item/breastfeeding | ✓ |
| Innocenti Declaration 1990+2005 | 多 URL 全失败 | ✗ gaps G_WHO_1 |
| Acceptable Medical Reasons 2009 | who.int/publications/.../WHO-NMH-NHD-09.01 | ✗ gaps G_WHO_2 |
| PAHO/WHO Guiding Principles 2003 | paho.org/.../principlescompfeeding.pdf | ✗ gaps G_WHO_3 |

---

## 5. 卡片清单(57 张)

详见 `30-cards/INDEX_BY_SOURCE.md` SRC-031 节。

按段分布:S0=5 / S1=18 / S2=5 / S3=3 / S4=11 / S5=4 / S6=7 / S7=3 / S8=1。

主战场:S1 新生儿(BFHI 10 步 + Code 4 大禁 + EBF 操作定义 + 中国产院差距)+ S4 6-9 月(辅食 4 大支柱 + Growth Standards + 6 月起含铁优先)+ S6 12-24 月(持续母乳到 2 岁 + 中国'早断'传统反对)。

---

## 6. 术语清单(34 张)

### G-ABBR(5 张)
- G-ABBR-WHO / G-ABBR-EBF / G-ABBR-CF / G-ABBR-IYCF / G-ABBR-BFHI

### G-TERM(25 张)
BFHI-10-steps / WHO-Code / WHO-six-months / WHO-two-years / Innocenti-Declaration / WHO-growth-standards / WHO-CF-principles / acceptable-medical-reasons / HIV-feeding / AFASS / formula-marketing / breastmilk-substitutes / Lancet-breastfeeding-series / LAM / NetCode / IBFAN / colostrum / skin-to-skin / rooming-in / early-initiation / nipple-confusion / mixed-feeding / responsive-feeding / relactation / galactagogue

### G-PERSON(4 张)
- G-PERSON-Victora(Cesar Victora,Lancet 2016 主编)
- G-PERSON-Horta(Bernardo Horta,IQ 元分析作者)
- G-PERSON-Dewey(Kathryn Dewey,UC Davis 营养学教授,PAHO/WHO Guiding Principles 主要作者)
- G-PERSON-Lutter(Chessa Lutter,PAHO 高级喂养专家)

---

## 7. 5 轮独立审框架(沿用 Phase 12)

```
轮 1 = Python 机器审 — title/hook/wtd/fm/glossary/related/cross-school
轮 2 = WHO 文档反向覆盖 — 12 个文档逐个 spot-check
轮 3 = 漏术语扫 — 34 期望术语 vs 现实
轮 4 = 用户三审 — hook 风格 + 跨派率 + 段分布
轮 5 = 深度审 — 跨文档独立卡 + evidence_level + 内部结构
```

5 轮全过 0 错(详见 checkpoint MD)。

---

## 8. 跨派对照硬指标

每张卡 ≥ 1 张 related 跨 SRC-031 之外(跨 AAP / 鲍 / 松田 / Karp / Brazelton / Lerner V1-V4 等)。

实际:**100% 跨派率**(57/57)+ 平均 3.70 related/卡 + 0 跨派孤岛 + 0 描述型 hook。

---

## 9. 工程纪律

- ID 隔离:SRC-031 + 段 ID +100 buffer ✓
- Tier 1 路径:`tier1-authoritative/notes/` ✓
- 索引文件 Edit 单点改不全文 Write ✓
- Python YAML 验证脚本必跑(每轮)✓
- 字数 + 学究词 + 跨派率 + hook 风格 4 个 Python 脚本必跑 ✓
- WebFetch 失败 → 记 gaps.md ✓

---

## 10. 完成定义(全部 ✓)

- [x] SRC-031.yaml(完整结构 + 跟现库 18+ 派跨派对照,Tier 1 路径)
- [x] 12/15 WHO 文档 WebFetch 成功 + 3 失败记 gaps
- [x] 所有 WHO 缩写建 G-TERM 术语(EBF / CF / BFHI / Code / Innocenti 等)
- [x] 所有经典学者建 G-PERSON 术语(Victora / Horta / Dewey / Lutter)
- [x] 5 轮独立审全过(0 错)
- [x] PHASE13_WHO.md 任务书(本文件)
- [x] checkpoint MD(初+二审 + 三+四+五轮审)
- [x] YAML 全部解析通过(57/57)
- [x] 0 跨派孤岛卡(100% 跨派率)
- [x] hook 全部抓眼句(0 描述型)
- [x] glossary_refs / related_cards 全部存在
- [x] source_index.yaml + INDEX_BY_SOURCE.md + progress.md 全部 Edit 单点更新
- [x] conflicts.md K 节整理
- [x] gaps.md 记 WebFetch 失败的文档

---

*v1.0 — 2026-05-04 Phase 13 完成 — WHO + UNICEF SRC-031(57 卡 + 34 术语);完成 4 国卫生指南完整闭环 ⭐⭐⭐*
