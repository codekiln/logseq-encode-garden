// Pure search v2. Import lazily; this module performs no fetch or DOM work. The caller
// fetches the manifest, the title index, the shards a query needs and the chunks of the
// rows it draws, and hands their text to the prepare functions, which check digests.
// Matching and ranking mirror the SDK's search::SearchIndex::query; the shared fixture
// tests/search-fixture.json keeps the two the same.
export const FORMAT_VERSION = 2;
export const LIMITS = Object.freeze({ query: 256, terms: 16, results: 100, snippet: 240, parents: 3 });
// Logseq's fuzzy page score (frontend/search.cljs), shared by All pages and search and
// ported to Rust as search::fuzzy_score: consecutive matches earn more, then a
// length-similarity term, and an exact substring adds 1000. Spaces, brackets, slashes,
// underscores and parentheses are ignored.
const fuzzyClean = (s) => s.toLowerCase().replace(/[[ \\/_\]()]+/g, '');
function fuzzyScore(query, name) {
  const q = fuzzyClean(query);
  const s = fuzzyClean(name);
  let i = 0, mult = 1, total = 0;
  for (let j = 0; j < s.length && i < q.length; j++) {
    if (q[i] === s[j]) {
      total += mult++;
      i++;
    } else mult = 1;
  }
  if (i < q.length) return 0;
  const max = Math.max(q.length, s.length);
  return total + (max ? 1 - (max - Math.min(q.length, s.length)) / max : 1) + (name.includes(query) ? 1000 : 0);
}

export const score = (query, name) => fuzzyScore(query, name);

// Lowercase, NFC and single spaces, as the SDK's search::normalize.
export function normalize(value) {
  return value.toLowerCase().normalize('NFC').split(/\p{White_Space}+/u).filter(Boolean).join(' ');
}
// Runs of letters, digits or marks; the SDK's char::is_alphanumeric or a combining mark.
const WORD = /[\p{Alphabetic}\p{N}\p{M}]+/gu;
export function words(normalized) {
  return normalized.match(WORD) || [];
}
const single = word => [...word].length === 1;

// 64-bit FNV-1a over UTF-8 bytes in four 16-bit limbs: the publisher's content digest.
const encoder = new TextEncoder();
export function digest(text) {
  let h0 = 0x2325, h1 = 0x8422, h2 = 0x9ce4, h3 = 0xcbf2;
  for (const byte of encoder.encode(text)) {
    h0 ^= byte;
    // The prime is 2^40 + 0x1b3: multiply by 0x1b3 and add the value shifted by 40 bits.
    const t0 = h0 * 0x1b3;
    const t1 = h1 * 0x1b3 + (t0 >>> 16);
    const t2 = h2 * 0x1b3 + (h0 << 8) + (t1 >>> 16);
    const t3 = h3 * 0x1b3 + (h1 << 8) + (t2 >>> 16);
    h0 = t0 & 0xffff; h1 = t1 & 0xffff; h2 = t2 & 0xffff; h3 = t3 & 0xffff;
  }
  return [h3, h2, h1, h0].map(h => h.toString(16).padStart(4, '0')).join('');
}

const hex = value => typeof value === 'string' && /^[a-f0-9]{16}$/u.test(value);
const route = value => typeof value === 'string' && /^p-[a-f0-9]{16}\.html$/u.test(value);
const text = value => typeof value === 'string' && value.trim().length > 0;
const count = value => Number.isSafeInteger(value) && value >= 0;
const fragment = /^(?:source-block-\d+|block-[a-f0-9]{8}(?:-[a-f0-9]{4}){3}-[a-f0-9]{12})$/u;
function invalid() { throw new TypeError('Invalid or incompatible search publication; reload the page and retry.'); }
function parse(source, expected) {
  if (typeof source !== 'string' || digest(source) !== expected) invalid();
  let value;
  try { value = JSON.parse(source); } catch { invalid(); }
  if (!value || value.format_version !== FORMAT_VERSION) invalid();
  return value;
}

/** File names, relative to the manifest. */
export const titlesFile = manifest => `lsg-search-titles-${manifest.titles}.json`;
export const shardFile = (manifest, key) => `lsg-search-shard-${manifest.shards.get(key)}.json`;
export const chunkFile = (manifest, number) => `lsg-search-chunk-${manifest.chunks[number]}.json`;

// expectedRevision comes from the page's manifest link, not cached index data.
// Validation establishes publication identity/shape, not cryptographic integrity.
export function prepareManifest(manifest, expectedRevision) {
  if (!manifest || !hex(expectedRevision) || manifest.format_version !== FORMAT_VERSION ||
      manifest.revision !== expectedRevision || !hex(manifest.titles) ||
      !/^lsg-search-engine-[a-f0-9]{16}\.mjs$/u.test(manifest.engine || '') ||
      !count(manifest.blocks) || !Array.isArray(manifest.chunks) || !manifest.chunks.every(hex) ||
      !Array.isArray(manifest.chunk_starts) || manifest.chunk_starts.length !== manifest.chunks.length ||
      !manifest.chunks.length !== !manifest.blocks ||
      !manifest.chunk_starts.every((start, at, starts) => count(start) && start < manifest.blocks && (at ? start > starts[at - 1] : start === 0)) ||
      !manifest.shards || typeof manifest.shards !== 'object' ||
      !Object.entries(manifest.shards).every(([key, value]) => key === normalize(key) && words(key)[0] === key && hex(value))) invalid();
  const shards = new Map(Object.entries(manifest.shards));
  const keys = [...shards.keys()];
  // A terminal shard holds only the word equal to its key: one-character words, and the
  // words left behind when a shard split by its next character.
  const terminal = new Set(keys.filter(key => single(key) || keys.some(other => other.length > key.length && other.startsWith(key))));
  return Object.freeze({ revision: manifest.revision, engine: manifest.engine, titles: manifest.titles,
    blocks: manifest.blocks, chunks: Object.freeze([...manifest.chunks]), chunkStarts: Object.freeze([...manifest.chunk_starts]),
    shards, terminal });
}

/** Validate the title index text and start an index that collects shards and chunks. */
export function createIndex(manifest, titlesSource) {
  const titles = parse(titlesSource, manifest.titles);
  if (!Array.isArray(titles.pages)) invalid();
  const byId = new Map();
  let start = 0;
  const pages = titles.pages.map((record, number) => {
    if (!Array.isArray(record) || !text(record[0]) || !route(record[1]) || byId.has(record[1]) ||
        !Array.isArray(record[2]) || !record[2].every(text) || !count(record[3])) invalid();
    const page = Object.freeze({ number, id: record[1], title: record[0], href: record[1],
      aliases: Object.freeze([...record[2]]), titleKey: normalize(record[0]),
      aliasKeys: Object.freeze(record[2].map(normalize)), start, blocks: record[3] });
    start += record[3];
    byId.set(page.id, page);
    return page;
  });
  if (start !== manifest.blocks) invalid();
  return { manifest, pages: Object.freeze(pages), byId, shards: new Map(), chunks: new Map() };
}

/** The page that holds block `number`; a page's blocks are consecutive records. */
export function pageOf(index, number) {
  let low = 0, high = index.pages.length - 1;
  while (low < high) {
    const middle = (low + high + 1) >> 1;
    if (index.pages[middle].start <= number) low = middle; else high = middle - 1;
  }
  return index.pages[low];
}

/** Validate a shard's text and keep its words with their block numbers. */
export function addShard(index, key, source) {
  const { manifest } = index;
  if (!manifest.shards.has(key)) invalid();
  const shard = parse(source, manifest.shards.get(key));
  if (!Array.isArray(shard.words)) invalid();
  const entries = new Map();
  for (const entry of shard.words) {
    if (!Array.isArray(entry) || typeof entry[0] !== 'string' || words(entry[0])[0] !== entry[0] ||
        !(manifest.terminal.has(key) ? entry[0] === key : entry[0].startsWith(key)) ||
        entries.has(entry[0]) || !Array.isArray(entry[1]) || !entry[1].length) invalid();
    const blocks = new Uint32Array(entry[1].length);
    let previous = 0;
    entry[1].forEach((delta, at) => {
      if (!count(delta) || (at && !delta)) invalid();
      previous += delta;
      if (previous >= manifest.blocks) invalid();
      blocks[at] = previous;
    });
    entries.set(entry[0], blocks);
  }
  index.shards.set(key, entries);
}

/** The number of the chunk that holds block `block`: the last chunk starting at or before it. */
export function chunkOf(manifest, block) {
  const starts = manifest.chunkStarts;
  let low = 0, high = starts.length - 1;
  while (low < high) {
    const middle = (low + high + 1) >> 1;
    if (starts[middle] <= block) low = middle; else high = middle - 1;
  }
  return low;
}

/** Validate a chunk's text and keep its block records. */
export function addChunk(index, number, source) {
  const { manifest } = index;
  if (!Number.isInteger(number) || number < 0 || number >= manifest.chunks.length) invalid();
  const chunk = parse(source, manifest.chunks[number]);
  const first = manifest.chunkStarts[number];
  const end = manifest.chunkStarts[number + 1] ?? manifest.blocks;
  if (!Array.isArray(chunk.blocks) || chunk.blocks.length !== end - first) invalid();
  index.chunks.set(number, Object.freeze(chunk.blocks.map((record, at) => {
    if (!Array.isArray(record) || record[0] !== pageOf(index, first + at).id || !fragment.test(record[1] || '') ||
        !text(record[2]) || !Array.isArray(record[3]) || record[3].length > LIMITS.parents || !record[3].every(text)) invalid();
    return Object.freeze({ fragment: record[1], text: record[2], parents: Object.freeze([...record[3]]) });
  })));
}

function terms(input) {
  if (typeof input !== 'string' || input.length > LIMITS.query * 2 || [...input].length > LIMITS.query || !input.isWellFormed()) {
    return { error: 'invalid-query' };
  }
  const query = normalize(input);
  const unique = [...new Set(words(query))];
  if (unique.length > LIMITS.terms) return { error: 'too-many-terms' };
  return { error: null, query, terms: unique };
}

// A word of two or more characters needs every shard that can hold a word starting with
// it; a one-character word matches only itself, in its own shard.
function shardKeys(manifest, term) {
  if (single(term)) return manifest.shards.has(term) ? [term] : [];
  return [...manifest.shards.keys()].filter(key => key.startsWith(term) || (term.startsWith(key) && !manifest.terminal.has(key)));
}

/** The shard keys a query needs, loaded or not. A query of one-character words needs none. */
export function shardsFor(index, input) {
  const parsed = terms(input);
  if (parsed.error || parsed.terms.every(single)) return [];
  return [...new Set(parsed.terms.flatMap(term => shardKeys(index.manifest, term)))];
}

/** The shard keys a query needs that the index does not hold yet. */
export function missingShards(index, input) {
  return shardsFor(index, input).filter(key => !index.shards.has(key));
}

const empty = () => ({ count: 0, results: [] });
const failure = error => ({ error, pages: empty(), blocks: empty(), currentPage: empty() });
const group = (hits, limit) => ({ count: hits.length, results: hits.slice(0, limit) });

/**
 * Grouped results: Pages, Blocks and, with `currentPage` (a page id), Current page.
 * Each group holds its full count and at most `limit` results. Block results name their
 * block number and page; `blockRow` adds text once its chunk is loaded. With
 * `blocks: false` only Pages is evaluated, so no shard is needed.
 */
export function query(index, input, { limit = LIMITS.results, currentPage = null, blocks = true } = {}) {
  const parsed = terms(input);
  if (parsed.error === 'invalid-query') return failure(parsed.error);
  if (!Number.isInteger(limit) || limit < 1 || limit > LIMITS.results) return failure('invalid-limit');
  if (parsed.error) return failure(parsed.error);
  const { query: normalized, terms: queryTerms } = parsed;
  if (!normalized) return failure(null);
  const pages = [];
  for (const page of index.pages) {
    let best = null;
    const candidates = [[page.titleKey, null], ...page.aliasKeys.map((key, at) => [key, page.aliases[at]])];
    for (const [key, alias] of candidates) {
      const value = fuzzyScore(normalized, key);
      let bucket;
      if (key === normalized) bucket = alias === null ? 0 : 1;
      else if (key.startsWith(normalized)) bucket = 2;
      else if (value > 0) bucket = 3;
      else continue;
      if (!best || bucket < best.bucket || (bucket === best.bucket && value > best.score)) best = { bucket, score: value, alias };
    }
    if (best) pages.push({ ...best, page });
  }
  pages.sort((a, b) => a.bucket - b.bucket || b.score - a.score || a.page.number - b.page.number);
  const outcome = failure(null);
  outcome.pages = group(pages.map(({ page, alias }) => ({ kind: 'page', page: page.id, title: page.title, href: page.href, alias })), limit);
  if (!blocks || queryTerms.every(single)) return outcome;
  if (missingShards(index, input).length) return failure('shards-not-loaded');
  let matched = null;
  const exact = [];
  for (const term of queryTerms) {
    const found = new Set();
    for (const key of shardKeys(index.manifest, term)) {
      for (const [word, blocks] of index.shards.get(key)) {
        if (single(term) ? word === term : word.startsWith(term)) for (const block of blocks) found.add(block);
        if (word === term) exact.push(new Set(blocks));
      }
    }
    matched = matched === null ? found : new Set([...matched].filter(block => found.has(block)));
  }
  const ranked = [...matched].map(block => ({ block, exact: exact.filter(set => set.has(block)).length }))
    .sort((a, b) => b.exact - a.exact || a.block - b.block)
    .map(({ block }) => { const page = pageOf(index, block); return { kind: 'block', block, page: page.id, title: page.title }; });
  outcome.blocks = group(ranked, limit);
  if (currentPage !== null) outcome.currentPage = group(ranked.filter(result => result.page === currentPage), limit);
  return outcome;
}

/** The chunk numbers that hold these block numbers and are not loaded yet. */
export function missingChunks(index, blocks) {
  return [...new Set(blocks.map(block => chunkOf(index.manifest, block)))].filter(number => !index.chunks.has(number));
}

/** A block row with text, breadcrumb parents and destination, or null while its chunk loads. */
export function blockRow(index, block) {
  const number = chunkOf(index.manifest, block);
  const chunk = index.chunks.get(number);
  if (!chunk) return null;
  const record = chunk[block - index.manifest.chunkStarts[number]];
  const page = pageOf(index, block);
  return { kind: 'block', block, page: page.id, title: page.title, href: `${page.href}#${record.fragment}`,
    text: record.text, parents: [...record.parents] };
}

// Ranges of `value` (UTF-16 offsets) whose words start with a query word.
function wordRanges(value, queryTerms) {
  const ranges = [];
  for (const match of value.matchAll(WORD)) {
    const word = match[0];
    const key = word.toLowerCase().normalize('NFC');
    const lengths = queryTerms.filter(term => single(term) ? key === term : key.startsWith(term)).map(term => term.length);
    if (!lengths.length) continue;
    const length = Math.max(...lengths);
    let end = 0;
    for (const piece of word) {
      end += piece.length;
      if (word.slice(0, end).toLowerCase().normalize('NFC').length >= length) break;
    }
    ranges.push([match.index, match.index + end]);
  }
  return ranges;
}

/**
 * Ranges `[start, end)` of `value`, in UTF-16 offsets, to highlight for `input`. Block
 * text marks the start of each word a query word begins; a page title or alias marks
 * the query as a substring, or else its characters in order.
 */
export function highlight(value, input, kind = 'block') {
  const parsed = terms(input);
  if (parsed.error || !parsed.query) return [];
  if (kind === 'block') return wordRanges(value, parsed.terms);
  const lower = value.toLowerCase();
  if (lower.length === value.length) {
    const at = lower.indexOf(parsed.query);
    if (at >= 0) return [[at, at + parsed.query.length]];
  }
  const wanted = [...parsed.query.replace(/[[ \\/_\]()]+/gu, '')];
  const ranges = [];
  let next = 0, offset = 0;
  for (const piece of value) {
    if (next < wanted.length && piece.toLowerCase() === wanted[next]) {
      next++;
      const last = ranges.at(-1);
      if (last && last[1] === offset) last[1] += piece.length; else ranges.push([offset, offset + piece.length]);
    }
    offset += piece.length;
  }
  return next === wanted.length ? ranges : [];
}

// Map the first match through grapheme spans before choosing a display window.
// Windows and ellipses respect whole graphemes, including emoji/combining text.
const segmenter = new Intl.Segmenter('und', { granularity: 'grapheme' });
/** Block text bounded to LIMITS.snippet code points around the first matched word. */
export function snippet(value, input) {
  if ([...value].length <= LIMITS.snippet) return value;
  const parsed = terms(input);
  const graphemes = [...segmenter.segment(value)];
  const first = parsed.error ? undefined : wordRanges(value, parsed.terms)[0];
  const match = first ? first[0] : 0;
  let at = 0;
  while (at < graphemes.length && graphemes[at].index + graphemes[at].segment.length <= match) at++;
  let start = at;
  let context = 0;
  while (start > 0 && context < 60) context += [...graphemes[--start].segment].length;
  const pieces = [];
  let used = start > 0 ? 1 : 0;
  let end = start;
  for (; end < graphemes.length; end++) {
    const piece = graphemes[end].segment;
    const length = [...piece].length;
    const suffix = end < graphemes.length - 1 ? 1 : 0;
    if (used + length + suffix > LIMITS.snippet) break;
    pieces.push(piece);
    used += length;
  }
  return (start ? '…' : '') + pieces.join('') + (end < graphemes.length ? '…' : '');
}

// Hosts keep immutable index routes intact and translate only navigation.
export function resolveResult(result, resolvePage = (_title, href) => href) {
  const [href, hash] = result.href.split('#');
  const adapted = resolvePage(result.title, href);
  if (typeof adapted !== 'string' || !adapted || adapted.includes('#')) {
    throw new TypeError('Search page resolver must return a route without a fragment.');
  }
  return adapted + (hash ? `#${hash}` : '');
}
