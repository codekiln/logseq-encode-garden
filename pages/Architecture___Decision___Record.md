alias:: [[ADR]]

- # [Architectural Decision Records (ADRs) | Architectural Decision Records](https://adr.github.io/)
	- ## From [[Book/Fundamentals of Software Architecture/ch/21 Architectural Patterns]] by [Mark Richards](https://learning.oreilly.com/search/?query=author%3A%22Mark%20Richards%22&sort=relevance&highlight=true), [Neal Ford](https://learning.oreilly.com/search/?query=author%3A%22Neal%20Ford%22&sort=relevance&highlight=true)
		- One of the most effective ways of documenting architectural decisions is through *Architectural Decision Records* ([ADRs](https://adr.github.io/)). [[Person/Michael Nygard]] first evangelized ADRs in a 2011 [blog post](https://oreil.ly/yDcU2), and in 2017, [Thoughtworks Technology Radar](https://oreil.ly/0nwHw) recommended the technique for widespread adoption.
		- An ADR consists of a short text file (usually one to two pages long) describing a specific architectural decision. While ADRs can be written using plain text or in a wiki page template, they are usually written in some sort of text document format, like [[AsciiDoc]] or [[Markdown]].
		- Tooling is also available for managing ADRs. Nat Pryce, coauthor of *Growing Object-Oriented Software, Guided by Tests* (Addison-Wesley, 2009), has written an open source tool called [ADR Tools](https://oreil.ly/6d8LN) that provides a command-line interface to manage ADRs, including numbering schemes, locations, and superseded logic. [[Person/Micha Kops]], a software engineer from Germany, provides some great examples of using ADR tools to manage architectural decision records: https://www.hascode.com/managing-architecture-decision-records-with-adr-tools/.
	- ## From [[Person/Jacqui Read/Book/Communication Patterns/ch/12 Effective Practices]]
		- ### Situations ADRs help avoid
			- A decision is made early in the life of a product. Later, an individual or team decides to change that decision. Without knowing how and why the initial decision was made, the change may cause huge problems. Maybe a particular technology was chosen to meet one or more requirements, and overriding that choice means those requirements are no longer met. You may not realize this until a lot of time and money have been wasted.
			- What  [[Person/Birgitta Böckeler]] of Thoughtworks calls “whack-a-mole” decisions: a decision is regularly brought up again and again, wasting time reinvestigating only to discover that the original decision was made for good reasons.
			- When onboarding, a new team member should have lots of questions about how your team has done things and why. Current team members likely do not have all the answers in their heads or want to spend their time explaining things over and over again.
			- Someone leaves the company and takes all the architectural decision knowledge and reasoning with them because it’s all in their head.
		- ### #Example structure
			- ```
			  # Identifier and Title (a statement of the decision made)
			  
			  ## Status
			  Draft/Decided/Superseded by ADR-XXX
			  
			  ## Context
			  Why you need to make the decision. Assumptions, constraints, and decision drivers.
			  
			  ## Evaluation Criteria
			  What is important to you in making this decision?
			  Which of your architectural characteristics apply to making this decision?
			  Should any constraints or decision drivers become a criterion?
			  
			  ## Options
			  Outlines of the options considered against the evaluation criteria (usually using a
			  score or rating), and trade-offs outside of the evaluation criteria.
			  
			  ## Decision
			  The choice that was made and why.
			  
			  ## Implications
			  The positive and negative consequences of the decision made.
			  
			  ## Consultation
			  If taking input from others, they should document it here. Details of those invited
			  to give input can be recorded, whether they provide input or not. Although
			  consultation takes place before a decision is made, it is documented at the end
			  because it can become long and obscure the decision itself.
			  ```
	- ## [Design Practice Repository (DPR) Version 1.5 (Git Pages) | design-practice-repository](https://socadk.github.io/design-practice-repository/)
		-
-