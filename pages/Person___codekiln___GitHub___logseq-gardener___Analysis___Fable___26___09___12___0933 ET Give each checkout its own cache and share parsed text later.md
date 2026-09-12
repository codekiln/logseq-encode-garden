author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Keep editor buffers and worktrees separate in the shared cache]], [[My/Pref/Dev/Tool/git/Worktree]], [[My/Principle/Simplify/Minimize Surface Area]]

- # Give each checkout its own cache and share parsed text later
	- Codex's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Keep editor buffers and worktrees separate in the shared cache]] names a boundary the Brief leaves out: the saved files, an unsaved Neovim buffer, and an agent's worktree can hold different text for the same path. The editor half of the argument is right and is standard practice. The worktree half can be simpler than Codex proposes.
	- ## The editor keeps an overlay of open buffers
		- The LSP client sends the text of every open document, and that text wins over the file on disk until the document closes. rust-analyzer and other language servers keep those buffers as an overlay on top of a snapshot of the disk, and garden-core should take the same shape: a source of files that is either the checkout on disk or the checkout with an overlay of open buffers on top.
		- ~~~text
		  garden <command>:   Disk(checkout)                          -> index -> answer
		  garden lsp:         Disk(checkout) + Overlay(open buffers)  -> index -> answer
		  ~~~
		- This is how the plan in [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Ship the agent CLI first and let the LSP inherit the index]] still holds: the resolver, the index, and the cache are shared, and the LSP adds the overlay and document versions. A parse result that arrives for an older version of a buffer is discarded, as Codex says.
	- ## Each checkout gets its own cache directory
		- Codex proposes sharing parsed content between worktrees, keyed by content hash, while keeping file membership and reference indexes per checkout. I would leave the sharing out of the first version. Key the cache by the real path of the directory that holds `logseq/config.edn`, store it under `$XDG_CACHE_HOME/<tool>/<hash of that path>/`, and let each worktree pay one cold parse when it is created.
		- Worktrees in this repository live for one pull request, per [[My/Pref/Dev/Tool/git/Worktree]], so a per-worktree cold parse happens about as often as `git worktree add` does. A shared content store is a second index with its own eviction rules, and [[My/Principle/Simplify/Minimize Surface Area]] says to leave it out until a worktree's first command is slow enough that someone notices. The cold-parse measurement in [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Measure the corpus before designing the cache]] says whether that day comes.
		- Codex is right that configuration belongs in the key. `logseq/config.edn` decides how filenames and journal names become page names, so its hash sits beside the path in the cache identity, and changing it rebuilds the cache.
	- ## One fixture set serves both clients
		- Codex's protocol replay test for the editor is the right acceptance test. The CLI has the same test one layer down: a small fixture garden with expected JSON answers. The LSP replay applies an overlay to the same fixtures and checks that completion sees the unsaved alias while a command run beside it sees the saved graph.
