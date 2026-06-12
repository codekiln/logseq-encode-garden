logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[Obsidian/Q/If I'm using dotfiles, can I set a global hotkey for Obsidian actions like copy file path and copy link to heading?]]

- # Does [[Obsidian]] have a global config location like [[XDG]] home for cross-vault defaults, and do vault-local settings override them?
	- ## [[My Answer]]
		- Obsidian is a hot mess when it comes to this. It's like the app was built without any knowledge of the conventions for configuration with dotfiles. The community is obviously really confused, as well.
		- Of course, I could use chezmoi for obsidian prefs, but that's a pretty weird model: I'd be iterating over vaults and doing a `chezmoi apply` of the obsidian settings to each. In addition, obsidian plugins have some subtleties here; see [A non-standard, symlink-based Obsidian architecture on macOS - Help - Obsidian Forum](https://forum.obsidian.md/t/a-non-standard-symlink-based-obsidian-architecture-on-macos/113130/4).
	- ## [[AI Answer]]
		- **Short answer:** Obsidian has both a global app-level config directory and vault-local `.obsidian/` config, but they serve different purposes — global stores app state (vault list, sync metadata), vault-local stores all user preferences. There is no defaults-inheritance hierarchy; hotkeys and other settings cannot be set globally to propagate to all vaults.
		- ### Config locations
			- **Vault-local:** `.obsidian/` in the vault root. Stores hotkeys, theme, plugin settings, and all user preferences. This is the primary config surface.
			- **Global/app-level:**
				- macOS: `~/Library/Application Support/obsidian/`
				- Linux: `~/.config/obsidian/` (respects `$XDG_CONFIG_HOME` if set — Obsidian follows the [[XDG Base Directory Specification]] on Linux)
				- Windows: `%APPDATA%\Obsidian\`
			- The global directory holds `obsidian.json` (vault registry, app-level state) and IndexedDB/Local Storage for sync metadata. It does not hold hotkeys, themes, or plugin configs.
		- ### Override hierarchy
			- There is no override hierarchy between global and vault-local config. The two locations hold entirely different data categories. Vault-local settings are not overriding global defaults — they are the only place those settings exist.
			- Obsidian is fundamentally vault-scoped: each vault has a fully independent configuration. No setting in the global app config propagates into vault configs.
		- ### Hotkeys and dotfiles at the global level
			- `hotkeys.json` is vault-local only. No global equivalent exists natively.
			- You cannot set hotkeys in a global config that apply across all vaults.
			- Workarounds for cross-vault hotkey consistency:
				- Track `.obsidian/hotkeys.json` per-vault in dotfiles ([[chezmoi]], [[GNU Stow]]) — gives version control and cross-machine sync, but each vault still gets its own copy.
				- Use hard links or symlinks between vault `.obsidian/` directories to share the same `hotkeys.json` file.
				- Community plugin **obsidian-global-hotkeys** adds OS-level (system-wide) hotkeys, stored in `.obsidian/plugins/obsidian-global-hotkeys/data.json` — vault-local, but fires even when Obsidian is not focused. Also trackable via dotfiles.
		- ### Sources
			- [How Obsidian stores data — Obsidian Help](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data)
			- [Configuration folder — Obsidian Help](https://help.obsidian.md/configuration-folder)
			- forum results
				- [Having hotkeys be global across vaults — Obsidian Forum](https://forum.obsidian.md/t/having-hotkeys-be-global-across-vaults/7084)
				- [Global Settings / Same settings across multiple vaults — Obsidian Forum](https://forum.obsidian.md/t/global-settings-same-settings-themes-and-plugins-across-multiple-vaults/41789)
				- [A non-standard, symlink-based Obsidian architecture on macOS - Help - Obsidian Forum](https://forum.obsidian.md/t/a-non-standard-symlink-based-obsidian-architecture-on-macos/113130/4)
			- [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/latest/)