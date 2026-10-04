- # September 25 release handoff
	- Production note: [[Music/Composition/Log/26/09/25 Fri]].
	- Public episode: [GitP.26.09.25](https://codekiln.github.io/gitpa/#/page/Ceremony%2F2026%2F09%2F25).
	- Object key: `gitpa/episodes/2026-09-25/GitP.26.09.25.mp3` in the `logseq-encode-garden` bucket.
	- Backblaze object SHA-1: `bb21670ca393a0d0afa5a5ab22eef27f457aa6a5`, reported by the public object's response header. Local source comparison and a SHA-256 release manifest remain to be added.
	- On [[2026-10-04 Sun]], the public media URL returned HTTP 200, `audio/mpeg`, and `Content-Length: 23569806`; a request for the opening byte returned HTTP 206 with the matching total length.
	- ## Publication record
		- These fields reproduce the [published Gitpa episode record](https://github.com/codekiln/gitpa/blob/main/gitp-garden/assets/Ceremony/2026/09/25/episode.yml). The YAML can be saved as `episode.yml` and consumed by Gitpa's existing RSS builder alongside the public ceremony page. Its GUID and publication time belong to the existing release.
		- ~~~yaml
		  published: true
		  episode_title: GitP.26.09.25
		  description: MicroFreak SAWX and WaveUser preset 1910, with a Novation Launchpad sequence.
		  recorded_on: '2026-09-25'
		  published_at: '2026-10-03T12:00:00-04:00'
		  guid: gitpa20260925
		  page: Ceremony/2026/09/25
		  page_url: https://codekiln.github.io/gitpa/#/page/Ceremony%2F2026%2F09%2F25
		  audio_url: https://f005.backblazeb2.com/file/logseq-encode-garden/gitpa/episodes/2026-09-25/GitP.26.09.25.mp3
		  audio_length: 23569806
		  audio_type: audio/mpeg
		  ~~~
	- ## Ownership
		- Garden release preparation owns `recorded_on`, `audio_url`, `audio_length`, `audio_type`, the object key, and checksum evidence. The session note supplies a proposed title and description.
		- Gitpa episode review owns `published`, `published_at`, `guid`, `page`, `page_url`, and the final title and description.
