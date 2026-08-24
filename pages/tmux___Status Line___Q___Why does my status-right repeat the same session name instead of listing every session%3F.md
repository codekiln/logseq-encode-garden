logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Command/set-option]], [[tmux/Q/How can I query the current value of a tmux option?]]

- # Why does my [[tmux]] status-right repeat the same [[tmux/session]] name instead of listing every session?
	- ## [[AI Answer]]
		- **Short answer:** The right side is not showing four sessions — it is showing one session's name four times, once per live session. The global `status-right` shells out to `tmux list-sessions -F '…'` inside `#()`, and tmux expands `#{…}` across the whole format string **before** handing the command to `/bin/sh`. The `-F` template therefore reaches `list-sessions` already collapsed to the attached client's own session, and `list-sessions` prints that identical string once for every session it finds.
		- ### What the option actually holds
			- ~~~sh
			  tmux show-options -g status-right
			  # status-right "#(tmux list-sessions -F '#{?session_attached,[,}#{session_name}#{?session_attached,],}' | paste -sd' ' -) "
			  ~~~
		- ### The order of operations
			- `status-format[0]` draws the option through `#{T;=/#{status-right-length}:status-right}`, so the option's contents are expanded as a format.
			- That expansion walks the entire string, the text inside `#(…)` included. `#{session_name}` becomes the session of the client drawing the status line, and both `#{?session_attached,[,}` and `#{?session_attached,],}` resolve for that same session — which is where the brackets come from.
			- Only then does `/bin/sh` run what survives: `tmux list-sessions -F '[ls-encode-garden]' | paste -sd' ' -`.
			- `list-sessions` emits its `-F` template once per session, so four sessions produce four identical bracketed names. The number of copies equals `tmux list-sessions | wc -l`; kill a session and one copy disappears.
		- ### Why it started
			- Nothing in `~/.config/tmux/tmux.conf` sets `status-left` or `status-right` — that file only sets terminal features, passthrough, and `update-environment`. No theme, no plugin manager, no `set -ag` line, and no config reload appending to the option.
			- The options were written at runtime with `tmux set -g …` by an ad hoc layout script that stood up an agent workstream for a different repository on this same [[tmux]] server. `set -g` is server-global, so every session on the server inherits it, including sessions started later for unrelated work.
			- That script's other fingerprints are still on the server: `status-left` opens with its two-letter project tag, and `set-titles-string` still names the other project. `~/.config/tmux/tmux.conf` never reverts them, because unset-at-runtime options only return on a new server or an explicit unset.
		- ### Three ways to fix it
			- **Escape the inner hashes** so the shell receives the template rather than its expansion — `##` expands to a literal `#`:
			- ~~~sh
			  tmux set -g status-right "#(tmux list-sessions -F '##{?session_attached,[,}##{session_name}##{?session_attached,],}' | paste -sd' ' -) "
			  ~~~
			- **Drop the subshell.** The `S:` modifier loops a format over every session — no shell, no once-a-second job throttle, no escaping puzzle:
			- ~~~sh
			  tmux set -g status-right "#{S:#{?session_attached,[,}#{session_name}#{?session_attached,],} }"
			  # → [attached-session] other-session third-session
			  ~~~
			- **Restore the defaults**, since these globals were never in the config file:
			- ~~~sh
			  tmux set -gu status-right
			  tmux set -gu status-left
			  ~~~
			- `set -gu` unsets the option back to tmux's built-in default: `status-left` returns to `[#{session_name}] `, `status-right` to the truncated pane title plus clock.
		- ### Verified locally
			- On [[tmux/v/3.7b]], a throwaway server (`tmux -L fmttest`) with three sessions and `status-right` set to `#(tmux list-sessions -F '#{session_name}' | paste -sd, -)` wrote `one,one,one`. The same command with `##{session_name}` wrote `one,three,two`. The `#{S:…}` form rendered `[one] two three`.
		- ### Sources
			- [tmux(1) man page — FORMATS](https://man.openbsd.org/tmux.1#FORMATS) — `##` is replaced by a single `#`; `S:` loops a format over each session; `#()` inserts the last line of a shell command's output; `#{l:…}` marks a string as literal so it is not expanded.
