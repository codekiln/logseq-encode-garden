logseq-entity:: [[Logseq/Entity/Software/Plugin]]
see-also:: [[Flashcard/Spaced Repetition System]]
tags:: [[Obsidian/Plugin]]

- # [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition)
	- [[Obsidian]] community plugin for [[Flashcard/Spaced Repetition System|spaced repetition]] review of flashcards and notes; uses the SM-2 scheduling algorithm.
	- Plugin ID: `obsidian-spaced-repetition` · Author: st3v3nmw · License: MIT
	- ## Card formats
		- **Single-line:** `Question :: Answer` in a note tagged `#flashcards`
		- **Multi-line:** question and answer separated by a `?` on its own line
		- **Cloze:** `==highlighted text==` becomes a cloze deletion
		- **Whole-note review:** any note can be scheduled for periodic revisit on a decay curve
	- ## Key features
		- SM-2 scheduling algorithm (same family as Anki's default)
		- Review UI lives in the Obsidian sidebar panel
		- Supports multiple card decks via tags
		- Tracks ease factor, interval, and repetition count per card
