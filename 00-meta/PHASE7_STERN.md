# Phase 7 · Stern《婴儿的人际世界》— Self 心理学奠基

> 项目代号:parenting-kb · Phase 7(2026-05-03)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读**(按顺序):
> 1. 本文件(PHASE7_STERN.md)
> 2. `00-meta/checkpoints/checkpoint_PHASE6_LILLARD_AUDIT_20260503.md`(三审教训)
> 3. `00-meta/PHASE6_LILLARD.md`(模仿其结构)
> 4. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)
> 5. `00-meta/PHASE1_KARP.md` §10(14 条实战教训)
> 6. `00-meta/checkpoints/checkpoint_PHASE7_STERN_20260503.md`(本卷初+二审)
> 7. `00-meta/checkpoints/checkpoint_PHASE7_STERN_AUDIT_20260503.md`(三审产出)

---

## 0. 一句话任务

抓 Daniel N. Stern《The Interpersonal World of the Infant》(1985 Basic Books,self 心理学奠基),产 **43 张 v3.5 中文卡** + **14 张术语卡**(并行 session 41 张初版 + 我 R2 补 2 张 + 还原 still-face 术语)。**Self 4 阶段框架 + Affective attunement** 双轨完成,跟 Bowlby(关系)+ 蒙氏 Lillard(哲学)三角互补。

---

## 1. 选定的书 + 来源

**Daniel N. Stern《The Interpersonal World of the Infant: A View from Psychoanalysis and Developmental Psychology》**(1985,2000 Updated Edition)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/stern_interpersonal_world.md`(756KB,.epub 转 .md) |
| 作者 | **Daniel N. Stern**(1934-2012)— 瑞士裔美国精神分析师 + 发展心理学家,日内瓦大学 / Cornell Med 教授,**self 心理学教父** |
| 流派 | Tier 3 / 精神分析 + 发展心理学 / **self 框架** |
| 范围 | 0-3 岁完整(Stern 4 阶段自我感) |
| 出版 | 原版 1985 英文,Basic Books(纽约),Updated Edition 2000 |
| ISBN_en | 978-0-465-09559-9 |
| 中译本 | 有(《婴儿的人际世界:精神分析与发展心理学的视野》华东师大 2017) |

### 为什么这本(Phase 7 选择)

1. **Self 心理学奠基** — 跟 Bowlby(关系) + 蒙氏(哲学) 三足鼎立,本卷给"心理过程"
2. **Affective attunement(情感调谐)** — Stern 独家发现,中国家长高频痛点
3. **Vitality affects(活力情感)** — 大人喜怒哀乐之外的"动态质地",最适合婴儿期
4. **反 Mahler 共生融合论** — 中文文化"宝宝跟妈一体"迷思的反驳
5. **OCR 已就位**(.epub 转 .md,无 OCR 错字)

---

## 2. 段定义(本次产出)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S0 | 孕期 / 哲学 | s0-pregnancy | 4 张(C-S0-015..018) |
| S1 | 0-1 月 | s1-newborn | 5 张(C-S1-253..257) |
| S2 | 1-3 月 | s2-1to3mo | 4 张(C-S2-191..194) |
| S3 | 3-6 月 | s3-3to6mo | 5 张(C-S3-196..200) |
| S4 | 6-9 月 | s4-6to9mo | 7 张(C-S4-196..202)— +1 R2 补 |
| S5 | 9-12 月 | s5-9to12mo | 9 张(C-S5-291..299)— Stern 最强 + R2 补 still-face |
| S6 | 12-24 月 | s6-12to24mo | 5 张(C-S6-296..300) |
| S7 | 24-36 月 | s7-24to36mo | 4 张(C-S7-248..251) |
| **总计** | | | **43 张**(R2 补 C-S4-202 过度/不足刺激 + C-S5-299 still-face) |

S4 + S5 共 14 张是 Stern 最强 — 主观自我 + affective attunement 部分,跟蒙氏 + Bowlby 直接对话。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3/4/5/6 扩展。

### 评级 evidence_level(本书标尺)

Stern 学术深度 + 1970-80 年代实验数据 + 临床观察:
- **A**:与 Tier 1 共识对齐(Stern 跟 Bowlby / 现代神经科学一致处)+ Stern 实证强
- **B**:Stern 引用研究 + 临床观察 + 跨派一致
- **C**:Stern 个人精神分析推断(罕见)

实测产出(43 张终版):**A=31 / B=12 / C=0** 张 — A 级 72%(高于 Lillard 35%),反映 Stern 实证扎实 + 跟 Bowlby/Lillard/Karp/Wonder Weeks 跨派一致。

---

## 4. 工作流(基于 Phase 6 三审教训改进)

### 4.1 章节地图(SRC-018.yaml 已记录)

Stern 756KB / 11 章 / OCR 单长行 .md 文件:

```python
ch1_questions_background: 10953        # Questions and Their Background (4 senses overview)
ch2_perspectives_approaches: 34951     # Observed vs Clinical infant + 方法论
ch3_emergent_self: 87336                # Sense of Emergent Self(0-2 月)⭐
ch4_core_self_vs_other: 167502         # Core Self - 自他区分(2-6 月)⭐
ch5_core_self_with_other: 244015       # Core Self - 与他人在一起(2-6 月)RIGs / evoked companion
ch6_subjective_self_overview: 301348   # Subjective Self 总览(7-15 月)
ch7_affective_attunement: 333767       # Affective Attunement ⭐⭐⭐ Stern 最强
ch8_verbal_self: 391150                # Verbal Self(15+ 月)
ch9_observed_infant_clinical: 441809   # Clinical(横跨)
ch10_reconstructed_clinical_infant: 554260  # Reconstructed Clinical
ch11_therapeutic_implications: 613134  # Therapy(深度抽象)
bibliography: 664037
total_chars: 756079
```

### 4.2 chunk 策略

每章 30-80K 字符,Python `text[start:end]` 切片读取(主上下文)。Ch9 最长 112K,跳过临床细节聚焦 1-3-1 章。

### 4.3 反向覆盖审计(每章必做)

每段产卡完成后,主上下文从原文重列"父母从 Stern 视角必须知道的 N 件事",对比已写卡补漏。

实测 R2 补 5 张(并行 session 3 张 + 我 R2 补 2 张):
- C-S0-018:婴儿是真实测试者(反 Freud 幻想婴儿论)— 并行 session
- C-S3-200:宝宝也在调节你(mutual regulation,中国家长少知)— 并行 session
- C-S5-298:修复比完美更建 secure(rupture-and-repair)— 并行 session
- **C-S4-202:过度刺激 vs 不足刺激父母**(Stevie 案例 + 抑郁妈)— **我 R2 补**
- **C-S5-299:扑克脸 = 玩手机代价**(Tronick 1978 still-face)— **我 R2 补**

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-017 Bowlby V3 + SRC-018 Stern + 改 next_src_id → SRC-019)✅
│   └── tier3-books/notes/
│       └── SRC-018.yaml ✅(新建)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-018 节 + 顶部目录表 + 总数 +41)
│   ├── s0-pregnancy/      # C-S0-015..018 ✅(4)
│   ├── s1-newborn/        # C-S1-253..257 ✅(5)
│   ├── s2-1to3mo/         # C-S2-191..194 ✅(4)
│   ├── s3-3to6mo/         # C-S3-196..200 ✅(5)
│   ├── s4-6to9mo/         # C-S4-196..202 ✅(7,R2 补 202)
│   ├── s5-9to12mo/        # C-S5-291..299 ✅(9,R2 补 299) — Stern 最强
│   ├── s6-12to24mo/       # C-S6-296..300 ✅(5)
│   └── s7-24to36mo/       # C-S7-248..251 ✅(4)
├── 40-glossary/(14 张新)
│   ├── G-PERSON-Stern.yaml ✅
│   ├── G-TERM-emergent-self.yaml ✅
│   ├── G-TERM-core-self.yaml ✅
│   ├── G-TERM-subjective-self.yaml ✅
│   ├── G-TERM-verbal-self.yaml ✅
│   ├── G-TERM-affective-attunement.yaml ✅⭐
│   ├── G-TERM-vitality-affects.yaml ✅
│   ├── G-TERM-RIGs.yaml ✅
│   ├── G-TERM-amodal-perception.yaml ✅
│   ├── G-TERM-intersubjectivity.yaml ✅
│   ├── G-TERM-evoked-companion.yaml ✅
│   ├── G-TERM-self-recognition.yaml ✅
│   ├── G-TERM-baby-faces.yaml ✅
│   └── G-TERM-still-face-experiment.yaml ✅(R2 补)
└── 00-meta/
    ├── progress.md ✅(更新累计 + Phase 7 完成记录)
    ├── PHASE7_STERN.md ✅(本文件)
    └── checkpoints/
        ├── checkpoint_PHASE7_STERN_20260503.md ✅(初+二审)
        └── checkpoint_PHASE7_STERN_AUDIT_20260503.md ✅(三审)
```

---

## 6. 完成定义(实测)

- [x] 抓 Stern《The Interpersonal World of the Infant》全本(11 章)→ SRC-018.yaml + raw .md 已就位
- [x] 产 **41 张新卡**(任务范围 35-50 ✓)
- [x] 新建 **13 张术语卡**(任务范围 6-10 → 实际 13,因为 Stern 概念多)
- [x] 反向覆盖审计补 3 张(reality-tester / mutual-regulation / repair)
- [x] 三轮独立审计完成(R1 内部质量 + R2 漏知识点 + R3 漏术语 + 跨源)
- [x] checkpoint MD 完成(2 个:初+二审 + 三审)
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(无并行 session,直接更新)
- [x] 跨源 related_cards 标连(Stern ↔ Bowlby ↔ Davies ↔ Lillard ↔ Karp ↔ AAP ↔ 鲍秀兰 ↔ Brazelton)
- [x] 全部 41 张卡 YAML 验证通过(0 fail)
- [x] 全部 glossary_refs 指向存在的术语卡(0 missing)
- [x] 全部 related_cards 指向存在的知识卡(0 broken / 0 self-ref)
- [x] **严格审查:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 fm 单行 >80 / 0 学究词残留**
- [x] **跨源对照 ≥ 5 派一致 A 级卡**(C-S5-297 调谐 = 安全依恋根 4 派一致)

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 7 通过。

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 543 张知识卡 + 158 张术语卡**(Phase 6 末状态)
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - Stern self 框架 vs Bowlby attachment vs 蒙氏 self-formation:**3 派互补,不冲突**
   - Stern 反 Mahler "共生融合":Stern 立场强(Mahler 错)
   - Stern 反 Freud "幻想婴儿":Stern 立场强(Freud 误用于婴儿期)
4. ✅ **白话风格**(避免学究腔)— 修 54 处学究词
5. ✅ **跨源主动标连**(41 张卡平均 1.6 个跨源 related_cards)

---

## 8. 工程纪律(继承 + 新)

- 文件 .md 已 OCR(756KB,单长行,无 OCR 错字)
- 主上下文 Python offset 切片读取(每次 15-30K)
- 反向审计每段必做
- YAML 验证: 列表项不能以 `**` 开头(Phase 4 教训)
- 字段含 `"` 必须用 `'..."..."'` 单引号包裹(Phase 5 二审踩坑,本卷 2 处)
- **本次特别**:`title <= 15 字`、`hook 8-12 字` 是英文术语长导致最难,需主动用中文术语
- **学究词彻底**:Python 扫描 + bulk replace 工具

---

## 9. 立场对照(本次产出实测)

### 9.1 Stern vs Bowlby(依恋)

Stern 不反对 Bowlby — **补充心理过程**:
- Bowlby 给"宏观行为模式" + 进化解释
- Stern 给"微观心理过程"(attunement / RIGs / evoked companion)
- **结合用最强**

### 9.2 Stern vs 蒙氏(self-formation)

Stern 不反对蒙氏 — **补充心理细节**:
- 蒙氏给 self-formation 哲学命题
- Stern 给 4 senses self 心理细节
- 蒙氏 self-construction(C-S0-013)+ Stern self 4 阶段(C-S0-015)双轨

### 9.3 Stern 反 Mahler / Freud(经典精神分析)

直接对立 — Stern 立场强:
- 反 Mahler "正常自闭期 + 共生融合期"(C-S0-016)
- 反 Freud "刺激屏障 / 愿望满足幻想"(C-S0-018)
- 反"婴儿期防御机制论"(C-S0-018)
- 反"hatching 独立分离论"(C-S4-196)

### 9.4 Stern vs 中文文化常见误解

| 中文常见误解 | Stern 数据反驳 | 卡片 ID |
|---|---|---|
| "宝宝小什么都不懂" | 反:出生即跨感官 + 模仿表情 | C-S0-016 + C-S1-255 + C-S1-257 |
| "宝宝跟妈是一体的" | 反:从来不是一体,Mahler 错了 | C-S0-016 |
| "新生儿就是吃奶睡觉" | 反:有 alert inactivity 学习窗 | C-S1-253 |
| "宝宝在装可怜" | 反:0-18 月没有"演戏"能力 | C-S0-018 |
| "我对宝宝总笑脸他就好" | 反:关键是 vitality 同频不只表情 | C-S5-291 |
| "我得做完美妈" | 反:修复比完美更建 secure | C-S5-298 |
| "宝宝会说话了就该独立" | 反:仍需大量非语言互动 | C-S6-300 |
| "用嘴说不要哭" | 反:哭是 vitality affects 表达,合法 | C-S6-300 |
| "妈说乖跟爸说乖一样" | 反:we meanings 不同 | C-S7-249 |
| "宝宝代词用错要纠正" | 反:代词是 self 副产品不是技能 | C-S7-248 |
| "陪宝宝就是边玩边教" | 反:communion 不是 communication | C-S5-295 |

---

## 10. 改进建议(给后续 Phase 8 接手)

1. **Pikler / Gerber / Lansbury(RIE 派)** — 蒙氏邻近,floor bed / yes space 同源
2. **Shonkoff《From Neurons to Neighborhoods》** — Harvard NRC 神经发展底座
3. **WHO Infant Feeding Guideline** — Tier 1 国际权威循证
4. **松田道雄《育儿百科》** — 日本经典中译,跨 0-6 岁
5. **海蒂育儿大百科(Heidi Murkoff)** — 全球销量第一,百科式
6. **2000 Stern Updated Edition 续章** — narrative self 部分(本卷只覆盖 1985 原版)

---

## 11. 跟 Phase 6 教训对比

| Phase 6 教训 | Phase 7 应对 |
|---|---|
| YAML 引号嵌套陷阱 | ✅ 主动用单引号包(C-S6-299 + C-S7-248 各 1 处)|
| hook 字数 8-12 严格 | ✅ Python 扫 + 修 4 处 |
| title ≤ 15 严格 | ✅ Python 扫 + 修 19 处(英文术语长是最大挑战)|
| 学究词主动改 | ✅ Python 扫 + bulk replace 修 54 处 |
| 反向覆盖审计每章 + 收官 | ✅ 收官前补 3 张(reality-tester / mutual-reg / repair)|
| 跨源关联手动 | ✅ 主动标连 41 张卡(平均 1.6 个跨源)|
| 章节扫描列全清单 | ✅ 11 章全部 offset 确认 |
| **新教训:title 英文术语长易超 15** | ✅ 主动用中文术语对应("Affective attunement" → "情感调谐")|
| **新教训:跨源 link 不只 link 一个 source** | ✅ 主动 link 7 个 source(SRC-003/006/009/010/011/012/016)|

---

## 12. 工程意外(Phase 7 特有)

### 意外 1:Title 超 15 字(19 张)
- 主因:Stern 英文术语长("Affective attunement"/"Subjective self"/"Vitality affects"/"Communion")
- 修复:批量改用中文术语("情感调谐"/"主观自我"/"活力情感"/"共在")
- **教训**:用 Stern 卡时优先用中文术语 + 简短形式

### 意外 2:学究词残留(54 处)
- 主因:Stern 学术性强,翻译时不小心留了"机制 / 维度 / 认知 / 感知 / 本质 / 分化"
- 修复:Python bulk replace
- **教训**:Stern 类学术书产卡时主动用白话词("机制"→"过程", "维度"→"方面", "认知"→"理解")

### 意外 3:跨源 link 集中在 SRC-016
- Stern 卡的 related_cards 主要 link 到 SRC-016 (Lillard) — 因为 self-formation 哲学最相关
- 但缺少 link 到 SRC-009 (鲍秀兰) / SRC-010 (Brazelton) / SRC-013 (Wonder Weeks)
- 修复:R3 阶段主动加 6 个 cross-refs(到 SRC-009, SRC-010)
- **教训**:跨源 link 要有意识地分布到多个 source,不只 link 最相关的

### 意外 4:1 broken reference(C-S3-150)
- C-S3-200 引用了不存在的 C-S3-150
- 修复:改成 C-S3-029(Brazelton S3 实存)
- **教训**:related_cards 写完后必须 ls 验证存在

### 意外 5:9 张 A 级卡 (>71%) — 远超 Lillard 35%
- 不是 over-rate,是 Stern 引用的研究(Meltzoff / Field / Brazelton / Bowlby)硬数据
- A 级里 70%+ 是"反传统 + 有硬实验"类型 — 含金量高
- 但需在三审中 spot-check 确认每个 A 级都有 Tier 1 共识

---

## 13. 三轮审查独立 — Phase 7 教训

继承 Phase 6 教训,**三轮审计独立** 不是"再读一遍":

### R1 — 内部质量(Python 验证脚本)
- YAML 解析 ✓
- 字数 ✓(title/hook/wtd/fm)
- 学究词扫描 ✓
- glossary_refs 完整性 ✓
- related_cards 完整性 + 0 self-ref ✓
- 实测:**修 19 title + 4 hook + 1 fm + 54 学究词 + 2 YAML quote nesting**

### R2 — 漏知识点反向覆盖
- 主上下文重读 11 章关键段
- 列"父母从 Stern 视角必须知道的 N 件事"
- 跟已写 38 张 diff
- 补 3 张高价值漏卡:
  - C-S0-018 反 Freud "幻想婴儿" → 婴儿是 reality tester
  - C-S3-200 mutual regulation(宝宝也调节你)
  - C-S5-298 rupture-and-repair(修复比完美更建 secure)

### R3 — 漏术语 + 跨源对照
- 13 张术语全部建好(Stern 4 senses + attunement + vitality + RIGs 等)
- Cross-source 加 6 个 references(到 SRC-009 鲍秀兰 + SRC-010 Brazelton)
- 修 1 broken reference(C-S3-150 → C-S3-029)
- 最终 Stern 链到 7 个 source(SRC-003/006/009/010/011/012/016)

---

*v1.0 · 2026-05-03 — Phase 7 Stern Self 心理学奠基完整记录*
*基于 Phase 6 Lillard + 并行 Bowlby V3 教训整合*
*Self 4 阶段 + Affective attunement 双轨完成,Stern + Bowlby + 蒙氏三角互补*
*准备 Phase 8 候选:Pikler / Gerber / Lansbury(RIE 派)/ Shonkoff / WHO / 松田道雄 / 海蒂*
