logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: gitpa:episode:test
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/gitpa/episode/test
see-also:: [[GitP/mise/Task/episode/draft]]
- # Test Episode Preparation
	- Checks episode metadata extraction, media verification, asset-page layout, argument handling, and preservation of existing outputs before changing the preparation task.
	- ## Invocation
		- Runs from the `logseq-encode-garden` checkout:
			- ~~~sh
			  mise run gitpa:episode:test --verbose
			  ~~~
	- ## Inputs, outputs, and side effects
		- Loads the preparation implementation and creates synthetic session fixtures in temporary directories. Network verification is mocked.
		- Prints unittest results and exits unsuccessfully if a test fails. It creates no production page or handoff, uploads no media, and reads no real recording.
	- ## Dependencies and access
		- Mise supplies the declared Python version. Fixtures and mocks use Python's standard library.
	- ## Failure and recovery
		- A failing assertion identifies the behavior that changed. Compare that behavior with [[GitP/mise/Task/episode/draft]] before updating the implementation or its test expectations.
	- ## Source and help
		- [Preparation test file task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/gitpa/episode/test)
		- ~~~sh
		  mise run gitpa:episode:test --help
		  ~~~
