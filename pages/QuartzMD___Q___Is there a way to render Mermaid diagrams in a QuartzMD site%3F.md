logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Diagram/Mermaid]]

- # Is there a way to render [[Mermaid]] diagrams in a [[QuartzMD]] site?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes. Quartz has built-in Mermaid support enabled through the `ObsidianFlavoredMarkdown` plugin. Diagrams render automatically and adapt to the site's light/dark theme.
			- **Syntax:** Use a standard `mermaid` fenced code block in your Markdown:
				- ~~~
				  ```mermaid
				  sequenceDiagram
				      Alice->>Bob: Hello
				      Bob-->>Alice: Hi!
				  ```
				  ~~~
			- **Configuration**
				- Mermaid rendering is part of the `ObsidianFlavoredMarkdown` plugin in `quartz.config.ts`. It is **enabled by default** in a standard Quartz install.
				- If diagrams fail to render, reorder the plugins so that `ObsidianFlavoredMarkdown` appears **after** `SyntaxHighlighting` in the `plugins.transformers` list.
			- **Supported diagram types**
				- Flowcharts, sequence diagrams, timelines, and all other standard [[Mermaid]] diagram types are supported.
			- **Caveats**
				- Mermaid is rendered client-side via JavaScript. An open GitHub issue ([#1699](https://github.com/jackyzha0/quartz/issues/1699)) tracks a request to render diagrams to static SVG at build time instead.
			- ### Sources
				- [Quartz — Mermaid Diagrams](https://quartz.jzhao.xyz/features/Mermaid-diagrams)
				- [Issue #1699: feat(mermaid): options to render to static SVG](https://github.com/jackyzha0/quartz/issues/1699)
