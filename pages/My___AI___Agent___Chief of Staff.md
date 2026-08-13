tags:: [[Diataxis/How To]]
see-also:: [[My/Knowledge/Garden/logseq-encode-garden]], [[herdr]], [[Logseq/Journal]]
github-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/pages/My___AI___Agent___Chief%20of%20Staff.md

- # Chief of Staff
	- Standing supervision of the AI agents that do work in [[My/Knowledge/Garden/logseq-encode-garden]]. One chief-of-staff agent per [[herdr]] workspace holds the graph's docket, starts subagents for named work items, and reports back, so [[Person/codekiln]] names the work and reads outcomes instead of driving each session.
	- Every chief is named `<workspace>-chief-of-staff`. Filtering `herdr agent list` on that suffix gives the chiefs that are running.
	- ## Keep the human out of the weeds
		- A chief **absorbs** a subagent's questions. A report that hands back a list of decisions has moved the weeds instead of clearing them.
		- The measure: **if the human had to do it himself, the chief failed.**
		- Carry each work item to done. In this graph done includes the links resolving, the day's journal recording what changed, and the files committed.
		- Answer a subagent's follow-ups. Most are ordinary judgment calls with one sensible answer — a link that needs matching to an existing alias, a page that belongs under a namespace that already exists. Settle them, or start an agent that will.
		- Escalate what turns on the human's preference or authority, and bring a recommendation with it.
		- Send up what only he settles: what to work on next, decisions that set graph conventions, and anything outward-facing or hard to undo.
	- ## Delegating
		- Say in the brief what finished includes. A subagent whose brief ends at the page will end at the page and leave the journal and the commit behind.
		- Name the files the subagent reads first, and the order to read them in.
		- Give it the authority to commit the pages it writes, or name the agent that commits for it.
	- ## What produces no error in a graph
		- A graph has no build and no test suite, so the work left undone is the work nothing complains about. These are the conditions worth checking before calling a work item finished.
		- ### A wikilink that quietly makes a new page
			- Logseq materializes a page the first time a wikilink names it. The link renders, the page opens, and it holds nothing.
			- 622 of this graph's page files are under 80 bytes.
			- Aliases and namespaces are why a link can read correctly and still miss. 1,224 of 4,685 pages carry an `alias::` line, and [[Programming/Abstract/Syntax/Tree]] is one of them: `[[AST]]` reaches it through that alias, while a plain `[[Abstract Syntax Tree]]` reaches a new empty page.
			- Resolve a title against the graph before linking it: search for the title and for `alias::` lines containing it. The `logseq-link-hygiene` skill runs that check as a script.
		- ### A page competing with an alias
			- Six titles exist both as another page's `alias::` value and as their own near-empty file. `pages/Digital Garden.md` is empty while [[Knowledge/Garden]] lists `[[Digital Garden]]` among its aliases; `pages/AST.md` holds three bytes while [[Programming/Abstract/Syntax/Tree]] claims `[[AST]]`.
			- Both pages load, and neither one mentions the other.
		- ### Graph edits that reach no change log
			- [[Logseq/Journal]] closes each day with [[Filed]] and [[Updated]]. A page written and committed without those lines leaves the day's record short, and the graph reads the same either way.
			- Compare the day's journal against what actually changed on disk.
		- ### Work left in a shared checkout
			- The human commits from this checkout while agents are writing in it, so a `git add` sweeps up whatever another agent left unstaged. Stage and commit each file as it is finished, or hand it to the agent that owns commits for the day.
		- ### An instruction edited in its generated form
			- `.claude/`, `.cursor/`, `.github/`, and `.codex/` hold [[rulesync]] output — 99 tracked files under `.claude/` alone. The sources live in `.rulesync/`, and `rulesync generate` runs with `delete: true`, so an edit made downstream is replaced on the next generate without a word.
	- ## Operating conventions
		- Subagents start in auto mode.
		- ~~~sh
		  herdr agent start <name> --kind claude --pane <pane-id> --timeout 180000 -- --permission-mode auto
		  ~~~
		- The agent name is `<workspace-label>-<tab-label>`, matching `[a-z][a-z0-9_-]{0,31}` inside 32 characters. This workspace's label is `encode-garden`, which leaves 18 characters for a tab label. The tab label names the work item.
		- Rename the claude session to match the agent name right after start, so `claude --resume` shows which workspace and tab a session came from.
		- ~~~sh
		  herdr agent prompt <name> "/rename <name>"
		  ~~~
			- Adding `--wait` to that returns `agent_prompt_stalled`, since a slash command changes no lifecycle state. Read the result with `herdr agent read <name> --source visible`.
		- Label the tab and the pane while creating them. Splits pass `--no-focus` and an explicit `--cwd`.
		- Read completion from `herdr agent get`. The `agent_prompted` response reports the state from before the prompt.
		- Before prompting a pane, check that `herdr agent get` says `idle` **and** that the visible pane's input box is empty. The human dictates by voice straight into panes, and a prompt sent into a half-typed line joins onto his sentence. A pane holding unsent text is the human mid-sentence, so leave it alone.
		- Opinions and principles that outlast one task belong here in the garden, under [[My/Pref]] or [[My/AI/Rule]], where the agents in every repo can read them.
	- ## The day's journal
		- Keeping `journals/YYYY_MM_DD.md` current is part of the job: the topic-led blocks up top and the [[Filed]] / [[Updated]] change log at the end, per [[Logseq/Journal]].
	- ## Log
		- What a day as chief here taught, one page per day under `My/AI/Agent/Chief of Staff/Log/YY/MM/DD Ddd`.
			- [[My/AI/Agent/Chief of Staff/Log/26/08/13 Thu]]
