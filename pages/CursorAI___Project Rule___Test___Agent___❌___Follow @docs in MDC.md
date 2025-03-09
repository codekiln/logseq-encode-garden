# Can Cursor Agent Mode follow [[CursorAI/@/Docs]] references in [[.mdc]] files? **NO**
	- Tests whether [[CursorAI/Agent Mode]] mode pulls documentation docs into context if a [[CursorAI/Project Rule]] is activated that attempts to reference `@docs`
	  id:: 67cd6155-cbe2-435f-b834-0a271fa13258
	- ## Test Preparation
		- Try a docs query to one of the pre-built providers [[CursorAI/@/Docs/PreBuilt]]
			- Sample queries
				- `@Aws Lambda what's an Alias configuration?`
					- it should pull in 4-8 docs from [AliasConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_AliasConfiguration.html)
				- `@Ansible how can I install multiple collections with a requirements file?`
					- it should pull in 4-8 docs including [Installing collections — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html#install-multiple-collections-with-a-requirements-file)
					  id:: 67cc7ec6-3d01-44dd-b4ec-91822d930db5
		- Place these file at `.cursor/rules`
			- [[CursorAI/Project Rule/Link/GitHub]] [[CursorAI/Test/Fixture]]
				- [logseq-encode-garden/.cursor/rules/test-docs-at-reference-space.mdc at main · codekiln/logseq-encode-garden](https://github.com/codekiln/logseq-encode-garden/blob/main/.cursor/rules/test-docs-at-reference-space.mdc)
				- ### Optional; didn't use because the first test failed
					- [logseq-encode-garden/.cursor/rules/test-docs-at-reference-no-space.mdc at main · codekiln/logseq-encode-garden](https://github.com/codekiln/logseq-encode-garden/blob/main/.cursor/rules/test-docs-at-reference-no-space.mdc)
	- ## Test
		- {{embed [[CursorAI/Project Rule/Test/Standard Setup]]}}
		- Activate **Agent mode** in Cursor
		- ### Test - activate `Testing Docs At Reference No Space` from description in Agent Mode
		  id:: 67cc8297-c6ce-42a8-8c44-ae138563ec21
			- enter `Testing Docs At Reference No Space`
			- #### Expected Behavior
				- Rule is activated
				- Ansible docs are pulled into context
			- #### Observed Behavior
				- ✅ Rule is activated
					- > I'll help you access the documentation referenced in the test-docs-at-reference-no-space rule. Let me fetch the relevant documentation about Ansible.
				- ❌ Ansible docs are pulled into context
					- It tries to search for a directory called docs
						- > Let me try to locate the Ansible documentation in the docs directory.
		- ### Test - activate `Testing Docs At Reference No Space` from [[CursorAI/@/Cursor Rules]]
			- enter `@Cursor Rules` then select `Testing Docs At Reference No Space`
			- Expected Behavior and Observed behavior is same as in ((67cc8297-c6ce-42a8-8c44-ae138563ec21))