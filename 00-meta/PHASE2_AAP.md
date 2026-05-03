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

### 2.6 翻译两步走 + 缩写/人名规则(v1.1 新增 · 2026-05-02)

**背景**:Phase 2 AAP 卡(英文源)实战中,从英文 verbatim 直译损失白话度;缩写不友好;人名缺身份注释。沉淀此规则。

#### 2.6.1 翻译两步走工作流

**第一步 (English skeleton)**:从 verbatim 提炼英文 5 字段骨架
- title_en (≤ 8 words) / why_en (≤ 80 words) / what_en bullets / failure_en / hook_en
- 目的:确保事实精确 + 结构紧凑,不掺杂中文翻译噪音

**第二步 (Chinese 白话改写)**:按中文家长习惯**改写**,不是直译
- 标题 ≤ 15 字,hook 8-12 字
- why_matters ≤ 80 字,what_to_do 每条 ≤ 30 字 × 3-5 条
- failure_mode ≤ 80 字
- 数字保留(月龄 / 剂量 / 分贝 / 百分比)
- 长定语句 → 拆短句;学术词 → 口语词
- 写完念一遍,不像药品说明书或学术论文

#### 2.6.2 缩写规则

知识内容部分(front / back)**保留缩写**(如 SIDS, GERD, BLW),不为了让中文用户懂而打断行文展开。

在 citation 之前新增 `glossary:` 字段,列该卡用到的所有缩写:

```yaml
glossary:
  abbreviations:
    - SIDS: 婴儿猝死综合征(Sudden Infant Death Syndrome)
    - GERD: 胃食管反流病(Gastroesophageal Reflux Disease)
```

主词典在 [`00-meta/glossary.yaml`](glossary.yaml)(单一真相源,卡片 glossary 块从此处复制需要的项)。

#### 2.6.3 人名规则

知识内容中**保留姓**(如 Karp),不强行打断行文写全名。

在 `glossary:` 字段下 `people:` 子项列该卡引用的人名,格式 `姓: 全名 · 身份`:

```yaml
glossary:
  people:
    - Karp: Harvey Karp · 美国儿科医生,《卡普新生儿安抚法》作者
```

#### 2.6.4 专有名词规则

英文专业词第一次出现可用"中文(英文)"格式:
- 例:"后奶(hindmilk)"、"幽门狭窄(pyloric stenosis)"
- 例外:已是常用中文术语的不必标(如"母乳"、"配方奶")

复杂概念(需要 1 句解释才能懂)在 `glossary:` 字段下 `terms:` 子项加解释:

```yaml
glossary:
  terms:
    - 头发止血带综合征: 头发或细线缠绕婴儿手指/脚趾,可能切断血流甚至坏死
```

#### 2.6.5 卡片 yaml 完整 schema 修订(v3.4 · 2026-05-02)

```yaml
card_id: ...
stages: [...]
tags: [...]

front:
  title: ...        # 知识内容保留缩写/姓,不打断行文
  hook: ...

back:
  why_matters: ...
  what_to_do: ...
  failure_mode: ...
  evidence_level: ...

# 新字段:术语注释(在 citation 之前)— 卡片自包含
glossary:
  abbreviations:    # 该卡用到的缩写(可选,有就列)
    - SIDS: 婴儿猝死综合征(Sudden Infant Death Syndrome)
  people:           # 该卡引用的人名(可选,有就列)
    - Karp: Harvey Karp · 美国儿科医生,《卡普新生儿安抚法》作者
  terms:            # 该卡用到的专有名词(可选,有就列)
    - 头发止血带综合征: 头发或细线缠绕婴儿手指/脚趾,可能切断血流甚至坏死

citation:
  ...
```

`glossary` 三个子字段都可选,有需要才列;主词典 [`00-meta/glossary.yaml`](glossary.yaml) 是真相源。

### 2.7 前情提要规则(v1.2 新增 · 2026-05-02)

**背景**:用户反馈:"卡片一上来就说'很多人以为包紧能防 SIDS',谁能理解你在说什么?" — 卡片不能假设读者已知背景。

**规则**:每张卡必须**自包含**,`why_matters` 开头先做 2 句前情提要,再进入核心主张。

#### 2.7.1 前情提要包含什么

- **关键概念定义**(1 句):用最白话方式解释卡片标题里的核心词
  - 例:"包裹(swaddle)= 用薄布把宝宝紧裹成蚕蛹状,模拟子宫"
  - 例:"SBS(摇晃婴儿综合征)= 用力摇晃造成的脑出血,可能致死"
- **背景数字 / 严重性 / 历史**(1 句):让读者明白"为什么这件事值得花 60 秒读"
  - 例:"SIDS 美国每年约 3500 例,1 岁内最大死因之一"
  - 例:"老建议'推迟引入花生到 3 岁',但 LEAP 研究(2015)证明早引入反而预防 81% 过敏"

#### 2.7.2 然后才进入核心主张

- 核心主张 = 卡片要传达的关键观点 + 反直觉点 + 具体警告

#### 2.7.3 字数约束放宽(覆盖 PHASE1 §2.2)

- `why_matters`:从 ≤ 80 字 放宽到 **≤ 130 字**(40 字前情提要 + 90 字核心)
- 背面正文合计:从 ≤ 310 字 放宽到 **≤ 360 字**
- 其他字段不变(`title` ≤ 15 字 / `hook` 8-12 字 / `failure_mode` ≤ 80 字 / `what_to_do` 每条 ≤ 30 字 × 3-5 条)

#### 2.7.4 例外:何时可以省略前情提要

只有当卡片标题本身已经是完整自解释(读完标题就知道在说什么),且不涉及任何专业概念 / 数字 / 历史背景时,才可以省略前情提要。
- 例外少见。**默认必须写前情提要**。

#### 2.7.5 适用范围

- ✅ 所有新卡(R4 / R5 + 后续书)必须按此规则写
- ✅ 已有 37 张 AAP 卡需 refactor 时一并补前情提要
- ✅ Karp 33 张未来整合 refactor 时也补

### 2.8 术语卡片化(v1.3 新增 · 2026-05-02)

**背景**:用户决定把所有书的专有名词 / 缩写 / 人名做成独立卡片,知识卡引用术语 ID,渲染层做可点击链接 + 弹窗显示。

#### 2.8.1 文件结构 + ID 规则

```
40-glossary/                        # 新顶级目录(平级 30-cards)
├── G-ABBR-SIDS.yaml                # 缩写:G-ABBR-<exact-uppercase>
├── G-ABBR-AAP.yaml
├── G-PERSON-Karp.yaml              # 人名:G-PERSON-<Surname>
├── G-PERSON-Brazelton.yaml
├── G-TERM-swaddle.yaml             # 专有名词:G-TERM-<lowercase-slug>
├── G-TERM-pyloric-stenosis.yaml
└── INDEX.md                        # 字母索引(后期生成)
```

#### 2.8.2 术语卡 yaml schema (v1.0)

```yaml
glossary_id: G-ABBR-SIDS
type: abbreviation                  # abbreviation / person / term
display_name: SIDS                  # 在知识卡正文里显示的形式

full_name_en: Sudden Infant Death Syndrome
full_name_zh: 婴儿猝死综合征

one_liner: |                        # 1-2 句简短解释(弹窗顶部直接显示)
  ...

detail: |                           # 完整背景 markdown(弹窗展开后显示)
  ## 定义
  ...
  ## 流行病学
  ...
  ## 历史
  ...

key_facts:                          # 关键事实清单(可选,< 5 条)
  - ...

related_glossary:                   # 相关术语 ID(术语卡之间也互链)
  - G-ABBR-SBS
  - G-TERM-back-sleep

related_cards:                      # 引用本术语的知识卡 ID(可后期回填)
  - C-S1-016
  - C-S1-038

sources:                            # 引用源
  - source_id: SRC-XXX
  - external: 维基百科 / CDC / 综合医学常识

language: zh
status: draft
created: 2026-05-02
updated: 2026-05-02
```

#### 2.8.3 知识卡引用术语卡的方式

知识卡 yaml 的 `glossary` 字段(v3.4)→ 改为 `glossary_refs`(v3.5):

**Old (v3.4) — 内联展开**:
```yaml
glossary:
  abbreviations:
    - SIDS: 婴儿猝死综合征(Sudden Infant Death Syndrome)
  people:
    - Karp: Harvey Karp · 美国儿科医生...
```

**New (v3.5) — 引用术语 ID**:
```yaml
glossary_refs:                      # 扁平 list,不分类
  - G-ABBR-SIDS
  - G-ABBR-AAP
  - G-PERSON-Karp
  - G-TERM-swaddle
```

**渲染层职责**:
- 知识卡正文里 SIDS / Karp / swaddle 等词自动转可点击链接
- 点击 → 弹窗 → 显示术语卡的 `one_liner`(顶部)+ `detail`(展开)
- 术语卡之间(`related_glossary`)也互链,可在弹窗内继续跳转

#### 2.8.4 迁移路径

1. **样本** (本次):5 张代表术语卡(SIDS / DDH / LEAP / Karp / swaddle)→ 用户审风格
2. **批量生成** (用户审过后):基于 [`00-meta/glossary.yaml`](glossary.yaml) 现有 52 个条目 → 生成 52 张术语卡(补 detail / key_facts / related_*)
3. **知识卡 refactor**:37 张 AAP 卡的 `glossary` → `glossary_refs`(批量)
4. **R4 / R5 直接用 v3.5 schema**(`glossary_refs`)
5. **Karp 33 张**:未来整合时 refactor 同样改

#### 2.8.5 主词典 glossary.yaml 命运

- 短期:`glossary.yaml` 仍保留作为快速一览(条目精简版)
- 长期:`glossary.yaml` 废弃,术语卡是唯一真相源,加 `40-glossary/INDEX.md` 字母索引

### 2.9 知识卡 inline 引用渲染(v1.4 新增 · 2026-05-02)

**背景**:卡片正文常引用其他卡片(如"见 C-S3-006")。用户希望这些引用变可点击 → 弹窗显示被引卡内容,跟术语卡 `glossary_refs` 弹窗同款交互。

#### 2.9.1 引用格式(yaml 内不变)

知识卡正文(`why_matters` / `what_to_do` / `failure_mode` / `failure_mode`)中**保留 ID 文本**:
- 标准格式:`C-S<段>-<3 位编号>`(如 `C-S3-006` / `C-S5-002`)
- yaml schema **无需改动** — 现有 inline 写法照常
- 术语卡引用同理:`G-ABBR-XXX` / `G-PERSON-XXX` / `G-TERM-XXX` 在正文出现也变链接

#### 2.9.2 渲染层行为

**两种引用机制不同**:

**A. 知识卡引用 — ID 直接匹配**
- 正文里**直接写 ID**(如 "见 C-S3-006")
- 渲染层正则 `C-S\d+-\d+` 匹配 → 转链接
- 点击 → 弹窗:title + hook + why_matters 简版 + "查看完整卡"按钮

**B. 术语卡引用 — glossary_refs 列表 + display_name 匹配**
- 正文里写 human-readable 词(如 "SIDS" / "AAP" / "Karp" / "产后抑郁"),**不写 G-ID**
- 渲染层流程:
  1. 读卡片 `glossary_refs` 字段(如 `[G-ABBR-AAP, G-PERSON-Karp, G-TERM-postpartum-depression]`)
  2. 对每个 ref,fetch 对应术语卡的 `display_name`(AAP / Karp / 产后抑郁)
  3. 在正文里搜该 display_name 字符串,转链接
- 点击 → 弹窗:display_name + one_liner + detail 简版 + "查看完整卡"按钮

**为什么这样设计**:
- 正文保持 human-readable(读起来流畅,不是一堆 G-ID 噪音)
- `glossary_refs` 显式列出"该卡用了哪些术语" → 渲染层不需要 fuzzy match 全词典(快 + 准)
- 卡片底部**不重复术语解释**(弹窗就是注释,glossary_refs 就是清单)

弹窗内的链接也可继续点击(深度跳转)。

#### 2.9.3 渲染原则(必须遵守)

**A. glossary_refs 字段本身不展示给最终用户**
- yaml 源文件里有 `glossary_refs:` 字段,但渲染后的卡片视图(给父母看的最终界面)**不显示这个字段**
- glossary_refs 仅作为渲染层的索引元数据 — 用户在卡片底部看不到"专用名词清单"段落
- 同理 `related_cards` 字段也不直接渲染为列表(它是关联图元数据)
- 用户能看到的:title / hook / why_matters / what_to_do / failure_mode / citation 简版
- 用户看不到的:glossary_refs / related_cards / unit_ids / status / created / updated 等元数据

**B. 术语在正文中每次出现都是可点击链接**
- 例:正文出现"AAP"3 次 → 渲染时**3 个 'AAP' 都是链接**(不是只第一次)
- 例:正文出现"SIDS"5 次 → 5 个都可点击
- 不做"首次出现链接化,后续灰色"这种优化 — 用户随时回查
- 实现:渲染层用 global regex replace 替换所有匹配,不是只 first match

**C. 链接交互一致**
- 同一术语的所有链接,点击后弹同一个窗
- 弹窗内容由术语卡(40-glossary/G-XXX-XXX.yaml)决定 — 单一真相源

#### 2.9.3 与 yaml 字段的关系

- **`related_cards` 字段**(在 citation 后,现有):**保留** — 作为显式关联清单
  - 可能 inline 没出现但概念关联的卡也列在这
  - inline 已出现的 ID 也可重复列(冗余但便于扫描)
  - 双源互补:inline 是"读到这你可能想看",`related_cards` 是"完整关联图"

- **`glossary_refs` 字段**(术语引用,§2.8.3):**保留** — 同上逻辑
  - 显式术语清单 + inline 自动识别双源

- **不新增字段** — 渲染层主动识别 inline ID,yaml 不重复列

#### 2.9.4 渲染示例

**原文 yaml**:
```yaml
why_matters: |
  ...
  ① **铁缺乏 + 贫血筛查**(全员 — 见 C-S3-006)
  ② **牙医**(第一颗牙后 6 月内 — 见 C-S3-012)
  ...
```

**渲染效果**(伪 HTML):
```
① 铁缺乏 + 贫血筛查(全员 — 见 [C-S3-006](click))
                                  ↓ 点击
                              ┌──────────────────────────────┐
                              │ 📇 C-S3-006                  │
                              │ ──────────────────────────── │
                              │ 母乳宝宝 4 月起补铁,12 月查血    │
                              │ 母乳铁低,6 月起需求骤增          │
                              │                              │
                              │ AAP:4 月起母乳宝宝补 1 mg/kg/d │
                              │ 12 月儿保必查铁缺乏 + 贫血...    │
                              │                              │
                              │ [查看完整卡 →]                 │
                              └──────────────────────────────┘
```

#### 2.9.5 适用范围

- ✅ 所有现有 51 张知识卡(渲染时自动生效,无需改 yaml)
- ✅ 所有现有 56+ 术语卡(同样自动)
- ✅ 所有新卡(R5 + 后续书)按现有 inline 写法即可

#### 2.9.6 实现路径(给前端)

- **Obsidian**:写自定义插件用正则匹配 + Modal 渲染弹窗
- **Web**:渲染时把 ID 替换为 `<a class="card-link" data-id="C-S3-006">C-S3-006</a>`,JS 监听 click → fetch yaml → 弹窗
- **Markdown export**:把 ID 替换为 `[[C-S3-006]]` 标准 wiki link 格式,任何兼容工具都能跳转

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
