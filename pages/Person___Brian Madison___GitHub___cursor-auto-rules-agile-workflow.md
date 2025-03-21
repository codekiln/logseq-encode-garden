# [GitHub - bmadcode/cursor-auto-rules-agile-workflow](https://github.com/bmadcode/cursor-auto-rules-agile-workflow)
	- ## [[My Notes]]
	  id:: 67dd428f-9c6b-4d20-ab14-188778b80b92
		- I prepared a [[Merge Request]] [Fix spelling errors by codekiln · Pull Request #27 · bmadcode/cursor-auto-rules-agile-workflow](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/pull/27) into this repo to get to know the process. Here are my notes on the process. Similar to [[AI/Coding/Technique/Phased Planning/ai-coding dir]], this repo by [[Person/Brian Madison]] presents a system of [[CursorAI/Project Rules]] that implement an [[Agile]] workflow.
			- ### Workflow Review
				- #### Onboarding
					- I was initially a bit confused by the [introductory material in the root README.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/readme.md?plain=1#L3-L28), which contains important notices to new users before explaining what the repository does.
						- **Note** this does contain a great #Tip that is useful that I've mentioned before at [[CursorAI/How To/update workbench.editorAssociations for mdc to prevent custom editor]]
					- Just skip down to the Overview for more information.
				- #### Installation
					- The root README.md presents two quick start options, [**BOTH** of which rely on](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/readme.md?plain=1#L45-L82) these installation instructions:
						- `git clone https://github.com/bmadcode/cursor-auto-rules-agile-workflow.git`
						- `cd cursor-auto-rules-agile-workflow`
						- `./apply-rules.sh /path/to/your/project`
					- The result of running this against your project:
						- **1**. Copy all template rules to your project's `.cursor/rules/` directory
						  2. Add documentation to `docs/workflow-rules.md`
						  3. Update `.gitignore` to protect "private" rules (individual developer cursor rules that begin with `_` by this project's conventions)
						  4. Preserve any existing rules in your project
				- #### [Overview](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/readme.md#overview)
					- This rule system has a few components. The two most highly visible in the core `README.md` are:
						- ##### Using the agent to author and update custom [[CursorAI/Project Rules]]
							- kind of like [[Person/Geoffrey Huntley/Blog/25/02/You are using Cursor AI incorrectly...]]
							- This repo presents
							- Each type of [[CursorAI/Project Rule]] has a template in `.cursor/templatess/*.md`
								- #Example #PRD template - [cursor-auto-rules-agile-workflow/.cursor/templates/template-prd.md at main](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/.cursor/templates/template-prd.md)
								- I like this method of **standardizing how cursor creates project rules**  by using **configurable templates**. This seems flexible and powerful.
						- ##### Conventions for organizing cursor project rules using a [numerical catalog](https://github.com/codekiln/cursor-auto-rules-agile-workflow/tree/main?tab=readme-ov-file#file-organization) and separating private and public rules
							- This reminds me of the [[Dewey Decimal System]]
								- `0XX`: Core rules and standards
								- `1XX`: Tool and MCP rules
								- `3XX`: Testing standards
								- `8XX`: Workflow rules
								- `9XX`: Templates
								- `1XXX`: Language-specific rules
								- `2XXX`: Framework/library rules
							- I believe I remember reading something in the [[CursorAI/Forum]] about people who tested to see if the agent prioritizes items in numerical order, but I can't seem to find the link.
					- The project structure includes a `docs` dir with a single file - [docs/agile-readme.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/docs/agile-readme.md). This is the [[Agile]] part that's most like my [[AI/Coding/Technique/Phased Planning/ai-coding dir]].
						- In my MR I used it or invoked it like this:
							- > I've just forked this repository and checked out a branch. I've noticed there are a lot of spelling errors. I'd like to use this as an opportunity to try out the agile workflow mentioned in @agile-readme.md. Can you suggest what my first step should be to start an Epic to fix spelling and grammar and Stories for each file?
						- The project rules guided the agent to create a directory structure like this:
							- [.ai](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/tree/e26348726d94a6c1a2ce576358f55494a82b9965/.ai)
								- a #PRD document [prd.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/e26348726d94a6c1a2ce576358f55494a82b9965/.ai/prd.md), possible equivalent of [[AI/Coding/v0/File/2-TICKET-technical-specification.md]] in my workflow
								- an [arch.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/e26348726d94a6c1a2ce576358f55494a82b9965/.ai/arch.md), possible equivalent of [[AI/Coding/v0/File/2-TICKET-technical-specification.md]] which contained a beautiful [[Mermaid Diagram]] that looked like this:
									- ![image.png](../assets/image_1742556555015_0.png){:height 430, :width 122}
							- [epic-1/](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/tree/e26348726d94a6c1a2ce576358f55494a82b9965/.ai/epic-1)
								- [/.ai/epic-1/story-1.story.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/e26348726d94a6c1a2ce576358f55494a82b9965/.ai/epic-1/story-1.story.md)
					- The project structure also includes an `xnotes` directory which is intended to be used for drafting longer prompts to copy andpaste into [[CursorAI/Agent Mode]]. AFAICT this directory is only meant as a tempfile staging area for a human crafting prompts; it's **not critical to read and can be ignored**. Expand this node if you want more info.
					  collapsed:: true
						- this directory is added to [[CursorAI/.cursorindexingignore]] [here](https://github.com/codekiln/cursor-auto-rules-agile-workflow/blob/main/.cursorindexingignore) and **also** added to [[.cursorignore]] [here](https://github.com/codekiln/cursor-auto-rules-agile-workflow/blob/main/.cursorignore).
							- **Side-note**: I'm both relieved and dismayed to see others adding the same paths to both files. I've argued for better documentation on when people should use one vs the other in [[CursorAI/Forum/24/12/Questions on .gitignore, .cursorignore, .cursorban]] [here](https://forum.cursor.com/t/questions-on-gitignore-cursorignore-cursorban/34713/16?u=codekiln).
						- This directory contains a few things for an [[Agile]]-like workflow with project rules.
							- [xnotes/801-workflow-agile.mdc](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/xnotes/801-workflow-agile.mdc) is a cursor project rule which describes the relationship between files used in coding. AFAICT this isn't actually in use, because it's not in the right directory; perhaps it's a draft.
							- [xnotes/workflow-agile.md](https://github.com/bmadcode/cursor-auto-rules-agile-workflow/blob/main/xnotes/workflow-agile.md) looks like another take at the agile workflow. Again, this isn't in the proper cursor rules directory, so the only way to reference it is to at message it.
	- ## [[see-also]]
		- [[Person/Brian Madison/YouTube/25/02/Unlock Cursor AI Automatic Rule Generation]] which is a video overview of this