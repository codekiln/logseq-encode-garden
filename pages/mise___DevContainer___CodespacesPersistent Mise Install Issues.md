logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]], [[mise]], [[DevContainer]]
see-also:: [[mise]], [[DevContainer]], [[GitHub/Codespace]], [[DevContainer/Hook/postCreateCommand]], [[mise/Tool/Explanation/When to Declare Tools]]
via:: [[2026-05-18 Mon]]
- # Persistent mise tool state in dev containers and Codespaces
	- ## Overview
		- [[mise]] installs real binaries into a **data directory** and activates them on `PATH` from project configuration (usually `mise.toml`). On a normal workstation that default layout is durable; in a **[[DevContainer]]** or **[[GitHub/Codespace]]**, the same model works but **storage semantics** differ.
		- Containers are disposable: some paths survive stop/start, others are recreated on **rebuild**. If mise's data directory lives in ephemeral storage, a rebuild can wipe Node, Python, `uv`, and other installs even though `mise.toml` still declares them—adding latency, network dependency, and an unpredictable dev loop.
		- The design question is not whether mise fits dev containers, but **where installed tool state lives** relative to the container's persistence boundary.
	- ## Context
		- Locally, mise typically stores tools under something like `~/.local/share/mise` and switches versions per project without extra ceremony.
		- A dev container configuration usually separates two jobs: **declare** what the environment should contain, and **materialize** those things at the right lifecycle phase. mise is strong at the first (declarative `[tools]` pins); the second is **installed state**—downloads and builds under `MISE_DATA_DIR` (or the default data path).
		- **[[GitHub/Codespace]]** makes the issue visible because `/workspaces` is a well-known **persistent** mount for the repo and adjacent workspace data, while much of the rest of the filesystem may not survive rebuild the same way.
	- ## Key Principles
		- **Configuration ≠ installed state.** `mise.toml` (and friends) say *which* tools; mise still has to download or build them into its data directory.
		- **Persistence is explicit.** Treat expensive, project-derived installs as state that must survive rebuilds—either on a platform-persistent path (e.g. under `/workspaces` in Codespaces) or on a **named volume** in generic devcontainer setups.
		- **`MISE_DATA_DIR` sets the store; lifecycle hooks populate it.** Pointing the variable at durable storage does not install tools by itself; hooks such as **[[DevContainer/Hook/postCreateCommand]]** running `mise install` converge the environment after the workspace is available.
		- **Install location and shell activation are separate.** Where binaries live (`MISE_DATA_DIR`) is distinct from whether `node`, `python`, etc. resolve to mise-managed versions (`mise activate` in shell startup).
		- **Image vs project layers.** A common split: bake **mise** (or a devcontainer feature) into the image; let **project tool versions** stay declarative in `mise.toml` and install at create time into persistent storage—avoid baking every project runtime into the image unless you accept version drift from the declarative source of truth.
	- ## Mechanism
		- **Default vs persistent paths.** Default data under `/home/vscode/.local/share/mise` may be lost on rebuild; the same tree under `/workspaces/.local/share/mise` is more likely to survive Codespaces rebuilds because `/workspaces` is the central durable workspace mount.
		- **Controlling the store.** mise honors `MISE_DATA_DIR`; installs then land under that path (e.g. `…/installs`). Pair `containerEnv` with a lifecycle command that runs `mise install` once `mise.toml` is on disk.
		- **Lifecycle placement.** **[[DevContainer/Hook/postCreateCommand]]** is a good default for `mise install`: the source tree and devcontainer config exist, and the command can read pins and write binaries into the configured data directory.
		- **Codespaces path vs named volume.** `/workspaces/.local/share/mise` is simple and human-inspectable in Codespaces but is a **platform convention**, not universal. A devcontainer-spec pattern mounts an explicit volume (e.g. `${devcontainerId}-mise-data` → `/mise-data`) and sets `MISE_DATA_DIR=/mise-data` for portability at the cost of visibility from the repo tree.
		- **What stays in the image.** The substrate provides OS, mise itself, a **persistent store location**, lifecycle hooks, and shell activation; project runtimes flow from `mise.toml` into that store rather than only into disposable container layers.
	- ## Examples
		- **Codespaces-oriented** (persistent under `/workspaces`):
			- ~~~json
			  {
			    "containerEnv": {
			      "MISE_DATA_DIR": "/workspaces/.local/share/mise"
			    },
			    "postCreateCommand": "mise install"
			  }
			  ~~~
		- **Portable devcontainer** (explicit volume):
			- ~~~json
			  {
			    "mounts": [
			      "source=${devcontainerId}-mise-data,target=/mise-data,type=volume"
			    ],
			    "containerEnv": {
			      "MISE_DATA_DIR": "/mise-data"
			    },
			    "postCreateCommand": "mise install"
			  }
			  ~~~
		- **Declarative pins** (configuration only; installs still require `mise install` + durable `MISE_DATA_DIR`):
			- ~~~toml
			  [tools]
			  node = "24"
			  python = "3.12"
			  uv = "latest"
			  ~~~
	- ## Misconceptions
		- **"mise doesn't work in dev containers."** False—the failure mode is **ephemeral install cache**, not incompatibility.
		- **"Setting `MISE_DATA_DIR` is enough."** False without an idempotent install step; an empty persistent directory should still converge via `mise install`.
		- **"Persistent cache replaces authoritative config."** Dangerous if the environment only works because of stale binaries outside the repo; keep `mise.toml` authoritative and treat durable storage as an **optimization**, not a hidden second source of truth—same class of risk as other package-manager caches and named Docker volumes.
