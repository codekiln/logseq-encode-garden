- [[Keyshort]] [[vim]] [[vim/Keyshort]]
	- **Find `old` and Replace with `new` in the Current Document** #card
	  card-last-score:: 5
	  card-repeats:: 4
	  card-next-schedule:: 2026-07-19T15:22:36.049Z
	  card-last-interval:: 25.4
	  card-ease-factor:: 2.52
	  card-last-reviewed:: 2026-06-24T06:22:36.049Z
		- Shortcut:
			- `:%s/old/new/g` replaces all matches in the current file
			- `:%s/old/new/gc` prompts for confirmation on each match
		- Description: Uses Vim substitution across the entire current buffer (`%`) to do find-and-replace in one command.