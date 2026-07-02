logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude Code/Plugin/Marketplace]], [[Claude/Desktop/Extension]]

- # Is it possible to add plugin marketplaces, install plugins, etc. for Claude Code in Claude Desktop, all using the CLI?
	- ## [[AI Answer]]
		- Short answer: **yes, partially** — [[Claude/Code]] plugin/marketplace management works from the CLI, but as `/plugin` slash commands typed inside an interactive session, not standalone shell subcommands. [[Claude/Desktop]]'s own extension system is separate and has no CLI at all.
		- ### Claude Code plugin/marketplace commands
			- Inside a running `claude` session: `/plugin marketplace add <source>`, `/plugin marketplace list`, `/plugin marketplace update [name]`, `/plugin marketplace remove <name>` manage marketplaces; `/plugin install <name>@<marketplace>`, `/plugin uninstall`, `/plugin list`, `/plugin enable`/`/plugin disable`, `/plugin update <name>` manage plugins. [[Answer/Official]] from [Discover and install plugins - Claude Code Docs](https://code.claude.com/docs/en/discover-plugins.md)
			- There is no headless `claude plugin install ...` shell subcommand documented — these are slash commands that only work inside an active session, not arguments to the `claude` binary itself.
		- ### Scripting an alternative: editing settings directly
			- Marketplace and enabled-plugin state lives under `extraKnownMarketplaces` and `enabledPlugins` keys in `~/.claude/settings.json` (user scope) or a project's `.claude/settings.json`. Editing this file directly and restarting Claude Code is a workable non-interactive path for provisioning plugins, e.g. from dotfiles or a setup script. [[Answer/Official]] from [Plugins reference - Claude Code Docs](https://code.claude.com/docs/en/plugins-reference)
		- ### Claude Desktop is a separate system for this
			- The embedded Claude Code panel inside [[Claude/Desktop]] is still [[Claude/Code]] running in a terminal panel — it uses the exact same plugin/marketplace mechanism above.
			- [[Claude/Desktop]]'s own **Extensions** feature (Settings > Extensions) is unrelated: it installs `.mcpb`-packaged local MCP servers, not Claude Code plugins (skills/agents/hooks/commands), and is GUI-only with no CLI or scripting path — see [[Claude/Desktop/Extension]].
		- Bottom line: Claude Code plugin/marketplace setup can be scripted by editing `settings.json` even though there's no dedicated non-interactive CLI subcommand; Claude Desktop's separate Extensions system can't be managed from the CLI at all.
