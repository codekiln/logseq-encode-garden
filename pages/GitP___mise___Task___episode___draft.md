logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: gitpa:episode:draft
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/codex/gitp-house-split/mise-tasks/gitpa/episode/draft
see-also:: [[GitP/How To/Prepare an Episode Handoff]], [[GitP/House/Back]]
- # Prepare Episode Evidence and Handoff
	- Collects the source note, Ableton track names, MP3 checksum, and optional transcription assessment for an episode review. Exports proposed episode copy and optional verified enclosure metadata for the Gitpa importer.
	- ## Invocation
		- Runs from the `logseq-encode-garden` checkout:
			- ~~~sh
			  mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project'
			  ~~~
		- `--note` selects a source page explicitly. `--mp3` selects a prepared MP3 outside the project directory. `--audio-url` verifies a permanent public MP3 URL against the local file.
	- ## Inputs and outputs
		- Inputs: a project name containing `YY.MM.DD`, one Ableton `.als` set, a prepared MP3, and a session note in the garden's `pages/` directory.
		- Output page: `GitP/Session/YY/MM/DD Day/Production Evidence`, containing source links, track names, checksum, observations, and recognition-quality findings when requested.
		- Output asset: `assets/GitP/Session/YYYY/MM/DD/handoff.json`, containing `recorded_on`, `episode_title`, and `description`. A successful public-media check adds `audio_url`, `audio_length`, and `audio_type` together.
		- The proposed description comes from a `Description:` source-note bullet or the source note's device heading. Listening review determines the final public copy.
	- ## Side effects
		- Creates a new evidence page and JSON handoff. Existing outputs stop preparation before inspection. `--evidence-page` and `--output-dir` select fresh comparison destinations.
		- Reads source recordings without moving them. `--audio-url` makes HTTP requests to verify media type, length, opening audio range, and Backblaze checksum when available.
		- `--transcribe` runs local speech recognition and may download Python dependencies and model files. It creates temporary audio for recognition; findings appear on the evidence page.
	- ## Dependencies and access
		- Mise supplies the task's declared Python, FFmpeg/ffprobe, and uv versions. Optional local recognition uses MLX Whisper on Apple Silicon macOS; `--transcript` assesses an existing Whisper JSON file.
		- Ordinary preparation needs local read access to the session files. Public-media verification uses the supplied HTTPS URL. This task prepares metadata; uploading media and publishing the episode are separate jobs.
	- ## Failure and recovery
		- Ambiguous source-note discovery: select the page with `--note`.
		- Existing output: retain the edited page and handoff, then select fresh output paths for a comparison.
		- Media mismatch: compare the uploaded object with the prepared MP3 before producing another handoff.
	- ## Source and help
		- [Preparation file task](https://github.com/codekiln/logseq-encode-garden/blob/codex/gitp-house-split/mise-tasks/gitpa/episode/draft)
		- ~~~sh
		  mise run gitpa:episode:draft --help
		  ~~~
