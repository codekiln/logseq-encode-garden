created-by:: [[Person/codekiln]]
date-created:: [[2025/03]]

- # [Scan for Project Rules in Subdirectories of .cursor/rules - Feature Requests - Cursor - Community Forum](https://forum.cursor.com/t/scan-for-project-rules-in-subdirectories-of-cursor-rules/61534)
	- ## Update - [[My Notes]]
		- This is now possible in `0.47`; see [[CursorAI/Project Rule/Test/Agent/✅/Find MDC/in Subfolder]]
	- ## #[[Original Poster]]
	  collapsed:: true
		- According to [my tests](https://codekiln.github.io/logseq-encode-garden/#/page/cursorai%2Fproject%20rule%2Ftest), as of `v0.46.11`, Cursor does not activate project rules which are stored in sub-directories of the `.cursor/rules/` location. See [codekiln/cursor-project-rule-test: Testing the Cursor Project Rule feature](https://github.com/codekiln/cursor-project-rule-test/tree/main) for an independent repository you can clone and test.
		  id:: 67cd820f-9032-4812-9511-89dc99f62135
		- If Cursor did, then we would be able to use [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to reference Cursor Project Rules stored in a centralized repository, shared among many users and projects. This would unlock a whole new way to share project rules between users and repositories. In my opinion, it’s very important that Cursor enable its community to collaborate together on developing mature, open source cursor rules, and adding this feature would be an important step in that direction.
		- An example of the types of repositories that could be contributed on by multiple people is [[Person/codekiln/GitHub/cursor-ai-sdlc]], which proposes a way to use a particular directory to be a bridge between external tools like [[JIRA]] and the [[SDLC]].
		- A number of users in the community have been interested in this functionality; see [Mastering Cursor Rules: A Developer’s Guide to Smart AI Integration - DEV Community](https://dev.to/dpaluy/mastering-cursor-rules-a-developers-guide-to-smart-ai-integration-1k65) for an example.
		- I’ve listed a number of dynamics and workarounds at [CursorAI/How To/Share Cursor Project Rules Across Repositories and Users](https://codekiln.github.io/logseq-encode-garden/#/page/cursorai%2Fhow%20to%2Fshare%20cursor%20project%20rules%20across%20repositories%20and%20users).