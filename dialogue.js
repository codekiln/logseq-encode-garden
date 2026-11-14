/** Original dialogue links can delegate playback to a host before inline fallback. */
(() => {
  if (window.logseqGardenerDialogueInstalled) return;
  window.logseqGardenerDialogueInstalled = true;
  const pending = new WeakMap();
  const recordingURL = value => {
    const url = new URL(value, document.baseURI);
    url.hash = '';
    return url.href;
  };
  function seek(audio, seconds) {
    const duration = audio.duration;
    const time = Number.isFinite(duration) && duration >= 0 ? Math.min(seconds, duration) : seconds;
    try { audio.currentTime = time; pending.delete(audio); }
    catch { pending.set(audio, seconds); }
  }
  const initialized = new WeakSet();
  function prepare(audio) {
    if (initialized.has(audio)) return;
    initialized.add(audio);
    audio.addEventListener('loadedmetadata', () => {
      if (pending.has(audio)) seek(audio, pending.get(audio));
    });
    audio.addEventListener('error', () => pending.delete(audio));
  }
  document.addEventListener('click', event => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const anchor = event.target.closest?.('a[data-lsg-dialogue-time]');
    if (!anchor || anchor.hasAttribute('download') || (anchor.target && anchor.target !== '_self')) return;
    const value = anchor.getAttribute('data-lsg-dialogue-time');
    if (!/^\d+$/.test(value || '')) return;
    const seconds = Number(value);
    if (!Number.isSafeInteger(seconds)) return;
    let source;
    try {
      const href = new URL(anchor.getAttribute('href'), document.baseURI);
      if (href.hash !== `#t=${seconds}`) return;
      source = recordingURL(href.href);
    } catch { return; }
    const request = new CustomEvent('lsg:media-seek', {
      bubbles: true, cancelable: true, detail: { source, seconds, anchor },
    });
    if (!anchor.dispatchEvent(request)) { event.preventDefault(); return; }
    const audio = Array.from(document.querySelectorAll('audio[data-lsg-recording]')).find(audio => {
      try { return recordingURL(audio.getAttribute('src')) === source; } catch { return false; }
    });
    if (!audio) return;
    event.preventDefault();
    prepare(audio);
    pending.set(audio, seconds);
    if (audio.readyState > 0) seek(audio, seconds);
    try { audio.play()?.catch?.(() => {}); } catch { /* Native media controls remain available. */ }
  }, true);
})();
