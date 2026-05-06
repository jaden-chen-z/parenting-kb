# Phase 14 · Murkoff《海蒂育儿大百科 0-1 岁》· Planning Checkpoint

> 2026-05-04 · 自主 session · 任务书 `00-meta/PHASE14_MURKOFF.md` v1.0

## 1. 源文件状态

- 路径:`10-sources/tier3-books/raw_pdfs/murkoff_what_to_expect_zh.md`
- 字节:1.88 MB(wc -m,UTF-8 字节)
- 字符:741,035(Python utf-8 解码)
- 行数:**单行**(整本压在 1 行,与 Karp/鲍秀兰类似 — 适用 §10.1 工程化分块)
- OCR 质量:中等。版权页 + TOC(0-22000 字符)有较多乱码;正文(22000+)中文可读,有少量错字 + 图片占位符散布。

## 2. SRC + 卡 ID 隔离实测

启动前 `ls SRC-{031..040}` 实测:**SRC-031..039 全空**(WHO session 用 SRC-031 但本地未占),**SRC-040 安全**。

各段当前 max 卡 ID(实测 `ls 30-cards/sX-*/C-S?-*.yaml | sort | tail -1`):
- S0: C-S0-1553 → 海蒂起点 ≥ C-S0-2053
- S1: C-S1-1602 → 海蒂起点 ≥ C-S1-2102
- S2: C-S2-1505 → 海蒂起点 ≥ C-S2-2005
- S3: C-S3-1646 → 海蒂起点 ≥ C-S3-2146
- S4: C-S4-1644 → 海蒂起点 ≥ C-S4-2144
- S5: C-S5-1643 → 海蒂起点 ≥ C-S5-2143

每 Part 内部各段 ID 用 +100 隔离区段,避免 Part 间撞:
- Part 1 S0 = 2053+ / S1 = 2102+
- Part 2 S1 = 2202+
- Part 3 S2 = 2005+ / S3 = 2146+
- Part 4 S3 = 2246+ / S4 = 2144+
- Part 5 S5 = 2143+
- Part 6 S1 = 2302+ / S2 = 2105+ / S3 = 2346+ / S4 = 2244+ / S5 = 2243+
- Part 7 S0 = 2153+ / S1 = 2402+(妈妈/特殊/早产 跨段)

## 3. 分段方案

正文按字符等长切 7 Part(每 ~103K 字符,带 500 字符 overlap),独立文件存于 `10-sources/tier3-books/raw_pdfs/murkoff_chunks/part_NN.md`。

| Part | 字符范围(全文绝对) | 大致内容 | 主段 |
|---|---|---|---|
| 1 | 22000 - 125220 | Ch 1-3 孕产期 + 喂养准备 + 母乳基础 | S0/S1 |
| 2 | 124720 - 227940 | Ch 4-5 新生儿 + 0-1 月 | S1 |
| 3 | 227440 - 330660 | Ch 6-8 1-2 / 2-3 / 3-4 月 | S2/S3 |
| 4 | 330160 - 433380 | Ch 9-10 + Ch 12 4-8 月 | S3/S4 |
| 5 | 432880 - 536100 | Ch 14-16 9-12 月 | S5 |
| 6 | 535600 - 638820 | Ch 17-19 四季 + 生病 + 急救 | 跨段(安全 + 红旗) |
| 7 | 638320 - 741035 | Ch 20-25 早产 + 特殊 + 妈妈 + 多胎 | S0/S1/S6 + 妈妈跨段 |

## 4. 增量优先级(避免重复造卡)

海蒂是美国主流大众百科,**只取增量**:
1. **优先抓**:gaps.md P0 缺口(G6 黄疸 / G7 脐带 / G8 新筛 / G9 疫苗 / G11 母乳→混合 / G14 24 月 M-CHAT)
2. **优先抓**:海蒂独家/主流大众视角(包皮环切 / 选保姆 / 选医生 / 多胎 / 特殊宝宝)
3. **跳过**:已 8 源充分覆盖且立场一致(如 SIDS 仰睡)
4. **产卡**:与 Karp / AAP / Bowlby / Davies 等立场不同 → 标 controversy + cross-link

## 5. 自主决策授权(任务书 §6)

按任务书 §6 自主决策:Part 数 / 卡数 / 跳过哪些主题 / evidence_level 评级 / tags / 跨派对照新建 / conflicts 追加 / gaps ✅ resolved 标记 / 字数微调。

例外打断条件未触发(OCR 损坏 < 30% / 未发现完全相反新立场 / SRC-040 安全 / 硬规则未破)。

## 6. 工作流

- Phase B:7 Part subagent **并行启动**,每 subagent 自主提取 + 直接写卡片 + 返回结构化摘要(不返回卡片正文,避免主上下文污染)
- Phase C:1 subagent 反向覆盖审计
- Phase D:1 subagent 跨源整合(related_cards 双向 / conflicts 追加 / evidence_level 升级)
- Phase E:SRC-040.yaml + source_index 单点 Edit + INDEX_BY_SOURCE.md 追加 + progress.md 头部更新 + completion checkpoint + 终端总结

## 7. 不做事项

- 不 git commit(任务书 §10:避免与 SRC-031 WHO session 冲突,完工后用户单独 commit)
- 不打扰用户(已一次性授权)
