author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Give publishing an explicit semantic support contract
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Publish by exporting plain Markdown to a standard site generator]] offers a useful rendering boundary. Its export proposal includes evaluating queries, while the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] schedules publishing before richer query semantics. That dependency needs an explicit decision.
	- ## A readable page can still lose its meaning
		- [[Logseq/Frontmatter]] is assembled from embedded subpages. Exporting only its local text would produce a heading and macro syntax while omitting the explanations a Logseq reader sees.
		- Choose a supported set of references, embeds, and queries for the initial publisher. Report unsupported constructs with their source locations and show a visible fallback in the output. An empty result should mean that a supported query ran and found nothing.
		- A compatibility report over the real garden can say which pages render fully and which depend on unsupported behavior. That is also an honest measure of progress toward using the garden without Logseq.
	- ## Incremental publication follows dependencies
		- Record which exported pages depend on another page or block. Changing a source block must invalidate its consumers even when their files are unchanged.
		- Query dependencies can be broader than today's result set. A new matching page should update a query page that previously had no link to it. Broad query invalidation is a reasonable starting point until narrower dependency rules are proven.
		- Detect recursive embeds and render a link at the cycle boundary. Expanding references into text needs a termination rule.
	- ## Publication scope must survive expansion
		- For graphs with private content, apply publication selection before evaluating exported backlinks, query results, embeds, and search entries. Filtering only the final page list can still reveal excluded content through a permitted page.
		- The public encode garden can remain the main publishing fixture, supplemented by a tiny mixed-visibility graph.
	- ## The decision this enables
		- Try an existing exporter against a written support contract. Assess preserved content and meaning alongside load speed and appearance. The static-site generator can handle presentation once the exported representation is dependable.
