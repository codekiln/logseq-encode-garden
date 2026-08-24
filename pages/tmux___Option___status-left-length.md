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
	- ## Set to 40 here, at runtime only
		- The value on the running server is `40`, which is what lets a full [[My/AI/Agent/Fleet]] session name like `hayward-2026-08-24` render instead of stopping at `[hayward-2`.
			- ~~~sh
			  tmux show-options -gv status-left-length
			  # 40
			  ~~~
		- **It is not in the config file.** `~/.config/tmux/tmux.conf` sets no status option at all — its stated intention is to keep close to default tmux behavior, and it holds only terminal features, passthrough, and `update-environment`. Checked [[2026/08/24]].
		- So the `40` was written at runtime with `set -g`, the same way [[tmux/Option/status-left]] and [[tmux/Option/status-right]] were on this server — see [[tmux/Status Line/Q/Why does my status-right repeat the same session name instead of listing every session?]].
		- A runtime `set -g` is server-global and outlives every session on that server, but **not the server**. On the next `tmux kill-server`, or the first session after a reboot, the cap returns to `10` and long session names start being cut again, with nothing to announce it.
		- Making it survive means one line in [[tmux/Config]], which is a [[My/Dotfiles]] change rather than a runtime one.
