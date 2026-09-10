logseq-entity:: [[Logseq/Entity/Term]]

- # documentHighlight
	- A [[LSP]] server capability (`textDocument/documentHighlight`) that returns every other occurrence of the symbol under the cursor within the current buffer, so a client can highlight or cycle through them without a separate references request.
	- [[nvim/Plugin/snacks.nvim/Words]] builds its `]]` / `[[` cycling on top of this capability — it has nothing to cycle through when the attached server doesn't advertise it.