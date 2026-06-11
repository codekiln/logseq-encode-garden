tags:: [[Claude/Code]], [[Diataxis/Explanation]]
see-also:: [[Claude/Code/Settings]]

- # Claude Code Settings Override & Precedence
	- ## Overview
		- When the **same key** appears in more than one Claude Code configuration file, the result is decided by two separate mechanisms that are easy to conflate:
			- 1. **`settings.json` scopes** — a fixed set of locations (user, project, local, managed) combined by a **precedence order**. There is no directory walk; each scope is a known path.
			- 2. **`CLAUDE.md` / rules** — instruction files that Claude Code discovers by **walking up the directory tree** and concatenating, rather than overriding.
		- "Override" therefore means different things depending on which mechanism is in play. The headline rule for `settings.json`: **most keys are *replaced* by the highest-precedence scope that defines them — they are not deep-merged.** A handful of keys are deliberate exceptions (permissions, some arrays, and plugin enablement).
	- ## The `settings.json` scopes
		- **Managed / enterprise policy** — system locations (`managed-settings.json`), plus MDM/OS policy and a `managed-settings.d/` drop-in directory. Cannot be overridden by anything below.
		- **User** — `~/.claude/settings.json`. Applies to every project on the machine.
		- **Project (shared)** — `.claude/settings.json`. Checked into source control and shared with the team.
		- **Project (local)** — `.claude/settings.local.json`. Personal, not checked in; Claude Code configures git to ignore it on creation.
	- ## Precedence order (highest → lowest)
		- 1. **Managed** — can't be overridden by anything.
		- 2. **Command-line arguments** — temporary, session-only overrides.
		- 3. **Local** (`.claude/settings.local.json`) — overrides project and user.
		- 4. **Project** (`.claude/settings.json`) — overrides user.
		- 5. **User** (`~/.claude/settings.json`) — applies when nothing more specific does.
		- The official phrasing: *"When the same setting appears in multiple scopes, Claude Code applies them in priority order."*
	- ## What "override" actually does: replace vs. merge
		- ### Default: replace
			- For most keys, the **highest-precedence scope that defines the key supplies the entire value** — lower scopes are ignored for that key. A `model` set in local replaces the `model` in project, which replaces the one in user.
		- ### Exception: permission rules merge
			- *"Permission rules behave differently because they merge across scopes rather than override."* The effective `allow` / `ask` / `deny` sets are the **union** across all scopes, so a project `deny` still applies even if your user settings only add `allow` entries.
		- ### Exception: a few arrays merge
			- Specific list-valued keys are documented to combine across scopes rather than replace — e.g. `claudeMdExcludes` (*"Arrays merge across layers"*) and the hook-related `allowedHttpHookUrls` / `httpHookAllowedEnvVars`.
		- ### Counter-example: `fallbackModel` does **not** merge
			- *"Unlike most array settings, this key does not merge across settings files: the highest-precedence file that defines it supplies the entire chain."* A reminder that array-valued ≠ automatically merged.
		- ### Managed drop-in directory deep-merges
			- Within managed settings, `managed-settings.json` is the base and `managed-settings.d/*.json` are merged on top alphabetically: *"Later files override earlier ones for scalar values; arrays are concatenated and de-duplicated; objects are deep-merged."* This deep-merge is specific to the managed drop-in layer, not to the user/project/local layers.
	- ## Plugins: resolved per-plugin across scopes
		- Plugin configuration is the case most relevant to a shared project file, and it behaves more like permissions than like a replaced scalar — each plugin's state is tracked **per-plugin, per-scope** (the **Installed** tab in `/plugin` groups plugins by the scope that enabled them).
		- ### `enabledPlugins`
			- An **object** mapping `"plugin-id@marketplace-id"` → boolean.
			- ~~~json
			  {
			    "enabledPlugins": {
			      "code-formatter@team-tools": true,
			      "deployment-tools@team-tools": true,
			      "experimental-features@personal": false
			    }
			  }
			  ~~~
			- Because resolution is per-plugin, a higher scope only overrides the **specific plugins it names** — you do not have to restate the whole map. Project settings take precedence over user settings, so setting a plugin to `false` in `~/.claude/settings.json` does **not** disable one the project's `.claude/settings.json` enables; to opt out on your machine, set that plugin `false` in `.claude/settings.local.json`.
		- ### `extraKnownMarketplaces`
			- An **object** mapping a marketplace name → a `source` config. Used in a project's `.claude/settings.json` so teammates automatically have the required plugin sources (they're prompted to install once they trust the folder).
			- ~~~json
			  {
			    "extraKnownMarketplaces": {
			      "my-team-tools": {
			        "source": { "source": "github", "repo": "your-org/claude-plugins" }
			      }
			    }
			  }
			  ~~~
			- Source shapes include `github` (`repo`, optional `ref`/`path`), `git` (`url`), `url`, `npm`, `file`, and `directory`. Prefer `github`/`git` for anything checked in — a local `directory` path won't resolve on a teammate's machine or in a fresh container.
		- ### What `/plugin` writes
			- `/plugin install plugin@marketplace` installs to **user scope** (`~/.claude/settings.json`) by default.
			- The interactive UI (and `--scope`) let you choose **project** scope (writes to `.claude/settings.json`, shared) or **local** scope (writes to `.claude/settings.local.json`, personal to the repo). `/plugin enable` / `/plugin disable` toggle the corresponding `enabledPlugins` entry.
	- ## Does Claude walk up parent directories?
		- **`settings.json`: no.** The scopes are fixed, known paths (user home, the project's `.claude/`, managed locations). Claude Code does not climb parent directories hunting for a `settings.json`; it reads the four scopes and applies the precedence above.
		- **`CLAUDE.md` / `CLAUDE.local.md`: yes.** *"Claude Code reads CLAUDE.md files by walking up the directory tree from your current working directory, checking each directory along the way."* All discovered files are **concatenated** (root → cwd order), not overridden — so a parent `CLAUDE.md` and a nested one both apply. Files in subdirectories load on demand when Claude reads files there. `.claude/rules/*.md` follow the same model.
	- ## Worked example: one shared Codespace, different plugins per person
		- **Goal:** everyone shares an identical checked-in `.claude/settings.json`, but each person enables a different mix of plugins.
		- 1. In the **shared** `.claude/settings.json`, register the marketplace via `extraKnownMarketplaces` (github source) and enable only the universal baseline in `enabledPlugins`.
		- 2. Each person puts their personal plugin toggles in **`.claude/settings.local.json`** (gitignored). Since `enabledPlugins` resolves per-plugin, local only needs the deltas — additional plugins set `true`, and any baseline plugin they want off set `false`.
		- 3. Because **local > project > user**, the local file wins for exactly the plugins it names and leaves the rest of the shared config untouched. Pushing customization into `settings.local.json` (rather than `~/.claude/settings.json`) is what makes per-person opt-out of a project-enabled plugin possible.
	- ## See also
		- [[Claude/Code/Settings]] — full settings reference (keys, env vars, the precedence list).
		- [[Claude Code/Plugin/Marketplace]] — marketplace `marketplace.json` structure.
		- [[Claude Code/Plugin]]
	- ## Sources
		- [Claude Code settings](https://code.claude.com/docs/en/settings) — settings files, precedence, replace-vs-merge.
		- [Discover and install prebuilt plugins](https://code.claude.com/docs/en/discover-plugins) — `enabledPlugins`, scopes, `/plugin install` defaults.
		- [Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) — `extraKnownMarketplaces`, team marketplaces.
		- [How Claude remembers your project](https://code.claude.com/docs/en/memory) — `CLAUDE.md` directory-tree traversal and concatenation.
