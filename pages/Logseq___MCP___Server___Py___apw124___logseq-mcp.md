tags:: [[MCP/Server]], [[Python]], [[Logseq]]

- # apw124's Logseq MCP Server
	- GitHub: [apw124/logseq-mcp](https://github.com/apw124/logseq-mcp)
	- ## Overview
		- ### [[My Notes]]
			- [[2025-05-10 Sat]]
			  id:: 681f94bc-4e32-43c9-84c8-24ff05aeae16
				- has a fairly rich block API but it's not super updated; only 8 commits
		- An earlier Python MCP server (MIT-licensed) with similar goals to [[Logseq/MCP/Server/Py/mcp-server-logseq]]. It exposes a rich set of namespace functions for Logseq operations.
	- ## Features
		- Rich set of namespace functions under `logseq.`:
			- `logseq.get_page`
			- `logseq.create_block`
			- `logseq.update_block`
		- Fine-grained block operations:
			- **Moving blocks**
			- Searching blocks by text content
		- Aims for full parity with Logseq's plugin API
		- ### Pages
		  [](https://github.com/apw124/logseq-mcp#pages)
			- `logseq.get_all_pages`: Get a list of all pages in the Logseq graph
			- `logseq.get_page`: Get a specific page by name
			- `logseq.create_page`: Create a new page
			- `logseq.delete_page`: Delete a page and all its blocks
		- ### Blocks
		  [](https://github.com/apw124/logseq-mcp#blocks)
			- `logseq.get_page_blocks`: Get all blocks from a specific page
			- `logseq.get_block`: Get a specific block by ID
			- `logseq.create_block`: Create a new block on a page
			- `logseq.insert_block`: Insert a block as a child of another block
			- `logseq.update_block`: Update an existing block
			- `logseq.move_block`: Move a block to a different location
			- `logseq.remove_block`: Remove a block and all its children
			- `logseq.search_blocks`: Search for blocks matching a query
	- ## Status
		- **Mostly inactive** (single-digit GitHub stars)
		- May have been a proof-of-concept
		- Precursor to the more polished dailydaniel project
	- ## Installation
		- Via source: `pip install -e .`
	- ## Usage
		- Tied to the Cursor IDE/Claude integration