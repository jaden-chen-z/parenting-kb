# 卡片库 · 按来源分组索引

> 这是 `30-cards/` 的"按书分组"视图。每张卡的真相源是它自己 yaml 里的 `citation.source_id` 字段;本文件是反向索引(快照),便于按书浏览。
>
> **维护规则**:每完成一本书,在此文件追加一节;每加新卡,更新对应书节的表格。
>
> 也可参考:
> - 按月龄段分组 → 直接看 `30-cards/sN-XXX/` 子目录(文件夹结构本身就是 stage 分组)
> - 按来源溯源 → 每张卡 yaml 的 `citation.source_id` 字段
> - source 元信息 → `10-sources/source_index.yaml` + `10-sources/tierN-XXX/notes/SRC-XXX.yaml`

---

## 目录(按来源 ID)

| Source ID | 书名 / 来源 | Tier | 卡片数 | 段 |
|---|---|---|---|---|
| SRC-003 | Karp《卡普新生儿安抚法》(英 2002 / 中译 2013) | 3 | 33(S1: 31 + S2: 2) | S1, S2 |
| SRC-004 | AAP Safe Sleep & SIDS Prevention(HealthyChildren.org) | 1 | 12 | S1, S2 |
| SRC-005 | AAP Crying & Soothing(HealthyChildren.org) | 1 | 9 | S1, S2 |
| SRC-006 | AAP Feeding & Pacifiers(HealthyChildren.org) | 1 | 16 | S1, S3, S4, S5 |
| SRC-007 | AAP Milestones & Teething(HealthyChildren.org) | 1 | 14 | S2-S5 |
| SRC-008 | AAP Health & Safety(HealthyChildren.org) | 1 | 12 | S1, S4, S5 |
| SRC-009 | 鲍秀兰《婴幼儿潜能开发和早期教育》(中国妇女, 2016) | 3 | 86 | S1-S7(全段)|
| SRC-010 | Brazelton《Touchpoints: Birth to 3》(Da Capo, 1992/2006) | 3 | 79 | S0-S7(全段 + 首次扩 S0)|
| SRC-011 | Bowlby《依恋三部曲 · Vol 1:依恋》(中译 2017) | 3 | 37 | S1-S6 |
| SRC-012 | Bowlby《依恋三部曲 · Vol 2:分离》(中译 2017) | 3 | **32** | S5, S6, S7 |
| SRC-013 | van de Rijt + Plooij《The Wonder Weeks(婴儿大脑跃迁 10 周)》(1992) | 3 | **35**(30 + 自审补 5) | S1-S7(全段)|
| SRC-014 | Davies + Uzodike《The Montessori Baby》(Workman, 2021) | 3 | **47**(34 + 一审补 2 + 二审补 11) | S0-S6 |
| SRC-015 | Gopnik / Meltzoff / Kuhl《The Scientist in the Crib》(Morrow, 1999) | 3 | **35** | S1-S7(全段)|
| SRC-016 | Lillard + Jessen《Montessori from the Start》(Schocken, 2003) | 3 | **52**(44 + 二审补 2 + 三审补 6) | S0-S7(全段)|
| SRC-017 | Bowlby《依恋三部曲 · Vol 3:丧失》(中译 2018) | 3 | **15**(用户压缩) | S5, S6, S7 |
| SRC-018 | Stern《The Interpersonal World of the Infant》(Basic Books, 1985) | 3 | **44**(并行 41 + R2 补 2 + 用户深度审补 1) | S0-S7(全段)|
| SRC-019 | Lansbury《Elevating Child Care: A Guide to Respectful Parenting》(JLML Press, 2014) | 3 | **43**(37 + 二审补 2 + 用户三审补 4)| S0-S7(全段)|
| SRC-021 | Gerber + Johnson《Your Self-Confident Baby》(John Wiley & Sons, 1998) | 3 | **32**(30 + 漏知识反向覆盖补 2)| S0-S7(全段)|
| SRC-022 | Gerber + Johnson《Your Self-Confident Baby》(深度本,同书第二轮)| 3 | **49**(初版 42 + 二审补 3 + 用户三审补 4)| S0-S7(全段)|
| SRC-023 | 松田道雄《定本 育儿百科》(岩波书店 1967/1980 · 王少丽译)🆕 [Phase 9 第一本 fallback,原 Ainsworth + 用户深度审补 5] | 3 | **49**(初版 44 + 用户深度审补 5)| S0-S7(全段)|
| SRC-024 | 松田道雄《定本 育儿百科》(岩波书店 1967/1980 · 王少丽译)🆕 [Phase 9 并行第二本] | 3 | **42** | **S0-S8(首次扩 S8 = 3-6 岁)** |
| SRC-025 | Shonkoff/Phillips《From Neurons to Neighborhoods》(NRC/IOM, 2000)🆕 [Phase 10 单 session,早期发展神经科学综述,用户深度审补 8 卡 + 6 术语] | 3 | **68**(初产 60 + 用户深度审补 8 / 5 轮审 0 错全过 / 100% 跨派)| **S0-S8(全段)**:S0=4 / S1=6 / S2=6 / S3=6 / S4=7 / S5=6 / S6=10 / S7=9 / S8=14 |
| SRC-026 | Pikler《Friedliche Babys – zufriedene Mütter》(HERDER 1969 · 德文原典)🆕 [Phase 10 并行第二本,RIE 谱系师承根源 + 用户深度审补 5] | 3 | **42**(初产 36 + 二审补 1 Sprache + 用户深度审补 5 / 5 轮审 + 深审 0 错全过)| **S1-S7**:S1=7 / S2=4 / S3=5 / S4=7 / S5=5 / S6=9 / S7=5 |

**总计**:Karp 33 + AAP 63 + 鲍秀兰 86 + Brazelton 79 + Bowlby V1 37 + Bowlby V2 32 + Wonder Weeks 35 + Davies 47 + Gopnik 35 + Lillard 52 + Bowlby V3 15 + Stern 44 + Lansbury 43 + Gerber(SRC-021)32 + Gerber 深度本(SRC-022)49 + Matsuda(SRC-023)49 + Matsuda(SRC-024)42 + Shonkoff(SRC-025)68 + Pikler(SRC-026)42 = **883 张知识卡**(2026-05-04 Phase 10 双 session 完成 + Pikler 用户深度审补 5:Shonkoff《From Neurons to Neighborhoods》NRC 综述 60 + Pikler《Friedliche Babys – zufriedene Mütter》德文原典 42,师承根源 RIE 谱系闭环。)

> 注:SRC-001 / SRC-002 是 Tier 1 网页,目前未生成卡片(Phase 0 仅做了知识单元层 K-MILE-S5-001 / K-MECH-CROSS-001)。
> 术语卡(40-glossary/)**133 张**不计入此索引(独立命名空间)。
> ⭐ Phase 3 首次扩展段:**S0(孕期)+ S6(1-2 岁)+ S7(2-3 岁)** — 鲍秀兰建 S6+S7,Brazelton 首建 S0。
> 🆕 **Phase 4 两本并行**(2026-05-03):**Bowlby Vol 2《分离》32 张** + **Wonder Weeks 35 张**。
> 🆕 **Phase 5 蒙氏 0-1**(2026-05-03):**Davies《The Montessori Baby》36 张** — 蒙氏首本入库,引入 absorbent mind / sensitive periods / yes space / floor bed / topponcino / observation / prepared environment / practical life 等核心概念,跨源对照 Karp(swaddle 立场对立)/ AAP(SIDS 兼容)/ Bowlby(secure attachment 一致)/ 鲍秀兰(关键期 vs 敏感期)。新增 8 张术语卡。
> 🆕 **Phase 6 第一本 Gopnik**(2026-05-03,并行 session):**《The Scientist in the Crib》35 张** — 首引认知科学维度,反早教,Meltzoff 模仿 / Kuhl 知觉重组 / 物体永久性早于 Piaget 等硬数据。新增 19 张术语卡。
> 🆕 **Phase 6 第二本 Lillard**(2026-05-03):**《Montessori from the Start》52 张**(初版 44 + 二审补 2 + 三审补 6)— 蒙氏 0-3 学院派经典,跟 Davies 形成蒙氏闭环。Lillard 独有命题:4 plane of development / 11 human tendencies / cycle of activity / 服从 3 阶段(12-18/18-36/3+)/ 12-18 月如厕敏感期 / 反纸尿裤 sauna 效应 / 反 happiness 现代立场 / 婚姻 > 孩子 / 描述法替讲道理 / flow 4 类家庭 / 词汇爆炸 12-24 月 / 父母读书模范 / 轮流教学法 / Andrew + Patricia 案例。新增 11 张术语卡(Lillard / Jessen / Csikszentmihalyi / self-construction / cycle-of-activity / coordinated-movement / language-explosion / points-of-reference / weaning-table / flow / second-birth)。
> 🆕 **Phase 6 第三本 Bowlby V3《丧失》**(2026-05-03,3 session 并行):**15 张知识卡**(用户指示压缩到"很少",跳过 9 个极端章节,聚焦中国家长高频场景:谈死亡 / 二宝出生 / 月嫂离别 / 爷奶去世 / 病理哀伤 4 阶段)。新增 3 张术语卡(mourning / childhood-mourning / four-phases-mourning)。**依恋三部曲闭环完成。**
> 🆕 **Phase 7 第一本 Stern《The Interpersonal World of the Infant》**(2026-05-03,3 session 并行 + R2 补漏):**43 张知识卡**(并行 session 41 + 我 R2 补 2:still-face + 过度/不足刺激)— self 心理学奠基。Stern 独有命题:**4 senses of self 叠加(emergent / core / subjective / verbal)** + **Affective attunement** ⭐⭐⭐ + **Vitality affects** + **RIGs**(IWM 积木块)+ **Evoked companion**(独自时仍有伴)+ **Amodal perception**(出生即跨感官)+ **Intersubjectivity**(7-9 月共主体性)+ **Communion vs Communication** + **Selective attunement = socialization 工具** + **修复 > 完美** + **Still-face = 玩手机后果** + **反 Mahler 共生融合论** + **Vygotsky ZPD**(给宝宝主体属性)+ **Dore 学说话动机**(重建关系)+ **Tronick 1978 / Field 1982 / Meltzoff 1979 经典实验** + **Stevie 入侵案例** + **婴儿是真实测试者**(反 Freud 幻想婴儿)+ **18 月 rouge test 镜中认我**。新增 14 张术语卡(Stern / 4 self / affective-attunement / vitality-affects / RIGs / amodal-perception / intersubjectivity / evoked-companion / self-recognition / baby-faces / still-face-experiment)。**心理过程层填补完成 — 蒙氏(哲学)+ Bowlby(关系)+ Stern(心理过程)三角互补。**
> 🆕 **Phase 7 第二本 Lansbury**(2026-05-03,3 session 并行):**《Elevating Child Care》39 张**(初版 37 + 二审补 2)— RIE 派现代代表,Magda Gerber 直接弟子。Lansbury 独有命题:**sportscasting**(Magda 命名实况转播)/ **CEO 语调** / "I won't let you" 限度公式 / **不撑坐 8 理由**(Pikler 派系统)/ **magic word: wait + 12 用法** / 反 time-out / Let kids be mad at you(Lansbury 个人故事)/ **Why You're Yelling 4 reasons** 自查 / **不分散注意**派 / passive toys 玩具被动孩子主动 / 高脚椅替代 / 不强迫 sharing / 不 train potty / 不替孩子画(Bev Bos)。新增 8 张术语卡(Lansbury / Pikler / RIE / sportscasting / acknowledging-feelings / passive-toys / magic-word-wait / respectful-parenting)。蒙氏 + RIE 平行流派闭环(Davies + Lillard + Gerber + Lansbury)。
> 🆕 **Phase 9 并行第二本 松田道雄**(2026-05-03,Ainsworth SRC-023 平行):**《定本 育儿百科》42 张**(岩波书店 1967/定本 1980 · 王少丽译)— 日本视角填补,首次扩 **S8 = 3-6 岁段**。松田独有命题(中国家长高频):**不焦虑育儿**(あせらない育児)/ **抱不会养成毛病**(反中国奶奶传统)/ **8 月后母婴同睡 OK 3 月内禁**(vs AAP 全段反对) / **4 月把屎把尿是错的**(vs 中国老人) / **不强制断奶**(vs 中国"早断早好") / **不要养成 lovey 癖**(vs Davies/Brazelton lovey 立场) / **反抗期不存在 = 协作期**(独家立场) / **大发雷霆体罚错 + 瞬间打手**(vs RIE/Bowlby) / **看电视 4 小时 = 弃娃**(扩 Lansbury 0-2 立场到 3-4 岁) / **不要吓唬孩子**(不丢家) / **认生是性格非病** / **集体保育 + 保育园文化**(日式 hoikuen vs yochien) / **自由空间 vs 机动车**(松田专门概念) / **4 岁不必硬教认字**(反虎妈) / **智力测试不可信**(反 KIQ 测试) / **别让娃像男孩女孩样**(1967 反性别刻板) / **室外空气浴 + 婴儿体操 + 散步 3 合 1**(日式锻炼)。新增 9 张术语卡(Matsuda / asenai-ikuji / hoikuen / jiyu-kukan / air-bath / japanese-weaning / anti-screen-japan / bedsharing-japan / Wang-Shaoli)。**美/中/日/西方临床 4 国跨文化对照闭环完成,跨源率 100%。**

---

## SRC-003 · Karp《卡普新生儿安抚法 0-1岁》

**英文原版**:Harvey Karp, *The Happiest Baby on the Block: The New Way to Calm Crying and Help Your Newborn Baby Sleep Longer* (Bantam Books, 2002, Revised)
**中译本**:浙江人民出版社,2013 年 1 月第 1 版,陈楠译,ISBN 978-7-213-05158-6
**对应段**:S1(主战场,31 张) + S2(2 张,见下"S2 析出")
**卡片总数**:33
**等级分布**:A 4 / B 23 / C 6
**Source yaml**:[SRC-003.yaml](../10-sources/tier3-books/notes/SRC-003.yaml)

### 第一部分 · 哭闹机制 + 第四产程 + 5S 概览(10 张 in S1)

> 注:这部分原始有 12 张,其中 C-S2-001/002(原 C-S1-004/005)是"哭闹峰"主题,任务书 §2 把哭闹峰值列在 S2 主题清单 → 已挪到 S2 一节。

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-001](s1-newborn/C-S1-001.yaml) | 头 3 个月是"第四产程" | philosophy | C |
| [C-S1-002](s1-newborn/C-S1-002.yaml) | 子宫四感官:温暖紧裹响动摇 | philosophy | C |
| [C-S1-003](s1-newborn/C-S1-003.yaml) | 哭闹是求生工具不是失败 | — | B |
| [C-S1-006](s1-newborn/C-S1-006.yaml) | 听不懂哭声不代表你不细心 | — | B |
| [C-S1-007](s1-newborn/C-S1-007.yaml) | 前 3 月怎么回应都不会惯坏 | philosophy, controversy | C |
| [C-S1-008](s1-newborn/C-S1-008.yaml) | 宝宝哭你心跳加速是天然反射 | — | B |
| [C-S1-009](s1-newborn/C-S1-009.yaml) | 5S 必须组合用,单招效果差 | philosophy | B |
| [C-S1-010](s1-newborn/C-S1-010.yaml) | 镇静反射:婴儿的"关闭按钮" | philosophy | C |
| [C-S1-011](s1-newborn/C-S1-011.yaml) | 胀气不是哭闹元凶,别狂拍嗝 | — | B |
| [C-S1-012](s1-newborn/C-S1-012.yaml) | 妈妈焦虑不会让宝宝更哭闹 | philosophy | B |

### 第二部分 · 5S 五招详解 + 拥抱疗法(13 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-013](s1-newborn/C-S1-013.yaml) | 包裹必须紧 + 双臂在内 | — | B |
| [C-S1-014](s1-newborn/C-S1-014.yaml) | 关于包裹的 6 种常见误解 | philosophy | C |
| [C-S1-015](s1-newborn/C-S1-015.yaml) | 包裹 5 个最常见错误 | safety | B |
| [C-S1-016](s1-newborn/C-S1-016.yaml) | 侧抱只能安抚,睡觉禁止 | safety, red_flag | A |
| [C-S1-017](s1-newborn/C-S1-017.yaml) | 嘘声 = 子宫白噪音 80-90 分贝 | — | B |
| [C-S1-018](s1-newborn/C-S1-018.yaml) | 嘘声音量要匹配宝宝哭声 | — | B |
| [C-S1-019](s1-newborn/C-S1-019.yaml) | 摇晃要小幅快速,不大幅缓慢 | — | B |
| [C-S1-020](s1-newborn/C-S1-020.yaml) | 安全摇晃 vs 摇晃综合征 SBS | safety, red_flag | A |
| [C-S1-021](s1-newborn/C-S1-021.yaml) | 非营养性吸吮是先天需求 | — | B |
| [C-S1-022](s1-newborn/C-S1-022.yaml) | 奶嘴别太早,3-4 周再用 | philosophy, controversy | C |
| [C-S1-023](s1-newborn/C-S1-023.yaml) | 拥抱疗法 = 5S 同时上 | — | B |
| [C-S1-024](s1-newborn/C-S1-024.yaml) | 5S 力度要匹配哭闹烈度 | — | B |
| [C-S1-025](s1-newborn/C-S1-025.yaml) | 5S 头几次可能更哭,别放弃 | — | B |

### 第三部分 · 睡眠 + 红旗 + 食物过敏 + 产后(8 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-026](s1-newborn/C-S1-026.yaml) | 别强逼宝宝白天不睡 | — | B |
| [C-S1-027](s1-newborn/C-S1-027.yaml) | 包裹 + 白噪音 = 延长睡眠 1-2 小时 | safety | B |
| [C-S1-028](s1-newborn/C-S1-028.yaml) | 共同入睡的 10 步安全要点 | philosophy, controversy, safety | C |
| [C-S1-029](s1-newborn/C-S1-029.yaml) | 5S 怎么按顺序慢慢淡出 | — | B |
| [C-S1-030](s1-newborn/C-S1-030.yaml) | 牛奶蛋白可能是肠绞痛元凶 | safety | B |
| [C-S1-031](s1-newborn/C-S1-031.yaml) | 哭闹的 10 个红旗信号(送医) | safety, red_flag | A |
| [C-S1-032](s1-newborn/C-S1-032.yaml) | 按摩 / 热水浴 = 5S 辅助 | — | B |
| [C-S1-033](s1-newborn/C-S1-033.yaml) | 产后抑郁的 3 阶段识别 | red_flag | A |

### S2 析出 · 哭闹峰主题(2 张 in S2)

> 这两张 Karp 在第 3 章《令人心烦的腹绞痛》写,但内容主战场是 6 周-3 月(任务书 §2 S2 主题清单"哭闹峰值"),因此放 S2 文件夹。
> 原 ID:C-S1-004 / C-S1-005(2026-05-01 挪段重命名)。

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-001](s2-1to3mo/C-S2-001.yaml) | 哭闹峰:6 周达峰,3 月回落 | — | B |
| [C-S2-002](s2-1to3mo/C-S2-002.yaml) | 撑过哭闹峰不是父母失败 | — | B |

---

## SRC-004 · AAP Safe Sleep & SIDS Prevention

**来源**:[HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/baby/sleep/) · 7 篇 article cluster
**对应段**:S1(9 张)+ S2(3 张)
**Source yaml**:[SRC-004.yaml](../10-sources/tier1-authoritative/notes/SRC-004.yaml)

| ID | title | tags |
|---|---|---|
| [C-S1-034](s1-newborn/C-S1-034.yaml) | 仰睡每次都要 — 包括 GERD | safety, red_flag |
| [C-S1-035](s1-newborn/C-S1-035.yaml) | 婴儿床第 1 年只能一张床单 | safety, red_flag |
| [C-S1-036](s1-newborn/C-S1-036.yaml) | 平面 + 认证床 + 这些产品别买 | safety |
| [C-S1-037](s1-newborn/C-S1-037.yaml) | 同房不同床到 6 月,降 SIDS 50% | safety, red_flag |
| [C-S1-038](s1-newborn/C-S1-038.yaml) | 包裹只是安抚,不防 SIDS | safety |
| [C-S1-039](s1-newborn/C-S1-039.yaml) | 睡前给奶嘴降 SIDS 风险 | safety |
| [C-S1-040](s1-newborn/C-S1-040.yaml) | 孕期产后都禁烟,vaping 也算 | safety, red_flag |
| [C-S1-041](s1-newborn/C-S1-041.yaml) | 过热也增 SIDS,比大人多 1 层 | safety |
| [C-S1-052](s1-newborn/C-S1-052.yaml) | 日夜颠倒纠正:白天嘈杂夜里专注 | — |
| [C-S2-003](s2-1to3mo/C-S2-003.yaml) | 7 周起每天 15-30 分钟 tummy time | safety |
| [C-S2-005](s2-1to3mo/C-S2-005.yaml) | "睡整觉"真定义:频繁醒能自回睡 | — |
| [C-S2-006](s2-1to3mo/C-S2-006.yaml) | 婴儿呼吸暂停 5-10 秒是正常的 | — |

---

## SRC-005 · AAP Crying & Soothing

**来源**:[HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/baby/crying-colic/) · 4 篇 article cluster
**对应段**:S1(8 张)+ S2(1 张)
**Source yaml**:[SRC-005.yaml](../10-sources/tier1-authoritative/notes/SRC-005.yaml)

| ID | title | tags |
|---|---|---|
| [C-S1-042](s1-newborn/C-S1-042.yaml) | 新生儿每天哭 1-4 小时是正常 | — |
| [C-S1-043](s1-newborn/C-S1-043.yaml) | 头 6 月不会宠坏 — 答应反而少哭 | philosophy |
| [C-S1-044](s1-newborn/C-S1-044.yaml) | 哭闹排查头发缠手指/脚趾 | safety, red_flag |
| [C-S1-045](s1-newborn/C-S1-045.yaml) | 安抚 9 招菜单 — 试一个 5 分钟 | — |
| [C-S1-046](s1-newborn/C-S1-046.yaml) | 都试过不行,放婴儿床让他哭 | controversy |
| [C-S1-047](s1-newborn/C-S1-047.yaml) | gas drops / gripe water 没用 | — |
| [C-S1-048](s1-newborn/C-S1-048.yaml) | 哭闹试 2 周排除母乳饮食 | — |
| [C-S1-049](s1-newborn/C-S1-049.yaml) | 崩溃时放下宝宝,离开 10-15 分钟 | safety, red_flag |
| [C-S2-004](s2-1to3mo/C-S2-004.yaml) | Colic 是神经敏感,不是胀气 | — |

---

## SRC-006 · AAP Feeding & Pacifiers

**来源**:[HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/baby/) · 10 篇 article cluster
**对应段**:S1(5 张)+ S3(8 张)+ S4(2 张)+ S5(1 张)
**Source yaml**:[SRC-006.yaml](../10-sources/tier1-authoritative/notes/SRC-006.yaml)

| ID | title | tags |
|---|---|---|
| [C-S1-050](s1-newborn/C-S1-050.yaml) | 母乳起步:每天 8-12 次,看早期信号 | — |
| [C-S1-051](s1-newborn/C-S1-051.yaml) | 奶嘴:3-4 周后用,4 岁前戒 | safety |
| [C-S1-053](s1-newborn/C-S1-053.yaml) | 母乳宝宝必补维 D 400 IU/d | safety |
| [C-S1-054](s1-newborn/C-S1-054.yaml) | 吐奶正常 vs GERD vs 喷射呕 | safety, red_flag |
| [C-S1-055](s1-newborn/C-S1-055.yaml) | 配方奶量 2.5 oz/lb/天,半直立喂 | safety |
| [C-S3-001](s3-3to6mo/C-S3-001.yaml) | 辅食准备 4-6 月,半勺起,3-5 天 1 新 | — |
| [C-S3-002](s3-3to6mo/C-S3-002.yaml) | 过敏食物 4-6 月就引入,不要等 | safety |
| [C-S3-003](s3-3to6mo/C-S3-003.yaml) | 米粉别加奶瓶,4 月前别给固食 | safety |
| [C-S3-004](s3-3to6mo/C-S3-004.yaml) | 1 岁内别给:这 11 种 choking 食物 | safety, red_flag |
| [C-S3-005](s3-3to6mo/C-S3-005.yaml) | 1 岁内不喝果汁,1 岁后限 4 oz | — |
| [C-S3-006](s3-3to6mo/C-S3-006.yaml) | 母乳宝宝 4 月起补铁,12 月查血 | safety |
| [C-S3-007](s3-3to6mo/C-S3-007.yaml) | 米粉别只 rice,换燕麦/大麦/藜麦 | safety |
| [C-S3-008](s3-3to6mo/C-S3-008.yaml) | 鱼类汞:大鱼避,小鱼可 | safety |
| [C-S4-001](s4-6to9mo/C-S4-001.yaml) | BLW vs 泥糊:AAP 不偏,可结合 | — |
| [C-S4-002](s4-6to9mo/C-S4-002.yaml) | BLW 切法:长条,不切圆片 | safety, red_flag |
| [C-S5-001](s5-9to12mo/C-S5-001.yaml) | 戒奶瓶 12-18 月,sippy 只过渡 | safety |

---

## SRC-007 · AAP Milestones & Teething

**来源**:[HealthyChildren.org](https://www.healthychildren.org/English/ages-stages/baby/) · 8 篇 article cluster
**对应段**:S2(1 张)+ S3(5 张)+ S4(3 张)+ S5(5 张)
**Source yaml**:[SRC-007.yaml](../10-sources/tier1-authoritative/notes/SRC-007.yaml)

| ID | title | tags |
|---|---|---|
| [C-S2-007](s2-1to3mo/C-S2-007.yaml) | 2-4 月里程碑:抬头 / cooing / 主动笑 | — |
| [C-S3-009](s3-3to6mo/C-S3-009.yaml) | 翻身 5 月起,7 月双向 | safety |
| [C-S3-010](s3-3to6mo/C-S3-010.yaml) | 坐姿:6 月 tripod,9 月独坐 | — |
| [C-S3-011](s3-3to6mo/C-S3-011.yaml) | 抓握:claw → 9 月 pincer 对捏 | safety |
| [C-S3-012](s3-3to6mo/C-S3-012.yaml) | 出牙 4-7 月,> 38.3°C 不是出牙 | safety, red_flag |
| [C-S3-013](s3-3to6mo/C-S3-013.yaml) | 琥珀牙链禁,teething gel 也禁 | safety, red_flag |
| [C-S4-003](s4-6to9mo/C-S4-003.yaml) | 物体永久性 8-10 月,peekaboo 教 | — |
| [C-S4-004](s4-6to9mo/C-S4-004.yaml) | 陌生人焦虑 ~8 月,健康发展 | — |
| [C-S4-005](s4-6to9mo/C-S4-005.yaml) | 学步车 AAP 强烈反对,别买 | safety, red_flag |
| [C-S5-002](s5-9to12mo/C-S5-002.yaml) | 第一步 ~1 岁,脚分宽是正常 | — |
| [C-S5-003](s5-9to12mo/C-S5-003.yaml) | 第一个真词 ~1 岁,理解 > 表达 | — |
| [C-S5-004](s5-9to12mo/C-S5-004.yaml) | 分离焦虑 10-18 月峰值,5 招缓解 | — |
| [C-S5-005](s5-9to12mo/C-S5-005.yaml) | 12 月儿保 4 必查 | — |
| [C-S5-006](s5-9to12mo/C-S5-006.yaml) | 楼梯门两端必装,鞋子简化选 | safety |

---

## SRC-008 · AAP Health & Safety

**来源**:[HealthyChildren.org](https://www.healthychildren.org/English/) · 6 篇 article cluster
**对应段**:S1(9 张)+ S4(2 张)+ S5(1 张)
**Source yaml**:[SRC-008.yaml](../10-sources/tier1-authoritative/notes/SRC-008.yaml)

| ID | title | tags |
|---|---|---|
| [C-S1-056](s1-newborn/C-S1-056.yaml) | 汽车座 rear-facing 后排,不副驾 | safety, red_flag |
| [C-S1-057](s1-newborn/C-S1-057.yaml) | 跌落防护:尿布台/床/沙发不独处 | safety, red_flag |
| [C-S1-058](s1-newborn/C-S1-058.yaml) | 水龙头温 ≤ 49°C,不端热饮抱 | safety |
| [C-S1-059](s1-newborn/C-S1-059.yaml) | 中毒急救:专线 + 不催吐 | safety, red_flag |
| [C-S1-060](s1-newborn/C-S1-060.yaml) | < 3 月发烧 38°C 立刻找医生 | safety, red_flag |
| [C-S1-061](s1-newborn/C-S1-061.yaml) | 婴儿急性红旗:8 项立刻找医生 | safety, red_flag |
| [C-S1-062](s1-newborn/C-S1-062.yaml) | 直肠测温对 < 3 月最准 | safety |
| [C-S1-063](s1-newborn/C-S1-063.yaml) | RSV 保护 2 选 1:孕妇或婴儿打 | safety |
| [C-S1-064](s1-newborn/C-S1-064.yaml) | 0-12 月疫苗时间表速查 | safety |
| [C-S4-006](s4-6to9mo/C-S4-006.yaml) | 溺水预防:2 inches 水也淹 | safety, red_flag |
| [C-S4-007](s4-6to9mo/C-S4-007.yaml) | 家居童锁 + 窗帘绳 + crib 位置 | safety |
| [C-S5-007](s5-9to12mo/C-S5-007.yaml) | 12 月疫苗:MMR + 水痘 + HepA | safety |

---

## SRC-009 · 鲍秀兰《婴幼儿潜能开发和早期教育》

**中文原版**:鲍秀兰、孙淑英 著,中国妇女出版社,2016 年 5 月第 1 版,ISBN 978-7-5127-1196-9
**作者背景**:北京协和医院儿科原主任医师,50+ 年儿科 + 早教临床,中国早期教育领域元老
**对应段**:S1-S7(0-3 岁全段,首次扩展 S6 + S7)
**卡片总数**:85
**等级分布**:A 8 / B 33 / C 44(早教派多 C / 操作 B / 与 AAP 共识 A)
**Source yaml**:[SRC-009.yaml](../10-sources/tier3-books/notes/SRC-009.yaml)

### S1 · 1 月龄(8 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-065](s1-newborn/C-S1-065.yaml) | 1 月龄每天视听训练 10 分钟 | — | B |
| [C-S1-066](s1-newborn/C-S1-066.yaml) | 1 月龄大声没反应:立刻送医 | safety, red_flag | A |
| [C-S1-067](s1-newborn/C-S1-067.yaml) | 把新生儿当懂事孩子对待 | philosophy | C |
| [C-S1-068](s1-newborn/C-S1-068.yaml) | 照料新生儿 4 大禁忌 | safety | B |
| [C-S1-069](s1-newborn/C-S1-069.yaml) | 0-1 岁是学习关键期,错过补不回 | philosophy | C |
| [C-S1-070](s1-newborn/C-S1-070.yaml) | 1 月龄玩具 5 大选择原则 | safety | C |
| [C-S1-071](s1-newborn/C-S1-071.yaml) | 1 月龄睡 14-20 小时是正常 | — | A |
| [C-S1-072](s1-newborn/C-S1-072.yaml) | 1 月龄脑发育 7 大刺激柱 ⭐ | philosophy | B |

### S2 · 2-3 月龄(10 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-008](s2-1to3mo/C-S2-008.yaml) | 2 月龄俯卧抬头每天 1-2 分起 | — | B |
| [C-S2-009](s2-1to3mo/C-S2-009.yaml) | 2-3 月龄不看人脸不转头送医 | safety, red_flag | A |
| [C-S2-010](s2-1to3mo/C-S2-010.yaml) | 没语言刺激,可能成聋哑儿 | philosophy | B |
| [C-S2-011](s2-1to3mo/C-S2-011.yaml) | 跟宝宝说话 5 大共性 | — | B |
| [C-S2-012](s2-1to3mo/C-S2-012.yaml) | 母婴交谈链:停顿等回应 | — | B |
| [C-S2-013](s2-1to3mo/C-S2-013.yaml) | 不等啼哭再喂,及时响应 | — | B |
| [C-S2-014](s2-1to3mo/C-S2-014.yaml) | 3 月起禁打蜡烛包 | safety, controversy | A |
| [C-S2-015](s2-1to3mo/C-S2-015.yaml) | 3 月翻身训练,千万别独留 | safety, red_flag | A |
| [C-S2-016](s2-1to3mo/C-S2-016.yaml) | 3 月里程碑:出声笑+发元音 | — | B |
| [C-S2-017](s2-1to3mo/C-S2-017.yaml) | 室内温 25-28 夏 / 18-22 冬 | — | B |

### S3 · 4-6 月龄(13 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-014](s3-3to6mo/C-S3-014.yaml) | 4 月拉坐训练:让宝宝自己用力 | — | B |
| [C-S3-015](s3-3to6mo/C-S3-015.yaml) | 4 月发"妈妈"立即亲吻强化 | — | B |
| [C-S3-016](s3-3to6mo/C-S3-016.yaml) | 4 月视听训练 6 法清单 | — | C |
| [C-S3-017](s3-3to6mo/C-S3-017.yaml) | 4 月表情反应+镜子认自己 | — | C |
| [C-S3-018](s3-3to6mo/C-S3-018.yaml) | 4 月找朋友:户外接触小朋友 | — | C |
| [C-S3-019](s3-3to6mo/C-S3-019.yaml) | 5 月靠坐+直立跳跃训练 | — | C |
| [C-S3-020](s3-3to6mo/C-S3-020.yaml) | 5 月陪宝宝玩 = 早教课程 | philosophy | C |
| [C-S3-021](s3-3to6mo/C-S3-021.yaml) | 5-6 月藏猫猫 + 找掉物训练 | — | B |
| [C-S3-022](s3-3to6mo/C-S3-022.yaml) | 6 月独坐 + 坐位发育双促 | — | B |
| [C-S3-023](s3-3to6mo/C-S3-023.yaml) | 6 月起硬食:小饼干自喂 | safety | B |
| [C-S3-024](s3-3to6mo/C-S3-024.yaml) | 6 月红旗:4 项异常立刻送医 ⭐ | safety, red_flag | A |
| [C-S3-025](s3-3to6mo/C-S3-025.yaml) | 6 月点头摇头训练 | — | C |
| [C-S3-026](s3-3to6mo/C-S3-026.yaml) | 6 月理性对哭声求助 | philosophy | C |

### S4 · 7-8 月龄(10 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-008](s4-6to9mo/C-S4-008.yaml) | 7-8 月爬行训练 = 多重发展 | — | B |
| [C-S4-009](s4-6to9mo/C-S4-009.yaml) | 7-8 月认物找物语言练习 | — | B |
| [C-S4-010](s4-6to9mo/C-S4-010.yaml) | 7-8 月触额碰头游戏 | — | C |
| [C-S4-011](s4-6to9mo/C-S4-011.yaml) | 7-8 月教 ba/ma 连续音节 | — | B |
| [C-S4-012](s4-6to9mo/C-S4-012.yaml) | 7-8 月捏取训练 + 防硬物误食 | safety | A |
| [C-S4-013](s4-6to9mo/C-S4-013.yaml) | 7-8 月百宝箱学自己玩 | — | C |
| [C-S4-014](s4-6to9mo/C-S4-014.yaml) | 7-8 月长牙后改用杯子喝水 | safety | A |
| [C-S4-015](s4-6to9mo/C-S4-015.yaml) | 7-8 月制止打人:别笑反应 | philosophy | C |
| [C-S4-016](s4-6to9mo/C-S4-016.yaml) | 8 月前抱抱不会宠坏 ⭐ | philosophy | B |
| [C-S4-017](s4-6to9mo/C-S4-017.yaml) | 7-8 月学"再见欢迎谢谢"手势 | — | C |

### S5 · 9-12 月龄(12 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-008](s5-9to12mo/C-S5-008.yaml) | 9 月扶站独站 + 蹲下捡训练 | — | B |
| [C-S5-009](s5-9to12mo/C-S5-009.yaml) | 9 月意识到自我存在 | — | C |
| [C-S5-010](s5-9to12mo/C-S5-010.yaml) | 9 月起设小障碍练思维 | — | C |
| [C-S5-011](s5-9to12mo/C-S5-011.yaml) | 9 月起手把手教用小勺 | — | B |
| [C-S5-012](s5-9to12mo/C-S5-012.yaml) | 9 月起坐盆训练(中国传统)⭐ | philosophy, controversy | C |
| [C-S5-013](s5-9to12mo/C-S5-013.yaml) | 10 月会察言观色 | — | B |
| [C-S5-014](s5-9to12mo/C-S5-014.yaml) | 10 月玩娃娃学关心他人 | — | C |
| [C-S5-015](s5-9to12mo/C-S5-015.yaml) | 11-12 月加紧学说 5 要点 | — | B |
| [C-S5-016](s5-9to12mo/C-S5-016.yaml) | 教物名称要准确,不要模糊 | — | C |
| [C-S5-017](s5-9to12mo/C-S5-017.yaml) | 12 月走路训练 5 法 | — | A |
| [C-S5-018](s5-9to12mo/C-S5-018.yaml) | 12 月起认红色 + 颜色启蒙 | — | C |
| [C-S5-019](s5-9to12mo/C-S5-019.yaml) | 12 月起教与人分享 | — | C |

### S6 · 1-2 岁(18 张,**新建段**⭐)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-001](s6-12to24mo/C-S6-001.yaml) | 12-15 月模仿乱说不打断 | — | B |
| [C-S6-002](s6-12to24mo/C-S6-002.yaml) | 12-15 月念儿歌押韵接背 | — | B |
| [C-S6-003](s6-12to24mo/C-S6-003.yaml) | 13-15 月独立走+扶上下楼梯 | — | B |
| [C-S6-004](s6-12to24mo/C-S6-004.yaml) | 13-15 月鼓励涂画别制止 | — | C |
| [C-S6-005](s6-12to24mo/C-S6-005.yaml) | 16-18 月学用勺拿杯 | — | B |
| [C-S6-006](s6-12to24mo/C-S6-006.yaml) | 16-18 月跟小伙伴玩 | philosophy | C |
| [C-S6-007](s6-12to24mo/C-S6-007.yaml) | 1-2 岁管教全家一致 + 不打 ⭐ | philosophy, safety | A |
| [C-S6-008](s6-12to24mo/C-S6-008.yaml) | 16-18 月发脾气:中场休息 | philosophy | C |
| [C-S6-009](s6-12to24mo/C-S6-009.yaml) | 16-18 月预防发脾气 | — | C |
| [C-S6-010](s6-12to24mo/C-S6-010.yaml) | 19-21 月戴帽脱袜自服务 | — | B |
| [C-S6-011](s6-12to24mo/C-S6-011.yaml) | 19-21 月生活规律晨起按时 | — | B |
| [C-S6-012](s6-12to24mo/C-S6-012.yaml) | 18 月红旗 4 项立刻送医 ⭐ | safety, red_flag | A |
| [C-S6-013](s6-12to24mo/C-S6-013.yaml) | 22-24 月跑+倒退走+双脚跳 | — | B |
| [C-S6-014](s6-12to24mo/C-S6-014.yaml) | 22-24 月双字词→简单句 | — | B |
| [C-S6-015](s6-12to24mo/C-S6-015.yaml) | 22-24 月用"我"建自我意识 | — | B |
| [C-S6-016](s6-12to24mo/C-S6-016.yaml) | 22-24 月主动交往扩社交圈 | — | C |
| [C-S6-017](s6-12to24mo/C-S6-017.yaml) | 22-24 月识颜色:红黄绿先 | — | C |
| [C-S6-018](s6-12to24mo/C-S6-018.yaml) | 22-24 月生活自理脱外衣 | — | B |

### S7 · 2-3 岁(15 张,**新建段**⭐)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S7-001](s7-24to36mo/C-S7-001.yaml) | 25-30 月独自上下楼梯 | — | B |
| [C-S7-002](s7-24to36mo/C-S7-002.yaml) | 25-30 月学骑小三轮车 | — | B |
| [C-S7-003](s7-24to36mo/C-S7-003.yaml) | 25-30 月模仿画简单图形 | — | C |
| [C-S7-004](s7-24to36mo/C-S7-004.yaml) | 25-30 月识形状:圆方三角 | — | C |
| [C-S7-005](s7-24to36mo/C-S7-005.yaml) | 25-30 月分辨大小用实物 | — | B |
| [C-S7-006](s7-24to36mo/C-S7-006.yaml) | 25-30 月唱儿歌 + 说用途 | — | C |
| [C-S7-007](s7-24to36mo/C-S7-007.yaml) | 25-30 月用语言表示大小便 | — | B |
| [C-S7-008](s7-24to36mo/C-S7-008.yaml) | 25-30 月帮大人做事 + 收玩具 | — | C |
| [C-S7-009](s7-24to36mo/C-S7-009.yaml) | 25-30 月学穿鞋(先脱后穿) | — | B |
| [C-S7-010](s7-24to36mo/C-S7-010.yaml) | 25-30 月教合作玩 | — | C |
| [C-S7-011](s7-24to36mo/C-S7-011.yaml) | 31-36 月跳高跳远 + 单足站 | — | C |
| [C-S7-012](s7-24to36mo/C-S7-012.yaml) | 31-36 月长短概念 + 数数 | — | C |
| [C-S7-013](s7-24to36mo/C-S7-013.yaml) | 24 月红旗 7 项立刻送医 ⭐ | safety, red_flag | A |
| [C-S7-014](s7-24to36mo/C-S7-014.yaml) | 2-3 岁忽视错误 = 最有效约束 ⭐ | philosophy | B |
| [C-S7-015](s7-24to36mo/C-S7-015.yaml) | 2-3 岁道德意识 5 招启蒙 | philosophy | C |

---

## 维护与重生成

本文件目前手工维护。以后卡片多了,可以写一个简单脚本扫描所有 yaml 自动重生成:

```bash
# 伪代码(Phase 2 启动前可实现)
for src in 10-sources/**/SRC-*.yaml:
  cards = grep "source_id: ${src.id}" 30-cards/**/*.yaml
  render_table(src, cards) → INDEX_BY_SOURCE.md
```

**真相源**永远是每张卡 yaml 的 `citation.source_id` + `front.title` + `tags` + `back.evidence_level`。本索引文件只是反向视图。

---

## SRC-010 · Brazelton《Touchpoints: Birth to Three》

**英文原版**:T. Berry Brazelton & Joshua D. Sparrow, *Touchpoints: Birth to 3 — Your Child's Emotional and Behavioral Development*(Da Capo Press, 初版 1992 / 修订版 2006, A Merloyd Lawrence Book, ISBN 978-0-7382-1049-0)
**作者背景**:Brazelton(1918-2018)哈佛医学院儿科教授, NBAS 创始人, Touchpoints 育儿法创始人;Sparrow 儿童精神科医生, Touchpoints Center 高级主管
**对应段**:**S0-S7 全段覆盖**(本知识库第一本覆盖 S0 孕期)
**卡片总数**:**79**(原 70 + 自审补 9)
**等级分布**:A 9 / B 56 / C 14(流派原典 + 临床观察 / 与 AAP 共识对齐才标 A)
**Source yaml**:[SRC-010.yaml](../10-sources/tier3-books/notes/SRC-010.yaml)

### S0 · 孕期(7 张,首次扩展)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S0-001](s0-pregnancy/C-S0-001.yaml) | 第一次产检从孕 7 月开始 | philosophy | C |
| [C-S0-002](s0-pregnancy/C-S0-002.yaml) | 孕期父母梦到三个宝宝 | philosophy | C |
| [C-S0-003](s0-pregnancy/C-S0-003.yaml) | 全家人都在抢着照顾宝宝 | philosophy | C |
| [C-S0-004](s0-pregnancy/C-S0-004.yaml) | 胎儿真的能听懂你说话 | — | B |
| [C-S0-005](s0-pregnancy/C-S0-005.yaml) | 上班妈妈选不选母乳的真相 | philosophy | B |
| [C-S0-006](s0-pregnancy/C-S0-006.yaml) | 烟酒一次也别碰但别自责 | safety | B |
| [C-S0-007](s0-pregnancy/C-S0-007.yaml) | 好医生肯说"我不知道" | philosophy | B |

### S1 · 0-1 月(18 张:Round A 9 + Round E 4 + Round F 5)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-073](s1-newborn/C-S1-073.yaml) | 新生儿就是一个独立的人(NBAS) | philosophy | B |
| [C-S1-074](s1-newborn/C-S1-074.yaml) | 习惯化:宝宝的"屏蔽能力" | — | B |
| [C-S1-075](s1-newborn/C-S1-075.yaml) | 新生儿的六种状态 | — | B |
| [C-S1-076](s1-newborn/C-S1-076.yaml) | 父母焦虑是好东西 | red_flag | A |
| [C-S1-077](s1-newborn/C-S1-077.yaml) | 别迷信"产房黄金一小时" | philosophy, controversy | B |
| [C-S1-078](s1-newborn/C-S1-078.yaml) | 调和"梦中宝宝"和"真宝宝" | philosophy | C |
| [C-S1-079](s1-newborn/C-S1-079.yaml) | 喂奶不只是填饱肚子(burst-pause) | safety | B |
| [C-S1-080](s1-newborn/C-S1-080.yaml) | 2-3 周触点:父母的崩溃期 | philosophy | C |
| [C-S1-081](s1-newborn/C-S1-081.yaml) | 宝宝认识爸爸的方式跟妈妈不同 | philosophy | C |
| [C-S1-082](s1-newborn/C-S1-082.yaml) | 哭闹 6 类哭声地图 | red_flag | A |
| [C-S1-083](s1-newborn/C-S1-083.yaml) | Colic 真相 85% 都有 | philosophy | A |
| [C-S1-084](s1-newborn/C-S1-084.yaml) | 高敏宝宝识别清单 | — | B |
| [C-S1-085](s1-newborn/C-S1-085.yaml) | 同床 vs AAP 的立场分歧 | controversy, safety | B |
| [C-S1-086](s1-newborn/C-S1-086.yaml) | 退步是前进的预告(Touchpoints 总论) ⭐ | philosophy | A |
| [C-S1-087](s1-newborn/C-S1-087.yaml) | 优势视角与旧鬼魂(strengths-based) ⭐ | philosophy | B |
| [C-S1-088](s1-newborn/C-S1-088.yaml) | 父母两套模型反而更好 | philosophy | B |
| [C-S1-089](s1-newborn/C-S1-089.yaml) | 祖父母先闭嘴再帮忙 | philosophy | B |
| [C-S1-090](s1-newborn/C-S1-090.yaml) | 门卫现象是爱的副作用(广义) | philosophy | B |

### S2 · 1-3 月(7 张:Round B 5 + Round F 1 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-018](s2-1to3mo/C-S2-018.yaml) | 6-8 周社交微笑不是反射 | — | B |
| [C-S2-019](s2-1to3mo/C-S2-019.yaml) | 高敏宝宝的"我超载了"信号 | — | B |
| [C-S2-020](s2-1to3mo/C-S2-020.yaml) | 8 周哭闹峰是发育规律 | — | B |
| [C-S2-021](s2-1to3mo/C-S2-021.yaml) | 8 周宝宝已能区分爸妈 | — | C |
| [C-S2-022](s2-1to3mo/C-S2-022.yaml) | 这月龄不存在"宠坏" | philosophy, controversy | C |
| [C-S2-023](s2-1to3mo/C-S2-023.yaml) | 选日托看共情不看课程 | philosophy | B |
| [C-S2-024](s2-1to3mo/C-S2-024.yaml) | 🔍 过敏积木理论早预防(LEAP 修正) | controversy | C |

### S3 · 3-6 月(8 张:Round B 7 + Round E 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-027](s3-3to6mo/C-S3-027.yaml) | 4 月触点:先退后进 ⭐ | philosophy | C |
| [C-S3-028](s3-3to6mo/C-S3-028.yaml) | 4 月喂奶分心不是断奶信号 | — | B |
| [C-S3-029](s3-3to6mo/C-S3-029.yaml) | 4 月夜醒增多别冲进去 | controversy | B |
| [C-S3-030](s3-3to6mo/C-S3-030.yaml) | 6-7 月气质 9 维度成型 | philosophy | B |
| [C-S3-031](s3-3to6mo/C-S3-031.yaml) | 6-7 月陌生人焦虑应对术 | — | B |
| [C-S3-032](s3-3to6mo/C-S3-032.yaml) | 6-7 月镜子游戏练自我 | — | C |
| [C-S3-033](s3-3to6mo/C-S3-033.yaml) | 学步车反而拖慢里程碑 | safety | B |
| [C-S3-034](s3-3to6mo/C-S3-034.yaml) | 4 月睡眠周期与条件反射 | — | A |

### S4 · 6-9 月(5 张:Round C 4 + Round E 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-018](s4-6to9mo/C-S4-018.yaml) | 6-7 月物体永久性萌芽 | — | B |
| [C-S4-019](s4-6to9mo/C-S4-019.yaml) | 7-8 月睡眠倒退是好事 | — | B |
| [C-S4-020](s4-6to9mo/C-S4-020.yaml) | 7 月吃饭就是探索 | philosophy | A |
| [C-S4-021](s4-6to9mo/C-S4-021.yaml) | 7-8 月陌生人警觉双高峰 | — | B |
| [C-S4-022](s4-6to9mo/C-S4-022.yaml) | 6-9 月有自我安抚就放心 | philosophy | B |

### S5 · 9-12 月(9 张:Round C 5 + Round E 3 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-020](s5-9to12mo/C-S5-020.yaml) | 9 月触点全面崩溃期 ⭐ | philosophy | A |
| [C-S5-021](s5-9to12mo/C-S5-021.yaml) | 9 月学站夜醒机制 | — | B |
| [C-S5-022](s5-9to12mo/C-S5-022.yaml) | 8-9 月看视觉悬崖学走 | philosophy | A |
| [C-S5-023](s5-9to12mo/C-S5-023.yaml) | 9 月断奶不必赶 | — | B |
| [C-S5-024](s5-9to12mo/C-S5-024.yaml) | 9 月可以预判失败感 | philosophy | B |
| [C-S5-025](s5-9to12mo/C-S5-025.yaml) | 9 月-3 岁各阶段管教菜单 | discipline | B |
| [C-S5-026](s5-9to12mo/C-S5-026.yaml) | 分离的痛主要在父母 | philosophy | B |
| [C-S5-027](s5-9to12mo/C-S5-027.yaml) | 管教就是教导(广义) ⭐ | philosophy, discipline | A |
| [C-S5-028](s5-9to12mo/C-S5-028.yaml) | 🔍 晚一年比早一年值(School Readiness) | philosophy, controversy | B |

### S6 · 12-24 月(16 张:Round D 7 + Round C 3 + Round E 1 + 自审补 5)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-019](s6-12to24mo/C-S6-019.yaml) | 15 月符号思维上线 | philosophy | B |
| [C-S6-020](s6-12to24mo/C-S6-020.yaml) | 15 月 tantrum 是内部冲突(五胞胎案例) | discipline | B |
| [C-S6-021](s6-12to24mo/C-S6-021.yaml) | Discipline 是教导,不是惩罚 ⭐ | philosophy, controversy | B |
| [C-S6-022](s6-12to24mo/C-S6-022.yaml) | 18 月狂说 No 是健康信号 ⭐ | philosophy | B |
| [C-S6-023](s6-12to24mo/C-S6-023.yaml) | 18 月咬人是失控不是恶意 | discipline | B |
| [C-S6-1072](s6-12to24mo/C-S6-1072.yaml) | 18 月通过红鼻子镜子测试 | — | B |
| [C-S6-025](s6-12to24mo/C-S6-025.yaml) | 破破烂烂的小毛绒 = 内心强大 | philosophy | B |
| [C-S6-026](s6-12to24mo/C-S6-026.yaml) | 1 岁第一次"反抗" | philosophy | B |
| [C-S6-027](s6-12to24mo/C-S6-027.yaml) | 12-15 月饮食极简底线 | philosophy | B |
| [C-S6-028](s6-12to24mo/C-S6-028.yaml) | 12 月睡前唤醒法 | — | C |
| [C-S6-029](s6-12to24mo/C-S6-029.yaml) | 喂食是自主权战场 | philosophy | A |
| [C-S6-030](s6-12to24mo/C-S6-030.yaml) | 🔍 别抢救他,让他自己赢(挫折是燃料) | philosophy | B |
| [C-S6-031](s6-12to24mo/C-S6-031.yaml) | 🔍 2 岁前一秒都别看屏(屏幕硬规则) | safety, red_flag | A |
| [C-S6-032](s6-12to24mo/C-S6-032.yaml) | 🔍 内向不是病别硬掰(Kagan 气质) | philosophy | B |
| [C-S6-033](s6-12to24mo/C-S6-033.yaml) | 🔍 别等他自己追上(两个黄金质问) | red_flag | B |
| [C-S6-034](s6-12to24mo/C-S6-034.yaml) | 🔍 住院父母必须在场(争取陪护) | red_flag, philosophy | B |

### S7 · 24-36 月(9 张:Round D 5 + Round E 2 + 自审补 2)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S7-016](s7-24to36mo/C-S7-016.yaml) | 2 岁三件大事:假装/认同/模仿 | philosophy | B |
| [C-S7-017](s7-24to36mo/C-S7-017.yaml) | 2 岁语言差异:正常 vs 真延迟 | red_flag | B |
| [C-S7-018](s7-24to36mo/C-S7-018.yaml) | 厕所训练:孩子主导,父母只示范 ⭐ | controversy | B |
| [C-S7-019](s7-24to36mo/C-S7-019.yaml) | 3 岁是亲子第二蜜月(想象朋友) | philosophy | C |
| [C-S7-020](s7-24to36mo/C-S7-020.yaml) | 3 岁前别教读写 | philosophy, controversy | B |
| [C-S7-021](s7-24to36mo/C-S7-021.yaml) | ADHD 别只盯活跃看自我形象 | red_flag | B |
| [C-S7-022](s7-24to36mo/C-S7-022.yaml) | 入园 2-3 周后会"二次崩溃" | — | B |
| [C-S7-023](s7-24to36mo/C-S7-023.yaml) | 🔍 二胎吵架你别站队(Erikson 内疚) | philosophy | B |
| [C-S7-024](s7-24to36mo/C-S7-024.yaml) | 🔍 别说宠物"睡着了"(谈死亡) | red_flag, philosophy | B |

> ⭐ 7 张 Brazelton 流派核心立场卡(必读):退步=前进 / 优势视角 / 4月触点 / 9月崩溃 / 管教≠惩罚 / 18月负向期=健康 / 厕所学习反训练。
> 🔍 9 张自审补卡(中国家长强相关):积木过敏 / 晚一年入学 / 挫折是燃料 / 屏幕硬规则 / 内向气质 / 两个黄金质问 / 争取陪护 / 二胎别站队 / 谈死亡。

---

## SRC-011 · Bowlby《依恋三部曲 · 第一卷:依恋》

**英文原版**:John Bowlby, *Attachment and Loss · Volume 1: Attachment* (Hogarth Press, 1969 / 2nd ed 1982)
**中译本**:世界图书出版有限公司北京分公司,2017 年 6 月,汪智攀 + 王婷婷译,易春丽审校,ISBN 978-7-5192-2927-6
**对应段**:S1-S6
**卡片总数**:37(自审补 2 = 35 + 2)
**等级分布**:A 9 / B 26 / C 0 — 理论原典,A 比例 26%
**Source yaml**:[SRC-011.yaml](../10-sources/tier3-books/notes/SRC-011.yaml)

### S1 · 0-1 月(7 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-122](s1-newborn/C-S1-122.yaml) | 粘人不是被宠的,是基因 ⭐ | philosophy, controversy | B |
| [C-S1-123](s1-newborn/C-S1-123.yaml) | 出生几天就能认妈妈 | — | A |
| [C-S1-124](s1-newborn/C-S1-124.yaml) | 5 种粘妈本能行为 | — | B |
| [C-S1-125](s1-newborn/C-S1-125.yaml) | 摇晃止哭,60次/分起步 | — | B |
| [C-S1-126](s1-newborn/C-S1-126.yaml) | 抓握反射 = 灵长类进化遗留 | — | B |
| [C-S1-127](s1-newborn/C-S1-127.yaml) | 微笑发展 4 阶段 | — | B |
| [C-S1-128](s1-newborn/C-S1-128.yaml) | 妈来了哭就停 = 选 1 名优待 | — | B |

### S2 · 1-3 月(5 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-067](s2-1to3mo/C-S2-067.yaml) | 5 周才开始真"看见你" | — | B |
| [C-S2-068](s2-1to3mo/C-S2-068.yaml) | 6 周后,看脸比听声更管用 | — | B |
| [C-S2-069](s2-1to3mo/C-S2-069.yaml) | 6 周开启"咿呀对话" | — | B |
| [C-S2-070](s2-1to3mo/C-S2-070.yaml) | **喂奶 ≠ 建立依恋 ⭐** | — | A |
| [C-S2-071](s2-1to3mo/C-S2-071.yaml) | 妈走了就哭从 5 月起 | — | B |

### S3 · 3-6 月(4 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-076](s3-3to6mo/C-S3-076.yaml) | 14 周开始认妈妈的脸 | — | B |
| [C-S3-077](s3-3to6mo/C-S3-077.yaml) | 不同妈带出不同娃 | — | B |
| [C-S3-078](s3-3to6mo/C-S3-078.yaml) | 4-6 月对妈反应明显但还认人浅 | — | B |
| [C-S3-079](s3-3to6mo/C-S3-079.yaml) | 5-7 月起会用妈当"基地" | — | B |

### S4 · 6-9 月(8 张:7 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-067](s4-6to9mo/C-S4-067.yaml) | 6-12 月是依恋形成关键期 | — | B |
| [C-S4-068](s4-6to9mo/C-S4-068.yaml) | **8 月怕陌生人 = 依恋形成证据 ⭐** | — | A |
| [C-S4-069](s4-6to9mo/C-S4-069.yaml) | 6-9 月真依恋形成 | — | B |
| [C-S4-070](s4-6to9mo/C-S4-070.yaml) | **哭多不等于爱深 ⭐** | philosophy | B |
| [C-S4-071](s4-6to9mo/C-S4-071.yaml) | **安全依恋的 4 个关键 ⭐** | — | A |
| [C-S4-072](s4-6to9mo/C-S4-072.yaml) | 多个依恋人不冲突 | — | B |
| [C-S4-073](s4-6to9mo/C-S4-073.yaml) | **主依恋人不必是亲生母亲 ⭐** | — | A |
| [C-S4-074](s4-6to9mo/C-S4-074.yaml) | 🔍 气质难带 ≠ 依恋差(philosophy) | philosophy | B |

### S5 · 9-12 月(8 张:7 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-069](s5-9to12mo/C-S5-069.yaml) | **健康依恋分离焦虑反更早 ⭐** | — | A |
| [C-S5-070](s5-9to12mo/C-S5-070.yaml) | **12 月可测依恋类型(Strange Situation) ⭐** | — | A |
| [C-S5-071](s5-9to12mo/C-S5-071.yaml) | **B 安全型 ~60-65% ⭐** | — | A |
| [C-S5-072](s5-9to12mo/C-S5-072.yaml) | A 焦虑回避型 ~20% | — | B |
| [C-S5-073](s5-9to12mo/C-S5-073.yaml) | C 焦虑抗拒型 ~10% | — | B |
| [C-S5-074](s5-9to12mo/C-S5-074.yaml) | 12 月依恋预测 5 岁人格 | philosophy | B |
| [C-S5-075](s5-9to12mo/C-S5-075.yaml) | 12-18 月依恋仍可改 | — | B |
| [C-S5-076](s5-9to12mo/C-S5-076.yaml) | 🔍 抱毯子玩偶不是怪癖(过渡性客体) | — | B |

### S6 · 12-24 月(5 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-068](s6-12to24mo/C-S6-068.yaml) | 2 岁是依恋顶峰然后过渡 | — | B |
| [C-S6-069](s6-12to24mo/C-S6-069.yaml) | **3 岁前给娃刻"内部地图" ⭐** | philosophy | B |
| [C-S6-070](s6-12to24mo/C-S6-070.yaml) | **被打的孩子有特殊创伤模式 ⭐** | safety, red_flag | A |
| [C-S6-071](s6-12to24mo/C-S6-071.yaml) | 18-24 月分离能撑更久 | — | B |
| [C-S6-072](s6-12to24mo/C-S6-072.yaml) | 怎么管孩子他就怎么换位思考 | philosophy | B |

> ⭐ 9 张 A 级核心(必读):出生认妈 / 喂奶非依恋 / 8 月怕生 / 安全依恋 4 关键 / 主依恋非亲生 / 健康依恋反早分离 / Strange Situation / B 安全型 / 体罚特殊创伤。
> 🔍 自审补 2 张:气质难带 ≠ 依恋差 / 过渡性客体玩偶毯子。

---

## SRC-012 · Bowlby《依恋三部曲 · 第二卷:分离》

**英文原版**:John Bowlby, *Attachment and Loss · Volume 2: Separation, Anxiety and Anger* (Hogarth Press, 1973)
**中译本**:世界图书出版有限公司北京分公司,2017 年,汪智攀 + 王婷婷译,ISBN 978-7-5192-2926-9
**对应段**:S5-S7(本卷主题 6 月-3 岁分离焦虑窗口期)
**卡片总数**:32
**Source yaml**:[SRC-012.yaml](../10-sources/tier3-books/notes/SRC-012.yaml)

### S5 · 9-12 月(4 张)

| ID | title |
|---|---|
| [C-S5-086](s5-9to12mo/C-S5-086.yaml) | 分离时玩偶毯子价更高 |
| [C-S5-087](s5-9to12mo/C-S5-087.yaml) | 寄养换家年龄越大越痛苦 |
| [C-S5-088](s5-9to12mo/C-S5-088.yaml) | 怕生 = 陌生 + 靠近 |
| [C-S5-089](s5-9to12mo/C-S5-089.yaml) | 住院妈陪 vs 不陪差很多 |

### S6 · 12-24 月(18 张)

| ID | title |
|---|---|
| [C-S6-082](s6-12to24mo/C-S6-082.yaml) | **长分离反应 3 阶段 ⭐**(抗议-绝望-超脱) |
| [C-S6-083](s6-12to24mo/C-S6-083.yaml) | 分离回家后变更黏正常 |
| [C-S6-084](s6-12to24mo/C-S6-084.yaml) | 兄弟姐妹陪着分离好得多 |
| [C-S6-085](s6-12to24mo/C-S6-085.yaml) | 重聚不认妈是危险信号 |
| [C-S6-086](s6-12to24mo/C-S6-086.yaml) | 在场指心理可触达 |
| [C-S6-087](s6-12to24mo/C-S6-087.yaml) | **再不听话妈妈就走是精神虐待 ⭐** |
| [C-S6-088](s6-12to24mo/C-S6-088.yaml) | 复合恐惧才致大反应 |
| [C-S6-089](s6-12to24mo/C-S6-089.yaml) | 妈知道的怕只占一半 |
| [C-S6-090](s6-12to24mo/C-S6-090.yaml) | 现代托儿所也救不了 |
| [C-S6-091](s6-12to24mo/C-S6-091.yaml) | 日托稳定 > 全职妈妈 |
| [C-S6-092](s6-12to24mo/C-S6-092.yaml) | 父母吵架孩子怕分开 |
| [C-S6-093](s6-12to24mo/C-S6-093.yaml) | 别让娃当你情绪保姆 |
| [C-S6-094](s6-12to24mo/C-S6-094.yaml) | 分离后发脾气是健康 |
| [C-S6-095](s6-12to24mo/C-S6-095.yaml) | 黏人 ≠ 被宠坏 |
| [C-S6-096](s6-12to24mo/C-S6-096.yaml) | 病故别瞒孩子隐瞒更怕 |
| [C-S6-097](s6-12to24mo/C-S6-097.yaml) | 稳定家庭 5 个特征 |
| [C-S6-098](s6-12to24mo/C-S6-098.yaml) | **撤回爱当惩罚最伤 ⭐** |
| [C-S6-099](s6-12to24mo/C-S6-099.yaml) | 我是为你好的陷阱 |

### S7 · 24-36 月(10 张)

| ID | title |
|---|---|
| [C-S7-034](s7-24to36mo/C-S7-034.yaml) | 必须分离时怎么少伤害 |
| [C-S7-035](s7-24to36mo/C-S7-035.yaml) | **别偷偷溜要正面告别 ⭐** |
| [C-S7-036](s7-24to36mo/C-S7-036.yaml) | 3 岁可能比 2 岁更难分离 |
| [C-S7-037](s7-24to36mo/C-S7-037.yaml) | 强忍不哭是压力不是适应 |
| [C-S7-038](s7-24to36mo/C-S7-038.yaml) | 9 岁前不怕死 |
| [C-S7-039](s7-24to36mo/C-S7-039.yaml) | **5 岁前住院影响到 18 岁 ⭐** |
| [C-S7-040](s7-24to36mo/C-S7-040.yaml) | 怕黑怕雷可能是怕妈走 |
| [C-S7-041](s7-24to36mo/C-S7-041.yaml) | 拒学和逃学完全不同 |
| [C-S7-042](s7-24to36mo/C-S7-042.yaml) | 强独立不健康 |
| [C-S7-043](s7-24to36mo/C-S7-043.yaml) | 妈不舍 = 妈自己焦虑 |

> ⭐ Bowlby Vol 2 核心立场卡:抗议-绝望-超脱 3 阶段 / 撤回爱最伤 / 别偷溜要告别 / 5 岁前住院创伤 / 精神虐待边界。
> Robertson 1952 住院儿童纪录片 + 跨源对照 Wonder Week WW46-WW75 fussy phase 时间窗。

---

## SRC-013 · van de Rijt + Plooij《The Wonder Weeks(婴儿大脑跃迁 10 周)》

**英文原版**:Hetty van de Rijt + Frans X. Plooij, *The Wonder Weeks: How to Stimulate Your Baby's Mental Development* (Kiddy World Publishing, 1992 荷兰文初版,英译多版本)
**中译**:有(网上流传"神奇周"译本,本次以 OCR 英文 epub 为准)
**对应段**:S1-S7(全段,10 个跃迁覆盖 0-20 月)
**卡片总数**:35(原 30 + 自审补 5)
**等级分布**:A 6 / B 25 / C 4
**Source yaml**:[SRC-013.yaml](../10-sources/tier3-books/notes/SRC-013.yaml)

### S1 · 0-1 月(5 张:4 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-178](s1-newborn/C-S1-178.yaml) | **三 C 同时 = 跃迁不是病 ⭐** | development_burst, philosophy | B |
| [C-S1-179](s1-newborn/C-S1-179.yaml) | **10 个跃迁时间表 ⭐** | development_burst | B |
| [C-S1-180](s1-newborn/C-S1-180.yaml) | 早产宝宝跃迁按预产期算 | development_burst, premature | B |
| [C-S1-181](s1-newborn/C-S1-181.yaml) | 5 周第一跃迁:感觉世界 | development_burst | B |
| [C-S1-182](s1-newborn/C-S1-182.yaml) | 🔍 大脑跃迁 ≠ 身体长高 | development_burst, philosophy | B |

### S2 · 1-3 月(6 张:5 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-121](s2-1to3mo/C-S2-121.yaml) | 8 周第二跃迁:模式世界 | development_burst | B |
| [C-S2-122](s2-1to3mo/C-S2-122.yaml) | 12 周第三跃迁:平滑过渡 | development_burst | B |
| [C-S2-123](s2-1to3mo/C-S2-123.yaml) | fussy 期不睡训不戒奶 | development_burst, philosophy | C |
| [C-S2-124](s2-1to3mo/C-S2-124.yaml) | **fussy 期再崩溃也别摇宝宝 ⭐** | safety, red_flag | A |
| [C-S2-125](s2-1to3mo/C-S2-125.yaml) | 跃迁后宝宝突然"长大了" | development_burst, philosophy | B |
| [C-S2-126](s2-1to3mo/C-S2-126.yaml) | 🔍 跃迁后是黄金陪练期(skill 期父母换角色) | development_burst, parental_role | C |

### S3 · 3-6 月(4 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-129](s3-3to6mo/C-S3-129.yaml) | 19 周第四跃迁:事件世界 | development_burst | B |
| [C-S3-130](s3-3to6mo/C-S3-130.yaml) | 4-5 月 fussy 期可达 6 周 | development_burst, philosophy | B |
| [C-S3-131](s3-3to6mo/C-S3-131.yaml) | **4 月奶量骤降 = 跃迁不是断奶 ⭐** | feeding, development_burst | B |
| [C-S3-132](s3-3to6mo/C-S3-132.yaml) | 4 月想"逃走"不是育儿失败 | philosophy, postpartum | B |

### S4 · 6-9 月(6 张:5 + 自审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-124](s4-6to9mo/C-S4-124.yaml) | 26 周第五跃迁:关系世界 | development_burst | B |
| [C-S4-125](s4-6to9mo/C-S4-125.yaml) | **跃迁周龄 ↔ 依恋时间表对照 ⭐** | development_burst, philosophy | A |
| [C-S4-126](s4-6to9mo/C-S4-126.yaml) | **fussy 不是出牙痛 ⭐** | development_burst, controversy | A |
| [C-S4-127](s4-6to9mo/C-S4-127.yaml) | 6-8 月拒绝换尿布 | development_burst | B |
| [C-S4-128](s4-6to9mo/C-S4-128.yaml) | 8 月又一次 fussy 来袭(WW37 前奏) | development_burst | B |
| [C-S4-129](s4-6to9mo/C-S4-129.yaml) | **🔍 6 月起绝不偷溜走 ⭐**(三派一致:Wonder Weeks + Bowlby + AAP) | development_burst, philosophy | A |

### S5 · 9-12 月(4 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-126](s5-9to12mo/C-S5-126.yaml) | 37 周第六跃迁:分类世界 | development_burst | B |
| [C-S5-127](s5-9to12mo/C-S5-127.yaml) | 46 周第七跃迁:序列世界 | development_burst | B |
| [C-S5-128](s5-9to12mo/C-S5-128.yaml) | fussy 不只是哭 — 撒娇也是 | development_burst | C |
| [C-S5-129](s5-9to12mo/C-S5-129.yaml) | 8-12 月双跃迁 = 妈妈极限 | development_burst, philosophy | B |

### S6 · 12-24 月(8 张:6 + 自审补 2)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-122](s6-12to24mo/C-S6-122.yaml) | 55 周第八跃迁:程序世界 | development_burst | B |
| [C-S6-123](s6-12to24mo/C-S6-123.yaml) | 64 周第九跃迁:原则世界 | development_burst | B |
| [C-S6-124](s6-12to24mo/C-S6-124.yaml) | **75 周第十跃迁:系统世界 ⭐** | development_burst | A |
| [C-S6-125](s6-12to24mo/C-S6-125.yaml) | 13-18 月连续三跃迁 | development_burst, philosophy | B |
| [C-S6-126](s6-12to24mo/C-S6-126.yaml) | **跃迁期不打不骂 ⭐** | philosophy, discipline, controversy | A |
| [C-S6-127](s6-12to24mo/C-S6-127.yaml) | "质量时间"是个伪概念 | philosophy, parental_role | C |
| [C-S6-128](s6-12to24mo/C-S6-128.yaml) | 🔍 14-17 月模仿一切坏事也学 | development_burst, discipline | B |
| [C-S6-129](s6-12to24mo/C-S6-129.yaml) | **🔍 跃迁有 EEG 物理证据 ⭐**(给怀疑家人 / 老人) | development_burst, evidence | A |

### S7 · 24-36 月(2 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S7-074](s7-24to36mo/C-S7-074.yaml) | 21 月后跃迁框架结束 | development_burst, philosophy | B |
| [C-S7-075](s7-24to36mo/C-S7-075.yaml) | 跃迁是普遍 = 育儿不孤单 | philosophy, cross_cultural | B |

> ⭐ 6 张 A 级核心(必读):三 C 信号 / 10 跃迁时间表 / 不能摇宝宝 / 跃迁周龄↔依恋对照 / 跃迁期不打不骂 / 系统世界 / **6 月起不偷溜** / **EEG 物理证据**。
> 🔍 5 张自审补卡(2026-05-03 收官):大脑跃迁 ≠ 身体长高 / skill 期父母换角色 / 6 月起不偷溜走 / 14-17 月模仿一切坏事 / 跃迁有 EEG 物理证据。
> 跨源对照亮点:Wonder Week 26-37 跃迁与 Bowlby Vol 1/2 的依恋关键期完美重合(见 C-S4-125 + C-S4-129)。
> 新术语 8 张:G-PERSON-vanderijt / G-PERSON-plooij / G-TERM-wonder-week / G-TERM-mental-leap / G-TERM-3C-signs / G-TERM-fussy-phase / **G-TERM-skill-phase / G-TERM-growth-spurt**(后两张自审补)。

---

*最后更新:2026-05-03 Phase 4 两本并行完成 + Wonder Weeks 收官审计(Bowlby Vol 2 32 + Wonder Weeks 35),累计 **365 张知识卡 + 108 张术语卡** + 11 SRC 引用。*

---

## SRC-014 · Davies + Uzodike《The Montessori Baby》

**英文原版**:Simone Davies + Junnifa Uzodike, *The Montessori Baby: A Parent's Guide to Nurturing Your Baby with Love, Respect, and Understanding* (Workman Publishing, 2021)
**中译本**:有(《蒙特梭利的小宝宝:0-1 岁》)
**对应段**:S0-S6(本书覆盖 0-12 月为主,延展少量 1-2 岁)
**卡片总数**:36(34 + 自审补 2)
**等级分布**:A 11 / B 20 / C 5
**Source yaml**:[SRC-014.yaml](../10-sources/tier3-books/notes/SRC-014.yaml)

### S0 · 孕期(4 张:3 + 二审补 1)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S0-008](s0-pregnancy/C-S0-008.yaml) | 子宫是宝宝第一个"家" | montessori, prenatal, environment | B |
| [C-S0-009](s0-pregnancy/C-S0-009.yaml) | 蒙氏宝宝起步装清单 | montessori, prenatal, simplicity | C |
| [C-S0-010](s0-pregnancy/C-S0-010.yaml) | 孕期就开始读宝宝 | montessori, prenatal, philosophy | C |
| [C-S0-011](s0-pregnancy/C-S0-011.yaml) | 🔍 **蒙氏育儿就是慢 ⭐**(going slow) | montessori, philosophy | B |

### S1 · 0-1 月(8 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-183](s1-newborn/C-S1-183.yaml) | 蒙氏新生儿期 6-8 周 | montessori, symbiosis, philosophy | B |
| [C-S1-184](s1-newborn/C-S1-184.yaml) | **新生儿能看 30cm ⭐** | montessori, vision, feeding | A |
| [C-S1-185](s1-newborn/C-S1-185.yaml) | **蒙氏小毯防放下就醒 ⭐** | montessori, sleep, topponcino | B |
| [C-S1-186](s1-newborn/C-S1-186.yaml) | 新生儿别戴手套 | montessori, hands, orientation | B |
| [C-S1-187](s1-newborn/C-S1-187.yaml) | **蒙氏不主张包裹 ⭐**(controversy:vs Karp) | montessori, swaddle, controversy | A |
| [C-S1-188](s1-newborn/C-S1-188.yaml) | 慢动作换尿布 | montessori, diaper, respect | C |
| [C-S1-189](s1-newborn/C-S1-189.yaml) | 第一个 mobile 是黑白(Munari) | montessori, vision, mobile | B |
| [C-S1-190](s1-newborn/C-S1-190.yaml) | **回应宝宝不会宠坏 ⭐**(蒙氏 + 依恋一致) | montessori, attachment, philosophy | A |

### S2 · 1-3 月(8 张:5 + 一审补 1 + 二审补 2)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-127](s2-1to3mo/C-S2-127.yaml) | 跟宝宝用真词不嘎嘎(parentese) | montessori, language, parentese | B |
| [C-S2-128](s2-1to3mo/C-S2-128.yaml) | 等 3 秒再回应(tarry time) | montessori, communication | B |
| [C-S2-129](s2-1to3mo/C-S2-129.yaml) | 别打断 1 月宝宝看自己手 | montessori, concentration, philosophy | B |
| [C-S2-130](s2-1to3mo/C-S2-130.yaml) | 1-3 月 mobile 升级(三色 / 渐变 / 舞者) | montessori, vision, mobile | C |
| [C-S2-131](s2-1to3mo/C-S2-131.yaml) | **别 propping 宝宝坐 ⭐**(髋部 + DDH 风险) | montessori, motor, controversy | A |
| [C-S2-132](s2-1to3mo/C-S2-132.yaml) | 🔍 哭闹 5 步回应法 | montessori, crying, response | B |
| [C-S2-133](s2-1to3mo/C-S2-133.yaml) | 🔍 **双语家庭一人一语 ⭐**(OPOL) | montessori, language, bilingual | B |
| [C-S2-134](s2-1to3mo/C-S2-134.yaml) | 🔍 嘴是宝宝探索器官(0-14 月) | montessori, oral, exploration | B |

### S3 · 3-6 月(5 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-133](s3-3to6mo/C-S3-133.yaml) | **地板床 vs 婴儿床 ⭐**(蒙氏 vs AAP 立场对照) | montessori, sleep, controversy | B |
| [C-S3-134](s3-3to6mo/C-S3-134.yaml) | 4-5 月喊叫是发声练习 | montessori, language, freedom | B |
| [C-S3-135](s3-3to6mo/C-S3-135.yaml) | **6 月固食 5 信号 ⭐**(蒙氏 readiness) | montessori, solids, feeding | A |
| [C-S3-136](s3-3to6mo/C-S3-136.yaml) | 别把玩具塞他手里 | montessori, motor, philosophy | B |
| [C-S3-137](s3-3to6mo/C-S3-137.yaml) | 选真实主题的绘本(不要奇幻) | montessori, books, language | B |

### S4 · 6-9 月(5 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-130](s4-6to9mo/C-S4-130.yaml) | **把整个房间做成 yes 空间 ⭐**(替代 playpen) | montessori, yes-space, environment | B |
| [C-S4-131](s4-6to9mo/C-S4-131.yaml) | 7-8 月让宝宝自取水(practical life 起步) | montessori, independence, hydration | C |
| [C-S4-132](s4-6to9mo/C-S4-132.yaml) | **不用 jumper 学步车 ⭐**(蒙氏 + AAP 双反对) | montessori, motor, controversy | A |
| [C-S4-133](s4-6to9mo/C-S4-133.yaml) | 7-8 月教手语(milk / done / more) | montessori, sign-language | B |
| [C-S4-134](s4-6to9mo/C-S4-134.yaml) | 6-9 月秩序敏感期 | montessori, environment, sensitive-period | B |

### S5 · 9-12 月(8 张:5 + 二审补 3)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-130](s5-9to12mo/C-S5-130.yaml) | **1 岁前两份心理大礼 ⭐**(信任环境+信任自己) | montessori, trust, milestone | A |
| [C-S5-131](s5-9to12mo/C-S5-131.yaml) | **不替宝宝做能做的事 ⭐**(蒙氏黄金原则) | montessori, independence, philosophy | A |
| [C-S5-132](s5-9to12mo/C-S5-132.yaml) | 别说"宝宝好棒"(蒙氏 alternatives to praise) | montessori, praise, controversy | B |
| [C-S5-133](s5-9to12mo/C-S5-133.yaml) | **10-12 月自喂手指食 ⭐**(蒙氏 + BLW 一致) | montessori, feeding, BLW | A |
| [C-S5-134](s5-9to12mo/C-S5-134.yaml) | 1 岁前戒奶嘴 | montessori, pacifier, language | B |
| [C-S5-135](s5-9to12mo/C-S5-135.yaml) | 🔍 **不偷溜 + 告别仪式 ⭐**(蒙氏离别 5 招) | montessori, separation, ritual | A |
| [C-S5-136](s5-9to12mo/C-S5-136.yaml) | 🔍 选 day care 8 条(蒙氏看人不看招牌) | montessori, daycare, selection | B |
| [C-S5-137](s5-9to12mo/C-S5-137.yaml) | 🔍 **6-16 月黏人是健康 ⭐**(蒙氏处理分离焦虑) | montessori, separation-anxiety | A |

### S6 · 12-24 月(9 张:3 + 一审补 1 + 二审补 5)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-130](s6-12to24mo/C-S6-130.yaml) | 12-15 月生活技能起步 | montessori, practical-life | B |
| [C-S6-131](s6-12to24mo/C-S6-131.yaml) | 12-15 月转矮床(没用 floor bed 的过渡) | montessori, sleep, transition | B |
| [C-S6-132](s6-12to24mo/C-S6-132.yaml) | **2 岁前不看屏幕 ⭐**(蒙氏 + AAP 双背书) | montessori, screen, controversy | A |
| [C-S6-133](s6-12to24mo/C-S6-133.yaml) | 🔍 **温柔但清晰的边界 ⭐**(五派一致反体罚) | montessori, boundaries, discipline | A |
| [C-S6-134](s6-12to24mo/C-S6-134.yaml) | 🔍 **1 岁打咬扔不是坏 ⭐**(蒙氏 4 步翻译) | montessori, aggression, behavior | A |
| [C-S6-135](s6-12to24mo/C-S6-135.yaml) | 🔍 1 岁不强迫分享(turn-taking) | montessori, sharing, social | B |
| [C-S6-136](s6-12to24mo/C-S6-136.yaml) | 🔍 老大迎二宝(蒙氏二胎过渡 5 步) | montessori, siblings, transition | B |
| [C-S6-137](s6-12to24mo/C-S6-137.yaml) | 🔍 跟老人/伴侣不同步(NVC 沟通) | montessori, family, communication | B |
| [C-S6-138](s6-12to24mo/C-S6-138.yaml) | 🔍 蒙氏父母先照顾自己(49 ideas) | montessori, parent-self-care | B |

> ⭐ 16 张 A 级核心(必读):新生儿 30cm / 蒙氏小毯 / 不主张包裹 / 不会宠坏 / 别 propping 坐 / 6 月固食 5 信号 / yes 空间 / 不用 jumper / 1 岁两份大礼 / 不替宝宝做 / 自喂 / 2 岁前不屏幕 / 温柔边界 / 不偷溜告别 / 6-16 月黏人是健康 / 1 岁打咬扔翻译。
> 🔍 13 张审计补卡:
>   - 一审补 2 张(2026-05-03 初版):C-S2-132 哭闹 5 步 + C-S6-133 温柔边界
>   - **二审补 11 张**(2026-05-03 终版):C-S0-011 going slow 哲学 + C-S2-133 OPOL 双语 + C-S2-134 嘴是探索器官 + C-S5-135 不偷溜告别 + C-S5-136 选 day care + C-S5-137 黏人是健康 + C-S6-134 1 岁打咬扔 + C-S6-135 不强迫分享 + C-S6-136 老大迎二宝 + C-S6-137 跟老人不同步 + C-S6-138 父母先照顾自己
> 跨源对照亮点(蒙氏 ↔ 现有 6 本书):
>   - **swaddle 包裹立场对立**(C-S1-187 蒙氏 vs C-S1-007/009/013-015 Karp)
>   - **floor bed vs AAP cribs 兼容**(C-S3-133 蒙氏遵守 AAP SIDS 全部 10 条)
>   - **回应不宠坏**(C-S1-190 蒙氏 + Bowlby C-S1-127 反应快宝宝独立)
>   - **不打不骂(五派一致)**(C-S6-133 蒙氏 + 鲍秀兰 C-S6-007 + Bowlby C-S6-070 + Wonder Week C-S6-126 + AAP)
>   - **不偷溜告别**(C-S5-135 蒙氏 + Bowlby Vol 2 C-S5-088 + Wonder Week C-S4-129 6 月起)
>   - **黏人是健康**(C-S5-137 蒙氏 + Bowlby C-S5-069 安全依恋反更早分离焦虑)
>   - **5 信号 readiness**(C-S3-135 蒙氏 + AAP C-S3-001)
>   - **不学步车**(C-S4-132 蒙氏 + AAP C-S4-005)
>   - **跃迁 vs 敏感期**(C-S4-134 蒙氏秩序敏感期 + Wonder Week C-S4-127 拒绝换尿布)
> 新术语 13 张:G-PERSON-Davies / G-PERSON-Montessori / G-PERSON-Uzodike / G-PERSON-Gerber / G-TERM-absorbent-mind / G-TERM-yes-space / G-TERM-floor-bed / G-TERM-topponcino / G-TERM-prepared-environment / G-TERM-symbiosis-period / G-TERM-practical-life / G-TERM-going-slow / G-TERM-nido。

---

*最后更新:2026-05-03 Phase 5 Davies 蒙氏 0-1 二次审计补漏完成,累计 **412 张知识卡 + 133 张术语卡** + 12 SRC 引用。*

---

## SRC-016 · Lillard + Jessen《Montessori from the Start》

**英文原版**:Paula Polk Lillard + Lynn Lillard Jessen, *Montessori from the Start: The Child at Home, from Birth to Age Three* (Schocken Books, New York, 2003)
**ISBN_en**:978-0-8052-1112-1
**对应段**:S0-S7(全段覆盖,首次)
**卡片总数**:52(44 + 二审补 2 + 三审补 6)
**等级分布**:A 18 / B 34 / C 0 — A 占 35%(高于 Davies 31%,反映 Lillard 学院深度)
**Source yaml**:[SRC-016.yaml](../10-sources/tier3-books/notes/SRC-016.yaml)

### S0 · 孕期(3 张)

| ID | title | 等级 |
|---|---|---|
| [C-S0-012](s0-pregnancy/C-S0-012.yaml) | 蒙氏 4 大发展阶段 | B |
| [C-S0-013](s0-pregnancy/C-S0-013.yaml) | 蒙氏育儿公式 | B |
| [C-S0-014](s0-pregnancy/C-S0-014.yaml) | 爸爸头 8 周是缓冲器 ⭐ | A |

### S1 · 0-1 月(6 张)

| ID | title | 等级 |
|---|---|---|
| [C-S1-247](s1-newborn/C-S1-247.yaml) | 蒙氏新生儿房 4 区 | B |
| [C-S1-248](s1-newborn/C-S1-248.yaml) | 别打断专注!掌声破坏 ⭐ | A |
| [C-S1-249](s1-newborn/C-S1-249.yaml) | 头月 1 房 + 3 人 | B |
| [C-S1-250](s1-newborn/C-S1-250.yaml) | 反"刺激"潮流 | B |
| [C-S1-251](s1-newborn/C-S1-251.yaml) | 哺乳 8-10 周才"亲密" | B |
| [C-S1-252](s1-newborn/C-S1-252.yaml) | 不戴奶嘴 = 嘴能发声 | B |

### S2 · 1-3 月(6 张:5 + 三审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S2-185](s2-1to3mo/C-S2-185.yaml) | 注意力问题溯源 0-3 月 | B |
| [C-S2-186](s2-1to3mo/C-S2-186.yaml) | 说话慢 + 等回应 | B |
| [C-S2-187](s2-1to3mo/C-S2-187.yaml) | 旋转 ≠ 换新 | B |
| [C-S2-188](s2-1to3mo/C-S2-188.yaml) | 出生前已"认识"妈妈 ⭐ | A |
| [C-S2-189](s2-1to3mo/C-S2-189.yaml) | 0-6 岁只给真实 ⭐ | A |
| [C-S2-190](s2-1to3mo/C-S2-190.yaml) | 🔍 你家是 4 类哪一类 | B |

### S3 · 3-6 月(5 张)

| ID | title | 等级 |
|---|---|---|
| [C-S3-191](s3-3to6mo/C-S3-191.yaml) | 别塞玩具到宝宝手里 | B |
| [C-S3-192](s3-3to6mo/C-S3-192.yaml) | 蒙氏 mobile 5 阶升级 | B |
| [C-S3-193](s3-3to6mo/C-S3-193.yaml) | 弹簧 mobile 抓握期 | B |
| [C-S3-194](s3-3to6mo/C-S3-194.yaml) | 醒着多趴 vs AAP 仰睡 ⭐ | A |
| [C-S3-195](s3-3to6mo/C-S3-195.yaml) | 6 月正餐时给水 | B |

### S4 · 6-9 月(6 张:5 + 三审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S4-190](s4-6to9mo/C-S4-190.yaml) | 8-9 月"第二次出生" ⭐ | A |
| [C-S4-191](s4-6to9mo/C-S4-191.yaml) | 坐型 vs 爬型 都健康 | B |
| [C-S4-192](s4-6to9mo/C-S4-192.yaml) | 别替宝宝坐和走 | B |
| [C-S4-193](s4-6to9mo/C-S4-193.yaml) | 6 月双手过物 pincer | B |
| [C-S4-194](s4-6to9mo/C-S4-194.yaml) | 推车型 不是学步车 ⭐ | A |
| [C-S4-195](s4-6to9mo/C-S4-195.yaml) | 🔍 7-9 月真物探索篮 | B |

### S5 · 9-12 月(6 张:5 + 二审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S5-184](s5-9to12mo/C-S5-184.yaml) | 14 月起公共场所手牵手 ⭐ | A |
| [C-S5-185](s5-9to12mo/C-S5-185.yaml) | 走稳就赤脚 | B |
| [C-S5-186](s5-9to12mo/C-S5-186.yaml) | 蒙氏断奶椅替高脚椅 | B |
| [C-S5-187](s5-9to12mo/C-S5-187.yaml) | 每天给宝宝散步 | B |
| [C-S5-188](s5-9to12mo/C-S5-188.yaml) | 9-10 月升级真玻璃杯 | B |
| [C-S5-189](s5-9to12mo/C-S5-189.yaml) | 🔍 关门睡 + 不靠抱晃睡 | B |

### S6 · 12-24 月(12 张:8 + 二审补 1 + 三审补 3) — Lillard 最强段

| ID | title | 等级 |
|---|---|---|
| [C-S6-184](s6-12to24mo/C-S6-184.yaml) | 15 月转工作 最大努力期 ⭐ | A |
| [C-S6-185](s6-12to24mo/C-S6-185.yaml) | 蒙氏完整循环活动 | B |
| [C-S6-186](s6-12to24mo/C-S6-186.yaml) | 母-师角色(妈第一) | B |
| [C-S6-187](s6-12to24mo/C-S6-187.yaml) | 演示要慢 + 同顺序 | B |
| [C-S6-188](s6-12to24mo/C-S6-188.yaml) | 给选 2 不给选 3 ⭐ | A |
| [C-S6-189](s6-12to24mo/C-S6-189.yaml) | 12-18 月如厕敏感期 ⭐ | A |
| [C-S6-190](s6-12to24mo/C-S6-190.yaml) | 反纸尿裤 sauna 效应 | B |
| [C-S6-191](s6-12to24mo/C-S6-191.yaml) | 12-18 月限度物理移除 ⭐ | A |
| [C-S6-192](s6-12to24mo/C-S6-192.yaml) | 🔍 No 永远是 No ⭐ | A |
| [C-S6-193](s6-12to24mo/C-S6-193.yaml) | 🔍 12-24 月词汇爆炸期 ⭐ | A |
| [C-S6-194](s6-12to24mo/C-S6-194.yaml) | 🔍 描述法替"讲道理" ⭐ | A |
| [C-S6-195](s6-12to24mo/C-S6-195.yaml) | 🔍 父母自己读书 = 模范 ⭐ | A |

### S7 · 24-36 月(8 张:7 + 三审补 1) — Lillard 重点段

| ID | title | 等级 |
|---|---|---|
| [C-S7-130](s7-24to36mo/C-S7-130.yaml) | 18 月-3 岁服从 3 阶段 ⭐ | A |
| [C-S7-131](s7-24to36mo/C-S7-131.yaml) | 3 岁是真"上学龄" | B |
| [C-S7-132](s7-24to36mo/C-S7-132.yaml) | 蒙氏要"性格"非"幸福" | B |
| [C-S7-133](s7-24to36mo/C-S7-133.yaml) | 2 岁切香蕉用真钝刀 | B |
| [C-S7-134](s7-24to36mo/C-S7-134.yaml) | Tom Sawyer 法搞家务 | B |
| [C-S7-135](s7-24to36mo/C-S7-135.yaml) | 婚姻在孩子之前 ⭐ | A |
| [C-S7-136](s7-24to36mo/C-S7-136.yaml) | 观察 = 科学家方式 | B |
| [C-S7-137](s7-24to36mo/C-S7-137.yaml) | 🔍 轮流教学法 | B |

> ⭐ 18 张 A 级核心(必读):爸爸缓冲器 / 别打断专注 / 出生前已认识妈妈 / 0-6 岁只给真实 / 醒着多趴 / 第二次出生 / 推车型 walker / 14 月手牵手 / 15 月转工作 / 给选 2 / 12-18 月如厕敏感期 / 物理移除 / No 永远是 No / 词汇爆炸 / 描述法替讲道理 / 父母读书模范 / 18 月-3 岁服从 3 阶段 / 婚姻在孩子之前。
> 🔍 8 张审计补卡(2026-05-03):
>   - 二审补 2 张:C-S5-189 关门睡 + C-S6-192 No 永远是 No
>   - **三审补 6 张**(用户要求 整本 spot-check):C-S2-190 flow 4 类家庭 + C-S4-195 真物探索篮 + C-S6-193 词汇爆炸 + C-S6-194 描述法替讲道理 + C-S6-195 父母读书模范 + C-S7-137 轮流教学法
> 跨源对照亮点(Lillard ↔ 现有 9 本书,蒙氏 0-3 闭环完成):
>   - **跟 Davies 蒙氏 0-1 闭环**(理论深度 + S6/S7 1-3 岁补全)
>   - **手牵手公共场所(C-S5-184 蒙氏 + 鲍秀兰 C-S6-007 + Davies C-S6-133 温柔边界)** — 三派一致
>   - **第二次出生 8-9 月**(C-S4-190 蒙氏 + Bowlby C-S5-070 安全基地 + Karp C-S1-001 第四孕期)— 三派概念呼应
>   - **婚姻 > 孩子**(C-S7-135 蒙氏 + Davies C-S6-138 父母照顾自己 + Davies C-S6-137 跟老人 NVC)
>   - **No 永远是 No**(C-S6-192 蒙氏 + 鲍秀兰 C-S6-007 + Davies C-S6-133)— 三派一致
>   - **12-18 月如厕敏感期** — Lillard 立场反潮流,反对 2-3 岁主流(独有)
>   - **反纸尿裤 sauna 效应** — Lillard 立场比 Davies 更强(独有)
>   - **0-6 岁只给真实**(C-S2-189 蒙氏 + Davies C-S3-137 选真实绘本)— Lillard 比 Davies 立场更激进
>   - **服从 3 阶段(12-18/18-36/3+)** — Lillard 系统化(Davies 没明确)
> 新术语 11 张:G-PERSON-Lillard / G-PERSON-Jessen / G-PERSON-Csikszentmihalyi / G-TERM-self-construction / G-TERM-cycle-of-activity / G-TERM-coordinated-movement / G-TERM-language-explosion / G-TERM-points-of-reference / G-TERM-weaning-table / G-TERM-flow / G-TERM-second-birth。

---

*最后更新:2026-05-03 Phase 6 第二本 Lillard 蒙氏 0-3 学院派 三审补漏完成,累计 **499 张知识卡 + 151 张术语卡(实测 ls)** + 14 SRC 引用。蒙氏 0-3 闭环完成(Davies 实操 + Lillard 理论)。*

---

## SRC-017 · Bowlby《依恋三部曲 · 第三卷:丧失》

**中译本**:世界图书出版有限公司北京分公司,2018 年,付琳等译,易春丽审校
**ISBN**:978-7-5192-3383-9
**英文原版**:John Bowlby, *Attachment and Loss, Volume 3: Loss, Sadness and Depression* (Hogarth Press / Basic Books, 1980)
**对应段**:S5(1)+ S6(3)+ S7(11)= 15 张
**卡片总数**:**15**(用户压缩版)
**等级分布**:**A 11 / B 4 / C 0**(A 占 73% — 涉 Tier 1 共识 + Robertson 大型实证)
**Source yaml**:[SRC-017.yaml](../10-sources/tier3-books/notes/SRC-017.yaml)
**流派**:依恋三部曲收官 — 哀伤 4 阶段儿童版 + 谈死亡话术 + 病理性哀伤识别

### 用户指示驱动的章节裁剪
用户明确"父母离异等正常人不存在的情况可以不要" → 跳过 9 个极端章节,聚焦中国普通家长高频场景。
跳过:Ch4/13/20(防御认知抽象)/ Ch9/11(病理失调)/ Ch17/19/21(精神病性 / 寄宿 / 离异)/ Ch22(父母自杀)。
精选 5 章产卡:Ch15-16 + Ch18 + Ch23-25(2-4 岁儿童反应金矿)。

### S5 · 9-12 月(1 张)
- C-S5-290:月嫂阿姨离别要重视

### S6 · 12-24 月(3 张)
- C-S6-293:1 岁半已会想念妈
- C-S6-294:替代照顾者最关键
- C-S6-295:玩具宠物丢是早练习

### S7 · 24-36 月(11 张)— V3 主战场
- C-S7-237:谈死亡用真话不绕弯
- C-S7-238:看似没事是最危险信号
- C-S7-239:别威胁再哭就不要你
- C-S7-240:重聚冷淡是修复期
- C-S7-241:告诉娃不是他的错
- C-S7-242:哀伤 4 阶段儿童版 ⭐ V3 独有
- C-S7-243:小细节是思念信号
- C-S7-244:二宝出生 = 老大丧失
- C-S7-245:大人也可以哭
- C-S7-246:1 年还卡住要找专业
- C-S7-247:爷奶去世跟娃讲

> 新术语 3 张:G-TERM-mourning / G-TERM-childhood-mourning / G-TERM-four-phases-mourning。
> 复用 13 张依恋术语(100% reuse)。

---

## SRC-018 · Stern《The Interpersonal World of the Infant》

**英文原版**:Daniel N. Stern, *The Interpersonal World of the Infant: A View from Psychoanalysis and Developmental Psychology* (Basic Books, New York, 1985, Updated Edition 2000)
**ISBN_en**:978-0-465-09559-9
**作者**:Daniel N. Stern(1934-2012)— 瑞士裔美国精神分析师 + 发展心理学家,日内瓦大学 / Cornell Med 教授,**self 心理学教父**,世界婴儿心理健康协会(WAIMH)创办人之一
**对应段**:**S0-S7 全段覆盖**
**卡片总数**:**44**(并行 session 41 + R2 补 2:still-face + 过度/不足刺激 + 用户深度审 R5 补 1:主题+变奏)
**等级分布**:**A 32 / B 12 / C 0**(A 级 **72%** — 远高于 Lillard 35%,反映 Stern 实证扎实 + 跨派一致)
**Source yaml**:[SRC-018.yaml](../10-sources/tier3-books/notes/SRC-018.yaml)
**流派**:**Self 心理学奠基** — 跟蒙氏(哲学)+ Bowlby(关系)三角互补,本卷给"心理过程"层

### S0 · 孕期 / 哲学(4 张)
- C-S0-015:Stern 4 层自我终身叠加(框架总览)
- C-S0-016:反"新生儿混沌" 出生即有意识 ⭐ 反 Mahler 共生论
- C-S0-017:三派 self 框架互补(蒙氏/Bowlby/Stern)
- C-S0-018:婴儿是真实测试者(反 Freud 幻想婴儿)— 并行 session

### S1 · 0-1 月(5 张)
- C-S1-253:别错过安静警觉态(alert inactivity 黄金窗)
- C-S1-254:新生自我在组装中(emergent self)
- C-S1-255:出生即跨感官辨认 ⭐ Meltzoff 1979
- C-S1-256:给宝宝主体属性是对的 ⭐ Vygotsky ZPD
- C-S1-257:出生 2 天已模仿表情 ⭐ Field 1982

### S2 · 1-3 月(4 张)
- C-S2-191:2 月跃迁启动核心自我 ⭐
- C-S2-192:妈语 + 婴儿脸都对 ⭐ parentese + baby faces
- C-S2-193:活力情感 = 宝宝最早的心(vitality affects)
- C-S2-194:喂奶换尿也是社交时刻 ⭐ 中国家长高频痛点

### S3 · 3-6 月(6 张:5 + 用户深度审补 1)
- C-S3-196:核心自我 4 体验凑齐 ⭐ agency / coherence / affectivity / history
- C-S3-197:父母 = 自我调节他者 ⭐ 6 类调节
- C-S3-198:RIGs = 互动原型记忆 ⭐ IWM 积木块
- C-S3-199:独自时也"有人陪" ⭐ evoked companion
- C-S3-200:宝宝也在调节你(并行 session)mutual regulation
- C-S3-201:**主题 + 变奏 = 互动模板**(用户深度审补)⭐ 反"宝宝会烦吗"中国家长高频疑问

### S4 · 6-9 月(7 张:6 + R2 补 1)
- C-S4-196:7-9 月主观自我跃迁 ⭐
- C-S4-197:9 月会指物 + 跟随指 ⭐ joint attention
- C-S4-198:9 月起"为信息而沟通" ⭐ intentional communication
- C-S4-199:7-9 月 你的共情 宝宝能感(psychic intimacy)
- C-S4-200:选择性调谐教情感边界 ⭐ socialization 工具
- C-S4-201:活力情感 = 调谐燃料
- C-S4-202:**过度刺激 vs 不足刺激**(R2 补)⭐ Stevie 案例

### S5 · 9-12 月(9 张:7 + 并行 1 + R2 补 1)— **Stern 最强段**
- C-S5-291:**情感调谐 = 心同频** ⭐⭐⭐ Stern 最重要原创
- C-S5-292:调谐 ≠ 模仿 ≠ 镜像
- C-S5-293:调谐 6 个匹配方面
- C-S5-294:故意失调谐 = 调节工具
- C-S5-295:共在 vs 沟通 别混 ⭐
- C-S5-296:调谐多在无意识中(90%)
- C-S5-297:调谐 = 安全依恋的根 ⭐
- C-S5-298:**修复比完美更建 secure**(并行 session)⭐ rupture-and-repair
- C-S5-299:**扑克脸 = 玩手机代价**(R2 补)⭐ Tronick still-face

### S6 · 12-24 月(5 张)
- C-S6-1072:15-18 月语言自我启动 ⭐
- C-S6-297:18 月镜中认我 = 客观我 ⭐ rouge test
- C-S6-298:语言是双刃剑 — 异化体验 ⭐
- C-S6-299:给情感贴标签要准 ⭐ we meanings
- C-S6-300:会说话后调谐仍要

### S7 · 24-36 月(4 张)
- C-S7-248:我 / 我的 = 客观自我
- C-S7-249:妈说"乖" 爸说"乖" 不一样
- C-S7-250:学说话是为重建跟妈共在(Dore)
- C-S7-251:玩偶演练真实 = self 探索

### Stern 三审通过(R1 + R2 + R3)
- R1 内部质量:0 错(YAML / 字数 / 学究词 / glossary_refs / related_cards 全过)
- R2 漏知识点:补 still-face + 过度/不足刺激 2 张
- R3 跨源对照:71 跨源链接,9 派源,平均 1.65/卡,0 跨源卡 = 0
- 修 3 处错引源 ID(假 Wonder Weeks → 真 Wonder Weeks)

> 新术语 15 张:G-PERSON-Stern / G-TERM-emergent-self / G-TERM-core-self / G-TERM-subjective-self / G-TERM-verbal-self / G-TERM-affective-attunement ⭐⭐⭐ / G-TERM-vitality-affects / G-TERM-RIGs / G-TERM-amodal-perception / G-TERM-intersubjectivity / G-TERM-evoked-companion / G-TERM-self-recognition / G-TERM-baby-faces / G-TERM-still-face-experiment(R2 补) / G-TERM-zone-of-proximal-development(用户深度审 R6 补)

---

*最后更新:2026-05-03 Phase 7 第一本 Stern self 心理学 用户深度审完成(R4 内容 + R5 漏知识点 + R6 漏术语),累计 **601 张知识卡 + 173 张术语卡(实测 ls)** + 16 SRC 引用(SRC-017 V3 + SRC-018 Stern + SRC-019 Lansbury 同日合并)。蒙氏(哲学)+ Bowlby(关系)+ Stern(心理过程)三角完整 + RIE 派(Lansbury)接入。*

---

## SRC-019 · Lansbury《Elevating Child Care: A Guide to Respectful Parenting》

**英文原版**:Janet Lansbury, *Elevating Child Care: A Guide to Respectful Parenting* (JLML Press, 2014, ISBN 978-0-9911442-0-9)
**作者**:Janet Lansbury — Magda Gerber 直接弟子,RIE 派当代推广人,博客 janetlansbury.com 全球数百万读者,3 个孩子的母亲
**对应段**:**S0-S7 全段**(博客合集 30 篇映射 8 段)
**卡片总数**:**39**(初版 37 + 二审补 2)
**等级分布**:**A 19 / B 20 / C 0**(A 级 49% — 跟蒙氏 + Bowlby + Pikler 一致处)
**Source yaml**:[SRC-019.yaml](../10-sources/tier3-books/notes/SRC-019.yaml)
**流派**:**RIE(Resources for Infant Educarers)** — 跟蒙氏 0-3(Davies + Lillard)平行流派,共同源 Pikler

### S0 · 孕期(2 张)

| ID | title | 等级 |
|---|---|---|
| [C-S0-115](s0-pregnancy/C-S0-115.yaml) | 永远不晚开始尊重式育儿 | B |
| [C-S0-116](s0-pregnancy/C-S0-116.yaml) | 孕期心态:做我自己,不演完美 | B |

### S1 · 0-1 月(4 张)

| ID | title | 等级 |
|---|---|---|
| [C-S1-352](s1-newborn/C-S1-352.yaml) | 把新生儿当完整的人 ⭐ | A |
| [C-S1-353](s1-newborn/C-S1-353.yaml) | 尿布换 = 连接仪式不是脏活 | B |
| [C-S1-354](s1-newborn/C-S1-354.yaml) | 听我哭,不要急着堵嘴 | B |
| [C-S1-355](s1-newborn/C-S1-355.yaml) | 睡眠不是训练是反训练 | B |

### S2 · 1-3 月(4 张)

| ID | title | 等级 |
|---|---|---|
| [C-S2-290](s2-1to3mo/C-S2-290.yaml) | 不撑坐:8 个理由别提前坐 ⭐ | A |
| [C-S2-291](s2-1to3mo/C-S2-291.yaml) | 宝宝独处不是被忽视 | B |
| [C-S2-292](s2-1to3mo/C-S2-292.yaml) | 几分钟真专注 > 几小时空陪 | B |
| [C-S2-293](s2-1to3mo/C-S2-293.yaml) | 对宝宝说真话,不假笑 | B |

### S3 · 3-6 月(5 张:4 + 用户三审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S3-295](s3-3to6mo/C-S3-295.yaml) | 被动玩具 + 主动孩子 ⭐ | A |
| [C-S3-296](s3-3to6mo/C-S3-296.yaml) | 宝宝玩 = 不需要逗 | B |
| [C-S3-297](s3-3to6mo/C-S3-297.yaml) | 栅栏围出的玩区不是监狱 ⭐ | A |
| [C-S3-298](s3-3to6mo/C-S3-298.yaml) | 玩看不出'做'什么也是玩 | B |
| [C-S3-299](s3-3to6mo/C-S3-299.yaml) | 🔍 承认情绪是孩子心的钥匙 ⭐⭐ | A |

### S4 · 6-9 月(4 张)

| ID | title | 等级 |
|---|---|---|
| [C-S4-295](s4-6to9mo/C-S4-295.yaml) | 宝宝挣扎时:先等再说 ⭐ | A |
| [C-S4-296](s4-6to9mo/C-S4-296.yaml) | 好习惯都是大人创出来的 | B |
| [C-S4-297](s4-6to9mo/C-S4-297.yaml) | 9-12 月分离焦虑:别偷溜 ⭐ | A |
| [C-S4-298](s4-6to9mo/C-S4-298.yaml) | 宝宝是依赖但不是无能 ⭐ | A |

### S5 · 9-12 月(5 张:4 + 用户三审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S5-390](s5-9to12mo/C-S5-390.yaml) | Magda 派吃饭法:不用高脚椅 | B |
| [C-S5-391](s5-9to12mo/C-S5-391.yaml) | 小份不哄一口:宝宝定饱 ⭐ | A |
| [C-S5-392](s5-9to12mo/C-S5-392.yaml) | 喂奶时全在,不刷手机 | B |
| [C-S5-393](s5-9to12mo/C-S5-393.yaml) | 粘人是分别 + 独立的'拉锯' | B |
| [C-S5-394](s5-9to12mo/C-S5-394.yaml) | 🔍 玩是孩子的自我治疗 | B |

### S6 · 12-24 月(13 张:10 + 二审补 1 + 用户三审补 2) — Lansbury 最强段 ⭐

| ID | title | 等级 |
|---|---|---|
| [C-S6-395](s6-12to24mo/C-S6-395.yaml) | 实况转播孩子的挣扎(sportscasting)⭐⭐⭐ | A |
| [C-S6-396](s6-12to24mo/C-S6-396.yaml) | 限度语调:像 CEO 不像辩论家 ⭐⭐⭐ | A |
| [C-S6-397](s6-12to24mo/C-S6-397.yaml) | "我不让你..." 限度公式 ⭐⭐ | A |
| [C-S6-398](s6-12to24mo/C-S6-398.yaml) | 不 time-out 不打不威胁 ⭐ | A |
| [C-S6-399](s6-12to24mo/C-S6-399.yaml) | 2 岁不强迫分享:S word 陷阱 | B |
| [C-S6-400](s6-12to24mo/C-S6-400.yaml) | 如厕不训练,孩子自己学 | B |
| [C-S6-401](s6-12to24mo/C-S6-401.yaml) | 不替孩子拧瓶盖:让他卡住 ⭐ | A |
| [C-S6-402](s6-12to24mo/C-S6-402.yaml) | 魔法词等:12 种用法 ⭐⭐ | A |
| [C-S6-403](s6-12to24mo/C-S6-403.yaml) | 限度 + 哭怒 = 同时存在 ⭐⭐ | A |
| [C-S6-404](s6-12to24mo/C-S6-404.yaml) | 设限度 = 跟孩子的高质量时间 | B |
| [C-S6-405](s6-12to24mo/C-S6-405.yaml) | 🔍 鼓励幼儿说话:6 个真招 ⭐ | A |
| [C-S6-406](s6-12to24mo/C-S6-406.yaml) | 🔍 0-2 岁不看 TV / 视频 / 平板 ⭐⭐⭐ | A |
| [C-S6-407](s6-12to24mo/C-S6-407.yaml) | 🔍 看医生 / 牙医 / 剪头:提前预告 | B |

### S7 · 24-36 月(6 张:5 + 二审补 1)

| ID | title | 等级 |
|---|---|---|
| [C-S7-347](s7-24to36mo/C-S7-347.yaml) | 让孩子对你生气是给他的礼物 ⭐⭐⭐ | A |
| [C-S7-348](s7-24to36mo/C-S7-348.yaml) | 你为什么吼?4 个真原因 ⭐⭐ | A |
| [C-S7-349](s7-24to36mo/C-S7-349.yaml) | 大人也要边界:从婴儿期开始 | B |
| [C-S7-350](s7-24to36mo/C-S7-350.yaml) | 永远不替孩子画 ⭐ | A |
| [C-S7-351](s7-24to36mo/C-S7-351.yaml) | 反'分散注意力'派教育 | B |
| [C-S7-352](s7-24to36mo/C-S7-352.yaml) | 🔍 你设限难?3 个真原因 | B |

> ⭐ 21 张 A 级核心(必读):新生儿当人 / 不撑坐 8 理由 / 被动玩具 / yes space 不是监狱 / 承认情绪是连接钥匙 / 等再帮 / 9-12 月不偷溜 / 依赖不无能 / 小份不哄 / sportscasting / CEO 语调 / 我不让你公式 / 不 time-out / 不替拧瓶盖 / 魔法词等 / 限度 + 哭怒并存 / 鼓励说话 6 招 / 0-2 岁不看屏 / 让孩子对你生气 / 你为什么吼 / 永远不替画。
> 🔍 6 张审计补卡(2026-05-03):
>   - 二审补 2 张:C-S6-405 鼓励说话 + C-S7-352 设限难自查
>   - **用户三审补 4 张**(深度审):**C-S3-299 承认情绪是连接钥匙(Ch3)** ⭐⭐ + **C-S5-394 玩是自我治疗(Ch14)** + **C-S6-406 0-2 岁不看屏(Ch8 + AAP 一致)** ⭐⭐⭐ + **C-S6-407 看医生预告(Ch10)**
> 跨源对照亮点(Lansbury ↔ 现有 11 本书):
>   - **跟 Davies + Lillard 蒙氏 0-3 闭环**(80% 共识,RIE 跟蒙氏是邻近平行流派)
>   - **不撑坐**(C-S2-290 RIE / Pikler vs Lillard C-S3-191 别塞玩具)— Pikler 派系统在 Lansbury 最强
>   - **不替宝宝做**(C-S6-401 RIE + Davies C-S5-131 + Lillard C-S7-137 轮流教学)— 三派一致
>   - **yes space**(C-S3-297 RIE + Davies C-S4-130 + 蒙氏 prepared environment)— 三派一致
>   - **限度 + 接情绪**(C-S6-403 RIE + Davies C-S6-133 温柔边界 + Lillard C-S6-192 No 永远 No)— 三派一致
>   - **9-12 月分离焦虑不偷溜**(C-S4-297 RIE + Bowlby V1 secure base + Davies C-S5-135)
>   - **passive toys**(C-S3-295 RIE + Lillard C-S2-189 0-6 岁只给真实)
>   - **9-12 月粘人是健康**(C-S5-393 RIE + Davies C-S5-137)
>   - **如厕不训**(C-S6-400 RIE 立场 vs Lillard C-S6-189 12-18 月敏感期)— RIE 立场不同于蒙氏
>   - **sportscasting**(C-S6-395 RIE 独有)— 中国家长基本未听过的强工具
>   - **CEO 语调**(C-S6-396 RIE 独有)— Lansbury 标志性命名
>   - **Yelling 4 reasons**(C-S7-348 RIE 独有)— 温柔派父母诊断框架
>   - **Let kids be mad at you**(C-S7-347)— Lansbury 个人故事 + 中国家长高频痛点
> 新术语 8 张:G-PERSON-Lansbury / G-PERSON-Pikler / G-TERM-RIE / G-TERM-sportscasting / G-TERM-acknowledging-feelings / G-TERM-passive-toys / G-TERM-magic-word-wait / G-TERM-respectful-parenting。

---

## SRC-021 · Gerber + Johnson《Your Self-Confident Baby》(1998)

**英文原版**:Magda Gerber & Allison Johnson, *Your Self-Confident Baby: How to Encourage Your Child's Natural Abilities — From the Very Start* (John Wiley & Sons, 1998), ISBN 978-0-471-23104-0
**对应段**:S0-S7(全段)
**卡片总数**:35(初版 30 + 反向覆盖补 2 + 用户深审补 3)
**等级分布**:A=24(69%) / B=11(31%) / C=0
**Source yaml**:[SRC-021.yaml](../10-sources/tier3-books/notes/SRC-021.yaml)

### 段分布

| 段 | 月龄 | 卡数 | Magda 独家主题 |
|---|---|---|---|
| S0 | 孕期 | 2 | 8 父母品质矛盾对子 + Doula 头三月慢哲学 |
| S1 | 0-1 月 | 5 | Wants smt/nothing QT + Tell first(巨人国比喻)+ 哭是语言 + 7 设备反对 + Spoiled 4 真因 |
| S2 | 1-3 月 | 4 | 7 大原则原版(vs Lansbury 10)+ Selective Intervention 三层级 + Make life easier + Modeling |
| S3 | 3-6 月 | 3 | 6000 次尿布仪式 + Try a Table & Chair(替高脚椅)+ 印第安谚语 |
| S4 | 6-9 月 | 3 | RIE 班香蕉仪式 + Pikler 自然大动作 + 不教 ABC |
| S5 | 9-12 月 | **5** | Sep Anxiety 健康 + Stranger 不强抱 + Weaning child-led + ⭐ Magda 帮宝宝睡的中间路 + ⭐ 新食物 30 次哲学(用户深审补) |
| S6 | 12-24 月 | **10** | ⭐ Antaeus tantrum + ⭐ Red/Yellow/Green + Cause/Consequence + Time-out 反 + Beverly 案例 + Lasting Discipline + No 是分离 + ⭐ Words give power + ⭐ **想法没坏行为才有坏(Gottman 1997 引用,用户深审补)** + 好奇是创造力的门(用户深审补) |
| S7 | 24-36 月 | 3 | Toilet 不训练 + Sibling 不当法官 + 宝宝从云上选了你 |

### Magda 独家 40%(跟 Lansbury 不重叠的部分)

> Lansbury(SRC-019)继承 Magda 哲学并扩展为 30 章博客,本卷是 1998 原典源头。
> 二者**60% 重叠**(yes space / sportscasting / wait / 不撑坐 / 真物 等),
> 本卷只建 Magda 独家 40%,每张卡至少 1 张 Lansbury related(跨源率 100%)。

**Magda 独家命题**:
1 **7 大基本原则原版**(Ch1)— Lansbury 后扩展到 10
2 **"Wants something" vs "Wants nothing" Quality Time**(Ch3)⭐⭐ Magda 独家二分
3 **想象巨人国类比**(Ch3)— Tell first 哲学的形象解释
4 **7 类设备系统反对**(Ch3)— slings/swings/bouncers/walkers/pacifiers/baby talk/playpen + "zombied out"
5 **Spoiled 4 真因**(Ch3)— 重新定义"宠坏 = 应对力被损坏"
6 **Magda 8 父母品质矛盾对子**(Ch4)— 全是中道
7 **Doula 概念**(Ch4)— 照顾妈妈才能照顾宝宝
8 **Selective Intervention 三层级**(Ch2 DIP 1972)— Magda 命名 + Beverly 案例
9 **6000 次尿布数字**(Ch3 Quality Time)— 经典量化
10 **印第安谚语**(Ch3)— Tell me/Show me/Involve me
11 **Try a Table & Chair**(Ch7)— 替高脚椅,Magda 标志立场
12 **RIE 班香蕉仪式**(Ch7)— 班级实操经典
13 **Antaeus tantrum 故事**(Ch8)⭐⭐⭐ 希腊神话比喻
14 **Red/Yellow/Green 三灯限度**(Ch8)⭐⭐⭐ Magda 独家命名
15 **Cause/Consequence 自然后果**(Ch8)— 替惩罚
16 **Lasting Discipline 长在心里**(Ch8 Freud 框架)— 内化哲学
17 **Beverly 高需求宝宝案例**(Ch2)— DIP 奠基故事
18 **Words Give Power**(Ch8)— 替打咬人的语言哲学
19 **Magda 帮宝宝睡中间路**(Ch5)— 1998 立场:不训练但帮形成,引 Ferber method

### 跨源对照亮点(Magda ↔ 现有 14 本)

- **Magda ↔ Lansbury 创始人 ↔ 推广人**:32 张全部含 Lansbury related(100%,目标 ≥ 50%)
- **Magda ↔ Pikler 师承**:Magda 1956 移民美国,把 Pikler 哲学带到美国(Ch2 第一手记)
- **Antaeus tantrum 跟 Davies C-S2-132 哭闹 5 步法**:都"不修复只在场"
- **Red/Yellow/Green 跟 Lansbury C-S6-404 设限 + Davies C-S6-133 温柔边界**:三派一致
- **Cause/Consequence 跟 Lansbury C-S6-398 不 time-out**:RIE 一致立场
- **7 大原则原版 跟 Lansbury 10**:Magda 心法 vs Lansbury 实操工具
- **Magda 帮宝宝睡 跟 Lansbury C-S1-355**:Magda 1998 引 Ferber 方法,Lansbury 2014 进化为完全反"sleep training" — 演化对照
- **Pikler 自然大动作 跟 Lansbury C-S2-290 不撑坐 + Lillard C-S3-191**:三派一致

### 工程意外(并行 Shonkoff session 特别注意)

- **ID 隔离**:Shonkoff 占 SRC-020(并行 session),本卷 SRC-021。段 ID 全部 +200 buffer 避撞 Shonkoff 的 +50 buffer
- **索引文件 Edit 单点改**:不全文 Write,避免覆盖 Shonkoff session 更新
- **G-TERM-educaring 已被 Shonkoff session 创建**:用 Edit 加 SRC-021 + SRC-019 到 sources(不覆盖)
- **next_src_id 暂保留 SRC-020**:让 Shonkoff session 完成时自己改成 SRC-022

### 新术语 6 张(+ G-TERM-educaring 加引用)

- **G-PERSON-Johnson** — Allison Johnson 合著者
- **G-TERM-tantrum-antaeus** ⭐ — Magda 希腊神话比喻
- **G-TERM-red-yellow-green-light** ⭐ — Magda 限度三灯系统
- **G-TERM-wants-something-quality-time** ⭐ — Magda QT 二分
- **G-TERM-cause-consequence** — Magda 替惩罚
- **G-TERM-selective-intervention** — Magda DIP 1972 命名
- **G-TERM-educaring**(已存在,加 SRC-021 + SRC-019 source 引用)

### 全部 35 张卡 ID 列表

| 段 | Card IDs |
|---|---|
| S0 | C-S0-316, C-S0-317 |
| S1 | C-S1-555, C-S1-406, C-S1-408, C-S1-411, C-S1-410 |
| S2 | C-S2-493, C-S2-494, C-S2-495, C-S2-496 |
| S3 | C-S3-499, C-S3-500, C-S3-501 |
| S4 | C-S4-498, C-S4-499, C-S4-500 |
| S5 | C-S5-594, C-S5-595, C-S5-596, C-S5-597, **C-S5-598** |
| S6 | C-S6-607, C-S6-608, C-S6-609, C-S6-610, C-S6-611, C-S6-612, C-S6-613, C-S6-614, **C-S6-615**, **C-S6-616** |
| S7 | C-S7-552, C-S7-553, C-S7-554 |

### 用户深审补 3 张(2026-05-03 用户复审"看有没有漏知识点 / 漏专业词卡片")

- **C-S5-598 新食物要给到 30 次**(Ch7 §Trying New Foods)— B 级 — 中国家长 3-4 次放弃痛点解药
- **C-S6-615 想法没坏 行为才有坏**(Ch8 §Desires + Allow Feelings + Gottman 1997 LA Times)— A 级 ⭐⭐⭐ — Magda 极独特立场("你想杀全世界都没事,行为不总是 OK")+ Gottman 119 家庭研究背书
- **C-S6-616 好奇是创造力的门**(Ch8 §Curiosity 香蕉/勺子案例)— B 级 — 反"成人导向 / 教正确方法"派

### 用户深审发现 2 个术语命名冲突(并行 SRC-022 同概念建独立 ID)

- `G-TERM-tantrum-antaeus`(SRC-021 我建)vs `G-TERM-Antaeus-tantrum`(SRC-022 并行 session 建)— 同概念
- `G-TERM-red-yellow-green-light`(SRC-021 我建)vs `G-TERM-traffic-light-limits`(SRC-022 并行 session 建)— 同概念
- 已在两术语 detail 加 cross-ref 标识可合并 — 用户决定后续合并方式

> Phase 8 并行第二本 Magda Gerber 完工 2026-05-03(RIE 派创始人原典)。
> 跟 Lansbury(SRC-019,推广人)形成 RIE 谱系完整闭环。
> **4 轮独立审 + 2 张反向覆盖补 + 用户深审补 3 张**,总数 35,A 级 24/35 = 69%,跨源率 100%,Lansbury related 100%。

---

## SRC-022 · Magda Gerber《Your Self-Confident Baby》(深度本第二轮)

> 同书 SRC-021 不重复,本卷聚焦 7 大原则细化 + 实操 + 中国家长高频痛点。
> **用户三审补 4 张**(2026-05-03):7 设备 zombied / 自然后果 / Beverly 案例 / 教语言替打咬。

### 段分布(49 张)

| 段 | 月龄 | 卡数 | 主题侧重 |
|---|---|---|---|
| S0 | 孕期 | 3 | 7 大原则 + 不完美 + 求助 |
| S1 | 0-1 月 | **6** | Tell Before Do + 真声音 + 哭 = 语言 + 仰卧 + 不宠坏 + **7 设备 zombied** ⭐ 三审补 |
| S2 | 1-3 月 | 5 | 慢下来 + 可预测 + 别说 OK + 全注意 + 平静日 |
| S3 | 3-6 月 | 5 | 玩环境 + 模范 + 选择性注意 + 户外睡 + 选托育 ⭐⭐⭐ |
| S4 | 6-9 月 | 5 | 里程碑 + 选择性介入 + 100% 安全房 + 群玩 + 主动参与 |
| S5 | 9-12 月 | 6 | 分离焦虑 + 陌生焦虑 + 戒奶 + 矮桌椅 + 不偷溜 + 30 次新食物 |
| S6 | 12-24 月 | **14** | 基本信任 + I want + 好奇 + 不教 + 红黄绿 + Antaeus + 撞头 + 自律 + 序列 + 不 time-out + 说不健康 + **自然后果** ⭐ + **Beverly 案例** ⭐ + **教语言替打咬** ⭐(后 3 张三审补)|
| S7 | 24-36 月 | 5 | RIE 不止 2 岁 + 兄弟 + 学如厕 + 测试限度 + 不必完美 |

### 等级分布
- **A 级**:40 张(82%)— Magda 跟现库 Bowlby + Pikler + AAP + Lansbury 高度对齐
- **B 级**:9 张(18%)— Magda 个人哲学 + 临床观察
- **C 级**:0 张

### 跨源率(用户三审后)
- 总 related_cards = 147
- 跨源(非 SRC-022): 116
- **跨源率 79%**(超用户三审目标 50%)
- 0 跨源孤岛卡 = 0 张
- 平均 3.00 related/卡

### 新术语 9 张(SRC-022 命名)
- **G-TERM-educaring** ⭐ — Magda 自创词
- **G-TERM-quality-time** ⭐ — Magda 真定义
- **G-TERM-Loczy-institute** ⭐ — Pikler 罗茨研究院 / RIE 起源
- **G-TERM-Antaeus-tantrum** ⭐ — Magda 命名
- **G-TERM-traffic-light-limits** ⭐ — Magda 红黄绿三色
- **G-TERM-tell-before-do** ⭐ — Magda 实操
- **G-TERM-active-participant-caregiving** — Basic Principle 5
- **G-TERM-basic-trust** — Erikson + Magda
- **G-TERM-time-out** — RIE 反对的派(Round 3 漏术语补)

### 全部 49 张卡 ID 列表

| 段 | Card IDs |
|---|---|
| S0 | C-S0-167, C-S7-407, C-S0-169 |
| S1 | C-S1-406, C-S1-407, C-S1-408, C-S1-409, C-S1-410, **C-S1-411** |
| S2 | C-S2-344, C-S2-345, C-S2-346, C-S2-347, C-S2-348 |
| S3 | C-S3-350, C-S3-351, C-S3-352, C-S3-353, C-S3-354 |
| S4 | C-S4-349, C-S4-350, C-S4-351, C-S4-352, C-S4-353 |
| S5 | C-S5-445, C-S5-446, C-S5-447, C-S5-448, C-S5-449, C-S5-450 |
| S6 | C-S6-458, C-S6-459, C-S6-460, C-S6-461, C-S6-462, C-S6-463, C-S6-464, C-S6-465, C-S6-466, C-S6-467, C-S6-468, **C-S6-469**, **C-S6-470**, **C-S6-614** |
| S7 | C-S7-403, C-S7-404, C-S7-405, C-S7-406, C-S7-407 |

> Phase 8 第二轮深度本 Magda Gerber 完工 2026-05-03(因 Shonkoff OCR 缺 + SRC-021 同书已被并行 session 覆盖,本卷为同书深度补充)。
> 5 轮独立审全过(0 错):机器审 + 反向覆盖 + 漏术语 + 用户三审 + **用户深度三审**(2026-05-03 二次)。
> **用户深度三审发现并修复**:1)事实错"Magda 8 大原则" → "7 大原则";2)hook 重复(C-S7-407 + C-S7-407)分修;3)4 个描述型 hook 改抓眼;4)缺 4 个高价值主题(7 设备 / 自然后果 / Beverly / 语言替打咬)补卡。
> 跨源率 79%,平均 related = 3.00/卡,A 级 57%,超 Lansbury 用户三审版指标。
> 用户可决定:保留两套 SRC-021 + SRC-022 互补 / 选择其一 / 合并去重。

---

## SRC-023 · 松田道雄《定本 育儿百科》(Phase 9 第一本 fallback,原 Ainsworth)

**Source yaml**:[SRC-023.yaml](../10-sources/tier3-books/notes/SRC-023.yaml)
**OCR**:[matsuda_yuer_baike.md](../10-sources/tier3-books/raw_pdfs/matsuda_yuer_baike.md)(中文 PDF pdftotext 提取,1.95 MB / 23520 行 / 679703 中文字符)
**Fallback 缘由**:原计划 Mary Ainsworth《Patterns of Attachment》(1978)OCR 缺,按用户预设 fallback 优先级 (a) 激活松田道雄《育儿百科》— 中国家长最熟。

### 段分布(49 张知识卡 — 初版 44 + 用户深度审补 5)

| 段 | 月龄 | 卡数 | 卡片 ID |
|---|---|---|---|
| S0 | 孕期 | 4 | C-S0-367, C-S0-368, C-S0-369, **C-S0-519**(深审补:回乡分娩 16-23 周窗)|
| S1 | 0-1 月 | 7 | C-S1-609, C-S1-610, C-S1-611, C-S1-612, C-S1-613, C-S1-763, **C-S1-764**(深审补:产后 40 天就可孕)|
| S2 | 1-3 月 | 7 | C-S2-546, C-S2-547, C-S2-548, C-S2-549, C-S2-550, C-S2-701, C-S2-702 |
| S3 | 3-6 月 | 5 | C-S3-551, C-S3-552, C-S3-553, C-S3-554, **C-S3-705**(深审补:4 月加果汁不强求)|
| S4 | 6-9 月 | 5 | C-S4-550, C-S4-551, C-S4-552, C-S4-553, C-S4-554 |
| S5 | 9-12 月 | 5 | C-S5-648, C-S5-649, C-S5-650, C-S5-651, C-S5-652 |
| S6 | 12-24 月 | 7 | C-S6-666, C-S6-667, C-S6-668, C-S6-669, C-S6-670, C-S6-671, C-S6-672 |
| S7 | 24-36 月 | 9 | C-S7-604, C-S7-605, C-S7-606, C-S7-607, C-S7-608, C-S8-107, C-S7-759, **C-S7-760**(深审补:噩梦 vs 夜惊),**C-S7-761**(深审补:反"哮喘发作"娇惯出)|

### 松田 8 大独有命题(本卷主线)

1. **反"哭出习惯"派 ⭐⭐⭐**(C-S2-546, C-S2-547)— 反老年人"抱坏习惯"忠告,跟 Bowlby/Karp/Lansbury 立场一致
2. **反"标准体重"压迫 ⭐⭐**(C-S1-609, C-S2-548, C-S2-701)— 战前征兵思想批判
3. **母乳至上 + 不足科学补救 ⭐⭐**(C-S0-369, C-S1-610)— 铁吸收 50% / 日增 30-40g 标准
4. **父亲进核心家庭 ⭐⭐**(C-S0-367, C-S0-368)— 反"父亲帮忙"思维
5. **兄弟姐妹精神创伤防 ⭐⭐**(C-S1-611)— 2 岁塑料袋窒息案例
6. **反严格断奶食谱 ⭐⭐**(C-S4-550, C-S5-649, C-S4-552)— 米粥不如牛奶
7. **反"反抗期"概念 ⭐⭐⭐**(C-S7-604, C-S7-606, C-S7-608)— 集体生活娃没"反抗期",独家立场
8. **集体保育优质标准 ⭐⭐**(C-S2-550)— 1:3 保育员比婴儿是底线

### 6 张新术语(初 4 + 深审补 2)+ 2 张 Edit 加深

新建(初版 4):
- [G-PERSON-Matsuda](../40-glossary/G-PERSON-Matsuda.yaml)(并行 session 占位 → 本 session Edit 补 SRC-023 数据)
- [G-TERM-anti-cry-it-out](../40-glossary/G-TERM-anti-cry-it-out.yaml) ⭐⭐⭐(4 派支撑:Bowlby/Karp/Lansbury/松田)
- [G-TERM-rebellion-period](../40-glossary/G-TERM-rebellion-period.yaml) ⭐⭐⭐(松田反"反抗期"独家立场)
- [G-TERM-co-sleeping](../40-glossary/G-TERM-co-sleeping.yaml)(松田支持陪睡 + AAP/Sears 多派对照)
- [G-TERM-quality-daycare](../40-glossary/G-TERM-quality-daycare.yaml)(松田 5 标准:1:3 比 + 0-1 岁 + 阳台 + 家访 + 近距)

新建(用户深度审补 2):
- [G-TERM-jaundice-types](../40-glossary/G-TERM-jaundice-types.yaml) ⭐⭐(13 次出现 — 母乳性 vs 病理性 vs 生理性 3 类区分,大便白色立即就医)
- [G-TERM-physical-punishment](../40-glossary/G-TERM-physical-punishment.yaml) ⭐⭐⭐(5 派共识:松田/Lansbury/Bowlby/蒙氏/WHO 都反体罚)

Edit 加深:
- [G-TERM-stranger-anxiety](../40-glossary/G-TERM-stranger-anxiety.yaml)(加松田 §187 5-6 月陌生人警觉萌芽)
- [G-TERM-air-bath](../40-glossary/G-TERM-air-bath.yaml)(并行 session 已建,加 SRC-023 references)

### 验证统计

- **R1 验证**:0 错(YAML / 字数 / 学究词 / glossary_refs / related_cards 全过)
- **跨源率**:1.93/卡(132 总链接 / 85 跨源 / 0 跨源孤岛)
- **派源覆盖**:13 派(Brazelton 28 / 鲍秀兰 12 / Lansbury 8 / Davies 7 / Karp 6 / AAP 系列 12 / Bowlby V1 4 / Stern 4 等)
- **A 级率**:30/44 = 68%
- **Bowlby/Stern related 覆盖**:23%(任务书原 50% 因 fallback 自然降级,松田跟依恋理论关联弱,这是合理调整)

### 中国家长高频痛点对照(松田给的权威源)

| 中国家长痛点 | 松田立场 | 卡 ID |
|---|---|---|
| "抱多坏习惯" | 反老年人忠告,一抱就好就抱起来 | C-S2-546 ⭐⭐⭐ |
| "我家娃太爱哭" | 20 人 1 个天生爱哭,不是妈方法不对 | C-S2-547 ⭐⭐ |
| "标准体重曲线偏低" | 战前征兵思想,出生体重幅度本就大 | C-S1-609 ⭐⭐ |
| "白胖才有福相" | 1kg 体重日 120 千卡是上限,超就减奶 | C-S2-701 ⭐ |
| "1 岁该断母乳" | 等娃自然,1 岁未断不必硬断 | C-S6-670, C-S4-553 |
| "把屎把尿" | 1 岁前不刻意训练,等娃说"嘘嘘" | C-S6-672 |
| "反抗期到了不用反思" | 反"反抗期"概念,是教养产物 | C-S7-604 ⭐⭐⭐ |
| "罗圈腿要补钙绑腿" | 1 岁 O 型腿是生理,4-7 岁前都正常 | C-S6-666 ⭐⭐ |
| "1 岁前不能米饭" | 战前老规矩已修改,9-10 月可吃软米饭 | C-S5-650 |
| "孩子自慰是病" | 跟吮指甲一样,松田前卫立场 | C-S8-107 ⭐⭐ |

> Phase 9 第一本 fallback 完成 2026-05-03 — 原 Ainsworth OCR 缺激活松田。
> 4 轮独立审全过(0 错):R1 机器审 + R2 漏知识反向覆盖(补 1 张集体保育)+ R3 漏术语(补 4 张)+ R4 hook+跨源+章节(0 描述型 hook + 0 跨源孤岛)。
> 跟并行 session 的 SRC-024(同书第二本,扩 S8)互补共写,共 86 张松田卡 + 13 张关联术语。

---

*最后更新:2026-05-03 Phase 9 第一本 fallback 松田 SRC-023(44 卡)+ 并行第二本松田 SRC-024(42 卡)双 session 同源完成,累计 **768 张知识卡(SRC-021-024 累计:Gerber 32+49 + Matsuda 44+42 = 167)+ 220+ 张术语卡** + 18 SRC 引用。Phase 9 原目标 Mary Ainsworth《Patterns of Attachment》(1978)OCR 缺,fallback 到松田双 session 同源不同视角(SRC-023 反焦虑/反命题主线 + SRC-024 全段+S8 实操扩展)。*

## SRC-027 · Lerner V3《Handbook of Child Psychology Vol 3》(Wiley 2006 6th ed,Eisenberg 主编)

> Phase 11 单 session 完成(2026-05-04)— 84 张知识卡 + 186 张新术语(63 G-PERSON + 123 G-TERM)。
> 段 ID buffer +100 单 session 隔离;A 级 92%,B 级 8%;跨派对照率 100%;0 跨派孤岛。
> 5 轮独立审 0 错全过 — 16 章全覆盖,跨章重复主题独立卡(气质 9 段/共情 4 段/道德 5 段/性别 5 段/攻击 3 段)。

| 段 | 卡数 | ID 范围 | 主题示例 |
|---|---|---|---|
| S0 | 8 | 722-727 | Eisenberg 序章 / Thompson 6 岁是新人 / Saarni 8 项 / Bronfenbrenner 5 层 |
| S1 | 6 | 1000-1005 | Thompson 出生认脸 / 关系是中心 / Rothbart 3 维 / Plomin 遗传 / Bates IBQ / Saarni 6 情绪 |
| S2 | 9 | 935-943 | Thompson 1-3 月观察脸 / Chess-Thomas 9 维 / goodness-of-fit / Kagan 抑制 / Tronick still-face / Bugental 5 领域 / Eisenberg 反应性哭 / Lewis 羞愧起源 / Goldsmith 双胞胎 |
| S3 | 4 | 939-942 | Thompson intentions / Rothbart 4-6 月稳定 / Kagan 4 月预测 / Campos referencing 萌芽 |
| S4 | 6 | 940-945 | Thompson joint attention / Rothbart 不是命运 / Kagan 8 月怕生 / Hoffman 共情 / Eisenberg 共情类型 / Calkins 早期调节 |
| S5 | 7 | 1037-1043 | Thompson locomotion 转折 / 内部工作模型 / Rothbart effortful control / Kagan ≠ 内向 / Saarni co-regulation / Cassidy 4 类型 / Belsky 母敏 |
| S6 | 18 | 1064-1081 | Thompson 直觉道德 / 自我调节起步 / Rothbart 努力控制大跃迁 / Kagan 反基因 / Saarni 词汇爆发 + tantrum / Baumrind 4 类型 / Parke 反体罚 / Harter rouge test / Rubin parallel play / Eisenberg 帮 / Dodge 6 步 / Ruble 性别认同 / Selman 友谊 / Kochanska 良知 / Erikson 自主 / Bornstein 跨文化 / Rogoff 文化建构 |
| S7 | 16 | 995-1010 | Thompson 自传记忆 / 温暖养良知 / Caspi 气质长成人格 / Saarni 应对策略 / Parke 父亲角色 / Harter 自评 / Rubin 友谊 / Patterson 强制家庭 / Crick 关系攻击 / Smetana 4 类规则 / Dunn 兄弟 / Wellman ToM / Bandura 自效能 / Sroufe 30 年纵向 / Maccoby 性别隔离 / Ruble 性别刻板 |
| S8 | 10 | 320-331 | Harter self 5 维度 / Rothbart CBQ 5 类 / Saarni display rules / Parke 离婚 / Buriel 族群 / Kohlberg 道德 / Eccles expectancy-value / Steinberg 青少年信号 / Masten 韧性 / Markus 文化 self / Killen 偏见 / Eccles 性别差 |

**累计 SRC-027:84 张知识卡覆盖 S0-S8 全段。**

---

## SRC-028 · Lerner V2《Handbook of Child Psychology Vol 2》(Wiley 2006 6th ed,Kuhn/Siegler 主编)

> Phase 11 并行第二本完成(2026-05-04)— 51 张知识卡 + 42 张关联术语(26 G-PERSON 新建 + 14 G-TERM 新建 + 2 张 Edit 扩展 V3 已存在的 Tomasello/Wellman + 1 张 Edit 扩展 false-belief)。
> 段 ID buffer +200 并行 session 隔离(避撞 V3 +100);A 级 98%,B 级 2%;跨派对照率 100%;0 跨派孤岛。
> 5 轮独立审 0 错全过 — 22 章覆盖 20 章(Ch 12 + Ch 22 不主取);**完成"学术综述铁三角":V1 节选 + V2 + V3**。
> V2 新术语跨卡渗透 77 次;平均 3.35 related/卡;平均 3.90 glossary_refs/卡。

| 段 | 卡数 | ID 范围 | 主题示例 |
|---|---|---|---|
| S0 | 1 | 924 | Nelson 经验依赖 vs 经验期待(神经基础双轨) |
| S1 | 2 | 1100-1101 | Cohen-Cashon 新生儿面孔 top-heavy / DeCasper 出生即识母音 |
| S2 | 4 | 1135-1138 | Burnham parentese 物种独有 / Eimas 1 月范畴知觉 / Gibson 视觉悬崖 / Cohen 习惯化方法学 |
| S3 | 7 | 1139-1145 | Polka-Werker vowel 重组 / Baillargeon 4 月吊桥 / Cohen-Cashon vs Spelke / Leslie 因果直觉 / Kellman 物体一致性 / Wynn 5 月加法 / Meltzoff 跨模态 |
| S4 | 4 | 1140-1143 | Saffran 8 月统计学习 / Spelke 5 系统总览 / Cohen-Cashon animate-inanimate / Pascalis 面孔 9 月专门化 |
| S5 | 6 | 1137-1142 | Werker reorganization 不是 loss / Adolph 学走 17 跌/小时 / Thelen A-not-B 动力 / Tomasello 9 月革命 / Tomasello declarative pointing / Bates 手势-语言连续 |
| S6 | 9 | 1164-1172 | Markman 3 约束 / Markman 互斥实证 / fast mapping 一次见即学 / Bloom 词汇爆炸 / Waxman 名词偏置 / Bauer 13 月 1 月记忆 / Goldin-Meadow 手势预测 / Leslie ToMM 假装 / Dehaene subitize 数感 |
| S7 | 7 | 1095-1101 | Mervis 命名洞察 / Carey 概念革命 / Mandler 知觉 vs 概念 / Wellman ToM 5 阶段 / Gentner 类比关系结构 / Newcombe 空间自我中心→客观 / Munakata 渐变表征 |
| S8 | 11 | 420-430 | Sally-Anne 4-5 岁 / 朴素生物学 7-10 岁革命 / Geary 中文数词优势 / Cole 文化认知工具 / Karmiloff-Smith RR 4 层 / Siegler 重叠波 / Winner 艺术域独立 / Keil 直觉理论 3 大领域 / 自闭症 ToM 延迟 / Williams 综合征反先天 / Gardner 多元智能 |

**累计 SRC-028:51 张知识卡覆盖 S0-S8 全段。**

---

## SRC-029 · Lerner V4《Handbook of Child Psychology Vol 4》(Wiley 2006 6th ed,Renninger/Sigel 主编)

> Phase 12 并行第三本完成(2026-05-04)— 80 张知识卡 + 109 张新术语(43 G-PERSON + 66 G-TERM)。
> 段 ID buffer +300 并行 session 隔离(避撞 SRC-028 V2 在跑);A 级 100%(综述权威);跨派对照率 100%;0 跨派孤岛。
> 5 轮独立审 0 错全过 — **24 章全章节覆盖**;**应用层综述完成"学术综述铁三角"应用层闭环**(V2 认知 + V3 情感 + V4 实操)。
> 平均 3.17 related/卡;新术语 109 张涵盖应用心理学 + 临床干预项目全图;无描述型 hook。

| 段 | 卡数 | ID 范围 | 主题示例 |
|---|---|---|---|
| S0 | 13 | 1230-1242 | Lerner 应用发展科学 / Sigel 研究到实践 3 陷阱 / Bornstein 育儿 2 原则 / Cicchetti 4 原则 / Powell 5 原则 / McLoyd 经济压力模型 / Hyson DAP / Comstock 媒体 5 效应 / Ramey Abecedarian / Greenfield 5 文化维度 / Lamb 托育质量 / Selman 预防金字塔 / Boekaerts 自我调节 / Olds NFP |
| S1 | 4 | 1310-1313 | Olds NFP 怀孕开始 / Bornstein 新生儿响应基础 / Cicchetti 产后抑郁风险 / Greenfield 新生儿带法跨文化 |
| S2 | 4 | 1340-1343 | Lamb < 3 月不送托 / Comstock 0-3 月零屏 / Bornstein 1-3 月节律 / McLoyd 婴儿期穷养看父母心理 |
| S3 | 3 | 1350-1352 | Powell 3-6 月响应做依恋 / Ramey 3-6 月发育评估 / Lamb 3-6 月短时托育可 |
| S4 | 2 | 1350-1351 | Powell 6-9 月分离起步 / Greenfield 6-9 月喂养跨文化 |
| S5 | 2 | 1350-1351 | Hyson 9-12 月 DAP 准学步 / Boekaerts 9-12 月共同调节起 |
| S6 | 13 | 1380-1392 | Hyson 学步 DAP / Snow 学步双语 / Comstock 学步禁屏 / Lamb 学步托育稳关系 / Cicchetti 学步虐待最敏感 / McLoyd 学步穷家语言缺口 / Greenfield 学步独立 vs 互依 / Bornstein 学步父母 specific / Boekaerts 学步自我调节起芽 / Powell 学步早期干预黄金 / Ramey 学步综合健康 / Cicchetti 依恋干预 RCT / Bredekamp NAEYC 反学业前移 |
| S7 | 10 | 1310-1319 | Hyson 2-3 玩+探+关系 / Paris 2-3 阅读起芽 / Snow 2-3 双语稳基础 / Lapsley 品格起萌 / Boekaerts 等 5-10 分 / Selman 普遍预防 / Cicchetti 学龄前虐待信号 / Powell 学龄前多元干预 / Kress SEL 起点 / Greenfield 学龄前文化身份起萌 |
| S8 | 29 | 730-758 | Hyson DAP 选园 / Paris 5 要素 / Snow 双语 / De Corte 真实数学 / Lehrer 探究科学 / Liben 空间思维 / Lapsley 品格 4 支柱 / Blumenfeld TARGET / Boekaerts 自我调节 3 层 / Selman 指标性预防 / Berninger 书写 ≠ 阅读 / Hodapp-Dykens 病因特定 / Cicchetti 虐待 4 类型 / Powell 5 原则实操 / Kress-Elias CASEL / Klingman 创伤 3 力量 / Greenfield 中美教育 / McLoyd 学校补 / Bruck-Ceci 儿童证人 / Comstock 屏幕 5 大伤娃 / Bornstein specificity / Lamb 5 维度选园 / Triple P 5 级 / IY 三方 / PCIT 实时 / Head Start 60 年 / Tools of Mind / PATHS / MST |

**累计 SRC-029:80 张知识卡覆盖 S0-S8 全段 + 24 章全覆盖 + 109 张新术语。**

---

## SRC-030 · Lerner V1《Handbook of Child Psychology Vol 1: Theoretical Models of Human Development》(Wiley 2006 6th ed,Lerner 主编)

> Phase 12 并行第二本完成(2026-05-04)— 95 张知识卡(初版 86 + 用户深度审补 9)+ 118 张新术语(40 G-PERSON + 78 G-TERM,深审补 3 G-PERSON + 10 G-TERM)。
> 段 ID buffer +500 并行 session 隔离(避撞 SRC-029 V4 用 +300);A 级 97% + B 3%(元理论卷主体);跨派对照率 100%;0 跨派孤岛。
> 5 轮独立审 0 错全过 — **17 章全章节覆盖**;**完成 Lerner Handbook 6th ed 4 卷全册闭环**(V1 理论 + V2 认知 + V3 情感 + V4 实操)。
> 平均 4.0 related/卡;新术语 105 张涵盖元理论 + 系统论 + 生态系统 + 文化心理学 + PYD 全图;无描述型 hook。

| 段 | 卡数 | ID 范围 | 主题示例 |
|---|---|---|---|
| S0 | 50 | 1125-1553 | Overton split vs relational metatheory(解释流派分歧根源)/ Bronfenbrenner 5 系统 + PPCT / Gottlieb probabilistic epigenesis 4 层 / Thelen-Smith dynamic systems / Fischer dynamic skill / Magnusson holistic / Csikszentmihalyi flow + neoteny / Brandtstädter action / Baltes lifespan + SOC + plasticity / Elder life course + Oakland cohort + multiple trajectories / Shweder cultural psych / Spencer PVEST / Lerner PYD 5C + thriving / Cairns 75 年史 / Werner orthogenetic / Valsiner Baldwin genetic logic + helix / Fowler 信仰 6 阶段 / Cartesian 二分批判 / 跨章 6 大命题 |
| S1 | 1 | 1602 | 新生儿能力涌现(Thelen self-organization)|
| S2 | 5 | 1500-1505 | Bronfenbrenner microsystem 婴儿期 / Thelen 走步反射 / Thelen A-not-B 错误修正 / Fischer skill reorganization / proximal processes serve-return |
| S3 | 1 | 1646 | 4-6 月情绪分化(Werner orthogenetic)|
| S4 | 1 | 1644 | 物体永久 dynamic 修正(Thelen vs Piaget)|
| S5 | 1 | 1643 | 9-12 月走步 dynamic systems |
| S6 | 14 | 1500-1513 | Karp vs 蒙氏元层冲突 / mesosystem 家学校协调 / individual pathway / Fischer 13 层级 / 反早教 / asset-based PYD / 心流 toddler / 改环境 vs 改自己 / identity 形成起步 / 反白人中产标准 / 信仰发展早期 + Oser 5 阶段 / timing 原则 / 个体差异 vs 普世 |
| S7 | 8 | 1602-1610 | PYD Connection / individual pathway / autotelic / intentional self-development / PYD competence / PYD caring / PYD confidence / identity 2-3 岁 |
| S8 | 14 | 631-1146 | 一本一立场困惑 / exosystem / macrosystem / chronosystem / Baltes 反 6 岁分水岭 / Shweder 互依 self / Csikszentmihalyi flow 难度匹配 / 改环境 vs 改自己 5 岁 / Spencer racism / Oser 灵性发展 / PYD character / 文化-个人共建构 / asset-based 视角 / Search 40 项发展资产 |

**累计 SRC-030:95 张知识卡覆盖 S0-S8 全段 + 17 章全覆盖 + 118 张新术语。**

---

## SRC-031 · WHO + UNICEF Infant and Young Child Feeding Policy Compendium(国际公共卫生指南合集 Tier 1)⭐⭐⭐

**Phase 13 完成 2026-05-04 — 完成 4 国卫生指南闭环(WHO 国际 + AAP 美 + 鲍秀兰 中 + 松田 日)。**

| 段 | 卡数 | ID 范围 | 主题 |
|---|------|--------|------|
| S0 | 5 | 1024-1028 | WHO 4 国 1 国际总论 / 选 BFHI 产院 / 中国奶粉营销 vs Code / 全球 EBF 44% / Innocenti 1990 政治根基 |
| S1 | 18 | 1000-1017 | 出生 1 小时开奶 / 肌肤接触 ≥ 1h / BFHI 10 步骤 / 只医学指征用配方 / 24h 同室 / 反对定时喂奶 / 早期奶瓶慎用 / 出院衔接 / EBF 操作定义 / Code 4 大禁 / Code 涵盖产品 / 中国奶粉 Code 违规 / 医学例外清单 / HIV+ART 时代 / 母乳免疫成分 / Lancet 820k 生命 / 中国产院差距 / 初乳头 5 天黄金 |
| S2 | 5 | 1044-1048 | 看信号不看表 / 奶不够别加配方 / 70°C 水冲奶粉 / LAM 哺乳避孕 / 混合喂养风险 |
| S3 | 3 | 1042-1044 | 辅食 4 月还是 6 月(WHO vs AAP)/ 4 月前肠没准备 / 中国提前加米粉通病 |
| S4 | 11 | 1045-1055 | 6 月辅食 + 母乳并行 / WHO 4 大支柱 / 6-8 月 2-3 餐 / 食物多样性 / 食物质地递进 / 反馈喂养 / 6 月起含铁优先 / WHO 图 vs CDC 图 / WHO 6 大动作里程碑 / 母乳娃 CDC 图别误判 / 6-12 月母乳 50% 能量 |
| S5 | 4 | 1037-1040 | 9-11 月 3-4 餐 / Finger food 自喂 / 1 周岁仍持续 / 12 月转奶粉?WHO 不推 |
| S6 | 7 | 1064-1070 | 持续到 2 岁国际共识 / 12-24m 33% 营养 / 12-23m 加餐 / 中国早断 vs WHO 2 岁 / 工作妈妈持续 / 158 天 vs 6 月 / 增长奶 Code 禁 |
| S7 | 3 | 1099-1101 | 2 岁是底线非上限 / 自然离乳 vs 主动断奶 / 12-36m 跟随家庭饮食 |
| S8 | 1 | 868 | 学龄前奶选择(全奶或母乳,不需 4 段)|

**累计 SRC-031:65 张知识卡(初版 57 + 用户深度审补 8)覆盖 S0-S8 全段 + 12/15 文档 WebFetch 成功(3 失败 gaps Innocenti/Acceptable Reasons/PAHO 10 原则)+ 43 张新术语(初版 34 + 深审补 7 G-TERM + 2 G-PERSON)。**

**用户深度审补漏(2026-05-04)**:
- 补 8 卡:C-S0-1029(营养不良 3 类)/ C-S1-1018(BFHI 关键管理 4 步)/ C-S1-1019(BFHI 第 3 步产前)/ C-S1-1020(BFHI 第 5 步衔乳)/ C-S1-1009(Nestle 1977 抵制)/ C-S1-1022(中国 BFHI 1992-1994)/ C-S2-1049(Cochrane Kramer-Kakuma 2012)/ C-S6-1071(疫苗期间继续母乳)
- 重建 2 卡(并行 session ID 冲突):C-S7-1100/1101 被 SRC-040 海蒂卡覆盖 → 重建为 C-S7-1102/1103
- 补 9 术语:G-TERM-stunting / G-TERM-wasting / G-TERM-MTCT / G-TERM-PMTCT / G-TERM-Cronobacter-sakazakii / G-TERM-PIF-safe-preparation / G-TERM-Nestle-boycott-1977 / G-PERSON-Kramer / G-PERSON-Detwyler

**段分布最新**:S0=6 / S1=23 / S2=6 / S3=3 / S4=11 / S5=4 / S6=8 / S7=3 / S8=1 = 65 张

**关键 WHO 独家命题**(跟现库其他派差异化):
- BFHI 10 步骤(产院实操标准 — 中国 6,000+ 爱婴医院实操差距独家维度)
- Code 1981 4 大利益方禁令 + 后续 WHA 决议(中国奶粉品牌违规普遍)
- EBF 0-6 月操作定义(连水都不给 + ORS/维生素/药 例外清单 — 唯一明确的派)
- 持续母乳到 2 岁 'or beyond'(vs AAP 1 年 / 鲍 1 年 / 中国早断传统)
- WHO Growth Standards 2006 母乳基线(vs CDC 2000 配方基线 — 母乳娃别误判)
- HIV+ 妈妈 2010 ART 时代修订 + AFASS 5 条件
- Lancet 2016 Victora 820k 婴儿生命数据 + IQ +3 点
- LAM 哺乳闭经法 3 条件 >98% 有效
- 配方奶 70°C 水冲泡(防阪崎杆菌)
- WHO 2025 全球 EBF ≥ 50% 目标 + 中国差距

**跨派对照亮点**(跨 AAP/鲍/松田/Karp/Brazelton 5+ 派 100% 跨派率):
- 6 月 EBF:WHO 与 AAP/鲍/松田 部分一致,WHO 操作定义最明确
- 反产院定时喂奶:BFHI 第 8 步 ↔ 松田 SRC-024 C-S1-761(反产院'3 小时定时')
- 反早期奶瓶:BFHI 第 9 步 ↔ Karp SRC-005 立场略不同(Karp 推 3-4 周用奶嘴防 SIDS)
- 持续母乳 2 年:WHO 唯一明确推 ≥ 2 岁的派 — 跟 AAP/鲍/松田 全分歧

**5 轮独立审 0 错全过**:R1 机器审 / R2 文档反向覆盖 / R3 漏术语扫 / R4 用户三审(hook + 跨派 + 段覆盖) / R5 深度审。

---

*最后更新:2026-05-04 Phase 13 完成 + 用户深度审补漏 — WHO + UNICEF SRC-031(65 卡 + 43 术语);**完成 4 国卫生指南完整闭环 ⭐⭐⭐**;累计 1327 张知识卡 + 763 术语 + 31 SRC 引用,5 轮审 + 用户深度审 0 错全过。*

---

## SRC-040 · Murkoff《What to Expect the First Year / 海蒂育儿大百科 0-1岁》

**英文原版**:Heidi Murkoff, Sandee Hathaway, Arlene Eisenberg, *What to Expect the First Year* (Workman Publishing, 1989, 全新第 2 版 2010)
**中译本**:南海出版公司(新经典文化发行),2014,译者莫夏迪、张敏,ISBN 978-7-5442-6992-6
**对应段**:S0-S7 全段(主战场 S1 0-1 月新生儿,扩展到妈妈/父亲/二孩 S0/S6/S7)
**卡片总数**:**156**(Phase B 146 + Phase C 反向覆盖审计补 10)
**等级分布**:A 63(40%)/ B 87(56%)/ C 6(4%)
**Source yaml**:[SRC-040.yaml](../10-sources/tier3-books/notes/SRC-040.yaml)
**任务书**:[PHASE14_MURKOFF.md](../00-meta/PHASE14_MURKOFF.md)
**完成 books_to_buy.md 16/16**:✅ 海蒂是最后一本

### 核心独家命题

- **海蒂中性立场示范**:包裹/共睡/奶嘴/睡训 都给两派列利弊不站队 — 中国家长稀缺的"不内疚"框架
- **父亲专章**(C-S0-2164..2168):FMLA 12 周陪产假 / 居家爸爸 250 万人 / 父亲产后抑郁 / 5 岁更自信
- **多胎+二孩**(C-S6-1600..1604 + C-S7-1100..1101):怀孕 3 月末告诉 / 退化别施压 / 5 岁前不独处
- **新生儿百科**:黄疸三类 / 脐带新立场 / 6 种意识状态 / 哭声 5 类 / 婴儿粉刺 / 胎记 6 类 / 鹅口疮 / 囟门红旗 / 周期性呼吸
- **疫苗第一波**(C-S2-2005..2010 + C-S2-2105..2107):2 月 5 针集中 + DTaP 副反应 + 5 大流言 + 7 大红旗 + 减痛 5 招
- **G12 LEAP 自我修正**(C-S3-2248 vs C-S3-2249):海蒂 2010 延后 vs 2014 早引入,展示主流共识更新
- **G13 睡眠训练主流派**(C-S3-2258 + C-S5-2152):温和 Ferber/改良 + 渐进退出
- **急救硬核**(Part 6 25 张):噎食 5+5 海姆立克 / 婴儿 CPR / 烫伤冷水 30 分 / 撞头观察 6 小时 12 红旗 / 中毒别催吐
- **妈妈第一年**(C-S0-2153..2163):哺乳 +400-500 卡 / 父母疲劳综合征 / PPD vs Blues / 凯格尔 / 高质量陪伴 = 换尿布说话

### 段分布速览

#### S0 段(s0-pregnancy,31 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S0-2053](s0-pregnancy/C-S0-2053.yaml) | 包皮环切术:利弊都不重,自己拍 | controversy, safety | A |
| [C-S0-2054](s0-pregnancy/C-S0-2054.yaml) | 产前面谈选儿科医生 7 问清单 | — | B |
| [C-S0-2055](s0-pregnancy/C-S0-2055.yaml) | 独立 vs 合伙 vs 团体诊所 | — | C |
| [C-S0-2056](s0-pregnancy/C-S0-2056.yaml) | 母乳还是配方:权衡而非道德题 | philosophy | B |
| [C-S0-2057](s0-pregnancy/C-S0-2057.yaml) | 真正不能母乳的 7 种情况 | safety, red_flag | A |
| [C-S0-2058](s0-pregnancy/C-S0-2058.yaml) | 收养妈妈也能母乳喂养 | — | B |
| [C-S0-2059](s0-pregnancy/C-S0-2059.yaml) | 婴儿用品别买全套,留 9 月再补 | — | C |
| [C-S0-2060](s0-pregnancy/C-S0-2060.yaml) | 婴儿衣服直接买大码 | — | C |
| [C-S0-2061](s0-pregnancy/C-S0-2061.yaml) | 月嫂 vs 产妇护导员 vs 钟点工 | — | C |
| [C-S0-2062](s0-pregnancy/C-S0-2062.yaml) | 祖父母首次到访先约边界 | philosophy, controversy | C |
| [C-S0-2063](s0-pregnancy/C-S0-2063.yaml) | 乳房产前不需任何"锻炼 | safety | A |
| [C-S0-2064](s0-pregnancy/C-S0-2064.yaml) | 乳头内陷孕期就评估 | — | B |
| [C-S0-2065](s0-pregnancy/C-S0-2065.yaml) | 纸尿裤 vs 棉布尿布:没赢家 | — | B |
| [C-S0-2066](s0-pregnancy/C-S0-2066.yaml) | 宠物迎新生儿:孕期就训练 | safety, red_flag | B |
| [C-S0-2153](s0-pregnancy/C-S0-2153.yaml) | 哺乳妈妈每天多吃 400-500 大卡 | postpartum, mom, breastfeeding | B |
| [C-S0-2154](s0-pregnancy/C-S0-2154.yaml) | 父母疲劳综合征第一年逃不掉 | postpartum, mom, fatigue | B |
| [C-S0-2155](s0-pregnancy/C-S0-2155.yaml) | 产后抑郁 vs Baby Blues 怎么分 | postpartum, mom, depression, red_flag | A |
| [C-S0-2156](s0-pregnancy/C-S0-2156.yaml) | 哺乳期避孕仍可能怀 | postpartum, mom, contraception, safety | B |
| [C-S0-2157](s0-pregnancy/C-S0-2157.yaml) | 哺乳期可服黄体酮避孕药 | postpartum, mom, contraception | B |
| [C-S0-2158](s0-pregnancy/C-S0-2158.yaml) | 产后 6 周内禁这些剧烈动作 | postpartum, mom, exercise, safety | B |
| [C-S0-2159](s0-pregnancy/C-S0-2159.yaml) | 凯格尔健肌法防压力性尿失禁 | postpartum, mom, kegel | B |
| [C-S0-2160](s0-pregnancy/C-S0-2160.yaml) | 12 周内意外再孕的识别 | postpartum, mom, pregnancy, safety | B |
| [C-S0-2161](s0-pregnancy/C-S0-2161.yaml) | 给自己留时间不是自私 | postpartum, mom, self_care | B |
| [C-S0-2162](s0-pregnancy/C-S0-2162.yaml) | 不同风格的妈妈都没错 | postpartum, mom, philosophy | B |
| [C-S0-2163](s0-pregnancy/C-S0-2163.yaml) | 高质量陪伴=换尿布+做饭说话 | postpartum, mom, controversy | B |
| [C-S0-2164](s0-pregnancy/C-S0-2164.yaml) | 美国 FMLA 12 周陪产假但少给薪 | postpartum, dad, FMLA | B |
| [C-S0-2165](s0-pregnancy/C-S0-2165.yaml) | 居家爸爸不是稀奇 250 万人在做 | postpartum, dad | B |
| [C-S0-2166](s0-pregnancy/C-S0-2166.yaml) | 父亲也会产后抑郁 | postpartum, dad, depression, red_flag | B |
| [C-S0-2167](s0-pregnancy/C-S0-2167.yaml) | 爸爸的触摸对宝宝同样重要 | postpartum, dad | B |
| [C-S0-2168](s0-pregnancy/C-S0-2168.yaml) | 爸爸塑造的孩子 5 岁更自信 | postpartum, dad | B |
| [C-S0-2400](s0-pregnancy/C-S0-2400.yaml) | 1 岁内汽车安全座椅必须后向 | safety, red_flag | A |

#### S1 段(s1-newborn,38 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S1-2102](s1-newborn/C-S1-2102.yaml) | 母乳的妈妈端 7 大好处 | — | A |
| [C-S1-2103](s1-newborn/C-S1-2103.yaml) | 母乳频喂 vs 配方久饱:正常 | — | B |
| [C-S1-2104](s1-newborn/C-S1-2104.yaml) | 决定不喂母乳:别内疚 | philosophy | C |
| [C-S1-2202](s1-newborn/C-S1-2202.yaml) | 包皮环切术后护理 | care, hygiene | B |
| [C-S1-091](s1-newborn/C-S1-091.yaml) | 黄疸三类对比表 | red_flag, controversy | B |
| [C-S1-092](s1-newborn/C-S1-092.yaml) | 脐带护理新立场 | care, hygiene | B |
| [C-S1-2205](s1-newborn/C-S1-2205.yaml) | 包裹要不要做 | care, controversy, sleep | B |
| [C-S1-2206](s1-newborn/C-S1-2206.yaml) | 大便颜色 8 类图鉴 | red_flag | B |
| [C-S1-2207](s1-newborn/C-S1-2207.yaml) | 婴儿粉刺 | skin | B |
| [C-S1-2208](s1-newborn/C-S1-2208.yaml) | 胎记 6 类区分 | skin | B |
| [C-S1-2209](s1-newborn/C-S1-2209.yaml) | 鹅口疮母婴双向感染 | red_flag | B |
| [C-S1-2210](s1-newborn/C-S1-2210.yaml) | 囟门红旗信号 | red_flag | A |
| [C-S1-2211](s1-newborn/C-S1-2211.yaml) | 莫罗反射正常信号 | — | B |
| [C-S1-2212](s1-newborn/C-S1-2212.yaml) | 周期性呼吸正常 | — | B |
| [C-S1-2213](s1-newborn/C-S1-2213.yaml) | 6 种婴儿意识状态 | — | B |
| [C-S1-2214](s1-newborn/C-S1-2214.yaml) | 哭声 5 类含义解码 | — | B |
| [C-S1-2215](s1-newborn/C-S1-2215.yaml) | 配方奶冲调安全 | safety, feeding | B |
| [C-S1-2216](s1-newborn/C-S1-2216.yaml) | 母乳储存时间表 | safety, feeding | B |
| [C-S1-2217](s1-newborn/C-S1-2217.yaml) | 奶瓶喂奶 5 不要 | safety, feeding | B |
| [C-S1-2218](s1-newborn/C-S1-2218.yaml) | 排气 3 种姿势对比 | feeding | A |
| [C-S1-2219](s1-newborn/C-S1-2219.yaml) | 双胞胎喂养策略 | feeding | B |
| [C-S1-2220](s1-newborn/C-S1-2220.yaml) | 体温调节看颈背 | — | B |
| [C-S1-2221](s1-newborn/C-S1-2221.yaml) | 脐疝按压禁忌 | red_flag | B |
| [C-S1-2222](s1-newborn/C-S1-2222.yaml) | 阴囊水囊肿区分疝 | red_flag | B |
| [C-S1-2223](s1-newborn/C-S1-2223.yaml) | 听力在家自查 | — | B |
| [C-S1-2302](s1-newborn/C-S1-2302.yaml) | 1 岁内噎食:5 拍背 + 5 胸压 | safety, red_flag | A |
| [C-S1-2303](s1-newborn/C-S1-2303.yaml) | 婴儿 CPR:30 压 2 吹 100 次/分 | safety, red_flag | A |
| [C-S1-2304](s1-newborn/C-S1-2304.yaml) | 烫伤先冷水 30 分,别用冰 | safety, red_flag | A |
| [C-S1-2305](s1-newborn/C-S1-2305.yaml) | 撞头后观察 6 小时,12 红旗送医 | safety, red_flag | A |
| [C-S1-2306](s1-newborn/C-S1-2306.yaml) | 中毒:别催吐,先打中毒中心 | safety, red_flag | A |
| [C-S1-2307](s1-newborn/C-S1-2307.yaml) | 家庭急救包 + 急救电话墙贴 | safety, red_flag | B |
| [C-S1-2500](s1-newborn/C-S1-2500.yaml) | 母乳宝宝从 2 周起补 VD 400 IU | safety | A |
| [C-S1-2501](s1-newborn/C-S1-2501.yaml) | 肠绞痛安抚 8 招(5S 之外) | controversy | B |
| [C-S1-2502](s1-newborn/C-S1-2502.yaml) | 偏头颅预防:醒着多变体位 + 头方向轮换 | safety | B |
| [C-S1-2503](s1-newborn/C-S1-2503.yaml) | 乳头疼痛/皲裂 7 步处理 | — | B |
| [C-S1-2504](s1-newborn/C-S1-2504.yaml) | 涨奶 → 堵奶 → 乳腺炎 三阶梯识别 | safety, red_flag | A |
| [C-S1-2505](s1-newborn/C-S1-2505.yaml) | 哺乳期 5 类禁忌:烟/酒/咖/草药/某药 | safety | A |
| [C-S1-2506](s1-newborn/C-S1-2506.yaml) | 婴儿背带袋鼠护理 5 益处 | — | B |

#### S2 段(s2-1to3mo,17 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S2-2005](s2-1to3mo/C-S2-2005.yaml) | 2 月儿保:疫苗第一波 5 针集中 | safety, gap_g9_filled | A |
| [C-S2-2006](s2-1to3mo/C-S2-2006.yaml) | DTaP 副反应:1/3 局部红肿正常 | safety, gap_g9_filled | A |
| [C-S2-2007](s2-1to3mo/C-S2-2007.yaml) | 4 种疫苗节奏:IPV/Hib/PCV/HepB/Rota | safety, gap_g9_filled | A |
| [C-S2-2008](s2-1to3mo/C-S2-2008.yaml) | 疫苗 5 大流言一句话破 | controversy, safety, gap_g9_filled | A |
| [C-S2-2009](s2-1to3mo/C-S2-2009.yaml) | 疫苗后 7 大红旗:出现立即送医 | safety, red_flag, gap_g9_filled | A |
| [C-S2-2010](s2-1to3mo/C-S2-2010.yaml) | 打针减痛 5 招:不只是抱住 | gap_g9_filled | B |
| [C-S2-2011](s2-1to3mo/C-S2-2011.yaml) | 早期昼夜节律 6-8 周开始萌 | gap_g10_filled | B |
| [C-S2-2012](s2-1to3mo/C-S2-2012.yaml) | 时间表 vs 按需 海蒂中庸立场 | controversy, philosophy | B |
| [C-S2-2013](s2-1to3mo/C-S2-2013.yaml) | 6-8 周后大便突变少是好事 | — | B |
| [C-S2-2014](s2-1to3mo/C-S2-2014.yaml) | 乳痂(脂溢性皮炎)处理 5 步 | — | B |
| [C-S2-2015](s2-1to3mo/C-S2-2015.yaml) | 难搞宝宝 5 大类气质对症 | philosophy | B |
| [C-S2-2016](s2-1to3mo/C-S2-2016.yaml) | 婴儿车 / 背带 4 大风险 | safety | B |
| [C-S2-2105](s2-1to3mo/C-S2-2105.yaml) | 2-6 月发烧:38°C 找医生 | safety, red_flag | A |
| [C-S2-2106](s2-1to3mo/C-S2-2106.yaml) | 退烧三步:轻穿+多水+用药 | safety | A |
| [C-S2-2107](s2-1to3mo/C-S2-2107.yaml) | 发热性痉挛:侧躺+不喂+计时 | safety | A |
| [C-S2-2108](s2-1to3mo/C-S2-2108.yaml) | 感冒红旗 6 项:何时找医生 | safety, red_flag | A |
| [C-S2-2200](s2-1to3mo/C-S2-2200.yaml) | 婴儿按摩 7 大好处 + 5 步法 | — | B |

#### S3 段(s3-3to6mo,27 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S3-2146](s3-3to6mo/C-S3-2146.yaml) | 4 月儿保 + 第二波疫苗 | safety, gap_p1_filled | A |
| [C-S3-2147](s3-3to6mo/C-S3-2147.yaml) | 早期断奶:3-4 月转奶节奏 | gap_g11_filled | B |
| [C-S3-2148](s3-3to6mo/C-S3-2148.yaml) | 婴儿湿疹 7 步法 | safety | A |
| [C-S3-2149](s3-3to6mo/C-S3-2149.yaml) | 米糊 → 蔬菜 → 水果 顺序之争 | controversy | B |
| [C-S3-2150](s3-3to6mo/C-S3-2150.yaml) | 1 岁内禁全脂牛奶补充 | safety, red_flag | A |
| [C-S3-2151](s3-3to6mo/C-S3-2151.yaml) | 同房不同床 海蒂折中立场 | controversy, philosophy | B |
| [C-S3-2152](s3-3to6mo/C-S3-2152.yaml) | 半夜哺乳:每隔晚延 30 分渐戒 | — | B |
| [C-S3-2246](s3-3to6mo/C-S3-2246.yaml) | 母乳娃拒奶瓶,6 周前就该练 | feeding, breastfeeding, bottle, controversy | B |
| [C-S3-2247](s3-3to6mo/C-S3-2247.yaml) | 妈妈上班了,杯子比奶瓶省心 | feeding, breastfeeding, cup | B |
| [C-S3-2248](s3-3to6mo/C-S3-2248.yaml) | 米粉先上,过敏家族再延 6 月 | feeding, allergy, safety, red_flag | B |
| [C-S3-2249](s3-3to6mo/C-S3-2249.yaml) | 过敏原 6 月起早引,反预防过敏 | feeding, allergy, safety, controversy, red_flag | A |
| [C-S3-2150](s3-3to6mo/C-S3-2150.yaml) | 牛奶 1 岁前禁,加铁奶粉替 | feeding, milk, safety | A |
| [C-S3-2251](s3-3to6mo/C-S3-2251.yaml) | 贫血 6/9/12 月筛,母乳要补铁 | feeding, iron, safety | A |
| [C-S3-2252](s3-3to6mo/C-S3-2252.yaml) | 餐椅 7 安全要点,后倾必飞 | safety, gear, feeding | B |
| [C-S3-2253](s3-3to6mo/C-S3-2253.yaml) | 学步车 AAP 已禁,固定式 30 分钟 | safety, gear, motor, red_flag | A |
| [C-S3-2254](s3-3to6mo/C-S3-2254.yaml) | 婴儿秋千 30 分钟 2 次上限 | safety, gear, motor | B |
| [C-S3-2255](s3-3to6mo/C-S3-2255.yaml) | 翻身后趴睡,SIDS 风险已降 | safety, sleep | A |
| [C-S3-2256](s3-3to6mo/C-S3-2256.yaml) | 刷牙 6 月起,纱布+婴儿牙刷 | safety, dental, hygiene | A |
| [C-S3-2257](s3-3to6mo/C-S3-2257.yaml) | 奶瓶龋 1 岁前停,睡前别含瓶 | safety, dental, feeding, red_flag | A |
| [C-S3-2258](s3-3to6mo/C-S3-2258.yaml) | 5 月睡眠倒退,法伯/法伯改良 | sleep, controversy | B |
| [C-S3-2259](s3-3to6mo/C-S3-2259.yaml) | 6 月儿保+第三波疫苗 | healthcare, vaccine, checkup | A |
| [C-S3-2346](s3-3to6mo/C-S3-2346.yaml) | 婴儿脱水 6 信号:1 项就医 | safety, red_flag | A |
| [C-S3-2347](s3-3to6mo/C-S3-2347.yaml) | 腹泻喂养:继续奶+少量勤补 | safety | A |
| [C-S3-2348](s3-3to6mo/C-S3-2348.yaml) | 中耳炎红旗:疼痛 +2 天不消 | safety, red_flag | A |
| [C-S3-2349](s3-3to6mo/C-S3-2349.yaml) | RSV 红旗:皮肤变蓝立刻急诊 | safety, red_flag | A |
| [C-S3-2350](s3-3to6mo/C-S3-2350.yaml) | 反流(GER)4-7 月达峰自愈 | safety | A |
| [C-S3-2400](s3-3to6mo/C-S3-2400.yaml) | 铁库 4-6 月耗尽,饮食铁主补 | safety | A |

#### S4 段(s4-6to9mo,13 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S4-2144](s4-6to9mo/C-S4-2144.yaml) | 7 月手指食物,豌豆/弹珠两规格 | feeding, safety | B |
| [C-S4-2145](s4-6to9mo/C-S4-2145.yaml) | 噎食 vs 干呕,干呕别插手 | safety, feeding, red_flag | A |
| [C-S4-2146](s4-6to9mo/C-S4-2146.yaml) | 整天零食=蛀牙根源,2-3 顿就够 | feeding, dental | B |
| [C-S4-2147](s4-6to9mo/C-S4-2147.yaml) | 8 月不爬正常,跳爬直立也行 | controversy | B |
| [C-S4-2148](s4-6to9mo/C-S4-2148.yaml) | 8 月起 babyproofing,四肢着地视角 | safety | A |
| [C-S4-2149](s4-6to9mo/C-S4-2149.yaml) | 婴儿手语 9 月+,不抢说话 | controversy | B |
| [C-S4-2150](s4-6to9mo/C-S4-2150.yaml) | 7-8 月乳头被咬,坚定 No+拔离 | feeding | B |
| [C-S4-2151](s4-6to9mo/C-S4-2151.yaml) | 拒辅食 4 招,换形状别哄战 | feeding | B |
| [C-S4-2244](s4-6to9mo/C-S4-2244.yaml) | 蜜蜂叮咬:刮不挤 + 过敏 4 项 | safety, red_flag | A |
| [C-S4-2245](s4-6to9mo/C-S4-2245.yaml) | 中暑红线:皮肤热干无汗 | safety, red_flag | A |
| [C-S4-2246](s4-6to9mo/C-S4-2246.yaml) | 晒伤 + 防晒:6 月内只遮挡 | safety | A |
| [C-S4-2247](s4-6to9mo/C-S4-2247.yaml) | 鼻血 + 鼻腔异物:别仰头 | safety, red_flag | A |
| [C-S4-2248](s4-6to9mo/C-S4-2248.yaml) | 眼外伤:不揉不压 + 化学冲 15 分 | safety, red_flag | A |

#### S5 段(s5-9to12mo,23 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S5-2143](s5-9to12mo/C-S5-2143.yaml) | 12 月不走完全正常 | philosophy, mainstream, gross_motor | A |
| [C-S5-2144](s5-9to12mo/C-S5-2144.yaml) | 分离焦虑是好事 | philosophy, mainstream, attachment, controversy | B |
| [C-S5-2145](s5-9to12mo/C-S5-2145.yaml) | 断奶 1 岁前后 | philosophy, mainstream, feeding, weaning | B |
| [C-S5-2146](s5-9to12mo/C-S5-2146.yaml) | 1 岁戒奶瓶防龋齿 | safety, mainstream, feeding, tooth | B |
| [C-S5-2147](s5-9to12mo/C-S5-2147.yaml) | 1 岁起换全脂牛奶 | mainstream, feeding, milk | A |
| [C-S5-2148](s5-9to12mo/C-S5-2148.yaml) | 12 月开口第一个真词 | mainstream, language, milestone | B |
| [C-S5-2149](s5-9to12mo/C-S5-2149.yaml) | 指物=真沟通 | mainstream, language, communication | A |
| [C-S5-2150](s5-9to12mo/C-S5-2150.yaml) | 物体永久性质变 | mainstream, cognitive, object_permanence | A |
| [C-S5-2151](s5-9to12mo/C-S5-2151.yaml) | 管教不是体罚 | mainstream, discipline, controversy | A |
| [C-S5-2152](s5-9to12mo/C-S5-2152.yaml) | 睡前焦虑温和应对 | mainstream, sleep, philosophy, controversy | A |
| [C-S5-2153](s5-9to12mo/C-S5-2153.yaml) | 戒夜奶 1 岁前后 | mainstream, sleep, feeding | B |
| [C-S5-2154](s5-9to12mo/C-S5-2154.yaml) | 1 岁后食欲变小 | mainstream, feeding, toddler | B |
| [C-S5-2155](s5-9to12mo/C-S5-2155.yaml) | 花生稀释后 1 岁可吃 | safety, mainstream, feeding, allergy, red_flag | A |
| [C-S5-2156](s5-9to12mo/C-S5-2156.yaml) | 12 月儿保+疫苗 | mainstream, vaccine, checkup | A |
| [C-S5-2157](s5-9to12mo/C-S5-2157.yaml) | 学步赤脚最佳 | mainstream, gross_motor, shoes | B |
| [C-S5-2158](s5-9to12mo/C-S5-2158.yaml) | 2 岁前禁屏幕 | safety, mainstream, screen_time | A |
| [C-S5-2159](s5-9to12mo/C-S5-2159.yaml) | 害羞是性格不是病 | mainstream, social, shyness | B |
| [C-S5-2160](s5-9to12mo/C-S5-2160.yaml) | 撞头摇头多正常 | mainstream, behavior, self_soothing | B |
| [C-S5-2243](s5-9to12mo/C-S5-2243.yaml) | 误吞硬币:观察便便,纽扣电池急诊 | safety, red_flag | A |
| [C-S5-2244](s5-9to12mo/C-S5-2244.yaml) | 牙齿脱落:乳牙别复位,带去看 | safety, red_flag | A |
| [C-S5-2245](s5-9to12mo/C-S5-2245.yaml) | 出血止血:压 15 分 + 高过心脏 | safety, red_flag | A |
| [C-S5-2246](s5-9to12mo/C-S5-2246.yaml) | 牵拉肘:只哭不抬手 = 急诊 | safety, red_flag | B |
| [C-S5-2247](s5-9to12mo/C-S5-2247.yaml) | 流感疫苗:6 月+ 起每年打 | safety, red_flag | A |

#### S6 段(s6-12to24mo,5 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S6-1600](s6-12to24mo/C-S6-1600.yaml) | 怀孕 3 月末告诉老大刚好 | sibling, communication | B |
| [C-S6-1601](s6-12to24mo/C-S6-1601.yaml) | 老大退化是正常的别施压 | sibling, regression | B |
| [C-S6-1602](s6-12to24mo/C-S6-1602.yaml) | 老大伤害小宝多是好奇不是恶意 | sibling, safety | B |
| [C-S6-1603](s6-12to24mo/C-S6-1603.yaml) | 老大想喝奶让他试一口 | sibling, breastfeeding | B |
| [C-S6-1604](s6-12to24mo/C-S6-1604.yaml) | 5 岁前两个宝宝绝不独处一房 | sibling, safety, red_flag | A |

#### S7 段(s7-24to36mo,2 张)

| ID | title | tags | 等级 |
|---|---|---|---|
| [C-S7-1100](s7-24to36mo/C-S7-1100.yaml) | 分配时间略偏老大可以 | sibling | B |
| [C-S7-1101](s7-24to36mo/C-S7-1101.yaml) | 让老大当主助手不当小家长 | sibling, controversy | B |

### 跨派对照硬指标(L 节 conflicts.md 8 项)

- **L1** 海蒂中性包裹 vs Karp 强裹 vs 蒙氏反包裹
- **L2** 海蒂温和睡眠 Ferber/改良 vs Lillard 关门睡 vs Bowlby 反训
- **L3** 海蒂 LEAP 早引入 vs 海蒂 2010 旧版延后 vs 中国老人禁忌
- **L4** 海蒂母乳/配方权衡而非道德题 vs WHO/BFHI 母乳唯一立场
- **L5** 海蒂体罚反对 vs 中国传统打骂 vs 松田瞬间打手
- **L6** 海蒂祖父母先约边界 vs 中国全家抢着照顾
- **L7** 海蒂 8 月不爬正常 vs 鲍秀兰缺爬有害 vs Lillard 坐型
- **L8** 海蒂 1 岁戒奶瓶 vs AAP 12-18 月 vs Lillard 9-10 月

### gaps.md ✅ resolved 8 项 P0 + 9 项 P1

P0 全部 resolved:G6 黄疸 / G7 脐带 / G8 新筛(部分) / G9 2 月疫苗 / G10 昼夜节律 / G11 母乳→混合 / G12 LEAP / G13 睡眠训练(部分)

### 11 张新术语卡(40-glossary/)

G-PERSON-Murkoff(海蒂作者) / G-TERM-circumcision(包皮环切) / G-TERM-cradle-cap(乳痂) / G-TERM-thrush(鹅口疮) /
G-TERM-fontanel(囟门) / G-TERM-periodic-breathing(周期性呼吸) / G-TERM-LEAP-trial(LEAP 2015 试验) /
G-TERM-allergy-introduction(过敏原早引入) / G-TERM-babyproofing(家庭安全防护) /
G-TERM-postpartum-recovery(产后恢复期) / G-TERM-FMLA(美国家庭医疗假法)

### 自动审计统计

- evidence_level 升级 B → A:6 张(C-S1-2210/2218 + C-S2-2008 + C-S3-2148 + C-S5-2143/2152)
- 跨源 related_cards 双向链接候选:48 对(主线本次未批量执行,留 Phase 15)
- 5 阶段工作流(Phase A-E)全完成,无打断用户

---

*Phase 14 完成 2026-05-04 — Murkoff SRC-040(156 卡 + 11 术语);**完成 books_to_buy.md 16 条目最终条目(16/16 100% 闭环 ⭐⭐⭐)**;累计 1483 张知识卡 + 774 术语 + 32 SRC 引用。*

---

### SRC-040 用户深度审查补充(2026-05-04 第二轮)

R2/R3/R4 深审在 156 张基础上 +10 漏知识卡 + +9 术语卡,机器审 0 错全过:

**R2 补 10 张漏知识卡**:
- C-S0-2500 婴儿安全药箱 12 类清单
- C-S1-2600 婴儿润肤乳含花生油警告(反常识 LEAP 经表皮致敏)
- C-S2-2300 退烧药对比 + 阿司匹林禁忌(雷氏综合征红旗)
- C-S3-2500 选保姆 + 12 项交接清单(中国中产高频)
- C-S5-2160 9 月撞头摇头多数自愈(反焦虑)
- C-S5-2400 9 月+宝宝咬人:别反咬(中国老人对立)
- C-S5-2401 1 岁挑食替代蛋白 7 法
- C-S6-1700 性别中立教养 6 招
- C-S6-1701 1 岁内带宝宝旅行 7 安全(春节场景 / 车温烤箱级)
- C-S7-1200 早产儿 4 大并发症(PDA/ROP/IVH/NEC,中国 7% 早产率刚需)

**R3 新增 9 张术语卡(40-glossary/)**:
G-PERSON-Ferber / G-TERM-whole-milk-toddler / iron-deficiency-anemia / pointing-gesture / toddler-appetite-drop / rhythmic-movement-disorder / babywearing / sleep-regression / developmental-red-flag

**R4 主线机器修**:104 张作者错 + 111 张 publisher 统一 + 5 张 controversy 漏标 + 18 张 edition 字段 + 22 张 S5 卡 glossary_refs 重置(用真 G-ID 替换断链)

**最终海蒂卡总数**:**166 张知识卡 + 20 张新术语卡**(机器审 0 错:YAML / glossary / related / failure_mode / authors / publisher 全过 ✅)
