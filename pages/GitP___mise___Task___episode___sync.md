logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/gitpa]]
task-config-root:: .
task-name:: episode:sync
source-link:: https://github.com/codekiln/gitpa/blob/main/mise-tasks/episode/sync
see-also:: [[GitP/How To/Prepare Podcast Metadata]]
- # Sync an Episode into Gitpa
	- Mirrors a garden session and its asset pages into Gitpa as [[Logseq/Entity/Proxy/Page]] instances. Run it after preparing or editing an episode in this garden.
	- ## Invocation
		- From the Gitpa checkout:
			- ~~~sh
			  mise run episode:sync -- --source /path/to/logseq-encode-garden 'GitP/A/Session/26/09/24-Thu'
			  ~~~
		- Use `--source` to select a review worktree when preparing a paired garden/Gitpa PR.
	- ## Inputs and outputs
		- The source session lives under `pages/`. Its embedded recording and linked asset pages are copied with identical filenames into Gitpa's `gitp-garden/pages/`.
		- Each copy carries the source Logseq URL, code-forge URL, and sync date. Relative source assets are copied to matching destination paths.
	- ## Side effects
		- A new proxy starts with the source properties and body. Resync replaces the body and proxy properties while preserving Gitpa's other properties, including tags and publication identity.
		- A destination page with the same name that is not a proxy stops the sync. Review that collision before changing either page.
		- Public remote asset links remain links; this task uploads no media and publishes no website.
	- ## Dependencies and recovery
		- Mise supplies Python. Both repository checkouts must be available locally; source preparation and uploads happen before sync.
		- Check reported missing source assets and repair their links or files. Run the sync again after updating the garden episode.
	- ## Source and help
		- [Episode sync task](https://github.com/codekiln/gitpa/blob/main/mise-tasks/episode/sync)
		- `mise run episode:sync --help`
