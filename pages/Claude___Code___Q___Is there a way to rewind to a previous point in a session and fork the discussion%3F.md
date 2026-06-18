logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Desktop/Q/Is it possible to fork a conversation in Claude Desktop?]]

- # Is there a way to rewind to a previous point in a [[Claude/Code]] session and fork the discussion?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** **Yes.** `/rewind` (or double-tap `Esc` when the prompt is empty) rolls back to a prior checkpoint; it mutates the session in place. To **preserve the original** and branch, follow with `/branch`. There is no single command that rewinds *and* forks atomically as of 2026-06.
			- **`/rewind` — roll back to any earlier checkpoint:**
				- Type `/rewind` in the prompt (or **double-tap `Esc`** with an empty input) to open a list of every prior user turn as a checkpoint.
				- For each checkpoint you can choose:
					- **Restore code and conversation** — reverts both file edits and conversation history to that point; the original prompt is placed back in the input field.
					- **Restore conversation** — rewinds history only; keeps current file state.
					- **Restore code** — reverts file edits only; keeps the full conversation.
					- **Summarize from here / up to here** — compresses rather than discards turns.
				- **Important:** `/rewind` mutates the current session in place — the "forward" history after the checkpoint is discarded. It does **not** create a fork on its own. Claude Code shows "The conversation will be forked" as a description, but as of 2026-06 a confirmed bug means no separate resumable fork is saved ([GitHub #55347](https://github.com/anthropics/claude-code/issues/55347)).
				- **Out of scope:** commands with external side effects (`git push`, API calls, package installs) are **not** reverted — only in-session file edits and conversation turns.
			- **`/branch` — fork from the *current* point (no rollback):**
				- `/branch [optional-name]` copies the session at its **current** state into a new session ID, leaving the original intact for later `/resume`.
				- `/fork` was the earlier name; it was renamed `/branch` (around v2.1.77).
				- From the terminal: `claude --resume <session-id> --fork-session` or `claude --continue --fork-session` achieves the same result from outside the interactive session.
				- Session-scoped permission approvals do **not** carry over to the new branch.
			- **Two-step: rewind then fork (branch from a *prior* point):**
				- There is no single command for "go back to message N and branch from there."
				- Workaround: run `/rewind` → "Restore code and conversation" to roll the current session back to the target checkpoint, then immediately run `/branch` to fork from that restored point.
				- Forked sessions are **grouped** under their root session in the `/resume` picker; press `→` to expand the group and see child branches.
			- **VSCode / IDE extension:**
				- Rewind and fork per-message are also available via UI controls on individual messages in the Claude Code VSCode extension (shipped in v2.1.19; [Threads by Boris Cherny](https://www.threads.com/@boris_cherny/post/DT8oWNyEgaD/)).
			- **Sources:** [Checkpointing — Claude Code Docs](https://code.claude.com/docs/en/checkpointing) · [Manage sessions — Branch a session — Claude Code Docs](https://code.claude.com/docs/en/sessions) · [/rewind bug #55347 (GitHub)](https://github.com/anthropics/claude-code/issues/55347) · [How to Use Claude Code /rewind (mindstudio.ai)](https://www.mindstudio.ai/blog/claude-code-rewind-command-rollback) · [Mastering /btw, /fork, and /rewind (Towards AI)](https://medium.com/@richardhightower/mastering-claude-codes-btw-fork-and-rewind-the-context-hygiene-toolkit-5ceefa59623d)
