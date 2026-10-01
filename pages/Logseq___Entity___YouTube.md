logseq-entity:: [[Logseq/Entity/Definition]]

- # YouTube Video
	- In this garden, **YouTube Video** pages model one identifiable video published on YouTube.
	- ## Identity and scope
		- The YouTube video ID is the deduplication key. Search `youtube.com/watch?v=<id>` and `youtu.be/<id>` across pages before creating a page, regardless of title, channel, or page namespace.
		- A page that merely embeds or cites a video while documenting another subject is not a YouTube Video instance. A raw transcript child page is part of its parent video's notes, not a second video entity.
	- ## Naming
		- Prefer `<creator>/YouTube/<YY>/<MM>/<short title>` when the publishing creator and publication month are known. The creator may be a person, company, organization, or software project. Preserve an established video page's path when marking an existing instance.
		- A video in an ordered run can instead live beneath a series hub, with a published ordinal before its short title. [[Logseq/Entity/Series]] governs ordinals and ordering.
	- ## Frontmatter
		- `logseq-entity::` with [[Logseq/Entity/YouTube]] marks a video. Add [[Logseq/Entity/Series]] after it when the video is an installment of an ordered series.
		- Record `date-created::` from the video's publication date when verifiable. Link its known year through `logseq-created-time-year::` to a matching [[Logseq/Entity/Time/Year]] page. Shared property conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- Lead with a bullet-wrapped H1 that links to the video's watch URL. Name the publisher or speaker when known; keep any synopsis and notes beneath the heading.
		- A `{{video ...}}` block is useful when inline playback or timestamped notes are part of the page. Notes with clickable `{{youtube-timestamp ...}}` headings nest beneath that video block.
	- ## Combined with Podcast Episode
		- A video that is also a podcast episode lists [[Logseq/Entity/Podcast/Episode]] first. That page holds the shape for the combination: video seconds as the clock, chapters as headings, snips, highlights, and frames for what only the video shows.
	- ## Related type
		- A YouTube playlist is a separate entity modeled by [[Logseq/Entity/YouTube/Playlist]]. A video's playlist membership does not change its video identity.
