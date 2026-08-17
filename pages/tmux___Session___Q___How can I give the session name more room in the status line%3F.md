logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Option/status-left-length]], [[tmux/Option/status-right]]

- # How can I give the [[tmux/session/Name]] more room in the [[tmux/Status Line]]?
	- ## [[AI Answer]]
		- **Short answer:** raise [[tmux/Option/status-left-length]]. One line in `~/.config/tmux/tmux.conf` ([[tmux/Config]]):
			- ~~~sh
			  set -g status-left-length 40
			  ~~~
		- ### What is doing the cutting
			- [[tmux/Option/status-left]] is `[#{session_name}] `, so a name of N characters wants N + 3 columns.
			- `status-left-length` defaults to `10`, and `status-format[0]` applies it as `#{T;=/#{status-left-length}:status-left}` — keep the first ten characters, discard the rest. The bracket takes one of them, so **nine characters of the session name survive**, and the closing `]` is never reached: `encode-2026-08-17` draws as `[encode-20`.
			- Nothing else is narrowing it. The default `status-left` has no per-cell `=N:` limit inside the format string, so the length cap is the only bound on the name. A per-cell limit would survive any change to the cap.
		- ### What it costs
			- The cap is a maximum, not a reservation: with `status-justify left` the window list starts immediately after whatever the left component actually drew, so the columns come out of the **window list**, and only for sessions whose names are long.
			- | Session name                          | Left component drawn                     | Columns | Beyond the default |
			  |---------------------------------------|------------------------------------------|---------|--------------------|
			  | `gardening`                           | `[gardening] `                           | 12      | 2                  |
			  | `cos-2026-08-17`                      | `[cos-2026-08-17] `                      | 17      | 7                  |
			  | `encode-2026-08-17`                   | `[encode-2026-08-17] `                   | 20      | 10                 |
			  | `mn-kb chief of staff 2026-08-17 mon` | `[mn-kb chief of staff 2026-08-17 mon] ` | 38      | 28                 |
			- Nothing is lost until the three parts together exceed the client width, at which point the window list is what gets the `<` and `>` scroll markers. A six-window session with a 107-column window list and a 39-column right component needs 163 columns at a 17-column left, against 156 at the default cap — so a 191-column terminal has room to spare.
			- The numbers for any given client:
				- ~~~sh
				  tmux display-message -p '#{client_width}'
				  tmux display-message -p '#{w:#{T:status-left}}'
				  tmux display-message -p '#{w:#{T:status-right}}'
				  ~~~
		- ### Where to find more columns
			- Drop the brackets from `status-left` for two more characters of name per session:
				- ~~~sh
				  set -g status-left '#{session_name} '
				  ~~~
			- Take eleven columns off the right end by shortening the pane-title cell in [[tmux/Option/status-right]], then bringing [[tmux/Option/status-right-length]] down to match:
				- ~~~sh
				  set -g status-right '"#{=10:pane_title}" %H:%M %d-%b-%y'
				  set -g status-right-length 30
				  ~~~
			- Shorten the window names when the window list is the part under pressure — each one costs its index, a colon, its name and a flag column, plus a separator.
		- ### Sources
			- [tmux(1) man page — status-left-length, status-right-length, status-justify, FORMATS](https://man.openbsd.org/tmux.1)
