tags:: [[chezmoi/Docs]]

- # `run_once_` scripts in [[chezmoi]]
	- A script prefixed `run_once_` executes **once per unique rendered-content version**. chezmoi stores the SHA256 hash of each run in its state database; a script with previously-seen content is silently skipped, even if the filename changes.
	- ## State management
		- To force a re-run, clear the recorded state: `chezmoi state delete-bucket --bucket=scriptState`
		- For [[chezmoi/Template]] scripts, the content is hashed *after* template execution, so changing template data (e.g. `.chezmoidata`) that alters the rendered output counts as new content and triggers a re-run.
	- ## Timing variants
		- `run_once_before_` — runs before chezmoi updates target files; common for bootstrapping (e.g. installing a password manager before reading secrets)
		- `run_once_after_` — runs after chezmoi updates target files
	- ## Trade-off vs `run_onchange_`
		- `run_once_` is appropriate for one-time setup where re-running on every content change is undesirable.
		- If you want automatic re-execution whenever a plugin list or config file changes, use [[chezmoi/Script/run_onchange_]] instead.
	- See [[chezmoi/Script]] for full naming conventions and the `.chezmoiscripts/` directory.
