tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/Is there a way to remove recent items from the Claude Desktop Code tab?

- # Is there a way to remove recent items from the [[Claude/Desktop/Code]] tab?
	- ## [[AI Answer]]
		- **Short answer:** There is no in-app control to remove or clear entries from the **Recent** folder list in the Code tab. The only current workaround is to quit Claude Desktop and delete the entries by hand from the `projects` key in `~/.claude.json`.
		- **No in-app removal (as of mid-2026):** The Recent list has no right-click menu, hover action, "Remove from recents", or "Clear all" button, and Settings exposes no way to prune it. This is tracked as several open / duplicated requests: [#68350](https://github.com/anthropics/claude-code/issues/68350) (the one documenting the file workaround), [#72181](https://github.com/anthropics/claude-code/issues/72181), [#35187](https://github.com/anthropics/claude-code/issues/35187), and [#54044](https://github.com/anthropics/claude-code/issues/54044).
		- **File-editing workaround:** The Recent list is backed by the `projects` object in `~/.claude.json` (in your home directory), keyed by each folder's absolute path.
			- 1. **Quit Claude Desktop completely first.** A live session rewrites its own entry on exit, so edits made while the app is running are overwritten.
			- 2. Open `~/.claude.json` in a text editor and find the `"projects"` object.
			- 3. Delete the whole key/value block for the path you want gone (e.g. the `"/absolute/path/to/some-folder": { … }` entry). Deleting all inner entries — leaving `"projects": {}` — clears the list entirely.
			- 4. Save, then reopen Claude Desktop.
		- **Why duplicate-looking rows appear:** entries are keyed by absolute path, so the same folder name opened from two locations (e.g. one under `ghq/` and one under `Documents/`) shows as two separate Recent rows and needs two separate deletions.
		- **Caveat:** `~/.claude.json` also holds CLI settings and per-project state; edit only inside `"projects"` and keep a backup, since a malformed file can reset other state.
		- **Sources:** [Issue #68350 — no way to remove a project from recents without editing ~/.claude.json](https://github.com/anthropics/claude-code/issues/68350), [Issue #72181 — no way to remove entries from the "Recent" folders list](https://github.com/anthropics/claude-code/issues/72181).
