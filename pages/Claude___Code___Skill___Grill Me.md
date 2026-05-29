- # [Grill Me](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
	- A [[Claude/Code/Skill]] by [[Person/Matt Pocock]] that interviews the user relentlessly about a plan or design until reaching shared understanding.
	- ## How it works
		- Triggered when the user says "grill me", "interview me", "ask me questions", "let's figure this out", or similar phrases.
		- Walks the decision tree depth-first, finishing one branch before opening another.
		- Asks questions one at a time — never bundled.
		- Provides a recommended answer with each question.
		- If a question can be answered by exploring the codebase, explores the codebase instead.
	- ## SKILL.md
		- ~~~
		  ---
		  name: grill-me
		  description: Interview the user relentlessly about a plan or design until reaching shared
		  understanding, resolving each branch of the decision tree. Use when user wants to
		  stress-test a plan, get grilled on their design, or mentions "grill me".
		  ---
		  
		  Interview me relentlessly about every aspect of this plan until we reach a shared
		  understanding. Walk down each branch of the design tree, resolving dependencies between
		  decisions one-by-one. For each question, provide your recommended answer.
		  
		  Ask the questions one at a time.
		  
		  If a question can be answered by exploring the codebase, explore the codebase instead.
		  ~~~
	- ## Source
		- [[Person/Matt Pocock/GitHub/skills]]
