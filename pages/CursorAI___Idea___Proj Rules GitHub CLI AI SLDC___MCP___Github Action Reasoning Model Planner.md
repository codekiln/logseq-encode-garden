tags:: Idea

- # Using #[[GitHub Action]] create plans and triage project status and backlog with a #[[LLM Reasoning Model]] using #MCP
	- ## Context
		- The parent idea, [[CursorAI/Idea/Proj Rules GitHub CLI AI SLDC/MCP]] describes how #[[GitHub/MCP]] could enable Cursor to utilize GitHub project planning functionalities. This would enable it to plan what to do and possibly keep an agent scratchpad in the issue comments whose history is more idiomatically recorded in the repository, the way that a real software engineer would.
	- ## Impetus
		- This idea extends the parent idea farther. Many Cursor power users swear that using a reasoning model to create the action plan is an essential first step to effectively using Cursor; see also [[CursorAI/Technique/Frontload Design]]. As of early 2025, it is a bit awkward to use reasoning models in Cursor.
			- It's not possible to use one's own API key to use reasoning models:
				- {{embed [[CursorAI/Settings/API Keys/OpenAI API Keys]]}}
			- Also, using reasoning models requires usage-based pricing, which isn't feasible for every person or team; in particular, usage-based pricing may be disabled at the team-level:
				- {{embed [[CursorAI/Usage-Based Pricing/For Premium Models]]}}
		- ## Idea - develop a GitHub Action which uses MCP to interact with GitHub
		  id:: 67b34adf-84b1-42b5-9ec7-9762d794bad0
			- As a result of the above, we could develop a GitHub Action which is itself an MCP client that could utilize a #[[GitHub MCP]] server in the action itself to develop more advanced planning abilities. For #Example -
				- an execution plan for each issue
				- filing issues or sub-tasks
				- organizing the project backlog to sequence work
			- An API key with access to a reasoning model could be used to execute planning in the issues.
			- A [[Github Scheduled Workflow]] #cron could "wake up" and do [[Backlog Grooming]] on the project
			- When a [[git commit]] is pushed, it could trigger a workflow that would execute a "plan" with an [[LLM Reasoning Model]] against the [[Best Next Action]], storing an [[Intermediate Work Product]] somewhere in the GitHub Project, such as in an Issue Comment
			- The local CursorAI model could use its *own* access to MCP to access the Intermediate Work Product left in the project to start from the instructions the LLM Reasoning Model left.
		- ## The difference between [[System 1 vs System 2 Thinking]] may be mirrored in fast, intuitive Local Cursor usage vs slow, [[CICD]]-initiated use of [[LLM Reasoning Model]]s to conduct advanced [[Backlog Grooming]] and initiate [[CursorAI/Technique/Frontload Design]]
		  id:: 67b34ff1-a5f9-4b33-ae50-1b9bd81c36ff
			- [[Inference Time Compute]] cost and latency grows with the length of the [[Chain of Thought]]. It may eventually be structurally important to bifurcate when and where we use reasoning models.
				- The cost structure of reasoning models encourage Cursor and likely also other [[AI Coding Tool]]s to develop licensing models that restricts the use of reasoning models in their agent mode.
			- But there remains an important need to develop a well-reasoned plan on what to do. CICD may have a role in doing some [[System 2 Thinking]] pre-work and sequencing to help the [[System 1 Thinking]] [[CursorAI/Agent Mode]] make the most of its resources.