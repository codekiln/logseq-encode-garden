tags:: [[Claude/Desktop]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]

- # Where can I find the changelog for [[Claude/Desktop]] on the web?
	- ## [[AI Answer]]
		- [[Answer/Official]] from https://claude.com/docs/cowork/changelog
		- **Short answer:** [claude.com/docs/cowork/changelog](https://claude.com/docs/cowork/changelog) — its own page title is literally **"Release notes for Claude Desktop."** Each entry is a real Desktop build number (e.g. `v1.21459.3`, dated 2026-07-16) with changes grouped into **General / Code / Cowork / 3P** sections, so it's the one place that maps changes to actual Desktop app versions.
		- **How this differs from the CLI changelog and “what's new” pages the user already found:**
			- [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog) is the **Claude Code CLI** changelog — versioned against the CLI (e.g. `2.1.209`), not the Desktop app build number.
			- [code.claude.com/docs/en/whats-new](https://code.claude.com/docs/en/whats-new) is a **weekly dev digest for Claude Code**; each week is tagged with a CLI version range (e.g. `v2.1.202–v2.1.206`). It calls out Desktop-related features in prose (e.g. "In-app browser on Desktop," "Claude Desktop on Linux") but doesn't map those to Desktop version numbers — Desktop bundles its own embedded Claude Code engine on a separate release cadence, confirmed by cowork-changelog entries like "Updated the embedded Claude Code engine to the latest version."
			- [support.claude.com/en/articles/12138966-release-notes](https://support.claude.com/en/articles/12138966-release-notes) is a broader, less granular release-notes page spanning Claude web/mobile/Desktop/Cowork as one narrative feed, with no version numbers at all.
		- **Practical implication:** to find which Desktop build shipped a given fix, check the cowork changelog's version/date entries directly rather than trying to back-derive it from the CLI changelog or the weekly digest.