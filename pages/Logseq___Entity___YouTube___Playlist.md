logseq-entity:: [[Logseq/Entity/Definition]]

- # YouTube Playlist
	- In this garden, **YouTube Playlist** pages model one identifiable playlist published on YouTube.
	- ## Identity and scope
		- The YouTube `list` ID is the deduplication key. Search playlist URLs and existing hub pages before creating a second page for a different name for the same playlist.
		- An informal list of video links without a YouTube playlist ID is a collection or series, but not a YouTube Playlist instance.
	- ## Relationship to [[Logseq/Entity/Series]]
		- An ordered playlist declares `logseq-entity::` with [[Logseq/Entity/YouTube/Playlist]] first and [[Logseq/Entity/Series]] second. The playlist hub is the one external work and the named sequence; member videos remain distinct [[Logseq/Entity/YouTube]] pages.
		- Prefer a hub near its member videos, often `<creator>/YouTube/Series/<name>`; retain a requested or established path when it is already the series hub. Put a published ordinal on members only when the playlist or publisher uses one.
	- ## Frontmatter and page shape
		- Shared property conventions live on [[Logseq/Frontmatter]]. Add a verifiable `date-created::` and creation-year link when the playlist's own creation date is known; the date of its oldest video does not establish the playlist's creation date.
		- Lead with a bullet-wrapped H1 linked to the playlist URL. Describe the scope briefly and list member video page links in playlist order when known.
