alias:: [[ticketCLI]]
tags:: [[Task/Management/Git-Friendly]]

- [wedow/ticket: Fast, powerful, git-native ticket tracking in a single bash script. Dependency graphs, priority levels, zero setup.](https://github.com/wedow/ticket)
  title:: tk
	- [[CLI/Tool]] that implements a git-backed issue tracker for AI agents.
	- ## Data Model
		- [[Markdown Yaml Frontmatter]] files in `.tickets/`.
	- ## Notable
		- there's a "migrating from beads" section with a [[Beads]] [uninstall script](https://gist.github.com/banteg/1a539b88b3c8945cd71e4b958f319d8d) `migrate-beads`
		- Rooted in the Unix Philosophy
			- inspired by [[Person/Joe Armstrong/Blog/14/06/25/Minimal Viable Program]]
	- ## Features
		- supposedly allows managing and querying against complex issue dependency graphs (unverified)
	- ## [[Engineering]] decisions
		- written in [[Shell/Script]]; see the [ticket executable](https://github.com/wedow/ticket/blob/master/ticket).
		- uses [[Behavior/Driven/Development]] with the [[behave]] python library; see the [features directory](https://github.com/wedow/ticket/tree/master/features) for files such as [ticket_notes.feature](https://github.com/wedow/ticket/blob/master/features/ticket_notes.feature).
	-