# Config (`srcr.toml`)
	- In the MVP, the config file is the primary interface. Humans, CI, devcontainer builds, and AI agents all converge on the same artifact: a declarative description of which source repositories should exist on disk, at which refs, under which root layout.
	- ## Role in the system
		- Sourcer separates **desired state** (what `srcr.toml` says) from **realized state** (what exists under the source root after `srcr install`).
		- That boundary mirrors [[mise]], [[npm]], and other tools that read a manifest and reconcile the environment.
		- Unlike a package manager, Sourcer does not resolve version graphs or build artifacts. It materializes git (and eventually other SCM) trees at stable paths keyed by canonical identity.
	- ## File location and discovery
		- Project-local: `srcr.toml` at the repository root of the project being worked on (alongside or near `mise.toml`, `package.json`, etc.).
		- User-global: a dotfile or XDG path for personal defaults (exact discovery TBD; precedence should favor project over user over built-in defaults).
		- Multiple files may merge in the future; MVP can assume a single effective config per invocation context.
	- ## Top-level keys (MVP)
		- `root` — filesystem root for all materialized sources (default `~/sources`).
		- `[sources]` — table of canonical identities → ref or source object (see access policy below).
	- ## Access policy (MVP vs Phase 2)
		- Sourcer separates two concepts (see [[Person/codekiln/GitHub/sourcer/Project/Overview/Trust]]):
			- **Install by default** — identity is in `[sources]`; `srcr install` clones or updates it at the declared ref.
			- **Allowed to download** — identity or wildcard may be materialized; identities not in `[sources]` need an explicit allow rule before clone (Phase 2).
		- **MVP:** listing under `[sources]` means **allowed** and **installed on `install`**. No separate `[allow]` table in MVP.
		- **Phase 2:** optional `[allow]` for wildcards without auto-install; optional `install = false` on a `[sources]` entry (allowed, path-resolvable, not cloned until `srcr use`).
		- Phase 2 example:
			- ~~~toml
			  [allow]
			  "github.com/my-org/*" = true
			  "github.com/my-org/internal-*" = true
			  [sources]
			  "github.com/example/explore-only" = { ref = "main", install = false }
			  ~~~
	- ## `[sources]` — declaration model
		- Keys use the canonical identity form `<provider>/<owner>/<repository>` (no scheme, no `.git` suffix).
		- Values are either a **ref string** (happy path) or a **source object** (escape hatch).
		- ### String form
			- ~~~toml
			  [sources]
			  "github.com/example/project" = "main"
			  "github.com/example/library" = "v1.2.3"
			  "codeberg.org/person/tool" = "latest"
			  ~~~
			- Semantics:
				- `"main"`, `"v1.2.3"` — checkout that ref after clone or on update.
				- `"latest"` — provider-defined resolution (e.g. default branch tip); document per-provider behavior in implementation.
		- ### Object form
			- ~~~toml
			  [sources]
			  "github.com/example/project" = "main"
			  "github.com/example/private-tool" = { ref = "main", clone = "ssh" }
			  "internal.example.com/platform/tool" = {
			    ref = "main",
			    remote = "ssh://git@internal.example.com/platform/tool.git"
			  }
			  ~~~
			- MVP object keys (intentionally small):
				- `ref` — branch, tag, or commit-ish name (required when using object form).
				- `clone` — transport preference: `"https"` | `"ssh"` (provider may default to https for public hosts).
				- `remote` — full clone URL when identity alone is insufficient (self-hosted, non-standard paths).
				- `path` — override local directory relative to `root`; use only when layout cannot follow the default convention.
			- Provider defaults should derive:
				- HTTPS clone URL from identity when `remote` is omitted.
				- Default path `root/<identity-as-path>` e.g. `~/sources/github.com/example/project`.
		- ### Identity → URL → path (worked example)
			- Identity: `github.com/acme/widget`
			- Default remote: `https://github.com/acme/widget.git`
			- Default path with `root = "~/sources"`: `~/sources/github.com/acme/widget`
			- Ref `v2.0.0` → `git fetch` + `git checkout v2.0.0` (exact git mechanics are implementation detail; config only names intent).
	- ## Layout root (`root`)
		- Default tree:
			- ~~~
			  ~/sources/
			    github.com/
			      owner/
			        repository/
			  ~~~
		- Repository **identity** never changes when `root` changes; only the resolved absolute path changes.
		- Precedence for `root` (highest wins):
			- 1. CLI flag e.g. `srcr install --root /mnt/ssd/sources`
			- 2. Environment variable `SRCR_ROOT`
			- 3. `root` in `srcr.toml`
			- 4. Built-in default `~/sources`
		- Examples:
			- ~~~sh
			  srcr install --root /mnt/ssd/sources
			  ~~~
			- Phase 2 (ad-hoc materialization):
				- ~~~sh
				  srcr use github.com/example/project --root /mnt/ssd/sources
				  ~~~
			- ~~~sh
			  export SRCR_ROOT=/mnt/shared/sources
			  ~~~
			- ~~~toml
			  root = "~/sources"
			  ~~~
	- ## Symmetry with [[mise]]
		- Mental mapping:
			- mise `[tools]` → Sourcer `[sources]`
			- `mise install` → `srcr install`
			- tool version pin → git ref pin
		- Sourcer remains a **separate binary and config schema**; it should not require a mise plugin to feel native.
		- Recommended project pattern:
			- ~~~toml
			  # mise.toml
			  [tools]
			  srcr = "latest"
			  ~~~
			- ~~~toml
			  # mise.toml tasks (illustrative)
			  [tasks.sources-install]
			  run = "srcr install"
			  ~~~
		- Onboarding: `mise install` then `mise run sources-install` (or project-specific task name).
	- ## Editor and schema affordances
		- Ship a published **JSON Schema** for `srcr.toml` even though the on-disk format is TOML.
		- [[Taplo]] (and editors that delegate to it) can attach the schema for:
			- autocomplete on `[sources]` keys and object fields
			- enum validation for `clone = "https" | "ssh"`
			- warnings on unknown keys (guards typo-driven silent misconfig)
		- Document a one-line editor snippet (VS Code `evenBetterToml`, etc.) pointing at the schema URL.
		- Rationale: in the MVP, users spend more time editing the file than memorizing CLI flags; schema quality directly reduces support burden.
	- ## Reconciliation semantics (`srcr install`)
		- For each entry in `[sources]` where `install` is not `false` (MVP: all entries):
			- Resolve identity → path and remote.
			- Allow check (MVP: must be listed in `[sources]`).
			- If path missing: clone at `ref`.
			- If path exists: fetch and checkout `ref` (idempotent; no-op when already correct).
			- If entry removed from config: **do not** delete by default in MVP (safe default); explicit prune command is a future addition.
		- Partial failure: document whether `install` stops on first error or continues and reports aggregate status (recommend aggregate + non-zero exit for CI).
	- ## What config deliberately does not do (MVP)
		- No imperative mutation: no `srcr use` / `srcr unuse` writing the file (Phase 2; see [[Person/codekiln/GitHub/sourcer/Project/Overview]] non-goals and [[Person/codekiln/GitHub/sourcer/Project/Overview/CLI]] Phase 2 commands).
		- No dependency graph between sources (ordering is declaration order or topological sort later).
		- No build or compile hooks.
		- No replacement for [[git submodules]] when a hard submodule pin is required for reproducible builds.
	- ## Example project `srcr.toml`
		- A service repo that keeps adjacent libraries on disk for reading and agent context:
			- ~~~toml
			  root = "~/sources"
			  [sources]
			  "github.com/my-org/api-contracts" = "main"
			  "github.com/my-org/shared-go" = "v1.4.2"
			  "github.com/my-org/observability-lib" = { ref = "main", clone = "ssh" }
			  ~~~
		- After `srcr install`, `srcr where github.com/my-org/api-contracts` always returns the same path regardless of which machine ran install, modulo `root` override.
	- ## Future config directions (Phase 2 and beyond)
		- `[allow]` table and `install = false` on `[sources]` entries (see access policy above).
		- Included config fragments (`import = "allow.d/*.toml"`).
		- Per-source TTL or eviction metadata for garbage collection.
		- Content-addressed snapshot pins (commit SHA required, immutability guarantees).
		- Imperative `srcr use` for [[DevContainer/Feature]] one-liners without hand-editing the developer's global config (see [[Person/codekiln/GitHub/sourcer/Project/Overview/CLI]]).