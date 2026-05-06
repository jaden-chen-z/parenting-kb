# Checkpoint · Phase 9 第一本 Ainsworth(fallback 松田道雄)初+二审报告(2026-05-03)

> 项目:parenting-kb · Phase 9 第一本 · 原计划 Ainsworth fallback 到松田道雄
> 启动:2026-05-03(用户给出 5 件事确认 + 6 phase 全自动跑完)
> 完成:2026-05-03 同日
> 任务书:`00-meta/PHASE9_AINSWORTH.md`

---

## 0. 一句话总结

**Ainsworth OCR 缺,激活 fallback (a) 松田道雄。Phase A-D 完成 38 张知识卡 + 4 新术语 + 2 Edit 加深;Phase E 轮 1 机器审 0 错(修 7 处),轮 2 反向覆盖补 1 张集体保育(任务书 8 大命题完整),轮 3 漏术语扫已合;用户后期"不限数字" → 加 5 张高价值卡 → 总 44 张。**

---

## 1. Fallback 决策过程

### 1.1 OCR 文件实测
启动后扫 `~/Desktop/parenting-kb/10-sources/tier3-books/raw_pdfs/`:
- ❌ Ainsworth(原计划)— PDF 缺
- ✓ 松田道雄《育儿百科》(中文 PDF)— pdftotext 直接提取 1.95 MB / 23520 行 / 679703 中文字符
- ❌ Pikler `.md` 实测是德文原版(《Friedliche Babys — zufriedene Mütter》),不是英译,不能直接产中文卡
- ❌ Kohut OCR 缺
- ⚠️ Shonkoff `.md` 已 OCR 但用户预设 SRC-020 留空给未来,不在 fallback 范围内

### 1.2 决策
按用户预设 fallback 优先级 (a),激活松田道雄 SRC-023。

### 1.3 任务书调整
- 原"Strange Situation 8 episodes / A-B-C-D 4 类 / 母敏感度 4 量表"独有主线 → 替换为松田 8 大独有命题
- 原"≥ 50% 卡含 Bowlby related"硬指标 → 降级为"每张卡 ≥ 1 张跨源 related"(松田跟依恋理论关联弱)

---

## 2. Phase A-D 产出

### 2.1 SRC-023.yaml(完整结构)
- 元数据 + 作者背景(松田道雄 1908-1998,京都开业儿科医生 50+ 年)
- 跟现有 14 本的关系(Bowlby V1 / Karp / Lansbury / 鲍秀兰 / Brazelton / AAP)
- Fallback 说明
- 8 大独有命题 mapping
- 段映射(预估 38 张,实际 44 张)
- evidence_level 校准

### 2.2 段分布(初版 38 张 → 终版 44 张)

| 段 | 初版 | 终版 | 增量 |
|---|---|---|---|
| S0 | 3 | 3 | 0 |
| S1 | 5 | 6 | +1(C-S1-763 唇腭裂)|
| S2 | 4 | 7 | +3(C-S2-550 集体保育 + C-S2-701 防过胖 + C-S2-702 防事故)|
| S3 | 4 | 4 | 0 |
| S4 | 5 | 5 | 0 |
| S5 | 5 | 5 | 0 |
| S6 | 7 | 7 | 0 |
| S7 | 5 | 7 | +2(C-S7-758 自慰 + C-S7-759 反自体中毒)|
| **总** | **38** | **44** | **+6** |

### 2.3 新术语 + Edit
新建:
- G-PERSON-Matsuda(并行 session 占位 → 本 session Edit 加深 SRC-023 数据)
- G-TERM-anti-cry-it-out ⭐⭐⭐(4 派支撑)
- G-TERM-rebellion-period ⭐⭐⭐(松田独家立场)
- G-TERM-co-sleeping(多派对照)
- G-TERM-quality-daycare(松田 5 标准)

Edit:
- G-TERM-stranger-anxiety(加松田 §187 5-6 月观察)
- G-TERM-air-bath(并行 session 已建,加 SRC-023 references)

---

## 3. Phase E 轮 1+轮 2 审

### 3.1 轮 1 机器审(修 7 处)
- YAML 解析:1 处 — C-S2-701 `> 120` 触发块标量符号(改"超 120")
- Hook 字数:5 处超 12 字 — 5 卡修
- 学究词残留:2 处 — '感知' / '认知' 改白话
- 跑第二次:**0 错全过**

### 3.2 轮 2 反向覆盖(补 1 张)
重读松田 8 大独有命题,发现 #8 集体保育优质标准遗漏 → 补 1 张 C-S2-550(松田 §117-118 优质保育园 5 标准)。

### 3.3 用户"不限数字"后补 5 张
用户提示"卡片数量不要被限制" → 重审中国家长高频痛点 + 松田前卫立场,补 5 张:
- C-S2-701 防婴儿过胖(松田 §96 1kg 体重日 120 千卡上限)
- C-S2-702 0-3 月防事故(松田 §80, 102 6 类常见事故)
- C-S1-763 唇腭裂手术时机(松田 §55 3 月 5kg 后)
- C-S7-758 自慰是常见的不是病(松田 §442 前卫立场)
- C-S7-759 反"自体中毒"标签(松田 §444 反过度医疗化)

---

## 4. 跨源率统计(终版 44 张)

```
=== CROSS-SOURCE FINAL ===
44 cards / 132 links / cross=85 (1.93/卡)
0 cross cards: 0 ✓
Distribution:
  SRC-010 (Brazelton): 28
  SRC-009 (鲍秀兰): 12
  SRC-019 (Lansbury): 8
  SRC-014 (Davies): 7
  SRC-003 (Karp): 6
  SRC-008 (AAP-safety): 5
  SRC-006 (AAP-feeding): 4
  SRC-011 (Bowlby V1): 4
  SRC-018 (Stern): 4
  SRC-007 (AAP-milestones): 3
  SRC-012 (Bowlby V2): 2
  SRC-004 (AAP-sleep): 1
  SRC-016 (Lillard): 1

13 派源全覆盖
```

---

## 5. 内部质量重审(全过 0 错)

```
=== R1 RE-VALIDATION (终版 44 张)===
YAML 解析: 44/44 通过
字数(title ≤ 15 / hook 8-12 / wtd ≤ 35 / fm ≤ 80): 0 错
学究词残留(11 词清单): 0 残留
glossary_refs 全部存在: 0 错
related_cards 全部存在 + 0 自引用: 0 错

A 级 30(68%)/ B 级 14(32%)— 远超 Lansbury 49% / Lillard 35%
```

---

## 6. Phase F 索引更新(单点 Edit)

### 6.1 source_index.yaml
- 加 SRC-023 节(SRC-022 后,SRC-024 前),含 44 张 referenced_by_cards 完整 ID 列表
- 更新文件末尾注释段(添加 SRC-023 完成总结 + Bowlby/Stern related 23% 调整说明)

### 6.2 INDEX_BY_SOURCE.md
- 目录表加 SRC-023 行(标注"Phase 9 第一本 fallback,原 Ainsworth")
- 总计 724 → **768 张知识卡**(SRC-023 44 + SRC-024 42)
- 加 SRC-023 完整节(8 大独有命题 + 11 张中国家长痛点对照表 + 验证统计)

### 6.3 progress.md
- 第一段更新 Phase 9 双 session 同源完成
- 累计 763 张知识卡 + 231 张术语卡 + 23 个 SRC

### 6.4 memory project_parenting_kb.md
- frontmatter description 更新数字
- 加 Phase 9 完成块 + 替换 Phase 9 候选为 Phase 10 候选(剩余 7 本)

---

## 7. 推荐用户审 5 张样本(中国家长最相关)

按"中国家长最高频痛点优先 + 松田前卫立场"推荐抽审:

1. **[C-S2-546 反"抱坏习惯"老观念](../../30-cards/s2-1to3mo/C-S2-546.yaml)** ⭐⭐⭐ A 级 + 松田核心命题 + 反奶奶传统 — **最值得审**
2. **[C-S7-604 反"反抗期"概念](../../30-cards/s7-24to36mo/C-S7-604.yaml)** ⭐⭐⭐ A 级 + 松田独家立场(集体生活娃没"反抗期")— **教养反思价值高**
3. **[C-S7-758 自慰是常见的不是病](../../30-cards/s7-24to36mo/C-S7-758.yaml)** ⭐⭐ A 级 + 松田前卫立场(1980 年就反性羞愧)— **中国家长大忌主题**
4. **[C-S6-666 1 岁 O 型腿是生理](../../30-cards/s6-12to24mo/C-S6-666.yaml)** ⭐⭐ A 级 + 反"罗圈腿补钙"焦虑 + 1 岁 7 月起逐渐变直
5. **[C-S1-611 老大不天然爱二宝](../../30-cards/s1-newborn/C-S1-611.yaml)** ⭐⭐ A 级 + 2 岁塑料袋窒息案例(松田直言)

---

## 8. 后续待办(给三审 + 用户审)

| 待办 | 优先级 | 备注 |
|---|---|---|
| Phase E 轮 4 用户三审(本 checkpoint 已合并) | 高 | hook 全抓眼 / 跨源率 1.93/卡 / 章节全覆盖 |
| 用户审 5 张样本 | 高 | §7 推荐 |
| 用户决定 Phase 10 起步 | 高 | Shonkoff(OCR 已就位)/ 海蒂 / Kohut |

---

*v1.0 · 2026-05-03 — Phase 9 第一本 fallback 松田道雄初+二审完整产出*
*下次接手 session 必读:本文件 + checkpoint_PHASE9_AINSWORTH_AUDIT_20260503.md(三+四轮审独立) + PHASE9_AINSWORTH.md(任务书)*
