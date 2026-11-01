// Reader collapse and block zoom, loaded after page load.
(() => {
  if (window.logseqGardenerInitOutline) { window.logseqGardenerInitOutline(); return; }
  const ZOOM = '#zoom/';
  const lists = (li) => li.querySelectorAll(':scope>ul,:scope>details>ul');
  const kids = (li) => [...lists(li)].flatMap((ul) => [...ul.children]);
  const roots = (box) => [...box.querySelectorAll(':scope>ul.outline>li')];
  // null at the top level; undefined outside the source outline.
  function parentItem(li) {
    const ul = li.parentElement;
    if (ul?.tagName !== 'UL') return undefined;
    if (ul.classList.contains('outline')) return null;
    let up = ul.parentElement;
    if (up?.tagName === 'DETAILS') up = up.parentElement;
    return up?.tagName === 'LI' && up.closest('.outline') ? up : undefined;
  }
  // The SDK's BlockId: the id:: UUID when the block has an anchor, otherwise its path.
  function blockId(li) {
    const anchor = li.querySelector(':scope>span[id^="block-"]');
    if (anchor) return anchor.id.slice(6);
    const path = [];
    for (let item = li, up; item; item = up) {
      up = parentItem(item);
      if (up === undefined) return null;
      const siblings = up ? kids(up) : roots(item.parentElement.parentElement);
      path.unshift(siblings.indexOf(item) + 1);
    }
    return path.join('.');
  }
  function find(box, id) {
    if (!/^\d+(\.\d+)*$/.test(id)) return document.getElementById('block-' + id.toLowerCase())?.closest('li');
    let items = roots(box), item = null;
    for (const n of id.split('.')) {
      item = items[Number(n) - 1];
      if (!item) return null;
      items = kids(item);
    }
    return item;
  }
  function toggle(li) {
    const details = li.querySelector(':scope>details');
    if (details) details.open = !details.open;
    else li.classList.toggle('folded');
    arrowState(li);
  }
  const closed = (li) => li.classList.contains('folded') || li.querySelector(':scope>details')?.open === false;

  const arrows = new WeakMap();
  const arrowState = (li) => arrows.get(li)?.setAttribute('aria-expanded', String(!closed(li)));
  function controls(root) {
    const items = [...(root.matches?.('.outline li') ? [root] : []), ...root.querySelectorAll('.outline li')];
    for (const li of items) {
      if (!kids(li).length || !li.querySelector(':scope>.bullet,:scope>details>summary>.bullet')) continue;
      if (!arrows.has(li)) {
        const arrow = document.createElement('button');
        arrow.type = 'button';
        arrow.className = 'lsg-arrow';
        arrow.setAttribute('aria-label', 'Toggle children');
        arrow.innerHTML = '<svg viewBox="0 0 16 16" width="20" height="20" aria-hidden="true"><path d="M4 6l4 4 4-4z" fill="currentColor"/></svg>';
        arrows.set(li, arrow);
        li.prepend(arrow);
      }
      arrowState(li);
    }
  }

  let zoomed = null;
  function unzoom() {
    if (!zoomed) return;
    const { li, mark, view, main, states } = zoomed;
    zoomed = null;
    if (mark.isConnected) mark.replaceWith(li);
    view.remove();
    main.removeAttribute('data-lsg-zoomed');
    for (const [node, open, folded] of states) {
      if (node.tagName === 'DETAILS') node.open = open;
      else node.classList.toggle('folded', folded);
      arrowState(node.tagName === 'DETAILS' ? node.parentElement : node);
    }
  }
  function label(li) {
    const row = li.querySelector(':scope>details>summary') || li;
    const copy = row.cloneNode(true);
    copy.querySelectorAll('ul,details,.bullet,.lsg-arrow,.task-checkbox').forEach((node) => node.remove());
    const text = copy.textContent.replace(/\s+/g, ' ').trim();
    return text.length > 80 ? text.slice(0, 79) + '…' : text;
  }
  function zoom(id) {
    if (zoomed?.id === id && zoomed.view.isConnected) return;
    unzoom();
    const main = document.querySelector('main');
    const box = main?.querySelector('ul.outline')?.parentElement;
    const li = box && find(box, id);
    if (!li || blockId(li) === null) return;
    const ancestors = [];
    for (let up = parentItem(li); up; up = parentItem(up)) ancestors.push(up);
    const crumb = document.createElement('nav');
    crumb.className = 'lsg-breadcrumb';
    crumb.setAttribute('aria-label', 'Block parents');
    const page = document.createElement('a');
    page.href = location.pathname.split('/').pop() || './';
    page.textContent = main.querySelector(':scope>h1')?.textContent || 'Page';
    crumb.append(page);
    const sep = (text) => { const span = document.createElement('span'); span.textContent = text; crumb.append(span); };
    if (ancestors.length > 3) { sep('›'); crumb.append('⋯'); }
    for (const up of ancestors.slice(0, 3).reverse()) {
      sep('›');
      const link = document.createElement('a');
      link.href = ZOOM + blockId(up);
      link.textContent = label(up);
      crumb.append(link);
    }
    const states = [li, ...li.querySelectorAll('li')].flatMap((item) => {
      const details = item.querySelector(':scope>details');
      return details ? [[details, details.open, false]] : [[item, false, item.classList.contains('folded')]];
    });
    for (const [node] of states) {
      if (node.tagName === 'DETAILS') node.open = true;
      else node.classList.remove('folded');
      arrowState(node.tagName === 'DETAILS' ? node.parentElement : node);
    }
    const mark = document.createComment('lsg-zoom');
    li.replaceWith(mark);
    const view = document.createElement('div');
    view.className = 'lsg-zoom';
    const ul = document.createElement('ul');
    ul.className = 'outline';
    ul.append(li);
    view.append(crumb, ul);
    main.prepend(view);
    main.setAttribute('data-lsg-zoomed', '');
    zoomed = { id, li, mark, view, main, states };
    window.scrollTo(0, 0);
  }
  function route() {
    let id = null;
    try { if (location.hash.startsWith(ZOOM)) id = decodeURIComponent(location.hash.slice(ZOOM.length)); }
    catch { id = null; }
    if (id) zoom(id); else unzoom();
  }

  document.addEventListener('click', (event) => {
    const arrow = event.target.closest?.('.lsg-arrow');
    if (arrow && arrows.get(arrow.parentElement) === arrow) {
      event.preventDefault();
      toggle(arrow.parentElement);
      return;
    }
    const bullet = event.target.closest?.('.outline .bullet');
    if (bullet) {
      event.preventDefault();
      const li = bullet.closest('li');
      const article = li.closest('.lsg-journal');
      // Restore the page first so the block's position is counted where it belongs.
      if (zoomed?.view.contains(li)) unzoom();
      const id = blockId(li);
      if (id === null) return;
      const page = article?.querySelector('.journal-title')?.getAttribute('href');
      if (page) location.href = page + ZOOM + id;
      else if (location.hash === ZOOM + id) route();
      else location.hash = ZOOM.slice(1) + id;
      return;
    }
    // The strip over a child list's guide line toggles the block that owns the list.
    const ul = event.target;
    if (ul.tagName === 'UL' && ul.closest('.outline') && !ul.classList.contains('outline') && event.offsetX < 6) {
      const li = ul.parentElement.tagName === 'DETAILS' ? ul.parentElement.parentElement : ul.parentElement;
      if (li.tagName === 'LI') toggle(li);
    }
  });
  document.addEventListener('toggle', event => {
    if (event.target.tagName === 'DETAILS') arrowState(event.target.parentElement);
  }, true);
  window.logseqGardenerInitOutline = (root = document) => { controls(root); route(); };
  window.addEventListener('hashchange', route);
  window.logseqGardenerInitOutline();
  new MutationObserver(records => {
    for (const record of records) {
      if (record.type === 'attributes') arrowState(record.target);
      else if ([...record.addedNodes].some(node => node.nodeType === 1 && !node.classList.contains('lsg-arrow'))) controls(record.target);
    }
  }).observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
})();
