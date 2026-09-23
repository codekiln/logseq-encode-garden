logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Obsidian/Plugin/Easy Copy]], [[Obsidian/Plugin/Copy Link]]
via:: [[PKM/Log/26/09/23 Wed - Stacked Discussions in Multi-Tier Gardens]]
- # Can a [[Keyshort]] add a block id to a todo in [[Obsidian]], compatible with a [[Logseq/Block/Reference]]?
	- ## [[AI Answer]]
		- **Short answer:** yes for the block id — a todo is a list item, and two plugins already tracked here mint an id and copy a link to it from one bindable command. No for the [[Logseq]] half: nothing produces a `((uuid))` that [[Logseq]] resolves.
		- ### Native block ids reach a todo, but no command mints them
			- [[Answer/Official]] from [Link to a block in a note](https://help.obsidian.md/links#Link+to+a+block+in+a+note).
			- A block is "a unit of text in your note, such as a paragraph, block quote, or list item," so a `- [ ] task` line qualifies. For a list item the identifier sits directly on the bullet: `- [ ] call the bank ^37006f`.
			- Typing `^` inside a link opens a picker of existing blocks, and `[[^^text]]` searches blocks across the vault.
			- Obsidian ships no command that creates an identifier, so out of the box there is nothing in **Settings → Hotkeys** to bind.
		- ### Plugins that mint the id on a keystroke
			- [[Obsidian/Plugin/Easy Copy]] — **Contextual Copy** with **Auto block ID** enabled generates an identifier for the block under the cursor and copies `[[Note#^blockid|summary]]`. Already bound here to `⌥ ⇧ C`, per ((6a218786-743c-420e-babe-492761235524)).
			- [[Obsidian/Plugin/Copy Link]] — **Copy block link** auto-creates or reuses an identifier and yields `[[Note#^blockid]]`, one link per line across a multi-block selection. It also offers **Copy anchor link** (`[[#^blockid]]`) and **Copy block URL** (an `obsidian://open` deep link). Installed through [[BRAT]] rather than the directory.
			- Both are ordinary commands, so either can carry a hotkey. Neither treats a task line specially, which is what makes them work on todos.
		- ### Where compatibility stops
			- Obsidian writes `^blockid` trailing the line and references it as `[[Note#^blockid]]`, embedding as `![[Note#^blockid]]`.
			- Logseq writes `id:: <uuid>` as a block property on its own line and references it as `((uuid))`.
			- The identifier format and the reference syntax both differ, so a link either tool makes is inert in the other. A bridge would need a plugin that writes `id:: <uuid>` beneath the task and copies `((uuid))` to the clipboard.
			- [[Obsidian/Plugin/Obsidian Todoseq]] is the closest thing that exists: it reads Logseq's `TODO` / `DOING` / `DONE` / `LATER` / `NOW` / `WAIT` keywords and `SCHEDULED:` / `DEADLINE:` metadata. It carries the task vocabulary across, not the reference syntax.
		- ### Scope of this answer
			- Drawn from the official Obsidian help and from the plugins recorded in this garden. The full community directory was not swept, so a `((uuid))`-emitting plugin may exist unrecorded.
