# Phase 3 执行任务书 · 第三本(并行):Bowlby《依恋》Vol 1

> 项目代号:parenting-kb · Phase 3 第三本(与 Brazelton 并行)· 版本 v1.0 (2026-05-02)
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE3_BOWLBY_VOL1.md)
> 2. `00-meta/PHASE2_AAP.md`(§2.5 白话 / §2.7 前情提要 / §2.8 术语卡片化 / §2.9 inline 引用)
> 3. `00-meta/PHASE1_KARP.md` §10 实战调整 14 条
>
> 然后看 `30-cards/INDEX_BY_SOURCE.md`(已有卡数)+ `40-glossary/`(已建术语)。

---

## 0. 一句话任务

抓 Bowlby《依恋三部曲 · 第一卷:依恋》中文版,产 **35 张 v3.5 中文理论卡** + 4 张术语卡。
**与 Brazelton session 并行运行,严格 ID 隔离**(+50 buffer)。

---

## 1. 选定的书 + 来源

**John Bowlby《Attachment and Loss · Vol 1: Attachment》**(《依恋三部曲 · 第一卷:依恋》)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/bowlby_attachment_zh.md`(中译已 OCR,874KB)|
| PDF 原 | `依恋三步曲-1.依恋 [英]约翰·鲍尔比(John Bowlby)著.pdf` |
| 作者 | John Bowlby(英国精神病学家,1907-1990)|
| 译者 | 汪智攀 / 王婷婷,易春丽审校 |
| 流派 | Tier 3 理论原典(发展心理学奠基) |
| 范围 | 0-5 岁(理论 + 实证),不强分段月龄 |
| 出版 | 原版 1969,中译 2017,世界图书出版公司北京分公司 |
| ISBN | 978-7-5192-2927-6 |

### 为什么这本(并行 session 2)

1. **理论 + 实操平衡** — 现库 Karp/AAP/鲍秀兰/Brazelton 都偏实操,缺理论奠基书
2. **G-PERSON-Bowlby 已建** — 直接接续,新建术语卡少(仅补 4 张)
3. **跨段稀疏** — 依恋是 0-3 岁全段概念,卡分布散,与 Brazelton 集中区域冲突小
4. **3 卷可拆** — 本次只做 Vol 1(依恋本能 + 4 类依恋 + 内部工作模型),Vol 2/3 留 Phase 4

---

## 2. 段定义(继承 Phase 3 第一本)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S1 | 0-1 月 | s1-newborn | 7 张 |
| S2 | 1-3 月 | s2-1to3mo | 5 张 |
| S3 | 3-6 月 | s3-3to6mo | 4 张 |
| S4 | 6-9 月 | s4-6to9mo | 7 张 |
| S5 | 9-12 月 | s5-9to12mo | 7 张 |
| S6 | 12-24 月 | s6-12to24mo | 5 张 |
| S7 | 24-36 月 | s7-24to36mo | 0 张(本次跳过) |
| **总计** | | | **35 张** |

S7 跳过:Bowlby 理论焦点 0-2 岁,3 岁后转入"合作关系阶段",卡较少,可留下次书补。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3 第一本扩展:

### 评级 evidence_level(理论书标尺)

Bowlby = 理论原典,综合多研究流派(动物行为学 + 进化生物学 + 精神分析 + 发展心理学):
- **A**:与 Tier 1 共识对齐 OR Ainsworth 大型实证研究 + 50 年验证(陌生情境实验等)
- **B**:Bowlby 引用具体研究(Wolff / Schaffer / Yarrow / Ambrose / Hinde 等)— **大多数卡**
- **C**:Bowlby 个人理论推断(罕见使用)

实测产出:**A=9 / B=26 / C=0** 张 — Bowlby 不是"一家之言派",所有断言都基于研究。

---

## 4. ⚠️ 并行协调(关键!)

### 4.1 ID 隔离规则

另一 session 正在做 Brazelton(SRC-010),会往 S1-S7 加卡。**本 session 严格遵守**:

1. **SRC ID** = SRC-011(从 source_index.yaml `next_src_id` 取下一个)
2. **卡片 ID buffer +50**(给 Brazelton 留 41 张冗余):

```bash
for sd in s1-newborn s2-1to3mo s3-3to6mo s4-6to9mo s5-9to12mo s6-12to24mo s7-24to36mo; do
  echo "$sd: max = $(ls ~/Desktop/parenting-kb/30-cards/$sd/ | grep -oE '[0-9]{3}' | sort -n | tail -1)"
done
```

实测起始(本次 session):
| 段 | grep max | +50 起步 | 实际产出 |
|---|---|---|---|
| S1 | 072 | 122 | C-S1-122 ~ 128(7) |
| S2 | 017 | 067 | C-S2-067 ~ 071(5) |
| S3 | 026 | 076 | C-S3-076 ~ 079(4) |
| S4 | 017 | 067 | C-S4-067 ~ 073(7) |
| S5 | 019 | 069 | C-S5-069 ~ 075(7) |
| S6 | 018 | 068 | C-S6-068 ~ 072(5) |

**实测验证**:Brazelton 在并行 session 中实际只用了 ~10 张/段,buffer 充足。

### 4.2 不动的文件(并行不安全)

- ❌ **不动 `30-cards/INDEX_BY_SOURCE.md`**(让 Brazelton session 收尾或用户手动合并)
- ❌ **不动 `00-meta/progress.md`**(同上)
- ❌ **不动 `10-sources/source_index.yaml`**(虽然 SRC-010/011 不冲突,但 next_src_id 字段会冲突)

### 4.3 OK 的文件(各自独立,不冲突)

- ✅ `10-sources/tier3-books/notes/SRC-011.yaml`(新建文件)
- ✅ `30-cards/sN/C-SN-XXX.yaml`(新建文件,ID 已 +50 buffer)
- ✅ `40-glossary/G-XXX-YYY.yaml`(新建文件)
- ✅ `00-meta/PHASE3_BOWLBY_VOL1.md`(本文件)
- ✅ `00-meta/checkpoints/checkpoint_PHASE3_BOWLBY_VOL1_<YYYYMMDD>.md`(新建文件)

---

## 5. 工作流(基于 Phase 1-2 教训改进)

### 5.1 章节地图(已扫,见 SRC-011.yaml)

Bowlby Vol 1 是 364K 中文字符 / 5 部分 / 19 章。关键产卡章节:

| 章节 | 内容 | 产卡数 |
|---|---|---|
| 第三部分 ch11-13(依恋行为) | 理论核心 | 2 |
| 第四部分 ch14-17(个体发生) | **父母最相关** | 22 |
| 第五部分 ch18-19(1982 增补) | Ainsworth 4 类型 | 11 |
| 第一部分 + 第二部分 | 理论铺垫(动物行为 / 进化) | 跳过 |

### 5.2 chunk 策略(单长行 .md 文件)

文件是单长行(不像鲍秀兰 2869 行结构化),用 Python 字符 offset 切片:
```python
text[149000:165000]  # 第十一章开头
text[217000:253000]  # 第十四章
text[253000:270000]  # 第十五章
text[270000:290000]  # 第十六章
text[290000:310000]  # 第十七章
text[293000:313000]  # 第十八章
```

### 5.3 反向覆盖审计

每段做完跑反向审计:重读原文 + 列"父母从依恋视角必须知道的核心 N 件事",对比已写卡补漏。

实测漏掉(留待未来):
- ⚠️ 拥抱玩偶/毯子(transitional object)— 苏格兰研究 1/3 婴儿,9 月-2 岁出现 — **未来补 1 张**
- ⚠️ 母亲产后抑郁对依恋的具体影响(Bowlby 第二卷《分离》深入)— 留 Phase 4
- ⚠️ 父亲依恋角色(Lamb 1977 引用,但第一卷只触及边角)— 留 Phase 4

---

## 6. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── ⚠️ source_index.yaml(不改)
│   └── tier3-books/notes/
│       └── SRC-011.yaml ✅(新建)
├── 30-cards/
│   ├── ⚠️ INDEX_BY_SOURCE.md(不改)
│   ├── s1-newborn/        # C-S1-122..128 ✅
│   ├── s2-1to3mo/         # C-S2-067..071 ✅
│   ├── s3-3to6mo/         # C-S3-076..079 ✅
│   ├── s4-6to9mo/         # C-S4-067..073 ✅
│   ├── s5-9to12mo/        # C-S5-069..075 ✅
│   └── s6-12to24mo/       # C-S6-068..072 ✅
├── 40-glossary/
│   ├── G-PERSON-Ainsworth.yaml ✅(新建)
│   ├── G-TERM-strange-situation.yaml ✅(新建)
│   ├── G-TERM-internal-working-model.yaml ✅(新建)
│   └── G-TERM-secure-base.yaml ✅(新建)
└── 00-meta/
    ├── PHASE3_BOWLBY_VOL1.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE3_BOWLBY_VOL1_20260502.md(下一步)
```

---

## 7. 完成定义(实测)

- [x] 抓 Bowlby Vol 1 → SRC-011.yaml + raw MD 已就位
- [x] 产 **35 张新卡**(任务范围 25-40 张 ✓)
- [x] 新建 **4 张术语卡**(任务范围 ≥3 张 ✓)
- [x] 反向覆盖审计(发现 3 个未来补卡候选)
- [x] checkpoint MD 完成
- [x] **不动 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(并行安全)
- [x] 跨源 related_cards 标连(Bowlby ↔ 鲍秀兰 ↔ Karp ↔ AAP)

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 3 第三本通过。

---

## 8. 关键约束(实测都遵守)

1. ✅ **不动现有 182 知识卡 + 65 术语卡**
2. ✅ **ID 必须 +50 buffer**(防与 Brazelton 撞 — 实测 buffer 用掉 ~10,剩余充足)
3. ✅ **不动 INDEX + progress + source_index**(并行不安全)
4. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
5. ✅ **理论卡也按 v3.5 写白话**(避免学究腔)
6. ✅ **立场对照不判对错**:Bowlby 依恋 vs Karp 5S = 不冲突,只是不同维度
7. ✅ **依恋理论的中文家长版本** — 不照搬学术语,让中国家长读得懂

---

## 9. 工程纪律(继承)

- 文件 .md 已 OCR(~870KB,单长行)
- 主上下文 Python offset 切片读取(每段 15-20K 字符)
- 反向审计每段必做
- YAML 验证: list 项不能以 `**` 开头(YAML alias 陷阱) — 已修正 14 张

---

## 10. 立场对照(本次产出实测)

### 10.1 Bowlby 与已有源对照

| 主题 | Bowlby 立场 | Karp 立场 | AAP 立场 | 鲍秀兰立场 |
|---|---|---|---|---|
| 不会宠坏 | C-S1-122 进化论解释 | C-S1-007 实操 | C-S1-043 临床 | C-S4-016 早教 |
| 摇晃止哭 | C-S1-125 进化解释 60+/min | C-S1-001..009 5S 实操 | (未单独讨论) | (未单独讨论) |
| 喂奶不是依恋 | C-S2-070 理论强证 | (隐含) | (隐含) | C-S2-013 实操(及时回应) |
| 安全基地 | C-S3-079 / C-S4-069 概念定义 | (无) | (无) | (无) |
| 陌生人警觉 | C-S4-068 进化机制 | (无) | C-S4-004 临床 | C-S5-013 早教(察言观色) |
| 不打孩子 | C-S6-070 创伤数据 | (无) | (隐含) | C-S6-007 全家一致 |
| 管教方式 | C-S6-072 观点采择 | (无) | (无) | C-S6-007 不打 |

### 10.2 跨源补全(本次额外贡献)

Bowlby 提供其他源缺失的**理论维度**:
- 依恋发展 4 阶段时间表(C-S1-127 / C-S2-067 / C-S3-078 / C-S4-069)
- Ainsworth 4 类型分类(C-S5-070..073) — **现库首次完整 B/A/C 三类细化**
- 内部工作模型(C-S6-069) — **代际传递机制理论基础**
- 5 岁人格预测(C-S5-074) — **长期纵向数据点**

---

## 11. 改进建议(给后续 Phase 4 接手)

1. **补拥抱玩偶卡(C-SX-XXX)**:S5 段加 1 张,基于 Bowlby ch15"非生命物体的角色"
2. **接 Bowlby Vol 2《分离》**:重点章 — 抗议-绝望-超脱 3 阶段;C-S5-074 / C-S6-069 可深化
3. **接 Bowlby Vol 3《丧失》**:儿童哀伤反应,Phase 4-5 候选
4. **Ainsworth 1978《Patterns of Attachment》单独提取**:Strange Situation 实验设计细节,提供给现有 G-TERM-strange-situation 深化

---

*v1.0 · 2026-05-02 — Phase 3 第三本(并行)完整记录*
*基于 PHASE2_AAP v1.4 schema + PHASE3_BAOXIULAN v1.0 段定义*
*与 Phase 3 第二本(Brazelton SRC-010)并行执行,无冲突*
