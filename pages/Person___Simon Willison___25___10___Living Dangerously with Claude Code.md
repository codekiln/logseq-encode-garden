- [Living dangerously with Claude](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/?__readwiseLocation=#atom-everything) - [[Claude Code/--dangerously-skip-permissions]]
	- [[Person/Simon Willison]] talks about You Only Live Once ([[YOLO]]) mode, aka [--dangerously-skip-permissions - for use in special Development containers - Claude Docs](https://docs.claude.com/en/docs/claude-code/devcontainer), which has advantages ...
	  
	  > The wild thing is that all three of these projects weren’t even a priority for me—**they were side quests**, representing pure curiosity that I could outsource to Claude Code and solve in the background while I was occupied with something else.
	- * but he takes this opportunity to also talk zero in on risks of prompt injection, and why it's important. perfect example ...
	  
	  > If a coding agent—in this case OpenHands— reads this env.html file it can be tricked into grepping the available environment variables for hp_ (matching GitHub Personal Access Tokens) and sending that to the attacker’s external server for “help debugging these variables”.