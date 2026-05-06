// cards.jsx — 知识卡片栈
// 卡片数据由 build_cards_json.py 从 30-cards/*.yaml 生成 cards.json,前端 fetch 加载。
// 术语字典由同一脚本生成 glossary.json,Card 内文本会自动识别引用的术语并可点击弹窗。
//
// ─── 通用排版规范 ──────────────────────────────────────
// 每张卡的 back 含 4 个区块,按需出现:
//   lede        : 起首句,引出核心;显示在 title 下方
//   body[]      : 后续段落
//   what[]      : 行动清单 → 编号 01-NN
//   fail        : caveat 段,左竖线 + italic
// 正文支持的轻量 markdown:
//   **xxx**     → 加粗强调(纯加粗,不下划线)
//   术语词       → 自动识别 + 虚下划线 + 可点击弹术语卡(GlossaryPopup)
// ─────────────────────────────────────────────────────

// 多用户:每个用户的收藏 / 进度通过 PKB.auth.dataKey(scope) per-user 隔离。
// 进度 = 该用户在某段中"最远到达过的卡片 idx"。Cards 进入时从进度恢复 idx。


// Claude 官方色系抽出的 5 种纸色
const CARD_COLORS = [
  { bg: '#F5F4EE', ink: '#2a221a' }, // Ivory
  { bg: '#EBE4D2', ink: '#2a221a' }, // Sand
  { bg: '#E8C5B4', ink: '#3a221a' }, // Faded Coral
  { bg: '#CFD9C8', ink: '#1f2a1a' }, // Sage
  { bg: '#D8B4A0', ink: '#3a2218' }, // Warm Clay
];

// 异步加载全部卡片(由 build_cards_json.py 从 30-cards/*.yaml 生成的 cards.json)
// 原 5 张 hardcoded 样卡已移除(2026-05-04)
//
// 缓存破坏:fetch 时加 ?t=<时间戳>,绕过 iOS Safari 永久缓存(cards.json 无版本号)
// 这样每次重生成 JSON 后,刷新页面就能拿到最新数据
function useCards() {
  const [data, setData] = React.useState(null);
  const [error, setError] = React.useState(null);
  React.useEffect(() => {
    fetch('cards.json?t=' + Date.now(), { cache: 'no-store' })
      .then((r) => { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then((j) => setData(j))
      .catch((e) => setError(e));
  }, []);
  return { data, error };
}

// 异步加载术语字典(40-glossary/*.yaml → glossary.json)。
// 返回 { byId: { glossary_id: term }, all: [...] }
function useGlossary() {
  const [data, setData] = React.useState(null);
  React.useEffect(() => {
    fetch('glossary.json?t=' + Date.now(), { cache: 'no-store' })
      .then((r) => r.ok ? r.json() : null)
      .then((j) => {
        if (!j || !j.items) return setData({ byId: {}, all: [] });
        const byId = {};
        j.items.forEach((it) => { byId[it.glossary_id] = it; });
        setData({ byId, all: j.items });
      })
      .catch(() => setData({ byId: {}, all: [] }));
  }, []);
  return data;
}

// 给定卡片的 glossary_refs 和全局 glossary,生成"该卡正文中要识别的搜索词 → 术语"映射。
// 每个术语收集多个搜索别名(display_name 去括号注解 / full_name_zh / full_name_en / aliases[] /
// 各种缩写形式),在 parseRichText 里拿来扫文本。
//
// aliases 字段:词条 yaml 中 `aliases: [5S, 5S 法]` 这类列表,补简写 / 同义词。
// 详见 conflicts_data/README.md(语言规范) 与各词条 yaml。
function buildSearchTerms(glossaryRefs, glossaryById) {
  if (!glossaryRefs || !glossaryRefs.length || !glossaryById) return [];
  const terms = [];
  const seen = new Set();
  for (const id of glossaryRefs) {
    const g = glossaryById[id];
    if (!g) continue;
    const aliases = new Set();
    // display_name 形如 "第四产程 (fourth trimester)" — 取括号前主名 + 括号内英文
    const dn = (g.display_name || '').trim();
    if (dn) {
      const m = dn.match(/^(.+?)\s*[\(（]\s*(.+?)\s*[\)）]\s*$/);
      if (m) {
        aliases.add(m[1].trim());
        aliases.add(m[2].trim());
      } else {
        aliases.add(dn);
      }
    }
    if (g.full_name_zh) aliases.add(g.full_name_zh.trim());
    if (g.full_name_en) aliases.add(g.full_name_en.trim());
    // aliases[] — 词条手工补的简写 / 同义词
    if (Array.isArray(g.aliases)) {
      for (const a of g.aliases) {
        if (a && typeof a === 'string') aliases.add(a.trim());
      }
    }
    for (const alias of aliases) {
      if (!alias || alias.length < 2) continue;       // 太短的容易误匹配
      const key = alias.toLowerCase();
      if (seen.has(key)) continue;
      seen.add(key);
      terms.push({ alias, glossary: g });
    }
  }
  // 按长度降序排,避免 "AAP" 命中 "AAPI" 这种前缀冲突
  terms.sort((a, b) => b.alias.length - a.alias.length);
  return terms;
}

// 把 hex ink 色变成不同透明度
function inkAlpha(hex, a) {
  const h = hex.replace('#', '');
  const r = parseInt(h.substr(0, 2), 16);
  const g = parseInt(h.substr(2, 2), 16);
  const b = parseInt(h.substr(4, 2), 16);
  return `rgba(${r},${g},${b},${a})`;
}

// ── 收藏 + 进度 都走 server API(本地 admin_server.py / 云端 Cloudflare Functions)
// CardStack 顶层一次性加载 favorites + progress,通过 props 传给 Card。
// 收藏数据是 ordered list,顺序 = 展示顺序;新收藏 push 末尾(未浏览部分后面)。
// 进度只升不降(回看不让倒退),scope = 'stage:S1' | 'favorites'。

// 单张卡片
function Card({ data, total, color, glossaryById, cardsById, onTermClick, onCardClick, isFavorited, onToggleFavorite }) {
  const ink = color.ink;
  const ink55 = inkAlpha(ink, 0.55);
  const ink70 = inkAlpha(ink, 0.7);
  const ink40 = inkAlpha(ink, 0.4);
  const ink25 = inkAlpha(ink, 0.25);
  const ink08 = inkAlpha(ink, 0.08);
  // fav 状态由 CardStack 顶层 favList 派生,toggle 也由顶层 setter 派发(走 API)
  const fav = !!isFavorited;
  const toggleFav = (e) => {
    if (e) e.stopPropagation();
    if (onToggleFavorite) onToggleFavorite(data.card_id);
  };
  // 当前卡的术语搜索表 — 在卡 props 变时重算一次
  const searchTerms = React.useMemo(
    () => buildSearchTerms(data.glossary_refs, glossaryById),
    [data.glossary_refs, glossaryById]
  );
  // ctx 一次性传给所有 parseRichText 调用
  const richCtx = { searchTerms, onTermClick, cardsById, onCardClick, ink };
  return (
    <div style={{
      width: '100%',
      height: '100%',
      borderRadius: 18,
      overflow: 'hidden',
      position: 'relative',
      background: color.bg,
      boxShadow: '0 18px 48px rgba(60,40,20,0.28), 0 2px 0 rgba(255,255,255,0.45) inset',
      color: color.ink,
      ['--ink']: ink,
      ['--ink-55']: ink55,
      ['--ink-40']: ink40,
      ['--ink-25']: ink25,
      fontFamily: "ui-sans-serif, -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif",
      display: 'flex',
      flexDirection: 'column',
    }}>
      {/* 极轻纸质质感：一层很深但很淡的 noise + 周边微暗角。不强到能被看作“纹理” */}
      <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none', borderRadius: 18 }}
           preserveAspectRatio="none">
        <defs>
          <filter id={`grain-${data.card_id}`}>
            <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed={data.no * 7 + 11} />
            <feColorMatrix values={`0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.5 0`} />
          </filter>
          <radialGradient id={`vig-${data.card_id}`} cx="0.5" cy="0.5" r="0.85">
            <stop offset="0.65" stopColor="rgba(0,0,0,0)" />
            <stop offset="1" stopColor="rgba(0,0,0,0.12)" />
          </radialGradient>
        </defs>
        <rect width="100%" height="100%" filter={`url(#grain-${data.card_id})`} opacity="0.07" style={{ mixBlendMode: 'multiply' }} />
        <rect width="100%" height="100%" fill={`url(#vig-${data.card_id})`} />
      </svg>

      {/* 卡片内容 */}
      <div style={{
        position: 'relative',
        padding: '40px 34px 30px',
        display: 'flex',
        flexDirection: 'column',
        gap: 0,
        height: '100%',
        overflow: 'auto',
      }}>
        {/* 顶部 eyebrow：收藏勾选框 · 一根细横 · 卡号 */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 9.5,
          letterSpacing: '0.24em',
          color: ink55,
        }}>
          <button
            onClick={toggleFav}
            onMouseDown={(e) => e.stopPropagation()}
            onPointerDown={(e) => e.stopPropagation()}
            style={{
              all: 'unset',
              display: 'inline-flex',
              alignItems: 'center',
              gap: 7,
              cursor: 'pointer',
              fontFamily: 'inherit',
              fontSize: 'inherit',
              letterSpacing: 'inherit',
              color: fav ? ink : ink55,
            }}
          >
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: 13, height: 13,
              border: `1px solid ${fav ? ink : ink40}`,
              borderRadius: 2,
              background: fav ? ink : 'transparent',
              transition: 'all 0.15s ease',
            }}>
              {fav && (
                <svg width="9" height="9" viewBox="0 0 9 9" fill="none">
                  <path d="M1.5 4.8 L3.5 6.8 L7.5 1.8" stroke={color.bg} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              )}
            </span>
            收藏
          </button>
          <span style={{ flex: 1, height: 1, background: ink25 }} />
          <span>{String(data.no).padStart(2, '0')} / {String(total).padStart(2, '0')}</span>
        </div>

        {/* hook —— 副标，衬线 italic，小字号、行距大 */}
        <div style={{
          marginTop: 26,
          fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
          fontSize: 13,
          color: ink55,
          fontStyle: 'italic',
          letterSpacing: '0.06em',
          lineHeight: 1.6,
        }}>
          ——{data.front.hook}
        </div>

        {/* title —— 杂志大标 */}
        <h1 style={{
          margin: '10px 0 0',
          fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
          fontSize: 30,
          fontWeight: 700,
          lineHeight: 1.28,
          letterSpacing: '0.005em',
          color: ink,
          textWrap: 'balance',
        }}>
          {data.front.title}
        </h1>

        {/* lede —— 首段，drop cap 风格的开场
            whiteSpace: pre-wrap — build_cards_json.py 在含列表标记时保留 \n;
                                   纯散文段不含 \n,无视觉影响。 */}
        <p style={{
          margin: '22px 0 0',
          fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
          fontSize: 15,
          lineHeight: 1.85,
          color: ink,
          whiteSpace: 'pre-wrap',
          /* 不用 text-wrap: pretty — 它为避免寡行会把中间行也提前换,中文里看着右边一片留白 */
        }}>
          {parseRichText(data.back.lede, ink, richCtx)}
        </p>

        {/* pull quote —— 数据卡，左竖线 + 大数字 */}
        {data.back.pullQuote && (
          <div style={{
            margin: '22px 0 0',
            paddingLeft: 16,
            borderLeft: `2px solid ${ink40}`,
            display: 'flex',
            alignItems: 'baseline',
            gap: 14,
          }}>
            <div style={{
              fontFamily: "'Noto Serif SC', Georgia, serif",
              fontSize: 32,
              fontWeight: 600,
              letterSpacing: '-0.01em',
              color: ink,
              lineHeight: 1,
            }}>
              {data.back.pullQuote.figure}
              <span style={{
                fontSize: 13,
                fontWeight: 400,
                marginLeft: 4,
                color: ink55,
              }}>{data.back.pullQuote.unit}</span>
            </div>
            <div style={{
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 10,
              letterSpacing: '0.18em',
              color: ink55,
              textTransform: 'uppercase',
              flex: 1,
              lineHeight: 1.4,
            }}>
              {data.back.pullQuote.caption}
            </div>
          </div>
        )}

        {/* body —— 后续段落 */}
        {data.back.body && data.back.body.map((para, i) => (
          <p key={i} style={{
            margin: '16px 0 0',
            fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
            fontSize: 14.5,
            lineHeight: 1.85,
            color: ink,
            whiteSpace: 'pre-wrap',
            /* 不用 text-wrap: pretty,理由同 lede */
          }}>
            {parseRichText(para, ink, richCtx)}
          </p>
        ))}

        {/* 段落分隔 —— 三颗装饰点 */}
        <div style={{
          margin: '30px auto 26px',
          color: ink40,
          letterSpacing: '0.6em',
          fontSize: 11,
        }}>
          ··· 
        </div>

        {/* what —— 编号列表，杂志清单样式 */}
        <div style={{
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 9.5, letterSpacing: '0.24em',
          color: ink55,
          marginBottom: 14,
        }}>
          ACTIONS · 怎么做
        </div>
        <ol style={{
          margin: 0,
          padding: 0,
          listStyle: 'none',
          display: 'flex',
          flexDirection: 'column',
          gap: 14,
          counterReset: 'item',
        }}>
          {data.back.what.map((item, i) => (
            <li key={i} style={{
              display: 'grid',
              gridTemplateColumns: '32px 1fr',
              columnGap: 12,
              alignItems: 'baseline',
            }}>
              <span style={{
                fontFamily: "'Noto Serif SC', Georgia, serif",
                fontSize: 18,
                fontWeight: 500,
                fontStyle: 'italic',
                color: ink55,
                borderBottom: `1px solid ${ink25}`,
                paddingBottom: 2,
                textAlign: 'left',
              }}>{String(i + 1).padStart(2, '0')}</span>
              <span style={{
                fontFamily: "'Noto Serif SC', Georgia, serif",
                fontSize: 14.5,
                lineHeight: 1.7,
                color: ink,
              }}>{parseRichText(item, ink, richCtx)}</span>
            </li>
          ))}
        </ol>

        {/* failure mode */}
        <div style={{
          marginTop: 26,
          padding: '14px 0 14px 16px',
          borderLeft: `3px solid ${inkAlpha(ink, 0.18)}`,
        }}>
          <div style={{
            fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
            fontSize: 9.5, letterSpacing: '0.24em',
            color: ink55,
            marginBottom: 6,
          }}>
            CAVEAT · 常见误区
          </div>
          <div style={{
            fontFamily: "'Noto Serif SC', Georgia, serif",
            fontSize: 13.5,
            lineHeight: 1.85,
            color: ink70,
            fontStyle: 'italic',
            whiteSpace: 'pre-wrap',
          }}>
            {parseRichText(data.back.fail, ink, richCtx)}
          </div>
        </div>

        {/* positions —— 立场对照(仅冲突卡片显示) */}
        {data.back.positions && data.back.positions.views && data.back.positions.views.length > 0 && (
          <div style={{
            marginTop: 26,
            padding: '14px 0 14px 16px',
            borderLeft: `3px solid ${inkAlpha(ink, 0.18)}`,
          }}>
            <div style={{
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 9.5, letterSpacing: '0.24em',
              color: ink55,
              marginBottom: 8,
            }}>
              POSITIONS · 立场对照
            </div>
            {data.back.positions.issue && (
              <div style={{
                fontFamily: "'Noto Serif SC', Georgia, serif",
                fontSize: 13,
                lineHeight: 1.7,
                color: ink70,
                fontStyle: 'italic',
                marginBottom: 12,
              }}>
                {parseRichText(data.back.positions.issue, ink, richCtx)}
              </div>
            )}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {data.back.positions.views.map((v, i) => (
                <div key={i} style={{
                  display: 'grid',
                  gridTemplateColumns: 'minmax(72px, max-content) 1fr',
                  columnGap: 12,
                  alignItems: 'baseline',
                }}>
                  <div style={{
                    fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
                    fontSize: 10,
                    letterSpacing: '0.16em',
                    color: ink,
                    textTransform: 'uppercase',
                    paddingTop: 2,
                  }}>
                    <div style={{ fontWeight: 700 }}>{v.school}</div>
                    {v.source && (
                      <div style={{
                        fontSize: 9,
                        letterSpacing: '0.12em',
                        color: ink55,
                        marginTop: 2,
                        fontWeight: 400,
                      }}>{v.source}</div>
                    )}
                  </div>
                  <div style={{
                    fontFamily: "'Noto Serif SC', Georgia, serif",
                    fontSize: 13.5,
                    lineHeight: 1.75,
                    color: ink,
                  }}>
                    {parseRichText(v.stance, ink, richCtx)}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* citation —— 杂志末尾署名 */}
        <div style={{
          marginTop: 'auto',
          paddingTop: 28,
          display: 'flex',
          alignItems: 'flex-end',
          justifyContent: 'space-between',
          gap: 14,
        }}>
          <div style={{ flex: 1 }}>
            <div style={{
              width: 32, height: 1,
              background: ink40,
              marginBottom: 10,
            }} />
            {/* 书名 / 网站名 / 文档名 — 网站类不用《》(避免视觉撞《Heidi 育儿百科》和"AAP 网页"差别)
                有 url(网站类)→ 整段做超链接;没 url(纸书)→ 普通文本 */}
            {data.citation.url ? (
              <a
                href={data.citation.url}
                target="_blank"
                rel="noopener noreferrer"
                onClick={(e) => e.stopPropagation()}
                style={{
                  fontFamily: "'Noto Serif SC', Georgia, serif",
                  fontSize: 12,
                  fontStyle: 'italic',
                  color: ink70,
                  lineHeight: 1.5,
                  textDecoration: 'underline',
                  textDecorationStyle: 'dotted',
                  textUnderlineOffset: 3,
                }}
              >
                {data.citation.book_zh || data.citation.url}
                <span style={{ fontSize: 9, marginLeft: 4, opacity: 0.6 }}>↗</span>
              </a>
            ) : (
              <div style={{
                fontFamily: "'Noto Serif SC', Georgia, serif",
                fontSize: 12,
                fontStyle: 'italic',
                color: ink70,
                lineHeight: 1.5,
              }}>
                {data.citation.book_zh ? `《${data.citation.book_zh}》` : ''}
              </div>
            )}
            <div style={{
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 9, letterSpacing: '0.14em',
              color: ink55,
              marginTop: 3,
              lineHeight: 1.5,
            }}>
              {data.citation.authors && data.citation.authors.toUpperCase()}
              {data.citation.authors && data.citation.location ? ' · ' : ''}
              {data.citation.location}
            </div>
          </div>
          <div style={{
            fontFamily: "'Noto Serif SC', Georgia, serif",
            fontSize: 18,
            fontWeight: 600,
            color: ink70,
            border: `1px solid ${ink40}`,
            width: 36, height: 36,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            borderRadius: 3,
            letterSpacing: 0,
          }}>
            {data.back.evidence}
          </div>
        </div>
      </div>
    </div>
  );
}

// 通用富文本解析:
//   1. **xxx**         → 强调:纯加粗,**不下划线、不 italic**(让"下划线 = 可点击术语"视觉上唯一)
//   2. ctx.searchTerms → 术语:点击弹 GlossaryPopup,虚线下划线
//   3. C-Sx-NNN 卡片 ID → 点击弹 CardRefPopup,虚线下划线(跟术语视觉一致,统一是"可点深入")
//   ** 包裹的内部也会扫 glossary / 卡片 ID
// ctx = { searchTerms, onTermClick(g, el), cardsById, onCardClick(c, el), ink }
const CARD_REF_RE = /\bC-S[0-9]+-[A-Z0-9_-]+\b/g;

function parseRichText(text, ink, ctx) {
  if (!text) return [];
  let key = 0;

  // 给一段 plain text 扫 glossary,返回 React 元素数组(普通文本 + 可点击 span 混合)
  function scanForGlossary(s) {
    const elements = [];
    if (!s) return elements;
    const terms = ctx && ctx.searchTerms;
    if (!terms || !terms.length) {
      elements.push(<React.Fragment key={key++}>{s}</React.Fragment>);
      return elements;
    }
    const lower = s.toLowerCase();
    let cursor = 0;
    while (cursor < s.length) {
      let bestPos = -1; let bestTerm = null;
      for (const term of terms) {
        const aliasLower = term.alias.toLowerCase();
        const pos = lower.indexOf(aliasLower, cursor);
        if (pos < 0) continue;
        if (bestPos < 0 || pos < bestPos
            || (pos === bestPos && term.alias.length > bestTerm.alias.length)) {
          bestPos = pos; bestTerm = term;
        }
      }
      if (bestTerm == null) {
        elements.push(<React.Fragment key={key++}>{s.slice(cursor)}</React.Fragment>);
        break;
      }
      if (bestPos > cursor) {
        elements.push(<React.Fragment key={key++}>{s.slice(cursor, bestPos)}</React.Fragment>);
      }
      const matchedText = s.slice(bestPos, bestPos + bestTerm.alias.length);
      const g = bestTerm.glossary;
      elements.push(
        <span
          key={key++}
          className="glossary-link"
          onClick={(e) => {
            e.stopPropagation();
            ctx && ctx.onTermClick && ctx.onTermClick(g, e.currentTarget);
          }}
          style={{
            cursor: 'pointer',
            borderBottom: `1.5px dashed ${inkAlpha(ink, 0.55)}`,
            paddingBottom: 1,
          }}
        >{matchedText}</span>
      );
      cursor = bestPos + bestTerm.alias.length;
    }
    return elements;
  }

  // 先按"C-Sx-NNN"切片,每片再扫 glossary。卡片 ID 命中后直接生成可点击 span。
  function scanForCardRefsAndGlossary(s) {
    if (!s) return [];
    const cardsById = ctx && ctx.cardsById;
    const out = [];
    if (!cardsById) return scanForGlossary(s);

    let cursor = 0;
    let m;
    const re = new RegExp(CARD_REF_RE.source, 'g');
    while ((m = re.exec(s)) !== null) {
      const cardId = m[0];
      const card = cardsById[cardId];
      // 没找到对应卡 → 当普通文字处理(避免无效 ref 显示成可点)
      if (!card) continue;
      if (m.index > cursor) {
        const before = scanForGlossary(s.slice(cursor, m.index));
        for (const el of before) out.push(el);
      }
      out.push(
        <span
          key={key++}
          className="card-ref"
          onClick={(e) => {
            e.stopPropagation();
            ctx && ctx.onCardClick && ctx.onCardClick(card, e.currentTarget);
          }}
          style={{
            cursor: 'pointer',
            borderBottom: `1.5px dashed ${inkAlpha(ink, 0.55)}`,
            paddingBottom: 1,
          }}
        >{cardId}</span>
      );
      cursor = m.index + cardId.length;
    }
    if (cursor < s.length) {
      const tail = scanForGlossary(s.slice(cursor));
      for (const el of tail) out.push(el);
    }
    return out;
  }

  const out = [];
  // 切 **xxx** 强调段;每段不论 plain 还是 emphasis 内部都扫 glossary + 卡片 ref
  const re = /\*\*([^*]+)\*\*/g;
  let last = 0; let m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) {
      const plainPart = scanForCardRefsAndGlossary(text.slice(last, m.index));
      for (const el of plainPart) out.push(el);
    }
    const innerElements = scanForCardRefsAndGlossary(m[1]);
    out.push(
      <strong key={key++} style={{
        fontStyle: 'normal',
        fontWeight: 700,
      }}>{innerElements}</strong>
    );
    last = m.index + m[0].length;
  }
  if (last < text.length) {
    const tail = scanForCardRefsAndGlossary(text.slice(last));
    for (const el of tail) out.push(el);
  }
  return out;
}

// ── 术语弹窗 ─────────────────────────────────────────────
// 知识卡里的术语词点击后,弹出此 popup。
// 排版规范参考 Card:米色纸感 + serif 标题 + 顶部 eyebrow + body lede。
// 位置:fixed,贴 stage 区域(宽度=stage 宽,高度=stage 高/2),顶部紧贴被点击词下方,
//       超出 stage 底部时 clamp 在 stage 内。
// 关闭:点击 backdrop / 关闭按钮 / Esc。
function GlossaryPopup({ glossary, anchorRect, stageRect, onClose, cardsById, glossaryById, onSwitchGlossary }) {
  // Esc 关闭(Hook 必须无条件调用,放在 early return 前面)
  React.useEffect(() => {
    const onKey = (e) => { if (e.key === 'Escape') onClose && onClose(); };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);

  if (!glossary) return null;

  // 配色 — 选用 Card 第一色(Ivory)以区别于卡片堆。
  const bg = '#F5F4EE';
  const ink = '#2a221a';
  const ink55 = inkAlpha(ink, 0.55);
  const ink70 = inkAlpha(ink, 0.7);
  const ink40 = inkAlpha(ink, 0.4);
  const ink25 = inkAlpha(ink, 0.25);

  // 位置计算:width/left 锁 stage,height = stage/2,top 在被点击词下方,clamp 在 stage 内
  const popupHeight = Math.max(220, Math.round(stageRect.height / 2));
  let top = anchorRect.bottom + 8;
  if (top + popupHeight > stageRect.bottom) {
    top = Math.max(stageRect.top + 8, stageRect.bottom - popupHeight);
  }
  const left = stageRect.left;
  const width = stageRect.width;

  // 解析 display_name 主名 / 括号注解(如 "第四产程 (fourth trimester)")
  const dn = glossary.display_name || '';
  const dnMatch = dn.match(/^(.+?)\s*[\(（]\s*(.+?)\s*[\)）]\s*$/);
  const titleMain = dnMatch ? dnMatch[1].trim() : dn;
  const titleAnnotation = dnMatch ? dnMatch[2].trim() : '';

  // type 标签
  const typeLabel = ({
    'term': 'TERM · 术语',
    'abbreviation': 'ABBR · 缩写',
    'person': 'PERSON · 人物',
  })[glossary.type] || 'GLOSSARY';

  return (
    <React.Fragment>
      {/* backdrop — fixed 全屏,透明,点击关闭(stopPropagation 阻止子级冒泡到这里) */}
      <div
        onClick={onClose}
        onTouchStart={(e) => { e.stopPropagation(); }}
        onMouseDown={(e) => { /* 让 onClick 触发 */ }}
        style={{
          position: 'fixed', inset: 0,
          background: 'transparent',
          zIndex: 9998,
        }}
      />
      {/* popup 主体 */}
      <div
        onClick={(e) => e.stopPropagation()}
        onMouseDown={(e) => e.stopPropagation()}
        onTouchStart={(e) => e.stopPropagation()}
        onTouchEnd={(e) => e.stopPropagation()}
        style={{
          position: 'fixed',
          top, left, width,
          height: popupHeight,
          background: bg,
          borderRadius: 18,
          boxShadow: '0 20px 56px rgba(60,40,20,0.36), 0 2px 0 rgba(255,255,255,0.55) inset',
          color: ink,
          fontFamily: "ui-sans-serif, -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif",
          display: 'flex', flexDirection: 'column',
          zIndex: 9999,
          overflow: 'hidden',
        }}
      >
        {/* 极轻纸感 noise(参考 Card,但 seed 用 glossary_id 哈希) */}
        <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none', borderRadius: 18 }}
             preserveAspectRatio="none">
          <defs>
            <filter id={`gpop-grain-${glossary.glossary_id}`}>
              <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed={(glossary.glossary_id || '').length * 11 + 7} />
              <feColorMatrix values={`0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.5 0`} />
            </filter>
          </defs>
          <rect width="100%" height="100%" filter={`url(#gpop-grain-${glossary.glossary_id})`} opacity="0.07" style={{ mixBlendMode: 'multiply' }} />
        </svg>

        {/* 内容区(参照 Card 的 padding 节奏) */}
        <div style={{
          position: 'relative',
          padding: '26px 28px 22px',
          display: 'flex', flexDirection: 'column',
          gap: 0,
          height: '100%',
          overflow: 'auto',
        }}>
          {/* 顶部 eyebrow:类型 · 横线 · 关闭 */}
          <div style={{
            display: 'flex', alignItems: 'center', gap: 10,
            fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
            fontSize: 9.5, letterSpacing: '0.24em',
            color: ink55,
          }}>
            <span>{typeLabel}</span>
            <span style={{ flex: 1, height: 1, background: ink25 }} />
            <button
              onClick={onClose}
              style={{
                all: 'unset',
                cursor: 'pointer',
                width: 18, height: 18,
                display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
                fontSize: 13, color: ink55,
                lineHeight: 1,
              }}
              aria-label="关闭"
            >✕</button>
          </div>

          {/* title — 主名(serif 大标) */}
          <h2 style={{
            margin: '20px 0 0',
            fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
            fontSize: 26, fontWeight: 700,
            lineHeight: 1.28, letterSpacing: '0.005em',
            color: ink, textWrap: 'balance',
          }}>
            {titleMain}
          </h2>

          {/* 副名:括号注解 / 中文全名 / 英文全名 */}
          {(titleAnnotation || glossary.full_name_zh || glossary.full_name_en) && (
            <div style={{
              marginTop: 6,
              fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
              fontSize: 12.5, fontStyle: 'italic',
              lineHeight: 1.55, color: ink55,
              letterSpacing: '0.04em',
            }}>
              {[titleAnnotation, glossary.full_name_zh, glossary.full_name_en]
                .filter(Boolean).join('  ·  ')}
            </div>
          )}

          {/* one_liner — 主体段落,lede 风格 */}
          {glossary.one_liner && (
            <p style={{
              margin: '20px 0 0',
              fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
              fontSize: 14.5, lineHeight: 1.85,
              color: ink,
              whiteSpace: 'pre-wrap',
            }}>
              {glossary.one_liner}
            </p>
          )}

          {/* 关联术语 — 点击切换到该术语,popup 不关 */}
          {glossary.related_glossary && glossary.related_glossary.length > 0 && glossaryById && (
            <div style={{ marginTop: 20 }}>
              <div style={{
                fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
                fontSize: 9, letterSpacing: '0.22em', color: ink55,
                marginBottom: 8,
              }}>RELATED · 相关术语</div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 10px' }}>
                {glossary.related_glossary.map((rid) => {
                  const rg = glossaryById[rid];
                  if (!rg) return null;
                  const dnRaw = rg.display_name || rid;
                  const main = (dnRaw.match(/^(.+?)\s*[\(（]/) || [null, dnRaw])[1].trim();
                  return (
                    <button
                      key={rid}
                      onClick={() => onSwitchGlossary && onSwitchGlossary(rg)}
                      style={{
                        all: 'unset',
                        cursor: 'pointer',
                        fontFamily: "'Noto Serif SC', serif",
                        fontSize: 13, lineHeight: 1.4,
                        color: ink,
                        borderBottom: `1.5px dashed ${inkAlpha(ink, 0.45)}`,
                      }}
                    >{main}</button>
                  );
                })}
              </div>
            </div>
          )}

          {/* 关联卡片 — 点击跳到 Cards.html?stage=Sx&card=ID */}
          {glossary.related_cards && glossary.related_cards.length > 0 && cardsById && (
            <div style={{ marginTop: 18 }}>
              <div style={{
                fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
                fontSize: 9, letterSpacing: '0.22em', color: ink55,
                marginBottom: 8,
              }}>RELATED · 相关卡片</div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                {glossary.related_cards.map((cid) => {
                  const cleanId = String(cid).split('#')[0].trim();   // 容许 yaml 里 'C-S1-001  # 备注'
                  const c = cardsById[cleanId];
                  if (!c) return null;
                  const url = `Cards.html?stage=${encodeURIComponent(c.stage)}&card=${encodeURIComponent(cleanId)}`;
                  return (
                    <a
                      key={cleanId}
                      href={url}
                      style={{
                        textDecoration: 'none',
                        fontFamily: "'Noto Serif SC', serif",
                        fontSize: 13, lineHeight: 1.5,
                        color: ink,
                        display: 'flex', alignItems: 'baseline', gap: 8,
                      }}
                    >
                      <span style={{
                        fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
                        fontSize: 9, letterSpacing: '0.14em', color: ink55,
                      }}>{c.stage}</span>
                      <span style={{ borderBottom: `1px dotted ${inkAlpha(ink, 0.4)}` }}>{c.front.title}</span>
                    </a>
                  );
                })}
              </div>
            </div>
          )}

          {/* 底部 — glossary id 小字 */}
          <div style={{
            marginTop: 'auto',
            paddingTop: 16,
            display: 'flex', alignItems: 'center', gap: 8,
          }}>
            <span style={{ width: 24, height: 1, background: ink40 }} />
            <span style={{
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 9, letterSpacing: '0.18em',
              color: ink55,
            }}>{glossary.glossary_id}</span>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

// ── 卡片引用弹窗 ─────────────────────────────────────────────
// 当卡片正文 / 立场对照里出现 C-Sx-NNN 引用,点击时弹此 popup,展示被引用卡的速览。
// 风格跟 GlossaryPopup 一致(米色纸感),底部"打开这张卡"按钮跳到 Cards.html?stage=Sx&card=ID。
function CardRefPopup({ card, anchorRect, stageRect, onClose }) {
  React.useEffect(() => {
    const onKey = (e) => { if (e.key === 'Escape') onClose && onClose(); };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [onClose]);

  if (!card) return null;

  const bg = '#F5F4EE';
  const ink = '#2a221a';
  const ink55 = inkAlpha(ink, 0.55);
  const ink70 = inkAlpha(ink, 0.7);
  const ink40 = inkAlpha(ink, 0.4);
  const ink25 = inkAlpha(ink, 0.25);

  const popupHeight = Math.max(260, Math.round(stageRect.height / 2));
  let top = anchorRect.bottom + 8;
  if (top + popupHeight > stageRect.bottom) {
    top = Math.max(stageRect.top + 8, stageRect.bottom - popupHeight);
  }
  const left = stageRect.left;
  const width = stageRect.width;

  // 跳转链接 — 同段内传 stage + card 让 Cards.html 直接定位到这张卡
  const jumpUrl = `Cards.html?stage=${encodeURIComponent(card.stage)}&card=${encodeURIComponent(card.card_id)}`;

  return (
    <React.Fragment>
      <div
        onClick={onClose}
        onTouchStart={(e) => { e.stopPropagation(); }}
        style={{ position: 'fixed', inset: 0, background: 'transparent', zIndex: 9998 }}
      />
      <div
        onClick={(e) => e.stopPropagation()}
        onMouseDown={(e) => e.stopPropagation()}
        onTouchStart={(e) => e.stopPropagation()}
        onTouchEnd={(e) => e.stopPropagation()}
        style={{
          position: 'fixed',
          top, left, width,
          height: popupHeight,
          background: bg,
          borderRadius: 18,
          boxShadow: '0 20px 56px rgba(60,40,20,0.36), 0 2px 0 rgba(255,255,255,0.55) inset',
          color: ink,
          fontFamily: "ui-sans-serif, -apple-system, 'PingFang SC', 'Noto Sans SC', sans-serif",
          display: 'flex', flexDirection: 'column',
          zIndex: 9999,
          overflow: 'hidden',
        }}
      >
        <svg style={{ position: 'absolute', inset: 0, width: '100%', height: '100%', pointerEvents: 'none', borderRadius: 18 }}
             preserveAspectRatio="none">
          <defs>
            <filter id={`cpop-grain-${card.card_id}`}>
              <feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed={(card.card_id || '').length * 13 + 5} />
              <feColorMatrix values={`0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.5 0`} />
            </filter>
          </defs>
          <rect width="100%" height="100%" filter={`url(#cpop-grain-${card.card_id})`} opacity="0.07" style={{ mixBlendMode: 'multiply' }} />
        </svg>

        <div style={{
          position: 'relative',
          padding: '26px 28px 22px',
          display: 'flex', flexDirection: 'column',
          gap: 0, height: '100%', overflow: 'auto',
        }}>
          {/* 顶部 eyebrow:CARD · 阶段 · 关闭 */}
          <div style={{
            display: 'flex', alignItems: 'center', gap: 10,
            fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
            fontSize: 9.5, letterSpacing: '0.24em',
            color: ink55,
          }}>
            <span>CARD · {card.stage} {card.stageName}</span>
            <span style={{ flex: 1, height: 1, background: ink25 }} />
            <button
              onClick={onClose}
              style={{
                all: 'unset', cursor: 'pointer',
                width: 18, height: 18,
                display: 'inline-flex', alignItems: 'center', justifyContent: 'center',
                fontSize: 13, color: ink55, lineHeight: 1,
              }}
              aria-label="关闭"
            >✕</button>
          </div>

          {/* hook —— 副标 italic */}
          {card.front && card.front.hook && (
            <div style={{
              marginTop: 16,
              fontFamily: "'Noto Serif SC', Georgia, serif",
              fontSize: 13, color: ink55, fontStyle: 'italic',
              letterSpacing: '0.06em', lineHeight: 1.6,
            }}>——{card.front.hook}</div>
          )}

          {/* title — serif 大标 */}
          <h2 style={{
            margin: '8px 0 0',
            fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
            fontSize: 24, fontWeight: 700,
            lineHeight: 1.28, letterSpacing: '0.005em',
            color: ink, textWrap: 'balance',
          }}>{card.front && card.front.title}</h2>

          {/* lede 预览(纯文本,不嵌套 parseRichText 避免 popup-in-popup) */}
          {card.back && card.back.lede && (
            <p style={{
              margin: '20px 0 0',
              fontFamily: "'Noto Serif SC', 'Source Han Serif SC', Georgia, serif",
              fontSize: 14, lineHeight: 1.85, color: ink,
              whiteSpace: 'pre-wrap',
            }}>{card.back.lede}</p>
          )}

          {/* 跳转按钮 */}
          <a
            href={jumpUrl}
            style={{
              marginTop: 'auto',
              alignSelf: 'flex-start',
              textDecoration: 'none',
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 11, letterSpacing: '0.18em',
              color: ink70,
              border: `1px solid ${ink40}`,
              padding: '8px 14px',
              borderRadius: 4,
            }}
          >打开这张卡 →</a>

          {/* 底部 card_id 小字 */}
          <div style={{
            marginTop: 12,
            display: 'flex', alignItems: 'center', gap: 8,
          }}>
            <span style={{ width: 24, height: 1, background: ink40 }} />
            <span style={{
              fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
              fontSize: 9, letterSpacing: '0.18em', color: ink55,
            }}>{card.card_id}</span>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}

function Section({ label, children, inkSoft }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      <div style={{
        fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
        fontSize: 9, letterSpacing: '0.22em',
        color: inkSoft || 'rgba(60,40,20,0.5)',
        textTransform: 'uppercase',
      }}>
        · {label} ·
      </div>
      {children}
    </div>
  );
}

// 卡片栈：左半点击 → 下一张；右半点击 → 上一张
function CardStack() {
  // URL 参数:?favorites=1 收藏夹 / ?stage=S1 段过滤 / ?card=C-S1-001 直跳指定卡(分享/术语跳转用)
  const params = new URLSearchParams(location.search);
  const favoritesMode = params.get('favorites') === '1';
  const stageFilter = params.get('stage') || '';   // 'S0'..'S8' 或空
  const directCardId = params.get('card') || '';   // 'C-S1-001' 等

  // 异步加载全部卡片(从 cards.json,见文件顶部 useCards hook)
  const { data: cardsData, error: cardsError } = useCards();
  // 异步加载术语字典(用 byId 加速 lookup)
  const glossaryData = useGlossary();
  const glossaryById = glossaryData ? glossaryData.byId : null;
  // 术语 popup 状态:被点击词的 anchor + 选中的术语
  const [popup, setPopup] = React.useState(null); // { glossary, anchorRect } | null
  // 卡片引用 popup 状态:点击正文里的 C-Sx-NNN 触发
  const [cardPopup, setCardPopup] = React.useState(null); // { card, anchorRect } | null
  const stageRef = React.useRef(null);
  const onTermClick = React.useCallback((g, anchorEl) => {
    if (!g || !anchorEl) return;
    setCardPopup(null);  // 互斥:打开术语 popup 时关掉卡片 popup
    setPopup({ glossary: g, anchorRect: anchorEl.getBoundingClientRect() });
  }, []);
  const onCardClick = React.useCallback((c, anchorEl) => {
    if (!c || !anchorEl) return;
    setPopup(null);  // 互斥:打开卡片 popup 时关掉术语 popup
    setCardPopup({ card: c, anchorRect: anchorEl.getBoundingClientRect() });
  }, []);
  const closePopup = React.useCallback(() => setPopup(null), []);
  const closeCardPopup = React.useCallback(() => setCardPopup(null), []);

  // ── 远端数据(收藏 + 进度)── 由 server / Cloudflare KV 持久化,跨设备同步
  const email = (window.PKB && PKB.auth.currentUser()) || null;
  const [favList, setFavList] = React.useState([]);
  const [progress, setProgress] = React.useState({});
  const [remoteLoaded, setRemoteLoaded] = React.useState(false);
  const favSaveChainRef = React.useRef(Promise.resolve());
  const progressSaveChainRef = React.useRef(Promise.resolve());

  // 一次性加载收藏 + 进度
  React.useEffect(() => {
    if (!email) { setRemoteLoaded(true); return; }
    const localFavs = PKB.auth.readJSON('favorites', []);
    const localProgress = PKB.auth.readJSON('progress', {});
    Promise.all([
      PKB.api.getFavorites(email).then((j) => ({ ok: true, ...j })).catch(() => ({ ok: false })),
      PKB.api.getProgress(email).then((j) => ({ ok: true, ...j })).catch(() => ({ ok: false })),
    ]).then(([f, p]) => {
      const nextFavs = f.ok && Array.isArray(f.favorites) ? f.favorites : localFavs;
      const nextProgress = p.ok && p.progress && typeof p.progress === 'object' && !Array.isArray(p.progress) ? p.progress : localProgress;
      setFavList(nextFavs);
      setProgress(nextProgress);
      PKB.auth.writeJSON('favorites', nextFavs);
      PKB.auth.writeJSON('progress', nextProgress);
      setRemoteLoaded(true);
    });
  }, [email]);

  // toggleFavorite — 乐观更新 + 本地落盘 + 远端排队保存
  const toggleFavorite = React.useCallback((cardId) => {
    if (!email) return;
    setFavList((prev) => {
      const next = prev.slice();
      const at = next.indexOf(cardId);
      if (at >= 0) next.splice(at, 1);     // 取消
      else next.push(cardId);               // 新加 → 末尾
      PKB.auth.writeJSON('favorites', next);
      favSaveChainRef.current = favSaveChainRef.current
        .catch(() => {})
        .then(() => PKB.api.putFavorites(email, next));
      favSaveChainRef.current.catch(() => {});
      return next;
    });
  }, [email]);

  // 实际渲染的卡片集合(按 favorites / stage 过滤,no 段内重编号)
  // - favorites 模式: 按 favList 顺序展示(新加的在末尾)
  // - stage 模式: 按 cards.json 原顺序
  const visibleCards = React.useMemo(() => {
    if (!cardsData) return [];
    if (favoritesMode) {
      const byId = {};
      cardsData.cards.forEach((c) => { byId[c.card_id] = c; });
      const ordered = favList.map((id) => byId[id]).filter(Boolean);
      return ordered.map((c, i) => ({ ...c, no: i + 1 }));
    }
    let cards = cardsData.cards;
    if (stageFilter) {
      cards = cards.filter((c) => c.stage === stageFilter);
    }
    return cards.map((c, i) => ({ ...c, no: i + 1 }));
  }, [cardsData, favoritesMode, stageFilter, favList]);

  // 进度 scope: 收藏模式用 'favorites',否则 'stage:S1'
  const progressScope = favoritesMode ? 'favorites' : (stageFilter ? `stage:${stageFilter}` : null);
  const [idx, setIdx] = React.useState(0);

  // remoteLoaded 后:有 ?card= 优先跳;否则从进度恢复 idx
  const initJumpedRef = React.useRef(false);
  React.useEffect(() => {
    if (!remoteLoaded || !visibleCards.length || initJumpedRef.current) return;
    if (directCardId) {
      const i = visibleCards.findIndex((c) => c.card_id === directCardId);
      if (i >= 0) { setIdx(i); initJumpedRef.current = true; return; }
    }
    if (progressScope) {
      const saved = progress[progressScope];
      if (typeof saved === 'number' && saved > 0 && saved < visibleCards.length) {
        setIdx(saved);
      }
    }
    initJumpedRef.current = true;
  }, [remoteLoaded, visibleCards.length, directCardId, progressScope, progress]);

  // 越界 clamp(收藏被取消等)
  React.useEffect(() => {
    if (!visibleCards.length) return;
    if (idx >= visibleCards.length) setIdx(visibleCards.length - 1);
    else if (idx < 0) setIdx(0);
  }, [visibleCards.length, idx]);

  // 进度持久化 — debounce 800ms 防翻卡时频繁写
  React.useEffect(() => {
    if (!remoteLoaded || !email || !progressScope || !visibleCards.length) return;
    const saved = progress[progressScope] || 0;
    if (idx <= saved) return;     // 进度只升不降
    const t = setTimeout(() => {
      const next = { ...progress, [progressScope]: idx };
      setProgress(next);
      PKB.auth.writeJSON('progress', next);
      progressSaveChainRef.current = progressSaveChainRef.current
        .catch(() => {})
        .then(() => PKB.api.putProgress(email, next));
      progressSaveChainRef.current.catch(() => {});
    }, 800);
    return () => clearTimeout(t);
  }, [idx, remoteLoaded, email, progressScope, progress, visibleCards.length]);

  // 重置当前 scope 的进度 — Cards 页右上角 ↻ 调用
  const resetProgress = React.useCallback(() => {
    if (!email || !progressScope) return;
    const next = { ...progress };
    delete next[progressScope];
    setProgress(next);
    setIdx(0);
    PKB.auth.writeJSON('progress', next);
    progressSaveChainRef.current = progressSaveChainRef.current
      .catch(() => {})
      .then(() => PKB.api.putProgress(email, next));
    progressSaveChainRef.current.catch(() => {});
  }, [email, progressScope, progress]);

  // cardsById:GlossaryPopup 用来查 related_cards 的 stage + title
  const cardsById = React.useMemo(() => {
    if (!cardsData) return null;
    const m = {};
    for (const c of cardsData.cards) m[c.card_id] = c;
    return m;
  }, [cardsData]);
  // 切换 popup 内的术语(点 related_glossary 触发)
  const onSwitchGlossary = React.useCallback((g) => {
    if (!g) return;
    setPopup((prev) => prev ? { ...prev, glossary: g } : prev);
  }, []);

  const [anim, setAnim] = React.useState(null); // {dir: 'next'|'prev', from: 0, to: 1}
  // 触摸滑动:startRef 记录触摸起点
  const startRef = React.useRef(null);
  const total = visibleCards.length;

  // 段名:从 cardsData.stages 查 / favorites 显示"收藏夹" / 兜底"全部卡片"
  const stageMeta = cardsData && cardsData.stages.find((s) => s.id === stageFilter);
  const stageName = favoritesMode ? '收藏夹' : (stageMeta ? stageMeta.name : '全部卡片');
  const stageLabel = favoritesMode ? `${total} 张` : (stageMeta ? stageMeta.id : `${total} 张`);

  // 加载 / 错误状态(放最前,避免后面用到 cardsData 时 null)
  if (cardsError) {
    return (
      <div style={{ padding: 40, textAlign: 'center', color: '#5a2a20', fontFamily: "'Noto Serif SC', serif" }}>
        <div style={{ fontSize: 18, fontWeight: 600, marginBottom: 12 }}>载入失败</div>
        <div style={{ fontSize: 13, lineHeight: 1.7, color: 'rgba(40,30,20,0.6)' }}>
          {String(cardsError.message)}<br />
          <small>请确认 cards.json 已生成 — 在 50-frontend/ 目录跑 <code>python3 build_cards_json.py</code></small>
        </div>
      </div>
    );
  }
  if (!cardsData) {
    return (
      <div style={{ padding: 40, textAlign: 'center', color: 'rgba(40,30,20,0.5)', fontFamily: "'Noto Serif SC', serif", fontSize: 14 }}>
        载入中…
      </div>
    );
  }

  // 空收藏夹
  if (favoritesMode && total === 0) {
    return (
      <div style={{
        minHeight: '100vh',
        background: 'transparent',
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
        padding: 32, textAlign: 'center', gap: 16,
      }}>
        <div style={{
          fontFamily: "'Noto Serif SC', serif",
          fontSize: 22, fontWeight: 600, color: '#3b2a18',
        }}>收藏夹是空的</div>
        <div style={{
          fontFamily: "'Noto Serif SC', serif",
          fontSize: 14, lineHeight: 1.7, color: 'rgba(40,30,20,0.6)',
          maxWidth: 280,
        }}>
          打开任何一张知识卡片，点击左上角"收藏"按钮，卡片会出现在这里。
        </div>
        <a href="Stage Folders.html" style={{
          marginTop: 24,
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 11, letterSpacing: '0.18em',
          color: 'rgba(40,30,20,0.7)',
          textDecoration: 'none',
          padding: '10px 16px',
          border: '1px solid rgba(40,30,20,0.25)',
          borderRadius: 4,
        }}>← 返回阶段</a>
      </div>
    );
  }

  const missingDirectCard = !!directCardId && !cardsData.cards.some((c) => c.card_id === directCardId);
  if (missingDirectCard || (!favoritesMode && total === 0)) {
    return (
      <div style={{
        minHeight: '100vh',
        background: 'transparent',
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
        padding: 32, textAlign: 'center', gap: 16,
      }}>
        <div style={{
          fontFamily: "'Noto Serif SC', serif",
          fontSize: 22, fontWeight: 600, color: '#3b2a18',
        }}>{missingDirectCard ? '没有找到这张卡片' : '这个阶段没有卡片'}</div>
        <a href="Stage Folders.html" style={{
          marginTop: 24,
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 11, letterSpacing: '0.18em',
          color: 'rgba(40,30,20,0.7)',
          textDecoration: 'none',
          padding: '10px 16px',
          border: '1px solid rgba(40,30,20,0.25)',
          borderRadius: 4,
        }}>← 返回阶段</a>
      </div>
    );
  }

  const go = (dir) => {
    if (anim) return;
    if (dir === 'next' && idx >= total - 1) return;
    if (dir === 'prev' && idx <= 0) return;
    const to = dir === 'next' ? idx + 1 : idx - 1;
    setAnim({ dir, from: idx, to });
    setTimeout(() => {
      setIdx(to);
      setAnim(null);
    }, 460);
  };

  // 触摸 handlers — 横滑翻页,纵滑让卡内 overflow:auto 自然滚动
  // 阈值 50px 且横向位移 > 纵向位移才视为翻页手势
  const onTouchStart = (e) => {
    const t = e.touches && e.touches[0];
    if (!t) return;
    startRef.current = { x: t.clientX, y: t.clientY };
  };
  const onTouchEnd = (e) => {
    const start = startRef.current;
    startRef.current = null;
    if (!start) return;
    const t = (e.changedTouches && e.changedTouches[0]) || (e.touches && e.touches[0]);
    if (!t) return;
    const dx = t.clientX - start.x;
    const dy = t.clientY - start.y;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) {
      // 横滑判定成立:左滑(dx<0)→下一张;右滑(dx>0)→上一张
      if (dx < 0) go('next'); else go('prev');
    }
  };

  // 计算每张卡的 transform
  // - 当前卡：居中
  // - 下一张：在右侧待命（next 动画时从右滑入；prev 动画时不变）
  // - 上一张：在左侧待命（prev 动画时从左滑入；next 动画时不变）
  const transformFor = (cardIdx) => {
    const W = '100%';
    if (!anim) {
      if (cardIdx < idx) return 'translateX(-110%)';
      if (cardIdx > idx) return 'translateX(110%)';
      return 'translateX(0)';
    }
    // 动画中
    const { dir, from, to } = anim;
    if (dir === 'next') {
      // from 从中心 → 左外；to 从右外 → 中心
      if (cardIdx === from) return 'translateX(-110%) rotate(-3deg)';
      if (cardIdx === to)   return 'translateX(0)';
      if (cardIdx < from)   return 'translateX(-110%)';
      return 'translateX(110%)';
    } else {
      // prev: from 中心 → 右外；to 左外 → 中心（倒放）
      if (cardIdx === from) return 'translateX(110%) rotate(3deg)';
      if (cardIdx === to)   return 'translateX(0)';
      if (cardIdx < from)   return 'translateX(-110%)';
      return 'translateX(110%)';
    }
  };

  return (
    <div style={{
      height: '100%',                // #root 已固定 100vh,这里 100% 跟随
      background: 'transparent',
      paddingTop: 16,
      paddingBottom: 16,
      display: 'flex',
      flexDirection: 'column',
      overflow: 'hidden',             // 防内容溢出页面
    }}>
      {/* 顶部小 header */}
      <div style={{
        padding: '20px 24px 16px',
        display: 'flex',
        alignItems: 'baseline',
        justifyContent: 'space-between',
      }}>
        <a href="Stage Folders.html" style={{
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 11, letterSpacing: '0.16em',
          color: 'rgba(40,30,20,0.55)',
          textDecoration: 'none',
        }}>← 返回</a>
        <div style={{
          fontFamily: "'Noto Serif SC', serif",
          fontSize: 13, fontWeight: 600, color: 'rgba(40,30,20,0.7)',
          letterSpacing: '0.04em',
        }}>
          {stageName} <span style={{ opacity: 0.5, marginLeft: 6, fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace", fontSize: 10 }}>{stageLabel}</span>
        </div>
        <div style={{
          display: 'flex', alignItems: 'baseline', gap: 8,
          fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace",
          fontSize: 11, letterSpacing: '0.16em',
          color: 'rgba(40,30,20,0.55)',
        }}>
          <span>{idx + 1} / {total}</span>
          {/* 重置进度 ↻ — 把当前 scope(stage:Sx 或 favorites)的进度清零并跳回第 1 张
              fav 模式下也允许(只是清进度,不动收藏 list 顺序)*/}
          {progressScope && email && (
            <button
              onClick={(e) => { e.stopPropagation(); resetProgress(); }}
              title="重置本段进度"
              style={{
                all: 'unset', cursor: 'pointer',
                fontSize: 13, lineHeight: 1,
                color: 'rgba(122,42,42,0.7)',
              }}
            >↻</button>
          )}
        </div>
      </div>

      {/* 卡片舞台 */}
      <div
        ref={stageRef}
        onTouchStart={onTouchStart}
        onTouchEnd={onTouchEnd}
        onTouchCancel={onTouchEnd}
        style={{
          flex: 1,
          margin: '8px auto',
          width: 'calc(100% - 40px)',
          maxWidth: 380,
          position: 'relative',
          minHeight: 0,                  // 关键: flex:1 子才能严格按可用空间收缩
        }}
      >
        {visibleCards.map((c, i) => {
          // 只渲染当前 + 邻接 1 张,避免 1437 卡同进 DOM
          const inWindow = Math.abs(i - idx) <= 1 || (anim && (i === anim.from || i === anim.to));
          if (!inWindow) return null;
          return (
            <div key={c.card_id} style={{
              position: 'absolute',
              inset: 0,
              transform: transformFor(i),
              transition: anim ? 'transform 460ms cubic-bezier(.2,.8,.2,1)' : 'none',
              willChange: 'transform',
            }}>
              <Card data={c} total={total} color={CARD_COLORS[i % CARD_COLORS.length]}
                    glossaryById={glossaryById} cardsById={cardsById}
                    onTermClick={onTermClick} onCardClick={onCardClick}
                    isFavorited={favList.indexOf(c.card_id) >= 0}
                    onToggleFavorite={toggleFavorite} />
            </div>
          );
        })}
      </div>

      {/* 术语弹窗 — popup 是顶层,fixed 定位,backdrop 点击关闭 */}
      {popup && stageRef.current && (
        <GlossaryPopup
          glossary={popup.glossary}
          anchorRect={popup.anchorRect}
          stageRect={stageRef.current.getBoundingClientRect()}
          onClose={closePopup}
          cardsById={cardsById}
          glossaryById={glossaryById}
          onSwitchGlossary={onSwitchGlossary}
        />
      )}

      {/* 卡片引用弹窗 — 点击正文 C-Sx-NNN 触发 */}
      {cardPopup && stageRef.current && (
        <CardRefPopup
          card={cardPopup.card}
          anchorRect={cardPopup.anchorRect}
          stageRect={stageRef.current.getBoundingClientRect()}
          onClose={closeCardPopup}
        />
      )}

    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<CardStack />);
