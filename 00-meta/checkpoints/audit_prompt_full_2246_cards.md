# 审计提示词 · 全库 24 SRC / 2,246 卡 全维度体检(v1.0 · 2026-05-04)

> 给新 session 用 —— 直接 copy 整段(从 `# 任务` 开始到末尾)粘贴到 Claude Code 即可启动审计。
> 你是审计员,**不是产卡员** —— 仅产出审计报告 + 元数据修复(merge 标记 / related_cards / 字数压缩 / tags 修正)。**不创建新知识卡**,**不重写卡片正文**(除非明确字数超限或乱字)。
> **本审计涵盖全库** —— 包括前次 491 卡审计已审过的 10 SRC + 14 个新 SRC。前次报告(`audit_report_491_cards_20260503.md`)是输入,不是替代;本次重做完整 dedup 因为新卡可能与已审卡冲突。

---

# 任务

育儿知识库现有 **1,437 张知识卡 + 809 张术语卡 = 2,246 卡**,跨 **24 个 SRC + 9 段(S0-S8)**。

**用户首要诉求**:
1. ⭐ 找内容近似的卡合并(跨源 + 同源都查)
2. 找表达不清 / 学究腔 / 含糊
3. 其他卡级问题

**审计员加 5 个维度**(本任务书新增,见 §3 维度 5-9):
- 术语卡孤儿检测(809 卡多少有引用)
- 跨段一致性(同概念跨段描述偏移)
- 可操作性(what_to_do 空话率)
- 红旗信号链完整性(月龄链断点)
- stage 错位 + 双向链断裂 + 索引漂移(三个一起查)

## 🔓 一次性权限请求(开头一次性确认)

向用户请求以下工具的全部权限,之后**不打扰**:

| 工具 | 用途 |
|---|---|
| Bash | grep / find / wc / 自检脚本 / yq 索引核对 |
| Read | 卡片 / 规范 / 索引 |
| Edit | 修元数据(字数压缩 / glossary_refs / related_cards / tags / merge 标记) |
| Write | 审计报告 / merge_candidates.md / 各维度子报告 / audit_log |
| Agent(Task)| spawn subagent 分批审 |
| TodoWrite | 进度跟踪 |

**只在以下场景例外打断用户**(写 questions_for_user 后**继续跑**,不阻塞):
- 两张卡 100% 完全相同需用户决定保留哪张
- 立场显著反转需用户拍板
- L1 自动合并涉及超过 5 张卡的大簇(降低误合风险)

---

## 1. 全部范围

### 24 SRCs / 1,437 知识卡

| SRC | 来源 | 卡数 | 是否前次审过 |
|---|---|---|---|
| SRC-003 | Karp 卡普 | 34 | ✅ |
| SRC-004~008 | AAP cluster × 5 | 63 | ✅ |
| SRC-009 | 鲍秀兰 | 88 | ✅ |
| SRC-010 | Brazelton | 83 | ✅ |
| SRC-011 | Bowlby V1 | 38 | ✅ |
| SRC-012 | Bowlby V2 | 32 | ✅ |
| SRC-013 | Wonder Weeks | 35 | ✅ |
| SRC-014 | Davies | 49 | ✅ |
| SRC-015 | Gopnik | 35 | ✅ |
| SRC-016 | Lillard | 56 | ✅(部分)|
| **SRC-017** | Bowlby V3 | 15 | ❌ |
| **SRC-018** | Stern | 44 | ❌ |
| **SRC-019** | Lansbury | 43 | ❌ |
| **SRC-021** | Gerber A | 35 | ❌ |
| **SRC-022** | Gerber B | 49 | ❌ |
| **SRC-023** | 松田 A | 49 | ❌ |
| **SRC-024** | 松田 B | 48 | ❌ |
| **SRC-025** | NRC Shonkoff | 68 | ❌ |
| **SRC-026** | Pikler 德 | 42 | ❌ |
| **SRC-027** | Lerner V3 | 69 | ❌ |
| **SRC-028** | Lerner V2 | 48 | ❌ |
| **SRC-029** | Lerner V4 | 93 | ❌ |
| **SRC-030** | Lerner V1 | 95 | ❌ |
| **SRC-031** | WHO+UNICEF | 65 | ❌ |
| **SRC-040** | Murkoff 海蒂 | 121 | ❌ |

### 9 段(S0-S8)/ 1,437 知识卡 + 809 术语卡

```
s0-pregnancy   ~106
s1-newborn     ~182
s2-1to3mo      ~115
s3-3to6mo      ~110
s4-6to9mo      ~109
s5-9to12mo     ~129
s6-12to24mo    ~230
s7-24to36mo    ~147
s8-3to6yr       ~99
40-glossary    ~809  (G-ABBR / G-PERSON / G-TERM)
```

---

## 2. 项目结构(自查)

```
~/Desktop/parenting-kb/
├── 00-meta/
│   ├── README.md                        # 总任务书 v3.0
│   ├── PHASE1_KARP.md                   # 卡片规范 v3.3 (§2 / §2.5 白话 / §10 14 条)
│   ├── PHASE2_AAP.md                    # v1.4 (§2.6-2.9)
│   ├── PHASE3-14 多份任务书              # 各 Phase 教训
│   ├── progress.md                      # 当前进度
│   ├── conflicts.md                     # 18+ 项已识别(prev audit + Phase 11/12 H/I/J 节)
│   ├── gaps.md                          # P0/P1/P2 缺口清单
│   └── checkpoints/
│       ├── audit_report_491_cards_20260503.md           # ⭐ 前次审计(参考)
│       ├── audit_prompt_447_cards.md                    # 前次提示词(参考)
│       ├── audit_prompt_remaining_cards.md              # 中间版提示词(已被本文件覆盖)
│       └── audit_prompt_full_2246_cards.md              # ← 本文件
├── 30-cards/                            # 1,437 张知识卡
│   ├── INDEX_BY_SOURCE.md               # 全卡索引
│   └── s0-s8 ...
└── 40-glossary/                         # 809 张术语卡
```

---

## 3. 9 大审计维度

### 维度 1 · ⭐ 内容近似 / 合并候选(用户首要诉求)

**判定 4 级 + 1 个延伸**:

| 级 | 判定 | 处理 |
|---|---|---|
| **L1** 完全重复 | front.title 80%+ 重叠 + back 主张完全一致 | 自动 Edit 加 `merge_into: C-XXX`;keeper 选 evidence 高的;**审计员可直接标** |
| **L2** 实质重复(可合并)| 主张相同,只是来源不同 | 标 `merge_candidate: true` + `merge_with: [C-XXX]`;**待用户拍板** |
| **L3** 互补(应互链不合)| 同主题不同立场 / 不同维度 | 双向 Edit `related_cards`(若缺) |
| **L4** 表面像本质不同 | 关键词撞但论点不同 | 留报告备注,不动卡 |
| **L1.5** 同 SRC 内部重复 | 同书内部章节描述同一现象 | **新增** — 标 `merge_into` keeper 取在前出现的 |

**5 个 hotspot 重点查**:

1. **Gerber 双 SRC 内部 dedup**(SRC-021 vs 022 — 同书并行 session)
2. **松田双 SRC 内部 dedup**(SRC-023 vs 024 — 同书并行)
3. **Lerner V1-V4 跨卷重叠**(95+93+69+48 = 305 张,内部跨卷必有重复)
4. **NRC × Lerner 元理论重叠**(Bronfenbrenner / dynamic systems / lifespan / 突触修剪 等)
5. **Stern × Bowlby × Brazelton 婴儿心理学三角重叠**(self / attunement / mutual regulation / mirroring 等)

### 维度 2 · 表达不清 / 风格

按 PHASE1_KARP §2.5:

| 问题 | 处理 |
|---|---|
| 学究腔("持续暴露于多感官刺激")| Edit 重写 |
| 主语不当("新生儿"/"父母")| Edit 改"宝宝/你" |
| 被动堆叠("被运动刺激")| Edit 改主动 |
| 一句话 >2 个"和" | Edit 拆句 |
| 数字消失变"较高比例" | Edit 还原数字 |

**自检**:每张卡 `back` 大声念,听起来像论文摘要 → 重写。

### 维度 3 · 字数 / schema 合规

| 字段 | 上限 |
|---|---|
| `front.title` | 15 字 |
| `back.why_matters` | 80 字 |
| `back.what_to_do` 每条 | 30 字 |
| `back.what_to_do` 总 | 150 字 |
| `back.failure_mode` | 80 字 |
| 背面正文合计 | 310 字 |

超 → 审计员直接 Edit 压缩,**不改主张**。

### 维度 4 · 元数据完整性

- citation 5 字段(book_title_en/zh / authors / year / location / source_id)全填?
- failure_mode 不能空
- tags 漏标 / 误标(safety / philosophy / controversy / red_flag)
- evidence_level 诚实(A 需 ≥2 Tier 1+综述 / B 需 1 Tier 1+单项研究 / C 仅 philosophy)
- glossary_refs 内联未抽离
- hook 不能空 / 描述型(§10.10)

### ✨ 维度 5 · 术语卡孤儿率(本任务新增)

**判定**:809 张 G-* 术语卡里多少有 ≥1 张知识卡通过 `glossary_refs` 引用?

```bash
# 方法
1. ls 40-glossary/*.yaml → 列 G-ID
2. grep "G-XXX" 30-cards/ → 计数引用
3. 输出孤儿清单 + 引用密度直方图
```

**严重度**:
- 孤儿率 > 10% = 知识卡 glossary_refs 不到位(P1)
- 孤儿率 > 30% = 系统性问题,术语卡批量重复或废卡(P0)

**自动修复**:孤儿术语卡 Edit 加 `orphan: true` 标记,不删。在主报告里列 + 建议:用户决定删 / 保留 / 重链。

### ✨ 维度 6 · 跨段一致性(本任务新增)

**判定**:同一概念跨段(如"应答式互动" S0 出现 vs S5 出现 vs S7 出现)的描述是否一致?evidence_level 是否漂移?跨派立场是否冲突?

**重点查 5 个跨段概念**:
1. **应答式互动 / Serve and Return**(SRC-002 + SRC-014 + 多源)
2. **依恋 / Attachment**(SRC-011/012/017 + Stern + 鲍秀兰 + Brazelton)
3. **关键期 / 敏感期**(蒙氏 vs Hubel-Wiesel vs Bowlby)
4. **自我调节 / 共调节**(Stern + Brazelton + Lerner V3)
5. **物体永久性**(Piaget 经典 vs Spelke / Gopnik 早期版)

每个查:卡片在不同段是否描述漂移?核心数字 / 月龄是否一致?如不一致,写报告。

### ✨ 维度 7 · 可操作性(本任务新增)

**判定**:`what_to_do` 是否真"可执行"?抽样审"空话率"。

**典型空话**:
- "重视沟通" / "多陪伴" / "营造安全环境" / "尊重宝宝节奏"

**典型可执行**:
- "每次喂奶后竖抱拍嗝 3-5 分钟"
- "12-18 月戒奶瓶,先撤夜奶,7-10 天换 sippy"

**抽样**:每个 SRC 抽 5 张,统计空话率。> 30% = P1 警告。

报告每 SRC 空话样例 1-3 个 + 建议改写方向。

### ✨ 维度 8 · 红旗信号链完整性(本任务新增)

**判定**:gaps.md 提到的红旗月龄链(0-1 / 2-3 / 6 / 9 / 12 / 18 / 24 / 36 月)是否每个月龄都有 `red_flag` tag 卡?

```bash
# 方法
for stage in s0..s8:
  count cards with tag "red_flag" in stage
```

发现的断点:
- 哪个月龄没 red_flag 卡 = gap
- 哪个月龄红旗清单不全(漏症状)= 内容 gap

不补卡(本审计员不创新卡),写 gaps.md 追加。

### ✨ 维度 9 · 索引一致性 + 双向链 + stage 错位(三合一)

#### 9a. source_index ↔ 实际卡片 漂移

```bash
# 检查每 SRC referenced_by_cards 列表
for src in source_index['sources']:
  registered = src['referenced_by_cards']
  actual = grep "source_id: ${src.id}" 30-cards/
  diff registered vs actual → 列漂移
```

漂移 → 自动 Edit source_index 修齐。

#### 9b. 双向 related_cards 完整性

```bash
# A 卡 related [B] 但 B 卡 related 没 A → 单向链
for card in 30-cards:
  for related in card.related_cards:
    check related.related_cards contains card → 否则单向
```

单向链 → 自动 Edit 补反向。

#### 9c. stage 错位

卡 ID `C-S5-XXX` 但内容是 18 月+ 事(应 S6)?抽样查标题 vs 内容月龄。

错位 → 报告标记,**不动卡**(rename 风险大),建议用户后续手工迁移。

---

## 4. 工作流(防 token 爆炸)

**2,246 卡的全库审计 — subagent 隔离是底线**。

### Phase A · 准备(主线,~10 分钟)

```
1. Read 00-meta/PHASE1_KARP.md §2 + §2.5 + §10
2. Read 00-meta/PHASE2_AAP.md §2.6-2.9
3. Read 00-meta/checkpoints/audit_report_491_cards_20260503.md(前次发现)
4. Read 00-meta/conflicts.md(已识别立场)
5. Read 30-cards/INDEX_BY_SOURCE.md(全卡片地图)
6. ls 40-glossary/ | wc -l + 抽 10 张看 schema
```

主上下文增长:< 50 KB。

### Phase B · 24 SRC 单源审(subagent × 24,~5-6 小时)

每 SRC 一个 subagent,prompt 模板:

```
任务:审 SRC-XXX 全部 N 张卡(列表 ...)
读规范: PHASE1_KARP §2.2 §2.5 §10 + PHASE2_AAP §2.6-2.9
检查 4 个 intrinsic 维度:
  维度 2 表达问题
  维度 3 字数 schema
  维度 4 元数据完整性
  维度 1.L1.5 同源内部 dedup
  维度 7 可操作性(每 SRC 抽 5 张审空话率)
返回 yaml:
  source_id: SRC-XXX
  total_cards: N
  intrinsic_issues: [{card_id, issue_type, severity, detail, suggested_fix}, ...]
  intra_source_dedups: [{cluster, level, action, keeper}, ...]
  vacuous_what_to_do: [{card_id, sample, fix}, ...]
  totals_per_issue: {...}
返回 ONLY yaml,字段名英文,无 preamble。
```

每 subagent 输出 ~5-15 KB,总 ~120-360 KB。

### Phase C · 9 段跨源 dedup(subagent × 9,~3-4 小时)

每段 1 个 subagent,审该段全部卡片(跨 24 SRC):

```
任务:审 stage S? 全部 N 张卡(跨 24 源)
做 1 件事:**找 merge candidate 簇**(L1/L2/L3/L4)
重点 5 个 hotspot(见任务书 §3 维度 1)
返回 yaml:
  stage: S?
  total_cards: N
  merge_clusters: [{topic, level, cards, keeper, reason, action_taken}, ...]
  hotspot_findings: {...}
返回 ONLY yaml。
```

9 段 × ~10 KB = ~90 KB。

### Phase D · 5 个新维度并行审(subagent × 5,~1-2 小时)

| Subagent | 维度 | 输出文件 |
|---|---|---|
| D1 | 维度 5 · 术语孤儿 | `glossary_orphans.yaml` |
| D2 | 维度 6 · 跨段一致 | `cross_stage_drift.yaml` |
| D3 | 维度 7 · 可操作性 全本扫 | `vacuous_actions.yaml` |
| D4 | 维度 8 · 红旗链 | `red_flag_chain.yaml` |
| D5 | 维度 9 · 索引漂移+双向链+stage错位 | `index_consistency.yaml` |

每 subagent 用 grep + 抽样,不读所有卡正文。

### Phase E · 主线汇总 + 自动修复(~1 小时)

整合 24 + 9 + 5 = 38 份子报告:

1. 自动 Edit 修明显问题:
   - L1 直接合(`merge_into`)
   - L1.5 同源合(`merge_into`)
   - 字数压缩
   - 缺 glossary_refs 补
   - 缺 related_cards 双向补
   - 错 tag 修
   - hook 描述型重写
   - source_index 漂移修
2. 标记 L2 / L3,**不动卡**
3. Write 主报告 `audit_report_full_2246_cards_YYYYMMDD.md`
4. Write `merge_candidates.md` —— L2 待用户拍板
5. Write `audit_log.md` —— 自动改动轨迹
6. 追加 conflicts.md / gaps.md(若发现)
7. 终端打印总结(§9 模板)

---

## 5. 输出

### 主报告

`00-meta/checkpoints/audit_report_full_2246_cards_YYYYMMDD.md`

格式:

```markdown
# 审计报告 · 全库 24 SRC / 2,246 卡 全维度体检

## 总评(数字)
- 范围: 24 SRC + 9 段 + 5 新维度
- 审计 1,437 知识卡 + 809 术语卡 = 2,246
- 自动修复: X 张卡(详见 audit_log)
- L1 直接合: X 簇
- L1.5 同源合: X 簇
- L2 待用户拍板: X 簇
- L3 互链补: X 对
- 表达问题修: X
- 字数压: X
- 元数据补: X
- 术语孤儿: X / 809
- 红旗链断点: X 个月龄
- 索引漂移: X 处 / 双向链单边: X 对 / stage 错位: X 张

## 维度 1 · 合并候选 (主菜)
[L1/L1.5/L2/L3 簇清单 + 5 hotspot 发现]

## 维度 2 · 表达问题
[per-source breakdown]

## 维度 3 · 字数合规
[超限统计 + 已压清单]

## 维度 4 · 元数据
[broken refs / missing fields / wrong tags / wrong evidence_level]

## 维度 5 · 术语孤儿
[孤儿清单 + 引用密度]

## 维度 6 · 跨段一致性
[5 跨段概念漂移报告]

## 维度 7 · 可操作性
[空话样例 + 建议]

## 维度 8 · 红旗链
[月龄链断点 + gaps.md 追加项]

## 维度 9 · 索引一致性
[漂移修复 + 单边链补 + stage 错位标记]

## conflicts.md / gaps.md 追加
[新发现]

## 待用户决策(P0)
[merge_candidates.md / 立场冲突 / stage 错位待迁移 / 等]
```

### 副产物

1. **`merge_candidates.md`** ⭐ 用户首要看(L2 簇待拍板)
2. `audit_log.md` —— 可回滚轨迹
3. `glossary_orphans.yaml` —— 术语孤儿清单
4. `cross_stage_drift.yaml` —— 跨段不一致
5. `vacuous_actions.yaml` —— 空话清单
6. `red_flag_chain.yaml` —— 红旗链状态
7. `index_consistency.yaml` —— 索引漂移 + 单边链 + stage 错位
8. `conflicts.md` 追加
9. `gaps.md` 追加

---

## 6. 边界

| ❌ 不要 | ✅ 应该 |
|---|---|
| 一次 Read 全 1437+809 卡到主上下文 | 严守 subagent 隔离 |
| 创建新知识卡 | 缺口写 gaps.md |
| 真删除卡 | 标记冗余,等用户最终拍板 |
| 重写卡片主张 | 只压字数 / 改 tone,不动论点 |
| 替用户选立场 | conflicts 只列各方(任务书 §0 #5)|
| 凭训练记忆补内容 | 任何主张追溯回某卡某源 |
| 跨 SRC 强行合卡(L3 互补不该合)| 严守 4 级判定 |
| 删除孤儿术语卡 | 标 `orphan: true`,等用户决定 |
| 自动迁移 stage 错位卡 | 标记报告,不重命名 |

---

## 7. 起步 5 分钟

```bash
cd ~/Desktop/parenting-kb

# 1. 看清规模
find 30-cards -name "*.yaml" | wc -l    # 1437
find 40-glossary -name "*.yaml" | wc -l  # 809

# 2. Read 规范文档(主线,见 §4 Phase A)

# 3. spawn 第一个 subagent (SRC-017 Bowlby V3 - 最小,15 卡 - 当 benchmark)
# 看输出质量 OK 后批量启动其余 23 个

# 4. Phase C 跨段 dedup (9 段,可并)

# 5. Phase D 5 新维度 (5 subagent 并行)

# 6. Phase E 主线汇总
```

---

## 8. 完成定义

- [ ] 24 个 SRC 全审(Phase B 输出 24 份)
- [ ] 9 个 stage 全跨段 dedup(Phase C 输出 9 份)
- [ ] 5 个新维度(Phase D 输出 5 份)
- [ ] **`merge_candidates.md`** ⭐(用户首要)
- [ ] `audit_report_full_2246_cards_YYYYMMDD.md` 主报告
- [ ] `audit_log.md` 列出所有自动修复
- [ ] 5 个新维度子报告 yaml(`glossary_orphans` / `cross_stage_drift` / `vacuous_actions` / `red_flag_chain` / `index_consistency`)
- [ ] conflicts.md / gaps.md 追加(若有)
- [ ] progress.md 加"全库 2246 卡审计完成"段
- [ ] 终端打印总结(§9 模板)+ 待用户决策清单

---

## 9. 终端总结模板(完工时打印)

```
========================================
全库 24 SRC / 2,246 卡 全维度体检完成
========================================
范围: 24 SRC × 9 段 × 9 维度

自动修复:
  L1 直接合: X 簇
  L1.5 同源合: X 簇
  字数压缩: X
  glossary_refs 补: X
  related_cards 双向补: X 对
  tags 修正: X
  evidence_level 调整: X
  hook 重写: X
  source_index 漂移修: X
  其他元数据: X

合并待拍板 (merge_candidates.md):
  L2 实质重复簇: X
  L3 互补已互链: X 对
  L4 表面像本质不同: X 簇(列报告)

5 hotspot 发现:
  Gerber 021 vs 022 内部: X
  松田 023 vs 024 内部: X
  Lerner V1-V4 跨卷: X
  NRC × Lerner: X
  Stern × Bowlby × Brazelton: X

5 新维度结果:
  术语孤儿: X / 809 (X%)
  跨段不一致: X 个概念漂移
  空话率: X 张 (建议改写)
  红旗链断点: X 个月龄
  索引漂移 X / 单边链 X / stage 错位 X

新增:
  conflicts.md 追加: X
  gaps.md 追加: X

待用户决策(P0):
  - merge_candidates.md X 簇拍板 ⭐
  - 立场冲突 X 项
  - 术语孤儿删/留 X 张
  - stage 错位卡迁移 X 张
========================================
```

---

*v1.0 完。9 个维度 / 24 SRC / 2,246 卡 / 38 份子报告 / 9 份产出 — 这是项目最深度体检。*
