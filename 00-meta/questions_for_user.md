# 待用户回答的问题

> 我无法/不应替你拍板的判断点,逐条记录在这里。
> 格式:背景 + 选项 + 我的建议 + 最后更新日期。

---

## Q1:附录 B 样本 raw HTML 是否需要补抓

**Status: ✅ RESOLVED 2026-04-30 — Decision: B(Phase 1 启动时顺手补抓)**

**背景**:任务书附录 B 提到的 2 份"已抓样本"(CDC LTSAE 9 月里程碑 + Harvard Serve and Return),用户给我的是 verbatim 整理后的 yaml,**没有保留原始 HTML 文件**。SRC-001 / SRC-002 的 `local_file` 字段我暂时填 `null`。

**影响**:审计追溯路径不完整(URL 能再访问当前版本,但页面可能更新)。

**选项**:
- A. 不补抓 —— verbatim 已记录,raw 文件不是审计必需。永久 `local_file: null`,在 `gaps.md` 标注。
- ✅ B. Phase 1 启动时顺手补抓 —— 把 raw HTML 落到 `tier1-authoritative/raw/`,完整闭环。
- C. 现在就补抓(违反 Phase 0"不抓取"原则)。

**我的建议**:**B**(Phase 1 顺手补,成本低,审计闭环更干净)

**执行**:Phase 1 第一批 fetch 任务里包含 SRC-001/002 raw HTML 重抓,落地到 `10-sources/tier1-authoritative/raw/`,回填 `local_file` + `file_size_bytes`。

**最后更新**:2026-04-30

---

## Q2:Phase 1 启动前是否先购书

**Status: ✅ RESOLVED 2026-04-30 — Decision: A(先 Phase 1,书后买)**

**背景**:Phase 1 是 S1(0-1 月)端到端 POC,核心源是 Tier 1(免费机构)+ Tier 2(免费摘要)。Tier 3 书籍主要用于深度和流派原典,但不是 S1 必需 —— S1 主题清单(任务书 §2)的喂养/安抚/反射/睡眠/筛查/产后妈妈/儿保等都能用 Tier 1/2 覆盖。

**选项**:
- ✅ A. 先 Phase 1,书后买 —— Phase 1 跑通后再决定要不要买书,先验证 schema 和方法论
- B. 先购 S1 强相关的 2-3 本(Karp Happiest Baby + Brazelton Touchpoints + 鲍秀兰《0-3 岁早期教育》),Phase 1 同时启动
- C. 全部购齐再启动

**我的建议**:**A**(Phase 1 先验证流程,书是 Phase 2-3 的深度补充)

**执行**:Phase 1 仅用 Tier 1+2 跑通。Phase 1 验收后再回看 `books_to_buy.md`,根据 S1 卡片质量决定要不要买书补强。

**最后更新**:2026-04-30

---

## Q3:卡片正反面语言策略

**Status: ✅ RESOLVED 2026-04-30 — Decision: B(卡面中文 + verbatim 英文 + 中译参考)**

**背景**:任务书 §4.3 schema `language: zh` 默认中文卡面,但 verbatim 引用是英文。Phase 1 验收点之一是"引用语言偏好"。家庭语言:你 + 太太均能阅读英文,但日常用中文。

**选项**:
- A. 卡面中文 + verbatim 英文原文(背面 sources_summary 用英文,简洁)
- ✅ B. 卡面中文 + verbatim 英文原文 + 中译参考(双语对照,内容更长)
- C. 卡面中文 + verbatim 全部翻译为中文(失真风险高,违反"verbatim"原则)

**我的建议**:**B**(双语对照,失真小,太太或家中长辈用时也能看)

**执行**(卡片 schema 本地约定 v3.1,Phase 1 起生效):
卡片 yaml 在 §4.3 基础上新增字段:

```yaml
back:
  ...
  verbatim_en: |          # 必填: 英文 verbatim(取自 source yaml)
    "..."
  verbatim_zh: |          # 必填: 中译参考(标注为参考,非权威)
    "..." (中译参考,以英文原文为准)
  sources_summary_en: ... # 英文源汇总(简洁)
  sources_summary_zh: ... # 中文源汇总
```

中译以"参考"标记 —— 任何引用主张以英文原文为准,中译只是辅助。

**最后更新**:2026-04-30

---
