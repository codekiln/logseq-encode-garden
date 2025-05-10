tags:: [[Logseq]], [[MCP/Server]], [[Feedback]]
date-created:: [[2025/04/25]]
created-by:: [[Logseq/Forum/User/gww]]

- # [MCP Server for LogSeq - Feedback - Logseq](https://discuss.logseq.com/t/mcp-server-for-logseq/32004)
	- ## #[[Original Poster]]
		- links to
			- [GitHub - smithery-ai/mcp-obsidian: A connector for Claude Desktop to read and search...](https://github.com/smithery-ai/mcp-obsidian)
			- IIUC strong value proposal of LogSeq is ability to reference and query text blocks levaraging on Datalog technology?
			- Here is more advanced MCP server using obsidian behind the scenes, and I see no reason why it can not use LogSeq as well !
				- [https://hub.docker.com/r/mcp/basic-memory](https://hub.docker.com/r/mcp/basic-memory)
			- Maybe relevant / helpful links:
				- [https://mcp.so/server/mcp-server-datadog](https://mcp.so/server/mcp-server-datadog)
				- [GitHub - 2b3pro/roam-research-mcp: MCP Server for Roam Research Graph Integration](https://github.com/2b3pro/roam-research-mcp)
		- [[Logseq/Forum/User/gww]] [Summary - gww - Logseq](https://discuss.logseq.com/u/gww/summary)
			- Background in graph algorithms and distributed systems
			- Experience with Rust and functional programming (Elixir)
			- Strong preference for KISS principles and data ownership
			- Interested in VIM integration with Logseq
			- Limited JavaScript experience
	- ## #[[Related/Post]]
		- [[Logseq/MCP/Server/Survey/Report]]
		- [[Logseq/Proj/LsqMCP/PRD]]
	- ## #[[My Notes]]
		- Several MCP server implementations exist:
			- Python-based servers:
				- [[Logseq/MCP/Server/Py/mcp-server-logseq]] (most active)
				- [[Logseq/MCP/Server/Py/ergut/mcp-logseq-server]]
				- [[Logseq/MCP/Server/Py/apw124/logseq-mcp]]
				- [[Logseq/MCP/Server/Py/ruliana/mcp-pkm-logseq]]
			- JavaScript-based servers:
				- [[Logseq/MCP/Server/JS/@joelhooks/logseq-mcp-tools]]
		- Key considerations:
			- Read/write access to graphs
			- Multi-graph support
			- Real-time updates vs polling
			- Performance with large graphs
			- Cross-platform compatibility