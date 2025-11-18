alias:: [[Claude Code Marketplace]], [[Claude Code Marketplaces]]

- # Claude Code Plugin Marketplaces
	- Official docs: [Plugin marketplaces - Claude Code Docs](https://code.claude.com/docs/en/plugin-marketplaces)
	- ## [[My Notes]]
		- Claude Code Plugin Marketplaces are defined by [[Claude Code/.claude-plugin/marketplace.json]] [docs here](https://code.claude.com/docs/en/plugin-marketplaces#create-your-own-marketplace).
			- A **[[Claude Code Marketplace]]** can define many [[Claude Code Plugin]]s.
			- Each **[[Claude Code Plugin]]** can have many
				- **[[Claude Code/Command]]s**: Create markdown files in `commands/` directory
				- **[[Claude Code/Subagent]]s**: Create agent definitions in `agents/` directory
				- **[[Claude Code Skills]]**: Create `SKILL.md` files in `skills/` directory
				- **[[Claude Code/Hook]]s**: Create `hooks/hooks.json` for event handling
				- **[[Claude Code/MCP Server]]s**: Create `.mcp.json` for external tool integration
			- For example, [[Person/Daniel Avila/GitHub/claude-code-templates]] defines within its marketplace.json a [supabase-toolkit plugin](https://github.com/davila7/claude-code-templates/blob/main/.claude-plugin/marketplace.json#L31-L55) for [[Supabase]] (among dozens of other plugins)
				- ```
				  {
				        "name": "supabase-toolkit",
				        "source": "./",
				        "description": "Complete Supabase workflow with specialized commands, data engineering agents, and MCP integrations",
				        "version": "1.0.0",
				        "author": {"name": "Daniel Avila"},
				        "license": "MIT",
				        "keywords": ["supabase", "database", "postgresql", "data"],
				        "strict": false,
				        "commands": [
				          "./cli-tool/components/commands/database/supabase-backup-manager.md",
				          "./cli-tool/components/commands/database/supabase-data-explorer.md",
				          "./cli-tool/components/commands/database/supabase-migration-assistant.md",
				          "./cli-tool/components/commands/database/supabase-performance-optimizer.md",
				          "./cli-tool/components/commands/database/supabase-schema-sync.md"
				        ],
				        "agents": [
				          "./cli-tool/components/agents/data-ai/data-engineer.md",
				          "./cli-tool/components/agents/data-ai/data-scientist.md"
				        ],
				        "mcpServers": [
				          "./cli-tool/components/mcps/database/postgresql-integration.json",
				          "./cli-tool/components/mcps/database/mysql-integration.json",
				          "./cli-tool/components/mcps/database/supabase.json"
				        ]
				      }
				  ```
			-
	- ## Creating a Claude Code Plugin Marketplace
		-