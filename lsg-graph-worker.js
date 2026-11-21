(() => {
const ALPHA_MIN = 0.001, DECAY = 1 - Math.pow(ALPHA_MIN, 1 / 300), RADIUS = 52, THETA2 = 0.25;
let n = 0, x, y, vx, vy, ea, eb, strength, bias, forces, alpha = 0, target = 0, paused = false, live = false;
let fixed = -1, fx = 0, fy = 0, timer = 0, release = 0;
const jiggle = (i, j) => (((i * 2654435761 + j * 40503) >>> 0) / 4294967296 - 0.5) * 1e-6;
function prepare() {
const degree = new Uint32Array(n);
for (let k = 0; k < ea.length; k++) { degree[ea[k]]++; degree[eb[k]]++; }
strength = new Float64Array(ea.length); bias = new Float64Array(ea.length);
for (let k = 0; k < ea.length; k++) {
const da = degree[ea[k]], db = degree[eb[k]];
strength[k] = 1 / Math.min(da, db); bias[k] = da / (da + db);
}
}
function link() {
const d = forces.link_distance;
for (let k = 0; k < ea.length; k++) {
const s = ea[k], t = eb[k];
let dx = x[t] + vx[t] - x[s] - vx[s] || jiggle(s, t), dy = y[t] + vy[t] - y[s] - vy[s] || jiggle(t, s);
const l = Math.sqrt(dx * dx + dy * dy), m = (l - d) / l * alpha * strength[k];
dx *= m; dy *= m;
vx[t] -= dx * bias[k]; vy[t] -= dy * bias[k];
vx[s] += dx * (1 - bias[k]); vy[s] += dy * (1 - bias[k]);
}
}
let cap = 0, cx0, cy0, csize, kids, head, count, mx, my, next, cells;
function grow(c) {
if (c < cap) return;
cap = Math.max(64, cap * 2);
const re = (a, T, m = 1, fill = 0) => { const b = new T(cap * m).fill(fill); if (a) b.set(a); return b; };
cx0 = re(cx0, Float64Array); cy0 = re(cy0, Float64Array); csize = re(csize, Float64Array);
kids = re(kids, Int32Array, 4, -1); head = re(head, Int32Array, 1, -1);
count = re(count, Uint32Array); mx = re(mx, Float64Array); my = re(my, Float64Array);
}
function cell(x0, y0, size) {
grow(cells);
cx0[cells] = x0; cy0[cells] = y0; csize[cells] = size; head[cells] = -1; count[cells] = 0;
kids.fill(-1, cells * 4, cells * 4 + 4);
return cells++;
}
function quadrant(c, px, py) { const h = csize[c] / 2; return (px >= cx0[c] + h ? 1 : 0) | (py >= cy0[c] + h ? 2 : 0); }
function child(c, q) { const h = csize[c] / 2; const k = cell(cx0[c] + (q & 1 ? h : 0), cy0[c] + (q & 2 ? h : 0), h); kids[c * 4 + q] = k; return k; }
const leaf = c => kids[c * 4] < 0 && kids[c * 4 + 1] < 0 && kids[c * 4 + 2] < 0 && kids[c * 4 + 3] < 0;
function build() {
let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
for (let i = 0; i < n; i++) { x0 = Math.min(x0, x[i]); y0 = Math.min(y0, y[i]); x1 = Math.max(x1, x[i]); y1 = Math.max(y1, y[i]); }
if (!next || next.length !== n) next = new Int32Array(n);
next.fill(-1); cells = 0;
cell(x0, y0, Math.max(x1 - x0, y1 - y0, 1) * 1.0001);
for (let p = 0; p < n; p++) {
let c = 0;
for (;;) {
if (leaf(c)) {
const o = head[c];
if (o < 0) { head[c] = p; break; }
if (Math.abs(x[o] - x[p]) < 1e-9 && Math.abs(y[o] - y[p]) < 1e-9 || csize[c] < 1e-6) { next[p] = o; head[c] = p; break; }
head[c] = -1;
head[child(c, quadrant(c, x[o], y[o]))] = o;
continue;
}
const q = quadrant(c, x[p], y[p]), k = kids[c * 4 + q];
if (k < 0) { head[child(c, q)] = p; break; }
c = k;
}
}
for (let c = cells - 1; c >= 0; c--) {
if (leaf(c)) {
let m = 0;
for (let p = head[c]; p >= 0; p = next[p]) m++;
count[c] = m;
if (head[c] >= 0) { mx[c] = x[head[c]]; my[c] = y[head[c]]; }
continue;
}
let m = 0, sx = 0, sy = 0;
for (let q = 0; q < 4; q++) { const k = kids[c * 4 + q]; if (k >= 0) { m += count[k]; sx += mx[k] * count[k]; sy += my[k] * count[k]; } }
count[c] = m;
if (m) { mx[c] = sx / m; my[c] = sy / m; }
}
}
const stack = [];
function charge() {
build();
const s = forces.charge_strength * alpha, max2 = forces.charge_range * forces.charge_range;
for (let i = 0; i < n; i++) {
const px = x[i], py = y[i];
let fxi = 0, fyi = 0;
stack.length = 0; stack.push(0);
while (stack.length) {
const c = stack.pop();
if (!count[c]) continue;
let dx = mx[c] - px, dy = my[c] - py, l = dx * dx + dy * dy;
if (csize[c] * csize[c] / THETA2 < l) {
if (l < max2) {
if (!dx) { dx = jiggle(i, c); l += dx * dx; }
if (!dy) { dy = jiggle(c, i); l += dy * dy; }
if (l < 1) l = Math.sqrt(l);
const w = s * count[c] / l; fxi += dx * w; fyi += dy * w;
}
continue;
}
if (!leaf(c)) {
const nx = Math.min(Math.max(px, cx0[c]), cx0[c] + csize[c]) - px, ny = Math.min(Math.max(py, cy0[c]), cy0[c] + csize[c]) - py;
if (nx * nx + ny * ny < max2) for (let q = 0; q < 4; q++) if (kids[c * 4 + q] >= 0) stack.push(kids[c * 4 + q]);
continue;
}
if (l >= max2) continue;
if (!(head[c] === i && next[i] < 0)) {
if (!dx) { dx = jiggle(i, c); l += dx * dx; }
if (!dy) { dy = jiggle(c, i); l += dy * dy; }
if (l < 1) l = Math.sqrt(l);
}
for (let p = head[c]; p >= 0; p = next[p]) if (p !== i) { fxi += dx * s / l; fyi += dy * s / l; }
}
vx[i] += fxi; vy[i] += fyi;
}
}
function collide() {
const grid = new Map(), home = new Float64Array(n * 2);
for (let i = 0; i < n; i++) {
const gx = Math.floor((x[i] + vx[i]) / RADIUS), gy = Math.floor((y[i] + vy[i]) / RADIUS), key = gx * 1048576 + gy;
home[i * 2] = gx; home[i * 2 + 1] = gy;
let list = grid.get(key);
if (!list) grid.set(key, list = []);
list.push(i);
}
for (let i = 0; i < n; i++) {
const xi = x[i] + vx[i], yi = y[i] + vy[i];
for (let gx = home[i * 2] - 1; gx <= home[i * 2] + 1; gx++) for (let gy = home[i * 2 + 1] - 1; gy <= home[i * 2 + 1] + 1; gy++) {
const list = grid.get(gx * 1048576 + gy);
if (!list) continue;
for (const j of list) {
if (j <= i) continue;
let dx = xi - x[j] - vx[j], dy = yi - y[j] - vy[j], l = dx * dx + dy * dy;
if (l >= RADIUS * RADIUS) continue;
if (!dx) { dx = jiggle(i, j); l += dx * dx; }
if (!dy) { dy = jiggle(j, i); l += dy * dy; }
l = Math.sqrt(l);
const m = (RADIUS - l) / l * 0.5;
vx[i] += dx * m; vy[i] += dy * m; vx[j] -= dx * m; vy[j] -= dy * m;
}
}
}
}
function tick() {
alpha += (target - alpha) * DECAY;
link(); charge(); collide(); collide();
let sx = 0, sy = 0;
for (let i = 0; i < n; i++) { vx[i] -= x[i] * 0.02 * alpha; vy[i] -= y[i] * 0.02 * alpha; sx += x[i]; sy += y[i]; }
sx /= n || 1; sy /= n || 1;
for (let i = 0; i < n; i++) {
x[i] -= sx; y[i] -= sy;
if (i === fixed) { x[i] = fx; y[i] = fy; vx[i] = vy[i] = 0; continue; }
vx[i] *= 0.5; vy[i] *= 0.5; x[i] += vx[i]; y[i] += vy[i];
}
}
const settled = () => alpha < ALPHA_MIN && target === 0;
const post = done => self.postMessage({ type: 'tick', x: Float32Array.from(x), y: Float32Array.from(y), done });
function run() {
timer = 0;
if (paused) return;
const start = Date.now();
do tick(); while (!live && !settled() && Date.now() - start < 100);
live = true;
if (release && Date.now() > release) { target = 0; release = 0; }
const done = settled();
post(done);
if (!done) timer = setTimeout(run, Math.max(0, 16 - (Date.now() - start)));
}
const schedule = () => { if (!timer && !paused) timer = setTimeout(run, 0); };
self.onmessage = ({ data }) => {
if (data.type === 'start') {
n = data.x.length; live = !!data.live; forces = data.forces;
x = Float64Array.from(data.x); y = Float64Array.from(data.y);
if (data.phyllotaxis) for (let i = 0; i < n; i++) { const r = 10 * Math.sqrt(0.5 + i), a = i * Math.PI * (3 - Math.sqrt(5)); x[i] = r * Math.cos(a); y[i] = r * Math.sin(a); }
vx = new Float64Array(n); vy = new Float64Array(n); ea = data.a; eb = data.b;
prepare(); alpha = 1; target = 0; schedule();
} else if (data.type === 'forces') { forces = data.forces; alpha = 1; schedule(); }
else if (data.type === 'drag') {
fixed = data.node; fx = data.x; fy = data.y;
target = 0.3; alpha = Math.max(alpha, 0.3); release = Date.now() + 2000; schedule();
} else if (data.type === 'release') fixed = -1;
else if (data.type === 'pause') { paused = true; clearTimeout(timer); timer = 0; }
else if (data.type === 'resume') { paused = false; schedule(); }
};
})();