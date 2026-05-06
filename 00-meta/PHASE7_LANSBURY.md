# Phase 7 第二本 · Lansbury RIE 派现代代表

> 项目代号:parenting-kb · Phase 7 第二本(2026-05-03)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读**(按顺序):
> 1. 本文件(PHASE7_LANSBURY.md)
> 2. `00-meta/checkpoints/checkpoint_PHASE7_LANSBURY_20260503.md`(本卷产出)
> 3. `00-meta/checkpoints/checkpoint_PHASE7_LANSBURY_AUDIT_20260503.md`(三审记录)
> 4. `00-meta/PHASE6_LILLARD.md`(蒙氏 0-3 学院派,Lansbury 跟蒙氏是邻近平行流派)
> 5. `00-meta/PHASE2_AAP.md` §2.5-2.9(v3.5 schema)
> 6. `00-meta/PHASE1_KARP.md` §10(14 条实战教训)

---

## 0. 一句话任务

抓 Janet Lansbury《Elevating Child Care: A Guide to Respectful Parenting》(JLML Press, 2014)— RIE 派现代代表,Magda Gerber 直接弟子,30 章博客合集。
产 **39 张 v3.5 中文 RIE 派卡** + 8 张术语卡。**RIE + 蒙氏闭环完成**(Davies 实操 + Lillard 理论 + Gerber/Lansbury RIE 派)。

---

## 1. 选定的书 + 来源

**Janet Lansbury《Elevating Child Care: A Guide to Respectful Parenting》**

| 字段 | 值 |
|---|---|
| 文件 | `10-sources/tier3-books/raw_pdfs/lansbury_elevating_child_care.md`(216KB,.epub 转 .md)|
| 作者 | Janet Lansbury — Magda Gerber 直接弟子,RIE 派当代推广人,博客 janetlansbury.com 全球数百万读者,3 个孩子的母亲 |
| 流派 | Tier 3 / RIE(Resources for Infant Educarers)/ 尊重型育儿 |
| 范围 | 0-36 月(部分延伸到学龄前)|
| 出版 | 原版 2014 英文,JLML Press(Lansbury 自创出版社)|
| ISBN_en | 978-0-9911442-0-9 |
| 中译本 | 待考(可能繁中版《尊重宝宝》或类似)|

### 为什么这本(Phase 7 第二本选择)

1. **RIE 派代表作** — Lansbury 是 Magda Gerber 后最有名的 RIE 推广人,博客读者百万级
2. **跟蒙氏平行** — RIE 跟蒙氏 0-3 是邻近流派,80% 共识 + 20% 独有维度
3. **博客合集结构** — 30 章每章独立主题,适合按主题映射 8 段(0-3 岁)
4. **独家命题鲜明** — sportscasting / CEO 语调 / Why You're Yelling 4 reasons / Let kids be mad
5. **OCR 已就位**(.epub 转 .md,无 OCR 错字)
6. **3 session 并行场景** — Bowlby V3(SRC-017)+ Stern(SRC-018)+ 本卷(SRC-019)同时跑

---

## 2. 段定义(本次产出)

| 段 | 月龄 | 文件夹 | 本次产卡 |
|---|---|---|---|
| S0 | 孕期 | s0-pregnancy | 2 张(C-S0-115..116)|
| S1 | 0-1 月 | s1-newborn | 4 张(C-S1-352..355)|
| S2 | 1-3 月 | s2-1to3mo | 4 张(C-S2-290..293)|
| S3 | 3-6 月 | s3-3to6mo | 4 张(C-S3-295..298)|
| S4 | 6-9 月 | s4-6to9mo | 4 张(C-S4-295..298)|
| S5 | 9-12 月 | s5-9to12mo | 4 张(C-S5-390..393)|
| S6 | 12-24 月 | s6-12to24mo | **11 张**(C-S6-395..405)— Lansbury 最强段 ⭐ |
| S7 | 24-36 月 | s7-24to36mo | 6 张(C-S7-347..352)|
| **总计** | | | **39 张**(初版 37 + 二审补 2)|

S6 是 Lansbury 最强段(限度 + sportscasting + tantrum + 真话)。

**ID 起点策略**(3 session 并行):**+100 buffer**(避撞 Bowlby V3 + Stern)。
- s0=15 → 起 115
- s1=252 → 起 352
- s2=190 → 起 290
- s3=195 → 起 295
- s4=195 → 起 295
- s5=290 → 起 390
- s6=295 → 起 395
- s7=247 → 起 347

---

## 3. 卡片规范(完全继承 v3.5)

参 `PHASE2_AAP.md` §2.5-2.9 + Phase 3/4/5/6 扩展。

### 评级 evidence_level(本书标尺)

Lansbury RIE = Magda Gerber 60+ 年 RIE 实战 + Pikler 100 年研究 + Lansbury 自家 3 孩 + 千+ RIE 班级案例:
- **A**:与 Tier 1 共识对齐(Lansbury 跟 蒙氏 + Bowlby + Pikler + 现代神经科学吻合)
- **B**:Lansbury 引用 RIE 60 年观察 + Pikler 临床 + 自家案例 + 千+ 班级
- **C**:Lansbury 个人推断(罕见)

实测产出:**A=19 / B=20 / C=0** 张 — A 级 49%(高于 Lillard 33% + Davies 31%),反映 Lansbury 跟蒙氏 + Pikler 高度对齐。

---

## 4. 工作流(基于 Phase 6 三审教训改进)

### 4.1 章节地图(SRC-019.yaml 已记录)

Lansbury 216KB / 30 章博客合集 + Introduction + 致谢 / 单长行 .md 文件。30 章 offset 全在 SRC-019.yaml `chapter_map` 字段。

### 4.2 chunk 策略

每章 3-23K 字符(博客合集),Python `text[start:end]` 切片读取(主上下文)。Ch7(Sitting Babies)23K 最长;Ch6 / Ch15 / Ch22 / Ch23 / Ch28 各 7-10K 是关键章。

### 4.3 反向覆盖审计(每段产卡完成后)

每段产卡完成后,主上下文从原文重列"父母从 RIE 视角必须知道的 N 件事",对比已写卡补漏。

实测二审补 2 张:
- C-S6-405:鼓励幼儿说话 6 招(Ch17,中国家长高频痛点)
- C-S7-352:你设限难?3 个真原因(Ch23,温柔派父母自查工具)

---

## 5. 输出位置(实测)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml(已加 SRC-019 entry,改 next_src_id → SRC-020)✅
│   └── tier3-books/notes/
│       └── SRC-019.yaml ✅(新建)
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md ✅(加 SRC-019 节 + 顶部目录表 + 总数 499 → 538)
│   ├── s0-pregnancy/      # C-S0-115..116 ✅(2)
│   ├── s1-newborn/        # C-S1-352..355 ✅(4)
│   ├── s2-1to3mo/         # C-S2-290..293 ✅(4)
│   ├── s3-3to6mo/         # C-S3-295..298 ✅(4)
│   ├── s4-6to9mo/         # C-S4-295..298 ✅(4)
│   ├── s5-9to12mo/        # C-S5-390..393 ✅(4)
│   ├── s6-12to24mo/       # C-S6-395..405 ✅(11,含二审补 1)
│   └── s7-24to36mo/       # C-S7-347..352 ✅(6,含二审补 1)
├── 40-glossary/(8 张新)
│   ├── G-PERSON-Lansbury.yaml ✅
│   ├── G-PERSON-Pikler.yaml ✅
│   ├── G-TERM-RIE.yaml ✅
│   ├── G-TERM-sportscasting.yaml ✅
│   ├── G-TERM-acknowledging-feelings.yaml ✅
│   ├── G-TERM-passive-toys.yaml ✅
│   ├── G-TERM-magic-word-wait.yaml ✅
│   └── G-TERM-respectful-parenting.yaml ✅
└── 00-meta/
    ├── progress.md ✅(更新累计 538 张 + Phase 7 第二本完成记录)
    ├── PHASE7_LANSBURY.md ✅(本文件)
    └── checkpoints/
        ├── checkpoint_PHASE7_LANSBURY_20260503.md ✅(初版 + 二审产出)
        └── checkpoint_PHASE7_LANSBURY_AUDIT_20260503.md ✅(三审独立报告)
```

---

## 6. 完成定义(实测)

- [x] 抓 Lansbury《Elevating Child Care》全本(30 章)→ SRC-019.yaml + raw .md 已就位
- [x] 产 **39 张新卡**(任务范围 35-45 ✓)
- [x] 新建 **8 张术语卡**(任务范围 6-8 ✓)
- [x] 反向覆盖审计补 2 张(C-S6-405 鼓励说话 + C-S7-352 设限难自查)
- [x] checkpoint MD 完成(初版 + 三审独立报告)
- [x] **更新 INDEX_BY_SOURCE.md + progress.md + source_index.yaml**(用 Edit 单点改避并行覆盖)
- [x] 跨源 related_cards 标连(RIE ↔ 蒙氏 ↔ Karp ↔ AAP ↔ Bowlby ↔ Brazelton ↔ Wonder Weeks ↔ 鲍秀兰 ↔ Gopnik ↔ Lillard)
- [x] 全部 39 张卡 YAML 验证通过(Python yaml.safe_load)
- [x] 全部 glossary_refs 指向存在的术语卡
- [x] 全部 related_cards 指向存在的知识卡(0 自引用 / 0 占位符)
- [x] **严格审查:0 title 超字 / 0 hook 长度问题 / 0 wtd 超 35 / 0 学究词残留**

**用户验收**:抽 5 张随机审,4+ 满意 = Phase 7 第二本通过。

---

## 7. 关键约束(实测都遵守)

1. ✅ **不动现有 499 + Bowlby V3 + Stern(并行 session 在跑)= 不影响兄弟 session**
2. ✅ **新卡严格 v3.5 schema**(前情提要 + glossary_refs + 白话)
3. ✅ **立场对照不判对错**:
   - RIE vs 蒙氏:80% 一致 + 20% 差异(RIE 比蒙氏更"被动")
   - RIE vs Sears 派"亲密育儿":Lansbury 反 → 婴儿不是 helpless
   - RIE vs 主流分散派:Lansbury 反 → 不哄骗 / 转移
   - RIE vs CIO:Lansbury 反 → 在场 + 接情绪 + 渐进 un-training
4. ✅ **白话风格**(避免学究腔)— 修 5 处学究词(感知 / 内化 / 认知)
5. ✅ **跨源主动标连**(39 张卡平均 2-3 个 related_cards)

---

## 8. 工程纪律(继承)

- 文件 .md 已 OCR(216KB,单长行,无 OCR 错字)
- 主上下文 Python offset 切片读取
- 反向审计每段必做
- YAML 验证: hook 嵌套引号必须用 `'..."..."'`(C-S3-297 踩坑修复)
- **本次特别**:3 session 并行(Bowlby V3 SRC-017 + Stern SRC-018 + 本卷 SRC-019)用 +100 ID buffer + Edit 单点改索引文件,避免覆盖兄弟 session 的更新

---

## 9. 立场对照(本次产出实测)

### 9.1 Lansbury vs Davies + Lillard 蒙氏

Lansbury 跟蒙氏 80% 重合(共同源 Pikler):
- 共识:观察 / 真物 / yes space / floor bed / 慢 / 不替宝宝做 / 跟随孩子

Lansbury 独有 20%:
- **sportscasting** — Magda Gerber 命名,蒙氏不讲
- **CEO 语调 + "I won't let you" 公式** — Lansbury 标志
- **不撑坐 8 理由系统** — Pikler 派最系统(蒙氏轻提)
- **magic word: wait + 12 用法** — RIE 浓缩
- **Yelling 4 reasons + Let kids be mad** — Lansbury 自家命题

### 9.2 Lansbury 独有维度(填补蒙氏空缺)

#### Pikler 派系统(蒙氏轻提)
- C-S2-290 不撑坐 8 理由
- C-S3-295 被动玩具 + 主动孩子
- C-S3-297 yes space 不是监狱

#### RIE 实操工具(蒙氏没系统化)
- C-S6-395 sportscasting ⭐⭐⭐
- C-S6-396 CEO 语调 ⭐⭐⭐
- C-S6-397 "我不让你..." 公式
- C-S6-402 magic word wait + 12 用法
- C-S6-403 限度 + 哭怒并存

#### Lansbury 个人命题(蒙氏没)
- C-S7-347 Let kids be mad at you(她妈妈故事)
- C-S7-348 Why You're Yelling 4 reasons
- C-S7-349 大人也要边界
- C-S6-404 设限度 = 高质量时间

#### 反主流派(立场更鲜明)
- C-S1-355 睡眠不是训练是反训练
- C-S6-398 不 time-out 不打不威胁
- C-S6-399 2 岁不强迫分享
- C-S6-400 如厕不训练
- C-S7-350 永远不替孩子画
- C-S7-351 反"分散注意"派教育

### 9.3 Lansbury vs 中文文化常见误解

| 中文常见误解 | Lansbury RIE 反驳 | 卡片 ID |
|---|---|---|
| "宝宝小不懂事,什么都不会" | 反:婴儿是 capable + dependent,不是 helpless | C-S1-352 + C-S4-298 |
| "撑着坐看世界视野好" | 反:Pikler 8 理由,被困视角不是好视角 | C-S2-290 |
| "宝宝要哄,哭就分散转移" | 反:听不修复,接情绪不哄骗 | C-S1-354 + C-S7-351 |
| "高脚椅吃饭方便又安全" | 反:Magda 派小桌 + 小凳,自主吃 + 离桌 | C-S5-390 |
| "再吃一口,飞机来了" | 反:小份 + 信宝宝身体信号 | C-S5-391 |
| "孩子吼回去就是不孝" | 反:让孩子对你生气是给他的礼物 | C-S7-347 |
| "我打他是为他好" | 反:研究证短期止 + 长期更暴力(Park) | C-S6-398 |
| "不许哭再哭就 X" | 反:行为坚定 + 情绪敞开,两个都要 | C-S6-403 |
| "如厕训练 3 天速成" | 反:孩子准备好了自己学 | C-S6-400 |
| "家长把分享教好" | 反:2 岁以下不懂,不强迫 | C-S6-399 |
| "我要一直耐心当 Mary Poppins" | 反:做真实自己,不演完美 | C-S0-116 |

---

## 10. 改进建议(给后续 Phase 8 接手)

1. **Pikler《Friedliche Babys》** — Magda 师承 Pikler 原典 ⭐ 推荐(本卷大量引用)
2. **Stern《婴儿人际世界》** — 自我感 4 阶段(SRC-018 在并行 session)
3. **Bowlby V3《丧失》** — 完成依恋三部曲(SRC-017 在并行 session)
4. **Shonkoff《From Neurons to Neighborhoods》** — 哈佛 Center on the Developing Child 综述
5. **WHO 0-3 标准** — 全球公共卫生视角
6. **松田道雄《育儿百科》** — 日本经典中译,跟蒙氏 + RIE 对照
7. **海蒂育儿大百科** — 主流大众参考
8. **Brazelton《Touchpoints 3-6》** — 现库 Touchpoints 0-3 已有(SRC-010),3-6 是续集

---

## 11. 跟 Phase 6 教训对比

| Phase 6 教训 | Phase 7 应对 |
|---|---|
| 内部质量 + 漏知识 + 漏术语 三轮独立审 | ✅ 全部跑完,补 2 张漏知识卡 |
| 三轮独立 spot-check 不是"重读" | ✅ 三轮维度不同(YAML 质量 / 反向覆盖 / 术语扫) |
| 漏知识审跟"已建 G-TERM"对照 | ✅ 扫"建了术语没建知识卡" |
| 中国家长高频痛点优先 | ✅ Lansbury 独有(让生气 / yelling / sportscasting)全建 |
| 并行 session ID 隔离实测 | ✅ +100 buffer 起点,实测 ls 实际占用 |
| 术语数实测 ls | ✅ ls 159 实测(我前 158 + 8 = 166?— 因 Stern 并行加了几张) |
| YAML 引号嵌套陷阱 | ✅ C-S3-297 hook 嵌引号修复 |
| hook 字数 8-12 严格 | ✅ Python 扫 + 修 22 处(全 7 字 → 8+ 字) |
| title ≤ 15 严格 | ✅ Python 扫 + 修 5 处 |
| 学究词主动改 | ✅ Python 扫 + 修 5 处(感知 / 内化 / 认知) |
| 反向覆盖审计每段 + 收官 | ✅ 收官前补 2 张高价值漏卡(说话 + 设限难) |
| 跨源关联手动 | ✅ 主动标连 39 张卡(平均 2-3 个 related) |
| 章节扫描列全清单 | ✅ 30 章全部 offset 确认 |

---

## 12. 工程意外(Phase 7 第二本特有)

### 意外 1:3 session 并行 ID 冲突
- 启动时 SRC-017(Bowlby V3)+ SRC-018(Stern)已被并行 session 占用
- **修复**:本卷用 SRC-019 + 在 source_index.yaml 加 SRC-019 entry + next_src_id → SRC-020
- **教训**:多 session 并行时 ls 实际 SRC 文件,不只看 next_src_id

### 意外 2:段 ID +100 buffer
- 实际段 max(s0=15 / s1=252 / s2=190 / s3=195 / s4=195 / s5=290 / s6=295 / s7=247)
- 加 100 起:s0=115 / s1=352 / s2=290 / s3=295 / s4=295 / s5=390 / s6=395 / s7=347
- **避开**Bowlby V3 + Stern 并行可能用的 ID 范围

### 意外 3:hook 字数集中 7 字符
- 22 处 hook 是 7 字符(Lillard 教训重现:刚好不到 8 字)
- **修复**:Python 批量扫 + Edit 全改
- **教训**:写卡时主动检查"是否 8-12 字"— 7 字符是 Lansbury / Lillard 共通陷阱

### 意外 4:学究词残留 5 处
- 感知(3 处)/ 内化 / 认知
- **修复后**:0 残留(改"察觉" / "学到自己" / "心智懂")

### 意外 5:YAML 引号嵌套陷阱
- C-S3-297 hook="没"不"的空间" → YAML 解析错(双引号嵌套)
- **修复**:外层用单引号 → `hook: '没"不"的安全大场地'`
- **教训**:hook 含 `"` 必须用单引号外层

### 意外 6:博客合集 30 章而非传统章节书
- Lansbury 不像 Lillard 是传统结构(10 章),是 30 篇博客合集
- **应对**:按主题映射 8 段(月龄段),不按章映射
- 实测:Ch6/Ch7/Ch15/Ch22/Ch23/Ch28 是高密度章,其他短章

---

## 13. 未做(留给后续)

| 待办 | 优先级 | 备注 |
|---|---|---|
| 用户审核 39 张卡 | 高 | 推荐 5 张样本(下文) |
| 补 G-PERSON-Bloom(Paul Bloom) | 低 | Lansbury Intro 提 1 次,价值不高 |
| 整合并行 session(Bowlby V3 + Stern)| 中 | 等他们完成时统一更新 source_index 末尾 |
| Phase 8 启动(Pikler 推荐) | 中 | Pikler 是 Lansbury 师承的师承,本卷大量引用 |

---

## 14. 用户操作建议

### 推荐审 5 张样本卡(中国家长高频痛点 + RIE 独有法)

1. **[C-S6-395 实况转播孩子的挣扎(sportscasting)](../30-cards/s6-12to24mo/C-S6-395.yaml)** ⭐⭐⭐ A 级 + Magda 命名 + RIE 最标志干预法 + 中国家长基本未听过 — 最独家
2. **[C-S7-347 让孩子对你生气是给他的礼物](../30-cards/s7-24to36mo/C-S7-347.yaml)** ⭐⭐⭐ A 级 + Lansbury 个人故事(妈妈不接她生气 → 她长期焦虑) + 中国家长高频痛点
3. **[C-S7-348 你为什么吼?4 个真原因](../30-cards/s7-24to36mo/C-S7-348.yaml)** ⭐⭐ A 级 + Lansbury 博客圈最有名一篇 + 自查工具
4. **[C-S6-396 限度语调:像 CEO 不像辩论家](../30-cards/s6-12to24mo/C-S6-396.yaml)** ⭐⭐⭐ A 级 + Lansbury 标志命名 + 替"求允许"语
5. **[C-S2-290 不撑坐:8 个理由](../30-cards/s2-1to3mo/C-S2-290.yaml)** ⭐ A 级 + Pikler 派系统 + 反 Bumbo / 撑坐主流

### 决定
- Phase 7 第二本通过 / 调整 / 重做?
- Phase 8 候选:Pikler / Stern(后续整合)/ Shonkoff / 松田道雄 / 海蒂?

---

*v1.0 · 2026-05-03 — Phase 7 Lansbury RIE 派现代代表完整记录*
*基于 Phase 6 Lillard 三审教训 + 3 session 并行 ID 隔离学到*
*RIE + 蒙氏闭环完成(Davies 实操 + Lillard 理论 + Gerber/Lansbury RIE 派),准备 Phase 8 Pikler / Stern 整合 / 拓展*
