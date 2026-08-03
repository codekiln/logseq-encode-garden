logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[LangChain]]

- # [LangSmith Remote MCP](https://docs.langchain.com/langsmith/langsmith-remote-mcp)
	- [[MCP]] server hosted by [[LangSmith]] itself, so there is nothing to deploy: point a client at `https://api.smith.langchain.com/mcp` (or the EU, APAC, and AWS regional hosts).
	- Supersedes the self-deployed [[LangSmith/MCP/Server]], which is now deprecated, and exposes the same tool surface: `get_thread_history`, `list_prompts`, `get_prompt_by_name`, `push_prompt`, `fetch_runs`, `list_projects`, `list_datasets`, `list_examples`, `read_dataset`, `read_example`, `create_dataset`, `update_examples`, `list_experiments`, `run_experiment`, `get_billing_usage`.
	- Interactive clients authenticate over [[OAuth]] 2.1 with dynamic client registration ([RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)) — no client ID to provision and no API key to manage. Programmatic clients send a LangSmith API key in the `X-Api-Key` header instead; the deprecated standalone server used `LANGSMITH-API-KEY`.
	- Sessions are scoped to the calling user's LangSmith workspace permissions, so a tool call can only read what that account can read.
	- Speaks the Streamable HTTP transport and is stateless, so any compliant client connects with the URL alone. Large payloads use character-budget pagination (`page_number`, `total_pages`, `max_chars_per_page`) rather than cursors.
	- [[OpenAI]]'s [[Codex]] CLI cannot use it: Codex omits the [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) `resource` parameter during the OAuth flow, so login appears to succeed but `initialize` fails with an auth error ([openai/codex#20729](https://github.com/openai/codex/issues/20729)).
	- Self-hosted LangSmith v0.16+ serves it at `https://<host>/api/mcp`, but it stays inert (404) until an Ed25519 signing JWKS is supplied as `config.signingJwks`.
