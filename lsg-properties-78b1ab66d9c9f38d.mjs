/** Site-scoped disclosure preference. Early parsing restoration lives in properties-start.js. */
const early = window.logseqGardenerInitProperties;
const selector = '.page-properties > details > summary';
function visit() {
  const pending = early.pending();
  if (pending !== undefined) {
    early.o = pending;
    return;
  }
  early.o = undefined;
  const now = Date.now();
  try {
    const saved = JSON.parse(window.localStorage.getItem(early.k));
    if (saved && typeof saved.open === 'boolean' && Number.isFinite(saved.seen) &&
        saved.seen <= now && now - saved.seen < 30 * 86400000) {
      window.localStorage.setItem(early.k, JSON.stringify({ open: saved.open, seen: now }));
      early.o = saved.open;
    } else window.localStorage.removeItem(early.k);
  } catch {
    try { window.localStorage.removeItem(early.k); } catch { /* Storage is blocked. */ }
  }
}
function initialize(root = document) {
  visit();
  early(root);
}
document.removeEventListener('click', early.c);
document.addEventListener('click', event => {
  const summary = event.target.closest?.(selector);
  // The early script owns pending choices: it saves after propagation or when the page is left.
  if (summary && !event.target.closest('a') && !event.defaultPrevented) early.s(event, !summary.parentElement.open);
});
initialize();
delete early.c;
// A Back/Forward cache restore re-reads the preference through visit(), which renews it.
early.r = visit;
window.logseqGardenerInitProperties = initialize;
