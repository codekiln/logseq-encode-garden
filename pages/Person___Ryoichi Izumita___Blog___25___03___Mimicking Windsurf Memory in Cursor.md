# [Mimicking Windsurf’s “Memory” Feature in Cursor — Let Generative AI Create Rules | by Ryoichi Izumita | Mar, 2025 | Medium](https://rizumita.medium.com/mimicking-windsurfs-memory-feature-in-cursor-let-generative-ai-create-rules-c5d2c1976c4d)
	- ## [[My Notes]]
	  id:: 67d6dce5-6e71-49e1-9ecc-34db0e651bc4
		- describes a [[CursorAI/Project Rule]] that, like [[CursorAI/Project Rule/cursor-project-rule-editor.mdc]], can create a new project rule. Goes into a bit more detail than other examples I've seen about how to explain to cursor the various [[CursorAI Project Rule Types]] and when to use them, presumably because memories should have different activation properties that the user should control.
		- It seems to me that storing memories in cursor project rules may be functional but inefficient. I'd prefer to have Cursor store its memories in [[Logseq]], as described in [[CursorAI/Idea/Using Logseq with Project Rules]]. Of course, in that context, the memories would be shared across instances, so it may not make sense to use a symlinked common directory, but instead use a project memory logseq garden.
	- ## Quotes
		- In [[Windsurf]] , you can easily store information in Memory by using its Cascade function (akin to Cursor’s agent). Simply say something like: “Please remember ___.” From then on, Windsurf will refer to that stored information whenever you generate content or have a conversation.
			- **Examples**
				- “Please summarize the steps we’ve taken so far and store them in memory.”
				- “Please research the usage of the ___ library and store it in memory.”
			- Once you give such an instruction, the content is automatically saved to Memory in Windsurf.
	-