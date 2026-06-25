logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a setting that hides or shows dot folders and dot files in the [[VSCode/Term/Explorer]] panel on the left by default?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [files.exclude - VS Code docs](https://code.visualstudio.com/docs/getstarted/settings)
		- **Short answer:** `files.exclude` controls which files and folders are hidden from the Explorer. VS Code does **not** hide all dot files by default — only a small set of VCS/system entries. Adding `**/.*` hides all dot-prefixed items.
		- VS Code's **`files.exclude`** setting (User or Workspace scope) accepts glob patterns; any matched path is hidden from the Explorer sidebar and from quick-open.
		- Default entries shipped with VS Code:
			- `**/.git` → `true`
			- `**/.svn` → `true`
			- `**/.hg` → `true`
			- `**/CVS` → `true`
			- `**/.DS_Store` → `true`
			- `**/Thumbs.db` → `true`
		- These defaults hide specific VCS/OS metadata but **not** dot files in general (`.env`, `.claude`, `.rulesync`, etc. all appear in the Explorer by default).
		- To hide **all** dot files and dot folders, open Settings JSON and add:
			- ~~~json
			  "files.exclude": {
			    "**/.*": true
			  }
			  ~~~
		- There is no built-in Explorer toggle button for dot-file visibility; it is always controlled through `files.exclude` in settings.
		- The related setting **`search.exclude`** controls which files are omitted from search results — it is independent of Explorer visibility.
		- Since VS Code 1.73, **`explorer.excludeGitIgnore`** (`true`/`false`) hides all `.gitignore`-matched entries from the Explorer (see [[VSCode/Q/Is there any way to toggle the visibility of gitignored items in the sidebar]]).
