logseq-entity:: [[Logseq/Entity/CLI/Flag]]
alias:: [[git/ls-files/-i]]

- # `--ignored` / `-i`
	- Flag on [[git/ls-files]].
	- Shows only files matching an ignore pattern. **Must be paired with either `-c` or `-o`**: with `-c` it narrows the tracked-file listing to only those tracked paths that also match an exclude pattern; with `-o` it narrows the untracked-file listing the same way.
	- Standard ignore rules are **not** automatically active for this flag — at least one `--exclude*` option (commonly [[git/ls-files/--exclude-standard]]) is required, or `-i` matches nothing.
