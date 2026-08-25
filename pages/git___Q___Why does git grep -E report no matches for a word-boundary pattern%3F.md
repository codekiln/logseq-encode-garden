logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[git/Q/Why does git check-ignore report nothing for a tracked file?]], [[My/AI/Agent/Chief of Staff]]

- # Why does `git grep -E` report no matches for a word-boundary pattern?
	- ## [[AI Answer]]
		- **Short answer: `\b` carries no meaning in the pattern language `git grep -E` uses, so the whole pattern stops matching anything.** The search prints nothing and exits `1`, which is the same result it gives for a word that is genuinely absent. Use `git grep -P` with the pattern in single quotes.
		- `\b` is the regular-expression escape for a word boundary, meaning the edge between a letter and a space or a punctuation mark. It is how you ask for `cat` and skip `concatenate`.
		- ### Measured here
			- Run on [[2026-08-25 Tue]] against `pages/LazyVim___Tutorial___Work with the Terminal.md` in this graph, under git 2.55.0 with no `grep.patternType` set:
			- | Command                            | Output | Exit |
			  |------------------------------------|--------|------|
			  | `git grep -c -F 'LazyVim'`          | `5`    | `0`  |
			  | `git grep -c -E 'LazyVim'`          | `5`    | `0`  |
			  | `git grep -c -E '\bLazyVim\b'`      | none   | `1`  |
			  | `grep -c -E '\bLazyVim\b'`          | `5`    | `0`  |
			  | `git grep -c -P '\bLazyVim\b'`      | `5`    | `0`  |
			- The `git grep -c -E 'LazyVim'` row shows that `-E` reads this file correctly. The answer changes only on the rows whose pattern carries `\b`.
		- ### The pattern matches nothing at all
			- One explanation for this behavior is that git reads `\b` as the backspace character, which would make the pattern ask for a literal backspace in front of the word. The evidence goes against that.
			- Two files were searched with `git grep --no-index`. One held the text `plain LazyVim here`. The other held `lit`, then the single byte `0x08`, then `LazyVim here`. The pattern `\bLazyVim` matched neither file, and the pattern `\b` on its own also matched neither.
			- So a pattern holding `\b` matches no line of any file, whatever that line contains.
		- ### What to use instead
			- **`git grep -P '\bword\b'`** keeps the whole-word search and keeps git's own choice of which files to read. It needs a git built with PCRE2, which this machine has.
			- **`git grep -F 'word'`** searches for a fixed string. It also matches inside longer words, so `cat` finds `concatenate` too.
			- **`grep -rE '\bword\b'`** handles `\b` the usual way. It reads files from the working directory, so it also opens untracked and ignored files, and it ignores git's index.
		- ### A shell that rewrites the pattern defeats `-P` as well
			- `-P` needs `\b` to reach git as two characters, a backslash and a `b`. Several shell constructs replace it with the single byte `0x08` first, and then `-P` finds nothing either. The symptom matches the `-E` failure while the cause differs, so ruling out one leaves the other.
			- Measured on [[2026-08-25 Tue]] under zsh on this machine:
			- | Construct                            | What git receives   |
			  |--------------------------------------|---------------------|
			  | `'\bword\b'` in single quotes         | a backslash and `b` |
			  | a heredoc, delimiter quoted or not   | a backslash and `b` |
			  | `printf '\bword\b'`                   | the byte `0x08`     |
			  | `echo -e '\bword\b'`                  | the byte `0x08`     |
			  | `$'\bword\b'`                         | the byte `0x08`     |
			- On `pages/LazyVim___Tutorial___Work with the Terminal.md`, `git grep -c -P` returns `5` for the single-quoted pattern and nothing for the `0x08` form. Single-quote the pattern and it arrives whole.
		- ### Run a positive control first
			- A search that reports nothing gives no sign of whether the pattern failed or the word is absent. Search for the same word with `-F` on a path that you know holds it. A count from `-F` alongside silence from `-E` on one file points at the pattern.
		- ### A false answer costs more when several agents share a graph
			- Each seat in [[My/AI/Agent/Fleet]] searches before it writes, so a search tool that answers false shapes what gets written. On [[2026-08-25 Tue]] a whole-word search reported that no tracked file in [[My/Dotfiles]] held a term, and a fixed-string search for the same term then found 27 occurrences of it in one file.
