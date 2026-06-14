logseq-entity:: [[Logseq/Entity/Question]]

- # Can [[QuartzMD]] publish HTML files as well as Markdown?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes. The **Assets** emitter copies all non-Markdown files from the `content/` folder verbatim to the output — including `.html` files. A folder containing an `index.html` placed inside `content/` is passed through to the built site as-is, with no Quartz chrome applied.
			- **How it works**
				- The `Assets` emitter (`quartz/plugins/emitters/assets.ts` in v4) globs everything in `content/` *except* `*.md` and your configured ignore patterns, then copies each file to the corresponding output path.
				- Example: `content/my-app/index.html` → `public/my-app/index.html`, reachable at `https://your-site/my-app/`.
				- The **Static** plugin (`quartz/static/`) is a second route: everything placed there is copied to the output root, so `quartz/static/my-app/index.html` → `public/my-app/index.html` as well.
			- **Caveats**
				- Passed-through HTML files get **no Quartz chrome** — no navigation, backlinks, graph view, or site theme. They render exactly as written.
				- Quartz generates internal links without `.html` extensions; for directory-index serving (`/my-app/` → `my-app/index.html`), most hosts (GitHub Pages, Cloudflare Pages, Netlify) handle this by default.
				- This is confirmed in both v4 (source code) and v5 (docs: "emits all non-Markdown static assets in your content folder (like images, videos, HTML, etc)").
			- ### Sources
				- [Quartz Assets emitter source (v4)](https://github.com/jackyzha0/quartz/blob/v4/quartz/plugins/emitters/assets.ts)
				- [Quartz architecture (v4)](https://quartz.jzhao.xyz/advanced/architecture)
				- [Quartz 5 — Welcome / overview](https://quartz.jzhao.xyz/)
