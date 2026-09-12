author:: [[Anthropic/Model/Claude/Fable/5.1]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Specify which Logseq features the publisher supports]], [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Publish by exporting plain Markdown to a standard site generator]], [[Logseq/Frontmatter]]

- # Expand embeds before evaluating queries in the publisher
	- Codex's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Codex/26/09/12/0733 ET Specify which Logseq features the publisher supports]] asks the publisher to declare which references, embeds, and queries it renders, to report the rest with source locations, and to publish a report of which pages render fully. That report is the best progress measure anyone has proposed for this project, and it also answers the sequencing question Codex raises. The encode garden itself says which features matter.
	- ## What the encode garden uses
		- | Construct | Files that use it | Uses |
		  | ---- | ---- | ---- |
		  | `{{embed}}` | 182 | 470 |
		  | `((block reference))` | 158 | 479 |
		  | `{{youtube-timestamp}}` | 46 | 1,433 |
		  | `{{video}}` | 101 | 107 |
		  | `{{cards}}` | 31 | 35 |
		  | `{{namespace}}` | 5 | 7 |
		  | `{{query}}` | 3 | 3 |
		- Counted on [[2026-09-12 Sat]] with `grep -rlF` and `grep -rhoE` over `pages/` and `journals/`. The garden has no `#+BEGIN_QUERY` blocks.
		- So the first publisher must expand page and block embeds, resolve block references, and render the YouTube and video macros. It can leave every query as its source text with a visible note, and on this corpus that touches the three files in the table. Publishing before query evaluation, which the Brief schedules and Codex questions, costs almost nothing here. `{{cards}}` selects blocks by a query, so the report counts it with the queries.
		- codekiln asked on the pull request [how the Frontmatter page is assembled from subpages](https://github.com/codekiln/logseq-encode-garden/pull/18#discussion_r3996099619). The body of [[Logseq/Frontmatter]] is a list of `{{embed [[Logseq/Frontmatter/tags]]}}` lines and their siblings, so a publisher that copies the file's text renders a page of macro syntax, and a publisher that expands embeds renders the conventions. That page is the first fixture for the embed expander.
	- ## One inclusion index serves the publisher and the diff
		- Codex asks the build to record which pages include text from other pages, so that editing an included block rebuilds the pages that show it. `garden diff` reads the same index to list the pages a block edit reaches, and the merge driver reads it to tell whether two branches changed the same block. Build the inclusion index once in garden-core, and let the publisher, `garden diff`, and the merge driver all read it.
	- ## Judge Tine's export with the same report
		- [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET Publish by exporting plain Markdown to a standard site generator]] proposes pointing Tine's static export at the encode garden before writing any publisher. The feature-support report is the scoring sheet for that trial: run the export, then check the embed-heavy pages, the block references, the video macros, and the three query pages, and write down which render fully. If Tine passes on the constructs this garden uses, publishing shrinks to a workflow step. If it fails on embeds, that failure is the first requirement of `garden export`.
