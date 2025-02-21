tags:: [[Idea]]

- # Using [[CursorAI/Project Rule]] with the [[GitHub/CLI]] for an AI-Assisted SLDC
- ## Impetus
	- Most of the use cases for Cursor that are seen on web are about using CursorAI for coding.
	- Many advanced uses of Cursor require up-front planning about the design of the feature; see also [[CursorAI/Technique/Frontload Design]]. Recently, several Cursor templates have also tried to bake-in a light, text-based project management approach, for example, see [[Person/John Nathaniel Marquez]]'s project, [[GitHub/T1nker-1220/NEW-PROJECT-RULES-ULTRA-CONTEXT-FOR-AI-MEMORIES-LESSONS-SCRATCHPAD-WITH-PLAN-AND-ACT-MODES]] or [[Person/Max Fahl]]'s project, [[GitHub/maxfahl/cursor-agent-master-prompt]]. These experiments are cool and they point to how the system benefits from creative thinking. **But why don't we take it one step further and make Cursor actually utilize a remote project management system via CLI commands?**
	- Cursor could be more helpful if it could be more of a software engineer, interacting with the SLDC project management artifacts as a whole. Here I'll focus on GitHub's project management capabilities and CLI, but the same principles could be applied to [[Gitlab/CLI/glab]] or to [[JIRA/CLI]] with [[GitHub/ankitpokhrel/jira-cli]] as the project management software of choice.
	- To begin with, Project Rules can help Cursor's Agent Mode with:
		- drafting [Github Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) and Sub-Isssues
			- plan what needs to be done
		- [Using labels and milestones to track work - GitHub Docs](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work)
			- organize when to do what and answer queries about the repo
		- maintaining issue statuses on the [Github Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
		- checking out issues in a branch
		- submitting a well-formed merge request with a great description that references the issue(s) it closes
		- checking on status of github actions
	- This page proposes an idea for how to create reusable, agential workflows for SLDC automation using Cursor Project Rules.
- ## Project Rules for wrapping `gh`
	- When using [[CursorAI/Agent Mode]], the agent can read [[CursorAI/Project Rule]] to craft CLI command invocations for the GitHub CLI, `gh`. A lot of information about this CLI is likely already in the training data, but Project Rules may let users focus the AI's attention on the details about how to use it in an AI-assisted [[Software/Engineering/Development Life Cycle (SLDC)]] and specifically within the context of Cursor.
	- A centerpiece of this approach is that rather than explicitly saying what should be done in the composer chat, the [[Product Requirements Document]] should most likely be specified in a external project management software like a GitHub issue.
	- ### Defining the [[PRD]] in the [[GitHub/Issue]]
		- A project rule `gh-issue-update.mdc` rule could be created to help with the ideating phase of the issue. Perhaps a [[GitHub/Project]] `status` could be applied to the issue to signal that it is in a design phase.
		- A draft issue can be created as a markdown issue, and [[GitHub/CLI/gh/issue/create]] can create an issue when it's time, or [[GitHub/CLI/gh/issue/edit]] could edit an issue if it needs to be updated.
	- ### Checking out a [[GitHub/Issue]] to work on it
		- [[GitHub/CLI/gh/issue/develop]] can check out a branch from another branch, and link the branch to the issue. The new branch will be configured as the base branch for pull requests created using  [[GitHub/CLI/gh/pr/create]].
		- A project rule could be created, `gh-issue-develop.mdc`, which describes how to use the CLI to do this, and when it should be activated. Then a developer could explicitly ask to start working on an issue, and the Agent would suggest the command needed to do that.
	- ### Downloading [[GitHub/Issue]] into local assets so the Cursor agent can work on it
		- Whether or not an issue was drafted locally, it probably makes sense to make sure the most recent version of the issue is available locally so the agent can work on it.
		- A project rule could be created, `gh-issue-refresh.mdc` which uses [[GitHub/CLI/gh/issue/view]] to download [[GitHub/Issue]]s to [[Markdown]] files locally. It may make sense to highlight this as the active issue to be worked on.
		- It might make sense to have a cache of open issues assigned to the current user, organized by status, for example, something like:
		- ```
		  .gh/
		    pr/
		      in-progress/
		        43/
		          pr-43-description.md
		          pr-43-comments.md
		      completed/
		        (... similar to above)
		    issue/
		      in-progress/
		        23/
		          issue-23-description.md
		          issue-23-comments.md
		      completed/
		        (... similar to above)
		  ```
		- I get the sense that the in-progress items would be be useful if committed to the branch, but `.gh/completed/` would be in `.gitignore` and could be regularly purged from the local cache.
	- ### Creating a [[GitHub/PR]]
		- Authoring a merge request requires several steps:
			- creating a focused merge request description
			- running tests
			- pushing
			- checking CI results
			- ...
		- In particular, a `gh-pr-draft.mdc` could draft a merge request description, and  `gh-pr-create.mdc` could create the merge request using [[GitHub/CLI/gh/pr/create]].
	- The ideas here are by no means a complete list of the [[SLDC]] items that could be automated with project rules, but they are a good start for understanding what's possible.
- ## Reusing `gh` Project Rules Across Multiple Projects
	- So far, early testing seems to indicate that subdirectories of [[CursorAI/.cursor/rules]] may be scanned for `.mdc` files. As a result, it may be possible to use [[git/submodule]]s to pull in a standard set of `gh-cursor` project rules. This would enable an entire team to have a similar set of affordances for mapping Github SLDC operations on to Cursor.
- ## Association between custom scripts and custom project rules
	- In time, it may make sense to have some scripts that are associated with the stages of the SDLC and which constrain the github CLI actions that are taken, so as to increase consistency and decrease the number of tokens needed to figure out what to do.
	- Perhaps a framework like [[FabricAI]] could be useful, although I haven't approached that yet.
	- Alternatively, a [[Python/Package]] or [[Programming/Language/Go]] package could be included which is expected to be used by the project rules.
- ## Scratchpad
	- The repository for this shared set of project rules could have a .gitignored scratchpad directory for placing intermediate context.
	- In fact, it may even in time be useful to have a [[Logseq]] directory and use project rules to fill out a knowledge graph about the world using that. An exciting side-effect of this is that the Logseq UI could be able to browse the "thoughts" that the AI added to its knowledge base, and even edit them. Logseq lends itself well to this, since its use of namespaces could be facilitated by [[AI/LLM/Technique/Hierarchical Summarization]].