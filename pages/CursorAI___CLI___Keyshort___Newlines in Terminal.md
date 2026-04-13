- [[Keyshort]] [[CursorAI/CLI]] [[CursorAI/CLI/Keyshort]]
	- **Insert newline in Cursor CLI input (universal / tmux-safe)** #card
	  card-last-interval:: 4.91
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-04-17T05:24:12.697Z
	  card-last-reviewed:: 2026-04-12T08:24:12.697Z
	  card-last-score:: 5
		- Most reliable in all terminals (including tmux, screen, and SSH): `Ctrl+J`, and typing `\` then `Enter` (backslash followed by Enter). See [Terminal Setup | Cursor Docs](https://cursor.com/docs/cli/reference/terminal-setup).
		- In tmux and screen, Shift+Enter and Option+Enter do not reach Cursor CLI; the same doc tells you to use the universal options instead.