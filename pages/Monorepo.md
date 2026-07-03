logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[nx]], [[GitHub/vercel/turborepo]], [[Dependency/Update/Automation]], [[Security/DevSecOps/Taxonomy]]

- # Monorepo
	- ## Overview
		- A **monorepo** (monolithic repository) keeps **many related packages, apps, or services** in **one version-control root** instead of splitting each unit into its own repo.
		- Teams choose it to share **CI**, **lint/format rules**, **internal libraries**, and **atomic cross-package changes**—especially when releases must move several modules in lockstep.
	- ## Context
		- Common in **large product companies** and open ecosystems (JS/TS with **[[nx]]** or **[[GitHub/vercel/turborepo]]**, **Python** workspaces, **Rust** workspaces, **Go** multi-module layouts).
		- Tension with **multi-repo**: monorepos reduce cross-repo coordination cost but raise demands on **build graph performance**, **access control**, and **[[Dependency/Update/Automation]]** / **[[Software/Composition/Analysis]]** at scale.
	- ## Key Principles
		- **Workspace boundaries** — Clear package names, ownership, and dependency rules so the graph stays navigable.
		- **Task graph + caching** — Incremental builds and remote cache (where available) keep CI and local dev tractable.
		- **Policy for internal APIs** — Shared libraries need semver or explicit consumer contracts so refactors do not silently break distant packages.
	- ## Mechanism
		- **Workspace manifests** — `pnpm`/`yarn`/`npm` workspaces, **Poetry** / **uv** workspace tables, **Cargo** workspaces, **Bazel**/Buck-style targets, etc., declare how packages resolve each other.
		- **Orchestrators** — Tools like **[[nx]]** and **[[GitHub/vercel/turborepo]]** schedule tasks, fan out tests, and dedupe work across the tree.
		- **CI fan-out** — Path filters, affected-only pipelines, and merge queues prevent “every push rebuilds the world” unless necessary.
	- ## Examples
		- One Git root shipping a **mobile app**, **web app**, and **shared design-system package** with a single design-token bump spanning all three.
		- **[[PyPoetry/Concept/How to handle Monorepos in Poetry vs uv]]** — language-specific packaging trade-offs inside a Python workspace.
	- ## Misconceptions
		- “**Monorepo = one deployable**” — **False**; many deployables can live in one repo with separate release cadences.
		- “**Monorepo fixes all coordination**” — **Oversold**; you still need **ownership**, **boundaries**, and tooling discipline or the tree becomes a **big ball of mud**.