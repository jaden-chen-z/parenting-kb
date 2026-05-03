# Checkpoint · Phase 3 Bowlby Vol 1 自审补丁(2026-05-03)

> 项目:parenting-kb · Phase 3 第三本 · Bowlby《依恋三部曲 · 第一卷:依恋》
> 主 checkpoint:`checkpoint_PHASE3_BOWLBY_VOL1_20260502.md`
> 本文件:**自审后补丁记录**(2026-05-03 同 session 完成)

---

## 0. 一句话总结

按用户要求做完整自审 → 发现 4 维度 7 处问题 → 补 5 张卡 + 4 处修订 → **总计 37 知识卡 + 7 术语卡**(原 35+4 → 37+7)。

---

## 1. 自审发现(4 维度)

### 维度 1:卡片结构 ✅ 合格

- ✅ 必填字段全部完整(0 处缺失)
- ✅ YAML 全部解析通过(45/45 — 含本次修订)
- ✅ Glossary refs 全部指向存在的术语卡
- ✅ Cross-card refs 全部指向存在的知识卡

### 维度 2:遗漏的知识点(3 处)

| 漏点 | 处理 |
|---|---|
| 过渡性客体 / 拥抱玩偶 | ✅ 已补 [C-S5-076](../../30-cards/s5-9to12mo/C-S5-076.yaml) |
| 气质 vs 依恋(反宿命论) | ✅ 已补 [C-S4-074](../../30-cards/s4-6to9mo/C-S4-074.yaml) |
| D 混乱型独立卡 | ✅ 已补 [G-TERM-disorganized-attachment](../../40-glossary/G-TERM-disorganized-attachment.yaml) |

### 维度 3:遗漏的术语卡(4 处)

| 缺卡 | 处理 |
|---|---|
| G-PERSON-Spitz(八月焦虑提出者) | ✅ 已补 [G-PERSON-Spitz](../../40-glossary/G-PERSON-Spitz.yaml) |
| G-PERSON-Harlow(恒河猴依恋经典) | ✅ 已补 [G-PERSON-Harlow](../../40-glossary/G-PERSON-Harlow.yaml) |
| G-TERM-Moro-reflex(C-S1-126 直接用) | ✅ Brazelton session 已建([G-TERM-Moro-reflex](../../40-glossary/G-TERM-Moro-reflex.yaml)),复用,更新 C-S1-126 引用 |
| G-TERM-disorganized-attachment(D 型) | ✅ 已补(同上) |

### 维度 4:内容质量(4 处学究词)

| 卡 | 修订 |
|---|---|
| [C-S1-124](../../30-cards/s1-newborn/C-S1-124.yaml) | "终止条件" → "目的" / "行为系统" → "本能反应" / "目标校正系统" → "自动定位妈妈"|
| [C-S1-127](../../30-cards/s1-newborn/C-S1-127.yaml) | "操作性消退" → "宝宝渐渐不爱笑了(因为没人捧场,笑就消退)" |
| [C-S2-068](../../30-cards/s2-1to3mo/C-S2-068.yaml) | "本体觉/触觉" → "触觉/动作感觉" / "新皮层控制" → "新皮层(理性脑)开始工作"|
| [C-S5-074](../../30-cards/s5-9to12mo/C-S5-074.yaml) | "内化进人格" → "变成性格本身" |

---

## 2. 补丁后产出清单

### 2.1 新增知识卡(2 张)

| ID | 标题 | 等级 | 段 |
|---|---|---|---|
| [C-S4-074](../../30-cards/s4-6to9mo/C-S4-074.yaml) | 气质难带 ≠ 依恋差(philosophy) | B | S4 |
| [C-S5-076](../../30-cards/s5-9to12mo/C-S5-076.yaml) | 抱毯子玩偶不是怪癖(过渡性客体) | B | S5 |

### 2.2 新增术语卡(3 张,本 session)

| ID | 类型 | 来源 |
|---|---|---|
| [G-PERSON-Spitz](../../40-glossary/G-PERSON-Spitz.yaml) | 人物 | 八月焦虑 + 依附性抑郁 + 孤儿院研究 |
| [G-PERSON-Harlow](../../40-glossary/G-PERSON-Harlow.yaml) | 人物 | 恒河猴绒布妈妈实验 + 反 Freud 次级驱力 |
| [G-TERM-disorganized-attachment](../../40-glossary/G-TERM-disorganized-attachment.yaml) | 术语 | D 混乱型(Main & Solomon 1990) |

### 2.3 复用已建术语卡(1 张)

- [G-TERM-Moro-reflex](../../40-glossary/G-TERM-Moro-reflex.yaml)(Brazelton session 2026-05-02 建,我加 C-S1-126 引用)

### 2.4 引用更新(5 张原卡)

- C-S1-122:加 G-PERSON-Harlow
- C-S1-126:加 G-PERSON-Harlow + G-TERM-Moro-reflex
- C-S2-070:加 G-PERSON-Harlow
- C-S4-068:加 G-PERSON-Spitz
- C-S6-070:加 G-TERM-disorganized-attachment

### 2.5 学究词修订(4 张原卡)

- C-S1-124, C-S1-127, C-S2-068, C-S5-074

---

## 3. 最终段分布(本次 session 总产出)

| 段 | 月龄 | 卡数 | 卡 ID 范围 |
|---|---|---|---|
| S1 | 0-1 月 | 7 | C-S1-122..128 |
| S2 | 1-3 月 | 5 | C-S2-067..071 |
| S3 | 3-6 月 | 4 | C-S3-076..079 |
| S4 | 6-9 月 | **8**(+1) | C-S4-067..074 |
| S5 | 9-12 月 | **8**(+1) | C-S5-069..076 |
| S6 | 12-24 月 | 5 | C-S6-068..072 |
| **合计** | | **37 张** | |

术语卡:**7 张**(原 4 + 新 3,Brazelton 已建的 Moro 复用)

---

## 4. ID 隔离最终验证

Brazelton 在我审计期间继续推进:
- S4: 022(我开始时 021,审计期间又 +1)
- S5: 027(我开始时 024)

我的最高 ID:S4=074, S5=076,**buffer 余量 ~50 张**,完全安全。

---

## 5. 跨源对照增强

### 新增对照点(本次补卡贡献)

| 主题 | Bowlby | 已有源 |
|---|---|---|
| 过渡性客体(玩偶毯子) | C-S5-076 | (Karp/AAP 未单独讨论) |
| 气质 vs 依恋反宿命论 | C-S4-074 | 鲍秀兰 G-PERSON-Bao 隐含 |
| 喂养≠依恋的 Harlow 实证 | C-S2-070 + G-PERSON-Harlow | (其他源都隐含,Bowlby + Harlow 是源头) |

---

## 6. 用户验收建议(更新版)

按补丁后,推荐抽审 5 张:
- [C-S2-070](../../30-cards/s2-1to3mo/C-S2-070.yaml)(喂奶≠依恋,A 级,中国家长高频痛点)
- [C-S4-074](../../30-cards/s4-6to9mo/C-S4-074.yaml)(**新增** — 气质难带 ≠ 依恋差)
- [C-S5-071](../../30-cards/s5-9to12mo/C-S5-071.yaml)(B 安全型)
- [C-S5-076](../../30-cards/s5-9to12mo/C-S5-076.yaml)(**新增** — 抱毯子玩偶不是怪癖)
- [C-S6-072](../../30-cards/s6-12to24mo/C-S6-072.yaml)(管教方式 → 观点采择)

---

## 7. 已知未做(留给后续)

| 待办 | 优先级 |
|---|---|
| 用户审核 Bowlby 37 张卡 | 高 |
| 合并 source_index.yaml + INDEX_BY_SOURCE.md(等 Brazelton 收尾) | 高 |
| Phase 4 启动:Bowlby Vol 2《分离》 | 中 |
| 补 G-PERSON-Wolff/Schaffer/Yarrow 等研究者卡 | 低(可选) |
| 修订过长 why_matters(8 张超 290 字) | 低(用户已允许字数无上限) |

---

*本文件 = Phase 3 第三本(Bowlby Vol 1)自审 + 补丁完整记录*
*主 checkpoint 在 checkpoint_PHASE3_BOWLBY_VOL1_20260502.md*
