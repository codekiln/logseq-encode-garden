logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Code/Q/Why can't I scroll up in tmux copy mode when Claude Code is in TUI mode?]]

- # Why does piping `claude --help` to [[bat]] break keyboard scrolling while `mise --help` works fine?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** yes, this is a [[Claude/Code]]-specific bug, not a [[bat]] misconfiguration. [[Claude/Code]] enables an enhanced keyboard-input protocol (the kitty keyboard protocol / xterm's `modifyOtherKeys`, aka XTMODKEYS) on the terminal and doesn't always restore it afterward. The piped `--help` text itself carries no escape bytes — the terminal is left in this altered input mode from Claude Code's own terminal setup, so it mangles what `less` (bat's underlying pager) reads back from the keyboard.
		- **Why `j` stops working and `ctrl+j` scrolls with blank lines:**
			- While the enhanced mode is enabled, ordinary keys like `j` are no longer sent to the terminal as the plain byte `j` — they arrive as multi-byte `CSI u` escape sequences instead.
			- `less` doesn't recognize that sequence as its "scroll down" command, so it falls back to treating the bytes as literal input on its colon-style command line — matching the `:jjjjjjj...` shown at the bottom of the screen.
			- `ctrl+j` (linefeed, `0x0A`) partially survives this re-encoding, so it does trigger a scroll, but the surrounding altered escape sequences are what produce the extra blank lines.
			- `mise --help | bat` works because `mise` never touches these terminal keyboard modes, so the terminal stays in normal input state.
		- **Documented in the wild:** [anthropics/claude-code#38761](https://github.com/anthropics/claude-code/issues/38761) ("Terminal left in enhanced keyboard mode after exit — Ctrl-C/Ctrl-D broken") describes exactly this mechanism for Ghostty + tmux and was fixed in Claude Code v2.1.86, but the underlying protocol-restoration problem has recurred since: [#62423](https://github.com/anthropics/claude-code/issues/62423) (legacy XTMODKEYS still sent even when the terminal advertises the kitty protocol) and [#69063](https://github.com/anthropics/claude-code/issues/69063) (extra blank lines while scrolling [[tmux]] scrollback, same Ghostty + tmux setup) are both still open.
		- **Workaround:** run `printf '\e[<u\e[=0u\e[>0m'` (or `reset`) to force the terminal back to normal keyboard mode after the glitch appears. As a standing fix, a `Stop` hook in `~/.claude/settings.json` that runs that `printf` on every Claude Code exit prevents the leak from persisting into the next command.
		- Related: [[Claude/Code/Q/Why can't I scroll up in tmux copy mode when Claude Code is in TUI mode?]] is a different symptom (alternate screen buffer) from the same general family of Claude Code terminal-mode side effects.
