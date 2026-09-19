logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Pane/Q/What's the easiest way to get the CWD of a pane?]]

- # What's the easiest way to bind a key that copies a [[tmux/Pane]]'s CWD to the clipboard, or displays it?
	- ## [[AI Answer]]
		- **Short answer:** put a `bind-key` line in `[[.tmux.conf.local]]` that pipes `#{pane_current_path}` through `pbcopy`; chain a `display-message` onto it with `\;` for on-screen confirmation, or use `display-message` alone to just show it.
		- ### Copy silently to the clipboard
			- ~~~
			  bind-key y run-shell "printf '%s' '#{pane_current_path}' | pbcopy"
			  ~~~
			- `run-shell` expands `#{...}` format variables itself before handing the string to `/bin/sh`, so there's no need to nest a `tmux display-message -p` call inside it.
			- Use `printf '%s'`, not `echo -n` — verified live: macOS's `/bin/sh` (bash in POSIX mode) doesn't treat `-n` as a flag there, so `echo -n '...' | pbcopy` copies the literal string `-n /path/...` instead of the path.
		- ### Copy and show a confirmation
			- ~~~
			  bind-key y run-shell "printf '%s' '#{pane_current_path}' | pbcopy" \; display-message "copied #{pane_current_path}"
			  ~~~
			- `\;` chains a second tmux command onto the same binding — confirmed this registers as one atomic binding by loading it via `tmux source-file` and checking `list-keys`. Typing an unescaped `;` straight at a shell prompt to `tmux bind-key ...` does *not* chain the same way, since the shell strips the backslash first and tmux then treats it as two separate top-level commands; this only matters when testing from a shell prompt instead of a config file.
		- ### Just display it, no clipboard
			- ~~~
			  bind-key Y display-message "#{pane_current_path}"
			  ~~~
			- No `run-shell` needed — `display-message` alone already substitutes `#{pane_current_path}` and prints it to the status line for `display-time` milliseconds.
		- Add whichever binding to the managed tmux config and reload with `tmux source-file ~/.config/tmux/tmux.conf`. (Correction: my [[oh-my-tmux]] / `.tmux.conf.local` advice above no longer matches this machine — the dotfiles repo removed oh-my-tmux and manages `~/.config/tmux/tmux.conf` directly via [[chezmoi]] now.)
		- Tracked as a feature request: [codekiln/dotfiles#114](https://github.com/codekiln/dotfiles/issues/114) — pick the actual key and land it in the managed `tmux.conf`.
		- ### Sources
			- [tmux(1) man page — bind-key, run-shell, display-message, PARSING SYNTAX](https://man.openbsd.org/tmux.1)
