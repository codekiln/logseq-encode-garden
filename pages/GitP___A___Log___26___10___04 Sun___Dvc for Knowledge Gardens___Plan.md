- # DVC for Knowledge Gardens
	- Use `assets/.remote/` for named local working files and the `.dvc` files that describe them. Git stores the `.dvc` metadata; DVC restores selected working files from B2. Public episode URLs refer to separately published objects with stable names.
	- The layout has passed a disposable B2 trial. Registering the first asset in the garden and adding the mise tasks are the next actions under Put the layout to work.
	- ## A recording and its metadata
		- The September 24 MP3 uses this layout:
			- ~~~text
			  assets/.remote/GitP/Session/2026/09/24/
			    GitP.26.09.24.mp3       # working audio, ignored by Git
			    GitP.26.09.24.mp3.dvc   # path and checksum, committed to Git
			  ~~~
		- `dvc add assets/.remote/GitP/Session/2026/09/24/GitP.26.09.24.mp3` creates the adjacent `.mp3.dvc` file. Inside that metadata, `path: GitP.26.09.24.mp3` means the MP3 beside the `.dvc` file. [DVC's file format](https://doc.dvc.org/user-guide/project-structure/dvc-files) defines paths relative to the metadata file's directory.
		- A fresh clone contains `assets/.remote/GitP/Session/2026/09/24/GitP.26.09.24.mp3.dvc`. Running `dvc pull assets/.remote/GitP/Session/2026/09/24/GitP.26.09.24.mp3.dvc` restores `assets/.remote/GitP/Session/2026/09/24/GitP.26.09.24.mp3`. Running `dvc pull` restores all assets described by the checkout's DVC metadata. [DVC pull targets](https://doc.dvc.org/command-reference/pull) explains selecting one asset.
		  id:: 6ac23ac7-9313-45ac-8535-5e04bba58aa2
	- ## What Git stores
		- Commit the adjacent `.dvc` files and `.dvc/config`. DVC's generated `.dvc/.gitignore` excludes its local cache and runtime files. Pipeline definitions and their result checksums belong in `dvc.yaml` and `dvc.lock` when a conversion pipeline is added.
		- The garden's ignore rules allow DVC metadata anywhere beneath `assets/.remote/` while excluding the working files:
			- ~~~gitignore
			  /assets/.remote/**
			  !/assets/.remote/**/
			  !/assets/.remote/**/*.dvc
			  ~~~
		- The directory exception lets Git reach nested metadata. The `.dvc` exception makes the metadata eligible for commit. `git add assets/.remote/GitP/Session/2026/09/24/GitP.26.09.24.mp3.dvc` stages the metadata; the MP3 remains ignored.
	- ## What B2 stores
		- Configure the DVC remote as `s3://logseq-encode-garden/dvc/` with endpoint `https://s3.us-east-005.backblazeb2.com`. DVC stores file content beneath that prefix using checksum-derived names such as `dvc/files/md5/<first-two-characters>/<remaining-characters>`.
		- DVC reads the checksum in the `.dvc` file to find the B2 object, downloads it to its local `.dvc/cache/`, and restores the named file under `assets/.remote/`. The local path and B2 object name serve different purposes: the local path identifies the recording; the storage name identifies its contents.
		- `assets/.remote/` contains the files selected for the current checkout. DVC can list and retrieve files represented by that checkout's metadata. Browsing arbitrary existing B2 objects requires the B2 client; those objects gain DVC tracking only when explicitly added or imported.
		- [[GitP/A/Log/26/10/04 Sun/Fnox/Plan]] supplies the garden's B2 credentials from the encrypted cache on the Mac. [DVC's compatible-server settings](https://doc.dvc.org/user-guide/data-management/remote-storage/amazon-s3#s3-compatible-servers-non-amazon) describes using a Backblaze endpoint with the S3 client.
	- ## Public episode audio
		- The [September 24 podcast MP3](https://f005.backblazeb2.com/file/logseq-encode-garden/gitpa/episodes/2026-09-24/GitP.26.09.24.mp3) is published at `gitpa/episodes/2026-09-24/GitP.26.09.24.mp3`. Listeners and RSS use that stable URL.
		- A publication task copies the chosen local MP3 to its named release object and verifies the public URL. `dvc push` uploads versioned DVC content under `dvc/`; publishing gives the approved episode a permanent audience-facing URL.
		- The public garden tracks approved media. Rough recordings and collected Ableton projects belong to the private garden's private bucket. Each garden uses the same local path convention with its own B2 credentials and DVC remote.
	- ## Tested layout
		- On [[2026-10-04 Sun]], DVC restored the prepared September 24 MP3 from B2 into a fresh Git clone using the adjacent `.dvc` file under `assets/.remote/`. The restored file's SHA-256 matched the original prepared MP3.
		- The fresh clone contained metadata and omitted the audio. Pulling the September 24 metadata restored only that MP3; a full pull restored the other test asset. Git tracked the `.dvc` files and ignored the working files throughout.
		- The trial used the garden's cached credentials and a unique B2 prefix under `dvc/layout-trials/`. All trial objects were removed afterward. The original prepared recording and existing public MP3 were left in place.
	- ## Put the layout to work
		- TODO Add garden asset mise tasks for `add`, `fetch`, `push`, and `status`, using [the tested fnox assets profile](https://github.com/codekiln/logseq-encode-garden/blob/main/fnox.toml). `add` takes a local recording path and produces its adjacent `.dvc` file; `fetch` takes that `.dvc` path and restores its recording.
		- TODO Initialize DVC in the garden, configure the B2 remote described under What B2 stores, and register [the approved September 24 MP3](https://f005.backblazeb2.com/file/logseq-encode-garden/gitpa/episodes/2026-09-24/GitP.26.09.24.mp3) under the exact local path shown under A recording and its metadata. Commit its metadata after upload and restore succeed.
		- TODO Track a WAV-to-MP3 conversion using [the garden media preparation task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/gitpa/media/prepare), with input and output paths under `assets/.remote/`. Verify that changing the WAV requires rebuilding its MP3.
		- TODO Restore a collected Ableton project into a clean location in the [private knowledge garden](https://github.com/codekiln/logseq-garden) and open the set before migrating more recordings.
