logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Andy Miller]]
date-created:: [[2014]]

- # [Grav](https://getgrav.org/)
	- Source repository: [getgrav/grav](https://github.com/getgrav/grav).
	- [[GitHub/Star]]: 15,634 on getgrav/grav (checked 2026-08-18).
	- Written in [[PHP]]; 2.x requires PHP 8.3.11 or later.
	- MIT licensed. Current release 2.0.19, published 2026-08-14.
	- Built on Twig for templating and Symfony components for events, console, cache, and YAML parsing, with Parsedown rendering the Markdown.
	- The 2.0 line adds a REST API for headless use, a rebuilt admin, and an MCP server that lets an agent read and write site content directly.
	- CalTopo's training and documentation site at [training.caltopo.com](https://training.caltopo.com/) is built on Grav, serving `<meta name="generator" content="GravCMS" />` over Grav's `learn2` documentation theme.
	- ## Flat file, no database
		- A page is a folder under `user/pages/` containing a [[Markdown]] file. The file's [[Markdown/Frontmatter/Yaml]] carries title, slug, date, and publish state; its filename selects the Twig template; folder nesting is simultaneously the URL structure and the site navigation, with numeric folder prefixes setting order. Configuration is YAML under `user/config/`. Nothing is stored anywhere else — installing is unzipping an archive, with no schema and no install wizard.
		- What that buys: the entire site is [[git/Friendly]] plain text that diffs, branches, and edits in any editor, and backs up by copying a directory. The general shape of the tradeoff is on [[File/Flat]].
		- What it costs: work a database would do with an index has to be recomputed instead, so Grav caches aggressively and its own requirements page recommends a PHP user cache — APCu, Memcached, or Redis — for acceptable performance. Relational content that a database gives away for free (multi-language, multi-user, cross-referenced collections) instead needed a purpose-built object layer, Flex, added in 2018.
