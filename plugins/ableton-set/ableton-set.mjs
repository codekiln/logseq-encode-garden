// lsg first-party plugin ableton-set (logseq-gardener-docs/pages/lsg___Ref___First-Party Plugins.md): an
// Ableton Live Set page as a track view. The entry holds `title`, the Set's `live-version`,
// `tempo` and `time-signature`, and `tracks`; a track holds `title`, `url`, its settings as
// written, `arm` as a boolean, `devices` in chain order, and `tracks` when it is a group. A
// routing value that names another track's page is `{ title, url, detail }`.
const TYPES = { audio: 'Audio', midi: 'MIDI', return: 'Return', group: 'Group' };
// [key, label] in the order Live's In/Out section shows them.
const ROUTING = [
  ['audio-from', 'Audio from'],
  ['midi-from', 'MIDI from'],
  ['midi-channel', 'MIDI channel'],
  ['monitor', 'Monitor'],
  ['audio-to', 'Audio to'],
  ['midi-to', 'MIDI to'],
];
const MONITOR = ['In', 'Auto', 'Off'];
// A group may hold groups; the build reads no deeper.
const MAX_DEPTH = 8;

const text = (value) => (typeof value === 'string' ? value.trim() : '');

/** `url` on the site's origin, or `null`. */
function siteLink(url, base) {
  try {
    const href = new URL(text(url), base);
    return text(url) && href.origin === new URL(base).origin ? href.href : null;
  } catch {
    return null;
  }
}

/**
 * One setting as a row, `{ key, label, value, href }`, or nothing when the track does not state
 * it. A routing that names another track's page gives that track's title as `value`, its page
 * on this site as `href` and the rest of the setting as `detail`.
 */
function settingRow(key, label, setting, base) {
  if (text(setting)) return [{ key, label, value: text(setting), href: null }];
  const title = text(setting?.title);
  if (!title) return [];
  const row = { key, label, value: title, href: siteLink(setting.url, base) };
  if (text(setting.detail)) row.detail = text(setting.detail);
  return [row];
}

/** The tracks of `list` that have a title: `{ title, href, type, kind, rows, arm, devices, tracks }`. */
function trackList(list, base, depth) {
  if (!Array.isArray(list) || depth > MAX_DEPTH) return [];
  return list.flatMap((track) => {
    const title = text(track?.title);
    if (!title) return [];
    const group = Array.isArray(track.tracks);
    const written = text(track.type);
    const kind = Object.hasOwn(TYPES, written.toLowerCase()) ? written.toLowerCase() : group ? 'group' : '';
    return [{
      title,
      href: siteLink(track.url, base),
      // The type as Live names it; a type the plugin does not know stays as written.
      type: TYPES[kind] ?? written,
      kind,
      rows: ROUTING.flatMap(([key, label]) => settingRow(key, label, track[key], base)),
      arm: typeof track.arm === 'boolean' ? track.arm : null,
      devices: Array.isArray(track.devices) ? track.devices.map(text).filter(Boolean) : [],
      tracks: group ? trackList(track.tracks, base, depth + 1) : null,
    }];
  });
}

/** The entry as the view draws it, `{ title, facts, tracks }`, or `null` when it names no track. */
export function setView(metadata, base) {
  const tracks = trackList(metadata?.tracks, base, 0);
  if (!tracks.length) return null;
  const facts = [
    text(metadata['live-version']) && `Live ${text(metadata['live-version'])}`,
    text(metadata.tempo) && `${text(metadata.tempo)} BPM`,
    text(metadata['time-signature']),
  ].filter(Boolean);
  return { title: text(metadata.title), facts, tracks };
}

/** How many tracks `tracks` hold, counting each group and the tracks inside it, as Live numbers them. */
export function trackCount(tracks) {
  return tracks.reduce((count, track) => count + 1 + (track.tracks ? trackCount(track.tracks) : 0), 0);
}

function element(doc, tag, className, content) {
  const node = doc.createElement(tag);
  if (className) node.className = className;
  if (content !== undefined) node.textContent = content;
  return node;
}

function drawTrack(doc, track) {
  const item = element(doc, 'li', track.tracks ? 'lsg-as-group' : 'lsg-as-track');
  if (track.kind) item.dataset.type = track.kind;
  const head = element(doc, 'div', 'lsg-as-head');
  const name = element(doc, track.href ? 'a' : 'span', 'lsg-as-name', track.title);
  if (track.href) name.setAttribute('href', track.href);
  head.append(name);
  if (track.type) head.append(element(doc, 'span', 'lsg-as-type', track.type));
  item.append(head);
  if (track.rows.length || track.arm !== null) {
    const settings = element(doc, 'dl', 'lsg-as-settings');
    for (const row of track.rows) {
      const value = element(doc, 'dd');
      const state = row.key === 'monitor' && MONITOR.find((option) => option.toLowerCase() === row.value.toLowerCase());
      if (state) {
        // Live's three monitor buttons, with the chosen one marked; a screen reader hears it alone.
        value.className = 'lsg-as-monitor';
        for (const option of MONITOR) {
          const button = element(doc, option === state ? 'strong' : 'span', '', option);
          if (option !== state) button.setAttribute('aria-hidden', 'true');
          value.append(button);
        }
      } else if (row.href) {
        // A routing to another track of the Set: its name as a link, then Live's second box.
        const target = element(doc, 'a', 'lsg-as-target', row.value);
        target.setAttribute('href', row.href);
        value.append(target, row.detail ? ` ${row.detail}` : '');
      } else {
        value.textContent = [row.value, row.detail].filter(Boolean).join(' ');
      }
      settings.append(element(doc, 'dt', '', row.label), value);
    }
    if (track.arm !== null) {
      const value = element(doc, 'dd', track.arm ? 'lsg-as-arm lsg-as-armed' : 'lsg-as-arm', track.arm ? 'Armed' : 'Off');
      settings.append(element(doc, 'dt', '', 'Arm'), value);
    }
    item.append(settings);
  }
  if (track.devices.length) {
    item.append(element(doc, 'p', 'lsg-as-label', 'Devices'));
    const chain = element(doc, 'ol', 'lsg-as-devices');
    for (const device of track.devices) chain.append(element(doc, 'li', '', device));
    item.append(chain);
  }
  if (track.tracks) item.append(drawTracks(doc, track.tracks));
  return item;
}

function drawTracks(doc, tracks) {
  const list = element(doc, 'ol', 'lsg-as-tracks');
  for (const track of tracks) list.append(drawTrack(doc, track));
  return list;
}

/** The track view of `view`, a `<section>` to put above the page's outline. */
export function drawSet(doc, view) {
  const section = element(doc, 'section', 'lsg-ableton-set');
  section.setAttribute('aria-label', view.title ? `Track view of ${view.title}` : 'Track view');
  const count = trackCount(view.tracks);
  const caption = element(doc, 'p', 'lsg-as-caption');
  caption.append(element(doc, 'strong', '', 'Track view'), ` · ${[...view.facts, `${count} ${count === 1 ? 'track' : 'tracks'}`].join(' · ')}`);
  const scroller = element(doc, 'div', 'lsg-as-scroll');
  scroller.append(drawTracks(doc, view.tracks));
  section.append(caption, scroller);
  return section;
}

export default {
  id: 'ableton-set',
  apiVersion: 1,
  setup(host) {
    let shown = null;
    // A page without an entry gets `{}` and no view. The host replaces `<main>` on navigation,
    // so the view of the page before goes with it.
    const stop = host.onPageAdopted(({ main, metadata }) => {
      shown?.remove();
      const view = setView(metadata, host.baseURL);
      shown = view && main ? drawSet(host.document, view) : null;
      if (!shown) return;
      const outline = main.querySelector('.outline');
      if (outline) outline.before(shown);
      else main.append(shown);
    });
    return () => {
      stop();
      shown?.remove();
    };
  },
};
