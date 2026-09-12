author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Benchmark repeated commands and edits to widely linked pages
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Measure the corpus before designing the cache]] rightly asks for measurement. The response on the project hub also makes frontier performance an explicit interest. A whole-corpus parse time alone cannot settle the cache design or explain sluggish interaction.
	- ## Measure the work a person actually waits for
		- A persistent LSP pays startup cost once. An agent that invokes a short-lived CLI repeatedly may pay process startup, graph discovery, parsing, and JSON serialization on every lookup. A tolerable cold parse can become an expensive reading session.
		- Benchmark a realistic sequence of page resolution, backlinks, and block retrieval using separate processes. Compare an in-memory baseline, a persistent-cache path, and a batch request that resolves several names at once.
		- Record how soon the first useful answer arrives, how long the slowest requests take, memory use, and total elapsed time. Test both after clearing the application's cache and when the operating system already has the files in memory.
	- ## Corpus shape matters as well as size
		- Include a large page, a heavily referenced page, alias collisions, deeply nested blocks, and a reference cycle. A synthetic million-line garden made by repeating independent pages misses the dependencies most likely to make incremental updates expensive.
		- After an edit, the engine needs to read and parse the changed file. It also needs to check whether that edit changes where links in other files lead. Suppose Studio declares Workshop as an alias and a journal links to Workshop. Removing the alias changes the journal link's target even though the journal file is unchanged. The engine can reuse the journal's already-parsed text, but it must look up the link's target again.
		- Keep a lookup from each referenced name to the source blocks that use it, including names with no content file. When an alias is added or removed, that lookup identifies the links to check. Benchmark both the time to parse the edited file and the time until affected links return the updated results.
	- ## Test foreground work under load
		- Request completion while a large file is being parsed and while a save causes many links to be checked again. Background work should pause between small batches, or cancel obsolete work, so the completion request can run promptly.
		- Use these measurements to decide which work to reuse across commands, which work can run in the background, and when that work must pause so someone can type without waiting.
