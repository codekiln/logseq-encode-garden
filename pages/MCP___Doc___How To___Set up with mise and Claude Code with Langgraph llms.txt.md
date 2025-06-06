tags:: [[Diataxis/How To]]

- # How To Serve LangGraph & LangChain llms.txt via MCP with mise and validate in Claude Code
	- ## Goal
		- Stand up a local **MCP** documentation server using a YAML config for both LangGraph Python and LangChain Python `llms.txt`, wire it into **Claude Code** through `mise`, and confirm the connection with **MCP Inspector**.
	- ## Preconditions
		- You have `mise` ≥ 2024.6 installed and configured.
		- Your `mise.toml` already defines a `claude` task like:
			- ~~~toml
			  [tasks.claude]
			  # run mise install && mise reshim before running this.
			  description = "Run Claude Code CLI"
			  run = "npx @anthropic-ai/claude-code $@"
			  [tasks.claude.env]
			  CLAUDE_CODE_USE_BEDROCK    = "true"
			  AWS_PROFILE                = "bedrock"
			  AWS_REGION                 = "us-east-1"
			  ANTHROPIC_MODEL            = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
			  ANTHROPIC_SMALL_FAST_MODEL = "us.anthropic.claude-3-5-haiku-20241022-v1:0"
			~~~
		- You have `Node.js` ≥ 18 and `uvx` available (via `mise`'s `node` plugin).
		- **This guide assumes you already have the `uv` and `python` tools installed and shimmed via your home directory `mise.toml`, so that `uvx` is available on your PATH.**
			- See: [mise Getting Started – Adding tools](https://mise.jdx.dev/getting-started.html#3-adding-tools-to-mise-optional)
	- ## Procedure
		- ### 1. Add a YAML configuration for documentation sources
			- Create a `docs.yaml` file in the project root:
				- ~~~yaml
				  # MCP documentation sources
				  - name: LangGraph Python
				    llms_txt: https://langchain-ai.github.io/langgraph/llms.txt
				  - name: LangChain Python
				    llms_txt: https://python.langchain.com/llms.txt
				~~~
		- ### 2. Extend `mise.toml` with MCP tasks
			- Add the following to your `mise.toml`:
				- ~~~toml
				  [tasks.mpc-docs]
				  description = "Serve LangGraph & LangChain llms.txt via MCP"
				  alias       = "mcp"
				  run = '''
				  uvx --from mcpdoc mcpdoc \
				    --yaml docs.yaml \
				    --transport sse \
				    --port ${MPCDOC_PORT:-8082} --host localhost
				  '''
				  [tasks.mpc-inspect]
				  description = "Launch MCP Inspector UI"
				  run = "npx -y @modelcontextprotocol/inspector mise run mpc-docs"
				~~~
		- ### 3. (Optional) Add a local environment file
			- If you want to set a custom port or other environment variables, create a `.env` file (or reuse an existing one) with:
				- ~~~env
				  # optional override
				  MPCDOC_PORT=8082
				~~~
			- **Note:** By default, mise does NOT automatically load `.env` files. To have mise load this file for your tasks, add the following to your `mise.toml`:
				- ~~~toml
				  # This is forgiving: if .env does not exist, mise will ignore it without error.
				  # See: https://mise.jdx.dev/configuration/environments.html#setting-envvars
				  [env]
				  _.file = ".env"
				~~~
		- ### 4. Other ways to customize the port for the mpc-docs task
			- You can set the `MPCDOC_PORT` environment variable for the `mpc-docs` task in several mise-specific ways:
				- **Directly in the task definition:**
					- ~~~toml
					  [tasks.mpc-docs.env]
					  MPCDOC_PORT = "8083" # or any available port
					~~~
				- **Via the command line for a one-off run:**
					- ~~~sh
					  MPCDOC_PORT=8084 mise run mpc-docs
					~~~
				- **With a `.env` file as described above.**
			- See [mise: Setting EnvVars](https://mise.jdx.dev/configuration/environments.html#setting-envvars) for more options.
		- ### 5. Start the MCP server
			- Run:
				- ~~~sh
				  mise run mpc-docs
				~~~
			- You should see Uvicorn log output showing that it's serving on your selected port and has loaded two documentation sources.
		- ### 6. Inspect and validate
			- In another terminal, run:
				- ~~~sh
				  mise run mpc-inspect
				~~~
			- MCP Inspector opens in your browser at **http://127.0.0.1:6274**. Click **Connect**, then test **list_doc_sources** and **fetch_docs** to verify both sources load correctly.
		- ### 7. Connect Claude Code to the project server
			- 1. Add the MCP server to your project's `.mcp.json` using:
				- ~~~sh
				  claude mcp add-json langgraph-docs \
				    '{"type":"sse","url":"http://localhost:8082"}' \
				    -s project
				~~~
			-   See: [Claude Code Tutorials – Set up Model Context Protocol MCP (project scope)](https://docs.anthropic.com/en/docs/claude-code/tutorials#set-up-model-context-protocol-mcp)
			- 2. Create a `CLAUDE.md` file in the root of your repo with usage rules like:
				- ~~~markdown
				  for ANY question about LangGraph or LangChain, use the langgraph-docs server to help answer –  
				  + call list_doc_sources to view available llms.txt files  
				  + call fetch_docs to read them  
				  + reflect on the input question and fetched content before answering
				~~~
			- 3. Run:
				- ~~~sh
				  mise run claude
				~~~
			- 4. In Claude's terminal, run `/mcp status` and confirm `langgraph-docs` is connected. Ask:
				- > *"What types of memory does LangGraph support?"*  
				  Claude should respond using the local docs without external fetches.
	- ## Troubleshooting
		- **Port already in use** — You can resolve port conflicts by:
			- Setting a different value for `MPCDOC_PORT` in your `.env` file (and ensuring it's loaded as above)
			- Setting `MPCDOC_PORT` in the `[tasks.mpc-docs.env]` section of your `mise.toml`
			- Passing it inline for a single run: `MPCDOC_PORT=8085 mise run mpc-docs`
		- **Inspector can't connect** — verify `mpc-docs` is running and using the expected port.
		- **Claude doesn't see the server** — confirm `.mcp.json` includes the correct `langgraph-docs` entry and matches the transport/URL.
	- ## References
		- [mcpdoc GitHub](https://github.com/langchain-ai/mcpdoc)
		- [llms.txt spec](https://llmstxt.org/)
		- [LangGraph llms.txt](https://langchain-ai.github.io/langgraph/llms.txt)
		- [LangChain llms.txt](https://python.langchain.com/llms.txt)