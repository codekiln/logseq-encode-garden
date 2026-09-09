logseq-entity:: [[Logseq/Entity/Concept]]

- # [Stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
	- ## Overview
		- A **stack** is a chain of two or more pull requests in the same repository, where each layer depends on the one below it. The bottom pull request targets the stack's trunk (usually `main`, or another base such as a release branch). Each subsequent pull request targets the branch of the pull request below it.
		- Foundational changes — shared types, schema, core logic — live in lower layers. Dependent work — API routes, UI, tests that need that foundation — lives in higher layers.
		- Each pull request is a discrete, reviewable change. Reviewers see only the diff between that layer and the branch below it, not the whole stack at once.
		- Status as of the docs: **public preview**, subject to change. All branches must live in the same repository; cross-fork stacks and GitHub Desktop are not supported.
	- ## Context
		- Large features often need several sequential changes. Without stacks, the next change either waits for the previous pull request to merge, or everything lands in one oversized branch.
		- Hand-rolled dependent pull requests create extra work: keeping branches rebased, figuring out which CI and protection rules actually apply mid-stack, and reviewing one layer without stack context.
		- Stacks treat the chain as a connected unit while keeping each layer small. They also map cleanly onto high-volume or agent-driven work: one focused task per pull request, with dependencies recorded as the stack itself.
	- ## Key Principles
		- **Dependency direction.** If code in one layer depends on code in another, that dependency must sit in the same branch or a lower one.
		- **Split on concern or size.** Open a new branch when the work switches concern (backend → frontend, core → tests) or when the current branch is already large enough to review on its own.
		- **Merge bottom-up.** Pull requests merge from the bottom of the stack upward. Merging a mid-stack or top pull request can bring lower layers with it; upper layers that stay open retarget automatically.
		- **Same quality bar for every layer.** Branch protection (for example CODEOWNER approvals) and CI that apply to the trunk also apply to mid-stack pull requests, not only the bottom one.
	- ## Mechanism
		- ### Branch chain
			- ~~~text
			     ┌── feat/frontend     → PR #3 (base: feat/api-endpoints)  ← top
			    ┌── feat/api-endpoints → PR #2 (base: feat/auth-layer)
			   ┌── feat/auth-layer     → PR #1 (base: main)               ← bottom
			  main (trunk)
			  ~~~
		- ### Rebase
			- Cascading rebase is the hard part of stacks; GitHub handles it server-side from the pull request UI, or locally via the `gh stack` extension. After the bottom pull request merges, remaining branches rebase so the next open pull request targets the trunk.
		- ### Surfaces
			- **Website.** A stack icon and layer number on the pull request; a stack map in the merge box for status and one-click navigation (trunk at the bottom).
			- **[[GitHub/CLI]].** The `gh stack` extension creates and tracks branches in dependency order, rebases, pushes, submits linked pull requests, and moves between layers.
			- **APIs and automation.** Webhooks expose a `stack` object on `pull_request` events; REST can list, create, extend, and dissolve stacks; GraphQL exposes read-only stack fields. Agents can use the `gh-stack` skill.
		- ### Merging
			- Merge the whole stack by merging the top pull request (lower layers come with it).
			- Merge a prefix by merging a mid-stack pull request; layers above stay open and retarget the trunk.
			- Supports merge commit, squash, and rebase; merge-queue aware. History matches merging each pull request individually from the bottom.
			- API merges that participate in stacks use the asynchronous merge API for stacks.
		- ### Local CLI sketch
			- ~~~
			  gh extension install github/gh-stack
			  gh stack alias
			  gs init auth-layer
			  gs add api-routes
			  gs add frontend
			  gs push
			  gs submit
			  ~~~
	- ## Examples
		- Auth layer on `main` → API endpoints based on the auth branch → frontend based on the API branch: three pull requests, each reviewable alone, each only showing its own layer's diff.
		- An agent finishes one task, then starts the next that depends on it: each task becomes one pull request in the stack instead of one combined branch.
	- ## Misconceptions
		- **"Every layer must merge together."** The stack need not merge at once, but merges must proceed bottom-up.
		- **"Mid-stack pull requests skip trunk rules and CI."** Requirements follow the bottom pull request's base branch; protection and trunk-triggered checks apply across the stack.
		- **"A stack can span forks."** Branches must be in the same repository.
		- **"GitHub Desktop can manage stacks."** Stacked pull requests are available in the CLI, website, Mobile, and APIs — not Desktop.
	- ## Sources
		- [About stacked pull requests - GitHub Docs](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
		- [GitHub Stacked PRs / gh-stack](https://github.github.com/gh-stack/)
