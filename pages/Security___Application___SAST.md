logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Security/DevSecOps/Taxonomy]], [[Security/Application/DAST]], [[Software/Composition/Analysis]]

- # Static application security testing (SAST)
	- ## Overview
		- **SAST** analyzes **first-party source code** (and sometimes bytecode/IR) **without executing** the full app: dataflow, control flow, pattern rules, taint tracking, and policy checks to flag classes like injection, unsafe crypto, or auth mistakes.
		- Contrast with **[[Software/Composition/Analysis]]**, which targets **dependencies you import**, and **[[Security/Application/DAST]]**, which targets **running behavior**.
	- ## Context
		- Runs in **IDE**, **pre-commit**, or **CI** on each change; noisy without tuning; benefits from **reachable-path** pruning where tools support it.
		- **Automated fix** beyond inline hints is **less common** than dependency PR bots; see **[[Security/DevSecOps/Taxonomy]]** for how suites sometimes market cross-signal remediation.
	- ## Misconceptions
		- “**SAST replaces SCA**” — **False**; they answer different questions (your code vs their code).
		- “**Clean SAST = safe release**” — **False** without **DAST**, **composition analysis**, and **operational** hardening.
