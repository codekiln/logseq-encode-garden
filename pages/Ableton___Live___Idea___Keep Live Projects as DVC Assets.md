tags:: [[Idea]]
date-created:: [[2026-11-23 Mon]]
see-also:: [[Ableton/Live/Idea/Declare a Live Set in Logseq]], [[Asset/Mount]], [[Logseq/Entity/Asset/B2]]

- # Keep Live Projects as DVC Assets
	- Save each [[Ableton/Live]] project inside a git checkout under `assets/.remote/<mount>/`, back it up with [[DVC]] to a private [[Backblaze/B2]] bucket, and publish only outputs such as an episode MP3 to this garden. [[Person/codekiln]] raised this on [[2026-11-23 Mon]] and has not chosen between keeping projects in [[Person/codekiln/GitHub/logseq-garden]] and starting a repository just for Ableton.
	- ## Why move projects out of `~/Documents`
		- A Claude Code session in the desktop app could not read `~/Documents/ableton/GitP`, even with its command sandbox off. The app starts Claude Code through its `disclaimer` helper, so macOS checks the permissions of the Claude Code bundle, `claude.app`, rather than those of `Claude.app`.
		- That bundle declares no reason for Documents access in its `Info.plist`. This likely explains why macOS refused without a prompt and lists no Documents row for the bundle under Files & Folders.
		- Files & Folders grants all of `~/Documents` or none of it. A checkout under `~/ghq` is outside the folders macOS protects.
		- iCloud does not sync `~/Documents` on this Mac. After a DVC push, B2 holds a copy of each project.
	- ## Precedent
		- The [[GitP/A/Session/26/09/24-Thu]] project is a 630 MB collected ZIP in the private `logseq-garden` bucket, archived after the session. This idea has Live save into the tracked folder during the session instead.
	- ## Option: keep projects in logseq-garden
		- The `logseq-garden` mount has no `public` URL, so `site:build` stops when a published page links into it, as [[Asset/Mount]] describes. Project files stay private unless an output is copied to this garden on purpose.
		- Each project sits beside its asset page. A page-named folder holds Live's own `<date> Project` folder, as in the Sep 24 layout, so Live's browser keeps short names.
		- Live saves into the primary checkout only. A linked worktree is deleted after its PR merges, and its `assets/.remote/` is empty because git ignores those files.
	- ## Option: a repository just for Ableton
		- Projects that belong to no garden page, such as sketches outside GitP, fit without an asset page.
		- Per-session `.dvc` commits stay out of the garden's history, and the bucket gets its own key.
		- [[GitHub/codekiln/ableton-live-git-hooks]] could store each `.als` as XML that git can diff.
		- The repository needs its own bucket, key, fnox cache and mount, the setup that `asset:setup` performed for logseq-garden.
		- Garden pages would reach project files by absolute path, which does not resolve in a worktree or on another machine.
	- ## Either option
		- `gitpa:ableton:sync --output`, `gitpa:media:prepare` and `gitpa:media:upload` take file paths as arguments, so publishing needs no code change.
		- The Logseq 0.10.15 file watcher skips any path containing a folder whose name starts with `.`, so it ignores `assets/.remote/`. [graph.cljs](https://github.com/logseq/logseq/blob/0.10.15/deps/common/src/logseq/common/graph.cljs#L42-L72)
		- [[Asset/mise/Task/add]] copies single files and refuses WAV, AIFF and FLAC because this garden's bucket is public. A project folder full of recorded WAVs needs a ZIP, as on Sep 24, or a task that tracks a whole folder in a private bucket.
		- After each session, Collect All and Save copies samples from outside the project into it, as [[Ableton/Live/UG/05 Managing Files and Sets/07 Collecting External Files]] describes. Then the folder is tracked, its `.dvc` metadata committed, and its files pushed to B2.
		- [[My/AI/Rule/Upload a session WAV only when I ask]] would need to say that it covers the public bucket.
		- The 20 sessions from Sep 24 to Nov 22, at about the Sep 24 size, add roughly 6 GB a month.
