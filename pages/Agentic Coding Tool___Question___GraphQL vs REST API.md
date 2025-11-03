tags:: [[AI Coding]], [[Question]]

- # Question: Are agentic coding tools better at using GraphQL vs REST APIs?
	- This is an open question about the comparative effectiveness of agentic coding tools when working with GraphQL APIs versus REST APIs.
	- ## Considerations
		- GraphQL advantages for AI agents:
			- Strongly typed schema could help with tool/function calling
			- Single endpoint might simplify agent decision-making
			- Schema introspection provides self-documenting API structure
			- Queries allow requesting exactly needed fields
		- REST API advantages for AI agents:
			- Multiple endpoints might provide clearer action boundaries
			- More familiar pattern - large language models trained on more REST examples
			- Standard HTTP verbs (GET, POST, PUT, DELETE) align with common agent actions
			- Typically more verbose documentation and examples available
		- GraphQL challenges for AI agents:
			- Query construction requires understanding nested relationships
			- Mutations can be complex to construct correctly
			- May require understanding of GraphQL-specific concepts
		- REST API challenges for AI agents:
			- May require multiple API calls to get related data
			- Less self-documenting - requires understanding full API structure
			- Over-fetching or under-fetching data
	- ## Existing Literature
		- | Title                                                                    | Description                                                                                                                                  | Year / Venue | Link                                                                                                   |
		  | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------ |
		  | Sequential API Function Calling Using GraphQL Schema (GraphQL‑RestBench) | Dataset of natural‑language utterances paired with sequences of REST API calls using a GraphQL schema prompt to study LLM function‑calling.  | 2024 (EMNLP) | [https://aclanthology.org/2024.emnlp-main.1083.pdf](https://aclanthology.org/2024.emnlp-main.1083.pdf) |
		  | PrediQL: Automated Testing of GraphQL APIs with LLMs                     | Retrieval‑augmented, LLM‑guided fuzzer for GraphQL APIs that uses adaptive bandit learning for query generation and vulnerability detection. | 2025 (arXiv) | [https://arxiv.org/html/2510.10407v1](https://arxiv.org/html/2510.10407v1)                             |
		  | Large Language Models – Based Fuzzing Techniques: A Survey               | Survey of LLM‑based fuzzing tools and methods, including API/fuzzer contexts.                                                                | 2024 (arXiv) | [https://arxiv.org/html/2402.00350v1](https://arxiv.org/html/2402.00350v1)                             |
		-
	- ## Related
		- [[Atlassian/Confluence/API/GraphQL]]
		- [[Atlassian/Confluence/API/REST/v2]]
		- [[AI/Coding/Agentic]]