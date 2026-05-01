# 育儿知识库构建项目 · Claude Code 任务书 v3.0

> 项目代号：parenting-kb
> 目标用户：一对中文双语家庭，给两个 0-1 岁孩子使用
> 任务核心：**知识探索 → 知识提取 → 卡片生成** 三件事
> 最终产物：一个普通文件夹，里面有结构化的源 / 单元 / 卡片
> 任务书版本：v3.0（2026-04-30，相比 v2 主要变化：去掉 Obsidian 概念，回到普通文件夹）

---

## 0. 给 Claude Code 的元指令

阅读完整文档后再开始动手。本文档是你的唯一权威说明。

### 不可逾越的硬规则

1. **证据门槛**：本项目核心价值是"权威、受过证实的知识"。任何未经证实的主张不得入库。
2. **不要从盗版站点下载书籍**（LibGen / Z-Library / Anna's Archive 等）。预算允许购书——所需书籍写入 `00-meta/books_to_buy.md`，由用户合法购买后提供 PDF。
3. **不要凭训练记忆生成内容**——必须基于实际抓到的源，每条主张挂 ≥1 个一手引用。
4. **A 级证据要求**：≥2 个独立 Tier 1/2 一手源 + ≥1 个 peer-reviewed 系统综述。
5. **不要替用户做"争议话题"立场决策**——标记为 `pending_user_review`，写进 `00-meta/questions_for_user.md`。
6. **自媒体不作为来源**：知乎、微信公众号、小红书、母婴论坛、营销博客一律 **不作为引用源**（除非来自官方机构账号）。
7. **不要为凑数生成低质量卡片**——宁少勿滥。
8. **URL 易变**：永远先 search 验证当前 URL 再 fetch。
9. **HTML > 50KB 时用 subagent 提取**，避免主上下文污染。

### 必须做的事

- 每个 session 开头读 `00-meta/progress.md`，结尾更新它
- 遇到模糊判断点写进 `00-meta/questions_for_user.md`
- 每完成一个 milestone 输出 `00-meta/checkpoints/checkpoint_YYYYMMDD.md`

---

## 1. 三件事框架

整个项目就做这三件事，循环往复：

### 探索（Discovery）
找到正确的、当前有效的源 URL / 论文 DOI / 书目。手段：search-then-fetch、引用滚雪球、机构索引页爬取、关键词矩阵检索。

### 提取（Extraction）
从源里提取出 verbatim 关键内容，存为结构化的 source note（YAML）+ 原始文件备份（HTML/PDF）。手段：subagent 提取大文件、人工 verbatim 摘录、章节级解析 PDF。

### 卡片生成（Card Synthesis）
把多个 source 提取的内容综合成知识单元（知识层），再从单元蒸馏出卡片（呈现层）。手段：交叉验证、流派立场标注、证据等级评定、动作可执行性检查。

每个 stage（月龄段）走完一遍这三件事 = 一个 Phase。

---

## 2. 月龄段切分（5 段）

按发展真实"关节"切，不按均匀月份。

| 段 | 月龄 | 段名 | 文件夹 | 目标卡片数 |
|---|---|---|---|---|
| S1 | 0-1 月 | 第四产程 | `s1-newborn` | 80-100 |
| S2 | 1-3 月 | 社交萌芽 | `s2-1to3mo` | 50-70 |
| S3 | 3-6 月 | 认知爆发 | `s3-3to6mo` | 70-90 |
| S4 | 6-9 月 | 探索期 | `s4-6to9mo` | 80-100 |
| S5 | 9-12 月 | 前行走+前语言 | `s5-9to12mo` | 70-90 |

### 每段必须覆盖的主题清单

**S1 · 0-1 月**
建立喂养（母乳衔乳、配方奶节奏、按需 vs 按时）、安抚哭闹（Karp 5S、PURPLE crying、肠绞痛）、原始反射（Moro/rooting/sucking/palmar grasp/stepping）、新生儿黄疸、安全睡眠（SIDS、AAP 仰睡、合睡 vs 分床）、新生儿筛查、产后妈妈生理与心理（产后抑郁/焦虑、伤口恢复）、第一次儿保（出生后 3-5 天、2 周、1 月）、脐带护理、胎记观察、体温/喂养量警戒线。

**S2 · 1-3 月**
社交微笑（6-8 周首次出现机制）、tummy time（频率/时长/抗拒处理）、抬头与颈部肌肉、视觉追踪、cooing 元音发声、哭闹峰值（6-8 周达峰、12 周回落）、早期昼夜节律萌芽、眼神交流、辨认主要照护者、被动免疫开始下降。

**S3 · 3-6 月**
4 月睡眠倒退、翻身（俯→仰先于仰→俯）、笑、抓物、放嘴期、Piaget 主→次循环反应跃迁、辅食决策窗口（4 vs 6 月之争 + AAP/WHO 立场）、辅食准备信号、首次过敏原引入时机（LEAP 研究后范式转变）、母乳→混合喂养过渡。

**S4 · 6-9 月**
辅食实操（BLW vs 传统泥糊）、过敏原引入、噎食 vs 干呕区分、独坐独立性、爬行萌芽（不爬也正常的循证依据）、pincer grasp 萌芽、陌生人焦虑、物体永久性（A-not-B error）、joint attention、babbling 辅音重复期、出牙、分离焦虑起点。

**S5 · 9-12 月**
扶站、巡航、独走萌芽、第一个真词、指物（pointing 是后续语言能力最强预测因子）、分离焦虑高峰、物体永久性巩固、意图性沟通、精细动作精度、tantrum 前兆、睡眠训练抉择、扩展辅食形态、戒奶瓶/戒夜奶、12 月儿保 + 疫苗。

### 4 个跨段标签

每个卡片/单元用 tags 字段标记：

- `safety` — 安全（SIDS / 跌落 / 烫伤 / 噎食）
- `philosophy` — 流派立场（RIE / Pikler / 蒙氏 / Brazelton）
- `controversy` — 争议话题（睡眠训练 / cosleeping / 屏幕 / 母乳 vs 配方 / BLW vs 泥糊）
- `red_flag` — 红旗信号（"该看医生了"清单）

可叠加。

---

## 3. 文件夹结构

```
parenting-kb/
├── README.md                           # 项目说明
├── 00-meta/
│   ├── progress.md                     # 当前进度（每 session 更新）
│   ├── questions_for_user.md           # 待用户回答
│   ├── books_to_buy.md                 # 建议购买的书目清单
│   ├── conflicts.md                    # 流派/证据冲突
│   ├── gaps.md                         # 找不到的内容
│   └── checkpoints/
│       └── checkpoint_YYYYMMDD.md
├── 10-sources/
│   ├── source_index.yaml               # 全部源的索引（一个文件，便于检索）
│   ├── tier1-authoritative/
│   │   ├── raw/                        # 抓回的原始 HTML/PDF
│   │   │   ├── cdc_ltsae_9months.html
│   │   │   └── ...
│   │   └── notes/                      # 每个源一份提取后的 YAML
│   │       ├── SRC-001.yaml
│   │       └── ...
│   ├── tier2-academic/
│   │   ├── raw/
│   │   └── notes/
│   ├── tier3-books/
│   │   ├── raw_pdfs/                   # 用户提供的合法 PDF
│   │   └── notes/                      # 章节级提取
│   ├── tier4-chinese/
│   │   ├── raw/
│   │   └── notes/
│   └── tier5-video-podcast/
│       ├── raw/
│       └── notes/
├── 20-units/                           # 知识单元层
│   ├── s1-newborn/
│   │   ├── K-FEED-S1-001.yaml
│   │   └── ...
│   ├── s2-1to3mo/
│   ├── s3-3to6mo/
│   ├── s4-6to9mo/
│   └── s5-9to12mo/
└── 30-cards/                           # 卡片层（最终产物）
    ├── s1-newborn/
    │   ├── C-S1-001.yaml
    │   └── ...
    ├── s2-1to3mo/
    ├── s3-3to6mo/
    ├── s4-6to9mo/
    └── s5-9to12mo/
```

**ID 规则**：
- 源：`SRC-NNN`（全局唯一编号）
- 单元：`K-{TOPIC}-{STAGE}-{NNN}`，例 `K-FEED-S1-001`
- 卡片：`C-{STAGE}-{NNN}`，例 `C-S1-001`

**关联方式**：用 ID 字符串引用（不用 wiki-link）。例如卡片 yaml 里 `unit_ids: [K-FEED-S1-001, K-SOOTH-S1-003]`。

---

## 4. Schema 定义（YAML）

### 4.1 源 note schema

文件：`10-sources/tierN-.../notes/SRC-NNN.yaml`

```yaml
source_id: SRC-001
title: Milestones by 9 Months
org: CDC NCBDDD
source_type: webpage          # webpage / pdf / journal_article / book_chapter / video / podcast
url: https://www.cdc.gov/act-early/milestones/9-months.html
doi: null
isbn: null
tier: 1
language: en
paywall: false
captcha: false
accessed: 2026-04-30
fetch_method: search_then_fetch
local_file: ../raw/cdc_ltsae_9months.html
file_size_bytes: 76479

# 元信息
metadata:
  first_published: 2025-09-05
  last_reviewed: 2026-02-17
  authors: ["CDC NCBDDD subject matter experts"]

# verbatim 关键内容（按主题组织，全部直接引用，不改写）
verbatim_content:
  social_emotional_milestones:
    - "Is shy, clingy, or fearful around strangers"
    - "Shows several facial expressions, like happy, sad, angry, and surprised"
    - "Looks when you call her name"
    - "Reacts when you leave (looks, reaches for you, or cries)"
    - "Smiles or laughs when you play peek-a-boo"
  language_communication_milestones:
    - 'Makes a lot of different sounds like "mamamama" and "bababababa"'
    - "Lifts arms up to be picked up"
  cognitive_milestones:
    - "Looks for objects when dropped out of sight (like his spoon or toy)"
    - "Bangs two things together"
  movement_physical_milestones:
    - "Gets to a sitting position by herself"
    - "Moves things from one hand to her other hand"
    - 'Uses fingers to "rake" food towards himself'
    - "Sits without support"
  act_early_quote: |
    "You know your child best. Don't wait. If your child is not meeting one or more milestones,
    has lost skills he or she once had, or you have other concerns, act early."

# 给单元层用的精简摘要（你自己写，约 200 字）
summary: |
  CDC LTSAE 9 月龄里程碑使用 75% 通过率阈值（不是平均）。
  4 域共 13 个里程碑。Act Early 框架强调 regression 和未达成都是去筛查的信号。
  AAP 推荐 9-18-30 月节点做 standardized screening。
  重要免责：LTSAE 不是诊断工具。

# 此源支撑哪些单元（双向追踪，新建单元时反填）
referenced_by_units: []

notes: ""
```

### 4.2 知识单元 schema

文件：`20-units/sN-.../K-XXX-SN-NNN.yaml`

```yaml
unit_id: K-FEED-S1-001
node_name: 母乳按需喂养（cue-based feeding）
node_type: 实操原则        # 选项: 核心机制 / 实操原则 / 里程碑 / 红线 / 争议立场 / 流派观点
stages: [S1, S2]
domains: [喂养, 依恋, 睡眠]
evidence_level: A           # A / B / C — 严格按 §5 定义
status: pending_user_review # pending_user_review / approved / rejected
tags: []                    # safety / philosophy / controversy / red_flag, 可空
created: 2026-04-30
updated: 2026-04-30

# 核心论点（一句话主张, 1-3 条）
core_claims:
  - 健康足月儿应在母乳建立期使用按需喂养, 不按固定时间表
  - 按需喂养支持母乳供应建立 + 婴儿自我调节

# 来源（≥3 独立源 = A 级）
sources:
  primary:                  # 一手机构源
    - source_id: SRC-005
      verbatim_quote: |
        "On-demand feeding is recommended for healthy term infants..."
    - source_id: SRC-012
  supporting:               # 论文/系统综述
    - source_id: SRC-067
      type: cochrane_review
    - source_id: SRC-089
      type: rct

# 流派立场
schools:
  RIE: 兼容（强调 responsive caregiving）
  Pikler: 兼容
  Montessori: 缄默
  Brazelton: 兼容（Touchpoints 强调 cue reading）

# 关联节点（其他单元 ID）
related_units:
  - K-FEED-S1-002        # paced bottle feeding
  - K-SLEEP-S1-003       # newborn sleep patterns
  - K-ATTACH-S1-001      # early bonding

# 落地动作（具体可执行）
actions:
  - 观察喂养信号: 早期信号（咂嘴、找乳头、手到嘴）vs 晚期（哭）
  - 间隔范围: 新生儿期通常 1.5-3 小时, 但不强制
  - 夜间不限制: 夜奶频率支持泌乳

# 失败模式
failure_modes:
  - 把所有哭都解读为饿 → 过度喂养 / 反流
  - 走极端不按时也不响应信号 → 错过真饥饿信号
  - 强行延迟到 3 小时 → 影响泌乳 + 婴儿应激

# 测量指标
metrics:
  - 6 周内: 体重增长曲线（WHO 生长标准）
  - 妈妈乳房状态: 充盈 → 排空规律
  - 婴儿信号识别准确率（主观）

# 冲突 / 争议
conflicts:
  - 与"按时喂养"派别的张力（详见 conflicts.md）

# 给用户家的应用注解（可选）
application_notes: |
  大宝 7 月已过此阶段。二宝 9 月出生后立即适用。
```

### 4.3 卡片 schema

文件：`30-cards/sN-.../C-SN-NNN.yaml`

```yaml
card_id: C-S1-001
stage: S1
tags: [safety]              # 跨段标签

# 正面（≤15 字理想，能在 10 秒内记住主旨）
front:
  title: 哭不一定饿——优先排查"非饥饿信号"
  hook: ""                  # 可选, 抓眼一句

# 背面
back:
  why_matters: |
    新生儿哭闹有 5+ 种触发因素（饥饿只是其中之一）。
    盲目喂奶可能掩盖其他需求或导致过度喂养。
  what_to_do:
    - 先排查: 尿布 / 温度 / 抱姿 / 困倦 / 过度刺激
    - 距上次喂奶 < 90 分钟时优先非喂奶安抚
    - 启用 Karp 5S 顺序
  evidence_level: A
  sources_summary: AAP 2022 Caring for Your Baby; Karp Happiest Baby; Cochrane Review on Soothing
  failure_mode: |
    - 把所有哭当饿 → 过度喂养 / 反流加重
    - 走极端不喂奶 → 错过真饥饿信号

# 来源链路（追溯到单元再到源）
unit_ids:
  - K-FEED-S1-001
  - K-SOOTH-S1-003

# 关联卡片
related_cards:
  - C-S1-005          # PURPLE 哭闹周龄曲线
  - C-S1-008          # Karp 5S 完整步骤

# 元数据
language: zh                # 卡片正反面中文; 单元里 verbatim 原文
status: draft               # draft / reviewed / approved
created: 2026-04-30
updated: 2026-04-30
```

---

## 5. 证据等级（严格定义）

| 等级 | 标准 |
|---|---|
| **A** | ≥2 个独立 Tier 1（权威机构）一手引用 + ≥1 个 peer-reviewed 系统综述 / Cochrane / RCT |
| **B** | 1 个 Tier 1 + ≥2 个 peer-reviewed 单项研究；或 ≥3 peer-reviewed 单项研究但无 Tier 1 背书 |
| **C** | 流派原典（如 Pikler / Gerber 著作）的内部主张；或专家共识但缺循证 |

**规则**：
- A 是默认追求等级
- B 允许，必须显式标注
- **C 只允许在带 `philosophy` 标签的卡片**出现（即"这是某流派立场"，非循证结论）。其他主题不允许 C 级
- 不达 C 级的主张：**不入库**

宁可少卡片，不可写没把握的卡片。

---

## 6. 数据来源清单

### Tier 1 · 权威机构（免费、必抓）

| 机构 | 主入口 URL | 重点抓取 |
|---|---|---|
| Harvard Center on the Developing Child | developingchild.harvard.edu | key-concept/* + working papers + InBriefs |
| CDC LTSAE | cdc.gov/act-early | 2/4/6/9/12 月里程碑全部 |
| AAP HealthyChildren | healthychildren.org | ages-stages/baby/* + Bright Futures |
| AAP 政策声明 | publications.aap.org | Safe Sleep, Breastfeeding, Solid Foods 等 |
| WHO | who.int | motor milestones, Nurturing Care Framework, breastfeeding |
| NICHD | nichd.nih.gov | infant care, SIDS, breastfeeding |
| UNICEF | unicef.org/parenting | 0-12 月 |
| 中国国家卫健委 | nhc.gov.cn | 《0-6岁儿童健康管理服务规范》《婴幼儿喂养指南》《DST 量表》 |
| 中国营养学会 | cnsoc.org | 《0-6 月龄婴儿喂养指南》《7-24 月龄婴幼儿喂养指南》 |
| 中华医学会儿科学分会 | csp.org.cn | 0-12 月相关临床指南 |

### Tier 2 · 学术文献

数据库（按可获取性排序）：
1. PubMed (免费摘要)
2. PubMed Central (PMC) — 全文（注意 reCAPTCHA，从 DOI 路径）
3. **Cochrane Library** — 系统综述，**优先**
4. Semantic Scholar — 引用图
5. Google Scholar — 引用滚雪球
6. Unpaywall — 找开放获取版

核心期刊（手动 site: 检索）：
- Pediatrics
- Child Development
- Developmental Psychology
- Infancy
- Attachment & Human Development
- Acta Paediatrica
- Cochrane Database
- 中华儿科杂志（CNKI）

筛选规则：每主题取 Top 3 系统综述 + Top 5 高被引原始研究。优先近 5 年。

### Tier 3 · 书籍（预算允许）

**工作流**：
1. Phase 0 末尾生成 `00-meta/books_to_buy.md`（按优先级排序，标注 ISBN / 推荐理由 / 对应段）
2. 用户购买并把 PDF 放入 `10-sources/tier3-books/raw_pdfs/`
3. Claude Code 章节级提取到 `notes/` 下的 source yaml
4. **关键**：只引用书中可被独立 Tier 1/2 源验证的主张——书的作用是导航和深度，不是单点权威

**A 级必读书目（先列入 books_to_buy.md）**：

底座：
- *From Neurons to Neighborhoods* (NRC/IOM 2000) — National Academies Press 有免费 PDF, 直接下
- *Handbook of Child Psychology* (Lerner ed.)
- *The Interpersonal World of the Infant* — Daniel Stern
- *Attachment* — John Bowlby (Vol 1-3)

流派原典（必买）：
- *Dear Parent* / *Your Self-Confident Baby* — Magda Gerber
- *Peaceful Babies, Contented Mothers* — Emmi Pikler
- *Montessori from the Start* — Polk Lillard
- *The Happiest Baby on the Block* — Harvey Karp
- *Touchpoints: Birth to Three* — T. Berry Brazelton

实操参考：
- *Elevating Child Care* — Janet Lansbury
- *The Wonder Weeks* — Hetty van de Rijt
- *What to Expect the First Year* — Heidi Murkoff
- *The Scientist in the Crib* — Alison Gopnik

中文权威：
- 《0-3 岁早期教育和潜能开发》— 鲍秀兰
- 《育儿百科》（中文版）

预估购书清单总额：约 ¥3000-5000

### Tier 4 · 中文权威

- 国家卫健委所有 0-6 岁规范（直接 PDF）
- 中国营养学会喂养指南
- 中华儿科杂志相关综述（CNKI 检索 → 付费墙时标记 gap）
- 鲍秀兰团队论文及书籍

### Tier 5 · 视频/播客

- Harvard CDC YouTube 0-3 岁视频
- Janet Lansbury 播客 *Unruffled*
- Magda Gerber 历史录音（RIE Institute）
- Pikler Institute 视频
- Dr. Becky Kennedy *Good Inside* 0-12 月

转录后作为引用源，evidence_level ≤ B（视频内容难做严格 peer review）。

---

## 7. 三个 Pipeline

### 7.1 探索 Pipeline

```
1. 拿到 query/主题
2. 在 source_index.yaml 查重
3. site: 限定 search 验证当前 URL
4. 关键论文用 Cochrane / PubMed 系统综述检索
5. 把候选 URL/DOI 列表存入 candidates.yaml（待 fetch）
```

### 7.2 提取 Pipeline

```
1. fetch URL/PDF
2. 大于 50KB → spawn subagent 提取
3. subagent prompt 模板:
   "Read [文件路径] in chunks. This is a [来源类型] from [机构].
    Strip HTML/nav. Extract verbatim:
    1. [字段 1]
    2. [字段 2]
    Return ONLY structured findings, no preamble."
4. 原始文件存 raw/<filename>
5. 创建 source yaml (§4.1) 在对应 tier 的 notes/
6. 在 source_index.yaml 添加索引条目
```

### 7.3 卡片生成 Pipeline

```
1. 选定主题（如"S1 母乳按需喂养"）
2. 检索 source_index.yaml 找该主题相关的全部源
3. 评估证据等级（达 A 还是 B 还是 C）
4. 生成知识单元 yaml (§4.2)
   - 每条 core_claim 都挂引用
   - 流派立场全部填（unknown 也要标）
   - 关联节点列出
5. 单元生成后，蒸馏成卡片
   - 一个单元可以衍生 1-3 张卡片（不强求 1:1）
   - 卡片正面单句要"可记忆"
   - 背面动作要可执行
6. 卡片质量门（§9）逐项核对
7. 写入 30-cards/sN/
```

### 7.4 处理 reCAPTCHA / 付费墙

- **不要绕过**
- 找开放获取替代版本
- 关键源找不到替代 → 写 `gaps.md`，标注用户付费访问

---

## 8. 工作流（POC-first）

### Phase 0 · Bootstrap（半天）

1. 创建 `parenting-kb/` 目录 + 完整子目录
2. 把本任务书复制到 `00-meta/README.md`
3. 创建空的 `progress.md`、`questions_for_user.md`、`conflicts.md`、`gaps.md`、`source_index.yaml`
4. **生成 `books_to_buy.md` 完整清单**（基于 §6 Tier 3 列表，按优先级排序，每本注明：书名、作者、ISBN、推荐理由、对应段、预估价格）
5. 把作者已抓的 2 份样本（Serve and Return + 9 月里程碑）转换成 v3 格式：
   - 2 个 source yaml 放 `10-sources/tier1-authoritative/notes/`
   - 1-2 个 unit yaml 放 `20-units/s5-9to12mo/`（Serve and Return 是跨段机制，可放 `20-units/cross-stage/`）
6. `git init` + 首次 commit
7. **STOP，告诉用户 Phase 0 完成**

### Phase 1 · S1 端到端 POC（2-3 天）

只做 S1（0-1 月）一段，端到端跑通。

1. 探索：S1 相关 Tier 1 全部页面 URL 验证 + Tier 2 主题论文候选清单
2. 提取：批量 fetch、subagent 提取、生成 source yamls（30-50 个）
3. 卡片生成：知识单元（30-50 个）→ 卡片（80-100 张）
4. 写 Phase 1 checkpoint
5. **STOP，等用户审核**

POC 通过的判断标准：
- 用户随机抽 5 张卡片，4+ 张认为"有价值、引用充分、表述清晰"
- schema 是否需要调整在这一步反馈
- 引用语言（verbatim 英文 vs 翻译中文）的偏好确定

### Phase 2 · 扩展到全部 5 段

逐段执行 Phase 1 流程：S2 → S3 → S4 → S5
每段结束 checkpoint。

### Phase 3 · 跨段质量门

1. 跨段引用一致性检查（同一论点在不同段一致）
2. 4 个跨段标签覆盖度审计
3. `conflicts.md` 整理
4. 全部 unit status 扫描

### Phase 4 · 交付

- v1.0 数据包
- `00-meta/RELEASE_v1.0.md` 总结
- `00-meta/KNOWN_LIMITATIONS.md`

---

## 9. 卡片质量标准

每张卡片必须通过这 7 条：

1. **正面单句要"可记忆"**：能否在 10 秒内读完并记住主旨？
2. **背面 what_to_do 要可执行**：是否有具体动作？
3. **evidence_level 要诚实**：达到 §5 标准
4. **sources_summary 可追溯**：能从这条简短引用找回原始 unit 和 source
5. **failure_mode 不能空**：没有"做错的方式"说明论点太弱
6. **不和稀泥**：争议话题给立场或明确标 `controversy` + `pending_user_review`
7. **关联充分**：每张卡片至少引用 1 个 unit、列出 1+ 关联卡片或单元

**反例**（不允许）：
- ❌ "和宝宝多互动很重要" — 太空泛
- ❌ "新生儿哭闹是正常的" — 没动作
- ❌ "建议睡眠训练" — 争议话题不立场也不标记 `controversy`

**正例**：
- ✅ "PURPLE 哭闹周龄 6 周达峰、12 周回落——撑过这两周不是父母失败"
- ✅ "Tummy time 不是选项题——颈背肌肉只有这个时间窗发育"
- ✅ "陌生人焦虑出现是依恋形成的信号，不是性格问题"

---

## 10. 升级触发器（什么时候问用户）

写进 `00-meta/questions_for_user.md`：

1. 争议话题立场（睡眠训练 / cosleeping / BLW / 屏幕 / 母乳 vs 配方）
2. 流派矛盾无法仅凭循证决策
3. 关键 Tier 3 书籍找不到合法源（写入 books_to_buy）
4. 同一论点 ≥3 个源但结论不一致
5. 中文文化与西方循证的张力（把屎把尿 / 月子文化 等）
6. 段内卡片数明显超出或不足目标 30%

格式（参考）：

```markdown
## Q1: 睡眠训练立场（截至 S3）

**背景**：4 月睡眠倒退后，主流流派立场不一：
- AAP: 6 月后可考虑
- Karp: 4 月可启动温和方法
- Sears (依恋育儿): 反对任何睡眠训练
- 中文文化: 普遍反对哭睡

**3 个独立循证综述结论**：
- (引用 1)
- (引用 2)
- (引用 3)

**待你拍板**: 卡片库的默认立场是？
A. 不站立场，给多种方法对比
B. 偏向 4-6 月可启动温和方法
C. 偏向 6 月后再考虑
D. 反对任何睡眠训练

我的建议: B

最后更新: YYYY-MM-DD
```

---

## 11. 进度追踪

`00-meta/progress.md` 模板：

```markdown
# Progress · 育儿知识库

## 当前阶段
Phase 1 / Stage S1 (0-1 月)

## 完成度
- [x] 目录结构
- [x] schemas
- [x] source_index.yaml 初始化
- [/] Tier 1 抓取（5/9 机构）
- [ ] Tier 2 论文抓取
- [ ] 单元提取
- [ ] 卡片生成

## 已抓源数
Tier 1: 12 / 预估 40
Tier 2: 0 / 预估 60
Tier 3: 0 / 预估 15
Tier 4: 0 / 预估 10
Tier 5: 0 / 预估 8

## 已生成
单元: 0
卡片: 0

## 阻塞
- 无

## 待用户回答的问题
见 questions_for_user.md（共 0 条）

## 上次 session 结束时间
YYYY-MM-DD HH:MM

## 下次 session 起点
"继续抓 Tier 1 剩余 4 个机构"
```

每个 session 结束更新进度。每个 Phase 结束写 checkpoint。

---

## 12. 起步动作（你的第一个 todo）

按这个顺序：

1. 读完本文档全部
2. 创建 `parenting-kb/` 目录和完整子目录（§3）
3. 把本文档复制到 `00-meta/README.md`
4. 创建 `README.md`（项目介绍版，给项目根，简短）
5. 创建空 meta 文件：`progress.md`、`questions_for_user.md`、`conflicts.md`、`gaps.md`
6. 创建空 `10-sources/source_index.yaml`
7. **生成 `books_to_buy.md` 完整清单**（基于 §6 Tier 3，按优先级，每本注明书名/作者/ISBN/推荐理由/对应段/预估价格）
8. 把作者已抓的 2 份样本转换为 v3 格式 yaml 放入对应位置
9. `git init` + 首个 commit
10. **STOP，告诉用户 Phase 0 完成，列出待办（购书 / 决定 Phase 1 启动时机）**

Phase 0 完成的标志：
- `tree parenting-kb/` 显示完整骨架
- 所有 yaml 文件能被解析
- `books_to_buy.md` 内容齐全
- git log 有 1 条 commit
- progress.md 显示 Phase 0 完成

---

## 附录 A · 关键搜索 query 模板

每个主题 ≥3 个 query 角度。

### 喂养
- `infant breastfeeding establishment first month systematic review`
- `cue-based feeding vs scheduled feeding RCT`
- `paced bottle feeding evidence`
- `0-6 月龄婴儿喂养指南 中国营养学会`
- `responsive feeding infant 6-12 months`

### 睡眠
- `infant sleep consolidation 4 months systematic review`
- `4-month sleep regression mechanism`
- `extinction sleep training 0-12 months long-term outcomes Cochrane`
- `cosleeping safety AAP guidelines`
- `safe sleep SIDS prevention 2024`

### 哭闹
- `PURPLE crying period frequency curve`
- `colic infant evidence-based interventions Cochrane`
- `Karp 5S calming infant evidence`

### 大动作
- `WHO motor milestones windows of achievement`
- `tummy time evidence neck strength systematic review`
- `infant motor development Pikler natural sequence`

### 认知
- `object permanence Piaget A-not-B error infant`
- `joint attention emergence age longitudinal`
- `infant directed speech Patricia Kuhl`

### 依恋
- `infant attachment formation Bowlby Ainsworth`
- `secure base behavior 6-12 months`
- `stranger anxiety separation anxiety developmental timeline`

### 安全
- `SIDS sudden infant death syndrome prevention 2024 AAP`
- `infant choking hazards baby-led weaning evidence`
- `safe sleep environment AAP recommendations`

### 辅食
- `complementary feeding 4 vs 6 months WHO AAP`
- `baby-led weaning vs traditional spoon feeding RCT`
- `early allergen introduction LEAP study`

（Phase 1 中按需扩展）

---

## 附录 B · 已抓 verbatim 数据样本

任务书写作过程中已实抓 2 份 verbatim 数据，Phase 0 转换为 v3 yaml 格式后放入：

1. `10-sources/tier1-authoritative/notes/SRC-001.yaml` — 基于 CDC LTSAE 9 月里程碑实抓
2. `10-sources/tier1-authoritative/notes/SRC-002.yaml` — 基于 Harvard CDC Serve and Return 实抓
3. `20-units/s5-9to12mo/K-MILE-S5-001.yaml` — 基于 SRC-001
4. `20-units/cross-stage/K-MECH-CROSS-001.yaml` — Serve and Return 跨段机制，基于 SRC-002

---

*v3.0 完。执行中发现本文档不清楚处，写入 `00-meta/questions_for_user.md`，不要瞎拍板。*
