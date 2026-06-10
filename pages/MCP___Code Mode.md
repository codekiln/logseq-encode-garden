logseq-entity:: [[Logseq/Entity/concept]]

- # MCP/Code Mode
	- An execution strategy built on top of [[MCP]] (not part of the MCP spec itself) that emerged as a popular pattern in late 2025
	- Instead of the model calling individual tools one at a time, the model writes a short program that calls many tools programmatically; only the final result returns to the model context
	- ## Traditional MCP vs Code Mode
		- ### Traditional MCP
			- MCP server exposes 50–500 tools
			- The LLM sees all tool schemas upfront (large context cost)
			- The LLM decides which tool to call, calls it, sees the result, then decides the next call
			- Intermediate results flow through the model context at every step
		- ### Code Mode
			- MCP server exposes a small set of "meta tools"
			- The LLM discovers available capabilities, then writes code (Python, TypeScript, etc.)
			- That code executes in a sandbox and calls the underlying MCP tools programmatically
			- Only the final result is returned to the model — intermediate data stays in the sandbox
		- ### Example
			- Instead of six round-trips through the model (`search_github`, `get_issue`, `get_comments`, `get_pr`, `get_diff`, `summarize`), the model writes:
				- ~~~python
				  issues = github.search_issues(...)
				  comments = github.get_comments(...)
				  prs = github.get_prs(...)
				  ~~~
				- and executes it in one step
	- ## Why it matters
		- **Token efficiency** — some implementations report 90%+ reductions in context devoted to tool definitions; an entire API can fit in ~1000 tokens
		- **Better orchestration** — LLMs are generally stronger at writing sequential code than emitting long chains of tool calls, so complex workflows become more reliable
		- **Context hygiene** — intermediate data stays inside the sandbox instead of polluting the model's working context
		- **Multi-server composition** — easier to orchestrate across many MCP servers simultaneously
	- ## Mental model
		- MCP is the protocol. Code Mode is an execution strategy on top of MCP.
		- Analogous to: calling a REST API endpoint-by-endpoint vs. generating a typed SDK and writing code against it
		- MCP servers increasingly look less like collections of tools and more like **dynamically generated libraries** that agents can program against
	- ## Implementations and references
		- [[Cloudflare/MCP]] — ["Code Mode: the better way to use MCP"](https://blog.cloudflare.com/code-mode/) and ["give agents an entire API in 1000 tokens"](https://blog.cloudflare.com/code-mode-mcp/)
		- [[FastMCP]] — [Code Mode docs](https://gofastmcp.com/servers/transforms/code-mode)
		- Bifrost AI Gateway — [Code Mode](https://docs.getbifrost.ai/mcp/code-mode)
		- [How Code Mode Builds on MCP for Agent Tooling — Nordic APIs](https://nordicapis.com/how-code-mode-builds-on-mcp-for-agent-tooling/)
		- [Code Mode with Skills — Navendu Pottekkat](https://navendu.me/posts/code-mode/)
	- ## See also
		- [[MCP/Server]]
		- [[MCP/Gateway/Enterprise]]
