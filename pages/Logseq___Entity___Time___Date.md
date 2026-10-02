logseq-entity:: [[Logseq/Entity/Definition]]

- # Date
	- In this garden, **Date** pages model a single calendar day. Every instance is a journal page, so a date link and that day's journal entry are one page.
	- ## Naming
		- The title is `YYYY-MM-DD Day`, matching `:journal/page-title-format` in `logseq/config.edn`: [[2026-09-24 Thu]].
		- Logseq parses a date-shaped title, so `[[2026-09-24]]` lands on the same page. Prefer the weekday form on new writes; it reads as a day rather than a number.
		- The weekday must be the real weekday for that date.
		- On disk the journal file is `journals/YYYY_MM_DD.md`, with underscores. Links use the dashed title.
	- ## Instances need no file
		- A date link is complete on its own. It resolves and collects backlinks whether or not `journals/YYYY_MM_DD.md` exists, and Logseq writes the file when something is put on that day. Pointing a property at a day nothing was written on is ordinary.
	- ## Precision
		- This type is the day. A month is `[[YYYY/MM]]`, and a year, decade or century is a [[Logseq/Entity/Time/Year]] instance.
		- Use a day only when the day is known. [[Logseq/Date]] rules out padding a month to `01` to reach day precision.
	- ## Frontmatter
		- A property whose value is a day takes a Date link: `date-created::`, `date-completed::`, `date-purchased::`, and any other `date-<verb>::` property per [[Logseq/Date]].
		- An instance is a journal page and carries no `logseq-entity::` of its own; the shape of the title is what identifies it.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Relationship to [[Logseq/Date]] and [[Logseq/Journal]]
		- [[Logseq/Date]] governs which date form to type for a given precision. [[Logseq/Journal]] governs what goes inside a day's page. This type is the day itself, the page those links point at.
