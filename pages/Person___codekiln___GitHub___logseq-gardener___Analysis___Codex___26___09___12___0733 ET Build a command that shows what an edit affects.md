author:: [[Codex]]
see-also:: [[Person/codekiln/GitHub/logseq-gardener/Project/Brief]]
- # Build a command that shows what an edit affects
	- I would build `garden impact`: a command that tells someone editing a garden which links, page names, and block relationships their changes affect. A person or coding agent runs it after saving an edit and before committing, to find consequences that are easy to miss in the changed lines alone.
	- ## Who uses it and what the command does
		- A person edits a page in Neovim or Logseq, runs the command, and follows the reported source links to check affected notes. For example, removing an alias from one page can change where a journal link leads, even though the journal has no changed lines in Git.
		- A coding agent calls the same command in its worktree after editing. The result helps it find references that also need changing before presenting its work to the person.
		- The command uses garden-core to compare the graph at a chosen Git revision with the current saved files. Ordinary program code calculates the differences. The person or coding agent decides whether those differences are wanted and what to edit next.
		- ~~~text
		  Person or coding agent saves an edit
		                  |
		                  v
		       garden impact --base HEAD
		                  |
		       +----------+-----------+
		       |                      |
		       v                      v
		  Read files at HEAD     Read saved files
		       |                      |
		       v                      v
		  Resolve old links      Resolve current links
		       |                      |
		       +----------+-----------+
		                  |
		                  v
		  Report changed targets and affected source lines
		                  |
		                  v
		  Person or coding agent decides what to do next
		  ~~~
	- ## Example: removing an alias changes an unchanged journal
		- Suppose a page called Studio declares Workshop as an alias, and a journal uses that alias. Removing the declaration leaves the journal's spelling untouched, but the link now names a separate, fileless Workshop page.
		- ~~~text
		  Before the edit:
		  Journal -- link named Workshop --> Studio
		                                     alias: Workshop
		  After removing the alias from Studio:
		  Journal -- link named Workshop --> Workshop
		                                     no content file
		  Report:
		  Changed declaration: Studio's alias property
		  Affected reference:  the journal's Workshop link
		  Previous target:     Studio
		  Current target:      reference-only Workshop page
		  ~~~
		- The person can keep that result, restore the alias, or change the journal to link to Studio. The command makes the consequence visible and points to the relevant lines; the desired relationship is the author's choice.
	- ## Example: indentation changes which note a block belongs to
		- Moving a note about a deadline from one project to another can be a meaningful change even when every link still resolves. The command should show the changed parent, without calling the move a mistake.
		- ~~~text
		  Before:                    After:
		  Project Alpha              Project Alpha
		    Deadline: Friday         Project Beta
		  Project Beta                 Deadline: Friday
		  Report: Deadline: Friday moved
		          from Project Alpha to Project Beta
		  ~~~
		- Matching a moved block is dependable when it carries the same explicit UUID. If repeated text makes an ID-less block hard to match, the output should say that the match is uncertain.
	- ## What to build first
		- Begin with alias changes and links whose targets change. `garden impact --base HEAD` produces a readable report with file and line links; `--json` supplies the same findings to scripts and coding agents. Both forms identify the compared revisions and report when the graph could not be fully read.
		- Compare complete old and current graphs on small fixtures before optimizing. Report changes introduced by the edit separately from problems already present. Add removed block IDs, their callers, and changed parents when block parsing is ready.
		- The initial command reads saved edits and leaves files alone. Later, a proposed rename or move could be evaluated in memory, allowing the caller to see the effects before writing.
	- ## Why build this before automatic merging
		- Fable's [[Person/codekiln/GitHub/logseq-gardener/Analysis/Fable/26/09/12/0658 ET A Logseq-aware git merge driver before a CRDT]] proposes matching ID-less blocks by parent path and content. Repeated siblings, rewording, and subtree moves can make that match ambiguous.
		- An impact report lets someone inspect those matches and their consequences before the same matching code is allowed to combine edits automatically. The command is also useful on ordinary edits that never involve a merge.
		- The practical test is whether the report helps a person find affected notes they would otherwise have missed. Check examples from this garden's history, require source locations for findings, and compare optimized results with a full rebuild.
