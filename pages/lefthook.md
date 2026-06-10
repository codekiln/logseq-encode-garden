logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [lefthook](https://github.com/evilmartians/lefthook)
	- Fast, polyglot Git hooks manager: a single Go binary that runs hook commands (optionally in parallel) declared in a `lefthook.yml` at the repo root.
	- Installed and version-managed globally via [[mise]].
	- ## Use in this graph
		- A `pre-commit` hook runs the [[mise]] `secrets:scan` task over staged files to block commits that would add personal or employer identifiers to this public graph.
