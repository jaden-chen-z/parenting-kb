# 找不到的内容

> 抓不到 / 付费墙挡住 / 中译版找不到的源,记录在这。

---

## G1:SRC-001 / SRC-002 raw HTML 缺失

**背景**:附录 B 的 2 份样本 yaml 是 verbatim 整理版,但没有保留对应的 raw HTML 文件。

**影响**:source yaml 中 `local_file: null`,审计追溯路径不完整(虽然 URL 能再访问到当前版本,但页面可能更新)。

**处理**:见 `questions_for_user.md` Q1 —— 候选方案 B(Phase 1 启动时顺手补抓)。

**对应源**:
- SRC-001 https://www.cdc.gov/act-early/milestones/9-months.html
- SRC-002 https://developingchild.harvard.edu/key-concept/serve-and-return/

---

## G2:Harvard "5 Steps for Brain-Building Serve and Return" PDF 待抓

**背景**:K-MECH-CROSS-001 的 `actions` 字段当前是基于 SR 概念的二手概述,**未** verbatim 自 5 Steps PDF。

**影响**:落地动作未达 verbatim 标准,Phase 1 必须补。

**待抓 URL**:
- https://harvardcenter.wpenginepowered.com/wp-content/uploads/2017/06/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf

**处理**:Phase 1 第一批 fetch 任务。

---
