created-by:: [[Person/Jeff Dickey]]
readwise-link:: https://read.readwise.io/search/read/01kqqp7v0s6rn2ckz53w5xvyw9
date-created:: [[2018/10/09]]
logseq-entity:: [[Logseq/Entity/Article]]

- # [12 Factor CLI Apps](https://jdxcode.medium.com/12-factor-cli-apps-dd3c227a0e46)
	- Author: **[[Person/Jeff Dickey]]** - Source: [Medium](https://medium.com/)
	- ## Summary
		- Jeff Dickey adapts the [[12factor/app]] framing to CLI design, arguing that command-line products need their own UX discipline because they are scriptable, composable, and often used in contexts where web-style guidance is absent.
		- The article is also an early statement of the design philosophy behind [[oclif]]: strong help, predictable flags, useful diagnostics, TTY-aware presentation, structured output, fast startup, extensibility, and platform-native file locations.
	- ## Notes
		- Great help is the first product surface: commands should expose consistent `--help` behavior, useful examples, web-indexable docs, and shell completion.
		- Prefer flags when multiple values have different meanings; positional args are clearest only when the argument role is obvious.
		- Version output should be easy to discover and useful for debugging, including extra diagnostic context where helpful.
		- Treat stdout as machine-consumable output and stderr as user-facing messaging so warnings, progress, and errors do not corrupt redirected data.
		- Error messages should name what happened, explain how to fix it, and point to more detail when needed.
		- Rich terminal UI is useful only when the stream is interactive; colors, spinners, and progress bars need non-TTY and no-color fallbacks.
		- Prompts can improve ergonomics, but every prompt needs a noninteractive override for scripts and automation.
		- Tables should stay parseable: no borders, one entry per row, selectable columns, headers that can be disabled, sorting/filtering, and CSV/JSON output modes.
		- CLI startup time is part of UX, especially for scripting; defer loading work until the invoked command needs it.
		- Open source, contribution docs, licenses, conduct guidelines, and plugin systems make a CLI easier to diagnose and extend.
		- Multi-command CLIs need clear subcommand structure; the article favors colon-delimited topic commands in the Heroku style.
		- Follow XDG-style locations for config and data, with platform-appropriate cache paths.
