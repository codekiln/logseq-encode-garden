logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]

- # Can [[Obsidian]] be configured to show markdown files in folders that begin with a dot (dot-folders), e.g. to edit `.claude/skills/<skill-name>/SKILL.md`?
	- ## [[AI Answer]]
		- **Short answer:** Not natively — Obsidian hides any file or folder whose name starts with a dot from the file explorer, search, and graph, and there is no core setting to reveal them (the "Detect all file extensions" setting only affects unsupported file *types*, not dot-prefixed *names*). Community plugins close the gap.
		- ### Why the core setting doesn't help
			- Obsidian's vault adapter actively hides dotfiles/dot-folders; this is independent of the "Detect all file extensions" setting, which only toggles indexing of otherwise-unsupported extensions like `.json` or `.yml`. Users confirmed on the forum that enabling that setting still leaves a `.test`-style folder completely invisible.
		- ### Plugin options
			- **Hidden Folders Access** — opt-in, per-folder. You toggle specific root-level dot-folders (e.g. `.claude`, `.github`) in the plugin's settings, and it makes their contents visible in the file explorer, search, graph, metadata cache, and Bases — without renaming anything on disk, symlinking, or duplicating files. Because the folder keeps its literal dot-prefixed name on disk, external tools (git, Claude Code, other editors) are unaffected. This is the closest match for editing `.claude/skills/<skill-name>/SKILL.md` directly in Obsidian.
			  id:: 6a7348ad-b25e-434a-8b0e-b8e43b9dbc70
			- **Show Hidden Files** — broader, all-or-nothing. Exposes *every* dotfile/dot-folder plus unsupported file types at once by intercepting the vault adapter's deletion-reconciliation step (which is what Obsidian normally uses to hide dotfiles) and re-registering them. Simpler to install, but it also surfaces sensitive files like `.env` or `.git-credentials`, so it's less scoped than opting in folder-by-folder.
			- **obsidian-show-dotfiles** — a similar community plugin that browses/edits dot-prefixed folders in a dedicated sidebar panel rather than inline in the main file explorer.
		- ### Practical recommendation
			- For the stated goal (editing `.claude/skills/<skill-name>/SKILL.md`), install **Hidden Folders Access** and toggle on `.claude` specifically, rather than exposing every dotfile in the vault.
		- ### Sources
			- [Hidden Folders Access — Overview](https://dsebastien.github.io/obsidian-hidden-folders-access/)
			- [Hidden Folders Access — Obsidian community plugin listing](https://community.obsidian.md/plugins/hidden-folders-access)
			- [Surfacing Hidden Folders in Obsidian and Building an AI Base on Top](https://www.dsebastien.net/surfacing-hidden-folders-in-obsidian-and-building-an-ai-base-on-top/)
			- [Show Hidden Files — Obsidian community plugin listing](https://community.obsidian.md/plugins/show-hidden-files)
			- [obsidian-show-dotfiles — GitHub](https://github.com/chenqing0106/obsidian-show-dotfiles)
			- [Hidden folders (dotfiles) not showing in File Explorer despite "Detect all file types" — Obsidian Forum](https://forum.obsidian.md/t/hidden-folders-dotfiles-not-showing-in-file-explorer-despite-detect-all-file-types-being-enabled/106685)
			- [Enable use/access to hidden files and folders starting with a dot — Obsidian Forum feature request](https://forum.obsidian.md/t/enable-use-access-to-hidden-files-and-folders-starting-with-a-dot-dotfiles-dotfolders-within-obsidian/26908)