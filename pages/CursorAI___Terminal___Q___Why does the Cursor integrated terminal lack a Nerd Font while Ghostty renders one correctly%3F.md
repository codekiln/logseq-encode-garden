logseq-entity:: [[Logseq/Entity/Question]]

- # Why does the Cursor integrated terminal lack a Nerd Font while [[Ghostty]] renders one correctly?
	- ## [[AI Answer]]
		- **Short answer:** [[Ghostty]] is explicitly configured to use a Nerd Font (`font-family = JetBrainsMono Nerd Font Mono` in `~/.config/ghostty/config`), while [[CursorAI]]'s `settings.json` has no `terminal.integrated.fontFamily` (or `editor.fontFamily`) override at all, so its integrated terminal falls back to the editor's default monospace font — one without the patched glyph ranges a [[Font/Nerd Font]] provides.
		- [[CursorAI]] is a VS Code fork, and VS Code-based terminals read a dedicated `terminal.integrated.fontFamily` setting (separate from `editor.fontFamily`) to pick the font for the integrated shell panel. When that key is absent, the terminal uses the platform default monospace font rather than any Nerd Font installed system-wide.
		- Fix: add a Nerd Font to `terminal.integrated.fontFamily` in Cursor's `settings.json`, e.g. `"terminal.integrated.fontFamily": "JetBrainsMono Nerd Font Mono"`.
