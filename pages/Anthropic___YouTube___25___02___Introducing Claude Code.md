# [Introducing Claude Code - YouTube](https://www.youtube.com/watch?v=AJpK3YTTKZ4) - [[Anthropic/App/Claude Code]]
- runtime: 3min 54sec
	- ## my #notes
	  id:: 67bda95a-e5c3-4ba8-b5ec-a918606d2244
		- ((67bdac23-a87b-4eb9-8558-6222ee77337b))
		- ((67bdad0a-ee74-4ac1-996f-e5ba4e4feebf))
	- ## Vid
		- {{video https://www.youtube.com/watch?v=AJpK3YTTKZ4}}
			- ### Intro (skip)
			  collapsed:: true
				- {{youtube-timestamp 0}} Should we be doing like big smile or? - No, what you're doing- - Big smile's creepy. That's sort of what I'm getting at. I'm Boris, I'm an engineer. I'm Cat, I'm a product manager. We love seeing what people build with Claude, especially with coding,
				- {{youtube-timestamp 12}} and we want to make Claude better at coding for everyone. We built some tools, one of which we're sharing today. We're launching Claude Code as a research preview. Claude Code is an agentic coding tool
			- ### opening #Terminal and invoking `claude` [[CLI/Tool]]
				- {{youtube-timestamp 27}} that lets you work with Claude directly in your terminal. We're gonna show you an example of it in action. So we have a project here. It's a [[nextjs]] app. {{youtube-timestamp 35}} Let's open it up in an instance of Claude Code.
					- *right click on project folder > Services > New [[iTerm2]] Window Here*
					- *In the CLI: `claude` is invoked*
			- ### overview
				- {{youtube-timestamp 41}} Now that we've done this, Claude Code has access to all of the files in this repository.
					- One of the first times I've seen a compelling [[Chat]] #UI in #CLI - is this [[Curses]]?
					  id:: 67bdac23-a87b-4eb9-8558-6222ee77337b
				- We don't know much about this codebase. It looks like an app for chatting with a customer support agent.
			- ### explain codebase
				- Let's get Claude to help explain this codebase to us.
					- *they prompt it: "explain to me this project structure"*
				- Claude starts by reading the higher level files
				- {{youtube-timestamp 59}} and then it dives in deeper. Now it's going through all the components in the project. Cool, here's its final analysis.
					- *it gathers lots of context from the repository its analysis produces a report of key dependencies, deployment, project structure, etc*
					- *will this remove the need for tools like [[Repomix]] ?*
					  id:: 67bdad0a-ee74-4ac1-996f-e5ba4e4feebf
					- *it takes a minute or more (they speed it up)*
			- ### {{youtube-timestamp 76}} use case - editing code to update the website served by the repo
				- **use case - editing code:** So say I was asked to replace this left sidebar with a chat history, and I'm also gonna add a new chat button.
				- {{youtube-timestamp 82}} I'm gonna ask Claude to help me out here. We haven't specified any files or paths and Claude's already finding the right files to update by itself. Claude can also show its thinking and we can see how it's decided to tackle this problem.
			- {{youtube-timestamp 104}} Claude's asking me if I wanna accept these changes. I'll say, yeah. Now Claude's updating the nav bar, adding a button and icons as well. Next, it's updating the logic to ensure the saving state works correctly. After a bit, Claude completes the task.
			- {{youtube-timestamp 125}} Here's a summary of what it's done. Let's take a look at the app. So we're seeing the new chat button and new chat history section on the left. Let's check if I can start a new chat while keeping the previous one saved.
			- {{youtube-timestamp 140}} I'll try out the new chat button too. Great, it's all working. Now let's ask Claude to add some tests to make sure that the features we just added work. Claude's asking for permission to run commands. We'll say yes.
			- {{youtube-timestamp 161}} Claude is making some changes to run these tests. After getting the results, it continues with its plan until all tests pass. After a few minutes, it looks like we're good to go. Now I'm going to ask Claude to compile the app
			- {{youtube-timestamp 188}} and see if we get any build errors. Let's see what it finds. Claude identified the build errors and is now fixing them. Then it tries to build again. It'll keep going until it works. Now let's finish everything up by asking Claude to commit its changes
			- {{youtube-timestamp 210}} and push them to GitHub. Claude creates a summary and a description of our changes. And it'll push the changes to GitHub. That's it, that's an example of what Claude Code can do. We can't wait for people to start building with it.
		-