logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/What Obsidian keyboard shortcuts are most useful for pointing to pages and headings when working with external agentic coding tools like Claude Code?]]

- # If I'm using [[dotfiles]], can I set a global hotkey for [[Obsidian]] actions like copy file path and copy link to heading? [[card]]
	- ## [[My Answer]]
		- this isn't sufficiently answered yet. it's unclear what would let you copy the path to a heading
	- ## [[AI Answer]]
		- **Short answer:** Yes — two distinct things both go by "global hotkey" here, and dotfiles cover both paths.
		- ### 1. Managing in-app Obsidian hotkeys via dotfiles
			- Obsidian stores all assigned hotkeys in **`.obsidian/hotkeys.json`** inside the vault root. You can track this file with [[chezmoi]], [[GNU Stow]], or any symlink-based dotfiles manager.
			- Format is JSON: each entry maps a command ID to an array of key combos (modifiers + key).
			- **Caveat:** this is vault-local, not global to the OS. These hotkeys only fire when Obsidian is the focused app. If you want the same bindings on every machine, tracking `.obsidian/hotkeys.json` in your dotfiles repo is the right move.
			- Example structure:
				- ~~~json
				  {
				    "editor:copy-path": [{"modifiers": ["Mod", "Shift"], "key": "P"}]
				  }
				  ~~~
		- ### 2. System-wide (global) hotkeys — fire even when Obsidian is not focused
			- **obsidian-global-hotkeys plugin** (community plugin, `mjessome/obsidian-global-hotkeys`) — the most direct option. In its settings panel you enter a system-wide key combo and map it to any Obsidian command ID. The plugin config is stored in `.obsidian/plugins/obsidian-global-hotkeys/data.json`, which you can also track in dotfiles.
			- **[[Hammerspoon]]** (`~/.hammerspoon/init.lua`) — classic macOS dotfile. Bind a key combo to an `hs.urlevent.openURL("obsidian://...")` call or to an `hs.application.find("Obsidian"):activate()` + `hs.eventtap` sequence. Hammerspoon's Lua config is a first-class dotfile.
			- **[[Karabiner-Elements]]** (`~/.config/karabiner/karabiner.json`) — remap a key to an unused function key (e.g. `F18`), then pick that up in Hammerspoon or as an Obsidian hotkey. Config is a dotfile.
			- **[[Raycast]] / Alfred** — quicklinks using `obsidian://` URIs; Raycast dotfiles via `raycast export`.
		- ### Recommended approach for most dotfiles users
			- 1. Track `.obsidian/hotkeys.json` with your dotfiles manager — covers in-app bindings across machines.
			- 2. Install **obsidian-global-hotkeys** and track `.obsidian/plugins/obsidian-global-hotkeys/data.json` — adds system-wide reach with no extra tooling.
			- 3. If you already use [[Hammerspoon]], add `init.lua` rules instead — keeps everything in one Lua file.
		- ### Sources
			- [GitHub — obsidian-global-hotkeys (mjessome)](https://github.com/mjessome/obsidian-global-hotkeys)
			- [Obsidian Help — Hotkeys](https://help.obsidian.md/hotkeys)
			- [Obsidian Forum — Is there anyway to activate Obsidian system globally by some hotkey?](https://forum.obsidian.md/t/is-there-anyway-to-activate-obsidian-system-globallly-by-some-hotkey/47616)
			- [Hammerspoon — A Better, Better Hyper Key](https://evantravers.com/articles/2020/06/08/hammerspoon-a-better-better-hyper-key/)