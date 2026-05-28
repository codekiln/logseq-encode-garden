created-by:: [[Person/Dan Shipper]]
source-link:: https://every.to/p/after-automation
readwise-link:: https://read.readwise.io/new/read/01ksq4db7jpe953c6kc47279rt
date-created:: [[2026/05/21]]
logseq-entity:: [[Logseq/Entity/Article]]

- # [After Automation](https://every.to/p/after-automation)
	- By [[Person/Dan Shipper]] at [[Every]]; published 2026-05-21. Subtitle: *AI progress creates more work for humans, not less.*
	- ## Summary
		- Thesis: there is no tipping point where automation eliminates expert knowledge work—**the more Every automates, the more expert human work there is to do**.
		- AI **commoditizes the residue of past human expertise** (what was explicit enough to train on), which collapses the value of default model output and **raises demand for judgment, taste, and situation-specific difference**.
		- Work with agents splits into **agent employees** (delegated Slack/workflow agents; coworker vs embedded) and **human–agent collaboration OSes** ([[Codex/CLI]], [[Claude/Code]], Cowork)—the **human sandwich**: humans frame the task, steer/review, and decide what ships.
		- **Slop** is visible sameness at scale; abundance of cheap competence creates **status games for non-generic work**. Experts absorb the flood (review queues, evals, harnesses, CI) and also do **bigger work** enabled by models.
		- **Benchmarks measure models inside a frame** (the prompt). Saturation makes that frame cheap, which **stimulates more attempts** and more need for seniors to choose scope, migration, rollback, and whether a rewrite is warranted—the cycle repeats with a harder frame (**chart psychosis** if you only extrapolate curves).
		- Built on Every’s internal lab experience and the in-house **Senior Engineer** benchmark (vibe-coded Proof codebase rewrite); ties forward to [[Engineer/ing/Compound]] and prior **allocation economy** framing (2022).
	- ## Notes
		- **Every’s current stack:** ~30 people; Codex + Claude Code across coding, writing, design, support; alpha new models; agents answer ~95% of CEO email (still reviewed); Fin closed 40.1% of actionable support conversations in a May sample week without a human.
		- **Agent employees:** coworker agents (Claudie, Andy, Viktor, Plus One) vs embedded (Fin in support). Personal per-employee agents failed—agents need maintenance; team-owned agents stay fresh.
		- **Collaboration OS:** Dan runs SaaS (e.g. [[Cora]] email) inside Codex’s in-app browser; writing this essay in Proof with subagents for draft/research/edit; engineers live in agent pairing loops.
		- **Five-step commoditization loop:** cheap yesterday’s competence → rapid adoption (ops filing PRs, marketers making thumbnails) → sameness/slop → demand for difference/status → **new expert work** (review, sharpen, edit, build systems).
		- **Aliveness argument:** models know the **corpus** (already-done work); humans know what **needs doing now** with running wants/concerns—expert judgment stays structurally ahead.
		- **Senior Engineer benchmark:** agent gets broken vibe-coded production repo + plain-English “rewrite from first principles” prompt; GPT-5.5 hit 62/100 vs ~30 above prior Opus; score is **prompt-frame-dependent**—trivial to raise or zero by reframing.
		- **GDPval example:** impressive headline win rates, but tasks are frozen professional frames (e.g. audit sampling spreadsheet)—saturation shifts work to **experts adapting cheap frames to live problems**.
	- ## Links
		- [[Person/Dan Shipper/Blog/25/12/11/Compound Engineering - How Every Codes With Agents]]
		- [[Every/Blog/Source Code/25/08/18/My AI Had Already Fixed the Code Before I Saw It]]
		- [[Engineer/ing/Compound]]
		- [[Person/Every/GitHub/compound-engineering-plugin]]
		- [[AI/ES/25/11 Code/CODE/21 Fri/1700 Benchmarks vs economics the AI capability measurement gap]] — related lab-vs-field measurement theme
		- Author index: [every.to/@danshipper](https://every.to/@danshipper?sort=newest)
