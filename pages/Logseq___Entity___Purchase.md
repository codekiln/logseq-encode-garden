logseq-entity:: [[Logseq/Entity/Definition]]

- # Purchase
	- In this garden, **Purchase** pages model something acquired: when it was bought, what it cost, and where it came from. A page carries this entity alongside whatever the item itself is.
	- ## What counts as an instance
		- A specific item [[Person/codekiln]] owns, bought on a known day. The page is the item; this type adds the acquisition to it.
		- Not this type: something under consideration, which stays a shopping note, or a subscription and its recurring charge.
	- ## Naming
		- The page is the item and takes the item's own name, under its maker per [[Logseq/Pref/Page/Name]] — [[IK Multimedia/iLoud Micro Monitors]].
	- ## Frontmatter
		- `logseq-entity::` names the item's own type first, then this one: `logseq-entity:: [[Logseq/Entity/Hardware/Audio/Speaker]], [[Logseq/Entity/Purchase]]`.
		- `date-purchased::` — the day, as a [[Logseq/Entity/Time/Date]] link: `[[2022-08-20 Sat]]`.
		- `logseq-purchased-time-year::` — the same event at year precision, as a [[Logseq/Entity/Time/Year]] link: `[[20/2/2]]`. It sits alongside `date-purchased::` the way `logseq-created-time-year::` sits alongside `date-created::`, so every purchase of a given year collects as a backlink on that year.
		- `purchase-price::` — what was paid, with its currency symbol.
		- `purchase-link::` — the listing it was bought from, as a Markdown link.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- The acquisition lives in frontmatter. The body is the item's, and follows the item's own entity type.
	- ## Examples in this garden
		- [[IK Multimedia/iLoud Micro Monitors]].
