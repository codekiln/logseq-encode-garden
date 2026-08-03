logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[LangChain]]
see-also:: [[LangSmith/MCP/Remote]]

- # [LangChain Docs MCP](https://docs.langchain.com/use-these-docs)
	- Two complementary [[MCP]] servers that let an AI application query the LangChain documentation in real time. LangChain recommends connecting both — the guides supply the why and how, the reference supplies exact signatures.
	- | Server                | URL                                   | Covers                                                                                   |
	  | ----                  | ----                                  | ----                                                                                     |
	  | `docs-langchain`      | `https://docs.langchain.com/mcp`      | Conceptual guides, how-tos, tutorials, and product docs for [[LangChain]], [[langgraph]], and [[LangSmith]] |
	  | `reference-langchain` | `https://reference.langchain.com/mcp` | API reference: classes, methods, parameters, and signatures for all LangChain packages    |
	- No authentication — these serve public documentation, unlike the workspace-scoped [[LangSmith/MCP/Remote]].
	- Add both to [[Claude/Code]] with `claude mcp add --transport http docs-langchain https://docs.langchain.com/mcp` (and the same for `reference-langchain`). Project scope is the default; add `--scope user` to get them in every project.
	- [[Claude/Desktop]] takes the two URLs under **Settings → Connectors**. [[CursorAI]], [[VS Code]], [[Codex]], and Deep Agents Code each take them as `mcpServers` / `servers` entries in their own MCP config.
	- Built on Mintlify's MCP support, so every docs page also offers a contextual menu with [[llms.txt]] and copy-page options.
