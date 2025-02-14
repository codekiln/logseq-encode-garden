created-by:: [[Person/Brian Madison]]

- [Composer Agent Refined Workflow - Detailed Instructions and Example Repo for Practice - How To - Cursor - Community Forum](https://forum.cursor.com/t/composer-agent-refined-workflow-detailed-instructions-and-example-repo-for-practice/47180)
	- #Observations
		- longer post, lots of compelling, concrete suggestions on how to follow
	- #Quotes
		- High level
			- a .ai folder is the project mgmt history and memory for the project or task at hand.
			- with each item, it creates a story file with breakdown in great detail of how it will meet the objective, and then waits for my review of it.
			- once I approve it will execute and generally also use TDD
			- sometimes it thinks it is done, so i will tell it to run the tests (if it did not) and it will iterate on testing until it is all working
			- Between stories, I start a new chat - the nice thing is I can just greet the AI or ask it whats up, and it will know and suggest to generate a new story file or continue on the current one.
		- [[CursorAI/Agent Mode/Cost]]
			- > **Using Agent mode in cursor of course it not the most cost effective, but it will give you a glimpse** ... it works very well!
			- > don’t burn tool usage on simple things that you can be scripted into simple commands
			- [[CursorAI/Technique/Frontload Design]]
				- > Spend the MOST time on your plan / what you want to have built in the end, a good PRD with tech stack, constraints, preferences, clear goal, and details Story breakdown.
				- > Once Other cheaper / free models bugs are worked out, they will be better to use for generating stories and updating the PRD in an iterative fashion with the AI in cursor - in the meantime, feel the credit burn, or use external AI tool (especially for the PRD)
		- > More details and best practices in the repo [[GitHub/bmadcode/hak-news-aiadd-1]] - you can get an idea after a few days of running it through this process - it implemented the 9 stories in the .ai folder.
		-