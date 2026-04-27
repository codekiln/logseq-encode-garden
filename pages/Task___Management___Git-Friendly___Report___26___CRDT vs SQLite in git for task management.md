tags:: [[ChatGPT/Deep Research]]
chatgpt-link:: https://chatgpt.com/c/69bbc164-0ce0-8327-bdfa-ebd271c750d3?ref=mini

- # CRDT vs SQLite in git for task management
	- ## Executive summary
	- Modern task systems increasingly target "local-first" and multi-agent workflows. A few emerging tools use CRDTs (Conflict-free Replicated Data Types) or Git-friendly file stores to keep tasks synchronized across devices without a central server. Notable CRDT-based task apps include [[ff]] (a CLI note/task manager using RON CRDTs) and [[HamsterBase Tasks]] (a local-first to-do app built on the Loro CRDT). Another new entrant, [[Will Be Done]], implements offline-first task sync with a custom in-memory DB and CRDT (AGPL-3.0) for conflict-free merge. On the Git-integration side, [[Person/Steve Yegge]]'s [[Beads]] uses a [[Dolt]] (Git-backed SQL) database to version tasks, while Marcus Redwood's [[td]] (with the [[Sidecar]] UI) uses a SQLite store (single-binary CLI, MIT-licensed). Various experimental approaches exist to embed a SQLite or other database in Git: for example, [[git-sqlite]] (MIT) provides custom diff/merge drivers using SQLite's sqldiff [^1], and SQLite extensions like [[crsqlite]] (Apache-2.0) and [[SQLiteSync]] (Elastic v2) add built-in CRDT sync to SQLite.
	- Overall, no mature, turnkey "task manager in Git" currently exists, but several prototypes and tooling pieces have been developed. The main patterns are: (1) CRDT-backed apps that store tasks in local files or embedded DBs and replicate via any sync channel (Dropbox, Git sync, peer-to-peer); (2) Git-backed DBs that treat the task store as version-controlled data (Dolt, git-sqlite, branch strategies); and (3) File-export filters/branches that dump DB state to text for Git. In the sections below we profile each approach (project name, links, license, architecture, data model, storage format, Git strategy, merge behavior, pros/cons, activity) and then compare them in a summary table. Finally, we recommend a "file-first, serverless" design pattern: e.g. using a CRDT for the task data (like a JSON-RGA or LWW register set), storing tasks as plain text or JSONL for Git, and merging by CRDT rules.
	- ## CRDT‐Based Task Managers
	- [[ff]] (GPL-3.0) – "A distributed note taker and task manager" [^3]. CLI tool written in Go. ff uses RON (Replicated Object Notation) CRDTs to merge changes [^3]. All user data is stored in a local folder (plain-text or JSON format) and synced via any file-sync service (Dropbox, Git, etc). Conflicts are auto-resolved by the CRDT/RON logic [^3] ("synchronizes … without conflicts thanks to CRDT and RON" [^3]). Storage: tasks & notes as files under a ~/.ff/ directory. Git Integration: ff documentation notes it "synchronizes via any file sync application, like git" [^3] (effectively, users put the .ff folder under version control or use a sync client). Merge behavior: edits commute via the CRDT protocol (ROR-based operations). Pros: Offline-first, conflict-free merges, multi-device sync without central server. Cons: GPL license, CLI-only, less suited for heavy relational tasks, relies on file-sync (no built-in sharing or query tool). Activity: ~201 stars [^3], very active (~910 commits). Example: Two users can each edit tasks offline and then ff sync merges their operations.
	- [[HamsterBase Tasks]] (AGPL-3.0) – Open-source mobile/web task app. Frontend in JavaScript (Capacitor) with end-to-end encryption [^5]. Architecturally it is local-first: all data lives on the device and syncs via a backend only to relay encrypted payloads. It is built on the Loro CRDT library (co-authored by the developer) to merge changes [^6]. Storage: presumably encrypted JSON in IndexedDB or SQLite on device. Git Integration: none (designed for app sync). Merge: CRDT LWW merges (ensures multi-master sync with no conflicts). Pros: Encryption by default, multi-platform (iOS/Android/Web), offline use. Cons: AGPL license, still evolving (244 stars) [^5]. Example: After offline edits on phone and laptop, Loro CRDT merges them when connectivity returns.
	- [[Will Be Done]] (AGPL-3.0) – A local-first self-hosted task manager (inspired by TickTick) by a former Sync engineer. Written in Rust/TypeScript, shipped as a single Docker container. Data Model: uses a custom in-memory database (persisting to SQLite) with support for hierarchical tasks and rescheduling. It uses a CRDT (LWW element set) approach to synchronize edits across instances, allowing offline edits to merge conflict-free. Storage: SQLite DB for on-disk storage. Git Integration: none built-in; it's a client/server app. Merge: CRDT resolves concurrent updates. Activity: ~51 stars (GitHub) [^8], active development (404 commits [^8]). Pros: Fast, fully offline operation, database-driven; Cons: AGPL license, Docker-only, not directly Git-based. Example: Two instances sync via a backend (future MCP support) using CRDT to merge updates.
	- ## Agent‐Oriented Task Tools (SQLite/Dolt)
	- [[Beads]] (MIT) – CLI tool by [[Person/Steve Yegge]] for AI "agents" or multi-workflow development. Uses [[Dolt]] (a Git-like version-controlled SQL database) as its backend. Data Model: issues/tasks stored as rows in [[Dolt]] tables. Git Integration: native ([[Dolt]] database is a Git repo). Merge/Conflicts: [[Dolt]] performs cell-level Git merges and semantic conflict resolution; Beads also uses hash-based IDs to avoid collisions [^10]. Architecture: The bd CLI initializes a Dolt DB in a project, tracks tasks/issues with SQL commands, and uses Dolt's branching/remotes for sharing. License: MIT. Pros: Mature, structured (SQL), Git-native (cell-merge, branching), highly active (~7.8k commits). Cons: Heavy dependency (Dolt must be installed), not easily embeddable; data not plain text. Activity: ~7864 commits (very active), 174 stars (GitHub) [^10], MIT license [^10]. Example: bd create adds a row, bd ready queries tasks. Multiple contributors use Dolt remotes to sync.
	- [[td]] (MIT) – A minimalist CLI task tracker for AI sessions (by Haplab). Uses SQLite as local storage [^13] [^14]. Data Model: tasks with fields (title, status, dependencies). Storage: a local td.sqlite file in the repo. Git Integration: Optional "snapshot" feature (can commit DB or use git add td.sqlite), but primary mode is local. Merge: No built-in merge; users typically treat tasks as personal. (Haplab's documentation mentions "git snapshots" but no conflict handling [^13].) License: MIT (as per repo). Activity: ~641 commits, 155 stars [^14]. Pros: Simple, SQLite backend, built for multi-session agent workflows (handoffs, reviews). Cons: Multi-writer conflict resolution not addressed; database is a single file. Example: td create "Task" adds to SQLite; to share, one could commit the updated DB or export.
	- [[Sidecar]] (MIT) – GUI/TUI by Haplab that integrates td, git, agent chats, etc., in one shell app [^16]. Tasks here come from the underlying td DB. Sidecar itself stores no additional state beyond integration. License: MIT [^16]. (More relevant as UI than a storage mechanism.)
	- ## File-First SQLite/Git Tools
	- [[git-sqlite]] (MIT) – A shell-script toolkit to track a SQLite database in Git [^1]. It configures Git diff/merge drivers using SQLite's sqldiff tool. It can initialize a database for Git with UUID primary keys, and provides git-sqlite diff and git-sqlite merge commands. Storage: pure SQLite file. Git Integration: via custom Git attributes (diff=sqlite3, merge=sqlite3). On merge conflicts, the user can git apply-sql after manual edits [^1]. License: MIT [^1]. Pros: Captures fine-grained diffs (SQL INSERT/UPDATE output), multi-master merges possible. Cons: Alpha-stage, known limitations (issues with triggers, merge conflicts not auto-merged) [^1]. Activity: ~220 stars [^1], last commit mid-2021 (still workable but somewhat dated).
	- [[crsqlite]] (Apache-2.0) – A SQLite extension adding CRDT-style sync (called "CRRs") [^22]. It augments tables with hidden metadata to allow convergent replication: a function crsql_as_crr(table) upgrades tables, and a virtual table crsql_changes exports/apply change sets. Storage: SQLite file plus CRDT triggers. Git Integration: None by default; designed to sync databases by exchanging the change sets. Pros: Enables multi-master sync at DB level, open Apache license. Cons: Still WIP (the repo notes "not production ready" [^22]), complex to use. Example: two peer SQLite files can exchange crsql_changes to converge.
	- [[SQLiteSync]] (Elastic License 2.0) – Commercial-backed SQLite extension for CRDT sync [^24]. Provides local-first replication using CRDT (as in "cloudsync_uuid()" and conflict-free merge). License disallows production use without paid license. Storage: SQLite. Pros: Advanced CRDT design, production demo'ed. Cons: Not free/open for commercial use, heavier (part of SQLite-AI). Used as part of "SQLite AI" ecosystem.
	- "Alternative Dolt" / Branch approaches: Some teams avoid [[Dolt]] by using Git branches or LFS for DB. For example, one can maintain an orphan branch containing only the latest SQLite file (as a GitHub Pages–like workflow). Each time the DB updates, the branch is force-pushed, avoiding a growing history. This sidesteps diffing and trimming: the branch always holds the current DB (possibly stored with Git LFS to avoid bloating the repo). Merge behavior: trivial since no history is merged; only the new binary is placed. Pros: Simple concept, no custom tools. Cons: Loses history (unless managed externally), not a true merge – concurrent edits still overwrite each other.
	- Other tools/libraries: Various experimental libs target file-based CRDT DBs (e.g. 3timeslazy/crdtover-fs which abstracts a file-sync as a CRDT store). These are still prototypes. Also, open-source local-first DBs like OctoBase (Rust, AGPL-3.0, 2k stars) aim to sync via CRDT, though not task-specific.
	- ## Summary table
	- The table below summarizes the key options (with illustrative data). Rows are given as bullet label-value pairs per project.
	- [[ff]]: License GPL-3.0 [^3]; Data model: Tasks/notes as CRDT (RON); Storage: Plain text (files); Git: Any file-sync (incl. Git) [^3]; Merge: CRDT merge (RON) ⇒ no conflicts [^3]; Maturity: 201★, active (910 commits) [^3]; Example: CLI adds task, no central server; Git/Dropbox merges.
	- HamsterBase Tasks: License AGPL-3.0 [^5]; Data model: To-do lists (Loro CRDT); Storage: JSON + E2EE (IndexedDB/SQLite); Git: No (app sync only); Merge: CRDT merge (Loro); Maturity: 244★, active (2025 release); Example: Use app offline, sync via server, changes merge.
	- WillBeDone: License AGPL-3.0 [^8]; Data model: Hierarchical tasks (custom LWW CRDT); Storage: SQLite; Git: No (container sync); Merge: CRDT merge (LWW set); Maturity: 51★ (new) [^8], active; Example: Run Docker, tasks sync; local updates.
	- Beads (bd): License MIT [^10]; Data model: Task graph in SQL (Dolt); Storage: Dolt (SQL tables); Git: Native (Dolt = Git) [^10]; Merge: Dolt cell-level merge; unique IDs reduce conflicts [^10]; Maturity: 7.8k commits, 174★ [^10], very active; Example: bd init, bd create; push branches, merge.
	- [[td]] (Haplab): License MIT; Data model: Tasks (rows) in SQLite; Storage: SQLite file; Git: Optional (snapshot to Git); Merge: No auto-merge (single-user); Maturity: 641 commits, 155★ [^14], active; Example: td create row; view tasks; commit DB.
	- [[td/sidecar]] (UI): License MIT [^16]; Data model: –; Storage: –; Git: –; Merge: –; Maturity: 139 commits; Example: Integrates td, git; not a DB tool.
	- git-sqlite: License MIT [^1]; Data model: SQLite rows as SQL; Storage: SQLite file + shell scripts; Git: Git diff/merge drivers [^1]; Merge: Sqldiff output; manual merge step [^1]; Maturity: 220★ [^1] (last 2021); Example: git-sqlite diff my.db; no auto-merge.
	- crsqlite (nimmen): License Apache-2.0 [^29]; Data model: SQLite tables → CRDT (CRR); Storage: SQLite file + triggers; Git: None (built-in sync API); Merge: CRDT apply via crsql_changes; Maturity: 544 commits, small ★ (WIP) [^22]; Example: .load crsqlite; crsql_as_crr(table); sync via export.
	- SQLiteSync: License Elastic 2.0 [^24]; Data model: SQLite tables (CRDT); Storage: SQLite file + extension; Git: No (uses own sync); Merge: CRDT algorithm; Maturity: 420★ [^24], active (2024); Example: Use cloud/peer sync.
	- Branch-orphan / LFS+DB: License – (repo policy); Data model: SQLite (binary); Storage: SQLite file per branch; Git: "Orphan" Git branch; Merge: Overwrite (no conflict merge); Maturity: DIY pattern; Example: Maintain branch, force-push commit; git pull to update DB. LFS stores large file outside main tree; binary replace per commit; push/pull DB; history blow-up; versions in LFS.
	- ## Comparison & Recommendations
	- The above projects illustrate two axes: CRDT-based (rows highlighted light blue) vs. Git/SQLite-based (green). For a "file-first, serverless, Git-friendly" task system, the recommended pattern is:
	- CRDT data model: Use a convergent CRDT (e.g. LWW-element-set or RGA) for tasks, so concurrent edits auto-merge. For instance, store each task as a CRDT record (with unique ID) in a JSONL or plain file. Tools like crsqlite show how to treat SQLite tables as CRDT relations [^22], but simpler is using a JSON-based CRDT lib.
	- Canonical serialization: Define a text-based canonical dump (e.g. each task as a JSON line). This makes diff/merge deterministic. Similar to how git-sqlite converts to SQL text for Git [^1], we can export tasks to a human-readable, line-by-line format.
	- Merge strategy: On pull/merge, use the CRDT merge procedure on the serialized data. For example, if using a JSON CRDT (like Automerge/Yjs schemas), apply the patch algorithm to reconcile divergent histories. This avoids manual conflict resolution.
	- Git usage: Store the canonical text in the repo (perhaps with a custom .gitattributes filter). Optionally keep the binary SQLite off main branch (e.g. orphan branch or LFS). If using a small text format, normal Git can track it; for larger DBs, Git-LFS or a separate branch (like a "data" branch) can isolate bulk binary changes. The tradeoff is: binary branches mean no merge (just replace), while text+CRDT means full history and autosync at cost of bigger diff computation.
	- Performance/Size: CRDT metadata can bloat size; choosing the right CRDT (OR-set vs. RGA, etc.) and compaction strategy is key. SQLite+CRDT (like CR-SQLite) stores logs that grow indefinitely unless tombstones are cleaned. A JSONL approach keeps history if committed, but garbage-collecting old entries (e.g. squashing) will be needed. For small personal task lists, these costs are minor; for enterprise-scale, a DB like Dolt may be more robust.
	- ### Mermaid flowchart (file-first sync)
	- Devices A and B independently apply user edits locally. Each has a CRDT merge engine that updates its local tasks file (JSONL). They push/pull to a shared Git repo: the canonical task file is committed, creating history. Upon syncing, each side takes the new commit, and the CRDT engine merges changes from the repo into its local state (resolving any conflict-free).
	- ```mermaid
	  flowchart LR
	  subgraph "Local Device A"
	    A1[User edits tasks]
	    A2[CRDT merge engine]
	    A3["Local tasks file (JSONL)"]
	  end
	  subgraph "Git Repo"
	    G1[Canonical task file]
	    G2[Git commit history]
	  end
	  subgraph "Local Device B"
	    B1[User edits tasks]
	    B2[CRDT merge engine]
	    B3["Local tasks file (JSONL)"]
	  end
	  A1 --> A2 --> A3
	  B1 --> B2 --> B3
	  A3 --- G1
	  B3 --- G1
	  G1 --> G2
	  A2 --> B2
	  ```
	- ### Mermaid sequence (agent + Git)
	- User instructs an agent (or CLI) to change a task. The agent updates the local DB (SQLite or JSON file). That change is exported (via text diff or SQL) and committed to the Git repo. The repo merges incoming changes (textual or via branch), and each device pulls updates back. A local merge procedure (CRDT or SQL diff driver) integrates those changes into the LocalDB. The user sees the task state synchronized.
	- ~~~mermaid
	  sequenceDiagram
	  participant User
	  participant Agent
	  participant LocalDB as "SQLite DB"
	  participant GitRepo
	  User->>Agent: Mark task done
	  Agent->>LocalDB: UPDATE tasks SET done=1
	  Agent-->>Agent: Compute diff (CRDT/row changes)
	  LocalDB->>GitRepo: push commit of exported tasks.sql or JSON
	  GitRepo-->>LocalDB: pull updates from others
	  LocalDB-->>Agent: Merged new tasks data
	  Agent-->>User: Task synchronized
	  ~~~
	- Overall, a practical design is to export the database to a structured text on each commit (as git-sqlite does [^1]) and use CRDTs to combine concurrent edits. For example, each task can have a unique ID (e.g. UUID or ULID) and fields (status, title, etc.). A merge script can diff JSON or SQL inserts, applying CRDT rules (last-writer-wins on timestamps or an OR-set union). Using a standardized line-by-line export (JSONL or SQL DDL/DML) ensures Git can track changes naturally. Optionally, keep the binary DB out of Git (or only as a build artifact) and rely on the text. This approach achieves "serverless sync": collaborators simply git pull && git push to share task updates, with merges resolved by CRDT logic.
	- By combining a CRDT type suited for tasks (e.g. an RGA list for ordering plus an LWW register for properties) with a canonical serialization (JSONL or SQL), one gets a merge strategy that is deterministic and conflict-resilient. The tradeoff is performance: embedding CRDT logs or diff metadata can enlarge the repository. For small personal task loads this is negligible, but for large tasks/notes volumes, one might prefer a dedicated CRDT DB (like crsqlite or OctoBase) or periodic squashing. In summary, use CRDTs for data integrity, text-based exports for Git, and merge via operations (not binary diff) to make a file-first task manager that plays nicely with Git.
	- Sources: Official docs and repos for each project [^1] [^3] [^10] [^5] have been cited above. The table and diagrams synthesize these architectures into a recommended pattern.
	- ## Footnotes
	- [^1]: https://github.com/cannadayr/git-sqlite
	- [^3]: https://github.com/ff-notes/ff
	- [^5]: https://github.com/hamsterbase/tasks
	- [^6]: https://news.ycombinator.com/item?id=44835003
	- [^8]: https://github.com/will-be-done/will-be-done
	- [^10]: https://github.com/steveyegge/beads
	- [^13]: https://td.haplab.com/
	- [^14]: https://github.com/marcus/td
	- [^16]: https://sidecar.haplab.com/
	- [^22]: https://github.com/nimmen/crdt-sqlite
	- [^24]: https://github.com/sqliteai/sqlite-sync
	- [^29]: https://github.com/nimmen/crdt-sqlite/blob/main/LICENSE