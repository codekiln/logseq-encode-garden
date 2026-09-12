author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[CRDT]], [[My/Pref/Dev/Tool/git/Worktree]], [[My/AI/Rule/Dev Workflow with Git and Tmux]]

- # A Logseq-aware git merge driver before a CRDT
	- The Goals page says the implementation should support concurrent writes to the same block using [[CRDT]]s as a front end to the cache. The Brief says a CRDT is a long-term direction and no MVP dependency. Resolve the two pages in the Brief's favor, and add a smaller step before either.
	- ## How concurrent edits arrive today
		- Agents work in [[git/worktree]]s on their own branches and merge through pull requests, per [[My/AI/Rule/Dev Workflow with Git and Tmux]]. Two agents editing the same page meet at merge time, in git, as a textual conflict. A person edits in Logseq or nvim on main. The concurrency that exists is a merge problem, and git already has the extension point for it.
	- ## What a merge driver would do
		- Register a custom [merge driver](https://git-scm.com/docs/gitattributes#_defining_a_custom_merge_driver) for `pages/*.md` and `journals/*.md` through `.gitattributes`. Git hands it the base, ours, and theirs versions; the driver parses all three as block trees, matches blocks by `id::` when present and by parent path plus content otherwise, merges at block granularity, and leaves a textual conflict marker only inside a block both sides changed.
		- It is a small program over garden-core's parser and serializer, it runs wherever git runs, it needs no new storage layer, and it fits [[My/Principle/Simplify/Prefer Standards and Defaults]] and [[My/Principle/Simplify/Fewer and Deeper]]. It also serves the person in Logseq who merges an agent's branch.
	- ## What it settles before any CRDT
		- About five hundred blocks in the encode garden carry an `id::`; the rest have identity only by position. A merge driver forces the block-identity and ordering decisions the Brief lists for the CRDT phase, on real conflicts, while the cost of a wrong rule is one bad merge that git can undo.
		- [[My/Principle/Make Illegal States Unrepresentable]] applies once those rules exist: model a block's identity as a sum type, either an explicit UUID or a positional path, so no code path treats a positional block as stable across files.
