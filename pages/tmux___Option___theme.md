logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/status-left-length]], [[Ghostty]]

- ### [`theme`](https://man.openbsd.org/tmux#theme)
	- A [[tmux]] server option, added in tmux 3.8, that decides where the colours named `themeblack`, `themewhite`, `themegreen` and the rest come from. The default is `detect`.
	- The stock `status-style` is `bg=themegreen,fg=themeblack` and the stock `mode-style` is `noattr,bg=themeyellow,fg=themeblack`, so this option decides the colours of the status bar, the session picker and the other built-in modes.
	- ## Values
		- `detect` — the default. Use tmux's own `dark-theme-*` or `light-theme-*` colours, chosen by the theme the client reports. An unknown theme counts as dark.
		- `terminal` — map the theme colours to the terminal's ANSI colours. This is how tmux drew before 3.8.
		- `light` / `dark` — force tmux's light or dark colours.
	- ## [[My Notes]]
		- Measured [[2026/11/24]] on tmux 3.8: [[Ghostty]] running Catppuccin Mocha reported `client_theme` `light`, because macOS was in Light appearance and Ghostty had a single non-conditional `theme`. At `detect` tmux drew its light palette over the dark Mocha background. `terminal` restores Ghostty's palette.
	- ## Usage
		- Set it in [[tmux/Config]]. `-q` lets a tmux older than 3.8, which has no `theme` option, skip the line; an invalid value still reports `unknown value`.
			- ~~~sh
			  set -sq theme terminal
			  ~~~
		- Read the current value, and what an attached client reports:
			- ~~~sh
			  tmux show-options -sv theme
			  tmux list-clients -F '#{client_tty} #{client_theme} #{client_colours}'
			  ~~~
