# Progress · 育儿知识库

## 当前阶段

**Phase 3 第三本完成**(2026-05-03 audit)— Bowlby Vol 1《依恋》(中译)产出 = **37 张 v3.5 知识卡(跨 S1-S6)+ 1 SRC**。
**累计知识库**:Karp(33)+ AAP(63)+ 鲍秀兰(86)+ Brazelton Touchpoints(79)+ Bowlby V1(37)= **298 张知识卡** + **92 张术语卡** + **11 个 SRC**(其中 9 个被卡片实际引用)。
**任务书**:Phase 1 v1.2 / Phase 2 v1.4 / Phase 3 任务书 PHASE3_BAOXIULAN.md v1.0(后续 Brazelton + Bowlby 沿用同 schema)。
**待办**:用户审 5 本累计 298 张卡 + 决定第 6 本(候选见下文 §下次起点)。

## 完成度

### Phase 0 Bootstrap(2026-04-30)
- [x] 目录结构(§3)
- [x] schemas 落实(§4 v3)
- [x] 任务书归档到 `00-meta/README.md`
- [x] 项目根 `README.md`
- [x] meta 文件:progress.md / questions_for_user.md / conflicts.md / gaps.md
- [x] source_index.yaml(初始 2 份样本)
- [x] books_to_buy.md
- [x] 2 份样本转 v3 yaml(SRC-001, SRC-002, K-MILE-S5-001, K-MECH-CROSS-001)
- [x] git init + 首次 commit
- [x] 工具栈安装 → 见 `tooling.md`

### Phase 1 Karp(2026-05-01,1 天完成)

**任务书**:`00-meta/PHASE1_KARP.md`(v1.0 → v1.1 加白话风格 → v1.2 加 §10 实战调整 14 条)
**第一本书**:Karp《卡普新生儿安抚法》中译本(SRC-003)

- [x] OCR 长单行文件分块(11 个 15KB chunks 到 `karp_chunks/`)
- [x] 全书结构地图(3 批 subagent)
- [x] 主题反向索引
- [x] 10 个主题包并行提取 verbatim 素材
- [x] SRC-003.yaml(23 个主题块,OCR 错字修正)
- [x] source_index.yaml 更新
- [x] **第一部分 12 张卡片**(C-S1-001..012)— 哭闹机制 + 第四产程 + 5S 概览
- [x] **第二部分 13 张卡片**(C-S1-013..025)— 5S 五招详解 + 拥抱疗法
- [x] **第三部分 8 张卡片**(C-S1-026..033)— 睡眠 + 红旗 + 食物过敏 + 产后
- [x] 反向覆盖审计(每部分跑一次)— 补 9 张高价值漏掉卡
- [x] GitHub Top 3 调研 → §10.13 外部方法论吸收(2000-token 块 / 黑白名单 / non-overlapping / 输入输出比 / ToC)
- [x] checkpoint MD(`00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md`)
- [ ] **用户抽 5 张审核**(待)— 4+ 张满意 = POC 通过

### Phase 2 完成(2026-05-01 ~ 2026-05-02)

**任务书**:`00-meta/PHASE2_AAP.md` v1.4(§2.6 翻译两步走 / §2.7 前情提要 / §2.8 术语卡片化 / §2.9 inline 引用渲染)

**全部完成**:
- [x] R1 Safe Sleep(SRC-004): 9 + 复盘 R1.5 + 3 = 12 张
- [x] R2 Crying & Soothing(SRC-005): 9 张
- [x] R3 Feeding & Pacifiers(SRC-006): 9 + 复盘 R3.5 + 7 = 16 张
- [x] R4 Milestones & Teething(SRC-007): 14 张
- [x] R5 Health & Safety(SRC-008): 12 张
- [x] **AAP 63 张知识卡**(全 v3.5 schema)
- [x] **术语卡 60 张**(40-glossary/)
- [x] Karp 33 张回归 v3.5 schema(并行 batch refactor 完成)
- [x] R5 audit + 4 张新术语卡(RSV/MMR/DTaP/CDC)+ 9 张卡补 glossary_refs
- [x] checkpoint:`checkpoint_PHASE2_AAP_20260502.md`
- [x] INDEX_BY_SOURCE.md + progress.md 更新

**按解读 B 跳过**(留全部书产完后整合):
- [-] cross-validate Karp vs AAP evidence_level 升级
- [-] conflicts.md 整理(Karp vs AAP 立场对立:共睡 028 / 奶嘴 022 等)

**待用户**:
- [ ] 新 session 跑 96 张完整审计(提示词:`00-meta/checkpoints/audit_prompt_96_cards.md`)
- [ ] 决定 Phase 3 启动书(候选见下)

### Phase 3 第一本完成(2026-05-02)— 鲍秀兰

**任务书**:`00-meta/PHASE3_BAOXIULAN.md` v1.0
**第一本书**:鲍秀兰、孙淑英《婴幼儿潜能开发和早期教育》(中国妇女出版社, 2016)(SRC-009)

**全部完成**:
- [x] OCR 已成 .md(286KB / 2869 行,跳过 OCR 工程)
- [x] 章节地图(7 段映射 — S1-S7,首次扩展 S6 + S7)
- [x] **新建 2 段目录**:`30-cards/s6-12to24mo/` + `30-cards/s7-24to36mo/`
- [x] **S1(7 张)**:1 月龄(视听刺激/红旗/把新生儿当懂事/4 大禁忌/关键期/玩具/睡眠)
- [x] **S2(10 张)**:2-3 月龄(俯卧抬头/红旗/语言剥夺/baby talk 5 共性/母婴交谈链/响应需求/**禁打蜡烛包 ⭐**/翻身别独留/出声笑+元音/室温)
- [x] **S3(13 张)**:4-6 月龄(拉坐/强化"妈妈"/视听 6 法/镜子/找朋友/靠坐+跳跃/玩是正经事/藏猫猫/独坐+坐位优势/硬食/**6 月红旗 ⭐**/点头摇头/理性对哭声)
- [x] **S4(10 张)**:7-8 月龄(爬行/认物找物/触额碰头/教 ba/ma/捏取/百宝箱/**戒奶瓶**/制止打人/**8 月前抱抱不宠坏 ⭐**/再见欢迎)
- [x] **S5(12 张)**:9-12 月龄(扶站独站/自我意识/障碍训练/学小勺/**坐盆训练 ⭐**/察言观色/玩娃娃/学说 5 要点/教物名准/走路 5 法/认红色/与人分享)
- [x] **S6(18 张,新建)**:1-2 岁(模仿乱说/儿歌接背/独立走/涂画/学用勺/小伙伴玩/**管教全家一致 + 不打 ⭐**/中场休息/预防发脾气/戴帽脱袜/生活规律/**18 月红旗 ⭐**/跑+倒退+双脚跳/双字词→简单句/用"我"自我意识/主动交往/识颜色/生活自理)
- [x] **S7(15 张,新建)**:2-3 岁(独自上下楼梯/骑三轮车/模仿画/识形状/分辨大小/唱儿歌+说用途/语言表大小便/帮大人做事/学穿鞋/合作玩/跳高跳远+单足站/长短+数数/**24 月红旗 ⭐**/**忽视错误最有效约束 ⭐**/道德意识 5 招)
- [x] **新术语卡 4 张**(40-glossary/):**G-PERSON-Bao**(鲍秀兰人物)+ **G-TERM-critical-period**(关键期/Hubel-Wiesel/Genie 案例)+ **G-TERM-parentese**(父母语 5 共性 + 全球文化共性)+ **G-TERM-turn-taking**(母婴交谈链 + Romeo MIT 研究)
- [x] SRC-009.yaml(stub + referenced_by_cards 完整 85)
- [x] source_index.yaml 更新(SRC-009 + next_src_id → SRC-010)
- [x] INDEX_BY_SOURCE.md 全段更新(总计 181 张 + 64 张术语)
- [x] checkpoint:`checkpoint_PHASE3_BAOXIULAN_20260502.md`

**红旗信号矩阵(Phase 3 总结)**:
- **C-S1-066** 1 月大声没反应 + **C-S2-009** 2-3 月不看人脸 + **C-S3-024** 6 月 4 项 + **C-S6-012** 18 月 4 项 + **C-S7-013** 24 月 7 项
- 完整覆盖 0-3 岁所有月龄段红旗信号链

**立场对照(中文 vs 美国)**:
- ⭐ **C-S2-014 反对中国"打蜡烛包"传统**(与 Karp 包裹立场对照)
- ⭐ **C-S5-012 中国 9 月起坐盆训练**(与 AAP 18 月-3 岁立场对照)
- ⭐ **C-S6-007 鲍秀兰 vs Karp/AAP 体罚立场**(全部反对体罚一致)
- ⭐ **C-S7-014 忽视技巧**(与 Karp 5S 安抚立场不同维度)

**待用户**:
- [ ] 抽 5 张随机审 → 4+ 满意 = Phase 3 第一本通过
- [ ] 决定 Phase 3 第二本(候选见下)

### Phase 3 第二本候选(待启动)

1. **Brazelton《Touchpoints: Birth to Three》** — Karp 引用源,触摸点理论原典(已 OCR 在 raw_pdfs/)
2. **海蒂育儿大百科 0-1 岁** — 中文版,Murkoff 系列(PDF 在 raw_pdfs/,需 OCR)
3. **松田道雄《定本育儿百科》** — 日本经典中译,跨 0-6 岁(已 OCR)
4. **Bowlby《依恋三部曲》** — 依恋理论原典(中译已 OCR,3 卷)

## 已抓源数

| Tier | 已抓 | 预估 |
|---|---|---|
| Tier 1 权威机构 | **7**(SRC-001/002 网页 + SRC-004-008 AAP cluster × 5)| ~40 |
| Tier 2 学术 | 0 | ~60 |
| Tier 3 书籍 | **4**(SRC-003 Karp + SRC-009 鲍秀兰 + SRC-010 Brazelton + SRC-011 Bowlby V1)| ~15 |
| Tier 4 中文权威 | 0 | ~10 |
| Tier 5 视频/播客 | 0 | ~8 |

## 已生成

- 单元:2 个(K-MILE-S5-001, K-MECH-CROSS-001)— Phase 1-3 知识单元层暂跳过
- **知识卡:298 张**(全 v3.5 schema)
  - SRC-003 Karp:33 张(S1: 31 + S2: 2)
  - SRC-004 AAP Safe Sleep:12 张(S1: 9 + S2: 3)
  - SRC-005 AAP Crying:9 张(S1: 8 + S2: 1)
  - SRC-006 AAP Feeding:16 张(S1: 5 + S3: 8 + S4: 2 + S5: 1)
  - SRC-007 AAP Milestones:14 张(S2: 1 + S3: 5 + S4: 3 + S5: 5)
  - SRC-008 AAP Health & Safety:12 张(S1: 9 + S4: 2 + S5: 1)
  - **SRC-009 鲍秀兰:86 张**(S1: 7 + S2: 10 + S3: 13 + S4: 10 + S5: 12 + S6: 18 + S7: 15 + 1 补)
  - **SRC-010 Brazelton:79 张**(S0: 7 + S1-S7 全段覆盖,首扩 S0 孕期段)
  - **SRC-011 Bowlby V1:37 张**(S1: 7 + S2: 5 + S3: 4 + S4: 8 + S5: 8 + S6: 5)⭐
  - **段分布**:S0: 7 / S1: 95 / S2: 29 / S3: 38 / S4: 30 / S5: 36 / **S6: 39 / S7: 24**
- **术语卡:92 张**(40-glossary/)
- 2026-05-02:Phase 3 鲍秀兰 + Brazelton 全本完成,首建 S0/S6/S7 段
- 2026-05-03:Phase 3 第三本 Bowlby V1 audit 完成 + SRC-011 补登记 source_index

## 阻塞

- 无(等用户验收)

## 待用户回答的问题

- Phase 1 33 张卡片是否通过 POC?
- Phase 2 启动哪本书?
- `_drafts_part2/` 旧包裹草稿(原 008/009/010)是否可删?

## 已确认的关键决策

- **Q1 → B**: Phase 1 第一批 fetch 顺手补抓 SRC-001/002 raw HTML(2026-04-30)— **未做,Phase 2 补**
- **Q2 → A**: Phase 1 仅用 Tier 3 书跑通(2026-04-30)— Phase 1 实际只用 SRC-003 一本书
- **Q3 → B → SUPERSEDED**: 卡片语言策略(2026-04-30)— **被 PHASE1_KARP §2 覆盖**:全中文,不双语
- **新增决策(Phase 1 实战)**:
  - 字段名英文 key,展示层翻中文(待建 `render_labels.yaml`)
  - hook 默认填(从可选改为必填,§10.10)
  - evidence_level 单本书阶段标尺(§10.7):C = Karp 一家言 / B = Karp 引外部研究 / A = 与 Tier 1 共识对齐
  - 反向覆盖审计固化为工作流必备步骤(§10.4)

## 上次 session 结束时间

2026-05-03(Phase 3 第三本 Bowlby V1《依恋》中译 audit 完成 + SRC-011 补登记 source_index.yaml)

## 当前总览(298 张知识卡 + 92 张术语卡 + 8 段:S0-S7)

| Phase | 书 / 来源 | 卡数 | 段覆盖 | SRC |
|---|---|---|---|---|
| 1 | Karp《卡普新生儿安抚法》 | 33 | S1, S2 | SRC-003 |
| 2 | AAP HealthyChildren.org × 5 cluster | 63 | S1-S5 | SRC-004~008 |
| 3 (1) | 鲍秀兰《婴幼儿潜能开发》(中) | 86 | S1-S7(首扩 S6/S7) | SRC-009 |
| 3 (2) | Brazelton《Touchpoints: Birth to 3》(英) | 79 | S0-S7(首扩 S0) | SRC-010 |
| **3 (3)** | **Bowlby Vol 1《依恋》(中译)** | **37** | **S1-S6** | **SRC-011** |
| | **合计** | **298** | **S0-S7(8 段)** | **9 SRC 引用 / 11 SRC 登记** |

## 下次 session 起点

> 1. **用户验收 5 本累计 298 张卡**(抽样审,尤其 Bowlby V1 37 张依恋立场是否到位)
> 2. **决定第 6 本启动**(Phase 3 续):
>    - 候选 A:**Bowlby Vol 2《分离》** + **Vol 3《丧失》**(完成依恋三部曲,中译已 OCR)
>    - 候选 B:**Davies《The Montessori Baby》**(0-12 月专用蒙氏实操,英 EPUB)
>    - 候选 C:**Gopnik《Scientist in the Crib》**(认知科学,英 EPUB)
>    - 候选 D:**Stern《The Interpersonal World of the Infant》**(婴儿心理学经典)
>    - 候选 E:**Shonkoff《From Neurons to Neighborhoods》**(NRC 神经发展底座,免费正版)
>    - 候选 F:**WHO Infant Feeding Guideline**(国际权威循证,Tier 1)
>    - 候选 G:**松田道雄《育儿百科》**(日本经典中译,跨 0-6 岁,已 OCR)
>    - 候选 H:**海蒂育儿大百科**(中译已 OCR)
> 3. **术语卡 backlog**:SRC-010 / SRC-011 引用的 G-ID 还有部分待建,可作为独立批量任务
> 4. **conflicts.md 整理**(已积压):Karp vs AAP vs 鲍秀兰 vs Brazelton vs Bowlby 立场对立(共睡 / 奶嘴 / 安抚训练 / 体罚 等至少 8 处 controversy)
>
> **下一 session 必读**:
> - `00-meta/checkpoints/checkpoint_PHASE3_BOWLBY_VOL1_20260503_audit.md`(Bowlby V1 audit)
> - `00-meta/checkpoints/checkpoint_PHASE3_BRAZELTON_20260502.md`(Brazelton 完整产出)
> - `00-meta/checkpoints/checkpoint_PHASE3_BAOXIULAN_20260502.md`(鲍秀兰完整产出)
> - `00-meta/PHASE2_AAP.md` v1.4(§2.5-2.9 schema 规则)
> - `00-meta/PHASE1_KARP.md` §10 实战调整 14 条
