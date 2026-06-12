- # [[awk]] `-F` — field separator flag
	- `-F` sets the **field separator** (`FS`) used to split each input line into fields.
	- ## Syntax
		- ~~~bash
		  awk -F'<sep>' '{ ... }' file
		  ~~~
		- `<sep>` can be a literal character or an ERE (extended regular expression).
	- ## How it works
		- Without `-F`, `awk` splits on runs of whitespace (spaces and tabs, collapsing consecutive ones).
		- With `-F`, each line is split on the given separator; fields are referenced as `$1`, `$2`, ... `$NF`.
		- The field separator is also available as the built-in variable `FS`; `-F'\t'` is equivalent to `BEGIN { FS = "\t" }`.
	- ## Common examples
		- Tab-separated input:
			- ~~~bash
			  awk -F'\t' '{ print $1 }' file.tsv
			  ~~~
		- Colon-separated (`/etc/passwd`):
			- ~~~bash
			  awk -F':' '{ print $1 }' /etc/passwd
			  ~~~
		- Comma-separated:
			- ~~~bash
			  awk -F',' '{ print $2 }' file.csv
			  ~~~
	- ## Example: filter only mapped Obsidian hotkeys
		- [[Obsidian/Q/Using the Obsidian CLI, what one-liner filters obsidian hotkeys to show only actually-mapped commands?]]
		- `obsidian hotkeys` outputs tab-separated lines — command ID in `$1`, key binding in `$2` (empty if unmapped). `-F'\t'` splits on tab; `$2` as a condition passes only lines where the second field is non-empty:
			- ~~~bash
			  obsidian hotkeys | awk -F'\t' '$2'
			  ~~~
