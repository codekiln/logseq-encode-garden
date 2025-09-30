- [[Person/codekiln]] [[2025-09-29 Mon]]
	- Each project usually requires a combination of shared and project-specific rules.
	  
	  For example, some of my projects use rules and commands that are specific to the context of FastAPI. Others, use rules and commands specific to the context of typescript CLIs. I don't need all of my rules and commands in each project.
	  
	  Ideally, it would be possible to define my rules for technology A, e.g. FastAPI, in one repo, my rules for technology B, e.g. TypeScript in another repo, and my rules for technology C, e.g. EnterprisePrivateTechnology in another private repo, and just marshal those rules into the current repo and then use `rulesync` to spread those out to the various providers.
	  
	  One possible solution could be to use git submodules, but those may have problems:
	- in CI, if you have private repos, authentication permissions can get tricky with git submodules.
	- it's not clear that rulesync would support subdirectories needed for git submodules
	  
	  So, let's talk about what possible solutions are out there for this use case.
- [[Person/codekiln]] [[2025-09-30 Tue]] [here](https://github.com/dyoshikawa/rulesync/issues/329#issuecomment-3351131340) - #Idea about [[Context Engineering]]
  id:: 68dbb819-d57c-4e8c-89c8-ffd781928be9
	- > I guess, by resolving [#304](https://github.com/dyoshikawa/rulesync/issues/304), your request will also resolved at least partially.
	- Yes, I think the `--global` feature support will help individual developers not be as repetitive, for sure. But in my opinion, the larger problem is that engineering teams need a way to standardize and encapsulate their best practices (rules, commands, etc) across developers.
	- ## Side rant about context bloat in agentic coding tools
		- Today's AI coding tools work by requiring a developer to pre-load all the context the AI would need to know before starting the AI to work (rules files) or by at least loading an MCP server that connects the agent to additional docs. Each additional rule file and MCP server tool adds to the context burden, which leads to [context rot](https://research.trychroma.com/context-rot).
		- I have yet to see an agentic coding tool which can onboard **and offboard** context dynamically based on its runtime needs, but in my opinion, as a practical concern, the effective context limits I'm observing are not universally increasing fast enough to keep up with the complexity of engineering tasks, and I think we may need to try to find ways for an AI to know how to find where it should load rules and commands for a specific situation from.
		- For example, the techniques for doing json logging with OTEL in python under uwisgi have particular difficulties relative to doing json logging with OTEL in typescript under express. It's not that the problems are unrelated, but the challenging parts tend to be at the intersections between the technologies, where the context needs to get really specific. If agentic coding tools could know where your team has documented the AI instructions for these things and could ask you if it could do a brain dump for that problem's solutions ...
		- {{video https://www.youtube.com/watch?v=N5b4_5hvOog}}
		- ... and then later, offload that context so that the local repo isn't filled with bloat that's superfluous to 95% of the coding you're going to do there, it seems like that would be more optimal.
		- I sense that agentic coding tools may temporarily need something like the breakthrough that happened in GIS that led to google maps with the tile pyramid or image pyramid: if you have a problem that requires you to zoom in, you load different, zoomed in context (images, or in our case, rules and commands) that are suitable for that level of detail, and then, when you need to see where you're at, evaluate and change position, you have the AI zoom out, load in a different, zoomed out context (images, or in our case, rules and commands).
		- This is similar to what Lance Martin talked about on a recent [[Latent Space/Pod]]:
		  id:: 68dbb8b4-6466-4c91-be62-4b9b3c16c76e
			- > “What worked really well for me was just passing a simple markdown file—basically a list of docs with URLs and short descriptions—to the code agent. Then it can just grab the right doc and read it when needed. I actually use this all the time, and I don’t even bother with vector store indexing anymore. My go-to is [[llms.txt]] with a simple search tool and [[Claude Code]].” -- #Quote from [[Person/Lance Martin]], [[LangChain/Team]], [Context Engineering for Agents on latent.space podcast](https://youtu.be/_IlTcWciEC4?list=PLWEAb1SXhjlfkEF_PxzYHonU_v5LPMI8L&t=1155)
	- ## How does this impact   `rulesync` ? One option to consider ...
		- What if rulesync supported local proxy files which were like local symlinks to remote assets, and then during the generate step it could "unmarshall" that locally.
		- In the `.rulesync/{commands, rules, subagents}/*.md`'s yaml frontmatter, you could support a yaml key like `remote` which could have a pointer to where the command/rule/subagent definition was located, whether that's a webpage on the internet or whether that's a file in another github (or gitlab, or any SCM) repo. Then upon `rulesync generate`, it would create the file.
	- ## Side-note - Marshalling ver Unmarshalling
		- > **Marshalling** is the process of transforming an in‑memory object (including its structure, values, and reference relationships) into a data format suitable for storage or transmission so it can cross process/runtime/boundary lines [Wikipedia, *Marshalling (computer science)*](https://en.wikipedia.org/wiki/Marshalling_%28computer_science%29).
		- > **Unmarshalling** is the reverse: decoding that stored or transmitted representation back into a live in‑memory object, restoring types, references (where possible), and structure [Wikipedia, *Serialization*](https://en.wikipedia.org/wiki/Serialization).
		- Here, the equivalent of "marshalling" would be storing a rule / command / subagent definition in its canonical location, for example, in a knowledge base or canonical repo of best practices for an enterprise, and "unmarshalling" would be making making those pieces of remote context available to the AI coding agent.
	- ## Towards the future
		- Perhaps rulesync could define and support a particular kind of MCP server which would know about a particular structure of a repository of agentic coding tool definitions, and then it could make that MCP server available to the coding agent, so the agent could name the things it wants in its context and load those things into context.
		- Essentially, static context is dead; we need a river of context that changes with the problem.