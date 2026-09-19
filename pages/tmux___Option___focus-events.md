logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Bug/Vim Right Pane Insert Shows Up in Left Pane]], [[tmux/Pane/Active]]

- ### [`focus-events`](https://man.openbsd.org/tmux#focus-events)
	- A [[tmux]] server option that decides whether the programs running in panes are told when they gain and lose focus. The default is `off`.
	- A program hears about focus only if it asked the terminal to report it, by setting mode `1004`. [[nvim]] asks: it writes `\033[?1004h` at startup and `\033[?1004l` on exit, on NVIM v0.12.5. A shell prompt never asks, so a pane sitting at one receives nothing either way.
	- The events themselves are two escape sequences: `\033[I` on focus in and `\033[O` on focus out.
	- ## Values
		- `on` — ask the terminal for focus reporting and pass the events through to panes.
		- `off` — the default. Panes are never told.
	- ## Moving between panes is a focus change
		- Focus here means the active pane, rather than the terminal window on the desktop. Selecting a different pane sends focus-out to the pane being left and focus-in to the pane being entered, so an editor learns when you step over to the shell beside it and when you come back.
		- Measured [[2026-09-19 Sat]] on tmux 3.7c, with a program holding mode 1004 in one pane: at `on`, selecting away and back delivered `\033[O` then `\033[I`; at `off`, the same two calls delivered nothing; setting it back to `on` restored them.
		- The man page asks for attached clients to be detached and attached again after the option changes. The pane-to-pane events above arrived without that.
	- ## Usage
		- Set it in [[tmux/Config]]:
			- ~~~sh
			  set -s focus-events on
			  ~~~
		- `set -s` and `set -g` are equivalent here: [[tmux]] resolves an option's scope from its name. Measured [[2026-09-19 Sat]] on tmux 3.7c, `set -g focus-events on` leaves it reporting `on` under both `show-options -sv` and `show-options -gv`.
		- Or at runtime with [[tmux/Command/set-option]]:
			- ~~~sh
			  tmux set-option -s focus-events on
			  ~~~
		- Read the current value:
			- ~~~sh
			  tmux show-options -sv focus-events
			  ~~~
	- ## What an editor does with it
		- [[nvim]] fires its `FocusGained` autocommands when a pane becomes active again. [[LazyVim]] runs `checktime` on that event, in [lua/lazyvim/config/autocmds.lua](https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua), so a buffer whose file changed underneath it reloads on the way back in.
		- At `off` that reload waits for a hand-typed `:checktime` or `:e`. That is the difference between the two settings when a formatter, a script, or an agent in a neighbouring pane writes a file the editor has open.
	- ## Off here
		- `~/.config/tmux/tmux.conf` says nothing about it, so the server runs the stock `off` — measured [[2026-09-19 Sat]] on tmux 3.7c, against both the running server and one started with `-f /dev/null`.
		- [[tmux/Bug/Vim Right Pane Insert Shows Up in Left Pane]] ranks focus events first among the suspects for typed input rendering in the wrong pane under iTerm2, and reaches for `set -g focus-events off` as the first thing to try.
