# Checkpoint · Phase 8 Gerber 4 轮独立审 + 漏知识反向覆盖记录(2026-05-03)

> 项目:parenting-kb · Phase 8 并行第二本 · 4 轮独立审独立报告
> 启动:2026-05-03(主任务收官时)
> 完成:2026-05-03 同日
> 上次产出:`checkpoint_PHASE8_GERBER_20260503.md`(初+二审 30 张)

---

## 0. 一句话总结

**Phase 8 Magda Gerber 4 轮独立审完整跑完,继承 Phase 7 Lansbury 用户三审框架(YAML 机器审 / 漏知识反向覆盖 / 漏术语扫 / 用户三审 3 维度)。漏知识反向覆盖发现 2 张高价值漏知识(必补)+ 用户三审发现 2 处描述型 hook(必修)。Gerber 卡总数 30 → 32 张,跨源率 100%,Lansbury related 100%。**

---

## 1. 4 轮独立审框架(继承 Phase 7)

```
轮 1 = Python 机器审(YAML / 字数 / 学究词 / refs)
轮 2 = 漏知识反向覆盖(每章 spot-check)
轮 3 = 漏术语扫
+ 轮 4 = 用户三审 3 维度(hook 风格 / 跨源率 / 章节 spot-check)
```

---

## 2. 轮 1:Python 机器审结果

### 2.1 初次跑(发现 21 处)

| 维度 | 错数 | 详情 |
|---|---|---|
| YAML 错 | 6 | C-S0-316 / C-S0-317 / C-S1-558 / C-S5-594 / C-S6-608 / C-S7-553 — 全部因 `- "..."` 引号嵌套 |
| title > 15 字 | 0 | — |
| hook 不在 8-12 字 | 8 | 7 字(7 处)+ 13-18 字(1 处) |
| wtd > 35 字 | 0 | — |
| 学究词残留 | 7 | 认知(2)/ 内化(3)/ 机制(2)/ 人格(1) |
| ref 缺失 | 0 | — |
| 0 跨源孤岛 | 0 | — |
| 缺 Lansbury | 0 | 100% 卡有 Lansbury related 一开始就建立 |

### 2.2 修复后(0 错)

所有 21 处修复:

#### YAML 引号修复(6 处)
- 全部 `- "..."` → `- 「...」`(中文引号)
- YAML parser 不再把 `"` 解释成 quoted scalar 起始

#### Hook 字数修复(8 处)
| Card | 旧 hook | 字数 | 新 hook | 字数 |
|---|---|---|---|---|
| C-S1-557 | 等他三十年再 Primal Scream | 18 | 别说别哭等长大去治疗 | 11 |
| C-S2-493 | Lansbury 后来扩到 10 | 14 | 心法不是规则清单 | 8(后改"记 7 条不如懂尊重")|
| C-S3-499 | 脏不脏不是关键 | 7 | 脏不脏从来不是关键 | 9 |
| C-S3-500 | 高脚椅是小监狱 | 7 | 高脚椅就是个小监狱 | 9 |
| C-S4-500 | Einstein 三岁才说话 | 13 | 晚说话不等于晚智 | 8 |
| C-S6-609 | 翻饭就把饭收掉 | 7 | 翻饭就把饭直接收掉 | 9 |
| C-S6-613 | 他在划自己边界 | 7 | 他在划清自己的边界 | 9 |
| C-S7-554 | Magda 的匈牙利谚语收官 | 13 | 匈牙利谚语收尾全书 | 9 |

#### 二次 Hook 修复(再过审 3 处)
| Card | 字数 | 新 hook | 字数 |
|---|---|---|---|
| C-S0-317 | 7 | 只陪宝宝陪伴侣休息 | 9 |
| C-S7-553 | 7 | 不偏袒不评对错少介入 | 10 |
| C-S7-554 | 7 | 匈牙利谚语收尾全书 | 9 |

#### 学究词修复(7 处)
- 认知(C-S5-594 + C-S7-552)→ 心智 / 懂事
- 内化(C-S6-609 + C-S6-610 + C-S6-612)→ 长在心里 / 变规矩 / 记心里
- 机制(C-S5-595 + C-S6-607)→ 反应 / 能力
- 人格(C-S1-557)→ 性格

### 2.3 修后机器审(0 错全过)

```
YAML 错: 0
hook 错: 0
学究词: 0
0 跨源: 0
缺 Lansbury: 0
avg related=3.00, 跨源率=100%, Lansbury=100%
```

---

## 3. 轮 2:漏知识反向覆盖(逐章 spot-check)

### 3.1 8 章覆盖率核查

逐章对照"Magda 给了什么 vs 已建卡覆盖什么":

| 章 | 字数 | 已建覆盖 | spot-check 漏点 |
|---|---|---|---|
| Ch1 Respect/Principles | 15K | C-S2-493 | ✓ 7 大原则全覆盖 |
| Ch2 Birth of RIE | 16K | C-S2-494 + C-S6-611 + 术语 | ✓ Pikler/Loczy/DIP/Beverly 全覆盖 |
| Ch3 Newborn Baby(S1)| **65K** | C-S1-555..559(5 张) | ✓ Wants QT/Tell first/Crying/Devices/Spoiled 全覆盖,Colicky / SIDS 是 AAP 重叠跳过 |
| Ch4 Newborn Parents | 23K | C-S0-316..317 | ✓ 8 父母品质 + Doula 已覆盖 |
| **Ch5 First Months** | **92K** | C-S2-495..496 | ⚠️ **漏:Help Form Sleeping Habit** |
| Ch6 Child Care | 33K | (跳过)| 美国家长场景,跳过合理 |
| Ch7 Becomes Mobile(S5)| **77K** | C-S4-498..500 + C-S5-594..596 + C-S3-500 | ✓ 7 张已覆盖,Trying New Foods 30 次跟 Lansbury 重叠跳过 |
| **Ch8 Budding Toddler** | **141K** | C-S6-607..613(7 张) + C-S7-552..554 | ⚠️ **漏:Words Give Power** |

### 3.2 漏知识补 2 张(高价值,必补)

#### C-S5-597 Magda 帮宝宝睡的中间路(Ch5 §Help Your Baby Form the Sleeping Habit)A 级 ⭐⭐

**重要度**:
- Magda 1998 立场比 Lansbury 2014 更细
- Magda 立场:**不 CIO + 不 co-sleep + 支持 Ferber method**(渐进自我安抚)
- 关键差异:Magda 加了"先告知宝宝你的计划"(RIE 元素)
- Heidi 案例(Cynthia 妈妈,Magda Ch5 经典):6 月 4-5 晚学会

**核心**:
1 反 CIO(放任哭)
2 反"sleep training" 这个标签(Lansbury 也反)
3 反 co-sleep 主流派(Sears)
4 反"摇 / 走 / 喂入睡"(制造依赖)
5 **支持** Ferber method(渐进自我安抚)— Magda 直接引!
6 关键:**不只是技术,要先告诉宝宝你的计划**

**跨源**:
- ↔ Lansbury C-S1-355(Lansbury 反训练对照 — RIE 派内部演化)
- ↔ Davies C-S5-130(蒙氏睡眠观)
- ↔ Bowlby V1 C-S5-076(分离焦虑 + 睡眠)

#### C-S6-614 Words give power 替打咬人(Ch8 §Why It's Important to Talk Feelings)A 级 ⭐⭐

**重要度**:
- 中国家长 1.5-2 岁打人 / 咬人高峰期最高频痛点解药
- Magda 立场:**鼓励娃用语言表达情绪 → 他可能选说而不是推/打/咬**
- "如果他用语言能引起注意,就不需要靠负面行为"

**核心 5 招**:
1 重复他的词:"狗,你要摸狗"
2 帮他完成短语:他说 "up" → "你要我抱你"
3 给 2 选项问句:"你要苹果还是梨"
4 不强迫 repeat,只让他听
5 Be selective 你说的词(他模仿你)

**跨源**:
- ↔ Lansbury C-S6-405(鼓励幼儿说话 6 招)
- ↔ Lansbury C-S6-403(限度+情绪并存)
- ↔ Davies C-S2-127(真词不嘎嘎)

### 3.3 跳过的章节(说明为什么)

| 章 | 跳过原因 |
|---|---|
| Ch3 §Colicky / SIDS | 跟 AAP / Karp 重叠,无 Magda 独家立场 |
| Ch6 Child Care | 美国家长选托班场景,中国家长场景不同 |
| Ch7 §Trying New Foods 30 次 | 跟 Lansbury C-S5-391 + Davies C-S6-130 重叠太多 |
| Ch8 §Whining | 立场跟 C-S6-609 cause/consequence 重叠 |
| Ch8 §Cooperation in Caregiving 1.5-2 岁 | 跟 C-S3-499 + C-S3-501 + Lansbury C-S1-353 重叠 |

---

## 4. 轮 3:漏术语扫

### 4.1 候选漏术语扫(SRC-021 卡正文出现频次)

```
术语                        频次     已建术语?
-------------------------------------------------------
magda                     32       G-PERSON-Gerber(Magda 是名)
time-out                  2        G-TERM-time-out(已存在)
consequence               2        G-TERM-cause-consequence(我建)
wants something           1        G-TERM-wants-something-quality-time(我建)
wants nothing             1        包含在上一个术语里
spanking                  1        无独立术语,在 G-TERM-respectful-parenting 框架内
doula                     1        无独立术语,1 卡引用价值低
piaget                    1        G-PERSON-Piaget(已存在)
maslow                    1        无独立术语,1 卡引用价值低
antaeus                   1        G-TERM-tantrum-antaeus(我建)
ferber                    1        无独立术语,1 卡引用价值低
freud                     1        无独立术语,1 卡引用价值低
pikler                    1        G-PERSON-Pikler(已存在)
```

### 4.2 漏术语审决定:不补

理由:
- 1 卡引用的术语建独立卡价值不高
- Magda 引用的历史人物(Erikson / Piaget / Maslow / Freud)如果建独立 G-PERSON 卡需大量内容
- Spanking / Doula / Ferber 都跟现有术语重叠

---

## 5. 轮 4:用户三审 3 维度

### 5.1 (a)hook 风格审 — 2 处描述型(修)

发现 2 处描述型 hook(含"清单" / "坐标系"):

| Card | 旧 hook | 修后 hook | 改进 |
|---|---|---|---|
| C-S2-493 | 心法不是规则清单 | 记 7 条不如懂尊重 | 描述 → 抓眼对比 |
| C-S6-608 | Magda 给的限度坐标系 | 你的需要也算需要 | 描述 → 警句 |

修后:**0 描述型 hook**。

### 5.2 (b)跨源率审 — 100%(0 跨源孤岛)

每张 SRC-021 卡至少 1 张非 SRC-021 related。

实际统计:
- 32 张卡总 96 个 related
- 96 个全部跨源(跨源率 100%)
- 平均 3.00 个/卡

### 5.3 (c)章节 spot-check — 已在轮 2 完成

- 8 章逐章 spot-check 不跳过(继承 Lansbury 用户三审教训)
- 找出 2 张高价值漏知识(Ch5 sleep + Ch8 words)
- 已补 C-S5-597 + C-S6-614

### 5.4 (d)Lansbury related 100% — 创始人 ↔ 推广人对照

每张 Magda 卡至少 1 张 Lansbury(SRC-019)related,做创始人 ↔ 推广人对照:

实际统计:
- 32 张全部包含 Lansbury related
- Lansbury related 率 = 100%(目标 ≥ 50% 远超)
- 这是本卷核心价值 — 不是"复制 Lansbury",是"创始人对照推广人"

---

## 6. 内部质量重审(全过 0 错)

跑深度 Python 验证(修后):

| 维度 | 结果 |
|---|---|
| YAML 解析 | 32/32 通过 |
| 字数(title ≤ 15 / hook 8-12 / wtd ≤ 35 / fm ≤ 200) | **0 错** |
| 学究词残留 | **0** |
| glossary_refs 全部存在 | **0 错** |
| related_cards 全部存在 + 0 自引用 | **0 错** |
| 0 跨源卡 | **0 张** |
| 平均 related_cards | **3.00 个/卡** |
| Lansbury related 卡 | **32/32 = 100%** |

---

## 7. 段分布 + 等级分布(终版 32 张)

### 段分布

| 段 | 月龄 | 卡数 | 备注 |
|---|---|---|---|
| S0 | 孕期 | 2 | 不变 |
| S1 | 0-1 月 | 5 | 不变 |
| S2 | 1-3 月 | 4 | 不变 |
| S3 | 3-6 月 | 3 | 不变 |
| S4 | 6-9 月 | 3 | 不变 |
| S5 | 9-12 月 | **4** | 二审补 1(C-S5-597 Magda 帮宝宝睡的中间路) |
| S6 | 12-24 月 | **8** | 二审补 1(C-S6-614 Words give power) |
| S7 | 24-36 月 | 3 | 不变 |
| **总** | | **32** | 初版 30 + 漏知识反向覆盖补 2 |

### 等级分布

- **A 级**:23 张(72%)
- **B 级**:9 张(28%)
- **C 级**:0 张

A 级 72% **高于 Lansbury 49%**,反映 Magda 跟蒙氏 + Pikler + Bowlby 高度对齐。

---

## 8. 4 轮审框架沉淀(给后续 Phase 9)

### 8.1 框架完整版

```
轮 1 = Python 机器审(YAML / 字数 / 学究词 / refs)
        ├── YAML safe_load 解析
        ├── title ≤ 15 / hook 8-12 / wtd ≤ 35 字数
        ├── 学究词清单扫(15+ 词)
        ├── glossary_refs / related_cards 存在性
        ├── 0 自引用
        ├── 跨源率(每张至少 1 个非自卷 related)
        └── 特定派"姐妹篇" related 率(本卷 Lansbury 100%)

轮 2 = 漏知识反向覆盖(每章 spot-check)
        ├── 逐章对照"原文给了什么 vs 已建覆盖什么"
        ├── 不能因"内容单薄"跳过(Lansbury 用户三审教训)
        ├── 标记跳过章节理由
        └── 补漏卡时跨源 related 必含至少 1 个非自卷

轮 3 = 漏术语扫
        ├── 卡正文高频概念词频次扫
        ├── 跟现有术语库对照
        ├── 漏术语 build / pass 决定(1 卡引用 = 跳过)
        └── 历史人物(Maslow/Freud/Erikson)单独决策

轮 4 = 用户三审 3 维度
        (a) hook 风格审:不能描述型(含"派/清单/系统/工具/框架/坐标系"等)
        (b) 跨源率审:0 跨源孤岛
        (c) 章节 spot-check 审:逐章不跳过
        (d) [本卷新增] 姐妹篇 related 率审(本卷 Lansbury 100%)
```

### 8.2 Phase 8 Gerber 用户三审版补充

跟 Phase 7 Lansbury 用户三审(发现 4 张漏知识 + 5 描述型 hook + 13 张 0 跨源)对比:

| 维度 | Phase 7 Lansbury | Phase 8 Gerber |
|---|---|---|
| 漏知识 | 4 张高价值(Ch3/8/10/14)| 2 张高价值(Ch5/8)|
| 描述型 hook | 5 处 | 2 处 |
| 0 跨源孤岛 | 13 张 | 0 张(预防优于修)|
| 平均 related | 2.03 → 2.88 | 3.00(初版即达)|
| 姐妹篇 related 率 | N/A | **100%**(目标 ≥ 50% 远超)|

**改进点**:
- 跨源率"事前预防"比"事后修"更高效(Phase 7 修了 13 张,本卷 0 张需修)
- 姐妹篇 related 率作为新硬指标(本卷 100%,定义"创始人 ↔ 推广人对照"为本卷核心价值)
- hook 风格审保留(本卷 2 处描述型,比 Lansbury 5 处少 — 学习曲线)

---

## 9. 教训沉淀(给 Phase 9)

| 教训 | 实战修复 |
|---|---|
| YAML `- "..."` 嵌套陷阱 | 中文 「」 替英文 `"`,实测修 6 处 |
| 7 字符 hook 是中文白话陷阱 | Python 扫 + 修 8 处(7 字 → 8-12 字) |
| 描述型 hook 含"清单/系统/坐标系"等 | 修 2 处,改抓眼警句 |
| 学究词"内化"是 Magda 哲学核心难替 | 改"长在心里 / 变规矩 / 记心里"(白话 + 不丢哲学)|
| 并行 session 术语预创建 | Edit 加 source 不覆盖 |
| 文献中的"Magda 8 大原则"实测原版只有 7 | 不照搬二手描述,直接看原文 |

---

## 10. 推荐审 5 张样本(用户三审版)

按重要度 + 漏知识反向覆盖标记:

1. **[C-S6-607 Antaeus 故事:接地起](../../30-cards/s6-12to24mo/C-S6-607.yaml)** ⭐⭐⭐ A 级 + Magda 希腊神话独家
2. **[C-S6-608 红黄绿三灯设限度](../../30-cards/s6-12to24mo/C-S6-608.yaml)** ⭐⭐⭐ A 级 + 反密集母职 + hook 修后样本
3. **[C-S6-614 语言给娃武器替打咬](../../30-cards/s6-12to24mo/C-S6-614.yaml)** ⭐⭐ A 级 + **漏知识反向覆盖补**
4. **[C-S5-597 Magda 帮宝宝睡的中间路](../../30-cards/s5-9to12mo/C-S5-597.yaml)** ⭐⭐ A 级 + **漏知识反向覆盖补** + 1998 vs 2014 演化
5. **[C-S2-493 Magda 7 大原则原版](../../30-cards/s2-1to3mo/C-S2-493.yaml)** ⭐ A 级 + 哲学骨架 + hook 修后样本

### 验收标准

- Magda 32 张审版通过 / 调整 / 重做?
- 4 轮独立审 + 漏知识反向覆盖 + 跨源率 100% + Lansbury related 100% 框架是否引入 Phase 9?
- Phase 9 候选:Pikler 师承原典 / Ainsworth Strange Situation / 松田道雄 / Brazelton 3-6?

---

## 11. 完成度对比(初版 → 二审 → 三+四审)

| 维度 | 初版(30) | 二审(32) | 三+四审(32 终版) |
|---|---|---|---|
| 段覆盖 | S0-S7 | S0-S7(更深)| S0-S7 |
| 章节覆盖 | Ch1-Ch8 部分 | + Ch5 sleep + Ch8 words | 同二审 |
| A 级 % | 70% | 72% | **72%**(终版 23/32 张 A 级)|
| 跨源率 | 100% | 100% | **100%** |
| Lansbury related 率 | 90% | 100% | **100%** |
| hook 风格 | 2 描述型 | 2 描述型 | **全 hook 风格** |
| 0 跨源卡 | 0 张 | 0 张 | **0 张** |
| 平均 related | 3.00 | 3.00 | **3.00** |
| 学究词残留 | 7 | 7 | **0** |
| YAML 错 | 6 | 6 | **0** |
| 中国家长高频痛点覆盖 | 大部分 | 全部 | **全覆盖 + 打咬人替代 + 睡眠 1998 立场 + 三灯反密集母职** |

---

*v1.0 · 2026-05-03 — Phase 8 第二本 Magda Gerber 4 轮独立审 + 漏知识反向覆盖完整产出*
*累计:Magda 32 张 + 6 术语,跨 8 段 S0-S7,A 级 23 张(72%)*
*4 轮审框架沉淀:漏 spot-check 章节 + hook 风格 + 跨源率 + 姐妹篇 related 率 = 4 个维度*
*下次接手 session 必读:本文件 + checkpoint_PHASE8_GERBER_20260503.md(初+二审)+ PHASE8_GERBER.md(任务书)*
