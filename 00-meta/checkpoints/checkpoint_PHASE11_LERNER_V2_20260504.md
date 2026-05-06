# Checkpoint · Phase 11 Lerner V2(SRC-028)初+二审报告(2026-05-04)

> 项目:parenting-kb · Phase 11 并行第二本 · Lerner Handbook V2《Cognition, Perception, and Language》
> 完成:2026-05-04 同日(并行第一本 V3 SRC-027)
> 跟 `checkpoint_PHASE11_LERNER_V2_AUDIT_20260504.md`(三+四+五审)配套

---

## 0. 一句话总结

**Phase 11 SRC-028(51 张 Lerner V2 卡 + 42 张关联术语)初+二轮审 全过 0 错 — Python 机器审 + 反向覆盖 22 章 spot-check 全部通过。**

---

## 1. 双 session 并行场景(SRC-027 V3 + SRC-028 V2)

### 1.1 ID 隔离方案

| 段 | V3 (SRC-027) +100 buffer | V2 (SRC-028) +200 buffer | 避撞 |
|---|---|---|---|
| S0 | 824 | 924 | ✓ |
| S1 | 1000 | 1100 | ✓ |
| S2 | 1035 | 1135 | ✓ |
| S3 | 1039 | 1139 | ✓ |
| S4 | 1040 | 1140 | ✓ |
| S5 | 1037 | 1137 | ✓ |
| S6 | 1064 | 1164 | ✓ |
| S7 | 995 | 1095 | ✓ |
| S8 | 320 | 420 | ✓ |

实测无冲突。索引文件 Edit 单点改未覆盖 V3 工作。

### 1.2 启动前实测验证

```bash
grep "next_src_id" source_index.yaml  # SRC-027(V3 还在跑)
ls notes/SRC-*.yaml                    # SRC-027.yaml 存在
```

V3 在跑,我用 SRC-028 + 200 buffer 完全独立。

---

## 2. Phase A:必读上下文

✅ 完成读必读 9 文件:
- PHASE10_SHONKOFF.md(大综述模板)
- PHASE10_PIKLER.md(并行第二本经验)
- PHASE9_MATSUDA_AUDIT.md(用户三审框架)
- SRC-025/015/018/027.yaml(模板 + 接口)
- PHASE2_AAP.md §2.5-2.9(v3.5 schema)
- G-PERSON-Gopnik/Meltzoff/Kuhl/Spelke/Piaget(已建认知派术语)
- G-TERM-language-explosion/critical-period(已建)
- C-S3-188(物体永久卡样本)

---

## 3. Phase B:扫书结构 + 主题映射

### 3.1 OCR 文件实测

- 文件:lerner_handbook_v2.md(5,657,932 chars / 127,469 行)
- 22 章实测:Ch 1-22 全部 offset 已确认
- 主笔识别完成:每章主笔学者已 mapped

### 3.2 学者 hits 扫描(关键命题)

```
Spelke: 173 hits      Tomasello: 164      Mandler: 126
Werker: 120          Bloom: 123          Carey: 134
Wellman: 105         Adolph: 193         Thelen: 183
Bauer: 234           Goldin-Meadow: 148  Markman: 89
Karmiloff-Smith: 63  Munakata: 91        Newcombe: 77
Geary: 76            Dehaene: 55         Kellman: 104
Saffran: 74          Wynn: 97            Leslie: 68
Gentner: 66          Baillargeon: 63
```

### 3.3 SRC-028.yaml 完成

- 30 个 lerner_v2_unique_themes
- 16 个 crossreferences(跟现库 18 派 + V3 铁三角对接)
- 21 个 parent_pain_points
- chapter_offsets 22 章实测

---

## 4. Phase C:51 张卡(分多组按章节)

| 段 | 卡数 | 实际 ID 范围 | 主题概述 |
|---|---|---|---|
| S0 | 1 | C-S0-924 | Nelson 经验依赖 vs 经验期待 |
| S1 | 2 | C-S1-1100/1101 | Cohen-Cashon 新生儿面孔 / DeCasper 母音 |
| S2 | 4 | C-S2-1135-1138 | Burnham parentese / Eimas 范畴 / Gibson 视觉悬崖 / Cohen 习惯化 |
| S3 | 7 | C-S3-1139-1145 | Polka-Werker vowel / Baillargeon 吊桥 / Cohen vs Spelke / Cohen 因果 / Kellman 物体 / Wynn 5 月 / Meltzoff 跨模态 |
| S4 | 4 | C-S4-1140-1143 | Saffran 8 月 / Spelke 5 系统 / animate-inanimate / 面孔 9 月 |
| S5 | 6 | C-S5-1137-1142 | Werker reorganization / Adolph 学走 / Thelen A-not-B / Tomasello 9 月 / pointing / Bates 手势 |
| S6 | 9 | C-S6-1164-1172 | Markman 3 约束 / 互斥 / fast mapping / 词汇爆炸 / 名词偏 / Bauer 记忆 / Goldin-Meadow / Leslie 假装 / Dehaene |
| S7 | 7 | C-S7-1095-1101 | 命名洞察 / Carey 革命 / Mandler / Wellman ToM / Gentner 类比 / Newcombe 空间 / Munakata |
| S8 | 11 | C-S8-420-430 | Sally-Anne / 朴素生物 / Geary 中文优势 / Cole 文化 / Karmiloff-Smith RR / Siegler 重叠波 / Winner 艺术 / Keil 直觉 / 自闭 ToM / Williams / Gardner |
| **总** | **51** | | |

---

## 5. 轮 1:Python 机器审(初版 → 修复后)

### 5.1 初版扫描发现

- Title > 15 字:**4 处**(C-S2-1135 / C-S8-429 / C-S8-428 / C-S8-420)
- Hook 不在 8-12 字:**29 处**(多数 6-7 字偏短)
- what_to_do > 35:2 处
- broken related_cards:**10 处**(C-S3-186/C-S5-902/C-S6-101/C-S6-102 不存在)
- 0 跨源 related:**11 处**(只引 V2 1xxx 系列,缺现库跨派)

### 5.2 修复

- 4 个 title 缩短(全部 ≤ 15 字)
- 29 个 hook 调整到 8-12 字
- 2 个 wtd 简化
- 10 个 broken refs 替换为正确 ID(C-S3-186 → C-S3-187 / C-S5-902 → C-S6-926 / C-S6-101 → C-S6-957 / C-S6-102 → C-S6-963)
- 11 个 0 跨源卡补跨派 related(C-S5-013 / C-S5-016 / C-S6-018 / C-S7-001 / C-S8-100)

### 5.3 修复后

```
Title > 15: 0
Hook 8-12 violations: 0
wtd > 35: 0
fm > 80: 0
broken refs: 0
broken related: 0
0 跨源: 0
描述型 hook: 0
```

✅ Round 1 全清零

---

## 6. 轮 2:漏知识反向覆盖(逐章 spot-check)

### 6.1 章节覆盖统计

```
Ch 1 Nelson 神经基础: 2 cards
Ch 2 Saffran/Werker 听觉语言: 6 cards
Ch 3 Kellman 视觉: 4 cards
Ch 4 Adolph 大动作: 2 cards
Ch 5 Cohen-Cashon 婴儿认知: 7 cards
Ch 6 Tomasello 语言: 3 cards
Ch 7 Waxman/Lidz 词汇: 6 cards
Ch 8 Goldin-Meadow 手势: 1 cards
Ch 9 Bauer 记忆: 1 cards
Ch 10 Munakata 信息处理: 1 cards
Ch 11 Siegler 微观发生: 1 cards
Ch 12 Pressley 策略: 0(0-6 不主取)
Ch 13 Halford 推理: 1 cards
Ch 14 Keil 元学: 2 cards
Ch 15 Cole 文化: 1 cards
Ch 16 Gelman/Kalish 概念: 3 cards
Ch 17 Newcombe 空间: 1 cards
Ch 18 Geary 数学: 3 cards
Ch 19 Harris 社会认知: 4 cards
Ch 20 Winner 艺术: 1 cards
Ch 21 Gardner 神童: 1 cards
Ch 22 第二个十年: 0(0-6 不主取)

Total chapters covered: 20 / 22
```

### 6.2 跨章重复主题独立卡(关键检查)

| 主题 | 跨段独立卡 | 段分布 |
|---|---|---|
| 物体永久性 | 4 张 | S3(1140 吊桥)+ S5(1139 A-not-B)+ S4(1141 5 系统)+ S3(188 已存) |
| 语言/词汇 | 8+ 张 | S2-S7 全段 |
| 心智理论 | 5 张 | S5(1140)+ S6(1171)+ S7(1098)+ S8(420)+ S8(428) |
| 数概念 | 4 张 | S3(1144)+ S6(1172)+ S7(1099)+ S8(422) |
| 因果学习 | 2 张 | S3(1142)+ S5(1140) |
| 神经基础 | 2 张 | S0(924)+ S8(429) |
| 假装游戏 | 2 张 | S6(1171)+ S8(420) |

✅ 跨章重复主题都有独立卡覆盖,不合并

### 6.3 章节 spot-check 跳过的合理性

- Ch 12 Pressley 认知策略 — 学龄前 5+ 岁内容多,0-6 不主取
- Ch 22 Kuhn 第二个十年 — 青少年期,0-6 不主取

---

## 7. 双 session 累计 Phase 11 总览

| 维度 | V3(SRC-027) | V2(SRC-028) | 双 session 合计 |
|---|---|---|---|
| 卡数 | 84 | 51 | **135** |
| 术语 | 186(63 G-PERSON + 123 G-TERM) | 42(26 G-PERSON + 14 G-TERM + 2 扩展) | **228** |
| 段覆盖 | S0-S8 全段 | S0-S8 全段 | 双覆盖 |
| 段 ID buffer | +100 | +200 | 0 冲突 |
| A 级 % | 92% | 98% | — |
| 跨派率 | 100% | 100% | — |
| 章节覆盖 | 16/16(100%) | 20/22(91%) | — |

**Phase 11 合计**:135 张知识卡 + 228 张术语 = **完成"学术综述铁三角"**(V1 节选 + V2 + V3)

---

## 8. 工程意外(Phase 11 V2 特有)

### 意外 1:YAML curly quotes 解析错误(Phase 10 教训复现)
- 主因:`vs V2 反"训练"立场` 中文双引号在 double-quote string 中
- 修复:改用 single-quote 包裹外层
- **教训**:中文标点需谨慎,优先 single-quote 或 block scalar

### 意外 2:V3 已建 G-PERSON 跟 V2 重叠(Tomasello / Wellman)
- 主因:并行 session,V3 先建,我准备 Write 时报"file not read"
- 修复:Read + Edit 单点改加 SRC-028 引用,不覆盖 V3 工作
- **教训**:并行场景术语共享,要 Edit 不要 Write

### 意外 3:Round 1 发现 broken related refs(C-S3-186 等)
- 主因:写卡时凭印象写 ID(Phase 10 也踩过)
- 修复:Python 找正确 ID 替换(C-S3-187 / C-S6-926 / C-S6-957 / C-S6-963)
- **教训**:关键 cross-ref 必须 ls 验证存在

### 意外 4:11 张卡 0 跨源(全 V2 1xxx 系列)
- 主因:批量产卡时只引 V2 同主题卡,缺跨派
- 修复:Python 批量补跨派 related(C-S5-013 / C-S5-016 / C-S6-018 / C-S7-001 / C-S8-100)
- **教训**:跨派率不是自动满足,要主动标连

### 意外 5:46 张卡 glossary_refs 缺 V2 新建术语
- 主因:产卡时没建术语,事后建术语后没回头补 refs
- 修复:Python 批量给 46 张卡补 V2 新术语 refs
- **教训**:术语先建再产卡 / 或者建术语后回头 audit

---

## 9. 5 轮审框架(给 Phase 12)

继承 Phase 9-11 用户深度审 + 本卷新经验:

```
轮 1 = Python 机器审 — 字数 / yaml / refs / 跨派率
   - 关键:批量修 broken refs + 跨源孤岛
轮 2 = 反向覆盖逐章 spot-check
   - 关键:跨章重复主题独立卡(物体永久 / 数 / 心智理论 / 语言)
轮 3 = 漏术语扫
   - 关键:V2 主笔学者全建 G-PERSON,经典模型全建 G-TERM
   - 关键:产卡 + 建术语后回头 batch Edit glossary_refs(本卷踩坑)
轮 4 = 用户三审 3 维度
   - hook 风格 + 跨派率 + 章节覆盖
轮 5 = 用户深度审
   - 跨章主题 / 漏专业术语 / 内部结构 / 中国家长高频痛点
```

---

*v1.0 · 2026-05-04 — Phase 11 SRC-028 初+二审产出*
*51 张卡 + 42 关联术语;Round 1+2 全过 0 错;跨派率 100%;0 跨派孤岛;hook 全抓眼*
*下次 Phase 12 候选:Lerner V1 + V4 / Kohut self psychology / 海蒂育儿 / WHO 喂养 / Brazelton 3-6*
