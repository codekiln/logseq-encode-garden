logseq-entity:: [[Logseq/Entity/Question]]

- # Can each hackathon team share one API key through Claude Enterprise connectors, and how does ChatGPT secrets management differ?
	- ## [[AI Answer]]
		- **Short answer:** Neither product has a general secrets vault that a team member can add a key to. Claude's closest feature is a custom connector with a stored request header, which an Owner sets up once for the organization, so team members never handle the key. ChatGPT's closest features are GPT Action API-key auth and Codex cloud environment secrets.
		- **Claude: how a stored key works**
			- [[Answer/Official]] from [Anthropic: Add a connector that isn't in the directory](https://claude.com/docs/connectors/custom/add-unlisted).
				- An Owner (or, on Enterprise, a member with a custom role that manages the organization's libraries) adds a custom [[MCP]] connector under **Organization settings > Connectors**. Members then see it under **Customize > Connectors** and click **Connect**.
				- If the server uses an API key, choose **No sign-in** and put the key under **Request headers**. Claude stores each header value securely, does not show it again after saving, and sends it on every request.
				- Request headers suit a credential the whole organization shares, such as a service account. For per-person access, use OAuth.
				- Up to four headers. Header names are reviewed by Anthropic before Claude sends them, with `authorization`, `x-api-key`, and `x-auth-token` offered by default.
				- Authentication settings cannot be edited after the connector is created; remove it and add it again.
				- **Request headers are in beta for a limited set of organizations.** If the section is missing from the dialog, the organization does not have it yet.
			- **Gaps for the hackathon plan**
				- A team member cannot add their own key to their own account as a stored secret. The Owner-added connector is the stored-secret path, and the key sits with the Owner, not the team member.
				- One connector holds one key. Ten teams with ten keys need ten connectors, and I found no documented way to give each connector to one group of members only. [[Claude/Cowork]] and chat both see whatever connectors the member has enabled, so a team could use another team's connector unless an admin scopes it.
				- Anthropic's [Enterprise-managed auth](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization) assigns a connector to roles from identity-provider groups, so it is the documented route for per-group access. The article does not say which authentication types it covers or where credentials are stored, so I could not confirm it works with a plain API key.
		- **Claude desktop only: local extensions**
			- [[Answer/Official]] from [Anthropic: Getting started with local MCP servers on Claude Desktop](https://support.claude.com/en/articles/10949351). Desktop extensions (MCPB) mark fields as `"sensitive": true` in the manifest, and [[Claude/Desktop]] encrypts those values with the operating system's secure store (Keychain on macOS, Credential Manager on Windows).
			- This is per machine and per user: each team member would install the extension and paste the key once. It does not travel to other devices, other people, or cloud sessions.
			- A third-party critique, [Cyata](https://cyata.ai/blog/whispering-secrets-loudly-patch-meet-bypass/), argues that the encrypted blobs are not bound to the extension that created them, so another extension could reuse them. I could not verify that against Anthropic documentation.
		- **Claude: what does not exist**
			- Anthropic has no account-level secrets vault for chat, Cowork, and Claude Code. A feature request for one, [account-level secrets vault](https://claudeissues.com/issue/70716-feature-account-level-secrets-credentials-vault-across-chat-cowork-and-claude-co), was closed as not planned.
			- Without a vault, people paste keys into chat, where they stay in conversation history and the model can read them back. OAuth connector tokens are the exception, held server-side and hidden from the model.
		- **ChatGPT: what exists**
			- **GPT Actions.** [OpenAI: GPT Action authentication](https://developers.openai.com/api/docs/actions/authentication). The GPT builder can set API key auth (Basic, Bearer, or custom header) or OAuth, and the key is encrypted when stored. The page does not say who can view it afterward or how it behaves for people the GPT is shared with. OpenAI is retiring custom GPTs; a third-party search snippet puts Enterprise retirement at Dec 11, 2026, which I did not confirm on an OpenAI page.
			- **Apps and MCP connectors.** This rests on vendor guides, not OpenAI documentation ([Boomi](https://help.boomi.com/docs/Atomsphere/Platform/Connect_chatgpt_setup), [StackOne](https://www.stackone.com/blog/best-mcp-gateway-for-chatgpt-enterprise/)). Developer Mode and full read-write custom MCP apps need Business, Enterprise, or Education, and an admin or owner must enable Developer Mode. ChatGPT supports OAuth and no-auth. I found no sourced description of a stored shared API-key header like Claude's.
			- **Codex cloud secrets.** [[Answer/Official]] from [OpenAI: Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment). Secrets are an environment-level setting with an extra layer of encryption, decrypted only when a task runs. They are available to setup scripts only and are removed before the agent phase, so the agent itself cannot read them. The page does not say who can edit secrets or whether workspace members share them. For [[Codex]] work, this is the nearest thing to a managed secret in ChatGPT, but it exists for running a repository, not for giving chat or a GPT a key.
			- **Workspace controls.** Enterprise and Education workspaces disable apps by default, and admins grant access per app and per group, including limiting tools to read-only.
		- **Comparison for the hackathon**
			- | | Claude Enterprise | ChatGPT Enterprise |
			  |---|---|---|
			  | Admin stores one shared key for everyone | Custom connector with a request header (beta, limited orgs) | GPT Action API key (GPTs being retired); no sourced header equivalent for MCP apps |
			  | Team member stores their own key | Only locally, via a sensitive field in a desktop extension | Not found in documentation |
			  | Key hidden from the model | Yes for stored header and OAuth tokens | Codex secrets are removed before the agent phase; Action keys are encrypted |
			  | Per-group access | Enterprise-managed auth (identity-provider groups); header connectors not documented as scoped | Per-app, per-group admin grants |
			  | General vault across surfaces | None | None |
			- **Possible route for per-team keys (my suggestion, untested):** put each team's key behind a small MCP server or gateway the organization runs, authenticate it with each person's own OAuth login, and keep the key on the server. Both products connect to a remote MCP server, and neither has to store the key.
		- **Unverified:** whether the request-headers beta is open to this organization; whether a header connector can be limited to a group; and how ChatGPT treats a GPT Action key for people a GPT is shared with. Each needs a check in the organization's admin console or with the vendor.
