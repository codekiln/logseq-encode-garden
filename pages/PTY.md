alias:: [[pseudoterminal]]
logseq-entity:: [[Logseq/Entity/Concept]]

- # PTY (pseudoterminal)
	- A kernel-provided pair of virtual file descriptors — a **controller** end (`/dev/ptmx`) and a **subordinate** end (`/dev/pts/N`) — that together emulate a hardware serial terminal.
	- The **subordinate** end looks like a real `tty` device to any process that opens it: `isatty()` returns `true`, the process can query terminal size (`TIOCGWINSZ`), and it receives and sends [[ANSI]] escape sequences normally.
	- The **controller** end is held by the terminal emulator (or any host process); it reads the subordinate's output, interprets escape codes, and writes input back.
	- ## Why it matters
		- CLI programs check `isatty()` to decide whether to emit [[ANSI]] color and paging. Attached to a PTY → color on; attached to a pipe → color off.
		- [[nvim]]'s `:terminal` command allocates a PTY, so programs inside it behave as if in a real terminal (see [[vim/split/v]] for the `:vsplit | terminal` pattern).
		- A plain `:!cmd` subprocess gets a [[Unix/Pipe]], not a PTY — `isatty()` returns `false`.
	- ## Relationship to TTY
		- A **TTY** originally referred to a physical teletype or serial terminal. Modern usage treats TTY and PTY as near-synonyms in software; PTY specifically denotes the *virtual* (kernel-emulated) variety.
	- ## See also
		- [[PTY/Q/What is a proper PTY buffer and how is it different from a non-PTY subprocess?]]
		- [The TTY demystified (Linus Åkesson)](https://www.linusakesson.net/programming/tty/)