logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Logseq/Flashcard]]

- # What data does `srs-of-matrix.edn` store in a Logseq graph?
	- ## [[AI Answer]]
		- **Short answer:** It stores the shared [[SM-2]] interval matrix — a lookup table mapping `{repetition-count, easiness-factor}` to interval-in-days — used by Logseq's built-in `#card` spaced repetition system.
		- ### Structure
			- The file is [[EDN]] (Clojure's Extensible Data Notation). Its shape is:
				- ~~~edn
				  {repetition-count {easiness-factor interval-days, ...}, ...}
				  ~~~
			- **Outer key** (integer `0`, `1`, `2`, …): how many consecutive successful reviews a card has had (the repetition number `n` in [[SM-2]]).
			- **Inner key** (float e.g. `2.5`, `2.36`): the easiness factor (EF) for that cell.
			- **Inner value** (float): the calculated next interval in days.
		- ### Why it's called a "matrix"
			- [[SM-2]] defines a 2-D lookup table of `(n, EF) → interval`. As cards are reviewed with varying quality ratings, new `(n, EF)` cells are populated and the matrix grows. The file is essentially a memoised version of that table, shared across all cards in the graph.
		- ### Relationship to per-card state
			- There are two separate pieces of state:
				- **Per-card** (block properties on each `#card` block): `card-repeats::`, `card-next-schedule::`, `card-last-interval::`, `card-ease-factor::`. This records *this specific card's* history — how many times reviewed, current EF, next due date.
				- **The matrix** (`srs-of-matrix.edn`): answers "for *any* card at repetition `n` with easiness factor `EF`, what is the next interval?" It does not know or care which card is asking.
			- At review time the two work together:
				- 1. Read this card's `n` and `EF` from its block properties.
				- 2. Look up `(n, EF)` in the matrix → get the interval.
				- 3. After rating, update both: the card's block properties (new `n`, `EF`, due date) **and** the matrix cell for the new `(n, EF)`.
			- Two different cards with the same `(n, EF)` get the same interval from the matrix. The matrix is a graph-wide learned lookup table, not a per-card record.
		- ### Per-graph, local-only
			- Each graph has its own `logseq/srs-of-matrix.edn`. The file in `logseq/docs` (the official Logseq documentation graph, available at `ghq/github.com/logseq/docs`) is simply the SRS state for that graph — confirming the file is standard Logseq infrastructure, not custom to this garden.
		- [[Answer/Official]] from [Logseq source — spaced repetition](https://github.com/logseq/logseq)
