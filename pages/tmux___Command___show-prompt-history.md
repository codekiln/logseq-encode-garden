logseq-entity:: [[Logseq/Entity/CLI/Command]]
see-also:: [[tmux/Command/Prompt]]

- [tmux show-prompt-history](https://man.openbsd.org/tmux#show-prompt-history) [`-T` prompt-type]
	- Display the history of entries typed at the [[tmux/Command/Prompt]], newest last.
	- (alias: `showphist`)
	- Without `-T`, every prompt type is printed in turn, each under a `History for <type>:` heading and numbered from `1`.
		- ~~~
		  History for command:
		  1: set -g mode-keys vi
		  2: set status-keys vi
		  History for search:
		  ~~~
	- `-T` limits output to one type: `command`, `search`, `target`, or `window-target`. Anything else fails with `invalid type: <name>`.
		- The type comes from the `-T` flag on the `command-prompt` invocation that opened the prompt. Prompts bound without `-T` — rename session, rename window, `Prefix f` — land in `command`.
	- History belongs to the server, not a session, and is held in memory. It survives detaching but not `kill-server`, unless the `history-file` server option names a file to save it to.
	- `prompt-history-limit` (server option, default `100`) caps how many entries each type keeps.
	- `clear-prompt-history` (alias `clearphist`) is the counterpart, taking the same `-T`.
	- Documented under **STATUS LINE** in the man page, alongside the other [[tmux/Status Line]] commands, since the prompt is drawn there.
	- Nothing is bound to it by default; run it as `tmux show-prompt-history` from a shell or as `show-prompt-history` from the prompt itself.
	- Context and worked examples: [[tmux/Command/Prompt/Q/How can I see the history of commands I entered?]]
