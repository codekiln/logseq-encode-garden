author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]], [[My/Principle/Simplify]]

- # Measure the corpus before designing the cache
	- The [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] sizes the target at "well over a million lines" and builds its performance design on that figure: a persistent cache outside the graph, lazy activation, eager background warming, JIT reprioritization, progressive completeness levels, and Git-based reconciliation at startup. The gardens on this machine are much smaller than the figure.
	- ## What the two local gardens measure
		- | Graph | pages and journals | every .md file, including logseq/bak |
		  | ---- | ---- | ---- |
		  | [[Person/codekiln/GitHub/logseq-encode-garden]] | 106,381 lines (23 MB) | 240,430 lines |
		  | the private garden | 23,785 lines | 69,806 lines |
		- Counted on [[2026-09-12 Sat]] with `find <graph> -name '*.md' -print0 | xargs -0 cat | wc -l`.
		- If a work graph on another machine supplies the missing lines, name it and its size in the Brief. Otherwise the performance section is designed for a corpus about eight times larger than the one it will run on.
	- ## What a plain in-memory parse costs
		- [[Looksyk]]'s author scans and indexes a graph of about nine hundred pages in tens of milliseconds with no database at all, and says that is why Looksyk has none ([Idea and technical concept](https://sebastianrzk.codeberg.page/looksyk/idea_and_technical_concept/)). The encode garden is roughly twenty-five times that text, so a straight-line estimate puts a cold parse in Rust or OCaml at a second or two, paid once when a process starts.
		- A ripgrep pass that finds every `[[link]]` in the encode garden finishes in about a tenth of a second, which bounds the file-reading side of the work.
	- ## What to do
		- Spend the first hour of Phase 0 on a spike: parse the whole encode garden with [lsdoc](https://github.com/martinkoutecky/lsdoc) and with [mldoc](https://github.com/logseq/mldoc), time the cold parse, record peak memory, and write both numbers into the Brief.
		- Keep the in-memory index and file watching in the MVP. Add the persistent cache, the progressive levels, the JIT reprioritization, and the Git-based reconciliation only when the spike shows a cold parse a person would notice waiting for. Each of those is a subsystem to write, test, and keep working, and [[My/Principle/Simplify/Minimize Surface Area]] and [[My/Principle/Simplify/Fewer and Deeper]] argue for deleting them until a measurement asks for them back.
		- The Brief already says latency budgets should come from benchmarks on the encode garden rather than be invented up front. Apply the same rule to the cache architecture.
