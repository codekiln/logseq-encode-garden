logseq-entity:: [[Logseq/Entity/Discussion]], [[Logseq/Entity/Diataxis/Explanation]]
see-also:: [[Logseq/Entity/Hierarchy/Discussion]], [[My/Principle/Simplify/Don't Repeat Yourself DRY]]

- # Maker Discussion
	- Why each segment under [[Logseq/Entity/Person/Maker]] names what the person makes, why Songwriter and Conductor nest under Composer and Performer, why the shared rules sit on Maker, and what the family replaced.
	- ## Each entity name under Maker says what the person makes
		- `Maker/Music/Theory` names a maker of theory whose field is music. Heinrich Glarean is known for his theory, including his naming of the Ionian and Aeolian modes, so his hub carries Music Theorist alone, without Musician. [[Logseq/Entity/Person/Maker/Music/Tech]] works the same way for a person who builds a synthesis method or a music programming language.
		- Theory and Tech nest under Music because music is their field, so the music entities stay together in one namespace. They are kinds of Maker. Composer, Performer and Music Producer are kinds of Musician.
		- A person who builds music software and also makes music carries both entities, as `logseq-entity:: [[Logseq/Entity/Person/Maker/Music/Tech]], [[Logseq/Entity/Person/Maker/Music]]` does for a technologist whose role in music is unknown. Neither entity implies the other, so the page lists two lineages.
		- The alternative was to make Theory and Tech kinds of Musician. That would mark Glarean as a musician, and would leave no way to mark a technologist who makes no music.
	- ## Songwriter and Conductor nest under Composer and Performer
		- Writing a song is composing, and conducting is performing through an ensemble. [[Logseq/Entity/Person/Maker/Music/Composition/Song]] is a kind of Composer, and [[Logseq/Entity/Person/Maker/Music/Performance/Conducting]] is a kind of Performer.
		- With each page marked by the most specific entity in each lineage, as [[Logseq/Entity/Hierarchy/Discussion/Analysis/Opus/26/10/01/0611 ET Mark each page with the most specific entity in each lineage]] recommends, [[Person/Madonna]] carries Songwriter and Performer, and Songwriter already says she composes.
		- The alternative was to put Song and Conducting directly under Music, beside Composition and Performance. A songwriter's page would then need Composer as well to say that songs are compositions, or the Composer namespace would leave songwriters out.
	- ## Shared rules live on Maker
		- Marking, `created-by::` on works, the lean hub with one line saying what the person makes, and the marking for an unknown role are the same for every maker. They are written once, on [[Logseq/Entity/Person/Maker]], following [[My/Principle/Simplify/Don't Repeat Yourself DRY]]. Each child page holds only what differs: what counts as its instance, the cases near its boundary, and any frontmatter of its own.
		- The alternative was to repeat the shared rules on every child page. A change to one rule would then need an edit on each child page, and the copies would disagree whenever one was missed.
	- ## `Person/Music/*` was considered and rejected
		- The other shape put the music entities under `Logseq/Entity/Person/Music`, with `Person/Music/Composition`, `Person/Music/Theory` and the rest beneath it.
		- That shape has no common parent for music and art. A sound artist and a composer share the marking, `created-by::` and hub rules, which would either sit on [[Logseq/Entity/Person]], where they would apply to every person, or be copied into `Person/Music` and a separate `Person/Art`.
		- `Person/Music` also names a field without saying what the person does in it. `Maker` says that every entity in the family is about making something, and the segments under it say what is made.
	- ## History
		- [[2026-09-27 Sun]] — `Logseq/Entity/Person/Musician` added, for people whose work includes making, performing or producing music. Each hub that carried it listed [[Logseq/Entity/Person]] as well.
		- [[2026-10-10 Sat]] — codekiln renamed Musician to `Logseq/Entity/Person/Music/ian` in the morning, and later that day to [[Logseq/Entity/Person/Maker/Music]], rewriting it as the parent of the music maker entities and adding [[Logseq/Entity/Person/Maker]] and its children. Both old names stay as aliases of the Musician page.
