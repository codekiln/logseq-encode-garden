alias:: [[Py/Lib/mcp-pkm-logseq]]

tags:: [[MCP/Server]], [[Python]], [[Logseq]], [[PKM]]

- # MCP-PKM-Logseq
	- GitHub: [ruliana/mcp-pkm-logseq](https://github.com/ruliana/mcp-pkm-logseq)
	- PyPI: [mcp-pkm-logseq](https://pypi.org/project/mcp-pkm-logseq/)
	- ## Overview
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
