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
		- A free [Claude account](https://claude.ai) for the AI agent. Other AI tools work too — see "Use a different AI tool instead" below.
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
			- The first time, the agent asks you to sign in to your Claude account. After that, type any question about me and press Enter, such as "What does he care about?" or "What has he been reading lately?".
	- ## Use a different AI tool instead
		- If you would rather skip mise or Claude, open the `logseq-encode-garden` folder in any AI coding tool — Cursor, Codex, GitHub Copilot, or Claude Code. The garden carries its own AI setup, including the agent's instructions, so you can start asking about me right away.
	- ## Troubleshooting
		- `mise: command not found` — open a new terminal window, or run the activation line the install step printed.
		- The agent does not start — run `mise install` again to make sure the AI agent finished downloading, then retry step 4.
		- You do not want a Claude account — use "Use a different AI tool instead" above.
