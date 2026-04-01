alias:: [[SRS]]
tags:: [[Term]]

- # Flashcard Spaced Repetition Systems
	- [[tldr]]
		- A piece of [[Software]] that helps a human expand the capacity of their memory with a technique known as Spaced Repetition, where the distance between flashcards gets longer over time after many successful tests.
	- ## Summary
	- A spaced repetition system (SRS) is a memory scheduling strategy that optimizes when you review information so that you retain it with minimal effort. It is grounded in the observation that memory decays over time (the “forgetting curve”) but is strengthened when recall happens just before forgetting.
	  
	  ---
	- ## Core Idea
	  
	  Instead of reviewing material at fixed intervals, an SRS adapts the timing of each review based on how well you remember an item.
	- Easy items → reviewed less often
	- Difficult items → reviewed more frequently
	- Goal → keep each item at the edge of forgetting
	  
	  This creates an efficient allocation of attention across a large body of knowledge.
	  
	  ---
	- ## Key Concepts
	- ### 1. The Forgetting Curve
	  
	  Originating from Hermann Ebbinghaus’ work, memory retention declines exponentially without reinforcement.
	  
	  Each review resets or strengthens the curve.
	  
	  ---
	- ### 2. Retrieval Practice
	  
	  SRS relies on *active recall*, not passive review.
	- Prompt → attempt recall → check answer
	- The act of retrieval strengthens memory more than re-reading
	  
	  ---
	- ### 3. Spacing Effect
	  
	  Distributed practice over time is more effective than cramming.
	- Short intervals early (minutes → hours → days)
	- Longer intervals later (weeks → months → years)
	  
	  ---
	- ### 4. Adaptive Scheduling
	  
	  Each item has its own review schedule.
	  
	  Typical signals:
	- Correct vs incorrect
	- Ease/difficulty rating
	- Response latency (in more advanced systems)
	  
	  ---
	- ## Algorithmic Models
	- ### Leitner System (Simple)
	- Flashcards move between boxes
	- Each box has a longer review interval
	- Incorrect → reset to first box
	  
	  Good mental model, low precision
	  
	  ---
	- ### SM-2 (SuperMemo Algorithm)
	  
	  Developed for SuperMemo
	  
	  Tracks:
	- Ease factor (how hard an item is)
	- Interval growth function
	  
	  Roughly:
	- If correct → increase interval multiplicatively
	- If incorrect → reset interval
	  
	  Forms the basis for many modern systems
	  
	  ---
	- ### Modern Variants
	  
	  Used in tools like Anki:
	- Refined ease calculations
	- Fuzzing (randomness to avoid clumping)
	- Learning vs review phases
	- Optional features: leech detection, burying siblings, etc.
	  
	  ---
	- ## Mental Model
	  
	  Think of each memory as having a “decay timer.”
	- Review too early → wasted effort
	- Review too late → memory lost
	- Optimal review → just before forgetting
	  
	  SRS attempts to approximate this optimal timing per item.
	  
	  ---
	- ## Tradeoffs
	- ### Strengths
	- Extremely efficient for large knowledge bases
	- Long-term retention (months/years)
	- Scales well with automation
	- ### Limitations
	- Best for discrete, recallable facts (not deep understanding alone)
	- Requires consistent usage
	- Scheduling debt can accumulate
	  
	  ---
	- ## What It’s Good For
	- Vocabulary (languages)
	- Technical facts (APIs, commands)
	- Conceptual anchors (definitions, theorems)
	- Memorization-heavy domains (medicine, law)
	  
	  ---
	- ## What It’s Not
	- Not a full learning system
	- Not a substitute for synthesis, application, or intuition
	  
	  It is a *retention layer* that sits on top of understanding.
	  
	  ---
	- ## Composable View
	  
	  You can think of SRS as:
	  
	  ```
	  knowledge acquisition → encoding → spaced retrieval scheduling → long-term retention
	  ```
	  
	  It integrates best when paired with:
	- Meaningful context (why something matters)
	- Generative use (writing, explaining, building)
	- Interleaving across domains
	  
	  ---
	  
	  If you want, we can go deeper into:
	- Designing your own SRS algorithm
	- Using SRS with conceptual/graph-based knowledge (Logseq-style)
	- Failure modes (ease hell, leeches, overload)
	- Integrating SRS with AI agents or PKMs