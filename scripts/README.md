# GitP episode preparation

The garden prepares session evidence and selected release metadata. Gitpa imports the metadata to curate its public episode pages and feed.

With Python 3 and `ffprobe` available, run from this garden checkout:

```sh
mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project'
```

The task reads the matching garden session note, Ableton set, and prepared `GitP.26.09.24.mp3`. Pass `--note` when the date has several candidate notes, or `--mp3` for a prepared MP3 outside the project directory. It writes a Logseq page at `pages/GitP___Session___YY___MM___DD Day___Production Evidence.md` and a JSON handoff at `assets/GitP/Session/YYYY/MM/DD/handoff.json`. Source recordings remain in place.

`handoff.json` contains `recorded_on`, `episode_title`, and a proposed `description`. An explicit `Description:` bullet in the source note supplies the description; otherwise the note's device heading provides a brief proposal. Production observations and track names remain in the evidence page for listening review.

To attach an existing public release, pass `--audio-url https://.../episode.mp3`. The task checks its MIME type, length, opening range, and Backblaze SHA-1 when supplied before adding `audio_url`, `audio_length`, and `audio_type`. A failed check stops preparation. The evidence page records the local MP3's SHA-256. URLs must use permanent public HTTPS without credentials, query parameters, or fragments.

Gitpa's `mise run episode:import -- /path/to/handoff.json` consumes the JSON. Gitpa owns the final copy, public page, GUID, publication date, and publication decision. Existing editorial copy remains subject to Gitpa's importer conflict handling.

Both garden outputs are created exclusively. An existing evidence page or handoff stops the task before source inspection, preserving existing content and frontmatter. The evidence page must be directly under this garden's `pages/`; `--output-dir` controls only the JSON handoff directory. Source-note discovery excludes production evidence pages.

For a comparison, supply fresh paths for both outputs:

```sh
mise run gitpa:episode:draft -- '/path/to/GitP26.09.24 Project' \
  --evidence-page 'pages/GitP___Session___26___09___24 Thu___Production Evidence Comparison.md' \
  --output-dir assets/GitP/Session/2026/09/24/comparison
```


Optional `--transcript /path/to/whisper.json` assesses existing recognition output. `--transcribe` performs local recognition on a commentary stem whose duration matches the release, using the cached MLX Whisper dependencies and model. Recognition quality findings stay in the evidence page; transcription claims need listening review before inclusion in public copy. Live transcription requires macOS with the local MLX runtime; ordinary preparation and existing transcript assessment use Python's standard library and `ffprobe`.

The [September 24 production evidence](../pages/GitP___Session___26___09___24%20Thu___Production%20Evidence.md) records the uploaded release and the earlier rejected recognition finding. Its [JSON handoff](../assets/GitP/Session/2026/09/24/handoff.json) carries the public metadata.

Run the production tests with:

```sh
mise run gitpa:episode:test
```
