logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: asset:status
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/codex/dvc-asset-tasks/mise-tasks/asset/status
- # Inspect an Asset Backup
	- Reports whether a selected working file matches its DVC metadata and whether its content is in the local cache.
	- ## Invocation
		- Run from the garden checkout. The page argument is its logical name, without wikilink brackets.
			- ~~~sh
			  mise run asset:status -- GitP/A/Session/26/09/24-Thu/Asset/Synth/Full/mp3
			  ~~~
		- [[Logseq/Entity/Asset]] defines page-derived filenames and valid names.
	- ## Files and access
		- Reads local DVC metadata, cache and working file. Remote availability is verified by fetch or push.
		- Mise supplies Python, uv and FFmpeg; the asset package pins DVC and its S3 client. The Git checkout supplies `.dvc/config` and the `assets` fnox profile. Linked worktrees use the main checkout’s encrypted fnox cache.
		- Commit adjacent `.dvc` metadata for added assets and `dvc.yaml` plus `dvc.lock` for conversions. Working recordings stay ignored under `assets/.remote/`.
	- ## Recovery and help
		- A missing input needs adding or fetching before conversion. An invalid asset name needs correction according to [[Logseq/Entity/Asset]]. Storage authentication needs refreshing the garden’s fnox cache.
		- ~~~sh
		  mise run asset:status --help
		  ~~~
