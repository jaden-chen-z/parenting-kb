# Progress · 育儿知识库

## 当前阶段

**Phase 6 第一本完成**(2026-05-03)— Gopnik / Meltzoff / Kuhl《The Scientist in the Crib》/《摇篮里的科学家》(SRC-015, 35 张知识卡,认知科学经典)。
**累计知识库**:Karp(33)+ AAP(63)+ 鲍秀兰(86)+ Brazelton(79)+ Bowlby V1(37)+ Bowlby V2(32)+ Wonder Weeks(35)+ Davies(47)+ **Gopnik(35)** = **447 张知识卡** + **146 张术语卡** + **15 个 SRC**(其中 13 个被卡片实际引用)。
**任务书**:Phase 1 v1.2 / Phase 2 v1.4 / Phase 3 (BAOXIULAN + BOWLBY_VOL1) / Phase 4 WONDER_WEEKS / Phase 5 MONTESSORI_BABY / Phase 6 SCIENTIST_IN_CRIB。
**进行中**:**Lillard《Montessori from the Start》** — 与 Davies 形成蒙氏闭环(理论原典 vs 现代实操)。
**待办**:用户审 9 本累计 447 张卡 + Lillard 完成后做整本 conflicts.md 整理。

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

### Phase 4 两本并行完成(2026-05-03)

**任务书**:`00-meta/PHASE4_WONDER_WEEKS.md` v1.0(本 session)+ Bowlby Vol 2 任务书在并行 session

**全部完成**:
- [x] **SRC-012 Bowlby Vol 2《分离》(32 张)**(并行 session,凌晨开始)
  - S5(4 张):分离时玩偶毯子 / 寄养换家年龄 / 怕生 = 陌生 + 靠近 / 住院妈陪 vs 不陪
  - S6(18 张):**抗议-绝望-超脱 3 阶段 ⭐** / 重聚不认妈危险 / 撤回爱当惩罚 / 精神虐待边界 / 父母吵架孩子怕分开 / 别让娃当情绪保姆 / 我是为你好的陷阱 / 等
  - S7(10 张):**别偷溜要正面告别 ⭐** / **5 岁前住院影响到 18 岁 ⭐** / 拒学 vs 逃学不同 / 强独立不健康 / 等
  - 新术语:G-PERSON-Robertson(住院儿童纪录片) / G-TERM-protest-despair-detachment(3 阶段) / G-TERM-defensive-exclusion / G-TERM-pathological-mourning / G-TERM-anxious-attachment / G-TERM-role-reversal / G-TERM-agoraphobia / 复用术语 G-TERM-attachment / G-TERM-separation-anxiety / G-TERM-internal-working-model / G-PERSON-Bowlby
- [x] **SRC-013 Wonder Weeks《婴儿大脑跃迁 10 周》(30 张)**(本 session,11:30-12:13)
  - S1(4):**三 C 信号 = 跃迁不是病 ⭐** / **10 跃迁时间表 ⭐** / 早产校正 / 5 周第一跃迁
  - S2(5):8 周模式 / 12 周平滑过渡 / fussy 期不睡训不戒奶 / **fussy 期再崩溃别摇宝宝 ⭐** / 跃迁后突然长大
  - S3(4):19 周事件世界 / 4-5 月 fussy 可达 6 周 / **4 月奶量骤降不是断奶 ⭐** / 4 月想逃走不是失败
  - S4(5):26 周关系世界 / **跃迁周龄↔依恋时间表对照 ⭐** / **fussy 不是出牙痛 ⭐** / 6-8 月拒换尿布 / 8 月跃迁前奏
  - S5(4):37 周分类 / 46 周序列 / 撒娇也是 fussy / 8-12 月双跃迁妈妈极限
  - S6(6):55 周程序 / 64 周原则 / **75 周系统世界 ⭐** / 13-18 月三连击 / **跃迁期不打不骂 ⭐** / "质量时间"是伪概念
  - S7(2):21 月跃迁框架结束 / 跃迁是普遍 = 育儿不孤单
  - 新术语 6 张:G-PERSON-vanderijt / G-PERSON-plooij / G-TERM-wonder-week / G-TERM-mental-leap / G-TERM-3C-signs / G-TERM-fussy-phase
- [x] **并行协调**:+50 buffer ID 隔离,无冲突(SRC-012 用 C-SX-070..099 区间,SRC-013 用 C-SX-120+ 区间)
- [x] checkpoints:`checkpoint_PHASE4_WONDER_WEEKS_20260503.md`(并行 session 应有自己的 checkpoint)
- [x] source_index.yaml + INDEX_BY_SOURCE.md + progress.md(本文件)合并(2026-05-03 并行结束后)

**跨源亮点**:
- ⭐ **C-S4-125** Wonder Week + Bowlby + Brazelton + AAP 四派同时背书 6-9 月怕陌生人
- ⭐ **C-S6-126** Wonder Week + Bowlby + 鲍秀兰 三派一致反对体罚
- Wonder Week WW46-WW75 fussy phase 与 Bowlby Vol 2 分离焦虑窗口完美重合

**待用户**:
- [ ] 抽 5 张随机审 → 4+ 满意 = Phase 4 通过
- [ ] 决定 Phase 5 启动书(候选见下)

## 已抓源数

| Tier | 已抓 | 预估 |
|---|---|---|
| Tier 1 权威机构 | **7**(SRC-001/002 网页 + SRC-004-008 AAP cluster × 5)| ~40 |
| Tier 2 学术 | 0 | ~60 |
| Tier 3 书籍 | **8**(Karp / 鲍秀兰 / Brazelton / Bowlby V1 / Bowlby V2 / Wonder Weeks / Davies / **Gopnik**)+ Lillard 进行中 | ~15 |
| Tier 4 中文权威 | 0 | ~10 |
| Tier 5 视频/播客 | 0 | ~8 |

## 已生成

- 单元:2 个(K-MILE-S5-001, K-MECH-CROSS-001)— Phase 1-6 知识单元层暂跳过
- **知识卡:447 张**(全 v3.5 schema)
  - SRC-003 Karp:33 张
  - SRC-004 AAP Safe Sleep:12 张
  - SRC-005 AAP Crying:9 张
  - SRC-006 AAP Feeding:16 张
  - SRC-007 AAP Milestones:14 张
  - SRC-008 AAP Health & Safety:12 张
  - SRC-009 鲍秀兰:86 张
  - SRC-010 Brazelton:79 张
  - SRC-011 Bowlby V1:37 张
  - SRC-012 Bowlby V2:32 张
  - SRC-013 Wonder Weeks:35 张
  - SRC-014 Davies Montessori Baby:47 张
  - **SRC-015 Gopnik Scientist in the Crib:35 张**(S1: 7 + S2: 4 + S3: 4 + S4: 6 + S5: 4 + S6: 5 + S7: 5)⭐ 新增
  - **段分布**:S0: 11 / S1: 115 / S2: 47 / S3: 51 / S4: 47 / S5: 56 / S6: 79 / S7: 41 = 447
- **术语卡:146 张**(40-glossary/)
  - 2026-05-02:Phase 3 鲍秀兰 + Brazelton 全本完成,首建 S0/S6/S7 段
  - 2026-05-03 早:Phase 3 第三本 Bowlby V1 audit 完成 + SRC-011 补登记 source_index
  - 2026-05-03 凌晨-中午:**Phase 4 两本并行启动 + 完成**
    - 并行 session(凌晨 02:00-11:28)— Bowlby Vol 2 SRC-012(32 张 + 12 术语卡含复用)
    - 本 session(11:30-12:13)— Wonder Weeks SRC-013(30 张 + 6 术语卡)
  - 2026-05-03 12:30+:并行结束后合并 source_index.yaml + INDEX_BY_SOURCE.md + progress.md

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

2026-05-03(Phase 6 第一本 Gopnik《Scientist in the Crib》完成 + SRC-015 补登记 source_index;Lillard 进行中)

## 当前总览(447 张知识卡 + 146 张术语卡 + 8 段:S0-S7)

| Phase | 书 / 来源 | 卡数 | 段覆盖 | SRC |
|---|---|---|---|---|
| 1 | Karp《卡普新生儿安抚法》 | 33 | S1, S2 | SRC-003 |
| 2 | AAP HealthyChildren.org × 5 cluster | 63 | S1-S5 | SRC-004~008 |
| 3 (1) | 鲍秀兰《婴幼儿潜能开发》(中) | 86 | S1-S7(首扩 S6/S7) | SRC-009 |
| 3 (2) | Brazelton《Touchpoints: Birth to 3》(英) | 79 | S0-S7(首扩 S0) | SRC-010 |
| 3 (3) | Bowlby Vol 1《依恋》(中译) | 37 | S1-S6 | SRC-011 |
| 4 (1) | Bowlby Vol 2《分离》(中译) | 32 | S5-S7 | SRC-012 |
| 4 (2) | Wonder Weeks《婴儿大脑跃迁》 | 35 | S1-S7 | SRC-013 |
| 5 | Davies《The Montessori Baby》(蒙氏 0-1) | 47 | S0-S6(首引蒙氏)| SRC-014 |
| **6 (1)** | **Gopnik《Scientist in the Crib》/《摇篮里的科学家》** | **35** | **S1-S7(认知科学全段)** | **SRC-015** |
| 6 (2) | Lillard《Montessori from the Start》| 进行中 | — | (SRC-016 待) |
| | **合计** | **447** | **S0-S7(8 段)** | **13 SRC 引用 / 15 SRC 登记** |

## 下次 session 起点

> 1. **用户验收 8 本累计 401 张卡**(抽样审,尤其 Davies 蒙氏跟其他 7 本立场对照是否到位)
> 2. **决定 Phase 6 第 9 本启动**:
>    - 候选 A:**Lillard《Montessori from the Start》**(0-3 岁完整蒙氏,跟 Davies 形成蒙氏闭环)— **本 session 推荐**
>    - 候选 B:**Bowlby Vol 3《丧失》**(完成依恋三部曲,中译已 OCR)
>    - 候选 C:**Stern《The Interpersonal World of the Infant》**(自我感 4 阶段,与蒙氏 absorbent mind 对话)
>    - 候选 D:**Gopnik《Scientist in the Crib》**(认知科学,与蒙氏 absorbent mind 直接对话)
>    - 候选 E:**Gerber《Your Self-Confident Baby》/ Lansbury(RIE 派)**(尊重式育儿,蒙氏的姐妹流派 — yes space 就是 Gerber 命名)
>    - 候选 F:**Pikler《Friedliche Babys》**(德语育儿,跟蒙氏 floor bed / movement freedom 同根)
>    - 候选 G:**Shonkoff《From Neurons to Neighborhoods》**(NRC 神经发展底座)
>    - 候选 H:**WHO Infant Feeding Guideline**(国际权威循证,Tier 1)
>    - 候选 I:**松田道雄《育儿百科》**(日本经典中译,跨 0-6 岁)
>    - 候选 J:**海蒂育儿大百科**(中译已 OCR)
> 3. **术语卡 backlog**:SRC-010 / SRC-011 / SRC-014 引用的 G-ID 还有部分待建(如 G-PERSON-Uzodike / G-PERSON-Gerber / G-TERM-cestina)
> 4. **conflicts.md 整理**(已积压):Karp vs Davies(swaddle 立场对立,Phase 5 新增)+ 至少 11 处 controversy
> 5. **三派+ 一致卡集中审核**:跨源标连 ⭐ 卡新增(C-S6-133 温柔边界 4 派一致 + C-S5-130 信任两份大礼 + C-S4-132 不学步车)
>
> **下一 session 必读**:
> - `00-meta/checkpoints/checkpoint_PHASE5_MONTESSORI_BABY_20260503.md`(Davies 完整产出 + 跨源对照)
> - `00-meta/PHASE5_MONTESSORI_BABY.md`(Phase 5 任务书)
> - `00-meta/checkpoints/checkpoint_PHASE4_WONDER_WEEKS_20260503.md`(Phase 4 收官)
> - `00-meta/PHASE2_AAP.md` v1.4(§2.5-2.9 schema 规则)
> - `00-meta/PHASE1_KARP.md` §10 实战调整 14 条
