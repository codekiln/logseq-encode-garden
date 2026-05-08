tags:: [[npm/lib]]
alias:: [[nbb-logseq]], [[NBB-Logseq]], [[logseq/nbb-logseq]], [[@logseq/nbb-logseq]]
created-by:: [[Logseq]]
source-link:: https://github.com/logseq/nbb-logseq
logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [logseq/nbb-logseq: nbb with features enabled for logseq](https://github.com/logseq/nbb-logseq)
	- Software project by [[Logseq]] that packages [nbb](https://github.com/babashka/nbb) with Logseq-oriented features for ClojureScript scripting on Node.js.
	- ## What it is
		- `nbb-logseq` provides a script runtime for querying and validating Logseq graphs from command-line scripts.
		- It is a custom version of [nbb](https://github.com/babashka/nbb) that bundles Logseq-useful libraries, including [[Datascript]] and datascript-transit support.
		- It is useful for graph validation, export, query automation, and agent-side checks that need more structure than ad hoc text search.
	- ## Usage
		- Install the CLI globally through [[mise]]:
			- `mise use -g npm:@logseq/nbb-logseq@latest`
		- Run scripts with:
			- `nbb-logseq path/to/script.cljs`
		- The database-version branch is separate from the npm release path while Logseq DB graph support stabilizes.
	- ## In this garden
		- First used on [[2026/05/04]] while creating `logseq-link-hygiene`, a Rulesync skill that checks newly added Logseq wikilinks against existing pages and aliases before agents leave behind accidental stub links.
	- ## Links
		- GitHub: [logseq/nbb-logseq](https://github.com/logseq/nbb-logseq)
		- npm: [@logseq/nbb-logseq](https://www.npmjs.com/package/@logseq/nbb-logseq)
