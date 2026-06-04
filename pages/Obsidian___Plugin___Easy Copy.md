logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Person/Moy]]

- # [Easy Copy](https://obsidian.md/plugins?id=easy-copy)
	- [[Obsidian]] community plugin by Moy ([Moyf/easy-copy](https://github.com/Moyf/easy-copy)) that copies content intelligently based on cursor position.
	- **Downloads:** ~8,100 · **Status:** in official Community Plugins directory · **Version:** 1.7.1 (actively maintained)
	- ## Features
		- ### Contextual Copy (single command)
			- The core command **Easy Copy: Contextual Copy** detects what's at the cursor and acts accordingly — no need to think about which command to use.
			- **Inline code** — cursor inside `` `code` `` → copies the code text without the backticks.
			- **Formatted text** — cursor in `**bold**`, `*italic*`, or `==highlighted==` → copies the text without the markup.
			- **Heading line** — cursor on a heading → copies an internal link to that heading as `[[Note#Heading|Heading]]` (display text is the heading itself, so the link renders shorter visually).
			- **Block link** — cursor in a paragraph that already has a block ID → copies `[[Note#^blockid|summary]]`.
			- **Auto block ID** (optional, enable in settings) — if the paragraph has no block ID, the plugin generates one and copies the link with a content summary as display text.
		- ### Settings
			- **Link format** — wikilink (`[[Note#Heading|display]]`) or Markdown (`[display](Note#Heading)`).
			- **Custom copy targets** — toggle which element types (bold, italic, etc.) are included.
			- **Show notifications** — optional toast when content is copied.
			- **Right-click menu** — can add Contextual Copy to the editor context menu.
	- ## Installation
		- Search **Easy Copy** in Settings → Community plugins → Browse.
		- No default hotkey — assign one (e.g. `Ctrl+Alt+C`) in Settings → Hotkeys.
