# Phase 7 执行任务书 · 临床基础卡补全(AAP HealthyChildren + 中文产科)

> 项目代号:parenting-kb · Phase 7 任务书 · 版本 v1.0(2026-05-03)
>
> **触发**:491 卡审计(`audit_report_491_cards_20260503.md`)发现 12 项 P0 临床缺口 — 知识库目前只有"心理-安抚-依恋"侧,完全空缺循证医学产科+新生儿临床侧。
>
> **接手必读三件套**:
> 1. 本文件(PHASE7_CLINICAL_AAP.md)
> 2. `00-meta/PHASE2_AAP.md` v1.4(§2.6-2.9 schema 规则)
> 3. `00-meta/checkpoints/audit_report_491_cards_20260503.md` §3.1(P0 缺口清单)

---

## 0. 一句话任务

抓 AAP HealthyChildren 未覆盖页面 + 中文卫健委 / 产科指南,补 **30-40 张 S0+S1+S2+S3+S4 临床基础卡**,
解决 491 卡审计标出的 12 项 P0 缺口,把知识库从"心理派偏重"补成"心理 + 临床循证"双轮驱动。

---

## 1. 必读前置(按顺序)

1. **总任务书**:`00-meta/README.md`(v3.0 完整任务书,§0 硬规则不可逾越)
2. **审计报告**:`00-meta/checkpoints/audit_report_491_cards_20260503.md` §3.1(P0 12 项)
3. **Phase 2 规范**:`00-meta/PHASE2_AAP.md` v1.4(§2.6 翻译两步走 / §2.7 前情提要 / §2.8 术语卡 / §2.9 inline 引用)
4. **Phase 1 实战**:`00-meta/PHASE1_KARP.md` §10 实战调整 14 条
5. **已完成 5 张 P0 临床卡范本**:C-S1-091..095(黄疸 / 脐带 / 筛查 / Vit K / 第一次儿保)

---

## 2. 选定的源 + 抓取策略

### Tier 1 主源 — AAP HealthyChildren(已抓 SRC-004~008)
**未覆盖页面待抓**:
- AAP Jaundice in Newborns(C-S1-091 已用初稿,需 verbatim 抓全)
- AAP Umbilical Cord Care(C-S1-092 同上)
- AAP Newborn Screening Tests(C-S1-093 同上)
- AAP Vitamin K and the Newborn(C-S1-094 同上)
- AAP Well-Baby Visits Schedule(C-S1-095 同上)
- AAP Pediatric Symptom Checker(各种红旗)
- AAP Postpartum Depression Resources(产后心理)
- AAP Choking First Aid(噎食处理)
- AAP Vaccine Schedule 2024(2/4/6/9/12/18/24 月完整时间表)

### Tier 4 中文权威源 — 国家卫健委 + 中华医学会
**主要抓取(都有合法公开 PDF/HTML)**:
- 国家卫健委《0-6 岁儿童健康管理服务规范》(2017)
- 国家卫健委《新生儿疾病筛查管理办法》(2009)
- 中国营养学会《0-6 月婴儿喂养指南》(2022)
- 中华医学会儿科学分会《婴儿喂养指南》
- 中国《孕前和孕期保健指南》(中华医学会妇产科学分会)
- 国家免疫规划疫苗儿童免疫程序(2021 修订)

### Tier 3 书籍(预算允许买)
- **Heidi Murkoff《What to Expect the First Year》**(中译版"海蒂育儿大百科"已 OCR,可直接用)— 月-by-月 临床导览
- 中国《实用新生儿学》(邵肖梅主编)— 新生儿临床权威教材
- 《孕产大百科》(腾讯医典编)— 中国本土孕期权威

### 不抓
- 自媒体(知乎 / 小红书 / 微信公众号)
- 营销育儿博客
- 盗版站点

---

## 3. 卡片规范

**完全继承** PHASE2_AAP v1.4(见 PHASE2_AAP.md §2 全部内容):
- v3.5 schema(`glossary_refs` 扁平 list / 前情提要 / inline ID 引用)
- 全中文,白话风格(§2.5)
- **不审字数**(用户已取消,见 `feedback_parenting_kb_no_word_limit.md`)
- hook 默认填(§10.10)
- evidence_level:AAP 卡默认 A(Tier 1 + peer-reviewed)
- 关于争议立场(如 Vit K 拒打)→ controversy tag(已在 C-S1-094 范本)

**ID 规则**(继续从 491 卡审计后续号):
- S0:C-S0-015 起(已用到 C-S0-014)
- S1:C-S1-096 起(已用到 C-S1-095)+ 临床卡续号(注意 C-S1-122-128 是 Bowlby V1 已占)
- S2:C-S2-198 起(已用到 C-S2-189)
- S3:C-S3-196 起(已用到 C-S3-195)
- S4:C-S4-195 起(已用到 C-S4-194)

**SRC 续号**:SRC-017 起(SRC-016 已用)
- SRC-017:中国国家卫健委文档 cluster
- SRC-018:中国营养学会喂养指南
- SRC-019:中华医学会孕产科指南

---

## 4. 12 项 P0 主题清单(对应审计 §3.1)

按段 + 优先级排序:

### S0 段(产前)
1. **C-S0-015..017 产检窗口** — NT / 大排畸 / 糖耐 / B 群链 / 抗 D 注射时间表(新建 3 张)
2. **C-S0-018..020 待产包 + 分娩计划** — 临产 2 周操作清单 + 自然分娩 vs 剖宫产决策 + 无痛分娩 Q&A(3 张)
3. **C-S0-021..022 妊娠并发症识别** — 妊高 / 妊糖 / 胎位异常 / 先兆早产(2 张)

### S1 段(0-1 月)
- ✅ **C-S1-091 黄疸识别**(已建)
- ✅ **C-S1-092 脐带护理**(已建)
- ✅ **C-S1-093 新生儿筛查 4 项**(已建)
- ✅ **C-S1-094 Vit K 注射**(已建)
- ✅ **C-S1-095 第一次儿保 3 节点**(已建)
4. **C-S1-096 维生素 K 拒打 vs 接受立场对比卡**(深化)
5. **C-S1-097 第一周排便异常识别**(胎便 → 母乳便颜色变化 / 警告)
6. **C-S1-098 配方奶冲调安全 + 储存**(水温 / 比例 / 储存时间)
7. **C-S1-099 PURPLE crying 完整框架**(任务书要求,目前只 C-S1-178 提"三 C")
8. **C-S1-100..103 原始反射全套**(Moro / rooting / sucking / palmar / stepping / Babinski)

### S2 段(1-3 月)
9. **C-S2-198..200 2 月儿保 + 第一波疫苗**(DTaP/Hib/IPV/PCV/HepB/Rotavirus 时间表 + 接种反应 + 中美对照)
10. **C-S2-201 早期昼夜节律萌芽**(melatonin 6-8 周 + 晚长睡形成机制)
11. **C-S2-202 被动免疫下降**(母传 IgG 衰减 + 为什么 2-6 月免疫低谷)
12. **C-S2-203 1-3 月皮肤问题**(脂溢性皮炎 / 婴儿痤疮 / 早期湿疹)

### S3 段(3-6 月)
13. **C-S3-196..198 母乳→混合喂养过渡**(配方奶选购 / 一天混几次 / 怎样追奶 / 妈妈上班后挤奶,3 张)
14. **C-S3-199 4 月儿保 + 第二波疫苗**(2/4 月相邻节点)

### S4 段(6-9 月)
15. **C-S4-195 过敏原引入(LEAP)**(花生/鸡蛋/牛奶 6 月起早暴露)
16. **C-S4-196 噎食 vs 干呕区分**(gag 反射 vs 真噎,关键安全)
17. **C-S4-197 6 月儿保 + 第三波疫苗**
18. **C-S4-198 9 月儿保 + ASQ 发育筛查**

### S6/S7 段
19. **C-S7-137 24 月 M-CHAT 自闭症标准化筛查**(对照鲍秀兰 24 月红旗清单)

**总计:30+ 张新临床卡**(部分议题需多张拆分)

---

## 5. 工作流(继承 Phase 2 改进)

### 5.1 抓取阶段
- WebFetch 抓 AAP HealthyChildren 页面 + 中文卫健委公开 PDF
- 每页 raw 存 `10-sources/tier1-authoritative/raw/aap_<topic>.html`
- 中文卫健委 PDF 存 `10-sources/tier4-chinese/raw/`
- > 50KB 用 subagent(§7.2 任务书)
- chunk 大小 ~5KB(§10.13 §1)

### 5.2 source yaml 生成
- 每个主题 cluster 一份 SRC-XXX.yaml
- AAP 子主题:补到 SRC-004~008 已有 cluster(不新建 SRC)
- 中文新源:SRC-017(卫健委)/ SRC-018(营养学会)/ SRC-019(医学会)
- verbatim 字段保留英文原文 + 中文翻译参考

### 5.3 卡片生成 · 双轨并行
- **A 轨**:产新 P0 临床卡(优先填空白)
- **B 轨**:cross-validate 鲍秀兰 vs AAP / 卫健委 / 中华医学会立场(中西对照)

### 5.4 反向覆盖审计(§10.4)
每段产卡完成后,跑反向审计:
- 独立读 AAP + 卫健委原文 chunks
- 不带先验,从零列"父母最该知的临床事项"
- 与已写卡 diff,补漏 / 删冗 / 合并

### 5.5 跨段 + 跨派整合
- Phase 7 完成后,跑一次"全段红旗信号 + 儿保 + 疫苗时间链"完整性审计
- 和 491 卡审计 §3.3 红旗信号月龄链对照,补缺(9-10 月 + 12-15 月节点)
- 加 1 张"S1-S6 完整儿保 + 疫苗时间表"导航大卡

---

## 6. 完成定义

- [ ] 30-40 张新临床卡(覆盖 12 项 P0)
- [ ] 3 个新 SRC(SRC-017 卫健委 + SRC-018 营养学会 + SRC-019 医学会)
- [ ] AAP cluster 5 个 SRC 内补充 5-10 张未覆盖页面
- [ ] 全部新卡 v3.5 schema(含前情提要 + glossary_refs 全填 + failure_mode 不空)
- [ ] 红旗信号月龄链补全(9-10 月 + 12-15 月)
- [ ] PHASE7 checkpoint MD
- [ ] progress.md 更新到 Phase 7 完成
- [ ] INDEX_BY_SOURCE.md 加 SRC-017~019 章节

**用户验收**:抽 8 张随机审,6+ 张满意 = Phase 7 通过。
重点验收:S0 产检 + S1 黄疸/脐带/Vit K + S2 2 月疫苗 = 中国家长最焦虑的产房+月子期内容到位。

---

## 7. 与 491 卡审计的衔接

Phase 7 是 491 卡审计 §7 用户决策 Q6 = A 的执行。
本任务书完成后,知识库进化为:
- **从 491 → 525-535 张知识卡**
- **从"心理-安抚-依恋"偏重 → "心理 + 临床循证"双轮驱动**
- **覆盖中国家长产房+月子+第一波疫苗+辅食决策全周期**
- **可作为家庭快速决策手册的"临床部分"**

---

## 8. 启动建议(第一波抓什么)

按 P0 优先级 + 中国家长焦虑度排序:

**第一批(中国家长最痛点)**:
1. C-S2-198..200 2 月儿保 + 疫苗(产假返工高峰相关)
2. C-S0-015..017 产检窗口(孕期家长最焦虑)
3. C-S3-196..198 母乳→混喂过渡(产假结束高峰)
4. C-S1-098 配方奶冲调安全(月嫂常做错的事)

**第二批(临床基础)**:
5. C-S1-097 第一周排便识别
6. C-S2-202 被动免疫下降(为什么 2-6 月感冒多)
7. C-S4-195 过敏原引入 LEAP
8. C-S4-196 噎食 vs 干呕区分

**第三批(覆盖完整性)**:
9. C-S0-021..022 妊娠并发症
10. C-S1-099 PURPLE 完整框架
11. C-S1-100..103 原始反射全套
12. C-S7-137 M-CHAT 筛查

---

## 附录 · 上手 5 分钟

```bash
# 1. 看项目结构
cd ~/Desktop/parenting-kb
ls -la

# 2. 必读三件套(15-20 分钟)
cat 00-meta/PHASE7_CLINICAL_AAP.md                                     # 本文件
cat 00-meta/PHASE2_AAP.md                                              # v1.4 schema
cat 00-meta/checkpoints/audit_report_491_cards_20260503.md             # 审计 §3.1 P0 缺口

# 3. 看已建 5 张 P0 临床卡范本(10 分钟)
cat 30-cards/s1-newborn/C-S1-091.yaml   # 黄疸
cat 30-cards/s1-newborn/C-S1-092.yaml   # 脐带
cat 30-cards/s1-newborn/C-S1-093.yaml   # 筛查
cat 30-cards/s1-newborn/C-S1-094.yaml   # Vit K
cat 30-cards/s1-newborn/C-S1-095.yaml   # 第一次儿保

# 4. 启动:WebFetch AAP 2 月儿保 + 疫苗页(P0 优先级最高)
# https://www.healthychildren.org/English/ages-stages/baby/Pages/AAP-Schedule-of-Well-Child-Care-Visits.aspx
# https://www.healthychildren.org/English/ages-stages/baby/Pages/Recommended-Vaccines-for-2-Month-Olds.aspx

# 5. 中文源:国家卫健委 0-6 岁规范
# http://www.nhc.gov.cn/
# 检索"0-6 岁儿童健康管理服务规范" + "新生儿疾病筛查"
```

---

*v1.0 · 2026-05-03 — 491 卡审计 §7 Q6 = A 决策的执行任务书*
*接手 session:重点抓 12 项 P0 缺口,30-40 张新临床卡,把知识库从"心理偏重"补成"心理 + 临床"双轮驱动*
