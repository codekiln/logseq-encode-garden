tags:: [[Term]], [[Acronym]]
alias:: [[SFT]]

- # **SFT — Supervised Fine-Tuning**
	- **Definition:**
		- SFT is the process of training a pre-trained language model further on a labeled dataset (input–output pairs) under supervision.
	- **Goal:**
		- To align the model's responses with desired behaviors or domain-specific knowledge.
	- **How it works:**
		- Start with a base model (e.g., pretrained on general web text).
		- Train it using curated examples — often human-written prompts and ideal completions.
		- The loss function (usually cross-entropy) penalizes deviation from the target outputs.
	- **Example use cases:**
		- Fine-tuning a general model into a customer-support agent.
		- Teaching a model to follow instructions or code correctly.
	- **Example (simplified):**
		- ~~~
		  Prompt: Write a polite email requesting a refund.
		  Target: Dear support team, I'd like to request a refund for my order...
		  ~~~
