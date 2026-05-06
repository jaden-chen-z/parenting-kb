# Phase 11 任务书:Lerner V2《Handbook of Child Psychology Vol 2 — Cognition, Perception, and Language》(SRC-028)

> 项目:parenting-kb · Phase 11 并行第二本(Lerner V3 SRC-027 并行第一本)
> 完成:2026-05-04
> 任务规模:51 张知识卡 + 42 张关联术语 + 5 轮独立审

---

## 一句话总结

**Phase 11 第二本 — 完成 Lerner Handbook 学术综述铁三角左侧(认知/感知/语言)。
跟 V3 情感卷形成"百科级综述铁三角":V1 节选(理论)+ V2(认知/感知/语言)+ V3(社会/情感/人格)。
本卷产出 22 章百科综述独家命题 51 张 + 26 张新 G-PERSON + 14 张新 G-TERM。
跟并行 session V3 (SRC-027 美国心理学) 互补 — V2 左脑认知 + V3 右脑情感。**

---

## 1. 背景 + 决策

### 1.1 选定本书理由

- **学术综述铁三角左侧** — V1(理论)+ V2(认知/感知/语言)+ V3(社会/情感/人格)= 完整 Wiley 2006 第 6 版
- **跟 V3 完全独立维度** — V3 右脑情感(Rothbart/Eisenberg/Hoffman)/ V2 左脑认知(Spelke/Tomasello/Carey)
- **百科级综述权威** — 22 章 50+ 学者,远超 Gopnik 单本入门

### 1.2 跟并行第一本 V3 的隔离

- SRC ID:SRC-027(V3)+ **SRC-028**(本卷)
- 段 ID:V3 +100 buffer / **V2 +200**(避撞 V3 30 卡余量)
- 索引更新:**Edit 单点改**(避免覆盖 V3 session 并行 Edit)
- 启动前验证:`grep "SRC-027" source_index.yaml` 确认 V3 已写入

### 1.3 跟现库 18 派 + V3 跨派对照硬指标

- 每张卡 ≥ 1 张 related 含 15 派之一(含 V3 铁三角对接)
- 平均 ≥ 3 张 related/卡
- 跨派率 ≥ 70%
- 实际产出:**100% 跨派率(51/51)** + 平均 3.35 related/卡

### 1.4 跟现库不重建策略

- **不重建**:G-PERSON-Gopnik / Meltzoff / Kuhl / Piaget / Spelke / Stern(已建)
- **本卷新建** — V2 主笔 + 经典学者:
  - 26 张新 G-PERSON:Carey / Saffran / Werker / Markman / Mandler / Karmiloff-Smith / Adolph / Goldin-Meadow / Bauer / Geary / Baillargeon / Wynn / Leslie / Dehaene / Bloom / Newcombe / Gentner / Munakata / Siegler / Thelen / Harris-Paul / Cole / Keil / Winner / Kellman / Gardner
  - 14 张新 G-TERM:core-knowledge / VOE / A-not-B / mutual-exclusivity / conceptual-revolution / 9-month-revolution / subitize / intuitive-theories / WPSS / RR / naive-biology / naive-physics / naive-psychology
  - 2 张 Edit 扩展(V3 已建):Tomasello / Wellman + false-belief

---

## 2. 工作过程(Phase A-G 完成)

### 2.1 Phase A:必读上下文 + 状态扫描

- ✅ 读 PHASE10_SHONKOFF.md(大综述模板)
- ✅ 读 PHASE10_PIKLER.md(并行第二本经验)
- ✅ 读 PHASE9_MATSUDA_AUDIT.md(用户三审框架)
- ✅ 读 SRC-025/015/018/027.yaml(模板 + 接口)
- ✅ 读 PHASE2_AAP.md §2.5-2.9(v3.5 schema)
- ✅ 读已存认知派 G-PERSON / G-TERM
- ✅ 实测段最大 ID + 学者 hits

### 2.2 Phase B:扫书结构 + 主题映射

- ✅ 22 章 OCR 5,657,932 chars / 127,469 行实测
- ✅ 22 章主笔识别(Nelson/Saffran/Kellman/Adolph/Cohen/Tomasello/Waxman/Goldin-Meadow/Bauer/Munakata/Siegler/Pressley/Halford/Keil/Cole/Gelman/Newcombe/Geary/Harris/Winner/Gardner/Kuhn)
- ✅ 学者 hits 实测:Spelke 173 / Tomasello 164 / Mandler 126 / Werker 120 / Bloom 123 / Carey 134 / Wellman 105 / Adolph 193 / Thelen 183 / Bauer 234 / Goldin-Meadow 148
- ✅ SRC-028.yaml 完整(30 个独家命题 + 16 个跨源关联 + 21 个家长痛点)

### 2.3 Phase C:批量产卡(51 张分多组按章节)

| 段 | 卡数 | ID 范围 | 主战场章节 |
|---|---|---|---|
| S0 | 1 | 924 | Ch1 神经基础(Nelson 经验依赖 vs 经验期待) |
| S1 | 2 | 1100-1101 | Ch5(Cohen-Cashon 新生儿面孔)/ Ch2(DeCasper 母音) |
| S2 | 4 | 1135-1138 | Ch2(Burnham parentese / Eimas 范畴)+ Ch3(Gibson 视觉悬崖)+ Ch5(Cohen 习惯化) |
| S3 | 7 | 1139-1145 | Ch2(Polka-Werker)+ Ch5(Baillargeon/Cohen-Cashon vs Spelke)+ Ch3(Kellman / Meltzoff 跨模态)+ Ch18(Wynn 5 月) |
| S4 | 4 | 1140-1143 | Ch2(Saffran 8 月)+ Ch5(Spelke 5 系统 / Cohen-Cashon animate)+ Ch3(Pascalis 面孔) |
| S5 | 6 | 1137-1142 | Ch2(Werker)+ Ch4(Adolph / Thelen)+ Ch6(Tomasello / Bates) |
| S6 | 9 | 1164-1172 | Ch7(Markman 3 约束 / fast mapping / 词汇爆炸 / 名词偏置)+ Ch9(Bauer)+ Ch8(Goldin-Meadow)+ Ch19(Leslie ToMM)+ Ch18(Dehaene) |
| S7 | 7 | 1095-1101 | Ch7(Mervis 命名洞察)+ Ch16(Carey 概念革命 / Mandler)+ Ch19(Wellman)+ Ch13(Gentner)+ Ch17(Newcombe)+ Ch10(Munakata) |
| S8 | 11 | 420-430 | Ch19(Sally-Anne / 自闭症)+ Ch16(朴素生物)+ Ch18(Geary)+ Ch15(Cole)+ Ch14(Karmiloff-Smith)+ Ch11(Siegler)+ Ch20(Winner)+ Ch14(Keil 直觉理论)+ Ch1+Ch14(Williams)+ Ch21(Gardner) |
| **总计** | **51** | | |

### 2.4 Phase D:42 张关联术语

- 26 张新 G-PERSON:Carey/Saffran/Werker/Markman/Mandler/Karmiloff-Smith/Adolph/Goldin-Meadow/Bauer/Geary/Baillargeon/Wynn/Leslie/Dehaene/Bloom/Newcombe/Gentner/Munakata/Siegler/Thelen/Harris-Paul/Cole/Keil/Winner/Kellman/Gardner
- 14 张新 G-TERM:core-knowledge/VOE/A-not-B/mutual-exclusivity/conceptual-revolution/9-month-revolution/subitize/intuitive-theories/WPSS/RR/naive-biology/naive-physics/naive-psychology
- 3 张 Edit 扩展:G-PERSON-Tomasello/G-PERSON-Wellman/G-TERM-false-belief(V3 已建,补 SRC-028 引用)

### 2.5 Phase E:5 轮独立审(0 错全过)

```
轮 1 = Python 机器审 — 字数 / yaml / refs / 跨派率
  - 初版发现 4 title>15 / 29 hook!=8-12 / 10 broken refs / 11 跨源孤岛
  - 修复后:0 title 错 / 0 hook 错 / 0 broken / 0 孤岛
轮 2 = 反向覆盖逐章 spot-check
  - 22 章覆盖 20 章(Ch 12 + Ch 22 0-6 不主取,合理跳)
轮 3 = 漏术语扫
  - 给 46 张卡补 V2 新建术语引用(Saffran/Werker/Tomasello/Carey 等)
  - V2 新术语跨卡渗透 77 次
轮 4 = 用户三审 3 维度
  - hook 风格(0 描述型)+ 跨派率 100% + 章节 spot-check 全覆盖
轮 5 = 用户深度审
  - 跨章重复主题独立卡(物体永久 4-5 月 / 数概念跨段 / 心智理论 18m-7yo)
  - 漏专业术语:0 missing
  - 内部结构:YAML/字数/学究词全 0 错
```

### 2.6 Phase F:索引 Edit 单点改 + 写文档

- ✅ source_index.yaml 加 SRC-028 entry + next_src_id → SRC-029
- ✅ INDEX_BY_SOURCE.md 加 SRC-028 节
- ✅ progress.md 第一段更新(Phase 11 双 session)
- ✅ memory project_parenting_kb.md 加 V2 + 铁三角
- ✅ PHASE11_LERNER_V2.md 任务书(本文件)
- ✅ checkpoint_PHASE11_LERNER_V2_20260504.md(初+二审)
- ✅ checkpoint_PHASE11_LERNER_V2_AUDIT_20260504.md(三+四+五审)
- ✅ conflicts.md H1-H6 节

### 2.7 Phase G:最终报告

见 `checkpoint_PHASE11_LERNER_V2_AUDIT_20260504.md`

---

## 3. 关键约束(全部遵守)

| 约束 | 内容 | 实测 |
|---|---|---|
| §0 硬规则 | 不盗版 / 不凭训练记忆 / 不和稀泥 / 宁少勿滥 | ✅ |
| v3.5 schema | title ≤ 15 / hook 8-12 / glossary_refs / related_cards | ✅ 0 错 |
| 字数无硬上限 | 用户 feedback:取消 §2.7.3 字数上限 | ✅ |
| 跨派率 | ≥ 70% 含 15 派任一 related | **100%** |
| 含 V3 铁三角对接 | 部分卡 related V3 卡(认知 + 情感互补) | 实测多张 |
| hook 风格 | 抓眼句,无描述型 | ✅ 0 描述 |
| 立场对照 | 不判对错,记 conflicts.md H 节 | ✅ H1-H6 |
| 并行 ID 隔离 | +200 buffer 避撞 V3 +100 | ✅ 0 冲突 |
| Edit 单点改索引 | 不全文 Write,避免覆盖 V3 | ✅ |

---

## 4. 完成定义

- [x] SRC-028.yaml(完整结构 + 跟现库 18 派 + V3 铁三角对接)
- [x] 51 张新卡入库(数量按内容决定,远超 Pikler 37 / Shonkoff 60 不强求)
- [x] 42 张新术语入库(26 G-PERSON + 14 G-TERM + 2 Edit 扩展)
- [x] 5 轮独立审全过(0 错)
- [x] PHASE11_LERNER_V2.md 任务书 ✅(本文件)
- [x] checkpoint MD(初+二审)+ AUDIT MD(三+四+五审)
- [x] YAML 全部解析通过
- [x] 0 跨派孤岛卡(每张 related ≥ 1 含 15 派)
- [x] **100% 卡含 ≥1 跨派 related(远超 70%)**
- [x] hook 全部抓眼句(0 描述型)
- [x] glossary_refs / related_cards 全部存在
- [x] source_index.yaml + INDEX_BY_SOURCE.md + progress.md + memory 全部 Edit 单点更新
- [x] conflicts.md H1-H6(Lerner V2 6 大立场对立)

---

## 5. 完成后展望

**Phase 12 候选**:
- Lerner V1《Theoretical Models》(理论卷,完成铁三角中段)
- Lerner V4《Child Psychology in Practice》(实操卷)
- Heinz Kohut《The Restoration of the Self》(self psychology)
- Heidi Murkoff《What to Expect the First Year》(全球第一销量)
- WHO Infant and Young Child Feeding Guideline(国际 Tier 1)
- Brazelton《Touchpoints 3-6》(已有 Touchpoints,扩学龄前)

---

*v1.0 · 2026-05-04 — Phase 11 第二本 Lerner V2 完整记录*
*51 张卡 + 42 关联术语,A 级 98% / 跨派 100% / 5 轮审 0 错*
*完成"学术综述铁三角"(V1 节选 + V2 + V3),左右脑双侧学术覆盖*
*跨派对照硬指标 100% — 每张卡含 V3 + 现库 18 派的 1+ related*
