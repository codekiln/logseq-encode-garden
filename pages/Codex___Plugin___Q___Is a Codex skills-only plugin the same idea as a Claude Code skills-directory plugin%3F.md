logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Agent/Skills/Dir]]

- # Is a [[Codex/Plugin]] built as a "skills-only plugin" the same idea as a [[Claude/Code/Plugin/Skills-Directory Plugin]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Build plugins – Codex](https://learn.chatgpt.com/docs/build-plugins#create-a-skills-only-plugin-manually) and [Plugins reference — Skills-directory plugins](https://code.claude.com/docs/en/plugins-reference#skills-directory-plugins).
		- **Short answer:** No. The names collide but the two terms describe different axes. **Skills-only** is about *composition* — a plugin whose only component type is skills. **Skills-directory** is about *discovery* — a plugin found in place because of where its folder sits.
		- ### The two axes
			- | Axis | Codex "skills-only plugin" | Claude "skills-directory plugin" |
			  | ---- | ---- | ---- |
			  | What varies | Which components the bundle contains | How the host finds and loads the bundle |
			  | Defining trait | Manifest points at `skills/` and nothing else | A `.claude-plugin/plugin.json` inside a skills directory |
			  | Components allowed | Skills only, by definition | Anything — skills, agents, hooks, MCP |
			  | Install step | Yes: register in a marketplace source, then install | None: loads on the next session, labeled `<name>@skills-dir` |
			  | Lives where | Anywhere; the marketplace entry points at it | `~/.claude/skills/` or a project's `.claude/skills/` |
		- ### Why the Codex tree is the opposite row
			- The minimal Codex layout is `meeting-follow-up/` containing `.codex-plugin/plugin.json` and `skills/meeting-follow-up/SKILL.md`. In the table on [[Claude/Code/Plugin/Skills-Directory Plugin]] that is the **third** row — a skill packaged *inside* a plugin — which that page explicitly separates from the skills-directory case.
			- A skills-directory plugin is the **second** row: the manifest sits at `<skills-dir>/foo/.claude-plugin/plugin.json`, so the folder you were already using for a plain skill becomes a plugin without moving or installing anything.
		- ### What each actually maps to
			- Codex's skills-only plugin ↔ an ordinary Claude plugin that happens to ship only skills. Same idea, both need a marketplace source and an install.
			- Claude's skills-directory plugin ↔ Codex's repo marketplace plus project plugin configuration is the closest supported plugin workflow. Codex still installs a cached copy; it does not document discovering a full plugin merely from a manifest placed inside `.agents/skills/`.
			- For editing skills in place, use a plain [[Codex/Skill]] in a scanned directory: `$CWD/.agents/skills`, `$CWD/../.agents/skills`, `$REPO_ROOT/.agents/skills`, or `$HOME/.agents/skills`.
		- ### The practical difference
			- The skills-directory plugin exists to remove the install loop while authoring — edit `SKILL.md` and the running session picks it up; `/reload-plugins` for the rest. Codex's plugin workflow uses a marketplace and an installed copy. For its cache and refresh behavior, see [[Codex/Plugin/Q/Does registering a local plugin copy it into a home-directory cache?]].
		- ### Repo activation in current Codex clients
			- As of October 15, 2026, a repo can expose plugins through `.agents/plugins/marketplace.json` and enable one through its trusted project `.codex/config.toml`:
				- ~~~toml
				  [plugins."my-plugin@local-repo"]
				  enabled = true
				  ~~~
			- `my-plugin` matches the catalog entry; `local-repo` matches the catalog's top-level `name`. The catalog alone makes the plugin discoverable. Configured plugins can be installed or refreshed during marketplace refresh, even when configured as disabled. [Enable or disable a plugin for a repo](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).
			- This provides a declarative repo setup for supported local Codex clients, subject to project trust and enforced requirements. It does not establish a universal promise that opening a repo activates the plugin in every ChatGPT Work surface. Workspace-imported plugins have separately managed installation and enabled state.
			- To develop and distribute the package, see [[ChatGPT/Plugin/How To/Develop and Share a Team Plugin for ChatGPT and Claude]].
