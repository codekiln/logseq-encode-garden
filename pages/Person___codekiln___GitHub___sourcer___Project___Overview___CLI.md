# CLI (`srcr`)
	- The CLI is the reconciler and inspector for Sourcer: it reads [[Person/codekiln/GitHub/sourcer/Project/Overview/Config]], applies allow/install policy from config, and reports canonical paths and materialization state in forms humans and machines can rely on.
	- ## Design principles
		- **Config-first in MVP** — most workflows are edit `srcr.toml`, then run a small set of verbs.
		- **Deterministic paths** — given identity + config, `where` always prints the same path; never depends on cwd of a prior clone.
		- **Structured output from day one** — `--json` (or global `--format json`) is not an afterthought; agents and CI parse it without scraping text.
		- **Idempotent reconcile** — repeated `install` is safe; second run is mostly no-op when disk matches desired state.
		- **Fail closed on access** — identities not allowed by config error with explicit codes in JSON, not silent skips.
	- ## Global flags (intended)
		- `--root <path>` — override source root for this invocation (see config precedence).
		- `--config <path>` — explicit config file path.
		- `--json` — machine-readable stdout for supported subcommands.
		- `-q` / `--quiet` — errors only (human scripting).
		- `-v` / `--verbose` — show git/network steps (human debugging).
	- ## MVP commands
		- ### `srcr install`
			- Reconcile all `[sources]` entries with default install (where `install` is not `false`; MVP: all entries) against disk under `root`.
			- Use when: fresh machine, after pulling config changes, devcontainer image build, CI cache warm-up.
			- Behavior sketch:
				- Load merged config.
				- For each source to install: allow check (MVP: must be in `[sources]`) → clone or update → checkout `ref`.
				- Exit non-zero if any source failed (recommended for CI).
			- Does not remove repos dropped from config in MVP (avoid accidental data loss).
		- ### `srcr status`
			- Compare desired vs realized state for each declared source (and optionally scan disk for undeclared trees).
			- Human output: table of identity, ref wanted, ref on disk, dirty/clean, allowed, path.
			- JSON: array of per-source status objects (schema aligned with `use` output fields; see Phase 2).
			- Use when: "why is my agent not seeing library X?" before diving into git manually.
		- ### `srcr where <identity>`
			- Print resolved absolute path for one canonical identity without mutating disk.
			- Use when: shell scripts, editor workspace roots, agent tool wrappers, `cd "$(srcr where …)"`.
			- Must work even if clone does not exist yet (path is still deterministic; `exists: false` in JSON mode).
			- JSON reports `allowed` (and `exists`) without performing clone.
			- Example:
				- ~~~sh
				  cd "$(srcr where github.com/example/library)"
				  rg 'func Foo' .
				  ~~~
		- ### `srcr list`
			- List identities from config (and optionally list materialized repos under `root` not in config).
			- JSON: `{ "configured": [...], "materialized": [...] }` or flat list with `declared: true|false` per entry.
		- ### `srcr doctor`
			- Preconditions: `git` available, `root` writable, config parseable, `[sources]` / `[allow]` consistent, network reachable if install will run.
			- Reports misconfiguration early (wrong `SRCR_ROOT`, schema-invalid TOML, SSH agent missing for ssh clones).
			- Use in devcontainer `postCreateCommand` and CI setup jobs before expensive `install`.
	- ## Phase 2 commands
		- Phase 2 is out of MVP scope. See [[Person/codekiln/GitHub/sourcer/Project/Overview]] Phase 2 section.
		- ### `srcr use <identity>` (ad hoc materialization)
			- Materialize one repository by identity (replaces the defunct `srcr ensure`); optionally with ref override flags for one-shot use outside config.
			- Subject to allow policy: identity must match `[sources]` or an `[allow]` pattern.
			- Optional config-mutating mode may add the identity to `[sources]` (see overview non-goals).
			- Example:
				- ~~~sh
				  srcr use github.com/example/project --json
				  ~~~
			- Example JSON (contract to stabilize in implementation):
				- ~~~json
				  {
				    "uri": "github.com/example/project",
				    "path": "/home/user/sources/github.com/example/project",
				    "exists": true,
				    "cloned": false,
				    "allowed": true,
				    "ref": "main",
				    "ref_on_disk": "main",
				    "dirty": false
				  }
				  ~~~
			- Field notes:
				- `uri` — canonical identity (primary key).
				- `path` — absolute resolved path.
				- `exists` — directory present and looks like a git repo.
				- `cloned` — whether this invocation performed a fresh clone.
				- `allowed` — access policy permitted the operation.
				- `ref` / `ref_on_disk` / `dirty` — optional but valuable for status-oriented agents.
		- ### Other Phase 2 commands (deferred)
			- `srcr unuse` — remove identity from config and optionally disk.
			- `srcr remove` / `srcr prune` — delete materialized trees matching removed config entries.
			- `srcr migrate` — move existing non-conventional clones into canonical layout.
			- `srcr index` — metadata or [[llms.txt]] generation over the corpus.
	- ## Structured output contract
		- Stdout: JSON document or JSON lines per resource when streaming many sources.
		- Stderr: human-readable errors; never mix error text into JSON stdout (enables `jq` pipelines).
		- Stable field names across `use` (Phase 2), `status`, and `install` summary objects.
		- Version field recommended: `"schema_version": 1` at top level for forward compatibility.
		- Exit codes (illustrative):
			- `0` — success, all requested operations satisfied.
			- `1` — operational failure (git error, network).
			- `2` — not allowed (identity not in `[sources]` or `[allow]`).
			- `3` — config parse or validation error.
	- ## Consumers
		- **Humans** — `status` and `doctor` for everyday debugging; `where` for navigation.
		- **Shell** — `where` in scripts; `install` in Makefile/`mise` tasks.
		- **CI** — `install` + `status --json` gate merges when required sources must be present at pinned refs.
		- **AI agents (MVP)** — `install`, `where`, `status --json`, and `list --json`; planners use `path` + `allowed` without inventing `/tmp` clones.
		- **AI agents (Phase 2)** — `use … --json` for optional repos not in the install set.
		- **Devcontainers** — `install` during image build; `doctor` in `postCreateCommand` (see [[Person/codekiln/GitHub/sourcer/Project/Overview/DevContainer]]).
	- ## Comparison to adjacent tools
		- Not [[git]] — does not commit, branch, or merge; may shell out to git for clone/fetch/checkout only.
		- Not [[aqua]] / [[asdf]] — those install binaries; Sourcer installs source trees.
		- Complements [[mise]] — mise runs `srcr install` as a task; Sourcer does not manage compiler versions.
		- Lighter than [[git submodules]] for "repos you should read" — no submodule pointer commits required.
	- ## Example end-to-end session (MVP)
		- ~~~sh
		  # clone project, enter dev environment
		  cd ~/work/my-service
		  srcr doctor
		  srcr install
		  srcr status --json | jq '.sources[] | select(.dirty==true)'
		  cd "$(srcr where github.com/my-org/api-contracts)"
		  less README.md
		  ~~~
		- Agent equivalent (MVP): rely on pre-installed corpus from `install`; use `where` for paths.
		- Agent equivalent (Phase 2): single `use` call per optional library before code search tools run against `path`.
