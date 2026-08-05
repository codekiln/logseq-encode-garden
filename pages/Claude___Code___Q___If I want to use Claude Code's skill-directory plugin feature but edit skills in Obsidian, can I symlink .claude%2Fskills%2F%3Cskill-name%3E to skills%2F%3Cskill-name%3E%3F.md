logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/Can Obsidian be configured to show markdown files in folders that begin with a dot (dot-folders), e.g. to edit .claude/skills/<skill-name>/SKILL.md?]], [[Claude/Code/Plugin/Skills-Directory Plugin]]

- # If I want to use [[Claude/Code]]'s [[Claude/Code/Plugin/Skills-Directory Plugin]] feature but edit skills in [[Obsidian]], can I symlink `.claude/skills/<skill-name>` to `skills/<skill-name>`?
	- ## [[AI Answer]]
		- **Short answer:** Yes. Claude Code stats through symlinks when it scans `.claude/skills/`, so `.claude/skills/<skill-name>` can be a [[Symlink]] to a plain, non-dot folder like `skills/<skill-name>` — you edit the real files in [[Obsidian]] with zero configuration, and Claude Code loads the skill exactly as if it lived under the dot-directory directly. This sidesteps the [[Obsidian/Q/Can Obsidian be configured to show markdown files in folders that begin with a dot (dot-folders), e.g. to edit .claude/skills/<skill-name>/SKILL.md?]] problem entirely, since the real content never sits inside a hidden dot-folder.
		- ### What I verified (Claude Code 2.1.221, darwin-arm64)
			- Created `skills/test-skill/SKILL.md` with real frontmatter/content, then `ln -s ../../skills/test-skill .claude/skills/test-skill` (relative symlink) in a scratch project directory.
			- A fresh, non-interactive `claude -p` session in that directory logged `Loaded 1 unique skills (... project: 1 ...)` and, when asked, correctly quoted the skill's exact description pulled through the symlink — confirming a plain skill folder resolves fine as a symlink.
			- Repeated the test for a full **skills-directory plugin** (`.claude-plugin/plugin.json` + a nested `skills/` folder, per [[Claude/Code/Plugin/Skills-Directory Plugin]]), also symlinked in. `claude plugin list` detected it too, reporting it as a found project-scope plugin directory — the manifest was read through the symlink without issue.
		- ### The one catch: project-scope plugin trust, not the symlink
			- The skills-directory *plugin* case (manifest-bearing folder) didn't load automatically in the test — but the reason had nothing to do with the symlink. `claude plugin list` reported it explicitly: "1 project-scope plugin directory under `./.claude/skills/` was not loaded because this workspace was not trusted when plugins were scanned." That is the same trust gate [[Claude/Code/Plugin/Skills-Directory Plugin]] documents for any project-scope `@skills-dir` plugin, symlinked or not — accept the workspace trust dialog (or run `/reload-plugins` afterward) and it loads.
			- A **plain skill** (just `SKILL.md`, no `plugin.json`) isn't gated the same way — it loaded immediately, even in a fresh non-interactive session with no trust dialog involved.
		- ### Practical setup
			- Keep the real files outside the dot-directory: `skills/<skill-name>/SKILL.md` (or the full plugin folder for a skills-directory plugin).
			- Symlink it in with a **relative** link so it survives clone/move: `ln -s ../../skills/<skill-name> .claude/skills/<skill-name>`.
			- Edit `skills/<skill-name>/SKILL.md` directly in [[Obsidian]] — `skills/` isn't a dot-folder, so none of the dot-folder-visibility plugins are needed for this path.
			- `SKILL.md` edits take effect immediately in a running Claude Code session; other plugin pieces (`hooks/`, `.mcp.json`, `agents/`) still need `/reload-plugins` or a restart, per [[Claude/Code/Plugin/Skills-Directory Plugin]].
		- ### A competing convention worth knowing
			- Some orgs standardize the symlink in the *other* direction — treat `.claude/skills/` as canonical and symlink a plain-named directory (e.g. `.agents/skills`) to it, so other tools reach the same content without touching Obsidian visibility at all. Either direction is a valid use of the same underlying mechanism (dot-folder scanning follows symlinks); which one to use depends on whether the dot-directory or the plain directory is your source of truth.
		- ### Sources
			- [Plugins reference — Skills-directory plugins](https://code.claude.com/docs/en/plugins-reference#skills-directory-plugins)
			- Empirical test against locally installed `claude` 2.1.221 (debug log + `claude plugin list` output), described above.
