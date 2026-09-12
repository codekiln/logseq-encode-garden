author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Goals]], [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # A fast way to write, maintain, and publish a Logseq garden
	- I would build logseq-gardener so that a person can write in Neovim, work with coding agents, and publish a garden while keeping the existing Logseq Markdown files. A shared local engine would understand the pages, blocks, and links; each client would use that engine for the work it needs to do.
	- The everyday result should be simple: typing a link feels immediate, an agent can find the right note without repeatedly searching the whole repository, edits preserve the surrounding text, and a visitor can read a published page without downloading the garden.
	- ## Writing in Neovim
		- Opening a garden file starts `garden lsp` over standard input and output. The process loads previously indexed information, reads the open file, and checks for changes elsewhere in the background. The editor owns the process lifecycle.
		- Page completion recognizes full names, aliases, and pages that exist through references even though they have no content file. Following a link opens the content when available; for a fileless page, the editor offers the notes that refer to it.
		- Block-reference completion shows enough surrounding text to identify the intended block. Following a block reference opens its source location. Finding references shows where a page or block is used.
		- Completion uses the text currently in the editor, including unsaved changes. A half-written link should remain usable while typing. A separate command run in a terminal reads the saved garden.
	- ## Working with a coding agent
		- An agent needs the same page identities and reference information as the editor. I would expose that information through commands with readable output and a matching JSON form.
		- Proposed command examples:
			- ~~~text
			  garden page resolve "Logseq/Frontmatter" --json
			  garden page complete "Logseq/Front" --json
			  garden page backlinks "Logseq/Frontmatter" --json
			  garden block get <uuid> --json
			  garden impact --base HEAD --json
			  ~~~
		- A resolution result explains what matched: a page title, an alias, or a name used only in references. It includes source locations and any competing matches. An ambiguous alias needs a decision from the caller; a fuzzy spelling suggestion remains a suggestion.
		- Commands should accept batches of lookups so an agent can resolve the names in a draft together. Every result identifies the garden it belongs to. An explicit `--graph` selects a garden; otherwise the command finds the enclosing garden from the working directory.
		- Completion can return useful candidates while indexing continues. A command deciding whether a name already exists must finish the necessary search or report that the answer is incomplete. That distinction prevents an agent from creating a duplicate page because indexing was still underway.
	- ## One engine shared by the clients
		- ~~~text
		  Existing Markdown + graph configuration
		                      |
		                      v
		              garden-core
		       read pages and block trees
		       resolve names and references
		       retain original text and locations
		                      |
		                      v
		         reusable local index and cache
		                      |
		       +--------------+----------------+
		       |              |                |
		       v              v                v
		  garden commands  garden lsp     garden publish
		  person / agent   Neovim         static website
		  ~~~
		- garden-core owns the Logseq behavior: filename and title rules, aliases, namespaces, journals, block parents, UUIDs, properties, references, and supported queries. The command line, editor integration, and publisher call those functions.
		- I would evaluate existing parsers against both syntax examples and the resulting graph before committing to a core language. The trial must include original-text preservation, since accurate lookup alone does not establish that a parser is suitable for small, faithful edits.
		- The installed product should be a native executable with an embedded cache stored outside the garden. Markdown and graph configuration remain the saved knowledge. Removing the cache causes rebuilding.
	- ## Make speed a feature of the whole workflow
		- I would build a persistent index that short-lived commands can reuse, with a hot in-memory view for the editor. This directly serves repeated agent calls as well as interactive typing.
		- Opening the first garden file starts background work before completion is requested. The current file and likely completion candidates get priority. Background jobs pause between small batches so a large parse cannot occupy all the time needed to answer a keystroke.
		- Editing a file requires parsing its changed text and checking the references affected by the change. Removing an alias, for example, can change where links in untouched journals lead. The engine should reuse those journals' parsed text while looking up the affected targets again.
		- Each garden and worktree has its own current file list and reference index. Identical parsed content may be reused across checkouts, but uncommitted edits in one checkout must stay in that checkout's view. Unsaved editor buffers form a separate temporary view.
		- Cache entries record the content and configuration they were derived from. Startup checks saved files against that record, including untracked changes. Long-running clients watch for further edits and periodically reconcile their file list so a missed event can be recovered.
		- Measure opening a garden, repeated commands, completion during background parsing, and the delay between saving an edit and seeing affected links update. Include large pages and heavily referenced pages, alongside larger synthetic gardens. Set latency targets from those measurements and track the slow requests as well as the typical ones.
	- ## Help a person understand an edit before committing it
		- `garden impact` compares a chosen Git revision with the current saved files and reports affected links and block relationships. A person or coding agent runs it to find consequences outside the changed lines.
		- Suppose Studio declares Workshop as an alias and a journal links to Workshop. Removing the alias leaves the journal text unchanged, but its link now names a separate Workshop page. The report identifies the removed declaration, the journal's source line, and the old and new targets.
		- This calculation is ordinary program code. The person or coding agent decides whether the reported change is wanted. The command also reports uncertainty when it cannot confidently match a moved block.
		- ~~~text
		  Save an edit
		       |
		       v
		  garden impact --base HEAD
		       |
		       v
		  Inspect affected notes and source links
		       |
		       +--> Keep the result and commit
		       |
		       +--> Adjust the edit, then check again
		  ~~~
	- ## Add editing commands that preserve the files
		- Once reading and comparison are dependable, I would add page rename, block insert/update/move/delete, and property changes. Each operation produces a proposed patch and a report of affected references.
		- The edit uses original text and source ranges to preserve untouched bytes, including unfamiliar constructs. Moving a block keeps its explicit UUID attached. Renaming a page finds references according to the graph's naming rules.
		- Applying a patch checks that the source still matches the version used to prepare it. If a person or another agent has changed the file, the command reports the conflict and prepares a new preview. A stale preview should never overwrite newer work.
		- A rename that touches several files needs recovery from interruption. The operation records enough information to finish or undo its own writes, and reports partial completion if interrupted. A successful write to one file is not sufficient evidence that the whole rename succeeded.
	- ## Publish useful pages from the same garden
		- `garden publish` would produce an independently readable HTML document for each published page, with stable links, backlinks, a sitemap, and search. The build would use a standard static-site tool for layout and assets, with garden-core supplying the Logseq interpretation.
		- The exporter resolves page and block references and expands supported embeds. It evaluates a declared set of query forms and identifies unsupported features with source locations and visible output. An unsupported query should be distinguishable from a query that ran and found nothing.
		- The build records which pages include other content. Editing an included block rebuilds the pages displaying it. Adding a page may change query results, so rebuilding must account for newly matching content too.
		- Publication selection applies to query results, embedded text, backlinks, and search entries as well as the page list. Recursive embeds stop at a link to the repeated target.
	- ## Support concurrent work in deliberate steps
		- Git worktrees support independent work now. Separate graph views and source-version checks make that workflow useful while editing commands are being developed.
		- For simultaneous editing of the same block, I would add a shared editing session in which participating clients exchange operations with explicit block identities. A CRDT is a candidate for combining those operations; the experiment must cover text changes, moves, deletion, and sibling order together.
		- Direct edits from an outside editor arrive as changed files. The session must compare those files with its last saved version and either incorporate the change or identify a conflict. A CRDT only coordinates the operations it receives.
		- Any history needed to reconcile disconnected clients must be retained until those clients have caught up; it cannot be treated as disposable parsing cache. The design must distinguish that coordination history from the Markdown that records the current garden.
	- ## Deliver useful capabilities as the engine grows
		- **Read and navigate:** establish small compatibility fixtures, resolve pages and aliases through the command line, and connect that same resolver to Neovim completion. Add block navigation and backlinks. This is the first release I would want to use daily.
		- **Explain and apply edits:** ship `garden impact`, use actual garden edits to test its findings, then introduce previewable mutation commands. Preserve original text and compare every optimized update with a clean rebuild in the test corpus.
		- **Publish:** export supported references, embeds, and queries through the shared engine, then measure whether a visitor can read an individual page promptly. Publish a feature-support report alongside the build results.
		- **Edit together:** test operation-based collaboration on copies of a garden, including interrupted sessions and edits made outside the session, before using it on valuable notes.
		- The result would be a garden that remains comfortable to use from a terminal, an editor, an agent, and a website. Each addition should preserve the same names and relationships across those clients while reducing the waiting and manual repair involved in maintaining the files.
