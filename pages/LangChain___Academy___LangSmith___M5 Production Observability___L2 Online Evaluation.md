- https://academy.langchain.com/courses/take/intro-to-langsmith/lessons/60775196-lesson-2-online-evaluation
- # [[AI/Eval/LLM as Judge]]
	- Takeaways
	  id:: 67b6293c-3dd0-4540-93eb-7fe31f05b824
		- [[Langsmith Online Evaluators]] provide a way in the langsmith UI to define a prompt and a [[Structured Output]] schema, and ensure that every time a trace comes in that matches a [[LangSmith/Filter]], it gets classified
			- common use-cases
				- `is_hallucinating` yes or no
				- `helpfulness` 1-10
	- ## [[LangSmith/Evaluator/Online]]
		- it's not tied to a particular dataset, so we only have access to inputs and outputs from our runs
		- sampled from last 5 traces in project
		- default prompt is using structured output go get a score back from LLM
		- sample #Prompt
			- ```
			  Evaluator
			  Secrets & API Keys
			  
			  HUMAN
			  You are assessing a user's question, and determining whether or not it is related to LangSmith, an LLM observability and evaluation platform
			  
			  [BEGIN DATA]
			  ***
			  [User Query]: {{query}}
			  ***
			  
			  [END DATA]
			  ```
		- sample schema for [[AI/LLM/Structured Output]]
			- **about_langsmith**
			  (Is the user's question about LangSmith, LangChain's LLM evaluations and observability platform)
			- ✅ **Required**
			  🔽 **Boolean**
			- 🗑️ (Delete icon)
			- ➕ **Add criteria**
			- ⬜ **Additional properties allowed**
			  ✅ **Strict mode enabled**
		- they map it to `input.question` ... but how does it know about `.question`?
		- the online evaluation uses a filter
			- **about_langchain?** 🟢 **Sampling Rate: 1** 🔽 **1 filter**
			  *Online LLM-as-a-Judge Evaluator*
		- the evaluator
			- we get a sample run from tracing project
				- we get inputs and outputs
				- we can test our code (hit the test code button)
		- online evaluators with llm as judge is a way to add real-time feedback
	- ## 10:00 common use cases for [[LangSmith/Evaluator/Online]]
		- example: `is_hallucinating`
			- your documents might be getting old; this can help with that
			  *For document retrieval tasks, check for hallucinations in the output.*
			- **Section:**
			  **LLM-as-Judge Online Evaluator** - *Check if this {answer} is grounded in these {documents}*
			- **online evaluation method** for checking **hallucinations in document retrieval tasks**. The evaluation follows an **LLM-as-Judge** approach, where an AI system determines if an **answer is grounded** in a given set of documents.
			- **linking the evaluation to a feedback score**, which explicitly indicates whether the response was **hallucinated** or **grounded in the provided evidence**.
			- This method helps in **assessing the reliability** of LLM-generated answers in **retrieval-augmented generation (RAG)** systems.
		- `helpfulness` - score perceived helpfulness of the answer to a user
			- This use case demonstrates an **LLM-as-Judge Online Evaluator** that **scores the perceived helpfulness** of an AI-generated answer to a given question.
			- The **LLM evaluates** how useful the answer is on a scale from **1 to 10**.
			- The result is **stored as a feedback score**, with an example rating of **helpfulness = 7**.
			- This evaluation method helps **quantify the quality of responses** based on their **usefulness to the user**, supporting **iterative improvements** in LLM-generated content.
			- This approach can be particularly useful for **ranking AI-generated answers**, refining **chatbots**, and improving **customer support systems** that rely on LLMs.
		- Email writing assistant - `correctly_signed = True`
			- regex match that we correctly signed email
				- `correctly_signed = True`
				- code online evaluator for every trace
	-