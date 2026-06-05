logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]]
see-also:: [[Claude/Code/Q/What is the new TUI mode in Claude Code about?]]

- # Why can't I scroll up in [[tmux]] copy mode when [[Claude/Code]] is in [[TUI]] mode? [[card]]
  card-last-interval:: 5.4
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-06-10T17:52:43.007Z
  card-last-reviewed:: 2026-06-05T08:52:43.008Z
  card-last-score:: 5
	- ## [[My Answer]]
		- inside of claude, use `/tui default` to disable [[Claude Code/TUI]] mode. it was probably at `/tui fullscreen` before.
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** [[Claude/Code]] TUI mode activates the terminal **alternate screen buffer**, which never writes to [[tmux]]'s main scrollback — so copy mode has nothing to scroll through.
		- **How the alternate screen buffer works:**
			- TUI applications (vim, less, htop, Claude Code) activate the alternate screen on entry via the `smcup` terminal capability and restore the original screen via `rmcup` on exit.
			- The alternate screen is a completely separate display area; output written there never flows into [[tmux]]'s main pane scrollback buffer.
			- [[tmux]] copy mode only scrolls through **main pane scrollback**, so it sees nothing rendered during the TUI session.
		- **Workarounds:**
			- `export CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` — disables the alternate screen; the inline/scrollback renderer is used instead and conversation output flows normally into [[tmux]] scrollback.
			- Use Claude Code TUI's built-in navigation: `Page Up`/`Page Down`, arrow keys, and mouse scroll work within the TUI view itself.
		- Sources: [Claude Code — environment variables](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables)