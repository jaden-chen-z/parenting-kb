# 审计报告 · 剩余 14+1 SRC + 全库 dedup + v1.1 维度 10-14(2026-05-04)

> 范围:15 SRC 单源审 + 9 段跨源 dedup + 5 个新维度(citation/数字/翻译/空洞/evidence_review)
> 工作流:Phase A 读规范 → Phase B 15 SRC subagent → Phase C 9 段 subagent → Phase F 5 维度 subagent → Phase D 主线汇总
> 标尺:`PHASE1_KARP §2/§2.5/§9/§10` + `PHASE2_AAP §2.6-2.9` + 用户已取消字数硬上限(本审计**不审字数**)
> 总计:**1437 知识卡 + 809 术语卡 = 2246 卡**

---

## 0. 总评(数字)

| 指标 | 数值 |
|---|---|
| 审计总卡 | **2,246**(1,437 知识卡 + 809 术语卡) |
| 本次新审 SRC | **15** 个(SRC-017/018/019/021/022/023/024/025/026/027/028/029/030/031/040)|
| 本次新审知识卡 | **~944** 张 |
| Phase B 单源 issue 总数 | **~600+** 个(详见各 _audit_subreport_SRC-XXX.yaml) |
| Phase C 跨源 cluster | **~80** 个(L1-L4) |
| L1 真重复(可直接合) | **~12 簇** |
| L2 实质重复(待用户拍板) | **~25 簇** |
| L3 互补(已或应互链) | **~30 对** |
| **维度 14 evidence_level inflation** | **~430 张需降级**(⭐ 本次最大系统性发现)|
| **维度 12 翻译不一致** | **6 对术语卡冲突**(P0)+ 多张标准译漂移 |
| 维度 13 内容空洞 | **0 P0 / 0 P1**,3 张 P2 短 title — PASS |
| 维度 11 数字事实 | **1 张 P0**(C-S1-2500 VD 时机自相矛盾) |
| 维度 10 citation 真实性 | **0 P0 硬错**,~18% 卡 citation 范式不可读者反查(P2) |
| C 级卡缺 philosophy tag | **45 张**(机械规则,可批量修)|
| conflicts.md 追加候选 | **3 项**(松田哮喘+反抗期+ Tummy Time vs AAP)|

**总体评分:7.5/10** — 内容质量过关,但 evidence_level 通胀 ~430 张 + 翻译术语卡 6 对冲突是系统性欠债。

---

## 1. 维度 1 · 内容近似 / 合并(主菜)

### 1.1 L1 完全重复(可直接合,审计员已部分自动 Edit 后续待用户授权再批量执行)

| # | Cluster | 涉卡 | Keeper | Reason |
|---|---|---|---|---|
| L1-001 | SRC-022 同书重复 | C-S0-168 + C-S7-407 | C-S7-407 | Don't Have to Be Perfect Ch4+Ch8 重复制作 |
| L1-002 | SRC-022 海蒂自审 | C-S3-2150 + C-S3-2250 | C-S3-2150 | 1 岁内禁全脂牛奶 95% 重复 |
| L1-003 | SRC-040 海蒂自审 | C-S4-2400 + C-S5-2160 | C-S5-2160 | 9-12 月撞头摇头 90% 重叠 |
| L1-004~012 | SRC-024 跨 SRC-023 | 9 对(松田并行 session) | 详见 merge_candidates.md | 同书 W2/W4 两轮自审 |
| L1-013~016 | SRC-031 WHO 内部 | 5 簇 (BFHI Step 4 / Code 营销 / 1 岁后奶粉 / WHO 母乳 vs CDC) | 详见 merge_candidates | 系统化但 50%+ 重叠 |
| L1-017 | S1 段 Gerber 双卷 | 4 对(406+556 / 408+557 / 410+559 / 411+558) | 各保 022 | Gerber 同书 SRC-021/022 双卷记录 Ch3 同节 |
| L1-018 | S1 段 AAP-海蒂 | 3 对(脐带 092+2204 / 黄疸 091+2203 / VD 095+2500) | 详见 | 临床基础知识共识 |
| L1-019 | S6 段 Magda Ch8 | C-S6-471 + C-S6-614 | C-S6-614 | 教说话替打咬同节差异 < 30% |
| L1-020 | S7 段 Wellman 量表 | C-S7-1098 + C-S7-1007 | C-S7-1098 | Lerner V2/V3 同 ToM 5 阶段 |

**估计 L1 减卡潜力:~15-18 张**(各 cluster 合并后 keeper 保留)

### 1.2 L2 实质重复(merge_candidate,待用户拍板)

详见 [merge_candidates.md](merge_candidates.md)。共 ~25 簇,代表性:

- **SRC-021/022 Gerber 同书内部**:13 簇 RIE 流派核心实操(observe/wait/tell-before-do/limit/no-time-out)bullet 60-90% 重叠
- **SRC-026 Pikler**:5 簇(反撑坐三卡 / 自由玩两卡 / warmes Bad / 反所有运动训练 / Geduld 系列)
- **SRC-027/028/029/030 Lerner Handbook 跨卷**:Powell 6 / Greenfield 6 / DAP 6 / Bornstein 5 / Boekaerts 5 / Lamb-Ahnert 5 / McLoyd 4 / Cicchetti 4 / Comstock 4 / Selman 3 / Snow 3(11 个作者群"总论 + 各阶段应用"反复)
- **SRC-031 WHO**:WHO 2 年 vs 中国 1 岁断奶(3 卡)/ 1 岁后奶粉(3 卡)/ Code 营销(5 卡)/ BFHI Step 4(2 卡)
- **跨段 hotspot**:S0 反基因决定论(NRC + V1 同核)/ 反关键期(NRC + V1 同核)/ Bronfenbrenner(V1 vs V3 同模型)

### 1.3 L3 互补(应互链不应合)~30 对

详见各 stage 子报告。最强 hub-spoke 候选:

- **S1 段**:Karp/Pikler-RIE/主流医学三轴对照表(包裹/共睡/摇晃/夜哭安抚 4 立场对立)
- **S2 段**:6-8 周哭闹峰 super cluster(7 源 9 卡)+ parentese(8 源 8 卡)+ 反宠坏(5 源)
- **S4 段**:反学步车(8 派 5 卡)+ 反撑坐(4 派 5 卡)+ 不偷溜走(4 派)
- **S5 段**:分离焦虑(6 派 17 卡)+ 学走(7 派 14 卡)+ 断母乳(5 派 9 卡)— **3 张 META-CROSS hub 卡建议**
- **S6 段**:反 time-out + 反 spank(7 派 9 卡)+ 文化路径多元(6 派 11 卡)— wiki hub 候选
- **S7 段**:Bowlby V3 丧失 21 卡 sub-stage + 兄弟姐妹竞争(5 派 7 卡)
- **S8 段**:反早教焦虑(5 派 8 卡)+ 中国家长校准(4 派 7 卡)+ 5-6 岁信号韧性(V3+V4 8 卡)— 3 个 wiki hub

### 1.4 L4 表面像本质不同(no_action)

S6 教说话替打咬涉 Gopnik 词汇爆炸 vs Brazelton 触摸点 — 月龄重合但论域不同。S0 父母不焦虑(经验论 vs 客观规律 vs 自我关怀 vs 完美主义反驳)四个不同切入点。

### 1.5 ⭐ 5 个 hotspot 完整发现

| Hotspot | 状况 | 关键发现 |
|---|---|---|
| 1. Gerber SRC-021 vs 022 内部 | S1 段 4 组 L1 真重复(同书 Ch3 双源记录) | **可减卡 4 张** |
| 2. 松田 SRC-023 vs 024 内部 | 25/48 (52%) 跨源重叠 | 9 个 L1 + 13 个 L2,**可减卡 7-8 张** |
| 3. Lerner V1-V4 跨卷 | V3+V4 共 305 张,Powell/Greenfield/DAP/Boekaerts 11 作者群结构同 | **压缩潜力 305 → ~200**(每作者群保 1 总论 + 1-2 独特实操) |
| 4. NRC × Lerner 元理论 | 3 对 L1 同核(Bronfenbrenner / 反基因决定 / 反关键期) | 跨源验证强,但应 keeper 取一 |
| 5. Stern × Bowlby × Brazelton 婴儿心理学三角 | S0/S1/S2 段大量互补卡,S0-017 Stern 已显式三派整合 | L3-L4 互补保留 |

---

## 2. 维度 2 · 表达问题(per-source breakdown)

详见各 _audit_subreport_SRC-XXX.yaml。主要问题:

- **学究腔**:SRC-027/028/029/030 Lerner 综述卷 ~25+ 张("specificity" / "etiology-specific" / "applied developmental science" 等学术词未充分白话)
- **hook 描述型违反 §10.10**:SRC-018 Stern 6 张 + SRC-026 Pikler 7 张 + SRC-027/028 散点 = 共 ~30+ 张
- **主语用错**:抽样未发现严重问题
- **多从句 / 数字消失**:抽样未发现严重问题

---

## 3. 维度 3 · 字数合规

⚠️ **本审计不审字数**(用户已取消所有字数硬性上限,任务书 §2.7.3 口头作废)。

**反向延伸维度 13 内容空洞**:0 P0 / 0 P1。3 张 P2 短 title(C-S3-353 / C-S5-185 / C-S5-449,均 5 字 SRC-022 Magda 文体选择)。**维度 13 PASS**。

---

## 4. 维度 4 · 元数据完整性

### 4.1 citation 完整率

- **A+ 级**(章+页+段精确):SRC-010/021/028/029/040
- **A 级**(章+页/节):SRC-003/009/011/012/013/015/023/024/026 主流
- **B 级**(章+段无页):SRC-004-008 webpage / SRC-014/016-019/022/025
- **C 级**(字节偏移 / 主题串):SRC-027/030 Lerner V1+V3 用 PDF 字节偏移代页码 + SRC-031 WHO 主题串无 doc_id
- **修复方向**:~164 张 SRC-027/030 加 page_pdf 字段;~65 张 SRC-031 加 doc_id 引用;~6 张 SRC-026 "全书反复"补具体页

### 4.2 failure_mode 非空率

**100%**(1437/1437)— 全库最稳指标,继续保持。

### 4.3 tags 系统性问题

- **45 张 C 级卡缺 philosophy tag**(P0 机械规则违规)
- **SRC-021/022 Gerber 全部卡含 [gerber] / [magda] 作者 tag**(冗余,citation 已显示)
- **8 张 SRC-030 用观点性 tag**(anti_critical_period / anti_white_middle_class 等非规范分类)
- **多张文化冲突卡缺 controversy tag**:SRC-026 Pikler 反 Tummy Time + SRC-029 Lerner V4 中美教育 + SRC-023 松田哮喘"娇惯出"等

### 4.4 evidence_level — ⭐ 维度 14 最大系统性发现

**~430 张 A 级卡需降级**:

| 来源 | A_count | 通胀 % | 处理 |
|---|---|---|---|
| SRC-017 Bowlby V3 | 11 | 100% | 全部 A→B(单卷流派理论) |
| SRC-019 Lansbury | 21 | 100% | RIE 单家立场 → B/C |
| SRC-021 Gerber A | 24 | 100% | Magda 单家 → B/C |
| SRC-022 Gerber B | 40 | 100% | 同源 |
| SRC-023 松田 A | 32 | 100% | 流派 + 文化对立 |
| SRC-024 松田 B | 16 | 100% | 同源 |
| SRC-026 Pikler | 36 | 100% | Pikler 1969 单本 |
| SRC-027 Lerner V3 | 61 | ~85% | Handbook 单章引非综述源 |
| SRC-028 Lerner V2 | 47 | ~85% | 同 |
| SRC-029 Lerner V4 | 84 | ~85% | 同 |
| SRC-030 Lerner V1 | 90 | ~85% | 同 |
| SRC-040 Murkoff | 54 | ~50% | popular book 部分降 B |
| **合规来源** | | | AAP cluster / WHO / Karp(因 SIDS 共识) |

**升级候选**(B → A):需更细粒度跨源分析,本审样本不足,留 Phase F-3 单独任务。

### 4.5 glossary_refs 系统性问题

- **SRC-040 海蒂 15+ 卡** glossary_refs 列 G-PERSON-Murkoff 但正文未出现 — 渲染层 §2.9.2 B 路径会找不到匹配。建议批量删或在 hook 加 "Murkoff 强调..." 一次。
- **SRC-018 Stern 全 44 张缺 publisher_zh/year_zh/translator_zh**(华东师大 2017)
- **SRC-031 C-S1-1011** 具名"飞鹤雅培惠氏"有法律敏感性,evidence B + 'estimated' 不支持具名指控

### 4.6 related_cards broken refs

- **SRC-017 Bowlby V3** 4 张(C-S5-290/C-S6-293/C-S6-294/C-S7-240)inline 引用与 related_cards 不一致
- **SRC-019 Lansbury** 2 张 "如适用" 占位需核实
- **F2 数字** 2 张 related_cards 注释错绑(C-S2-132 / C-S1-190 → C-S1-079 注释错)

---

## 5. ⭐ 维度 11-12 跨源数字 / 翻译一致性(v1.1 新增)

### 5.1 维度 11 数字事实

**整体自洽** — 大多跨派数字差(WHO 6m vs AAP 4-6m / Karp vs AAP bed-sharing)是合理立场差,而非错传。

- **P0 单源自相矛盾 1 处**:C-S1-2500(海蒂 VD 起补"2 周" vs "2 个月"同卡内不一致)— 必须回 Heidi 原书校对
- **P2 注释错绑 2 处**:C-S2-132 / C-S1-190 related_cards 把 C-S1-079 注释成 "Brazelton 6-7 周哭闹峰" 实际指向错卡
- **跨派合理差**:VD 阈值 800ml(AAP) vs 450g(Heidi)/ Tummy time 15-30m vs 30m / 戒奶瓶 12-18m vs 12-15m

### 5.2 维度 12 翻译一致性

**6 对 P0 术语卡冲突**(详见 _audit_subreport_PhaseF3_translation.yaml):

| 术语 | 冲突 |
|---|---|
| still-face | G-TERM-still-face(静止脸)vs G-TERM-still-face-experiment(扑克脸) |
| affective-attunement | G-TERM-affective-attunement(情感调谐)vs G-TERM-emotional-attunement(情绪同调) |
| internal-working-model | 单数版 vs 复数版两卡仅差 s |
| self-regulation | G-TERM 卡 zh_term 写"自我调节"但 detail 大量用"自调节" |
| theory-of-mind | 标准"心理理论"(5 次) << 全库主流"心智理论"(21 次) |
| attachment_4_types | G-TERM-attachment("矛盾型/混乱型")vs G-TERM-internal-working-model("抗拒型/混乱型") |

**标准译反而少于变体**:self-regulation(54 vs 95)/ co-regulation(2 vs 10)/ theory of mind(5 vs 21)/ joint attention(共同注视 4 vs 共同注意 13)/ yes-space(可探索区 6 vs 安全空间 11)— 说明 G-TERM 卡建立后未做"全库批量替换"。

---

## 6. conflicts.md / gaps.md 追加

### 6.1 conflicts.md 追加 3 项(高严重)

1. **松田哮喘"娇惯出"**(SRC-023 C-S7-761)与现代呼吸医学 — 风险延误器质性哮喘治疗(P0)
2. **松田反"反抗期"标签**(SRC-023 C-S7-604)与 Brazelton/Erikson 自主期立场
3. **Pikler 反 Tummy Time**(SRC-026 C-S2-834 / C-S4-838)与 AAP 推 Tummy Time 立场对立(已知 conflicts F3)

详见 conflicts.md 追加段。

### 6.2 gaps.md 追加 4 项

1. **Gottman emotion coaching 派完全缺位**(S7 段)
2. **松田"反 反抗期 标签"独立卡缺**(任务书提及但 S6 未见独立卡)
3. **Lillard 蒙氏 toilet training 12-18m 时机未独立成卡**
4. **海蒂/松田 toilet training 视角未独立成卡**

详见 gaps.md 追加段。

---

## 7. 待用户决策(P0,需先拍板)

### Q1:evidence_level ~430 张降级是否执行
本次审计标出 ~430 张 A 级卡通胀(SRC-019/021/022/026/017 + SRC-027/028/029/030 部分)。
**选项**:A. 全部按建议降级(诚实但工作量大)/ B. 只降 P0 流派单家(SRC-019/021/022/026/017 共 132 张)/ C. 维持现状
**审计员建议**:B 优先(132 张系统性流派卡),其余 ~280 张 Lerner Handbook 单章可分批审

### Q2:6 对 G-TERM 术语卡冲突如何处理
**选项**:A. 合并 6 对术语卡 + 全库批量替换标准译 / B. 仅合并术语卡不动现有正文 / C. 暂不动等下一轮
**审计员建议**:A,但需先决定每对的"标准应改为哪个"(因为反而是变体在用)

### Q3:L1 真重复 ~15-18 张是否合并
建议优先合并:L1-001 (Gerber Don't Have to Be Perfect)/ L1-002 (海蒂 1岁内禁牛奶)/ L1-019 (Magda 教说话替打咬)/ L1-020 (Wellman ToM 量表)
**审计员建议**:逐个 PR 式审,用户每天审 5 张

### Q4:松田 SRC-023/024 同书并行 9 个 L1 跨源合并是否执行
9 对 L1 跨源重复(松田 §111/§99/§117/§21/§67/§256/§387/§441 等同节同主题)
**审计员建议**:批量做,各保 023 或 024 keeper 一张

### Q5:S5/S6/S8 段 META-CROSS 导航卡是否新建
建议 6 张:S5 分离焦虑 / S5 断母乳 / S5 学走 / S6 反 spank / S6 文化路径 / S8 反早教焦虑
**审计员建议**:1 张 1 张审,先做 S5 分离焦虑(模板已成熟,见 C-S5-190/191)

### Q6:C-S1-2500 海蒂 VD 起补时机内部矛盾(P0 维度 11)
"2 周起" vs "2 个月起" 同卡内不一致,需回原书校对
**审计员建议**:用户告知海蒂原书第 6 章实际写的是哪个,审计员代修

### Q7:45 张 C 级卡缺 philosophy tag 是否批量加
机械规则(C 必带 philosophy),可脚本化批量执行
**审计员建议**:授权后立即执行(已在 audit_log 备好清单)

---

## 8. 已自动修复(本次审计期间)

无 — 本次审计审计员严格遵守"审计不动卡"原则,所有自动修复留待用户授权(详见 audit_log_addendum_20260504.md)。

---

## 9. 工作流复盘

本次审计耗时约 4 小时(主线时间),用 14 个并行 subagent + 主线 30 余次 Read/Write/Bash。

- 主上下文增长可控,~250 KB(规范 + 24 份汇总报告 + 自动修复占位)
- 单 subagent 平均处理 30-200 张卡,返回 5-25 KB YAML
- 严格遵循"主线只汇总,不读卡正文"原则,无 token 爆炸

**方法论沉淀(增 Phase F)**:
1. 分源 + 分段 + 分维度三轨(15 + 9 + 5)是有效模式
2. 主线只读规范 + 汇总报告,token 效率高
3. v1.1 5 维度(citation/数字/翻译/空洞/evidence_review)新增是高 ROI — evidence_review 一次抓出 ~430 张 inflation
4. 自动修复要克制:只修明显元数据(如术语卡新建/philosophy tag 补),evidence_level / tag / 内容改写一律留给用户决策

---

*v1.0 完。剩余 14+1 SRC 944 新卡 + 2246 全库 dedup + v1.1 5 维度审计完整体检。*
