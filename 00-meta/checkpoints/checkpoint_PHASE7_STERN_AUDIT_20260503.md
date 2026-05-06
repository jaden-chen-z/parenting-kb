# Checkpoint · Phase 7 Stern 三审独立报告(2026-05-03)

> 项目:parenting-kb · Phase 7 第一本 · Stern《婴儿的人际世界》三轮独立审查
> 启动:2026-05-03(同日,跟初版同 session 串联)
> 完成:2026-05-03 同日
> 主产出 checkpoint:`checkpoint_PHASE7_STERN_20260503.md`

---

## 0. 一句话总结

**继承 Phase 6 Lillard 三审制(R1 内部质量 + R2 漏知识点 + R3 漏术语 / 跨源)**,Stern 三轮审查全部通过 — 0 内部质量错误 + R2 补 2 张高价值卡(still-face + 过度/不足刺激)+ R3 修 3 张引错源 ID + 增 5 张跨源链接。终版 43 张 + 14 术语,72% A 级,9 派跨源 71 链接,**通过验收。**

---

## 1. R1 — 内部质量审查

### 1.1 跑深度 Python 验证脚本(初次)

发现问题(43 卡测后):
- YAML 解析:**2 错** — C-S6-299 / C-S7-248 引号嵌套
- 字数严格(title ≤ 15):**19 处超**(Stern 英文术语撑爆)
- 字数严格(hook 8-12):**4 处不在范围**
- 字数严格(wtd ≤ 35):0
- 字数严格(fm 单行 ≤ 80):1 处
- 学究词残留(11 词):**32 卡 54 处**(机制 / 维度 / 认知 / 感知 等)
- glossary_refs 完整性:0 错
- related_cards 完整性:0 错(0 missing,0 self-ref)

### 1.2 修复

- ✅ YAML 2 处:外层加单引号
- ✅ Title 19 处:批量缩短,中英混排
- ✅ Hook 4 处:加修饰词到 8 字
- ✅ Fm 1 处:拆行
- ✅ 学究词 54 处:Python 一次性替换
  - 机制 → 过程
  - 维度 → 方面
  - 认知 → 理解
  - 感知 → 觉察
  - 本质 → 根本
  - 分化 → 区分
- ✅ 跑第二次验证:**0 错全过**

### 1.3 R1 终验

```
=== FINAL R1 VALIDATION ===
  YAML errors: 0
  Title >15: 0
  Hook 不在 8-12: 0
  wtd >35: 0
  fm 单行 >80: 0
  Academic words: 0
  Missing glossary_refs: 0
  Missing related_cards: 0
  Self refs: 0
  Glossary errors: 0
```

---

## 2. R2 — 漏知识点反向覆盖审计

### 2.1 流程

主上下文重读 Stern 11 章关键概念,跟已写 41 张卡 diff,识别"父母从 self 视角必须知道的 N 件事"。

### 2.2 发现

| 章 | 漏知识点 | 重要度 |
|---|---|---|
| Ch 7 / Ch 9 | **Tronick still-face experiment** — 妈突然没表情宝宝立刻崩 | ⭐⭐⭐(中国家长 #1 痛点:玩手机) |
| Ch 9 | **过度刺激 vs 不足刺激父母** — Stevie 入侵案例 + 抑郁妈案例 | ⭐⭐(中国家长高频"过度热情") |

### 2.3 R2 补 2 张

#### S4(1 张)
| ID | 标题 | 等级 |
|---|---|---|
| C-S4-202 | 过度刺激 vs 不足刺激 ⭐ | A |

#### S5(1 张)
| ID | 标题 | 等级 |
|---|---|---|
| C-S5-299 | 扑克脸 = 玩手机代价 ⭐ | A |

### 2.4 R2 验证

跑全套 Python 脚本,**0 错全过**:
- YAML 0 错
- 字数 0 错
- 学究词 0 残留
- glossary_refs 全部存在(C-S5-299 引 G-TERM-still-face-experiment 新建)
- related_cards 全部存在 + 0 自引用

### 2.5 同期发现 — 并行 session 已补 3 张

ls 实测 SRC-018 卡 = 43 张,而非我预期的 38 + 我新写 2 = 40 张。
另 3 张是并行 session 写入:
- C-S0-018:婴儿是真实测试者(反 Freud 幻想婴儿)
- C-S3-200:宝宝也在调节你(mutual regulation)
- C-S5-298:修复比完美更建 secure(rupture-and-repair)

**评估**:3 张并行卡质量好,内容互补,**保留**。
**调整**:我的 still-face 由 C-S5-298 → C-S5-299(避撞)。

---

## 3. R3 — 漏术语 + 跨源对照审查

### 3.1 漏术语审查

扫所有卡正文里出现的专业词,识别需要建独立术语:
- ✅ G-PERSON-Stern(必建,作者)
- ✅ G-TERM-emergent-self / core-self / subjective-self / verbal-self(4 阶段全建)
- ✅ G-TERM-affective-attunement(必建 ⭐⭐⭐)
- ✅ G-TERM-vitality-affects / RIGs / amodal-perception / intersubjectivity / evoked-companion(Stern 5 大概念)
- ✅ G-TERM-self-recognition(rouge test 关键)
- ✅ G-TERM-baby-faces(Stern 命名)
- ✅ G-TERM-still-face-experiment(R2 补,Tronick 实验)

**14 张术语卡全部建,无漏。**

### 3.2 跨源对照统计(R3 第 1 跑)

跑 Python 脚本统计 43 卡的 related_cards 跨源情况:

```
Stern 卡数: 43
Total related_cards links: 132
Self-source links (Stern↔Stern): 67
Cross-source links: 65 (1.51/卡)

跨源分布:
  SRC-016 (Lillard): 46 links
  SRC-003 (Karp): 7 links
  SRC-011 (Bowlby V1): 4 links
  SRC-009 (鲍秀兰): 3 links
  SRC-010 (Brazelton): 2 links
  SRC-006 (AAP-safety): 2 links  
  SRC-012 (Bowlby V2): 1 links
  SRC-013 (Wonder Weeks): 0 ← 问题!
  SRC-014 (Davies): 0 ← 问题!
  SRC-017 (Bowlby V3): 0 ← 问题!
  
0 跨源链接卡: 3
  C-S4-202 / C-S5-292 / C-S5-299
```

### 3.3 R3 修 + 补

#### 3.3.1 修引错源 ID(3 处)

发现 3 张卡的"Wonder Weeks"链接其实指向其他源:
- C-S2-191 引 C-S2-001 → 实际 Karp(应为 Wonder Weeks 8 周跃迁)
- C-S4-196 引 C-S4-001 → 实际 AAP-safety(应为 Wonder Weeks 26 周跃迁)
- C-S4-197 引 C-S4-001 → 同样错

**修复**:用 ls 找到真 Wonder Weeks ID:
- C-S2-001 → C-S2-121(Wonder Weeks 8 周第二跃迁)
- C-S4-001 → C-S4-124(Wonder Weeks 26 周第五跃迁,2 处)

#### 3.3.2 给 0 跨源 3 卡补跨源链接

- C-S4-202 → 加 C-S6-186(Lillard 母-师角色) + C-S5-070(Bowlby V1 安全依恋)
- C-S5-292 → 加 C-S2-127(Davies 真词不嘎嘎) + C-S1-018(Karp 5S)
- C-S5-299 → 加 C-S5-290(Bowlby V3 月嫂) + C-S6-294(Bowlby V3 替代照顾者)

### 3.4 R3 终验(修 + 补后)

```
=== R3 跨源对照(终版)===
Stern 卡数: 43
Total links: 138
Self links: 67
Cross links: 71 (1.65/卡)

跨源分布:
  SRC-016 (Lillard): 47
  SRC-003 (Karp): 7
  SRC-011 (Bowlby V1): 5
  SRC-013 (Wonder Weeks): 3 ✓(从 0 补到 3)
  SRC-009 (鲍秀兰): 3
  SRC-010 (Brazelton): 2
  SRC-017 (Bowlby V3): 2 ✓(从 0 补到 2)
  SRC-014 (Davies): 1 ✓(从 0 补到 1)
  SRC-012 (Bowlby V2): 1

0 跨源链接卡: 0 ✓
9 派源全覆盖
```

---

## 4. 三审教训(本次新增)

### 4.1 并行 session ID 隔离仍要警惕

Phase 6 教训:不只看 next_src_id,要 ls 实际 SRC 文件。
**Phase 7 新教训**:不只 ls SRC 文件,还要 **ls 实际段最大卡 ID** — 因为并行 session 可能写到我预期之外的 ID。
中途多次 ls 验证(每写完 5-10 张就 ls 一次)是必要的。

### 4.2 related_cards 必须 ls 验证

**Phase 7 新教训**:不能凭"段位 + 编号"猜其他源的卡 ID。
Stern 卡里我写"C-S2-001 — Wonder Weeks 第 2 跃迁",但 C-S2-001 实际是 Karp。
跨源 link 必须**先 ls 那个段**,看真实 Wonder Weeks ID 范围(本卷 121-126)再 link。

### 4.3 R3 跨源验证脚本是必须

光 R1(YAML / 字数 / 学究词)不够 — R3 跨源验证才能发现"引错源 ID"。
本次 R3 跑出 0 跨源卡 3 张 + 错引 3 处,如果没 R3 都会漏。
建议:**每个 Phase R3 必跑跨源 stat 脚本**(包括"卡 → 源"反查 + 0 跨源识别)。

### 4.4 Stern 学术派术语必须有"中文短版"

Stern 英文术语长(Affective attunement / verbal self / vitality affects)直接做 title 容易超 15 字。
Phase 7 教训:title 必须**先用中文表达 Stern 概念,再括号附英文术语**(如果需要),而不是直接 "Affective attunement = 心同频"。
本次 19 张 title 重写。

### 4.5 学究词在 self 心理学语境特别多

Stern 是精神分析 + 发展心理学,术语自然学究化(机制 / 维度 / 认知 / 感知 / 分化 等)。
Python 一次性替换 54 处后白话化,但**写卡时主动避免**会更高效。
Phase 7 教训:写 Stern 卡时,**每写一段 why_matters 立刻自检 11 个学究词**,而不是堆完再扫。

---

## 5. 完成度对比(初版 → R2 → R3)

| 维度 | 初版(41 并行) | R2(+2 = 43) | R3(终版 43)| 提升 |
|---|---|---|---|---|
| 卡片数量 | 41 | 43 | 43 | +2 R2 补 |
| 段覆盖 | S0-S7(8 段) | S0-S7 | S0-S7 完整 | 段不变 |
| 章节覆盖 | Ch 1-8 主体 | + Ch 9 临床精选 | + Ch 9 完整精选 | + Ch 9 |
| 中国家长高频痛点 | 大部分 | + still-face + 过度刺激 | **全覆盖** | ⭐ |
| 跨源链接数 | 65 | 65 | **71**(+6) | ⭐ |
| 9 派源覆盖 | 7 派 | 7 派 | **9 派**(+2) | ⭐ |
| 跨源链接 / 卡 | 1.51 | 1.51 | **1.65** | ⭐ |
| 0 跨源卡 | 3 | 3 | **0** | ⭐ |
| 错引源 ID 卡 | 3 | 3 | **0**(修 3) | ⭐ |
| A 级 % | 71% | 72% | 72% | +1% |
| 术语卡 | 13 | 14 | 14 | +1 |

---

## 6. 推荐用户审 5 张样本(三审版)

按"中国家长最高频痛点优先 + Stern 独家亮点"推荐抽审:

1. **[C-S5-291 情感调谐 = 心同频](../../30-cards/s5-9to12mo/C-S5-291.yaml)** ⭐⭐⭐ A 级 + Stern 最重要原创 + 中国家长 attunement 频率偏低 — 最实用
2. **[C-S5-299 扑克脸 = 玩手机代价](../../30-cards/s5-9to12mo/C-S5-299.yaml)** ⭐ A 级 + Tronick 实验 + 直接对应"边带娃边玩手机" — R2 补
3. **[C-S5-298 修复比完美更建 secure](../../30-cards/s5-9to12mo/C-S5-298.yaml)** ⭐ A 级 + 焦虑型妈最该读 — 并行补
4. **[C-S6-299 给情感贴标签要准](../../30-cards/s6-12to24mo/C-S6-299.yaml)** ⭐ A 级 + we meanings + 一辈子认错根源
5. **[C-S0-016 反"新生儿混沌"](../../30-cards/s0-pregnancy/C-S0-016.yaml)** ⭐ A 级 + 反 Mahler 共生 + 中国家长 #1 迷思

---

## 7. 决定与待办

### 决定
- Phase 7 第一本 Stern 三审版**通过 / 调整 / 重做**?
- Phase 8 启动书(候选见主 checkpoint §7)?

### 待办
| 待办 | 优先级 | 备注 |
|---|---|---|
| 用户审核 43 张样本 | 高 | §6 推荐 5 张 |
| 用户决定 Phase 8 候选 | 高 | Pikler / Gerber / 松田 / Shonkoff |
| conflicts.md 更新 | 中 | 加 Stern 反 Mahler 共生 |
| memory file 更新 | 高 | 累计数字 + Phase 7 状态 |

---

## 8. 三审教训沉淀(给后续 Phase 8+)

1. **三审独立 + 跑各自脚本**(R1 内部 / R2 反向覆盖 / R3 跨源)
2. **R3 必须跑跨源 stat 脚本** — 不只看 missing,要看错引源 + 0 跨源
3. **related_cards 跨源 link 必须 ls 验证** — 不能猜
4. **并行 session 中途多次 ls 实际 max ID** — 不只信 next_src_id
5. **学术派术语写卡时即时自检** — 别堆完再扫
6. **Title 用中文先行,英文术语括号附** — 防超 15 字

---

*本文件 = Phase 7 第一本 Stern 三审独立产出 checkpoint*
*累计:Stern 43 张 + 14 术语,跨 8 段 S0-S7,A 级 31 张(72%),9 派 71 跨源*
*三审教训 + 并行 session 协调经验沉淀 — 给 Phase 8+ 接手*
