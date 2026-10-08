see-also:: [[GitP/A/Session/26/10/06-Tue]], [[Person/codekiln/GitHub/gitpa]], [[Logseq/Entity/Proxy/Page/mise/Task/sync]]

- # Rename the October 6 session from `06-Thu` to `06-Tue`
	- October 6, 2026 was a Tuesday. The garden pages are already renamed to [[GitP/A/Session/26/10/06-Tue]], [[GitP/A/Session/26/10/06-Tue/Asset/Synth/Full/mp3]] and [[GitP/A/Session/26/10/06-Tue/Asset/MIDI/Full/mid]]. Their bodies still link the B2 objects under the old name, and gitpa still publishes the episode under the old name.
	- ## Where the old name remains
		- B2 holds two public objects under the old name, both answering anonymous requests with `200`:
			- [GitP___A___Session___26___10___06-Thu___Asset___Synth___Full.mp3](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___06-Thu___Asset___Synth___Full.mp3), the episode recording.
			- [GitP___A___Session___26___10___06-Thu___Asset___MIDI___Full.mid](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___06-Thu___Asset___MIDI___Full.mid), the full-session MIDI download.
			- Nothing exists yet under the `06-Tue` names.
		- The garden links those objects from four places: the session page (recording embed and MIDI download), the MP3 asset page, and the MIDI asset page.
		- Gitpa `main` carries three proxy pages under `GitP/A/Session/26/10/06-Thu`, their entries in [gitp-garden/.logseq-proxy/manifest.json](https://github.com/codekiln/gitpa/blob/main/gitp-garden/.logseq-proxy/manifest.json) (the `declarations`, `imports` and `pages` sections), and the episode's feed item.
		- The episode is live. [codekiln/gitpa#22 restore approved October 6 episode](https://github.com/codekiln/gitpa/pull/22) merged on [[2026-10-08 Thu]], and the [deployed feed](https://codekiln.github.io/gitpa/rss.xml) carries the item with `guid` `gitpa20261006`, an episode link to `#/page/GitP%2FA%2FSession%2F26%2F10%2F06-Thu`, and an enclosure at the old MP3 URL. See [rss.xml lines 24–33](https://github.com/codekiln/gitpa/blob/main/rss.xml#L24-L33).
		- The prepared exports in `~/Documents/ableton/GitP/GitP26.10.06 Project/` have MD5 sums equal to the ETags of both live objects, so they are the same files.
	- ## Copy the media to the new names
		- Upload each local export under its renamed asset page with [[GitP/mise/Task/media/upload]], from a garden checkout:
			- ~~~sh
			  mise run gitpa:media:upload -- "$HOME/Documents/ableton/GitP/GitP26.10.06 Project/GitP___A___Session___26___10___06-Thu___Asset___Synth___Full.mp3" 'GitP/A/Session/26/10/06-Tue/Asset/Synth/Full/mp3'
			  mise run gitpa:media:upload -- "$HOME/Documents/ableton/GitP/GitP26.10.06 Project/GitP___A___Session___26___10___06-Thu___Asset___MIDI___Full.mid" 'GitP/A/Session/26/10/06-Tue/Asset/MIDI/Full/mid'
			  ~~~
		- The task derives the object name from the page, so these create `GitP___A___Session___26___10___06-Tue___Asset___Synth___Full.mp3` and `GitP___A___Session___26___10___06-Tue___Asset___MIDI___Full.mid`. It checks SHA-1, length and media type on B2, then downloads the object and compares SHA-256 with the local file.
		- Check each new URL anonymously at the public S3 endpoint the other pages use: `curl -sI https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/<new name>` should return `200`, the same `Content-Length` and `Content-Type` as the old object, and the same ETag.
		- The old objects stay in place. The live feed keeps working through every step below.
	- ## Point the garden at the new objects
		- In a garden PR, replace `06-Thu` with `06-Tue` in the four B2 URLs on [[GitP/A/Session/26/10/06-Tue]], [[GitP/A/Session/26/10/06-Tue/Asset/Synth/Full/mp3]] and [[GitP/A/Session/26/10/06-Tue/Asset/MIDI/Full/mid]]. After that, `grep -rn "06-Thu" pages journals` should match only log text.
		- Merge it before the gitpa PR. Gitpa proxies record `logseq-proxy-codeforge-url::` links to garden `main`, so the renamed pages need to be on `main` when gitpa syncs them.
	- ## Rename the proxies and update the feed in gitpa
		- Work in a gitpa worktree off `origin/main`. Open PRs [codekiln/gitpa#23 Launchpad namespace import](https://github.com/codekiln/gitpa/pull/23) and [codekiln/gitpa#24 Microfreak namespace proxies](https://github.com/codekiln/gitpa/pull/24) also write `manifest.json`; whichever lands second rebases and re-runs sync.
		- Sync the three renamed pages from the garden's registered `main` checkout. The session page links its assets by URL, so each asset page needs its own run:
			- ~~~sh
			  for page in 'GitP/A/Session/26/10/06-Tue' 'GitP/A/Session/26/10/06-Tue/Asset/Synth/Full/mp3' 'GitP/A/Session/26/10/06-Tue/Asset/MIDI/Full/mid'; do
			    mise run logseq:entity:proxy:page:sync --source ~/ghq/github.com/codekiln/logseq-encode-garden --destination gitp-garden --page "$page" --apply
			  done
			  ~~~
		- Sync creates new proxy files, so the gitpa-owned properties start empty. Copy these three lines from the old session proxy into the new one, unchanged:
			- ~~~
			  public:: true
			  podcast-guid:: gitpa20261006
			  podcast-published-at:: 2026-10-07T05:28:02-04:00
			  ~~~
			- Keeping `podcast-guid::` tells podcast apps this is the episode they already have. Keeping `podcast-published-at::` keeps its place and date in the feed.
		- Remove the three `06-Thu` proxy pages with `git rm`, and delete their keys from the `declarations`, `imports` and `pages` sections of `manifest.json`. The sync task has no rename or removal option, so this part is a hand edit. Leaving the old session proxy public would also fail the feed build: [build_rss.py line 85](https://github.com/codekiln/gitpa/blob/main/scripts/build_rss.py#L85) rejects a duplicate GUID.
		- Run `mise run rss:build`, `mise run rss:check`, `mise run rss:test` and `mise run site:query:check`. The expected `rss.xml` diff is two lines in the October 6 item: the `<link>` and the enclosure `url`. Title, description, `guid`, `pubDate` and enclosure length stay the same.
		- `grep -rn "06-Thu" gitp-garden rss.xml` should return nothing.
		- In the PR's `gitpa-website` preview artifact, open the episode under the new page name and play the recording.
		- Merging deploys the site and feed. Afterwards, fetch `https://codekiln.github.io/gitpa/rss.xml` and check the item's new enclosure URL.
	- ## Retire the old objects
		- The feed is the only thing outside the two repositories known to hold the old MP3 URL. Apps that already downloaded the episode keep their copy; apps that refresh the feed pick up the new enclosure under the same GUID.
		- After the new feed has been live for a waiting period, check that neither repository nor the live feed contains `06-Thu`, then hide both old objects in B2. Hiding makes the name return `404` and keeps the stored version, so un-hiding restores it. Delete the hidden versions later if storage matters.
		- The garden's B2 tooling only uploads and verifies. Hiding happens in the Backblaze web console or with `rclone`/`aws` using the garden's Fnox `assets` credentials.
	- ## Follow-ups
		- Add a short "Rename a source page" section to [[Logseq/Entity/Proxy/Page]] once this has been done once: rename the source, sync the new name, carry the destination-owned properties, remove the old proxy and its manifest keys.
		- A rename option on [[Logseq/Entity/Proxy/Page/mise/Task/sync]] (for example `--rename-from <old page>`) would do the property carry-over and manifest cleanup in one previewed transaction. The task is vendored from this garden, so the change starts here and reaches gitpa by re-syncing [[Logseq/Entity/Proxy/Page]].
	- ## Questions
		- TODO Should the old episode link `#/page/GitP%2FA%2FSession%2F26%2F10%2F06-Thu` keep working on the website?
			- An `alias:: GitP/A/Session/26/10/06-Thu` on the garden session page would sync to gitpa and may let Logseq's exported site resolve the old address; the preview artifact can show whether it does. The cost is that the misnamed page name stays in both graphs' search.
		- TODO How long should the old B2 objects stay up after the new feed deploys before they are hidden?
