logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[Logseq/Entity/Proxy/Page/mise/Task/sync]], [[GitP/How To/Draft an Episode from Session Assets]]

- # Prepare Podcast Metadata
	- Prepare the episode in this garden, then mirror it into [[Person/codekiln/GitHub/gitpa]] for publication. The session page supplies the episode text and directly embeds the recording’s MP3 URL.
	- ## Prepare the session
		- Create or update the recording's episode page under `GitP/A/Session/YY/MM/DD-Day`. Set `logseq-entity:: [[Logseq/Entity/Podcast/Episode/GitP/A]], [[Logseq/Entity/Podcast/Episode]]` in its frontmatter. Link the music-making log and add the supported session details, preset downloads, and recording asset.
		- Give the page one H1 episode title and a short description as its first child. Embed the MP3 beneath it with `![Episode recording](https://…mp3)`. [[GitP/A/Session/26/10/06-Tue]] is an example.
		- Write chapter headings as plain timestamps and titles, such as `- ### 14:42 Adapters and input modes`. Keep one full recording on the episode; the published player turns timestamps into seek controls. Separate chapter recordings and waveform embeds are unnecessary.
		- Follow [[Logseq/Entity/Asset]] for the recording's asset page. The asset page holds file metadata and the audio link; the episode also embeds the MP3 URL directly.
	- ## Check preset research
		- Every saved preset linked from the session needs upstream notes covering saved export provenance, oscillator controls, filter, envelopes, LFO, modulation matrix and performance context. Include cited evidence and supported units, distinguishing the archived or factory baseline from observed session edits. [[Logseq/Entity/Preset/Synth/Microfreak]] describes the evidence limits.
		- Run `mise run gitpa:preset:audit --episode 'GitP/A/Session/YY/MM/DD-Day' --check` from this garden before publication. Resolve missing pages, stubs and unresearched sections; keep unsupported values and unavailable evidence explicit. The audit checks recorded coverage rather than proving every interpretation.
		- Use `mise run gitpa:preset:audit --all --json > /tmp/gitp-preset-audit.json` for an advisory historical report. It does not gate the whole site's deployment.
	- ## Mirror into Gitpa
		- Run [[Logseq/Entity/Proxy/Page/mise/Task/sync]] from the Gitpa checkout with this garden's checkout path, `--destination gitp-garden`, the session page name, and `--apply`. It copies the session as a [[Logseq/Entity/Proxy/Page]] instance. Sync the episode’s audio and MIDI asset pages separately by their exact page names so Gitpa includes their file metadata.
		- Sync every preset referenced by the session separately by its exact page name after enriching its notes upstream. Keep the preset research in this source garden and re-sync later corrections.
		- Edit the episode in this garden and sync again. Sync copies the episode body and `public::` selection from the source. Gitpa keeps `tags::`, `podcast-guid::`, and `podcast-published-at::`.
	- ## Prepare the publication PR
		- On the source [[Logseq/Entity/Podcast/Episode/GitP/A]] page in logseq-encode-garden, set `public:: true` to select publication or `public:: false` to exclude the episode from RSS and the website. Re-sync copies that selection to the publishing repository’s proxy. On the proxy, set `podcast-guid::` and `podcast-published-at::`; these identify the RSS release and remain destination-owned.
		- Run `mise run rss:build`, `mise run rss:check`, and `mise run rss:test` in Gitpa. RSS reads the proxy title, description, and recording link directly; enclosure size comes from the public media response.
		- Open a Gitpa PR with the episode title, a direct MP3 link, and the reason to listen: decide whether to publish this recording. The human merges the PR after one listen and a go decision.