logseq-entity:: [[Logseq/Entity/Software/Option]]

- ### [`pane-border-lines`](https://man.openbsd.org/tmux#pane-border-lines)
	- Selects the characters used to draw pane borders.
	- ## Values
		- `single` — single ACS or UTF-8 lines.
		- `double` — double UTF-8 lines.
		- `heavy` — heavy UTF-8 lines.
		- `simple` — ASCII lines.
		- `number` — pane numbers.
		- `spaces` — space characters.
		- `none` — no border for floating panes.
	- `double` and `heavy` fall back to ACS line drawing when UTF-8 is unavailable.
