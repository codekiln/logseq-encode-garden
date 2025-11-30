tags:: [[AI Coding]], [[Tool]]

- # [Vibe Kanban - Orchestrate AI Coding Agents](https://www.vibekanban.com/)
	- ## Overview
		- Platform designed to orchestrate AI coding agents, enabling developers to run multiple agents in parallel, manage tasks visually, and streamline code reviews
		- Integrates with various AI coding agents such as [[Claude Code]], [[OpenAI/Codex]], [[GitHub/CoPilot]], and others
		- Claims to be open source and built by developers for developers
	- ## Concerns / Risks
		- ### Not Actually Open Source
			- Some Reddit users complain that despite claims of being "open source," the tool is distributed as a compiled binary
			- The source code is not publicly available or auditable
			- This raises security concerns as users cannot verify what the binary actually does
		- ### Security Implications
			- Running compiled binaries from unknown sources is considered dangerous, especially for tools that interact with codebases and AI agents
			- Without source code access, users cannot audit for:
				- Malicious code
				- Data exfiltration
				- Unauthorized access to codebases or AI credentials
				- Backdoors or other security vulnerabilities
	- ## Key Features
		- ### Multi-Agent Orchestration
			- Run multiple AI coding agents simultaneously
			- Assign different tasks to specialized agents to enhance productivity
		- ### Visual Task Management
			- Intuitive kanban board to track each AI agent's progress
			- Clear overview of tasks in progress, ready for review, or completed
		- ### Seamless Code Review
			- Review AI-generated code directly within the interface
			- Start development servers, test changes, and merge confidently—all from one place
		- ### Centralized Configuration
			- Manage all AI agent configurations in a single location
			- Eliminates the need to switch between tools or track multiple settings
		- ### Parallel Workflows
			- Execute tasks in parallel or sequence
			- Allows AI agents to handle routine work while developers focus on architecture and complex problems
	- ## Getting Started
		- ### Installation
			- Requires Node.js 18+
			- Install via: `npx vibe-kanban`
		- ### Setup Steps
			1. Connect your preferred AI coding agents (Claude Code, Gemini CLI, Codex, etc.)
			2. Create tasks on your kanban board
			3. Assign tasks to appropriate AI agents
			4. Review code, merge changes, and deploy
	- ## Documentation
		- [Vibe Kanban Documentation](https://www.vibekanban.com/docs)
		- [Supported Coding Agents](https://www.vibekanban.com/docs/supported-coding-agents)
	- ## Related Concepts
		- [[AI/Coding/Concept/Multi-Agent Orchestration]]
		- [[AI/Coding/Technique/Knowledge Base/Agentic]]

