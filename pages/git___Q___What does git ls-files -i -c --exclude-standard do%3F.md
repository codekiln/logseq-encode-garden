logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[git/Q/Why does git check-ignore report nothing for a tracked file?]]

- # What does `git ls-files -i -c --exclude-standard` do?
	- ## [[AI Answer]]
		- **Short answer: it lists every tracked file that is also matched by a `.gitignore` (or other standard exclude) rule** — files git is tracking despite an ignore rule saying they should be excluded, typically added earlier with `git add -f`.
		- Step by step, from the [git-ls-files manual](https://git-scm.com/docs/git-ls-files):
			- [[git/ls-files/--cached]] (`-c`) selects the **tracked** files — everything currently in the index.
			- [[git/ls-files/--ignored]] (`-i`) then narrows that selection to only the entries which **also** match an exclude pattern. Per the flag's own doc, `-i` "must be used with either an explicit `-c` or `-o`" and does nothing on its own — it needs a base selection to filter.
			- [[git/ls-files/--exclude-standard]] supplies the exclude patterns to filter against: `.git/info/exclude`, every `.gitignore` in the tree, and the user's global excludes file. Without some `--exclude*` option, `-i` has no patterns to test against and matches nothing.
		- ### Measured in this repository
			- `.gitignore` line 36 has `**/CLAUDE.md`, yet two `CLAUDE.md` files are tracked (force-added on purpose so each directory carries agent instructions):
			- | Command | Output |
			  |---|---|
			  | `git ls-files -i -c --exclude-standard` | `journals/CLAUDE.md`<br>`pages/CLAUDE.md` |
			- Both paths are tracked (`-c`) **and** match the `**/CLAUDE.md` pattern (`-i` + `--exclude-standard`), which is exactly the intersection the three flags together select.
		- **Why this combination is useful:** plain `git status` and `git ls-files` (no flags) don't surface tracked-but-ignored files at all, since ignore rules only ever apply to *untracked* paths by default. This three-flag form is the standard way to audit "which committed files does my `.gitignore` think shouldn't be here?"
