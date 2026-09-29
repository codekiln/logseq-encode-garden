logseq-entity:: [[Logseq/Entity/Question]]
via:: [[LangSmith/26/09/29 Tue - Deep Agents]]

- # How do I run a double-blind labeling experiment with [[LangSmith/Annotation/Queue]]s?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Annotation queues](https://docs.langchain.com/langsmith/annotation-queues), researched by [[Anthropic/Model/Claude/5/5/Opus]] on [[2026-09-29 Tue]]
		- **Short answer:** have more than one reviewer label every item. Annotation queues already hide each reviewer's feedback from the others. Measuring where the reviewers agree is a step you do yourself, from the exported feedback.
		- ## Queue settings
			- **Number of reviewers per run** — how many reviewers must mark an item **Done** before it leaves the queue. Set it to 2 or more so every item gets independent labels.
			- **Use assigned reviewers** — names specific workspace members instead of a count. An item moves through **Needs Review** → **Needs Others' Review** → **Completed**, and completes only once every assigned reviewer has submitted.
			- In both modes, reviewers cannot see the feedback other reviewers left.
			- **Comments on items are visible to all reviewers**, so reviewers should keep their judgment in feedback scores and reviewer notes, and leave comments alone during the experiment.
			- Reservations lock an item for one reviewer for a set time; they switch off when every workspace member reviews each item.
		- ## Rubric
			- Define the feedback criteria and instructions on the queue, so every reviewer scores against the same rubric.
			- Threads can be queue items too, so a whole multi-turn conversation can be labeled as one item.
		- ## Measuring agreement
			- The docs describe no built-in agreement score between reviewers.
			- Pull the feedback with the SDK (for example `Client.list_feedback` filtered to the queue's runs), group it by run and feedback key, and compute agreement — percent agreement, or Cohen's kappa for two reviewers.
			- Items where reviewers diverge are the ones to discuss and fix the rubric on; the intersection where they agree is the labeled set to trust, and the signal to turn into an [[LangSmith/Evaluator]].
		- ## Blinding the output source
			- For comparing two models or prompts, pairwise annotation queues show two runs side by side and ask which is better or whether they're equivalent. They're created from **Datasets & Experiments**.
			- The docs don't say whether the pairwise view hides which experiment each side came from, or randomizes the sides. Check in the UI before relying on it as blind.
