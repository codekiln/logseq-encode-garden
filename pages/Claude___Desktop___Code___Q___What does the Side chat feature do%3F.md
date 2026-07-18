tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/What does the Side chat feature do?

- # What does the "Side chat" feature do in [[Claude/Desktop/Code]]?
	- ## [[AI Answer]]
		- **Short answer:** A **side chat** is a branched, throwaway conversation you open from inside a Code session — it can read everything in the main thread up to that point, but nothing said inside it feeds back into the main conversation. It exists so you can ask a clarifying question, check an assumption, or explore an idea without steering the session off course.
		- **How to open one:** **Cmd+;** (macOS) or **Ctrl+;** (Windows), or type `/btw` in the prompt box. Available in local, SSH, and WSL sessions. When you're done, close it and the main session continues where you left off.
		- **What it can see:** Full read access to the main thread's history up to the point it was opened — but no tools. One description frames it as the inverse of a sub-agent: a sub-agent gets an empty context with all tools available, while a side chat gets the full conversation history with no tools.
		- **Introduced:** Shipped as part of the April 2026 Claude Code desktop redesign, alongside the multi-session sidebar, drag-and-drop pane layout, and cloud Routines.
		- **Sources:** [Desktop application docs — "Ask a side question without derailing the session"](https://code.claude.com/docs/en/desktop#ask-a-side-question-without-derailing-the-session), [Claude Code Desktop Redesign guide](https://miraflow.ai/blog/claude-code-desktop-redesign-parallel-sessions-routines-workspace-guide).
