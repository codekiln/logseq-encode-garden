(() => {
if (window.logseqGardenerGraph) return;
const base = new URL('.', document.currentScript?.src || location.href);
const root = document.documentElement;
const STORE = 'logseq-gardener-graph';
const JOURNAL = 1, TAG = 2, PARENT = 4, BUILT_IN = 8, EXCLUDED = 16, ORPHAN = 32, REFERENCE_ONLY = 64, JOURNAL_ONLY = 128;
const COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'];
const NAMED = { green: '#008000', orange: '#ffa500' };
const rotl = (v, n) => (v << n) | (v >>> (32 - n));
const cljsHash = text => {
let h = 0;
for (let i = 0; i < text.length; i++) h = (Math.imul(31, h) + text.charCodeAt(i)) | 0;
if (!h) return 0;
const k = Math.imul(rotl(Math.imul(h, 0xcc9e2d51), 15), 0x1b873593);
h = (Math.imul(rotl(k, 13), 5) + 0xe6546b64) | 0;
h ^= 4; h ^= h >>> 16; h = Math.imul(h, 0x85ebca6b); h ^= h >>> 13; h = Math.imul(h, 0xc2b2ae35); h ^= h >>> 16;
return h;
};
const parentColor = title => COLORS[Math.abs(cljsHash(title)) % COLORS.length];
const routeOf = title => {
let h = 0xcbf29ce484222325n;
for (const byte of new TextEncoder().encode(title)) h = ((h ^ BigInt(byte)) * 0x100000001b3n) & 0xffffffffffffffffn;
return 'p-' + h.toString(16).padStart(16, '0') + '.html';
};
const sizeOf = degree => Math.trunc(8 * Math.max(1, Math.cbrt(degree || 1)));
function decode(buffer) {
const view = new DataView(buffer), bytes = new Uint8Array(buffer);
if (String.fromCharCode(...bytes.subarray(0, 4)) !== 'LSGG' || view.getUint16(4, true) !== 1) throw new Error('unknown graph format');
const n = view.getUint32(8, true), e = view.getUint32(12, true), links = view.getUint32(16, true);
const [x0, y0, x1, y1] = [24, 28, 32, 36].map(at => view.getFloat32(at, true));
let at = 40;
const int = () => { let value = 0, shift = 0, byte; do { byte = bytes[at++]; value += (byte & 127) * 2 ** shift; shift += 7; } while (byte > 127); return value; };
const start = new Uint32Array(n + 1);
for (let i = 0; i < n; i++) start[i + 1] = start[i] + int();
const text = bytes.subarray(at, at += start[n]);
const flags = bytes.slice(at, at += n);
const degree = new Uint32Array(n);
for (let i = 0; i < n; i++) degree[i] = int();
const x = new Float32Array(n), y = new Float32Array(n);
for (let i = 0; i < n; i++, at += 4) {
x[i] = x0 + view.getUint16(at, true) / 65535 * (x1 - x0);
y[i] = y0 + view.getUint16(at + 2, true) / 65535 * (y1 - y0);
}
const a = new Uint32Array(e), b = new Uint32Array(e);
for (let k = 0, s = 0, t = 0; k < e; k++) {
const step = int();
t = (step ? s + step : t) + int() + 1;
s += step; a[k] = s; b[k] = t;
}
const names = new Array(n), decoder = new TextDecoder();
const title = i => names[i] ??= decoder.decode(text.subarray(start[i], start[i + 1]));
return { n, links, flags, degree, x, y, a, b, title };
}
function fromJSON(json) {
const n = json.t.length, a = new Uint32Array(json.e.length / 2), b = new Uint32Array(json.e.length / 2);
for (let k = 0; k < a.length; k++) { a[k] = json.e[2 * k]; b[k] = json.e[2 * k + 1]; }
return { n, links: a.length, flags: Uint8Array.from(json.f), degree: new Uint32Array(n), x: new Float32Array(n), y: new Float32Array(n), a, b, title: i => json.t[i] };
}
function around(g, centre) {
const keep = new Int32Array(g.n).fill(-1), order = [centre];
keep[centre] = 0;
for (let k = 0; k < g.a.length; k++) {
const other = g.a[k] === centre ? g.b[k] : g.b[k] === centre ? g.a[k] : -1;
if (other >= 0 && keep[other] < 0) { keep[other] = order.length; order.push(other); }
}
const a = [], b = [];
for (let k = 0; k < g.a.length; k++) if (keep[g.a[k]] >= 0 && keep[g.b[k]] >= 0) { a.push(keep[g.a[k]]); b.push(keep[g.b[k]]); }
const pick = (array, T) => T.from(order, i => array[i]);
return { n: order.length, links: a.length, flags: pick(g.flags, Uint8Array), degree: new Uint32Array(order.length), x: pick(g.x, Float32Array), y: pick(g.y, Float32Array), a: Uint32Array.from(a), b: Uint32Array.from(b), title: i => g.title(order[i]) };
}
const load = (path, as, signal) => fetch(new URL(path, base), { signal }).then(response => {
if (!response.ok) throw Object.assign(new Error('HTTP ' + response.status), { status: response.status });
if (as === 'arrayBuffer') return new Response(response.body.pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
return response[as]();
});
function simulator() {
let worker = null, listener = null;
return (message, next) => {
if (!worker) {
worker = new Worker(new URL('lsg-graph-worker.js', base));
worker.onmessage = event => listener?.(event.data);
}
if (next) listener = next;
worker.postMessage(message);
};
}
const dark = () => root.getAttribute('data-lsg-theme') === 'dark';
const palette = () => dark()
? { node: '#93a1a1', tag: 'orange', current: '#ffffff', label: 'rgba(255,255,255,0.8)', edge: '#094b5a', selectedEdge: '#999' }
: { node: '#999', tag: 'green', current: '#045591', label: 'rgba(0,0,0,0.8)', edge: '#cccccc', selectedEdge: '#A5B4FC' };
const ACCENT = '#6366F1', HOVER_EDGE = '#A5B4FC', SELECTED = parentColor('ls-selected-nodes');
const rgb = color => {
let hex = (NAMED[color] || color).slice(1);
if (hex.length === 3) hex = hex.replace(/./g, '$&$&');
return [0, 2, 4].map(i => parseInt(hex.slice(i, i + 2), 16));
};
function webgl(canvas) {
const gl = canvas.getContext('webgl2', { antialias: true, preserveDrawingBuffer: true });
if (!gl) return null;
const program = (vertex, fragment) => {
const p = gl.createProgram();
for (const [type, text] of [[gl.VERTEX_SHADER, vertex], [gl.FRAGMENT_SHADER, fragment]]) {
const s = gl.createShader(type);
gl.shaderSource(s, '#version 300 es\nprecision mediump float;\n' + text);
gl.compileShader(s);
gl.attachShader(p, s);
}
gl.bindAttribLocation(p, 0, 'p'); gl.bindAttribLocation(p, 1, 'c'); gl.bindAttribLocation(p, 2, 's');
gl.linkProgram(p);
return gl.getProgramParameter(p, gl.LINK_STATUS) ? p : null;
};
const head = 'in vec2 p;uniform vec2 m,o;';
const lines = program(head + 'void main(){gl_Position=vec4(p*m+o,0,1);}', 'uniform vec4 c;out vec4 f;void main(){f=c;}');
const points = program(head + 'in vec4 c;in float s;uniform float k;out vec4 v;void main(){gl_Position=vec4(p*m+o,0,1);gl_PointSize=max(2.*s*k,2.);v=c;}',
'in vec4 v;out vec4 f;void main(){vec2 d=gl_PointCoord*2.-1.;float r=dot(d,d);if(r>1.)discard;f=v;}');
if (!lines || !points) return null;
const buffers = { p: gl.createBuffer(), c: gl.createBuffer(), s: gl.createBuffer(), nodes: gl.createBuffer(), edges: gl.createBuffer(), extra: gl.createBuffer() };
let counts = { nodes: 0, edges: 0 };
const attribute = (index, buffer, size, type, normalized) => {
gl.bindBuffer(gl.ARRAY_BUFFER, buffer); gl.enableVertexAttribArray(index);
gl.vertexAttribPointer(index, size, type, normalized, 0, 0);
};
const uniforms = (p, view) => {
gl.useProgram(p);
gl.uniform2f(gl.getUniformLocation(p, 'm'), 2 * view.k / view.w, -2 * view.k / view.h);
gl.uniform2f(gl.getUniformLocation(p, 'o'), 2 * view.tx / view.w - 1, 1 - 2 * view.ty / view.h);
};
const lineColor = (color, alpha = 1) => { const [r, g, b] = rgb(color); gl.uniform4f(gl.getUniformLocation(lines, 'c'), r / 255, g / 255, b / 255, alpha); };
return {
positions(xy) { gl.bindBuffer(gl.ARRAY_BUFFER, buffers.p); gl.bufferData(gl.ARRAY_BUFFER, xy, gl.DYNAMIC_DRAW); },
colors(rgba) { gl.bindBuffer(gl.ARRAY_BUFFER, buffers.c); gl.bufferData(gl.ARRAY_BUFFER, rgba, gl.DYNAMIC_DRAW); },
sizes(sizes) { gl.bindBuffer(gl.ARRAY_BUFFER, buffers.s); gl.bufferData(gl.ARRAY_BUFFER, sizes, gl.STATIC_DRAW); },
visible(nodes, edges) {
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffers.nodes); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, nodes, gl.STATIC_DRAW);
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffers.edges); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, edges, gl.STATIC_DRAW);
counts = { nodes: nodes.length, edges: edges.length };
},
draw(view, edgeColor, highlight, highlightColor) {
gl.viewport(0, 0, canvas.width, canvas.height);
gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
gl.enable(gl.BLEND); gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);
gl.disableVertexAttribArray(1); gl.disableVertexAttribArray(2);
uniforms(lines, view); attribute(0, buffers.p, 2, gl.FLOAT, false);
lineColor(edgeColor);
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffers.edges); gl.drawElements(gl.LINES, counts.edges, gl.UNSIGNED_INT, 0);
if (highlight.length) {
lineColor(highlightColor);
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffers.extra); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, highlight, gl.DYNAMIC_DRAW);
gl.drawElements(gl.LINES, highlight.length, gl.UNSIGNED_INT, 0);
}
uniforms(points, view); gl.uniform1f(gl.getUniformLocation(points, 'k'), view.k * view.dpr);
attribute(0, buffers.p, 2, gl.FLOAT, false); attribute(1, buffers.c, 4, gl.UNSIGNED_BYTE, true); attribute(2, buffers.s, 1, gl.FLOAT, false);
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buffers.nodes); gl.drawElements(gl.POINTS, counts.nodes, gl.UNSIGNED_INT, 0);
},
};
}
function canvas2d(canvas) {
const g = canvas.getContext('2d');
let xy, rgba, sizes, nodes = new Uint32Array(0), edges = new Uint32Array(0);
const path = (list, view, color) => {
g.beginPath();
for (let k = 0; k < list.length; k += 2) {
const s = list[k] * 2, t = list[k + 1] * 2;
g.moveTo(xy[s] * view.k + view.tx, xy[s + 1] * view.k + view.ty); g.lineTo(xy[t] * view.k + view.tx, xy[t + 1] * view.k + view.ty);
}
g.strokeStyle = color; g.lineWidth = 1; g.stroke();
};
return {
positions(value) { xy = value; }, colors(value) { rgba = value; }, sizes(value) { sizes = value; },
visible(n, e) { nodes = n; edges = e; },
draw(view, edgeColor, highlight, highlightColor) {
g.setTransform(view.dpr, 0, 0, view.dpr, 0, 0);
g.clearRect(0, 0, view.w, view.h);
path(edges, view, edgeColor);
if (highlight.length) path(highlight, view, highlightColor);
for (const i of nodes) {
g.fillStyle = `rgba(${rgba[i * 4]},${rgba[i * 4 + 1]},${rgba[i * 4 + 2]},${rgba[i * 4 + 3] / 255})`;
g.beginPath(); g.arc(xy[i * 2] * view.k + view.tx, xy[i * 2 + 1] * view.k + view.ty, Math.max(sizes[i] * view.k, 1), 0, 2 * Math.PI); g.fill();
}
},
};
}
const el = (tag, attrs = {}, ...children) => {
const node = document.createElement(tag);
for (const [name, value] of Object.entries(attrs)) node.setAttribute(name, value);
node.append(...children);
return node;
};
const styles = () => {
if (!document.querySelector('link[href$="lsg-graph.css"]')) document.head.append(el('link', { rel: 'stylesheet', href: new URL('lsg-graph.css', base).href }));
};
function Graph(box, options) {
const canvas = box.querySelector('canvas'), labels = el('canvas', { class: 'lsg-graph-labels', 'aria-hidden': 'true' });
canvas.after(labels);
const status = box.querySelector('.lsg-graph-status');
const draw = webgl(canvas) || canvas2d(canvas);
const text = labels.getContext('2d');
const view = { k: 1, tx: 0, ty: 0, w: 1, h: 1, dpr: 1 };
let g = null, fitting = false, visible = new Uint8Array(0), hovered = -1, selected = [], neighbours = new Set(), frame = 0, grid = null, adjacency = null;
const self = { box, canvas, view };
const say = message => { if (status) status.textContent = message; };
function fit() {
let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity, any = false;
for (let i = 0; i < g.n; i++) if (visible[i]) { any = true; x0 = Math.min(x0, g.x[i]); x1 = Math.max(x1, g.x[i]); y0 = Math.min(y0, g.y[i]); y1 = Math.max(y1, g.y[i]); }
if (!any) { x0 = y0 = -1; x1 = y1 = 1; }
view.k = Math.min(view.w / (x1 - x0 + 120), view.h / (y1 - y0 + 120), 2);
view.tx = view.w / 2 - (x0 + x1) / 2 * view.k; view.ty = view.h / 2 - (y0 + y1) / 2 * view.k;
}
function resize() {
const unsized = view.w <= 1;
view.dpr = window.devicePixelRatio || 1;
view.w = canvas.clientWidth || 1; view.h = canvas.clientHeight || 1;
if (unsized && g && view.w > 1) fit();
for (const c of [canvas, labels]) { c.width = Math.round(view.w * view.dpr); c.height = Math.round(view.h * view.dpr); }
self.redraw();
}
function colors() {
const p = palette(), rgba = new Uint8Array(g.n * 4);
const base = rgb(p.node), tag = rgb(p.tag), current = rgb(p.current), accent = rgb(ACCENT), chosen = rgb(SELECTED);
for (let i = 0; i < g.n; i++) {
const f = g.flags[i];
let c = i === hovered || neighbours.has(i) && !selected.includes(i) ? accent : selected.includes(i) ? chosen
: f & PARENT ? rgb(parentColor(g.title(i))) : f & TAG ? tag : options.centre && i === 0 ? current : base;
rgba.set([...c, 255], i * 4);
}
draw.colors(rgba);
}
function positions() {
const xy = new Float32Array(g.n * 2);
for (let i = 0; i < g.n; i++) { xy[i * 2] = g.x[i]; xy[i * 2 + 1] = g.y[i]; }
draw.positions(xy);
grid = null;
}
self.show = (mask, refit) => {
visible = mask;
if (refit) fitting = true;
const nodes = [], edges = [];
for (let i = 0; i < g.n; i++) if (visible[i]) nodes.push(i);
for (let k = 0; k < g.a.length; k++) if (visible[g.a[k]] && visible[g.b[k]]) edges.push(g.a[k], g.b[k]);
draw.visible(Uint32Array.from(nodes), Uint32Array.from(edges));
grid = null;
if (fitting) { fitting = false; fit(); }
self.count = nodes.length;
self.redraw();
};
self.set = (data, keepView) => {
g = data; hovered = -1; selected = []; neighbours = new Set(); adjacency = null;
self.g = g;
draw.sizes(Float32Array.from(g.degree, d => options.centre ? 8 : sizeOf(d)));
positions(); colors();
if (!keepView) { visible = new Uint8Array(g.n).fill(1); fitting = true; }
};
self.move = (x, y) => { g.x = x; g.y = y; positions(); self.redraw(); };
self.neighbours = i => {
if (!adjacency) {
adjacency = Array.from({ length: g.n }, () => []);
for (let k = 0; k < g.a.length; k++) { adjacency[g.a[k]].push(g.b[k]); adjacency[g.b[k]].push(g.a[k]); }
}
return adjacency[i];
};
self.select = i => {
if (!selected.includes(i)) selected.push(i);
neighbours = new Set(selected.flatMap(self.neighbours));
colors(); self.redraw(); options.onselect?.(selected);
};
self.clear = () => { selected = []; neighbours = new Set(); colors(); self.redraw(); };
self.selected = () => selected;
self.recolor = () => { colors(); self.redraw(); };
self.redraw = () => { if (!frame && g) frame = requestAnimationFrame(paint); };
function paint() {
frame = 0;
const p = palette(), focus = hovered >= 0 ? [hovered] : selected, highlight = [];
if (focus.length) for (let k = 0; k < g.a.length; k++) {
if ((focus.includes(g.a[k]) || focus.includes(g.b[k])) && visible[g.a[k]] && visible[g.b[k]]) highlight.push(g.a[k], g.b[k]);
}
draw.draw(view, p.edge, Uint32Array.from(highlight), hovered >= 0 ? HOVER_EDGE : p.selectedEdge);
text.setTransform(view.dpr, 0, 0, view.dpr, 0, 0);
text.clearRect(0, 0, view.w, view.h);
text.font = '12px system-ui,sans-serif'; text.textAlign = 'center'; text.textBaseline = 'top';
let drawn = 0;
for (let i = 0; i < g.n && drawn < 2000; i++) {
if (!visible[i] || i === hovered) continue;
const radius = (options.centre ? 8 : sizeOf(g.degree[i])) * view.k;
if (radius * 2 < 12 && !selected.includes(i)) continue;
const sx = g.x[i] * view.k + view.tx, sy = g.y[i] * view.k + view.ty;
if (sx < -200 || sx > view.w + 200 || sy < -50 || sy > view.h + 50) continue;
text.fillStyle = p.label; text.fillText(g.title(i), sx, sy + radius + 4);
drawn++;
}
if (hovered >= 0) {
const radius = (options.centre ? 8 : sizeOf(g.degree[hovered])) * view.k;
const sx = g.x[hovered] * view.k + view.tx, sy = g.y[hovered] * view.k + view.ty + radius + 4, label = g.title(hovered);
const width = text.measureText(label).width + 8;
text.fillStyle = 'rgba(238,238,238,1)'; text.fillRect(sx - width / 2, sy - 2, width, 18);
text.fillStyle = '#333333'; text.fillText(label, sx, sy);
}
if (!self.drawn) { self.drawn = true; performance.mark?.('lsg-graph-first-frame'); options.onfirst?.(); }
}
function hit(sx, sy) {
const CELL = 100;
if (!grid) {
grid = new Map();
for (let i = 0; i < g.n; i++) if (visible[i]) {
const key = Math.floor(g.x[i] / CELL) + ',' + Math.floor(g.y[i] / CELL);
(grid.get(key) || grid.set(key, []).get(key)).push(i);
}
}
const wx = (sx - view.tx) / view.k, wy = (sy - view.ty) / view.k, reach = 2;
let best = -1, bestDistance = Infinity;
for (let gx = Math.floor(wx / CELL) - reach; gx <= Math.floor(wx / CELL) + reach; gx++) for (let gy = Math.floor(wy / CELL) - reach; gy <= Math.floor(wy / CELL) + reach; gy++) {
for (const i of grid.get(gx + ',' + gy) || []) {
const d = Math.hypot(g.x[i] - wx, g.y[i] - wy), r = (options.centre ? 8 : sizeOf(g.degree[i])) + 3 / view.k;
if (d <= r && d < bestDistance) { best = i; bestDistance = d; }
}
}
return best;
}
self.open = i => {
if (g.flags[i] & REFERENCE_ONLY) { say(g.title(i) + ' — not published'); return; }
location.assign(new URL(routeOf(g.title(i)), base).href);
};
const zoom = (factor, sx, sy) => {
const k = Math.min(Math.max(view.k * factor, 0.005), 20);
view.tx = sx - (sx - view.tx) * k / view.k; view.ty = sy - (sy - view.ty) * k / view.k; view.k = k;
self.redraw();
};
const pointers = new Map();
let press = null, pinch = 0;
const local = event => { const r = canvas.getBoundingClientRect(); return [event.clientX - r.left, event.clientY - r.top]; };
canvas.addEventListener('pointerdown', event => {
canvas.focus({ preventScroll: true });
const [sx, sy] = local(event);
pointers.set(event.pointerId, [sx, sy]);
try { canvas.setPointerCapture(event.pointerId); } catch { /* Moves still arrive. */ }
if (pointers.size === 2) { const [a, b] = [...pointers.values()]; pinch = Math.hypot(a[0] - b[0], a[1] - b[1]); press = null; return; }
const node = hit(sx, sy);
press = { sx, sy, tx: view.tx, ty: view.ty, node, moved: false, shift: event.shiftKey, at: Date.now() };
if (event.pointerType === 'touch' && node >= 0) press.timer = setTimeout(() => { if (press && !press.moved) { press.long = true; self.select(node); } }, 500);
});
canvas.addEventListener('pointermove', event => {
const [sx, sy] = local(event);
if (pointers.has(event.pointerId)) pointers.set(event.pointerId, [sx, sy]);
if (pointers.size === 2) {
const [a, b] = [...pointers.values()], distance = Math.hypot(a[0] - b[0], a[1] - b[1]);
if (pinch) zoom(distance / pinch, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2);
pinch = distance;
return;
}
if (!press) {
const node = hit(sx, sy);
if (node !== hovered) { hovered = node; canvas.style.cursor = node >= 0 ? 'pointer' : ''; colors(); self.redraw(); }
return;
}
if (!press.moved && Math.hypot(sx - press.sx, sy - press.sy) < 4) return;
press.moved = true;
clearTimeout(press.timer);
if (press.node >= 0 && options.drag) {
if (!selected.includes(press.node)) self.select(press.node);
options.drag(press.node, (sx - view.tx) / view.k, (sy - view.ty) / view.k);
} else {
view.tx = press.tx + sx - press.sx; view.ty = press.ty + sy - press.sy; self.redraw();
}
});
const up = event => {
pointers.delete(event.pointerId);
if (pointers.size < 2) pinch = 0;
const was = press;
press = null;
if (!was) return;
clearTimeout(was.timer);
if (was.moved) { if (was.node >= 0) options.release?.(); return; }
if (was.node < 0 || was.long) return;
if (was.shift) self.select(was.node); else self.open(was.node);
};
canvas.addEventListener('pointerup', up);
canvas.addEventListener('pointercancel', up);
canvas.addEventListener('pointerleave', () => { if (hovered >= 0 && !press) { hovered = -1; colors(); self.redraw(); } });
canvas.addEventListener('wheel', event => {
event.preventDefault();
const [sx, sy] = local(event);
zoom(Math.exp(-event.deltaY * (event.deltaMode ? 0.05 : 0.002)), sx, sy);
}, { passive: false });
canvas.addEventListener('keydown', event => {
const step = 40, moves = { ArrowLeft: [step, 0], ArrowRight: [-step, 0], ArrowUp: [0, step], ArrowDown: [0, -step] };
if (moves[event.key]) { view.tx += moves[event.key][0]; view.ty += moves[event.key][1]; self.redraw(); }
else if (event.key === '+' || event.key === '=') zoom(1.25, view.w / 2, view.h / 2);
else if (event.key === '-') zoom(0.8, view.w / 2, view.h / 2);
else return;
event.preventDefault();
});
new MutationObserver(() => self.recolor()).observe(root, { attributes: true, attributeFilter: ['data-lsg-theme'] });
if (window.ResizeObserver) new ResizeObserver(resize).observe(canvas); else window.addEventListener('resize', resize);
self.resize = resize;
self.say = say;
return self;
}
const WAIT = 500;
function progress(graph, what, task) {
const text = el('span'), button = el('button', { type: 'button', class: 'lsg-graph-action', hidden: '' });
const overlay = el('div', { class: 'lsg-graph-loading' }, el('p', { role: 'status' }, el('span', { class: 'lsg-graph-spinner' }), text), button);
graph.box.append(overlay);
let state = '', controller = null, timer = 0;
const show = (next, message = '', label = '') => {
const focused = overlay.contains(document.activeElement);
state = next;
if (next) graph.box.setAttribute('data-lsg-load', next); else graph.box.removeAttribute('data-lsg-load');
text.textContent = message;
button.textContent = label;
button.hidden = !label;
if (focused) (label ? button : graph.canvas).focus();
};
async function run() {
controller?.abort();
clearTimeout(timer);
const mine = controller = new AbortController(), signal = mine.signal;
const loading = () => show('loading', `Loading the ${what}…`, 'Cancel');
if (state) loading(); else timer = setTimeout(loading, WAIT);
try {
await Promise.race([task(signal), new Promise((_, reject) => signal.addEventListener('abort', () => reject(signal.reason)))]);
if (controller === mine) show('');
} catch {
if (controller !== mine) return;
if (signal.aborted) show('cancelled', `The ${what} was not loaded.`, `Load the ${what}`);
else show('failed', `The ${what} could not be loaded.`, 'Retry');
} finally {
if (controller === mine) { clearTimeout(timer); controller = null; }
}
}
button.addEventListener('click', event => {
if (event.detail > 1) return;
if (state === 'loading') controller?.abort(); else run();
});
return run;
}
const read = () => { try { return JSON.parse(sessionStorage.getItem(STORE) || 'null'); } catch { return null; } };
const save = value => { try { sessionStorage.setItem(STORE, JSON.stringify(value)); } catch { /* Settings last for this page. */ } };
function globalGraph(box) {
styles();
const config = JSON.parse(box.getAttribute('data-lsg-graph'));
const saved = read() || {};
const state = { settings: { ...config.settings, ...saved.settings }, forces: { ...config.forces, ...saved.forces }, filters: saved.filters || [], hops: 0, paused: false };
if (!config.journals) state.settings.journals = false;
const panel = box.querySelector('.graph-filters');
const $ = selector => panel.querySelector(selector);
const files = {};
const simulate = simulator();
let simulated = false;
const graph = Graph(box, {
onselect: () => { $('[data-hops]').hidden = false; },
drag: (node, x, y) => { start(); simulate({ type: 'drag', node, x, y }); },
release: () => simulate({ type: 'release' }),
onfirst: () => graph.say(''),
});
const fetchData = (journals, signal) => {
const kept = files[journals];
if (kept && !kept.signal.aborted) return kept.promise;
const promise = load(journals ? config.journals : config.data, 'arrayBuffer', signal).then(decode).then(g => Object.assign(g, { homeX: g.x, homeY: g.y }));
files[journals] = { promise, signal };
promise.catch(() => { if (files[journals]?.promise === promise) delete files[journals]; });
return promise;
};
let shown = null;
async function data(signal) {
const g = await fetchData(!!state.settings.journals, signal);
signal.throwIfAborted();
if (shown !== g) { graph.set(g, false); shown = g; simulated = false; }
return g;
}
function mask() {
const g = shown, s = state.settings, keep = new Uint8Array(g.n);
let count = 0;
for (let i = 0; i < g.n; i++) {
const f = g.flags[i];
keep[i] = (s.journals || !(f & JOURNAL)) && (s.orphan_pages || !(f & ORPHAN)) && (s.builtin_pages || !(f & BUILT_IN)) && (s.excluded_pages || !(f & EXCLUDED)) ? 1 : 0;
count += keep[i];
}
$('[data-count=pages]').textContent = count + ' pages';
$('[data-count=links]').textContent = g.links + ' links';
if (state.filters.length) {
const words = state.filters.map(word => word.toLowerCase());
for (let i = 0; i < g.n; i++) if (keep[i] && !words.some(word => g.title(i).toLowerCase().includes(word))) keep[i] = 0;
}
const chosen = graph.selected();
if (state.hops && chosen.length) {
const near = new Uint8Array(g.n);
let edge = [...chosen];
for (const i of edge) near[i] = 1;
for (let step = 0; step < state.hops; step++) {
const next = [];
for (const i of edge) for (const j of graph.neighbours(i)) if (!near[j]) { near[j] = 1; next.push(j); }
edge = next;
}
for (let i = 0; i < g.n; i++) keep[i] &= near[i];
}
return keep;
}
const refresh = refit => {
graph.show(mask(), refit);
save({ settings: state.settings, forces: state.forces, filters: state.filters });
for (const button of panel.querySelectorAll('[data-setting]')) {
const name = button.getAttribute('data-setting');
button.setAttribute('aria-checked', String(name === 'paused' ? state.paused : !!state.settings[name]));
}
for (const input of panel.querySelectorAll('[data-force]')) {
const name = input.getAttribute('data-force');
input.value = state.forces[name];
$(`output[data-for=${name}]`).textContent = state.forces[name];
}
const list = $('[data-filters]');
list.replaceChildren(...state.filters.map((word, index) => el('li', {}, el('span', {}, word), el('button', { type: 'button', 'data-remove': String(index), 'aria-label': 'Remove filter ' + word }, '×'))));
$('[data-clear]').hidden = !state.filters.length;
if (state.filters.length) open('search', true);
};
function start() {
if (simulated) return;
simulated = true;
simulate({ type: 'start', x: shown.x, y: shown.y, a: shown.a, b: shown.b, forces: state.forces, live: true }, message => {
if (message.type === 'tick') graph.move(message.x, message.y);
});
if (state.paused) simulate({ type: 'pause' });
}
const open = (name, value) => {
const section = panel.querySelector(`[data-section=${name}]`);
const head = section.querySelector('.graph-filters-head');
const opened = value ?? head.getAttribute('aria-expanded') !== 'true';
head.setAttribute('aria-expanded', String(opened));
section.querySelector('.graph-filters-body').hidden = !opened;
};
function results(query) {
const list = $('[data-results]');
const words = query.trim().toLowerCase();
let found = [];
if (words) for (let i = 0; i < shown.n; i++) if (shown.title(i).toLowerCase().includes(words)) found.push(i);
const rank = i => { const t = shown.title(i).toLowerCase(); return (t === words ? 0 : t.startsWith(words) ? 1 : 2) * 1e4 + t.length; };
found = found.sort((a, b) => rank(a) - rank(b)).slice(0, 20);
list.replaceChildren(...found.map(i => el('li', {}, el('button', { type: 'button', 'data-node': String(i) }, shown.title(i)))));
}
panel.addEventListener('click', event => {
const target = event.target.closest('button');
if (!target) return;
const section = target.closest('.graph-filters-head');
if (section) { open(section.parentElement.getAttribute('data-section')); return; }
const name = target.getAttribute('data-setting');
if (name === 'paused') { state.paused = !state.paused; if (simulated) simulate({ type: state.paused ? 'pause' : 'resume' }); refresh(); return; }
if (name) {
state.settings[name] = !state.settings[name];
if (name === 'journals') state.hops = 0;
refresh();
if (name === 'journals') fetchGraph();
return;
}
if (target.matches('[data-reset=graph]')) {
state.filters = []; state.hops = 0; graph.clear(); $('[data-hops]').hidden = true; $('[data-hops-input]').value = 1; $('output[data-for=hops]').textContent = 1;
refresh(true); return;
}
if (target.matches('[data-reset=forces]')) {
state.forces = { ...config.forces };
const g = shown;
if (simulated) { simulate({ type: 'pause' }); simulated = false; }
g.x = g.homeX; g.y = g.homeY;
graph.set(g, true); refresh(); return;
}
if (target.matches('[data-search-open]')) { const input = $('[data-search-input]'); input.hidden = false; input.focus(); return; }
if (target.matches('[data-remove]')) { state.filters.splice(Number(target.getAttribute('data-remove')), 1); refresh(true); return; }
if (target.matches('[data-clear]')) { state.filters = []; refresh(true); return; }
if (target.matches('[data-node]')) {
const i = Number(target.getAttribute('data-node'));
if (event.shiftKey) graph.select(i); else graph.open(i);
return;
}
if (target.matches('[data-export]')) exportPng();
});
panel.addEventListener('keydown', event => {
const input = event.target.closest('[data-search-input]');
if (input && event.key === 'Enter' && input.value.trim()) {
state.filters.push(input.value.trim()); input.value = ''; results(''); refresh(true); event.preventDefault();
}
const node = event.target.closest('[data-node]');
if (node && event.key === 'Enter' && event.shiftKey) { graph.select(Number(node.getAttribute('data-node'))); event.preventDefault(); }
});
panel.addEventListener('input', event => {
const target = event.target;
if (target.matches('[data-search-input]')) results(target.value);
if (target.matches('[data-force]')) {
const name = target.getAttribute('data-force');
state.forces[name] = Number(target.value);
$(`output[data-for=${name}]`).textContent = target.value;
save({ settings: state.settings, forces: state.forces, filters: state.filters });
start();
simulate({ type: 'forces', forces: state.forces });
}
if (target.matches('[data-hops-input]')) {
state.hops = Number(target.value);
$('output[data-for=hops]').textContent = target.value;
graph.show(mask(), true);
}
});
function exportPng() {
const out = el('canvas');
out.width = graph.canvas.width; out.height = graph.canvas.height;
const c = out.getContext('2d');
c.fillStyle = getComputedStyle(document.body).backgroundColor || '#fff';
c.fillRect(0, 0, out.width, out.height);
c.drawImage(graph.canvas, 0, 0);
c.drawImage(box.querySelector('.lsg-graph-labels'), 0, 0);
out.toBlob(blob => {
const link = el('a', { href: URL.createObjectURL(blob), download: 'graph.png' });
document.body.append(link); link.click(); link.remove();
setTimeout(() => URL.revokeObjectURL(link.href), 1000);
}, 'image/png');
}
let ready = false;
const fetchGraph = progress(graph, 'graph', async signal => {
await data(signal);
refresh();
if (ready) return;
ready = true;
panel.hidden = false;
if (Object.keys(config.forces).some(name => config.forces[name] !== state.forces[name])) { start(); simulate({ type: 'forces', forces: state.forces }); }
});
graph.resize();
fetchGraph();
}
async function pageGraph(body) {
styles();
const KEY = 'logseq-gardener-page-graph-journals';
let journals = false;
try { journals = sessionStorage.getItem(KEY) === 'true'; } catch { /* Off by default. */ }
const toggle = el('button', { type: 'button', role: 'switch', class: 'lsg-switch', 'aria-checked': String(journals), 'aria-labelledby': 'lsg-page-graph-journals' });
const box = el('div', { class: 'lsg-graph lsg-page-graph-canvas' }, el('canvas', { class: 'lsg-graph-canvas', tabindex: '0', 'aria-label': 'Page graph' }), el('p', { class: 'lsg-graph-status', role: 'status' }));
body.replaceChildren(el('div', { class: 'graph-filters-row lsg-page-graph-row' }, el('span', { id: 'lsg-page-graph-journals' }, 'Show Journals'), toggle), box);
let route = location.pathname.split('/').pop();
if (!/^p-[0-9a-f]{16}\.html$/.test(route)) route = document.querySelector('.lsg-journal .journal-title')?.getAttribute('href') || '';
const graph = Graph(box, { centre: true });
const simulate = simulator();
if (!route) { graph.say('This view has no page to draw.'); return; }
let whole;
const missing = error => { if (!error.status) throw error; };
async function render(signal) {
if (whole === undefined) whole = await load('_graph/p/' + route.slice(2, 18) + '.json', 'json', signal).then(fromJSON, error => { missing(error); return null; });
let g = null;
if (whole) {
const keep = Uint8Array.from(whole.flags, f => journals || !(f & JOURNAL_ONLY) ? 1 : 0);
const order = [];
keep.forEach((k, i) => { if (k) order.push(i); });
const index = new Int32Array(whole.n).fill(-1);
order.forEach((i, at) => { index[i] = at; });
const a = [], b = [];
for (let k = 0; k < whole.a.length; k++) if (keep[whole.a[k]] && keep[whole.b[k]]) { a.push(index[whole.a[k]]); b.push(index[whole.b[k]]); }
g = { n: order.length, links: a.length, flags: Uint8Array.from(order, i => whole.flags[i]), degree: new Uint32Array(order.length), x: new Float32Array(order.length), y: new Float32Array(order.length), a: Uint32Array.from(a), b: Uint32Array.from(b), title: i => whole.title(order[i]) };
let first = true;
const laid = await new Promise(done => simulate({ type: 'start', x: g.x, y: g.y, a: g.a, b: g.b, forces: { link_distance: 70, charge_strength: -600, charge_range: 600 }, phyllotaxis: true }, message => {
if (signal.aborted) return;
if (first) { first = false; done(message); } else graph.move(message.x, message.y);
}));
g.x = laid.x; g.y = laid.y;
} else {
const global = decode(await load(journals ? '_graph/journals.bin' : '_graph/default.bin', 'arrayBuffer', signal).catch(error => { missing(error); return load('_graph/default.bin', 'arrayBuffer', signal); }));
let centre = -1;
for (let i = 0; i < global.n && centre < 0; i++) if (routeOf(global.title(i)) === route) centre = i;
if (centre >= 0) g = around(global, centre);
}
signal.throwIfAborted();
if (!g) { graph.say('This page has no page graph.'); return; }
graph.set(g, false);
graph.resize();
graph.show(new Uint8Array(g.n).fill(1));
graph.say('');
}
const fetchPage = progress(graph, 'page graph', render);
toggle.addEventListener('click', () => {
journals = !journals;
toggle.setAttribute('aria-checked', String(journals));
try { sessionStorage.setItem(KEY, String(journals)); } catch { /* This card keeps the setting. */ }
fetchPage();
});
await fetchPage();
}
window.logseqGardenerGraph = { page: pageGraph, decode, routeOf, cljsHash, parentColor, sizeOf, around };
const box = document.querySelector('[data-lsg-graph]');
if (box) globalGraph(box);
})();