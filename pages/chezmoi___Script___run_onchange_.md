tags:: [[chezmoi/Docs]]

- # `run_onchange_` scripts in [[chezmoi]]
	- A script prefixed `run_onchange_` re-executes only when its **rendered content** has changed since the last successful run. chezmoi tracks the SHA256 hash of the rendered script body.
	- ## Triggering re-runs from external files
		- Embed a hash comment referencing another file so chezmoi detects changes to that file even though it is not the script itself:
			- ~~~bash
			  #!/bin/sh
			  # package.toml hash: {{ include "dot_config/yazi/package.toml" | sha256sum }}
			  ya pkg install
			  ~~~
		- This is the canonical [[yazi]] plugin management pattern: when `package.toml` changes, chezmoi recomputes the hash, detects the script content has changed, and re-runs `ya pkg install`.
	- ## Ordering
		- Scripts execute alphabetically by filename. A numeric prefix (e.g. `run_onchange_after_75-install-yazi-packages.sh.tmpl`) controls position relative to other scripts.
	- ## Timing variants
		- `run_onchange_before_` — runs before chezmoi updates target files
		- `run_onchange_after_` — runs after chezmoi updates target files
	- ## Comparison
		- Re-triggers automatically whenever content changes — unlike [[chezmoi/Script/run_once_]], which will not re-run if the same content has already been seen.
	- See [[chezmoi/Script]] for full naming conventions and the `.chezmoiscripts/` directory.
