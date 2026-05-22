- [[Keyshort]] [[vim]] [[vim/Keyshort]]
	- **Find `old` and Replace with `new` in the Current Document** #card
	  card-last-score:: 5
	  card-repeats:: 3
	  card-next-schedule:: 2026-06-01T00:27:35.265Z
	  card-last-interval:: 9.68
	  card-ease-factor:: 2.42
	  card-last-reviewed:: 2026-05-22T08:27:35.265Z
		- Shortcut:
			- `:%s/old/new/g` replaces all matches in the current file
			- `:%s/old/new/gc` prompts for confirmation on each match
		- Description: Uses Vim substitution across the entire current buffer (`%`) to do find-and-replace in one command.