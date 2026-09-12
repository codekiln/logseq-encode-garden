author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Specify which Logseq features the publisher supports
	- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Publish by exporting plain Markdown to a standard site generator]] proposes exporting Markdown for a standard site generator. That export would include query results, while the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] schedules publishing before implementing queries. Decide which query forms the first publisher will be able to evaluate.
	- ## A readable page can still lose its meaning
		- The documentation page titled [[Logseq/Frontmatter]] contains embed directives for [[Logseq/Frontmatter/tags]], [[Logseq/Frontmatter/alias]], and other documentation pages. The [page's Markdown source](https://github.com/codekiln/logseq-encode-garden/blob/07bda4f2/pages/Logseq___Frontmatter.md#L3) shows those directives. To include the explanations from the linked pages, an exporter must expand the embeds; copying only the containing file leaves those explanations out.
		- Choose a supported set of references, embeds, and queries for the initial publisher. Report unsupported constructs with their source locations and show a visible fallback in the output. An empty result should mean that a supported query ran and found nothing.
		- A compatibility report over the real garden can say which pages render fully and which depend on unsupported behavior. That is also an honest measure of progress toward using the garden without Logseq.
	- ## Rebuild every published page affected by an edit
		- Record which pages include text from another page or block. When that included text changes, rebuild the published pages that display it, even when their own Markdown files are unchanged.
		- A page that displays query results may also need rebuilding when a new matching page is added. Checking only the pages in the previous result would miss that addition. Re-running all supported queries after an edit is a reasonable starting point; later, the engine can narrow which queries need to run again.
		- Detect recursive embeds and render a link at the cycle boundary. Expanding references into text needs a termination rule.
	- ## Keep private text out of public output
		- For graphs with private content, apply publication selection before evaluating exported backlinks, query results, embeds, and search entries. Filtering only the final page list can still reveal excluded content through a permitted page.
		- The public encode garden can remain the main publishing fixture, supplemented by a tiny mixed-visibility graph.
	- ## The decision this enables
		- Try an existing exporter against the list of supported Logseq features. Check that links lead to the right places, embeds include the expected text, and queries return the expected results, alongside load speed and appearance.
