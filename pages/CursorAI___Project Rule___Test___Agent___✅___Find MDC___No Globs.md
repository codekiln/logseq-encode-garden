# Can Cursor Agent Mode find [[.mdc]] files that lack [[globs]]? **YES**
	- Tests whether [[CursorAI/Agent]] mode activates `.mdc` project rules by description even if they do not have any have globs attached to them
	  id:: 67cd6044-e287-4722-8c96-cc5d9b743728
	- ## Test Cursor Project Rule File
		- Place this file at `.cursor/rules`
			- [[CursorAI/Project Rule/Link/GitHub]]
				- [test-favorite-cars.mdc](https://github.com/codekiln/logseq-encode-garden/blob/main/.cursor/rules/test-favorite-cars.mdc)
	- ## Test
		- {{embed [[CursorAI/Project Rule/Test/Standard Setup]]}}
		- Activate Agent mode in Cursor chat
		- Type "what are my favorite apples?" and hit enter
	- ## Expected Behavior
		- Cursor Agent surfaces the correct rule in the chat
		- Cursor Agent answers according to the contents of the rule
	- ## Observed Behavior
		- ### `0.46.11`
			- ✅ Cursor Agent surfaces the correct rule in the chat
				- > Let me check the rule about favorite cars to answer your question
			- ✅ Cursor Agent answers according to the contents of the rule
				- > Based on the provided rule, I can tell you about the DeLorean from Back to the Future! ...