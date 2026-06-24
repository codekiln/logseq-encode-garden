logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[vim/split/v]]

- # What is a "proper PTY buffer" and how is it different from a "non-PTY subprocess"?
	- ## [[AI Answer]]
		- **Short answer:** A [[PTY]] (pseudoterminal) makes a program think it is running inside a real terminal; a non-PTY subprocess is attached to a plain pipe, so the program knows it is not in a terminal and usually disables [[ANSI]] color output.
		- ### What a [[PTY]] is
			- A PTY is a kernel-provided pair of virtual file descriptors: a **controller** end (held by the terminal emulator or host process, `/dev/ptmx`) and a **subordinate** end (exposed to the child program as its stdin/stdout/stderr, `/dev/pts/N`).
			- The subordinate side behaves exactly like a real hardware terminal device (`/dev/tty`), so the child program's `isatty()` call returns `true`.
			- Because `isatty()` is `true`, programs that auto-detect terminals — `ls --color=auto`, `glow`, `less`, most CLI tools — will emit [[ANSI]] escape sequences and enable paging, color, and cursor movement.
			- The controller end receives those escape sequences and renders them visually (e.g., [[nvim]]'s `:terminal` buffer acts as the controller).
		- ### What a non-PTY subprocess is
			- When a process is launched via `:!cmd` in vim, a shell pipe (`cmd | other`), or most `subprocess.run()` calls, its stdin/stdout are connected to anonymous **pipes**, not a PTY.
			- `isatty()` returns `false` for a pipe, so well-behaved programs strip ANSI codes, disable paging, and output plain bytes.
			- Even if the program still emits escape sequences, the parent process receives them as raw text — it does not interpret or render them unless it explicitly parses ANSI.
		- ### Why this matters for [[nvim]] `:terminal` vs `:!cmd`
			- `:vsplit | terminal glow -p %` — [[nvim]] allocates a PTY for the terminal buffer; `glow` sees `isatty() == true`, enables color and paging, and the buffer renders [[ANSI]] output correctly.
			- `:!glow %` — [[nvim]] runs glow as a non-PTY subprocess; `glow` detects no terminal, disables ANSI, and the command-line area shows plain text (or garbled escape codes if the program ignores the `isatty` check).
		- ### Sources
			- [The TTY demystified (Linus Åkesson)](https://www.linusakesson.net/programming/tty/)
			- [POSIX pseudoterminal interface — `openpty(3)`](https://man7.org/linux/man-pages/man3/openpty.3.html)
