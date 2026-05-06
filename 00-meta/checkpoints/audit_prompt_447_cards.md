# 审计提示词 · 9 本书 447 张知识卡 + 146 张术语卡(v1.0 · 2026-05-03)

> 给新 session 用 —— 直接 copy 整段(从 `# 任务` 开始到末尾)粘贴到 Claude Code 即可启动审计。
> 你是审计员,**不是产卡员** —— 不许新建知识卡 / 不许改卡内容(除非明确标记需修)。
> 仅产出审计报告 + 必要的元数据修复(如补 glossary_refs / 修字数超限 / 加 related_cards 互链)。

---

# 任务

你正在审计育儿知识库 **9 本书的 447 张知识卡 + 146 张术语卡**。9 本来源:

| # | 源 | SRC | 卡数 |
|---|---|---|---|
| 1 | Karp《卡普新生儿安抚法》 | SRC-003 | 33 |
| 2 | AAP HealthyChildren(5 cluster) | SRC-004~008 | 63 |
| 3 | 鲍秀兰《婴幼儿潜能开发》 | SRC-009 | 86 |
| 4 | Brazelton《Touchpoints: Birth to 3》 | SRC-010 | 79 |
| 5 | Bowlby V1《依恋》 | SRC-011 | 37 |
| 6 | Bowlby V2《分离》 | SRC-012 | 32 |
| 7 | Wonder Weeks《婴儿大脑跃迁》 | SRC-013 | 35 |
| 8 | Davies《The Montessori Baby》 | SRC-014 | 47 |
| 9 | Gopnik《Scientist in the Crib》 | SRC-015 | 35 |

8 个月龄段:**S0**(孕期)/ **S1**(0-1)/ **S2**(1-3)/ **S3**(3-6)/ **S4**(6-9)/ **S5**(9-12)/ **S6**(12-24)/ **S7**(24-36),**单位均为月**。

---

## 项目结构(自查)

```
~/Desktop/parenting-kb/
├── 00-meta/
│   ├── README.md               # 总任务书 v3.0(§0 硬规则 / §4 schema / §9 卡片质量)
│   ├── PHASE1_KARP.md          # 卡片规范 v3.3(§2 字段 / §2.2 字数 / §2.4 引用 / §2.5 白话风格 / §10 14 条实战)
│   ├── PHASE2_AAP.md           # v1.4(§2.6 翻译 / §2.7 前情提要 / §2.8 术语卡 / §2.9 inline 引用)
│   ├── PHASE3_BAOXIULAN.md / PHASE3_BOWLBY_VOL1.md
│   ├── PHASE4_WONDER_WEEKS.md / PHASE4_BOWLBY_VOL2.md
│   ├── PHASE5_MONTESSORI_BABY.md / PHASE5_GOPNIK.md
│   ├── progress.md             # 当前进度(以本文件中列表为准,progress 偶有滞后)
│   ├── conflicts.md            # ⚠️ 目前几乎空 —— 你的产出之一是丰富它
│   ├── gaps.md                 # 找不到的内容
│   └── checkpoints/
│       ├── audit_report_96_cards_20260502.md       # 上次 96 卡审计报告(参考)
│       ├── audit_prompt_96_cards.md                # 上次审计提示词(参考)
│       ├── checkpoint_PHASE3_BAOXIULAN_20260502.md
│       ├── checkpoint_PHASE3_BOWLBY_VOL1_20260503_audit.md
│       ├── checkpoint_PHASE3_BRAZELTON_20260502.md
│       ├── checkpoint_PHASE4_BOWLBY_VOL2_20260503_audit.md
│       ├── checkpoint_PHASE4_WONDER_WEEKS_20260503.md
│       ├── checkpoint_PHASE5_DAVIES_AUDIT_20260503.md
│       ├── checkpoint_PHASE5_GOPNIK_20260503.md
│       ├── checkpoint_PHASE5_MONTESSORI_BABY_20260503.md
│       └── audit_prompt_447_cards.md               # ← 本文件
├── 10-sources/
│   ├── source_index.yaml       # 全部 SRC 索引(SRC-001~015,SRC-016 Lillard 进行中)
│   └── tier3-books/notes/SRC-{003,009-015}.yaml   # 源 metadata
├── 30-cards/                   # 知识卡(447 张)
│   ├── INDEX_BY_SOURCE.md      # 完整源 → 卡片映射
│   ├── s0-pregnancy/   (11)
│   ├── s1-newborn/     (115)
│   ├── s2-1to3mo/      (47)
│   ├── s3-3to6mo/      (51)
│   ├── s4-6to9mo/      (47)
│   ├── s5-9to12mo/     (56)
│   ├── s6-12to24mo/    (79)
│   └── s7-24to36mo/    (41)
└── 40-glossary/                # 术语卡(146 张:G-ABBR-* / G-PERSON-* / G-TERM-*)
```

---

## 审计 4 大维度

### 维度 A · 单卡质量(per card)

每张卡片自查 7 项(对应 PHASE1_KARP §2.2 + §2.5 + §9 + §10):

1. **字数上限(§2.2)**:
   - `front.title` ≤ 15 字(中文,不含标点)
   - `back.why_matters` ≤ 80 字
   - `back.what_to_do` ≤ 150 字总,每条 ≤ 30 字
   - `back.failure_mode` ≤ 80 字
   - 背面正文合计 ≤ 310 字
2. **白话风格(§2.5)**:主语用"宝宝/你"不用"新生儿/父母";一句话讲一件事;不堆从句;读出来不像论文摘要
3. **citation 完整性**:`book_title_en` / `book_title_zh` / `authors` / `year` / `location`(章节+页码)/ `source_id` 5 项必填
4. **failure_mode 不空**:没"做错的方式"= 论点太弱,标记
5. **tags 准确**:`safety` / `philosophy` / `controversy` / `red_flag` 是否漏标 / 误标
6. **evidence_level 诚实**:
   - **A** = ≥ 2 个独立 Tier 1/2 一手源 + ≥ 1 个 peer-reviewed 综述
   - **B** = 1 Tier 1 + ≥ 2 单项研究;或 ≥ 3 单项研究无 Tier 1 背书
   - **C** = 流派原典(philosophy 标签)/ 专家共识但缺循证 —— **C 只能在带 `philosophy` tag 的卡片**
7. **glossary_refs 全填**(§2.8 术语卡片化):正文出现的专业术语都该指向 G-ID,不应内联解释

### 维度 B · 跨源重复 / 整合(deduplication)

9 本里大量主题被多源覆盖,核心检查:

1. **主题重复矩阵**:列出"同一议题被 N 个源讲过"(N ≥ 2)的清单,例:
   - 包裹 swaddle:Karp + AAP Safe Sleep + 鲍秀兰 + Davies
   - 共睡 cosleep:Karp + AAP + Brazelton + Bowlby
   - 6-9 月陌生人焦虑:Wonder Weeks + Bowlby V1/V2 + Brazelton + AAP Milestones
2. **整合判断**:对每个重复主题,二选一:
   - **合并**:若 N 张卡结论一致 → 留 1 张主卡 + N-1 张冗余卡标 `merge_into: C-XXX-XXX`
   - **保留**:若 N 张卡立场不同 → 全部保留,但**互相 `related_cards` 链接**(目前可能有大量缺链)
3. **跨源验证**:多源一致 → `evidence_level` 应升级到 A,但不少卡可能仍标 C(单源);列出升级候选

### 维度 C · 主题覆盖 / 遗漏(gap analysis)

对照总任务书 §2 各段主题清单 vs 实际产出:

1. **逐段对照**:S0/S1/S2/.../S7 8 段,任务书原 § 2 每段列出 8-12 个核心主题
2. **找断点**:实际卡未覆盖的主题 → 列入 `gaps.md` 候选
3. **红旗信号链**:跨段红旗信号(0-1 / 2-3 / 6 / 9 / 12 / 18 / 24 / 36 月)是否每个月龄都有红旗卡;断链 = gap
4. **流派立场覆盖**:任务书要求 4 流派(RIE / Pikler / 蒙氏 / Brazelton)立场 + 中医文化对照,实际是否每个核心议题都有立场对照

### 维度 D · 立场冲突(conflicts.md 候选)

`conflicts.md` 目前几乎空 —— 你的核心产出之一是初次填充。

1. **同议题不同立场**:扫所有卡片,列出至少 8-12 处(progress.md 估算)流派对立,例:
   - 共睡:Karp 反对 vs 鲍秀兰部分支持
   - 安抚奶嘴:Karp/Davies 立场对照 AAP
   - 把屎把尿:鲍秀兰 9 月起 vs AAP 18 月-3 岁
   - 包裹:Karp/AAP 西方 vs 鲍秀兰反对中国"打蜡烛包"
   - 体罚:全派别一致反对(共识)
   - 睡眠训练:Karp 第四产程 vs Davies 蒙氏 vs Wonder Weeks fussy phase
2. **结构化输出**:每条 conflict 写明:
   - 议题(中文 + 英文术语)
   - 各流派立场(列表)
   - 涉及卡片 ID
   - 建议处理方式(并存 / 加 controversy tag / 用户拍板)

---

## 工作流(防 token 爆炸)

**447 + 146 = 593 张卡片**,主线绝不能一次 Read 完。strict subagent 隔离:

### Phase A · 准备(主线,< 10 分钟)

```
1. Read 00-meta/README.md (总任务书,只看 §0/§2/§4/§5/§9)
2. Read 00-meta/PHASE1_KARP.md §2 + §2.5 + §10
3. Read 00-meta/PHASE2_AAP.md §2.6-2.9
4. Read 00-meta/progress.md (当前总览)
5. Read 30-cards/INDEX_BY_SOURCE.md (全卡片地图)
6. Read 00-meta/checkpoints/audit_report_96_cards_20260502.md (上次审计参考)
```

主上下文增长:~30-50 KB(规范全在,卡片正文不进)。

### Phase B · 分源审(subagent × 9,并行/串行随你)

**每个 subagent 审 1 个 SRC 的所有卡片**(典型 30-90 张/源),prompt 模板:

```
任务: 审 SRC-XXX 全部 N 张卡(列表如下: C-S?-XXX, ...)
读规范文件:
  - 00-meta/PHASE1_KARP.md §2.2 §2.5 §10 (字数 + 白话 + 14 条实战)
  - 00-meta/PHASE2_AAP.md §2.8-2.9 (术语卡 / 引用渲染)
检查每张卡 7 项 (维度 A 1-7)
返回结构化 yaml,字段:
  source_id: SRC-XXX
  total_cards: N
  issues:
    - card_id: C-XXX-XXX
      issue_type: word_count_overflow / missing_failure_mode / wrong_evidence_level / inline_glossary / xueque_tone / missing_citation_field / tag_misuse
      detail: <一句话>
      severity: P0 / P1 / P2
      suggested_fix: <一句话>
  totals_per_issue_type: {...}
返回 ONLY yaml,无 preamble,字段名英文。
```

每个 subagent 输出 ~3-10 KB,主线汇总 = ~30-90 KB。

### Phase C · 跨源整合(subagent × 8)

**每个 subagent 审 1 个段(S0-S7)的所有卡片**,跨源找重复 + 找缺口,prompt 模板:

```
任务: 审 stage S? 全部 N 张卡(跨源,列表: C-S?-001..N)
读规范文件: 00-meta/PHASE1_KARP §2 + 总任务书 §2 (S? 主题清单)
做 3 件事:
  1. 重复矩阵: 找同主题被 ≥2 源讲过的,列出 {主题, 涉及卡片 IDs, 建议合并 or 互链}
  2. gap 分析: 对照任务书 §2 S? 主题清单,列出未覆盖主题
  3. conflict 提名: 列出立场对立的议题,涉及卡片 IDs
返回 yaml:
  stage: S?
  total_cards: N
  duplicate_clusters: [{topic, card_ids, action}, ...]
  gaps: [topic_not_covered, ...]
  conflict_candidates: [{topic, positions: {...}, card_ids}, ...]
```

8 段 × 3-10 KB = ~30-80 KB 汇总。

### Phase D · 主线汇总(< 30 分钟)

合并 9(Phase B)+ 8(Phase C)= **17 份子报告**,产出最终审计报告。期间:

- 用 `Read` + `Edit` 修明显错(字数超限可压、缺 glossary_refs 可补、漏 related_cards 可加)
- 不动卡片正文,除非明确质量问题
- conflicts.md 直接写入(从 Phase C conflict_candidates 整理)

---

## 输出要求

### 主报告

`00-meta/checkpoints/audit_report_447_cards_YYYYMMDD.md`

格式:

```markdown
# 审计报告 · 9 本书 447 张知识卡 + 146 张术语卡

## 总评(数字)
- 字数合规率: X% (xxx/447)
- citation 完整率: X%
- failure_mode 非空率: X%
- evidence_level 升级候选: N 张
- 重复簇: N 个
- 主题 gap: N 个
- conflict 候选: N 个

## 维度 A · 质量
[per-source breakdown + P0/P1/P2 优先级清单]

## 维度 B · 重复整合
[重复簇列表 + 合并/互链建议]

## 维度 C · 遗漏
[per-stage gap 清单]

## 维度 D · 冲突
[conflict 列表 + 立场对照表]

## 已自动修复
[列出本次审计期间已 Edit 的卡片 + 字段]

## 待用户决策
[需要用户拍板的争议项,标 P0]

## 下一步建议
[Phase 6 之后是否补卡 / 整合冗余 / 写 conflicts.md / etc.]
```

### 副产物

1. **`conflicts.md`** 初次填充(从 Phase C 提名整理),格式参考 README §10
2. **`gaps.md`** 追加(从 Phase C gap 分析)
3. **`audit_log.md`** —— 列出本次自动修复的所有卡片 ID + 字段 + 改动(可回滚审计轨迹)

---

## 边界(don't do)

| ❌ 不要 | ✅ 应该 |
|---|---|
| Read 整批卡片进主上下文 | 全部走 subagent,主线只看汇总 |
| 重写卡片正文 | 只修元数据(字数/glossary_refs/related_cards/tags/evidence_level) |
| 自创新卡 | 只产报告,不产卡;新卡缺口写 gaps.md 等用户决定 |
| 删除冗余卡 | 只标 `merge_candidate: true` + 写报告,删除等用户拍板 |
| 大改 conflicts.md 立场 | 只列冲突 + 各方立场,不替用户选边(任务书 §0 #5)|
| 凭训练记忆补内容 | 任何主张必须能追溯回某张卡 / 某个 source(任务书 §0 #3)|
| 一次 Read 全 447 张 | 用 subagent 分批,严守 §10.3 输入输出比 |

---

## 起步 5 分钟(给新 session)

```bash
# 1. 进项目
cd ~/Desktop/parenting-kb

# 2. 看清规模
find 30-cards -name "*.yaml" | wc -l    # 应 = 447
find 40-glossary -name "*.yaml" | wc -l  # 应 = 146
ls 30-cards/                              # 8 段

# 3. 读规范(主线 Read,~30 KB)
# 总任务书 + Phase 1 规范 + Phase 2 schema 升级 + 当前进度 + 索引
# 见上面 §Phase A 步骤 1-6

# 4. 启动分源 subagent(Phase B)
# 第一个 subagent 审 SRC-003 Karp 33 张卡作为 benchmark
# 看输出质量 OK 后批量 spawn 剩 8 个 subagent

# 5. 接 Phase C 跨段
# 8 个 stage subagent 并行/串行
```

---

## 完成定义

- [ ] 9 个 SRC 全审(Phase B 输出 9 份)
- [ ] 8 个 stage 全跨段检(Phase C 输出 8 份)
- [ ] `audit_report_447_cards_YYYYMMDD.md` 主报告完整
- [ ] `conflicts.md` 至少 8 条 conflict 入库
- [ ] `gaps.md` 至少 5 条 gap 入库
- [ ] `audit_log.md` 列出所有自动修复
- [ ] progress.md "已确认决策" 段补本次审计要点
- [ ] 终端打印总结 + 待用户决策清单

---

*v1.0 完。执行中遇到本提示词未覆盖的判断,写入 `questions_for_user.md`,不要瞎拍板。*
