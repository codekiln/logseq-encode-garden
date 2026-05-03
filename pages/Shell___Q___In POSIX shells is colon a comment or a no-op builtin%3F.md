---
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Shell/Builtin/type]]
via:: [[2026-05-01 Fri]]
---
- # In POSIX shells, is `:` a comment or a no-op builtin?
	- ## Answer
		- [[AI/Response]]
			- `:` is a **special builtin** (POSIX utility name `:`) that **always succeeds and does nothing** with the arguments it is given—it is **not** a comment token. A line like the following still **executes**; the words after `:` are **operands** to that no-op command, not comment text to the parser:
			  ~~~sh
			  : this is ignored
			  ~~~
			- People sometimes use that pattern as a **pseudo-comment** because the command has no side effects when the operands are simple words (avoid redirections, command substitutions, or other expansions you did not intend to run).
			- The same idea applies across common `/bin/sh` implementations and user shells such as [[Bash]] and [[zsh]], and to lean `sh` clones like **dash**—all treat `:` as this no-op builtin.
			- **Actual comments** in these languages still start with `#` (to end of line, per shell grammar).
			- **Reading other people’s scripts:** lines beginning with `:` are a weak signal you are in a **POSIX-style shell** script and the author chose a no-op command instead of `#` (sometimes to keep a line syntactically valid where a `#` line would not parse the way they want).
			- [POSIX.1-2024, Shell Command Language — special built-in utilities (includes `:`)](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html#tag_19_15)
