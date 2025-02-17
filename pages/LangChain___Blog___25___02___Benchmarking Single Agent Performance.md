# TODO [Benchmarking Single Agent Performance](https://blog.langchain.dev/react-agent-benchmarking/)
	- [[Key Insight]]
	  id:: 67b34893-0cae-45d0-80a2-7942b7a8f81b
		- Both more context and more tools degrade agent performance
		- Agents that require longer trajectories degrade more quickly
		- [[OpenAI/Model/o1]], [[OpenAI/Model/o3/Mini]], and [[Anthropic/Model/Claude/3.5/Sonnet]] are comparable and in a different league than [[OpenAI/Model/GPT/4o]] and [[Meta/AI/Model/llama/3.3-70B]]
		- [[o3-mini]] performs as well as [[o1]] and [[Claude 3.5 Sonnet]] with smaller context, but sees a steeper performance drop as context grows