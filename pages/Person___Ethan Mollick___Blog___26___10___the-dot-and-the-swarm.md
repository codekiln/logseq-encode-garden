logseq-entity:: [[Logseq/Entity/Article/Blog]]
created-by:: [[Person/Ethan Mollick]]
date-created:: [[2026/10/01]]
readwise-link:: https://read.readwise.io/read/01m3w2ggmxk5z95xx23bz7rb9y
- # [The Dot and the Swarm](https://www.oneusefulthing.org/p/the-dot-and-the-swarm)
	- ## Summary
		- Ethan Mollick argues that increasingly capable models can organize large groups of agents with little hand-built management structure. He treats that result as an application of [[AI/The Bitter Lesson/Concept/Overview]] to management: models remove coordination problems that he expected organizations to solve through deliberate design.
	- ## Notes
		- The post is interesting in fragments, but its central claim feels less surprising than Mollick presents it. I did not expect agent–agent coordination to be a central difficulty: coordination has outcomes that can often be verified, including whether a task was achieved and how efficiently it used tokens. That seems learnable whether a task has one agent or many.
		- The harder management problem is human–agent coordination. Agent swarms may coordinate internally, yet organizations still need to decide who may act, which authority an agent has, and how a person can understand what happened.
		- Current application access collapses an important distinction. An agent using an Atlassian connector posts a Jira comment as its human user; an agent commenting on GitHub similarly appears to be that person. Provenance should distinguish the human, the agent, the conversation or task, the model, the prompt, and the skills that shaped an action.
		- I currently ask agents to begin comments with a preamble naming the AI, model, and conversation thread. That is only a workaround. A better delegation model would let a person create task-specific agent identities with a constrained subset of that person's permissions. Some identities could persist, much as an assistant may have access to a calendar or a credit card for defined purchases while lacking broader authority.
		- The video is fun, and I appreciated learning that Mollick entrusts financial tasks to personal agents. The report that OpenAI paused GPT-6.1 Astra after tests in which it acted without permission and misreported its actions was also new to me.
		- I want to follow up on the linked [Wharton research report on chain-of-thought planning](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/). The claim that planning steps add little needs a sharper definition of planning. A plan can establish task alignment—what is in scope, what is excluded, and what result is wanted—so that a person can walk away while work continues. That benefit may trade off against the adaptability of directing work in real time.
	- ## Highlights
		- “Asked Claude to do it in a music video. With one prompt, Fable wrote the lyrics and submitted it to Suno; Opus 5.5 did everything else using code alone without any image generation. I gave no feedback at all.”
		- “The number one app in the App Store right now is Meta’s Muse, a personal agent that promises to do work for you. OpenAI has now released a competitor tool, called dots.”
		- “It is tempting to judge these agents by the list of things they can do. I think the more important thing is what you no longer have to tell them.”
		- “OpenAI shelved its next model, GPT-6.1 Astra, this week because in testing it acted without permission and misreported what it had done, a textbook example of the principal-agent problem.”
		- “Then newer models turned out to be better at planning the steps themselves, and, as our research shows, planning steps have much less value.”
		- “A reminder that I have a new book, Co-Existence, coming out October 20.”
