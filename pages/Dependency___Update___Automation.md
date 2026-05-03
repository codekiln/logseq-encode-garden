logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Software/Composition/Analysis]], [[Security/DevSecOps/Taxonomy]]

- # Dependency update automation
	- ## Overview
		- **Dependency update automation** is the practice of keeping declared third-party packages, tools, and libraries **current** with **minimal human toil**: bots open pull requests, policies choose semver vs pinning, CI proves green builds, and humans review only the diffs that matter.
		- It sits beside **declaring** dependencies (manifests, lockfiles, registries like **[[aqua]]**) and **observing** them (**[[Software/Composition/Analysis]]**): automation answers *when and how* versions move forward, not only *what* you depend on.
	- ## Context
		- Common surfaces: **Dependabot**, **Renovate**, **Mend**/WhiteSource-style bots, package-manager `upgrade` hooks in CI, and **lockfile refresh** jobs after policy changes.
		- Supply-chain pressure (transitives, typosquatting, compromised releases) pushes teams toward **pinning + verified provenance**; automation must respect those constraints instead of blind “latest”.
		- Paired with **[[Software/Composition/Analysis]]** priorities, bots are a **mitigation layer**: they accelerate **known-good upgrades** after findings—not a substitute for composition visibility (see **[[Security/DevSecOps/Taxonomy]]**).
	- ## Key Principles
		- **Policy before bots** — Default branch rules (allowed majors, grouping, ignore lists) prevent noise and surprise upgrades.
		- **Prove with CI** — Automated bumps should run the same tests, linters, and integration checks as human-driven changes.
		- **Human gate for risk** — Breaking semver, native binaries, and security-sensitive deps still warrant review even when bots draft the PR.
	- ## Mechanism
		- **Discovery** — Parse manifests and lockfiles; resolve newer versions against registry metadata and (optionally) advisory feeds.
		- **Patch proposal** — Open PRs with changelog links, diff stats, and co-authored attribution; optionally batch or stagger cadence.
		- **Merge and deploy** — Auto-merge only when policy + checks pass; otherwise queue for maintainer.
	- ## Examples
		- Renovate on a **[[Monorepo]]** with grouped devDependency bumps weekly, runtime deps daily.
		- `mise lock` / lockfile-first flows where CI fails on **stale** pins until a bot refreshes hashes.
	- ## Misconceptions
		- “**Always latest** is always safest” — **False** without verification; freshness trades off against **stability** and **review bandwidth**.
		- “Bots replace **[[Software/Composition/Analysis]]**” — **False**; updates change the graph, but **SCA** still tells you whether that graph is **licensed**, **vulnerable**, or **unmaintained**.