logseq-entity:: [[Logseq/Entity/software-project]]
tags:: [[CLI/Tool]], [[Rust]]
see-also:: [[CLI/Q/Are there CLI or terminal apps to manage hierarchical keyboard-shortcut reference for CLI and TUI tools, with spaced repetition?]]

- # [shaankhosla/repeater](https://github.com/shaankhosla/repeater)
	- Spaced repetition in the terminal: **Rust** CLI for drilling [[Markdown]] [[Flashcard/Spaced Repetition System]] flashcards (Q/A and cloze), **FSRS** scheduling, and [[SQLite]] progress so decks can live beside notes in a **git-friendly** repo layout.
		- [[My Note]] *SQLite is an awesome technology but it's annoying how so many technologies rely on it, given there's not an easy, idiomatic and correct way to use it with git. For now, I'll stick with [[Logseq/Flashcard]] system, which also places the [[SRS]] information into the markdown in such a way that persists progress in git*
	- Typical entry points: `repeater drill` and related subcommands (see repository README and `--help`).
	- {{embed [[repeater/Card/Format]]}}
	-