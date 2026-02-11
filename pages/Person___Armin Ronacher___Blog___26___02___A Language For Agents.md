tags:: [[Person]], [[Blog]], [[AI]], [[Programming Language]], [[Agent]]
alias:: [[Person/Armin Ronacher/Blog/26/02/A Language For Agents]]
readwise-link:: https://readwise.io/reader/shared/01kh0wm63s1crshkhw2drbemhm

- # [A Language For Agents](https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/)
	- ## Metadata
		- **Author:** [[Person/Armin Ronacher]]
		- **Source:** [lucumr.pocoo.org](https://lucumr.pocoo.org/)
		- **Published:** February 09
		- **Annotated in Readwise:** [Link](https://readwise.io/reader/shared/01kh0wm63s1crshkhw2drbemhm)
	- ## Key Highlights
		- Agents can still perform well in newer or underrepresented languages if documentation and tooling are good enough.
		- Tooling quality can matter more than language popularity in model weights (example: Swift tooling friction).
		- Lower coding cost reduces the importance of ecosystem breadth, because agents can port missing functionality.
		- A new language can succeed if it is designed with agent behavior and training realities in mind.
		- As generated code volume increases, readability and reviewability become more important than terseness.
		- Agents often skip LSP setup, so languages that remain understandable without LSP have an advantage.
		- Significant whitespace can be a reliability issue for token-level editing workflows.
		- Structural tokens can also fail when punctuation clusters tokenize poorly.
		- Agents prefer local reasoning and low-coupling code that avoids hidden context.
		- Macro-heavy code and alias-heavy imports both degrade agent reliability.
		- Flaky tests and environment divergence are especially costly for iterative agent workflows.
		- Unified, deterministic build/test signals help agents converge faster.
	- ## Selected Annotations
		- > Zig seems underrepresented in the weights (at least in the models I've used) and also changing quickly. That combination is not optimal, but it's still passable: you can program even in the upcoming Zig version if you point the agent at the right documentation.
		- > On the other hand, some languages are well represented in the weights but agents still don't succeed as much because of tooling choices. Swift is a good example: in my experience the tooling around building a Mac or iOS application can be so painful that agents struggle to navigate it.
		- > The biggest reason new languages might work is that the cost of coding is going down dramatically. The result is the breadth of an ecosystem matters less.
		- > New languages will work if their value proposition is strong enough and they evolve with knowledge of how LLMs train.
		- > The cost of writing code is going down, but because we are also producing more of it, understanding what the code does is becoming more important.
		- > There are situations when an agent just won't run the LSP — not because of technical limitations, but because it's also lazy and will skip that step if it doesn't have to.
		- > A language that doesn't split into two separate experiences (with-LSP and without-LSP) will be beneficial to agents because it gives them one unified way of working across many more situations.
		- > It pains me as a Python developer to say this, but whitespace-based indentation is a problem. The underlying token efficiency of getting whitespace right is tricky, and a language with significant whitespace is harder for an LLM to work with.
			- Note: I haven't had problems with this in months… is this really still a problem?
		- > On the other hand, braces that are not separated by whitespace can cause issues too.
		- > Readers of this blog might know that I'm a huge believer in async locals and flow execution context.
		- > Reformatting also often causes constructs to move to different lines.
		- > Much of what I've said boils down to: agents really like local reasoning.
		- > Agents often struggle with macros.
		- > Agents often hate it when aliases are involved.
		- > Nobody likes flaky tests, but agents even less so.