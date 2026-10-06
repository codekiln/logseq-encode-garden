logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: gitpa:media:upload
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/codex/fnox-media-upload/mise-tasks/gitpa/media/upload
see-also:: [[Logseq/Entity/Asset/B2]], [[GitP/A/Log/26/10/04 Sun/Fnox/Plan]]
- # Upload a Garden Asset
	- Uploads a prepared file under the flat filename derived from its existing B2 asset page. Repeated runs verify matching stored content and return its usable URL.
	- ## Invocation
		- Run from the garden checkout:
			- ~~~sh
			  mise run gitpa:media:upload -- '/path/to/prepared.mp3' 'GitP/A/Session/26/09/24-Thu/Asset/Synth/Full/mp3'
			  ~~~
		- `--verify-only` requires an existing object and performs no upload. `--bucket` selects a permitted bucket when the application key allows several buckets or is unrestricted.
	- ## Inputs and outputs
		- The local file extension must match the page's final format segment. The page must exist directly under `pages/` and declare [[Logseq/Entity/Asset/B2]]. Filename mapping follows [[Logseq/Entity/Asset]]; the bucket object uses that filename at its root.
		- MP3, WAV, FLAC, Ogg and video formats are checked with ffprobe. Images, PDFs and MIDI have format-signature checks; MicroFreak `.mfpz` files have ZIP integrity checks. Other extensions use their registered MIME type or `application/octet-stream` and full-file checksum verification.
		- Success establishes matching B2 SHA-1, length and MIME metadata plus a matching SHA-256 from a complete download. The task prints the verified URL. Public buckets are downloaded without authentication; private objects require garden B2 authentication to use the URL.
	- ## Side effects
		- Creates a named B2 object when absent. Conflicting content, hidden versions or media metadata stop the task. Matching existing objects are downloaded and verified without creating another version.
		- Asset pages and their tags remain unchanged. Add the verified URL to the asset page after a successful run. Website and podcast publication remain separate steps.
		- Keep uploads to the same object serialized across hosts. B2 Native uploads lack an atomic create-if-absent condition; the task checks immediately before upload but another host can write during that interval.
	- ## Dependencies and access
		- Mise supplies Python and FFmpeg/ffprobe. The helper uses Python's standard library and Backblaze's Native API.
		- Fnox runs from the registered garden checkout with the `assets` profile, daemon disabled and noninteractive authentication. Linked worktrees use that checkout's encrypted `fnox.local.toml`; a missing or incomplete cache stops execution before vault lookup. The target page is read from the worktree running the task.
		- The key needs list/read permissions and bucket lookup permission; uploading also needs write permission. The key's allowed bucket and filename prefix are checked before upload. A key scoped to one bucket supplies the default destination.
	- ## Failure and recovery
		- Missing cache: create or refresh the garden's cache while vault authentication is available, following [[fnox/Golden Path]]. Ordinary transfers use the cache while the Mac is unattended.
		- Conflicting destination: retain the existing object and choose the correct asset page or compare source files before a separate replacement decision.
		- Failed verification after upload: retain the source, inspect the named object, and retry verification. The task does not delete remote versions during recovery.
		- Oversized files: use a multipart-capable transfer for files beyond the Native single-upload limit.
	- ## Source and help
		- [Fnox upload file task](https://github.com/codekiln/logseq-encode-garden/blob/codex/fnox-media-upload/mise-tasks/gitpa/media/upload) and [B2 Native upload API](https://www.backblaze.com/apidocs/b2-upload-file).
		- ~~~sh
		  mise run gitpa:media:upload --help
		  python3 -m unittest discover -s mise-tasks/gitpa/media/lib
		  ~~~
