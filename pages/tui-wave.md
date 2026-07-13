logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Amos Troitski]]
via:: [tui-wave: a terminal audio editor (r/tui)](https://www.reddit.com/r/tui/comments/1ujq3qc/tuiwave_a_terminal_audio_editor/)
tags:: [[Rust]]

- # [tui-wave](https://github.com/biomassa/tui-wave)
	- [[GitHub/Star]]: 23 (checked 2026-07-12).
	- Keyboard-driven terminal audio editor for Linux, macOS, and Windows (mouse works too). Opens WAV files and shows a zoomable waveform you can navigate, play, and edit: selection, cut/copy/paste, undo/redo, normalize, gain, fades, reverse, trim, resample, mix-to-mono, and timeline markers with transient detection. Saves back to 16-bit, 24-bit, or 32-bit-float WAV and preserves BWF cue points across the round trip.
	- Renders the waveform as an inline image in the terminal via graphics protocols ([[Kitty/Graphics/Protocol]], Sixel, and iTerm2).
	- Optionally acts as a front-end to the Composer's Desktop Project (CDP), a decades-old suite of external command-line sound-transformation tools (spectral blurring, granulation, morphing, time-stretching), with a parameter form, breakpoint-envelope automation, preview, and full undo. CDP is not bundled.
	- Developed with LLM assistance by an author who works with audio rather than as a Rust developer, built to serve their own workflow.