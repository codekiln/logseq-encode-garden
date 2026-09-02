logseq-entity:: [[Logseq/Entity/Card]]

- # Bypass minimum_release_age for One Upgrade
	- [[mise]] [[mise/upgrade]]
		- **How do I upgrade a single [[mise/Tool]] to the newest release without waiting out [[mise/Config/Setting/minimum_release_age]]?** [[Card]]
			- Pass `--minimum-release-age 0s` and name the tool: `mise upgrade --minimum-release-age 0s claude-code`
			- A zero duration is special-cased to mean *no cutoff at all* — it does not mean "released 0 seconds ago". Without the tool name the bypass applies to everything outdated in that config.
			- The same flag exists on [[mise/install]], so `mise install claude-code@latest --minimum-release-age 0s` is the fresh-install equivalent.
			- [[My Notes]]
				- The flag is per-invocation and leaves [[mise/Config/mise.toml/Global]] alone. To skip the gate permanently for one tool, set `minimum_release_age_excludes = ["claude-code"]` in [[mise/Config/Setting]] instead.
				- In `src/install_before.rs`, `resolve_cli_minimum_release_age` turns a zero duration into a cutoff of `2099-01-01`, and the CLI flag arrives as the highest-precedence `before_date`, so it beats both the global setting and the built-in `24h` default for timestamped backends ([[mise/Backend/aqua]], [[mise/Backend/npm]], cargo, pipx, and some core plugins).
