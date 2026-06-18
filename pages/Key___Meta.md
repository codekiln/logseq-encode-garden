logseq-entity:: [[Logseq/Entity/Key]]
alias:: [[Key/Meta (M-)]], [[Key/Alt]]

- # Meta (M-)
	- Modifier key that in modern terminals maps to `Alt`/`Option`; used pervasively in Emacs, tmux, and readline for single-keystroke commands.
	- ## Larger Context
		- ### Origin
			- The Meta key originated on Unix/Lisp-machine keyboards (Sun, Symbolics). No modern keyboard has a physical Meta key; terminal emulators map it to `Alt` or `Option`.
		- ### macOS mapping
			- **`Option (⌥)`** — the correct Meta key in terminal emulators (iTerm2, Kitty, Alacritty, WezTerm). Requires configuration: in iTerm2, set *Left Option key* → **Esc+**.
			- **`Command (⌘)`** — a macOS-only UI modifier; terminal apps do **not** see it as Meta. Most `Cmd+` combos are intercepted by the OS before reaching the terminal.
		- ### Notation
			- | Notation | Meaning |
			  |----------|---------|
			  | `M-x` | Meta+x (press `Alt`/`Option`+x, or press `Esc` then `x`) |
			  | `ESC x` | Meta+x as two separate keystrokes (fallback when Option isn't forwarded as Esc+) |
		- ### Related modifier keys
			- **[[Key/Super]]** — maps to `Command (⌘)` on macOS, `Windows key` on Linux/Windows. Used in GUI window managers and Emacs (`s-`).
			- **[[Key/Hyper]]** — a fourth modifier from the Lisp-machine era; rarely present on modern hardware. Some Emacs users remap Caps Lock to Hyper (`H-`).
			- **[[Key/Control]]** — standard `Ctrl` modifier across all platforms (`C-`).
			- **[[Key/Alt]]** — on Linux/Windows, Alt is Meta in terminals. On macOS, Alt ≈ Option and serves as Meta when configured.
		- ### Where `M-` appears
			- [[tmux]] — `bind-key -T prefix M-1` through `M-7` select pane layouts.
			- [[Emacs]] — pervasive `M-x`, `M-f`, `M-b`, etc.
			- Readline/shell — `M-f` (forward word), `M-b` (backward word), `M-.` (insert last argument).
