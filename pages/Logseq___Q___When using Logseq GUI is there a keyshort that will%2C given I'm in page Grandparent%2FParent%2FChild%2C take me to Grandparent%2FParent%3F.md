logseq-entity:: [[Logseq/Entity/Question]]

- # When using the [[Logseq]] GUI, is there a [[Keyshort]] that will, given I'm in page `Grandparent/Parent/Child`, take me to `Grandparent/Parent`?
	- ## [[AI Answer]]
		- **Short answer:** No. Logseq ships no dedicated keyboard shortcut that jumps from a namespaced page to its immediate parent namespace page.
		- Checked `modules/shortcut/config.cljs` in the Logseq source: the `:go/*` shortcut group only defines `go/backward` (`⌘[`), `go/forward` (`⌘]`), `go/journals`, `go/home`, `go/all-pages`, `go/graph-view`, `go/next-journal`, `go/prev-journal`, etc. — there is no `go/parent` or namespace-aware entry.
		- **Practical alternatives:**
			- Click the breadcrumb segment at the top of the page. Logseq renders a clickable breadcrumb (`Grandparent > Parent > Child`) above the page title for namespaced pages; clicking `Parent` navigates straight there.
			- Use `⌘[` (`mod+open-square-bracket`, `go/backward`) if you arrived at `Child` by navigating *from* `Parent` in the same session — this is browser-style back/forward history, not namespace-aware, so it won't help if you opened `Child` directly (e.g. via search).
			- Use search/cmdk (`⌘k`) and type `Grandparent/Parent` to jump directly.
		- [[Answer/Official]] from [Logseq source](https://github.com/logseq/logseq) (`src/main/frontend/modules/shortcut/config.cljs`, `src/main/frontend/components/header.cljs` — `block-breadcrumb`)
