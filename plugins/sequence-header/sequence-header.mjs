// lsg first-party plugin sequence-header (logseq-gardener-docs/pages/lsg___Ref___First-Party Plugins.md): header
// links to the pages `prev::` and `next::` name. The entry holds `prev` and `next`, each
// `{url, title}`. [key, label, arrow]; the previous link goes before the spacer, next after.
const SIDES = [
  ['prev', 'Previous', 'M5 12l14 0M5 12l6 6M5 12l6 -6'],
  ['next', 'Next', 'M5 12l14 0M13 18l6 -6M13 6l6 6'],
];

/** The entry's links as `{ prev, next }`, each `{ href, title }` on the site's origin. */
export function sequenceLinks(metadata, base) {
  const links = {};
  for (const [key] of SIDES) {
    const { url, title } = metadata?.[key] ?? {};
    if (typeof url !== 'string' || typeof title !== 'string' || !title) continue;
    try {
      const href = new URL(url, base);
      if (href.origin === new URL(base).origin) links[key] = { href: href.href, title };
    } catch { /* a malformed URL gives no link */ }
  }
  return links;
}

/** Add `links` around the header's spacer and return them. */
export function drawLinks(doc, links) {
  const space = doc.querySelector('.lsg-header-space');
  if (!space) return [];
  return SIDES.filter(([key]) => links[key]).map(([key, label, arrow]) => {
    const { href, title } = links[key];
    const link = doc.createElement('a');
    link.className = `lsg-sequence lsg-sequence-${key}`;
    link.setAttribute('href', href);
    link.setAttribute('rel', key);
    link.setAttribute('aria-label', `${label}: ${title}`);
    const icon = `<svg class="lsg-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="${arrow}"/></svg>`;
    const text = '<span class="lsg-sequence-title"></span>';
    link.innerHTML = key === 'prev' ? icon + text : text + icon;
    link.querySelector('span').textContent = title;
    if (key === 'prev') space.before(link);
    else space.after(link);
    return link;
  });
}

export default {
  id: 'sequence-header',
  apiVersion: 1,
  setup(host) {
    let shown = [];
    const clear = () => shown.forEach((link) => link.remove());
    // A page without an entry gets `{}` and no links.
    const stop = host.onPageAdopted(({ metadata }) => {
      clear();
      shown = drawLinks(host.document, sequenceLinks(metadata, host.baseURL));
    });
    return () => {
      stop();
      clear();
    };
  },
};
