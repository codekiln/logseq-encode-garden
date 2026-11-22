logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/dotfiles]]
task-config-root:: chezmoi/dot_config/mise
task-name:: logseq:fix-wikilink-labels
source-link:: https://github.com/codekiln/dotfiles/blob/main/chezmoi/dot_config/mise/tasks/logseq/executable_fix-wikilink-labels
see-also:: [[Logseq/Link/Labeled Wikilink]], [[lefthook]]

- # Fix Labeled Wikilinks
	- Rewrites each [[Logseq/Link/Labeled Wikilink]], `[[Target|Label]]`, to `[[Target]]` in the pages of a Logseq graph. Gardens run it before every commit, and once with no arguments to convert existing pages.
	- ## Invocation
		- Runs as a global task from the root of a garden repository.
			- ~~~sh
			  mise run logseq:fix-wikilink-labels                       # every tracked graph page
			  mise run logseq:fix-wikilink-labels pages/A.md pages/B.md # these files
			  mise run logseq:fix-wikilink-labels --check               # report only, exit 1 if any
			  ~~~
		- Each garden's `lefthook.yml` runs it on staged Markdown, and `stage_fixed: true` puts the fix in the commit being made:
			- ~~~yaml
			  pre-commit:
			    commands:
			      logseq-wikilink-labels:
			        glob: "*.md"
			        run: mise run logseq:fix-wikilink-labels {staged_files}
			        stage_fixed: true
			  ~~~
	- ## Scope
		- Changes only Markdown files with `logseq/config.edn` in a parent directory, so a repository's README or specs are left alone. Inline code and fenced blocks are skipped, so a page can still show the Obsidian syntax.
	- ## Output
		- Prints `path:line: fixed: [[Target|Label]] -> [[Target]]` for each rewrite. A label that carried meaning in its sentence is dropped, so read the printed lines and reword the sentence when it needs the label back.
	- ## Source and help
		- ~~~sh
		  mise run logseq:fix-wikilink-labels --help
		  ~~~
