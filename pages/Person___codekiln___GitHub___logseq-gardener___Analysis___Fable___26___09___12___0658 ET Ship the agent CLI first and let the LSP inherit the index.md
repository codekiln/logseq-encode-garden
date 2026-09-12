author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[My/Principle/CLI/Centricity]], [[Logseq/NeoVim/LSP]]

- # Ship the agent CLI first and let the LSP inherit the index
	- The Goals page names three primary use cases, and the Brief sequences them as page index, then LazyVim completion, then references, blocks, publisher, richer semantics, mutation, and concurrency. The order is right. This page argues for making the first shipped client the CLI that agents use in this repository, and for measuring the project by whether those agents stop grepping.
	- ## The client already in daily use is an agent
		- Every agent session in this garden checks whether a page exists by grepping `pages/` and `journals/`. The repository's own instructions say to, and the link-hygiene skill exists because agents invent wikilinks when the grep is skipped. That is the Brief's "agents should not need to independently rediscover Logseq semantics by grepping a graph" problem, and it happens here several times a day.
		- | What agents resolve today | Count in the encode garden |
		  | ---- | ---- |
		  | `[[wikilinks]]` | about 33,000 |
		  | blocks carrying an `id::` | about 500 |
	- ## First commands, chosen by what replaces a grep
		- `garden page exists "Logseq/Publish"` with an exit code, so a skill can call it in a shell condition.
		- `garden page complete "Logseq/Pub" --json`, the same query the LSP completion will send.
		- `garden page backlinks "Logseq/Publish" --json`.
		- `garden block get <uuid> --json`, returning the block, its page, and its source location.
		- With those commands, the core rule and the link-hygiene skill in this repository can call the CLI, and every agent session becomes a test run against the real corpus. That is [[My/Principle/Make the Right Thing Easy and the Wrong Thing Hard]] applied to the agents, and [[My/Principle/CLI/Centricity]] applied to the project.
	- ## Why the LSP comes second and costs little
		- The LazyVim `[[` completion is the feature that started this project, and it stays Phase 2. Completion over stdio is the `page complete` query with a different transport, so once the CLI answers it, the LSP adds a protocol adapter and no new semantics.
		- A CLI can be tested in CI with fixtures and by agents in this repository. An LSP can only be tested by a person sitting in Neovim until the CLI exists to compare against.
	- ## One cut to the Phase 1 list
		- `garden status` sits in the Phase 1 command list. Defer it until there is a background indexer whose state a person would ask about. If the cache design gets deferred as [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Measure the corpus before designing the cache]] proposes, `status` has nothing to report.
