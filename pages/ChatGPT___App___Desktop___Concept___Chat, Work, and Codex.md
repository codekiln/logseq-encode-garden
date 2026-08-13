tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]

- # Chat, Work, and [[Codex]] in the ChatGPT app
	- ## Overview
		- As of August 2026, OpenAI presents [[ChatGPT/Chat]], [[ChatGPT/Work]], and [[Codex]] within one [[ChatGPT/App/Desktop]]. Its [official overview](https://learn.chatgpt.com/) describes Chat for conversation, Work for finished general-purpose deliverables, and Codex for software development.
		- The name **ChatGPT** refers to two levels: the overall application and the general-purpose side of the application. This double use is the main source of confusion.
		- ~~~text
		  ChatGPT desktop app
		  ├── ChatGPT
		  │   ├── Chat
		  │   └── Work
		  └── Codex
		  ~~~
	- ## ChatGPT names two levels
		- At the operating-system level, **ChatGPT** is the name of the application.
		- Inside the application, **ChatGPT** is also the label for the general-purpose side, opposite **Codex**. Chat and Work live within this inner ChatGPT side.
		- The phrase **ChatGPT desktop app** makes the outer meaning clear. **General-purpose ChatGPT** is a useful description for the inner meaning when the interface label alone would be ambiguous.
	- ## Three styles of work
		- ### Chat: hold a conversation
			- [[ChatGPT/Chat]] centers the interaction on a sequence of messages.
			- It fits questions, explanations, idea development, comparisons, planning, and other work where the conversation is the main structure.
			- The usual unit of interaction is a conversational turn.
		- ### Work: delegate general work
			- [[ChatGPT/Work]] centers the interaction on a goal and a useful result.
			- It can combine files, research, tools, and connected context into documents, spreadsheets, presentations, analysis, and other deliverables.
			- The usual unit of interaction is a task or work product.
		- ### Codex: delegate software work
			- [[Codex]] applies the goal-oriented style to software development.
			- Its working context includes repositories, source files, terminals, diffs, tests, and code review.
			- The usual unit of interaction is a software change that can be inspected and tested.
	- ## Application, experience, and model
		- Chat, Work, and Codex describe **experiences around AI models**. They are separate from the names of the models that power them.
		- ~~~text
		  Application: ChatGPT desktop app
		    Experience: Chat | Work | Codex
		      Model: the selected GPT model
		        Context and tools: conversation, files, browser, terminal, repositories, and connectors
		  ~~~
		- A model can appear in more than one experience. The surrounding instructions, context, tools, permissions, and working environment shape what it can do there.
	- ## Where the boundaries overlap
		- Work and Codex both accept goals, use tools, and produce artifacts. Their default contexts provide the useful distinction.
		- Work starts from general knowledge work and finished deliverables.
		- Codex starts from software projects and development workflows.
		- Their capabilities can overlap as both experiences gain more tools.
	- ## Vocabulary
		- **ChatGPT desktop app** — the overall application containing the different experiences.
		- **ChatGPT** — either the application as a whole or, within the application's selector, its general-purpose side.
		- **ChatGPT Chat** or **Chat** — the conversation-centered experience.
		- **ChatGPT Work** or **Work** — the general-purpose, goal-oriented work experience.
		- **Codex** — OpenAI's software-development agent and coding-oriented experience.
		- OpenAI calls the coding experience **Codex**. **ChatGPT Code** has no official product meaning as of August 2026.