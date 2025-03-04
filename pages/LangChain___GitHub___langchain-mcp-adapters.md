tags:: [[MCP]], [[langgraph]], [[Py/Lib]]

- # [langchain-ai/langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters?tab=readme-ov-file)
	- This library provides a lightweight wrapper that makes [Anthropic Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) tools compatible with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph).
	- ![MCP](https://raw.githubusercontent.com/langchain-ai/langchain-mcp-adapters/refs/heads/main/static/img/mcp.png)
	- ## Features
		- 🛠️ Convert MCP tools into [LangChain tools](https://python.langchain.com/docs/concepts/tools/) that can be used with [LangGraph](https://github.com/langchain-ai/langgraph) agents
		- 📦 A client implementation that allows you to connect to multiple MCP servers and load tools from them