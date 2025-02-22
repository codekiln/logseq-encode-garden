tags:: [[Anthropic/MCP]], #langgraph, Agentic

- # [Multi-Agent Workflows with MCP](https://www.ai.engineer/summit/2025/schedule/mcp-workflows)
	- summary
	  collapsed:: true
		- by [[Person/Dan Mason]]
			- Agents aren't really agents unless they can discover the world outside of the chatbox, and act on it -- and the MCP (Model Context Protocol) is an emerging standard for connecting agents to physical and digital worlds. This workshop will teach you how to build your own MCP client (not just the one built into Claude) and connect it to a multi-agent system (we'll be using [[langgraph]] but this approach works with Autogen, Crew AI and many more). This allows you to build powerful workflows that go way beyond writing code, and rethink how to express business logic as a set of roles, tools, and desired outcomes. We'll walk through examples together and then put them into practice -- come with ideas of workflows you want to build! [List of existing MCP servers here]
			- | Date   | Time          | Track      | Room                                       |
			  |-------:|:-------------:|:----------:|:-------------------------------------------|
			  | Feb 22 | 4:10pm-5:30pm | Workshops  | Jay Suites Sydney - 109 W 38th 2nd floor   |
			-
	- 16:12
	- ### MCP Workflows Workshop Notes
		- **Speaker:** Dan Mason, Principal, AI @ Stride (ex-ESPN, SSTK, NBCU)
		- **Setup for Hands-on Participation:**
			- Local environment with **Python 3.12+**
			- Package managers: **brew (or similar), pip, uv**
			- **LLM API keys** for Claude, OpenAI (OAI), Gemini
		- **Resources:**
			- **Links to Dan Mason’s GitHub, LinkedIn, etc.:** [http://jpsi.me](http://jpsi.me)
			- **Simple ReAct agent (LangGraph) with MCP gateway:**
				- [GitHub Repo](https://github.com/danmas0n/react-agent-with-mcp/)
			- **Multi-agent system (LangGraph) with MCP gateway:**
				- [GitHub Repo](https://github.com/danmas0n/multi-agent-with-mcp/)
	- ### [[Key Insight]] - #MCP is #Lego
	- #langgraph is the easiest to explain of all the frameworks #Quote -- [[Person/Dan Mason]]
		- it is #Expensive at least it gan me
		- it is model agnostic
	-