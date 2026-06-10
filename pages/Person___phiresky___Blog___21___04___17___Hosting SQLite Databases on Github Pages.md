logseq-entity:: [[Logseq/Entity/Article]]
created-by:: [[Person/phiresky]]
date-created:: [[2021/04/17]]
- # [Hosting SQLite Databases on Github Pages](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)
	- ## Summary
		- Runs SQL queries against a [[SQLite]] database served from static hosting (e.g. GitHub Pages) with no backend. SQLite is compiled to WebAssembly, and HTTP range requests fetch only the database pages a query touches, so the browser reads chunks on demand instead of downloading the whole file.
	- ## Notes
		- Combines static-hosting reliability with relational querying; on-demand range-request fetching keeps transfer small even for large databases.
