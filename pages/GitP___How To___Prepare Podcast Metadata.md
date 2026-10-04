logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[GitP/House/Back]], [[GitP/House/Front]], [[GitP/mise/Task/episode/draft]]
- # Prepare Podcast Metadata
	- ## Overview
		- After gathering session assets and selecting the episode audio, collect the garden note, Ableton track names, MP3 checksum, and optional transcription assessment on a session assets page. Export selected episode fields as JSON for the podcast website to import.
		- The JSON supplies a proposed title and description. A public MP3 URL adds verified enclosure metadata. Gitpa keeps the final copy, episode page, GUID, publication time, and publication decision.
		- Start with [[GitP/How To/Draft an Episode from Session Assets]] when only raw recordings and notes are available.
	- ## When the export helps
		- For the September 24 recording, the session note supplies the recording date and description; the prepared MP3 supplies the file size. The JSON lets Gitpa import those fields without retyping them.
		- If a recording has no release MP3 yet, gather and assess its assets first. A JSON export is not needed to keep notes or draft copy in the garden.
		- A permanent uploaded MP3 URL can be checked against the local file before adding its URL, byte length, and media type to the podcast feed.
	- ## Prerequisites
		- An Ableton project directory whose name contains the recording date as `YY.MM.DD`, a prepared MP3, and a session note in this garden's `pages/` directory.
		- [[mise]] installs the Python and FFmpeg versions declared by the preparation task. Optional transcription declares its own MLX Whisper and uv dependencies when it runs.
		- The project contains one `.als` set. The default MP3 name is `GitP.YY.MM.DD.mp3` in the project directory; `--mp3` selects another file.
	- ## Steps
		- ### 1. Prepare the session asset page and JSON
			- Run [[GitP/mise/Task/episode/draft]] on the session directory:
				- ~~~sh
				  mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project'
				  ~~~
			- The task creates `GitP/Session/26/09/24 Thu/Session Assets` as an LFM page and `assets/GitP/Session/2026/09/24/handoff.json`.
			- If several source notes match the date, pass `--note pages/<source-page>.md`. An explicit `Description:` bullet supplies the proposed description; otherwise the device heading supplies a short proposal.
			- The JSON contains `recorded_on`, `episode_title`, and `description`. Track names, observations, and source links stay on the session asset page for review.
		- ### 2. Attach a public MP3 if available
			- Add `--audio-url https://example.com/episode.mp3` to the preparation command. Use a permanent HTTPS URL.
			- The task checks media type, length, and the opening audio range against the prepared MP3, plus the Backblaze SHA-1 when supplied. Successful verification adds `audio_url`, `audio_length`, and `audio_type` to the JSON. The session asset page records the local SHA-256.
			- If speech recognition is useful, pass `--transcript /path/to/whisper.json` to assess existing output. On Apple Silicon macOS, `--transcribe` invokes [[GitP/mise/Task/episode/transcribe]] to run local MLX Whisper on a matching commentary stem; `--model` selects the model. Check recognized speech against the recording before using it in public copy.
		- ### 3. Review and import the JSON
			- Read the session assets and listen to the recording. [[GitP/Session/26/09/24 Thu/Session Assets]] and [its JSON export](../assets/GitP/Session/2026/09/24/handoff.json) provide an example.
			- From the Gitpa checkout, import the JSON:
				- ~~~sh
				  mise run episode:import -- /path/to/garden/assets/GitP/Session/2026/09/24/handoff.json
				  ~~~
			- The importer creates an unpublished draft, preserves existing episode copy and publication identity, and rejects conflicting media metadata. Review the public page and feed before publication.
	- ## Troubleshooting
		- An existing session asset page or JSON export stops preparation before inspection. For a new comparison, choose fresh destinations for both outputs:
			- ~~~sh
			  mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project' --assets-page 'pages/GitP___Session___26___09___24 Thu___Session Assets Comparison.md' --output-dir assets/GitP/Session/2026/09/24/comparison
			  ~~~
		- The session asset page must be directly under the garden's `pages/` directory. `--output-dir` selects the JSON destination. Source recordings and existing page content remain intact.
		- If public-media verification fails, check the uploaded object's length, content type, range support, and identity against the local MP3 before preparing another JSON export.
