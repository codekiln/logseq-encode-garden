logseq-entity:: [[Logseq/Entity/Question]]

- # What is the idiomatic way to create a new [[tmux]] session from inside an existing session?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Use the tmux command prompt: `Prefix + :`, type `new-session` (or the alias `new`), press Enter.
			- [[Answer/Official]] from [tmux manual — new-session](https://man7.org/linux/man-pages/man1/tmux.1.html)
			- The two idiomatic paths:
				- 1. **Command prompt (in-tmux):** `Prefix :new-session` — opens a new session and switches to it. Optionally append `-s <name>` to give it a name: `Prefix :new-session -s work`.
				- 2. **Shell (from any pane):** `tmux new-session -d -s <name>` creates a detached session without switching; omit `-d` to switch immediately.
			- The command prompt form is idiomatic because it stays inside tmux and avoids spawning a new terminal. The `:new` short form works identically.
			- To stay in the current session while creating the new one (and switch later with `Prefix s`), add `-d`: `Prefix :new-session -d -s <name>`.
