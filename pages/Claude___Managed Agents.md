logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Anthropic]]

- # [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)
	- Anthropic's service for running Claude agents through the Claude API: it runs the agent loop, stores agents and sessions, and runs tools in a sandbox.
	- In beta under the header `managed-agents-2026-04-01`, and on by default for all API accounts.
	- Three ways to run it, per the [self-hosted page](https://platform.claude.com/docs/en/managed-agents/self-hosted):
		- Cloud sandboxes (default): Anthropic runs the sandboxes, the service and the model.
		- [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes): you run the sandboxes; Anthropic runs the service and the model.
		- Self-hosted Managed Agents, launched 2026-11-12: you run the sandboxes and the service, and choose the model provider. Access is by request through an Anthropic account team.
	- ## Features
		- [[Claude/Managed Agents/Vault]] — stores credentials for MCP servers and environment variables, attached to sessions by ID.
