logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: gitpa:episode:transcribe
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/gitpa/episode/transcribe
see-also:: [[GitP/mise/Task/episode/draft]], [[GitP/How To/Draft an Episode from Session Assets]]
- # Transcribe a Session Recording
	- Produces a candidate transcript for checking against the recording. Recognition output needs listening review before it supplies public episode copy.
	- ## Invocation
		- From the garden checkout on Apple Silicon macOS:
			- ~~~sh
			  mise run gitpa:episode:transcribe -- /path/to/commentary.wav --output-dir /path/to/transcript
			  ~~~
		- `--model` selects a local model directory or MLX Whisper model.
	- ## Inputs and outputs
		- Input: a recording supported by MLX Whisper. Output: `commentary.json` in the selected output directory.
		- [[GitP/mise/Task/episode/draft]] invokes this task through its optional `--transcribe` flag and assesses the temporary result for recognition errors.
	- ## Dependencies and side effects
		- Mise declares MLX Whisper as a pinned `pypi:mlx-whisper` tool. Mise supplies its isolated Python environment through uv when this task is invoked; ordinary metadata preparation and tests do not install Whisper.
		- Recognition may download model files and writes transcript output. Source audio stays in place.
	- ## Failure and help
		- Requires Apple Silicon macOS. Missing recordings, unavailable models, and recognition failures stop transcription; metadata preparation can proceed without `--transcribe`.
		- ~~~sh
		  mise run gitpa:episode:transcribe --help
		  ~~~
