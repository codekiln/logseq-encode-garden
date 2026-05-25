logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Every]]
date-created:: [[2025/12/11]]

- # [EveryInc/compound-engineering-plugin: Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more](https://github.com/EveryInc/compound-engineering-plugin)
	- Ships the [[Compound Engineering]] workflow as skills and agents across [[Claude Code]], [[Codex/CLI]], [[CursorAI]], and related tools.
	- npm: [@every-env/compound-plugin](https://www.npmjs.com/package/@every-env/compound-plugin)
	- Philosophy: **each unit of engineering work should make subsequent units easier** — plan and review heavily, codify learnings, keep quality high so future changes stay cheap.
	- ## Core skills (slash commands)
		- `/ce-strategy` — maintain `STRATEGY.md` (problem, approach, persona, metrics, tracks).
		- `/ce-ideate` — optional big-picture ideation before brainstorming.
		- `/ce-brainstorm` — interactive requirements doc before planning.
		- `/ce-plan` — implementation plans from ideas or requirements docs.
		- `/ce-work` — execute plans (worktrees, task tracking).
		- `/ce-debug` — reproduce, trace, fix failures.
		- `/ce-code-review` / `/ce-doc-review` — multi-agent review.
		- `/ce-compound` — document learnings for the next cycle.
		- `/ce-product-pulse` — time-windowed usage/performance/error pulse reports → `docs/pulse-reports/`.
		- `/ce-setup` — environment check and project bootstrap after install.
	- ## Install (sketch)
		- **Claude Code:** `/plugin marketplace add EveryInc/compound-engineering-plugin` then `/plugin install compound-engineering`.
		- **Cursor:** `/add-plugin compound-engineering` or marketplace search.
		- **Codex:** `codex plugin marketplace add EveryInc/compound-engineering-plugin`; `bunx @every-env/compound-plugin install compound-engineering --to codex`; then install plugin via Codex `/plugins` TUI (skills + agents are separate steps). See [[Codex/Plugin]].
	- ## Essays
		- [[Person/Dan Shipper/Blog/25/12/11/Compound Engineering - How Every Codes With Agents]]
		- [[Every/Blog/Source Code/25/08/18/My AI Had Already Fixed the Code Before I Saw It]]
