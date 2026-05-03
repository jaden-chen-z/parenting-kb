# 审计提示词 · 两本书 96 张卡 + 60 张术语卡(v1.0 · 2026-05-02)

> 给新 session 用 — 直接 copy 整段(从 `# 任务` 开始到末尾)粘贴到 Claude Code 即可启动审计。
> 你是审计员,不是产卡员 — **不许新建知识卡 / 不许改卡内容**(除非明确标记需修)。
> 仅产出审计报告 + 必要的元数据修复(如补 glossary_refs / 修字数超限)。

---

# 任务

你正在审计一个育儿知识库的 **96 张知识卡 + 60 张术语卡**。这些卡是过去 2 个 session 产出的,用户希望系统检查质量 + 一致性。

## 项目结构(自查)

```
~/Desktop/parenting-kb/
├── 00-meta/
│   ├── PHASE1_KARP.md          # Phase 1 任务书(Karp 单本)
│   ├── PHASE2_AAP.md           # Phase 2 任务书(AAP,含 §2.6/2.7/2.8/2.9 规则)
│   ├── progress.md             # 当前进度
│   └── checkpoints/
│       ├── checkpoint_PHASE1_KARP_20260501.md
│       ├── checkpoint_PHASE2_AAP_20260502.md   # ← 看这份了解全本产出
│       └── audit_prompt_96_cards.md             # ← 本文件
├── 30-cards/                   # 知识卡(96 张)
│   ├── INDEX_BY_SOURCE.md      # 完整索引
│   ├── s1-newborn/             # 67 张
│   ├── s2-1to3mo/              # 7 张
│   ├── s3-3to6mo/              # 13 张
│   ├── s4-6to9mo/              # 5 张
│   └── s5-9to12mo/             # 7 张
├── 40-glossary/                # 术语卡(60 张)
│   ├── G-ABBR-*.yaml           # 21 张缩写
│   ├── G-PERSON-*.yaml         # 7 张人名
│   └── G-TERM-*.yaml           # 32 张专有名词
└── 10-sources/                 # SRC yaml + raw HTML
```

## 启动步骤(必读三件套)

1. 读 [`00-meta/PHASE2_AAP.md`](../PHASE2_AAP.md) **完整版**(尤其 §2.6 / §2.7 / §2.8 / §2.9 规则,这是审计标尺)
2. 读 [`00-meta/checkpoints/checkpoint_PHASE2_AAP_20260502.md`](checkpoint_PHASE2_AAP_20260502.md)(全本产出)
3. 读 [`30-cards/INDEX_BY_SOURCE.md`](../../30-cards/INDEX_BY_SOURCE.md)(96 张卡总览)

不要直接抓数据,先读完三件套。

---

## 审计 7 大维度

### 维度 1:Schema 一致性(v3.5)

每张卡必须有这些字段(按顺序):
```yaml
card_id / stages / tags / front (title + hook) / back (why_matters + what_to_do + failure_mode + evidence_level) / glossary_refs / citation / unit_ids / related_cards / language / status / created / updated
```

**检查**:
- 缺字段 / 字段顺序错乱 → 标记
- evidence_level 必须是 A / B / C 之一
- stages 必须是 list `[SX]`,不是字符串
- created / updated 日期格式 ISO

### 维度 2:字数上限(§2.2 + §2.7.3)

- `title` ≤ 15 字(中文,不含标点)
- `hook` 8-12 字(默认填,不能空)
- `why_matters` ≤ 130 字(放宽自 80 → 130)
- `what_to_do` 每条 ≤ 30 字 × 3-5 条
- `failure_mode` ≤ 80 字
- 背面合计 ≤ 360 字

**检查**:超限就标"需精简",列具体超几个字。

### 维度 3:前情提要(§2.7,关键)

`why_matters` 开头必须 2 句:
- 第 1 句:**关键概念定义**(白话,如"包裹(swaddle)= 用薄布把宝宝紧裹成蚕蛹状")
- 第 2 句:**背景数字 / 严重性 / 历史**(如"SIDS 美国每年约 3500 例")

然后才进入核心主张。

**检查**:开头是否直接进核心,缺前情提要 → 标"需补前情"。

### 维度 4:白话风格(§2.5)

- 主语用"宝宝/你",不用"新生儿/父母/婴儿"(术语必须时除外)
- 主动动词,不用被动
- 一句话讲一件事,不堆叠从句
- 数字保留(月龄/剂量/分贝)
- 念出来不像药品说明书 / 学术论文

**检查**:抽样几张读出声,标"学究化"卡。

### 维度 5:glossary_refs 完整性(§2.8 + §2.9)

对每张知识卡:
1. 扫描正文(why_matters + what_to_do + failure_mode)用到的术语 / 缩写 / 人名
2. 对照该卡 `glossary_refs` 字段
3. 检查 40-glossary/ 是否已有对应术语卡
4. 列出缺失:"卡 X 用了 Y 但 glossary_refs 没列"

**审计原则**(§2.9.3):
- glossary_refs 字段不展示给用户(后台元数据),所以宁可多列
- 同一术语在正文出现多次,渲染层每次都转链接 — 与 audit 无关(渲染层职责)

### 维度 6:citation 完整性

每张卡 `citation` 必须有:
- `page_title` / `publisher` / `portal` / `page_url_primary` / `accessed` / `language` / `location` / `source_id`
- AAP 卡 source_id 应在 SRC-004 ~ 008
- Karp 卡 source_id 应是 SRC-003

**检查**:缺字段 / source_id 错配 → 标记。

### 维度 7:跨卡一致性(高级)

抽样检查"同一主题在多张卡里说法一致":
- C-S1-022(Karp)vs C-S1-039(AAP)vs C-S1-051(AAP):奶嘴月龄是否一致(都说"母乳建立后")
- C-S1-016(Karp)vs C-S1-034(AAP):仰睡立场是否一致
- C-S1-028(Karp)vs C-S1-037(AAP):共睡立场(用户决定先不解,但内容自身要清晰)
- 数字一致:67× / 50% / 90% 这些数字在多张卡里出现是否一致

**检查**:数字 / 立场 / 月龄阈值在跨卡之间出现差异 → 标"需对齐"。

---

## 审计输出格式

写一份 `00-meta/checkpoints/audit_report_96_cards_<日期>.md`,结构:

```markdown
# 96 张卡审计报告(<日期>)

## 总评分
- Schema 一致性:X/96 通过
- 字数:X/96 合规
- 前情提要:X/96 合规
- 白话风格:X/96 合规
- glossary_refs:X/96 完整
- citation:X/96 完整
- 跨卡一致性:N 处冲突

## 维度 1 · Schema 不合规清单
- C-X-X:缺 X 字段 / 顺序错
- ...

## 维度 2 · 字数超限清单
- C-X-X:why_matters 145 字(超 130)
- ...

## 维度 3 · 前情提要缺失清单
- C-X-X:开头直接进主张,缺概念定义
- ...

## 维度 4 · 白话风格问题清单
- C-X-X:某句"学究化",建议改写

## 维度 5 · glossary_refs 缺失清单
- C-X-X:正文用了"X"但 glossary_refs 没列(术语卡 G-XXX 已存在)
- C-X-X:正文用了"X"但术语卡 G-XXX **不存在**(需新建术语卡 / 或决定不建)

## 维度 6 · citation 不完整清单
- C-X-X:缺 source_id / location

## 维度 7 · 跨卡冲突清单
- 主题 X:卡 A 说 X,卡 B 说 Y,数字不一致 / 立场冲突
- ...

## 修复建议
- 立即修(影响渲染 / 错字 / 字数小超):列具体 Edit 计划
- 待用户决定(立场冲突 / 重写整段):列问题 + 建议方向

## 总结
- 总体质量评分:X/10
- 建议下一步:[Phase 3 启动 / 先批量修 / 重写某几张]
```

---

## 审计执行流程(给新 session 自己用)

1. 读必读三件套(15-20 分钟)
2. **批量 Read 96 张卡**(用 grep / Bash 提取关键字段,不必逐张完整读 — 只看需审字段)
3. **批量 Read 60 张术语卡的 display_name**(为 glossary_refs 完整性 audit 做参考)
4. 维度 1-6 逐一检查,记录问题
5. 维度 7 抽样检查(选 5-10 个核心主题做跨卡对照)
6. 写审计报告
7. 报告里**列具体 Edit 计划**(可立即修的,标好 anchor + new content)
8. 大改动 / 立场冲突 / 重写整段 → 列问题给用户决定,**不要自己改**

---

## 重要边界

- **不许新建知识卡**(96 张是终态,如发现漏 → 列入 gaps,不补)
- **不许重写卡内容**(除非用户审完明确说"改这张")
- **可以修小问题**(字数小超 / 缺 glossary_refs / 错字)— 用 Edit 工具逐张
- **可以新建术语卡**(如果发现高频术语缺卡)— 按 §2.8 schema 写到 40-glossary/
- 审计完成后 → 把 report 给用户 → 等用户拍板下一步

---

## 用户偏好(从 Phase 1+2 沉淀)

- 一次审小批,不喜欢一次性 96 张倾倒 → 报告分维度,一次审 1 维度
- 卡片白话至上,见学究腔会直接打断
- 关心方法论可证伪("你怎么知道没漏")→ 主动给"扫描了 X 个 vs 有 Y 个"对照数据
- 不接受"凭训练记忆生成",所有发现要挂 file path / line number

---

*v1.0 · 2026-05-02 — 给 96 卡审计 session 用*
