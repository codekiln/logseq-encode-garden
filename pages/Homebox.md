logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [Homebox](https://homebox.software)
	- Repository: [sysadminsmedia/homebox](https://github.com/sysadminsmedia/homebox). [[GitHub/Star]]: 7714 (checked [[2026-11-01 Sun]]).
	- [[Self-hosted]] inventory and organization system for a home. Continues the archived [hay-kot/homebox](https://github.com/hay-kot/homebox).
	- Items sit in nested locations. Items and locations carry photos, tags, custom fields, attachments, and asset IDs.
	- Label templates lay out text, barcodes, shapes, and images at a chosen label size. Items and locations print on a label printer, in the browser, or as a PDF sheet. Presets cover Avery sheets, Brother DK rolls, Dymo, Brady, and Zebra stock; a Custom preset takes any width and height in millimetres.
	- An external label service can generate item and location labels. Homebox sends a GET request with the QR URL, title, and size, and the service returns an image.
	- REST API with an OpenAPI spec. API keys come from Profile in the web UI.
	- [dgahagan/homebox-mcp](https://github.com/dgahagan/homebox-mcp) is a third-party [[MCP/Server]] over that API. It answers inventory questions, creates items and attaches receipts and manuals, and prints QR labels for totes and shelves. It needs Homebox 0.26 or later.
	- Runs on [[SQLite]] by default, with [[PostgreSQL]] as the option for larger installs. Ships as a [[Docker]] image.
	- Licensed under AGPL-3.0.
	- Written in [[Go]].
