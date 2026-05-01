# Phase 1 执行任务书 · S1 新生儿 · 第一本:Karp《卡普新生儿安抚法》

> 项目代号:parenting-kb · S1(0-1 月)POC 第一本 · 版本 v1.2(2026-05-01)
> 这是给一个新 Claude Code session 看的自包含任务书。
>
> **v1.1 变更**:新增 §2.5 语气风格 — 卡片正反面必须白话,不学究化(2026-05-01 用户反馈)
> **v1.2 变更**:新增 §10 实战调整 — 沉淀 Karp 第一本的工程性教训(OCR 分块/subagent 限制/反向覆盖审计/分部分增量审核 等 12 条),修正 §2/3/附录的出版社/年份/译者占位为真实数据(2026-05-01)
> **下一 session 必读 §10**(与 §0-§9 同等优先)

---

## 0. 一句话任务

读 Karp《卡普新生儿安抚法》中译本,提取 S1(0-1 月)知识点,产出 **20-40 张中文循证卡片**,放入 `30-cards/s1-newborn/`。

---

## 1. 必读前置(按顺序)

1. **总任务书**:`00-meta/README.md`(v3.0 完整任务书,§0 硬规则不可逾越,§4 schema,§7 pipeline,§9 卡片质量标准)
2. **当前进度**:`00-meta/progress.md`
3. **已确认决策**:`00-meta/questions_for_user.md`(Q1-Q3 已 resolved)
4. **本任务书**:就是你正在看的这份(覆盖 Q3 的卡片语言策略)
5. **schema 样本**:
   - 已有源 yaml:`10-sources/tier1-authoritative/notes/SRC-001.yaml`、`SRC-002.yaml`
   - 已有单元 yaml:`20-units/s5-9to12mo/K-MILE-S5-001.yaml`、`20-units/cross-stage/K-MECH-CROSS-001.yaml`

---

## 2. 卡片规范 v3.3(覆盖任务书 §4.3 + Q3 决定)

**重要**:本规范覆盖 questions_for_user.md Q3 之前的"双语对照"方案。从此任务起,**全部卡片中文**,只在难翻译的专有术语后括号给英文。

### 2.1 语言规则

| 规则 | 说明 |
|---|---|
| 卡片正反面 | **全中文** |
| 专有术语处理 | 中文 + (English),只对**难翻译**或**首次出现**的专业术语,例:**应答式互动**(Serve and Return)|
| 缩写/学派名 | 直接英文,不强译,例:RIE / AAP / SIDS / Pikler / 蒙台梭利 |
| Verbatim 原文 | **不放卡片正反面**,只在 source yaml 里保留原文(英/中/德均可)|

### 2.2 字数上限(关键)

**一个知识点 = 一张卡片**。一张卡片的中文字数(不含标点 + 不含引用脚注):

| 字段 | 字数上限 | 说明 |
|---|---|---|
| `front.title`(标题)| **≤15 字** | 一句话主张,10 秒内读完记住 |
| `back.why_matters`(为什么重要)| **≤80 字** | 给一个理由,不和稀泥 |
| `back.what_to_do`(怎么做)| **≤150 字总,每条 ≤30 字** | 3-5 条 bullets,每条都是可执行动作 |
| `back.failure_mode`(失败模式)| **≤80 字** | 做错的方式,不能空 |
| **背面正文合计** | **≤310 字** | 不含 citation footer |
| `citation`(引用脚注)| ≤100 字 | 见 §2.4 |

### 2.3 字段定义(完整 yaml)

```yaml
card_id: C-S1-NNN              # NNN 从 001 起递增
stages: [S1]                   # 列表(与 §4.2 单元 schema 对齐),每张卡只填一个段;主段 = stages[0],卡片放对应文件夹
tags: []                       # safety / philosophy / controversy / red_flag,可空,可叠加

# 正面(中文,≤15 字)
front:
  title: 哭不一定饿——优先排查"非饥饿信号"
  hook: ""                     # 可选,抓眼一句

# 背面(全中文,字数受 §2.2 限制)
back:
  why_matters: |
    新生儿哭闹有 5 种以上触发因素(饥饿只是其中之一)。
    盲目喂奶可能掩盖其他需求或导致过度喂养。
  what_to_do:
    - 先排查:尿布 / 温度 / 抱姿 / 困倦 / 过度刺激
    - 距上次喂奶 < 90 分钟时优先非喂奶安抚
    - 启用 5S(Karp 5S)安抚顺序
  failure_mode: |
    把所有哭都当饿 → 过度喂养 / 反流加重。
    走极端不喂奶 → 错过真饥饿信号。
  evidence_level: A            # A / B / C(按任务书 §5 标准)
  
# 引用(论文式,见 §2.4)
citation:
  book_title_en: "The Happiest Baby on the Block: The New Way to Calm Crying and Help Your Newborn Baby Sleep Longer"
  book_title_zh: "卡普新生儿安抚法 0-1岁"
  authors:
    - Harvey Karp
  publisher_en: Bantam Books
  publisher_zh: 浙江人民出版社(中译)
  year: 2002
  year_zh: 2013                # 中译年份(若知)
  edition: Revised             # 版次(若知)
  location: 第 4 章《关键安抚法 5S》, 页 78-82  # 具体到章节 + 页码
  source_id: SRC-XXX           # 对应 10-sources/tier3-books/notes/SRC-XXX.yaml

# 关联节点
unit_ids:
  - K-SOOTH-S1-001             # 知识单元 ID(可不填,初期可省略)
related_cards:
  - C-S1-005                   # 相关卡片 ID(可不填)

# 元数据
language: zh
status: draft                  # draft / reviewed / approved
created: 2026-05-XX
updated: 2026-05-XX
```

### 2.4 引用脚注规范(论文式)

**必填字段**:
- `book_title_en`:**英文原版书名**(完整,含副标题)
- `book_title_zh`:中译本书名(若有中译)
- `authors`:作者列表(英文姓名为准)
- `year`:**英文原版**首版年份
- `location`:**精确到章节 + 页码**(例:"第 4 章, 页 78-82" 或 "Chapter 4, pp. 78-82")
- `source_id`:对应的源 yaml ID

**渲染样式**(给人看的最终卡片底部):
```
出处:Karp, H. (2002). The Happiest Baby on the Block. Bantam Books.
中译:卡普新生儿安抚法 0-1岁(浙江人民出版社,2013)
位置:第 4 章《关键安抚法 5S》, 页 78-82
SRC:SRC-003
```

### 2.5 语气风格(白话原则) — v3.3 新增

**重要**:卡片是给疲惫的父母看的,不是给学术评审看的。学究腔 = 失败。

| ✅ 这样写(白话) | ❌ 不要这样(学究) |
|---|---|
| 宝宝在妈妈肚子里待了 9 个月 | 新生儿出生前 9 个月持续暴露于... |
| 又暖又紧,一直在晃 | 持续受到温暖、紧裹、运动等多感官刺激 |
| 你给他准备的安静婴儿房 | 现代育儿环境中的安静卧室 |
| 6 周达峰,3 月回落 | 6 周龄达到哭闹峰值后 12 周龄回落 |
| 哭得越凶,包得越紧 | 当婴儿哭闹强度增加时,应相应加大包裹力度 |

**5 条写作原则**:

1. **主语用"宝宝/你"**,不用"新生儿/父母/婴儿"(除非术语必须,如"新生儿黄疸")
2. **用主动动词**,不用被动句——"待在"不是"被暴露于","在动"不是"被运动刺激"
3. **一句话讲一件事**,不堆叠从句——发现"和"超过两个就拆句
4. **数字保留**(分贝/厘米/月龄/百分比)——这些是这张卡的信息密度,白话化不等于稀释
5. **像在父母群里发消息那样**,不像写论文摘要——读出来不别扭即可

**自检 check**:写完一段大声念一遍。如果听起来像药品说明书或学术论文,就重写。

**适用范围**:
- ✅ `front.title` / `back.why_matters` / `back.what_to_do` / `back.failure_mode` 全部
- ✅ `front.hook`(若填)
- ❌ `citation` 字段(书目信息保持正式格式)
- ❌ source yaml 里的 `verbatim` 字段(verbatim 必须保留原文,不白话化)

---

## 3. 选定的书

**Karp《The Happiest Baby on the Block》中译本《卡普新生儿安抚法 0-1岁》**

| 字段 | 值 |
|---|---|
| 文件路径 | `~/Desktop/parenting-kb/10-sources/tier3-books/raw_pdfs/karp_happiest_baby_zh.md` |
| 文件大小 | 385 KB(中文 OCR 后)|
| 来源 | OCR 自扫描 PDF,语言 chi_sim+eng |
| 流派 | Karp 流派(`philosophy` 标签必引)|
| 对应段 | **S1(0-1 月)主战场**;延伸到 S2 |
| 涵盖主题(预估)| 安抚哭闹(5S 法)、PURPLE 哭闹周期、新生儿哭闹生理、睡眠安抚、第四产程概念 |

### 为什么先选这本

1. **直击 S1 主题**:任务书 §2 S1 清单里"安抚哭闹"和"5S Karp"主题,Karp 是流派原典级权威
2. **中文版本**:OCR 已完成,提取卡片**无翻译开销**
3. **范围合适**:38MB PDF / 385KB MD,POC 易于完整跑通,**不会越界到 S2-S5**
4. **流派原典**:卡片带 `philosophy` 标签时引用绝对正确
5. **可与 Tier 1 交叉验证**:5S 法的有效性有 AAP / Cochrane 综述支撑(Phase 1 后续 Tier 2 抓取时填补)

---

## 4. 工作流(5 步)

### 步骤 1:浏览全书结构(10-30 分钟)

使用 Read 工具读 `karp_happiest_baby_zh.md`(注意 OCR 中可能有少量错字),先读:
- 目录(TOC)/前 50 行
- 章节标题列表(`grep -n "^#" karp_happiest_baby_zh.md` 或类似)
- 抽样几段(中部 / 末部),看 OCR 质量

**>50KB 文件用 subagent 处理**(任务书 §7.2,本书 385KB 必须 subagent)。subagent 分块读,只返回结构化结果。

### 步骤 2:识别知识点清单(30-60 分钟)

按 S1 主题清单(任务书 §2)与 Karp 内容**交集**,列出候选知识点:

预估涵盖:
- PURPLE 哭闹曲线(6 周达峰、12 周回落)
- Karp 5S 安抚法(5 个具体动作)
- "第四产程"概念(出生后 3 月仍是孕期延续)
- 模拟子宫环境的原理
- 哭闹分类:饥饿 / 困倦 / 过度刺激 / 肠绞痛 / 不适
- 安抚顺序(从轻到强)
- 哭闹峰值 vs 异常哭闹的区分
- 睡眠的"白噪音"原理
- 包裹(swaddling)的循证依据 + 风险
- 第四产程 vs 早产儿矫正月龄

每条作为**一个候选卡片**。预估 20-40 个。

### 步骤 3:对每个知识点,用 subagent 提取(2-3 小时)

对每个候选卡片,**spawn 一个 subagent**,prompt 模板:

```
任务:从 karp_happiest_baby_zh.md 中提取关于"<主题>"的内容。
做法:
1. 用 grep 定位相关章节(中文关键词 + 英文如 "5S")
2. 读相关段落(>50KB 时分块读)
3. 提取:
   a) 核心论点(1-2 句中文)
   b) 支撑细节(机制/数据,verbatim 中文)
   c) 实操动作(若有)
   d) 失败模式(若有)
   e) 章节 + 页码位置(从中文目录或正文标题推断)
返回:不要原文复制全段,只要结构化字段。
```

subagent 返回的内容写入候选卡片草稿。

### 步骤 4:生成 source yaml + 卡片 yaml(1-2 小时)

#### 4.1 先建 SOURCE yaml

文件:`10-sources/tier3-books/notes/SRC-003.yaml`

参考 SRC-001/002 的 schema,填:
- 书名(英中双版)
- 作者
- ISBN(若知,可标"待核对")
- `local_file: ../raw_pdfs/karp_happiest_baby_zh.md`
- `summary`(200 字内,你的总结)
- `verbatim_content`:按主题组织(中文为主,英文术语保留)
- `referenced_by_units`:暂留空,后填

同时在 `10-sources/source_index.yaml` 加索引条目,递增 `next_src_id` 到 SRC-004。

#### 4.2 然后写卡片 yaml

文件:`30-cards/s1-newborn/C-S1-NNN.yaml`

每个卡片严格按 §2.3 schema。**字数严格按 §2.2 上限**。

**初期可以省略 unit_ids**(知识单元层暂不强制建,如果需要,放 `20-units/s1-newborn/`)。

### 步骤 5:自检 + 输出(30 分钟)

每张卡片自检 7 项(任务书 §9):
1. 正面 ≤15 字,可记忆
2. 背面 what_to_do 可执行
3. evidence_level 诚实(Karp 是 C 流派 / B 部分有循证支撑)
4. citation 可追溯到 SRC-003
5. failure_mode 不空
6. 争议话题给立场或标 `controversy`
7. 至少引用 1 个 source

整理输出:
- 写一个 `00-meta/checkpoints/checkpoint_PHASE1_KARP_YYYYMMDD.md`
- 列出本次产出的卡片数 + 主题清单
- 列出无法覆盖的 S1 主题(留待后续书)

---

## 5. 输出位置(必须严格按这个)

```
parenting-kb/
├── 10-sources/
│   ├── source_index.yaml                # 加 SRC-003 索引
│   └── tier3-books/notes/
│       └── SRC-003.yaml                 # 新建 - Karp 源
├── 30-cards/s1-newborn/
│   ├── C-S1-001.yaml
│   ├── C-S1-002.yaml
│   └── ...                              # 20-40 张
├── 20-units/s1-newborn/                 # 可选 - 若做单元层
│   ├── K-SOOTH-S1-001.yaml
│   └── ...
└── 00-meta/
    ├── progress.md                      # 更新进度
    └── checkpoints/
        └── checkpoint_PHASE1_KARP_YYYYMMDD.md
```

**ID 规则**:
- 源:SRC-003 起递增
- 卡片:C-S1-001 起递增
- 单元(若建):K-{TOPIC}-S1-001 起,TOPIC 例:SOOTH(安抚)/ CRY(哭闹)/ SLEEP(睡眠)/ FEED(喂养)

---

## 6. 完成定义

- [ ] 20-40 张卡片(全部中文)
- [ ] 全部字数符合 §2.2 上限
- [ ] 每张卡片 citation 完整(英文书名 + 作者 + 章节 + 页码)
- [ ] 1 个 source yaml(SRC-003)
- [ ] source_index.yaml 更新
- [ ] progress.md 更新
- [ ] checkpoint MD 写完
- [ ] 通知用户(终端打印总结)

**用户验收**:抽 5 张随机卡片审,4+ 张满意 = POC 通过 → 进下一本书。

---

## 7. 常见错误避免(don'ts)

| ❌ 不要 | ✅ 应该 |
|---|---|
| Read 整个 MD 进主上下文 | spawn subagent,subagent 用 offset/limit 分块读 |
| 把英文 verbatim 直接放卡片 | 中文表达,verbatim 留 source yaml |
| 字数超 §2.2 | 严控,超了精简 |
| citation 只写"Karp 2002" | 必须英文全称 + 中译 + 章节页码 |
| Karp 一家之言写成绝对结论 | tags 加 `philosophy`,evidence_level 标 C 或 B(循证支撑度看具体话题)|
| 凑数生成低质量卡片 | 任务书 §0 #7:**宁少勿滥** |
| 跨 S1 领域(碰到 S2-S5 内容)| 暂不写,标记到 gaps.md 或 progress.md "下一本书覆盖" |
| 把 OCR 错字直接当 verbatim | 看到明显错字(如"3l"实为"31")自己纠正 + 在 source yaml 里标注"已修正 OCR 错字"|

---

## 附录 A · 卡片 yaml 完整示例

```yaml
card_id: C-S1-001
stages: [S1]                   # 列表(与 §4.2 单元 schema 对齐),每张卡只填一个段;主段 = stages[0],卡片放对应文件夹
tags: [safety]

front:
  title: 哭不一定饿——先排查"非饥饿信号"
  hook: ""

back:
  why_matters: |
    新生儿哭闹有 5 种以上触发因素(饥饿只是其一)。
    盲目喂奶可能掩盖其他需求或导致过度喂养。
  what_to_do:
    - 先排查:尿布 / 温度 / 抱姿 / 困倦 / 过度刺激
    - 距上次喂奶 < 90 分钟时,优先非喂奶安抚
    - 启用 5S(Karp 5S)安抚顺序:包裹 / 侧抱 / 嘘声 / 摇晃 / 吸吮
  failure_mode: |
    把所有哭都当饿 → 过度喂养 / 反流加重。
    走极端不喂奶 → 错过真饥饿信号。
  evidence_level: B

citation:
  book_title_en: "The Happiest Baby on the Block: The New Way to Calm Crying and Help Your Newborn Baby Sleep Longer"
  book_title_zh: "卡普新生儿安抚法 0-1岁"
  authors: ["Harvey Karp"]
  publisher_en: "Bantam Books"
  publisher_zh: "浙江人民出版社"
  year: 2002
  year_zh: 2013
  edition: "Revised"
  location: "第 4 章《关键安抚法 5S》, 页 78-82"
  source_id: SRC-003

unit_ids: []
related_cards:
  - C-S1-005

language: zh
status: draft
created: 2026-05-01
updated: 2026-05-01
```

---

## 附录 B · Source yaml 模板(SRC-003)

参考 `10-sources/tier1-authoritative/notes/SRC-001.yaml` 的 schema,但 source_type 改成 `book_chapter`。

```yaml
source_id: SRC-003
title: "卡普新生儿安抚法 0-1岁(中译本)"
title_en: "The Happiest Baby on the Block: The New Way to Calm Crying and Help Your Newborn Baby Sleep Longer"
org: null
source_type: book_chapter
url: null
doi: null
isbn: null                       # 待核对
isbn_zh: null
tier: 3
language: zh                     # 中译本(英文原版独立 source 则另建)
paywall: false
captcha: false
accessed: 2026-05-XX
fetch_method: user_provided_pdf_ocr
local_file: ../raw_pdfs/karp_happiest_baby_zh.md
file_size_bytes: 384613

metadata:
  authors_en: ["Harvey Karp"]
  authors_zh: ["哈维·卡普"]
  publisher_en: "Bantam Books"
  publisher_zh: "浙江人民出版社"      # 待核对
  year_en: 2002
  year_zh: 2013                  # 待核对
  edition: "Revised"

# verbatim 关键内容(按主题组织,中文为主,英文术语保留)
verbatim_content:
  fourth_trimester_concept:
    - "..."
  five_s_method:
    swaddle: "..."
    side_stomach: "..."
    shush: "..."
    swing: "..."
    suck: "..."
  purple_crying_curve:
    - "..."

summary: |
  Karp《The Happiest Baby on the Block》是新生儿安抚领域流派原典。
  核心概念:第四产程(出生后 3 个月是孕期延续)+ 5S 安抚法(包裹 Swaddle / 侧抱 Side / 嘘声 Shush / 摇晃 Swing / 吸吮 Suck)。
  PURPLE crying 曲线(6 周达峰、12 周回落)是 Karp 重要观察。
  ⚠️ 注意:Karp 的循证强度因话题而异 —— 5S 有部分 RCT 支撑(B 级),但"第四产程"是流派概念(C 级)。

referenced_by_units: []          # 后填
notes: |
  Phase 1 Karp 单本提取产出。
  OCR 错字已在 verbatim_content 字段中纠正,可疑处标注"[OCR? → 实际]"。
  待 cross-validate:AAP soothing 指南 / Cochrane swaddle 综述。
```

---

## 附录 C · Karp 主题概览(Phase 1 候选卡片清单,~25 个)

主题(每个对应 1 张卡片,具体提取后可调整数量):

**🔥 第四产程(Fourth Trimester)**
1. 第四产程概念(出生后 3 月仍是孕期延续)
2. 子宫环境的特征(温暖/紧裹/嗡嗡声/摇晃)
3. 模拟子宫的临床意义

**🔥 PURPLE 哭闹**
4. PURPLE 是缩写,代表 6 个特征
5. 哭闹峰值曲线(2 周起 → 6 周达峰 → 12 周回落)
6. 撑过哭闹峰不是父母失败

**🔥 5S 安抚法**
7. 包裹(Swaddle)— 原理 + 风险(髋发育不良 / 过热)
8. 侧抱(Side/Stomach)— 安抚时姿势,睡眠**禁忌**
9. 嘘声(Shush)— 白噪音原理 + 音量
10. 摇晃(Swing)— 节奏与方向 + 摇婴综合征警告
11. 吸吮(Suck)— 安抚奶嘴 vs 母乳建立期冲突
12. 5S 必须按特定顺序 + 同时使用

**哭闹分类与排查**
13. 5 大触发:饥饿 / 困倦 / 过度刺激 / 肠绞痛 / 不适
14. 距上次喂奶时间作为首要排查指标
15. 异常哭闹红旗信号(送医)

**睡眠**
16. 模拟子宫帮助睡眠的机制
17. 白噪音 vs 安静:Karp 立场与流派分歧
18. 包裹睡眠的安全要点

**喂养(Karp 视角)**
19. 安抚奶嘴对母乳建立期的影响
20. 过度喂养的反流问题

**附加可能**
21. Karp 与 RIE / 依恋育儿派别的张力
22. 5S 的循证证据强度(Karp RCT)
23. 包裹与 SIDS 关系(AAP 立场对照)
24. 早产儿矫正月龄下的应用
25. 中国文化:绑带/捆绑 vs 西方 swaddle 异同

---

## 附录 D · 上手 5 分钟(给新 session)

```bash
# 1. 看项目结构
cd ~/Desktop/parenting-kb
ls -la

# 2. 读总任务书(2 分钟)
cat 00-meta/README.md | head -100

# 3. 读本任务书(就是这份,你已经在读了)

# 4. 看现有 schema 样本(2 分钟)
cat 10-sources/tier1-authoritative/notes/SRC-001.yaml
cat 20-units/s5-9to12mo/K-MILE-S5-001.yaml

# 5. 看待抓的源
ls 10-sources/tier3-books/raw_pdfs/karp_happiest_baby_zh.md
wc -m 10-sources/tier3-books/raw_pdfs/karp_happiest_baby_zh.md

# 6. 启动:用 Bash 工具看 Karp MD 第一段
head -100 10-sources/tier3-books/raw_pdfs/karp_happiest_baby_zh.md

# 然后按 §4 工作流走
```

---

## 10. 实战调整(v1.2 新增)

> 基于 Karp 第一本书 Phase 1 实战(2026-05-01),沉淀 12 条工程性/方法论教训。
> **下一本书/下一 session 接手时,§10 与 §0-§9 同等优先,先读这里能少走弯路。**

### 10.1 OCR 长单行文件需先工程化分块

任务书 §7.2 只规定 ">50KB 用 subagent",未覆盖 OCR 后**整本压在单行**的情形。

**实测**:Karp 中译本 OCR 输出 384KB / 155K 中文字符 / 整本压在单行。直接 Read 不能分块,subagent 也读不动。

**做法**:Python 切成 N 个 15KB chunks,**500 字符 overlap**,放到 `<原文件名>_chunks/` 子目录(参考 Karp `karp_chunks/`)。下一本书如果是同样格式,沿用此方法。

### 10.2 subagent 派生 prompt 容易"too long"

**现象**:主上下文累积后(读了任务书 + yaml + 多次提取报告),即使 subagent 的 prompt 文本极短,派生时也反复报 "Prompt is too long"。Karp 实战中遇 4-5 次。

**对策**:
- subagent prompt 极简(< 200 字),不要复述任务背景或 schema
- 工作流后半段(尤其审计步骤)考虑改用主上下文自读,不强行 subagent
- 不要"一个知识点一个 subagent"细颗粒分发 → 改成"一个 chunk 范围一个 subagent 提取多张卡素材"

### 10.3 章节地图改"按 chunk 范围批量",不"按主题分发"

任务书 §4 步骤 3 原说"对每个候选卡片 spawn 一个 subagent"。**实战改成**:

- 一轮(3 批 subagent):chunks 000-003 / 004-007 / 008-010,每批产出**章节地图 + 主题反向索引**
- 二轮(10 批 subagent):每批读 1-2 个 chunk,提取该范围全部卡片素材

效率约 3 倍,prompt 也更短。

### 10.4 工作流加一步:反向覆盖审计(强烈建议固化)

任务书 §4 步骤 5 只有"自检 7 项"。**实战新增**:

> 每部分卡片写完,主上下文(或独立 subagent)在**不看清单**的情况下,只读原 chunks,从零列"父母最该记的 N 件事",和已有清单做 diff。补漏 / 删冗 / 合并。

实战在 chunks 000-003 抓出 3 张高价值卡(听不懂哭声 ≠ 不细心 / 前 3 月不会惯坏 / 心跳加速是天然反射),**附录 C 候选清单都没列**。

**结论**:附录 C 是先验,不是穷尽。"父母心理类""反直觉类""数据型"卡往往不在先验清单里 → 见 §10.11。

### 10.5 流程改"分部分增量审核"

任务书 §4 默认一次性产出 20-40 张。**实战用户偏好**:按章节分部分,做完一部分就审,改完再做下一部分。

**做法**:把后续部分草稿 mv 到 `30-cards/s1-newborn/_drafts_part2/` 子目录(下划线前缀,不参与正式 ID 编号),审核完再回纳重编号。

### 10.6 出版社/年份/译者数据修正

**任务书原占位**:北京出版社,2010(标"待核对")
**实测真实数据**(OCR 第一行提取):
- 出版社:**浙江人民出版社**(杭州)
- 年份:**2013 年 1 月第 1 版第 1 次印刷**
- 译者:**陈楠**
- ISBN:**978-7-213-05158-6**
- 印张 13.25 / 首印 7000 册

§2.3 / §2.4 / 附录 A / 附录 B 已统一修正。

### 10.7 evidence_level 实际标尺(单本书阶段)

任务书 §5 给 A/B/C 通用定义,**单本书 Phase 1 实操**:

- **C** = Karp 一家之言/流派概念(第四产程、镇静反射、5S 组合理论)
- **B** = Karp 引用了外部研究(Brazelton 1962 哭闹峰、Wessel 3-3 规则、康涅狄格 1990 哭声辨识、Tiffany Field 1986 按摩)
- **A** = 仅在与 Tier 1(AAP/WHO 等)共识对齐时使用(SIDS 仰睡组合、产后抑郁三阶段)

Phase 1 大多数标 B/C,A 节制使用,**留给 Phase 2 cross-validate 后再升级**。

### 10.8 知识单元层(20-units/)Phase 1 跳过

任务书 §4.2 允许"初期省略 unit_ids"。**实战完全跳过**单元层,卡片直接挂 source(`unit_ids: []`),`citation.source_id` 直接指 SRC-XXX。

下一本书继续这个做法,**等 Phase 2-3 再统一回补单元层**。避免 Phase 1 在 schema 完美度上过度投入。

### 10.9 citation 模板加 `translator_zh` 字段

中译本是关键信息源,新增 `translator_zh: "陈楠"` 字段。附录 A 已补。**下一本如有中译,沿用**。

### 10.10 hook 字段:从"可选"改为"默认填"

任务书 §2.3 schema `hook: ""` 标"可选"。**实战默认每张都填**(8-12 字),作为 title 之外的情绪/反直觉钩子句。

例:
- C-S1-002 title "子宫四感官:温暖紧裹响动摇" + hook "安静婴儿房 ≠ 舒服环境"
- C-S1-008 title "宝宝哭你心跳加速是天然反射" + hook "这是生理反射,不是软弱"

**默认建议保留**;若用户不接受密度,可批量去掉。

### 10.11 主动找"父母心理 / 反直觉 / 数据型"卡

附录 C 25 个候选都"知识点导向"(5S 五招/PURPLE/第四产程)。**实战补的 3 张是"父母心理导向"**:

- C-S1-006 听不懂哭声不代表你不细心(数据卡:25%/50% 准确率)
- C-S1-007 前 3 月怎么回应都不会惯坏(标 `controversy`,中文文化分歧)
- C-S1-008 宝宝哭你心跳加速是天然反射(生理反射机制)

下一本书审计时,**主动找这三类卡**,不只跟着附录 C 主题清单走。

### 10.12 用户偏好(从第一本沉淀)

- 一次审小批,不喜欢一次性 20-40 张倾倒 → 见 §10.5
- 卡片白话至上,见学究腔会直接打断 → 见 §2.5
- 关心方法论可证伪("你怎么知道没漏") → 主动给反向审计 + diff(§10.4)
- yaml 字段名保持英文 key,展示层再翻中文(预留 `00-meta/render_labels.yaml` 映射表,**尚未建,Phase 2 启动前补**)
- 不接受"凭训练记忆生成",所有主张要挂 verbatim 引用
- 出版社年份等数据点必须以原文 OCR 为准,不用任务书占位 → 见 §10.6

### 10.13 外部方法论吸收(GitHub Top 3 调研,2026-05-01)

调研近半年 stars 最高的"从书提取知识点"3 个开源项目,抽取 5 条值得本项目沿用的实践:

| # | 外部做法 | 我们现状 | 下一本怎么改 | 优先级 |
|---|---|---|---|---|
| 1 | **2000-token 黄金块**(论文《Same Task, More Tokens》:LLM 推理在 2000-3000 token 区间最稳定) | 15KB / ~5000 中文字 / ~7500 token,过大 | chunk 改 ~5KB / ~1500 中文字 ≈ 2000 token | 高 |
| 2 | **prompt 黑白名单**(跳过版权页/目录/参考文献/译者后记/广告) | 仅 OCR 修正,无显式黑白名单 | subagent 提取 prompt 显式加"跳过这些页类型" | 中 |
| 3 | **Non-overlapping 去重**(prompt 禁止 + embedding cosine > 0.85 二次去重) | 无显式机制(靠人工审) | 每部分写完后,自动 cosine 相似度查 title 重叠 | 中 |
| 4 | **输入/输出长度比异常告警**(< 0.05 或 > 0.5 都告警) | 无 | 每 subagent 提取后统计字数比 | 高 |
| 5 | **按 ToC 章节切**(优于固定字符) | OCR 文件无干净 ToC,只能按字符 | 下一本若拿到原版 PDF,先用 PyMuPDF `get_toc()` | 视源文件 |

**强烈建议下本书启动前先加 #1 和 #4**(有论文/可量化依据)。**#3 在反向审计阶段固化**(扩展 §10.4)。

**调研来源**(GitHub Top 3 by stars,2025-11 至 2026-05):
- echohive42/AI-reads-books-page-by-page(~2.1k stars)— 亮点: prompt 显式黑白名单 + ANALYSIS_INTERVAL 阶段性摘要
- CaviraOSS/PageLM(~1.6k stars)— 亮点: 一份输入 → Cornell 笔记 + 闪卡 + 测验 + 播客 4 种产物 + non-overlapping 闪卡
- cognitivetech/ollama-ebook-summary(~619 stars)— 亮点: 按 ToC 章节切 + 2000 token 黄金块 + 输入/输出长度比异常检测

### 10.14 用新方法论回审第一本(2026-05-01)

用 §10.13 的 5 条审视已完成的第一部分卡片(C-S1-001..010),发现 **chunk 002 第 4 章《5 种盛行的肠绞痛理论》整章未充分挖掘**——Karp 反驳了 5 种流行误解,这些是**反直觉/误解纠正型**高价值卡(符合 §10.11)。

**新增 2 张第一部分卡片**:

- C-S1-011 胀气不是哭闹元凶,别狂拍嗝(B 级,Illingworth 1954 XX 光研究 + 多项打嗝药水否定研究)
- C-S1-012 妈妈焦虑不会让宝宝更哭闹(C 级,Karp"婴儿读不懂心思"论点,直击中国妈妈"我太焦虑害宝宝"的自责)

**第一部分总数 10 → 12 张**。包裹 3 张(原 _drafts_part2/)启动第二部分时从 ID 013 起。

**未来回审建议**:每本书 Phase 1 完成后,跑一次"§10.13 五条审视",尤其挖掘"反驳流行误解"类章节(Karp 第 4 章这种)——这种章节常被先验清单漏掉。

---

*v1.0 完。执行中发现本文档不清楚处,写入 `00-meta/questions_for_user.md`,不要瞎拍板。*
*v1.1 — §2.5 白话风格(2026-05-01)*
*v1.2 — §10 实战调整 12 条 + 数据修正(2026-05-01)*
