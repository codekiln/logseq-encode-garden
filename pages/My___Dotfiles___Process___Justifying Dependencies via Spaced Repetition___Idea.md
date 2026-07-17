tags:: [[Idea]]

- # Prune what I can't explain: spaced repetition as a retention gate
	- ## The idea
		- Give every dotfiles-managed dependency a flashcard: why it's installed, what job it does, which [[My/Principle]] or [[My/Pref]] it serves. Review the deck on a spaced-repetition cadence, the same mechanism already powering [[Logseq/Flashcard/Review/Favorite]] decks for tools like [[mise]], [[chezmoi]], [[tmux]], and [[yazi]].
		- If I can't answer a card — I've forgotten why something is there, or what principle it's supposed to serve — that entry gets flagged, not immediately removed. If I still can't explain it after a check-in period, it gets pruned from the dotfiles.
		- I kinda like this because it makes me responsible for knowing what's in my dotfiles. Anything I don't know about eventually gets pruned automatically, just by the passage of time and my own forgetting.
	- ## Why it fits here
		- Companion to [[My/Dotfiles/Process/Adding a New Global Dependency/Idea]]: that Idea is the entry gate — nothing gets installed without a written why. This is the exit gate — nothing stays installed without a *recalled* why. Entry is a one-time interview; retention is a recurring quiz.
		- [[My/Principle/Make the Right Thing Easy and the Wrong Thing Hard]]: today, forgetting why a tool is installed has zero consequence — the undisciplined path (silent, permanent cruft) is the easy one. A recall check flips that.
		- [[My/Principle/Favor Readers Over Writers]] applied to my future self as reader: if a dotfiles entry can't survive being read back to me later, it has already failed the point of writing it down.
		- The flashcard infrastructure for this partly already exists ([[Logseq/Flashcard/Review/Favorite]]) — the new part is treating a failed review as a *signal that feeds pruning*, not just a study aid.
	- ## Open questions
		- What counts as "explained" — free recall, or is recognizing the answer on the card enough?
		- Per-tool or per-principle: if I forget one transitive library dependency of a formula I do actively use and understand, is that a false-positive prune?
		- Cadence and grace period — how many missed reviews before an entry is flagged, how long flagged before it's actually pruned?
		- Scope for a first pass — Homebrew entries only, tying into [[My/Dotfiles/Process/Adding a New Global Dependency/Idea]]'s Try-before-commit window, or every dotfiles-managed tool including mise?
		- Who executes the prune — a manual weekly ritual I run myself, or a skill/agent that proposes removals from failed reviews for me to confirm?
	- See [[2026-07-17 Fri]].
