# 审计报告 · 10 本书 491 张知识卡 + 148 张术语卡(2026-05-03)

> 审计员:新 session,按 `audit_prompt_447_cards.md` v1.0 执行
> 实际规模:**491 张知识卡 + 148 张术语卡 + 10 本书**(提示词写 447 + 146 + 9 本,审计期间已增长 — 多出 SRC-016 Lillard 44 张 + 自审补几张 + 新增术语 2 张)
> 工作流:Phase A(主线读规范)+ Phase B(10 个 SRC 并行 subagent)+ Phase C(8 个 stage 并行 subagent)+ Phase D(主线汇总)
> 标尺:`PHASE1_KARP §2/§2.5/§9/§10` + `PHASE2_AAP §2.6-2.9`(术语卡 + glossary_refs + 前情提要)
> **重要**:本审计**不审字数**(用户已明确取消所有字数硬性上限,见 `feedback_parenting_kb_no_word_limit.md`)

---

## 0. 总评(数字)

| 指标 | 数值 |
|---|---|
| 审计卡片总数 | **491**(原审计提示词 447,新增 44) |
| 审计术语卡总数 | **148**(原 146,新增 2) |
| 审计 source 数 | **10**(原 9,新增 SRC-016 Lillard) |
| failure_mode 非空率 | **100%**(491/491) ✅ |
| citation 完整率 | **~99%**(SRC-012 全部 32 卡缺 publisher_en;C-S1-039 历史报错已修) |
| evidence_level 升级候选 | 5 张(主要在 Bowlby V2 + 鲍秀兰 + Davies) |
| evidence_level **降级**候选 | **22 张**(主要 Davies 8 张 + Lillard 7 张 + Karp 5 张 + Brazelton 7 张应降 B/C) |
| philosophy/controversy tag 缺失 | **70+ 张**(Bowlby V1 28 + Bowlby V2 5 + Karp 13 + 其他散点) |
| glossary_refs 孤儿/缺失 | **80+ 张**(Brazelton 38 张孤儿引用 + Gopnik 31 张三作者书漏 + Davies 8 张未挂 sensitive-periods 等) |
| 重复簇 | **35+ 个**(其中 5+ 派同主题"超饱和簇"6 个) |
| 主题 gap | **40+ 个**(P0 严重 12 个) |
| conflict 候选 | **18 个**(其中真冲突 12 个,余 6 个属命名/视角差异) |
| Star ⭐ 跨派背书卡已落地 | **6 张**(C-S4-125 / C-S5-130 / C-S5-069 / C-S6-126 / C-S6-133 / C-S7-039) |

**总体质量评分:8.1/10**(各源加权平均) — 内容质量过关,主要欠债在元数据(tag / glossary_refs / evidence_level 诚实性)+ 系统性 gap(临床基础卡空白)+ 跨派冲突未显式建对照卡。

---

## 1. 维度 A · 单卡质量(per-source breakdown)

### 1.1 各源得分一览

| Source | 卡数 | 得分 | 主要欠债 |
|---|---|---|---|
| SRC-003 Karp | 33 | 8.0/10 | evidence_level 通胀 5 张应 B→C;philosophy/controversy tag 漏 13 处 |
| SRC-004~008 AAP cluster | 63 | **9.0/10** | controversy tag 漏 9 处(中国文化对照卡未标);7 个疫苗缩写术语缺(Hib/IPV/PCV/HepA/HepB/Varicella/Rotavirus) |
| SRC-009 鲍秀兰 | 86 | 8.0/10 | 8 张学术引用伤白话(Romeo 2018/Hubel-Wiesel/Darwin/Lewis 等);C-S3-023 中西分歧 controversy 漏 |
| SRC-010 Brazelton | 79 | 8.2/10 | **38+ 个 glossary 孤儿引用**(Winnicott/Erikson/ADHD/habituation/sleep-cycle 等高频);8 张 evidence_level A 通胀 |
| SRC-011 Bowlby V1 | 37 | 8.2/10 | **28 张缺 philosophy/controversy tag**(Bowlby 原典作为依恋理论应大量标);12 张缺 G-PERSON-Ainsworth 默认互链 |
| SRC-012 Bowlby V2 | 32 | 8.2/10 | 3 张旗帜卡缺 philosophy(C-S5-089/C-S6-087/C-S6-098);**32 卡全缺 publisher_en**;G-TERM-role-reversal 在主卡 C-S6-093 漏挂(P0) |
| SRC-013 Wonder Weeks | 35 | **7.5/10** | **2017 复制研究失败完全未披露(P0 学术诚实性)**;C-S6-129 EEG 证据 A 级过高;6 张 epsilon 输入错误"周ε≈"批量替换 |
| SRC-014 Davies | 47 | 8.2/10 | **G-TERM-sensitive-periods + G-TERM-observation 缺失(P0,已修)**;8 张 evidence_level A 应降 B(蒙氏 philosophy 不应 A) |
| SRC-015 Gopnik | 35 | 8.0/10 | 3 张 P0:核心术语在主卡漏挂(C-S4-188 categorical-perception / C-S5-180 social-referencing / C-S5-182 fast-mapping);Meltzoff 1977 复制争议未披露;31 张三作者书漏挂 Meltzoff/Kuhl |
| SRC-016 Lillard | 44 | 8.0/10 | 7 张 evidence_level 高估(Lillard 独有命题应 B/C);8 张 glossary_refs 偏简(蒙氏术语未用足) |

**亮点共识**:
- failure_mode 100% 不空(491 张零空)— 全库最稳指标
- citation 5 必填项几乎 100% 完整(只有 Bowlby V2 系统性缺 publisher_en)
- 白话风格整体过关,只有鲍秀兰 8 张 + Brazelton 7 张含未译英文/学术引用是问题点

### 1.2 P0 问题清单(必修,18 项)

| # | 卡片/项 | 问题 | 修复动作 |
|---|---|---|---|
| 1 | C-S6-093 | role-reversal 主卡未挂 G-TERM-role-reversal(术语孤立) | 加 glossary_refs |
| 2 | C-S5-089 | 住院妈陪缺 philosophy/controversy/safety 多 tag | tags 改 [coping_strategy, safety, philosophy, controversy] |
| 3 | C-S6-087 | "再不听话妈妈走"威胁抛弃,旗帜卡缺 philosophy | tags 加 philosophy |
| 4 | C-S6-098 | 撤回爱,旗帜卡缺 philosophy | tags 加 philosophy |
| 5 | C-S4-188 | "听音是黑白不是灰" = categorical-perception 概念,主卡漏挂 G-TERM-categorical-perception | 加 glossary_refs |
| 6 | C-S5-180 | title 就是 social-referencing,漏挂 G-TERM-social-referencing | 加 glossary_refs |
| 7 | C-S5-182 | title 就是 fast-mapping,漏挂 G-TERM-fast-mapping | 加 glossary_refs |
| 8 | C-S1-241 + C-S2-183 + C-S5-181 | Meltzoff 1977 新生儿模仿 + 镜像神经元 + 9 月延迟模仿,2016/2018 复制争议完全未披露 | why_matters 加披露 + evidence_level 降 B + tags 加 controversy |
| 9 | SRC-013 全 35 卡 | 2017 复制研究失败完全未披露(Wonder Weeks 最大学术诚实性问题) | 新增 1 张"Wonder Weeks 学术争议"卡 |
| 10 | C-S6-129 | "跃迁有 EEG 物理证据"标 A,但缺独立复制 | 降 B + why_matters 加披露 |
| 11 | G-TERM-sensitive-periods 缺失 | 蒙氏核心术语没有 glossary 卡,5+ 张卡引用断链 | **本审计已新建** ✅ |
| 12 | G-TERM-observation 缺失 | 蒙氏方法论起点术语缺,4+ 张卡引用断链 | **本审计已新建** ✅ |
| 13 | C-S2-122 占位符 | failure_mode 残留 "C-S3-XXX",未替换为 C-S3-129 | Edit 直接修 |
| 14 | C-S1-012 | 标 B 但实际仅引 Karp 哲学论断,无独立 Tier 1/2 研究支撑 | evidence_level 改 C |
| 15 | C-S1-026 | 标 B 但内容是 Karp 第 15 章对"白天累点晚上睡好"的反驳论断,无独立研究 | evidence_level 改 C + 加 controversy |
| 16 | SRC-013 6 张 | "周ε≈"OCR 输入错误(C-S4-124/S5-126/S5-127/S6-122/S6-123/S6-124) | 全局批量替换 |
| 17 | Brazelton 38 张孤儿 | glossary_refs 指向不存在的 G-PERSON-Winnicott/Erikson/G-ABBR-ADHD 等 | 批量补建 glossary 或暂从 refs 删除 |
| 18 | AAP 7 个疫苗缩写 | C-S5-007 + C-S1-064 涉 Hib/IPV/PCV/HepA/HepB/Varicella/Rotavirus,glossary 全缺 | 批量补建 G-ABBR-XXX 7 个 |

### 1.3 P1 问题清单(重要,40+ 项)

详见每个 SRC 子审报告(已留存在 subagent 输出)。主要类型:
- **evidence_level 通胀**:Davies 8 张 + Brazelton 8 张 + Lillard 7 张 + Karp 5 张 + Bowlby V2 1 张 = 共 29 张应降 B/C
- **philosophy/controversy tag 漏**:Bowlby V1 28 张(系统性)+ Bowlby V2 5 张 + Karp 13 张 + 其他散点 = 共 60+ 张
- **glossary_refs 缺关键术语**:Bowlby V1 12 张缺 G-PERSON-Ainsworth + Gopnik 30+ 张缺 G-PERSON-Meltzoff/Kuhl + Davies 8 张缺 G-TERM-practical-life/sensitive-periods
- **citation 缺英文出版社**:SRC-012 全部 32 张缺 publisher_en("Hogarth Press / Tavistock Institute of Human Relations")

### 1.4 P2 问题清单(可选优化,80+ 项)
- 跨源反向链接(Lillard → Davies/Gopnik 单向)
- 蒙氏术语词典缺(rouge test / blicket / NVC 等)
- 个人术语词典缺(Bruner / Sorce-Emde / Kagan / Lewis 等)
- 部分标题英文/中文比例不统一

---

## 2. 维度 B · 跨源重复 / 整合

### 2.1 5+ 派"超饱和簇"6 个(整合质量最高)

| # | 主题 | 段 | 涉及源 | 卡片数 | 整合质量 |
|---|---|---|---|---|---|
| 1 | **5S 安抚单元** | S1 | Karp + AAP-Sleep + AAP-Crying + Davies + Lillard | 23 张 | 已自然分工(Karp 操作 / AAP 校准 / 蒙氏反对),但缺总览导航卡 |
| 2 | **6-9 月陌生人焦虑** | S4 | AAP + Brazelton + Bowlby + Wonder Weeks | 5 张 | **C-S4-125 是 ⭐ 跨 4 派整合卡,真实落地** |
| 3 | **9-12 月分离焦虑** | S5 | Bowlby V1 + Bowlby V2 + Brazelton + Wonder Weeks + Davies + AAP + 鲍秀兰 | 10 张 | **6 派全覆盖,跨派交叉验证最完整一段** |
| 4 | **反体罚 / 不打孩子** | S6 | Brazelton + Bowlby V1+V2 + Wonder Weeks + Davies + Lillard + 鲍秀兰 | 7 张 | **7 派一致 ⭐(C-S6-126 + C-S6-133 已主动整合)** |
| 5 | **学步车反对** | S4 | AAP + Davies + Lillard | 3 张 | 一致(任务书声称 4 派,鲍秀兰 S4 无独立卡是 gap) |
| 6 | **第四产程 / exterogestation 概念群** | S1 | Karp + Brazelton + Davies + Gopnik + Lillard | 6 张 | 5 派同主题异表述(子宫四感 / 独立的人 / 6-8 周共生期 / 长童年期 / 3 大问题),**缺概念地图整合卡** |

### 2.2 跨源整合不足(35+ 簇)

详见 8 份 stage 子报告。共性问题:
- 多张卡讲同主题但 related_cards 互链不完整(Brazelton/Davies 大量反向引 Bowlby 但 Bowlby V1 未反向引)
- 同一神经发育事件多个名字未做术语统一(如 6-8 周事件:Karp 哭闹峰 / Brazelton 触点 / WW8 跃迁 / Bowlby 6 周非选择性微笑)
- "中国传统育儿"立场在 7 派中只有鲍秀兰单源代言,导致"全部都是西方流派内部对话"偏差

### 2.3 evidence_level 升级候选(5 张)

跨多源同主题验证的卡,但仍标 B/C,可升级:
- **C-S4-016 鲍秀兰"8 月前抱抱不会宠坏"** B → A(Bowlby/Ainsworth 4 派背书,任务书 ⭐)
- **C-S6-008 鲍秀兰"中场休息(time-out)"** C → B(AAP/APA 推荐方法)
- **C-S2-001/004 哭闹峰** B → A(Karp + AAP + Brazelton + Wonder Weeks 4 派 + Brazelton 1962 N=82 + Wessel 3-3 共识)
- **C-S6-021 Brazelton "discipline = teaching"** A 可保留(已有 6 派一致 + AAP)
- **C-S5-076 过渡客体** B → 接近 A(Stevenson 苏格兰 1/3 婴儿 + Winnicott + 多源)

---

## 3. 维度 C · 主题覆盖 / 遗漏

### 3.1 严重 gap(P0)— 12 项

按段排序,中国家长高频痛点优先:

| # | 段 | 缺失主题 | 严重度 | 建议来源 |
|---|---|---|---|---|
| 1 | S0 | **产检窗口**(NT/大排畸/糖耐/B 群链/抗 D)0 卡 | P0 | 中文产科指南 / ACOG / WHO |
| 2 | S0 | **待产包 + 分娩计划 + 无痛分娩决策** 0 卡 | P0 | Penny Simkin / 鲍秀兰孕产篇 |
| 3 | S0 | **妊娠并发症识别**(妊高/糖/胎位异常)0 卡 | P0 | ACOG 指南 |
| 4 | S1 | **新生儿黄疸** 0 卡(0-1 月最常就医原因) | P0 | SRC-008 AAP H&S |
| 5 | S1 | **脐带护理 + 残端脱落** 0 卡 | P0 | SRC-008 AAP / 鲍秀兰 |
| 6 | S1 | **新生儿筛查**(足底血/CCHD/PKU)只有 1 张听筛(C-S1-066) | P0 | SRC-008 AAP |
| 7 | S2 | **2 月儿保 + 第一波疫苗**(DTaP/Hib/IPV/PCV/HepB/Rotavirus)0 卡 | P0 | AAP Red Book + 中国 CDC |
| 8 | S2 | **早期昼夜节律萌芽**(melatonin 6-8 周) 0 卡 — 任务书明列 | P0 | AAP / Mindell 睡眠书 |
| 9 | S3 | **母乳→混合喂养过渡** 0 卡(产假结束高峰刚需) | P0 | La Leche League / WHO |
| 10 | S4 | **过敏原引入**(花生/鸡蛋/牛奶 LEAP 早暴露)0 卡 — 任务书明列 | P0 | SRC-006 AAP Feeding |
| 11 | S5 | **睡眠训练抉择**(extinction/Ferber/no-cry/fading)0 跨派对比卡 | P0 | AAP + Karp + Ferber + Sears 综述 |
| 12 | S6/S7 | **24 月 M-CHAT 自闭症筛查** 0 卡 | P0 | AAP Bright Futures |

### 3.2 重要 gap(P1)— 15+ 项

S0:产前抑郁筛查 / 月子文化 vs 产后恢复循证 / 母乳喂养准备
S1:维生素 K 注射 / 第一次儿保(3-5 天/2 周/1 月)/ PURPLE 完整框架 / 原始反射全套(Moro/rooting/sucking/palmar/stepping)
S2:被动免疫下降 / 配方奶冲调安全 / 大小便监测 / 浴疹湿疹起点
S3:4 月儿保 + 第二波疫苗 / 翻身后床上安全升级
S4:噎食 vs 干呕区分 / "不爬也正常"AAP 立场 / 6 月儿保 + 第三波疫苗 / 9 月儿保 + ASQ 筛查
S5:**指物 pointing / 意图性沟通**(任务书明列"语言能力最强预测因子") / 戒夜奶时机 / 精细动作精度
S6:18 月儿保 + 第四波疫苗 / picky eating 全程指南 / 牙刷训练 / 二孩家庭 / 与祖父母不一致
S7:词汇爆炸 + 句子语法 / 36 月发育里程碑全检 / 第二胎适应 / 完整如厕 SOP

### 3.3 红旗信号月龄链 — 已完整覆盖 ✅

| 月龄 | 卡片 | 来源 |
|---|---|---|
| 1 mo | C-S1-066 | 鲍秀兰(听筛迟发) |
| 2-3 mo | C-S2-009 | 鲍秀兰(不看人脸) |
| 6 mo | C-S3-024 | 鲍秀兰(4 项异常) |
| 18 mo | C-S6-012 | 鲍秀兰(4 项)+ C-S6-033 Brazelton(哲学层) |
| 24 mo | C-S7-013 | 鲍秀兰(7 项任一) |

**Gap**:9-10 mo + 12-15 mo 节点无独立红旗卡;36 mo 全检表缺。AAP M-CHAT 18/24 月标准化筛查未独立成卡。

### 3.4 4 流派立场覆盖

任务书要求 4 流派(RIE / Pikler / 蒙氏 / Brazelton)+ 中医文化对照:
- ✅ **蒙氏**:Davies 47 + Lillard 44 = 91 张,体系最完整
- ✅ **Brazelton**:79 张,8 段全覆盖
- 🟡 **RIE**:无独立 source(只在 Davies/Lillard 卡内引用 yes space / tarry time / wait-watch)— **gap**
- 🟡 **Pikler**:无独立 source(只在 Davies/Lillard 卡内引用 floor bed / freedom of movement)— **gap**
- ✅ **中医/中国传统**:鲍秀兰 86 张代言,但仅一源(其他派对中国文化的对照大多隐性)

---

## 4. 维度 D · 立场冲突(conflicts.md 候选)

详见 `00-meta/conflicts.md` 已填充版。本次审计共提名 **18 个 conflict 候选**,其中 12 个真冲突(需要标 controversy + 跨派对照卡),6 个属命名/视角差异(只需 mutual_link)。

### 4.1 高严重度真冲突(7 项)

1. **包裹 swaddle**:Karp/AAP 主张 vs Davies/Lillard 蒙氏反对 vs 鲍秀兰反"打蜡烛包"
2. **共睡 cosleep**:Karp 10 步共睡 vs AAP 严禁 bed-sharing
3. **奶嘴 pacifier**:Karp 鼓励 vs AAP 中立(SIDS 保护)vs Davies/Lillard 反对
4. **如厕训练时机**:Lillard 12-18 月反潮流 vs AAP 18 月-3 岁 vs 鲍秀兰 9 月坐盆 vs Brazelton 弹性 — **4 派 4 套时机标准 + 鲍秀兰内部矛盾**
5. **反早教 / Mozart effect**:Brazelton + Gopnik + Lillard 三派反对 vs 中国早教焦虑(闪卡/双语/Mozart)
6. **婚姻 vs 孩子优先**:Lillard ⭐ vs 中国"为孩子牺牲"(C-S7-135 + Davies C-S6-138)
7. **撤回爱 / 威胁抛弃**:Bowlby V2 强烈反对 vs 中国常用"妈不要你了"

### 4.2 中等严重度真冲突(5 项)

8. **戒奶瓶时间线**:AAP 12-18 月 + sippy 过渡 vs Lillard 9-10 月 + 完全反 sippy vs Brazelton 反"必须几月戒"
9. **睡眠训练**:Lillard 关门睡(C-S5-189)vs Davies 反强训 vs Brazelton 温和拍背 vs AAP 6 月+ 可启动 vs Bowlby 反对
10. **爬行 vs 不爬**:鲍秀兰"缺爬有害" vs Lillard "sitter 也健康"(缺 AAP 西医背书)
11. **拒学 vs 逃学**:Bowlby V2 严格区分 vs 中国教育界统称"不肯上学"
12. **强独立 / 懂事**:Bowlby V2 警告"懂事 = 焦虑回避型" vs 中国常夸"我家娃真懂事"

### 4.3 视角差异(非真冲突,只需 mutual_link)6 项

13. **第四产程命名**:Karp / 蒙氏 exterogestation / Brazelton "独立的人"
14. **6-8 周事件命名**:Karp 哭闹峰 / Brazelton 触点 / WW8 跃迁 / Bowlby 非选择性微笑
15. **物体永久性月龄**:Piaget 8-10 月行为版 vs Spelke 4 月认知版(同一现象不同测试)
16. **3 岁画像**:Brazelton "second honeymoon" / Bowlby 分离更难 / Lillard "上学龄"
17. **关键期 vs 敏感期术语**:鲍秀兰用 critical period / Davies+Lillard 用 sensitive periods(本质不同概念,**已新建 glossary 区分**)
18. **依恋形成路径**:鲍秀兰"妈妈喂养=主依恋" vs Bowlby "敏感回应者=主依恋"(Bowlby C-S2-070 直接颠覆)

---

## 5. ⭐ Star 跨派背书卡(已落地 6 张)

这些卡是知识库最高质量产出,适合作为跨源整合范本:

| 卡 ID | 主题 | 跨派背书 | 段 |
|---|---|---|---|
| **C-S4-125** | 跃迁周龄 ↔ 依恋时间表对照 | AAP + Brazelton + Bowlby + Wonder Weeks(4 派 ⭐) | S4 |
| **C-S5-130** | 1 岁前两份心理大礼(信任环境 + 信任自我) | Davies + Bowlby secure attachment + 多派呼应 | S5 |
| **C-S5-069** | 健康依恋让分离焦虑反更早 + 度过更快 | Bowlby + AAP + Davies + Brazelton(4 派一致) | S5 |
| **C-S6-126** | 跃迁期不打不骂 | Wonder Weeks + Bowlby + 鲍秀兰(主动整合) | S6 |
| **C-S6-133** | 温柔但清晰边界 | Davies + Bowlby + 鲍秀兰 + AAP + Lillard(5 派 ⭐) | S6 |
| **C-S7-039** | 5 岁前住院影响到 18 岁 | Bowlby V2(Douglas 4000+ 长期追踪 A 级证据) | S7 |

---

## 6. 已自动修复(本次审计期间)

| # | 文件/卡 | 修复内容 |
|---|---|---|
| 1 | `40-glossary/G-TERM-sensitive-periods.yaml` | 新建术语卡(P0)— 蒙氏核心术语,5+ 张卡引用断链 |
| 2 | `40-glossary/G-TERM-observation.yaml` | 新建术语卡(P0)— 蒙氏方法论起点,4+ 张卡引用断链 |

详见 `00-meta/checkpoints/audit_log_20260503.md`。

**未自动修复**(均需用户审过后做):
- 22 张 evidence_level 降级(影响知识诚信,需用户拍板)
- 70+ 张 tag 增改(需用户审 philosophy/controversy 适用性)
- 80+ 张 glossary_refs 补挂(需先批量建 glossary 卡如 G-PERSON-Winnicott/Erikson 等)
- 32 张 SRC-012 补 publisher_en(需用户确认书名)
- Wonder Weeks 复制争议披露 + 新增 1 张争议元卡(影响内容,需用户授权)
- Meltzoff 复制争议披露 + evidence_level 降 B(同上)

---

## 7. 待用户决策(P0,需先拍板)

### Q1:Wonder Weeks 复制争议如何披露
2017 复制研究(van der Veer / Plas-Plooij Pediatrics 类)未能精确验证 10 个时间表。SRC-013 全 35 卡未披露这一最大学术争议。
**选项**:
- A. 在 C-S6-129 加披露 + 降 B + 加 controversy(最小改动)
- B. 新增 C-S6-130 "Wonder Weeks 学术争议" 元卡(完整披露)
- C. 全 35 卡批量加 controversy(最严格)
**审计员建议**:B(平衡可信度 + 工程量)

### Q2:Meltzoff 1977 新生儿模仿如何处理
2016 PLOS ONE + 2018 Developmental Science 大规模复制失败,但 C-S1-241 仍标 A 级 + 用"42 分钟模仿"作头条。
**选项**:
- A. 降 B + why_matters 加披露
- B. 全部降 B,Gopnik 4 张 ToM 序列卡都补"复制争议未解"(C-S1-241/C-S2-183/C-S5-181 等)
**审计员建议**:B(科学诚信优先,中国家长会传 Meltzoff 实验为定论)

### Q3:evidence_level 22 张降级是否执行
本次审计共标出 22 张 evidence_level 通胀(蒙氏 / Karp 一家言 / Brazelton 临床观察被标 A)。
**选项**:
- A. 全部按审计建议降级(诚实但可能让某些核心卡看起来"不够权威")
- B. 只降 P0 几张(C-S1-012/026 + C-S6-129)
- C. 维持现状(用户接受当前 evidence_level 标尺)
**审计员建议**:A 但分批审(每批 5 张审一次)

### Q4:tag 系统性补 philosophy/controversy 是否执行
本次审计标出 60+ 张 Bowlby V1 + Karp + 散点缺 philosophy/controversy。
**选项**:
- A. 全部按审计补(几乎每张 Bowlby V1 卡都加 philosophy + 部分加 controversy)
- B. 只补 P0 旗帜卡(C-S5-089/C-S6-087/C-S6-098 等 5 张)
- C. 暂不动,等用户对 tag 体系做最终决策
**审计员建议**:A — Bowlby V1 是依恋理论原典,philosophy 漏标会让检索时找不到

### Q5:7 个疫苗缩写术语 + 关键人物术语是否批量补建
缺失高频术语:G-ABBR-{Hib,IPV,PCV,HepA,HepB,Varicella,Rotavirus} + G-PERSON-{Winnicott,Erikson,Ainsworth,Bruner,Spelke,Field,Kuhl(确认是否已建),Gerber,Montessori}
**选项**:
- A. 全部建(~15 张新术语卡,工程量大)
- B. 只建被引用 ≥3 次的(如 Winnicott / Erikson / Ainsworth / Meltzoff / Kuhl 共 5-6 张)
- C. 暂不建,从对应卡的 glossary_refs 中删除孤儿引用
**审计员建议**:A(术语卡是知识图谱基础,补全 1 次后续永久受益)

### Q6:S0 + S1 临床基础卡 P0 缺口是否补
S0 缺产检 + 分娩 + 并发症;S1 缺黄疸 + 脐带 + 新筛 + Vit K。这是中国家长产房+月子高频痛点。
**选项**:
- A. 启动 Phase 7,抓 1 本中文产科书 + 完整 AAP 临床卡 cluster(预估 30-40 张新卡)
- B. 只补 S1 5 张关键卡(黄疸/脐带/新筛/Vit K/第一次儿保)
- C. 维持"心理-安抚-依恋"侧偏重,不补临床
**审计员建议**:A — 没有循证医学产科腿,知识库无法应对真实新生儿期

---

## 8. 下一步建议

### 8.1 立刻可做(本周内)
1. ✅ 已修复 G-TERM-sensitive-periods + G-TERM-observation(P0 元数据)
2. 用户拍板 Q1-Q6 后,执行对应的批量修复
3. 修明显错字:C-S2-122 占位符 + Wonder Weeks 6 张"周ε≈"

### 8.2 短期(本月内)
1. 补 P0 临床卡(若 Q6 选 A 或 B):S0 产检/分娩/并发症 + S1 黄疸/脐带/新筛/Vit K + S2 2 月疫苗 + S5 睡眠训练对比卡
2. 补关键术语(若 Q5 选 A 或 B):G-PERSON-{Winnicott,Erikson,Ainsworth,...} + G-ABBR-疫苗系列
3. 写跨派对照卡(P1):tantrum 4 法对比 / 如厕 3 派对比 / 戒奶瓶 3 派对比 / 睡眠训练 4 派对比

### 8.3 中期(下月)
1. 启动 Phase 7 — 建议抓 RIE(Gerber《Your Self-Confident Baby》)+ Pikler — 补 4 流派覆盖
2. 跨源反向链接补全(Lillard → Davies/Gopnik 已做,需反向)
3. 写 wiki 整合卡:第四产程概念群 / 6-8 周事件群 / 5S vs 蒙氏不打扰 / S1 红旗就医总索引

### 8.4 长期(下季度)
1. 启动 Phase 8 — 中文产科 + WHO 喂养指南(中文 Tier 1)
2. 完整 4 流派立场覆盖(RIE + Pikler 进库)
3. 用户家应用层:大宝 + 二宝月龄对照,把 491 张卡按当前月龄做"今日推荐"过滤

---

## 9. 工作流复盘

本次审计耗时约 2 小时(主线时间),用 18 个并行 subagent(10 SRC + 8 stage)处理 491 + 148 张卡。
- 主上下文增长可控,~150 KB(规范 + 18 份汇总报告 + 自动修复)
- 单 subagent 平均处理 30-90 张卡,返回 5-15 KB YAML
- 严格遵循"主线只汇总,不读卡正文"原则,无 token 爆炸
- 唯一意外:SRC-016 数量(原审计提示词 9 本 447 张,实际 10 本 491 张)需在主线动态调整范围

**方法论沉淀**:
1. 分源 subagent + 分段 subagent 双轨是有效模式 — SRC 视角发现单卡问题,Stage 视角发现跨源问题
2. 主线只读规范 + 汇总报告,不读卡正文,token 效率高
3. 必须在 prompt 里明示"不审字数"(用户已取消上限),否则 subagent 会按旧标准产生大量 false positive
4. 自动修复要克制:只修明显元数据缺失(如术语卡新建),evidence_level / tag / 内容改写一律留给用户决策

---

*v1.0 完。本次审计期间未触发 questions_for_user.md 新增条目,所有判断点均在本报告 §7 待用户决策。*
