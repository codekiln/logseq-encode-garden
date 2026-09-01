# [dlvhdr/gh-dash: A beautiful CLI dashboard for GitHub](https://github.com/dlvhdr/gh-dash)
tags:: [[GitHub/CLI/Extension]], [[CLI/Tool]], [[Go]], [[Charm]]

- [[GitHub/CLI]] extension written in [[Go]] on [[Charm]]'s Bubble Tea, showing pull requests, issues and notifications as filterable sections in the terminal. Each section is a GitHub search filter.
	- ## Features
		- 📋 Sections — pull requests and issues grouped by search filter, one tab per section
		- 🔍 Search — any GitHub search syntax works as a section's filter
		- ⚡ Actions from the dashboard — check out, comment, approve, merge, without leaving the terminal
		- 👀 Diff view — reads through the configured pager
		- 🎨 Themable — colors, layout, and keybindings are all configurable
	- ## Why it is installed here
		- Pull request triage in the terminal instead of a browser tab per PR. The default screen is *My Pull Requests*, *Needs My Review* and *Involved*, which is the triage it was adopted for.
		- Declared in the dotfiles at `chezmoi/dot_config/gh/extensions.txt` — see [[GitHub/CLI/Extension]]
	- ## Configuration
		- Reads `$XDG_CONFIG_HOME/gh-dash/config.yml`, and **writes its own full defaults there on first run** if the file is missing.
			- That matters when judging the tool: a 116-line real-world config sounds configuration-heavy, but ~90 of those lines are byte-identical to what gh-dash generated for itself. A long config file is not evidence of a configuration-heavy tool when the tool prints its own defaults into it.
			- The dotfiles track that generated file as gh-dash wrote it, at [dotfiles/chezmoi/dot_config/gh-dash/config.yml](https://github.com/codekiln/dotfiles/blob/main/chezmoi/dot_config/gh-dash/config.yml), following [[My/Pref/Dev/Management/Configuration/Track What the Tool Writes]]. gh-dash writes the file only when it is missing, so a deployed config leaves it with nothing to write. Copied at v4.25.2 — copy it again on an upgrade that changes the defaults.
		- Settings worth reaching for later, none of them needed yet
			- `repoPaths` — maps repo names onto the local checkout tree, so keybindings can act on a working copy
			- `prsLimit` — default 20 per section
			- theme — [[catppuccin]] publishes a gh-dash theme
	- ## Facts
		- MIT, [v4.25.2](https://github.com/dlvhdr/gh-dash/releases/tag/v4.25.2) released 2026-07-10, ~12.3k stars
		- GitHub only. Four upstream attempts at other forges, none merged — there is no [[glab]] equivalent.
