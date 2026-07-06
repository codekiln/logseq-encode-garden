logseq-entity:: [[Logseq/Entity/Definition]]

- # Dotfiles Dependency Idea
	- In this garden, **Dotfiles Dependency Idea** pages model a want for the global toolchain — a job to be done that a tool might be adopted to handle. An idea is cheap to record and gains detail only when it is pursued.
	- ## What counts as an instance
		- A job or capability wanted from the dotfiles or global setup, whether or not a tool has been chosen for it — for example [[Terminal/Multiplexer/Idea]].
		- Not an instance: the tool itself (that is a [[Logseq/Entity/Dotfiles/Dep]], and usually also a [[Logseq/Entity/Software/Project]]); a [[My/Pref]] or [[My/Principle]] page.
	- ## Naming and links
		- Key the page to the job rather than to a tool, as an `/Idea` child of the capability page it concerns — [[Terminal/Multiplexer/Idea]] under [[Terminal/Multiplexer]].
		- Candidate tools are their own pages, linked from the idea. An already-installed tool can have an idea written for it after the fact.
	- ## Frontmatter
		- On instances, set `logseq-entity:: [[Logseq/Entity/Dotfiles/Dep/Idea]]`.
		- Instances carry no stage or status property; an idea's progress shows through the notes present on it.
		- Shared conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- Starts as a single sentence naming the job (the H1), with nothing else required.
		- As the idea is pursued, the page or its subpages gather a survey of alternatives, a security read of the candidates, and a decision naming the tool chosen — or recording that none was.
	- ## Relationships to other types
		- [[Logseq/Entity/Dotfiles/Dep]] — the tool adopted to do the job; an idea names its chosen dependency once one is selected.
		- [[Logseq/Entity/Software/Project]] — the candidate tools weighed for an idea are software projects.
