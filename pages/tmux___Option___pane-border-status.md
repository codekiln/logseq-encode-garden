logseq-entity:: [[Logseq/Entity/Software/Option]]
see-also:: [[tmux/Option/pane-border-format]], [[tmux/Pane/Border]], [[My/AI/Agent/Fleet]]

- ### [`pane-border-status`](https://man.openbsd.org/tmux#pane-border-status)
	- A [[tmux]] window option that controls whether pane-border status lines are shown and where they appear. The default is `off`.
	- It is the option a pane **title** depends on. Titles are set with `select-pane -T` and stored on the pane whatever this option says, but a border status line is the only place [[tmux]] draws them — so at the default `off` the titles are all still set and none of them can be read. Nothing errors and no value is unset, so nothing reports it.
	- Each pane gives up one row of its height to the line. Measured [[2026/08/24]] on [[tmux/v/3.7b]] with a 50-row client: two side-by-side panes are 49 rows tall at `top` and 50 rows tall at `off`.
	- ## Values
		- `off` — hide pane-border status lines. The default.
		- `top` — show a status line along the top border of each pane.
		- `bottom` — show a status line along the bottom border of each pane.
		- `top-floating` — show a top status line only on floating panes.
		- `bottom-floating` — show a bottom status line only on floating panes.
	- ## Usage
		- Set it in [[tmux/Config]]:
			- ~~~sh
			  set -g pane-border-status top
			  ~~~
		- `set -g` and `setw -g` are equivalent here, despite this being a window option: [[tmux]] resolves an option's scope from its name rather than from the flag. Measured [[2026/08/24]] on [[tmux/v/3.7b]], a config containing either spelling leaves the option reporting `top` under both `show-options -gv` and `show-options -gwv`.
		- Or at runtime with [[tmux/Command/set-option/g]]:
			- ~~~sh
			  tmux set-option -g pane-border-status top
			  ~~~
		- Set it for the current window only:
			- ~~~sh
			  tmux set-option -w pane-border-status top
			  ~~~
		- Read the current value with [[tmux/Command/show-options/gv]]:
			- ~~~sh
			  tmux show-options -gv pane-border-status
			  ~~~
		- Turn it off globally:
			- ~~~sh
			  tmux set-option -g pane-border-status off
			  ~~~
	- ## Displayed text
		- [[tmux/Option/pane-border-format]] controls the text in the border status line, and its stock value already renders `"#{pane_title}"` — so turning this option on is enough to make a title readable, with no format to write.
		- Render what a pane's border line will say, without attaching a client:
			- ~~~sh
			  tmux display-message -p -t '<session>:<window>.1' '#{E:pane-border-format}'
			  # #[reverse]1#[default] "Seneschal HUD"
			  ~~~
	- ## Set to `top` here, in the config
		- Every managing seat in [[My/AI/Agent/Fleet]] keeps a titled viewer pane beside its chat pane, so the window tree names both the repository the agent works in and what each pane is for. That whole convention rests on this option: at `off` the names are set and invisible.
		- `top` rather than `bottom` puts each name above the content it names, the way a title bar does. `bottom` would put it below, and for the lowest pane in a window it would sit directly against the client's own [[tmux/Status Line]], stacking two unrelated bars of text. Both spend one row per pane, so nothing is saved by the swap.
		- It began as a runtime `set -g`, which is server-global and outlives every session on that server but **not the server**: on the next `tmux kill-server`, or the first session after a reboot, it would have returned to `off` and every pane title in the fleet would have stopped being readable.
		- **It is now in the config file.** [[2026/08/24]], `set -g pane-border-status top` was added to the chezmoi source for `~/.config/tmux/tmux.conf` with a comment giving the reason — [[My/Dotfiles]] change `track-tmux-pane-border-status`, the companion to `track-tmux-status-left-length` found the same morning.
			- ~~~sh
			  tmux -L pbstest -f ~/.config/tmux/tmux.conf new-session -d -s hayward-2026-08-24
			  tmux -L pbstest split-window -h -t hayward-2026-08-24
			  tmux -L pbstest select-pane -t 'hayward-2026-08-24:0.1' -T 'Seneschal HUD'
			  tmux -L pbstest show-options -gv pane-border-status              # top
			  tmux -L pbstest display-message -p -t 'hayward-2026-08-24:0.1' '#{E:pane-border-format}'
			  # #[reverse]1#[default] "Seneschal HUD"
			  tmux -L pbstest kill-server
			  ~~~
			- An isolated socket is the way to check this while a fleet is attached — `kill-server` on the default socket would take every seat's session down with it.
		- The negative control is the instructive half. On a server started with `-f /dev/null`, the same `select-pane -T` call succeeds, `list-panes` still reports `1=Seneschal HUD`, and there is simply no border status line in which to read it. Attaching a client to each in turn and capturing the top row shows it plainly: the configured server draws `──0 "Seneschal chat"───┬──1 "Seneschal HUD"───`, and the unconfigured one draws nothing there at all — the shell content starts on row one.
	- ## The neighbouring border options are not in the config
		- Measured [[2026/08/24]] on [[tmux/v/3.7b]] against a `-f /dev/null` server, [[tmux/Option/pane-border-format]] and [[tmux/Option/pane-border-style]] on the running server are identical to stock, while three depart from it: [[tmux/Option/pane-border-indicators]] is `both` against a stock `colour`, [[tmux/Option/pane-border-lines]] is `double` against a stock `single`, and [[tmux/Option/pane-active-border-style]] is `fg=colour46,bold` against a stock expression that colours by pane mode.
		- Those three are residue of the retired [[oh-my-tmux]] layer — `set -g pane-border-indicators both` appears verbatim in its `tmux.conf.local` in the dotfiles' history — and they are deliberately **not** tracked. They are about how the border looks rather than whether it carries a name, so letting them fall back to stock on the next server start is the intended outcome.
	- ## Related
		- [[tmux/Keyshort/Pane/Show Pane Titles]]
