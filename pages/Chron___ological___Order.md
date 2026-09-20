logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Week/Review/26/09/20 Sun]]

- # Chronological order
	- ## Overview
		- **Chronological order** arranges items by **when they happened** — earlier before later — so the sequence itself is the index.
		- Journals, logs, and feeds use it so a reader can ask *what happened next?*
	- ## Context
		- In this garden, journaling is deliberately chronological; knowledge gardening is not. Related pages should sit near each other the way a [[Graph/Database]] clusters neighbors, not in the order they were filed.
		- Other orders in the garden answer different questions:
			- [[Alpha/Bet/ic/al/Order]] — by letters of the alphabet, for human-readable lists of words.
			- [[Lexicographic/Order]] — by the full character repertoire of a name, including digits and punctuation; the order [[OS/File/System]]s actually use.
	- ## Key Principles
		- **Time is the key** — the sort key is a date or timestamp, not a title.
		- **Precision follows knowledge** — year, month, or day per [[Logseq/Date]]; do not fake a day when only a year is known.
		- **Sequence is not proximity** — two notes written on consecutive days may be about unrelated things; chronology does not cluster by topic.
	- ## Mechanism
		- A journal page `journals/YYYY_MM_DD.md` and a wikilink in the `YYYY-MM-DD Day` shape are chronological addresses.
		- Entity paths that embed `<YY>/<MM>` (blogs, podcasts, books) use chronology as a *secondary* key after creator and type, so works still cluster by who made them.
	- ## Examples
		- Daily journals under `journals/`.
		- A blog post path `Person/<Name>/Blog/<YY>/<MM>/<slug>` — dated, but nested under the author.
		- A series path that *also* uses an ordinal — publication year and reading order can diverge; [[Logseq/Entity/Series]] prefers the ordinal when the published sequence numbers its parts.
	- ## Misconceptions
		- "Filing by date keeps related things together" — **False** unless the relatedness *is* the date (a trip, a conference). Topic clusters need a graph-like layout instead.
		- "Alphabetical and chronological are the two orders" — **Incomplete**; filesystem sort is [[Lexicographic/Order]], which is a generalization of [[Alpha/Bet/ic/al/Order]] and is not a time order.
