- # How can I refresh `.zshrc` in all of my open panes and windows in [[tmux]]?
	- ## Answer
		- [[AI/Response]]
			- Use `tmux send-keys` to broadcast a `source ~/.zshrc` command to every pane across all sessions:
			- ~~~bash
			  tmux list-panes -a -F '#{pane_id}' | xargs -I{} tmux send-keys -t {} 'source ~/.zshrc' Enter
			  ~~~
				- `-a` lists panes across **all sessions and windows**, not just the current one
				- `-F '#{pane_id}'` outputs each pane's unique ID (e.g. `%0`, `%1`)
				- `send-keys -t {}` targets each pane and types + executes the command
			- Alternatively, using a shell loop for more visibility:
			- ~~~bash
			  for pane in $(tmux list-panes -a -F '#S:#I.#P'); do
			    tmux send-keys -t "$pane" 'source ~/.zshrc' Enter
			  done
			  ~~~
			- **Caveats**
				- This sends keystrokes into whatever is currently running in each pane — if a pane has a long-running process active, the keystrokes will be buffered or misinterpreted
				- Panes running something other than a shell prompt (e.g. `vim`, `python`) will receive the literal text `source ~/.zshrc` — interrupt/exit those first if needed
				- New panes opened after running this will automatically source the updated `.zshrc` since they start fresh shells
			- [tmux send-keys docs](https://man7.org/linux/man-pages/man1/tmux.1.html)
	- ## My Notes
	- ## Related
		- [[tmux]]
