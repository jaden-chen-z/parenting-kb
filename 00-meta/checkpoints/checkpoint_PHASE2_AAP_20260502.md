# Checkpoint · Phase 2 AAP(2026-05-02)

> 项目:parenting-kb · Phase 2 第一本 · AAP《Caring for Your Baby》(healthychildren.org portal)
> 启动:2026-05-01(R1 Sleep)
> 完成:2026-05-02
> 任务书:`00-meta/PHASE2_AAP.md` v1.4(§2.6 翻译两步走 / §2.7 前情提要 / §2.8 术语卡片化 / §2.9 inline 引用渲染)

---

## 0. 一句话总结

AAP healthychildren.org 抓取 30+ 篇 article(5 SRC cluster),产 **63 张白话循证知识卡 + 60 张术语卡**,任务书 v1.0 → v1.4 升级 4 大方法论规则。**Phase 2 第一本超出目标**(40-60 → 63 张)。

---

## 1. 产出清单

### 1.1 Sources(5 SRC clusters)

| SRC ID | 主题 | Articles | 字符数 |
|---|---|---|---|
| [SRC-004](../../10-sources/tier1-authoritative/notes/SRC-004.yaml) | Safe Sleep & SIDS Prevention | 7 篇(原 4 + R1.5 补 3) | ~30K |
| [SRC-005](../../10-sources/tier1-authoritative/notes/SRC-005.yaml) | Crying & Soothing | 4 篇 | ~13.7K |
| [SRC-006](../../10-sources/tier1-authoritative/notes/SRC-006.yaml) | Feeding & Pacifiers | 10 篇(原 5 + R3.5 补 5) | ~22K |
| [SRC-007](../../10-sources/tier1-authoritative/notes/SRC-007.yaml) | Milestones & Teething | 8 篇 | ~25K |
| [SRC-008](../../10-sources/tier1-authoritative/notes/SRC-008.yaml) | Health & Safety | 6 篇 | ~22K |

**Total**:**35 篇 article / ~113K 字符**(远超任务书 §5 目标 8-15 篇)。

### 1.2 知识卡(63 张,v3.5 schema)

| 段 | 卡数 | 主要 ID 范围 |
|---|---|---|
| **S1** (0-1 月) | **36 张** | C-S1-034 ~ 064(部分跨段) |
| **S2** (1-3 月) | 7 张 | C-S2-003 ~ 007 |
| **S3** (3-6 月) | 13 张 | C-S3-001 ~ 013 |
| **S4** (6-9 月) | 5 张 | C-S4-001 ~ 007 |
| **S5** (9-12 月) | 7 张 | C-S5-001 ~ 007 |

按轮次分:
- **R1 Sleep & SIDS**:9 张(C-S1-034 ~ 041 + C-S2-003)
- **R1.5 复盘补**:3 张(C-S1-052 + C-S2-005/006)
- **R2 Crying & Soothing**:9 张(C-S1-042 ~ 049 + C-S2-004)
- **R3 Feeding & Pacifiers**:9 张(C-S1-050/051 + C-S3-001 ~ 005 + C-S4-001/002)
- **R3.5 复盘补**:7 张(C-S1-053/054/055 + C-S3-006/007/008 + C-S5-001)
- **R4 Milestones**:14 张(C-S2-007 + C-S3-009 ~ 013 + C-S4-003/004/005 + C-S5-002 ~ 006)
- **R5 Health & Safety**:12 张(C-S1-056 ~ 064 + C-S4-006/007 + C-S5-007)

### 1.3 术语卡(60 张,40-glossary/)

| 类型 | 数量 |
|---|---|
| **缩写** (G-ABBR-) | 21 张 |
| **人名** (G-PERSON-) | 7 张 |
| **专有名词** (G-TERM-) | 32 张 |

R5 audit 阶段补 4 张:G-ABBR-RSV / G-ABBR-MMR / G-ABBR-DTaP / G-ABBR-CDC

### 1.4 任务书 schema 演进(v1.0 → v1.4)

| 版本 | 日期 | 新增规则 |
|---|---|---|
| v1.0 | 2026-05-01 | 初始任务书 |
| v1.1 | 2026-05-01 | §2.6 翻译两步走 + 缩写/人名规则 |
| v1.2 | 2026-05-02 | §2.7 前情提要规则(why_matters 必含概念定义 + 背景数字)|
| v1.3 | 2026-05-02 | §2.8 术语卡片化(40-glossary/ + glossary_refs)|
| v1.4 | 2026-05-02 | §2.9 inline 引用渲染(自动链接化 + 弹窗,glossary_refs 不展示给用户)|

---

## 2. POC 完成定义打勾(任务书 §5)

- [x] 抓 8-15 个 AAP 子主题 → **35 篇**(超 2 倍以上)
- [x] 产 40-60 张新卡 → **63 张**(超目标)
- [-] cross-validate Karp 33 张升级 evidence_level → **按解读 B 跳过**(用户决定:Phase 全部书产完后统一整合)
- [-] conflicts.md ≥ 2 处 → **按解读 B 跳过**
- [x] checkpoint MD 完成 → 本文件
- [x] progress.md 更新
- [x] INDEX_BY_SOURCE.md 加 SRC-004+ 章节
- [-] 用户验收 → **本次 session 跳过样本验收,留新 session 做完整 audit**(见 §5)

---

## 3. 关键工程经验(给 Phase 3)

### 3.1 解读 B 决策(2026-05-02)

用户明确:不在 Phase 2 内做 Karp vs AAP 立场冲突整合 / evidence_level 升级。
- 各书产卡聚焦"独立视角",不动其他书已有卡
- conflicts.md 不写
- 整合留到所有书产完后统一做

**影响**:Phase 2 工作量降 40%(不需要逐张 cross-validate 33 张 Karp 卡),但 conflicts.md 留给后续阶段。

### 3.2 复盘补救机制(R1.5 / R3.5)

**触发**:每 ROUND 完后,用户问"漏了什么没"→ 我 audit 已抓 article 数 vs 入口页 article 总数,识别漏失。

**结果**:R1.5 补 3 张(漏:日夜颠倒 / 睡整觉真定义 / 睡眠周期),R3.5 补 7 张(漏:维 D / 铁 / 戒奶瓶 / 米粉砷 / 鱼汞 / 吐奶 / 配方量)。

**沉淀**:每 ROUND 完做"全 article 入口对照"是必要,不能"凑够目标卡数"就停。

### 3.3 翻译两步走(§2.6)

**问题**:从英文 verbatim 直译损失白话度;缩写不友好;人名缺身份。

**方案**:
1. 第一步从 verbatim 提英文 5 字段骨架(事实精确)
2. 第二步中文白话改写(不直译,按中文家长习惯)
3. 缩写 / 人名 / 专名在 `glossary_refs` 列出,渲染层弹窗解释

### 3.4 前情提要规则(§2.7)

**问题**:用户审 C-S1-038 时反馈"一上来就说'很多人以为包紧能防 SIDS',谁能理解你在说什么?"

**方案**:每张卡 `why_matters` 开头 2 句前情提要 — 概念定义 + 背景数字,然后才进入核心主张。

**字数放宽**:`why_matters` ≤ 80 → ≤ 130 字,背面合计 ≤ 310 → ≤ 360 字。

### 3.5 术语卡片化(§2.8)

**问题**:卡片底部内联展开缩写 / 人名 / 专名段,卡片冗长;同一术语在多张卡里重复定义。

**方案**:每个术语建独立卡(40-glossary/G-XXX-XXX.yaml),知识卡 `glossary_refs` 列引用 ID,渲染层做可点击链接 + 弹窗。
- ID 规则:`G-ABBR-<exact>` / `G-PERSON-<Surname>` / `G-TERM-<slug>`
- 术语卡 schema:display_name + one_liner + detail markdown + key_facts + related_glossary + related_cards

### 3.6 inline 引用 + 渲染原则(§2.9)

**问题**:卡片正文里"见 C-S3-006"这种引用如何变可点击。

**方案**:
- 知识卡 ID 直接匹配:正文写 `C-S?-???`,正则 `C-S\d+-\d+` 自动转链接
- 术语卡 display_name 匹配:渲染层读 `glossary_refs` → 反查 display_name → 在正文搜该词转链接
- **关键渲染原则**:
  - `glossary_refs` / `related_cards` 等元数据**不展示给最终用户**(只是后台索引)
  - 术语在正文中**每次出现都是链接**(不限第一次)
  - 同一术语的所有链接弹同一窗

---

## 4. 工程数据

### 4.1 WebFetch 输入/输出比抽样(§10.13 §4)

| Article | 比例 | 备注 |
|---|---|---|
| Safe Sleep 9 Ways | ~1.0 | 完整 |
| AAP Policy Explained | ~1.0 | 完整 |
| Swaddle How-to | ~0.4 | 部分总结但 verbatim 引号保留 |
| Settling-In Breastfeeding | 拒绝返回 | 版权策略,fallback 到 How-Often |
| BLW + Cereal-in-Bottle | ~0.6 | 部分总结化 |
| Movement 8-12 / Emotional-Social / Language | 内容过滤拦截 | 改 facts list prompt 重抓成功 |

**经验**:超长 verbatim prompt 易触发版权策略 / 内容过滤;改"列 facts" prompt 风格更稳。

### 4.2 反向覆盖审计(§10.4)

每 ROUND 完跑 — 不带先验从原 article 列"父母最该记的事 N 项",和已写卡 diff。
**Phase 2 收益**:R1.5 补 3 张 + R3.5 补 7 张 + R5 audit 补 9 张 glossary_refs + 4 张术语卡。
**结论**:**接近 1/4 的卡来自审计阶段**,这一步不能跳。

### 4.3 chunk 大小(§10.13 §1)

实操中网页源大多单文件 < 12K 字符,无需 chunk。少数长文(AAP Policy Explained 11.6K)整篇保留不切。

---

## 5. 下一步(给新 session)

### 5.1 用户验收

**用户要求**:新开 session 做 Karp 33 + AAP 63 = **96 张卡完整审计**。
- 审计提示词见本 checkpoint 末尾附录(独立 prompt,可直接 copy)。

### 5.2 Phase 3 候选下一本书

按任务书 PHASE2_AAP §6 完成定义,Phase 2 第一本通过 → 进 Phase 2 第二本 / Phase 3:

1. **Brazelton《Touchpoints: Birth to Three》**
   - Karp 引用源(Brazelton 1962 哭闹峰研究)
   - Touchpoints 育儿法原典
   - 中译本《图点教育法》待购

2. **鲍秀兰《0-3 岁早期教育和潜能开发》**
   - 中文 Tier 4 权威
   - 补东方文化视角
   - 国内主流育儿建议参考源

3. **WHO《Infant and Young Child Feeding Guideline》**
   - 全球性循证视角
   - 与 AAP 的"美式"立场互补

### 5.3 全本完成后的整合阶段(P 末)

按解读 B,所有书产完后统一做:
- conflicts.md 整理(Karp vs AAP / Brazelton 等立场对立)
- evidence_level 升级(B → A 当多源对齐)
- 知识图谱(可选)— 卡片之间依赖关系可视化
- render_labels.yaml(英文 key → 中文展示标签)

---

## 6. 用户操作建议

1. **抽 5 张随机卡审**(任务书 §6 验收标准)— 4+ 张满意 = Phase 2 第一本通过
2. **新 session 跑 96 张完整 audit**(用本 checkpoint 附录的提示词)
3. **决定 Phase 3 启动书**(候选见 §5.2)

---

## 附录 · 96 卡审计提示词(给新 session)

见同目录 `audit_prompt_96_cards.md`(独立文件,便于 copy-paste 到新 session 启动)。

---

*v1.0 · 2026-05-02 — Phase 2 AAP 完成产出汇总*
