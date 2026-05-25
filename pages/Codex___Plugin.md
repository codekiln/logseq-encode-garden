# [Build plugins – Codex](https://developers.openai.com/codex/plugins/build)
	- Author-facing guide; for installing and using plugins in Codex, see [Plugins](https://developers.openai.com/codex/plugins).
	- Prefer a local [[Codex/Skill]] while iterating on one repo or one personal workflow; build a plugin to share across teams, bundle app integrations or MCP config, package lifecycle hooks, or publish a stable package.
	- ## Scaffold with `@plugin-creator`
		- Built-in skill scaffolds `.codex-plugin/plugin.json` and can generate a local marketplace entry for testing.
		- Existing plugin folders can use `@plugin-creator` to wire into a local marketplace.
	- ## Marketplaces
		- JSON catalog of plugins; one marketplace can start as a single-plugin test list and grow into a curated catalog.
		- Repo-scoped: `$REPO_ROOT/.agents/plugins/marketplace.json` with plugins often under `$REPO_ROOT/plugins/`.
		- Personal: `~/.agents/plugins/marketplace.json` with plugins often under `~/.codex/plugins/`.
		- Each `plugins[]` entry: `source.path` is `./`-prefixed relative to the marketplace root (not relative to `.agents/plugins/`); `interface.displayName` is the picker label; include `policy.installation`, `policy.authentication`, and `category` on each entry.
		- Restart Codex after marketplace changes.
		- ### CLI
			- ~~~
			  codex plugin marketplace add owner/repo
			  codex plugin marketplace add owner/repo --ref main
			  codex plugin marketplace add https://github.com/example/plugins.git --sparse .agents/plugins
			  codex plugin marketplace add ./local-marketplace-root
			  ~~~
			- `codex plugin marketplace list` — configured marketplaces and resolved roots.
			- `codex plugin marketplace upgrade` / `remove marketplace-name`.
			- Git sources: `owner/repo`, `owner/repo@ref`, HTTP/HTTPS/SSH URLs; `--sparse PATH` (repeatable) for sparse checkout; `--ref` pins a ref.
		- Codex also reads legacy `$REPO_ROOT/.claude-plugin/marketplace.json`.
		- Installs land in `~/.codex/plugins/cache/$MARKETPLACE_NAME/$PLUGIN_NAME/$VERSION/` (`local` for local plugins); per-plugin on/off in `~/.codex/config.toml`.
	- ## Minimal plugin (manual)
		- Manifest at `.codex-plugin/plugin.json` only inside `.codex-plugin/`; `skills/`, `hooks/`, `assets/`, `.mcp.json`, `.app.json` at plugin root.
		- ~~~
		  {
		    "name": "my-first-plugin",
		    "version": "1.0.0",
		    "description": "Reusable greeting workflow",
		    "skills": "./skills/"
		  }
		  ~~~
		- Stable kebab-case `name` — plugin identifier and component namespace.
		- Skill at `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`) and body instructions.
		- Wire into a marketplace (via `@plugin-creator` or manual `marketplace.json`), restart Codex.
	- ## Workspace sharing (Codex app)
		- Plugins → Created by you → Share — workspace members or link; appears under Shared with you (not public Plugin Directory).
		- Admins can set `plugin_sharing = false` in `requirements.toml`.
	- ## Manifest (published shape)
		- Top-level: `name`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, `skills`, `mcpServers`, `apps`, `hooks`.
		- `interface`: `displayName`, `shortDescription`, `longDescription`, `developerName`, `category`, `capabilities`, legal URLs, `defaultPrompt`, `brandColor`, `composerIcon`, `logo`, `screenshots`.
		- Paths relative to plugin root, start with `./`; assets under `./assets/` when possible.
		- Default hooks file `hooks/hooks.json` is auto-discovered; manifest `hooks` can override (path, array of paths, or inline objects).
		- Hook commands get `PLUGIN_ROOT`, `PLUGIN_DATA` (and `CLAUDE_PLUGIN_*` for compatibility); plugin hooks are non-managed until user trusts them ([Hooks](https://developers.openai.com/codex/hooks)).
	- ## Bundled MCP
		- `.mcp.json` may be a direct server map or wrapped `mcp_servers` object.
		- Post-install policy in config, e.g. `plugins."my-plugin".mcp_servers.docs` with `enabled`, `default_tools_approval_mode`, per-tool `approval_mode`.
	- ## Git-backed marketplace entries
		- `"source": "url"` when plugin is at repo root; `"source": "git-subdir"` with `url`, `path`, `ref` or `sha` for subdirectory plugins.
		- Unresolvable entries are skipped without failing the whole marketplace.
	- Official Plugin Directory self-serve publishing: coming soon.
	- ## Related
		- [[Person/Every/GitHub/compound-engineering-plugin]] — example marketplace plugin (`codex plugin marketplace add EveryInc/compound-engineering-plugin`); see [[Engineer/ing/Compound]].