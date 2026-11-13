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
		- `public`, with `--public`: the HTTP status of a HEAD request to the file's public URL, or `private` for a mount with no `public` line.
	- A summary line on stderr gives the totals.
	- ## Invocation
		- Run from the garden checkout.
			- ~~~sh
			  mise run asset:report > report.tsv
			  mise run asset:report --public > report.tsv
			  ~~~
	- ## Files and access
		- Reads `asset-mounts.toml`, the page files and `assets/.remote/`. [[Asset/Mount]] documents the mount file.
		- `--public` sends one HEAD request per file over HTTPS and needs no B2 credentials.
		- A linked worktree has no local copies, so run it in the main checkout to see which files are restored there.
