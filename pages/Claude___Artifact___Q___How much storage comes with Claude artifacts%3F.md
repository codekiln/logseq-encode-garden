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
		- **Uploaded images and other files**
			- People who can edit an artifact can upload images, PDFs, and CSVs to it. [Claude Academy](https://academy.claude.com/tutorials/build-custom-artifacts-with-claude) says each artifact has a storage limit and sends readers to the Help Center for the amount; the help article gives only the 20 MB text-only figure, so whether uploads share that pool is unstated.
			- On Team and Enterprise, uploaded assets are stored persistently under the organization's data retention and deletion policies. [Artifacts admin guide](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans) lists no storage quota, per-file limit, or organization-wide cap, and shows no page for storage figures.
			- Artifact activity counts toward each user's usage limits, shared with the rest of Claude including Claude Code; there is no separate allowance. That covers usage, not stored bytes.
			- The 1 TB per-organization storage figure belongs to the developer Files API, not artifacts.
		- **Unverified:** I found no published cap on the number of documents, on total `db` capability size, or on organization-wide artifact storage. See [[Claude/Artifact/Q/How can I find my storage quota for Claude artifacts on seat-based Enterprise?]].
