tags:: [[Idea]]
date-created:: [[2026-03-21 Sat]]

- # Terminal-first toolbelt learning: snips, flashcards, coaches, Readwise-style reading
	- [[CursorAI/CLI/Thread]] `e79ba087-945a-4a4b-a058-ee5b5be43812`
	- Want external systems that help learn the coding toolbelt end-to-end: Neovim, tmux, ripgrep, lazygit, VS Code, PyCharm, and similar — not only reference, but retention.
	- Prefer staying in the terminal: take notes from the shell, use `rg` and other CLIs there, and reduce “AI does it for me” in favor of **teaching**.
	- ## Flashcards
		- One leg is spaced repetition / flashcards (already practiced in this graph with `#card` on keyshort and other pages).
	- ## Coaches (concept)
		- **AI Terminal Coach** — guides how to do things in the terminal rather than performing them for you; pairs with interactive review.
		- **AI Engineering Coach** — same spirit for broader engineering workflow; overlaps with teaching-oriented agent skills (see related link below).
		- [[Learning/Idea/26/03/Terminal toolbelt learning/Proto Session/26/03/21 Sat]] — proto session log (dated filename); cursor-agent + tmux split-pane coaching experiment.
		- [[Learning/Idea/26/03/Terminal toolbelt learning/Proto Session/26/03/25 Wed]] — zsh × tmux refresh constraints + garden `rg` ladder; coach withholds playbook.
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
	- ## Wishlist: [[Readwise/CLI/Idea/26/03/Readwise-like TUI and CLI]] Readwise-like CLI / TUI
	- [[AI/Coding/Idea/26/03/AI Coding Coach as Skill]] — teaching-first agent / skill idea.