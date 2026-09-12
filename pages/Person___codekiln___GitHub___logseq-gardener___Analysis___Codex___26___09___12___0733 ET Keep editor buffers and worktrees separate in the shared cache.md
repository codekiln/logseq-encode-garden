author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Keep editor buffers and worktrees separate in the shared cache
	- The [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] wants editors, scripts, and agents to reuse a cache. The missing boundary is which version of the garden each client means. Saved files, an unsaved Neovim buffer, and an agent's worktree can all contain different text for the same relative path.
	- ## An editor owns its unsaved text
		- The [LSP document-open contract](https://github.com/microsoft/language-server-protocol/blob/gh-pages/_specifications/lsp/3.17/textDocument/didOpen.md) makes the client's supplied text authoritative for an open document. [Document changes carry versions](https://github.com/microsoft/language-server-protocol/blob/gh-pages/_specifications/lsp/3.17/textDocument/didChange.md), so a completion request can be answered against the synchronized buffer.
		- If someone changes a page's `alias::` in Neovim, editor completion should reflect the unsaved alias while a separate CLI invocation still sees the saved graph. Writing the editor's transient interpretation into a shared current-state index would mix those views.
		- Give each editor session a buffer layer over the saved graph. Track document versions, and discard an older parse result if a newer version has arrived. The core can expose parsing from supplied text while the LSP manages the document lifecycle.
	- ## A worktree is a different saved graph
		- [[My/Pref/Dev/Tool/git/Worktree]] makes multiple checkouts part of the expected workflow. A repository identity or Git commit alone cannot identify the current graph: worktrees at the same commit can have different uncommitted edits.
		- Identify each checkout separately. If parse artifacts are shared, key them by content and every relevant parser input; retain checkout-specific file membership, configuration, and reference indexes.
		- Configuration belongs in invalidation too. Changing filename or journal-title interpretation can change identities even when no Markdown file changed.
	- ## The editor acceptance test
		- Replay open, change, completion, save, and close messages in an automated protocol test. Include unsaved aliases, an unfinished link, a Unicode character before the cursor, and a delayed parse arriving after newer text.
		- This qualifies Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Ship the agent CLI first and let the LSP inherit the index]]: the resolver can be shared, but correct editor behavior also needs document ownership and version handling. A protocol replay can test that behavior before a person opens Neovim.
