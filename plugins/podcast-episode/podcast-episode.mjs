// lsg first-party plugin podcast-episode: a player that keeps an episode's recording playing
// while the reader moves between pages. The build gives each episode page an entry with
// `recording` (a URL relative to the site root), `title` and `chapters`. On the first episode
// page the module moves that page's inline <audio> into a player outside <main>; on a later
// episode with another recording, a button takes the player over only when the reader starts
// it. The timestamp of each chapter (a heading, or a bullet under `## Chapters`) and each dialogue
// timestamp (`lsg:media-seek`) seek the player, which shows the current chapter and the chapters
// that enclose it, a link to the full recording, and whether the recording is playing. lsg/Ref/First-Party Plugins, in
// logseq-gardener-docs/pages/lsg___Ref___First-Party Plugins.md, documents the plugin.

/** `value` as an absolute URL without its fragment, or null. */
export function recordingURL(value, base) {
  try {
    const url = new URL(value, base);
    url.hash = '';
    return url.href;
  } catch {
    return null;
  }
}

/** `seconds`, kept within the recording when its length is known. */
export function clampTime(seconds, duration) {
  return Number.isFinite(duration) && duration >= 0 ? Math.min(seconds, duration) : seconds;
}

/** The time a `lsg:media-seek` request asks for when it names `source`, otherwise null. */
export function requestedTime(detail, source) {
  const seconds = detail?.seconds;
  if (!Number.isSafeInteger(seconds) || seconds < 0 || typeof detail.source !== 'string') return null;
  return detail.source === source ? seconds : null;
}

/** The entry's chapters that are well formed; a parent must be an earlier chapter. */
export function chaptersOf(value) {
  if (!Array.isArray(value)) return [];
  const chapters = [];
  for (const { anchor, seconds, title, parent } of value) {
    if (typeof anchor !== 'string' || !Number.isSafeInteger(seconds) || seconds < 0) continue;
    chapters.push({
      anchor,
      seconds,
      title: typeof title === 'string' ? title : '',
      parent: Number.isSafeInteger(parent) && parent >= 0 && parent < chapters.length ? parent : null,
    });
  }
  return chapters;
}

/** `seconds` as the player shows a time: `5:15` or `1:02:03`. */
export function formatTime(seconds) {
  const s = Math.max(0, Math.floor(seconds));
  const pad = (n) => String(n).padStart(2, '0');
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60);
  return h ? `${h}:${pad(m)}:${pad(s % 60)}` : `${m}:${pad(s % 60)}`;
}

/** What the player's status says about the recording: `Ended`, `Paused` or `Playing`. */
export function playbackStatus({ ended, paused }) {
  return ended ? 'Ended' : paused ? 'Paused' : 'Playing';
}

/** The index of the chapter playing at `seconds`: the latest start at or before it, the later
 * chapter in page order on a tie, or -1 before the first chapter. */
export function currentChapter(chapters, seconds) {
  let current = -1;
  chapters.forEach((chapter, index) => {
    if (chapter.seconds <= seconds && (current < 0 || chapter.seconds >= chapters[current].seconds)) current = index;
  });
  return current;
}

/** The chapter at `index` and the chapters that enclose it, outermost first. */
export function chapterTrail(chapters, index) {
  const trail = [];
  for (let at = index; at !== null && at >= 0 && at < chapters.length && trail.length < chapters.length; at = chapters[at].parent) {
    trail.unshift(chapters[at]);
  }
  return trail;
}

/** The length of the timestamp that starts `text` when it is `seconds`, otherwise 0. */
export function timestampLength(text, seconds) {
  const match = /^\d{1,2}(?::[0-5]\d){1,2}/.exec(text);
  if (!match) return 0;
  const value = match[0].split(':').reduce((total, part) => total * 60 + Number(part), 0);
  return value === seconds ? match[0].length : 0;
}

/** The episode an adoption describes, or null on a page without this plugin's entry. */
export function episodeOf(adoption, base) {
  const { recording, title, chapters } = adoption.metadata ?? {};
  const source = typeof recording === 'string' ? recordingURL(recording, base) : null;
  if (!source) return null;
  return {
    source,
    title: typeof title === 'string' && title ? title : adoption.page.title,
    url: new URL(adoption.page.url, base).href,
    chapters: chaptersOf(chapters),
  };
}

/** The page's inline <audio> for `source`, outside references and embeds. */
export function inlineAudio(main, source, base) {
  for (const audio of main?.querySelectorAll('audio') ?? []) {
    if (audio.closest('.references, .embed-block, .embed-page')) continue;
    if (recordingURL(audio.getAttribute('src'), base) === source) return audio;
  }
  return null;
}

// A block's bullet sits directly in its item, or in the summary of a collapsed block; the block's
// text follows it, inside a heading element when the block is a heading.
const BULLET = ':scope > .bullet, :scope > details > summary > .bullet';
const HEADING = /^H[1-6]$/;

/** The text node that starts the text of the block whose list item is `item`, or null. */
export function leadingText(item) {
  const after = item?.querySelector(BULLET)?.nextSibling;
  const first = after?.nodeType === 1 && HEADING.test(after.tagName) ? after.firstChild : after;
  return first?.nodeType === 3 ? first : null;
}

export default {
  id: 'podcast-episode',
  apiVersion: 1,
  setup(host) {
    const doc = host.document;
    const base = host.baseURL;
    let region = null, footer = null, audio = null, link = null, full = null, status = null, trail = null;
    let playing = null; // the episode the player holds
    let here = null; // the episode of the page on screen
    let pending = null;
    let offer = null; // the button that starts the page's own episode in the player
    let origin = null; // where the player's <audio> came from, to put it back on cleanup
    let controls = []; // [seek link, the timestamp text it replaced] on the page on screen
    let shown = null; // the chapter trail on display, as `source index`

    const say = (text) => { if (status) status.textContent = text; };
    const applySeek = () => {
      if (pending === null || audio.readyState < 1) return;
      try {
        audio.currentTime = clampTime(pending, audio.duration);
        pending = null;
      } catch {
        say('Unable to seek. Use the recording controls to try again.');
      }
    };
    const play = () => {
      say('');
      // play() runs inside the reader's click, before the recording's metadata exists.
      try {
        Promise.resolve(audio.play()).catch(() => say('Press play in the recording controls to listen.'));
      } catch {
        say('Press play in the recording controls to listen.');
      }
    };
    // The trail changes only when the chapter or the episode does, not on every time update.
    const showChapter = () => {
      const index = currentChapter(playing.chapters, audio.currentTime);
      const key = `${playing.source} ${index}`;
      if (key === shown) return;
      shown = key;
      const chapters = chapterTrail(playing.chapters, index);
      trail.replaceChildren(...chapters.flatMap((chapter, at) => {
        const item = doc.createElement('a');
        item.href = `${playing.url}#${encodeURIComponent(chapter.anchor)}`;
        item.textContent = chapter.title || formatTime(chapter.seconds);
        // The trail ends with the chapter playing now.
        if (at === chapters.length - 1) item.setAttribute('aria-current', 'true');
        if (!at) return [item];
        const separator = doc.createElement('span');
        separator.setAttribute('aria-hidden', 'true');
        separator.textContent = '›';
        return [separator, item];
      }));
    };
    const show = (episode) => {
      playing = episode;
      link.href = episode.url;
      link.textContent = episode.title;
      full.href = episode.source;
      showChapter();
    };
    function build(episode, element) {
      region = host.persistentRegion('player');
      footer = doc.createElement('footer');
      footer.className = 'lsg-episode-player';
      footer.setAttribute('aria-label', 'Episode recording');
      link = doc.createElement('a');
      link.className = 'lsg-episode-player-title';
      status = doc.createElement('span');
      status.className = 'lsg-episode-player-status';
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      // A new tab, as lsg opens external links: loading the recording here would stop the player.
      full = doc.createElement('a');
      full.className = 'lsg-episode-player-recording';
      full.target = '_blank';
      full.rel = 'noopener noreferrer';
      full.textContent = 'Full recording';
      audio = element;
      origin = { parent: element.parentNode, next: element.nextSibling, label: element.getAttribute('aria-label') };
      audio.controls = true;
      audio.setAttribute('aria-label', 'Full episode recording');
      // A relative src would resolve against each later page's address; an unloaded recording
      // can take the absolute URL without interrupting anything.
      if (audio.paused && audio.readyState === 0) audio.setAttribute('src', episode.source);
      audio.addEventListener('loadedmetadata', applySeek);
      audio.addEventListener('durationchange', applySeek);
      audio.addEventListener('error', () => { pending = null; say('The recording could not load.'); });
      audio.addEventListener('timeupdate', () => showChapter());
      for (const name of ['playing', 'pause', 'ended']) audio.addEventListener(name, () => say(playbackStatus(audio)));
      trail = doc.createElement('span');
      trail.className = 'lsg-episode-player-chapter';
      const details = doc.createElement('div');
      details.className = 'lsg-episode-player-details';
      details.append(link, trail, status, full);
      footer.append(details, audio);
      region.element.append(footer);
      doc.body.classList.add('lsg-has-episode-player');
      show(episode);
      if (!audio.paused) say('Playing');
    }
    // Play `episode` from `seconds`; another episode's recording replaces the current one.
    function activate(episode, seconds) {
      if (playing?.source !== episode.source) {
        audio.pause();
        audio.setAttribute('src', episode.source);
        audio.load();
        show(episode);
        offer?.remove();
      }
      pending = seconds;
      applySeek();
      play();
    }
    // Put the page's timestamps back as text.
    const release = () => {
      for (const [control, text] of controls) if (control.isConnected) control.replaceWith(text);
      controls = [];
    };
    // Turn the timestamp that starts each chapter's block into a link that seeks the player.
    function seekControls(episode) {
      for (const chapter of episode.chapters) {
        const first = leadingText(doc.getElementById(chapter.anchor)?.parentElement);
        if (!first) continue;
        const length = timestampLength(first.data, chapter.seconds);
        if (!length) continue;
        const text = length < first.data.length ? (first.splitText(length), first) : first;
        const control = doc.createElement('a');
        control.className = 'lsg-episode-seek';
        control.href = `${episode.source}#t=${chapter.seconds}`;
        control.textContent = text.data;
        control.setAttribute('aria-label', `Play from ${formatTime(chapter.seconds)}`);
        control.addEventListener('click', (event) => {
          if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
          event.preventDefault();
          activate(episode, chapter.seconds);
        });
        text.replaceWith(control);
        controls.push([control, text]);
      }
    }
    // Show the page on screen: its inline recording moves into the player, disappears when the
    // player already holds it, or becomes a button that starts it in the player.
    function adopt(episode) {
      if (!episode) return;
      const element = inlineAudio(host.document.querySelector('main'), episode.source, base);
      if (!element || element === audio) return;
      if (!audio) return build(episode, element);
      const item = element.closest('li');
      if (playing.source === episode.source) {
        element.remove();
      } else {
        offer = doc.createElement('button');
        offer.type = 'button';
        offer.className = 'lsg-episode-play';
        offer.textContent = `Play ${episode.title}`;
        offer.addEventListener('click', () => activate(episode, 0));
        element.replaceWith(offer);
      }
      item?.classList.add('lsg-episode-recording-origin');
    }
    const stop = host.onPageAdopted((adoption) => {
      offer = null;
      controls = [];
      here = episodeOf(adoption, base);
      adopt(here);
      if (here && audio) seekControls(here);
    });
    const seek = (event) => {
      if (!here || !audio || event.defaultPrevented || !event.cancelable) return;
      const seconds = requestedTime(event.detail, here.source);
      if (seconds === null) return;
      event.preventDefault();
      activate(here, seconds);
    };
    doc.addEventListener('lsg:media-seek', seek);
    return () => {
      stop();
      release();
      doc.removeEventListener('lsg:media-seek', seek);
      if (!audio) return;
      audio.pause();
      if (origin.label === null) audio.removeAttribute('aria-label');
      else audio.setAttribute('aria-label', origin.label);
      // The recording returns to its page, so the page works as it does without the plugin.
      if (origin.parent?.isConnected) origin.parent.insertBefore(audio, origin.next?.parentNode === origin.parent ? origin.next : null);
      doc.body.classList.remove('lsg-has-episode-player');
      region.dispose();
    };
  },
};
