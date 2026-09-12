author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Resolve pages through evidence from the whole graph]], [[My/Principle/Make Illegal States Unrepresentable]], [[My/Principle/Dispel Ambiguity]]

- # Answer page existence with a typed result and an exit code
	- Codex's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Resolve pages through evidence from the whole graph]] is right, and it corrects my [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Ship the agent CLI first and let the LSP inherit the index]]: a page-existence command that reads only `pages/` would say that [[CLI]] does not exist, while the Goals page links it. In a Logseq file graph a name exists when a file carries it, when a `title::` property declares it, when another page declares it as an `alias::`, when any block links or tags it, or when it is an ancestor inside a namespaced name. Logseq's `extract` code in [extract.cljc](https://github.com/logseq/logseq/blob/master/deps/graph-parser/src/logseq/graph_parser/extract.cljc) builds pages from all of those sources at once, and the tool should too.
	- ## Make the answer a type
		- The resolver returns one of a fixed set of results, so a caller cannot read an ambiguous or provisional answer as a plain match. [[My/Principle/Make Illegal States Unrepresentable]] is the reason, and [[My/Principle/Dispel Ambiguity]] is what the caller gets from it.
		- ~~~text
		  Resolved   { name, file (optional), evidence: [ FileTitle | TitleProperty | AliasOf <page> | ReferencedFrom <file:line> | NamespaceParentOf <page> ] }
		  Ambiguous  { candidates: [ <page> with its evidence ] }
		  NoMatch    { suggestions: [ <page> ] }
		  Incomplete { scope still indexing }
		  ~~~
		- A fuzzy suggestion lives only inside NoMatch, so punctuation normalization can never silently resolve a misspelling to a different page. Every alias claimant stays in the evidence list, so a name that two pages both declare as an alias comes back Ambiguous with both of them.
	- ## Give the shell the same answer as an exit code
		- Agents in this repository call the link checker from shell conditions, so `garden page exists <name>` prints nothing and exits with a code that names the result, while `garden page resolve <name> --json` prints the evidence. Both run the same function.
		- ~~~text
		  0  Resolved
		  1  NoMatch
		  2  Ambiguous
		  3  Incomplete
		  ~~~
		- `--batch` reads names from standard input and prints one JSON line per name, which is what the link-hygiene skill needs when it checks every wikilink in a draft.
	- ## Configuration decides identity, so the resolver reads it first
		- This garden's `logseq/config.edn` sets `:file/name-format :triple-lowbar` and `:journal/page-title-format "yyyy-MM-dd EEE"`. The name format turns `Person___codekiln.md` into `Person/codekiln`, and the title format turns `journals/2026_09_12.md` into `2026-09-12 Sat`. Change either setting and the same files name different pages, so the resolver loads the configuration before it names anything, and the cache key includes it.
	- ## What this replaces in the repository
		- The link checker in `.rulesync/skills/logseq-link-hygiene/scripts/resolve-wikilinks.cljs` builds its index from files and reports a reference-only page as unresolved. Once `garden page resolve --batch` exists, that skill calls it and drops its own index. Whether a new spelling deserves a warning stays a rule of this garden, written on its rule pages: the resolver reports what exists, and the skill decides what to say about it.
