tags:: [[Claude/Desktop]], [[Q]]
alias:: [[Anthropic/App/Claude Desktop/Q/Is it possible to fork a conversation in Claude Desktop]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Desktop]], [[LibreChat/Fork]]
title:: Claude/Desktop/Q/Is it possible to fork a conversation in Claude Desktop?

- # Is it possible to fork a conversation in [[Claude/Desktop]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** **Yes** — but the affordance depends on which [[Claude/Desktop]] tab you are in. The **Code** tab has an explicit **Fork from here** action (and shares Claude Code’s `/branch` / `/fork` session branching). The **Chat** tab supports branching conversations without losing the original, including a dedicated **Fork** control in recent releases and an older pattern of **editing a prior message** to start an alternate thread.
			- **Code tab (Claude Code in Desktop):**
				- Hover a past message and choose **Fork from here** to open a new session that copies history up to that point; the parent chat stays intact ([GitHub issue describing Desktop Code-mode fork](https://github.com/anthropics/claude-code/issues/49954)).
				- In the same engine as the CLI, `/branch` creates a conversation branch at the current point; `/fork` is an alias unless `CLAUDE_CODE_FORK_SUBAGENT` changes that behavior ([Commands — `/branch`](https://code.claude.com/docs/en/commands.md), [Manage sessions — Branch a session](https://code.claude.com/docs/en/sessions.md)).
				- From the terminal, `claude --continue --fork-session` or `claude --resume --fork-session` forks before resuming ([Manage sessions](https://code.claude.com/docs/en/sessions.md)).
			- **Chat tab:**
				- Anthropic’s help docs describe **editing a prior chat message** to create a **different version of the conversation** (with its own artifacts) while keeping earlier work — a branch-by-edit pattern ([What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)).
				- Product roundups in early 2026 also list **Fork** as a first-class Chat control (hover a message → **Fork from here**), alongside `/rewind` and `/recap`; treat UI labels as version-dependent and confirm in your build.
			- **What “fork” means here:**
				- The forked thread inherits messages **up to the fork point**; parent and child diverge independently afterward ([Manage sessions](https://code.claude.com/docs/en/sessions.md)).
				- Forking is for exploring alternatives, not for a blank slate (start a new chat) and not a token saver (both threads retain copied history).
			- **Limits / caveats:**
				- **Code tab:** a forked Desktop Code session reuses the **same working directory** as the parent unless you manually use worktree flows; “fork into worktree” from **Fork from here** was requested but is not the default today ([feature request #49954](https://github.com/anthropics/claude-code/issues/49954)).
				- **CLI branches:** session-scoped permission approvals do **not** carry over to the new branch ([Manage sessions](https://code.claude.com/docs/en/sessions.md)).
				- **Cowork** and **incognito** chats follow different session rules; this answer targets normal Chat and Code conversations.
