created-by:: [[Every]]
date-created:: [[2025/08/18]]
logseq-entity:: [[Logseq/Entity/Article]]

- # [My AI Had Already Fixed the Code Before I Saw It](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)
	- By Kieran Klaassen (GM of [[Cora]]); [[Source Code]] column at [[Every]].
	- ## Summary
		- Introduces **compounding engineering**: development systems with memory where PRs, bugs, and reviews permanently upgrade defaults—not one-off prompts.
		- Example: [[Claude/Code]] review comments cited prior PR patterns (naming, test scope, error handling) without being asked.
		- Contrasts short-term “prompt, ship, reset” AI coding with systems that make tomorrow faster than today.
	- ## Playbook (five steps)
		- 1. **Teach through work** — `CLAUDE.md` for taste; `llms.txt` for architecture-level rules.
		- 2. **Turn failures into upgrades** — fix + test + rule + eval so the category stays guarded.
		- 3. **Orchestrate in parallel** — plan / delegate / review lanes (e.g. three terminals).
		- 4. **Keep context lean but yours** — prune generic copied rules; ten specific beats one hundred generic.
		- 5. **Trust the process, verify output** — tests, evals, spot checks; teach the system when it errs.
	- ## Cora outcomes (claimed)
		- Feature ship time: **>1 week → 1–3 days** average over ~three months.
		- More bugs caught pre-production; PR review cycles **days → hours**.
	- ## Links
		- [[Engineer/ing/Compound]]
		- [[Person/Dan Shipper/Blog/25/12/11/Compound Engineering - How Every Codes With Agents]]