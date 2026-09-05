logseq-entity:: [[Logseq/Entity/CLI/Command]]
see-also:: [[git]]

- # [git ls-files](https://git-scm.com/docs/git-ls-files)
	- Merges the file listing in the [[git]] index with the actual working-directory listing, and shows different combinations of the two depending on which selection flags are given.
	- **Usage:** `git ls-files [<selection flags>] [<exclude flags>] [<path>...]`
	- Without any selection flag (`-c`/`-s`/`-d`/`-o`/`-u`/`-k`/`--resolve-undo`), the default is `-c` (cached, i.e. tracked files).
	- ## Child flags in this garden
		- [[git/ls-files/--cached]] (`-c`)
		- [[git/ls-files/--ignored]] (`-i`)
		- [[git/ls-files/--exclude-standard]]
