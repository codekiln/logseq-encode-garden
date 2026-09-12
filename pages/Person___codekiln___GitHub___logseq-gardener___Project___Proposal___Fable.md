author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Goals]], [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]], [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Codex]]

- # One Logseq engine that agents, Neovim, git, and a website all call
	- I would build logseq-gardener as one library that reads a Logseq file graph the way Logseq does, and a set of thin clients that all call it: a command line that agents in this repository use in place of grep from the first week, a language server that gives Neovim completion and navigation from the same index, a graph diff that git hooks and pull requests run, an exporter that hands plain Markdown to a standard site generator, and a git merge driver that merges concurrent edits block by block. Examples use the Brief's working alias `garden`; the name is an open decision, per [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET One tool carries four names and two of them collide]].
	- ~~~text
	  pages/  journals/  assets/  logseq/config.edn
						  |
						  v
				 +------------------+
				 |   garden-core    |   parse (lsdoc or mldoc)
				 |                  |   graph model with source spans
				 |                  |   original text of every file
				 |                  |   persistent index per checkout
				 +--------+---------+
						  |
		  +--------+------+-------+-----------+
		  |        |      |       |           |
		  v        v      v       v           v
		garden   garden  garden  garden      git
		page /   lsp     diff    export      merge
		block                                driver
		  |        |      |       |           |
		agents,  Neovim  hooks,  Quartz,    concurrent
		skills           PRs     Hugo, Zola branches
	  ~~~
	- ## Decide the parser with three tests in the first week
		- Whichever parser I pick decides the language, the license, and how much of the engine I get for free, so I would run these three tests before writing any other code. Each test runs on the encode garden and on the public `logseq/docs` graph, with a tool already installed here or with one `cargo` command.
		- ~~~text
		  Syntax:      lsdoc's differential test against mldoc   -> zero unclassified mismatches
		  Graph:       Logseq's graph-parser at tag 0.10.15      -> same pages, aliases, parents, refs, UUIDs
		  Round trip:  parse then serialize every file           -> identical bytes (tine-check)
		  ~~~
		- When all three pass, garden-core is built in Rust on lsdoc and tine-core, and I would open a conversation with Tine's maintainer about a CLI and an LSP sharing tine-core. When the graph test fails, the missing parts of Logseq's `extract` code get ported and the fixture stays. When the syntax test fails on constructs this garden uses, the core is built on mldoc in OCaml, and the graph layer is a port either way. The outcome is recorded as an architectural decision record page under this project. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Pick the parser first and let the language follow]] and [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Use Logseq's own graph-parser as the oracle and require a byte-identical round trip]] hold the evidence.
	- ## Model the graph so a wrong state cannot be built
		- Page identity, block identity, and resolve results are sum types, so no code path treats a positional block as stable, reads an ambiguous name as a match, or answers from a warming index as if it were complete. Graph scope is a required argument of every core function. Every node keeps its source file and byte span, and the engine keeps the original text of every file, which is what later edits and the round-trip test depend on.
		- ~~~text
		  Page      = FileBacked(path, name) | ReferenceOnly(name)
					  with evidence: file title, title property, alias of <page>, referenced from <file:line>, namespace parent of <page>
		  BlockId   = Explicit(uuid) | Positional(page, path from root)
		  Resolve   = Resolved | Ambiguous(candidates) | NoMatch(suggestions) | Incomplete(scope)
		  ~~~
		- Graph discovery works like git's: the command walks up from the working directory to the nearest `logseq/config.edn`, and an explicit `--graph <path>` wins. The engine reads that configuration file first, because `:file/name-format` and `:journal/page-title-format` decide what the files are called.
	- ## Ship the command line that agents use in this repository
		- The first release is the set of commands that replace a grep, with `--json` on every one, `--batch` reading names from standard input, and exit codes a shell condition can test.
		- ~~~text
		  garden page resolve "Logseq/Publish" --json       what matched, the evidence, competing candidates
		  garden page exists  "Logseq/Publish"              no output; the exit code names the result
		  garden page complete "Logseq/Pub" --json          the same query the editor sends
		  garden page backlinks "Logseq/Publish" --json
		  garden block get <uuid> --json                    the block, its page, its source location
		  garden search "mldoc" --json
		  ~~~
		- The link-hygiene skill and the core rule in this repository switch to these commands as soon as they exist, so every agent session runs the engine against the real corpus and reports what it gets wrong. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Ship the agent CLI first and let the LSP inherit the index]] and [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Answer page existence with a typed result and an exit code]] carry the argument and the result type.
	- ## Keep one persistent index per checkout
		- Each checkout keeps one SQLite file under `$XDG_CACHE_HOME/<tool>/<hash of the checkout's real path>/`, holding pages, blocks, references, aliases, inclusion edges for embeds and block references, and a content hash for every source file. A command opens it, compares each file's size and modification time with the record the way `git status` does, reparses the files that changed, re-resolves the links whose targets those files could have changed, and answers. Deleting the directory costs one cold parse.
		- `garden lsp` holds the same index in memory and adds an overlay of open buffers with document versions on top, so completion sees an unsaved alias while a command in a terminal sees the saved graph. No daemon runs: the editor owns the language server's lifetime, and each command is its own process. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Agents calling the CLI justify a persistent cache on a small garden]] and [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Give each checkout its own cache and share parsed text later]] give the reasons.
	- ## Add Neovim as the second client of the same index
		- `garden lsp` speaks the Language Server Protocol over standard input and output. It completes page links from the page index and block references from the block index, goes to the definition of a page or block, lists references, and shows a block's text on hover. A page that exists only through references opens as the list of blocks that name it.
		- Its acceptance test is a recorded protocol session replayed without an editor: open, change, complete, save, and close, with an unsaved alias, an unfinished link, a Unicode character before the cursor, and a slow parse arriving after newer text.
	- ## Show what an edit changes in the graph before it is committed
		- `garden diff --base <revision>` compares the graph at that revision with the graph in the saved files and reports links whose target changed, new reference-only pages, blocks whose parent changed, moved blocks matched by UUID or reported as uncertain, and removed `id::` lines that other blocks still reference. Readable output carries file and line links, and `--json` carries the same findings.
		- It runs in this repository's lefthook pre-commit and in the link-hygiene skill, replacing the wikilink checker, and `.gitattributes` registers it as git's external diff driver for garden files so `git diff` can show graph changes on request. Its first fixtures are commits in this repository's history that removed alias lines. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Call the impact command garden diff and run it where the link checker runs]] has the details, and Codex's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Build a command that shows what an edit affects]] is where the command came from.
	- ## Publish by exporting Markdown a site generator can build
		- `garden export` writes one CommonMark file per published page with frontmatter, after resolving what only a Logseq-aware tool can: page identity and namespaces, wikilinks as relative paths, block references and page embeds expanded, the YouTube and video macros rendered, properties as frontmatter keys, and a backlinks list per page. The first version writes each query as its source text with a visible note, since the encode garden holds only a handful of them, and a report beside the build lists every page that used an unsupported construct and where.
		- A standard generator renders the folder: [[QuartzMD]] first, since it is already in this garden's prior art, with Hugo and Zola as the alternatives. Before any of that, Tine's static export runs against the encode garden for an hour and is scored with the same feature report. If it passes on embeds and block references, publishing is a workflow step. The measure of success is a visitor reading one page without downloading the garden, timed against the current site. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Publish by exporting plain Markdown to a standard site generator]] and [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0933 ET Expand embeds before evaluating queries in the publisher]] carry the counts and the reasoning.
	- ## Edit through commands that keep every untouched byte
		- After reading and the diff are dependable, the engine gains `page rename`, `block insert`, `block update`, `block move`, `block delete`, `property set`, and `property remove`. Each command prepares a patch from the original text and source spans, shows it as a dry run, records the source revision it was prepared against, refuses to write when the file has changed since, and writes atomically. Before a rename edits any of the files it touches, `garden` writes the list of planned edits to a log file. A run that is interrupted halfway reads that log when it starts again and either finishes the rename or puts the files back.
		- Every command's report is a `garden diff` between the file as it is and the file with the patch applied, so a person or an agent sees the graph consequences before agreeing to the write.
	- ## Merge concurrent edits in git before building a shared session
		- Concurrent edits in this repository arrive as branches, per [[My/AI/Rule/Dev Workflow with Git and Tmux]], so the first concurrency feature is a merge driver registered in `.gitattributes` for garden files. Git hands it base, ours, and theirs. The driver parses all three into block trees with the same matcher the diff uses, merges block by block, and leaves a textual conflict marker only inside a block both sides changed. A CRDT-backed session is the experiment after that, opened when a merge the driver cannot settle shows up in practice. [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET A Logseq-aware git merge driver before a CRDT]] has the argument.
	- ## Measure on the encode garden from the first week
		- The benchmark corpus is the encode garden and the public `logseq/docs` graph, plus small fixtures: Logseq's graph-parser test graphs, the file-graph importer's known issue classes, this repository's alias-removal commits, and a small mixed-visibility graph for publication filtering.
		- The benchmark rows:
			- cold parse time and peak memory
			- warm command time in a fresh process
			- a sequence of resolve, backlinks, and block lookups run as separate processes
			- completion latency while a large file parses in the background
			- time from saving an edit to an updated backlink
			- cache size on disk
			- the operation codekiln found slow in Looksyk and the one found slow in Tine, once each is named
		- Budgets come from those numbers and are written into this page when they exist.
	- ## Order of delivery
		- The parser decision and the fixtures, with the decision record written.
		- The command line with its per-checkout index, wired into this repository's skills so agents use it daily.
		- `garden lsp` for Neovim, from the same index, with the protocol replay test passing.
		- `garden diff` in the pre-commit hook and the link-hygiene skill, with the history fixtures passing.
		- Tine's export trial, then `garden export` and a Quartz build of the encode garden, timed against the current site.
		- The editing commands, with previews and revision checks.
		- The merge driver, then the shared-session experiment if a real merge needs it.
