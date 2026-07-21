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
				- **[[Claude Code/MCP/Server]]s**: Create `.mcp.json` for external tool integration
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
		- Four steps: build one or more **[[Claude Code Plugin]]s**, define `.claude-plugin/marketplace.json` at the marketplace repo root, host that repo on a git provider, then share it — users add it with `/plugin marketplace add` and install individual plugins with `/plugin install`.
		- ### Marketplace file required fields
			- `name` — kebab-case identifier; public-facing (`/plugin install my-tool@your-marketplace`). Each user can register only one marketplace per name — adding a second with the same name replaces the first.
			- `owner` — object with `name` (required) and `email` (optional).
			- `plugins` — array of plugin entries.
			- Reserved names blocked for third-party marketplaces (official Anthropic use only): `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `claude-plugins-community`, `claude-community`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `anthropic-agent-skills`, `knowledge-work-plugins`, `life-sciences`, `claude-for-legal`, `claude-for-financial-services`, `financial-services-plugins`, `first-party-plugins`, `healthcare` — plus names that impersonate an official one.
		- ### Marketplace file optional fields
			- `description`, `version` — also accepted nested under `metadata` for backward compatibility.
			- `$schema` — JSON Schema URL for editor autocomplete; ignored by Claude Code at load time.
			- `metadata.pluginRoot` — base directory prepended to relative plugin source paths.
			- `allowCrossMarketplaceDependenciesOn` — other marketplaces this marketplace's plugins may depend on; unlisted dependencies are blocked at install.
			- `renames` — map from a former plugin `name` to its current name, or to `null` if removed (Claude Code v2.1.193+).
		- ### Plugin entries
			- Required: `name` (kebab-case, public-facing) and `source` (where to fetch the plugin — see below).
			- Can include any plugin-manifest field (`description`, `version`, `author`, `commands`, `hooks`, …) plus marketplace-only fields: `category`, `tags`, `strict`, `relevance`, `defaultEnabled`, `displayName`.
			- `strict` (default `true`): `true` means `plugin.json` is authoritative and the marketplace entry only supplements it; `false` means the marketplace entry is the entire definition, and a component-declaring `plugin.json` on top of that is a load-time conflict.
			- Component paths (`skills`, `commands`, `agents`, `hooks`, `mcpServers`, `lspServers`) can point at custom subpaths, so several entries can share one plugin repo's directory tree without loading each other's components.
		- ### Plugin sources
			- | Source        | Fields                       | Notes                                                       |
			  | ------------- | ---------------------------- | ----------------------------------------------------------- |
			  | relative path | none                         | must start with `./`, resolves against the marketplace root |
			  | `github`      | repo, ref?, sha?             | GitHub `owner/repo`                                         |
			  | `url`         | url, ref?, sha?              | any git host                                                |
			  | `git-subdir`  | url, path, ref?, sha?        | sparse clone of one subdir, good for monorepos              |
			  | `npm`         | package, version?, registry? | installed via `npm install`                                 |
			- `github`, `url`, and `git-subdir` all accept `ref` (branch/tag) and `sha` (exact commit); when both are set, `sha` wins.
			- Relative-path plugins only resolve when the marketplace itself was added from git or a local directory. A marketplace added by direct URL to `marketplace.json` downloads just that file, so relative-path entries fail — use `github`, `npm`, or a git URL source instead.
		- ### Hosting and distribution
			- GitHub is the recommended host: `/plugin marketplace add owner/repo`. Any git host (GitLab, Bitbucket, self-hosted) works via its full URL.
			- To auto-prompt a team to install a marketplace on trusting the project folder, add it under `extraKnownMarketplaces` in `.claude/settings.json`; pair with `enabledPlugins` to set defaults.
			- `strictKnownMarketplaces` (managed settings) restricts which marketplaces users may add at all — an empty array locks it down completely, or an allowlist matches by exact source, `hostPattern`, or `pathPattern`.
			- Private repos: manual install/update reuses normal git credential helpers (HTTPS or SSH). Background auto-update disables credential helpers for its `git pull` — SSH keys loaded in `ssh-agent` still work — and falls back to a full re-clone on failure; set `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1` to keep the stale clone instead of re-cloning.
		- ### Version resolution
			- Resolved in order: `plugin.json` `version` → marketplace-entry `version` → git commit SHA.
			- Setting `version` pins the plugin to that string — bump it on every release, or omit it on a git-based source so every new commit counts as a new version.
			- Release channels: point two marketplaces at different refs/SHAs of the same plugin repo, then assign each to a user group through managed settings.
		- ### Renaming or removing a plugin
			- `name` is the stable identifier referenced in `enabledPlugins` and `pluginConfigs`; set `displayName` to change the UI label without breaking existing installs.
			- To actually rename or remove an entry, add a top-level `renames` map (former name → new name, or `null` if removed) so existing users migrate automatically instead of hitting `plugin-not-found`. Treat it as append-only history — never edit or delete a prior mapping.
		- ### CLI management
			- `claude plugin marketplace add <source> [--scope user|project|local] [--sparse <paths...>]`
			- `claude plugin marketplace list [--json]`
			- `claude plugin marketplace remove <name> [--scope ...]`
			- `claude plugin marketplace update [name]`
			- Validate before sharing: `claude plugin validate .` against a marketplace directory, or against an individual plugin directory to check its `plugin.json` and skill/agent/command frontmatter.
		- ### See also
			- [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins)
			- [Plugins](https://code.claude.com/docs/en/plugins)
			- [Plugins reference](https://code.claude.com/docs/en/plugins-reference)