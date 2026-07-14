logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Package Management]], [[Software/Composition/Analysis]], [[Dependency/Update/Automation]]

- # Lockfile
	- ## Overview
		- A **lockfile** is a generated, machine-written file that pins the exact version — and usually a hash or checksum — of every resolved dependency in a project, so the same dependency graph installs identically wherever the lockfile travels.
		- It closes the gap between a **manifest**, which declares *ranges* or *intent* (`>=2.0,<3.0`), and an **install**, which needs one concrete, reproducible set of artifacts.
	- ## Context
		- Manifests (`pyproject.toml`, `package.json`, `Cargo.toml`, [[mise/Config/mise.toml]]) describe what a project *wants*; lockfiles describe what a resolver actually *picked*, including transitive dependencies the manifest never names.
		- Lockfiles became standard as [[Package Management]] tooling matured — once a project's transitive graph grew deep enough, "whatever the resolver picks today" stopped being safe across machines, CI runs, and time.
		- A committed lockfile is also the artifact that makes a dependency graph auditable, which is why it shows up again in [[Software/Composition/Analysis]] and [[Dependency/Update/Automation]] workflows.
	- ## Key Principles
		- **Reproducibility** — the same lockfile, installed with a lock-respecting command, yields the same dependency set regardless of when or where it runs.
		- **Resolved, not declared** — a lockfile records concrete versions and per-entry integrity data for the *whole* graph, not just the direct dependencies a manifest lists.
		- **Manifest stays the source of intent** — a lockfile is derived from a manifest; regenerating it from an unchanged manifest and registry state should reproduce the same result.
		- **Committed, not ignored** — most ecosystems recommend checking the lockfile into version control so every contributor and CI run installs the same graph.
	- ## Mechanism
		- A resolver reads the manifest's constraints, walks the full dependency graph, and picks one consistent set of versions satisfying every constraint.
		- That resolution is serialized into the lockfile: exact version, source (registry, path, or Git ref), and an integrity hash or checksum per entry.
		- A later install can read the lockfile directly instead of re-resolving, skipping registry queries and graph search — the same property that makes locked installs faster also makes them deterministic.
		- A strict or frozen mode (`--locked`, `--frozen`, or an equivalent CI setting) fails the install instead of silently re-resolving when the manifest and lockfile have drifted apart.
	- ## Examples
		- [[mise]] — `mise lock` writes `mise.lock`, pinning tool versions, checksums, and per-platform download URLs; see [[Person/Jeff Dickey/Blog/26/03/02/Top 10 Features in Mise You're Not Using]]. [[mise/settings]]'s `--locked` flag (also `MISE_LOCKED=1` / `settings.locked=true`) fails an install when a tool has no pre-resolved URL in the lock for the current platform.
		- [[npm]] — `package-lock.json`, written by `npm install`; `npm ci` installs strictly from it and fails if it's out of sync with `package.json`.
		- [[uv]] — `uv.lock`, one project-wide lockfile; `uv sync` installs from it.
		- [[PyPoetry]] — `poetry.lock`; see [[PyPoetry/Concept/How to handle Monorepos in Poetry vs uv]] for how it compares to `uv.lock` in a monorepo.
		- [[cargo]] — `Cargo.lock`; applications check it in, while libraries often leave it out so downstream consumers resolve their own versions.
		- [[Nix]] — `flake.lock`, pinning the exact revision of every flake input, including [[Nix/Package/Registry]] itself, rather than just individual package versions.
	- ## Misconceptions
		- "A lockfile and a manifest are redundant" — **False**; the manifest states acceptable ranges, the lockfile states the one resolution actually chosen. Deleting the lockfile and reinstalling can silently change versions.
		- "Lockfiles are only for applications" — **Ecosystem-dependent**; library authors often skip committing one (e.g. `Cargo.lock` for a library crate) so consumers resolve against their own constraints, while applications and services almost always commit one.
		- "Any install command respects the lockfile" — **False**; only lock-aware commands (`npm ci`, `uv sync`, a `--locked`/`--frozen` flag) guarantee it — a plain "install" may still re-resolve and rewrite the lockfile.
