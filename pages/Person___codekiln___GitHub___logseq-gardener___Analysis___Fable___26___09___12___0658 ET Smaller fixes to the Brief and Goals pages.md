author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]], [[Person/codekiln/GitHub/logseq-gardener/Project/Goals]]

- # Smaller fixes to the Brief and Goals pages
	- Each item here is a one-line change or a short rewrite. The larger arguments are on the sibling pages under this namespace.
	- ## Design details
		- Put the cache under `$XDG_CACHE_HOME/<tool>/<graph-id>/`, with `~/.cache` as the fallback the [[XDG]] spec defines, per [[My/Pref/Dev/Tool/Prefer XDG-Compliant CLI Tools]].
		- Discover a graph the way git discovers `.git`: walk up from the current directory to the nearest `logseq/config.edn`, and accept an explicit `--graph <path>` that wins. The Brief's "strong evidence that the garden is being used" is a heuristic where [[My/Principle/Explicit is better than Implicit]] wants a rule.
		- Make graph scope a required argument in the core API rather than a default, so cross-graph behavior cannot happen by accident. The Brief asks for that outcome, and [[My/Principle/Make Illegal States Unrepresentable]] is how to get it.
		- Model provisional versus resolved results as a type on the return value, so a caller cannot read a provisional answer as final.
	- ## Fixtures that already exist
		- This garden's `logseq/config.edn` sets `:file/name-format :triple-lowbar`. Logseq's graph-parser handles that format and a legacy one in [extract.cljc](https://github.com/logseq/logseq/blob/master/deps/graph-parser/src/logseq/graph_parser/extract.cljc), so the compatibility fixtures need both.
		- [og_import_graph_cases.md](https://github.com/logseq/logseq/blob/master/docs/og_import_graph_cases.md) classifies the file-graph importer's known issue classes with regression tests, and the [graph-parser test graphs](https://github.com/logseq/logseq/tree/master/deps/graph-parser/test/resources) are small deterministic fixtures. Both answer the Brief's question about which malformed or legacy constructs must be tolerated.
	- ## The two pages overlap
		- The Goals page restates the Brief's opening sections and adds a stronger CRDT commitment than the Brief makes. Keep Goals as three sentences that link into the Brief's sections, or fold it in. [[My/Principle/Simplify/Not every distinction is worth recording]] applies to two pages saying one thing.
		- The Goals page's "fastest incremental and lazily-cached back-end" is a superlative nobody can check. "A fast back end" says what is meant.
	- ## Writing
		- The non-goals list is phrased as things the first version is "not intended to" do. [[My/Pref/Dev/AI/OpenSpec]] wants each non-goal to be a real goal deferred, stated in the positive, and [[My/AI/Rule/State the Positive]] wants the "X, not Y" sentences rewritten. "Replace Git" and "implement a browser SPA" were never on the table and can go; "safe mutations" and "a publisher" are real deferred goals and belong there.
		- "Canonical" and "durable" recur through the Brief; both are on [[My/AI/Rule/How to Communicate Effectively With Me/Words and Phrases to Avoid]]. "Standard" and "lasting" carry the meaning.
		- The Brief is pasted standard Markdown: blank lines, `---` rules, and pull quotes whose `>` sits alone on one line with the quoted sentence on the next, so the quotes render empty in Logseq. The repository's `logseq-convert-md-to-lfm` skill fixes the structure, and the Phase headings become nested bullets.
		- The hub page's About line reads "humans of AI Agents" and "that are in maintained in the style of"; "humans or AI agents" and "maintained in the style of" were meant.
