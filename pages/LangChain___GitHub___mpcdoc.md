tags:: [[MCP/Server]]

- # [langchain-ai/mcpdoc GitHub Repository](https://github.com/langchain-ai/mcpdoc)
	- ## Setup
		- ### 1 - Test MCP server out locally
			- ```
			  uvx --from mcpdoc mcpdoc \
			      --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
			      --transport sse \
			      --port 8082 \
			      --host localhost
			  ```
			- #### Sample run
				- ```
				  uvx --from mcpdoc mcpdoc \
				      --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
				      --transport sse \
				      --port 8082 \
				      --host localhost
				  Installed 32 packages in 27ms
				  
				      ███╗   ███╗ ██████╗██████╗ ██████╗  ██████╗  ██████╗
				      ████╗ ████║██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝
				      ██╔████╔██║██║     ██████╔╝██║  ██║██║   ██║██║
				      ██║╚██╔╝██║██║     ██╔═══╝ ██║  ██║██║   ██║██║
				      ██║ ╚═╝ ██║╚██████╗██║     ██████╔╝╚██████╔╝╚██████╗
				      ╚═╝     ╚═╝ ╚═════╝╚═╝     ╚═════╝  ╚═════╝  ╚═════╝
				  
				  
				  Launching MCPDOC server with 2 doc sources
				  INFO:     Started server process [52524]
				  INFO:     Waiting for application startup.
				  INFO:     Application startup complete.
				  INFO:     Uvicorn running on http://localhost:8082 (Press CTRL+C to quit)
				  ```
			- #### 1.1 - Use [[MCP/Inspector]] to view the connection and test it out
				- `npx @modelcontextprotocol/inspector`
				- ##### Sample Run
					- ```
					  npx @modelcontextprotocol/inspector
					  
					  Need to install the following packages:
					  @modelcontextprotocol/inspector@0.8.2
					  Ok to proceed? (y) y
					  
					  Starting MCP inspector...
					  ⚙️ Proxy server listening on port 6277
					  🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
					  ```
				- Go to `http://127.0.0.1:6274` and then click on Tools and click through to test out `list_doc_sources` and `fetch_docs`
		- ### 2 - set up [[CursorAI/Settings/MCP]]
			- [[My Notes]]
				- instructions in the source are very clear; only thing that surprised me a bit was using [[CursorAI/Rule/User]] instead of [[CursorAI/Project Rules]]
		-
			-