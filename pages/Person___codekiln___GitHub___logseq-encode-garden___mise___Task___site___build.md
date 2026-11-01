logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: site:build
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/site/build
see-also:: [[Person/codekiln/GitHub/logseq-gardener]]

- # Publish the Garden as a Website
	- Builds the site served at https://codekiln.github.io/logseq-encode-garden/ from every page and journal with `lsg publish` from [[Person/codekiln/GitHub/logseq-gardener]]. Run it to preview the site before pushing. The Publish workflow runs it on every pull request and deploys its output from `main`.
	- ## Invocation
		- Run from the garden checkout, naming a new directory outside it:
			- ~~~sh
			  mise run site:build --output /tmp/encode-site
			  open /tmp/encode-site/index.html
			  ~~~
		- `--lsg` runs another lsg executable, such as a release under test. `--diagnostics` saves lsg's report of unresolved links and unsupported markup to a file.
	- ## Inputs and outputs
		- Reads `pages/`, `journals/`, `assets/` and `logseq/config.edn`. The config sets `:publishing/all-pages-public? true`, so every page is published except one marked `public:: false`.
		- Writes the site to the output directory, which must not exist yet. `index.html` is the journals feed and `pages.html` lists every page.
		- Old `#/page/<name>` addresses from the publish-spa site redirect to the matching page.
		- Stops with a list of page files when lsg leaves a page out of the site.
		- Prints lsg's time for each phase and the size of the site.
	- ## Dependencies and access
		- mise supplies lsg and uv. The task needs no credentials and works offline.
	- ## Failure and recovery
		- An existing output directory stops lsg; choose a new one.
		- A page reported as left out usually has a title the task derives differently from lsg. Compare its `title::` property and filename with lsg's page title rules.
	- ## Source and help
		- ~~~sh
		  mise run site:build --help
		  ~~~
