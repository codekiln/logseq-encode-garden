created-by:: [[Person/Dan Shipper]]
source-link:: https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents
date-created:: [[2025/12/11]]
logseq-entity:: [[Logseq/Entity/Article]]

- # [Compound Engineering: How Every Codes With Agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
	- Co-authored with Kieran Klaassen ([every.to/@kieran_1355](https://every.to/@kieran_1355)); updated 2026-04-06.
	- ## Summary
		- At [[Every]], essentially **100% of code is agent-written**; engineering shifts from typing to orchestrating agents in a **plan → work → review → compound** loop.
		- **Compound engineering** expects each feature to make the *next* feature easier by persisting lessons (bugs, failed tests, review insights) for future agents—while codebase complexity still grows, agent knowledge of the codebase grows faster.
		- Five in-house products run primarily by single owners serving thousands of users; claim: one developer with the right system can match ~five developers of a few years ago.
		- Open-sourced workflow: [[Person/Every/GitHub/compound-engineering-plugin]].
	- ## Notes
		- **Plan:** agents study repo structure, commit history, and external best practices before planning—most human time lives here.
		- **Review:** engineer judges output and meta-lessons, not just line-by-line nits.
		- **Compound:** capture what was learned so the next agent session inherits it (feeds into `CLAUDE.md`-style context and team memory).
		- Tool-agnostic framing: [[Claude Code]] primary internally; also Factory Droid and [[Codex/CLI]].
	- ## Links
		- [[Compound Engineering]]
		- [[Every/Blog/Source Code/25/08/18/My AI Had Already Fixed the Code Before I Saw It]] — earlier narrative on the same idea.
