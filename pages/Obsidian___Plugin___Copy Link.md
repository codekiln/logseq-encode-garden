logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Person/churnish]]

- # [Copy Link](https://github.com/churnish/copy-link)
	- [[Obsidian]] community plugin by churnish that adds right-click commands for copying links to files, headings, and blocks in multiple formats.
	- **Downloads:** ~520 · **Status:** not yet in official Community Plugins directory — install via [[BRAT]] · **PR pending:** [obsidianmd/obsidian-releases#8068](https://github.com/obsidianmd/obsidian-releases/pull/8068)
	- ## Features
		- ### File commands (file context menu)
			- **Copy note link** — shortest unique path wikilink, e.g. `[[Note]]`.
			- **Copy note link as footnote** — inline footnote form: `^[[[Note]]]`.
			- **Copy note embed** — `![[Note]]`.
		- ### Block commands (editor context menu)
			- **Copy block link** — auto-creates or reuses a block ID: `[[Note#^blockid]]`. Supports multi-block selection (one link per line).
			- **Copy block embed** — `![[Note#^blockid]]`. Multi-block aware.
			- **Copy block link as footnote** — `^[[[Note#^blockid]]]`. Multi-block aware.
			- **Copy anchor link** — just the anchor without the file path: `[[#^blockid]]`.
			- **Copy block URL** — `obsidian://open?vault=…&file=…%23%5Eblockid` deep link.
			- **Copy block link with selection as caption** — `[[Note#^blockid|selected text]]`.
	- ## Installation
		- Install [[BRAT]], then add `churnish/copy-link` via BRAT's **Add plugin** flow.
		- Or download `copy-link.zip` from the [latest release](https://github.com/churnish/copy-link/releases) and unzip into `.obsidian/plugins/`.
