logseq-entity:: [[Logseq/Entity/Definition]]
alias:: [[Subscribed Feed]]

- # Feed Subscribed
	- In this garden, **Feed Subscribed** marks a page whose subject publishes an [[RSS]] or Atom feed that belongs in my [[RSS/Reader]]. The marker carries the intent and the feed address; the reader holds the actual subscription.
	- ## What counts as an instance
		- A page for a blog, site, newsletter, [[Logseq/Entity/Podcast]], release channel, or [[Logseq/Entity/Repo]] that emits a feed worth following.
		- The marker is **additive**. It rides on whatever entity the page already is, listed after the primary one: `logseq-entity:: [[Logseq/Entity/Website]], [[Logseq/Entity/Feed/Subscribed]]`.
		- Not an instance: a single post — that is [[Logseq/Entity/Article]] or [[Logseq/Entity/Article/Blog]]. A feed read once and abandoned; drop the marker rather than recording a lapsed intent.
	- ## Naming and links
		- The type imposes no naming rule. An instance keeps the name its primary entity gives it, so a personal blog stays at `Person/<Name>/Blog` and its posts stay beneath it.
		- One instance per feed. A site publishing several feeds gets one page per feed only when the feeds are genuinely separate publications.
	- ## Frontmatter
		- **`feed-url::`** — required; the RSS or Atom URL a reader subscribes to, not the site's homepage. Find it from the homepage's `<link rel="alternate" type="application/rss+xml">`.
		- **`feed-last-sync-date::`** — optional; the date the subscription was last confirmed present in the reader, per [[Logseq/Date]]. Absent means unconfirmed.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- No shape of its own beyond the frontmatter. The primary entity's shape governs, with the feed named among the page's links.
	- ## Getting an instance into the reader
		- The set of intended subscriptions is the backlinks of this page, each carrying its `feed-url::`.
		- [[Readwise]] is the reader here, and it exposes no programmatic route to its subscriptions. The [[Readwise/CLI]] covers documents, highlights and tags only, and the [Reader API](https://readwise.io/reader_api) documents save, list, update, bulk update, delete, tags and webhooks — no feed endpoint on either.
		- What works instead: collect the unsynced `feed-url::` values into an [[OPML]] file and load it through [[Readwise/Reader/Preferences/Add to Feed/Upload OPML file]], or add a single feed by hand at [[Readwise/Reader/Preferences/Add to Feed]]. Then stamp `feed-last-sync-date::` on the pages that went in.
	- ## Relationship to other entity types
		- **[[Logseq/Entity/Website]]** — the usual primary type for a site whose feed is followed.
		- **[[Logseq/Entity/Article/Blog]]** — the individual posts that arrive through the feed; those pages are not instances of this type, their parent hub is.
		- **[[Logseq/Entity/Podcast]]** — a podcast's feed takes this marker the same way a blog's does.
		- **[[Logseq/Entity/Person]]** — a person hub is not the instance; the blog or site page beneath it is.
	- ## Examples in this garden
		- [[Person/Przemysław Szypowicz/Blog]]
