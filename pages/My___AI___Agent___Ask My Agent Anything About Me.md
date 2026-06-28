tags:: [[Diataxis/How To]]
see-also:: [[My]]
github-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/pages/My___AI___Agent___Ask%20My%20Agent%20Anything%20About%20Me.md

- # Ask My Agent Anything About Me
	- ## What the ...?
		- Maybe this is corny, or maybe AI is not your thing. Avert your eyes if so. Otherwise, read on.
		- Let's say you want to get in touch with me.
			- Well, maybe send me an email, if you can.
			- Or open a github issues on this knowledge garden, perhaps.
		- But if you'd like to hang out in my little [[Knowledge Garden]] and get to know it and me a bit, and if you have an [[AI Coding Tool]], then this page shows you how to install [[Agent/Skills]] and get them set up so you can ask my agent about me, backed by this knowledge garden. It's a work-in-progress avatar of [[Person/codekiln]].
	- ## Prerequisites
		- A computer with a terminal: Terminal on macOS, any terminal on Linux, or WSL on Windows.
		- [git](https://git-scm.com/downloads). Check with `git --version`, and install it if that fails.
		- An AI coding agent. The one-command path below uses Claude Code, which needs a paid [Claude plan](https://claude.com/pricing) (Pro starts around $20 per month) or pay-as-you-go API credits; mise installs the agent itself in step 3. To ask for free instead, skip to "Free alternative: GitHub Copilot".
	- ## Steps
		- ### 1. Install [[mise]] if you don't already have it
			- mise is one of my favorite tools. It's by [[Person/Jeff Dickey]], an awesome developer. It's one tool that installs everything else and runs the agent for you.
			- On macOS or Linux, run this, then open a new terminal window:
			- ~~~sh
			  curl https://mise.run | sh
			  ~~~
			- If it prints a line to add to your shell.
				- If you want to use mise generally, then I recommend that you add that line to your shell so your terminal can find mise for each of the [[mise Jobs to be Done]].
				- If you just want to get started here, without using mise generally on your system, just run `mise activate` before the next tasks.
			- On Windows, install mise inside WSL, or follow the [mise install guide](https://mise.jdx.dev/getting-started.html).
			- Check that it works:
			- ~~~sh
			  mise --version
			  ~~~
		- ### 2. Copy the garden to your computer
			- ~~~sh
			  git clone https://github.com/codekiln/logseq-encode-garden
			  cd logseq-encode-garden
			  ~~~
		- ### 3. Let mise set it up
			- From inside the folder, allow this project's settings, then install what it needs. This step also downloads the AI agent.
			- ~~~sh
			  mise trust
			  mise install
			  ~~~
		- ### 4. Ask away
			- ~~~sh
			  mise run ask-my-agent-anything-about-me
			  ~~~
			- #### What does this do?
				- See [logseq-encode-garden/mise-tasks/ask-my-agent-anything-about-me at main · codekiln/logseq-encode-garden · GitHub](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/ask-my-agent-anything-about-me) for the source code.
				- Technically, the [[AI Skill]] it relies upon is managed by [[rulesync]] and is available here: [logseq-encode-garden/.rulesync/skills/ask-my-agent-anything-about-me/SKILL.md at main · codekiln/logseq-encode-garden · GitHub](https://github.com/codekiln/logseq-encode-garden/blob/main/.rulesync/skills/ask-my-agent-anything-about-me/SKILL.md)
			- The first time, the agent asks you to sign in to Claude with your paid plan, or to set up API credits. After that, type any question about me and press Enter, such as "What does codekiln care about?" or "What have they been reading lately?".
	- ## Free alternative: GitHub Copilot
		- To ask at no cost, use GitHub Copilot's free tier in [VS Code](https://code.visualstudio.com). You still need git and the cloned folder from step 2, but not mise or a paid plan.
		- 1. Install VS Code and its GitHub Copilot extension, then sign in with a free GitHub account, which includes Copilot Free.
		- 2. Open the `logseq-encode-garden` folder.
		- 3. Open Copilot Chat, switch it to agent mode, and ask your question about me.
		- The garden includes Copilot instructions, so the agent answers from its pages and journals. The free tier limits how many agent requests you get each month.
		- Already use Cursor, Codex, or Claude Code? Open the folder in any of them and ask — each reads the garden's included setup.
	- ## Troubleshooting
		- `mise: command not found` — open a new terminal window, or run the activation line the install step printed.
		- The agent does not start — run `mise install` again to make sure the AI agent finished downloading, then retry step 4.
		- You do not want to pay for Claude — use "Free alternative: GitHub Copilot" above.