tags:: [[Claude Code]], [[Q]]
alias:: [[Anthropic/App/Claude Code/Q/How can I fix dark text on a dark background in the terminal]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude Code/Settings]]

- # How can I fix dark text on a dark background in the [[Claude Code]] terminal?
	- ## Answer
		- [[AI/Response]]
			- **Match the built-in theme to your terminal:** Run `/theme` in a session, or open the theme picker from `/config`, and pick a preset that fits a dark terminal. The **auto** option tries to detect whether the terminal background is light or dark so the UI tracks the terminal. Claude Code does not change the terminal emulator’s own palette; it only maps its TUI colors onto what the terminal reports. Official reference: [Configure your terminal for Claude Code — Match the color theme](https://code.claude.com/docs/en/terminal-config#match-the-color-theme).
			- **If presets still look wrong:** Some users hit TUI color bugs (for example unreadable or inverted colors on certain terminals or versions). Updating Claude Code (or trying the **stable** update channel in `/config`) is the first practical check; search or follow upstream issues such as [anthropics/claude-code#40795](https://github.com/anthropics/claude-code/issues/40795) (closed as duplicate of broader dark-mode color threads) for similar reports.
			- **Fine-tune with a custom theme (v2.1.118+):** In `/theme`, choose **New custom theme…** to edit tokens with a live preview, or add JSON under `~/.claude/themes/`. Start from a **base** like `dark` or `dark-ansi`, then set **overrides** for readability—for example raise contrast on **default foreground** and secondary text via the `text`, `inactive`, and `subtle` tokens (documented in the same terminal-config section under **Color token reference**). Files in that directory are watched and reload without restarting the CLI.
			- **Also verify the host terminal:** Mis-set ANSI bright/black colors, tmux without passthrough, or a light-theme terminal while Claude Code thinks the background is dark can all produce “dark on dark.” Aligning the terminal profile with OS appearance, or toggling truecolor vs ANSI-only in the terminal, often narrows the problem before custom overrides.
