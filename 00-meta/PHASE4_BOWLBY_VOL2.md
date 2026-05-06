# Phase 4 执行任务书 · Bowlby《依恋三部曲 · 第二卷:分离》

> 项目代号:parenting-kb · Phase 4 第一本 · 版本 v1.0 (2026-05-03)
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE4_BOWLBY_VOL2.md)
> 2. `00-meta/PHASE3_BOWLBY_VOL1.md` + checkpoints(Vol 1 工程经验)
> 3. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)+ `PHASE1_KARP.md` §10(实战 14 条)

---

## 0. 一句话任务

抓 Bowlby《依恋三部曲 · 第二卷:分离》中文版,产 **30 张 v3.5 中文白话卡** + 6 张术语卡。
**全自动模式**(用户要求一次性跑完,不分段问审)。

---

## 1. 选定的书 + 来源

**John Bowlby《Attachment and Loss · Vol 2: Separation, Anxiety and Anger》**(《依恋三部曲 · 第二卷:分离》)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/bowlby_separation_zh.md`(中译已 OCR,950KB)|
| 作者 | John Bowlby(英国精神病学家,1907-1990)|
| 译者 | 汪智攀 / 王婷婷 |
| 流派 | Tier 3 理论原典(发展心理学奠基) |
| 范围 | 主要 1.5-3 岁(Robertson 研究样本年龄) |
| 出版 | 原版 1973,中译 2017,世界图书出版公司北京分公司 |
| ISBN | 978-7-5192-2926-9 |

### 为什么是 Vol 2(Phase 4 第一本)

1. **接续 Vol 1** — Internal Working Model 在 Vol 2 才正式定义
2. **抗议-绝望-超脱 3 阶段** — 住院 / 异地分离场景的家长实操指南
3. **焦虑型依恋的成因诊断** — 中文文化"再不听话就走"是高频精神虐待
4. **角色倒置(role reversal)** — 中文"懂事孩子"现象的理论解释
5. OCR 已就位,工程开销低

---

## 2. 段定义(继承 Phase 3)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S1 | 0-1 月 | s1-newborn | 0 张 |
| S2 | 1-3 月 | s2-1to3mo | 0 张 |
| S3 | 3-6 月 | s3-3to6mo | 0 张 |
| S4 | 6-9 月 | s4-6to9mo | 0 张 |
| S5 | 9-12 月 | s5-9to12mo | 4 张 |
| S6 | 12-24 月 | s6-12to24mo | 17 张 |
| S7 | 24-36 月 | s7-24to36mo | 9 张 |
| **总计** | | | **30 张** |

**段分布解释**:Vol 2 的 Robertson 研究样本是 13-32 月 + 拒学症研究 6-15 岁 →
本卷家长应用主要落在 S5-S7(尤其 S6/S7),S1-S4 不出卡(Vol 1 已覆盖)。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Vol 1 自审实战调整:
- 字段无上限(用户已说),但 `what_to_do` 单条 ≤35 字
- 学究词主动改白话(参 Vol 1 自审清单)
- 列表项不能以 `**` 或 `"` 开头(YAML alias 陷阱)
- 字符串含冒号必须加引号

### 评级 evidence_level 标尺(继承 Vol 1)

- **A**:与 Tier 1 共识对齐 OR Robertson / Bowlby 系列大型实证
- **B**:Bowlby 引用具体研究(Heinicke / Yarrow / Hersov / Coopersmith 等)
- **C**:Bowlby 个人推断(罕用)

实测产出:**A=12 / B=18 / C=0** 张

---

## 4. ID 隔离

并行 session 已停,但保留 +10 buffer 防漏写。
本次 session 起始 ID:
- S5: 086(原 max=076 + 10)
- S6: 082(原 max=072 + 10)
- S7: 034(原 max=024 + 10)

实测产出:
- S5: C-S5-086 ~ 089(4 张)
- S6: C-S6-082 ~ 098(17 张)
- S7: C-S7-034 ~ 042(9 张)
- 总计 30 张

---

## 5. 工作流(全自动)

### 5.1 章节地图(本卷 22 章 / 4 部分)

| 部分 | 章节 | 产卡数 |
|---|---|---|
| 1. 安全焦虑与困扰 | Ch 1-4(Robertson 观察) | 12(高产) |
| 2. 焦虑与恐惧理论 | Ch 5-12 | 4 |
| 3. 焦虑型依恋 | Ch 13-19(成因 + 病理) | 9 |
| 4. 家庭背景 + 安全依恋 | Ch 20-22(预测 + 治疗) | 5 |

### 5.2 chunk 切片(Python offset)

```python
# 主上下文逐 chunk 读
chunks = [
    (15326, 32000),    # Ch 1 Robertson
    (32000, 50000),    # Ch 2 精神病学
    (50000, 66000),    # Ch 3 实验
    (97500, 118000),   # Ch 7 唤起恐惧
    (180000, 200000),  # Ch 14-15 焦虑型成因
    (210000, 225000),  # Ch 16 反驳溺爱
    (225934, 245000),  # Ch 18 学校恐怖症
    (279000, 300000),  # Ch 21 安全依恋成长
]
```

### 5.3 反向覆盖审计

每 chunk 跑反向审计,列"父母从分离视角必须知道的核心 N 件事",对比已写卡补漏。
本次实测:无重大遗漏。

---

## 6. 输出位置

```
parenting-kb/
├── 10-sources/tier3-books/notes/
│   └── SRC-012.yaml ✅(新建)
├── 30-cards/
│   ├── s5-9to12mo/         # C-S5-086..089 ✅
│   ├── s6-12to24mo/        # C-S6-082..098 ✅
│   └── s7-24to36mo/        # C-S7-034..042 ✅
├── 40-glossary/
│   ├── G-PERSON-Robertson.yaml ✅(新建)
│   ├── G-TERM-protest-despair-detachment.yaml ✅(新建)
│   ├── G-TERM-anxious-attachment.yaml ✅(新建)
│   ├── G-TERM-defensive-exclusion.yaml ✅(新建)
│   ├── G-TERM-pathological-mourning.yaml ✅(新建)
│   └── G-TERM-transitional-object.yaml ✅(新建,含 Vol 1 关联)
└── 00-meta/
    ├── PHASE4_BOWLBY_VOL2.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE4_BOWLBY_VOL2_20260503.md ✅
```

**不动**(等用户合并):
- ❌ `30-cards/INDEX_BY_SOURCE.md`
- ❌ `00-meta/progress.md`
- ❌ `10-sources/source_index.yaml`(虽然 next_src_id=SRC-012 已对,但保险不改)

---

## 7. 完成定义

- [x] 抓 Bowlby Vol 2 → SRC-012.yaml + raw MD 已就位
- [x] 产 30 张新卡(任务范围 30-50 张 ✓)
- [x] 新建 6 张术语卡(任务范围 ≥4 张 ✓)
- [x] 反向覆盖审计每 chunk 必做
- [x] checkpoint MD 完成
- [x] **不动 INDEX + progress + source_index**
- [x] 跨源 related_cards 标连(Vol 1 ↔ Vol 2 + 鲍秀兰 + AAP + Karp)
- [x] 全部 37 张 yaml 验证通过(Python yaml.safe_load 0 fail)
- [x] glossary_refs 全部存在
- [x] related_cards 全部存在
- [x] 学究词检查通过(2 个伪阳性,实际 0)

---

## 8. 关键约束(全部遵守)

1. ✅ 不动现有 220+ 知识卡 + 75+ 术语卡(Brazelton + Bowlby Vol 1 完成后基线)
2. ✅ ID +10 buffer(并行已停,保险)
3. ✅ 不动 INDEX + progress + source_index
4. ✅ 新卡严格 v3.5 schema(前情提要 + glossary_refs + 白话)
5. ✅ 立场对照不判对错:Bowlby Vol 2 vs Karp / AAP / 鲍秀兰 = 不同维度
6. ✅ 主上下文产出,不派生 subagent
7. ✅ 全自动跑完,中间不问用户

---

## 9. 工程纪律(本次实战)

### YAML 陷阱(Vol 1 经验)

1. **列表项不能以 `**` 开头**(已避免)
2. **字符串含冒号必须加引号**(已避免)
3. **列表项以 `"` 开头会被解析为引用字符串**(本次踩坑 6 次,已修复)
4. **数字嵌套子列表慎用**(已避免)
5. **`front:` 别打成 `front>`**(本次踩坑 2 次,已修复)

### OCR 修正

Vol 2 OCR 错字模式:
- "丽惧 / 铠惧 / 慌惧 / 恕怖 / 恺怖 / 怠惧 / 邵怖 / 妨惧 / 慄惧" 等都是"恐惧 / 恐怖"
- "卯独"未发现
- "狒狒"OCR 偶有失败
- 字间空格断裂频繁
- 上下文推断为主,不一一标记

---

## 10. 立场对照(Vol 2 主要贡献)

### 10.1 Bowlby Vol 2 与 Vol 1 的衔接

| 主题 | Vol 1 | Vol 2 |
|---|---|---|
| 依恋本能 | C-S1-122..128 提出 | (默认基础) |
| Internal Working Model | C-S6-069 提及 | **正式定义并应用** |
| 4 类依恋 | C-S5-070..073 | (在分离场景下深化) |
| 安全依恋好处 | C-S5-071 | C-S6-097 / C-S7-042 量化 |
| 体罚危害 | C-S6-070 / C-S6-072 | C-S6-098 加深(撤回爱) |

### 10.2 Vol 2 独有维度

- **抗议-绝望-超脱 3 阶段**(C-S6-082)— 现库首次完整描述长分离反应
- **Robertson 5 招** 实操指南(C-S7-034)— 住院场景父母手册
- **角色倒置**(C-S6-093)— 中文"懂事孩子"的理论解释
- **隐瞒病故反加重恐惧**(C-S6-096)— 反中文文化默认
- **拒学 vs 逃学**区分(C-S7-041)— 临床诊断
- **怕黑可能是怕妈走**(C-S7-040)— 投射机制揭示

### 10.3 反"溺爱论"全面证实(C-S6-095)

Bowlby Vol 2 第十六章直接挑战 Freud 1905-1926 主流的"过度爱 → 宠坏 → 焦虑"理论:
- Maccoby & Masters 1970 综述否定
- Stendler 1954:14/20 "过度依赖"儿童来自不稳定家庭(不是过度爱)
- 灵长类研究也支持反对
- "焦虑型依恋"取代"过度依赖"(C-S6-095 + G-TERM-anxious-attachment)

---

## 11. 改进建议(给后续 Phase 5 接手)

1. **Bowlby Vol 3《丧失》** — 病理性哀伤系统化,儿童丧亲场景
2. **Ainsworth 1978《Patterns of Attachment》** — Strange Situation 实验设计细节
3. **Lillard / Davies 蒙台梭利系列** — 环境设计维度
4. **Gerber / Lansbury RIE 派** — 尊重式育儿,直接基于 Pikler / Bowlby

---

*v1.0 · 2026-05-03 — Phase 4 第一本 完整记录*
*基于 PHASE3_BOWLBY_VOL1 v1.0 schema + 工程经验*
*全自动模式,无 subagent 派生*
