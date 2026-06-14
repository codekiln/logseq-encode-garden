logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Flashcard/Spaced Repetition System]], [[Flashcard/Spaced Repetition System/Free]]
tags:: [[Question]]

- # In [[Obsidian]], is there any spaced repetition flashcard system available either built in or through popular community plugins?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** **No built-in SRS.** Obsidian core has no spaced repetition or flashcard functionality. The dominant community plugin is [[Obsidian/Plugin/Spaced Repetition]] (`obsidian-spaced-repetition` by st3v3nmw), which supports multiple card formats and uses SM-2. A newer alternative, [[Obsidian/Plugin/Recall]], uses the [[FSRS]] algorithm. Anki-bridge plugins exist for those who prefer the Anki ecosystem.
		- ### Built-in support
			- **None.** Obsidian's core app has no [[Flashcard/Spaced Repetition System|SRS]] or flashcard feature.
		- ### Community plugins
			- #### 1. [[Obsidian/Plugin/Spaced Repetition]] (most popular)
				- Algorithm: **SM-2** (same family as Anki's default scheduler)
				- Card formats:
					- **Single-line:** `Question :: Answer` inside a note tagged `#flashcards`
					- **Multi-line:** question and answer separated by a `?` line
					- **Cloze:** `==highlighted text==` becomes a cloze deletion
				- Also supports **whole-note review** — a note itself is scheduled for revisit on a decay curve
				- Review UI lives in Obsidian's sidebar panel
			- #### 2. [[Obsidian/Plugin/Recall]]
				- Algorithm: **[[FSRS]]** ([[Flashcard/Spaced Repetition System/Free|Free Spaced Repetition Scheduler]]) — a more modern, better-calibrated algorithm than SM-2
				- Supports note-level and card-level scheduling
			- #### 3. Flashcards (reuseman)
				- Plugin ID: `flashcards-obsidian`
				- Syntax is close to Anki's native format
				- Less actively maintained as of 2025
			- #### 4. Anki bridge plugins (Obsidian to Anki / AnkiSync)
				- Bridges Obsidian notes to the external [Anki](https://apps.ankiweb.net/) desktop app via the AnkiConnect add-on
				- Anki handles all scheduling; Obsidian is the authoring environment only
				- Requires Anki and AnkiConnect running locally; syncs to AnkiWeb for cross-device review
		- ### Practical recommendation
			- **Stay in Obsidian:** use [[Obsidian/Plugin/Spaced Repetition]] (SM-2, large community, actively maintained) or [[Obsidian/Plugin/Recall]] ([[FSRS]], newer algorithm with better memory modeling)
			- **Prefer Anki's ecosystem:** use an Anki-bridge plugin; Anki's scheduling is battle-tested and syncs across devices via AnkiWeb
		- ### Sources
			- [obsidian-spaced-repetition GitHub](https://github.com/st3v3nmw/obsidian-spaced-repetition)
			- [Recall GitHub](https://github.com/martin-jw/obsidian-recall)
			- [Obsidian community plugins — spaced repetition](https://obsidian.md/plugins?search=spaced%20repetition)
