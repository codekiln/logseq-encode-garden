### `logseq-gardener` Project Goals
	- `garden` aims to create the fastest incremental and lazily-cached back-end for three primary use-cases:
		- 1 - an `garden` [[CLI]] for humans, agents and scripts to query and update [[Logseq/OG]]-style [[Knowledge Gardens]]
		- 2 - an `garden lsp` CLI-powered,  back-end for an [[LSP]] that can enable [[LazyVim]] to provide a [[Logseq]]-style user interface
			- an editor plugin starts `garden lsp` and keep that process around; no TCP sockets or ports or server set-up.
		- 3 - `garden publish` a cache-backed static HTML per-page output for SEO and indexing
	- `garden-core` should provide a parser, a graph model, and caching affordances.
		- It's meant to be as performant as possible, respecting that caching can start in the background the moment the engine knows about a garden, then incrementally enriched as each command is executed.
			- ```
			  graph activation
			        ↓
			  background mldoc outline parsing
			        ↓
			  in-memory page/ref index
			        ↓
			  [[ autocomplete
			  ```
	- The implementation should provide support for concurrent writes to the same file and even the same block, using [[CRDT]]s as a front-end to the cached backend.
-