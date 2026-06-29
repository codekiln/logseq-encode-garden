logseq-entity:: [[Logseq/Entity/Question]]

- # Can [[QuartzMD]] publish HTML files as well as Markdown?
	- ## [[AI Answer]]
		- **Short answer:** Yes, but *how* depends on what you are publishing. A single page or a widget on a Markdown page is easy; a whole self-contained static app (multiple `.html` + `.js` + `.css` with relative links) needs a **verbatim-copy** route, because the `content/` route rewrites paths.
		- **The slug gotcha (read this first).** The **Assets** emitter (`quartz/plugins/emitters/assets.ts`) copies non-Markdown files from `content/`, but it runs every path through `slugifyFilePath` (`@quartz-community/utils`), which **lowercases every path segment** and **strips the `.html` extension**. So `content/App/Index.html` lands at `public/app/index` (no extension), and `About.html` becomes `about`. That silently breaks relative links like `<a href="About.html">` and any case-sensitive `app.js`/`App.js` references. Fine for a one-off image or PDF; bad for a multi-file HTML app.
		- **A. One page, no Quartz chrome → `content/` (Assets).** Drop the `.html` in `content/`; it is published (no nav/backlinks/graph/theme). Just keep names lowercase and link without `.html` extensions to match the slug behavior above. Docs: "emits all non-Markdown static assets in your content folder (like images, videos, HTML, etc)."
		- **B. A widget on a normal Quartz page → inline raw HTML in Markdown.** The parse pipeline runs `remark-rehype` with `allowDangerousHtml: true` (`quartz/processors/parse.ts`), so raw HTML written inside a `.md` page passes through unescaped on an otherwise fully-chromed page. Enable `enableInHtmlEmbed` on ObsidianFlavoredMarkdown to parse wikilinks/tags inside those blocks.
		- **C. A whole static app with separated JS/CSS → a verbatim route (recommended).** To keep exact filenames, case, extensions, and nested structure, do **not** route the app through `content/`:
			- **Static emitter:** put the app under `quartz/static/<app>/`. `quartz/plugins/emitters/static.ts` globs that folder and copies each file with its **raw path** (no slugify) to `public/static/<app>/`, served at `/static/<app>/`. Preserves `index.html`, `app.js`, casing, and subdirectories exactly. (This folder also holds Quartz's own assets like icons/OG image — keep your app in its own subfolder.)
			- **Custom emitter:** for arbitrary output paths, write an emitter that calls `write({ ctx, slug, ext: ".html", content })` per file (see Quartz "making plugins").
			- **Post-build copy:** copy the app folder into `public/` after `npx quartz build` as a build step.
			- For any of these, prefer **relative** asset links (`./app.js`) so the app survives being served under a subpath (`baseUrl`).
		- ### Sources
			- [Quartz Assets plugin docs](https://quartz.jzhao.xyz/plugins/Assets) — "emits all non-Markdown static assets in your content folder (like images, videos, HTML, etc)"
			- [Quartz — making plugins (custom emitter / `write`)](https://quartz.jzhao.xyz/advanced/making-plugins)
			- Quartz v5 source (`@jackyzha0/quartz` 5.0.0): `quartz/plugins/emitters/assets.ts` (slugifies via `slugifyFilePath`), `quartz/plugins/emitters/static.ts` (verbatim copy), `quartz/processors/parse.ts`; `slugifyFilePath` in `@quartz-community/utils`
