logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Ableton/Live/Idea/Store-Ableton-in-the-Garden]]

- # Can [[DVC]] keep files with certain extensions in a different remote from the rest, so lossless audio goes to a private [[Backblaze/B2]] bucket?
	- ## [[AI Answer]]
		- **Short answer:** yes. An `outs` entry in a `.dvc` file can name its own `remote:`, and `dvc push`, `dvc pull` and `dvc fetch` then use that remote for that file and the default remote, `garden`, for every other file. DVC has no setting that picks a remote by extension, so `mise run asset:add` would write `remote:` into the `.dvc` file of each WAV, AIFF and FLAC file it tracks. [[Answer/Official]] from [.dvc Files](https://doc.dvc.org/user-guide/project-structure/dvc-files)
		- ### How DVC routes one file
			- The field sits beside the hash in the `.dvc` file. `dvc.yaml` stage outputs accept it too.
				- ~~~yaml
				  outs:
				  - md5: f94ac8fb418cf875ea34e36bd56f5074
				    size: 16
				    hash: md5
				    path: mix.wav
				    remote: private
				  ~~~
			- DVC 2.7.0 added the field in [#6486 dvcfile: support remote per output](https://github.com/treeverse/dvc/pull/6486), which says it is set by hand, with no CLI flag. DVC 3.49.0 made `-r` skip a file whose `remote:` names a different remote, in [#10365 sync: skip if remote doesn't match output remote](https://github.com/treeverse/dvc/pull/10365). The asset package pins DVC 3.67.1 in [mise-tasks/asset/pyproject.toml](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/pyproject.toml), so it has both.
			- `dvc push`, `dvc pull` and `dvc fetch` choose a remote from the file's `remote:` field first, then `-r`, then `core.remote`. [dvc push](https://doc.dvc.org/command-reference/push) · [dvc fetch](https://doc.dvc.org/command-reference/fetch)
				- With no `-r`, each routed file goes to or comes from its own remote, and the rest use `garden`.
				- With `-r garden`, routed files are skipped, so no `dvc push` command sends a file marked `remote: private` to the public bucket. The filter is `outs_filter` in [dvc/repo/fetch.py](https://github.com/treeverse/dvc/blob/3.67.1/dvc/repo/fetch.py#L62).
				- With `-r private` and no target, DVC also pushes every unrouted file to `private`, because `-r` replaces the default remote for those files. The asset tasks always pass a target.
			- `dvc gc -c` checks each routed file against its own remote and the other files against the default remote, and warns that files using the `remote` field may be deleted from a remote they aren't routed to. [dvc gc](https://doc.dvc.org/command-reference/gc) `dvc gc -w -c` cleans `garden` and each remote that a file in the workspace names, as `_merge_remote_obj_ids` in [dvc/repo/gc.py](https://github.com/treeverse/dvc/blob/3.67.1/dvc/repo/gc.py#L157) shows. A remote that no workspace file names is left alone.
			- `dvc status -c` ignores routed files. `_cloud_status` in [dvc/repo/status.py](https://github.com/treeverse/dvc/blob/3.67.1/dvc/repo/status.py#L96) skips every object that belongs to an output's own remote, so it reports `Cache and remote 'garden' are in sync.` while the private copy is missing. `dvc data status --not-in-remote` checks routed files against their own remote.
		- ### Choosing the remote by extension
			- `dvc remote` stores a URL, an endpoint, credentials and transfer settings for each remote, and nothing that matches paths, globs or extensions. `dvc add --remote` works only with `--to-remote`, which uploads a file straight to a remote, and it writes no `remote:` field.
			- The garden's `asset:add` therefore has to write the field. DVC 3.67.1 accepts it written either way:
				- After `dvc add`, append `remote: private` to the new `.dvc` file.
				- Before `dvc add`, write a `.dvc` file holding only `path` and `remote`. `dvc add` fills in the hash and size and keeps `remote:`. With this order a lossless file's `.dvc` file names the private remote from the moment it exists.
			- Running `dvc add` again on a changed file keeps its `remote:` field.
		- ### Credentials for each remote
			- `dvc(..., remote=True)` in [mise-tasks/asset/lib/assets.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/lib/assets.py#L63-L79) checks that the main checkout's encrypted `fnox.local.toml` holds `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for the `assets` profile. It removes every `AWS_` variable from the environment and runs DVC under `fnox --profile assets exec`. [fnox.toml](https://github.com/codekiln/logseq-encode-garden/blob/main/fnox.toml) reads both values from the garden's B2 key in 1Password.
			- `.dvc/config` sets no keys, so DVC's S3 client falls back to those environment variables, and every S3 remote in one DVC run uses the same key. A per-remote key set with `dvc remote modify --local` goes into `.dvc/config.local` as plain text, outside fnox. [Amazon S3 remote](https://doc.dvc.org/user-guide/data-management/remote-storage/amazon-s3)
			- A B2 application key can reach one bucket, a group of buckets or every bucket in the account. [Application Keys](https://www.backblaze.com/docs/cloud-storage-application-keys) That leaves two setups:
				- A key that reaches both buckets, in the `assets` profile. A plain `dvc push` then reaches both remotes. [[GitP/mise/Task/media/upload]] uses the same profile and picks its bucket from a single-bucket key: with a key for two buckets it stops and asks for `--bucket` on every upload. [b2_upload.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/gitpa/media/lib/b2_upload.py#L141-L146)
				- A second key, restricted to the private bucket, in its own fnox profile. The asset tasks run DVC for a private-mount file under that profile with `-r private`. If the `assets` key is restricted to the public bucket, a `dvc push` run under it stops with an access error on private files.
			- The second key fits better: `media:upload` keeps working as it does today, and the key that publishes files can't read the private ones.
		- ### A private mount
			- A second owned mount in `asset-mounts.toml`, with a matching remote in `.dvc/config`, would look like this. The bucket name is a placeholder.
				- ~~~toml
				  [mounts.logseq-encode-garden-private]
				  path   = "assets/.remote/logseq-encode-garden-private"
				  bucket = "logseq-encode-garden-private"
				  dvc    = "private"
				  ~~~
				- ~~~ini
				  ['remote "private"']
				      url = s3://logseq-encode-garden-private/dvc/
				      endpointurl = https://s3.us-east-005.backblazeb2.com
				  ~~~
			- The mount fits [[Asset/Mount]]'s rules: it has the owning keys `path`, `bucket` and `dvc`, and it has no `public`, so it is private. `mise run site:build` stops on any page that links into it, and the proxy page sync refuses to borrow it ([core.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/lib/core.py#L475-L476)). The `.gitignore` rules for `assets/.remote/` already cover its folder.
			- The asset tasks assume one owned mount. `owned_mount_folder()` in [assets.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/lib/assets.py#L46-L51) stops with `must declare one mount with a bucket` when two mounts have a bucket, so adding the mount stops every `asset:*` task until `assets.py` changes.
			- Each `.dvc` file is committed to this public repository, so the name, size and MD5 of every private recording stay public. Only the audio is private.
			- A login later would hand out short-lived links to files in this bucket, as [[Ableton/Live/Idea/Store-Ableton-in-the-Garden]] describes.
		- ### What a scratch test showed
			- On [[2026-11-26 Thu]] I ran DVC 3.67.1 from the asset package's virtual environment in a scratch repository with two local-folder remotes, `garden` as the default and `private`. `mix.mp3` had no `remote:` field, and `mix.wav` and `take.flac` had `remote: private`.
				- `dvc push` put the MP3 in `garden` and the WAV and FLAC in `private` only.
				- `dvc push -r garden` pushed only the MP3. `dvc push -r private` with no target put the MP3 in `private` too.
				- `dvc pull` in a fresh clone restored every file from its own remote. With the `private` folder moved away, it restored the MP3 and failed on the routed files only.
				- `dvc fetch -r garden` fetched only the MP3.
				- After `dvc remove take.flac.dvc`, `dvc gc -w -c -f` deleted the FLAC and the WAV's older version from `private` and left `garden` alone. After every routed file was removed, it left `private` untouched.
				- A WAV pushed to `garden` before it had `remote: private` was copied to `private` on the next push, and `dvc gc -w -c -f` then deleted the copy in `garden`.
				- With the private copy deleted, `dvc status -c` still reported the cache in sync with `garden`, and `dvc data status --not-in-remote` listed the WAV.
				- The stub `.dvc` file and the re-add described above kept `remote: private`.
		- ### Changes the asset tasks would need
			- TODO Create a private B2 bucket and an application key restricted to it, store the key in 1Password, and add a fnox profile for it beside `assets` in `fnox.toml`.
			- TODO Add the `private` remote to `.dvc/config` and the private mount to `asset-mounts.toml`.
			- TODO Update [[Asset/Mount]] for a garden that owns more than one mount: which owned mount an `asset:*` task writes to, and how a mount names its fnox profile. A new key, such as `fnox`, would need validation in [mounts.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/asset/lib/mounts.py).
			- TODO Replace `owned_mount_folder()` in `assets.py` with a lookup by format: WAV, AIFF and FLAC go to the owned mount without `public`, and every other format goes to the owned mount with `public`. `mounts.check_compressed` then refuses lossless audio only for a mount with `public`, and the `Uncompressed` test in `mise-tasks/asset/tests/test_assets.py` changes with it.
			- TODO In `asset:add`, write the stub `.dvc` file with the mount's `dvc` remote before running `dvc add` on a file in the private mount.
			- TODO In `asset:push` and `asset:fetch`, pass `-r` with the mount's remote and run DVC under the mount's fnox profile, with `dvc()` checking the fnox cache for that profile's keys.
			- TODO Add a test or lefthook check that every `.dvc` file in the private mount's folder names the private remote, and that every `.dvc` file for a WAV, AIFF or FLAC file has a `remote:` field.
			- TODO Point `asset:convert` at the WAV's new folder, and move the stage in `dvc.yaml` and the WAV files in `assets/.remote/logseq-encode-garden/` to the private mount.
			- TODO Use `dvc data status --not-in-remote` wherever a task checks that B2 holds a file, such as the offloading task on [[Ableton/Live/Idea/Store-Ableton-in-the-Garden]].
			- TODO Update [[Logseq/Entity/Asset/B2]] and [[Asset/mise/Task/add]] to say lossless audio goes to the private mount.
