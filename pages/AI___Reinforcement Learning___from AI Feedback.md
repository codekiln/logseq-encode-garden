tags:: [[Term]], [[Acronym]] 
alias:: [[RAFT]]

- # **RAFT — Reinforcement Learning from AI Feedback**
	- **Definition:**
		- RAFT is a newer alignment technique similar to RLHF (Reinforcement Learning from Human Feedback), but it replaces the human reward model with **AI-generated feedback**.
	- **Goal:**
		- To scale alignment cheaply and consistently by using another model (or ensemble) to provide feedback instead of humans.
	- **How it works:**
		- Collect candidate responses from a model.
		- Use another (trusted) model to **evaluate or rank** those responses.
		- Train the main model using reinforcement learning (e.g., PPO) based on those AI-provided scores.
	- **Advantages:**
		- Reduces human labor and cost.
		- Enables faster iteration and continuous alignment.
		- Can leverage expert models for domain-specific feedback loops.
	- **In short:**
		- **SFT**: “Teach it what to do.” (explicit supervision)
		- **RAFT**: “Teach it how to improve itself.” (reinforcement with AI evaluators)