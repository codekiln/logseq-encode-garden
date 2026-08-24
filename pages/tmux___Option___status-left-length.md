logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/status-left]], [[My/AI/Agent/Fleet]]

- ### [`status-left-length`](https://man.openbsd.org/tmux#status-left-length)
	- A [[tmux]] session option setting the maximum width, in columns, of the left component of the [[tmux/Status Line]]. The default is `10`.
	- It caps rather than reserves. A left component narrower than the cap draws at its own width and the window list begins immediately after it, so raising the cap spends columns only on the sessions whose names need them.
	- Under the default [[tmux/Option/status-left]] of `[#{session_name}] `, the opening bracket takes the first column, so the cap admits `status-left-length - 1` characters of the [[tmux/session/Name]] — nine at the default `10`.
	- ## Usage
		- Raise it in [[tmux/Config]]:
			- ~~~sh
			  set -g status-left-length 40
			  ~~~
		- Or at runtime with [[tmux/Command/set-option/g]]:
			- ~~~sh
			  tmux set-option -g status-left-length 40
			  ~~~
		- Read the current value with [[tmux/Command/show-options/gv]]:
			- ~~~sh
			  tmux show-options -gv status-left-length
			  ~~~
		- Render the left component exactly as the status line draws it, cap and all:
			- ~~~sh
			  tmux display-message -p '#{T;=/#{status-left-length}:status-left}'
			  ~~~
	- ## How the cut is made
		- `status-format[0]` applies the cap as `#{T;=/#{status-left-length}:status-left}`. The `=N` format modifier keeps the first N characters and discards the rest.
		- `=N` takes an optional marker as a second argument — `#{=/9/…:session_name}` appends `…` when it trims. The stock `status-format` supplies none, so a truncated left component stops mid-word with nothing to mark the cut: at the default cap, the session name `encode-2026-08-17` draws as `[encode-20`, and the closing `]` is never reached.
	- ## Set to 40 here, in the config
		- `40` is what lets a full [[My/AI/Agent/Fleet]] session name like `hayward-2026-08-24` render instead of stopping at `[hayward-2`.
			- ~~~sh
			  tmux show-options -gv status-left-length
			  # 40
			  ~~~
		- It began as a runtime `set -g`, the same way [[tmux/Option/status-left]] and [[tmux/Option/status-right]] were on this server — see [[tmux/Status Line/Q/Why does my status-right repeat the same session name instead of listing every session?]]. A runtime `set -g` is server-global and outlives every session on that server, but **not the server**: on the next `tmux kill-server`, or the first session after a reboot, the cap would have returned to `10` and long session names would have started being cut again, with nothing to announce it.
		- **It is now in the config file.** [[2026/08/24]], `set -g status-left-length 40` was added to the chezmoi source for `~/.config/tmux/tmux.conf` with a comment giving the reason — [[My/Dotfiles]] change `track-tmux-status-left-length`. A server started from that file reports `40` with no runtime `set -g` issued to it; the same probe against `-f /dev/null` reports `10` and renders `[hayward-2`.
			- ~~~sh
			  tmux -L slltest -f ~/.config/tmux/tmux.conf new-session -d -s hayward-2026-08-24
			  tmux -L slltest show-options -gv status-left-length            # 40
			  tmux -L slltest display-message -p '#{T;=/#{status-left-length}:status-left}'
			  # [hayward-2026-08-24]
			  tmux -L slltest kill-server
			  ~~~
			- An isolated socket is the way to check this while a fleet is attached — `kill-server` on the default socket would take every seat's session down with it.
		- The neighbouring status options are **not** in the config, and do not need to be. Measured [[2026/08/24]] on [[tmux/v/3.7b]] against a `-f /dev/null` server, [[tmux/Option/status-left]], [[tmux/Option/status-right]], [[tmux/Option/status-right-length]], `status-style` and `status-interval` on the running server are identical to stock — the `set -gu` restore proposed on the status-right question page has been applied. `status-left-length` was the only status option left departing from stock.
