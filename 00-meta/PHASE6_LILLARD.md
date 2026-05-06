# Phase 6 第二本 · Lillard 蒙氏 0-3 学院派

> 项目代号:parenting-kb · Phase 6 第二本(2026-05-03)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读**(按顺序):
> 1. 本文件(PHASE6_LILLARD.md)
> 2. `00-meta/PHASE5_MONTESSORI_BABY.md`(Davies 实操,Lillard 是其学院派续集)
> 3. `00-meta/checkpoints/checkpoint_PHASE5_DAVIES_AUDIT_20260503.md`(二审教训)
> 4. `00-meta/checkpoints/checkpoint_PHASE6_LILLARD_20260503.md`(本卷产出)
> 5. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)
> 6. `00-meta/PHASE1_KARP.md` §10(14 条实战教训)

---

## 0. 一句话任务

抓 Paula Polk Lillard + Lynn Lillard Jessen《Montessori from the Start》(蒙氏 0-3 学院派经典 2003),产 **46 张 v3.5 中文蒙氏卡** + 8 张术语卡。**蒙氏 0-3 闭环完成**(Davies 实操 + Lillard 理论)。

---

## 1. 选定的书 + 来源

**Paula Polk Lillard + Lynn Lillard Jessen《Montessori from the Start: The Child at Home, from Birth to Age Three》**(蒙台梭利从 0 岁开始 — 0-3 岁的教育)

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/lillard_montessori_from_the_start.md`(528KB,.epub 转 .md)|
| 作者 | Paula Polk Lillard(AMI primary 蒙氏教师 / Forest Bluff School 共办)+ Lynn Lillard Jessen(AMI 0-3 双认证,Paula 女儿)|
| 流派 | Tier 3 / 蒙氏 0-3 学术深度派 |
| 范围 | 0-3 岁完整(比 Davies 0-1 更广 + 更深)|
| 出版 | 原版 2003 英文,Schocken Books(纽约)|
| ISBN_en | 978-0-8052-1112-1 |
| 中译本 | 有(《蒙台梭利从 0 岁开始 — 0-3 岁的教育》)|

### 为什么这本(Phase 6 选择)

1. **蒙氏 0-3 闭环** — 跟 Davies(0-1)合起来 = 蒙氏 0-3 全段 + 哲学 + 实操双轨
2. **学院深度** — Paula 是 AMI 资深教师,引经据典(Csikszentmihalyi flow / Lise Eliot 神经科学)
3. **覆盖 1-3 岁**(Davies 主要 0-1)— 填补现库 1-3 岁的蒙氏空白
4. **系统化"意志"理论**(Davies 没明确)— Ch9 是全本最深章
5. **OCR 已就位**(.epub 转 .md,无 OCR 错字)

---

## 2. 段定义(本次产出)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S0 | 孕期 | s0-pregnancy | 3 张(C-S0-012..014)|
| S1 | 0-1 月 | s1-newborn | 6 张(C-S1-247..252)|
| S2 | 1-3 月 | s2-1to3mo | 5 张(C-S2-185..189)|
| S3 | 3-6 月 | s3-3to6mo | 5 张(C-S3-191..195)|
| S4 | 6-9 月 | s4-6to9mo | 5 张(C-S4-190..194)|
| S5 | 9-12 月 | s5-9to12mo | 6 张(C-S5-184..189)— 含二审补 1 |
| S6 | 12-24 月 | s6-12to24mo | 9 张(C-S6-184..192)— 含二审补 1,Lillard 最强段 |
| S7 | 24-36 月 | — | 7 张(C-S7-130..136)— Lillard 重点 vs Davies 没覆盖 |
| **总计** | | | **46 张** |

S6 + S7 共 16 张是 Lillard 重点 — 这是 Davies 缺失的部分,Lillard 给了完整 1-3 岁理论 + 实操。

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3/4/5 扩展。

### 评级 evidence_level(本书标尺)

Lillard 蒙氏 0-3 = 100 年 AMI 培训 + Lillard 母女 30+ 年实操 + 引现代科学:
- **A**:与 Tier 1 共识对齐(Lillard 跟 AAP / Bowlby / 现代神经科学吻合)
- **B**:Lillard / Jessen 引用研究 / AMI 100 年观察 / 自家案例
- **C**:Lillard 个人理论推断(罕见)

实测产出:**A=15 / B=31 / C=0** 张 — A 级 33%(高于 Davies 31%),反映 Lillard 学院深度。

---

## 4. 工作流(基于 Phase 5 教训改进)

### 4.1 章节地图(SRC-016.yaml 已记录)

Lillard 528KB / 10 章 + 序 + 结论 / 单长行 .md 文件。10 章正文起点:

```python
preface: 2883
introduction: 27628
ch1_completion_human_being: 46324
ch2_welcoming_newborn: 73019
ch3_discovering_world: 100376
ch4_hand_brain: 116612
ch5_crawling_coordination: 153844
ch6_practical_life: 202498
ch7_personal_care: 256728
ch8_language_intelligence: 353998
ch9_developing_will: 426036
ch10_conclusion: 473958
total_chars: 524871
```

### 4.2 chunk 策略

每章 15-50K 字符,Python `text[start:end]` 切片读取(主上下文)。Ch7 最长 97K,需拆 2 半。

### 4.3 反向覆盖审计(每章必做)

每段产卡完成后,主上下文从原文重列"父母从蒙氏视角必须知道的 N 件事",对比已写卡补漏。

实测二审补 2 张:
- C-S5-189:关门睡 + 不抱晃睡(Lillard Ch7 入睡哲学)
- C-S6-192:No 永远是 No(Lillard Ch9 限度核心)

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-015 Gopnik + SRC-016 Lillard + 改 next_src_id → SRC-017)✅
│   └── tier3-books/notes/
│       └── SRC-016.yaml ✅(新建)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-016 节 + 顶部目录表 + 总数 412 → 493)
│   ├── s0-pregnancy/      # C-S0-012..014 ✅(3)
│   ├── s1-newborn/        # C-S1-247..252 ✅(6)
│   ├── s2-1to3mo/         # C-S2-185..189 ✅(5)
│   ├── s3-3to6mo/         # C-S3-191..195 ✅(5)
│   ├── s4-6to9mo/         # C-S4-190..194 ✅(5)
│   ├── s5-9to12mo/        # C-S5-184..189 ✅(6,含二审补 1)
│   ├── s6-12to24mo/       # C-S6-184..192 ✅(9,含二审补 1)
│   └── s7-24to36mo/       # C-S7-130..136 ✅(7)
├── 40-glossary/(8 张新)
│   ├── G-PERSON-Lillard.yaml ✅
│   ├── G-PERSON-Jessen.yaml ✅
│   ├── G-TERM-self-construction.yaml ✅
│   ├── G-TERM-cycle-of-activity.yaml ✅
│   ├── G-TERM-coordinated-movement.yaml ✅
│   ├── G-TERM-language-explosion.yaml ✅
│   ├── G-TERM-points-of-reference.yaml ✅
│   └── G-TERM-weaning-table.yaml ✅
└── 00-meta/
    ├── progress.md ✅(更新累计 493 张 + Phase 6 完成记录)
    ├── PHASE6_LILLARD.md ✅(本文件)
    └── checkpoints/
        └── checkpoint_PHASE6_LILLARD_20260503.md ✅
```

---

## 6. 完成定义(实测)

- [x] 抓 Lillard《Montessori from the Start》全本(10 章)→ SRC-016.yaml + raw .md 已就位
- [x] 产 **46 张新卡**(任务范围 35-50 ✓ 偏上)
- [x] 新建 **8 张术语卡**(任务范围 5-8 ✓)
- [x] 反向覆盖审计补 2 张(关门睡 + No 永远是 No)
- [x] checkpoint MD 完成
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(无并行 session,直接更新)
- [x] 跨源 related_cards 标连(蒙氏 ↔ Davies ↔ Karp ↔ AAP ↔ Bowlby ↔ Brazelton ↔ Wonder Weeks ↔ 鲍秀兰 ↔ Gopnik)
- [x] 全部 46 张卡 YAML 验证通过(Python yaml.safe_load)
- [x] 全部 glossary_refs 指向存在的术语卡
- [x] 全部 related_cards 指向存在的知识卡(0 自引用 / 0 占位符)
- [x] **严格审查:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 学究词残留**

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 6 第二本通过。

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 412 + 35(Gopnik)= 447 张知识卡**
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - 蒙氏 vs 现代如厕训练:Lillard 12-18 月敏感期 vs 主流 2-3 岁(Lillard 立场强)
   - 蒙氏 vs 现代纸尿裤:Lillard 反 sauna 效应(Lillard 比 Davies 更强)
   - 蒙氏 vs 现代 happiness:Lillard 要 character(反主流但内省)
4. ✅ **白话风格**(避免学究腔)— 修 4 处学究词(突触/协调/维度)
5. ✅ **跨源主动标连**(46 张卡平均 3 个 related_cards)

---

## 8. 工程纪律(继承)

- 文件 .md 已 OCR(528KB,单长行,无 OCR 错字)
- 主上下文 Python offset 切片读取
- 反向审计每段必做
- YAML 验证: 列表项不能以 `**` 开头(Phase 4 教训)
- 字段含 `"` 必须用 `'..."..."'` 单引号包裹(Phase 5 二审踩坑)
- **本次特别**:Gopnik 并行 session 占用 SRC-015,Lillard 改用 SRC-016 + 检查 ID 范围

---

## 9. 立场对照(本次产出实测)

### 9.1 Lillard vs Davies(蒙氏内部)

Lillard 跟 Davies 几乎所有立场一致,但:
- Lillard **更深理论**(4 plane / 11 human tendencies / cycle of activity / 服从 3 阶段)
- Lillard **覆盖 S6/S7 1-3 岁**(Davies 主要 0-1)
- Lillard **立场更鲜明**(如纸尿裤 / 如厕敏感期 / happiness vs character)
- Davies **更友好** + **更现代**(适合"想试试" 的家长)
- Lillard **更学术** + **更鲜明**(适合"想理解为什么" 的家长)

### 9.2 Lillard 独有维度(填补 Davies 空缺)

#### 蒙氏哲学深度(Davies 没系统讲)
- C-S0-012 4 平面发展(0-24 岁完整)
- C-S0-013 蒙氏教育公式
- C-S6-186 母-师角色
- C-S7-136 观察 = 科学家方式

#### 蒙氏 1-3 岁实操(Davies 较弱)
- C-S6-184 15 月转工作
- C-S6-185 完整循环活动
- C-S6-187 演示步骤要慢 + 一致
- C-S7-133 2 岁切香蕉真钝刀
- C-S7-134 Tom Sawyer 法

#### 蒙氏意志 3 阶段(Davies 没分段)
- C-S6-188 给选 2 不给选 3
- C-S6-191 12-18 月物理移除
- C-S6-192 No 永远是 No
- C-S7-130 服从 3 阶段
- C-S7-131 3 岁是真"上学龄"

#### 蒙氏家庭系统(Davies 部分有)
- C-S0-014 爸爸 8 周缓冲器
- C-S1-249 头月 1 房 + 3 人
- C-S7-135 婚姻在孩子之前

#### 反潮流强立场(Lillard 比 Davies 更强)
- C-S6-189 12-18 月如厕敏感期(反 2-3 岁主流)
- C-S6-190 反纸尿裤 sauna 效应
- C-S2-189 0-6 岁只给真实(反卡通)
- C-S5-189 关门睡 + 不抱晃睡
- C-S7-132 蒙氏要"性格"非"幸福"

### 9.3 Lillard vs 中文文化常见误解

| 中文常见误解 | Lillard 数据反驳 | 卡片 ID |
|---|---|---|
| "如厕训练 2-3 岁正常" | 反:1950 年代 92% 18 月就完成,纸尿裤错过敏感期 | C-S6-189 + C-S6-190 |
| "宝宝小不能用真刀" | 反:2 岁钝刀 + 监护可切香蕉(蒙氏 100 年实证)| C-S7-133 |
| "孩子幸福第一" | 反:character + discipline 才是真长期幸福 | C-S7-132 |
| "全家围着孩子转" | 反:婚姻才是基础,孩子是建在上面 | C-S7-135 |
| "妈妈陪睡到 5 岁正常" | 反:从婴儿期就建自我入睡能力 | C-S5-189 |
| "宝宝玩两下就好" | 反:完整循环(准备 + 做 + 收尾)才是教育 | C-S6-185 |
| "卡通启蒙好" | 反:0-6 岁只给真实,卡通让宝宝学到"无后果"| C-S2-189 |

---

## 10. 改进建议(给后续 Phase 7 接手)

1. **Bowlby Vol 3《丧失》** — 完成依恋三部曲 ⭐ 推荐
2. **Stern《婴儿人际世界》** — 自我感 4 阶段,跟蒙氏 absorbent mind 对话
3. **Pikler《Friedliche Babys》** — floor bed / movement freedom 同根
4. **Gerber 自信的宝宝 / Lansbury** — RIE 派,yes space 命名者
5. **Shonkoff** — 哈佛 Center on the Developing Child 综述
6. **WHO 0-3 标准** — 全球公共卫生视角
7. **松田道雄《育儿百科》** — 日本经典,跟蒙氏对照
8. **海蒂百科** — 主流大众参考

---

## 11. 跟 Phase 5 教训对比

| Phase 5 教训 | Phase 6 应对 |
|---|---|
| YAML 引号嵌套陷阱 | ✅ 主动用单引号包(C-S7-136 + G-TERM-self-construction 各 1 处)|
| hook 字数 8-12 严格 | ✅ Python 扫 + 修 21 处 |
| title ≤ 15 严格 | ✅ Python 扫 + 修 5 处 |
| 学究词主动改 | ✅ Python 扫 + 修 4 处(突触 / 协调 / 维度 x2)|
| 反向覆盖审计每章 + 收官 | ✅ 收官前补 2 张高价值漏卡 |
| 跨源关联手动 | ✅ 主动标连 46 张卡(平均 3 个 related)|
| 章节扫描列全清单 | ✅ 10 章 + Intro 全部 offset 确认 |

---

## 12. 工程意外(Phase 6 第二本特有)

### 意外 1:Gopnik 并行 session 占用 SRC-015
- 启动时 next_src_id=SRC-015,但实际 SRC-015 已被 Gopnik 用
- **修复**:Lillard 改用 SRC-016 + 在 source_index.yaml 加 SRC-015 + SRC-016 entry + 改 next_src_id → SRC-017
- **教训**:多 session 并行时,启动前要 `ls 10-sources/tier3-books/notes/` 实际查 SRC 文件,不只看 source_index.yaml 的 next_src_id

### 意外 2:Gopnik 部分 ID 范围
- Gopnik 用了 S4 184-189 — 我之前算 S4 起点要重扫
- **修复**:重新 ls 30-cards 各段确认实际 max,改 S4 起点为 190(原以为 189)+ S7 改 130(原以为 129)

### 意外 3:hook 字数集中 7 字符
- 21 处 hook 是 7 字符(刚好不到 8 字)
- **教训**:写卡时主动检查"是否 8-12 字" — 7 字符是常见陷阱

### 意外 4:学究词残留 4 处
- 修复后 0 残留

### 意外 5:误创 backup 文件
- 写卡时手滑创建了 C-S7-131_NEW_BACKUP_DELETE.yaml
- **修复**:rm 删除

---

*v1.0 · 2026-05-03 — Phase 6 Lillard 蒙氏 0-3 学院派完整记录*
*基于 Phase 5 Davies 教训 + Gopnik 并行 session ID 隔离学到*
*蒙氏 0-3 闭环完成(Davies 实操 + Lillard 理论),准备 Phase 7 依恋三部曲 / 认知科学拓展 / RIE 派*
