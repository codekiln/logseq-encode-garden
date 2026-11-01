/** Logseq's journals feed: later batches near the bottom, Linked References when opened. */
(() => {
  if (window.logseqGardenerInitJournals) return;
  const fetchPage = async href => {
    const response = await fetch(href);
    if (!response.ok) throw new Error(`${href}: ${response.status}`);
    return new DOMParser().parseFromString(await response.text(), 'text/html');
  };
  let loading = false;
  const observer = 'IntersectionObserver' in window
    ? new window.IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) more(entry.target);
    }, { rootMargin: '0px 0px 500px 0px' })
    : null;
  const watch = link => { if (observer) { observer.unobserve(link); observer.observe(link); } };
  async function more(link) {
    if (loading || !link.isConnected) return;
    loading = true;
    try {
      const page = await fetchPage(link.getAttribute('href'));
      for (const article of page.querySelectorAll('article.lsg-journal')) link.before(document.adoptNode(article));
      const next = page.querySelector('[data-lsg-journals-earlier]');
      if (next) link.setAttribute('href', next.getAttribute('href'));
      else {
        observer?.unobserve(link);
        link.remove();
        return;
      }
    } catch {
      // Earlier still opens the batch file.
      observer?.unobserve(link);
      return;
    } finally {
      loading = false;
    }
    // Observe again so a link that is still near the viewport loads the next batch.
    watch(link);
  }
  document.addEventListener('toggle', async event => {
    const details = event.target;
    if (!details.matches?.('details[data-lsg-journal-refs]') || !details.open || details.hasAttribute('data-lsg-loading')) return;
    details.setAttribute('data-lsg-loading', '');
    try {
      const page = await fetchPage(details.getAttribute('data-lsg-journal-refs'));
      const section = page.querySelector('[data-lsg-backlinks]');
      if (!section) throw new Error('no linked references');
      const adopted = document.adoptNode(section);
      adopted.removeAttribute('id');
      adopted.querySelector('details.backlinks-disclosure')?.setAttribute('open', '');
      details.replaceWith(adopted);
      window.logseqGardenerInitBacklinks?.(adopted.parentElement);
    } catch {
      // The link inside the section still opens the journal's references.
      details.removeAttribute('data-lsg-loading');
    }
  }, true);
  /** Watch the Earlier link under `root`; hosts call this after replacing page content. */
  window.logseqGardenerInitJournals = (root = document) => {
    for (const link of root.querySelectorAll('[data-lsg-journals-earlier]')) watch(link);
  };
  window.logseqGardenerInitJournals();
})();
