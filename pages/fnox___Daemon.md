tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[fnox/Golden Path]]

- # [[fnox]] daemon
	- ## Overview
		- The **daemon** is an opt-in background process that keeps resolved secrets in memory for a user session. When a config points at remote providers such as [[1Password]], Bitwarden, AWS Secrets Manager or Vault, it spares repeated `fnox get`, `fnox exec` and shell-hook refreshes a provider round trip.
		- Upstream describes it in [Cache secrets in memory](https://fnox.jdx.dev/guide/daemon.html). Both the guide and the source were read from a local clone of [jdx/fnox](https://github.com/jdx/fnox) at commit `03e9aee` (2026-10-01).
	- ## Context
		- It is the in-memory counterpart to the encrypted on-disk cache of the [[fnox/Golden Path]]. The daemon writes nothing to disk and loses its contents when it stops; `fnox sync --local-file` survives restarts and works offline.
		- Unix only. It listens on a Unix domain socket, never TCP, and checks that each client belongs to the same user. Other platforms get an "unsupported" error; `--no-daemon` or `FNOX_DAEMON=off` forces direct resolution.
	- ## Key Principles
		- Off unless enabled. fnox ignores the daemon until `[daemon] enabled = true` is in config or `FNOX_DAEMON=on` is set.
		- A cache hit skips the provider. A miss resolves the secret and stores it in memory.
		- Interactive clients resolve a miss in their own terminal, then hand the value to the daemon. Authentication that needs a terminal, such as a FIDO2 PIN and key touch, stays attached to that terminal. Explicitly non-interactive clients let the daemon resolve misses, and never prompt.
		- Nothing invalidates a cached value when the remote secret changes. Run `fnox daemon clear` after changing a secret at its source.
	- ## Mechanism
		- Enable it with a top-level section in `fnox.toml`:
			- ~~~toml
				[daemon]
				enabled = true
				idle_timeout = "8h"
				~~~
		- Supported read commands start the daemon on demand. It can also be managed directly: `fnox daemon start`, `status`, `clear`, `stop`.
		- Commands that use it: `exec`, `get`, `hook-env`, `export`, `list --values`, `check --all`, `tui`, `mcp`, `proxy run`, `ci-redact`. Commands that change things still resolve directly: `sync`, `reencrypt`, `edit`, `set`, `remove`, `provider`, `lease create`.
		- `fnox check --all` connects to the daemon but never reuses cached values, so it still validates against the providers.
		- Cached values are discarded on `fnox daemon clear`, `fnox daemon stop`, the idle timeout (default `8h`), or a change to the config files, profile, provider references, post-processing options, or relevant `FNOX_*` and provider environment variables.
		- Opt out per secret or per provider with `daemon_cache = false`:
			- ~~~toml
				[secrets]
				PAYMENT_API_KEY = { provider = "op", value = "Payments/api-key", daemon_cache = false }

				[providers.op]
				type = "1password"
				vault = "Engineering"
				daemon_cache = false
				~~~
		- Skip it for one call with `fnox --no-daemon get DATABASE_URL`, or for a session with `export FNOX_DAEMON=off`.
	- ## Examples
		- Check what is running: `fnox daemon status`
		- Force a refresh after rotating a secret in [[1Password]]: `fnox daemon clear`
	- ## Misconceptions
		- It is not a replacement for the sync cache. It does not survive a reboot or help offline.
		- It is not per directory. The socket path depends on the profile, `--no-defaults`, `--if-missing` and the age key file, not on the project, so shells in different projects reach the same daemon.
		- Sharing the daemon is not the same as sharing cached values. Each cache key hashes the full path and contents of every config file in play. Two [[Git/Worktree]] checkouts of one repo have different absolute paths, so by this reading of the source they would not hit each other's entries even with identical config. Upstream documents neither case, and this has not been run.
