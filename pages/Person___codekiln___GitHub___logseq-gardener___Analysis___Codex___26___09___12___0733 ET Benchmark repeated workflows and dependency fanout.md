author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Benchmark repeated workflows and dependency fanout
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Measure the corpus before designing the cache]] rightly asks for measurement. The response on the project hub also makes frontier performance an explicit interest. A whole-corpus parse time alone cannot settle the cache design or explain sluggish interaction.
	- ## Measure the work a person actually waits for
		- A persistent LSP pays startup cost once. An agent that invokes a short-lived CLI repeatedly may pay process startup, graph discovery, parsing, and JSON serialization on every lookup. A tolerable cold parse can become an expensive reading session.
		- Benchmark a realistic sequence of page resolution, backlinks, and block retrieval using separate processes. Compare an in-memory baseline, a persistent-cache path, and a batch request that resolves several names at once.
		- Include the wait for the first useful answer, slow-tail latency, memory, and total elapsed time. Distinguish a fresh application cache from an operating-system file cache that is already warm.
	- ## Corpus shape matters as well as size
		- Include a large page, a heavily referenced page, alias collisions, deeply nested blocks, and a reference cycle. A synthetic million-line garden made by repeating independent pages misses the dependencies most likely to make incremental updates expensive.
		- The Brief's “edit one file” invariant should separate reparsing from semantic invalidation. Renaming an alias target can change the meaning of references in many unchanged files. Updating an embedded block can affect multiple published pages.
		- Keep unresolved references indexed by their spelling so introducing a page or alias can resolve them without reparsing every source file. The affected semantic indexes still need updating.
	- ## Test foreground work under load
		- Request completion while a large file is being parsed and while a save invalidates many dependents. Background work needs bounded scheduling or cancellation if it can otherwise delay the foreground request.
		- This yields a better cache decision: which work must be reused across commands, which work can run in the background, and which work must yield when someone types. The simpler architecture should earn its place with these measurements.
