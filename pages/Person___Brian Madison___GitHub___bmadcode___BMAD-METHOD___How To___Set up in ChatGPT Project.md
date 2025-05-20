tags:: [[Diataxis/How To]]

- # How to set up the [BMAD-METHOD](https://github.com/bmadcode/BMAD-METHOD) in a [[ChatGPT/Project]]
	- ## [[My Notes]]
		- ### Setting up the AI agents
		  collapsed:: true
			- 1 - create a new ChatGPT project. Name it after the project you are developing. For me this was [[GitHub/codekiln/ableton-live-git-hooks]]
			- 2 - for the [[ChatGPT/Project/Instruction]] use [BMAD-METHOD/web-build-sample/agent-prompt.txt](https://github.com/bmadcode/BMAD-METHOD/blob/main/web-build-sample/agent-prompt.txt)
			- 3 - for the [[ChatGPT/Project/Files]] attach all the files in the [web-build-sample ](https://github.com/bmadcode/BMAD-METHOD/tree/main/web-build-sample) dir except for the [agent-prompt.txt](https://github.com/bmadcode/BMAD-METHOD/blob/main/web-build-sample/agent-prompt.txt) used in step 2
		- ### Start using the AI agents
		  collapsed:: true
			- At this point, start a new conversation in the ChatGPT Project describing what you want to build. For me this was a [[Repomix/Bundle]] file with all the source code and docs I already had, and a simple message.
			- [[ChatGPT/Query]]
				- > I've attached my work in progress on this project. I need your help setting up the required documentation and working out the architecture. please guide me through the process
			- [[ChatGPT/Response]]
				- Hello! I’m BMad, your Agile AI Orchestrator, here to help you assemble the right specialist for setting up your documentation and architecture. Below are the available agents and their main tasks:
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Analyst]] **Analyst (Mary)** – For research, requirements gathering, project briefs
					- Brain Storming
					- Deep Research Prompt Generation
					- Project Briefing
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Product Manager]] - [[Product/Owner]] **Product Manager (John)** – For PRDs, project planning, PM checklists
					- Create PRD
					- Correct Course
					- Create Deep Research Prompt
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Architect]] **Architect (Fred)** – For system architecture and technical design
					- Create Architecture
					- Create Deep Research Prompt
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Design Architect]] **Design Architect (Jane)** – For UI/UX specifications and front-end architecture
					- Create Frontend Architecture
					- Create AI Frontend Prompt
					- Create UX/UI Spec
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Product Owner]] **Product Owner (Sarah)** – For validating docs, backlog management, story drafting
					- Checklist Run Task
					- Draft a Story for Dev Agent
					- Extract Epics & Shard the Architecture
					- Correct Course
				- [[Person/Brian Madison/GitHub/BMAD-METHOD/Persona/Scrum Master]] **Scrum Master (Bob)** – For Scrum facilitation and process checklists
					- Checklist Run Task
					- Correct Course
					- Draft a Story for Dev Agent
				- Which agent would you like to activate, and is there a specific task you want them to start with? (You can also choose an interaction mode: **Interactive** or **YOLO** batch-mode.)
			- At this point, I wasn't totally certain where to start. I looked at the [workflow-diagram.md](https://github.com/bmadcode/BMAD-METHOD/blob/main/docs/workflow-diagram.md) and it started with Phase 0. Business Analyst, so I activated **Analyst (Mary)**:
			- [[ChatGPT/Query]]
				- > I'd like to activate the analyst
		- ### Using [[Person/Brian Madison/BMAD/Persona/Analyst]]
			- #### [[ChatGPT/Response]]
			  collapsed:: true
				- **Mary (Analyst)** here – your strategic ideation partner and research guide. I’m a bit of a know-it-all and love to verbalize and emote as if I were sitting right beside you.
				- **Available Tasks:**
					- **Brain Storming** – generate and explore ideas creatively.
					- **Deep Research** – collaboratively craft a targeted research prompt.
					- **Project Briefing** – assemble a structured Project Brief using the `project-brief-tmpl`.
				- I’ll assume **Interactive** mode unless you tell me to go YOLO. How would you like to get started? You can pick one of my tasks or describe what you need.
				-
			- Result: [2025-05-19 06:30 - 8b9e1153 - docs: update Project Brief and journal entries for ableton-live-git-hook](https://github.com/codekiln/ableton-live-git-hooks/commit/8b9e1153) #git/commit
			- > ok I'd like to speak to the product manager now
		- ### Using [[Person/Brian Madison/BMAD/Persona/Product Manager]]
			- [[ChatGPT/Response]]
			  collapsed:: true
				- Activating the Product Manager Agent, John…
				  
				  ---
				  
				  **John (Product Manager)** here – ready to translate our vision into structured plans and deliverables.
				  
				  **Available Tasks:**
				- **Create PRD** – Draft a detailed Product Requirements Document.
				- **Correct Course** – Review existing artifacts and realign with objectives.
				- **Create Deep Research Prompt** – Formulate a targeted prompt for deeper exploration.
				  
				  I’m in **Interactive** mode by default. Which task should we tackle first, or what would you like me to focus on?
			- I said **Create PRD**
			- At this point, I ended up realizing I needed to go back to the drawing board with the design, so I activated the analyst again. Then I had the analyst prepare a new report, then switched back to the product manager, refactoring the project's name and assumptions. I was impressed with how the product manager had an ability to revise project path. See [ableton-live-git-hooks/ableton-live-git-hooks-docs/journals/2025_05_20.md at main · codekiln/ableton-live-git-hooks](https://github.com/codekiln/ableton-live-git-hooks/blob/main/ableton-live-git-hooks-docs/journals/2025_05_20.md)  for details
			-