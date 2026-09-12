# logseq-gardener  — Project Brief
- ## Working definition
  
  logseq-gardener is a fast, local-first semantic engine for existing **Logseq OG/file-based knowledge gardens**.
  
  Its source of truth is the user's existing Markdown files:
  
  ```
  pages/
  journals/
  assets/
  logseq/
  ```
  
  It should understand those files as a Logseq knowledge graph without requiring the user to migrate them into another canonical database format.
  
  The project exists partly as an **exit strategy from the Logseq application** as Logseq shifts active development toward its database-backed product while the older Git-friendly file format enters maintenance mode.
  
  The goal is not initially to reproduce the Logseq application.
  
  The goal is to make the **data model that made Logseq valuable independently usable**.
  
  At a high level:
  
  ```
  Logseq Markdown
                    pages/ journals/ assets/
                              │
                              ▼
                    ┌──────────────────┐
                    │   garden-core    │
                    │                  │
                    │ parser           │
                    │ graph model      │
                    │ incremental idx  │
                    │ derived cache    │
                    └────────┬─────────┘
                             │
                  one stable semantic API
                             │
        ┌────────────────────┼─────────────────────┐
        │                    │                     │
        ▼                    ▼                     ▼
      CLI                  LSP                Publisher
        │                    │                     │
  humans / agents       Neovim/LazyVim          static HTML
  scripts / tools       completion/gd/gr        SEO/search
  ```
  
  The core principle is:
  
  > 
  
  Parse Logseq once, model it once, index it once, and allow many tools to consume the same understanding.
  
  ---
- # Project name and components
  
  Working repository name:
  
  ```
  logseq-gardener
  ```
  
  Conceptual components:
  
  ```
  logseq-gardener/
    garden-core
    garden-cli
    garden-lsp
    garden-publish
    integrations/
        nvim/
    benchmarks/
    compatibility/
    docs/
  ```
  
  This is a conceptual layout rather than a prescribed language-specific directory structure.
  
  garden-core is the important component. Everything else should be relatively thin.
  
  The public executable should tentatively be called:
  
  ```
  logseq-garden
  ```
  
  Examples in this document use the shorter working alias:
  
  ```
  garden
  ```
  
  because it is easier to read and type.
  
  ---
- # Motivation
  
  The project's author has several large, long-lived Logseq knowledge gardens, collectively containing well over a million lines of Markdown.
  
  These gardens are:
- stored in Git;
- edited by humans;
- edited increasingly often by AI coding agents;
- sometimes opened in Logseq;
- sometimes manipulated directly as Markdown;
- candidates for editing primarily from LazyVim/Neovim;
- candidates for publication as fast, indexable knowledge-garden websites.
  
  The current Logseq application provides valuable semantic behavior around these files, but the underlying Markdown corpus should not depend indefinitely on Logseq itself for navigation, reference resolution, querying, editing, or publication.
  
  The project should therefore treat **Logseq OG Markdown as an independent durable knowledge format**.
  
  ---
- # Core model
  
  The conceptual beauty of Logseq is its tree/forest-oriented data model.
  
  A garden consists of a forest of nodes.
  
  The most important node types are:
  
  ```
  Page
  Block
  ```
  
  A block contains:
  
  ```
  content
  properties
  children
  references
  source location
  optional stable identity / UUID
  ```
  
  A page can usefully be exposed through much of the same node interface:
  
  ```
  page
  ├── properties/frontmatter
  └── top-level blocks
    ├── child block
    ├── child block
    └── ...
  ```
  
  The internal model may therefore share a general Node abstraction between pages and blocks.
  
  However, the implementation must **not erase meaningful differences between page identity and block identity merely for conceptual elegance**.
  
  For example:
  
  ```
  Page
    canonical Logseq page name
    source file
    aliases
    namespace relationships
    page properties
    top-level children
  
  Block
    content
    position in parent
    properties
    optional explicit UUID
    descendants
  ```
  
  A useful semantic model will likely eventually include concepts such as:
  
  ```
  Graph
  Page
  Block
  Property
  PageRef
  BlockRef
  Tag
  Alias
  Embed
  Task
  Query
  SourceLocation
  ```
  
  Every derived semantic entity should retain enough source provenance to identify the Markdown from which it came.
  
  ---
- # Source-of-truth rule
  
  Markdown files are authoritative.
  
  The cache is not.
  
  ```
  Git-tracked Markdown
        │
        │ parse
        ▼
  derived semantic cache
  ```
  
  The cache must always be reconstructible.
  
  No user knowledge should exist only in the cache.
  
  Deleting the entire cache should at worst cause a performance penalty while it is rebuilt.
  
  The cache should normally live outside the knowledge garden, for example:
  
  ```
  ~/.cache/logseq-gardener/<graph-id>/
  ```
  
  and must never need to be committed to Git.
  
  An embedded database such as SQLite is acceptable if useful.
  
  A required external database service is not.
  
  The project should specifically avoid operational characteristics such as:
  
  ```
  database daemon setup
  ports
  server discovery
  stale background engines
  manually started services
  ```
  
  A user should be able to install one executable and use it.
  
  ---
- # Primary use cases
- ## 1. CLI for humans, agents, and scripts
  
  The project should expose its semantic engine as a first-class CLI.
  
  Illustrative read operations:
  
  ```
  garden pages
  garden page "Logseq/Publish"
  
  garden complete "Logseq/Pub"
  
  garden refs "Logseq/Publish"
  garden backlinks "Logseq/Publish"
  
  garden block 67c48ebc-07e8-498f-b9ee-08d339d0469d
  
  garden search "mldoc"
  
  garden status
  ```
  
  The exact command hierarchy should be designed deliberately.
  
  A resource-oriented API may ultimately be cleaner:
  
  ```
  garden page list
  garden page get "Logseq/Publish"
  garden page refs "Logseq/Publish"
  garden page backlinks "Logseq/Publish"
  
  garden block get <uuid>
  
  garden search "mldoc"
  ```
  
  Machine-readable output is a first-class requirement.
  
  Commands should eventually support predictable structured output such as:
  
  ```
  --json
  ```
  
  so that the same CLI is pleasant for:
  
  ```
  humans
  shell scripts
  Claude Code
  Codex
  Copilot
  Cursor
  other agents
  ```
  
  Agents should not need to independently rediscover Logseq semantics by grepping a graph every time they work.
  
  The CLI should give them the same semantic understanding available to the editor.
  
  ---
- ## 2. Language server for editors
  
  garden lsp should expose the same semantic engine using the Language Server Protocol.
  
  The principal first editor target is:
  
  ```
  LazyVim / Neovim
  ```
  
  An editor integration should be thin.
  
  Conceptually:
  
  ```
  LazyVim
   │
   ├── existing generic Markdown tooling
   │
   └── Logseq-specific client
             │
             ▼
         garden lsp
             │
             ▼
        garden-core
  ```
  
  The editor should spawn:
  
  ```
  garden lsp
  ```
  
  as a long-running process communicating over standard input/output.
  
  The user should not configure:
  
  ```
  TCP sockets
  ports
  server processes
  database services
  ```
  
  Initial LSP/editor capabilities should focus on high-value Logseq behavior:
  
  ```
  [[ page-reference completion
  go to definition for [[Page]]
  find references / backlinks
  ((UUID)) block-reference navigation
  block-reference completion
  hover / preview where useful
  ```
  
  Generic Markdown intelligence should continue to coexist with tools such as Marksman rather than being unnecessarily reimplemented.
  
  ---
- ## 3. Static knowledge-garden publishing
  
  garden publish should eventually use the same parsed graph to produce a static website.
  
  The initial motivating publication corpus is:
  
  ```
  https://github.com/codekiln/logseq-encode-garden
  ```
  
  The current Logseq SPA publication model effectively serializes the graph into a large browser-side database and requires the visitor to load a substantial portion of the garden before rendering individual content.
  
  The replacement should instead be able to generate:
  
  ```
  one page
        ↓
  one independently useful HTML document
  ```
  
  A page request should not require downloading the entire garden.
  
  Static output should eventually support:
  
  ```
  real page HTML
  stable URLs
  SEO metadata
  search-engine indexing
  backlinks
  internal references
  incremental rebuilds
  sitemaps
  optional client-side search
  optional graph visualization loaded only when requested
  ```
  
  The publisher should be another client of garden-core, not a separate Logseq parser.
  
  ---
- # Performance philosophy
  
  Performance is a primary project requirement rather than a later optimization.
  
  The target corpus includes gardens with more than one million lines.
  
  The engine should therefore use:
  
  > 
  
  lazy activation, eager background warming, and JIT reprioritization.
- ## Lazy activation
  
  Starting Neovim or invoking unrelated commands should not automatically parse every known garden.
  
  A garden becomes active when the engine is given strong evidence that the garden is being used.
  
  For example:
  
  ```
  open first file within graph
        ↓
  identify graph root
        ↓
  activate graph
  ```
- ## Eager background warming
  
  Once a graph becomes active, indexing should begin opportunistically in the background.
  
  The system should not wait until the user types [[ before beginning expensive work.
  
  Conceptually:
  
  ```
  graph activated
      ↓
  load any previous cache
      ↓
  cheap graph discovery
      ↓
  parse high-value/current files
      ↓
  background semantic parsing
      ↓
  incrementally richer index
  ```
- ## JIT reprioritization
  
  Interactive actions may reprioritize work already underway.
  
  For example:
  
  ```
  background parser currently processing graph
             │
  user requests completion for "Logseq/Pub"
             │
             ▼
  prioritize likely relevant unresolved files/entities
  ```
  
  However:
  
  > 
  
  An interactive completion request must never block waiting for a whole-graph indexing operation.
  
  It should query the best currently available snapshot and return promptly.
  
  ---
- # Progressive completeness
  
  A cold garden does not have to transition from:
  
  ```
  nothing
  ```
  
  directly to:
  
  ```
  perfect semantic knowledge
  ```
  
  The engine may progressively improve its understanding.
  
  For example:
  
  ```
  Level 0
  cheap page/file discovery
  
  Level 1
  canonical page identity
  page references
  basic properties
  
  Level 2
  blocks
  UUID references
  backlinks
  aliases
  namespaces
  
  Level 3
  tasks
  embeds
  queries
  richer semantics
  ```
  
  Results should become available as soon as they are trustworthy enough for the operation being requested.
  
  The system should distinguish internally between provisional and fully resolved information when necessary.
  
  ---
- # Warm startup and incremental indexing
  
  A previously indexed graph should not require a whole-graph parse every time a client starts.
  
  A warm cache should be usable immediately.
  
  Reconciliation should then determine what changed.
  
  For Git-backed gardens, Git itself may provide useful invalidation information:
  
  ```
  last indexed commit
        +
  current HEAD
        +
  working-tree changes
        +
  filesystem changes since process start
  ```
  
  The implementation should investigate whether this can sharply reduce startup reconciliation work.
  
  File watching should allow an active graph to incrementally re-index only files that change.
  
  The central invariant should be:
  
  ```
  edit one file
     ↓
  reparse only what is necessary
     ↓
  update dependent semantic indexes
  ```
  
  rather than rebuilding the whole garden.
  
  ---
- # Multiple gardens
  
  Multiple graphs are a first-class requirement from the beginning.
  
  A user may have:
  
  ```
  work graph
  personal graph
  public garden
  private garden
  specialized project graphs
  ```
  
  Each graph should have its own identity and cache.
  
  ```
  Graph A → Cache A
  Graph B → Cache B
  Graph C → Cache C
  ```
  
  Queries should normally be scoped to one graph.
  
  Cross-graph behavior should not be introduced accidentally.
  
  If cross-graph search or linking is later supported, it should be explicit.
  
  ---
- # Shared cache across humans, editors, and agents
  
  A major goal is that all clients benefit from the same previously computed semantic knowledge.
  
  For example:
  
  ```
  garden cache
                         │
        ┌────────────────┼───────────────┐
        │                │               │
       CLI              LSP            agent
        │                │               │
      human           Neovim          AI tool
  ```
  
  A user should not pay separately for:
  
  ```
  Neovim indexing
  agent indexing
  CLI indexing
  publishing indexing
  ```
  
  The underlying cache and semantic definitions should be reusable.
  
  Long-running clients such as garden lsp may maintain an in-memory hot index over the same persistent cache used by short-lived CLI invocations.
  
  A mandatory always-running daemon should not be required.
  
  ---
- # Read-only first
  
  The first implementation must be read-only.
  
  This should be an architectural property, not merely a documented convention.
  
  Early core APIs should simply contain no method capable of mutating the user's Markdown.
  
  This permits testing against real and valuable knowledge gardens with very low risk.
  
  Initial development should prioritize:
  
  ```
  parse
  index
  resolve
  complete
  search
  navigate
  reference
  publish
  ```
  
  before:
  
  ```
  insert
  update
  move
  delete
  rename
  merge
  ```
  
  ---
- # Future mutation API
  
  The system should nevertheless be designed so that mutations can later become first-class operations.
  
  Likely operations include:
  
  ```
  page create
  page rename
  
  block insert
  block update
  block move
  block delete
  
  property set
  property remove
  ```
  
  The eventual command vocabulary and semantics should review existing Logseq APIs for useful precedent.
  
  Mutation should operate semantically on pages and blocks rather than forcing every client to perform raw Markdown text surgery.
  
  For example:
  
  ```
  garden block update <uuid> --content "..."
  ```
  
  should eventually be able to compute and preview the minimum source-file change required.
  
  Mutation operations should initially support:
  
  ```
  dry run
  diff preview
  expected source revision
  atomic write
  clear conflict reporting
  ```
  
  before silent automated writes are considered safe.
  
  ---
- # Concurrency and CRDT direction
  
  Concurrent editing is an important long-term use case.
  
  Human editors and multiple AI agents may eventually operate on the same graph simultaneously, potentially even on the same block.
  
  The architecture should therefore **not foreclose CRDT-backed or otherwise conflict-aware editing**.
  
  However, a CRDT implementation is not an MVP dependency.
  
  The progression should likely be:
  
  ```
  read-only semantic engine
  
        ↓
  
  safe single-operation mutations
  with revision checking
  
        ↓
  
  operation log / explicit concurrency model
  
        ↓
  
  concurrent block-level editing
  
        ↓
  
  CRDT-backed collaborative mutation where justified
  ```
  
  A CRDT should not replace Markdown as the user's durable canonical representation unless a later explicit design decision changes the project's fundamental goals.
  
  Instead, a CRDT may eventually serve as a coordination or editing layer that reconciles back to the file-backed graph.
  
  The design should pay particular attention to:
  
  ```
  stable block identity
  source revisions
  block ordering
  parent/child relationships
  concurrent modification
  merge semantics
  Git interaction
  ```
  
  ---
- # Parsing and semantic compatibility
  
  The project should not casually invent a new interpretation of Logseq Markdown.
  
  Before choosing a parser or semantic representation, the implementation should perform an architectural review of existing work.
  
  Particularly relevant prior art includes:
  
  ```
  logseq/mldoc
  
  Logseq OG graph-parser
  
  Logseq's OG → DB importer and its
  compatibility/regression cases
  
  Tine / lsdoc
  
  Looksyk
  
  Markdown Oxide
  
  LogseqLSP
  
  relevant newer OCaml projects
  inside the Logseq organization
  ```
  
  Questions to answer include:
  
  ```
  What exactly constitutes a page?
  
  How is a page name derived from a filename?
  
  How are namespaces encoded?
  
  How do title:: and aliases affect identity?
  
  How are journals treated?
  
  How are block UUIDs represented and resolved?
  
  What parser output is needed for indexing?
  
  Can mldoc's fast outline-only mode be reused?
  
  Should mldoc itself be linked directly?
  
  Would a compatible Rust parser be preferable?
  
  Which real-world malformed or legacy constructs
  must be tolerated?
  ```
  
  Parser fidelity and index performance should both be benchmarked rather than assumed.
  
  ---
- # Implementation-language decision
  
  The implementation language for the semantic core is intentionally not fixed by this brief.
  
  Two especially plausible directions are:
  
  ```
  OCaml
    direct use of Logseq's mldoc ecosystem
    strong parsing/tooling heritage
    compatibility advantage
  
  Rust
    strong systems/LSP ecosystem
    straightforward native distribution
    strong performance/tooling
    existing relevant projects such as Looksyk
  ```
  
  The choice should be made through an explicit architectural decision record based on:
  
  ```
  mldoc compatibility
  performance
  incremental parsing/indexing needs
  LSP implementation
  binary distribution
  FFI complexity
  licensing
  maintenance burden
  existing reusable code
  ```
  
  Do not choose a language merely because it is currently fashionable or familiar.
  
  ---
- # Initial benchmark corpus
  
  The first substantial real-world test garden should be:
  
  ```
  codekiln/logseq-encode-garden
  ```
  
  This graph is useful because it is both large and semantically nontrivial.
  
  It includes real examples of:
  
  ```
  Logseq namespaces
  filename encoding
  properties
  aliases
  UUID-bearing blocks
  references
  agent-authored content
  publication concerns
  ```
  
  Its current published web version also provides a concrete performance problem that garden publish may eventually solve.
  
  Development should supplement this real corpus with small deterministic fixtures representing difficult Logseq edge cases.
  
  Personal knowledge gardens should never be the project's only correctness corpus.
  
  ---
- # Benchmark requirements
  
  Performance work should be measurable.
  
  The project should establish repeatable benchmarks for at least:
  
  ```
  cold graph activation
  
  time to first useful page-completion index
  
  complete cold semantic index
  
  warm startup with no changes
  
  warm startup after one changed file
  
  time from save to updated completion/reference result
  
  page completion latency
  
  page lookup latency
  
  backlink lookup latency
  
  block UUID lookup latency
  
  peak memory
  
  persistent cache size
  ```
  
  The primary UX constraint is more important than any initial numeric target:
  
  > 
  
  Typing [[ in a large graph must not appear to freeze while the graph is indexed.
  
  Similarly:
  
  > 
  
  A warm graph should feel immediately available.
  
  Concrete latency budgets should be established from benchmarks on logseq-encode-garden rather than invented prematurely.
  
  ---
- # Reliability requirements
  
  Correctness takes precedence over speculative cleverness.
  
  The engine should:
  
  ```
  never mutate source during read/index operations
  
  never require the cache to recover user knowledge
  
  tolerate interrupted indexing
  
  detect stale cache entries
  
  recover from cache corruption by rebuilding
  
  avoid silently guessing ambiguous page identity
  
  make graph scope explicit
  
  preserve source locations
  
  produce deterministic machine-readable output
  ```
  
  Operations that cannot be answered completely because the background index is still warming should have an explicit representation for incomplete or provisional state where necessary.
  
  ---
- # Compatibility philosophy
  
  The compatibility target is:
  
  ```
  Logseq OG / file-based graph semantics
  ```
  
  The project should not automatically adopt incompatible semantics from the newer Logseq database model.
  
  The newer DB implementation and importer are valuable as:
  
  ```
  documentation
  test cases
  edge-case knowledge
  architectural prior art
  ```
  
  but not necessarily as the model that logseq-gardener should reproduce.
  
  The user owns Markdown.
  
  The engine exists to understand that Markdown.
  
  ---
- # Relationship to generic Markdown
  
  Logseq files remain Markdown files.
  
  The project should coexist with generic Markdown tooling rather than attempting to replace all of it.
  
  For the initial Neovim use case:
  
  ```
  generic Markdown
    → Tree-sitter
    → Marksman / existing Markdown tooling
  
  Logseq semantics
    → garden lsp
  ```
  
  The project should add knowledge that generic Markdown tools do not possess:
  
  ```
  Logseq page identity
  Logseq namespaces
  block UUIDs
  block references
  properties
  aliases
  backlinks
  embeds
  queries
  task semantics
  ```
  
  It should avoid producing duplicate diagnostics or competing implementations of features that existing Markdown tools already handle correctly.
  
  ---
- # Initial development sequence
  
  The project should advance through narrow vertical slices.
  
  **Phase 0 — Architecture and compatibility**
  
  Study the reference implementations and decide:
  
  ```
  parser strategy
  core language
  semantic model
  cache strategy
  graph identity
  incremental invalidation model
  ```
  
  Create compatibility fixtures and benchmarks before implementing broad features.
  
  **Phase 1 — Read-only page index**
  
  On logseq-encode-garden:
  
  ```
  activate graph
  enumerate pages
  derive canonical page identities
  persist disposable cache
  incrementally refresh changed files
  ```
  
  Expose:
  
  ```
  garden pages
  garden page get
  garden complete
  garden status
  ```
  
  **Phase 2 — LazyVim vertical slice**
  
  Implement enough LSP/editor support that:
  
  ```
  [[Logseq/Pub
  ```
  
  immediately produces page-reference completion.
  
  The editor must not wait for a graph-wide parse.
  
  **Phase 3 — Reference graph**
  
  Add:
  
  ```
  page refs
  backlinks
  go-to-definition
  find-references
  aliases
  namespaces
  ```
  
  **Phase 4 — Block semantics**
  
  Add:
  
  ```
  block hierarchy
  id:: UUID indexing
  ((UUID)) completion
  block go-to-definition
  block references
  embeds
  ```
  
  **Phase 5 — Publisher**
  
  Produce static per-page HTML from the same semantic model.
  
  Measure first-content and page-load behavior against the current Logseq-published Encode Garden.
  
  **Phase 6 — Richer Logseq semantics**
  
  Investigate:
  
  ```
  properties
  tasks
  queries
  templates
  advanced embeds
  ```
  
  **Phase 7 — Safe mutations**
  
  Add explicit previewable page/block mutation operations.
  
  **Phase 8 — Concurrent editing**
  
  Only after mutation semantics and stable node identity are trustworthy, investigate CRDT-backed collaborative editing and merging.
  
  ---
- # Explicit non-goals for the first version
  
  The first version is not intended to:
  
  ```
  replace every Logseq UI feature
  
  implement the new Logseq DB model
  
  provide real-time collaborative editing
  
  replace Git
  
  become the canonical storage database
  
  implement a browser SPA
  
  implement every Markdown feature itself
  
  rewrite user files during indexing
  
  require a daemon or server setup
  ```
  
  Keeping these out of the initial scope is important.
  
  ---
- # Architectural principle
  
  The central artifact of the project should not be:
  
  ```
  a Neovim plugin
  ```
  
  or:
  
  ```
  a static-site generator
  ```
  
  or:
  
  ```
  an AI-agent MCP server
  ```
  
  It should be:
  
  > 
  
  **a fast, faithful, local semantic engine for Logseq file gardens.**
  
  Everything else is an adapter.
  
  ```
  garden-core
                             │
              ┌──────────────┼──────────────┐
              │              │              │
             CLI            LSP          publisher
              │              │              │
        humans/agents      editors           web
  ```
  
  This boundary is what allows the same million-line garden to become fast once and remain fast everywhere.
  
  ---
- # Project thesis
  
  logseq-gardener should make a Logseq OG garden useful without requiring Logseq.
  
  A person should eventually be able to point the tool at years of existing Markdown and immediately obtain:
  
  ```
  semantic search
  page and block resolution
  backlinks
  editor completion
  agent tooling
  static publishing
  safe structured mutation
  ```
  
  while retaining the properties that made the file-based Logseq format attractive in the first place:
  
  ```
  plain files
  Git
  portability
  inspectability
  local ownership
  long-term durability
  ```
  
  The long-term aspiration is therefore larger than a Logseq Neovim plugin:
  
  > 
  
  Preserve the useful semantic model of file-based Logseq as an open, high-performance knowledge-garden substrate that can support editors, humans, AI agents, scripts, and websites independently of the original application.
-