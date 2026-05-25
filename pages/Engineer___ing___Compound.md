logseq-entity:: [[Logseq/Entity/concept]]
alias:: [[Compound Engineering]]

- # Compound engineering
	- Development approach from [[Every]]: each unit of engineering work should make the next unit **easier**, not harder—by documenting bugs, review lessons, and patterns so agents and humans compound context over time.
	- Contrast with traditional engineering, where each feature tends to add complexity and local knowledge debt.
	- ## Loop
		- 1. **Plan** — agents read issues, research approaches, synthesize implementation plans (codebase + commit history + external best practices).
		- 2. **Work** — agents implement and test against the plan.
		- 3. **Review** — engineer reviews output and lessons learned.
		- 4. **Compound** — feed results back into the system (`CLAUDE.md`, `llms.txt`, evals, rules) so the next loop starts smarter.
		- Roughly **80%** plan + review, **20%** work + compound.
	- ## Tooling
		- Primary stack at Every includes [[Claude Code]], [[Codex/CLI]], and Factory [[Droid]]; packaged for others as [[Person/Every/GitHub/compound-engineering-plugin]] ([[Codex/Plugin]] marketplace: `EveryInc/compound-engineering-plugin`).
	- ## Sources
		- [[Person/Dan Shipper/Blog/25/12/11/Compound Engineering - How Every Codes With Agents]]
		- [[Every/Blog/Source Code/25/08/18/My AI Had Already Fixed the Code Before I Saw It]]