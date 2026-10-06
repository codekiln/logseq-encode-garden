logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[Logseq/Entity/Proxy/Page/mise/Task/sync]], [[GitP/How To/Draft an Episode from Session Assets]]
- # Prepare Podcast Metadata
	- Prepare the episode in this garden, then mirror it into [[Person/codekiln/GitHub/gitpa]] for publication. The session page supplies the episode text; its linked asset page supplies the recording.
	- ## Prepare the session
		- Create or update the recording's [[Logseq/Entity/Podcast/Episode]] page under `GitP/A/Session/YY/MM/DD-Day`. Link the music-making log and add the supported session details, preset downloads, and recording asset.
		- Give the page one H1 episode title and a short description as its first child. Embed the MP3 asset page beneath it. [[GitP/A/Session/26/09/24-Thu]] is an example.
		- Follow [[Logseq/Entity/Asset]] for the recording's asset page. The audio link belongs there; episode pages embed that page.
	- ## Mirror into Gitpa
		- Run [[Logseq/Entity/Proxy/Page/mise/Task/sync]] from the Gitpa checkout with this garden's checkout path, `--destination gitp-garden`, the session page name, and `--follow-embeds`. It copies the session and its embedded asset pages as [[Logseq/Entity/Proxy/Page]] instances.
		- Edit the episode in this garden and sync again. The proxy's body and properties follow the source; Gitpa keeps `tags::`, `public::`, `podcast-guid::` and `podcast-published-at::`.
	- ## Prepare the publication PR
		- On the Gitpa proxy, set `public:: true`, `podcast-guid::`, and `podcast-published-at::`. The latter two identify the RSS release and retain their values after publication. `public::` is the publication switch.
		- Run `mise run rss:build`, `mise run rss:check`, and `mise run rss:test` in Gitpa. RSS reads the proxy title, description, and recording link directly; enclosure size comes from the public media response.
		- Open a Gitpa PR with the episode title, a direct MP3 link, and the reason to listen: decide whether to publish this recording. The human merges the PR after one listen and a go decision.
