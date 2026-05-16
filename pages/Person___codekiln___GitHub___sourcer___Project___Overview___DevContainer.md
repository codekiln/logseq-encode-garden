- # DevContainer integration
	- Parent: [[Person/codekiln/GitHub/sourcer/Project/Overview]]
	- DevContainers, [[DevContainer/Feature]]s, and [[GitHub Codespaces]] usually open **one** repository. Sourcer provides a repeatable way to materialize **many** trusted repos into predictable paths inside the container filesystem.
	- ## Problem being solved
		- Service development often needs adjacent repos: API contracts, shared libraries, platform SDKs, infra modules, internal docs.
		- Without a convention, teams either:
			- manually clone into random paths in `postCreateCommand`,
			- vendor copies (stale),
			- or never clone — agents and new hires lack context.
		- Single-repo devcontainer defaults reinforce that gap.
	- ## Design fit
		- Declarative `srcr.toml` in the **project repo** lists `[sources]` required for this codebase.
		- `srcr install` during **image build** or **container create** populates `root` (default `~/sources`).
		- `srcr where` gives stable paths for editor multi-root, scripts, and agent tools.
		- Access policy (see [[Person/codekiln/GitHub/sourcer/Project/Overview/Trust]]): MVP `[sources]` defines what `install` fetches; Phase 2 `[allow]` may permit optional `srcr use` — important for images baked with credentials.
	- ## Recommended placement in devcontainer lifecycle
		- ### Image build (best cache behavior)
			- Copy `srcr.toml` (and optional Phase 2 `allow` fragments) early.
			- Run `srcr install` before copying full application source.
			- Docker layer caches heavy git clones when only app code changes.
			- Example Dockerfile fragment:
				- ~~~dockerfile
				  COPY srcr.toml /work/srcr.toml
				  RUN srcr install
				  COPY . /work
				  ~~~
		- ### postCreateCommand (developer iteration)
			- Run `srcr doctor` then `srcr install` to pick up config changes without rebuild.
			- Pair with [[mise]]: install `srcr` tool, then `mise run sources-install`.
		- ### postStartCommand
			- Optional `srcr status --json` for health checks in Codespaces UI or internal telemetry.
	- ## `devcontainer.json` sketch
		- ~~~json
		  {
		    "name": "my-service",
		    "build": { "dockerfile": "Dockerfile" },
		    "postCreateCommand": "mise install && srcr doctor && srcr install",
		    "remoteUser": "vscode"
		  }
		  ~~~
		- Mount considerations:
			- Bind-mount host `~/sources` only when intentionally sharing cache across host and container; document access-policy implications.
			- Default: corpus lives **inside** image or container volume for reproducible agent sandboxes.
	- ## Dev Container Features
		- A [[DevContainer/Feature]] can wrap Sourcer for consumers who do not author full Dockerfiles:
			- Feature installs `srcr` binary (or relies on mise feature).
			- Feature accepts parameters: list of identities + refs, or path to bundled `srcr.toml` snippet.
			- Feature runs `srcr install` in feature install phase.
		- MVP constraint: config is **file-edited** — feature should ship a `srcr.toml` fragment or env-injected temp config, not mutate user's global dotfiles; run `srcr install`, not `srcr use`.
		- Phase 2: `srcr use github.com/org/lib` inside feature install enables one-line feature definitions and cache-friendly layers (see [[Person/codekiln/GitHub/sourcer/Project/Overview]] Phase 2).
	- ## Codespaces and CI parity
		- Same `srcr.toml` in repo root for:
			- local devcontainer,
			- GitHub Codespaces prebuild,
			- CI job that needs cross-repo `rg` before tests.
		- CI example:
			- ~~~yaml
			  - run: srcr doctor && srcr install && srcr status --json
			  - run: rg 'DeprecatedAPI' $(srcr where github.com/my-org/api-contracts)
			  ~~~
	- ## AI agent configuration inside containers
		- Pre-cloned corpus means agents need not hold git hosting credentials if network policy blocks outbound git.
		- Agent instructions reference identities, not paths:
			- "Before editing handlers, read `srcr where github.com/my-org/api-contracts`."
		- Phase 2: structured `srcr use … --json` for optional repos not baked into image (must match `[allow]` or `[sources]` with `install = false`).
		- Combines with overview goal: explicit structural boundaries for agents in [[DevContainer]] environments.
	- ## Networking and secrets
		- Image build needs clone credentials (SSH agent mount, PAT, or read-only deploy keys) **once** at build time.
		- Runtime agent without network: relies on baked corpus — aligns with access boundary.
		- Document pattern: separate **build secrets** from **runtime agent** profile.
	- ## Multi-root workspace
		- VS Code / Cursor `devcontainer.json` `workspaceFolder` stays primary repo.
		- Add folders via script reading `srcr list` paths, or document manual `folders` array using known layout:
			- `~/sources/github.com/my-org/api-contracts`
			- `~/sources/github.com/my-org/shared-go`
		- Future: `srcr vscode-folders --json` emitter for editor integration.
	- ## mise integration in containers
		- ~~~toml
		  # mise.toml inside devcontainer
		  [tools]
		  srcr = "1"
		  git = "latest"
		  [tasks.sources-install]
		  run = "srcr install"
		  ~~~
		- `postCreateCommand`: `mise install && mise run sources-install`
		- Keeps Sourcer version pinned like other dev tools.
	- ## Anti-patterns
		- Cloning ad hoc in `postCreateCommand` without `srcr.toml` — paths drift, access policy is unauditable.
		- Giving agents PAT with repo:all while also using Sourcer — bypasses the corpus boundary.
		- Baking secrets into `srcr.toml`; use build-args and secret mounts.
		- Relying on host-only paths in agent prompts — breaks Codespaces and fresh clones.
	- ## Long-term devcontainer directions (out of MVP)
		- Content-addressed image layers per source snapshot.
		- [[GitHub/Action]] publishing a feature proxy for a repo version.
		- Automatic `llms.txt` index generation over baked corpus for agent retrieval.
