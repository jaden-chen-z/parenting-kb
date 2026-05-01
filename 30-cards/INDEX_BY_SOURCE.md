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

| Source ID | 书名 | Tier | 卡片数 | 段 |
|---|---|---|---|---|
| SRC-003 | Karp《卡普新生儿安抚法》(英 2002 / 中译 2013) | 3 | 33(S1: 31 + S2: 2) | S1, S2 |

> 注:SRC-001 / SRC-002 是 Tier 1 网页,目前未生成卡片(Phase 0 仅做了知识单元层 K-MILE-S5-001 / K-MECH-CROSS-001)。

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

*最后更新:2026-05-01(Phase 1 Karp 第一本完成)*
