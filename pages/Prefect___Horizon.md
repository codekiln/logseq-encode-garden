created-by:: [[Prefect]]
logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [Horizon](https://www.prefect.io/horizon)
	- Enterprise [[MCP/Gateway/Enterprise]] and governance platform for deploying, discovering, managing, and controlling [[MCP]] servers across teams.
	- Works with any MCP-compliant client, including Claude, Cursor, Windsurf, VS Code, OpenAI, and Amazon Bedrock.
	- Built on [[FastMCP]], the open-source Python framework from [[Prefect]].
	- ## Capabilities
		- **Deploy** — push code to GitHub and get a production MCP server URL in ~60 seconds, with built-in OAuth 2.1, autoscaling, and monitoring.
		- **Registry** — centralized catalog of internal and third-party MCP servers with ownership tracking, version management, and approval workflows.
		- **Gateway & access control** — tool-level role-based access control, authentication tied to identity providers, and audit trails for every access attempt.
		- **Remix** — compose custom MCP endpoints by combining tools from multiple servers for a team's specific needs.
	- ## Identity & security
		- Supports 65+ identity-provider integrations across SAML, OIDC, OAuth, and SCIM, including Okta, Microsoft Entra ID, Google Workspace, and Auth0.
