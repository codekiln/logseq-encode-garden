logseq-entity:: [[Logseq/Entity/Software/Project]]
see-also:: [[AI/Agent/Harness]], [[langgraph]]

- # [Deep Agents](https://docs.langchain.com/deepagents)
	- [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) — 29,853 [[GitHub/Star]]s as of [[2026-09-29 Tue]]
	- "The batteries-included agent harness." Built on [[langgraph]].
	- Written in [[Python]]; a [[TypeScript]] version lives at [langchain-ai/deepagentsjs](https://github.com/langchain-ai/deepagentsjs).
	- Built-in capabilities: a virtual filesystem for context management, [[AI/Agent/Subagent]] spawning, long-term memory in `AGENTS.md` files, [[AI/Agent/Skill]]s, task planning, and [[AI/Workflow/Human in the Loop]] approval.
	- ## Virtual filesystem
		- Every deep agent gets file tools: `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob` and `grep`. With a sandbox backend it also gets `execute` for shell commands.
		- The files live wherever the configured backend puts them:
			- `StateBackend` — in the agent's [[langgraph]] state, scoped to one thread; the default
			- `FilesystemBackend` — real files under a root directory on local disk
			- `LocalShellBackend` — local disk plus shell execution
			- `StoreBackend` — the LangGraph store, persisting across threads, with storage scoped per user, per assistant or per thread
			- `CompositeBackend` — routes path prefixes to different backends, such as `/memories/` to the store and everything else to state
			- a custom backend that implements `ls`, `read`, `write`, `edit`, `glob` and `grep`
		- Permission rules declare which paths the agent can read or write. They don't apply to sandbox backends.
		- The filesystem does the context offloading:
			- a tool result over 20,000 tokens is saved to a file and replaced by its path and first 10 lines; the agent re-reads or greps it when needed
			- once context passes 85% of the model's window, older large file writes and edits in history are replaced by a pointer to the file
		- Source: [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview), [Backends](https://docs.langchain.com/oss/python/deepagents/backends), [Context engineering](https://docs.langchain.com/oss/python/deepagents/context-engineering)
