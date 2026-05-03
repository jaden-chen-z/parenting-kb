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
| SRC-010 | Brazelton《Touchpoints: Birth to 3》(Da Capo, 1992/2006) | 3 | **79** | S0-S7(全段 + 首次扩 S0)|

**总计**:Karp 33 + AAP 63 + 鲍秀兰 86 + Brazelton 79 = **261 张知识卡**(2026-05-02 Phase 3 第二本 Brazelton 完成 + 自审补 9 张高价值漏卡)

> 注:SRC-001 / SRC-002 是 Tier 1 网页,目前未生成卡片(Phase 0 仅做了知识单元层 K-MILE-S5-001 / K-MECH-CROSS-001)。
> 术语卡(40-glossary/)**88 张**不计入此索引(独立命名空间);Phase 3 Brazelton 新增 **20 张**(8 核心 + 12 高频自审补):G-TERM-touchpoint / G-PERSON-Sparrow / G-ABBR-NBAS / G-TERM-regression-progression / G-TERM-strengths-based / G-TERM-six-states / G-TERM-discipline / G-TERM-toilet-learning / G-TERM-tantrum / G-TERM-negativism / G-TERM-lovey / G-TERM-temperament / G-TERM-symbolic-play / G-TERM-self-soothing / G-TERM-gatekeeping / G-TERM-bonding / G-TERM-fussy-period / G-TERM-cognitive-burst / G-TERM-spoiling-myth / G-TERM-imaginary-friend。SRC-010 引用 79 个 G-ID,46 张仍待补 backlog。
> ⭐ Phase 3 首次扩展段:**S0(孕期)+ S6(1-2 岁)+ S7(2-3 岁)** — 鲍秀兰建 S6+S7,Brazelton 首建 S0。
> 🔍 **自审补卡** (2026-05-02 收官后):Brazelton 9 章高价值漏入 — Allergies 积木理论 / School Readiness 晚一年 / Self-Image 挫折是燃料 / Television 屏幕硬规则 / Fears Kagan 内向气质 / Delays 两个黄金质问 / Hospitalization 争取陪护 / Sibling Rivalry Erikson 内疚 / Loss and Grief 别说"睡着了"。

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
| [C-S6-024](s6-12to24mo/C-S6-024.yaml) | 18 月通过红鼻子镜子测试 | — | B |
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

*最后更新:2026-05-02 收官审计后(Phase 3 第二本 Brazelton 完成,**261 张知识卡 + 88 张术语卡** + S0 孕期段首建 + 自审补 9 卡 + 12 高频术语)*
