tags:: [[Claude 3.7 Sonnet]]

- # DOING [Claude 3.7 Sonnet and Claude Code \ Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet)
	- ## my #notes
	  id:: 67bdaeaa-116b-417e-908b-0b425596704e
		- Anthropic is possibly differentiating themselves by adding something kind of like a [[Continuously Variable Transmission]] for model reasoning, rather than having to pick between a reasoning model and a traditional non-reasoning model.
			- API users can set a budget, which will be essential for controlling reasoning
				- {{embed ((67bda723-8a2a-4d9d-b97a-e2be0fe6cefa))}}
	- ## [[Claude 3.7 Sonnet]]
		- ### #Price
			- same as [[Claude 3.5 Sonnet]]: $3 per million input tokens and $15 per million output tokens—which **includes thinking tokens**
		- ### unified reasoning and inference
			- both an ordinary LLM and a reasoning model in one
				- pick when you want the model to answer normally and when you want it to [think longer before answering](https://www.anthropic.com/research/visible-extended-thinking).
			- **standard** mode
				- Claude 3.7 Sonnet is an upgraded version of [[Claude 3.5 Sonnet]]
			- **[[Claude/Extended Thinking]]** mode
				- self-reflects before answering
			- prompting for the model works similarly in both modes
		- ### control [[LLM Reasoning Model]] budget through [[Anthropic/API]] - #Cool
		  id:: 67bda723-8a2a-4d9d-b97a-e2be0fe6cefa
			- through the API, users can also control the *budget *for thinking: you can tell Claude to think for no more than N tokens, for any value of N up to its output limit of 128K tokens. This allows you to trade off speed (and cost) for quality of answer
		- ### [[AI Coding]] #Performance
			- id:: 67bda7c6-4be2-42e4-ba74-00ab2bce6aba
			  > There's a reason Claude is the default model for all Cursor users—Anthropic's approach to building models delivers on real-world tasks. During our extensive testing of [[Claude 3.7 Sonnet]], we've seen significant improvements in the model's ability to understand and handle complex codebases and multi-step tasks. Now **with two ways to think, Claude cements its place as the industry leader for coding**. -- #Quote  from [[Person/Michael Truell]] [[CursorAI]] Cursor, CEO
		- {{embed ((67bda4a7-d654-498c-b488-fa501bbca5de))}}
	- ## Claude Code
		- [[Anthropic/YouTube/25/02/Introducing Claude Code]]
		- limited research preview
		- [[AI/Coding/Tool]] -  to delegate engineering tasks to Claude