logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Can Celik]]
date-created:: [[2026/03/27]]
see-also:: [[tmux]], [[Zellij]], [[Terminal/Multiplexer]], [[My/AI/Agent/Chief of Staff]], [[My/AI/Agent/Fleet]]

- # [herdr](https://herdr.dev)
	- Terminal-native agent multiplexer: surfaces the state of every coding agent at a glance — blocked, working, done — as real terminal panes rather than a wrapped interpretation of them. Self-described as "the runtime your coding agents live on."
	- [herdrdev/herdr](https://github.com/herdrdev/herdr) — [[GitHub/Star]]: 24,249 (checked 2026-08-04). Apache 2.0.
	- Written in [[Rust]]; ships as a single binary rather than an Electron app, and runs inside whatever terminal is already in use.
	- ## Where it sits against [[tmux]]
		- Covers the multiplexer basics that make it a plausible [[tmux]] replacement rather than a companion: detach and reattach from any terminal, sessions that survive restarts, and attach over SSH. Weighed on [[Terminal/Multiplexer/Idea]].
		- Keeps tmux-style prefix keys while treating mouse click, drag, and split as equally first-class, so neither input mode is the fallback.
	- ## What the agent orientation adds
		- Agent state detection is the premise: panes are labeled by whether the agent inside is blocked, working, or done, which is the piece a general-purpose multiplexer leaves to the human to infer.
		- A socket API lets agents drive the multiplexer themselves — spawning panes, reading output, and waiting on each other — rather than only being driven by a human at the prefix key.
		- Plugins extend panes and workflows, distributed through a marketplace.
	- ## Adoption
		- [[Person/Chris Power]] switched over after about 10 years on [[tmux]], won over by the agent-state pane and by being able to SSH into a remote box and leave an agent running unattended — [[Person/Chris Power/YouTube/26/08/herdr]].
		- Installed from [[My/Dotfiles]] since [[2026/08/11]] as a global [[mise]] tool, alongside [[tmux]] rather than replacing it, to try the agent-state pane in daily use.
			- Config lives at `~/.config/herdr/config.toml` and holds two settings. `onboarding = false` stops herdr's first-run write from editing a [[chezmoi]]-managed file; `[update] version_check = false` leaves the version to [[mise]], which herdr already defers to. Its defaults supply the rest — the `ctrl+b` prefix and [[Catppuccin/Mocha]].
			- Detection manifests stay on: they refresh the screen-pattern rules behind the blocked/working/idle labels, which decay as agent interfaces change.
	- ## No longer the primary multiplexer here, since [[2026/08/24]]
		- [[Person/codekiln]] on [[2026-08-25 Tue]]: *"herdr is not retired; it's just not primary as my multiplexer right now."* The software is alive and this graph said otherwise for a day.
		- The server was stopped on the morning of [[2026/08/24]] and its ~24 orphaned sessions killed. [[My/AI/Agent/Fleet]] runs on [[tmux]] now, and the standing instruction is not to start the herdr server or use `herdr` commands. That instruction is about which multiplexer the seats run, and it carries no verdict on the tool.
		- The reason was hierarchy rather than any fault in the agent-state pane. A herdr workspace holds panes, and the agent name carried the whole address in 32 characters, so `<workspace-label>-<tab-label>` had to encode the repository and the work item together. [[tmux]] names five nested levels separately — session, window, pane, `claude` session, branch and worktree — and `C-b w` walks all of them in one picker.
		- What went with it is the blocked/working/done label read off the pane border, which [[tmux]] has no equivalent for. The fleet reads a session's state from its own transcript instead — see [[My/AI/Agent/Fleet/Bed Down]] on `ctx-check`.
		- Orphaned sessions were the practical cost of the run: nothing reaped a workspace whose agents had finished, so they accumulated until the server was stopped by hand.
