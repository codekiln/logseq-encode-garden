logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: asset:convert
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/codex/dvc-asset-tasks/mise-tasks/asset/convert
- # Convert a Tracked WAV to MP3
	- Registers a DVC conversion stage and rebuilds its MP3 when the WAV or preparation code changes.
	- ## Invocation
		- Run from the garden checkout. The page argument is its logical name, without wikilink brackets.
			- ~~~sh
			  mise run asset:convert -- Course/Asset/Audio/Lesson/wav Course/Asset/Audio/Lesson/mp3
			  ~~~
		- [[Logseq/Entity/Asset]] defines page-derived filenames and valid names.
	- ## Files and access
		- Creates `dvc.yaml`, `dvc.lock` and the working MP3. Later runs reproduce the stage. DVC restores pipeline outputs using the same fetch task.
		- Mise supplies Python, uv and FFmpeg; the asset package pins DVC and its S3 client. The Git checkout supplies `.dvc/config` and the `assets` fnox profile. Linked worktrees use the main checkout’s encrypted fnox cache.
		- Commit adjacent `.dvc` metadata for added assets and `dvc.yaml` plus `dvc.lock` for conversions. Working recordings stay ignored under `assets/.remote/`.
	- ## Recovery and help
		- A missing input needs adding or fetching before conversion. An invalid asset name needs correction according to [[Logseq/Entity/Asset]]. Storage authentication needs refreshing the garden’s fnox cache.
		- ~~~sh
		  mise run asset:convert --help
		  ~~~
