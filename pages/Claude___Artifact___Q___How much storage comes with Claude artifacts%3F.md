logseq-entity:: [[Logseq/Entity/Question]]

- # How much storage comes with Claude artifacts?
	- ## [[AI Answer]]
		- **Short answer:** 20 MB of persistent data per artifact, text only. Anthropic does not say whether personal and shared storage split that figure, or give a per-item or per-account total.
		- [[Answer/Official]] from [Anthropic: What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them).
			- The limit is 20 MB per artifact.
			- Storage takes text only: no images, files, or binary data. JSON strings fit.
			- Personal storage is private to each viewer; shared storage is the same data for everyone using the artifact.
			- It is offered on Pro, Max, Team, and Enterprise, on Claude web and Claude Desktop. Free is not listed.
			- Legacy artifacts store data only after publishing, and unpublishing deletes it permanently.
		- **Other documented limits**, for artifacts published from Claude Code
			- The rendered page must be 16 MiB or smaller, including embedded `data:` URIs. Source: [Claude Code Docs: Share session output as artifacts](https://code.claude.com/docs/en/artifacts).
			- The `assets` capability takes uploads of 20 MiB each (CSS and JS 16 MiB, SVG 2 MiB). This comes from the runtime capability notes in the Claude Code session, not from a public doc.
		- **Unverified:** I found no published cap on the number of documents or on total `db` capability size.
