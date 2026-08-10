logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[CursorAI/Project Rule/Link/GitHub]]

- # Is there a convention for linking to a specific file and line in a [[GitHub]] or GitLab repo that an IDE can open and highlight?
	- ## [[AI Answer]]
		- **Short answer:** There are **two** conventions and they are separate. Code hosts use a **URL fragment**, not a query parameter — `#L42` and a range form. Editors use their own **URI scheme** (`vscode://`, `jetbrains://`), and only [[JetBrains]] actually uses query parameters. No standard bridges the two, so a single [[Markdown]] link cannot both render on the web and open in an IDE; extensions do the translation instead.
		- ### Host permalinks — the `#L` fragment
			- | Host | Single line | Range | Notes |
			  | ------------------ | ------------ | ------------- | ---------------------------------------------- |
			  | [[GitHub]]         | `#L42`       | `#L10-L20`    | also `#L10C5-L12C20` for column precision      |
			  | [[Gitlab]]         | `#L42`       | `#L10-20`     | range has no second `L`                        |
			  | Bitbucket          | `#<file>-42` | select + copy | anchor embeds the filename, e.g. `#test.py-29` |
			- Two rules make these durable and are the whole trick:
				- 1. Pin the path to a **commit SHA**, not a branch — `blob/<sha>/…` instead of `blob/main/…`. Both hosts bind `y` to "copy permalink", which rewrites the branch to the SHA for you.
				- 2. For a rendered file type (`.md` in particular), [[GitHub]] ignores line anchors until you defeat the renderer with `?plain=1`:
					- ~~~
					  https://github.com/<org>/<repo>/blob/<sha>/README.md?plain=1#L10-L20
					  ~~~
			- Pasting such a permalink into an issue, PR, or discussion body on [[GitHub]] expands it into a rendered code snippet.
		- ### Editor URI schemes — what an IDE actually picks up
			- | Editor | Shape |
			  | ------------------------------------- | ----------------------------------------------------------------------------- |
			  | [[VSCode]] (and [[CursorAI]] forks)   | `vscode://file/<absolute-path>:<line>:<col>` — forks swap the scheme name      |
			  | [[JetBrains]]                         | `jetbrains://<tool>/navigate/reference?project=<name>&path=<rel-path>:<line>`  |
			  | [[Zed]]                               | `zed://file/<absolute-path>:<line>`                                            |
			  | TextMate / MacVim                     | `txmt://open?url=file:///…&line=42`, `mvim://open?url=file:///…&line=42`       |
			- The `<tool>` tag in the [[JetBrains]] form is the IDE id — `idea`, `pycharm`, `webstorm`.
			- These are machine-local by construction: [[VSCode]] and [[Zed]] need an **absolute** path, and [[JetBrains]] needs a project name that exists on that machine. They belong in generated tooling output, not in a document committed to a repo.
		- ### The plain-text form that travels everywhere
			- `path/to/file.py:42` — optionally `:42:8` with a column. This is the grep and compiler-diagnostic convention, and terminals inside [[VSCode]], [[JetBrains]], iTerm2, and [[Ghostty]] linkify it and jump to the line.
			- It is not a URL, so it survives any transport, but it renders as inert text on the web.
		- ### Practical choice for a document living in the repo
			- **Read on the web** → SHA-pinned permalink with an `#L` range. Precise, permanent, but frozen to that commit.
			- **Read in an editor** → a relative [[Markdown]] link, `[foo.py](src/foo.py)`. [[VSCode]] honors an `#L23` anchor on a relative link when the **target is another `.md` file**; for source files it opens the file but does not jump to the line, so line precision is not portable here.
			- **Bridging** is extension territory: `open-in-vscode` opens a pasted [[GitHub]] or GitLab line link in the editor, and [[VSCode/Extension/GitLens]] does the reverse — copy the remote URL for the current line.
		- [[Answer/Official]] from [Creating a permanent link to a code snippet](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-a-permanent-link-to-a-code-snippet), [File management](https://docs.gitlab.com/user/project/repository/files/), [Hyperlink to source code in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/hyperlink-to-source-code-in-bitbucket/), and [Understanding JetBrains URL Scheme](https://medium.com/@alanhe421/understanding-jetbrains-url-scheme-4e315cd7cc63)
