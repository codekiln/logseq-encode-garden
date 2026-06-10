tags:: [[chezmoi/Docs]]

- # `run_` scripts in [[chezmoi]]
	- A script whose filename begins with `run_` (without `once_` or `onchange_`) executes **every time** `chezmoi apply` is run.
	- Use sparingly; prefer [[chezmoi/Script/run_onchange_]] or [[chezmoi/Script/run_once_]] to avoid unnecessary re-execution.
	- Must be idempotent — chezmoi makes no attempt to prevent duplicate side-effects.
	- See [[chezmoi/Script]] for naming conventions, timing modifiers, and the `.chezmoiscripts/` directory.
