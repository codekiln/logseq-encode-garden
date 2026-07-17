tags:: [[Idea]]

- # Prune what I can't explain: spaced repetition as a retention gate
	- ## The idea
		- Give every dotfiles-managed dependency a flashcard: why it's installed, what job it does, which [[My/Principle]] or [[My/Pref]] it serves. Review the deck on a spaced-repetition schedule, the same mechanism already running [[Logseq/Flashcard/Review/Favorite]] decks for tools like [[mise]], [[chezmoi]], [[tmux]], and [[yazi]].
		- If I can't answer a card — I've forgotten why something is there, or what principle it's supposed to serve — that entry gets flagged, not pruned right away. If I still can't explain it after a check-in period, it gets pruned from the dotfiles.
		- I kinda like this because it makes me responsible for knowing what's in my dotfiles. Anything I don't know about eventually gets pruned, just by the passage of time and my own forgetting.
	- ## Why it fits here
		- Companion to [[My/Dotfiles/Process/Adding a New Global Dependency/Idea]]: that Idea is the entry gate — nothing gets installed without a written why. This is the exit gate — nothing stays installed without a *recalled* why. Entry is a one-time conversation; staying installed depends on a repeated check.
		- [[My/Principle/Make the Right Thing Easy and the Wrong Thing Hard]]: today, forgetting why a tool is installed has no consequence at all — leaving unexplained tools in place is the easy path. A recall check changes that.
		- [[My/Principle/Favor Readers Over Writers]] applied to my future self as reader: if I can't understand a dotfiles entry when I read it again later, it has failed the reason it was written down in the first place.
		- The flashcard system for this already exists in part ([[Logseq/Flashcard/Review/Favorite]]) — the new part is using a failed review as a reason to prune, not just as a study prompt.
	- ## Open questions
		- What counts as "explained" — remembering the answer on my own, or is recognizing it on the card enough?
		- Per-tool or per-principle: if I forget one small library dependency of a tool I do use and understand, would that wrongly get pruned?
		- Schedule and grace period — how many missed reviews before an entry is flagged, and how long flagged before it's actually pruned?
		- Scope for a first pass — Homebrew entries only, tying into [[My/Dotfiles/Process/Adding a New Global Dependency/Idea]]'s Try-before-commit window, or every dotfiles-managed tool including mise?
		- Who does the pruning — a weekly check I run myself, or a skill/agent that suggests removals from failed reviews for me to confirm?
	- See [[2026-07-17 Fri]].
