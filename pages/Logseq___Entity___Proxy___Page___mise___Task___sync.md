logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: logseq:entity:proxy:page:sync
task-entrypoint:: mise-tasks/logseq/entity/proxy/page/sync
task-files:: {"mise-tasks/logseq/entity/proxy/page/sync":"mise-tasks/logseq/entity/proxy/page/sync","mise-tasks/logseq/entity/proxy/page/lib/core.py":"mise-tasks/logseq/entity/proxy/page/lib/core.py","mise-tasks/logseq/entity/proxy/page/lib/companions.py":"mise-tasks/logseq/entity/proxy/page/lib/companions.py"}
task-dependencies:: [[Logseq/Entity/Proxy/Page/mise/Task/docs/serve]]
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/sync
see-also:: [[Logseq/Entity/Proxy/Page]], [[Logseq/Entity/Definition]]
- # Sync a Proxy Page and Its Companion Tasks
	- Copies a source page into another Logseq garden, together with its entity definitions, declared task references, executable files, helpers, and linked assets. Re-sync refreshes source changes and reports conflicting destination edits before applying changes.
	- ## Invocation
		- Runs from the source checkout or a destination garden containing the imported file task. Source and destination arguments identify graph roots containing `pages/` and `logseq/`:
			- ~~~sh
			  mise run logseq:entity:proxy:page:sync --source /path/to/logseq-encode-garden --destination /path/to/other-garden --page 'Logseq/Entity/Proxy/Page'
			  ~~~
		- The command previews the full import. Adding `--apply` writes the changes:
			- ~~~sh
			  mise run logseq:entity:proxy:page:sync --source /path/to/logseq-encode-garden --destination /path/to/other-garden --page 'Logseq/Entity/Proxy/Page' --apply
			  ~~~
		- `--page` is the source page's logical name, with slash namespaces. On re-sync, `--source` can be omitted when the destination page's proxy metadata resolves to a local source graph.
		- `--follow-embeds` also syncs every page the page embeds with the `embed` macro, and the pages those embed, in the same batch. A podcast session and its embedded recording, artwork and preset pages sync together this way:
			- ~~~sh
			  mise run logseq:entity:proxy:page:sync --source /path/to/logseq-encode-garden --destination /path/to/other-garden --page 'GitP/A/Session/26/09/24-Thu' --follow-embeds --apply
			  ~~~
	- ## Inputs and outputs
		- Reads the source page and the entity definitions named by `logseq-entity::`. Definitions declare companion tasks with `entity-tasks::`; task references declare implementation paths and required task dependencies through [[Logseq/Entity/Mise/Task]].
		- Copies pages under their source logical names, adds [[Logseq/Entity/Proxy/Page]] membership, and sets source URL, available code forge URL, and sync date. Source bodies replace destination bodies.
		- On re-sync, page properties follow the source: new ones are added, changed ones updated, and ones the source dropped are removed. `tags::`, the proxy keys, and the properties named by an entity definition's `entity-proxy-destination-properties::` keep their destination values. [[Logseq/Entity/Proxy/Page]] states the rule; the preview lists each property added, updated or removed.
		- Copies linked `../assets/` files and explicitly mapped task files. Source implementation paths start at the repository root, even when the source graph occupies a subdirectory; destination paths start at the destination graph root.
		- Records imported ownership, source paths, destination paths, and last imported hashes in `.logseq-proxy/manifest.json`. A repeat run previews only the changes still needed.
		- The manifest keeps current source task declarations and path mappings for onward imports from a proxy garden.
	- ## Side effects
		- Preview reads local files and reports planned changes, property changes, conflicts, missing assets and embedded pages, and upstream removal candidates. `--apply` creates or refreshes the previewed imports and manifest after validation.
		- An existing page without proxy metadata is a name collision. A task file with local edits, an unowned file at the target path, or competing source ownership stops application. Destination edits remain available for review.
		- Files removed from upstream task mappings remain in the destination and appear as cleanup candidates. Missing linked source assets are warnings; missing declared task requirements stop application.
		- Application stages writes and retains recovery information or restores previous files if a write fails.
	- ## Dependencies and access
		- Mise supplies Python through the file task's tool metadata. The sync implementation uses Python's standard library and requires local read access to the source and write access to the destination for `--apply`.
		- Source discovery follows [[Logseq/Entity/Proxy/Page]]: a code forge URL resolves through locally registered ghq repositories, and a Logseq graph URL can resolve through the desktop graph list. An explicit `--source` selects a graph directly.
		- Imported task files retain executable mode. The destination's mise task discovery must include its `mise-tasks/` directory.
	- ## Failure and recovery
		- Unresolved source: provide `--source` with the graph root or make the existing source repository available locally.
		- Page collision: compare the source and destination pages and choose which page belongs in the destination before syncing again.
		- Missing task declaration or implementation: repair the source task reference or restore the named file, then preview again.
		- Local implementation edit: review the destination file against its source and retain or reconcile the edit before syncing again.
		- Interrupted application: run `mise run logseq:entity:proxy:page:sync --destination /path/to/other-garden --recover` to restore the previous files, then run a fresh preview.
		- Conflicting ownership: reconcile the source mappings so each destination implementation path has one source owner.
	- ## Illustrated guide
		- [How Logseq proxies work](../mise-tasks/logseq/entity/proxy/page/docs/index.html) explains first imports, refreshes, multiple source gardens, manifest ownership, Git tracking, and parallel-agent integration.
		- Open the guide in a local browser with the imported docs task:
			- ~~~sh
			  mise run logseq:entity:proxy:page:docs:serve
			  ~~~
		- The server binds to `127.0.0.1`; `--port` selects a port, `--no-open` keeps browser selection manual, and Ctrl-C stops the server.
	- ## Source and help
		- [Sync file task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/sync), [page sync implementation](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/lib/core.py), and [companion import implementation](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/lib/companions.py).
		- ~~~sh
		  mise run logseq:entity:proxy:page:sync --help
		  ~~~
