logseq-entity:: [[Logseq/Entity/Concept]]

- # Claude Project RAG
	- Retrieval augmented generation (RAG) is how a Claude project holds more knowledge than fits in the model's context window.
	- ## Notes from the official docs
		- [Retrieval augmented generation (RAG) for projects | Claude Help Center](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
			- RAG for projects is available on paid plans (Pro, Max, Team, and Enterprise).
			- Previously, projects had a knowledge capacity limit based on the [context window](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans). Once you reached this threshold, it wasn't possible to add more content. With RAG, you can continue adding knowledge beyond these limits while maintaining full functionality.
			- RAG activates automatically when needed.
			- All existing projects automatically benefit from RAG when the project knowledge exceeds context limits.
		- The same article says RAG can expand capacity by up to 10x, shows a visual indicator when a project is RAG-enabled, and can switch a project back to context-based processing if knowledge drops below the threshold. In RAG mode Claude uses a project knowledge search tool to retrieve relevant passages.
	- ## Open
		- The point at which RAG starts, and how the capacity percentage behaves once it does, are not stated in the docs. See [[Claude/Project/Q/What is the limit on the capacity for adding knowledge to a Claude project?]].
