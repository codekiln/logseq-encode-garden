(() => {
if (window.logseqGardenerSlides) return;
document.head.append(Object.assign(document.createElement('style'), { textContent: '.lsg-slides-tip{margin:0 0 8px;font-size:14px}.lsg-slides-tip code{padding:0 4px;border-radius:4px;background:var(--lsg-surface)}.reveal{position:relative;overflow:hidden;width:100%;height:400px;background:#fff;color:var(--lsg-muted);font-size:42px;line-height:1.3;text-align:center;touch-action:pinch-zoom}:root[data-lsg-theme=dark] .reveal{background:var(--lsg-background)}.reveal:focus{outline:none}.reveal:focus-visible{outline:2px solid var(--lsg-focus);outline-offset:2px}.reveal:fullscreen{width:100vw;height:100vh}.reveal .backgrounds{position:absolute;inset:0;background-position:center;background-repeat:no-repeat;background-size:cover}.reveal .slides{position:absolute;left:50%;top:50%;width:960px;height:700px;transform:translate(-50%,-50%) scale(var(--slide-scale,1));pointer-events:none}.reveal .slides>section{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:safe center;box-sizing:border-box;padding:20px 0;pointer-events:auto;transition:transform var(--lsg-speed,.8s) cubic-bezier(.26,.86,.44,.985),opacity var(--lsg-speed,.8s),visibility var(--lsg-speed,.8s);visibility:hidden}.reveal .slides>section.present{visibility:visible;transform:none}.reveal .slides>section[data-dir=left]{transform:translateX(-150%)}.reveal .slides>section[data-dir=right]{transform:translateX(150%)}.reveal .slides>section[data-dir=up]{transform:translateY(-150%)}.reveal .slides>section[data-dir=down]{transform:translateY(150%)}.reveal .slides>section:is([data-transition=fade],[data-transition=none]):not(.present){transform:none;opacity:0}.reveal .slides>section[data-transition=none]{transition:none}.reveal :is(h1,h2,h3,h4,h5,h6){margin:0 0 20px;color:var(--lsg-title);font-weight:600;line-height:1.2;text-transform:uppercase;overflow-wrap:normal}.reveal h1{font-size:2em}.reveal h2{font-size:1.5em}.reveal h3{font-size:1.2em}.reveal h4{font-size:1.1em}.reveal :is(p,ul,ol){margin:20px 0}.reveal :is(ul,ol){display:inline-block;text-align:left}.reveal section img{max-width:100%;max-height:none;margin:1rem auto}.reveal pre{margin:20px auto;width:90%;text-align:left;font-size:.55em}.reveal pre.code,.reveal .hljs{background:none}.reveal .controls{position:absolute;right:12px;bottom:12px;z-index:2;width:110px;height:110px}.reveal .controls button{position:absolute;width:40px;height:40px;padding:0;border:0;background:none;color:var(--lsg-link);cursor:pointer;opacity:.9}.reveal .controls button:disabled{opacity:.1;cursor:default}.reveal .controls button::before{content:"";position:absolute;inset:12px;border:solid currentColor;border-width:0 0 5px 5px}.reveal .navigate-left{left:0;top:35px}.reveal .navigate-left::before{transform:rotate(45deg)}.reveal .navigate-right{right:0;top:35px}.reveal .navigate-right::before{transform:rotate(-135deg)}.reveal .navigate-up{left:35px;top:0}.reveal .navigate-up::before{transform:rotate(135deg)}.reveal .navigate-down{left:35px;bottom:0}.reveal .navigate-down::before{transform:rotate(-45deg)}.reveal .progress{position:absolute;left:0;right:0;bottom:0;z-index:2;height:3px;color:var(--lsg-link)}.reveal .progress span{display:block;height:100%;background:currentColor;transform-origin:0 0;transform:scaleX(var(--lsg-progress,0));transition:transform .8s cubic-bezier(.26,.86,.44,.985)}.reveal .lsg-blackout{position:absolute;inset:0;z-index:5;background:#000}.reveal .lsg-jump{position:absolute;left:12px;top:12px;z-index:6;width:8em;padding:4px 8px;border:1px solid var(--lsg-border);border-radius:4px;font:inherit;font-size:16px}.reveal.overview .slides,.reveal.overview .backgrounds,.reveal.overview .controls{display:none}.reveal .lsg-overview{position:absolute;inset:0;z-index:3;display:flex;gap:12px;overflow:auto;padding:12px;box-sizing:border-box;background:inherit}.reveal .lsg-overview>div{display:flex;flex-direction:column;gap:12px;flex:none}.reveal .lsg-overview button{position:relative;flex:none;overflow:hidden;width:192px;height:140px;padding:0;border:1px solid var(--lsg-border);background:inherit;color:inherit;font:inherit;cursor:pointer}.reveal .lsg-overview button[aria-current=true]{outline:3px solid var(--lsg-focus)}.reveal .lsg-overview section{position:absolute;left:0;top:0;width:960px;height:700px;display:flex;flex-direction:column;justify-content:safe center;transform:scale(.2);transform-origin:0 0;pointer-events:none}' }));
const el = (tag, attrs = {}, ...children) => {
const node = document.createElement(tag);
for (const [name, value] of Object.entries(attrs)) node.setAttribute(name, value);
node.append(...children);
return node;
};
const MEDIA = 'img,video,audio,iframe,object,embed,svg,canvas,hr,table';
const kids = li => [...li.querySelectorAll(':scope>ul>li,:scope>details>ul>li')].filter(item => item.querySelector(':scope>.bullet,:scope>details>summary>.bullet'));
function content(li) {
const box = document.createElement('div');
const details = li.querySelector(':scope>details');
const childLists = new Set(kids(li).map(item => item.parentElement));
const nodes = [...li.childNodes].filter(node => node !== details);
if (details) nodes.push(...(details.querySelector(':scope>summary')?.childNodes ?? []), ...[...details.children].filter(node => node.tagName !== 'SUMMARY'));
for (const node of nodes) if (!(node.nodeName === 'UL' && childLists.has(node))) box.append(document.importNode(node, true));
box.querySelectorAll('.bullet,.lsg-arrow,.task-checkbox,.task-marker,.page-properties,.block-properties,span[id^="block-"],span[id^="source-block-"]').forEach(node => node.remove());
box.querySelectorAll('[id]').forEach(node => node.removeAttribute('id'));
return box.textContent.trim() || box.querySelector(MEDIA) ? box : null;
}
function columns(outline) {
const walk = (li, out) => { out.push(li); for (const kid of kids(li)) walk(kid, out); return out; };
return [...(outline?.children ?? [])].filter(li => li.tagName === 'LI')
.map(li => walk(li, []).map(item => ({ li: item })).filter(slide => (slide.box = content(slide.li))))
.filter(column => column.length);
}
function section(slide) {
const node = el('section');
for (const { name, value } of slide.li.attributes) if (name.startsWith('data-slide-')) node.setAttribute('data-' + name.slice(11), value);
const speed = { fast: '.4s', slow: '1.2s' }[node.getAttribute('data-transition-speed')];
if (speed) node.style.setProperty('--lsg-speed', speed);
node.append(slide.box.cloneNode(true));
return node;
}
window.logseqGardenerSlides = outline => {
const deck = el('div', { class: 'reveal', tabindex: '0', role: 'region', 'aria-label': 'Slides' });
const body = el('div', { class: 'lsg-slides-card' }, el('p', { class: 'lsg-slides-tip' }, 'Tip: press ', el('code', {}, 'f'), ' to go fullscreen'), deck);
const cols = columns(outline);
const flat = cols.flatMap((column, c) => column.map((_, r) => [c, r]));
const backgrounds = el('div', { class: 'backgrounds' });
const slides = el('div', { class: 'slides' });
const button = (name, label) => el('button', { type: 'button', class: 'navigate-' + name, 'aria-label': label });
const controls = el('aside', { class: 'controls' }, button('left', 'previous slide'), button('right', 'next slide'), button('up', 'above slide'), button('down', 'below slide'));
const progress = el('div', { class: 'progress' }, el('span'));
deck.replaceChildren(backgrounds, slides, controls, progress);
if (!flat.length) { deck.append(el('p', {}, 'This page has no blocks to show.')); return body; }
let c = 0, r = 0, overview = null, blackout = null, jump = null, drawn = false;
const shown = new Map();
const at = (col, row) => cols[col]?.[row] && col + '/' + row;
const index = () => flat.findIndex(([col, row]) => col === c && row === r);
function draw() {
const reach = { present: at(c, r), left: at(c - 1, 0), right: at(c + 1, 0), up: at(c, r - 1), down: at(c, r + 1) };
const keys = new Map(Object.entries(reach).filter(([, key]) => key).map(([dir, key]) => [key, dir]));
for (const [key, node] of shown) if (!keys.has(key)) { node.remove(); shown.delete(key); }
for (const [key, dir] of keys) {
let node = shown.get(key);
if (!node) {
const [col, row] = key.split('/').map(Number);
node = section(cols[col][row]);
node.setAttribute('data-dir', dir);
shown.set(key, node);
slides.append(node);
}
}
void slides.offsetWidth;
for (const [key, dir] of keys) {
const node = shown.get(key);
node.classList.toggle('present', dir === 'present');
if (dir === 'present') node.removeAttribute('data-dir');
else {
const [col, row] = key.split('/').map(Number);
node.setAttribute('data-dir', col < c ? 'left' : col > c ? 'right' : row < r ? 'up' : 'down');
}
node.setAttribute('aria-hidden', String(dir !== 'present'));
}
const present = shown.get(reach.present);
const style = backgrounds.style;
style.backgroundImage = present.dataset.backgroundImage ? 'url(' + JSON.stringify(present.dataset.backgroundImage) + ')' : '';
style.backgroundColor = present.dataset.backgroundColor || '';
style.backgroundSize = present.dataset.backgroundSize || '';
style.backgroundPosition = present.dataset.backgroundPosition || '';
const [left, right, up, down] = controls.children;
left.disabled = !reach.left;
right.disabled = !reach.right;
up.disabled = !reach.up;
down.disabled = !reach.down;
deck.style.setProperty('--lsg-progress', flat.length > 1 ? index() / (flat.length - 1) : 1);
if (overview) mark();
}
const go = (col, row) => {
col = Math.max(0, Math.min(cols.length - 1, col));
row = Math.max(0, Math.min(cols[col].length - 1, row));
if (col === c && row === r) return;
c = col;
r = row;
draw();
};
const step = by => { const next = flat[index() + by]; if (next) go(...next); };
function scale() {
if (!deck.isConnected) { if (drawn) observer.disconnect(); return; }
drawn = true;
const { width, height } = deck.getBoundingClientRect();
if (width && height) deck.style.setProperty('--slide-scale', Math.min(width / 960, height / 700));
}
const observer = new ResizeObserver(scale);
observer.observe(deck);
function mark() {
for (const item of overview.querySelectorAll('button')) {
const here = item.dataset.at === c + '/' + r;
item.setAttribute('aria-current', String(here));
if (here) item.scrollIntoView({ block: 'nearest', inline: 'nearest' });
}
}
function toggleOverview() {
if (overview) { overview.remove(); overview = null; deck.classList.remove('overview'); deck.focus(); return; }
overview = el('div', { class: 'lsg-overview', role: 'listbox', 'aria-label': 'Slide overview' });
cols.forEach((column, col) => overview.append(el('div', {}, ...column.map((slide, row) => el('button', { type: 'button', 'data-at': col + '/' + row, 'aria-label': 'Slide ' + (col + 1) + '/' + (row + 1) }, section(slide))))));
deck.classList.add('overview');
deck.append(overview);
mark();
}
function openJump() {
jump = el('input', { class: 'lsg-jump', type: 'text', 'aria-label': 'Go to slide', placeholder: 'Go to slide' });
jump.addEventListener('keydown', event => {
event.stopPropagation();
if (event.key === 'Escape' || event.key === 'Enter') {
const value = jump.value.trim();
const pair = value.match(/^(\d+)\s*\/\s*(\d+)$/);
if (event.key === 'Enter' && pair) go(Number(pair[1]) - 1, Number(pair[2]) - 1);
else if (event.key === 'Enter' && /^\d+$/.test(value) && flat[Number(value) - 1]) go(...flat[Number(value) - 1]);
jump.remove();
jump = null;
deck.focus();
event.preventDefault();
}
});
deck.append(jump);
jump.focus();
}
function fullscreen() {
if (document.fullscreenElement === deck) document.exitFullscreen?.();
else deck.requestFullscreen?.().catch(() => {});
}
deck.addEventListener('keydown', event => {
if (event.target !== deck && event.target.closest('input,textarea,select')) return;
event.stopPropagation();
if (event.ctrlKey || event.metaKey || event.altKey || event.key === 'Tab') return;
if (blackout) { blackout.remove(); blackout = null; event.preventDefault(); return; }
const key = event.key, shift = event.shiftKey, lower = key.toLowerCase();
const act = {
arrowleft: () => shift ? go(0, 0) : go(c - 1, 0),
h: () => go(c - 1, 0),
arrowright: () => shift ? go(cols.length - 1, 0) : go(c + 1, 0),
l: () => go(c + 1, 0),
arrowup: () => go(c, shift ? 0 : r - 1),
k: () => go(c, r - 1),
arrowdown: () => go(c, shift ? cols[c].length - 1 : r + 1),
j: () => go(c, r + 1),
n: () => step(1),
p: () => step(-1),
' ': () => step(shift ? -1 : 1),
b: () => deck.append(blackout = el('div', { class: 'lsg-blackout' })),
'.': () => deck.append(blackout = el('div', { class: 'lsg-blackout' })),
g: openJump,
escape: toggleOverview,
o: toggleOverview,
enter: () => { const choice = event.target.closest('.lsg-overview button'); if (choice) choice.click(); else if (overview) toggleOverview(); },
f: fullscreen,
}[lower];
if (!act) return;
event.preventDefault();
act();
});
deck.addEventListener('focus', () => deck.classList.add('focused'));
deck.addEventListener('blur', () => deck.classList.remove('focused'));
deck.addEventListener('click', event => {
const control = event.target.closest('.controls button');
const choice = event.target.closest('.lsg-overview button');
if (control) {
const name = control.className.slice(9);
if (name === 'left') go(c - 1, 0); else if (name === 'right') go(c + 1, 0); else go(c, r + (name === 'up' ? -1 : 1));
} else if (choice) {
const [col, row] = choice.dataset.at.split('/').map(Number);
go(col, row);
toggleOverview();
}
if (!event.target.closest('a,input')) deck.focus();
});
draw();
setTimeout(scale);
return body;
};
})();