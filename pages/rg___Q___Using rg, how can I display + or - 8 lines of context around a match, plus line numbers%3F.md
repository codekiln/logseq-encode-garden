logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[rg]], [[rg/manpage]]
via:: [[2026-05-20 Wed]]

- # Using [[rg]], how can I display + or - 8 lines of context around a match, plus line numbers?
	- ## Answer
		- [[AI/Response]]
			- **Symmetric context (8 lines before and after each match):** use `-C 8` or `--context=8`, e.g. `rg -n -C8 PATTERN path/`. `-C` is shorthand for the same line count with `-B` and `-A` together.
			- **Asymmetric context (+8 after only / −8 before only):** use `-A 8` (`--after-context=8`) for lines after the match, or `-B 8` (`--before-context=8`) for lines before. You can combine them independently, e.g. `rg -n -B3 -A8 PATTERN` (3 before, 8 after). Order matters when mixing with `-C`: later flags partially override earlier ones (see `rg --help` under `-C`).
			- **Line numbers:** add `-n` or `--line-number` on the same command. Example with all three ideas: `rg -n -C8 foo .`
			- **TTY note:** [[rg]] may omit line numbers (and color) when stdout is not a terminal; use `-n` explicitly when piping or redirecting output.
			- [ripgrep user guide — printing context](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md#printing-context)
