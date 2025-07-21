# Markdown Flavors / Syntaxes / Variants
	- See also [[Markdown/Guide/Extended Syntax]]
	- ## Quick reference: dialects with first-class  *interactive*  or  *data-storage*  features
		- | Dialect | Live widgets / code | Structured metadata | Typical storage mechanism |
		  | ---- | ---- | ---- |
		  | [[Logseq]] MD | Queries, Agile boards | `property::` blocks | In-file key-value pairs |
		  | [[Obsidian]] + Dataview | Dataview tables & JS | YAML front-matter, inline fields | YAML + inline |
		  | [[R/Markdown]] | Shiny, HTML widgets | YAML params | YAML header |
		  | [[R/Quarto]] | Shiny, Observable, Jupyter | YAML header | YAML header |
		  | [[MDX]] | React components | ES module imports | JavaScript objects |
		  | [[GFM]] / GLFM | Task-list checkboxes, Mermaid | Limited (Front matter on GitLab) | Front matter or repo data |
	- ## Examples
		- ### [[Markdown/Flavor/CommonMark]]
		- ### [[Markdown/Flavor/Github]] GitHub Flavored Markdown (GFM)
		- ### [[Markdown/Flavor/GitLab]] GitLab Flavored Markdown (GLFM)
		- ### [[Logseq/Flavored Markdown]]
		- ### [[App/Obsidian/Markdown]] + Dataview
		- ### [[R/Markdown]] & [[R/Quarto]]
			- **Why** – weave prose with executable code chunks for reproducible research; Quarto generalises R Markdown to any language (R, Python, Julia, Observable) and modern interactivity
				- [Bookdown](https://bookdown.org/yihui/rmarkdown/params-knit.html)
				- [Quarto](https://quarto.org/docs/interactive/?utm_source=chatgpt.com)
			- **Use** – academic papers, Shiny dashboards, corporate reports
			- **Renderers** – R (rmarkdown), Quarto CLI (Rust+Go), knitr, Jupyter kernels
			- **Interactive / data** – HTML widgets, embedded Shiny apps, Observable JS, parameterised reports; YAML front-matter stores document-level metadata and runtime params
		- ### [[MDX]] (Markdown + JSX)
			- **Why** – let React components live inline with Markdown for docs that need live code demos or UI components[ReadMe](https://docs.readme.com/main/docs/mdx)
			- **Use** – [[nextjs]] / [[Docusaurus]] / Storybook sites, ReadMe.io docs
			- **Renderers** – Node toolchain `@mdx-js` (Babel/ESBuild), integrated in React, Astro, SvelteKit via adapters
			- **Interactive / data** – any React component (charts, sandboxes) can read remote data or local JSON at runtime
		- ### [[AsciiDoc]] / Asciidoctor
			- **Why** – richer technical-writing features (attributes, macros, includes) and direct DocBook export; emerged before CommonMark for book manuals[Asciidoctor Docs](https://docs.asciidoctor.org/asciidoc/latest/macros/ui-macros/?utm_source=chatgpt.com)
			- **Use** – Red Hat docs, Spring Framework guides, O’Reilly book tooling
			- **Renderers** – Ruby (Asciidoctor), Java (AsciidoctorJ), JS (asciidoctor.js), Python (asciidoc3)[AsciiDoc3](https://www.asciidoc3.org/documentation/userguide/?utm_source=chatgpt.com)
			- **Interactive / data** – attribute substitutions, UI macros, PlantUML & GraphViz extensions; can pull external files and variables at build time
		- ### [[Djot]]
			- **Why** – John MacFarlane’s attempt to keep CommonMark simplicity but add attributes, math, footnotes, and generic containers while parsing faster [Djot](https://www.djot.net/)
			- **Status / use** – early adopters in static-site tooling; Pandoc can convert to/from Djot
			- **Renderers** – official JS implementation plus Lua, Rust, Go, Prolog parsers[Djot](https://www.djot.net/)
			- **Interactive / data** – element-level attributes make it easier to attach metadata; no built-in live interactivity yet
	- C-level libraries exist for CommonMark, GFM, and Djot; Ruby and JavaScript dominate AsciiDoc and MDX toolchains; R and multi-language kernels drive R Markdown and Quarto.