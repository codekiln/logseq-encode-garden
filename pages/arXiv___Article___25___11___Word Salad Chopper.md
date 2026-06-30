logseq-entity:: [[Logseq/Entity/Article]]
date-created:: [[2025/11/01]]

- # [Word Salad Chopper: Reasoning Models Waste A Ton Of Decoding Budget On Useless Repetitions, Self-Knowingly](https://arxiv.org/abs/2511.00536)
	- arXiv:2511.00536 · Wenya Xie, Shaochen (Henry) Zhong, Hoang Anh Duy Le, Zhaozhuo Xu, Jianwen Xie, Zirui Liu
	- ## Summary
		- Large reasoning models waste significant decoding budget through meaningless token repetitions — and their hidden states reveal the model is self-aware of the loop.
		- A single-layer linear classifier over newline-token hidden states detects word salad during generation with minimal overhead.
		- Removing detected word salad tokens and regenerating yields substantial length savings with minimal quality loss; the authors argue this filtering should be standard practice.
	- ## Key Quote
		- id:: 6a437857-f7f5-4bd4-bf20-84ebc0ccbc89
		  > "...a significant portion of these tokens are useless self-repetitions—what we call 'word salad'—that exhaust the decoding budget without adding value."
	- ## Examples in [Appendix G](https://arxiv.org/html/2511.00536v1#A7)
		- #### Case 1: Semantic Loop from Unresolved Ambiguity (MATH-500).
			- The model begins with valid reasoning but then becomes trapped in a semantic loop — repeating the same confusion without resolution:
			- >  ‘‘But when I added step-by-step, I got 9997.\n\n’’
			  ‘‘But wait, 6270 + 3737 is 10,007, so why is the step-by-step adding 3000, 700, 30, and 7 giving me 9997?\n\n’’
			  ‘‘But why does the step-by-step addition give me 9997?\n\n’’ (chopped here)
			  ‘‘Wait, so 6270 + 3737 is 10,007...\n\n’’
			- WSC detects early signs of degeneration and chops at the third chunk, followed by a regeneration prompt. The regenerated continuation quickly resolves the problem with correct reasoning within a 4k budget.
		- #### Case 2: Endless Enumeration without Convergence (MATH-500).
			- The model attempts a brute-force enumeration without reaching a conclusion:
			- >  ‘‘For k=1: ...’’
			  ‘‘k=12: ...’’
			  ‘‘k=14: ...’’ (chopped here)
			  ‘‘k=27: ...’’
			- Here, WSC intervenes at chunk 318 to prevent further unbounded enumeration, ensuring the continuation remains within budget. This illustrates WSC’s ability to detect degeneration early and prevent catastrophic repetition.
	- ## Context
		- Defines "word salad" specifically as the **token bloat** variety — see [[Word/Salad]] for the full taxonomy.