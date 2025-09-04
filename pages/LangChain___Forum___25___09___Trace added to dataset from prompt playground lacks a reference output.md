created-by:: [[Person/codekiln]]

- # [Trace added to dataset from prompt playground lacks a reference output - Product Help / LangSmith - LangChain Forum](https://forum.langchain.com/t/trace-added-to-dataset-from-prompt-playground-lacks-a-reference-output/1439)
	- When I try to add a trace from the prompt playground to a dataset, the Reference Output is not filled in with the output from the prompt playground. Furthermore, when I go to try to manually add a reference output, hitting submit does not save the output. The dataset does not have a schema, so it’s not a validation error that’s preventing it from being saved as far as I know.
	- ## [](https://forum.langchain.com/t/trace-added-to-dataset-from-prompt-playground-lacks-a-reference-output/1439#p-2417-expected-behavior-1) Expected Behavior
	  
	  Adding a trace from any project to a dataset adds the output as the reference output for that example.
	- ## [](https://forum.langchain.com/t/trace-added-to-dataset-from-prompt-playground-lacks-a-reference-output/1439#p-2417-actual-behavior-2) Actual Behavior
	  
	  Adding a trace from the playground project to a dataset does not add the output to the example at all. The resulting example added to the dataset is missing a reference output.