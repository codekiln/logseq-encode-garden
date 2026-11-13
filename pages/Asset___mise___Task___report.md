logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: asset:report
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/report
- # List Linked B2 Files
	- Prints one row per file that a page in `pages/` or `journals/` links into a mount declared in `asset-mounts.toml`, as tab-separated columns:
		- `mount` and `file`: the mount the link points into and the file name, with `%20` decoded.
		- `pages`: how many pages link the file.
		- `form`: `public` when pages link the mount's public URL, `relative` when they link `../assets/.remote/<mount>/<file>`, and `both` when pages use both.
		- `pointer`: whether `assets/.remote/<mount>/<file>.dvc` exists, so [[Asset/mise/Task/fetch]] can restore the file.
		- `local`: whether the file itself sits in `assets/.remote/<mount>/`.
		- `space`: whether the file name has a space. A `yes` marks a file that needs a copy with a hyphen in place of each space, the naming rule [[Logseq/Entity/Asset]] describes.
		- `public`, with `--public`: the HTTP status the file's public URL returns to a HEAD request, such as `200` or `404`. The column shows `private` for a mount whose entry in `asset-mounts.toml` has no `public` URL, and `error` when the request gets no answer.
	- The task writes totals to stderr: how many files pages link, and how many of them have a DVC pointer, a local copy or a space in the name. With `--public` it also counts the files whose public URL answered `200`.
	- ## Invocation
		- Run from the garden checkout.
			- ~~~sh
			  mise run asset:report > report.tsv
			  mise run asset:report --public > report.tsv
			  ~~~
	- ## Files and access
		- Reads `asset-mounts.toml`, the page files and `assets/.remote/`. [[Asset/Mount]] documents the mount file.
		- With `--public`, the task sends a HEAD request to each file's public URL. The public URLs need no B2 credentials.
		- The task looks for local copies in the checkout it runs from. A linked git worktree holds no downloaded B2 files, so there every row says `no` under `local`; run the task from the main checkout to see which files are on disk.
