see-also:: [[Logseq/Entity/Asset/B2]], [[Asset/mise/Task/fetch]]

- # Asset Mount
	- A mount ties a folder of remote files in a garden checkout to the place they are stored and the URL they are published at. Pages will link a mounted file by relative path, `../assets/.remote/<mount>/<file>`, so Logseq shows it from disk. `mise run site:build` and gitpa's website and RSS builds will replace `../assets/.remote/<mount>/` with the mount's `public` base URL. Until the sub-issues of [#347 Link B2 assets by relative path and publish them as public URLs](https://github.com/codekiln/logseq-encode-garden/issues/347) land, pages link the B2 URL directly.
	- Each garden declares its mounts in `asset-mounts.toml` at its root. The file's first line is a comment linking this page.
	- ## Example
		- ~~~toml
		  [mounts.logseq-encode-garden]
		  path   = "assets/.remote/logseq-encode-garden"
		  bucket = "logseq-encode-garden"
		  dvc    = "garden"
		  public = "https://s3.us-east-005.backblazeb2.com/logseq-encode-garden"
		  ~~~
	- ## Keys
		- The table name under `mounts` is the mount's name. It matches the last folder of `path`.
		- `path`: the folder the files sit in, relative to the garden root, always `assets/.remote/<mount>`.
		- `bucket`: the B2 bucket that stores the files. Each file sits at the top level of the bucket and is named after its asset page, as [[Logseq/Entity/Asset/B2]] describes: the page `Course/Asset/Diagram/Overview/png` is stored as `Course___Asset___Diagram___Overview.png`.
		- `dvc`: the name of the DVC remote in `.dvc/config` that stores backups of the files. [[Asset/mise/Task/fetch]] restores a file from that remote.
		- `public`: the base URL a published page links instead of the mount folder, with no trailing slash. A file's public URL is `<public>/<file>`.
		- `source`: the ghq address of the garden that owns the files, such as `github.com/codekiln/logseq-encode-garden`.
	- ## Owning and borrowing gardens
		- A garden owns a mount when the mount's files live in that garden's B2 bucket and DVC remote. Its mount has `path`, `bucket` and `dvc`, and `public` when the bucket is public.
		- A garden that links another garden's files borrows the mount. Its mount has `path`, `public` and `source`, with the same `path` and `public` as the owning garden. When gitpa's [[Logseq/Entity/Proxy/Page/mise/Task/sync]] task copies a page that links into a mount, the task will also write that mount's borrowed declaration into the destination garden's `asset-mounts.toml`.
		- A mount without `public` is private. When a page links into a private mount, `mise run site:build` and gitpa's builds will stop and name the page and the file.
	- ## Validation
		- [mise-tasks/asset/lib/mounts.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/lib/mounts.py) reads `asset-mounts.toml` and stops with an error that links this page when a mount has an unknown key, lacks a key its role needs, mixes owning and borrowing keys, or has a `path` other than `assets/.remote/<mount>`. The `asset:*` tasks keep each file in the folder of the mount that has a `bucket`. `mise run site:build` will load the file through `mounts.py` once the sub-issues of [#347 Link B2 assets by relative path and publish them as public URLs](https://github.com/codekiln/logseq-encode-garden/issues/347) change them.
