# Checkpoint · Phase 4 Bowlby Vol 2 自审补丁(2026-05-03)

> 项目:parenting-kb · Phase 4 第一本 · Bowlby《依恋三部曲 · 第二卷:分离》
> 主 checkpoint:`checkpoint_PHASE4_BOWLBY_VOL2_20260503.md`
> 本文件:**自审后补丁记录**(2026-05-03 同 session 完成)

---

## 0. 一句话总结

按用户要求做完整自审 → 发现 4 维度 7 处问题 → **修 3 处 + 补 2 卡 + 建 2 术语 + 回填 4 张** →
**总计 32 知识卡 + 8 新术语卡**(原 30+6 → 32+8)。

---

## 1. 自审发现(4 维度)

### 维度 1:卡片结构 ⚠️ 3 处小问题

| 问题 | 卡 | 修复 |
|---|---|---|
| what_to_do[2] = 39 字(>35) | C-S6-088 | ✅ 缩短到"入园第一周 3 个叠加,必须妈陪渐进"(20 字)|
| hook = 15 字(>12) | C-S7-034 | ✅ "Robertson 5 招实证" → "Robertson 实测 5 招"(12 字)|
| 学究词"内化" | C-S6-098 | ✅ "每次都内化" → "每次都刻进心里" |

### 维度 2:遗漏的知识点 ⚠️ 2 个大遗漏(必补)

#### 遗漏 1:广场恐怖症 = 焦虑型依恋的成人版(Ch 19)

完全跳过的章节,Bowlby 重新解读传统精神病学:
- 患者真正怕的是"独自离家",不是拥挤本身
- **大部分患者童年期是拒学症儿童**(C-S7-041 已建)
- **代际传递率 ~75%** — 妈妈"舍不得让孩子上学/独立"实际是自己未解决的焦虑型依恋
- 中文家长高频:"妈妈陪读到博士" / "妈妈不敢独自坐高铁"

✅ 已补:[C-S7-043](../../30-cards/s7-24to36mo/C-S7-043.yaml) — **妈不舍 = 妈自己焦虑(别把焦虑传下一代)**(A 级)

#### 遗漏 2:父母伪造叙事 → 孩子内部模型崩溃(Ch 20)

完全跳过的章节,Bowlby 揭示:
- 父母真实行为(忽视/苛求/拒绝)vs 父母版本("我极其爱你")严重矛盾
- 孩子的 4 种应对结果(坚持自己/接受父母/妥协/认知崩溃)
- 中文文化"妈妈这么辛苦都是为了你"是经典伪造话术
- Bowlby 推测精神分裂部分起源于此(Ch 20 注 5)

✅ 已补:[C-S6-099](../../30-cards/s6-12to24mo/C-S6-099.yaml) — **我是为你好的陷阱(真实体验 vs 妈妈版本)**(B 级)

### 维度 3:遗漏的术语卡 ⚠️ 2 处

| 缺卡 | 处理 |
|---|---|
| 角色倒置(role reversal)— C-S6-093 / S7-041 / S7-043 多处用 | ✅ 已建 [G-TERM-role-reversal](../../40-glossary/G-TERM-role-reversal.yaml) |
| 广场恐怖症(agoraphobia)— C-S7-043 主题 | ✅ 已建 [G-TERM-agoraphobia](../../40-glossary/G-TERM-agoraphobia.yaml) |

### 维度 4:跨源术语卡 related_cards 回填(双向引用) ⚠️ 4 处

Vol 1 已建的核心术语卡 related_cards 没有 link 到 Vol 2 新卡,渲染时检索体验不全:

| 术语卡 | 操作 |
|---|---|
| [G-PERSON-Bowlby](../../40-glossary/G-PERSON-Bowlby.yaml) | ✅ 加入 4 张 Vol 2 代表卡(C-S6-082/097/S7-042 + Vol 1 C-S5-070) |
| [G-TERM-internal-working-model](../../40-glossary/G-TERM-internal-working-model.yaml) | ✅ 加入 5 张 Vol 2 卡(082/086/097/099/S7-040)+ source_id: SRC-012 |
| [G-TERM-separation-anxiety](../../40-glossary/G-TERM-separation-anxiety.yaml) | ✅ 加入 4 张 Vol 2 卡(082/S7-034/035/039)+ source_id: SRC-012 |
| [G-TERM-attachment](../../40-glossary/G-TERM-attachment.yaml) | ✅ 加入 5 张 Vol 1+Vol 2 入口卡 + source_id: SRC-011/012 |

---

## 2. 补丁后产出清单

### 2.1 新增知识卡(2 张)

| ID | 标题 | 等级 | 段 |
|---|---|---|---|
| [C-S6-099](../../30-cards/s6-12to24mo/C-S6-099.yaml) | 我是为你好的陷阱 | B | S6 |
| [C-S7-043](../../30-cards/s7-24to36mo/C-S7-043.yaml) | 妈不舍 = 妈自己焦虑 | A | S7 |

### 2.2 新增术语卡(2 张,本 session 自审)

| ID | 类型 | 来源 |
|---|---|---|
| [G-TERM-role-reversal](../../40-glossary/G-TERM-role-reversal.yaml) | 术语 | 角色倒置(Bowlby 拒学症 A 模式核心机制) |
| [G-TERM-agoraphobia](../../40-glossary/G-TERM-agoraphobia.yaml) | 术语 | 广场恐怖症(Bowlby 重命名"假性恐怖症") |

### 2.3 修复(4 张原卡)

- C-S6-088:what_to_do 字数修复
- C-S7-034:hook 字数修复
- C-S6-098:"内化"→"刻进心里"
- C-S6-099:YAML 列表项首位 `"` 错误修复(audit 中再次踩坑,Vol 1 老问题)

### 2.4 跨源回填(4 张已建术语卡)

- G-PERSON-Bowlby:Vol 2 入口卡
- G-TERM-internal-working-model:Vol 2 关联卡
- G-TERM-separation-anxiety:Vol 2 关联卡
- G-TERM-attachment:Vol 1+Vol 2 入口卡

---

## 3. 最终段分布(本次 session 总产出 = 30 + 2 = 32)

| 段 | 月龄 | 卡数 | 卡 ID 范围 |
|---|---|---|---|
| S5 | 9-12 月 | 4 | C-S5-086..089 |
| S6 | 12-24 月 | **18**(+1) | C-S6-082..099 |
| S7 | 24-36 月 | **10**(+1) | C-S7-034..043 |
| **合计** | | **32 张** | |

术语卡:**8 张**(原 6 + 自审新 2)
- G-PERSON-Robertson
- G-TERM-protest-despair-detachment
- G-TERM-anxious-attachment
- G-TERM-defensive-exclusion
- G-TERM-pathological-mourning
- G-TERM-transitional-object
- G-TERM-role-reversal ⭐ 新
- G-TERM-agoraphobia ⭐ 新

---

## 4. 等级分布(更新)

| 等级 | Vol 2 数量 | 占比 |
|---|---|---|
| A | **13** | 41% |
| B | **19** | 59% |
| C | 0 | 0% |

A 级新增 1 张(C-S7-043)。

---

## 5. 反向覆盖审计:本次自审审过的章节

| chunk | 章节 | 主审产出 | 漏点 | 自审补 |
|---|---|---|---|---|
| 1 | Ch 1 Robertson | 7 张 | 无 | — |
| 2 | Ch 2-3 精神病学+实验 | 5 张 | 无 | — |
| 3 | Ch 7 唤起恐惧 | 4 张 | 无 | — |
| 4 | Ch 14-15 焦虑型成因 | 5 张 | 无 | — |
| 5 | Ch 16-17 反驳溺爱 | 4 张 | 无 | — |
| 6 | Ch 18 学校恐怖症 | 2 张 | 无 | — |
| 7 | Ch 21 安全依恋成长 | 3 张 | 无 | — |
| **新审 8** | **Ch 4 灵长类** | 0 张 | 主题与 Vol 1 C-S1-122 重叠,跳过 | — |
| **新审 9** | **Ch 19 广场恐怖症** | 0 张 | **大遗漏:成人版焦虑型依恋** | ✅ C-S7-043 |
| **新审 10** | **Ch 20 家庭背景遗漏** | 0 张 | **大遗漏:伪造叙事 / 我是为你好** | ✅ C-S6-099 |
| **新审 11** | **Ch 22 人格成长路径** | 0 张 | 主题与 Vol 1 C-S6-069 重叠,跳过 | — |

---

## 6. 跨源对照增强(本次补卡贡献)

### 新增对照点

| 主题 | Vol 2 新卡 | 中文文化高频版本 |
|---|---|---|
| 妈妈自己焦虑投射给孩子 | C-S7-043 | "妈妈陪读" / "妈妈不敢离家" / "孩子上大学妈妈搬过去" |
| "我是为你好"伪造叙事 | C-S6-099 | "妈妈这么辛苦都是为你" / "都是为你好" / "棍棒底下出孝子" |
| 角色倒置(术语化)| G-TERM-role-reversal | "懂事的孩子真贴心" / "妈妈这辈子就指望你了" |
| 广场恐怖症(术语化)| G-TERM-agoraphobia | "妈妈不舍得让孩子离开" |

### Vol 2 ↔ Vol 1 概念深化(完整版)

| 主题 | Vol 1 | Vol 2 |
|---|---|---|
| Internal Working Model | C-S6-069 提及 | **C-S6-082/086/097/099/S7-040 多处应用** |
| 4 类依恋 | C-S5-070..073 分类 | C-S6-082 + 焦虑型依恋术语化 + C-S7-043 成人版 |
| 安全基地 | C-S3-079 | C-S6-097 / C-S7-042 量化 + 成人版 |
| 不打孩子 | C-S6-070 / C-S6-072 | **C-S6-087(威胁离开)+ C-S6-098(撤回爱)+ C-S6-099(伪造叙事)精神虐待 3 形式** |
| 8 月怕生 | C-S4-068 | C-S5-088 复合恐惧机制 |

---

## 7. 用户验收建议(更新版)

按补丁后,推荐抽审 5 张样本卡(中国家长高频痛点优先):

1. [C-S6-099](../../30-cards/s6-12to24mo/C-S6-099.yaml)(**新增** — 我是为你好的陷阱)
2. [C-S7-043](../../30-cards/s7-24to36mo/C-S7-043.yaml)(**新增** — 妈不舍 = 妈自己焦虑)
3. [C-S6-093](../../30-cards/s6-12to24mo/C-S6-093.yaml)(角色倒置 — 跟 G-TERM-role-reversal 配套)
4. [C-S6-087](../../30-cards/s6-12to24mo/C-S6-087.yaml)(再不听话妈妈就走是精神虐待)
5. [C-S6-095](../../30-cards/s6-12to24mo/C-S6-095.yaml)(黏人 ≠ 被宠坏)

---

## 8. 工程意外 + 教训

### 自审中再次踩坑(Vol 1 老问题再现)

1. **YAML 列表项以 `"` 开头**:C-S6-099 第 34 行 `- "我是爱你的"...` 又踩
   - 这是 Vol 1 自审 + Vol 2 主审都已经修过的问题
   - **结论**:每次写新卡都会再次出错;**应固化 YAML lint pre-write 检查**
   - **推荐**:写卡前用模板 + 写后立即 `yaml.safe_load` 单文件验证

### 检测工具改进(自审实战)

本次自审建立的脚本:
1. `field validation` — 必填字段 + 长度限制
2. `xueyong scan` — 学究词扫描(扩展词表)
3. `cross-ref check` — glossary_refs / related_cards 双向有效性
4. `chapter coverage diff` — 反向审计(对照已写卡 vs 原文)
5. `source_id grep` — 检测 Vol 2 文件归属

未来 Phase 5 可直接复用脚本。

---

## 9. 已知未做(留给后续)

| 待办 | 优先级 |
|---|---|
| 用户审核 Bowlby Vol 2 全部 32 张卡 | 高 |
| 合并 source_index.yaml(SRC-012 引用回填 + next_src_id → SRC-013) | 高 |
| 合并 INDEX_BY_SOURCE.md(Vol 2 节添加) | 高 |
| Phase 5 启动:候选见主 checkpoint §7 | 中 |
| 修 5 个 pre-existing YAML 错误(MMR/REM/spoiling-myth/temperament/turn-taking) | 低(非本 session 引入) |
| 父亲依恋角色卡(留蒙台梭利补) | 低 |

---

## 10. 最终验证(全 OK)

```
Vol 2 cards: 32(原 30 + audit 补 2)
新术语卡: 8(原 6 + audit 补 2)
回填术语卡: 4(Bowlby + IWM + 分离焦虑 + 依恋)
YAML errors: 0
Bad glossary refs: 0
Bad card refs: 0
学究词命中: 0(原"内化"已修)
字段长度问题: 0(原 2 处已修)
```

---

*本文件 = Phase 4 第一本(Bowlby Vol 2)自审 + 补丁完整记录*
*主 checkpoint 在 checkpoint_PHASE4_BOWLBY_VOL2_20260503.md*
*与 Vol 1 自审同样模式,但本次发现的"漏章节"(Ch 19 + Ch 20)是 Vol 1 没遇到的*
