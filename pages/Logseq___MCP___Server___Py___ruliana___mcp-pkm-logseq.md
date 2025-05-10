alias:: [[Py/Lib/mcp-pkm-logseq]]

tags:: [[MCP/Server]], [[Python]], [[Logseq]], [[PKM]]

- # MCP-PKM-Logseq
	- GitHub: [ruliana/mcp-pkm-logseq](https://github.com/ruliana/mcp-pkm-logseq)
	- PyPI: [mcp-pkm-logseq](https://pypi.org/project/mcp-pkm-logseq/)
	- ## Overview
		- ### [[My Notes]]
			- [[2025-05-10 Sat]] not very mature API. Created by [[Person/Ronie Uliana]], a #Shopify employee
			  id:: 681f9276-1927-4b40-b629-cf360eb855aa
				- a unique item is that you configure the server by creating a Logseq page
					- Create a page named "MCP PKM Logseq" in your Logseq graph to serve as the guide for AI assistants. Add the following content:
						- Description of your tagging system (e.g., which tags represent projects, areas, resources)
						- List of frequently used tags and what topics they cover
						- Common workflows you use to organize information
						- Naming conventions for pages and blocks
						- Instructions on how you prefer information to be retrieved
						- Examples of useful topic combinations for searching
						- Any context about your personal knowledge management approach
		- A specialized MCP server geared towards personal knowledge management scenarios. Instead of exposing every possible Logseq operation, it defines custom "tools" for specific queries.
	- ## Features
		- Custom query tools:
			- `get_personal_notes(topics, from_date, to_date)`
			- `get_todo_list(...)`
		- Domain-specific AI instructions
		- `logseq://guide` resource page with usage notes
	- ## Status
		- **Active** (v0.2.2 released April 2025)
		- Narrow scope means it might be used alongside a more general solution
	- ## Installation
		- Via PyPI: `pip install mcp-pkm-logseq`
	- ## Requirements
		- Python 3.12+
	- ## Compatibility
		- OS-neutral (tested on Mac/Windows for Claude)
	- ## Limitations
		- No push notifications
		- No multi-graph features
		- Assumes one personal graph context
		- Write access limited to marking todos as done