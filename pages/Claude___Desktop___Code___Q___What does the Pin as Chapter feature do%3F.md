tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
alias:: [[Anthropic/App/Claude Desktop/Code/Q/What does the Pin as Chapter feature do]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Desktop/Q/Is it possible to fork a conversation in Claude Desktop?]]
title:: Claude/Desktop/Code/Q/What does the Pin as Chapter feature do?

- # What does the "Pin as Chapter" feature do in [[Claude/Desktop/Code]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** **Pin as Chapter** is an experimental **Research Preview** feature in the **Code** tab of [[Claude/Desktop]] that turns chosen points in a long transcript into **named chapters** and builds a **table of contents** so you can jump between major phases of work without scrolling the whole thread.
			- **What it is for:**
				- Long [[Claude/Code]] sessions accumulate many assistant turns (debugging, refactors, reviews). Pin as Chapter is meant to mark “this message starts a new phase” and give the session a lightweight outline—similar to chapter markers in a document.
			- **How you use it (intended UI):**
				- On an **assistant** message in the transcript, use **Pin as Chapter** (shown on hover in demos; some builds also expose it via **right-click → Pin as chapter** and a title dialog).
				- The UI can **auto-suggest a chapter title** from the message (e.g. task names like “Debug pointer down event”).
				- Pin **multiple** messages to define several chapters.
			- **What you should see when it works:**
				- A **chapter heading** at the pinned point in the transcript.
				- A **chapter index / table of contents** (described in product demos as appearing toward the **top-left** of the Code view) listing pinned chapters; selecting an entry **scrolls/jumps** to that section.
			- **Implementation note:** Pinning is backed by session tooling such as `mcp__ccd_session__mark_chapter` (internal Desktop/Code session MCP), not a user-facing slash command in public docs.
			- **Status and limits:**
				- Shipped as **Research Preview** / experimental at **Code with Claude 2026** (May 2026); labels and placement may change between Desktop builds.
				- **Not** the same as **Fork from here** / session branching ([[Claude/Desktop/Q/Is it possible to fork a conversation in Claude Desktop?]])—chapters organize **one** transcript; fork copies history into a **new** session.
				- **Not** the open GitHub request for `/pin` bookmarks that survive compaction ([#32874](https://github.com/anthropics/claude-code/issues/32874))—that is a separate, CLI-oriented bookmark idea.
			- **Known issues:** Some users report that **Pin as chapter** completes with **no visible** TOC, divider, or confirmation—pins may register silently while the chapter UI does not render ([bug summary](https://www.stepcodex.com/en/issue/bug-pin-as-chapter-mark-chapter)). If nothing appears after pinning, update Desktop/Code and retry; treat missing UI as a known gap until your build shows the index.
			- **Sources:** [Code with Claude 2026 keynote summary (Pin as Chapter)](https://ai-heartland.com/news/news-code-with-claude-2026-keynote/), [Code with Claude London guide 2026 (feature table)](https://ai-heartland.com/explain/code-with-claude-london-guide-2026/), [Anthropic workshop demo (Pin as Chapter segment)](https://www.youtube.com/watch?v=MmgxjBTTX34).
