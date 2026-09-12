date-created:: [[2026-09-12 Fri]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]], [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal]], [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]], [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Astra]]
- # Logseq-Gardener Ecosystem Research Brief
	- ## Executive summary
		- The research supports the central premise in the current [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]: [[Person/codekiln/GitHub/logseq-gardener]] should be a new engine-first project whose source of truth is existing [[Logseq/OG]] Markdown, with CLI/agents, Neovim/LSP, and static publishing as clients of one semantic model. That is already the direction captured in the brief and the [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]] / Codex proposals.
		- The ecosystem has changed enough in 2026 that the implementation recommendation sharpens to:
			- 1. Start a new `logseq-gardener` repository, but **do not start a new Logseq parser**.
			- 2. Prototype the core in Rust against `lsdoc`, while treating official `mldoc` plus [[Logseq/OG]]'s `graph-parser` as the compatibility oracles.
		- The strongest discovery is [martinkoutecky/lsdoc](https://github.com/martinkoutecky/lsdoc). It is now a standalone, native-Rust reimplementation of Logseq's `mldoc`, explicitly designed to be behavior-equivalent at the level needed for indexing and rendering. It exposes `parse`, `refs`, and a source-oriented `parse_outline` API with source spans; it has differential testing against `mldoc@1.5.9`, real-graph checks, fuzzing, complexity gates, and a ready-made command for comparing the two parsers on your own graph. It is AGPL-3.0 and very young—created in June 2026 and still being pushed in September 2026—but technically it is almost uncannily aligned with what `garden-core` needs.
		- At the same time, do not assume `lsdoc` compatibility proves Logseq compatibility. `mldoc` parses syntax; [[Logseq/OG]]'s `deps/graph-parser` turns that syntax into pages, block identities, page refs, properties, namespaces, aliases, journals, and the DataScript representation that users actually experience as "Logseq semantics." Its `extract.cljc`, `block.cljs`, `mldoc.cljc`, `property.cljs`, configuration code and tests are therefore at least as important as the parser itself. The official graph-validator is especially useful because it already invokes `logseq.graph-parser.cli/parse-graph`, exposes the graph's DataScript DB and full Markdown AST, and validates real Logseq concerns such as block references, queries, properties, assets and missing page targets. [^1]
		- Recommended hierarchy:
			- **Compatibility specification:** official `mldoc` + [[Logseq/OG]] `graph-parser` + graph-validator.
			- **Likely parser implementation:** `lsdoc`, assuming it passes the [[Person/codekiln/GitHub/logseq-encode-garden]] differential tests.
			- **Graph/index architectural prior art:** Tine first, [[Looksyk]] second.
			- **LSP/editor architectural prior art:** [[Markdown/Oxide]] first; Marksman and obsidian.nvim for coexistence/UX patterns.
			- **Publishing semantic prior art:** `logseq/publish-spa` for what Logseq considers publishable, plus the older `logseq/publish` for the much more relevant static-per-page architectural direction.
			- **Project strategy:** new repository, locally pin/adapt/vendor where useful; do not fork an entire application such as Tine, [[Looksyk]], [[Markdown/Oxide]], or [[Logseq/OG]].
		- The recommendation is materially stronger than earlier because Tine now describes its `crates/tine-core` as a GUI-free pure-Rust core covering parse/serialize, model, indexing, queries, references and HTML publishing; it also uses an in-memory graph cache for whole-graph reads. That makes Tine an unusually good source of implementation patterns, but a poor project shell for `logseq-gardener`, whose CLI/LSP/publisher-first product boundary is different. [^2]
		- One major decision must happen before code is copied or vendored: **licensing**. [[Logseq/OG]], `mldoc`, `lsdoc`, Tine and [[Looksyk]] are AGPL-family projects, whereas [[Markdown/Oxide]] and obsidian.nvim are Apache-2.0 and Marksman, graph-validator, and publish-spa are MIT. [^3] If `logseq-gardener` is itself intended to be AGPL, direct reuse becomes much simpler. If a permissively licensed core is required, the parser decision becomes as much a licensing decision as a technical one.
		- The first engineering task before creating substantive `garden-core` code:
			- ~~~
			  git clone https://github.com/martinkoutecky/lsdoc
			  cd lsdoc
			  node tools/graph-check.mjs \
			    /path/to/logseq-encode-garden \
			    --mode both
			  ~~~
		- That command is provided specifically for comparing `lsdoc` and real `mldoc` on an existing Logseq graph and benchmarks them as well as reporting semantic parser divergences.
		- [[Person/codekiln/GitHub/logseq-encode-garden]] is an unusually good first corpus: GitHub currently indexes approximately 4,968 Markdown files under `pages/` and 507 under `journals/`, about 5,475 Markdown page/journal files total, and code search finds `id::` in 318 Markdown files. It is therefore large enough to make caching and incremental behavior real engineering concerns rather than speculative architecture.
	- ## Repository landscape
		- Relevance abbreviations: **Core** = parser/index/semantic core; **Editor** = LSP/Neovim; **Publish** = static/publishing; **Bench** = useful corpus/performance precedent; **CLI** = humans/agents/scripts.
		- ### lsdoc (P0)
			- Priority: P0
			- URL: [martinkoutecky/lsdoc](https://github.com/martinkoutecky/lsdoc)
			- Language / license / status: Rust; AGPL-3.0. Created June 2026, pushed Sept. 1, 2026; young but unusually serious correctness/performance infrastructure.
			- What it contributes: Native-Rust Logseq Markdown/Org parser explicitly aiming at `mldoc` behavior for indexing/rendering, with source spans and differential oracle tooling.
			- Specific paths: `src/`; `AST.md`; `OUTLINE.md`; `SPEC.md`; `DECISIONS.md`; `harness/`; `bootstrap/`; `tools/graph-check.mjs`. Public APIs to inspect first: `parse`, `refs`, `parse_outline`.
			- Relevance: Core, Bench
		- ### mldoc (P0)
			- Priority: P0
			- URL: [logseq/mldoc](https://github.com/logseq/mldoc)
			- Language / license / status: OCaml + Angstrom; AGPL-3.0; official and active. [^4]
			- What it contributes: Official Logseq Markdown/Org syntax parser and therefore the strongest parser oracle. Current code contains a deliberately fast outline-only path.
			- Specific paths: `lib/export/conf.ml`; `lib/mldoc_parser.ml`; especially `lib/syntax/md_outline.ml`; `lib/syntax/heading0.ml`; `lib/syntax/paragraph.ml`; `bench/time_graph.ml`; `bench/time_parse.ml`. The outline parser is line-oriented and explicitly avoids Angstrom choice/backtracking on the Logseq hot path.
			- Relevance: Core, Bench
		- ### Logseq OG graph-parser (P0)
			- Priority: P0
			- URL: [logseq/og deps/graph-parser](https://github.com/logseq/og/tree/version/file/deps/graph-parser)
			- Language / license / status: Clojure/ClojureScript within [[Logseq/OG]]; AGPL-3.0. [[Logseq/OG]] is now the official home of the file version. [^5]
			- What it contributes: The missing layer between "parsed Markdown" and actual Logseq graph meaning. Treat as a semantic specification/oracle.
			- Specific paths: `deps/graph-parser/src/logseq/graph_parser/extract.cljc`; `block.cljs`; `mldoc.cljc`; `property.cljs`; `config.cljs`; `schema/`; `util.cljs`; `test/`.
			- Relevance: Core, CLI oracle
		- ### Tine (P0)
			- Priority: P0
			- URL: [martinkoutecky/tine](https://github.com/martinkoutecky/tine)
			- Language / license / status: Rust core + SolidJS/TypeScript UI; AGPL-3.0-only; active, usable pre-1.0 project, 302 stars when crawled. [^2]
			- What it contributes: Ground-up Logseq-compatible outliner with a pure-Rust core, graph cache, search/backlinks/query machinery, source-preserving saves, and static HTML export. Probably the richest implementation reference for the eventual `garden-core`.
			- Specific paths: `crates/tine-core/`; `docs/adr/`; particularly `docs/adr/0015-lsdoc-wire-contract.md`, `docs/adr/0005-lsdoc-separate-parser-crate.md`, `src/devtools/lsdoc-diff/`, `crates/lsdoc-block-parse.rs`, parser/oracle scripts.
			- Relevance: Core, Publish, Bench
		- ### Logseq graph-validator (P0)
			- Priority: P0
			- URL: [logseq/graph-validator](https://github.com/logseq/graph-validator)
			- Language / license / status: ClojureScript/Node; MIT; official Logseq utility. [^1]
			- What it contributes: A ready-made executable oracle for "does Logseq itself consider this graph structurally valid?" It uses graph-parser and exposes its DataScript DB/full AST to tests.
			- Specific paths: `graph_validator.mjs`; `action.cljs`; `.graph-validator/` custom-test model. Most important call: `logseq.graph-parser.cli/parse-graph`. [^1]
			- Relevance: Core oracle, CLI, Bench
		- ### Markdown Oxide (P1)
			- Priority: P1
			- URL: [Feel-ix-343/markdown-oxide](https://github.com/Feel-ix-343/markdown-oxide) — [[Markdown/Oxide]]
			- Language / license / status: Rust; Apache-2.0; large, active project with 815 commits and ~2.2k stars when crawled. [^6]
			- What it contributes: The best directly relevant Rust LSP reference: workspace/vault indexing, completion, definitions, references, rename, symbols, diagnostics, fuzzy/unindexed block completion, multi-editor support.
			- Specific paths: `src/main.rs`; `src/cli.rs`; `src/completion/`; `src/gotodef.rs`; `src/references.rs`; `src/rename.rs`; `src/symbol.rs`; `src/diagnostics.rs`; `.agents/skills/testing-neovim/SKILL.md`.
			- Relevance: Editor, Core patterns
		- ### Looksyk (P1)
			- Priority: P1
			- URL: [Looksyk on Codeberg](https://codeberg.org/sebastianrzk/looksyk) — [[Looksyk]]
			- Language / license / status: Rust backend plus frontend; AGPL; actively documented, but explicitly a hobby project. Official site advertises large-graph indexing and public benchmarks. [^7]
			- What it contributes: Independent Rust-backed, Markdown-first knowledge platform explicitly optimizing fast indexing of large graphs. Useful for index scheduling, query and performance ideas.
			- Specific paths: `backend/` first, including its Cargo benchmarks; `frontend/looksyk/`; official `migration_from_logseq/`, installation and benchmark/technical-concept docs. Development is centered around the Rust backend. [^7]
			- Relevance: Core, Bench, Publish ideas
		- ### Marksman (P1)
			- Priority: P1
			- URL: [artempyanykh/marksman](https://github.com/artempyanykh/marksman)
			- Language / license / status: F#/.NET; MIT; mature, ~3.3k stars, self-contained binaries. [^9]
			- What it contributes: Mature generic Markdown LSP already solving completion, definitions, references, rename, diagnostics and wiki-link handling. It is the thing `garden lsp` should coexist with rather than duplicate.
			- Specific paths: `Marksman/`; `LanguageServerProtocol/`; `Tests/`; `Benchmarks/`; `MarkdigPatches/`; `.marksman.toml`.
			- Relevance: Editor
		- ### obsidian.nvim (P1)
			- Priority: P1
			- URL: [obsidian-nvim/obsidian.nvim](https://github.com/obsidian-nvim/obsidian.nvim)
			- Language / license / status: Lua; Apache-2.0; actively maintained, updated Aug. 2026. [^10]
			- What it contributes: Strong Neovim-native precedent for making a Markdown dialect feel native without inventing a separate filetype; current implementation includes an in-process LSP with rename/update-links and PKM actions.
			- Specific paths: `lua/obsidian/note.lua`; `docs/LSP-Progress.md`; [LSP wiki](https://github.com/obsidian-nvim/obsidian.nvim/wiki/LSP); follow implementations of definitions, references/backlinks, rename and code actions. [^11]
			- Relevance: Editor
		- ### publish-spa (P1)
			- Priority: P1
			- URL: [logseq/publish-spa](https://github.com/logseq/publish-spa)
			- Language / license / status: ClojureScript/Node; MIT; official/current; DB-graph support is explicitly on indefinite hold. [^12]
			- What it contributes: Official current file-graph publisher. Important as a publication-semantics oracle, even though its SPA architecture is precisely what you want to escape.
			- Specific paths: `src/`; `publish_spa.mjs`; `action.yml`; `nbb.edn`; `test/`.
			- Relevance: Publish, Core oracle
		- ### old logseq/publish (P1)
			- Priority: P1
			- URL: [logseq/publish](https://github.com/logseq/publish)
			- Language / license / status: React/Next.js; historical/early-stage project. [^13]
			- What it contributes: Earlier Next.js static publisher whose stated motivation was that bundling the whole Logseq web app was slow and not SEO-friendly. Conceptually much closer to the eventual publisher.
			- Specific paths: `src/components/` — particularly LS* Logseq-specific renderers — and the JSON-to-static-render transformation path. [^13]
			- Relevance: Publish
		- ### nbb-logseq (P2)
			- Priority: P2
			- URL: [logseq/nbb-logseq](https://github.com/logseq/nbb-logseq) — [[Logseq/npm/@logseq/nbb-logseq]]
			- Language / license / status: ClojureScript/Node; official Logseq project; used by graph-validator and publish-spa. [^14]
			- What it contributes: Easiest way to script current Logseq ClojureScript/DataScript semantics from Node; useful for generating golden graph fixtures and differential checks.
			- Specific paths: `nbb.edn`; examples around graph scripting; pin graph-parser as a git dependency for oracle tooling.
			- Relevance: CLI, Core oracle
		- ### LogseqLSP (P2)
			- Priority: P2
			- URL: [WhiskeyJack96/logseqlsp](https://github.com/WhiskeyJack96/logseqlsp)
			- Language / license / status: Go; no license detected by GitHub; last code push Nov. 5, 2023, so effectively stale for this project.
			- What it contributes: Historical attempt at a Logseq-aware language server; valuable mainly for seeing which Logseq editor operations somebody thought were worth mapping into LSP.
			- Specific paths: `main.go`; `document/`; `files/`; `logseq/`; `lsp.json`.
			- Relevance: Editor, historical
		- ### logseq-go (P2)
			- Priority: P2
			- URL: [aholstenson/logseq-go](https://github.com/aholstenson/logseq-go)
			- Language / license / status: Go; explicitly early-development and warns that modification may destroy data. [^15]
			- What it contributes: Useful future mutation/API precedent: page rename/delete, reference updates, linked references, block lookup, aliases and namespaces.
			- Specific paths: Root graph model, watcher code (`watcher.go`), page/block mutation and reference-update implementations.
			- Relevance: CLI/mutation reference
		- The ordering matters. `lsdoc` / `mldoc` / `graph-parser` answer correctness questions; Tine answers many engine questions; [[Markdown/Oxide]] answers many LSP questions. [[Looksyk]] is worth studying after those rather than before them because its migration guide documents semantic differences from Logseq: tags may need conversion from `#tag` to double-bracket page links, queries use a different syntax, TODOs can be migrated to checkbox form, and nested assets are not indexed. [^16]
		- There is also an operational mismatch between [[Looksyk]] and the design constraints: its documented Docker path exposes a backend on port 11000. [^17] That does not make its indexing code uninteresting; it is simply a reason not to inherit its runtime/service boundary.
		- The current Logseq product split makes the official OG code especially valuable as a fixed compatibility target. Logseq announced on April 24, 2026 that file-based Markdown graphs moved to `logseq/og`, while the main `logseq/logseq` product became the database-graph line. [^5] This supports the framing already in the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]: [[Logseq/OG]] behavior should be a compatibility target, not an application dependency.
	- ## Public benchmark gardens
		- A practical finding from this research is that truly large, openly available, Git-backed [[Logseq/OG]] gardens are not abundant. [[Person/codekiln/GitHub/logseq-encode-garden]] is substantially more interesting as a scale benchmark than the public examples verified; the official docs graph and Pengx's garden are more valuable as correctness/publishing diversity tests.
		- ### codekiln/logseq-encode-garden
			- Repository: [codekiln/logseq-encode-garden](https://github.com/codekiln/logseq-encode-garden) — [[Person/codekiln/GitHub/logseq-encode-garden]]
			- Published site: [codekiln.github.io/logseq-encode-garden](https://codekiln.github.io/logseq-encode-garden/)
			- Verified approximate size: 4,968 `pages/*.md` + 507 `journals/*.md` ≈ 5,475 Markdown files. GitHub code search also finds `id::` in 318 Markdown files.
			- Notable features / value: Real journals, explicit UUID-bearing content, namespaces/file-name encoding, aliases/properties/references, extensive accumulated real-world material, agent-edited content and an existing publication workload. These are exactly the characteristics called out in the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]].
			- Why benchmark it: Primary performance corpus. Large enough to expose startup/index/cache problems; also exercises actual editor, agent and publishing workloads.
		- ### Official Logseq docs graph
			- Repository: [logseq/docs](https://github.com/logseq/docs)
			- Published site: [docs.logseq.com](https://docs.logseq.com/)
			- Verified approximate size: GitHub currently indexes about 210 Markdown files under `pages/`.
			- Notable features / value: First-party graph whose publishing pipeline is explicitly cited by publish-spa; naturally contains broad Logseq syntax/documentation examples. [^12]
			- Why benchmark it: Primary compatibility canary. Small enough for exhaustive comparison; official enough that parser differences deserve investigation.
		- ### pengx17/knowledge-garden
			- Repository: [pengx17/knowledge-garden](https://github.com/pengx17/knowledge-garden)
			- Published site: [pengx17.github.io/knowledge-garden](https://pengx17.github.io/knowledge-garden/)
			- Verified approximate size: About 160 Markdown page files by GitHub code search; repository tree also contains a substantial collection of Logseq-style assets including PDFs/media.
			- Notable features / value: Older real-life public Logseq garden with media/assets and an established published form.
			- Why benchmark it: Publishing regression corpus. Not a scale benchmark, but useful for avoiding an implementation accidentally tailored only to one graph.
		- Also manufacture synthetic stress gardens, because a real garden gives ecological validity but poor control. A generator should be able to produce, for example, 10k/50k/100k pages with controlled fan-out, namespace depth, explicit-UUID density, journals, heavily referenced hub pages and block-ref chains. That lets you answer whether an index has O(n) versus hidden O(n²) behavior rather than merely observing that one real graph was "fast enough." `lsdoc` itself takes this philosophy seriously: its project explicitly runs adversarial performance and stack-overflow gates in addition to correctness differentials.
		- [[Person/codekiln/GitHub/logseq-encode-garden]] should nevertheless remain the release acceptance corpus. Its current repo was pushed on September 12, 2026 and its configured homepage is the current published garden, making it a living rather than archival workload.
	- ## Fork, adapt, or build new
		- Recommendation: **new project**, selectively adapted dependencies/reference implementations.
		- ### logseq-gardener itself
			- Recommendation: **NEW PROJECT**
			- Rationale: None of the existing projects has the exact product boundary: one read-first semantic engine shared by a CLI/agents, stdio LSP and page-oriented static publisher, with Markdown authoritative and no mandatory daemon. That boundary is the core insight in the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]].
		- ### lsdoc
			- Recommendation: **ADAPT / PIN / possibly vendor a local fork**
			- Rationale: This may eliminate the highest-risk task—faithfully parsing Logseq Markdown—without forcing Tine's application architecture on you. Its public API is intentionally consumable as a Cargo dependency and provides source spans plus refs/outline APIs.
		- ### mldoc
			- Recommendation: **ADAPT AS ORACLE; fork only if Proposal C wins**
			- Rationale: It is canonical and now has a highly relevant fast `parse_outline_only` path. But making it the production core means accepting an OCaml core or an FFI/process boundary. [^4]
		- ### Logseq OG graph-parser
			- Recommendation: **ADAPT SEMANTICS/TESTS; do not make it the production engine initially**
			- Rationale: It encodes the behavior you need to reproduce, but pulling the CLJS/DataScript stack into the production core would work against the "single small native executable" goal. Its real value is as the semantic oracle. [^1]
		- ### Tine
			- Recommendation: **ADAPT heavily; do not fork the whole project**
			- Rationale: `tine-core` already addresses parsing/indexing/query/search/publishing and source preservation, but Tine is an interactive outliner application with Tauri/SolidJS, editing lifecycle and product concerns the engine does not need. [^2]
		- ### Markdown Oxide
			- Recommendation: **ADAPT architecture/tests; do not fork**
			- Rationale: Excellent LSP implementation and completion/navigation code, but its graph semantics are PKM/Obsidian-oriented rather than Logseq's page/block/UUID model. [^6]
		- ### Looksyk
			- Recommendation: **ADAPT performance/index ideas; do not fork as base**
			- Rationale: Its goals overlap strongly, but migration explicitly changes some Logseq semantics, and its service/port deployment model conflicts with the one-binary/no-server-setup requirement. [^7]
		- ### Marksman
			- Recommendation: **KEEP AS A PEER**
			- Rationale: It already handles ordinary Markdown/wikilink LSP behavior well. `garden lsp` should add Logseq semantics and either avoid or deliberately de-duplicate overlapping requests. [^9]
		- ### obsidian.nvim
			- Recommendation: **STUDY / coexist, don't fork for Logseq**
			- Rationale: Strong reference for Neovim PKM UX and in-process LSP behavior, but centered on Obsidian semantics. [^11]
		- ### LogseqLSP
			- Recommendation: **STUDY ONLY**
			- Rationale: Stale code plus no detected license is enough to rule out code reuse absent a later license clarification.
		- ### publish-spa
			- Recommendation: **USE AS PUBLISHING ORACLE, not renderer architecture**
			- Rationale: It is the official file-graph publication path and therefore tells you how Logseq constructs the publishable graph, but it still emits an SPA rather than independently crawlable pages. [^12]
		- ### old logseq/publish
			- Recommendation: **ADAPT rendering ideas**
			- Rationale: Its explicit motivation was to produce static HTML because Logseq's bundled SPA could be slow and SEO-unfriendly—the same problem identified independently. [^13]
	- ## Recommended core decision
		- Ranked implementation paths:
		- ### First choice: Proposal B
			- Rust engine-first using `lsdoc` if it survives the real corpus.
			- ~~~
			  lsdoc
			    ↓
			  Logseq semantic graph layer
			    ↓
			  incremental index + cache
			    ↓
			  CLI / LSP / publisher
			  ~~~
			- This gives Rust for the persistence/index/LSP systems work, while outsourcing the parser problem to a project whose stated purpose is precisely to provide a native-Rust, source-aware `mldoc` equivalent. Tine is evidence that this overall Rust architecture is viable for a real Logseq-compatible application; it already describes a GUI-free Rust core and cached whole-graph reads. [^2]
		- ### Second choice: Proposal C
			- An OCaml/`mldoc`-based core, if the compatibility experiment exposes important `lsdoc` gaps.
			- The case for C is stronger than "OCaml is good at parsers." Current `mldoc` actually has a dedicated Logseq indexing-like fast path: `parse_outline_only`, and `md_outline.ml` says directly that it is line-oriented and avoids the more expensive Angstrom choice/backtracking hot path while preserving Logseq-relevant outline material. That makes C a technically serious alternative, not merely a conservative fallback.
		- ### Proposal A as UI spike only
			- A Marksman + tiny blink.cmp source + simple index can prove that double-bracket wiki-link completion in [[LazyVim]] feels right. It should not become the long-term architecture because the moment agents, backlinks, block refs and the publisher need the same data, putting indexing logic inside the Neovim side becomes duplicated work. That is precisely the problem the shared semantic engine in the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]] is designed to avoid.
			- Treat A as an optional one-evening vertical slice, not as an alternative product architecture.
		- Also, consistent with the note in the [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]] proposal, do not make upstream collaboration part of the initial plan. Pin commits, create local forks or vendor code where licensing permits, learn from six months of real use, and only then decide whether any upstream relationship is strategically desirable.
	- ## Architecture comparison
		- ### Compatibility oracle
			- `mldoc` + [[Logseq/OG]] `graph-parser` + graph-validator
		- ### Shared input
			- [[Logseq/OG]] garden: `pages/` · `journals/` · `assets/` · `logseq/`
		- ### Proposal A — Minimal weekend MVP
			- small garden CLI/indexer (page names + refs)
			- small blink.cmp source for Logseq double-bracket wiki-link completion
			- Marksman as generic Markdown LSP
			- [[LazyVim]]
		- ### Proposal B — Rust engine-first (recommended)
			- `lsdoc` parser + Logseq semantic layer
			- `garden-core` (Rust): graph · incremental index · cache
			- `garden` CLI (humans · agents · scripts)
			- `garden lsp` (stdio)
			- `garden publish` (per-page static output)
			- [[LazyVim]] / Neovim
			- differential tests against the compatibility oracle
		- ### Proposal C — OCaml parser-first
			- `mldoc` / OCaml outline-only + full parser
			- semantic graph · incremental index · cache
			- `garden` CLI · `garden lsp` · publisher
			- [[LazyVim]] / Neovim
			- semantic tests against the compatibility oracle
		- The key difference is where the durable boundary lives.
		- ### Comparison dimensions
			- First double-bracket wiki-link completion
				- Proposal A: Fastest route
				- Proposal B: Slightly more setup
				- Proposal C: Slightly more setup
			- Shared CLI/agent semantics
				- Proposal A: Partial
				- Proposal B: Excellent
				- Proposal C: Excellent
			- LSP architecture
				- Proposal A: Thin custom completion first
				- Proposal B: Natural in Rust ecosystem
				- Proposal C: Good, but more integration work
			- Publisher reuse
				- Proposal A: Weak initially
				- Proposal B: Same core/index
				- Proposal C: Same core/index
			- Canonical parser fidelity
				- Proposal A: Regex/minimal initially
				- Proposal B: `lsdoc`, verified against `mldoc`
				- Proposal C: Direct `mldoc`
			- Distribution
				- Proposal A: Simple Lua + ad hoc CLI
				- Proposal B: Strong single-native-binary potential
				- Proposal C: OCaml binary/runtime/build considerations
			- Long-term indexing work
				- Proposal A: Eventually rewritten
				- Proposal B: Done in intended architecture
				- Proposal C: Done in intended architecture
			- Best use
				- Proposal A: UX experiment
				- Proposal B: Strategic default
				- Proposal C: Compatibility-driven fallback
			- Key external inspiration
				- Proposal A: Marksman/Blink
				- Proposal B: `lsdoc` + Tine + [[Markdown/Oxide]]
				- Proposal C: `mldoc` + graph-parser
		- The important detail in Proposal B is that `lsdoc` should not itself define Logseq semantic truth. It defines parsed syntax. The graph layer still needs to answer questions such as: does a referenced page exist without a backing file, which alias wins or is ambiguous, how does `title::` interact with filename identity, what is a journal's canonical page name, how does a block UUID resolve, and how does a change to an alias invalidate links elsewhere? That is exactly where the [[Logseq/OG]] graph-parser oracle becomes indispensable.
		- For the LSP, [[Markdown/Oxide]] is worth studying more closely than either LogseqLSP or obsidian.nvim at the transport/architecture level. Its Rust source cleanly separates `completion`, `gotodef`, `references`, `rename`, `symbols` and `diagnostics`, while `src/main.rs` ties those operations to a vault abstraction. Its own Neovim tests exercise vault-wide fuzzy block completion. That is almost exactly the kind of decomposition `garden lsp` needs, even though the underlying semantics differ.
		- Meanwhile, obsidian.nvim is the better reference for how overlapping Markdown and PKM behavior should feel inside Neovim: its current LSP can rename a target note and update references across a vault, and reacts to filesystem renames. [^11] That makes it useful prior art for eventually deciding which LSP methods belong to Marksman and which belong to `garden lsp`.
	- ## Benchmark and experiment plan
		- The first goal should not be "make a benchmark suite." It should be collect enough evidence to choose B versus C and establish a performance baseline that future caching work can actually improve.
		- ### Record the corpus before touching the architecture
			- On a clean checkout:
			- ~~~
			  export GRAPH="$HOME/src/logseq-encode-garden"
			  git -C "$GRAPH" rev-parse HEAD
			  git -C "$GRAPH" status --short
			  printf 'Markdown/Org files: '
			  find "$GRAPH/pages" "$GRAPH/journals" \
			    -type f \( -name '*.md' -o -name '*.org' \) \
			    -print0 | tr -cd '\0' | wc -c
			  printf 'Lines: '
			  find "$GRAPH/pages" "$GRAPH/journals" \
			    -type f \( -name '*.md' -o -name '*.org' \) \
			    -print0 | xargs -0 cat | wc -l
			  printf 'Bytes: '
			  du -sh "$GRAPH/pages" "$GRAPH/journals"
			  printf 'Files containing explicit id:: properties: '
			  rg -l '^\s*-?\s*id::\s+' \
			    "$GRAPH/pages" "$GRAPH/journals" | wc -l
			  printf 'Page-reference occurrences: '
			  rg -o '\[\[[^]]+\]\]' \
			    "$GRAPH/pages" "$GRAPH/journals" | wc -l
			  printf 'UUID-style block-reference occurrences: '
			  rg -o '\(\([0-9A-Fa-f-]{36}\)\)' \
			    "$GRAPH/pages" "$GRAPH/journals" | wc -l
			  ~~~
			- GitHub's current public index already gives a useful sanity check: about 5,475 Markdown files across `pages/` and `journals/`, with at least 318 Markdown files containing `id::`.
		- ### Run the parser shootout before building garden-core
			- The single highest-value experiment is already packaged by `lsdoc`:
			- ~~~
			  mkdir -p "$HOME/src/vendor"
			  cd "$HOME/src/vendor"
			  git clone https://github.com/martinkoutecky/lsdoc
			  cd lsdoc
			  node tools/graph-check.mjs "$GRAPH" --mode both
			  ~~~
			- That harness installs/uses real `mldoc`, compares normalized parser behavior, benchmarks the two parsers, and writes a local report. It is designed specifically for running against arbitrary Logseq graphs.
			- Run the modes separately as artifacts:
			- ~~~
			  node tools/graph-check.mjs "$GRAPH" --mode diff \
			    | tee "$HOME/tmp/encode-garden-lsdoc-diff.txt"
			  node tools/graph-check.mjs "$GRAPH" --mode bench \
			    | tee "$HOME/tmp/encode-garden-parser-bench.txt"
			  ~~~
			- The decision rule for the repository ADR:
				- Choose Rust/`lsdoc` if the Encode Garden and Logseq docs graph have zero unexplained divergences affecting the semantic projection required, and its source spans are accurate enough for future source-preserving edits. Otherwise quantify the cost of fixing `lsdoc` against the cost of making `mldoc` the production parser.
			- That distinction matters because `lsdoc`'s own differential comparison deliberately excludes spans—`mldoc` does not expose equivalent inline spans—so source-location correctness needs its own tests.
		- ### Establish Logseq semantic truth independently of parsing
			- Install/run the official validator against a clean graph:
			- ~~~
			  git clone https://github.com/logseq/graph-validator
			  cd graph-validator
			  yarn install
			  node graph_validator.mjs "$GRAPH"
			  ~~~
			- That is an officially documented local invocation; the validator parses the graph using Logseq's own graph-parser stack and tests block refs, queries, properties, page refs and other semantic relationships. [^1]
			- Then create a small oracle script using the same parse-graph entry point that dumps deterministic normalized JSON:
			- ~~~
			  {
			    "pages": [],
			    "aliases": [],
			    "namespaces": [],
			    "blocks": [],
			    "block_refs": [],
			    "page_refs": [],
			    "properties": []
			  }
			  ~~~
			- Compare that JSON against `garden-core` in CI. This is the missing test between:
				- `lsdoc` == `mldoc`
				- and
				- `garden-core` == Logseq
			- They are not equivalent.
		- ### Give garden a benchmarkable CLI contract immediately
			- Require these commands before the cache gets sophisticated:
			- ~~~
			  garden --graph "$GRAPH" index --wait
			  garden --graph "$GRAPH" status --json
			  garden --graph "$GRAPH" page complete "Logseq/Pub" --json
			  garden --graph "$GRAPH" page resolve "Logseq/Publish" --json
			  garden --graph "$GRAPH" page backlinks "Logseq/Publish" --json
			  garden --graph "$GRAPH" block get UUID --json
			  ~~~
			- `index --wait` exists primarily for tests and explicit maintenance. Interactive clients should not normally need to invoke it synchronously.
			- `status --json` should expose enough benchmark metadata to make the system observable:
			- ~~~
			  {
			    "graph": "...",
			    "cache_path": "...",
			    "state": "warming|ready",
			    "files_discovered": 5475,
			    "files_parsed": 4100,
			    "pages_known": 0,
			    "blocks_known": 0,
			    "source_revision": "...",
			    "schema_version": 1,
			    "parser_version": "..."
			  }
			  ~~~
			- That turns performance debugging into measurement rather than intuition.
		- ### Measure cold full indexing
			- Use a disposable XDG cache so nothing contaminates the graph or the normal cache:
			- ~~~
			  export BENCH_CACHE="$TMPDIR/logseq-gardener-bench-cache"
			  hyperfine \
			    --runs 5 \
			    --prepare "rm -rf '$BENCH_CACHE'" \
			    --export-json garden-cold-index.json \
			    "XDG_CACHE_HOME='$BENCH_CACHE' \
			     garden --graph '$GRAPH' index --wait"
			  ~~~
			- This measures full end-to-end cold work, including file discovery, parse, semantic graph construction and cache persistence.
			- For peak memory on macOS:
			- ~~~
			  rm -rf "$BENCH_CACHE"
			  /usr/bin/time -l \
			    env XDG_CACHE_HOME="$BENCH_CACHE" \
			    garden --graph "$GRAPH" index --wait \
			    >/tmp/garden-index.out
			  ~~~
			- On Linux:
			- ~~~
			  rm -rf "$BENCH_CACHE"
			  /usr/bin/time -v \
			    env XDG_CACHE_HOME="$BENCH_CACHE" \
			    garden --graph "$GRAPH" index --wait \
			    >/tmp/garden-index.out
			  ~~~
			- Record wall time, peak RSS and final index size separately. A fast implementation that consumes several gigabytes is not necessarily a useful Neovim/agent backend.
		- ### Measure time to first useful completion
			- This is the benchmark that most directly encodes the UX concern.
			- Cold-cache:
			- ~~~
			  hyperfine \
			    --runs 20 \
			    --prepare "rm -rf '$BENCH_CACHE'" \
			    --export-json garden-cold-completion.json \
			    "XDG_CACHE_HOME='$BENCH_CACHE' \
			     garden --graph '$GRAPH' \
			     page complete 'Logseq/Pub' --json >/dev/null"
			  ~~~
			- The important contract is that this command should return the best available candidate set without waiting for complete indexing. The engine can continue warming afterward when it is operating in the long-running LSP process.
			- This lets Proposal B implement the design described:
			- ~~~
			  graph activation
			         ↓
			  open old cache immediately
			         ↓
			  discover cheap page candidates
			         ↓
			  background semantic indexing
			         ↓
			  user types Logseq/Pub…
			         ↓
			  query current snapshot immediately
			         +
			  reprioritize related unresolved work
			  ~~~
			- The double-bracket wiki-link event does not start indexing; it only changes scheduling priority.
		- ### Measure warm process startup and query latency
			- First create a complete cache:
			- ~~~
			  rm -rf "$BENCH_CACHE"
			  XDG_CACHE_HOME="$BENCH_CACHE" \
			    garden --graph "$GRAPH" index --wait
			  ~~~
			- Then benchmark the kind of pattern an AI agent will create—many fresh CLI processes:
			- ~~~
			  hyperfine \
			    --warmup 5 \
			    --runs 100 \
			    --export-json garden-warm-complete.json \
			    "XDG_CACHE_HOME='$BENCH_CACHE' \
			     garden --graph '$GRAPH' \
			     page complete 'Logseq/Pub' --json >/dev/null"
			  ~~~
			- And several semantic operations:
			- ~~~
			  hyperfine --warmup 3 --runs 50 \
			    "XDG_CACHE_HOME='$BENCH_CACHE' \
			     garden --graph '$GRAPH' page resolve 'Logseq/Publish' --json >/dev/null" \
			    "XDG_CACHE_HOME='$BENCH_CACHE' \
			     garden --graph '$GRAPH' page backlinks 'Logseq/Publish' --json >/dev/null"
			  ~~~
			- This benchmark is important because the agent use case changes the optimization target. An LSP process can amortize everything in memory; a coding agent may issue many independent shell commands. The [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]] / Codex drafts correctly identify persistent reusable cache state as valuable even when no daemon exists.
		- ### Measure one-file incremental reindex correctly
			- Do not benchmark edits against the primary garden. Create a detached worktree:
			- ~~~
			  export BGRAPH="$TMPDIR/encode-garden-bench-worktree"
			  git -C "$GRAPH" worktree add --detach "$BGRAPH" HEAD
			  export EDIT_CACHE="$TMPDIR/logseq-gardener-edit-cache"
			  XDG_CACHE_HOME="$EDIT_CACHE" \
			    garden --graph "$BGRAPH" index --wait
			  ~~~
			- Use the known `pages/Q.md` fixture, which exists in the public corpus. Create a small preparation script that changes its content on every iteration:
			- ~~~
			  cat > "$TMPDIR/garden-prepare-edit.sh" <<'EOF'
			  #!/bin/sh
			  set -eu
			  git -C "$BGRAPH" checkout -- pages/Q.md
			  printf '\n- gardener-benchmark:: %s\n' "$(uuidgen)" \
			    >> "$BGRAPH/pages/Q.md"
			  EOF
			  chmod +x "$TMPDIR/garden-prepare-edit.sh"
			  export BGRAPH
			  hyperfine \
			    --runs 30 \
			    --prepare "$TMPDIR/garden-prepare-edit.sh" \
			    --export-json garden-single-file-reindex.json \
			    "XDG_CACHE_HOME='$EDIT_CACHE' \
			     garden --graph '$BGRAPH' index --wait"
			  ~~~
			- The important internal assertion is not just elapsed time. Instrument `garden status --json` or trace output to verify:
				- 1. 1 source file reparsed
				- 2. N semantic entities changed
				- 3. 0 unrelated source files reparsed
			- Some graph-wide re-resolution may still be needed when an alias/page identity changes, but that should reuse already-parsed facts from unaffected files rather than reparse their Markdown. That distinction is central to the incremental model in the Codex proposal.
			- A second incremental fixture should deliberately edit a widely linked page or alias, because that separates cheap file parsing from potentially expensive semantic invalidation.
		- ### Measure cache size and rebuildability
			- After full indexing:
			- ~~~
			  CACHE_PATH="$(
			     XDG_CACHE_HOME="$BENCH_CACHE" \
			     garden --graph "$GRAPH" status --json \
			     | jq -r '.cache_path'
			  )"
			  du -sh "$CACHE_PATH"
			  du -ah "$CACHE_PATH" | sort -h | tail -20
			  ~~~
			- If the final design uses SQLite and status exposes the database file:
			- ~~~
			  DB="$(
			     XDG_CACHE_HOME="$BENCH_CACHE" \
			     garden --graph "$GRAPH" status --json \
			     | jq -r '.database_path'
			  )"
			  sqlite3 "$DB" '
			    SELECT
			      (SELECT page_count FROM pragma_page_count()) *
			      (SELECT page_size FROM pragma_page_size()) AS bytes;
			  '
			  sqlite3 "$DB" 'PRAGMA journal_mode;'
			  sqlite3 "$DB" 'PRAGMA integrity_check;' 
			  ~~~
			- Finally prove the core invariant:
			- ~~~
			  rm -rf "$BENCH_CACHE"
			  XDG_CACHE_HOME="$BENCH_CACHE" \
			    garden --graph "$GRAPH" index --wait
			  ~~~
			- The rebuilt semantic output should be deterministic. No semantic fact should be unrecoverable after deleting the cache. That is the source-of-truth principle in the [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]].
		- ### Benchmark result set to commit
			- `lsdoc` vs `mldoc` parser differential — mismatch classes + parser times
			- Cold complete index — wall / CPU / peak RSS
			- Cold time-to-first-completion — p50 / p95 / max
			- Warm `garden page complete` fresh process — p50 / p95
			- Warm resolve/backlinks fresh process — p50 / p95
			- Single ordinary file edit — reindex latency + files reparsed
			- Widely linked/alias edit — semantic reconciliation latency
			- LSP open→completion eventually — p50 / p95, including buffer overlay
			- Persistent cache — bytes total and bytes/source-MB
			- Delete/rebuild determinism — semantic snapshot equality
			- Publisher full build later — build time / output bytes
			- Publisher incremental edit later — affected-page count / build latency
		- Do not set hard latency targets until this table has real baseline numbers.
	- ## Licensing and compatibility constraints
		- The licensing issue deserves a place in Phase 0, because it can change the implementation language and dependency strategy.
		- AGPL-3.0 or AGPL-family projects: [[Logseq/OG]], `mldoc`, current Logseq, `lsdoc`, Tine and [[Looksyk]]. [[Logseq/OG]] and `mldoc` identify themselves as AGPL-3.0; `lsdoc` explicitly tells consumers that its Cargo git dependency is AGPL-3.0; Tine explicitly uses AGPL-3.0-only; [[Looksyk]] advertises itself as AGPL. [^3] [^2]
		- Permissive projects: [[Markdown/Oxide]] is Apache-2.0, obsidian.nvim is Apache-2.0, Marksman is MIT, and Logseq graph-validator and publish-spa are MIT. [^6]
		- LogseqLSP: GitHub currently detects no license in the repository metadata. Treat it as read-only prior art unless/until the licensing status is clarified; public source code without a usable license is not the same as reusable open-source code.
		- This creates an important design branch:
			- Are you comfortable with `logseq-gardener` being AGPL?
				- yes → direct `lsdoc`/Tine reuse is much simpler → Rust + `lsdoc` is attractive
				- no / unsure → freeze imports; use AGPL projects as behavioral oracles → clean-room/permissive implementation or licensing review
		- That diagram is intentionally conservative rather than legal advice. In particular, putting AGPL software behind a process boundary is not something to assume automatically resolves derivative-work or distribution obligations. If maintaining a permissive license is important, get specific licensing advice before importing or linking AGPL implementation code.
		- There is also a semantic compatibility issue independent of licensing: don't conflate Logseq DB's current API/data model with [[Logseq/OG]] semantics. Logseq's 2026 product split explicitly separates the Markdown/file product from the database graph product. [^5] The new ChatGPT plugin, for example, is explicitly for Logseq DB graphs and tells agent clients not to use legacy file-graph conventions such as `property:: value`. [^23] That project may eventually offer useful ideas for a typed agent API, but it should not define `garden-core`'s model.
		- Similarly, [[Looksyk]]'s Logseq migration instructions show why "can import a Logseq graph" is weaker than "implements Logseq semantics." Its optional migration steps alter tags, queries and TODO representation. [^16] Tine makes the stronger claim that it directly reads and writes the same Logseq graph layout and can switch between the two applications on the same files, which is much closer to `logseq-gardener`'s compatibility requirement. [^2]
		- Finally, keep source preservation independent of parsing correctness. `lsdoc`'s AST includes source spans, and Tine explicitly tests parse/serialize round trips and format-preserving behavior, but `lsdoc`'s `mldoc` differential intentionally normalizes away spans because `mldoc` cannot supply equivalent inline positions. [^2] Future mutation safety therefore needs three different compatibility axes:
			- syntax equivalence — `mldoc` ↔ `lsdoc`
			- graph equivalence — Logseq graph-parser ↔ `garden-core`
			- source preservation — original bytes ↔ garden mutation/serialization
		- That three-way separation in the [[Person/codekiln/GitHub/logseq-gardener/Project/Proposal/Fable]] / Codex proposals is correct and should survive into the repository architecture.
	- ## Recommended repository starting point
		- After this survey, create `logseq-gardener` as a new monorepo with approximately this first structure:
			- ~~~
			  logseq-gardener/
			  ├── crates/
			  │   ├── garden-core/
			  │   │   ├── source / parser boundary
			  │   │   ├── semantic graph
			  │   │   ├── resolution
			  │   │   ├── incremental invalidation
			  │   │   └── cache
			  │   ├── garden-cli/
			  │   ├── garden-lsp/
			  │   └── garden-publish/          # later
			  ├── integrations/
			  │   └── nvim/                    # deliberately thin
			  ├── compatibility/
			  │   ├── fixtures/
			  │   ├── mldoc/
			  │   ├── graph-parser/
			  │   └── expected/
			  ├── benchmarks/
			  │   ├── scripts/
			  │   ├── results/
			  │   └── synthetic/
			  ├── docs/
			  │   ├── adr/
			  │   ├── architecture.md
			  │   ├── compatibility.md
			  │   └── benchmark-methodology.md
			  └── vendor/                      # only after license decision
			  ~~~
		- The first ADR should be "Parser and project-license strategy." Do not vendor anything beforehand.
		- The first implementation milestone should expose only:
			- ~~~
			  garden status
			  garden page list
			  garden page resolve
			  garden page complete
			  ~~~
		- with deterministic `--json`, explicit `--graph`, read-only operation, and enough instrumentation to measure cache/index state. That matches the CLI-first agent strategy in both proposed plans without prematurely committing to publisher, mutations, merge drivers or CRDTs.
		- The first editor milestone should then be almost boring:
			- ~~~
			  LazyVim
			     │
			     ├── Marksman ───────── generic Markdown
			     │
			     └── garden lsp ─────── Logseq semantics
			                                │
			                                ▼
			                           same garden-core
			  ~~~
		- Marksman remains a mature generic Markdown service with wiki-link completion/navigation, while `garden lsp` earns its existence by understanding Logseq concepts Marksman does not: canonical page identity, fileless referenced pages, aliases/namespaces, journals, explicit block UUIDs, `((block-ref))`, Logseq properties, embeds and eventually queries. [^9]
		- And the publisher should not initially become another web framework. The most interesting lesson from Logseq's own older publish project is architectural: resolve Logseq semantics once, then generate ordinary static material. That project itself was created because shipping the full Logseq application was heavy, client-rendered and not SEO-friendly. [^13] The current plan of a semantic exporter feeding per-page static output is therefore not only adjacent to the editor/agent project; it is one of the strongest validations that `garden-core` is the correct center.
	- ## Project thesis
		- **`logseq-gardener` is not a Neovim plugin, not a Logseq clone, and not a static-site generator. It is a high-performance, source-preserving semantic implementation of [[Logseq/OG]] file graphs, with stable query and eventually mutation APIs that editors, humans, AI agents, Git tooling, and publishers can share.**
		- That is substantially more defensible after surveying the current ecosystem than trying to fork any single existing application.
	- ## Footnotes
		- [^1]: https://github.com/logseq/graph-validator?utm_source=chatgpt.com
		- [^2]: https://github.com/martinkoutecky/tine?utm_source=chatgpt.com
		- [^3]: https://github.com/logseq/og?utm_source=chatgpt.com
		- [^4]: https://github.com/logseq/mldoc?utm_source=chatgpt.com
		- [^5]: https://logseq.io/page/b2ad9ce1-9cb7-4436-8083-54cb4516d324/df4dc09d-0a12-4c87-904e-22a9bf4c350a?utm_source=chatgpt.com
		- [^6]: https://github.com/Feel-ix-343/markdown-oxide?utm_source=chatgpt.com
		- [^7]: https://sebastianrzk.codeberg.page/looksyk/?utm_source=chatgpt.com
		- [^9]: https://github.com/artempyanykh/marksman?utm_source=chatgpt.com
		- [^10]: https://github.com/obsidian-nvim?utm_source=chatgpt.com
		- [^11]: https://github.com/obsidian-nvim/obsidian.nvim/wiki/LSP?utm_source=chatgpt.com
		- [^12]: https://github.com/logseq/publish-spa?utm_source=chatgpt.com
		- [^13]: https://github.com/logseq/publish?utm_source=chatgpt.com
		- [^14]: https://github.com/logseq/nbb-logseq?utm_source=chatgpt.com
		- [^15]: https://github.com/aholstenson/logseq-go?utm_source=chatgpt.com
		- [^16]: https://sebastianrzk.codeberg.page/looksyk/migration_from_logseq/?utm_source=chatgpt.com
		- [^17]: https://sebastianrzk.codeberg.page/looksyk/installation/?utm_source=chatgpt.com
		- [^23]: https://github.com/logseq/chatgpt-logseq-plugin?utm_source=chatgpt.com
