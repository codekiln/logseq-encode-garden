logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: logseq:entity:proxy:page:docs:serve
task-entrypoint:: mise-tasks/logseq/entity/proxy/page/docs/serve
task-files:: {"mise-tasks/logseq/entity/proxy/page/docs/serve":"mise-tasks/logseq/entity/proxy/page/docs/serve","mise-tasks/logseq/entity/proxy/page/docs/index.html":"mise-tasks/logseq/entity/proxy/page/docs/index.html"}
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/docs/serve
see-also:: [[Logseq/Entity/Proxy/Page]], [[Logseq/Entity/Proxy/Page/mise/Task/sync]]
- # Open the Proxy Algorithm Guide
	- Opens an illustrated guide to proxy imports, refreshes, multiple source gardens, manifest ownership, Git tracking, and parallel work.
	- ## Invocation
		- Runs from the garden checkout or a destination graph containing the imported docs task:
			- ~~~sh
			  mise run logseq:entity:proxy:page:docs:serve
			  ~~~
		- `--port` selects the local port; `--no-open` serves the guide without launching the default browser:
			- ~~~sh
			  mise run logseq:entity:proxy:page:docs:serve --port 8768 --no-open
			  ~~~
	- ## Inputs and outputs
		- Serves the adjacent [HTML guide](../mise-tasks/logseq/entity/proxy/page/docs/index.html) on `127.0.0.1`. The guide includes diagrams, lifecycle tabs, interactive conflict examples, and links to the implementation.
		- The task's file mapping includes the launcher and HTML so they travel with [[Logseq/Entity/Proxy/Page/mise/Task/sync]].
	- ## Side effects and access
		- Opens the default browser unless `--no-open` is supplied. The server runs until Ctrl-C and creates no build output or log files.
		- Mise supplies Python. The server uses Python's standard library and requires local access to the guide and an available localhost port.
	- ## Failure and recovery
		- An occupied port can be replaced with another `--port` value. A missing guide requires restoring the mapped HTML file.
	- ## Source and help
		- [Docs launcher](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/logseq/entity/proxy/page/docs/serve).
		- ~~~sh
		  mise run logseq:entity:proxy:page:docs:serve --help
		  ~~~
