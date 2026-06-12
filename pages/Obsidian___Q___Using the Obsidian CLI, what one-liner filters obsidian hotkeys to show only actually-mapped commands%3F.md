logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Obsidian/CLI]]

- # Using the [[Obsidian/CLI]], what one-liner filters `obsidian hotkeys` to show only actually-mapped commands?
	- ## [[AI Answer]]
		- [[AI/Response]]
		- **Short answer:** `obsidian hotkeys | awk -F'\t' '$2'`
		- `obsidian hotkeys` outputs tab-separated lines: command ID in column 1, key binding (if any) in column 2. Unmapped commands have an empty second field. `awk -F'\t' '$2'` prints only lines where the second field is truthy (non-empty).
		- ~~~bash
		  obsidian hotkeys | awk -F'\t' '$2'
		  ~~~
		- Example output (mapped only):
			- ~~~
			  app:go-back	⌘ ⌥ ←
			  app:go-forward	⌘ ⌥ →
			  app:open-help	F1
			  app:open-settings	⌘ ,
			  command-palette:open	⌘ P
			  ~~~
		- **Alternative using `grep`:** `obsidian hotkeys | grep -P '\t.+'` — matches lines with at least one character after the tab.
