# [Add Command | Rulesync](https://rulesync.dyoshikawa.com/reference/cli-commands.html#add-command)
	- The `add` command can either scaffold one Rulesync feature file or append one declarative source to `rulesync.jsonc`. See [[rulesync/Skill/Declarative Source]] for the source-fetching workflow this feeds.
	- ## Feature scaffolding
		- A feature keyword creates a valid, editable starter file
			- ```bash
			  # Named Markdown features
			  rulesync add rule --name overview
			  rulesync add command --name review-pr.md
			  rulesync add subagent --name planner
			  rulesync add skill --name project-context
			  rulesync add check --name security
			  
			  # Singleton features
			  rulesync add mcp
			  rulesync add hooks
			  rulesync add permissions
			  
			  # Deprecated compatibility scaffold; prefer permissions
			  rulesync add ignore
			  ```
		- Named features accept a name with or without the `.md` suffix. Skills use the directory layout `.rulesync/skills/<name>/SKILL.md`; other named features create `<name>.md` in their canonical directory. Names cannot contain path separators.
		- When the target file exists, interactive execution asks before replacing it; declining leaves it unchanged. JSON, silent, and non-interactive execution fail safely — pass `--force` to overwrite explicitly.
		- Feature keywords are reserved when no source-specific option is present. To add a source whose identifier is also a feature keyword, supply a source option that makes the intent explicit, e.g. `rulesync add skill --transport npm`.
	- ## Declarative sources
		- For any other source identifier, `add` appends one source to `rulesync.jsonc`, preserving JSONC comments, and immediately runs the declarative source resolver: it installs selected rules into `.rulesync/rules/.curated/`, selected skills into `.rulesync/skills/.curated/`, and updates `rulesync.lock` or `rulesync-npm.lock.json`.
			- ```bash
			  # GitHub source (default transport)
			  rulesync add anthropics/skills --skills skill-creator
			  
			  # Rules only; direct .md files are selected from rules/
			  rulesync add acme/ai-standards --rules testing-guidelines,typescript-conventions
			  
			  # Rules and skills from separate paths in one source
			  rulesync add acme/ai-assets --rules "*" --rules-path exports/rules --skills review-pr --path exports/skills
			  
			  # Any Git remote through the git CLI (uses local git credentials, e.g. GCM/SSH)
			  rulesync add https://example.com/team/skills.git --transport git --ref main --path skills
			  
			  # npm-compatible registry
			  rulesync add @acme/skill-package --transport npm --registry https://registry.npmjs.org
			  ```
		- The selected configuration file must already exist — run `rulesync init` first, or pass `--config <path>`. Adding a source whose normalized identity is already present fails rather than silently duplicating lockfile entries; edit the existing entry instead.
		- Only the source being added is fetched; existing declarations are not re-fetched, and they must already be locked/installed (run `rulesync install` first if not). The operation is transactional: if the new source fails to install, Rulesync restores the manifest, source lockfiles, curated rules, and curated skills to their pre-command state.
		- ### Options
			- | Option | Description |
			  | --- | --- |
			  | `--name <name>` | Name for a rule, command, subagent, skill, or check scaffold |
			  | `--force` | Replace an existing scaffold file without prompting |
			  | `--skills <skills>` | Comma-separated skill names. `*` selects all skills. |
			  | `--rules <rules>` | Comma-separated rule names. Names may omit `.md`; `*` selects direct `.md` files under rulesPath. |
			  | `--transport <type>` | `github` (default), `git`, or experimental `npm` |
			  | `--ref <ref>` | Git ref, npm version, or npm dist-tag |
			  | `--path <path>` | Skills path within the source; defaults to `skills` |
			  | `--rules-path <path>` | Rules path within the source; defaults to `rules` |
			  | `--registry <url>` | npm-compatible registry URL |
			  | `--token-env <name>` | Environment variable containing the npm registry token |
			  | `--token <token>` | GitHub token for private repositories |
			  | `--config <path>` | Configuration file to edit (default: `rulesync.jsonc`) |
		- When neither `--skills` nor `--rules` is given, all skills are installed for backward compatibility. Providing only `--rules` installs no skills.
