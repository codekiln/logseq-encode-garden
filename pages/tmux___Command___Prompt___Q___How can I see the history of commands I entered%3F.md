logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Option/status-keys]]

- # How can I see the history of commands I entered at the [[tmux/Command/Prompt]]? And what is that prompt called?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [tmux(1), STATUS LINE](https://man.openbsd.org/tmux#show-prompt-history)
		- **Short answer:** `show-prompt-history` (alias `showphist`) prints everything typed at the prompt this server has kept; inside the prompt itself, [[Key/Arrow/Up]] and [[Key/Arrow/Down]] walk the same list. The prompt is called the **command prompt** — `command-prompt` is the command that opens it.
		- ### Seeing the history with [[tmux/Command/show-prompt-history]]
			- `tmux show-prompt-history` displays history for every prompt type. `-T <prompt-type>` narrows it to one of `command`, `search`, `target`, `window-target`.
			- Each prompt type keeps its own list, so a `:` command and a `/` search never mix:
				- ~~~
				  History for command:
				  1: set -g mode-keys vi
				  2: set status-keys vi
				  3: set mouse on
				  History for search:
				  ~~~
			- The newest entry is last, and the numbering restarts per type.
			- `tmux clear-prompt-history` (alias `clearphist`) wipes it, `-T` for a single type.
			- From inside the prompt, [[Key/Arrow/Up]] and [[Key/Arrow/Down]] recall the previous and next entry. Which other editing keys work is set by [[tmux/Option/status-keys]].
		- ### Making it outlive the server
			- Prompt history lives in the running server's memory, so `kill-server`, a reboot, or a crash takes it with them.
			- `history-file` (server option, empty by default) points at a file tmux writes prompt history to on exit and reads back on start. In [[tmux/Config]]:
				- ~~~
				  set -s history-file ~/.tmux_history
				  ~~~
			- `prompt-history-limit` (server option, default `100`) caps entries per prompt type.
			- `history-limit` is unrelated — that one is pane scrollback.
		- ### What the prompt is called
			- The wiki and the man page both call it **the command prompt**: an interactive prompt opened with `Prefix :` that replaces the status line, and the command behind it is `command-prompt`.
			- The man page documents it under **STATUS LINE**, and the sibling commands there name it the **status prompt** — `clear-prompt-history` reads "Clear status prompt history". Same thing; the wording follows where the prompt is drawn.
			- Every prompt in tmux is this one widget with a prompt type attached: copy-mode `/` runs `command-prompt -T search`, `Prefix '` runs `-T window-target`, `Prefix .` runs `-T target`. Prompts bound without `-T` — rename session, rename window, `Prefix f` — fall into the `command` type, so a session name typed at a rename prompt shows up in the `command` history alongside real commands.