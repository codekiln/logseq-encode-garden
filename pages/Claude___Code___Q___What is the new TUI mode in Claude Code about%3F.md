logseq-entity:: [[Logseq/Entity/question]]

- # What is the new TUI mode in [[Claude/Code]] about?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** TUI mode is a fullscreen alternate-screen renderer that displays Claude Code conversations in a dedicated terminal view, separate from native terminal scrollback. It shipped in v2.1.110 (April 2026) and has since become the default renderer.
		- **How to use it:**
			- Run `/tui fullscreen` within a session to switch to the renderer mid-conversation, no restart needed.
			- A `tui` setting can set the default for all new sessions.
			- To opt out and stay in inline/scrollback mode: `export CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1`
		- **Key features:**
			- Flicker-free rendering — draws into a separate alternate screen buffer instead of streaming into terminal scrollback
			- Lower memory usage than the inline renderer on long sessions
			- Mouse support: scroll and click links with the mouse
			- Keyboard navigation: arrow keys, Page Up/Down, Home/End
			- Clickable hyperlinks rendered in the conversation
			- Auto-follows new messages; a "jump to bottom" pill appears when scrolled up
		- **What problem it solves:** The old inline renderer appended each turn into terminal scrollback, which caused visible flicker on large sessions and held all output in memory. The alternate-screen renderer keeps conversation output in a managed buffer — cleaner display, lower overhead — at the cost of not being in normal terminal scrollback (where you'd need `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` to recover that behavior).
		- Sources: [Claude Code Changelog](https://code.claude.com/docs/en/changelog) · [Claude Code v2.1.110 release — ClaudeWorld](https://claude-world.com/articles/claude-code-21110-release/)
