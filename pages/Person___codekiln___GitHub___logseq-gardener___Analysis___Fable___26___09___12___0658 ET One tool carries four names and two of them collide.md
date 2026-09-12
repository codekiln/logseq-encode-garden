author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[My/Principle/Dispel Ambiguity]], [[My/Principle/Make it Obvious]], [[Logseq/Idea/Rust Rewrite]]

- # One tool carries four names and two of them collide
	- The Brief names the repository `logseq-gardener`, the executable `logseq-garden`, the working alias `garden`, and the library `garden-core`. A reader meets four names for one thing before the first command runs, which is the cost [[My/Principle/Simplify/Avoid Cognitive Load]] asks to avoid.
	- ## `garden` is already a command
		- [garden-io/garden](https://github.com/garden-io/garden) is a Kubernetes development tool whose binary is `garden`, with thousands of stars and activity this year. Anyone who has it installed gets the wrong tool, and every search for the command name lands on it.
	- ## `logseq-garden` already means the thing being tended
		- [[Logseq/Garden]] is this garden's own term for one Logseq graph. An executable with the same name makes "open the logseq-garden" ambiguous between the tool and the graph, which [[My/Principle/Dispel Ambiguity]] rules out.
	- ## `logseq-gardener` already exists with different contents
		- [codekiln/logseq-gardener](https://github.com/codekiln/logseq-gardener) is a TypeScript Nx and Lerna monorepo with a `packages/lgpm` command-line package, last pushed in January 2025 and without a README. The hub page's earlier text described it as a sketch for managing multiple garden patches with [[nx]]; today's rewrite dropped that line, so the page no longer explains what a visitor finds in the repository. Archive or rename the old repository before reusing the name, or restore one sentence of history on the hub page.
	- ## Pick one name and test it
		- Use the same word for the repository, the crate or opam package, and the binary, with `-core` reserved for the library crate if the workspace needs one.
		- Before settling, check the candidate against `which`, Homebrew, crates.io or opam, npm, and a web search, and say it aloud. [[Logseq/Idea/Rust Rewrite]] lists `lgskr` as a short form; a name with no vowels fails [[My/Principle/Make it Obvious]] because nobody can say or remember it.