author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Resolve pages through evidence from the whole graph
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Ship the agent CLI first and let the LSP inherit the index]] proposes a page-existence command. The useful answer needs to explain how a name exists. A page can have a source file, be named by references, appear as a namespace ancestor, or resolve through an alias. Several of those can apply together.
	- ## The garden already exposes the distinction
		- [[CLI]] appears in the [[Person/codekiln/GitHub/logseq-gardener/Project/Goals]], but there is no corresponding page file. A file-only lookup would reject a name the graph already uses.
		- The current [link checker's page-index and classify functions](https://github.com/codekiln/logseq-encode-garden/blob/07bda4f2/.rulesync/skills/logseq-link-hygiene/scripts/resolve-wikilinks.cljs#L63) build their title index from files under `pages/`. Reference-only pages are absent from that index. Exact alias lookup also stores a single target, so conflicting alias declarations can overwrite one another before the ambiguity check runs.
		- Logseq's [build-pages-aux](https://github.com/logseq/logseq/blob/63b76c5db4e7b710551c8c1ba7a4f00e5b94bb0b/deps/graph-parser/src/logseq/graph_parser/extract.cljc#L189) combines the file's page, pages found through references, and namespace ancestors. That is a concrete semantic baseline for the replacement.
	- ## What the resolver should return
		- Return the matched identity, all contributing evidence with source locations, any content file, and competing candidates. Model evidence as a collection: a page may have both a file and incoming references.
		- Distinguish a complete search with no match from an incomplete index. Completion can offer provisional candidates; a creation or rename check needs a complete answer for the relevant scope.
		- Retain all alias claimants. Keep fuzzy suggestions separate from resolution so punctuation normalization cannot silently turn a typo into a different page.
	- ## The decision this changes
		- Put reference extraction, alias handling, and namespace identity into the earliest useful resolver. The Brief's later reference phase can add navigation and richer queries, but page existence already depends on graph-wide evidence.
		- A reference-only page is valid graph structure. Whether a newly introduced spelling deserves a warning is an editorial policy, which should compare the proposed change with the existing garden.
