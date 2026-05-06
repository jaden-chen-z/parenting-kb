# Phase 4 执行任务书 · Wonder Weeks(并行)

> 项目代号:parenting-kb · Phase 4 第二本(与 Bowlby Vol 2 SRC-012 并行)· 版本 v1.0 (2026-05-03)
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE4_WONDER_WEEKS.md)
> 2. `00-meta/PHASE3_BOWLBY_VOL1.md`(段定义 / 工作流 / ID 隔离参考)
> 3. `00-meta/checkpoints/checkpoint_PHASE3_BOWLBY_VOL1_20260503_audit.md`(自审教训)
>
> 然后看 `40-glossary/G-PERSON-Brazelton.yaml` + `G-TERM-touchpoint.yaml` + `G-TERM-regression-progression.yaml`(理论邻近,要标 related)。

---

## 0. 一句话任务

抓 van de Rijt + Plooij《The Wonder Weeks》(婴儿大脑跃迁 10 周),产 **30 张 v3.5 中文跃迁理论卡** + 6 张术语卡。
**与 Bowlby Vol 2 session 并行运行,严格 ID 隔离**(+50 buffer)。

---

## 1. 选定的书 + 来源

**Hetty van de Rijt + Frans X. Plooij《The Wonder Weeks: How to Stimulate Your Baby's Mental Development》**(婴儿大脑跃迁 10 周 / 神奇周)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/vanderijt_wonder_weeks.md`(.epub 转 .md, 822KB)|
| 作者 | Hetty van de Rijt(1942-2019)+ Frans X. Plooij(1944-),荷兰发展心理学家夫妇 |
| 师承 | Niko Tinbergen(1973 诺奖动物行为学家)+ Jane Goodall 黑猩猩研究背景 |
| 流派 | Tier 3 实操 + 发展规律预测派(类似 Brazelton 触摸点) |
| 范围 | 0-20 月(0-75 周),10 个跃迁时间表 |
| 出版 | 原版 1992 荷兰文,英译多版本 |
| 系列 | The Wonder Weeks |

### 为什么这本(并行 session 2)

1. **可预测时间表** — 中国家长最焦虑"宝宝突然狂哭睡眠倒退"的痛点解药
2. **Brazelton 触摸点理论的姐妹篇** — Brazelton 在英译序中直接背书:"独立得出相同结论"
3. **跨段全覆盖** — 10 跃迁覆盖 S1-S6(1.5 年),与 Bowlby Vol 2(分离焦虑)完美互补
4. **OCR 已就位**(.epub 转 .md,无 OCR 错字,只需 HTML 标签处理)
5. **G-PERSON-Brazelton 已建** — 理论邻近,直接标 related

---

## 2. 段定义(继承 Phase 3 段制)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S1 | 0-1 月 | s1-newborn | 4 张(C-S1-178..181) |
| S2 | 1-3 月 | s2-1to3mo | 5 张(C-S2-121..125) |
| S3 | 3-6 月 | s3-3to6mo | 4 张(C-S3-129..132) |
| S4 | 6-9 月 | s4-6to9mo | 5 张(C-S4-124..128) |
| S5 | 9-12 月 | s5-9to12mo | 4 张(C-S5-126..129) |
| S6 | 12-24 月 | s6-12to24mo | 6 张(C-S6-122..127) |
| S7 | 24-36 月 | s7-24to36mo | 2 张(C-S7-074..075) |
| **总计** | | | **30 张** |

S6 卡数最多 — 1-2 岁是 Wonder Week 最密集跃迁年(WW55 + WW64 + WW75 三连击)。
S7 跳过详细跃迁卡 — 本书覆盖到 75 周(17.3 月)止,后续仅给 2 张延展卡(后续展望 + 跨文化总结)。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3 第三本扩展。

### 评级 evidence_level(本书标尺)

Wonder Weeks = van de Rijt + Plooij 35 年自然观察 + 灵长类研究背景 + 6/10 跃迁有独立 EEG 验证:
- **A**:与 Tier 1 共识对齐 OR Wonder Week + Bowlby + Brazelton 三派一致(罕见)
- **B**:van de Rijt 引用具体研究 / 跨文化数据 / EEG 验证 — **大多数卡**
- **C**:个人理论推断(实操建议为主)

实测产出:**A=5 / B=22 / C=3** 张 — 跃迁普遍性证据较强,A 级稍多。

---

## 4. ⚠️ 并行协调(关键!)

### 4.1 ID 隔离规则

另一 session 正在做 Bowlby Vol 2(SRC-012),会往 S1-S6 加卡。**本 session 严格遵守**:

1. **SRC ID** = SRC-013(跳过 SRC-012,即使 source_index.yaml 还显示 next=SRC-011)
2. **卡片 ID buffer +50**(给 Bowlby Vol 2 留 40 张冗余):

```bash
for sd in s1-newborn s2-1to3mo s3-3to6mo s4-6to9mo s5-9to12mo s6-12to24mo s7-24to36mo; do
  echo "$sd: max=$(ls ~/Desktop/parenting-kb/30-cards/$sd/ | grep -oE '[0-9]{3}' | sort -n | tail -1)"
done
```

实测起始(本次 session,2026-05-03):
| 段 | grep max | +50 起步 | 实际产出 |
|---|---|---|---|
| S1 | 128 | 178 | C-S1-178..181(4) |
| S2 | 071 | 121 | C-S2-121..125(5) |
| S3 | 079 | 129 | C-S3-129..132(4) |
| S4 | 074 | 124 | C-S4-124..128(5) |
| S5 | 076 | 126 | C-S5-126..129(4) |
| S6 | 072 | 122 | C-S6-122..127(6) |
| S7 | 024 | 074 | C-S7-074..075(2) |

**实测验证**:Bowlby Vol 2 在并行 session 中预计用 35-40 张/段,buffer 充足。

### 4.2 不动的文件(并行不安全)

- ❌ **不动 `30-cards/INDEX_BY_SOURCE.md`**(让 Bowlby Vol 2 收尾或用户手动合并)
- ❌ **不动 `00-meta/progress.md`**(同上)
- ❌ **不动 `10-sources/source_index.yaml`**(避免 next_src_id 字段冲突)
- ❌ **不动 `10-sources/tier3-books/notes/SRC-012.yaml`**(Bowlby Vol 2 session 在写)

### 4.3 OK 的文件(各自独立,不冲突)

- ✅ `10-sources/tier3-books/notes/SRC-013.yaml`(新建文件)
- ✅ `30-cards/sN/C-SN-XXX.yaml`(新建文件,ID 已 +50 buffer)
- ✅ `40-glossary/G-XXX-YYY.yaml`(新建文件)
- ✅ `00-meta/PHASE4_WONDER_WEEKS.md`(本文件)
- ✅ `00-meta/checkpoints/checkpoint_PHASE4_WONDER_WEEKS_<YYYYMMDD>.md`(新建文件)

---

## 5. 工作流(基于 Phase 3 经验改进)

### 5.1 章节地图(已扫,见 SRC-013.yaml)

Wonder Weeks 822KB / 12 章 + 后记 / 单长行 .md 文件。章节偏移:

```python
chapter01: 25753   # Growing Up: How Your Baby Does It(框架)
chapter02: 40964   # Newborn: Welcome to the World
chapter03: 72367   # Wonder Week 5: Sensations
chapter04: 99622   # Wonder Week 8: Patterns
chapter05: 146745  # Wonder Week 12: Smooth Transitions
chapter06: 189308  # Wonder Week 19: Events
chapter07: 252222  # Wonder Week 26: Relationships
chapter08: 330870  # Wonder Week 37: Categories
chapter09: 385431  # Wonder Week 46: Sequences
chapter10: 442850  # Wonder Week 55: Programs
chapter11: 496462  # Wonder Week 64: Principles
chapter12: 603434  # Wonder Week 75: Systems
postscript: 713615 # Counting on Difficult Times
```

### 5.2 chunk 策略

每跃迁章节 15-25K 字符,Python `text[start:end]` 切片读取。

### 5.3 反向覆盖审计(每段必做)

每段产卡完成后,主上下文(不看清单)从原文重列"父母从认知跃迁视角必须知道的 N 件事",对比已写卡补漏。

实测覆盖完整(无未补漏点)— 30 张卡覆盖了:
- 总览框架(3 C 信号 / 10 跃迁时间表 / 早产校正)
- 每个跃迁的认知机制 + 父母对策
- 跨源对照(尤其 Bowlby + Brazelton + AAP)
- 跨段哲学(质量时间是伪概念 + 跃迁是普遍 = 不孤单)

---

## 6. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── ⚠️ source_index.yaml(不改)
│   └── tier3-books/notes/
│       └── SRC-013.yaml ✅(新建)
├── 30-cards/
│   ├── ⚠️ INDEX_BY_SOURCE.md(不改)
│   ├── s1-newborn/        # C-S1-178..181 ✅
│   ├── s2-1to3mo/         # C-S2-121..125 ✅
│   ├── s3-3to6mo/         # C-S3-129..132 ✅
│   ├── s4-6to9mo/         # C-S4-124..128 ✅
│   ├── s5-9to12mo/        # C-S5-126..129 ✅
│   ├── s6-12to24mo/       # C-S6-122..127 ✅
│   └── s7-24to36mo/       # C-S7-074..075 ✅
├── 40-glossary/
│   ├── G-PERSON-vanderijt.yaml ✅(新建)
│   ├── G-PERSON-plooij.yaml ✅(新建)
│   ├── G-TERM-wonder-week.yaml ✅(新建)
│   ├── G-TERM-mental-leap.yaml ✅(新建)
│   ├── G-TERM-3C-signs.yaml ✅(新建)
│   └── G-TERM-fussy-phase.yaml ✅(新建)
└── 00-meta/
    ├── PHASE4_WONDER_WEEKS.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE4_WONDER_WEEKS_20260503.md(下一步)
```

---

## 7. 完成定义(实测)

- [x] 抓 Wonder Weeks → SRC-013.yaml + raw .md 已就位
- [x] 产 **30 张新卡**(任务范围 25-40 张 ✓)
- [x] 新建 **6 张术语卡**(任务范围 ≥4 张 ✓)
- [x] 反向覆盖审计(无未补漏点)
- [x] checkpoint MD 完成
- [x] **不动 INDEX_BY_SOURCE.md + progress.md + source_index.yaml + SRC-012.yaml**(并行安全)
- [x] 跨源 related_cards 标连(Wonder Week ↔ Bowlby ↔ Brazelton ↔ AAP)

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 4 第二本通过。

---

## 8. 关键约束(实测都遵守)

1. ✅ **不动现有 351 知识卡 + 98 术语卡**
2. ✅ **ID 必须 +50 buffer**(防与 Bowlby Vol 2 撞)
3. ✅ **不动 INDEX + progress + source_index + SRC-012**(并行不安全)
4. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
5. ✅ **理论卡也按 v3.5 写白话**(避免学究腔)
6. ✅ **立场对照不判对错**:Wonder Week 跃迁 vs Brazelton 触摸点 = 不冲突,只是不同维度强调
7. ✅ **Wonder Week 理论的中文家长版本** — 不照搬"sensorimotor period"等学术语

---

## 9. 工程纪律(继承)

- 文件 .md 已 OCR(822KB,单长行,无 OCR 错字)
- 主上下文 Python offset 切片读取(每段 15-25K 字符)
- 反向审计每段必做
- YAML 验证: 列表项不能以 `**` 开头(Phase 3 教训)
- 字段含 `"` 必须用 `'..."..."'` 单引号包裹(本次 1 张卡修)

---

## 10. 立场对照(本次产出实测)

### 10.1 Wonder Week 与已有源对照

| 主题 | Wonder Week 立场 | Bowlby 立场 | Brazelton 立场 | AAP / 鲍秀兰立场 |
|---|---|---|---|---|
| 跃迁 fussy phase | 神经科学视角(EEG) | (无) | 触摸点临床观察 | (隐含) |
| 6-9 月怕陌生人 | C-S4-124 关系世界 | C-S4-068 进化机制 | (触摸点 6-7 + 9 月) | C-S4-004 临床 / C-S5-013 早教 |
| 13-18 月叛逆 | C-S6-123 原则世界 | C-S6-068 依恋顶峰 | (触摸点 12 + 18 月) | C-S6-007 全家一致(鲍) |
| 体罚有害 | C-S6-126 跃迁期信任 | C-S6-070 创伤数据 | (无) | C-S6-007 不打 |
| fussy 不是出牙 | C-S4-126 数据反驳 | (无) | (无) | (隐含) |

### 10.2 Wonder Week 独有维度(填补理论空缺)

- **可预测的 10 跃迁时间表**(C-S1-179) — 现库首次"可日历化"育儿挑战
- **3 C 信号识别框架**(C-S1-178, G-TERM-3C-signs)— Bowlby/Brazelton 都没明确化的"前奏识别"
- **跃迁 vs 大脑物理变化**(C-S6-124) — 6-9 跃迁有 EEG 同步证据,神经科学背书
- **质量时间是伪概念**(C-S6-127) — 现库首次直接挑战"职场妈妈 KPI 式陪伴"

---

## 11. 改进建议(给后续 Phase 5 接手)

1. **接 Bowlby Vol 3《丧失》**:儿童哀伤反应,跟 Wonder Week 75 周(17.3 月)系统跃迁(自我意识)有关
2. **接 Stern《婴儿人际世界》**:跟 Wonder Week 26+ 关系世界深度对照
3. **接 Gopnik《摇篮里的科学家》**:跟 WW37/46(分类 / 序列)的"婴儿是研究员"主题深度对话
4. **接 RIE / Lansbury**:跟 Wonder Week WW64/75 期间的"自主独立"主题深度对话
5. **补 G-PERSON-Tinbergen**(Wonder Weeks 师承)— 给 Plooij/van de Rijt 卡背景
6. **补 G-PERSON-Goodall**(Plooij 黑猩猩研究背景)— 灵长类研究的人类延伸

---

*v1.0 · 2026-05-03 — Phase 4 第二本(并行 Wonder Weeks)完整记录*
*基于 PHASE3_BOWLBY_VOL1 v1.0 段定义 + 并行协调框架*
*与 Phase 4 第一本(Bowlby Vol 2 SRC-012)并行执行,无冲突*
