tags:: [[Idea]]
date-created:: [[2026-03-21 Sat]]

- # Terminal-first toolbelt learning: snips, flashcards, coaches, Readwise-style reading
	- Want external systems that help learn the coding toolbelt end-to-end: Neovim, tmux, ripgrep, lazygit, VS Code, PyCharm, and similar — not only reference, but retention.
	- Prefer staying in the terminal: take notes from the shell, use `rg` and other CLIs there, and reduce “AI does it for me” in favor of **teaching**.
	- ## Flashcards
		- One leg is spaced repetition / flashcards (already practiced in this graph with `#card` on keyshort and other pages).
	- ## Coaches (concept)
		- **AI Terminal Coach** — guides how to do things in the terminal rather than performing them for you; pairs with interactive review.
		- **AI Engineering Coach** — same spirit for broader engineering workflow; overlaps with teaching-oriented agent skills (see related link below).
	- ## Snip / highlight pipeline (missing standard)
		- While reading `man rg` (example), used tmux copy mode and yanked a tip — but yank-only does not attach **source**, **section**, or a path into the knowledge garden.
		- Wish: a **standard flow** from “selection in pager or tmux” → **personal notes** with **attribution** → optional **flashcard** and **coach context** (quizzes, “what flag was that?”).
		- Analog: [Readwise Reader](https://readwise.io/read) on the web — save a page, open it, bookmarklet shows **your highlights** on the page; in Reader you see the **full document plus highlights**.
	- ## Example snip (ripgrep)
		- Source: `man rg` (ripgrep manual), captured from terminal (tmux copy mode).
		- ~~~
		  Tip: to disable all smart filtering and make ripgrep behave a bit more like classical
		  grep, use rg -uuu.
		  ~~~
	- ## Wishlist: Readwise-like CLI / TUI
		- **Pipe a document into Readwise** from the shell (save full text or URL-derived doc with stable identity).
		- **TUI reader** that shows the document **with highlights** in the terminal — Readwise Reader experience without leaving the shell.
		- Partial reality today: community Reader CLIs and APIs (see related); nothing yet matches “pager selection → attributed highlight → sync’d reader + flashcard queue” as one frictionless habit.
	- ## Related in this graph
		- [[Readwise/CLI]] — existing notes on Reader CLI tooling (`rw-cli`, APIs).
		- [[AI/Coding/Idea/26/03/AI Coding Coach as Skill]] — teaching-first agent / skill idea.
