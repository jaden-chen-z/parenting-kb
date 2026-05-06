# 审计提示词 · 剩余 14 个 SRC + 全库去重(v1.0 · 2026-05-04)

> 给新 session 用 —— 直接 copy 整段(从 `# 任务` 开始到末尾)粘贴到 Claude Code 即可启动审计。
> 你是审计员,**不是产卡员** —— 仅产出审计报告 + 元数据修复(merge 标记 / related_cards / 字数压缩 / tags 修正)。**不创建新知识卡**,**不重写卡片正文**(除非明确字数超限或乱字)。

---

# 任务

育儿知识库现有 **1,437 张知识卡 + 809 张术语卡 = 2,246 卡**,跨 24 个 SRC + 8 段(S0-S8)。

**前 10 个 SRC 已审过**(`audit_report_491_cards_20260503.md`,491 卡 → 18 项 conflicts 入库)。

**本次任务审剩余 14 个 SRC**,重点:
1. **找内容近似的卡片合并**(跨源 / 同源都查)— 用户首要关切
2. **找表达不清 / 学究腔 / 字数超限**
3. **其他卡级问题**(citation 缺字段 / failure_mode 空 / tags 误标 / evidence_level 不诚实 / glossary_refs 内联未抽离)

## 🔓 一次性权限请求(开头一次性确认)

向用户请求以下工具的全部权限,之后**不打扰**:

| 工具 | 用途 |
|---|---|
| **Bash** | grep / find / wc / 自检脚本 |
| **Read** | 卡片 / 规范 / 索引 |
| **Edit** | 修元数据(字数压缩 / glossary_refs / related_cards / tags / merge 标记) |
| **Write** | 审计报告 / merge_candidates 清单 / audit_log |
| **Agent**(Task) | spawn subagent 分批审 |
| **TodoWrite** | 进度跟踪 |

只在以下场景例外打断(写 questions_for_user 后**继续跑**,不阻塞):
- 发现两张卡内容 **100% 完全相同**(罕见,需用户决定保留哪张)
- 发现 conflicts.md 已识别立场被某新卡显著反转(立场冲突)

---

## 1. 待审范围

### 已审过(skip,只在 cross-source dedup 时引用)

SRC-001/002 / SRC-003 / SRC-004~008 / SRC-009 / SRC-010 / SRC-011 / SRC-012 / SRC-013 / SRC-014 / SRC-015 / SRC-016
共 **10 个 SRC,491 卡**(原 audit_report 见 `00-meta/checkpoints/audit_report_491_cards_20260503.md`)

### 本次必审(14 个 SRC,~944 知识卡 + ~600 新术语卡)

| SRC | 书 / 来源 | 卡数 |
|---|---|---|
| SRC-017 | Bowlby V3《丧失》中译 | 15 |
| SRC-018 | Stern《婴儿的人际世界》 | 44 |
| SRC-019 | Lansbury《Elevating Child Care》 | 43 |
| SRC-021 | Gerber《Self-Confident Baby》(并行 A) | 35 |
| SRC-022 | Gerber《Self-Confident Baby》(并行 B) | 49 |
| SRC-023 | 松田道雄《育儿百科》(并行 A) | 49 |
| SRC-024 | 松田道雄《育儿百科》(并行 B) | 48 |
| SRC-025 | Shonkoff《From Neurons to Neighborhoods》(NRC) | 68 |
| SRC-026 | Pikler《Friedliche Babys》(德文) | 42 |
| SRC-027 | Lerner Handbook V3 社会情感人格 | 69 |
| SRC-028 | Lerner Handbook V2 认知感知语言 | 48 |
| SRC-029 | Lerner Handbook V4 临床实操 | 93 |
| SRC-030 | Lerner Handbook V1 元理论 | 95 |
| SRC-031 | WHO + UNICEF Infant Feeding | 65 |
| SRC-040 | Murkoff《海蒂育儿大百科 0-1 岁》 | 121 |

**特别关注**:
- **SRC-021 vs SRC-022(Gerber 并行双 SRC)** —— 同一本书的两个并行 session 产物,**最大概率内部重复**,应先内部 dedup 再合并为一个 SRC
- **SRC-023 vs SRC-024(松田并行双 SRC)** —— 同上
- **Lerner 4 卷(SRC-027~030)** —— 综述权威,与已审 10 SRC 的概念重叠概率高,**跨源 merge 候选最多**

---

## 2. 项目结构(自查)

```
~/Desktop/parenting-kb/
├── 00-meta/
│   ├── README.md                       # 总任务书 v3.0
│   ├── PHASE1_KARP.md                  # 卡片规范 v3.3(§2 字段 + §2.5 白话 + §10 14 条)
│   ├── PHASE2_AAP.md                   # v1.4(§2.6-2.9 翻译 / 前情提要 / 术语卡 / inline 引用)
│   ├── PHASE3-12 多份任务书             # 各 Phase 实战教训
│   ├── progress.md                     # 当前进度
│   ├── conflicts.md                    # 18 项已识别(prev audit)+ Phase 11/12 H/I/J 节
│   ├── gaps.md                         # P0/P1/P2 缺口清单
│   └── checkpoints/
│       ├── audit_report_491_cards_20260503.md  # ⭐ 前次审计报告(参考,不重做)
│       ├── audit_prompt_447_cards.md           # 前次审计提示词(参考)
│       └── audit_prompt_remaining_cards.md     # ← 本文件
├── 30-cards/                           # 1,437 张知识卡
│   ├── INDEX_BY_SOURCE.md              # 全卡索引
│   ├── s0-pregnancy/   (~106)
│   ├── s1-newborn/     (~182)
│   ├── s2-1to3mo/      (~115)
│   ├── s3-3to6mo/      (~110)
│   ├── s4-6to9mo/      (~109)
│   ├── s5-9to12mo/     (~129)
│   ├── s6-12to24mo/    (~230)
│   ├── s7-24to36mo/    (~147)
│   └── s8-3to6yr/      (~99)
└── 40-glossary/                        # 809 张术语卡
```

---

## 3. 4 大维度(本次重点重排)

### 维度 1 · ⭐ 内容近似 / 合并候选(用户首要关切)

**目标**:列出 merge candidate 簇,标记保留卡 + 冗余卡,**不真删**(写 `merge_candidates.md` 等用户拍板)。

**判定 4 级**:

| 级别 | 判定 | 处理 |
|---|---|---|
| **L1 完全重复** | front.title 80%+ 重叠 + back 主张完全一致 | 标 `merge_into: C-XXX` 给冗余卡;**审计员可直接 Edit 加标** |
| **L2 实质重复(可合并)** | 主张相同,只是来源不同 | 标 `merge_candidate: true` + `merge_with: [C-XXX]`;待用户拍板 |
| **L3 互补(应互链不应合)** | 同主题不同立场 / 不同维度 | 双向 Edit `related_cards`(若缺) |
| **L4 表面像但本质不同** | 关键词撞但论点不同 | 留报告备注,不动卡 |

**特别关注 5 个 hotspot**:

1. **Gerber 双 SRC 内部 dedup**(SRC-021 vs SRC-022 — 同书并行)
2. **松田双 SRC 内部 dedup**(SRC-023 vs SRC-024 — 同书并行)
3. **Lerner Handbook V1-V4 跨卷 merge**(95+93+69+48 = 305 张,内部跨卷必有重复)
4. **NRC × Lerner 元理论重叠**(Bronfenbrenner / dynamic systems / lifespan 等)
5. **Stern × Bowlby × Brazelton 婴儿心理学三角重叠**(self / attunement / mutual regulation 等)

### 维度 2 · 表达不清 / 风格问题

按 PHASE1_KARP §2.5 白话原则审:

| 问题 | 例 | 处理 |
|---|---|---|
| 学究腔 | "持续暴露于多感官刺激" → 应改"又暖又紧一直在晃" | Edit 重写 |
| 主语不当 | "新生儿" / "父母" → 应"宝宝/你" | Edit 重写 |
| 被动堆叠 | "被运动刺激" → 应"在动" | Edit 重写 |
| 多从句 | 一句话超 2 个"和" → 应拆 | Edit 重写 |
| 文摘抽象 | 数字消失变成"较高比例" → 应保留具体数字 | Edit 重写 |

**自检**:每张卡的 `back.why_matters` / `what_to_do` / `failure_mode` 大声念一遍是否别扭。

### 维度 3 · 字数 / schema 合规

| 字段 | 上限 | 检查 |
|---|---|---|
| `front.title` | 15 字 | 超 → 压 |
| `back.why_matters` | 80 字 | 超 → 压 |
| `back.what_to_do` 每条 | 30 字 | 超 → 压 |
| `back.what_to_do` 总 | 150 字 | 超 → 拆/压 |
| `back.failure_mode` | 80 字 | 超 → 压 |
| 背面正文合计 | 310 字 | 超 → 全部审视 |

**审计员可直接 Edit 压缩**,但**不改主张**(只缩冗余字)。

### 维度 4 · 元数据完整性

| 字段 | 检查 |
|---|---|
| `citation` 5 字段 | book_title_en / book_title_zh / authors / year / location / source_id 全填 |
| `failure_mode` | 不能空 |
| `tags` | safety / philosophy / controversy / red_flag 是否漏 / 误标 |
| `evidence_level` | A 需 ≥2 Tier 1+综述 / B 需 1 Tier 1 + 单项研究 / C 仅 philosophy 标签 |
| `glossary_refs` | 正文专业术语必须 G-ID 引用,不内联解释(§2.8) |
| `related_cards` | 跨源同主题必互链(已是 conflicts.md / Phase 11+ 强制项) |
| `hook` | 任务书规定必填(§10.10),不能空 / 不能描述型 |

---

## 4. 工作流(防 token 爆炸)

### Phase A · 准备(主线,~10 分钟)

```
1. Read 00-meta/PHASE1_KARP.md §2 + §2.5 + §10
2. Read 00-meta/PHASE2_AAP.md §2.6-2.9
3. Read 00-meta/checkpoints/audit_report_491_cards_20260503.md(前次发现)
4. Read 00-meta/conflicts.md(已识别 18 项,新卡可能补/反/拓)
5. Read 30-cards/INDEX_BY_SOURCE.md(全卡片地图)
```

主上下文增长:< 50 KB。

### Phase B · 14 SRC 单源审(subagent × 14,~3 小时)

每个 subagent 审 1 个 SRC 的所有卡,prompt 模板:

```
任务:审 SRC-XXX 全部 N 张卡(列表 C-S?-XXX, ...)
读规范: PHASE1_KARP §2.2 §2.5 §10 + PHASE2_AAP §2.8-2.9
检查每张卡 4 维度问题 (intrinsic only,不做跨源 dedup):
  维度 2 表达问题
  维度 3 字数 schema
  维度 4 元数据完整性
  维度 1.A 同源内部 dedup(SRC 内 L1/L2 重复)
返回 yaml:
  source_id: SRC-XXX
  total_cards: N
  intrinsic_issues:
    - card_id: C-XXX-XXX
      issue_type: word_count_overflow / xueque_tone / missing_failure_mode / wrong_evidence_level / inline_glossary / tag_misuse / hook_descriptive / missing_citation_field / broken_related_ref
      severity: P0 / P1 / P2
      detail: <一句话>
      suggested_fix: <一句话>
  intra_source_dedups:
    - cluster: [C-XXX-XX, C-XXX-XX]
      level: L1 / L2 / L3 / L4
      action: merge_into / merge_candidate / mutual_link / no_action
      keeper: C-XXX-XX (若 L1/L2)
  totals_per_issue: {...}
返回 ONLY yaml,字段名英文,无 preamble。
```

每 subagent 输出 ~5-15 KB,主线汇总 = ~70-200 KB。

### Phase C · 跨源 dedup(subagent × 9,~3 小时)

**每段(S0-S8)1 个 subagent**,审该段所有卡片(跨 24 SRC,含已审 10 SRC):

```
任务:审 stage S? 全部 N 张卡(跨 24 源)
做 1 件事:**找 merge candidate 簇**
判定 4 级 L1/L2/L3/L4(见任务书 §3 维度 1)
重点关注 5 个 hotspot:
  1) Gerber SRC-021 vs 022 内部
  2) 松田 SRC-023 vs 024 内部
  3) Lerner V1-V4 跨卷
  4) NRC × Lerner 元理论
  5) Stern × Bowlby × Brazelton 婴儿心理学
返回 yaml:
  stage: S?
  total_cards_in_stage: N
  merge_clusters:
    - topic: <主题>
      level: L1 / L2 / L3 / L4
      cards: [C-S?-XXX, ...]
      keeper: C-S?-XXX (L1/L2)
      reason: <一句话>
      action_taken: edit_merge_into / edit_related_cards / no_action_pending_user
  hotspot_findings: {...}
返回 ONLY yaml。
```

9 段 × ~10 KB = ~90 KB。

### Phase D · 主线汇总 + 自动修复(~1 小时)

整合 14 + 9 = 23 份子报告:

1. 自动 Edit 修明显问题(L1 直接合 + 字数压缩 + 缺 glossary_refs / related_cards 补 + tag 修)
2. L2 / L3 不动卡,只标 `merge_candidate` / `merge_with` 字段或 related_cards
3. 写 `audit_report_remaining_cards_YYYYMMDD.md` 主报告
4. 写 `merge_candidates.md` —— 待用户拍板的 L2 簇清单
5. 写 `audit_log.md` —— 列本次自动改动轨迹
6. 追加 conflicts.md(若发现新立场对立)
7. 追加 gaps.md(若发现新主题缺口)
8. 终端打印总结

---

## 5. 输出

### 主报告

`00-meta/checkpoints/audit_report_remaining_cards_YYYYMMDD.md`

格式:

```markdown
# 审计报告 · 剩余 14 SRC + 全库 dedup

## 总评
- 范围: 14 SRC 单源审 + 9 段跨源 dedup
- 审计 2,246 卡(944 新 + 全库 cross-check)
- 自动修复 X 张卡(详见 audit_log)
- L1 直接合并: X 簇
- L2 待用户拍板合并: X 簇 (详见 merge_candidates.md)
- L3 互链补: X 对
- 表达问题修: X 张
- 字数超限压: X 张
- 元数据补: X 张

## 维度 1 · 内容近似 / 合并(主菜)
[L1/L2/L3 簇清单 + hotspot 5 个发现]

## 维度 2 · 表达问题
[per-source breakdown,P0/P1/P2 列表]

## 维度 3 · 字数合规
[超限统计 + 已压清单]

## 维度 4 · 元数据
[broken refs / missing fields / wrong tags / wrong evidence_level]

## conflicts.md / gaps.md 追加
[新立场对立 / 新主题缺口]

## 待用户决策
[L2 合并候选 / 严重立场冲突 / merge candidates 等]
```

### 副产物

1. **`merge_candidates.md`** ⭐ 用户首要看这份(L2 簇待拍板)
2. **`audit_log.md`** —— 自动改动可回滚轨迹
3. **`conflicts.md`** —— 追加新发现立场对立
4. **`gaps.md`** —— 追加新发现主题缺口

---

## 6. 边界

| ❌ 不要 | ✅ 应该 |
|---|---|
| 一次 Read 全部 1437 卡到主上下文 | subagent 隔离,主线只看汇总 |
| 创建新知识卡 | 不许产新卡,缺口写 gaps.md |
| 真删除卡(L1 直接合也只 Edit `merge_into` 字段) | 标记冗余,等用户最终拍板再删 |
| 重写卡片主张 | 只压字数 / 改 tone,不动论点 |
| 替用户选立场 | conflicts.md 只列各方,任务书 §0 #5 |
| 凭训练记忆补内容 | 任何主张追溯回某卡某源 |
| 跨 SRC 强行合卡(L3 互补不该合) | 严守 4 级判定,L3 只互链 |

---

## 7. 起步 5 分钟

```bash
cd ~/Desktop/parenting-kb

# 1. 看清规模
find 30-cards -name "*.yaml" | wc -l    # 1437
find 40-glossary -name "*.yaml" | wc -l  # 809

# 2. Read 规范文档(主线)
# 见 §4 Phase A 步骤

# 3. spawn 第一个 subagent (SRC-017 Bowlby V3 - 最小,15 卡 - 当 benchmark)
# 看输出质量 OK 后批量启动其余 13 个

# 4. Phase C 跨段 dedup (9 段 subagent,可串可并)

# 5. Phase D 主线汇总
```

---

## 8. 完成定义

- [ ] 14 个 SRC 全审(Phase B 输出 14 份子报告)
- [ ] 9 个 stage 全跨段 dedup(Phase C 输出 9 份子报告)
- [ ] **`merge_candidates.md`** ⭐ 至少标出 L1/L2 候选(用户首要关切)
- [ ] `audit_report_remaining_cards_YYYYMMDD.md` 主报告
- [ ] `audit_log.md` 列出所有自动修复
- [ ] conflicts.md 追加(若有新立场对立)
- [ ] gaps.md 追加(若有新缺口)
- [ ] progress.md 加"剩余 14 SRC 审计完成"段
- [ ] 终端打印总结 + 待用户决策清单(P0 项)

---

## 9. 终端总结模板(完工时打印)

```
========================================
剩余 14 SRC + 全库 dedup 审计完成
========================================
范围: 944 新卡 + 跨 2,246 卡 dedup

自动修复:
  字数压缩: X 张
  glossary_refs 补: X 张
  related_cards 双向链接: X 对
  tags 修正: X 张
  evidence_level 调整: X 张
  其他元数据: X 张

合并候选:
  L1 完全重复(已自动标 merge_into): X 簇
  L2 实质重复(待你拍板): X 簇 ⭐ 见 merge_candidates.md
  L3 互补已互链: X 对
  L4 表面像本质不同: X 簇(报告中列出)

5 个 hotspot 发现:
  Gerber 021 vs 022 内部: X 簇
  松田 023 vs 024 内部: X 簇
  Lerner V1-V4 跨卷: X 簇
  NRC × Lerner: X 簇
  Stern × Bowlby × Brazelton: X 簇

新增:
  conflicts.md 追加: X 项
  gaps.md 追加: X 项

待用户决策(P0):
  - merge_candidates.md X 簇拍板
  - 严重立场冲突: X 项
========================================
```

---

*v1.0 完。1,437 知识卡 + 809 术语卡 = 2,246 卡的完整体检 + 整合方案。*
