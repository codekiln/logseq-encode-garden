see-also:: [[Ableton/Live/Idea/Store-Ableton-in-the-Garden/Plan/Discussion]]

- [[2026-11-28 Sat]]
	- [[AI/Response]] from [[Anthropic/Model/Claude/5/5/Opus]]
		- Plan for keeping whole Live projects in this garden under `assets/Ableton/Project/`, carrying out the recommendation on [[Ableton/Live/Idea/Store-Ableton-in-the-Garden]]. Sets and presets go in git as XML through a clean/smudge filter. Each project's `Samples/` folder goes to a new private [[Backblaze/B2]] bucket, `logseq-encode-garden-private`, through [[dvc]]. Rendered MP3s and images stay asset pages in the public bucket, `logseq-encode-garden`, as [[Logseq/Entity/Asset/B2]] describes.
		- ## Storage by file
			- Git, through the `ableton` filter, stored as XML: `.als` Sets, `.alc` clips, `.adg` rack presets and `.adv` device presets. All four are gzip-compressed XML; one factory `.adv` uses Live's binary format, and `gzip -dcf` passes it through unchanged.
			- Git, as is: `.agr`, `.ask` and `.xmp` files. Some `.agr` grooves are binary, so they stay out of the filter.
			- DVC, private bucket: the `Samples/` folder of each project, as one directory output whose `.dvc` file names `remote: private`. Recordings on this Mac are `.aif`, so this covers every audio format.
			- DVC, public bucket: MP3s, PNGs and other published outputs, through the existing `asset:*` tasks and the `logseq-encode-garden` mount.
			- Ignored: `Backup/` (git history replaces Live's timestamped copies), `*.asd` analysis files, which Live rebuilds, and the macOS `Icon\r` file.
		- ## Project folder convention
			- A project documents one garden page, its owner, such as a session `GitP/A/Session/26/11/06-Fri` or a template `GitP/A/Template/LPP-Seq`. The folder name is the owner's page name written the way [[Logseq/Entity/Asset]] writes file names: `___` for each `/` and hyphens for spaces.
				- ~~~
				  assets/Ableton/Project/GitP___A___Session___26___11___06-Fri/
				    .gitignore                              /Samples, /Backup, *.asd, Icon?
				    GitP___A___Session___26___11___06-Fri___Set.als       -> GitP/A/Session/26/11/06-Fri/Set
				    GitP___A___Session___26___11___06-Fri___Set___Alt.als -> GitP/A/Session/26/11/06-Fri/Set/Alt
				    Presets/                                .adg and .adv, filtered
				    Samples.dvc                             remote: private
				    Samples/                                Recorded, Processed, Imported (ignored by git)
				  ~~~
			- A Set file's name maps back to its Set page by turning `___` into `/`. The main Set is `<owner>___Set.als`; another Set in the same project adds a name, `<owner>___Set___<Name>.als`.
			- `mise run ableton:set:import --als <file> --performance '<owner>'` already writes `<owner>/Set` and its `<owner>/Set/Track/...` pages per [[Logseq/Entity/Ableton/Set]]. Its `source::` property would hold the Set's path from the repository root, so a reader can open the file from the page.
			- A Set page names its file in `source::` as text. A Markdown link to a git-tracked `.als` under `assets/` would make [[Logseq/Entity/Proxy/Page/mise/Task/sync]] copy the gzip working file into gitpa.
			- Live saves only into the primary checkout. A linked worktree holds the Sets but no `Samples/`, so an agent can edit a Set's XML on a branch and the PR shows the diff.
		- ## Experiment results
			- Run on [[2026-11-28 Sat]] in [codekiln/making-music](https://github.com/codekiln/making-music) (private), tracked in [making-music#1 Experiments for keeping Live projects in git and DVC](https://github.com/codekiln/making-music/issues/1).
			- ### Home-swap filter
				- [making-music#2 Clean/smudge filter that swaps the home folder](https://github.com/codekiln/making-music/issues/2): on the LPP-Seq and Pattern A and B templates and two session Sets, clean then smudge gave back Live's XML unchanged. Clean twice changed nothing, two clones wrote the same `.als`, and a clone with another `$HOME` got that home folder in every path.
				- After clean, no username was left in the four Sets. Before clean they held it on 48, 0, 274 and 463 lines, all in `FileRef/Path`.
				- Seven saved versions of one session Set took 1.5 MB of git storage through the filter and 7.2 MB as Live's gzip files.
				- A plain `git clone` with the filter configured fails when the smudge script is a file in the same repository: git writes the Sets before the script. The filter commands have to live outside the repository, in the dotfiles gitconfig or a script installed by mise.
			- ### Leak check
				- [making-music#3 Pre-commit check for gzip and home-folder leaks in staged Sets](https://github.com/codekiln/making-music/issues/3): the check reads staged blobs and refuses gzip, non-XML, the current `$HOME` and the username, including the username as a folder name in a `RelativePath`.
				- A rule against every `/Users/<name>` path refused all four real Sets: each holds three paths from factory presets naming the home folders of people at Ableton. [making-music#9](https://github.com/codekiln/making-music/pull/9) dropped that rule. CI runs as another user, so it sees a username only through a `SET_LEAK_NAMES` repository secret.
			- ### DVC with two keys
				- [making-music#4 DVC Samples folder routed to a private B2 remote](https://github.com/codekiln/making-music/issues/4) used the logseq-garden bucket as the private remote and logseq-encode-garden as the public one, each with its own key, under `experiments/making-music/dvc/`.
				- A stub `Samples.dvc` keeps `remote: private` through `dvc add` and a re-add. `dvc add` writes `/Samples` to the project's `.gitignore`, and the `.als` stays tracked. `*.asd` in `.dvcignore` keeps analysis files out.
				- With one key per bucket, a plain `dvc push` or `dvc pull` fails with a 403 on the other bucket. Every task names its `.dvc` targets and its remote. An untargeted `dvc pull -r public` still reads the private `.dir` object and fails.
				- `dvc status -c` reports a private object in sync when it is missing. `dvc data status --not-in-remote --granular` with `-r private` finds it.
				- B2 keeps a deleted object as a hidden version, so deleting from a bucket means deleting every version.
		- ## Steps
			- ### Private bucket and credentials
				- TODO Create the B2 bucket `logseq-encode-garden-private` with private access, and an application key restricted to it. Store the key in [[1Password]] and add a [[fnox]] profile for it beside `assets` in `fnox.toml`.
				- TODO Add the remote to `.dvc/config`: `['remote "private"']`, `url = s3://logseq-encode-garden-private/dvc/`, `endpointurl = https://s3.us-east-005.backblazeb2.com`. Leave `core.remote = garden`; the 835 existing `.dvc` files rely on it.
			- ### The `ableton` filter
				- TODO Add a root `.gitattributes`: `assets/Ableton/Project/**/*.als filter=ableton -merge`, and the same line for `.alc`, `.adg` and `.adv`. `-merge` makes two branches that both changed a Set stop with a conflict, since a line merge can produce XML Live can't load.
				- TODO Install the clean and smudge scripts from [making-music experiments/2-home-swap-filter](https://github.com/codekiln/making-music/tree/main/experiments/2-home-swap-filter) outside the repository, and define `[filter "ableton"]` to run them in the global gitconfig in [codekiln/dotfiles chezmoi/dot_gitconfig](https://github.com/codekiln/dotfiles/blob/main/chezmoi/dot_gitconfig), and add a mise task, `ableton:filter:install`, that sets the same two keys in one clone. Leave `filter.ableton.required` off, so the Publish workflow's clone, which has no filter, checks out plain XML.
				- TODO Add a [[lefthook]] pre-commit check that every staged blob for those four extensions starts with `<?xml`. A clone without the filter would otherwise commit gzip.
				- TODO Point the identity guard in `lefthook.yml` at the staged XML (`git show :<path>`). It reads the working file, which is gzip, so it misses the home-folder paths each `<Path Value=...>` holds.
			- ### Project tasks
				- TODO Write `ableton:project:add <owner>`. It checks that the owner page exists, that the folder name matches it, and that every sample reference in each Set is relative to the project, which Collect All and Save does ([[Ableton/Live/UG/05 Managing Files and Sets/07 Collecting External Files]]). Then it writes the project `.gitignore`, writes a stub `Samples.dvc` holding `path: Samples` and `remote: private`, runs `dvc add`, and stages the Sets.
				- TODO Write `ableton:project:push`, `ableton:project:fetch` and `ableton:project:offload`, running DVC with `-r private` under the private fnox profile. `offload` checks `dvc data status --not-in-remote` before deleting `Samples/` and its cache entries; `dvc status -c` skips outputs routed to their own remote.
				- TODO Add a check that every `.dvc` file under `assets/Ableton/Project/` names `remote: private`, as a lefthook command and in the tasks' tests. A `Samples.dvc` without it goes to the public bucket on the next `dvc push`.
				- TODO Add `*.asd` to `.dvcignore`.
			- ### Garden pages
				- TODO Write [[Logseq/Entity/Ableton/Project]] for the folder convention above, linked from [[Logseq/Entity/Ableton/Set]].
				- TODO Add Live projects to [[My/AI/Rule/Logseq/Store binary files in B2 through DVC]]: Sets and presets go in git as XML, `Samples/` goes to the private bucket.
				- TODO Fix [[Ableton/File/.agr]], which calls every groove binary.
			- ### Pilot
				- TODO Move [[GitP/A/Template/Pattern A and B]] into `assets/Ableton/Project/GitP___A___Template___Pattern-A-and-B/`. Open the smudged Set in Live 12, save it without changes, and read the XML diff to see how much view state a plain save rewrites. In the same sitting, check whether Live opens an uncompressed `.als`.
				- TODO Move [[GitP/A/Template/LPP-Seq]] the same way, then `dvc remove` both `GitP___A___Template___*___Asset___Set.als.dvc` files and update their asset pages.
				- TODO Move one session project out of `~/Documents/ableton/GitP/`, run `ableton:project:add` and `ableton:set:import`, and push its samples.
		- ## Open questions
			- The clean filter swaps the home folder for `~` and the smudge filter restores it, per [[Ableton/Live/Idea/Store-Ableton-in-the-Garden/Plan/Discussion/Analysis/Opus/26/11/28/0738 ET Swap the home folder for a tilde in the filter and restore it on checkout]]. Two Live tests on that page remain.
			- Should `Ableton Project Info/` be tracked? It was empty in the temporary projects on this Mac and held one `.cfg` file in a third-party pack project.
			- Should samples imported from factory packs go to the private bucket, or stay ignored, since Live can restore them from the pack?
			- Does the loose-recording private mount on [[dvc/Q/Can DVC keep files with certain extensions in a different remote from the rest, so lossless audio goes to a private B2 bucket?]] still need building once projects carry their own samples? The WAV behind the `dvc.yaml` MP3 stage is the one file that needs it today.
			- The plan follows [[My/Principle/Balance/Risk vs Reward/wrt Privacy - Make Things As Public As They Can Be]]: Sets and pages are public, uncompressed audio is private. A `.dvc` file still publishes each sample folder's size and hash.
