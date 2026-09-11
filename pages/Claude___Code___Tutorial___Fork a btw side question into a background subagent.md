tags:: [[Claude/Code]], [[Diataxis/Tutorial]]
alias:: [[Anthropic/App/Claude Code/Tutorial/Fork a btw side question into a background subagent]]
title:: Claude/Code/Tutorial/Fork a btw side question into a background subagent

- # Tutorial: Ask a side question with `/btw`, fork it, and switch back with the arrow keys
	- ## Summary
		- [`/btw`](https://code.claude.com/docs/en/commands#all-commands) lets you ask a question about the current session without adding it to the conversation history. If the answer needs real tool access (reading a file, running a command), press `f` in the answer overlay to spin the question into a **forked subagent** that inherits the whole conversation. The fork runs in a panel below your prompt while you keep working in the main session, and `↑`/`↓` moves the panel's selection between the main session's row and the fork's row.
		- Source: [Interactive mode — Side questions with /btw](https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw) and [Sub-agents — Observe and steer running forks](https://code.claude.com/docs/en/sub-agents#observe-and-steer-running-forks).
	- ## Before You Start
		- **Claude Code CLI** installed and authenticated (`claude --version` works). See [[Claude/Code/How To/Install]].
		- `/btw` without a question requires **v2.1.212 or later** (earlier versions require a question every time) — [commands reference](https://code.claude.com/docs/en/commands#all-commands).
		- The `f`-to-fork key in the `/btw` overlay requires **v2.1.187 or later**; the newer `Shift+Left`/`Shift+Right` history-stepping keys require **v2.1.257 or later** — [Side questions with /btw](https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw).
		- Forking is a *local-session-only* feature: it isn't available over [Remote Control](https://code.claude.com/docs/en/remote-control) or in the VS Code extension's chat panel, where `/btw` opens a panel instead of the terminal overlay — same source.
	- ## Steps
		- ### 1. Start (or resume) a session and do some work
			- Have a normal conversation with Claude — read some code, make an edit, whatever the actual task is. `/btw` answers only from what's *already* in this conversation (your messages, Claude's replies, and gathered tool results), so ask your side question after Claude has seen the thing you're curious about.
		- ### 2. Ask a side question with `/btw`
			- ~~~
			  /btw what was the name of that config file again?
			  ~~~
			- The question and its answer appear in a **dismissible overlay** and never enter the conversation history. Run `/btw` again with no question to reopen the overlay on your most recent exchange.
			- You can run `/btw` even while Claude is still generating its main response — the side question runs independently and doesn't interrupt that turn.
			- Docs: [Side questions with /btw](https://code.claude.com/docs/en/interactive-mode#side-questions-with-%2Fbtw).
		- ### 3. Fork the question if it needs real tool access
			- Side questions have **no tool access** — Claude can't read files, run commands, or search to answer one. If the answer actually requires that, press `f` in the overlay:
				- > "Start a forked subagent that inherits the parent conversation plus this question and answer, so it can continue with full tool access. You stay in the current session and find the fork in the panel below your prompt."
			- This is distinct from the standalone [`/fork`](https://code.claude.com/docs/en/commands#all-commands) command, which copies the *whole* session into a new background session in [agent view](https://code.claude.com/docs/en/agent-view#copy-the-session-with-%2Ffork) rather than opening a row in the in-terminal fork panel. See [Fork the current conversation](https://code.claude.com/docs/en/sub-agents#fork-the-current-conversation) for how a conversation fork differs from other subagents.
		- ### 4. Switch between the fork and your main session with the arrow keys
			- Once forked, a panel opens below the prompt input with one row for the main session and one row per running fork. Use these keys ([Observe and steer running forks](https://code.claude.com/docs/en/sub-agents#observe-and-steer-running-forks)):
				- | Key | Action |
				  | --- | --- |
				  | `↑` / `↓` | Move the panel's selection between rows (main session ↔ each fork) |
				  | `Enter` | Open the selected fork's transcript and send it follow-up messages |
				  | `x` | Stop the selected fork, or dismiss its row once it's no longer running |
				  | `Esc` | Return focus to the prompt input |
			- So the "down key to switch" workflow is: press `↓` to move the panel's selection onto the fork's row, `Enter` to open its transcript, work there, then `Esc` (or select the main-session row with `↑`) to get back to your original conversation. Built-in commands like `/model` still act on your main conversation even while a fork's transcript is open.
			- Claude Code removes a fork's row automatically when it finishes successfully; a failed or stopped fork's row stays for 30 seconds so you have time to inspect it.
	- ## Verification
		- After pressing `f`, a new row appears in the panel below the prompt — that's the fork, running in the background.
		- Pressing `↓` moves the highlighted row from the main session down to the fork; `Enter` opens its transcript inline.
		- When the fork finishes, its result arrives as a message in your main conversation and its row disappears from the panel.
	- ## What You Learned
		- `/btw` answers side questions from context already in the session, without touching conversation history or using tools.
		- Pressing `f` in the `/btw` overlay escalates a side question into a **forked subagent** with full tool access, tracked in a panel below the prompt.
		- `↑`/`↓` moves between the main session and fork rows in that panel; `Enter` attaches to a row's transcript and `Esc` returns you to the prompt.
	- ## Next Steps
		- For side tasks that don't need the whole conversation's history, look at plain [subagents](https://code.claude.com/docs/en/sub-agents) instead of a fork.
		- To copy an *entire* session into its own background session (rather than forking one `/btw` answer), use [`/fork`](https://code.claude.com/docs/en/commands#all-commands) and manage it from [agent view](https://code.claude.com/docs/en/agent-view).
	- ## Related
		- [[Claude/Code/Command/Slash]]
		- [[Claude/Code/Docs/Tutorial/Run parallel Claude Code sessions with Git worktrees]]
