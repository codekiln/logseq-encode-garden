logseq-entity:: [[Logseq/Entity/question]]

- # When using [[bat]] as a pager, is there a keyboard shortcut that brings up the keyboard shortcuts?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Press `h` (or `H`) — this is the `less` help key, since [[bat]] delegates paging to `less` by default.
			- [[bat]] has no built-in interactive keyboard layer; all navigation belongs to the configured pager. The default pager is `less`, launched with flags like `-R` (preserve ANSI color), `-F` (exit if output fits on one screen), and `-K` (quit on Ctrl-C).
			- In `less`, `h` opens the built-in help screen listing every available command and key binding. From the less manual: *"h or H Help: display a summary of these commands. If you forget all the other commands, remember this one."*
			- **To use a different pager:** set `BAT_PAGER` or `PAGER` (e.g. `export BAT_PAGER="less -R"`). The help key then depends on whatever pager you configure.
			- Refs: [bat README — Using a different pager](https://github.com/sharkdp/bat#using-a-different-pager), [less man page](https://www.man7.org/linux/man-pages/man1/less.1.html)
