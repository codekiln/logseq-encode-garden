logseq-entity:: [[Logseq/Entity/Software/Project]]
tags:: [[Agent/Skills/Marketplace]]
created-by:: [[Person/mahidalhan]]
see-also:: [[Person/forztf/GitHub/open-skilled-sdd]], [[Person/Elon Musk/First-Principles Framework]]

- # [mahidalhan/claude-hacks](https://github.com/mahidalhan/claude-hacks)
	- Skills, slash commands, and utility hacks for [[Claude/Code]], distributed as a plugin marketplace (install via `/plugin marketplace add mahidalhan/claude-hacks`).
	- Originally published as `skilled-spec`; cited in [[Person/forztf/GitHub/open-skilled-sdd]] README as the "Original English version" that inspired open-skilled-sdd's skill-based approach.
	- ## Notable skills
		- `architecture-introspector` — applies [[Person/Elon Musk/First-Principles Framework]] (Question → Delete → Simplify → Accelerate → Automate) to analyze and simplify software architecture; triggered via `/analyze-architecture`
		- `exa-code-context` — real code search via Exa API (`EXA_API_KEY` required)
		- `explainer` / `threaded-explainer` — recursive and chunked explanations with comprehension checks
		- `skill-creator` — scaffold new skills via `/create-skill`
	- ## Plugin groups
		- `code-intelligence` — architecture analysis + code search
		- `learning-tools` — interactive teaching
		- `creative-tools` — diagrams, UI design, generative art, ASCII explanations
		- `workflow-tools` — session handoffs, planning, orchestration, standup summaries
		- `skill-tools` — skill scaffolding
		- `git-tools` — semantic commits, PR descriptions
	- ## Zero-install hacks
		- `statusline.sh` — custom [[Claude/Code]] status line (directory, model, context %, git status, cost)
		- `publish-skill` — publish skills from any project to a personal marketplace repo
	- ## See also
		- [[Person/Elon Musk/First-Principles Framework]]
		- [[Person/forztf/GitHub/open-skilled-sdd]]
		- [[Vercel/Skills]]
