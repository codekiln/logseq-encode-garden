logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[AI/Eval]]

- # In AI training, what's a "distractor"?
	- ## [[AI Answer]]
		- Short answer: a **distractor** is a deliberately incorrect-but-plausible item — an answer option, a passage, or a piece of context — included so a model has to identify the *right* signal and resist being misled. The term is borrowed from psychometrics (multiple-choice test design), where the wrong answer choices on an item are called distractors.
		- **In evaluation / multiple-choice benchmarks** (the most common usage): the incorrect answer choices in an MCQ are the distractors. Benchmarks like [[AI/Eval/MMLU]] and ARC present a question with one correct option and several distractors; well-written distractors are *plausible* (e.g. common misconceptions), which makes the item discriminating rather than trivially guessable.
		- **In retrieval / long-context / RAG** ("distractor documents" or "distractor passages"): irrelevant or superficially-relevant text inserted alongside the gold passage to test whether the model can find the needle and ignore noise. [HotpotQA](https://arxiv.org/abs/1809.09600) formalized a **"distractor setting"** where each question ships with 2 gold paragraphs plus 8 Wikipedia distractor paragraphs; "needle in a haystack" long-context tests use the same idea.
		- **In training (not just eval):** distractors are mixed into training data on purpose so the model learns the discrimination skill rather than overfitting to clean inputs — e.g. hard negatives in retrieval/contrastive training, or distractor context in long-context and tool-use fine-tuning. A *hard* distractor is one that is close to the correct answer and therefore most informative.
		- **Why they matter:** the quality of the distractors largely determines how hard and how diagnostic a question is. Weak distractors inflate scores (the answer is obvious); strong distractors expose whether the model actually reasons or just pattern-matches.
