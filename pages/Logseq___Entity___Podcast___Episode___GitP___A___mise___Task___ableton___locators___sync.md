logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: logseq:entity:podcast:episode:gitp:a:ableton:locators:sync
task-entrypoint:: mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/sync
task-files:: {"mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/sync":"mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/sync"}
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/sync
see-also:: [[Logseq/Entity/Podcast/Episode/GitP/A]], [[GitP/mise/Task/ableton/sync]], [[Ableton/File/.als]]

- # Mark Episode Chapters in an Ableton Live Set
	- Writes the timed chapter headings of a [[Logseq/Entity/Podcast/Episode/GitP/A]] page into the episode's [[Ableton/Live]] Set as arrangement locators, so the Set can be navigated by the same chapters as the episode.
	- ## Invocation
		- Runs from the garden checkout or from a destination graph that imported the task with an episode. `--page` is the episode's logical name and `--set` is the Live Set file:
			- ~~~sh
			  mise run logseq:entity:podcast:episode:gitp:a:ableton:locators:sync --page 'GitP/A/Session/26/11/01-Sun' --set ~/Documents/ableton/GitP/'26.11.01 Project'/26.11.01.als
			  ~~~
		- The command prints the plan. Adding `--apply` writes the Set.
		- `--graph` reads the page from another graph; the default is the graph holding the task. In Gitpa, `--graph /path/to/logseq-encode-garden` picks up headings edited since the last proxy sync.
		- `--start-beat` gives the arrangement position, in beats, of the recording's 00:00. The default, 0, is bar 1.
		- `--prune` also removes locators that match no chapter.
	- ## Inputs and outputs
		- Reads every H3–H6 heading that starts with a timestamp or an `audio-timestamp` macro, following the Chapters section of [[Logseq/Entity/Podcast/Episode/GitP/A]]. Timestamp-led bullets and headings inside code fences stay out.
		- Each chapter becomes a locator at its time converted to beats at the Set's tempo. Headings that share a time share one locator, their names joined with ` / `. A link contributes its label, or the last segment of its page name: `### 00:00 Enter [[Microfreak/Preset/259 Infini Pad]]` becomes `Enter 259 Infini Pad`.
		- Each written locator's annotation holds the episode page name. A re-run renames, moves and removes those locators as the headings change, and leaves the Set untouched when it already matches. A locator already at a chapter's time takes the chapter's name; other locators stay.
	- ## Side effects and access
		- `--apply` copies the previous Set to `Backup/<name> [YYYY-MM-DD HHMMSS].als` beside it, the folder Live uses for its own backups, then replaces the Set. Only the arrangement locator list changes; the rest of the XML stays byte for byte.
		- Live keeps an open Set in memory. Close the Set before applying, or reopen it afterwards without saving; saving the open copy writes over the new locators. The task warns when Live is running.
		- Mise supplies Python through uv. The task uses only the standard library.
	- ## Failure and recovery
		- A Set whose tempo changes over the arrangement is refused.
		- A missing page, a page without timed headings, or a file that is not a Live Set stops the task before writing.
		- Copying the backup over the Set undoes a sync.
	- ## Source and help
		- [Locator sync task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/sync) and its [tests](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/tests/test_sync.py):
			- ~~~sh
			  python3 -m unittest discover -s mise-tasks/logseq/entity/podcast/episode/gitp/a/ableton/locators/tests -v
			  ~~~
		- ~~~sh
		  mise run logseq:entity:podcast:episode:gitp:a:ableton:locators:sync --help
		  ~~~
