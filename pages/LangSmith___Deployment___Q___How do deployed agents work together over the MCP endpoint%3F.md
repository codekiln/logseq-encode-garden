logseq-entity:: [[Logseq/Entity/Question]]
via:: [[LangSmith/26/09/29 Tue - Deep Agents]]
see-also:: [[A2A]], [[LangSmith/Deep Agents]]

- # How do deployed agents work together over the [[MCP]] endpoint, including from [[Claude/Code]] or [[Codex]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Agent Server: MCP endpoint](https://docs.langchain.com/langsmith/server-mcp), researched by [[Anthropic/Model/Claude/5/5/Opus]] on [[2026-09-29 Tue]]
		- **Short answer:** every [[LangSmith/Deployment]] serves `/mcp`, and each agent in it shows up there as one MCP tool. Any MCP client that speaks Streamable HTTP — another agent, [[Claude/Code]], [[Codex]] — can list those tools and call an agent like any other tool.
		- ## What the endpoint exposes
			- The Agent Server implements MCP over the Streamable HTTP transport at `/mcp`. It is on by default in `langgraph-api>=0.2.3`; `"disable_mcp": true` in `langgraph.json` turns it off.
			- Each deployed agent becomes one tool: the tool name is the agent's name, the description is the agent's description, and the input schema is the agent's input schema. Name and description are set in `langgraph.json`.
			- The docs recommend explicit, minimal input and output schemas. The default `MessagesState` accepts any message type, which is too loose for another model to fill in well.
			- Auth is the same as the rest of the deployment's API; on LangSmith that is an `X-Api-Key` header.
			- The endpoint has no sessions. Every `/mcp` call is independent, so one tool call is one fresh run of the agent, with no thread carried to the next call.
		- ## Agent to agent
			- An agent in one deployment can load another deployment's `/mcp` tools with `langchain-mcp-adapters` (`load_mcp_tools` or `MultiServerMCPClient`) and hand them to its own model. The calling agent's model then decides when to delegate to the other agent, the same way it picks any tool.
			- That makes deployed agents interchangeable: swapping one for another means pointing the client at a different URL.
			- Because calls are stateless, MCP suits one-shot delegation: ask a question, get an answer.
				- For long-running or multi-turn work between agents, the docs point to other routes: [[A2A]], served per assistant at `/a2a/{assistant_id}` with tasks and streaming ([A2A endpoint](https://docs.langchain.com/langsmith/server-a2a)), or [[LangSmith/Deep Agents]] async subagents, which launch, check, steer and cancel runs on a remote deployment over the Agent Protocol ([Async subagents](https://docs.langchain.com/oss/python/deepagents/async-subagents)).
		- ## From [[Claude/Code]]
			- ~~~bash
			  claude mcp add --transport http finance-agent \
			    https://<deployment-host>/mcp \
			    --header "X-Api-Key: $LANGSMITH_API_KEY"
			  ~~~
			- The agent then appears to Claude Code as a tool named after the agent.
		- ## From [[Codex]]
			- `codex mcp add --url` registers a Streamable HTTP server, but its only auth flag is `--bearer-token-env-var`, which sends `Authorization: Bearer`. LangSmith expects `X-Api-Key`, so set the header in `~/.codex/config.toml`:
			- ~~~toml
			  [mcp_servers.finance-agent]
			  url = "https://<deployment-host>/mcp"
			  env_http_headers = { "X-Api-Key" = "LANGSMITH_API_KEY" }
			  ~~~
			- `env_http_headers` maps a header name to the environment variable that holds its value. Checked against the `codex mcp add --help` output and the config keys of codex-cli 0.158.0, not against a live deployment.
		- ## User-scoped tools
			- Going the other way, a deployed agent can call MCP servers on behalf of each user. Custom auth middleware fills `langgraph_auth_user`, and a node builds a `MultiServerMCPClient` with that user's token in the request headers, so each user gets only their own tools.
