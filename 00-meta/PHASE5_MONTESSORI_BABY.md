# Phase 5 执行任务书 · Davies 蒙氏 0-1

> 项目代号:parenting-kb · Phase 5(2026-05-03)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE5_MONTESSORI_BABY.md)
> 2. `00-meta/checkpoints/checkpoint_PHASE4_WONDER_WEEKS_20260503.md`(Phase 4 教训 + 严格审查)
> 3. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema:前情提要 / 术语卡片化 / inline 引用)
> 然后看:
> - `40-glossary/G-PERSON-Davies.yaml` + `G-PERSON-Montessori.yaml`(蒙氏作者卡)
> - `40-glossary/G-TERM-absorbent-mind.yaml` + `G-TERM-yes-space.yaml` + `G-TERM-floor-bed.yaml` + `G-TERM-topponcino.yaml`(蒙氏核心 4 概念)

---

## 0. 一句话任务

抓 Simone Davies + Junnifa Uzodike《The Montessori Baby》(蒙氏 0-1 岁实操手册),产 **36 张 v3.5 中文蒙氏卡** + 8 张术语卡。**蒙氏理论首次全面入库**。

---

## 1. 选定的书 + 来源

**Simone Davies + Junnifa Uzodike《The Montessori Baby: A Parent's Guide to Nurturing Your Baby with Love, Respect, and Understanding》**(蒙特梭利的小宝宝 0-1 岁)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/davies_montessori_baby.md`(.epub 转 .md, 624KB)|
| 作者 | Simone Davies(蒙氏 0-3 + 3-6 双 AMI 教师,《Montessori Notebook》创始人,荷兰阿姆斯特丹)+ Junnifa Uzodike(蒙氏 0-3 教师,Fruitful Orchard 创办人,尼日利亚) |
| 流派 | Tier 3 实操 + 蒙氏 0-3 哲学派 |
| 范围 | 0-12 月为主,延展少量 1-2 岁 |
| 出版 | 原版 2021 英文,Workman Publishing(纽约)|
| ISBN_en | 978-1-5235-0693-7 |
| 中译本 | 有(《蒙特梭利的小宝宝:0-1 岁》)|

### 为什么这本(Phase 5 选择)

1. **首次引入蒙氏理论** — 知识库已有 7 本但蒙氏 0-3 完全空白
2. **跟现有 7 本派生大量对照** — Karp(swaddle)/ AAP(SIDS)/ Bowlby(secure attachment)/ 鲍秀兰(critical period)
3. **Davies 是蒙氏 0-3 现代翻译者**(把学术语翻译成现代家长能用)
4. **OCR 已就位**(.epub 转 .md,无 OCR 错字)
5. **0-1 全段覆盖** — 跟现有源完美互补

---

## 2. 段定义(本次产出)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S0 | 孕期 | s0-pregnancy | 3 张(C-S0-008..010) |
| S1 | 0-1 月 | s1-newborn | 8 张(C-S1-183..190) |
| S2 | 1-3 月 | s2-1to3mo | 6 张(C-S2-127..132)— 含自审补 1 |
| S3 | 3-6 月 | s3-3to6mo | 5 张(C-S3-133..137) |
| S4 | 6-9 月 | s4-6to9mo | 5 张(C-S4-130..134) |
| S5 | 9-12 月 | s5-9to12mo | 5 张(C-S5-130..134) |
| S6 | 12-24 月 | s6-12to24mo | 4 张(C-S6-130..133)— 含自审补 1 |
| S7 | 24-36 月 | — | 0 张(本书覆盖至 1-2 岁初) |
| **总计** | | | **36 张** |

S1 卡数最多 — 0-1 月是蒙氏共生期 + 新生儿适应,实操点最密。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3/4 扩展。

### 评级 evidence_level(本书标尺)

Davies 蒙氏 0-1 = 100 年蒙氏观察 + 个人实操 + 跨流派引用:
- **A**:与 Tier 1 共识对齐(罕见,蒙氏 0-12 月安全建议跟 AAP 重合处)
- **B**:Davies 引用神经科学 / 蒙氏 100 年观察 / 跨文化数据
- **C**:Davies 个人理论推断(实操建议为主)— 实操派书籍特征

实测产出:**A=11 / B=20 / C=5** 张 — 跨派一致 + AAP 兼容点比预期多。

---

## 4. 工作流(基于 Phase 4 经验改进)

### 4.1 章节地图(SRC-014.yaml 已记录)

Davies 624KB / 9 章 + 后记 / 单长行 .md 文件。章节字节偏移:

```python
ch1_introduction: 13664      # 短引言
ch2_principles: 37337        # 蒙氏 5 原理
ch3_conception_to_6weeks: 70093  # 孕期 + 出生 + 共生期
ch4_setting_up_home: 130509  # yes space + floor bed
ch5_parenting: 191521        # 信任 / 尊重 / 专注 / 边界
ch6_activities: 241139       # 语言 + 动作活动
ch7_putting_into_practice: 376301  # 进食 + 睡眠 + 物理护理
total_chars: 624120
```

### 4.2 chunk 策略

每章 15-25K 字符,Python `text[start:end]` 切片读取。

### 4.3 反向覆盖审计(每段必做)

每段产卡完成后,主上下文从原文重列"父母从蒙氏视角必须知道的 N 件事",对比已写卡补漏。

实测自审补 2 张:
- C-S2-132:哭闹 5 步回应法(Davies 详细流程)
- C-S6-133:温柔但清晰的边界(蒙氏纪律方式)

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-014 + 改 next_src_id → SRC-015)✅
│   └── tier3-books/notes/
│       └── SRC-014.yaml ✅(新建)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-014 节 + 顶部目录表 + 总数 365 → 401)
│   ├── s0-pregnancy/      # C-S0-008..010 ✅(3)
│   ├── s1-newborn/        # C-S1-183..190 ✅(8)
│   ├── s2-1to3mo/         # C-S2-127..132 ✅(6)
│   ├── s3-3to6mo/         # C-S3-133..137 ✅(5)
│   ├── s4-6to9mo/         # C-S4-130..134 ✅(5)
│   ├── s5-9to12mo/        # C-S5-130..134 ✅(5)
│   └── s6-12to24mo/       # C-S6-130..133 ✅(4)
├── 40-glossary/(8 张新)
│   ├── G-PERSON-Davies.yaml ✅
│   ├── G-PERSON-Montessori.yaml ✅
│   ├── G-TERM-absorbent-mind.yaml ✅
│   ├── G-TERM-yes-space.yaml ✅
│   ├── G-TERM-floor-bed.yaml ✅
│   ├── G-TERM-topponcino.yaml ✅
│   ├── G-TERM-prepared-environment.yaml ✅
│   └── G-TERM-symbiosis-period.yaml ✅
└── 00-meta/
    ├── progress.md ✅(更新累计 401 张 + Phase 5 完成记录)
    ├── PHASE5_MONTESSORI_BABY.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE5_MONTESSORI_BABY_20260503.md ✅
```

---

## 6. 完成定义(实测)

- [x] 抓 Davies《The Montessori Baby》全本(7 大章节)→ SRC-014.yaml + raw .md 已就位
- [x] 产 **36 张新卡**(任务范围 30-45 ✓)
- [x] 新建 **8 张术语卡**(任务范围 ≥5 ✓)
- [x] 反向覆盖审计补 2 张(哭闹 5 步 / 温柔边界)
- [x] checkpoint MD 完成
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(并行已结束,直接更新)
- [x] 跨源 related_cards 标连(蒙氏 ↔ Karp ↔ AAP ↔ Bowlby ↔ Brazelton ↔ Wonder Weeks ↔ 鲍秀兰)
- [x] 全部 36 张卡 YAML 验证通过
- [x] 全部 glossary_refs 指向存在的术语卡
- [x] 全部 related_cards 指向存在的知识卡(0 自引用 / 0 占位符)
- [x] 严格审查:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 学究词残留

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 5 通过。

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 365 知识卡 + 108 术语卡**
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - 蒙氏 swaddle vs Karp:不冲突,看父母优先项(动作自由 vs 安抚 / 睡眠)
   - 蒙氏 floor bed vs AAP cribs:不冲突,Davies 引用 AAP SIDS 全部 10 条并标"应遵循"
   - 蒙氏 sensitive period vs 鲍秀兰 critical period:现代神经科学倾向"敏感期"
4. ✅ **白话风格**(避免学究腔)— 改完 23 处学究词
5. ✅ **跨源主动标连**(36 张卡平均 3-5 个 related_cards)

---

## 8. 工程纪律(继承)

- 文件 .md 已 OCR(624KB,单长行,无 OCR 错字)
- 主上下文 Python offset 切片读取
- 反向审计每段必做
- YAML 验证: 列表项不能以 `**` 开头(Phase 4 教训)
- 字段含 `"` 必须用 `'..."..."'` 单引号包裹
- **本次特别**:不存在 ID 撞、related_cards 引用 C-S1-005 → 修复改 C-S1-007 / C-S1-003

---

## 9. 立场对照(本次产出实测)

### 9.1 蒙氏 vs 已有源对照表

| 主题 | Davies 蒙氏 | 现有源 | 立场 |
|---|---|---|---|
| swaddle 包裹 | C-S1-187 不主张 | Karp C-S1-007/013-015 主张 | **直接对立** |
| floor bed | C-S3-133 主张 | AAP C-S1-016 仰睡 | **兼容**(蒙氏遵守 AAP) |
| 反应回应 | C-S1-190 不会宠坏 | Bowlby C-S1-127 / Karp C-S1-007 | **三派一致** |
| 跃迁期严格 | C-S6-133 温柔边界 | Wonder Week C-S6-126 不打不骂 + Bowlby C-S6-070 + 鲍秀兰 C-S6-007 | **四派一致** |
| 6 月固食 | C-S3-135 5 信号 | AAP C-S3-001 readiness | **完全一致** |
| 学步车 | C-S4-132 反对 | AAP C-S4-005 反对 | **双背书** |
| 屏幕 | C-S6-132 反对 | AAP 立场 | **双背书** |
| 自喂 BLW | C-S5-133 主张 | AAP C-S4-001 BLW 接受 | **一致** |
| 秩序敏感期 | C-S4-134 6-9 月 | Wonder Week C-S4-127 6-8 月拒绝换尿布 | **机制不同但现象一致** |

### 9.2 蒙氏独有维度(填补现库空缺)

#### 蒙氏 0-3 哲学
- C-S5-131 不替宝宝做 — 蒙氏黄金原则,现库首次明确
- C-S5-132 alternatives to praise — 不夸奖,跟 Carol Dweck 成长型思维一致
- C-S2-129 不打断专注 — 1 月起练专注力的方法论

#### 蒙氏环境工程
- C-S0-009 起步装清单 — 9 件物代替 8000 件,反消费主义
- C-S4-130 yes space 替代 playpen — 整屋安全 vs 关在围栏
- C-S3-133 floor bed — 跟 AAP 兼容的睡眠方案

#### 蒙氏共生期工具
- C-S1-185 topponcino — 解决"放下就醒"的物理工具
- C-S1-186 不戴手套 — 手是新生儿 orientation
- C-S1-188 慢动作换尿布 — 尊重的最早体验

#### 蒙氏 practical life(生活技能)
- C-S4-131 7-8 月自取水
- C-S5-133 10-12 月自喂手指食
- C-S6-130 12-15 月生活技能起步

### 9.3 蒙氏 vs 中文文化常见误解

| 中文常见误解 | Davies 蒙氏数据 | 卡片 ID |
|---|---|---|
| "宝宝必须戴手套防抓花" | 反:手是新生儿 orientation,抓花会自愈 | C-S1-186 |
| "一哭就抱会宠坏" | 反:6 月以下不存在宠坏,反应快宝宝反而独立 | C-S1-190 |
| "用塑料碗免摔" | 反:用真碗 / 真勺,蒙氏 practical life | C-S5-133 / C-S6-130 |
| "学步车走得早" | 反:走得反而晚 + DDH 风险 | C-S4-132 |
| "夸宝宝聪明" | 反:夸天赋 → 怕失败,夸过程 → 接受挑战 | C-S5-132 |
| "iPad 救星" | 反:2 岁前任何屏幕 = 语言 / 专注 / 睡眠损伤 | C-S6-132 |
| "宝宝 6-9 月挑剔 = 性格" | 反:健康的秩序敏感期 | C-S4-134 |
| "替宝宝做更快" | 反:剥夺自主性建立,长期 = 习得性无助 | C-S5-131 |

---

## 10. 改进建议(给后续 Phase 6 接手)

1. **接 Lillard《Montessori from the Start》** — 0-3 完整蒙氏,跟 Davies 形成蒙氏闭环 ⭐ 推荐
2. **接 Pikler / Gerber(RIE 派)** — yes space 概念溯源(Gerber 命名),floor bed 同根
3. **接 Bowlby Vol 3《丧失》** — 完成依恋三部曲
4. **接 Stern / Gopnik** — 自我感 / 认知科学,跟蒙氏 absorbent mind 对话
5. **补术语:G-PERSON-Uzodike(Junnifa)** — 本卷合著者,尼日利亚蒙氏教师
6. **补术语:G-PERSON-Gerber(Magda)** — yes space 命名者,RIE 创始人
7. **补术语:G-TERM-cestina** — 蒙氏摩西篮,跟 topponcino 配套
8. **补术语:G-TERM-practical-life** — 1-3 岁蒙氏核心(本卷已多处引用)

---

## 11. 跟 Phase 4 教训对比

| Phase 4 教训 | Phase 5 应对 |
|---|---|
| YAML alias **`**`** 开头陷阱 | ✅ 本次 0 出现 |
| 中文双引号引发 mapping 错误 | ✅ 全用单引号包外 |
| related_cards 占位符 / 自引用 | ✅ 自动检验 + 即时修(2 处 C-S1-005 → 改 C-S1-007/003)|
| 学究词残留 | ✅ Python 扫描 23 处 → 全改 |
| 字数超标 | ✅ Python 扫描 24 处 → 全改 |
| 跨源关联手动 | ✅ 已主动标连 36 张卡 |

---

*v1.0 · 2026-05-03 — Phase 5 Davies 蒙氏 0-1 完整记录*
*基于 PHASE4 教训 + 严格审查工作流升级*
*蒙氏理论首次全面入库,准备 Phase 6 蒙氏闭环 / RIE / 依恋三部曲收官*
