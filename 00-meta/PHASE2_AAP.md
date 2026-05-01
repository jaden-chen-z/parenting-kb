# Phase 2 执行任务书 · 第二本:AAP《Caring for Your Baby and Young Child》

> 项目代号:parenting-kb · Phase 2 第一本(Phase 1 Karp 收官,2026-05-01)· 版本 v1.0
> 这是给**新 Claude Code session** 看的自包含任务书。
>
> **接手必读三件套**(按顺序):
> 1. 本文件(PHASE2_AAP.md)
> 2. `00-meta/PHASE1_KARP.md` v1.2(§10 实战调整 14 条 — **跳过会重蹈覆辙**)
> 3. `00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md`(Karp 已经做了什么)
>
> 然后看 `30-cards/INDEX_BY_SOURCE.md` 了解 Karp 33 张已有卡的清单。

---

## 0. 一句话任务

抓 AAP《Caring for Your Baby》在线 portal(healthychildren.org),产 **40-60 张中文循证卡片**,**同时给 Karp 33 张已有卡做 cross-validate**(B 升 A / 解 controversy / 真冲突写 conflicts.md)。

---

## 1. 选定的书 + 来源

**AAP《Caring for Your Baby and Young Child: Birth to Age 5》**(美国儿科学会权威工具书,7th Ed 2019)

- 在线 portal:[https://www.healthychildren.org/English/ages-stages/baby/](https://www.healthychildren.org/English/ages-stages/baby/)
  - 子主题:feeding / sleep / safety / crying / development / vaccines / colic / breastfeeding 等
- 中译本:《美国儿科学会育儿百科》第 6 版(北京科学技术出版社)— 可选,**官网英文优先**
- **Tier 1 权威源** → A 级证据天然支撑
- **不用 OCR**,直接 WebFetch HTML(避开 Phase 1 主要工程挑战)

### 为什么选这本作为 Phase 2 第一本

1. Tier 1 权威 → 直接 cross-validate Karp 33 张(把 B 升 A,解 controversy)
2. 0-12 月全段覆盖 → S2-S5 都能填一些(Karp 主要在 S1)
3. 网页源,chunk 策略可以用 §10.13 §1 推荐的 ~5KB
4. 免费 + 合法,不需要购书

---

## 2. 卡片规范

**完全继承** PHASE1_KARP v3.3(见 PHASE1_KARP.md §2 全部内容):

- 全中文,白话风格(§2.5)
- 字数上限 §2.2(title ≤15 字 / why_matters ≤80 字 / 背面合计 ≤310 字)
- hook 默认填(§10.10)
- evidence_level 实操标尺(§10.7)— **AAP 卡默认可标 A**(它本身是 Tier 1 + 同行评议引用)
- schema 用 `stages: [SX]` 列表(§2.3),每张卡只填一个段(§本次决策 2026-05-01)

**ID 规则**(继续从 Phase 1 续号):
- 各段卡片 ID 接续 Phase 1:S1 从 C-S1-034 起,S2 从 C-S2-003 起,S3-S5 从 C-SX-001 起
- 源 ID 从 SRC-004 起(`source_index.yaml` 里 `next_src_id` 已设)

---

## 3. 工作流(基于 Phase 1 教训改进 — §10.13)

### 3.1 抓取阶段(网页源,不是 OCR)

- 用 WebFetch 抓 healthychildren.org 各子主题页
- 每页 raw HTML 存 `10-sources/tier1-authoritative/raw/aap_<topic>.html`
- **>50KB 用 subagent 提取**(§7.2 任务书)
- **chunk 大小 ~5KB**(1500 中文字 ≈ 2000 token,§10.13 §1)
- **prompt 黑白名单**(§10.13 §2):跳过 nav / 广告 / 页脚 / 评论 / 相关链接

### 3.2 source yaml 生成

每个 AAP 子主题一份 SRC-XXX.yaml,字段照 SRC-001/002 schema(网页类型),verbatim 字段保留英文原文 + 关键中译参考。

### 3.3 卡片生成 · 双轨并行

**A 轨:产新卡**(优先 S2-S5,Karp 没覆盖的)
- S2:tummy time / 4 月睡眠 / cooing / 社交微笑 / 颈部肌肉
- S3:翻身 / 辅食决策(4 vs 6 月)/ Piaget 反应 / 早期过敏原引入(LEAP)
- S4:BLW vs 泥糊 / 陌生人焦虑 / 物体永久性 / 出牙
- S5:扶站 / 第一个真词 / 分离焦虑 / 12 月儿保

**B 轨:cross-validate Karp 33 张**(把 B 升 A,解 controversy)

具体优先 cross-validate 清单:

| Karp 卡 | 现状 | AAP 验证目标 |
|---|---|---|
| C-S1-016 侧抱 SIDS | A | 补 AAP Safe Sleep 官方 verbatim |
| C-S1-020 摇晃 vs SBS | A | 补 AAP 婴儿安全摇晃指南 |
| C-S1-022 奶嘴 vs 母乳建立 | C, controversy | AAP 立场对照,可能解争议 |
| C-S1-028 共同入睡 10 步 | C, controversy | AAP 反对成人床共睡 → conflicts.md |
| C-S1-030 牛奶蛋白过敏 | B | LEAP 研究 + AAP 立场,可能升 A |
| C-S1-031 红旗信号 | A | 补 AAP "何时打 911" 官方清单 |
| C-S1-033 产后抑郁 | A | 补 AAP 推荐转介路径 |

### 3.4 反向覆盖审计(§10.4 — **必做**)

每段(S1/S2/...)产卡完成后,跑一次反向审计:
- 独立读 AAP 该段全部 chunks
- 不带先验,从零列"父母最该记的 N 件事"
- 与已写卡 diff,补漏 / 删冗 / 合并

Karp 这一步抓出 9 张高价值卡,**接近 1/3**,下一本不能跳。

### 3.5 输入/输出长度比异常告警(§10.13 §4)

每段提取后,统计 `output_chars / chunk_chars`:
- < 0.05 → 提取太少,可能漏关键内容,⚠️ 重做
- > 0.5 → 提取太多,verbatim 应精简

---

## 4. 输出位置

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml                # 加 SRC-004 ... 起
│   └── tier1-authoritative/
│       ├── raw/aap_*.html               # 每个 AAP 子主题一个
│       └── notes/SRC-004.yaml ...       # 每个一份 source yaml
├── 30-cards/
│   ├── INDEX_BY_SOURCE.md               # 加 SRC-004+ 章节
│   ├── s1-newborn/                      # 续号(从 C-S1-034 起)
│   ├── s2-1to3mo/                       # 续号(从 C-S2-003 起)
│   ├── s3-3to6mo/                       # 新建从 C-S3-001 起
│   ├── s4-6to9mo/                       # 新建从 C-S4-001 起
│   └── s5-9to12mo/                      # 新建从 C-S5-001 起
└── 00-meta/
    ├── progress.md                      # 更新
    ├── conflicts.md                     # 记 Karp vs AAP 真争议(优先 028 共睡 / 022 奶嘴)
    └── checkpoints/
        └── checkpoint_PHASE2_AAP_YYYYMMDD.md
```

---

## 5. 完成定义

- [ ] 抓 8-15 个 AAP 子主题(每个一份 SRC-XXX yaml + raw HTML)
- [ ] 产 40-60 张新卡(S1-S5 都有覆盖)
- [ ] cross-validate Karp 33 张 → ≥ 5 张升级 evidence_level
- [ ] conflicts.md 记 ≥ 2 处 Karp vs AAP 真争议
- [ ] checkpoint MD 完成
- [ ] progress.md 更新
- [ ] INDEX_BY_SOURCE.md 加 SRC-004+ 章节

**用户验收**:抽 5 张随机审,4+ 张满意 = Phase 2 第一本通过 → 进 Phase 2 第二本(Brazelton 或鲍秀兰)。

---

## 6. 关键约束(继承 + Phase 2 特定)

**继承自 PHASE1_KARP v1.2**:

| 章节 | 内容 |
|---|---|
| §0 硬规则 | 不盗版 / 不凭训练记忆 / 不和稀泥 / 宁少勿滥 |
| §2 卡片规范 v3.3 | schema / 字数 / 引用 / **白话风格** |
| §5 evidence_level | A/B/C 通用定义 + §10.7 单本书阶段实操标尺 |
| §10 实战教训 14 条 | 全部继承,**§10.13 五条改进必做** |

**Phase 2 特定**:

- chunk **5KB**(不是 Phase 1 的 15KB,§10.13 §1)
- prompt **黑白名单**(§10.13 §2)
- **输入/输出比异常告警**(§10.13 §4)
- **网页源**不是 OCR,§10.1 不适用
- **双轨**:新卡 + cross-validate(Phase 1 没有这一轨)
- **conflicts.md** 必须维护(Phase 1 没生成内容)

---

## 7. 常见错误避免

| ❌ 不要 | ✅ 应该 |
|---|---|
| 把 AAP 内容直接当 Karp 升级版 | AAP 是循证背书,Karp 是流派——区分清楚 |
| 抓盗版资源 | 用 healthychildren.org 官方免费内容 |
| 把每个 AAP 主题都做成卡 | 优先 cross-validate Karp 已有的 + 补 S2-S5 缺的 |
| 把 Karp vs AAP 冲突当 Karp 错 | 写到 conflicts.md,标 `controversy` tag,等用户拍板 |
| 用 Karp 的 chunk 大小(15KB) | §10.13 §1:用 ~5KB |
| 跳过反向覆盖审计 | 每段必做,Karp 这一步抓出 1/3 高价值卡 |
| 一次性产 40-60 张倾倒给用户 | 分段审,每段 8-15 张做完就给用户审 |

---

## 8. 启动建议(第一波抓什么)

按 cross-validate 优先级,先抓与 Karp S1 卡对应的 AAP 子主题:

**第一批(给 Karp 升级)**:
1. AAP Safe Sleep + SIDS Prevention → 升级 C-S1-016 / C-S1-020
2. AAP Crying & Colic → cross-validate C-S1-003/004 等哭闹机制卡
3. AAP Breastfeeding & Bottle-feeding → 升级 C-S1-021/022(吸吮 + 奶嘴)
4. AAP Postpartum Depression → 升级 C-S1-033

**第二批(S2-S5 新卡)**:
5. AAP 2-month / 4-month / 6-month / 9-month / 12-month milestone pages
6. AAP Tummy Time guide
7. AAP Solid Foods(S3 辅食决策)
8. AAP Stranger Anxiety / Separation Anxiety

---

## 附录 · 上手 5 分钟

```bash
# 1. 看项目结构
cd ~/Desktop/parenting-kb
ls -la

# 2. 必读三件套(15-20 分钟)
cat 00-meta/PHASE2_AAP.md                                       # 本文件
cat 00-meta/PHASE1_KARP.md                                      # §10 必读
cat 00-meta/checkpoints/checkpoint_PHASE1_KARP_20260501.md      # Karp 全产出

# 3. 看 Karp 已有 33 张作为 cross-validate 基准
cat 30-cards/INDEX_BY_SOURCE.md                                 # 按书分组索引

# 4. 看几张代表卡
cat 30-cards/s1-newborn/C-S1-016.yaml   # SIDS 仰睡(待 cross-validate)
cat 30-cards/s1-newborn/C-S1-022.yaml   # 奶嘴 controversy
cat 30-cards/s1-newborn/C-S1-028.yaml   # 共睡 controversy

# 5. 启动:WebFetch AAP Safe Sleep 第一个页面
# https://www.healthychildren.org/English/ages-stages/baby/sleep/Pages/default.aspx
# > 50KB → spawn subagent 提取(参考 §3.1)
```

---

*v1.0 · 2026-05-01 — 基于 PHASE1_KARP v1.2 教训(§10 共 14 条)升级*
*Phase 1 Karp 完成产出参见 `checkpoint_PHASE1_KARP_20260501.md`*
