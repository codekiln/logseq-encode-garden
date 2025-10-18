tags:: [[HackerNews]]

- # [OpenAI Codex CLI: Lightweight coding agent that runs in your terminal | Hacker News](https://news.ycombinator.com/item?id=43708025)
	- ## [[My Notes]] [[2025-04-18 Fri]]
	  id:: 68021420-5b60-4dcf-a5b6-b18dba954e26
	  collapsed:: true
		- great discussion comparing various [[AI Coding]] tools and [[AI Coding Techniques]] and related issues
			- nobody is very impressed with [[OpenAI Codex]] at [[HackerNews]] at this time
			- first I've heard anyone have anything nice to say about [[AWS/Q]]
				- > Claude Code is just way too expensive. These days I’m using Amazon Q Pro on the CLI. Very similar experience to Claude Code minus a few batteries. But it’s capped at $20/mo and won’t set my credit card on fire. --[artdigital here](https://news.ycombinator.com/item?id=43712470)
			- a lot of people are very passionate about [[IDE/Cline]], [[Claude Code]], [[aider]] but say Claude Code is too [[Expensive]]
				- > I use [[aider]]+ [[OpenRouter]] with [[Gemini/2.5/pro]] and it cost 1/6 of what [[Claude 3.7 Sonnet]] does. The [[aider/docs/llms/leaderboard]] - includes relative pricing theses days. - [aitchnyu](https://news.ycombinator.com/user?id=aitchnyu) [here](https://news.ycombinator.com/item?id=43713490)
					- This table mentions two different "Edit formats" - `architect` vs `diff` vs `diff-fenced` vs `whole` - these terms are new to me
				- > [[Google/AI/Model/Gemini/2.5/pro/experimental]] is superior to [[Claude 3.7 Sonnet]] when I use it with Aider [1]. And it is free (with some high limit).
				- A few people mention that [[Claude Code]] is actually **not** that expensive once you learn to control costs
					- [jasonjmcghee](https://news.ycombinator.com/user?id=jasonjmcghee) [1 day ago](https://news.ycombinator.com/item?id=43711801) on controlling claude code costs
					  collapsed:: true
						- If you get a hang of controlling costs, it's much cheaper. If you're exhausting the context window, I'm not surprised you're seeing high cost.
						- Be aware of the "cache".
						- Tell it to read specific files, never use /compact (that'll bust cache, if you need to, you're going back and forth too much or using too many files at once).
						- Never edit files manually during a session (that'll bust cache). THIS INCLUDES LINT.
						- Have a clear goal in mind and keep sessions to as few messages as possible.
						- Write / generate markdown files with needed documentation using claude.ai, and save those as files in the repo and tell it to read that file as part of a question.
						- **I'm at about ~$0.5-0.75 for most "tasks" I give it**. I'm not a super heavy user, but it definitely helps me (it's like having a super focused smart intern that makes dumb mistakes).
						- **If i need to feed it a ton of docs etc. for some task, it'll be more in the few $, rather than < $1**. But I really only do this to try some prototype with a library claude doesn't know about (or is outdated).
						  **For hobby stuff, it adds up - totally**.
						- For a company, massively worth it. Insanely cheap productivity boost (if developers are responsible / don't get lazy / don't misuse it).
					- [Implicated](https://news.ycombinator.com/user?id=Implicated) [1 day ago](https://news.ycombinator.com/item?id=43712547) on controlling claude code costs
					  collapsed:: true
						- I keep seeing this sentiment [that [[Claude Code]] is too [[Expensive]]]and it's wild to me.
						- Sure, it might cost a few dollars here and there. But what I've personally been getting from it, for that cost, is so far away from "expensive" it's laughable.
						  Not only does it do things I don't want to do, in a _super_ efficient manner. It does things I don't know how to do - contextually, within my own project, such that when it's done I _do_ know how to do it.
						  Like others have said - if you're exhausting the context window, the problem is you, not the tool.
						  Example, I have a project where I've been particularly lazy and there's a handful of models that are _huge_. I know better than to have Claude read those models into context - that would be stupid. Rather - I tell it specifically what I want to do within those models, give it specific method names and tell it not to read the whole file, rather search for and read the area around the method definition.
						  If you _do_ need it to work with very large files - they probably shouldn't be that large and you're likely better off refactoring those files (with Claude, of course) to abstract out where you can and reduce the line count. Or, if anything, literally just temporarily remove a bunch of code from the huge files that isn't relevant to the task so that when it reads it it doesn't have to pull all of that into context. (ie: Copy/paste the file into a backup location, delete a bunch of unrelated stuff in the working file, do your work with claude then 'merge' the changes to the backup file and copy it back)
						- If a few dollars here and there for getting tasks done is "too expensive" you're using it wrong. The amount of time I'm saving for those dollars is worth many times the cost and the number of times that I've gotten unsatisfactory results from that spending has been less than 5.
						  I see the same replies to these same complaints everywhere - people complaining about how it's too expensive or becomes useless with a full context. Those replies all state the same thing - if you're filling the context, you've already screwed it up. (And also, that's why it's so expensive)
						  I'll agree with sibling commenters - have claude build documentation within the project as you go. Try to keep tasks silo'd - get in, get the thing done, document it and get out. Start a new task. (This is dependent on context - if you have to load up the context to get the task done, you're incentivized to keep going rather than dump and reload with a new task/session, thus paying the context tax again - but you also are going to get less great results... so, lesson here... minimize context.)
						- 100% of the time that I've gotten bad results/gone in circles/gotten hallucinations was when I loaded up the context or got lazy and didn't want to start new sessions after finishing a task and just kept moving into new tasks. If I even _see_ that little indicator on the bottom right about how much context is available before auto-compact I know I'm getting less-good functionality and I need to be careful about what I even trust it's saying.
						- It's not going to build your entire app in a single session/context window. Cut down your tasks into smaller pieces, be concise.
						- It's a skill problem. Not the tool.