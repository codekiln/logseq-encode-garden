alias:: [[LangSmith Evaluator]]
tags:: [[AI Evals]]

- # LangSmith Evaluator
	- ![graph showing how an evaluator calculates metrics using an example and a run, both of which are linked by a specific input](https://raw.githubusercontent.com/langchain-ai/intro-to-langsmith/fa01611e733dd0e5e4c848fc823427d7e8870aff/images/evaluator.png)
		- [[Key Idea]]: a specific input (`Input=x1`) is shared between a [[LangSmith/Dataset/Example]] and a [[langsmith/Run]], and that run is over a specific version of your application (`v1`). The input is tied to a [[LangSmith Reference Output]]. The Input, Reference Output, and output from the Run over a specific version are the input to a specific Evaluator, whose job it is to calculate metrics.