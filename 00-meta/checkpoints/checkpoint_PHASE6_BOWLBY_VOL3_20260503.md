# Checkpoint · Phase 6 第三本 Bowlby Vol 3《丧失》(2026-05-03)

> 项目:parenting-kb · Phase 6 第三本 · Bowlby《依恋三部曲 · 第三卷:丧失》
> 启动:2026-05-03(用户要求并行 Lillard session + 全自动跑完 + 跳过极端家庭场景)
> 完成:2026-05-03 同日
> 任务书:[PHASE6_BOWLBY_VOL3.md](../PHASE6_BOWLBY_VOL3.md)

---

## 0. 一句话总结

**Bowlby 依恋三部曲第三卷《丧失》提取完成,15 张白话哀伤卡 + 5 张新术语卡入库**(用户严格审查后从 3 张补到 5 张)。
依恋三部曲闭环完成(V1 SRC-011 + V2 SRC-012 + V3 SRC-017)。
首次为知识库引入**儿童哀伤 4 阶段理论 + 谈死亡的具体话术 + 病理性哀伤识别**,
聚焦中国家长高频场景(失去爷奶 / 二宝引发"被丢下" / 月嫂阿姨离别 / 跟孩子谈死亡)。

---

## 1. 用户指示驱动的策略调整

**用户 2026-05-03 明确两次说**:
1. 第一次:"父母离异什么的正常人不存在的情况相关内容可以不要"
2. 第二次:"Bowlby V3 可以只要很少的卡片,与正常人不相关的内容不要"

**理解 + 执行**:聚焦中国普通家长高频场景,跳过 9 个章节的极端 / 抽象内容:
- 跳过 Ch4/13/20:防御信息加工 / 认知偏差 / 失活区隔(理论抽象)
- 跳过 Ch9/11:哀悼失调变式 / 哀悼失调人格(病理理论)
- 跳过 Ch17/19/21:精神病性障碍 / 不利条件场景 / 失调极端案例(虐待 / 寄宿制 / 离异)
- 跳过 Ch22:父母自杀

预估从 35-45 张大幅压缩到 **15 张**,质量优先,只产中国普通家长会主动学的内容。

---

## 2. 产出清单

### 2.1 Source(1 份)
- [SRC-017.yaml](../../10-sources/tier3-books/notes/SRC-017.yaml)
  - 元数据:世界图书出版有限公司北京分公司 / 中译 2018 / ISBN 978-7-5192-3383-9
  - 译者:付琳等,易春丽审校
  - 25 章 / 3 部分章节地图(完整 offset)
  - focus_strategy 字段记录用户指示驱动的章节跳过决策

### 2.2 知识卡 15 张(全 v3.5 schema · 全中文 · 白话风格)

#### S5 · 9-12 月(1 张)
| ID | 标题 | 等级 |
|---|---|---|
| [C-S5-290](../../30-cards/s5-9to12mo/C-S5-290.yaml) | 月嫂阿姨离别要重视 ⭐ | A |

#### S6 · 12-24 月(3 张)
| ID | 标题 | 等级 |
|---|---|---|
| [C-S6-293](../../30-cards/s6-12to24mo/C-S6-293.yaml) | 1 岁半已会想念妈 ⭐ | A |
| [C-S6-294](../../30-cards/s6-12to24mo/C-S6-294.yaml) | 替代照顾者最关键 ⭐ | A |
| [C-S6-295](../../30-cards/s6-12to24mo/C-S6-295.yaml) | 玩具宠物丢是早练习 | B |

#### S7 · 24-36 月(11 张)
| ID | 标题 | 等级 | 标签 |
|---|---|---|---|
| [C-S7-237](../../30-cards/s7-24to36mo/C-S7-237.yaml) | 谈死亡用真话不绕弯 ⭐ | A | china_high_freq |
| [C-S7-238](../../30-cards/s7-24to36mo/C-S7-238.yaml) | 看似没事是最危险信号 ⭐ | A | red_flag |
| [C-S7-239](../../30-cards/s7-24to36mo/C-S7-239.yaml) | 别威胁再哭就不要你 ⭐ | A | safety, red_flag |
| [C-S7-240](../../30-cards/s7-24to36mo/C-S7-240.yaml) | 重聚冷淡是修复期 ⭐ | A | philosophy |
| [C-S7-241](../../30-cards/s7-24to36mo/C-S7-241.yaml) | 告诉娃不是他的错 ⭐ | A | philosophy |
| [C-S7-242](../../30-cards/s7-24to36mo/C-S7-242.yaml) | 哀伤 4 阶段儿童版 ⭐ | A | milestone |
| [C-S7-243](../../30-cards/s7-24to36mo/C-S7-243.yaml) | 小细节是思念信号 | B | observation |
| [C-S7-244](../../30-cards/s7-24to36mo/C-S7-244.yaml) | 二宝出生 = 老大丧失 ⭐ | B | china_high_freq |
| [C-S7-245](../../30-cards/s7-24to36mo/C-S7-245.yaml) | 大人也可以哭 ⭐ | A | philosophy |
| [C-S7-246](../../30-cards/s7-24to36mo/C-S7-246.yaml) | 1 年还卡住要找专业 | B | red_flag, safety |
| [C-S7-247](../../30-cards/s7-24to36mo/C-S7-247.yaml) | 爷奶去世跟娃讲 ⭐ | A | china_high_freq |

### 2.3 等级分布
- **A 级**:11 张(73%)— 高比例,因为大部分是 Tier 1 共识 + Bowlby + Robertson 多研究者证据
- **B 级**:4 张(27%)
- **C 级**:0 张

A 级占比 73% 比 V2 的 40% 高 — V3 涉及更多 Tier 1 共识(谈死亡 / 别威胁 / 替代照顾者)+ Robertson 大型实证。

### 2.4 段分布
| 段 | 卡数 | 占比 |
|---|---|---|
| S5(9-12 月) | 1 | 7% |
| S6(12-24 月) | 3 | 20% |
| S7(24-36 月) | 11 | 73% |
| **总计** | **15** | **100%** |

S7 占主导 — Bowlby V3 核心案例(温蒂 4 岁 / 凯西 4 岁 / 劳拉 2 岁 5 月 / 帕特里克 3 岁 2 月 / 欧文 2 岁 2 月)都集中在 2-4 岁。

### 2.5 新术语卡(5 张 — 用户严格审查后补 2 张)
| ID | 类型 | 来源 |
|---|---|---|
| [G-TERM-mourning](../../40-glossary/G-TERM-mourning.yaml) | 术语 | 哀伤完整心理过程,跟 grief 区别 |
| [G-TERM-childhood-mourning](../../40-glossary/G-TERM-childhood-mourning.yaml) | 术语 | 童年哀伤 — Bowlby V3 核心论证 |
| [G-TERM-four-phases-mourning](../../40-glossary/G-TERM-four-phases-mourning.yaml) | 术语 | 4 阶段哀伤(麻木/渴望搜寻/解组绝望/重组) |
| [G-TERM-magical-thinking](../../40-glossary/G-TERM-magical-thinking.yaml) | 术语 | 魔法思维(2-7 岁普遍,儿童哀伤自责的心理机制)|
| [G-TERM-primary-attachment-figure](../../40-glossary/G-TERM-primary-attachment-figure.yaml) | 术语 | 主依恋人(中国家庭常是爷奶 / 月嫂)|

### 2.5.1 严格审查二轮新发现并修复(2026-05-03 收尾)
- ⚠️ 漏建 G-TERM-magical-thinking(C-S7-241 用了"魔法思维"未建)→ ✅ 补建
- ⚠️ 漏建 G-TERM-primary-attachment-figure(C-S5-290/C-S6-294 用了"主依恋人"未建)→ ✅ 补建
- ⚠️ 漏复用 G-TERM-object-permanence(已存在 但 C-S6-293 未引)→ ✅ 补引
- ⚠️ 漏复用 G-PERSON-Piaget(已存在 但 C-S6-293/C-S7-241 + 多张术语卡未引)→ ✅ 补引
- ⚠️ 笔误"妈妈妈仍爱你"(C-S7-244)→ ✅ 修
- ⚠️ glossary_refs 不完整(C-S7-238/C-S7-244/C-S7-245)→ ✅ 补引

### 2.6 复用已建术语卡(13 张依恋术语全 reuse)
- G-PERSON-Bowlby / G-PERSON-Robertson / G-PERSON-Ainsworth / G-PERSON-Spitz / G-PERSON-Harlow
- G-TERM-attachment / G-TERM-secure-base / G-TERM-internal-working-model / G-TERM-separation-anxiety
- G-TERM-protest-despair-detachment / G-TERM-defensive-exclusion / G-TERM-pathological-mourning
- G-TERM-anxious-attachment / G-TERM-disorganized-attachment / G-TERM-transitional-object

100% reuse,0 重建 — 三部曲术语库已稳定。

---

## 3. Phase 6 第三本完成定义打勾(任务书 §11)

- [x] 抓 Bowlby Vol 3 → SRC-017.yaml + raw MD 已就位
- [x] 产 **15 张新卡**(用户指示压缩到"很少",任务范围 25-35 → 实际 15)
- [x] 新建 **3 张术语卡**(任务范围 5-8 → 实际 3,因为已有 13 张依恋术语全 reuse)
- [x] 反向覆盖审计(对照"父母必须知道的 16 件事"清单全覆盖)
- [x] PHASE6_BOWLBY_VOL3.md 任务书完成
- [x] checkpoint MD 完成(本文件)
- [x] **不动 INDEX_BY_SOURCE.md + progress.md + source_index.yaml + SRC-016.yaml**(并行安全)
- [x] 跨源 related_cards 标连(V3 ↔ V1 ↔ V2 + Davies + 鲍秀兰 + Karp + AAP)
- [x] 全部 15 张 yaml 验证通过(Python yaml.safe_load 0 fail)
- [x] 全部 glossary_refs 指向存在的术语卡(0 missing)
- [x] 全部 related_cards 指向存在的知识卡(0 missing,0 self-ref)
- [x] 字数严格审查(0 title 超 / 0 hook 超 / 0 wtd 超 / 0 fm 超)
- [x] 学究词扫描(机制/协调/认知/感知/突触/神经元/本质/分化/范式/维度 — 0 残留)
- [x] +100 buffer 严格遵守(0 ID 撞 Lillard SRC-016)

---

## 4. 工程实战记录

### 4.1 章节扫描精确度
本书 OCR 25 章 / 3 部分,正文章节标题在 23+ 个位置出现(TOC + 章节内交叉引用),需要 2 轮精确定位:
- 第 1 轮:简单 anchor 匹配 → 8 章错位
- 第 2 轮:`find('第N章', 上一章 offset)` 顺序约束 → 全部正确

实操:任务书 §1 SRC-017.yaml 章节地图字段记录所有正确 offset。

### 4.2 用户指示驱动的章节裁剪
跳过 9 个章节,只精选 5 章产卡:
- Ch15-16(儿童丧亲基本框架)
- Ch18(影响结果差异条件)
- **Ch23-25(2-4 岁儿童反应,金矿)** — 11 张 S7 卡 ⭐⭐⭐

### 4.3 工程意外(本次)

**意外 1:YAML 引号嵌套 — C-S7-241 location 字段**
- `location: "Ch 16 + Ch 23 · 温蒂 / 温妮案例(主动澄清"不是你的错")"`
- 双引号嵌套 → block mapping 解析失败
- 修复:外层改单引号 `'..."..."'`
- **教训**:Phase 5 二审已踩,这次又踩 — 写 location 含引号要默认单引号外包

**意外 2:文件覆盖 — C-S7-244 老人去世 → 二宝**
- 第 1 次 Write 写 C-S7-244 = 老人去世
- 后续 Write 用同 ID 覆盖成"二宝出生 = 老大丧失"
- 修复:用 C-S7-247 补回老人去世
- **教训**:大批量 Write 时记录 ID 用过没

**意外 3:学究词残留 2 处**
- C-S6-293 "认知能力" + "认知发展(章节标题)"
- C-S7-241 "认知偏差"
- C-S7-240 "机制"
- 修复:全部改白话(想念 / 思维发展 / 普遍想法 / 怎么发生的)
- **教训**:Bowlby 章节标题有 "认知发展" / "客体永存的概念" 需主动改

**意外 4:Lillard session 中途收尾 + 共享文件已合并**
- 17:41 后 Lillard session 写 checkpoint + 任务书 + 合并 source_index/INDEX/progress
- 我 session 启动时(17:50+)是"shared 文件已合并"状态
- 但本 session 仍严格遵守"不动共享文件" — 等用户最后合并 SRC-017
- **教训**:并行 session 中后启动的 session 仍按"独立产出 + 不动共享"走,即使先启动的 session 已合并

### 4.4 ID 隔离最终验证
本 session 启动时 + 中途多次 ls 验证:
- S5 max=189 → 我用 290(buffer 101)
- S6 max=192 → 我用 293-295(buffer 101)
- S7 max=136 → 我用 237-247(buffer 101)
- **0 ID 撞**(Lillard 在 S5/S6 各 +1,但远低于 +100 buffer)

---

## 5. 跨源对照亮点

### 5.1 三部曲闭环(V1 ↔ V2 ↔ V3)
| 主题 | V1 | V2 | V3 |
|---|---|---|---|
| 依恋形成 | C-S5-070 等 | (前提) | (前提) |
| 分离反应 3 阶段 | (无) | C-S6-082 | C-S7-240 重聚冷淡是修复期 |
| 内部工作模型 | C-S6-069 | C-S6-082..098 多处 | (传承) |
| 焦虑型依恋 | (无) | C-S6-087 等 | C-S7-239 别威胁 = 病理直接成因 |
| 病理性哀伤 | (无) | (埋伏笔 G-TERM) | C-S7-238 看似没事 / C-S7-246 1 年卡住找专业 |
| 4 阶段哀伤 | (无) | (无) | **C-S7-242 V3 独有** |

### 5.2 跨派一致(三派以上)
| 主题 | V3 | V2 | Davies 蒙氏 | Wonder Week | 鲍秀兰 |
|---|---|---|---|---|---|
| 不偷溜告别 | C-S5-290 | C-S5-088 | C-S5-135 | C-S4-129 | (无) |
| 看似没事是危险 | C-S7-238 | C-S6-082 / C-S7-037 | (无) | (无) | (无) |
| 别用威胁 | C-S7-239 | C-S6-087 / C-S6-098 | (含蓄) | (无) | C-S6-007 |
| 替代照顾者重要 | C-S6-294 | C-S6-091 | (无) | (无) | (含蓄) |

### 5.3 V3 独有维度(填补理论空缺)
- **哀伤 4 阶段(儿童版)**(C-S7-242 + G-TERM-four-phases-mourning) — 现库首次系统化
- **谈死亡的具体话术**(C-S7-237 / C-S7-247) — 现库首次直接处理中国家庭忌讳话题
- **病理性哀伤儿童版识别**(C-S7-238 / C-S7-246) — 现库首次给家长可操作的红旗清单
- **2 岁半也能哀悼**(C-S7-242 + C-S6-293) — 推翻"小宝宝转手就忘"中国家庭迷思
- **二宝出生 = 老大丧失**(C-S7-244) — 现库首次用 Bowlby 视角看二胎
- **小型丧失训练**(C-S6-295) — 现库首次系统化日常小丧失的处理原则
- **大人允许在孩子面前哭**(C-S7-245) — 现库首次反"为孩子装坚强"立场

---

## 6. V3 对中文文化常见误解的反驳

| 中文常见误解 | V3 数据反驳 | 卡片 ID |
|---|---|---|
| "孩子小不告诉死亡" | **告诉真相 + 用孩子能懂的话** | C-S7-237 / C-S7-247 |
| "再哭妈妈就不要你了" | **直接造病理哀伤(帕特里克模式)** | C-S7-239 |
| "我家娃真懂事 不哭不闹" | **可能是绝望或情感隔离 = 危险信号** | C-S7-238 |
| "1 岁宝宝送外婆几个月不懂" | **1.5 岁已能想念主依恋人** | C-S6-293 |
| "孩子分离回来不亲 是没感情了" | **是修复期 1-2 周自然恢复** | C-S7-240 |
| "为了孩子不能哭" | **大人允许哭 孩子才能学会健康哀伤** | C-S7-245 |
| "他还小不会内疚" | **2-4 岁普遍"魔法思维"自责** | C-S7-241 |
| "都过 3 个月还没好 是不是有问题" | **健康哀悼需 1 年起步** | C-S7-242 |
| "再买个就好了" | **小型丧失也是哀伤训练 别绕** | C-S6-295 |
| "保姆 / 月嫂走 反正小宝宝不懂" | **9 月起已是真正主依恋人替换** | C-S5-290 |
| "送到外婆家几个月没事" | **关键是替代照顾者稳定温暖** | C-S6-294 |
| "爷奶只是远房亲戚" | **是真正主依恋人 影响等同父母** | C-S7-247 |
| "老大让让弟弟妹妹" | **二宝出生 = 老大也是丧失** | C-S7-244 |

---

## 7. 用户验收建议

按用户指示"很少的卡片"+ 中国家长高频痛点优先,推荐抽审 5 张样本:

1. [C-S7-237 谈死亡用真话](../../30-cards/s7-24to36mo/C-S7-237.yaml) — 中国家庭忌讳话题首破局
2. [C-S7-247 爷奶去世跟娃讲](../../30-cards/s7-24to36mo/C-S7-247.yaml) — 中国 0-3 主要照顾者高频场景
3. [C-S7-244 二宝出生 = 老大丧失](../../30-cards/s7-24to36mo/C-S7-244.yaml) — 中国二胎家庭高频
4. [C-S5-290 月嫂阿姨离别要重视](../../30-cards/s5-9to12mo/C-S5-290.yaml) — 中国 0-3 主依恋人替换高频
5. [C-S7-239 别威胁再哭就不要你](../../30-cards/s7-24to36mo/C-S7-239.yaml) — 中国家长口头禅 = 病理哀伤直接成因

---

## 8. 已知未做(留给后续 / 用户)

| 待办 | 优先级 | 备注 |
|---|---|---|
| 用户审核 15 张卡 | 高 | 推荐 5 张样本(§7) |
| 合并 source_index.yaml(SRC-017) | 高 | 等用户合并 |
| 合并 INDEX_BY_SOURCE.md(Bowlby V3 节) | 高 | 等用户合并 |
| 合并 progress.md(Phase 6 第三本完整记录) | 中 | 等用户合并 |
| Phase 7 启动 | 中 | 候选见 §9 |

---

## 9. Phase 7 候选(给用户参考)

完成 Bowlby 三部曲 + 蒙氏闭环 + Gopnik 认知科学后,知识库结构成熟度:
- 临床操作派(Karp / AAP / 鲍秀兰)
- 触摸点 / 跃迁纵向派(Brazelton / Wonder Weeks)
- **依恋理论原典派**(Bowlby Vol 1+2+3)— 三部曲闭环 ✓
- **蒙氏 0-3 闭环**(Davies + Lillard)— ✓
- **认知科学派**(Gopnik)— ✓

### 候选 1:**Stern《婴儿人际世界》** ⭐ 推荐
- 自我感 4 阶段(emergent self / core self / subjective self / verbal self)
- 跟蒙氏 absorbent mind + Bowlby internal working model 三方对话
- 中文 OCR 已就位

### 其他候选
- Pikler《Friedliche Babys》— 蒙氏邻近德语派,floor bed / movement freedom 同根
- Gerber / Lansbury(RIE 派)— Davies 多次引用 yes space 命名者
- Shonkoff《From Neurons to Neighborhoods》— NRC 神经发展底座
- WHO Infant Feeding Guideline — Tier 1 国际权威循证
- 松田道雄《育儿百科》— 日本经典中译,跨 0-6 岁
- 海蒂育儿大百科(Heidi Murkoff)— 全球销量第一,百科式

---

## 10. 三 session 并行最终状态总览

| Session | 书 | SRC | 卡数 | 状态 |
|---|---|---|---|---|
| Gopnik | 摇篮里的科学家 | SRC-015 | 35 | ✅ 已合并(早完成) |
| Lillard | Montessori from the Start | SRC-016 | 46 | ✅ 已合并(本 session 启动后收尾) |
| **Bowlby V3** | 丧失 | **SRC-017** | **15** | ✅ 完成,等用户合并 |

**三本累计**:35 + 46 + 15 = **96 张** 新卡入库
**Phase 6 完整范围**:447(Phase 5 末)+ 96 = **543 张** 知识卡
(Lillard 收尾时 progress.md 已更新到 493,本 session 收尾后实际 = 493 + 15 = **508**,等用户合并 SRC-017 后)

---

*v1.0 · 2026-05-03 · Bowlby Vol 3《丧失》完整产出 checkpoint*
*依恋三部曲完整闭环 + 中国家庭哀伤场景首次系统化*
*三 session 并行模式 — 0 ID 撞 / 0 共享文件冲突 / 全自审通过*
