alias:: [[llms.txt]]

- # [The /llms.txt file – llms-txt](https://llmstxt.org/)
	- > A proposal to standardise on using an `/llms.txt` file to provide information to help LLMs use a website at inference time.
	- [[My Notes]]
		- #Discovered #Via [[langgraph/llms-txt]]
		  id:: 67effe02-9841-4d65-88f0-df9a2914cc9e
			- > specifically `llms.txt` and `llms-full.txt`. These files allow large language models (LLMs) and agents to access programming documentation and APIs, particularly useful within integrated development environments (IDEs).
			- > As of March 9, 2025, IDEs do not yet have robust native support for llms.txt. However, you can still use llms.txt effectively through an MCP server.
			- > We provide an **MCP server** that was designed to serve documentation for LLMs and IDEs:
			- > 👉  [[LangChain/GitHub/mpcdoc]]
			- > This MCP server allows integrating `llms.txt` into tools like **Cursor**, **Windsurf**, **Claude**, and **Claude Code**.
			- > 📘 **Setup instructions and usage examples** are available in the repository.