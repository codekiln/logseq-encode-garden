author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Codex]], [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]]

- # Where my plan agrees with Codex's proposal and where it departs
	- [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Codex]] and [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]] describe the same engine and most of the same clients. This page lists what I would take from Codex's proposal as written and the places where my plan makes a different call, so that each one can be decided on its own.
	- ## Taken as written
		- `garden impact`, under the name `garden diff`, as the first feature after reading and navigation, for the reasons on [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Call the impact command garden diff and run it where the link checker runs]].
		- The overlay of unsaved editor buffers over the saved graph, and separate views per checkout.
		- Typed resolve results that separate a match, an ambiguous name, no match, and an index still warming.
		- The publisher's feature-support report, and its rule that an unsupported query looks different from an empty one.
		- Editing commands that keep untouched bytes, check the source revision before writing, and record enough to finish or undo a multi-file rename.
		- A persistent index that short-lived commands reuse, which [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Agents calling the CLI justify a persistent cache on a small garden]] now agrees with.
	- ## Where I would decide differently
		- ### Publishing comes earlier
			- Codex sequences publishing after `garden impact` and the editing commands. I would run Tine's static export against the encode garden in the first week, because the published site's problem is concrete today and the trial costs an hour, and then schedule `garden export` after the reference graph and before mutations.
		- ### Concurrency starts in git
			- Codex proposes a shared editing session in which clients exchange operations with explicit block identities. Concurrent edits in this repository meet at merge time in git, so I would build the block-aware merge driver first, per [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET A Logseq-aware git merge driver before a CRDT]], and open the session experiment when a merge the driver cannot settle shows up in practice.
		- ### Pick the tool's name before anyone installs the binary
			- Codex's proposal keeps `garden` throughout. The collisions in [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET One tool carries four names and two of them collide]] stand, and renaming gets expensive once someone has installed the binary.
		- ### Sharing parsed text across worktrees waits
			- Codex keys shared parse artifacts by content hash. I would give each checkout its own cache directory and add sharing when a worktree's first command is measured slow, per [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Give each checkout its own cache and share parsed text later]].
		- ### Name the tool that runs each parser test
			- Codex evaluates parsers against syntax, the resulting graph, and text preservation. My plan names the tool that runs each test: lsdoc's differential check, a dump from Logseq's own graph-parser under nbb-logseq, and a byte-identical round trip through tine-core's serializer, per [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Use Logseq's own graph-parser as the oracle and require a byte-identical round trip]].
