- # Meta key
	- The **Meta key** is a modifier key originating from Unix/Lisp-machine keyboards (Sun, Symbolics). Modern systems have no physical Meta key; terminal emulators map it to `Alt`/`Option`.
	- ## macOS mapping
		- **`Option (⌥)`** — the Meta key in terminal emulators (iTerm2, Kitty, Alacritty, WezTerm). Must be configured: in iTerm2, set *Left Option key* → **Esc+**.
		- **`Command (⌘)`** — a macOS-only UI modifier; terminal apps do **not** see it as Meta and most `Cmd+` combos are intercepted by the OS before reaching the terminal.
	- ## Notation
		- | Notation | Meaning |
		  |----------|---------|
		  | `M-x` | Meta+x (press Alt/Option+x, or press Esc then x) |
		  | `ESC x` | Meta+x sent as two keystrokes (fallback when Option isn't forwarded) |
	- ## Related modifier keys
		- **`Super`** — maps to `Command (⌘)` on macOS, `Windows key` on Linux/Windows. Used in GUI window managers (i3, Sway, GNOME) and Emacs (`s-`).
		- **`Hyper`** — a fourth modifier from the same Lisp-machine era; rarely present on modern hardware. Some Emacs users remap a key (e.g. Caps Lock) to Hyper (`H-`).
		- **`Control (Ctrl, C-)`** — standard across all platforms.
		- **`Alt`** — on Linux/Windows, Alt is Meta in terminals. On macOS, `Alt` ≈ `Option` and serves as Meta when configured.
	- ## Where `M-` appears
		- [[tmux]] — `bind-key -T prefix M-1` through `M-7` select pane layouts; requires Option forwarded as Esc+ in the terminal.
		- [[Emacs]] — pervasive `M-x`, `M-f`, `M-b`, etc.
		- Readline / shell — `M-f` (forward word), `M-b` (backward word), `M-.` (insert last argument).
