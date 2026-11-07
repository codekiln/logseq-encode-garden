(() => {
if (window.logseqGardenerSidebar) return;
const KEY = 'logseq-gardener-right-sidebar';
const ZOOM = '#zoom/';
const SOURCE = 'source-block-';
const root = document.documentElement;
const base = new URL('.', document.currentScript?.src || location.href);
const toggle = () => document.querySelector('[data-lsg-right-toggle]');
const el = (tag, attrs = {}, ...children) => {
const node = document.createElement(tag);
for (const [name, value] of Object.entries(attrs)) node.setAttribute(name, value);
node.append(...children);
return node;
};
const PATHS = {
page: 'M14 3v4a1 1 0 0 0 1 1h4M17 21h-10a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2z',
block: 'M12 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0 -6 0',
refs: 'M9 6l11 0M9 12l11 0M9 18l11 0M5 6l0 .01M5 12l0 .01M5 18l0 .01',
contents: 'M9 6l11 0M9 12l11 0M9 18l11 0M5 6l0 .01M5 12l0 .01M5 18l0 .01',
graph: 'M10 5a2 2 0 1 0 4 0a2 2 0 1 0-4 0M3 19a2 2 0 1 0 4 0a2 2 0 1 0-4 0M17 19a2 2 0 1 0 4 0a2 2 0 1 0-4 0M6.5 17.5 12 13l5.5 4.5M12 7v6',
slides: 'M3 4l18 0M4 4v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-10M12 16l0 4M9 20l6 0M8 12l3 -3l2 2l3 -3',
help: 'M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0M12 17l0 .01M12 13.5a1.5 1.5 0 0 1 1 -1.5a2.6 2.6 0 1 0 -3 -4',
chevron: 'M6 9l6 6l6 -6',
dots: 'M5 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0M12 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0M19 12m-1 0a1 1 0 1 0 2 0a1 1 0 1 0 -2 0',
close: 'M18 6l-12 12M6 6l12 12',
};
const icon = name => {
const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
svg.setAttribute('class', 'lsg-icon');
svg.setAttribute('viewBox', '0 0 24 24');
svg.setAttribute('aria-hidden', 'true');
const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
path.setAttribute('d', PATHS[name]);
svg.append(path);
return svg;
};
const desktop = () => { try { return window.matchMedia('(min-width: 640px)').matches; } catch { return true; } };
const read = () => {
try { return JSON.parse(window.localStorage.getItem(KEY) || 'null'); } catch { return null; }
};
const save = () => {
try { window.localStorage.setItem(KEY, JSON.stringify(state)); } catch { /* The current page keeps its state. */ }
};
const keyOf = card => [card.type, card.route || '', card.block || ''].join(' ');
const defaults = () => {
const names = toggle()?.getAttribute('data-lsg-sidebar-default')?.split(' ').filter(Boolean) ?? [];
const cards = names.map(name => name === 'contents' ? { type: 'contents' } : { type: 'page', route: name });
return { open: cards.length > 0, width: 0, cards };
};
let state = read();
if (!state || !Array.isArray(state.cards)) state = defaults();
state.cards = state.cards.filter(card => card && PATHS[card.type]);
const routeAt = href => {
const url = new URL(href, document.baseURI);
url.hash = '';
return url.href.startsWith(base.href) ? url.href.slice(base.href.length) || 'index.html' : url.href;
};
const address = route => new URL(route, base).href;
const current = () => routeAt(location.href);
const cache = new Map();
const page = route => {
let text = cache.get(route);
if (text) cache.delete(route);
else text = fetch(address(route)).then(response => response.ok ? response.text() : null).catch(() => null);
cache.set(route, text);
if (cache.size > 20) cache.delete(cache.keys().next().value);
return text.then(html => html && new DOMParser().parseFromString(html, 'text/html'));
};
const lists = li => li.querySelectorAll(':scope>ul,:scope>details>ul');
const kids = li => [...lists(li)].flatMap(ul => [...ul.children]);
const parentItem = li => {
const ul = li.parentElement;
if (ul?.tagName !== 'UL') return undefined;
if (ul.classList.contains('outline')) return null;
let up = ul.parentElement;
if (up?.tagName === 'DETAILS') up = up.parentElement;
return up?.tagName === 'LI' && up.closest('.outline') ? up : undefined;
};
const blockId = li => {
const anchor = li.querySelector(':scope>span[id^="block-"]');
if (anchor) return anchor.id.slice(6);
const path = [];
for (let item = li, up; item; item = up) {
up = parentItem(item);
if (up === undefined) return null;
path.unshift((up ? kids(up) : [...item.parentElement.children]).indexOf(item) + 1);
}
return path.join('.');
};
const find = (doc, id) => {
if (id.startsWith(SOURCE)) return doc.getElementById(id)?.closest('li');
if (!/^\d+(\.\d+)*$/.test(id)) return doc.getElementById('block-' + id.toLowerCase())?.closest('li');
let items = [...(doc.querySelector('main>ul.outline')?.children ?? [])], item = null;
for (const n of id.split('.')) {
item = items[Number(n) - 1];
if (!item) return null;
items = kids(item);
}
return item;
};
const label = li => {
const copy = (li.querySelector(':scope>details>summary') || li).cloneNode(true);
copy.querySelectorAll('ul,details,.bullet,.lsg-arrow,.task-checkbox').forEach(node => node.remove());
const text = copy.textContent.replace(/\s+/g, ' ').trim();
return text.length > 80 ? text.slice(0, 79) + '…' : text;
};
const titleOf = doc => doc.querySelector('main>h1')?.textContent.trim() || 'Page';
const mark = doc => {
for (const li of doc.querySelectorAll('main>ul.outline li')) {
const id = blockId(li);
if (id !== null) li.setAttribute('data-lsg-block', id);
}
};
const openAll = li => {
for (const details of [li, ...li.querySelectorAll('li')].map(item => item.querySelector(':scope>details')).filter(Boolean)) details.open = true;
li.classList.remove('folded');
li.querySelectorAll('.folded').forEach(item => item.classList.remove('folded'));
};
const crumbs = (doc, route, li) => {
const nav = el('nav', { class: 'lsg-breadcrumb', 'aria-label': 'Block parents' }, el('a', { class: 'page-ref', href: address(route) }, titleOf(doc)));
const ancestors = [];
for (let up = parentItem(li); up; up = parentItem(up)) ancestors.push(up);
if (ancestors.length > 3) nav.append(el('span', {}, '›'), '⋯');
for (const up of ancestors.slice(0, 3).reverse()) nav.append(el('span', {}, '›'), el('a', { href: address(route) + ZOOM + up.getAttribute('data-lsg-block') }, label(up)));
return nav;
};
const routeOf = card => card.type === 'contents' ? toggle()?.getAttribute('data-lsg-contents') : card.route;
const emptyOutline = () => el('ul', { class: 'outline' }, el('li', {}, el('a', { class: 'bullet', href: '#' })));
const scripts = {};
const script = name => scripts[name] ||= new Promise(done => document.head.append(Object.assign(document.createElement('script'), { src: new URL(name, base).href, onload: done, onerror: done })));
let focusDeck = false;
async function content(card) {
if (card.type === 'help') return { title: 'Help', body: help() };
if (card.type === 'graph') {
const body = el('div', { class: 'lsg-page-graph' });
await script('lsg-graph.js');
if (window.logseqGardenerGraph) window.logseqGardenerGraph.page(body);
else {
delete scripts['lsg-graph.js'];
body.append(el('p', {}, 'The page graph could not be loaded.'), el('button', { type: 'button', class: 'lsg-card-retry' }, 'Retry'));
}
return { title: 'Page graph', body };
}
const route = routeOf(card);
if (card.type === 'slides') {
const doc = route === current() && !document.querySelector('main[data-lsg-zoomed]') ? document : route && await page(route);
if (!doc) return { missing: true };
await script('lsg-slides.js');
const body = window.logseqGardenerSlides?.(doc.querySelector('main>ul.outline')) ?? '';
const focus = focusDeck && body && body.querySelector('.reveal');
focusDeck = false;
return { title: el('a', { class: 'page-ref', href: address(route) }, titleOf(doc)), body, route, focus };
}
const doc = route && await page(route);
if (!doc) {
if (card.type === 'contents') return { title: 'Contents', body: el('div', { class: 'lsg-card-page' }, emptyOutline()) };
return { missing: true };
}
mark(doc);
const main = doc.querySelector('main');
if (card.type === 'page' || card.type === 'contents') {
const title = card.type === 'contents' ? 'Contents' : titleOf(doc);
main.querySelector(':scope>h1')?.remove();
main.querySelectorAll('.unlinked-references').forEach(node => node.remove());
main.querySelectorAll('.linked-references>details').forEach(node => { node.open = false; });
const value = [...main.querySelectorAll('.page-property')].find(row => row.querySelector('dt')?.textContent.trim().toLowerCase() === 'icon')?.querySelector('dd')?.textContent.trim();
const body = el('div', { class: 'lsg-card-page' }, ...main.childNodes);
return { title, icon: value, body, route };
}
const li = find(doc, card.block);
if (!li) return { missing: true };
const nav = crumbs(doc, route, li);
openAll(li);
const outline = el('ul', { class: 'outline' }, li);
if (card.type === 'refs') return { title: 'Block references', body: el('div', { class: 'lsg-card-page' }, nav, outline) };
return { title: nav, body: el('div', { class: 'lsg-card-page' }, outline) };
}
function help() {
const has = selector => document.querySelector(selector);
const rows = [
['t l', 'Toggle left sidebar'],
['t r', 'Toggle right sidebar'],
['t t', 'Toggle between dark and light theme'],
['t w', 'Toggle wide mode'],
['g h', 'Go to home'],
['g a', 'Go to all pages'],
has('[data-lsg-graph-shortcut]') && ['g g', 'Go to the graph view'],
has('[data-lsg-journals-link]') && ['g j', 'Go to journals'],
has('[data-lsg-search]') && ['mod k', 'Search'],
['alt shift c', 'Toggle the Contents card'],
['shift click', 'Open a page, block or block reference in the right sidebar'],
].filter(Boolean);
const list = el('dl', { class: 'lsg-help' });
for (const [keys, text] of rows) list.append(el('dt', {}, ...keys.split(' ').map(key => el('kbd', {}, key))), el('dd', {}, text));
return el('div', { class: 'lsg-help-card' }, el('h3', {}, 'Keyboard shortcuts'), list);
}
const aside = el('aside', { class: 'lsg-right-sidebar', 'aria-label': 'Right sidebar', hidden: '' });
const handle = el('div', { class: 'lsg-right-resize', role: 'separator', tabindex: '0', 'aria-orientation': 'vertical', 'aria-label': 'Resize right sidebar' });
const bar = el('div', { class: 'lsg-right-bar' },
el('button', { type: 'button', class: 'lsg-right-tab', 'data-add': 'contents' }, 'Contents'),
el('button', { type: 'button', class: 'lsg-right-tab', 'data-add': 'graph' }, 'Page graph'),
el('button', { type: 'button', class: 'lsg-right-tab', 'data-add': 'help' }, 'Help'));
const list = el('div', { class: 'lsg-right-cards' });
aside.append(handle, bar, list);
const styles = el('link', { rel: 'stylesheet', href: new URL('lsg-sidebar.css', base).href });
document.head.append(styles);
document.body.append(aside);
const sections = new Map();
let serial = 0;
function frame(card) {
const id = 'lsg-card-' + ++serial;
const head = el('button', { type: 'button', class: 'lsg-card-head', 'aria-controls': id }, icon('chevron'), el('span', { class: 'lsg-card-icon' }, icon(card.type)), el('span', { class: 'lsg-card-title' }, card.type === 'help' ? 'Help' : card.type === 'contents' ? 'Contents' : ''));
const menu = el('button', { type: 'button', class: 'lsg-button lsg-card-menu', 'aria-label': 'Card menu', 'aria-haspopup': 'menu', 'aria-expanded': 'false' }, icon('dots'));
const close = el('button', { type: 'button', class: 'lsg-button lsg-card-close', 'aria-label': 'Close card' }, icon('close'));
const body = el('div', { class: 'lsg-card-body', id });
const section = el('section', { class: 'lsg-card' }, el('div', { class: 'lsg-card-header' }, head, menu, close), body);
section.card = card;
return section;
}
async function fill(section) {
const card = section.card, body = section.querySelector('.lsg-card-body');
if (card.collapsed || section.filled) return;
section.filled = true;
body.replaceChildren(el('p', { class: 'lsg-card-loading', role: 'status' }, 'Loading…'));
const shown = await content(card);
if (!section.filled || card.collapsed) return;
const title = section.querySelector('.lsg-card-title');
if (shown.missing) {
title.textContent = 'Page';
body.replaceChildren(el('p', {}, 'This page is not published.'), el('button', { type: 'button', class: 'lsg-card-dismiss' }, 'Close'));
return;
}
title.replaceChildren(shown.title);
if (shown.icon) section.querySelector('.lsg-card-icon').replaceChildren(shown.icon);
body.replaceChildren(shown.body);
if (shown.focus) shown.focus.focus();
window.logseqGardenerInitReferences?.(body);
window.logseqGardenerInitTheme?.(body);
}
function render() {
root.setAttribute('data-lsg-right-sidebar', state.open ? 'open' : 'closed');
toggle()?.setAttribute('aria-expanded', String(state.open));
if (state.width > 0) root.style.setProperty('--lsg-right-width', state.width + 'px');
aside.hidden = !state.open;
const shown = state.open && !state.cards.length ? [placeholder] : state.cards;
const keep = new Set(shown.map(keyOf));
for (const [key, section] of sections) if (!keep.has(key)) { section.remove(); sections.delete(key); }
shown.forEach((card, index) => {
let section = sections.get(keyOf(card));
if (!section) sections.set(keyOf(card), section = frame(card));
section.card = card;
if (list.children[index] !== section) list.insertBefore(section, list.children[index] ?? null);
const head = section.querySelector('.lsg-card-head');
head.setAttribute('aria-expanded', String(!card.collapsed));
section.classList.toggle('lsg-card-collapsed', !!card.collapsed);
if (card.collapsed) { section.filled = false; section.querySelector('.lsg-card-body').replaceChildren(); }
if (state.open) fill(section);
});
save();
}
const placeholder = { type: 'contents' };
function add(card) {
const key = keyOf(card);
state.cards = [{ ...card, collapsed: false }, ...state.cards.filter(other => keyOf(other) !== key)];
state.open = true;
render();
list.scrollTop = 0;
}
function remove(cards) {
const gone = new Set(cards.map(keyOf));
state.cards = state.cards.filter(card => !gone.has(keyOf(card)));
if (!state.cards.length) state.open = false;
render();
if (!state.open) toggle()?.focus();
}
const collapse = (cards, collapsed) => { for (const card of cards) card.collapsed = collapsed; render(); };
const real = card => {
if (card === placeholder && !state.cards.length) state.cards = [placeholder];
return card;
};
let open = null;
function items(card) {
const many = state.cards.length > 1;
const others = () => state.cards.filter(other => other !== card);
return [
[['Close', () => remove([card])], many && ['Close others', () => remove(others())], many && ['Close all', () => remove([...state.cards])]],
[[card.collapsed ? 'Expand' : 'Collapse', () => collapse([card], !card.collapsed)], many && ['Collapse others', () => collapse(others(), true)], many && ['Collapse all', () => collapse(state.cards, true)], many && ['Expand all', () => collapse(state.cards, false)]],
[(card.type === 'page' || card.type === 'contents' || card.type === 'slides') && routeOf(card) && ['Open as page', () => location.assign(address(routeOf(card)))]],
].map(group => group.filter(Boolean)).filter(group => group.length);
}
function closeMenu(focus = true) {
if (!open) return;
const { menu, button } = open;
open = null;
menu.remove();
button.setAttribute('aria-expanded', 'false');
if (focus) button.focus();
}
function openMenu(button, card) {
closeMenu(false);
const menu = el('div', { class: 'lsg-card-popup', role: 'menu', 'aria-label': 'Card menu' });
items(card).forEach((group, index) => {
if (index) menu.append(el('hr', { role: 'separator' }));
for (const [text, act] of group) {
const item = el('button', { type: 'button', role: 'menuitem' }, text);
item.addEventListener('click', () => { closeMenu(); act(); });
menu.append(item);
}
});
button.after(menu);
button.setAttribute('aria-expanded', 'true');
open = { menu, button };
menu.querySelector('[role=menuitem]').focus();
}
document.addEventListener('click', event => {
if (open && !open.menu.contains(event.target) && !open.button.contains(event.target)) closeMenu(false);
});
aside.addEventListener('keydown', event => {
if (event.target === handle && (event.key === 'ArrowLeft' || event.key === 'ArrowRight')) {
resize(aside.getBoundingClientRect().width + (event.key === 'ArrowLeft' ? 5 : -5));
event.preventDefault();
return;
}
if (!open) return;
const choices = [...open.menu.querySelectorAll('[role=menuitem]')];
const index = choices.indexOf(document.activeElement);
if (event.key === 'Escape') { closeMenu(); event.stopPropagation(); }
else if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
choices[(index + (event.key === 'ArrowDown' ? 1 : -1) + choices.length) % choices.length].focus();
event.preventDefault();
event.stopPropagation();
}
});
aside.addEventListener('click', event => {
const target = event.target;
const section = target.closest('.lsg-card');
const card = section?.card;
const add_ = target.closest('[data-add]');
if (add_) { add({ type: add_.getAttribute('data-add') }); return; }
if (!card) return;
if (target.closest('.lsg-card-head')) { real(card); collapse([card], !card.collapsed); return; }
if (target.closest('.lsg-card-menu')) { real(card); open?.button === target.closest('.lsg-card-menu') ? closeMenu() : openMenu(target.closest('.lsg-card-menu'), card); return; }
if (target.closest('.lsg-card-close,.lsg-card-dismiss')) { real(card); remove([card]); return; }
if (target.closest('.lsg-card-retry')) { section.querySelector('.lsg-card-head').focus(); section.filled = false; fill(section); return; }
const bullet = target.closest('.bullet');
const li = bullet?.closest('li[data-lsg-block]');
const route = routeOf(card);
if (bullet) {
event.preventDefault();
event.stopPropagation();
if (li && route) location.assign(address(route) + ZOOM + li.getAttribute('data-lsg-block'));
}
});
aside.addEventListener('auxclick', event => {
const section = event.button === 1 && event.target.closest('.lsg-card-header') && event.target.closest('.lsg-card');
if (section) { event.preventDefault(); real(section.card); remove([section.card]); }
});
function resize(width) {
const view = window.innerWidth;
state.width = Math.round(Math.min(Math.max(width, 320, view * 0.1), view * 0.7));
handle.setAttribute('aria-valuenow', String(state.width));
render();
}
handle.addEventListener('pointerdown', event => {
event.preventDefault();
try { handle.setPointerCapture(event.pointerId); } catch { /* Moves still reach the handle. */ }
root.setAttribute('data-lsg-resizing', '');
const move = moved => resize(window.innerWidth - moved.clientX);
const stop = () => {
root.removeAttribute('data-lsg-resizing');
handle.removeEventListener('pointermove', move);
handle.removeEventListener('pointerup', stop);
handle.removeEventListener('pointercancel', stop);
};
handle.addEventListener('pointermove', move);
handle.addEventListener('pointerup', stop);
handle.addEventListener('pointercancel', stop);
});
function target(event) {
const node = event.target;
const section = node.closest('section.lsg-card');
const cardRoute = section && routeOf(section.card);
const bullet = node.closest('.bullet');
if (bullet) {
const [path, hash = ''] = (bullet.getAttribute('href') || '').split('#');
if (path && hash.startsWith(SOURCE)) return { type: 'block', route: routeAt(path), block: hash };
const li = bullet.closest('li');
if (section) {
const id = li?.getAttribute('data-lsg-block');
return id && cardRoute ? { type: 'block', route: cardRoute, block: id } : null;
}
const journal = li.closest('.lsg-journal')?.querySelector('.journal-title')?.getAttribute('href');
const zoomed = li.closest('.lsg-zoom');
let id = blockId(li);
if (zoomed && id !== null) {
const at = decodeURIComponent(location.hash.slice(ZOOM.length));
const rest = id.split('.').slice(1);
id = !rest.length ? at : /^\d+(\.\d+)*$/.test(at) ? [at, ...rest].join('.') : null;
}
return id ? { type: 'block', route: journal ? routeAt(journal) : current(), block: id } : null;
}
const link = node.closest('a[href]');
if (!link) return null;
const [path, hash = ''] = link.getAttribute('href').split('#');
const route = path ? routeAt(path) : cardRoute || current();
if (link.classList.contains('block-ref-link') && hash.startsWith('block-')) return { type: 'refs', route, block: hash.slice(6) };
if (path && hash.startsWith(SOURCE)) return { type: 'refs', route, block: hash };
if (('#' + hash).startsWith(ZOOM)) return { type: 'block', route, block: decodeURIComponent(hash.slice(ZOOM.length - 1)) };
if (path && (/^p-[\w-]+\.html$/.test(route) || link.matches('.page-reference a,a.page-ref,a.tag'))) return { type: 'page', route };
return null;
}
window.logseqGardenerSidebar = request => {
if (!desktop()) return;
if (request === 'toggle') { state.open = !state.open; render(); return; }
if (request === 'restore') { render(); return; }
if (request?.type === 'slides') {
const card = { type: 'slides', route: current() };
focusDeck = true;
add(card);
const deck = sections.get(keyOf(card)).querySelector('.reveal');
if (deck) { focusDeck = false; deck.focus(); }
return;
}
if (request === 'contents') {
const has = state.cards.find(card => card.type === 'contents');
if (has && state.open) remove([has]);
else add({ type: 'contents' });
return;
}
const card = request?.target && target(request);
if (card) add(card);
};
})();