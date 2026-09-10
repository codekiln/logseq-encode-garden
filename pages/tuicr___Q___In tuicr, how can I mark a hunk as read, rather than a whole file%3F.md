logseq-entity:: [[Logseq/Entity/Question]]

- # In [[tuicr]], how can I mark a hunk as read, rather than a whole file?
	- ## [[AI Answer]]
		- **Short answer:** press `R` with the cursor on that hunk to toggle it reviewed on its own, instead of `r`, which toggles the whole file.
		- `r` marks/unmarks the **entire focused file** as reviewed; `R` marks/unmarks just the **hunk under the cursor** ([Review actions](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md)).
		- A file whose hunks are individually marked reviewed is tracked separately from a file marked reviewed as a whole — the file-level `reviewed/total` count in the tree title reflects file-level state, not per-hunk state.
		- Use `[` / `]` to jump between hunks before pressing `R` on each one you've finished with.
		- Source: [KEYBINDINGS.md on GitHub](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md) ("Hiding reviewed files" section and Review actions table), local clone `github.com/agavra/tuicr`.
