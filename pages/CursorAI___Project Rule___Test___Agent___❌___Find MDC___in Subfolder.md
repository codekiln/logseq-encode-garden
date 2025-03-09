# Can Cursor Agent Mode pick up mdc files in subfolders? **NO**
	- Tests whether [[CursorAI/Agent Mode]] activates `.mdc` project rules by description when they are found in a subdirectory of `.cursor/rules`, such as in `.cursor/rules/subfolder/*.mdc`
	  id:: 67cd60f9-b734-486d-b050-7c9527e32250
	- ## Test Cursor Project Rule File - [[CursorAI/Test/Fixture/Subfolder Favorite Apples project rule]]
		- Install this cursor rule in the specified location (inside the `subfolder`):
			- [.cursor/rules/subfolder/test-favorite-apples.mdc](https://github.com/codekiln/logseq-encode-garden/blob/main/.cursor/rules/subfolder/test-favorite-apples.mdc)
	- ## Test
		- {{embed [[CursorAI/Project Rule/Test/Standard Setup]]}}
		- Activate Agent mode in Cursor chat
		- Type "what are my favorite apples?" and hit enter
	- ## Expected Behavior
		- Cursor Agent surfaces the correct rule
		- Cursor Agent answers according to the contents of the rule
	- ## Observed Behavior
		- ### `0.46.11`
			- Cursor Agent searches the codebase for the keyword
			- "I don't see any rules or information in the codebase about favorite apples. The only rule available is about favorite cars."
-