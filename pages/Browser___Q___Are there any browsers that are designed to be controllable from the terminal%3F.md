logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Browsh]], [[Kitty/Graphics/Protocol]]

- # Are there any browsers that are designed to be controllable from the terminal?
	- ## [[AI Answer]]
		- **Short answer:** Yes — not lynx-style text browsers, but real Chromium/Firefox engines that either approximate the page as TTY cells or stream pixels into a terminal that speaks [[Kitty/Graphics/Protocol]]. The latter is what you want for YouTube-class rich media inside a [[TUI]].
		- ### Two families
			- **Cell / block approximation** — a full browser runs headless; the client paints a text-grid stand-in (often Unicode half-blocks). Usable for layout and JS apps, weaker for video fidelity.
				- [[Browsh]] — headless Firefox + extension → interactive TTY (and browser) client. [brow.sh](https://www.brow.sh/) · [browsh-org/browsh](https://github.com/browsh-org/browsh)
				- Carbonyl — Chromium fork that renders natively into the terminal (half-block pixels), with WebGL/audio/video claimed; no window server required. [fathy.fr/carbonyl](https://fathy.fr/carbonyl) · [fathyb/carbonyl](https://github.com/fathyb/carbonyl)
			- **Pixel stream via Kitty graphics** — headless Chromium/Electron frames are drawn as real images in the terminal; mouse/keyboard (and sometimes trackpad) are forwarded back. Needs a compatible emulator ([[Ghostty]], [[Kitty]], [[WezTerm]], and others that implement the protocol).
				- terminal-browser (zenbu-labs) — Electron offscreen Chromium → Kitty pixels; agent-friendly “same tab” workflow; macOS-first with Linux work in progress. [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser)
				- casty — Chrome headless-shell + CDP screencast → Kitty graphics; no X11/VNC. Upstream [sanohiro/casty](https://github.com/sanohiro/casty); [cashmeredev/casty](https://github.com/cashmeredev/casty) adds `--embed` so a host [[TUI]] owns layout and drives navigate/scroll/click over a Unix-socket IPC (used by [kitty-graphics.el](https://github.com/cashmeredev/kitty-graphics.el) for inline browse in terminal Emacs — write-up: [cashmere.rs post](https://cashmere.rs/blog/kitty-graphicsel-v060-video-browser-and-improved-tmux/)).
				- glimpse-tty — active fork of awrit; Chromium in Kitty with mouse/keyboard. [TalAmuyal/glimpse-tty](https://github.com/TalAmuyal/glimpse-tty) (awrit: [chase/awrit](https://github.com/chase/awrit))
				- kitweb — Chrome under Xvfb, FFmpeg x11grab → Kitty frames + audio; Linux-only host, usable over SSH from elsewhere. [wensheng/kitweb](https://github.com/wensheng/kitweb)
		- ### Fit for a custom TUI that embeds pages / video
			- Closest shape today: **casty embed mode** — host positions Kitty image frames and sends JSON IPC commands; the browser does not own the whole terminal. That matches “stay in my TUI, pop open a real page with rich media.”
			- Alternative path: drive [[Browser/Headless]] Chromium yourself (CDP / automation) and paint frames with [[Kitty/Graphics/Protocol]] — same architecture casty uses, more DIY.
			- Standalone pixel browsers (terminal-browser, glimpse-tty, kitweb) are better as the whole pane than as an embeddable widget unless you wrap them.
		- ### Constraints
			- Rich media needs a real engine (Firefox/Chromium family above), not lynx/w3m.
			- Pixel fidelity depends on Kitty-graphics support in the emulator (and often on the multiplexer; tmux historically drops or needs careful setup for graphics protocols).
			- These projects vary a lot in maturity, OS support, and audio reliability — treat embed/TUI integration as experimental unless you own the host like kitty-graphics.el does.
