logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/In obsidian, how can I link to a heading in another file?]], [[Obsidian/Q/Is there a keyboard shortcut in Obsidian for quickly finding keyboard shortcuts in Obsidian?]]

- # What [[Obsidian]] [[Keyshort/User]] assigned to a plugin is useful for pointing to pages and headings when working with external agentic coding tools like [[Claude Code]]? [[card]]
  card-last-score:: 5
  card-repeats:: 2
  card-next-schedule:: 2026-06-28T20:45:31.520Z
  card-last-interval:: 4.61
  card-ease-factor:: 2.6
  card-last-reviewed:: 2026-06-24T06:45:31.520Z
	- ## [[My Answer]]
		- given you've installed [[Obsidian/Plugin/Easy Copy]] and have mapped the hotkeys to my preferences, `SHIFT + OPTION + C` copies a link to a heading
	- ## [[AI Answer]]
		- **Short answer:** Obsidian has no built-in hotkey for these by default, but two built-in commands cover files and two community plugins fill the heading-link gap. Assign hotkeys to them in **Settings → Hotkeys**.
		- ### Built-in commands (no default hotkey — must assign)
			- **Copy file path** — copies the vault-relative path (e.g. `folder/note.md`) to the clipboard. This is the most direct way to hand a file reference to [[Claude Code]] so it can read or edit that file.
			- **Copy Obsidian URL** — copies a deep-link URI in the form `obsidian://open?vault=VaultName&file=folder%2Fnote`. Useful when an external tool can open URLs, less useful for raw file-path needs.
			- Fastest way to discover what a command's hotkey is (or assign one): open the **Command palette** (`Cmd+P` / `Ctrl+P`), search for "copy file path" or "copy obsidian url", and the assigned hotkey is shown beside the command. To assign one, go to **Settings → Hotkeys** and search for the command name.
		- ### For headings (needs a community plugin)
			- Obsidian has **no native** "copy link to heading" command. Two widely-used plugins fill this gap:
				- [[Obsidian/Plugin/Easy Copy]] — place the cursor on a heading line, then trigger **Easy Copy: Contextual Copy** (you assign the hotkey). It copies `[[Note#Heading]]` to the clipboard. Works for blocks and paragraphs too.
				- [[Obsidian/Plugin/Copy Link]] — adds commands for copying wikilinks to files, headings, and blocks, including anchor variants like `[[Note#Heading]]` and block URLs.
			- After installing either plugin, go to **Settings → Hotkeys**, search for the plugin's command name, and assign a short chord (e.g. `Ctrl+Shift+H` for heading links).
		- ### Recommended minimal setup for Claude Code workflows
			- 1. Assign **Copy file path** to a short hotkey — gives Claude Code the vault-relative path it needs to open or edit the file.
			- 2. Install **Easy Copy** and assign its **Contextual Copy** command — place cursor on any heading to grab `[[Note#Heading]]`, which you can then paste into a Claude Code prompt as a precise pointer.
			- 3. (Optional) Right-click the file tab or the file in the sidebar → **Copy file path** works without a hotkey if you prefer the mouse.
		- ### Sources
			- [Obsidian Help — Hotkeys](https://help.obsidian.md/hotkeys)
			- [Easy Copy plugin — Obsidian Community Plugins](https://community.obsidian.md/plugins/easy-copy)
			- [Copy Link plugin — GitHub](https://github.com/greetclammy/copy-link)
			- [Forum: Copy link to bullet / heading and relative command palette shortcuts](https://forum.obsidian.md/t/copy-link-to-bullet-heading-and-relative-command-palette-shortcuts/18935)
			- [Forum: Add "Copy Wikilink" command](https://forum.obsidian.md/t/add-copy-wikilink-command/56121)