# Phase 10 · Shonkoff《From Neurons to Neighborhoods》— 早期发展神经科学综述

> 项目代号:parenting-kb · Phase 10(2026-05-04)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读**(按顺序):
> 1. 本文件(PHASE10_SHONKOFF.md)
> 2. `00-meta/checkpoints/checkpoint_PHASE10_SHONKOFF_20260504.md`(初+二审)
> 3. `00-meta/checkpoints/checkpoint_PHASE10_SHONKOFF_AUDIT_20260504.md`(三+四+五审)
> 4. `00-meta/checkpoints/checkpoint_PHASE9_MATSUDA_AUDIT_20260503.md`(用户三审框架基础)
> 5. `00-meta/PHASE7_STERN.md`(模仿 SRC 结构 — A 级 72%)
> 6. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)
> 7. `10-sources/tier3-books/notes/SRC-025.yaml`(完整 chapter map + 跨派对照)

---

## 0. 一句话任务

抓 Shonkoff/Phillips《From Neurons to Neighborhoods》(NRC/IOM 2000,Tier 2 综述权威),
产 **60 张 v3.5 中文卡** + **22 张关联术语**(18 张新建 + 4 张补建),
**填补"早期发展神经科学" + "公共政策" 维度**,跟现库 17 个 SRC(15 派)跨派对照率 100%。
A 级 92%(NRC 综述权威决定主体 A 级)+ 5 轮独立审 0 错。

---

## 1. 选定的书 + 来源

**Jack P. Shonkoff & Deborah A. Phillips (Editors)《From Neurons to Neighborhoods: The Science of Early Childhood Development》**(NRC/IOM 2000)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/shonkoff_neurons_neighborhoods.md`(1.78MB,40241 行,PDF→md OCR) |
| 编者 | **Jack P. Shonkoff**(Brandeis Heller Graduate School 教授 + 后期 Harvard Center on the Developing Child 创办人)+ **Deborah A. Phillips**(Georgetown 心理学教授 + NICHD ECCS 主持) |
| 委员会 | NRC + IOM 17 人多学科委员会(儿科 / 心理 / 神经科学 / 经济 / 政策),4 年综述工作 |
| 流派 | **Tier 2 NRC 综述权威 / 早期发展科学 / 政策学** |
| 范围 | 0-6 岁完整 + 政策视角 |
| 出版 | 2000 National Academy Press(Washington D.C.) |
| ISBN_en | 0-309-06988-2 |
| 中译本 | 无(中文圈 NRC 综述无系统中译) |

### 为什么这本(Phase 10 选择)

1. **填补"早期发展神经科学维度"** — 现库 15 派本无 Tier 2 综述权威派
2. **跟 Gopnik 单本 vs Shonkoff 17 人委员会综述** — 综述权威更高 + 政策影响更大
3. **Heckman 经济学 + 早期干预 RCT 数据** — Perry / Abecedarian / Head Start
4. **公共政策视角** — 中国家长缺这视角(NRC 是美国国家级 + 联合国引用)
5. **OCR 已就位**(40241 行 / 1.78MB,PDF 转 .md,无 OCR 错字)

### 关键校准(任务书预期 vs 实际书内容)

| 预期 | 实际 |
|---|---|
| Heckman 经济学曲线 | **不在 2000 年本书** — 是 Shonkoff 2006+ Center for the Developing Child 后续工作 |
| Toxic stress 框架 | **不在 2000 年本书** — 是 Shonkoff 2006+ 后续工作 |
| Serve-and-return 概念 | **不在 2000 年本书** — 是 Shonkoff 2006+ 后续工作 |
| Hart-Risley 30M words | **本书有** ✓(Ch 6 引用) |
| Sensitive vs critical period | **本书有** ✓(Ch 8 区分) |
| Self-regulation 主轴 | **本书有** ✓(Ch 5 整章) |
| Perry / Abecedarian RCT | **本书有** ✓(Ch 13 综述) |

预期产出 50-80 张实际产 60 张 — 中位偏低,因为 Heckman/toxic stress 后续概念不在本书,
但本书神经科学 + Hart-Risley + RCT 数据极硬,A 级 92% 远超 Stern A 级 72%。

---

## 2. 段定义(本次产出)

| 段 | 月龄 | 文件夹 | 本次产卡 | ID 起点(实测 max + 100 buffer)|
|---|---|---|---|---|
| S0 | 孕期 / 哲学 | s0-pregnancy | 4 张(C-S0-619..622) | 519 + 100 = 619 |
| S1 | 0-1 月 | s1-newborn | 6 张(C-S1-864..869) | 764 + 100 = 864 |
| S2 | 1-3 月 | s2-1to3mo | 6 张(C-S2-802..807) | 702 + 100 = 802 |
| S3 | 3-6 月 | s3-3to6mo | 6 张(C-S3-805..810) | 705 + 100 = 805 |
| S4 | 6-9 月 | s4-6to9mo | 5 张(C-S4-804..808) | 704 + 100 = 804 |
| S5 | 9-12 月 | s5-9to12mo | 6 张(C-S5-903..908) | 803 + 100 = 903 |
| S6 | 12-24 月 | s6-12to24mo | 10 张(C-S6-926..935) | 826 + 100 = 926 |
| S7 | 24-36 月 | s7-24to36mo | 7 张(C-S7-861..867) | 761 + 100 = 861 |
| S8 | 3-6 岁 | s8-3to6yr | 10 张(C-S8-207..216) | 107 + 100 = 207 |
| **总计** | | | **60 张** | |

S6(主战场)+ S8(早期干预 RCT 主战场)各 10 张 — Shonkoff NRC 综述的两大重点章节。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3-9 扩展。

### 评级 evidence_level(本书标尺)

NRC 综述 17 人委员会 + 多学科共识 + Tier 2 权威:
- **A**:NRC 综述 + 跨派一致 + 实证扎实(主体 60-70%)— Tier 2 NRC 委员会权威决定
- **B**:NRC 综述 + 跨派部分张力 + RCT 证据有限(20-30%)
- **C**:NRC 政策推断 + 委员会立场 + 实证薄弱(罕见)

实测产出(60 张终版):**A=55 / B=5 / C=0** 张 — A 级 92%(高于 Stern A 级 72%),
反映 NRC 综述权威 + 17 人共识 + 多学科背书的高级别证据。

---

## 4. 工作流(基于 Phase 9 用户深度审教训改进)

### 4.1 章节地图(SRC-025.yaml 已记录,实测 14 章)

```python
ch1_introduction: 75718              # Ch 1 Introduction
ch2_nature_nurture: 136421           # Ch 2 Rethinking Nature and Nurture
ch3_culture: 189859                  # Ch 3 Challenge of Studying Culture
ch4_causal_connections: 229583       # Ch 4 Making Causal Connections
ch5_self_regulation: 293489          # Ch 5 Acquiring Self-Regulation ⭐
ch6_communicating_learning: 392979   # Ch 6 Communicating and Learning ⭐
ch7_friends_peers: 517911            # Ch 7 Making Friends + Getting Along with Peers
ch8_developing_brain: 577274         # Ch 8 The Developing Brain ⭐⭐⭐
ch9_nurturing_relationships: 702440  # Ch 9 Nurturing Relationships ⭐⭐
ch10_family_resources: 837271        # Ch 10 Family Resources
ch11_child_care: 924669              # Ch 11 Growing Up in Child Care ⭐⭐
ch12_neighborhood: 1015538           # Ch 12 Neighborhood and Community
ch13_intervention: 1041544           # Ch 13 Intervention ⭐⭐⭐
ch14_conclusions: 1180086            # Ch 14 Conclusions and Recommendations
total_chars: 1780478
```

### 4.2 章节覆盖实际(Round 2 反向覆盖审计)

| Ch | 主题 | 卡数 | 覆盖度 |
|---|---|---|---|
| 1 | Introduction | 1 | 概念引入 |
| 2 | Nature/Nurture | 1 | 立场总览 |
| 3 | Culture | 0 | 间接覆盖(C-S6-935 中国娃多内疚) |
| 4 | Causal | 0 | 方法论,跳过 |
| **5** | **Self-Regulation** | **20** | 主战场(C-S1-864/865, S2-802/803, S5-906, S6-928 等) |
| **6** | **Communicating** | **9** | 主战场(parentese / joint-att / 30M words / 词汇爆炸) |
| 7 | Friends/Peers | 1 | 同伴互动概念(C-S4-808) |
| **8** | **Developing Brain** | **8** | 主战场(plasticity / sensitive period / Hubel-Wiesel / Greenough-Black) |
| **9** | **Nurturing Relationships** | **9** | 主战场(attachment / quality / 父亲角色) |
| 10 | Family Resources | 2 | 部分覆盖(贫困 / 母亲就业) |
| 11 | Child Care | 1 | quality 立场(C-S6-933) |
| 12 | Neighborhood | 0 | 间接覆盖(C-S8-211 贫困应激) |
| **13** | **Intervention** | **6** | 主战场(Perry / Abecedarian / Head Start / Fade-out / 3 要素) |
| 14 | Conclusions | 2 | 总结(NRC 6 原则 / 5 句话给中国家长) |

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-025 entry + next_src_id → SRC-026)✅
│   └── tier3-books/notes/
│       └── SRC-025.yaml ✅(完整 chapter map + 跨 12 派对照)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-025 节 + 总数 +60 = 833)
│   ├── s0-pregnancy/      # C-S0-619..622 ✅(4)
│   ├── s1-newborn/        # C-S1-864..869 ✅(6)
│   ├── s2-1to3mo/         # C-S2-802..807 ✅(6)
│   ├── s3-3to6mo/         # C-S3-805..810 ✅(6)
│   ├── s4-6to9mo/         # C-S4-804..808 ✅(5)
│   ├── s5-9to12mo/        # C-S5-903..908 ✅(6)
│   ├── s6-12to24mo/       # C-S6-926..935 ✅(10)— 主战场
│   ├── s7-24to36mo/       # C-S7-861..867 ✅(7)
│   └── s8-3to6yr/         # C-S8-207..216 ✅(10)— 主战场
├── 40-glossary/(22 张:18 新 + 4 补)
│   ├── G-PERSON-Shonkoff.yaml ✅
│   ├── G-PERSON-Phillips.yaml ✅
│   ├── G-PERSON-Hart-Risley.yaml ✅
│   ├── G-PERSON-Kagan.yaml ✅
│   ├── G-TERM-NRC.yaml ✅
│   ├── G-TERM-experience-expectant.yaml ✅
│   ├── G-TERM-experience-dependent.yaml ✅
│   ├── G-TERM-nature-nurture.yaml ✅
│   ├── G-TERM-30-million-words.yaml ✅
│   ├── G-TERM-cortisol.yaml ✅
│   ├── G-TERM-HPA-axis.yaml ✅
│   ├── G-TERM-executive-function.yaml ✅
│   ├── G-TERM-prefrontal-cortex.yaml ✅
│   ├── G-TERM-perry-preschool.yaml ✅
│   ├── G-TERM-abecedarian.yaml ✅
│   ├── G-TERM-self-regulation.yaml ✅
│   ├── G-TERM-biobehavioral-shift.yaml ✅
│   ├── G-TERM-empathy.yaml ✅
│   ├── G-TERM-self-efficacy.yaml ✅(Round 1 补)
│   ├── G-TERM-maternal-sensitivity.yaml ✅(Round 1 补)
│   ├── G-TERM-attention-regulation.yaml ✅(Round 1 补)
│   └── G-TERM-scaffolding.yaml ✅(Round 1 补)
└── 00-meta/
    ├── progress.md ✅(更新累计 + Phase 10 完成记录)
    ├── conflicts.md ✅(新增 E1-E5 节,5 项 Shonkoff 立场对照)
    ├── PHASE10_SHONKOFF.md ✅(本文件)
    └── checkpoints/
        ├── checkpoint_PHASE10_SHONKOFF_20260504.md ✅(初+二审)
        └── checkpoint_PHASE10_SHONKOFF_AUDIT_20260504.md ✅(三+四+五审)
```

---

## 6. 完成定义(实测)

- [x] 抓 Shonkoff《From Neurons to Neighborhoods》全本(14 章)→ SRC-025.yaml 完整 chapter map
- [x] 产 **60 张新卡**(任务范围 50-80 ✓)
- [x] 新建 **22 张关联术语**(18 新 + 4 补建,任务范围 12-18 → 实际 22)
- [x] 5 轮独立审计完成(Python 机器 + 反向覆盖 + 漏术语 + 用户三审 + 用户深度审)
- [x] checkpoint MD 完成(2 个:初+二审 + 三+四+五审)
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml + memory + conflicts.md**(全 Edit 单点改)
- [x] 跨派 related_cards 标连(Shonkoff ↔ 12 派全覆盖)
- [x] 全部 60 张卡 YAML 验证通过(0 fail)
- [x] 全部 glossary_refs 指向存在的术语卡(0 missing)
- [x] 全部 related_cards 指向存在的知识卡(0 broken / 0 self-ref)
- [x] **严格审查:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 fm 单行 >80**
- [x] **跨派对照率 100%**(60/60 至少 1 张 related 跨 12 派) — 远超 70% 目标
- [x] **平均 3.3 张 related/卡** — 远高于松田 SRC-024 的 1.4

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 773 张知识卡 + 233 张术语卡**(Phase 9 末状态)
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - Shonkoff vs Gopnik(NRC 综述 vs 单本实证)→ E1
   - Shonkoff vs Lillard(综述 vs 蒙氏哲学)→ E2
   - Shonkoff vs 松田(NRC 完全反体罚 vs 松田瞬间打手)→ E3
   - Shonkoff vs Lansbury(系统化早期干预 vs RIE 不打扰)→ E4
   - Shonkoff vs 商业早教(6 派一致反对)→ E5
4. ✅ **白话风格**(避免学究腔)— 学究词全改白话(突触 → 脑回路 / 皮质醇 → 应激激素 / 海马 → 脑里的记忆区 等)
5. ✅ **跨派主动标连**(60 张卡平均 3.3 个跨派 related_cards)
6. ✅ **段 ID +100 buffer 单 session 隔离生效**(无并行)

---

## 8. 工程纪律(继承 + 新)

- 文件 .md 已 OCR(1.78MB,40241 行,PDF→md,极少 OCR 错字)
- 主上下文 Python offset 切片读取(每次 15-30K)
- 反向审计每章必做
- YAML 验证:Chinese curly quotes 在 double-quote string 中需要 single-quote 包裹(Phase 10 踩坑 1 处,在 SRC-025 修复)
- 字段含中文 `"` 必须用 `'..."..."'` 单引号包裹
- **本次特别**:NRC 综述大书 + 跨学科 + 政策视角 — 选择性聚焦核心命题,跳过 Ch 4(方法论) + Ch 12(社区,内容偏宏观)

---

## 9. 立场对照(本次产出实测,详见 conflicts.md E1-E5)

### 9.1 Shonkoff vs Gopnik(神经科学综述 vs 实证认知派)

NRC 综述偏 sensitive period 立场,Gopnik 偏 critical period 立场。
**核心校准**:critical 只少数(感官缺陷)+ sensitive 多数(语言/依恋/情感调节)。
卡片:C-S0-620 / C-S5-907

### 9.2 Shonkoff vs Lillard 蒙氏(综述 vs 哲学派)

NRC 综述给 6 大原则,蒙氏给 prepared environment 哲学结构。
**互补不矛盾**。中国家长可同时用蒙氏哲学 + NRC 校准。
卡片:C-S0-622 / C-S6-186 等

### 9.3 Shonkoff vs 松田 体罚立场

NRC 完全反体罚(cortisol 累计伤 PFC) vs 松田部分支持瞬间打手。
NRC 立场跟 4 派(AAP/Lansbury/Bowlby/Brazelton)共识 — 立场更强。
卡片:C-S6-932(本卷)+ C-S8-100(松田)

### 9.4 Shonkoff vs Lansbury(系统化早期干预 vs 不打扰)

NRC 给系统化早期干预(Perry/Abecedarian)— 针对**高风险家庭**。
RIE 给不打扰立场 — 针对**普通家庭**。
**这不矛盾** — 干预对象不同。
卡片:C-S8-207-210 + C-S8-215

### 9.5 Shonkoff vs 商业早教(6 派一致反)

NRC + Gopnik + 松田 + Lansbury + Gerber + Lillard / Davies 蒙氏 = **6 派一致反商业早教**,
只有鲍秀兰部分支持。极强立场。
卡片:C-S0-619 / C-S3-808 / C-S7-866 / C-S8-216

### 9.6 Shonkoff vs 中文文化常见误解

| 中文常见误解 | NRC 数据反驳 | 卡片 ID |
|---|---|---|
| "0-3 错过就完了" | 多数是 sensitive 不是 critical | C-S0-620 / C-S5-907 |
| "他还小什么都不懂" | 出生 42 分钟就模仿 | C-S1-869 |
| "教 / 训练 / 早学才是早教" | 反早教 4 定理 + Perry/Abecedarian 玩为主 | C-S0-619 / C-S8-207 |
| "全职妈是金标准" | 看回应质量不看身份 | C-S6-933 / C-S8-212 |
| "他不听话 — 该打" | PFC 还在长 + 完全反体罚 | C-S6-928 / C-S6-932 |
| "提前学拼音赢起跑线" | 学龄前 5 项 ≠ 提前学业 | C-S7-866 / C-S8-213 |
| "毛绒玩具是娇气" | transitional object 是健康外延 | C-S7-867 |
| "妈妈抑郁孩子小不影响" | cortisol + 右前额 EEG 永久痕迹 | C-S2-806 / C-S3-809 |

---

## 10. 改进建议(给后续 Phase 11 接手)

1. **Pikler《Friedliche Babys》原典德译版** — RIE 师承,跟 Lansbury / Gerber 完整闭环
2. **Mary Ainsworth《Patterns of Attachment》(1978)** — 陌生情境法原典(SRC-023 fallback 错过)
3. **Heinz Kohut《The Restoration of the Self》(1977)** — Self psychology 完整版,跟 Stern 互补
4. **Heidi Murkoff《What to Expect the First Year》中译** — 全球销量第一,百科式
5. **WHO Infant and Young Child Feeding Guideline** — 国际 Tier 1 循证
6. **Shonkoff 后续工作** — 2006+ Center for the Developing Child:toxic stress / serve-and-return 单独立 SRC-026

---

## 11. 跟 Phase 9 教训对比

| Phase 9 教训 | Phase 10 应对 |
|---|---|
| YAML 引号嵌套陷阱 | ✅ Chinese curly quotes 在 double-quote 中需 single-quote 包裹(SRC-025 1 处)|
| hook 字数 8-12 严格 | ✅ Python 扫 + 修 13 处(7-9 字偏多)|
| title ≤ 15 严格 | ✅ Python 扫 + 0 错(NRC 概念可中文短)|
| 学究词主动改 | ✅ 神经科学词全改白话("突触修剪" → "脑回路精简" / "皮质醇" → "应激激素")|
| 反向覆盖审计每章 + 收官 | ✅ 14 章实测 11 章覆盖,Ch3/4/12 间接覆盖 |
| 跨派关联手动 | ✅ 主动标连 60 张卡(平均 3.3 个跨派)|
| **新教训:NRC 章节内容跨段 — 单段 ID 不够** | ✅ 跨段卡(eg HPA 轴跟所有段都相关)放最相关段 |
| **新教训:章节内容深 — 选择性聚焦不全覆盖** | ✅ Ch 4(方法论) + Ch 12(宏观社区)选择性跳过 |
| **新教训:NRC 综述权威决定 A 级 92%** | ✅ A 级远超 Stern 72% / 松田 33%,本身书的权威决定不是 over-rate |

---

## 12. 工程意外(Phase 10 特有)

### 意外 1:Heckman/toxic stress/serve-and-return 不在 2000 年本书
- 主因:这些是 Shonkoff 2006+ Center for the Developing Child 后续工作
- 修复:重新校准任务书 — 聚焦实际书内容(plasticity / sensitive periods / Hart-Risley / RCT)
- **教训**:任务书预测命题 vs 实际书内容 — 必须先扫书再细化预测

### 意外 2:YAML curly quotes 解析错误
- 主因:`"早期发展科学"` 中文双引号 在 double-quote string 中导致 YAML parser confused
- 修复:改用 single-quote 包裹 + block scalar `|`
- **教训**:中文标点在 YAML 中需谨慎 — 优先用 block scalar

### 意外 3:hooks 字数批量偏低(7 字)
- 主因:NRC 概念较抽象 — 第一遍写多用短词
- 修复:Python 扫描 + 批量改为 8-12 字
- **教训**:写 hook 时直接保 8-12 字 — 别等审才改

### 意外 4:related_cards 引用了不存在的 ID(C-S0-019 / C-S6-202 等)
- 主因:写卡时凭印象写 ID 而非查实
- 修复:Python 扫 + 批量替换为存在 ID
- **教训**:关键 cross-ref 必须 ls 验证存在 — Phase 7 也踩过

### 意外 5:S8 段 6 张卡全无跨派 related(早期干预 RCT 是 Shonkoff 独家领域)
- 主因:Perry / Abecedarian RCT 数据本就 Shonkoff 独家,自然内卷
- 修复:每张加 1 张跨派 related(松田 / Bowlby / Lillard)
- **教训**:跨派对照硬指标 100% 是要努力达到 — 不是自动满足

---

## 13. 5 轮审教训(给 Phase 11)

继承 Phase 9 用户深度审 + 本卷新增:

```
轮 1 = Python 机器审(YAML/字数/refs/cross-source)
   - 实测发现 9 missing glossary refs + 20 broken related card refs + 11 cards no cross-source
轮 2 = 反向覆盖审(章节 spot-check)
   - 实测覆盖 14 章中的 11 章,Ch3/4/12 间接覆盖
轮 3 = 漏术语扫
   - 实测 0 missing(因 Round 1 已修)
轮 4 = 用户三审 3 维度(hook 风格 + 跨派率 + 章节)
   - 实测 1 描述型 hook(C-S2-803)— 修
轮 5 = 用户深度审(跨章重复主题 + 漏专业术语 + 内部结构)
   - 实测 0 错(因前 4 轮已发现并修)
```

### 关键洞察

1. **Round 1 应主导** — 机器审能 catch 大部分问题(字数/refs/yaml)
2. **跨派对照率 100% 不是自动** — 需要主动标连
3. **broken refs 是高频错** — 写卡时凭印象写 ID 错误率高
4. **章节 spot-check 应用 location 字段而非主观判断** — 自动化更可靠

---

*v1.0 · 2026-05-04 — Phase 10 Shonkoff 早期发展神经科学综述完整记录*
*60 张卡 + 22 关联术语,A 级 92% / 跨派 100% / 5 轮审 0 错*
*NRC 综述 17 人委员会权威 + 政策视角 + 神经科学+ 早期干预 RCT 全填补*
*Phase 11 候选:Pikler 师承原典 / Ainsworth Strange Situation / Kohut Self psychology / 海蒂育儿大百科 / WHO 喂养指南 / Shonkoff 2006+ 后续工作*
