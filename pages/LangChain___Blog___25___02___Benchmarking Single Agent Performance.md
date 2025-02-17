date-created:: [[2025-02-10 Mon]]

- # TODO [Benchmarking Single Agent Performance](https://blog.langchain.dev/react-agent-benchmarking/)
	- [[Key Insight]]
	  id:: 67b34893-0cae-45d0-80a2-7942b7a8f81b
		- Both more context and more tools degrade agent performance
		- Agents that require longer trajectories degrade more quickly
		- #o1, #o3-mini, and #[[Claude 3.5 Sonnet]] are comparable and in a different league than #4o and [[Meta/AI/Model/llama/3.3-70B]]
		- #[[o3-mini]] performs as well as #[[o1]] and #[[Claude 3.5 Sonnet]] with smaller context, **but sees a steeper performance drop as context grows**
		  id:: 67b34954-34da-4d44-b9c0-7ad1e37ebf3c