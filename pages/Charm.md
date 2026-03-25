logseq-entity:: [[Logseq/Entity/company]]
alias:: [[Charmbracelet]]

- # [Charm](https://charm.land)
	- Company behind the [Charmbracelet](https://github.com/charmbracelet) GitHub org: an OSS ecosystem aimed at making the terminal **modern, expressive, and playful**—strong emphasis on [[TUI]] polish so the CLI does not have to feel like 1970s Unix if you do not want it to.
	- ## Composable stack
		- [Bubble Tea](https://github.com/charmbracelet/bubbletea) — [[TUI]] framework, Elm-style architecture.
		- [Bubbles](https://github.com/charmbracelet/bubbles) — reusable [[TUI]] widgets.
		- [Lip Gloss](https://github.com/charmbracelet/lipgloss) — styling (colors, layout) for [[TUI]]s and CLIs.
		- [[glow]] — [[TUI]] Markdown reader in the terminal.
		- [[Glamour]] — stylesheet-based Markdown rendering for CLI apps (feeds many [[TUI]] experiences).
		- Shell scripting layer — [[gum]]: interactive prompts, menus, and styling **without** writing Go; marketed as the approachable entry point to the same [[TUI]]-flavored ideas as the libraries above.
	- ## Pattern
		- **Libraries** for building [[TUI]]s → **tools** (especially gum) for using those ideas from bash/zsh with small composable commands instead of a full [[TUI]] app.
