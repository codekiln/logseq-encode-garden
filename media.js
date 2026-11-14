// Click-to-load video players and YouTube timestamps that seek them.
(() => {
  if (window.lsgMedia) return;
  window.lsgMedia = true;
  const names = { youtube: "YouTube", "youtube-nocookie": "YouTube", loom: "Loom", vimeo: "Vimeo", bilibili: "Bilibili" };
  const youtube = (box) => box.dataset.provider.startsWith("youtube");
  const load = (box, start) => {
    let src = box.dataset.embed;
    const extra = [];
    if (youtube(box)) {
      if (!/[?&]enablejsapi=1/.test(src)) extra.push("enablejsapi=1");
      extra.push("origin=" + encodeURIComponent(location.origin));
    }
    if (box.dataset.provider !== "other") extra.push("autoplay=1");
    if (start != null && youtube(box)) extra.push("start=" + start);
    if (extra.length) src += (src.includes("?") ? "&" : "?") + extra.join("&");
    const frame = document.createElement("iframe");
    frame.src = src;
    frame.title = (names[box.dataset.provider] || "Embedded") + " video";
    frame.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope";
    frame.allowFullscreen = true;
    box.replaceChildren(frame);
    box.dataset.loaded = "";
    return frame;
  };
  const command = (frame, func, args) =>
    frame.contentWindow?.postMessage(JSON.stringify({ event: "command", func, args }), "*");
  document.addEventListener("click", (event) => {
    if (event.defaultPrevented || event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const play = event.target.closest?.(".lsg-video-play");
    if (play) {
      event.preventDefault();
      const box = play.parentElement;
      load(box, box.dataset.start).focus();
      return;
    }
    const anchor = event.target.closest?.("a.youtube-timestamp[data-lsg-video]");
    if (!anchor) return;
    const box = document.querySelector(`.lsg-video[data-lsg-video="${anchor.dataset.lsgVideo}"]`);
    const seconds = Number(anchor.dataset.seconds);
    if (!box) return;
    event.preventDefault();
    const source = anchor.href.replace(/[?&]t=\d+s$/, "");
    const seek = new CustomEvent("lsg:media-seek", { bubbles: true, cancelable: true, detail: { source, seconds, anchor } });
    if (!anchor.dispatchEvent(seek)) return;
    const frame = box.querySelector("iframe");
    if (!frame) return void load(box, seconds);
    command(frame, "seekTo", [seconds, true]);
    command(frame, "playVideo", []);
  });
})();
