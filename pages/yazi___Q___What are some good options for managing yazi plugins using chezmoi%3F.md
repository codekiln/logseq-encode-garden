logseq-entity:: [[Logseq/Entity/question]]
via:: [[yazi/Plugin/fr.yazi]]

- # What are some good options for managing [[yazi]] plugins using [[chezmoi]]?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** The dominant pattern in highly-starred dotfiles repos is a `run_onchange_` chezmoi script that embeds a `sha256sum` of `package.toml` so chezmoi re-runs `ya pkg install` automatically whenever the plugin list changes.
			- **Option 1 — `run_onchange_` + `package.toml` hash (most idiomatic):**
				- Commit a `dot_config/yazi/package.toml` declaring plugins with pinned `rev` and `hash` values.
				- Add `.chezmoiscripts/run_onchange_install-yazi-plugins.sh.tmpl` with a hash comment so chezmoi detects changes:
					- ~~~bash
					  #!/bin/sh
					  # package.toml hash: {{ include "dot_config/yazi/package.toml" | sha256sum }}
					  ya pkg install
					  ~~~
				- chezmoi computes the hash at apply time; when `package.toml` changes, the script re-runs. Used by repos including `clay-coffman/dotfiles`, `iKadmium/dotfiles`, `german-molins/dotfiles`, `ninagrosse/dotfiles`.
				- `ninagrosse/dotfiles` adds a cleanup step before reinstalling: `rm -rf ~/.config/yazi/flavors && rm -rf ~/.config/yazi/plugins && ya pkg install`.
				- Numeric prefix on the script name (e.g. `run_onchange_after_75-install-yazi-packages.sh.tmpl`) controls ordering relative to other scripts (`german-molins/dotfiles`).
			- **Option 2 — `run_once_` with explicit plugin array (joelazar, 165 ★, highest-starred chezmoi+yazi repo):**
				- Plugin installation lives in `run_once_install_packages.sh.tmpl` alongside all other tooling.
				- A `scripts/utils_install` library defines `install_yazi_plugins` which: checks `ya` is available, runs `ya pkg upgrade`, then loops over a hardcoded `PLUGINS=()` array, calling `ya pkg list` before each `ya pkg add` to stay idempotent.
				- Git-clones theme [[Yazi/Flavor]] entries separately.
				- Trade-off: runs once on first setup; subsequent plugin changes require a manual re-run or script reset.
			- **Option 3 — Direct file vendoring (SwayKh/dotfiles, 153 ★):**
				- Plugin source directories (e.g. `compress.yazi/`, `full-border.yazi/`) are committed directly into `yazi/plugins/` and tracked in git.
				- No package manager invocation at apply time; plugins update only when you `git pull` or manually copy files.
				- A `package.toml` is still present for formal declaration but is not used at install time.
			- **Option 4 — `mise` as intermediate layer (TibiIius/dotfiles):**
				- [[yazi]] itself is installed via `mise` (declared in `config.toml.tmpl` under `[tools]`).
				- A chezmoi `run_onchange_` script delegates to `mise run yazi:install`, which calls `ya pkg install`.
				- Useful when you already manage tool versions with [[mise]].
			- **Option 5 — `run_onchange_before_` for full install including yazi (ulises-jeremias/dotfiles, 126 ★):**
				- `run_onchange_before_install-yazi.sh.tmpl` installs yazi itself (via pacman) and then calls `ya pkg add` for a small set of plugins.
				- Uses `before_` prefix so the script runs before other chezmoi operations.
				- Platform-gated with `{{- if eq .osid "linux-arch" -}}`.
			- **`package.toml` pinning (all serious configs):**
				- Pin both `rev` (git SHA) and `hash` (content hash) in `package.toml` for reproducibility — pattern used by Matt-FTW/dotfiles (747 ★, no chezmoi but the most elaborate yazi setup).
				- Example entry: `[plugins.yazi-plugin-name] \n git = "https://github.com/user/plugin.yazi" \n rev = "<sha>" \n hash = "<hash>"`
			- **Recommendation:** Option 1 (`run_onchange_` + `package.toml` sha256sum) is the most idiomatic chezmoi approach — declarative, automatically re-triggered, and `ya pkg install` is idempotent. Pair it with pinned `rev`/`hash` in `package.toml` for reproducibility.
			- Sources: [joelazar/dotfiles](https://github.com/joelazar/dotfiles), [clay-coffman/dotfiles](https://github.com/clay-coffman/dotfiles), [SwayKh/dotfiles](https://github.com/SwayKh/dotfiles), [ulises-jeremias/dotfiles](https://github.com/ulises-jeremias/dotfiles), [Matt-FTW/dotfiles](https://github.com/Matt-FTW/dotfiles)
