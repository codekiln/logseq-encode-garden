- # DVC for Knowledge Gardens
	- Use [[dvc]] to version large local assets and their conversion dependencies. Keep `assets/.remote` as a selectively populated working directory, with tracked DVC metadata outside that ignored directory. Publish approved media to named public objects whose URLs can appear directly in notes.
	- ## Storage
		- Each garden owns its DVC configuration, asset metadata, bucket or prefix, and credential scope. A clone obtains the graph and DVC metadata through Git; `dvc pull assets/example.wav.dvc` retrieves a selected asset, while `dvc pull` retrieves the assets represented by the current checkout. Files present in the bucket without DVC metadata require a separate object listing or mount. [DVC data discovery](https://doc.dvc.org/user-guide/data-management/discovering-and-accessing-data)
		- Public garden assets can use the existing `logseq-encode-garden` bucket after an authenticated configuration check. The private garden needs an `allPrivate` bucket for rough recordings and Ableton projects. B2 public access applies at bucket scope, so placing drafts under a private-looking prefix in a public bucket would expose the drafts. [Backblaze bucket access](https://www.backblaze.com/docs/cloud-storage-buckets)
		- Put DVC objects under `dvc/` and published objects under readable paths such as `gitpa/episodes/2026-09-25/GitP.26.09.25.mp3`. The disposable trial stored assets under `files/md5/<hash-prefix>/<hash-rest>` beneath the configured remote. A DVC cache is a content-addressed object store; a publication task must copy selected outputs to their named public paths.
		- Public release records should carry the source Git revision, DVC output hash, SHA-256, remote object key, public URL, content type, and length. Stable episode URLs require retaining the corresponding object. A changed release can receive a new object name so an existing RSS enclosure keeps referring to the same audio. [Backblaze download-by-name URLs](https://www.backblaze.com/apidocs/b2-download-file-by-name)
		- A private garden can retain source recordings and project manifests; the public encode garden can retain approved production notes and release metadata. The podcast website consumes the approved MP3 URL and episode content. Ableton migration needs an inventory of project files, referenced samples, and Collect All and Save dependencies before moving recordings into the private garden's storage.
	- ## Git metadata and local proxies
		- Ignore `/assets/.remote/` in Git. Put file sidecars at `assets/<name>.dvc`, with their output path relative to the sidecar: `.remote/<name>`. DVC-generated sidecars initially sit alongside their payload; moving a sidecar out of the ignored directory requires updating the output path. The trial exercised this arrangement successfully. [DVC sidecar format](https://doc.dvc.org/user-guide/project-structure/dvc-files)
		- Track `.dvc/config`, `.dvc/.gitignore`, `.dvcignore`, asset sidecars, `dvc.yaml`, and `dvc.lock`. Local caches and payloads remain Git-ignored. DVC records MD5 for the tested local files; a separate SHA-256 release manifest supports publication verification. A committed checksum identifies the intended file; remote status and a restore test establish whether the file is available.
		- Treat `assets/.remote` as DVC's local working directory when DVC owns an asset. A separate rclone mount can browse a bucket, but mounting over DVC outputs would join filesystem write-back and DVC cache operations in the same path. Ordinary editing, `dvc add`, and `dvc push` provide a clearer versioned workflow.
		- Explicit links to a hidden proxy path still need a Logseq rendering and Yazi search trial. Public notes can use permanent HTTP URLs. Private notes can use local proxy links and an asset-fetch task; private authenticated URLs need an access mechanism on each reading device.
	- ## B2 and remote authentication
		- Install the S3 extra, configure a garden remote, and use the bucket's actual S3 endpoint. The endpoint and remote prefix are non-secret project settings. DVC reads AWS credentials from the child process environment. [DVC S3-compatible remote configuration](https://doc.dvc.org/user-guide/data-management/remote-storage/amazon-s3)
			- ~~~sh
			  dvc remote add -d garden s3://GARDEN_BUCKET/dvc
			  dvc remote modify garden endpointurl https://ACTUAL_BUCKET_ENDPOINT
			  fnox --non-interactive --no-daemon --no-defaults --profile assets --if-missing error exec -- dvc push
			  fnox --non-interactive --no-daemon --no-defaults --profile assets --if-missing error exec -- dvc status -c
			  fnox --non-interactive --no-daemon --no-defaults --profile assets --if-missing error exec -- dvc pull assets/example.wav.dvc
			  ~~~
		- [[GitP/A/Log/26/10/04 Sun/Fnox/Plan]] supplies `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` through the per-garden `assets` profile. A persistent remote host needs its own decrypting identity; an ephemeral host needs an injected identity or vault service-account credential. SSH-agent forwarding alone does not give the proposed native age provider access to the private identity file.
		- Use a bucket-scoped application key and a prefix that covers the DVC remote. The S3 API requires an application key; the B2 primary key cannot authenticate S3 requests. B2 `writeFiles` also permits delete-by-name, so a read/list/write credential cannot enforce upload-only access. Retain object versions and use separate credentials for permanent version deletion. [Backblaze S3 application-key capabilities](https://www.backblaze.com/docs/cloud-storage-s3-compatible-app-keys)
		- Remote garbage collection needs its own retention policy covering every retained branch, tag, and garden sharing a remote. Deleting a local sidecar does not itself reclaim an object in B2. Make remote cleanup an explicit maintenance operation after restore checks. [DVC garbage collection](https://doc.dvc.org/command-reference/gc)
	- ## Disposable trial
		- On 2026-10-04, DVC `3.67.1` with its S3 extra ran in a temporary Python environment. The trial used a generated tone, FFmpeg, an isolated Git repository, and a local directory remote.
		- `dvc push` uploaded the WAV and MP3 to the local remote. `dvc status -c` reported the cache and remote in sync. A repeated `dvc repro` skipped the unchanged encoding stage.
		- A fresh Git clone contained metadata and omitted the WAV and MP3. A selective pull restored the WAV alone; a full pull then restored the MP3. Independent SHA-256 comparisons matched both restored files to the source files. `git check-ignore` identified both payloads as ignored, and `git ls-files` contained only DVC metadata and ignore files.
		- Changing the restored WAV caused `dvc status` to report the WAV sidecar's modified output and the encoding stage's modified dependency. This demonstrates change detection and dependency tracking for the local trial.
		- The WAV sidecar recorded MD5 `b5d15ccec25791b653addd81503aa5fb`; `dvc.lock` recorded the WAV dependency and MP3 output MD5 `6d90153353ad44d7ed449cd3bd16934e`. The remote keys were `files/md5/b5/d15ccec25791b653addd81503aa5fb` and `files/md5/6d/90153353ad44d7ed449cd3bd16934e`.
		- B2 transfer, unattended credential delivery, public URL publication, Logseq rendering, and complete Ableton project recovery remain to be exercised with a scoped test prefix and synthetic media.
	- ## Reproduce the local trial
		- These commands create a temporary repository and directory remote. They require `uv`, Python, Git, and FFmpeg. `DVC_SITE_CACHE_DIR` keeps DVC's system cache within the temporary trial directory.
			- ~~~sh
			  trial=$(mktemp -d /private/tmp/gitp-dvc-trial.XXXXXX)
			  UV_CACHE_DIR="$trial/uv-cache" uv venv "$trial/env"
			  UV_CACHE_DIR="$trial/uv-cache" uv pip install --python "$trial/env/bin/python" 'dvc[s3]==3.67.1'
			  export PATH="$trial/env/bin:$PATH"
			  export DVC_NO_ANALYTICS=true DVC_SITE_CACHE_DIR="$trial/site-cache"
			  mkdir "$trial/garden" "$trial/remote"
			  cd "$trial/garden"
			  git init
			  dvc init
			  dvc remote add -d garden "$trial/remote"
			  dvc config cache.type copy
			  mkdir -p assets/.remote
			  ffmpeg -hide_banner -loglevel error -f lavfi -i 'sine=frequency=440:duration=1' -c:a pcm_s16le assets/.remote/tone.wav
			  dvc add assets/.remote/tone.wav
			  python3 - <<'SIDE'
			  from pathlib import Path
			  src = Path('assets/.remote/tone.wav.dvc')
			  Path('assets/tone.wav.dvc').write_text(src.read_text().replace('path: tone.wav', 'path: .remote/tone.wav'))
			  src.unlink()
			  Path('.gitignore').write_text('/assets/.remote/\n')
			  SIDE
			  dvc stage add -n encode -d assets/.remote/tone.wav -o assets/.remote/tone.mp3 'ffmpeg -hide_banner -loglevel error -y -i assets/.remote/tone.wav -codec:a libmp3lame -b:a 128k assets/.remote/tone.mp3'
			  dvc repro
			  dvc push
			  dvc status -c
			  dvc repro
			  shasum -a 256 assets/.remote/tone.wav assets/.remote/tone.mp3 > "$trial/expected.sha256"
			  git check-ignore assets/.remote/tone.wav assets/.remote/tone.mp3
			  git add .dvc/config .dvc/.gitignore .dvcignore .gitignore assets/tone.wav.dvc dvc.yaml dvc.lock
			  git -c user.name='DVC prototype' -c user.email='prototype@example.invalid' commit -m 'Prototype DVC asset tracking'
			  git clone "$trial/garden" "$trial/fresh"
			  cd "$trial/fresh"
			  test ! -e assets/.remote/tone.wav
			  dvc pull assets/tone.wav.dvc
			  test ! -e assets/.remote/tone.mp3
			  dvc pull
			  shasum -a 256 -c "$trial/expected.sha256"
			  dvc unprotect assets/.remote/tone.wav
			  printf changed >> assets/.remote/tone.wav
			  dvc status
			  ~~~
	- ## Adoption
		- Run a synthetic asset round-trip through the intended B2 test prefix from the Mac and an unattended remote host. Verify selective pulls, credential failure messages, hash comparison, and recovery after clearing the local cache.
		- Pin DVC and FFmpeg in the garden's mise configuration before production pipelines. Put conversion commands and parameters under version control; DVC dependency hashes alone do not pin the encoder's implementation. [DVC pipeline definition](https://doc.dvc.org/user-guide/project-structure/dvcyaml-files)
		- Add shared asset entry points for inventory, fetch, add, push, status, and publication, with per-garden bucket configuration. A publication task verifies the MP3, uploads to its named release path, checks URL access and range requests, then updates the release manifest.
		- Inventory existing Git LFS paths before choosing migration candidates. Push and restore each migrated asset before removing its current storage representation; keep old Git LFS history available until its retention policy is settled.
		- Start Ableton migration with a complete collected project in private storage. Open the restored project on a clean location, verify sample dependencies, and compare rendered audio before expanding the migration.
