# GitP episode preparation

The garden prepares session evidence and selected release metadata. Gitpa imports the metadata to curate its public episode pages and feed.

With Python 3 and `ffprobe` available, run from this garden checkout:

```sh
mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project'
```

The task reads the matching garden session note, Ableton set, and prepared `GitP.26.09.24.mp3`. Pass `--note` when the date has several candidate notes, or `--mp3` for a prepared MP3 outside the project directory. It writes `session-note.md` and `handoff.json` under `assets/GitP/Session/YYYY/MM/DD/`. Source recordings remain in place.

`handoff.json` contains `recorded_on`, `episode_title`, and a proposed `description`. An explicit `Description:` bullet in the source note supplies the description; otherwise the note's device heading provides a brief proposal. Production observations and track names remain in the evidence note for listening review.

To attach an existing public release, pass `--audio-url https://.../episode.mp3`. The task checks its MIME type, length, opening range, and Backblaze SHA-1 when supplied before adding `audio_url`, `audio_length`, and `audio_type`. A failed check stops preparation. The evidence note records the local MP3's SHA-256. URLs must use permanent public HTTPS without credentials, query parameters, or fragments.

Gitpa's `mise run episode:import -- /path/to/handoff.json` consumes the JSON. Gitpa owns the final copy, public page, GUID, publication date, and publication decision. Existing editorial copy remains subject to Gitpa's importer conflict handling.

Both garden outputs are created exclusively. An existing evidence note or handoff stops the task before source inspection; use a fresh `--output-dir` to compare a new preparation with existing human edits.

Optional `--transcript /path/to/whisper.json` assesses existing recognition output. `--transcribe` performs local recognition on a commentary stem whose duration matches the release, using the cached MLX Whisper dependencies and model. Recognition quality findings stay in the evidence note; transcription claims need listening review before inclusion in public copy. Live transcription requires macOS with the local MLX runtime; ordinary preparation and existing transcript assessment use Python's standard library and `ffprobe`.

The September 24 example in `assets/GitP/Session/2026/09/24/` records the already uploaded release and its session evidence. Its earlier rejected recognition finding was retained without rerunning transcription.

Run the production tests with:

```sh
mise run gitpa:episode:test
```
