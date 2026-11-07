// Shared search controller. The engine and search data load when a visitor points at or
// focuses the search button, presses Cmd/Ctrl+K or opens search.
const revisionPattern = /^[a-f0-9]{16}$/u;
const fail = () => { throw new Error('Search data is unavailable or from another publication. Retry, or reload this page.'); };
function staticURL(href, base, origin) {
  const url = new URL(href, base);
  if (!['http:', 'https:'].includes(url.protocol) || url.origin !== origin ||
      url.username || url.password || url.search || url.hash) fail();
  return url;
}
export function publicationFromLink(link, base, origin) {
  if (!link) return null;
  const revision = link.getAttribute('data-revision');
  if (!revisionPattern.test(revision || '')) fail();
  const manifest = staticURL(link.getAttribute('href'), base, origin);
  if (!manifest.pathname.endsWith(`/lsg-search-manifest-${revision}.json`)) fail();
  return Object.freeze({ revision, manifest: manifest.href, origin, key: manifest.href + ':' + revision });
}

// Loads the manifest, engine and title index on first use, then the shards each query
// needs and the chunks of the rows it draws. Fetched files stay for the publication.
export function createSearchLoader({ fetchFile = (...args) => fetch(...args), importEngine = url => import(url) } = {}) {
  let current = null, cache = null, pending = null, controller = null, generation = 0, parts = new Map();
  function cancel() {
    generation++;
    controller?.abort(); controller = null; pending = null;
    // Unfinished shard and chunk fetches restart on the next query.
    for (const [key, part] of parts) if (!part.done) parts.delete(key);
  }
  function setPublication(publication) {
    if (current?.key === publication?.key) return false;
    cancel(); current = publication; cache = null; parts = new Map();
    return true;
  }
  async function textFile(url, signal) {
    const response = await fetchFile(url, { signal, redirect: 'error', credentials: 'same-origin', cache: 'no-cache' });
    if (!response.ok || (response.url && response.url !== url)) fail();
    return response.text();
  }
  function signal() {
    controller ||= new AbortController();
    const token = generation, active = controller.signal;
    return { signal: active, check() { if (active.aborted || generation !== token) throw new DOMException('Search closed or publication changed', 'AbortError'); } };
  }
  function load() {
    if (!current) return Promise.reject(new Error('Search is unavailable on this page.'));
    if (cache) return Promise.resolve(cache);
    if (pending) return pending;
    const publication = current, token = generation, run = signal();
    pending = (async () => {
      const manifest = JSON.parse(await textFile(publication.manifest, run.signal));
      run.check();
      if (manifest?.format_version !== 2 || manifest.revision !== publication.revision ||
          !/^lsg-search-engine-[a-f0-9]{16}\.mjs$/u.test(manifest.engine || '')) fail();
      const engineURL = staticURL(manifest.engine, publication.manifest, publication.origin);
      const engine = await importEngine(engineURL.href);
      run.check();
      const prepared = engine.prepareManifest(manifest, publication.revision);
      const titles = await textFile(staticURL(engine.titlesFile(prepared), publication.manifest, publication.origin).href, run.signal);
      run.check();
      const index = engine.createIndex(prepared, titles);
      cache = Object.freeze({ engine, index, publication });
      return cache;
    })().finally(() => { if (token === generation) pending = null; });
    return pending;
  }
  // Fetch each named file once; concurrent queries share the request.
  function fetchParts(names, add) {
    const { publication } = cache, run = signal();
    return Promise.all(names.map(([key, name, number]) => {
      if (!parts.has(key)) {
        const part = { done: false };
        part.promise = textFile(staticURL(name, publication.manifest, publication.origin).href, run.signal)
          .then(source => { run.check(); add(number, source); part.done = true; })
          .catch(problem => { if (parts.get(key) === part) parts.delete(key); throw problem; });
        parts.set(key, part);
      }
      return parts.get(key).promise;
    })).then(() => run.check());
  }
  /** Load the shards `input` needs into the cached index. */
  function shards(input) {
    const { engine, index } = cache;
    return fetchParts(engine.missingShards(index, input).map(key => ['shard:' + key, engine.shardFile(index.manifest, key), key]),
      (key, source) => engine.addShard(index, key, source));
  }
  /** Load the chunks that hold these block numbers into the cached index. */
  function chunks(blocks) {
    const { engine, index } = cache;
    return fetchParts(engine.missingChunks(index, blocks).map(n => ['chunk:' + n, engine.chunkFile(index.manifest, n), n]),
      (n, source) => engine.addChunk(index, n, source));
  }
  return { setPublication, load, shards, chunks, cancel };
}


// Logseq's groups, in its order. A filter shows one kind with every row.
const GROUPS = Object.freeze({ filters: 'Filters', pages: 'Pages', commands: 'Commands', current: 'Current page', blocks: 'Blocks' });
const FILTERS = Object.freeze([['pages', 'Search only pages'], ['current', 'Search only current page'], ['blocks', 'Search only blocks'], ['commands', 'Search only commands']]);
// The published site's own actions (shell.js), with the keys the shell binds.
const COMMANDS = Object.freeze([
  ['tw', 'Toggle wide mode', 't w'],
  ['tt', 'Toggle between dark/light theme', 't t'],
  ['tl', 'Toggle left sidebar', 't l', '[data-lsg-left-toggle]'],
  ['gh', 'Go to home', 'g h'],
  ['ga', 'Go to all pages', 'g a', '[data-lsg-all-pages]'],
  ['gj', 'Go to journals', 'g j', '[data-lsg-journals-link]'],
]);
const ROWS = 5;
const svg = path => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${path}</svg>`;
const ICONS = Object.freeze({
  page: svg('<path d="M14 3v4a1 1 0 0 0 1 1h4"/><path d="M17 21H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h7l5 5v11a2 2 0 0 1-2 2z"/>'),
  block: svg('<circle cx="12" cy="12" r="3"/>'),
  command: svg('<path d="M7 9a2 2 0 1 1 2-2v10a2 2 0 1 1-2-2h10a2 2 0 1 1-2 2V7a2 2 0 1 1 2 2z"/>'),
  filter: svg('<path d="M4 4h16v2.2a2 2 0 0 1-.6 1.4L15 12v7l-6 2v-8.5L4.5 7.6A2 2 0 0 1 4 6.2z"/>'),
});
// Words as the engine splits them, for commands and filters before the engine loads.
const wordsOf = value => value.toLowerCase().normalize('NFC').match(/[\p{Alphabetic}\p{N}\p{M}]+/gu) || [];
const matchesWords = (label, value) => {
  const wanted = wordsOf(value), have = wordsOf(label);
  return wanted.length > 0 && wanted.every(word => have.some(other => other.startsWith(word)));
};
function wordStarts(label, value) {
  const wanted = wordsOf(value), ranges = [];
  for (const match of label.matchAll(/[\p{Alphabetic}\p{N}\p{M}]+/gu)) {
    const word = match[0].toLowerCase();
    const length = Math.max(0, ...wanted.filter(term => word.startsWith(term)).map(term => term.length));
    if (length) ranges.push([match.index, match.index + length]);
  }
  return ranges;
}
const badge = count => count >= 100 ? '99+' : String(count);

export function installSearch(window, document) {
  if (window.logseqGardenerInitSearch) { window.logseqGardenerInitSearch(); return; }
  const loader = createSearchLoader();
  const apple = /Mac|iPhone|iPad|iPod/u.test(window.navigator?.platform || window.navigator?.userAgent || '');
  const MOD = apple ? '⌘' : 'Ctrl';
  let publication = null, resolvePage = null, dialog = null, input, status, results, body, chip, chipName, retryRow, tip, hint;
  let invoker = null, restore = true, prepared = null, task = 0, timer = null, completion = 0, listed = 0, evaluation = 0, failedLoad = false;
  // Search state: the filter, the expanded groups and the highlighted row's key.
  let filter = null, expanded = new Set(), rows = [], active = null, drawnFor = null, tipChoice = 0;
  const triggerSelector = '[data-lsg-search]';
  const supported = () => typeof window.HTMLDialogElement?.prototype.showModal === 'function';
  const controls = () => [...document.querySelectorAll(triggerSelector)];
  function announce(message, quiet = false) { status.textContent = message; status.classList.toggle('lsg-search-hidden', quiet); }
  function make(tag, attributes = {}, text = '') {
    const node = document.createElement(tag);
    for (const [key, value] of Object.entries(attributes)) node.setAttribute(key, value);
    node.textContent = text;
    return node;
  }
  const keys = (...labels) => { const key = make('kbd'); for (const label of labels) key.append(make('span', {}, label)); return key; };
  // Text with each range wrapped in Logseq's highlight span.
  function marked(text, ranges) {
    const node = make('span');
    let at = 0;
    for (const [start, end] of ranges) {
      if (start > at) node.append(text.slice(at, start));
      node.append(make('span', { class: 'ui__list-item-highlighted-span' }, text.slice(start, end)));
      at = end;
    }
    if (at < text.length) node.append(text.slice(at));
    return node;
  }
  function clearResults() { results.replaceChildren(); rows = []; input.removeAttribute('aria-activedescendant'); hint.hidden = true; }
  function error() {
    clearResults(); prepared = null; failedLoad = true; dialog.setAttribute('data-lsg-search-state', 'error');
    announce('Search data is unavailable or from another publication. Retry, or reload this page.');
    retryRow.hidden = false;
  }
  function close(focus = true) { if (dialog?.open) { restore = focus; dialog.close(); } }
  function createDialog() {
    if (dialog) return;
    dialog = make('dialog', { id: 'lsg-search-dialog', 'aria-label': 'Search' });
    const row = make('div', { class: 'lsg-search-input-row' });
    const label = make('label', { for: 'lsg-search-input', class: 'lsg-search-hidden' }, 'Search pages, blocks and commands');
    input = make('input', { id: 'lsg-search-input', type: 'search', autocomplete: 'off', spellcheck: 'false', maxlength: '512',
      placeholder: 'What are you looking for?', role: 'combobox', 'aria-expanded': 'true', 'aria-autocomplete': 'list',
      'aria-controls': 'lsg-search-results', 'aria-describedby': 'lsg-search-status' });
    row.append(label, input);
    body = make('div', { class: 'lsg-search-body' });
    chip = make('div', { class: 'lsg-search-filter', hidden: '' });
    chipName = make('span');
    const remove = make('button', { type: 'button', 'aria-label': 'Remove filter', 'data-lsg-search-remove-filter': '' }, '×');
    chip.append(make('span', {}, 'Search only:'), chipName, remove);
    status = make('p', { id: 'lsg-search-status', role: 'status', 'aria-live': 'polite', 'aria-atomic': 'true' });
    retryRow = make('div', { class: 'lsg-search-retry', hidden: '' });
    const retry = make('button', { type: 'button' }, 'Retry search');
    const reload = make('button', { type: 'button' }, 'Reload page');
    retry.addEventListener('click', () => { loader.cancel(); prepared = null; void load(); });
    reload.addEventListener('click', () => window.location.reload());
    retryRow.append(retry, reload);
    results = make('div', { id: 'lsg-search-results', role: 'listbox', 'aria-label': 'Search results' });
    body.append(chip, status, retryRow, results);
    const footer = make('div', { class: 'lsg-search-footer' });
    tip = make('div', { class: 'lsg-search-tip' });
    hint = make('button', { type: 'button', class: 'lsg-search-hint', hidden: '' });
    footer.append(tip, hint);
    dialog.append(row, body, footer);
    input.addEventListener('input', () => { expanded = new Set(); window.cancelAnimationFrame(timer); timer = window.requestAnimationFrame(evaluate); });
    dialog.addEventListener('close', () => {
      // A close event queued before a quick reopen belongs to the earlier visit.
      if (dialog.open) return;
      task++; window.cancelAnimationFrame(timer); loader.cancel(); dialog.setAttribute('data-lsg-search-state', 'closed');
      if (restore) (invoker?.isConnected ? invoker : controls()[0])?.focus();
    });
    dialog.addEventListener('click', event => {
      const target = event.target;
      if (target === dialog) {
        const box = dialog.getBoundingClientRect();
        if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) close();
        return;
      }
      const toggle = target.closest?.('[data-lsg-search-toggle]');
      if (toggle) { toggleGroup(toggle.getAttribute('data-lsg-search-toggle')); input.focus(); return; }
      if (target.closest?.('[data-lsg-search-remove-filter]')) { setFilter(null); input.focus(); return; }
      if (target.closest?.('.lsg-search-hint')) { run(current()); return; }
      const option = target.closest?.('.lsg-search-row');
      if (!option) return;
      if (option.tagName === 'A') {
        if (event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey) close(false);
      } else run(rows.find(entry => entry.node === option));
    });
    dialog.addEventListener('pointermove', event => {
      const option = event.target.closest?.('.lsg-search-row');
      if (option && option.id !== active) highlight(rows.find(entry => entry.node === option), false);
    });
    dialog.addEventListener('keydown', event => {
      // Focus can stay in the input until the close event; the page then owns the keys.
      if (!dialog.open) return;
      event.stopPropagation();
      if (event.isComposing || event.keyCode === 229) return;
      const mod = event.metaKey || event.ctrlKey, plain = !mod && !event.altKey && !event.shiftKey;
      if (event.key === 'Escape') {
        event.preventDefault();
        if (input.value) { input.value = ''; expanded = new Set(); input.focus(); evaluate(); }
        else if (filter) setFilter(null);
        else close();
        return;
      }
      if (mod && event.key.toLowerCase() === 'k' && !event.altKey && !event.shiftKey) { event.preventDefault(); input.focus(); input.select(); return; }
      if (mod && !event.altKey && !event.shiftKey && (event.key === 'ArrowDown' || event.key === 'ArrowUp')) {
        const group = current()?.group;
        if (group && !filter) toggleGroup(group, event.key === 'ArrowDown');
        event.preventDefault();
        return;
      }
      const ctrl = event.ctrlKey && !event.metaKey && !event.altKey && !event.shiftKey;
      const step = (plain && event.key === 'ArrowDown') || (ctrl && event.key.toLowerCase() === 'n') ? 1
        : (plain && event.key === 'ArrowUp') || (ctrl && event.key.toLowerCase() === 'p') ? -1 : 0;
      if (step) {
        event.preventDefault();
        if (rows.length) highlight(rows[(rows.indexOf(current()) + step + rows.length) % rows.length]);
        return;
      }
      if (document.activeElement !== input) return;
      if (event.key === 'Enter' && plain) {
        event.preventDefault();
        if (timer) evaluate();
        run(current());
      } else if (event.key === 'Backspace' && !input.value && filter) {
        event.preventDefault();
        setFilter(null);
      }
    });
    document.body.append(dialog);
  }
  const current = () => rows.find(entry => entry.node.id === active);
  function highlight(entry, scroll = true) {
    for (const other of rows) other.node.setAttribute('aria-selected', String(other === entry));
    active = entry?.node.id ?? null;
    if (entry) { input.setAttribute('aria-activedescendant', active); if (scroll) entry.node.scrollIntoView?.({ block: 'nearest' }); }
    else input.removeAttribute('aria-activedescendant');
    // Show more or Show less belongs to the highlighted group.
    for (const button of results.querySelectorAll('.lsg-search-more')) button.hidden = button.getAttribute('data-lsg-search-toggle') !== entry?.group;
    hint.hidden = !entry;
    if (entry) {
      const action = entry.kind === 'command' ? 'Trigger' : entry.kind === 'filter' ? 'Filter' : 'Open';
      hint.replaceChildren(make('span', {}, action), keys('⏎'));
    }
  }
  function drawTip() {
    const line = make('span');
    if (filter) line.append('Type', keys('ESC'), 'to clear search filter');
    else if (tipChoice) line.append(keys(MOD, '↓'), 'to show more results');
    else line.append('Type', keys('/'), 'to filter search results');
    tip.replaceChildren(make('b', {}, 'Tip:'), line);
  }
  function setFilter(kind) {
    filter = kind; expanded = new Set(); input.value = ''; active = null;
    chip.hidden = !kind;
    chipName.textContent = kind ? GROUPS[kind] : '';
    drawTip(); evaluate();
  }
  function toggleGroup(group, open = !expanded.has(group)) {
    if (open === expanded.has(group)) return;
    if (open) expanded.add(group); else expanded.delete(group);
    // Keep the highlight in the group when its hidden rows were highlighted.
    if (!open && current()?.group === group) active = `lsg-search-row-${group}-0`;
    evaluate();
  }
  function run(entry) {
    if (!entry) return;
    if (entry.kind === 'filter') { setFilter(entry.filter); input.focus(); return; }
    if (entry.kind === 'command') { close(); window.logseqGardenerShell?.actions?.[entry.id]?.(); return; }
    entry.node.click();
  }
  function commands() {
    const actions = window.logseqGardenerShell?.actions;
    if (!actions) return [];
    return COMMANDS.filter(([id, , , needs]) => typeof actions[id] === 'function' && (!needs || document.querySelector(needs)) &&
      (id !== 'tt' || window.logseqGardenerTheme)).map(([id, label, shortcut]) => ({ kind: 'command', id, label, shortcut }));
  }
  // The page being viewed: the title in `main > h1`, as hosts swap main.
  function currentPage(index) {
    const title = document.querySelector('main > h1')?.textContent.trim();
    return title ? index.pages.find(page => page.title === title)?.id ?? null : null;
  }
  // `data-lsg-search-drawn` advances when the result list for the input is drawn, block rows
  // whose chunk is still loading showing a placeholder line; `data-lsg-search-complete`
  // advances once every drawn row has its text.
  const drawn = () => results.setAttribute('data-lsg-search-drawn', String(++listed));
  const complete = () => {
    if (prepared) dialog.setAttribute('data-lsg-search-state', 'ready');
    drawn();
    results.setAttribute('data-lsg-search-complete', String(++completion));
  };
  // Builds the groups for the input and filter, fetching the shards a query needs and
  // the chunks of the block rows it shows; it runs again when those arrive.
  function evaluate() {
    window.cancelAnimationFrame(timer); timer = null;
    if (!dialog?.open) return;
    const token = ++evaluation, data = prepared, value = input.value;
    const again = () => { if (token === evaluation && prepared === data) evaluate(); };
    const failed = problem => { if (token === evaluation && prepared === data && dialog.open && problem.name !== 'AbortError') error(); };
    const slash = !filter && value.startsWith('/');
    const text = slash ? '' : value;
    const wants = kind => !filter || filter === kind || (filter === 'blocks' && kind === 'current');
    const groups = [];
    if (slash) {
      const rest = value.slice(1).trim().toLowerCase();
      const items = FILTERS.filter(([kind, label]) => label.toLowerCase().includes(rest) || GROUPS[kind].toLowerCase().includes(rest))
        .map(([kind, label]) => ({ kind: 'filter', filter: kind, label }));
      if (items.length) groups.push({ key: 'filters', count: items.length, items });
    }
    const searching = !!text.trim() && (wants('pages') || wants('current') || wants('blocks'));
    let outcome = null;
    if (searching && data) {
      const { engine, index } = data;
      const withBlocks = wants('current') || wants('blocks');
      if (withBlocks && engine.missingShards(index, text).length) { loader.shards(text).then(again, failed); return; }
      const page = currentPage(index);
      outcome = engine.query(index, text, { currentPage: page, blocks: withBlocks });
      if (outcome.error) { clearResults(); announce('Use up to 256 characters and 16 distinct words.'); complete(); return; }
      if (wants('pages') && outcome.pages.count) groups.push({ key: 'pages', ...outcome.pages, items: outcome.pages.results });
      outcome.blocksFor = { current: wants('current') && page ? outcome.currentPage : null,
        blocks: wants('blocks') ? { count: outcome.blocks.count - outcome.currentPage.count,
          results: outcome.blocks.results.filter(result => result.page !== page) } : null };
    }
    if (!slash && wants('commands')) {
      const items = commands().filter(command => !text.trim() || matchesWords(command.label, text));
      if (items.length) groups.push({ key: 'commands', count: items.length, items });
    }
    for (const key of ['current', 'blocks']) {
      const found = outcome?.blocksFor[key];
      if (found?.count) groups.push({ key, count: found.count, items: found.results });
    }
    for (const group of groups) group.shown = filter || expanded.has(group.key) ? group.items : group.items.slice(0, ROWS);
    const blocks = groups.filter(group => group.key === 'current' || group.key === 'blocks').flatMap(group => group.shown.map(result => result.block));
    const waiting = data && blocks.length ? data.engine.missingChunks(data.index, blocks) : [];
    if (waiting.length) loader.chunks(blocks).then(again, failed);
    draw(groups, value, data);
    if (failedLoad && !data) { error(); return; }
    if (searching && !data) { announce('Loading search…'); return; }
    const total = groups.reduce((sum, group) => sum + group.count, 0);
    announce(!groups.length && value.trim() ? 'No results.' : total ? `${total} results.` : '', groups.length > 0);
    if (waiting.length) drawn(); else complete();
  }
  function draw(groups, value, data) {
    const key = `${filter}\u0000${value}`;
    const keep = drawnFor === key ? active : null;
    drawnFor = key;
    const route = resolvePage || ((_title, href) => new URL(href, publication.manifest).href);
    rows = [];
    const sections = groups.map(group => {
      const section = make('div', { class: 'lsg-search-group', role: 'group', 'aria-labelledby': `lsg-search-group-${group.key}`, 'data-lsg-search-group': group.key });
      const header = make('div', { class: 'lsg-search-group-header' });
      const name = make('button', { type: 'button', id: `lsg-search-group-${group.key}`, class: 'lsg-search-group-name', tabindex: '-1', 'data-lsg-search-toggle': group.key }, GROUPS[group.key]);
      header.append(name, make('span', { class: 'lsg-search-count', 'aria-label': `${group.count} results` }, badge(group.count)));
      if (!filter && group.items.length > ROWS) {
        const open = expanded.has(group.key);
        const more = make('button', { type: 'button', class: 'lsg-search-more', tabindex: '-1', 'data-lsg-search-toggle': group.key, hidden: '' }, open ? 'Show less' : 'Show more');
        more.append(keys(MOD, open ? '↑' : '↓'));
        header.append(more);
      }
      section.append(header);
      group.shown.forEach((item, at) => {
        const entry = row(item, value, data, route, group.key, at);
        rows.push(entry); section.append(entry.node);
      });
      return section;
    });
    results.replaceChildren(...sections);
    highlight(rows.find(entry => entry.node.id === keep) || rows[0], false);
  }
  function row(item, value, data, route, group, at) {
    const id = `lsg-search-row-${group}-${at}`;
    const entry = { kind: item.kind, group, id: item.id, filter: item.filter };
    const icon = make('span', { class: 'lsg-search-icon', 'aria-hidden': 'true' });
    icon.innerHTML = ICONS[item.kind];
    const line = make('div', { class: 'lsg-search-line' });
    const label = make('span', { class: 'lsg-search-label' });
    line.append(icon, label);
    let node;
    if (item.kind === 'command' || item.kind === 'filter') {
      node = make('div', { id, role: 'option', class: 'lsg-search-row', 'aria-selected': 'false' });
      label.append(marked(item.label, wordStarts(item.label, item.kind === 'filter' ? value.slice(1) : value)));
      if (item.kind === 'filter') label.append(make('span', { class: 'lsg-search-note' }, '— Add filter to search'));
      else { const shortcut = make('span', { class: 'lsg-search-keys', 'aria-hidden': 'true' }); shortcut.append(keys(...item.shortcut.split(' '))); line.append(shortcut); }
      node.append(line);
    } else {
      const { engine, index } = data;
      const block = item.kind === 'block' ? engine.blockRow(index, item.block) : null;
      const href = engine.resolveResult(block || { title: item.title, href: item.href || item.page }, route);
      node = make('a', { id, role: 'option', class: 'lsg-search-row', 'aria-selected': 'false', tabindex: '-1', href });
      if (item.kind === 'page') {
        label.append(marked(item.alias || item.title, engine.highlight(item.alias || item.title, value, 'page')));
        if (item.alias) label.append(make('span', { class: 'lsg-search-alias' }, 'alias of'), marked(item.title, engine.highlight(item.title, value, 'block')));
      } else {
        // A breadcrumb of the page and up to three parents above the block text.
        const crumb = make('div', { class: 'lsg-search-crumb' });
        [item.title, ...(block?.parents || [])].forEach((part, step) => {
          if (step) crumb.append(make('span', { class: 'lsg-search-crumb-sep', 'aria-hidden': 'true' }, '›'));
          crumb.append(marked(part, engine.highlight(part, value, 'block')));
        });
        node.append(crumb);
        if (block) { const text = engine.snippet(block.text, value); label.append(marked(text, engine.highlight(text, value, 'block'))); }
        else label.append(make('span', { class: 'lsg-search-placeholder' }, '…'));
      }
      node.append(line);
    }
    node.setAttribute('data-lsg-search-kind', item.kind);
    entry.node = node;
    return entry;
  }
  async function load() {
    const token = ++task;
    retryRow.hidden = true; failedLoad = false;
    dialog.setAttribute('data-lsg-search-state', 'loading'); dialog.setAttribute('aria-busy', 'true');
    evaluate();
    try {
      const data = await loader.load();
      if (token !== task || !dialog.open) return;
      prepared = data; evaluate();
    } catch (problem) {
      if (token === task && dialog.open && problem.name !== 'AbortError') error();
    } finally { if (token === task) dialog.removeAttribute('aria-busy'); }
  }
  // Pointing at or focusing the button starts loading before the dialog opens.
  function prefetch() {
    if (!prepared && publication && supported()) loader.load().catch(() => { /* Opening retries and reports. */ });
  }
  function initialize(_root = document, options = {}) {
    if (Object.hasOwn(options, 'resolvePage')) resolvePage = options.resolvePage;
    let next = null;
    try { next = publicationFromLink(document.head.querySelector('link[rel="lsg-search"]'), document.baseURI, window.location.origin); }
    catch { /* Invalid metadata keeps ordinary navigation usable. */ }
    const changed = loader.setPublication(next);
    publication = next;
    if (changed) { task++; prepared = null; window.cancelAnimationFrame(timer); if (dialog) { clearResults(); close(); } }
    for (const control of controls()) control.hidden = !publication || !supported();
  }
  function open(control) {
    initialize();
    if (!publication || !supported()) return;
    createDialog();
    if (!dialog.open) {
      invoker = control || document.activeElement; restore = true;
      // Each open starts from an empty input, as Logseq's does.
      input.value = ''; filter = null; expanded = new Set(); active = null; drawnFor = null; chip.hidden = true;
      tipChoice = Math.random() < 0.5 ? 0 : 1; drawTip();
      dialog.showModal();
    }
    input.focus(); input.select();
    if (prepared) evaluate(); else void load();
  }
  document.addEventListener('click', event => {
    const control = event.target.closest?.(triggerSelector);
    if (control) { event.preventDefault(); open(control); }
  });
  for (const type of ['pointerover', 'focusin']) {
    document.addEventListener(type, event => { if (event.target.closest?.(triggerSelector)) prefetch(); });
  }
  document.addEventListener('keydown', event => {
    if ((event.metaKey || event.ctrlKey) && !event.altKey && !event.shiftKey && event.key.toLowerCase() === 'k' && !event.isComposing && publication && supported()) {
      event.preventDefault(); open(document.activeElement);
    }
  });
  window.logseqGardenerInitSearch = initialize;
  initialize();
  // The starter installs this module on pointer or focus; start loading at once.
  if (controls().some(control => control === document.activeElement || control.matches(':hover'))) prefetch();
}
