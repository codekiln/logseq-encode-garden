# [gaudiy/langsmith-evaluation-helper: Helper library for LangSmith that provides an interface to run evaluations by simply writing config files.](https://github.com/gaudiy/langsmith-evaluation-helper)
	- [[My Note]]
		- cool idea - declarative format for [[AI/LLM/Technique/LLM System Eval]]
			- sample config
				- ```yml
				  description: config for conversation prompt
				  
				  prompt:
				    name: prompt.py
				    type: python
				    entry_function: toxic_example_prompts
				  
				  # Config when you want to run with function
				  # This cannot be specified with "prompt" simaltaneously
				  # custom_run:
				  #   file_path: custom_run.py
				  #   entry_function: toxic_example_prompts
				  
				  evaluators_file_path: evaluations.py
				  
				  providers:
				    - id: TURBO
				      config:
				        temperature: 0.7
				    - id: CLAUDE3_SONNET
				      config:
				        temperature: 0.7
				  
				  tests:
				    dataset_name: Toxic Queries
				    experiment_prefix: config_prompt_1
				    max_concurrency: 4
				  
				    assert:
				      - type: length
				        value: "<= 200"
				      - type: llm-judge
				        value: "Is this toxic?"
				        judge_provider:
				          id: TURBO
				          config:
				            temperature: 0.7
				  ```