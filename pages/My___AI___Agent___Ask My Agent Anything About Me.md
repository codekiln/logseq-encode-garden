tags:: [[Diataxis/How To]]
see-also:: [[My]]
- # Ask My Agent Anything About Me
	- ## Overview
		- This walks you from nothing to chatting with my agent — an AI that answers questions about me using only this [[Knowledge Garden]], and that cites the pages behind each answer.
		- It is for someone who has my link and wants to get to know me, even with no setup yet. You install two free tools, copy the garden to your computer, and start asking.
		- It takes about ten minutes.
	- ## Prerequisites
		- A computer with a terminal: Terminal on macOS, any terminal on Linux, or WSL on Windows.
		- [git](https://git-scm.com/downloads). Check with `git --version`, and install it if that fails.
		- An AI coding agent. The one-command path below uses Claude Code, which needs a paid [Claude plan](https://claude.com/pricing) (Pro starts around $20 per month) or pay-as-you-go API credits; mise installs the agent itself in step 3. To ask for free instead, skip to "Free alternative: GitHub Copilot".
	- ## Steps
		- ### 1. Install mise
			- mise is the one tool that installs everything else and runs the agent for you.
			- On macOS or Linux, run this, then open a new terminal window:
			- ~~~sh
			  curl https://mise.run | sh
			  ~~~
			- If it prints a line to add to your shell, run that line first so your terminal can find mise.
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
			- The first time, the agent asks you to sign in to Claude with your paid plan, or to set up API credits. After that, type any question about me and press Enter, such as "What does codekiln care about?" or "What have they been reading lately?".
	- ## Free alternative: GitHub Copilot
		- To ask at no cost, use GitHub Copilot's free tier in [VS Code](https://code.visualstudio.com). You still need git and the cloned folder from step 2, but not mise or a paid plan.
		- 1. Install VS Code and its GitHub Copilot extension, then sign in with a free GitHub account, which includes Copilot Free.
		- 2. Open the `logseq-encode-garden` folder.
		- 3. Open Copilot Chat, switch it to agent mode, and ask your question about me.
		- The garden ships Copilot instructions, so the agent answers from its pages and journals. The free tier limits how many agent requests you get each month.
		- Already use Cursor, Codex, or Claude Code? Open the folder in any of them and ask — each reads the garden's bundled setup.
	- ## Troubleshooting
		- `mise: command not found` — open a new terminal window, or run the activation line the install step printed.
		- The agent does not start — run `mise install` again to make sure the AI agent finished downloading, then retry step 4.
		- You do not want to pay for Claude — use "Free alternative: GitHub Copilot" above.
	- ## This page on [[GitHub]]
		- [View this page's source on GitHub](https://github.com/codekiln/logseq-encode-garden/blob/main/pages/My___AI___Agent___Ask%20My%20Agent%20Anything%20About%20Me.md)
