logseq-entity:: [[Logseq/Entity/Definition]]

- # Record Label
	- In this garden, **Record Label** pages model a label or imprint that releases music recordings.
	- ## What counts
		- A record label is the business or imprint named on a release. A label page collects the [[Logseq/Entity/Music/Recording]] pages it released.
		- An imprint with its own name and catalog gets its own page. It links its parent label with `part-of::` when that label has a page.
		- A label that changes its name keeps one page, named for its current name, and its body lists the former names.
		- A recording studio, distributor, or publisher is a different thing from the label that released a recording.
	- ## Naming and placement
		- Place a label at `Label/<Name>`, using the name printed on its current releases, as [[Label/Invada Records]].
	- ## Finding and deduplicating
		- Check the exact page name, `alias::` values, former names, the official domain, and plain-text mentions of the label on recording and person pages. A label mentioned only in prose on a recording page gets its page when it is filed.
	- ## Relationships
		- A recording page links each of its labels with `record-label::`, defined at [[Logseq/Entity/Music/Recording/Frontmatter/record-label]]. Those links are the label's release list, so a label page lists recordings only to add notes about them.
		- Use `founded-by::` for founders with person pages and `part-of::` for a parent label.
	- ## Instance shape
		- Start each label page with `logseq-entity:: [[Logseq/Entity/Music/Label]]` and one H1 with the label's name, linked to its official site.
		- Add where the label is based, when it started, its founders, and a source link when known.
