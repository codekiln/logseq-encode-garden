logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: asset:add
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/codex/dvc-asset-tasks/mise-tasks/asset/add
- # Track a Local Asset
	- Copies a source file into `assets/.remote/` using the filename derived from its asset page, then creates adjacent `.dvc` metadata.
	- ## Invocation
		- Run from the garden checkout. The page argument is its logical name, without wikilink brackets.
			- ~~~sh
			  mise run asset:add -- /path/to/lesson.wav Course/Asset/Audio/Lesson/wav
			  ~~~
		- [[Logseq/Entity/Asset]] defines page-derived filenames and valid names.
	- ## Files and access
		- Creates a working copy and metadata. An existing working copy is updated by passing that same working path as SOURCE; a different source cannot replace it.
		- Mise supplies Python and uv; the asset package pins DVC and its S3 client. The Git checkout supplies `.dvc/config` and the `assets` fnox profile. Linked worktrees use the main checkout’s encrypted fnox cache.
		- Commit adjacent `.dvc` metadata for added assets and `dvc.yaml` plus `dvc.lock` for conversions. Working recordings stay ignored under `assets/.remote/`.
	- ## Recovery and help
		- A missing input needs adding or fetching before conversion. An invalid asset name needs correction according to [[Logseq/Entity/Asset]]. Storage authentication needs refreshing the garden’s fnox cache.
		- ~~~sh
		  mise run asset:add --help
		  ~~~
