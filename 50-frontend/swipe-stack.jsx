// swipe-stack.jsx — 可复用的"垂直拖拽展开堆叠"交互
//
// 用法：
//   <SwipeStack
//     items={[...]}                  // 任意数组
//     itemHeight={62}                // 折叠态每层露出的高度（必填）
//     expandedHeight={308}           // 展开态占用的纵向高度（含让位空间）
//     renderItem={({ item, idx, expanded, isExpanded }) => <YourCard ... />}
//     onEnter={(item, idx) => ...}   // 展开后再次右滑（或调用）触发"进入"
//     enableHorizontalEnter={true}   // 是否启用展开后水平右滑进入
//   />
//
// 行为：
// - 折叠态：按住任意一项向上拖 → 该项跟手上移，其它项同步下移让位
// - 拖到 35% 距离 OR 一次快速 flick（>0.5 px/ms）→ 吸附展开
// - 否则松手复位
// - 展开态：向下拖 → 收起；水平右滑 + 距离 > 80px → 触发 onEnter
//
// renderItem 收到的 props：
//   item, idx, expanded (number|null), isExpanded, flying, dragX
// 你只负责画卡片本身；位置 / 拖拽 / 让位由本组件接管。

(function (global) {
  const React = global.React;

  function SwipeStackItem({
    item, idx, total,
    itemHeight, expandedHeight,
    expanded, pendingExpand, dragProgress,
    onDragStart, onDragMove, onDragEnd,
    onEnter, enableHorizontalEnter,
    renderItem,
  }) {
    const yFor = React.useCallback((expandedIdx) => {
      if (expandedIdx == null) return idx * itemHeight;
      if (expandedIdx === idx) return 0;
      const slot = idx < expandedIdx ? idx : idx - 1;
      return expandedHeight + slot * itemHeight;
    }, [idx, itemHeight, expandedHeight]);

    const yFromExpanded = expanded != null ? yFor(expanded) : yFor(null);
    const isPending = pendingExpand === idx;
    const isExpanded = expanded === idx;

    // 拖动中:从当前位置(yFromExpanded)插值到目标位置(yTarget)
    // - 展开拖动(折叠态拉起): yTarget 是各 folder 在 expanded=pendingExpand 状态下的位置
    // - 收起拖动(展开态拉下): 整个 stack 都要回到默认堆叠位 yFor(null) = idx*itemHeight
    //   ↑ 没这层判断的话, 被拖的 folder yTarget 永远是 0, 视觉上不跟手, 松手时看起来"瞬间复位"
    const isCollapsing = pendingExpand != null && expanded === pendingExpand;
    let y;
    if (pendingExpand != null) {
      let yTarget;
      if (isCollapsing) {
        yTarget = idx * itemHeight;          // 收起目标 = 默认堆叠位
      } else if (pendingExpand === idx) {
        yTarget = 0;                          // 自己被展开 → 顶部
      } else {
        yTarget = yFor(pendingExpand);        // 其他 folder 让位
      }
      const p = Math.max(0, Math.min(1, dragProgress));
      y = yFromExpanded + (yTarget - yFromExpanded) * p;
    } else if (expanded != null) {
      y = yFor(expanded);
    } else {
      y = yFor(null);
    }

    // ── 手势
    const [dragX, setDragX] = React.useState(0);
    const [flying, setFlying] = React.useState(false);
    const startRef = React.useRef(null);
    const movedRef = React.useRef(false);
    const verticalRef = React.useRef(false);
    const lastRef = React.useRef(null);
    // dragX/flying/isExpanded 在 window mouseup listener 闭包里都是 stale,
    // 因此用 ref 让 endDrag 读最新值
    const dragXRef = React.useRef(0);
    const flyingRef = React.useRef(false);
    const isExpandedRef = React.useRef(false);
    isExpandedRef.current = expanded === idx;
    flyingRef.current = flying;

    const flyOutAndEnter = React.useCallback(() => {
      if (flyingRef.current) return;
      flyingRef.current = true;
      setFlying(true);
      setTimeout(() => {
        onEnter && onEnter(item, idx);
      }, 620);
    }, [onEnter, item, idx]);

    const beginDrag = (px, py) => {
      startRef.current = { x: px, y: py, t: Date.now() };
      lastRef.current = { x: px, y: py, t: Date.now(), vy: 0 };
      movedRef.current = false;
      verticalRef.current = false;
      onDragStart && onDragStart(idx);
    };
    const moveDrag = (px, py, ev) => {
      if (!startRef.current) return;
      const dx = px - startRef.current.x;
      const dy = py - startRef.current.y;
      if (!movedRef.current && (Math.abs(dx) > 4 || Math.abs(dy) > 4)) {
        movedRef.current = true;
        verticalRef.current = Math.abs(dy) > Math.abs(dx);
      }
      const now = Date.now();
      const dt = Math.max(1, now - lastRef.current.t);
      lastRef.current.vy = (py - lastRef.current.y) / dt;
      lastRef.current.x = px; lastRef.current.y = py; lastRef.current.t = now;

      if (enableHorizontalEnter && isExpandedRef.current && Math.abs(dx) > Math.abs(dy) && dx > 0) {
        ev?.preventDefault?.();
        const v = Math.max(0, dx);
        dragXRef.current = v;
        setDragX(v);
      } else {
        if (verticalRef.current) ev?.preventDefault?.();
        const signedUp = isExpandedRef.current ? dy : -dy;
        onDragMove && onDragMove(idx, Math.max(0, signedUp));
      }
    };
    const endDrag = () => {
      if (!startRef.current) return;
      const moved = movedRef.current;
      const vy = lastRef.current ? lastRef.current.vy : 0;
      if (enableHorizontalEnter && isExpandedRef.current && dragXRef.current > 0) {
        const dx = dragXRef.current;
        startRef.current = null;
        if (dx > 80) flyOutAndEnter();
        else { dragXRef.current = 0; setDragX(0); }
      } else {
        startRef.current = null;
        onDragEnd && onDragEnd(idx, moved, vy);
      }
    };

    const onTouchStart = (e) => { const t = e.touches[0]; beginDrag(t.clientX, t.clientY); };
    const onTouchMove = (e) => { const t = e.touches[0]; moveDrag(t.clientX, t.clientY, e); };
    const onTouchEnd = () => endDrag();
    const onMouseDown = (e) => {
      if (e.button !== 0) return;
      beginDrag(e.clientX, e.clientY);
      const mm = (ev) => moveDrag(ev.clientX, ev.clientY, ev);
      const mu = () => {
        window.removeEventListener('mousemove', mm);
        window.removeEventListener('mouseup', mu);
        endDrag();
      };
      window.addEventListener('mousemove', mm);
      window.addEventListener('mouseup', mu);
    };

    // ── 输出 transform
    let finalTransform;
    let opacity = 1;
    if (flying) {
      const flyX = (typeof window !== 'undefined' ? window.innerWidth : 420) + 400;
      finalTransform = `translateY(${y - 220}px) translateX(${flyX}px) rotate(18deg) scale(0.92)`;
      opacity = 0;
    } else if (isExpanded && dragX) {
      const lift = Math.min(dragX * 0.35, 80);
      const rot  = Math.min(dragX * 0.04, 8);
      finalTransform = `translateY(${y - lift}px) translateX(${dragX}px) rotate(${rot}deg)`;
    } else {
      finalTransform = `translateY(${y}px)`;
    }
    const transition = flying
      ? 'transform 620ms cubic-bezier(.5,.05,.7,.2), opacity 620ms ease-in'
      : (startRef.current || pendingExpand != null)
        ? 'transform 0ms'
        : 'transform 460ms cubic-bezier(.2,.8,.2,1)';

    return (
      <div
        className="swipe-stack-item"
        onMouseDown={onMouseDown}
        onTouchStart={onTouchStart}
        onTouchMove={onTouchMove}
        onTouchEnd={onTouchEnd}
        onTouchCancel={onTouchEnd}
        style={{
          position: 'absolute',
          top: 0, left: 0, right: 0,
          transform: finalTransform,
          transition,
          opacity,
          zIndex: 100 + idx,
          // touch-action: none 让 JS 完全接管手势,否则 iOS Safari/Chrome 会
          // 把纵向 pan 据为己有(尤其展开态),导致收起拖动时 JS 收不到 touchmove,
          // 看起来是"不跟手"。页面本身 overflow:hidden 不需要原生 scroll。
          touchAction: 'none',
          cursor: 'grab',
        }}
      >
        {renderItem({ item, idx, total, expanded, isExpanded, flying, dragX, flyOutAndEnter })}
      </div>
    );
  }

  function SwipeStack({
    items,
    itemHeight = 62,
    expandedHeight = 308,
    renderItem,
    onEnter,
    enableHorizontalEnter = false,
    snapDistance = 0.35,    // 拖到这个比例就吸附
    snapVelocity = 0.5,     // 或速度 > 这个 (px/ms) 也吸附
    style,
  }) {
    const [expanded, setExpanded] = React.useState(null);
    const [pendingExpand, setPendingExpand] = React.useState(null);
    const [dragProgress, setDragProgress] = React.useState(0);
    // window 上的 mousemove/mouseup listener 是 mousedown 时绑定的,
    // closure 捕获的是当时的 React state(stale)。用 ref 让 handleDragEnd
    // 读最新 dragProgress / expanded,避免 fast/snap 判定吃 0。
    const dragProgressRef = React.useRef(0);
    const expandedRef = React.useRef(null);
    expandedRef.current = expanded;

    const handleDragStart = (i) => {
      setPendingExpand(i);
      dragProgressRef.current = 0;
      setDragProgress(0);
    };
    const handleDragMove = (i, upPx) => {
      if (pendingExpand !== i) setPendingExpand(i);
      const exp = expandedRef.current;
      let startY;
      if (exp == null) {
        startY = i * itemHeight;
      } else if (exp === i) {
        startY = i * itemHeight;
      } else {
        const slot = i < exp ? i : i - 1;
        startY = expandedHeight + slot * itemHeight;
      }
      const distance = Math.max(40, startY);
      const p = Math.max(0, Math.min(1.05, upPx / distance));
      dragProgressRef.current = p;
      setDragProgress(p);
    };
    const handleDragEnd = (i, moved, vy) => {
      if (!moved) {
        setPendingExpand(null);
        dragProgressRef.current = 0;
        setDragProgress(0);
        return;
      }
      const exp = expandedRef.current;
      const directional = exp === i ? vy : -vy;
      const fast = directional > snapVelocity;
      const farEnough = dragProgressRef.current >= snapDistance;
      if (farEnough || fast) {
        setExpanded(exp === i ? null : i);
      }
      setPendingExpand(null);
      dragProgressRef.current = 0;
      setDragProgress(0);
    };

    return (
      <div className="swipe-stack" style={{
        position: 'relative',
        height: items.length * itemHeight + expandedHeight,
        ...style,
      }}>
        {items.map((item, i) => (
          <SwipeStackItem
            key={item.id ?? i}
            item={item}
            idx={i}
            total={items.length}
            itemHeight={itemHeight}
            expandedHeight={expandedHeight}
            expanded={expanded}
            pendingExpand={pendingExpand}
            dragProgress={dragProgress}
            onDragStart={handleDragStart}
            onDragMove={handleDragMove}
            onDragEnd={handleDragEnd}
            onEnter={onEnter}
            enableHorizontalEnter={enableHorizontalEnter}
            renderItem={renderItem}
          />
        ))}
      </div>
    );
  }

  global.SwipeStack = SwipeStack;
})(window);
