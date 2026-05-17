# Mise-inspired project conventions (speculative)
	- Design sketch for how the **Sourcer (`srcr`) implementation repo** might be organized if it deliberately follows [[mise]] ergonomics at the project level—not the end-user `srcr.toml` contract (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]]) or the command surface (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]]).
	- ## Status
		- Speculative. Nothing here is an implementation commitment; it captures conventions worth copying, deferring, or rejecting before scaffolding the Rust crate.
	- ## Why echo [[mise]]
		- ### [[My Notes]]
			- I've been pleased with the design choices that [[Person/Jeff Dickey]] made with mise, and I'm interested in learning more about those choices and mise by mirroring `srcr` on `mise` where appropriate.
		- [[mise]] already models the mental model Sourcer wants: declarative manifest → reconcile → inspect ([[mise/About]]; [mise-en-place overview](https://mise.jdx.dev/)). Contributors who know mise should recognize Sourcer's layout quickly.
		- [[mise/Architecture]] documents a **command-per-module** CLI layer ([architecture](https://mise.jdx.dev/architecture.html), e.g. [`install.rs`](https://github.com/jdx/mise/blob/main/src/cli/install.rs)); Sourcer's MVP verbs (`install`, `status`, `where`, `list`, `doctor`) map cleanly onto that pattern.
		- mise ships as a single fast binary with structured output and strong config validation—both are first-class for agents and CI (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec]] design goals; compare [[mise/install]] / [mise install](https://mise.jdx.dev/cli/install.html) as the reconcile verb for tools).
	- ## Language and toolchain (speculative)
		- [[Rust]] for the CLI and reconcile engine: predictable performance, easy static linking, good ecosystem for TOML + JSON + subprocess orchestration.
		- **clap** (derive) for subcommands and global flags aligned with [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]] (`--root`, `--config`, `--json`, exit codes).
		- **usage-lib** (with `clap` feature) so the same clap graph can emit a [[usageCLI]] spec and feed shell completions—same dependency stack as [[mise]] (`usage-lib` in [mise `Cargo.toml`](https://github.com/jdx/mise/blob/main/Cargo.toml)); bridge crate [clap_usage](https://github.com/jdx/usage/tree/main/clap_usage) ([[usageCLI]]; [usage.jdx.dev](https://usage.jdx.dev/)). [[Person/Jeff Dickey]] is `created-by` on [[mise]] and maintains [jdx/usage](https://github.com/jdx/usage) ([[Person/Jeff Dickey/GitHub/usage]]).
		- **serde** + **toml** for `srcr.toml`; **serde_json** for stdout contracts.
		- **taplo-compatible JSON Schema** published from the repo (see Config page); optional `schemars` or hand-maintained schema crate.
		- **git2** or thin `std::process` wrappers around `git`—favor whichever keeps error messages and exit codes stable for `doctor` and CI gates.
		- Dev loop: declare `rust`, `cargo`, and `srcr` (dogfood) in the repo's own `mise.toml` ([[mise]] key idea: project-local `mise.toml` in [[mise/About]]); `mise run check` / `mise run test` as the default contributor entrypoint ([[mise/JTBD/3 - Task Runner]]; [walkthrough tasks](https://mise.jdx.dev/walkthrough.html)).
	- ## Repository layout (speculative)
		- Flat, mise-like root—no deep monorepo until needed:
			- ~~~
			  srcr/                    # binary crate (name TBD: srcr vs sourcer)
			    src/
			      main.rs              # clap root, global flags, dispatch
			      cli/                 # one module per subcommand (mise pattern)
			        install.rs
			        status.rs
			        where.rs
			        list.rs
			        doctor.rs
			      config/              # load, merge, validate srcr.toml
			      model/               # Identity, SourceSpec, Root, AllowPolicy (Phase 2)
			      provider/            # github.com, gitlab.com, … URL + path defaults
			      reconcile/           # desired vs disk; clone/fetch/checkout
			      output/              # human tables vs JSON envelope + schema_version
			      error.rs
			    tests/                 # integration: temp dirs, fake remotes or fixtures
			  schema/
			    srcr.schema.json       # published URL target
			  completions/             # prerendered fallback scripts ([mise `completions/`](https://github.com/jdx/mise/tree/main/completions))
			    _srcr                    # zsh
			    srcr.bash
			    srcr.fish
			    srcr.ps1
			  srcr.usage.kdl             # checked-in usage spec (generated from `srcr usage`)
			  src/assets/
			    srcr-extra.usage.kdl     # dynamic `complete` mounts (identities, paths)
			  docs/                    # user docs (mdBook or mise-style site later)
			  mise.toml                # contributor tools + tasks
			  srcr.toml                # example / dogfood manifest for this repo
			  Cargo.toml
			  README.md
			  LICENSE
			  ~~~
		- **Intentionally not copied from mise (MVP):** `src/plugins/` ([[mise/plugin]]; [plugins](https://mise.jdx.dev/plugins.html)), backend registry ([[mise/Backend]]; [backend architecture](https://mise.jdx.dev/dev-tools/backend_architecture.html)), env-var manager ([[mise/JTBD/2 - Environment Manager]]; [environments](https://mise.jdx.dev/environments/)), task runner ([[mise/JTBD/3 - Task Runner]]), version cache layout—Sourcer is one domain (source trees), not a meta package manager ([[mise/JTBD/1 - Dev Tool Installer]]).
	- ## CLI structure
		- Follow mise's **one file per subcommand** under `src/cli/` ([[mise/Architecture]]; [command layer](https://mise.jdx.dev/architecture.html#command-layer)); each module owns:
			- argument definitions
			- invocation of shared `config::load` + `reconcile::*`
			- human vs JSON rendering via `output::`
		- Shared concerns live outside `cli/`:
			- global `App` struct (root, config path, format)
			- `error::ExitCode` mapping to CLI contract (`0` success, `1` git/network, `2` not allowed, `3` config)
		- Phase 2 commands (`use`, `unuse`, `prune`) add sibling modules without restructuring the tree—same pattern as mise adding commands over time.
	- ## Shell completions ([[usageCLI]] + clap_usage)
		- [[mise]] is written by [[Person/Jeff Dickey]] (`created-by` on [[mise]]), who also built [[usageCLI]] ([Usage](https://usage.jdx.dev/); [[usageCLI/spec]]). Sourcer should mirror mise's completion stack—not hand-maintaining four shell scripts—using [clap_usage](https://github.com/jdx/usage/tree/main/clap_usage) to bridge clap → usage spec, then the **usage** CLI to emit shell scripts ([usage completions CLI](https://usage.jdx.dev/cli/completions)).
		- ### Design goals for `srcr` completions
			- **Single source of truth** — clap derive definitions drive runtime parsing, usage spec export, and generated completion scripts (usage's stated goals: [Usage README](https://github.com/jdx/usage/blob/main/README.md); mise CLI docs are `@generated by usage-cli`—see [mise completion doc](https://mise.jdx.dev/cli/completion.html)).
			- **Dynamic where it matters** — `srcr where <identity>` and Phase 2 `srcr use <identity>` should complete canonical identities from the effective `srcr.toml`, not a static list baked into the binary (parallel: `complete "tool" run="mise registry …"` in [mise-extra.usage.kdl](https://github.com/jdx/mise/blob/main/src/assets/mise-extra.usage.kdl)).
			- **Graceful offline fallback** — checked-in prerendered scripts under `completions/` when the external `usage` binary is missing ([`completion.rs`](https://github.com/jdx/mise/blob/main/src/cli/completion.rs) `include_str!` for [`_mise`](https://github.com/jdx/mise/blob/main/completions/_mise), `mise.bash`, `mise.fish`, `mise.ps1`); mise prefers usage-generated bash/fish but falls back for zsh while quirks remain (see `--usage` flag comment in that file).
			- **Contributor ergonomics** — document like [[mise/How To/Install Mise/Shell Completions in Zsh]] and [mise completion](https://mise.jdx.dev/cli/completion.html); CI regenerates spec + completions when CLI surface changes (mise checks in [`mise.usage.kdl`](https://github.com/jdx/mise/blob/main/mise.usage.kdl)).
		- ### Pipeline (mirroring mise)
			- 1. **clap graph** — `Cli::command()` built from derive on `src/cli/*` + global flags ([[mise/Architecture]]).
			- 2. **Hidden `srcr usage` subcommand** (like mise's hidden `mise usage`) — converts `Cli` → `usage::Spec` via `usage-lib`, prints KDL to stdout; optional `min_usage_version` line at top ([`usage.rs`](https://github.com/jdx/mise/blob/main/src/cli/usage.rs); [usage spec](https://usage.jdx.dev/spec/)).
			- 3. **`srcr-extra.usage.kdl`** — appended custom `complete` directives clap cannot infer ([mise-extra.usage.kdl](https://github.com/jdx/mise/blob/main/src/assets/mise-extra.usage.kdl): `complete "task" run="mise tasks ls --complete"`, `complete "tool" run="mise registry --complete"`, etc.).
			- 4. **Checked-in `srcr.usage.kdl`** — committed artifact from `srcr usage` + extra file; used for docs generation and diff review in PRs (mise: [`mise.usage.kdl`](https://github.com/jdx/mise/blob/main/mise.usage.kdl), generated CLI pages under [mise `docs/cli/`](https://github.com/jdx/mise/tree/main/docs/cli)).
			- 5. **`srcr completion <shell>`** — shells out to the **usage CLI** (mise: `cmd("usage", …)` in [`completion.rs`](https://github.com/jdx/mise/blob/main/src/cli/completion.rs); install `usage` via mise—[[mise/How To/Install Mise/Shell Completions in Zsh]], [registry `usage.toml`](https://github.com/jdx/mise/blob/main/registry/usage.toml)):
				- ~~~sh
				  usage generate completion <shell> srcr \
				    --usage-cmd "srcr usage" \
				    --cache-key "<CARGO_PKG_VERSION>"
				  ~~~
				- Exact invocation pattern from mise: `usage generate completion <shell> mise --usage-cmd "mise usage" --cache-key <version>` ([source](https://github.com/jdx/mise/blob/main/src/cli/completion.rs)).
				- On failure, fall back to `include_str!("../../completions/…")` (mise `prerendered()` in the same file).
			- 6. **User install** — [[mise/How To/Install Mise/Shell Completions in Zsh]] (`mise use --global usage@latest`, `mise completion zsh > …`); [mise completion examples](https://mise.jdx.dev/cli/completion.html). Sourcer analogue: `srcr completion zsh > ~/.zsh/completions/_srcr`.
		- ### `srcr usage` implementation sketch
			- ~~~rust
			  // cli/usage.rs — hidden from default help (mise pattern)
			  let cli = Cli::command().version(Resettable::Reset);
			  let mut spec: usage::Spec = cli.into();
			  // optional spec tweaks before print
			  let extra = include_str!("../assets/srcr-extra.usage.kdl").trim();
			  println!("{min_version}\n{}\n{extra}", spec.to_string().trim());
			  ~~~
			- clap_usage's `generate(&mut cmd, "srcr", stdout)` remains useful for **bootstrapping** ([clap_usage README](https://github.com/jdx/usage/blob/main/clap_usage/README.md)); long term, prefer `usage-lib`'s `Into<usage::Spec>` path ([`usage.rs`](https://github.com/jdx/mise/blob/main/src/cli/usage.rs) `let mut spec: usage::Spec = cli.into()`).
			- Optional `--usage` flag on root command ([clap_usage example](https://github.com/jdx/usage/blob/main/clap_usage/README.md#usage)) for debugging spec emission without a subcommand.
		- ### Dynamic completions in `srcr-extra.usage.kdl` (speculative)
			- Identity argument on `where` (and later `use`):
				- ~~~kdl
				  complete "source_identity" run="srcr list --complete" descriptions=#true
				  ~~~
				- Implement `srcr list --complete` (hidden flag) printing one identity per line from merged config—parallel to [mise-extra.usage.kdl](https://github.com/jdx/mise/blob/main/src/assets/mise-extra.usage.kdl) `complete "task" run="mise tasks ls --complete"` and `complete "tool" run="mise registry --complete" descriptions=#true`.
			- Config and root paths:
				- ~~~kdl
				  complete "config_file" type="file" filter="*.toml"
				  complete "root_dir" type="dir"
				  ~~~
			- Ref values (harder): defer tag/branch completion to Phase 2; MVP may complete only identities, not every ref string.
			- Phase 2 `[allow]` wildcards: do not attempt pattern completion in shell; static identities only.
		- ### `srcr completion` subcommand (speculative)
		  id:: 6a09876d-c987-40cb-a512-938fe457398f
			- Aliases: `complete`, `completions` ([mise completion](https://mise.jdx.dev/cli/completion.html): `mise completion` with aliases `complete` / `completions` in [`completion.rs`](https://github.com/jdx/mise/blob/main/src/cli/completion.rs)).
			- Shells: `bash`, `fish`, `zsh`, `powershell` (same enum as mise; [doc examples](https://mise.jdx.dev/cli/completion.html)).
			- Flags:
				- `--include-bash-completion-lib` — [mise completion flag](https://mise.jdx.dev/cli/completion.html#--include-bash-completion-lib) (required for bash per upstream docs).
				- `--usage` — hidden on mise; forces usage path when prerendered is default ([`completion.rs` comment](https://github.com/jdx/mise/blob/main/src/cli/completion.rs): usage default for fish/bash, not zsh yet).
			- **Default policy (speculative):** follow mise's current split per [`call_usage` / `prerendered`](https://github.com/jdx/mise/blob/main/src/cli/completion.rs); ship **prerendered `_srcr`** for zsh until identity completion works under [[zsh/OhMyZsh]] ([[mise/Docs/Guides/Walkthrouh]] task-usage section: tab completion vs Oh My Zsh).
		- ### Prerendered scripts and CI
			- Regenerate in CI or via `mise run completions` when `src/cli/*` or `srcr-extra.usage.kdl` changes:
				- ~~~sh
				  srcr usage > srcr.usage.kdl
				  for shell in bash fish zsh powershell; do
				    srcr completion "$shell" > "completions/srcr.${shell}"
				  done
				  ~~~
				- Fail CI if `git diff` is non-empty (mise-style drift guard).
			- CLI reference markdown can be `@generated by usage-cli from usage spec` ([mise completion.md header](https://github.com/jdx/mise/blob/main/docs/cli/completion.md); [mise `docs/cli/`](https://github.com/jdx/mise/tree/main/docs/cli)).
		- ### Dogfood in project `mise.toml`
			- Declare the **usage** tool alongside rust ([registry `usage.toml`](https://github.com/jdx/mise/blob/main/registry/usage.toml)—backends `aqua:jdx/usage`, `cargo:usage-cli`; [[mise/Backend/aqua]]):
				- ~~~toml
				  [tools]
				  usage = "latest"
				  ~~~
			- Task `completions` depends on `usage` + built `srcr` binary.
		- ### What Sourcer likely does *not* need from usage (MVP)
			- Task-script `#USAGE` blocks ([[mise/Docs/Guides/Walkthrouh]] "Task Usage Spec"; [walkthrough](https://mise.jdx.dev/walkthrough.html))—Sourcer has no task runner in v1 ([[mise/JTBD/3 - Task Runner]]).
			- Spec mounts for `default_subcommand` / naked task names ([`usage.rs`](https://github.com/jdx/mise/blob/main/src/cli/usage.rs) sets `default_subcommand = "run"` and task mounts).
			- hosting on usage.sh ([Usage README](https://github.com/jdx/usage/blob/main/README.md)—optional later).
		- ### Open completion questions
			- Whether `srcr list --complete` should read only project `srcr.toml` or also user-global config (must match `where` resolution).
			- Caching: `--cache-key` should bump when spec or extra KDL changes, not only CLI semver.
			- Nushell / elvish: defer unless usage gains first-class support and a contributor asks.
	- ## Config handling in code
		- Parse → validate against schema → **effective config** struct (mirrors mise's project vs global `mise.toml` story at a smaller scale—[[mise/About]]; [walkthrough config](https://mise.jdx.dev/walkthrough.html)):
			- Project `srcr.toml` (primary)
			- Optional user-global file (XDG path TBD)
			- Overrides: `SRCR_ROOT`, `--root`, `--config`
		- Keep **identity as the map key** in memory (`BTreeMap` or ordered vec) so `status` and `install` iterate deterministically—important for stable JSON array order in agent pipelines.
		- String-or-table `SourceSpec` enum matches the progressive disclosure model on [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]].
		- Validation errors should cite TOML path + schema rule (Taplo/editor parity with runtime errors).
	- ## Core crates vs single crate
		- **Start as one binary crate** (mise-scale complexity is years away).
		- Split only when a boundary is obvious:
			- `srcr-config` — types + parse + schema (usable from tests and future LSP)
			- `srcr-provider` — identity → remote URL + default path
		- Avoid premature `srcr-core` / `srcr-cli` split until integration tests hurt.
	- ## Reconcile engine (speculative)
		- `install` walks `[sources]` (respecting future `install = false`), for each:
			- resolve path under `root`
			- allow check ([[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Trust]])
			- clone or fetch + checkout `ref`
			- record per-source result for aggregate exit code
		- `where` is pure resolution—no git side effects.
		- `status` diffs desired ref vs `HEAD` / tag / dirty working tree.
		- Idempotency and "no delete on config removal" match Config page semantics.
	- ## Testing conventions
		- **Unit:** provider URL/path derivation, config parsing edge cases, allow matching (Phase 2).
		- **Integration:** temp `root` + local bare repos or vendored fixtures; no network in default `cargo test`.
		- **Snapshot:** JSON stdout for `status --json` / `where --json` with `schema_version` field—agents depend on stable keys.
		- **mise tasks:** `mise run test`, `mise run lint`, `mise run ci` ([[mise/JTBD/3 - Task Runner]]; [walkthrough tasks](https://mise.jdx.dev/walkthrough.html)) wrapping `cargo test`, `clippy`, schema check that `srcr.schema.json` matches types.
	- ## Distribution and release (speculative)
		- Ship `srcr` the way mise ships `mise`:
			- GitHub releases with prebuilt binaries (target matrix: linux/macos, x86_64/aarch64)—compare [installing mise](https://mise.jdx.dev/installing-mise.html) ([[mise/How To/Install Mise/The First Time]]).
			- Optional [[aqua]] registry entry ([[mise/Backend/aqua]]; [aqua backend](https://mise.jdx.dev/dev-tools/backends/aqua.html)) for org-wide pinning
			- Document `mise use -g srcr@<version>` ([[mise/use]]; [mise use](https://mise.jdx.dev/cli/use.html)); consumers add `srcr` under `[tools]` in project `mise.toml`
		- Versioning: semver; config `schema_version` in JSON output is independent of CLI semver.
	- ## Documentation site (later)
		- User-facing docs parallel [mise.jdx.dev](https://mise.jdx.dev/) structure at a high level:
			- Getting started ([[mise/Docs/Guides/Getting Started]]; [getting started](https://mise.jdx.dev/getting-started.html)) — edit `srcr.toml` → `srcr install`
			- Config reference generated from schema (compare Taplo + JSON Schema note on [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]])
			- CLI reference per subcommand ([mise `docs/cli/`](https://github.com/jdx/mise/tree/main/docs/cli), usage-generated)
			- Devcontainer cookbook cross-linking [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/DevContainer]]
		- Contributor architecture: [[mise/Architecture]] ([architecture.html](https://mise.jdx.dev/architecture.html)).
	- ## Project `mise.toml` (dogfood sketch)
		- ~~~toml
		  [tools]
		  rust = "stable"
		  cargo-binstall = "latest"
		  taplo = "latest"
		  usage = "latest"
		  [tasks.check]
		  run = "cargo clippy -- -D warnings && cargo test"
		  [tasks.schema]
		  run = "taplo check -s schema/srcr.schema.json srcr.toml"
		  [tasks.completions]
		  run = "srcr usage > srcr.usage.kdl && srcr completion bash > completions/srcr.bash"
		  [tasks.ci]
		  depends = ["check", "schema", "completions"]
		  ~~~
		- Consumer projects would add `srcr` to `[tools]` and a `sources-install` task running `srcr install` (already sketched on [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]]).
	- ## Deliberate divergences from mise
		- No plugin system for SCM providers in MVP ([[mise/plugin]]; [plugins](https://mise.jdx.dev/plugins.html))—hard-code github/gitlab/codeberg conventions; add provider traits only when a second implementation hurts.
		- No shell hook / activate path ([[mise/activate]]; [mise activate](https://mise.jdx.dev/cli/activate.html), [[mise/Shim]])—Sourcer does not modify `PATH` or env; optional `SRCR_ROOT` only.
		- No `srcr use` writing config in MVP—imperative ergonomics deferred ([[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec]] non-goals; contrast [[mise/use]]); repo can still reserve `cli/use.rs` behind a feature flag later.
		- Smaller config surface than `mise.toml` (no `[tasks]` ([[mise/JTBD/3 - Task Runner]]), `[env]` ([[mise/JTBD/2 - Environment Manager]]), `[plugins]` in `srcr.toml`).
	- ## Open questions
		- Binary name: `srcr` vs `sourcer` on disk and in [[aqua]]—prefer short `srcr` for typing; crate package name may differ.
		- Library crate published to crates.io or binaries-only?
		- Use `uv`-style single static binary vs require system `git`—`doctor` should report which is assumed.
		- Whether to embed schema in binary for `srcr doctor --validate-config` offline.
		- Alignment with [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Design/Thinking]] personas before locking directory names.
	- ## Related pages
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]] — `srcr.toml` contract
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]] — verbs and JSON fields
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/DevContainer]] — image build + mise pairing
		- [[mise]] — hub; [mise.jdx.dev](https://mise.jdx.dev/)
		- [[mise/Architecture]] — [architecture](https://mise.jdx.dev/architecture.html)
		- [[mise/How To/Install Mise/Shell Completions in Zsh]] — [mise completion](https://mise.jdx.dev/cli/completion.html)
		- [[mise/Docs/Guides/Walkthrouh]] — [walkthrough](https://mise.jdx.dev/walkthrough.html); task `#USAGE` + completion notes
		- [[usageCLI]] — [usage.jdx.dev](https://usage.jdx.dev/); [[usageCLI/spec]]; [completions CLI](https://usage.jdx.dev/cli/completions)
		- [[Person/Jeff Dickey]] — author of mise and usage
		- [[Person/Jeff Dickey/GitHub/usage]] — [github.com/jdx/usage](https://github.com/jdx/usage)
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec]] — product goals and mise-compatible declaration model
	- ## Upstream source index (mise completion stack)
		- [mise `src/cli/completion.rs`](https://github.com/jdx/mise/blob/main/src/cli/completion.rs) — `usage generate completion`, prerendered fallbacks
		- [mise `src/cli/usage.rs`](https://github.com/jdx/mise/blob/main/src/cli/usage.rs) — hidden `mise usage` spec export
		- [mise `src/assets/mise-extra.usage.kdl`](https://github.com/jdx/mise/blob/main/src/assets/mise-extra.usage.kdl) — dynamic `complete` hooks
		- [mise `mise.usage.kdl`](https://github.com/jdx/mise/blob/main/mise.usage.kdl) — checked-in spec
		- [mise `registry/usage.toml`](https://github.com/jdx/mise/blob/main/registry/usage.toml) — install `usage` via mise
		- [jdx/usage `clap_usage/`](https://github.com/jdx/usage/tree/main/clap_usage) — clap → spec bridge