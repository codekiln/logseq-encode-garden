logseq-entity:: [[Logseq/Entity/Question]]
- # How can the [[Codex/CLI]] conversation name become the [[tmux]] pane title?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Codex Configuration Reference](https://developers.openai.com/codex/config-reference/), [Codex developer commands](https://developers.openai.com/codex/cli/slash-commands/), and [tmux(1)](https://man.openbsd.org/tmux.1):
			- **Short answer:** Add the `thread` item to Codex's terminal title in `$CODEX_HOME/config.toml` (normally `~/.codex/config.toml`):
				- ~~~toml
				  [tui]
				  terminal_title = ["thread"]
				  ~~~
			- Restart Codex, then name the chat with `/rename <name>`. Codex writes that chat name as the terminal title. tmux receives the same `OSC 2` title sequence and stores it as the pane's `pane_title`, which appears on the pane row when the [[tmux/session/Picker]] tree is expanded.
			- Check the result after suspending or exiting Codex in that pane with:
				- ~~~bash
				  tmux display-message -p -t "$TMUX_PANE" '#{pane_title}'
				  ~~~
			- **The resume-picker label has two possible sources.** [Codex's resume-picker source](https://github.com/openai/codex/blob/main/codex-rs/tui/src/resume_picker.rs) displays the saved chat name when one exists and otherwise falls back to the session preview, usually the first prompt. The `thread` terminal-title item displays the saved name when one exists and otherwise falls back to the thread UUID. Therefore `terminal_title = ["thread"]` matches named chats; it does not copy the preview text of an unnamed chat.
			- To mirror the unnamed fallback too, a small [[Codex/Hook]] helper can run on `SessionStart` and `Stop`: use the hook's `session_id` with App Server `thread/read`, choose `thread.name` or `thread.preview`, then run `tmux select-pane -t "$TMUX_PANE" -T "$label"`. [Codex App Server](https://developers.openai.com/codex/app-server/) exposes both fields, and [Codex Hooks](https://developers.openai.com/codex/hooks/) supplies the session ID. Using `/rename` keeps the setup to the native Codex option above.
			- `allow-rename` is unrelated: tmux uses it for a program changing the **window name**. `OSC 2` and `select-pane -T` set the **pane title**.
