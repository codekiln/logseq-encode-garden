author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Logseq/Publish/Workaround for Storage]], [[QuartzMD]], [[My/Principle/Simplify/Prefer Standards and Defaults]]

- # Publish by exporting plain Markdown to a standard site generator
	- Phase 5 has garden-core produce static per-page HTML with stable URLs, SEO metadata, sitemaps, backlinks, incremental rebuilds, optional client-side search, and an optional graph view. That list is a static site generator, and writing one is a second product.
	- ## The pain is real and specific
		- The encode garden's site is built by [[logseq/publish-spa]], which inlines the whole graph into `index.html`. The file passed GitHub's per-file push limit, so the [gh-pages workflow](https://github.com/codekiln/logseq-encode-garden/blob/main/.github/workflows/gh-pages.yml) now gzips the graph into a separate file and injects a loader, as [[Logseq/Publish/Workaround for Storage]] records. Every visitor still downloads the whole garden before reading one page.
	- ## Let garden-core resolve Logseq semantics and let a site generator render
		- Add a `garden export` command that writes one plain CommonMark file per page with frontmatter, after resolving what only a Logseq-aware tool can resolve: page identity and namespaces, `[[links]]` to relative paths, `((uuid))` refs and `{{embed}}`s inlined or linked, properties to frontmatter keys, queries to their current results, and a backlinks list per page.
		- Hand that folder to a generator that already does stable URLs, sitemaps, search, and incremental builds. [[QuartzMD]] is already in this garden's prior-art list and was built for Markdown gardens of this kind; Hugo and Zola are the other standard choices.
		- This keeps garden-core the only component that understands Logseq, which is the Brief's own architectural principle, and it follows [[My/Principle/Simplify/Prefer Standards and Defaults]] and [[My/Principle/Simplify/Minimize Surface Area]]. The export is also useful on its own: it is the portable form of the garden that the Brief's thesis promises.
	- ## Try Tine's export first
		- [Tine](https://github.com/martinkoutecky/tine) already has static HTML export with offline search, and its onboarding guide is published that way. Point it at the encode garden for an hour before writing any publisher. If the output is close enough, Phase 5 shrinks to a workflow step. If it falls short, the gaps become the export command's requirements list.
