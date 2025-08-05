tags:: [[Idea]]
alias:: [[AI/Coding/Technique/Using Agentic Documentation as Intermediary Step]] 
created-by:: [[Person/codekiln]]

- # #Agentic #[[Knowledge Base]] #[[Software Library]] #Documentation as an input to #[[AI Coding]]
	- Services like [[Devin]] (see its [[DeepWiki]]) and [[BlitzyAI]] seem to rely upon some automated, agentic documentation generation as an intermediary step.
		- It's almost like a form of slow digestion; the process of producing good documentation is like creating enzymes to break down problems in a way that's more specific to the body  - or enterprise - in which software is built
		- In the case of [[BlitzyAI]], this involves work on internal, private codebases.
	- ## #[[Mermaid Diagram]]
		-
		- {{renderer :mermaid_6891bd99-2b46-40d9-ace0-95d5f40c74b1, 4}}
			- ```mermaid
			  flowchart TD
			      Note["Used by: Blitzy, Devin"]
			      A[Arch Doc Agent]
			      B[Analyze Library]
			      C[Condensed, high-quality context for AI]
			      D[Code Planning Agent]
			      E[Coding Agent]
			      F[Code]
			  
			      Note --> A
			      A --> B
			      B -->|output| C
			      C -->|input| D
			      D --> E
			      E --> F
			      E -->|update| A
			  ```