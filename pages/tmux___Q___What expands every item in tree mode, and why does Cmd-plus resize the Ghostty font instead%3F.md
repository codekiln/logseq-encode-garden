logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Mode/Tree]], [[tmux/Command/choose-tree]], [[tmux/session/Picker/Keyshort/Expand all items]], [[Ghostty/Q/Is it possible to quickly increase or decrease the Ghostty font size with a keyboard shortcut?]]

- # What expands every item in [[tmux]] tree mode, and why does Cmd-plus resize the [[Ghostty]] font instead?
	- ## [[AI Answer]]
		- **Short answer:** [[tmux/Mode/Tree]] binds expand-all to `M-+`, and `M-` is [[Key/Meta]] — on [[macOS]] that is `⌥`, never `⌘`. `⌘+` is [[Ghostty]]'s own font-size binding and is swallowed before tmux can see it. Even the right keystroke only opens the tree as deep as it was built, so after [[tmux/Prefix]] `w` it does nothing. Opening the tree with `choose-tree -Z` shows sessions, windows, and panes at once.
		- ### The keystroke that needs nothing configured
			- `C-b :` opens the [[tmux/Command/Prompt]]; type `choose-tree -Z` and press `Enter`.
			- With neither `-s` nor `-w`, [[tmux/Command/choose-tree]] builds the tree down to panes and starts every branch open, so there is nothing left to expand.
			- `⌥⇧=` — `⌥` and the `+` key — is `M-+` and does reach tmux, as long as the tree was opened with [[tmux/Prefix]] `s`.
		- ### Why ⌘+ never arrives
			- `ghostty +list-keybinds` reports `keybind = super++=increase_font_size:1` and `keybind = super+==increase_font_size:1`. [[Ghostty]] acts on those itself and writes nothing to the pty, so tmux is never offered the keystroke.
			- `⌘` is not a terminal modifier at all — see [[Key/Mac/Command]]. Terminal programs receive [[Key/Control]] and [[Key/Meta]], never Command.
			- [[Key/Meta]] on macOS is `⌥`, and only when the terminal is told to send it that way. `macos-option-as-alt = true` in the [[Ghostty]] config makes `⌥⇧=` send `ESC` then `+`, which tmux reads as `M-+`. [[Ghostty]] ships no built-in `alt+` binding for `+` or `=`, so nothing intercepts it on the way through — unlike `alt+arrow_left` and `alt+arrow_right`, which do collide (see [[tmux/Keyshort/Pane/Resize Pane]]).
		- ### How far `M-+` actually reaches
			- | Tree opened with | What `M-+` does |
			  |------------------|-----------------|
			  | `choose-tree -Zs` ([[tmux/Prefix]] `s`) | opens the sessions to show their windows; panes stay hidden |
			  | `choose-tree -Zw` ([[tmux/Prefix]] `w`) | nothing — sessions are already open, and windows never open this way |
			  | `choose-tree -Z` (no `-s`, no `-w`) | the tree is already fully open; `M--` then `M-+` restores it |
			- Pressing `M-+` again does not descend another level; the expansion is bounded by how the tree was built, not by how many times the key is pressed.
			- After [[tmux/Prefix]] `w`, panes are reached one window at a time with `+`, [[Key/Arrow/Right]], or `l`.
		- ### The durable change
			- `bind-key W choose-tree -Z` in the [[tmux/Config]] puts a fully expanded tree on `C-b W`.
			- The tree-mode keys themselves cannot be rebound off [[Key/Meta]]: `tmux list-keys -T choose-tree` answers `table choose-tree doesn't exist`, and [[tmux/list-keys]] shows only the `prefix`, `root`, `copy-mode`, and `copy-mode-vi` tables. Tree-mode keys are compiled in.
			- No [[Ghostty]] change is called for. `macos-option-as-alt = true` is already delivering [[Key/Meta]]; unbinding `super++` would cost font-size control and still would not help, because tmux is waiting on `⌥`, not `⌘`.
		- ### Where the key list comes from
			- `C-h` or `F1` inside tree mode prints the table that [[tmux/session/Picker/Help]] mirrors, and [[tmux/man]] repeats it under `choose-tree`. Both list `M-+` as *Expand all* without qualifying the depth.
		- Behaviour above is [[tmux/v/3.7b]].
