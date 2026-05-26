alias:: [[ticketCLI]]
tags:: [[Task/Management/Git-Friendly]]

- # [wedow/ticket: Fast, powerful, git-native ticket tracking in a single bash script. Dependency graphs, priority levels, zero setup.](https://github.com/wedow/ticket)
	- [[CLI/Tool]] that implements a git-backed issue tracker for AI agents.
	- ## Data Model
		- [[Markdown Yaml Frontmatter]] files in `.tickets/`.
	- ## [[My Notes]]
		- there's a ["migrating from beads" section of the README](https://github.com/wedow/ticket#migrating-from-beads) with a [[Beads]] [uninstall script](https://gist.github.com/banteg/1a539b88b3c8945cd71e4b958f319d8d) `migrate-beads`
		- Rooted in the [[Unix/Philosophy]]
			- inspired by [[Person/Joe Armstrong/Blog/14/06/25/Minimal Viable Program]]
		- as of [[2026-05-26 Tue]], hasn't been updated in two months, probably because it's got a small surface area
		- uses [[Behavior/Driven/Development]] with the [[behave]] python library; see the [features directory](https://github.com/wedow/ticket/tree/master/features) for files such as [ticket_notes.feature](https://github.com/wedow/ticket/blob/master/features/ticket_notes.feature).
	- ## Features
		- supposedly allows managing and querying against complex issue dependency graphs (unverified)
	- ## [[Engineering Choices]]
		- written in [[Shell/Script]]; see the [ticket executable](https://github.com/wedow/ticket/blob/master/ticket).
	- ## [[Installation]]
		- ### Getting the [[Exec/ut/able]]
			- [[brew]]
				- ```
				  brew tap wedow/tools
				  brew install ticket
				  ```
			- git clone and symlink, then git pull for updates
		- ### [[AI/Agent/Setup]]
			- [[Agents.md]]
				- > This project uses a CLI ticket system for task management. Run `tk help` when you need to use it.