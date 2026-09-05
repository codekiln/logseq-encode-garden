logseq-entity:: [[Logseq/Entity/CLI/Flag]]

- # `--exclude-standard`
	- Flag on [[git/ls-files]].
	- Adds git's standard exclusion sources to the match: `.git/info/exclude`, the `.gitignore` file in each directory, and the user's global exclusion file (`core.excludesFile`).
	- This is what makes [[git/ls-files/--ignored]] evaluate against normal `.gitignore` behavior instead of matching nothing.
