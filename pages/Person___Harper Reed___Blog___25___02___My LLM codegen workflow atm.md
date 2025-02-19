tags:: [[AI/Coding]]
:LOGBOOK:
CLOCK: [2025-02-19 Wed 03:51:26]
:END:

- # DONE [My LLM codegen workflow atm | Harper Reed's Blog](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)
	- ## #notes
		- Awesome overview of a CLI-centric workflow for AI coding. solid advice.
		  id:: 67b5b920-e30f-48db-8a1a-8faa0d8f8b41
			- particular emphasis on using
				- [[mise]]
				- [[aider]]
				- [[llm-cli]]
				- [[Repomix]]
	- > tl:dr; Brainstorm spec, then plan a plan, then execute using LLM codegen. Discrete loops. Then magic. ✩₊˚.⋆☾⋆⁺₊✧
	- ## [[Greenfield Coding]] code dev (~15 min)
		- ### Step 1 - requirements elicitation - have #4o or #o3 interview you for the requirements
			- have it prompt you to have a requirements elicitation session, asking you one question at a time
			- at end of brainstorm, ask it to compile findings into a `spec.md` in root of repo
		- ### Step 2 - todo checklist - have #[[LLM Reasoning Model]] use `spec.md` to create `todo.md`
			- #TDD #Prompt
				- ```
				  Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.
				  
				  From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step in a test-driven manner. Prioritize best practices, incremental progress, and early testing, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.
				  
				  Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.
				  
				  <SPEC>
				  ```
			- non-TDD #Prompt
				- ```
				  Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. review the results and make sure that the steps are small enough to be implemented safely, but big enough to move the project forward. Iterate until you feel that the steps are right sized for this project.
				  
				  From here you should have the foundation to provide a series of prompts for a code-generation LLM that will implement each step. Prioritize best practices, and incremental progress, ensuring no big jumps in complexity at any stage. Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step.
				  
				  Make sure and separate each prompt section. Use markdown. Each prompt should be tagged as text using code tags. The goal is to output prompts, but context, etc is important as well.
				  
				  <SPEC>
				  ```
			- #Prompt to generate todos
				- ```
				  Can you make a `todo.md` that I can use as a checklist? Be thorough.
				  ```
		- ### Step 3 - coding - complete tasks in `todo.md`
			- success depends on step 2
			- could work with [[CursorAI]] or any other tool
			- prefers raw [[Claude]] and [[aider]]
			- #Claude
				- [[AI/Coding/Tip/Have a solid foundation with Language, Style and Tooling]]
					- > Claude has a tendency to just output react code - and having a solid foundation with the language, style, and tooling of your choice will help quite a bit.
				- use #Repomix to iterate when things get stuck
				- workflow
					- set up the repo (boilerplate, uv init, cargo init, etc)
					- paste in prompt into claude
					- copy and paste code from claude.ai into IDE
					- run code, run tests, etc
					- …
					- if it works, move on to next prompt
					- if it doesn’t work, use repomix to pass the codebase to claude to debug
					- rinse repeat ✩₊˚.⋆☾⋆⁺₊✧
			- #aider
				- works well with `todo.md` from **Step 2** above
				- essentially the same workflow as with Claude above
					- instead of pasting into claude, paste into aider
					- then play [[Game/Video/Cookie Clicker]] #LOL
				- > *An aside: Aider does really great benchmarking of new models for codegen in their *[LLM leaderboards](https://aider.chat/docs/leaderboards/)*. I find it to be a really great resource for seeing how effective new models are.*
	- ## [[Brownfield Coding]] - generate `output.txt` with #Repomix and process with #mise tasks
		- > I have a task collection defined in my global `~/.config/mise/config.toml` that allows me to do various things with my code base ([mise rules](https://mise.jdx.dev/)).
		- ### #note
			- #love
				- tasks are defined in a way that's agnostic to the programming language and is outside of the repo
				- CLI-centric for re-usability. much more widely applicable than [[CursorAI/Project Rules]]
		- #### [[AI/LLM]] task list
			- `LLM:clean_bundles` aka **generate bundles**
				- Generate LLM bundle `output.txt` using #Repomix
				- [[AI/Coding/Tip]]
					- > If I am blowing through tokens, and it is too big - I will edit the generate command to ignore parts of the code base that are not germane to this task.
					- > *One thing really nice about *`mise`* is that the tasks can be redefined and overloaded in the working directory’s *`.mise.toml`*. I can use a different tool to dump/pack the code, and as long as it generates an *`output.txt`* I can use my LLM tasks. This is helpful when various codebases differ so much. I regularly override the *`repomix`* step to include broader ignore patterns, or just use a more effective tool to do the packing.*
			- `LLM:copy_buffer_bundle`
				- Copy generated LLM bundle from `output.txt` to system clipboard for external use
			- `LLM:generate_code_review`
				- Generate code review output from repository content stored in `output.txt` using LLM generation
			- `LLM:generate_github_issues`
				- Generate GitHub issues from repository content stored in `output.txt` using LLM generation
			- `LLM:generate_issue_prompts`
				- Generate issue prompts from repository content stored in `output.txt` using LLM generation
			- `LLM:generate_missing_tests`
				- Generate missing tests for code in repository content stored in `output.txt` using LLM generation
			- `LLM:generate_readme`
				- Generate `README.md` from repository content stored in `output.txt` using LLM generation
		- Once the `output.txt` is generated, I pass it to the [[llm-cli]] command to do various transformations and then save those as a #Markdown file, something like:
			- `cat output.txt | LLM -t readme-gen > README.md`
			- `cat output.txt | LLM -m claude-3.5-sonnet -t code-review-gen > code-review.md`
		- example workflow
			- #Claude
				- go to the directory where the code lives
				- run `mise run LLM:generate_missing_tests`
				- look at the generated markdown file (`issue-prompts.md`)
				- grab the full context for the code: `mise run LLM:copy_buffer_bundle`
				- paste that into claude along with the first missing test “issue”
				- copy the generated code from claude into my ide.
				- …
				- run tests
				- rinse repeat ✩₊˚.⋆☾⋆⁺₊✧
			- #aider
				- go to the directory where the code lives
				- run aider (always make sure you are on a new branch for aider work)
				- run `mise run LLM:generate_missing_tests`
				- look at the generated markdown file (`issue-prompts.md`)
				- paste the first missing test “issue” into aider
				- watch aider dance ♪┏(・o･)┛♪
				- …
				- run tests
				- rinse repeat ✩₊˚.⋆☾⋆⁺₊✧
		- ### [[AI Coding Tips]] for legacy codebases
			- > These prompts are pretty old and busted (“boomer prompts” if I may). They need some refactoring. If you have ideas to make them better lmk.
			- #### #Prompt for [[Code Review]]
				- You are a senior developer. Your job is to do a thorough code review of this code. You should write it up and output markdown. Include line numbers, and contextual info. Your code review will be passed to another teammate, so be thorough. Think deeply  before writing the code review. Review every part, and don't hallucinate.
			- #### #Prompt for generating [[GitHub/Issue]]
				- *note - issue posting is not automated yet*
				- You are a senior developer. Your job is to review this code, and write out the top issues that you see with the code. It could be bugs, design choices, or code cleanliness issues. You should be specific, and be very good. Do Not Hallucinate. Think quietly to yourself, then act - write the issues. The issues will be given to a developer to executed on, so they should be in a format that is compatible with github issues
			- #### #Prompt for identifying [[Missing Tests]]
				- You are a senior developer. Your job is to review this code, and write out a list of missing test cases, and code tests that should exist. You should be specific, and be very good. Do Not Hallucinate. Think quietly to yourself, then act - write the issues. The issues  will be given to a developer to executed on, so they should be in a format that is compatible with github issues
	- ## Reflections
		- ### [[Phrase/Over One's Skies]]
			- > When I describe this process to people I say “you have to aggressively keep track of what’s going on because you can easily get ahead of yourself.”
			- > For some reason I say “over my skies” a lot when talking about LLMs. I don’t know why. It resonates with me. Maybe it’s because it is beautiful smooth powder skiing, and then all of a sudden you are like “WHAT THE FUCK IS GOING ON!,” and are completely lost and suddenly fall off a cliff.
		- ### LLM coding is largely Single-player
			- My main complaint about these workflows is that it is largely a solo endeavor - i.e. the interfaces are all *single player mode*.
			- I have spent years coding by myself, years coding as a pair, and years coding in a team. It is always better with people. These workflows are not easy to use as a team. The bots collide, the merges are horrific, the context complicated.
			- I really want someone to solve this problem in a way that makes coding with an LLM a multiplayer game. Not a solo hacker experience. There is so much opportunity to fix this and make it amazing.
		- ### haterade
			- > My main fear is about power consumption and the environmental impact. But… the code must flow. Right… sigh.
			- > If you are open to learning more, but don’t want to dig in and become a cyborg programmer - recommendation - read [[Book/Co-Intelligence]] by [[Person/Ethan Mollick]]