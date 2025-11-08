tags:: [[Term]], [[Acronym]], [[Abbreviation]] 
alias:: [[PPO]]

- # **PPO — Proximal Policy Optimization**
	- **Definition:**
		- PPO stands for **Proximal Policy Optimization** — a reinforcement learning (RL) algorithm that's widely used to fine-tune large language models (LLMs) such as GPT, Claude, and others after supervised fine-tuning (SFT).
	- ## 🧠 Conceptually
		- In reinforcement learning, the model is treated as an *agent* that generates *actions* (tokens, sentences, etc.) in response to *states* (prompts).
		- It then receives a **reward signal** — a numeric score representing how "good" the response was — and adjusts its behavior to maximize that reward.
		- PPO is a way of updating the model's parameters **without changing its behavior too drastically** in one step.
	- ## ⚙️ Technically
		- PPO improves the model's *policy* (its probability distribution over possible responses) using the idea of **trust regions** — it limits how far the new policy can move from the old one to prevent instability.
		- The optimization objective is roughly:
			- $$
			  L^{PPO} = \mathbb{E}\left[\min\left(r_t(\theta)A_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)A_t\right)\right]
			  $$
		- where:
			- $r_t(\theta)$ = ratio between new and old policy probabilities (how much we've changed the model's output distribution),
			- $A_t$ = advantage (how much better this action was than expected),
			- $\epsilon$ = small constant (e.g. 0.1–0.2) that limits how big updates can be.
		- This "clipped objective" ensures stable and efficient training.
	- ## 🧩 In LLM alignment (e.g. RLHF or RAFT)
		- The **policy** = the LLM itself (mapping prompts → responses).
		- The **reward** = either human feedback (RLHF) or AI-generated feedback (RAFT).
		- PPO updates the LLM so that it produces outputs with higher reward — but without forgetting what it already knows from SFT.
	- ## 🪄 In short
		- ** [[SFT]]:** teaches the model *what to do*.
		- **PPO (in RLHF/[[RAFT]]):** refines *how well it does it* based on feedback.
		- PPO is used because it's stable, efficient, and scales well for LLMs.