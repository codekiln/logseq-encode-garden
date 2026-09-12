author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Test graph meaning and preserve the original source text
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Pick the parser first and let the language follow]] makes differential comparison with mldoc the parser decision. That is a useful syntax test. The [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] promises compatibility with a knowledge graph, which needs another comparison after syntax parsing.
	- ## Graph construction adds behavior
		- In the inspected Logseq source, [get-page-name](https://github.com/logseq/logseq/blob/63b76c5db4e7b710551c8c1ba7a4f00e5b94bb0b/deps/graph-parser/src/logseq/graph_parser/extract.cljc#L85) applies title and filename precedence, [extract-page-alias-and-tags](https://github.com/logseq/logseq/blob/63b76c5db4e7b710551c8c1ba7a4f00e5b94bb0b/deps/graph-parser/src/logseq/graph_parser/extract.cljc#L120) creates alias and tag relationships, and [extract-pages-and-blocks](https://github.com/logseq/logseq/blob/63b76c5db4e7b710551c8c1ba7a4f00e5b94bb0b/deps/graph-parser/src/logseq/graph_parser/extract.cljc#L228) handles journal conversion, block ordering, and duplicate block IDs. Those operations sit above the Markdown AST.
		- Pin a Logseq reference revision and compare observable answers: page identities, alias candidates, parent-child relationships, backlinks, and explicit UUID resolution. Normalize generated internal IDs where they are incidental to the behavior being tested.
		- Exercise edits as well as initial loads. After removing an alias, moving a referenced block, or deleting the last reference to a fileless page, compare the incremental result with a clean rebuild. An index can pass every cold-parse fixture and still retain stale relationships.
	- ## Writing later changes what must be retained now
		- The Brief already asks future mutations to preview the minimum source-file change. An AST that discards original spacing, property order, delimiters, or unfamiliar syntax cannot supply that promise by itself.
		- Retain original text and reliable source spans beside the semantic model. Eventually, patch the affected range and preserve untouched bytes. A no-op rewrite should be byte-identical; a small property edit should produce a small diff.
		- Include imperfect files in the fixtures. An unsupported construct should remain recoverable as source text, with an explicit limit on what the engine understands.
	- ## How this changes the parser decision
		- Evaluate syntax fidelity, graph behavior, and suitability for minimal edits separately. A parser can be excellent for lookup while needing an additional source-preservation layer for mutation.
		- Favor a design that can explain disagreements with the reference implementation. Copying Logseq's automatic duplicate-ID repair into a read-only tool, for example, would conceal a conflict the caller needs to see.
