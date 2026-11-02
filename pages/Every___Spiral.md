logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Every]]
alias:: [[Spiral/App]], [[Write With Spiral]]

- # [Spiral](https://writewithspiral.com/)
	- AI writing partner from [[Every]] that learns a writer's voice from samples, uploads, or connected social channels, then drafts, edits, and rewrites text in that voice.
	- Pitched as a writing partner "for you and your agent": agents reach it over [[MCP]] or its API.
	- Sold on its own (Personal $15/month, Team $25/user/month) or in the Every bundle ($30/month) with [[Cora]], Monologue, Sparkle, Proof, and Plus One. Prices as of [[2026/11/02]].
	- ## MCP server
		- Remote Streamable HTTP server at `https://api.writewithspiral.com/mcp/`. Per-client setup steps: [agents.md](https://writewithspiral.com/agents.md).
		- Auth is OAuth by default: the first connection opens a browser to sign in. A paid plan can instead use an API key (`spiral_sk_...`, from Settings → Agent & API Keys) sent as `Authorization: Bearer`.
		- [[Claude/Code]]:
			- ~~~bash
			  claude mcp add --transport http --scope user spiral https://api.writewithspiral.com/mcp/
			  ~~~
		- Tools include `spiral_generate_writing`, `spiral_personalize_text` (rewrite in your voice), `spiral_humanize_text` (strip AI tells), `spiral_add_voice_samples`, and `spiral_list_workspaces`. The writing tools need a paid plan.
		- This garden's agents connect with the `connect-spiral` command in `.rulesync/commands/`.
