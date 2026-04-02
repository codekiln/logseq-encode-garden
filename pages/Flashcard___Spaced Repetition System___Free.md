alias:: [[FSRS]]
tags:: [[Term]]

- # Free Spaced Repetition System
	- **SRS** is the *category*.
	  **FSRS** is a *specific scheduling algorithm* inside that category.
	  
	  ---
	- ## SRS (Spaced Repetition System)
	  
	  A broad concept:
	- Any system that spaces reviews over time
	- Can be implemented many ways (Leitner, SM-2, custom heuristics)
	- Defines *what* you’re doing:
		- adaptive review timing
		- based on memory strength
		  
		  It’s not one algorithm — it’s a family of approaches.
		  
		  ---
	- ## FSRS (Free Spaced Repetition Scheduler)
	  
	  A modern *algorithm* for SRS scheduling.
	- Developed as an alternative to older models like SM-2
	- Used in tools like Anki (optionally) and projects like `repeater`
	- Defines *how* scheduling is computed
	  
	  ---
	- ## Core Difference
	  
	  |  | SRS | FSRS |
	  | ---- | ---- | ---- |
	  | Type | Concept / paradigm | Specific algorithm |
	  | Scope | Many possible implementations | One concrete implementation |
	  | Goal | Efficient memory retention | Optimize retention with predictive modeling |
	  | Flexibility | High (many strategies) | Fixed mathematical model (tunable) |
	  
	  ---
	- ## What Makes FSRS Different
	- ### 1. Explicit Memory Model
	  
	  FSRS models memory with variables like:
	- **Stability** (how long memory lasts)
	- **Difficulty** (intrinsic hardness of item)
	- **Retrievability** (probability of recall at a given time)
	  
	  Older systems (like SM-2) use simpler heuristics (ease factor + intervals).
	  
	  ---
	- ### 2. Target Recall Rate
	  
	  FSRS lets you aim for a specific retention probability:
	- e.g. 90% recall (as mentioned in `repeater`)
	- schedules reviews *just before* that probability drops below target
	  
	  This is much more explicit than classic SRS systems.
	  
	  ---
	- ### 3. Data-Driven Optimization
	  
	  FSRS can be **trained on your review history**:
	- Fits parameters to *your* memory behavior
	- Adapts to:
		- how quickly you forget
		- how you rate difficulty
		  
		  Traditional SRS algorithms are mostly static.
		  
		  ---
	- ### 4. Continuous vs Discrete Thinking
	- **SM-2 / Leitner** → step-based (“increase interval by factor”)
	- **FSRS** → probabilistic / continuous model of forgetting
	  
	  It’s closer to a *prediction problem* than a rule-based system.
	  
	  ---
	- ## Intuition
	- SRS = “review things less often as you learn them”
	- FSRS = “predict exactly when you’ll forget this, and schedule just before that”
	  
	  ---
	- ## Practical Implication
	  
	  With FSRS:
	- Fewer unnecessary reviews
	- Better long-term efficiency
	- More consistent retention at a chosen level (e.g. 90%)
	  
	  With generic SRS (older algorithms):
	- Simpler
	- More predictable
	- Slightly less optimal scheduling
	  
	  ---
	- ## Mental Compression
	  
	  [[SRS]] is the philosophy.
	  FSRS is a modern, data-driven implementation of that philosophy.