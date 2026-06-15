logseq-entity:: [[Logseq/Entity/Question]]

- # How can I configure Foam to use a subfolder as the workspace root?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- [[Answer/Official]] from [foam.files.include — foambubble/foam package.json](https://github.com/foambubble/foam/blob/master/packages/foam-vscode/package.json)
			- **Short answer:** two approaches work — a VS Code workspace file (`.code-workspace`) or the `foam.files.include` setting.
			- ### Method 1: VS Code workspace file (recommended for monorepos)
				- Create `<repo_root>/foam.code-workspace`:
				- ~~~json
				  {
				    "folders": [
				      { "path": "my-garden" }
				    ]
				  }
				  ~~~
				- Open VS Code by opening `foam.code-workspace` instead of the repo root folder. Foam treats `my-garden` as the workspace root; all daily note paths, template paths, and wikilinks resolve relative to it.
			- ### Method 2: `foam.files.include` setting
				- In `.vscode/settings.json` at the repo root (or in the `"settings"` block of your `.code-workspace`):
				- ~~~json
				  {
				    "foam.files.include": ["my-garden/**"]
				  }
				  ~~~
				- Per the official description: `"Use this to limit Foam to specific directories (e.g., ["notes/**"]) or file types."` Foam will only index and graph files under `my-garden/`. VS Code's workspace root stays at the repo root, so daily-note and template paths in settings must be written relative to the repo root (e.g. `"foam.openDailyNote.directory": "my-garden/journals"`).
			- ### Method 3: open the subfolder directly
				- The simplest approach — open `my-garden/` directly in VS Code (`File > Open Folder`). No configuration needed; Foam sees the folder as the workspace root.
			- ### Comparison
				- - 1. `.code-workspace` file — cleanest for monorepo; all Foam-relative paths resolve inside `my-garden`; lets VS Code also include sibling folders (e.g. `tools/`) if needed.
				- - 2. `foam.files.include` — keeps the repo root open; useful when other VS Code tooling needs the full repo in scope; requires manually prefixing Foam path settings.
				- - 3. Open subfolder directly — simplest; loses easy access to repo-root tooling.
