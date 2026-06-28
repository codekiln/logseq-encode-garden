tags:: [[Diataxis/How To]]
see-also:: [[My]]
github-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/pages/My___AI___Agent___Ask%20My%20Agent%20Anything%20About%20Me.md

- # Ask My Agent Anything About Me
	- ## Where am I?
		- you're at a page somewhere in the middle of [[My/Knowledge/Garden/logseq-encode-garden]] that's about to describe how you can ask an AI anything about me that's present in the garden.
	- ## What the ...?
		- Maybe this is corny, or maybe AI is not your thing. Avert your eyes if so. Otherwise, read on.
		- Let's say you want to get in touch with me.
			- Well, maybe send me an email, if you can.
			- Or open a github issues on this knowledge garden, perhaps.
		- But if you'd like to hang out in my little [[Knowledge Garden]] and get to know it and me a bit, and if you have an [[AI Coding Tool]], then this page shows you how to install [[Agent/Skills]] and get them set up so you can ask my agent about me, backed by this knowledge garden. It's a work-in-progress avatar of [[Person/codekiln]].
	- ## Prerequisites
		- A computer with a terminal: Terminal on macOS, any terminal on Linux, or WSL on Windows.
		- [git](https://git-scm.com/downloads). Check with `git --version`, and install it if that fails.
		- An AI coding agent — any one of [[Claude Code]], [[Codex]], [[CursorAI]], or [[GitHub/CoPilot]]. Install at least one before step 4; the task detects which you have and starts it. mise installs the setup tool ([[rulesync]]) for you in step 3, but not the agent itself. To ask for free, [[GitHub/CoPilot]] has a free tier; the others need a paid plan. See "Which AI agent?" below to choose.
	- ## Steps
		- ### 1. Install [[mise]] if you don't already have it
			- mise is one of my favorite tools. It's by [[Person/Jeff Dickey]], an awesome developer. It's a [[CLI/Tool]] that provides a task runner harness and can install any version of any CLI tool.
			- On macOS or Linux, run this, then open a new terminal window:
			- ~~~sh
			  curl https://mise.run | sh
			  ~~~
			- If it prints a line to add to your shell.
				- **If** you want to use mise generally, then I recommend that you add that line to your shell so your terminal can find mise for each of the [[mise Jobs to be Done]].
					- see also
						- {{embed ((6a2148e7-de37-41eb-8e2a-be0625840863))}}
				- **Else** if you just want to get started here without using mise more generally on your computer, just run [[mise/activate]] before the next tasks.
			- On Windows, install mise inside WSL, or follow the [mise install guide](https://mise.jdx.dev/getting-started.html).
			- Check that it works:
			- ~~~sh
			  mise --version
			  ~~~
		- ### 2. Copy this knowledge garden, `logseq-encode-garden` to your computer
			- ~~~sh
			  git clone https://github.com/codekiln/logseq-encode-garden
			  cd logseq-encode-garden
			  ~~~
		- ### 3. Let [[mise]] set it up
			- From inside the folder, allow this project's settings, then install what it needs. This installs the setup tool ([[rulesync]]) — not the AI agent, which you bring yourself (see "Which AI agent?").
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
			- The task finds your AI agent, sets up that tool's skill if it isn't ready, and starts it. If you have more than one agent, it asks which to use; to choose up front, run `mise run ask-my-agent-anything-about-me --tool copilot` (or `claude`, `codex`, `cursor`).
			- The first time, your agent may ask you to sign in or authorize it. After that, type any question about me and press Enter, such as "What does codekiln care about?" or "What have they been reading lately?".
	- ## Which AI agent?
		- The task works with any of these. Pick one, install it, and the one-command path above does the rest.
			- [[GitHub/CoPilot]] — has a **free tier**, so this is the no-cost option. A free GitHub account includes Copilot Free.
			- [[Claude Code]] — paid: a [Claude plan](https://claude.com/pricing) (Pro starts around $20 per month) or API credits.
			- [[Codex]] — paid, via an OpenAI account.
			- [[CursorAI]] — paid; its terminal agent is `cursor-agent`.
		- Prefer an editor to the terminal? Open the `logseq-encode-garden` folder in [VS Code](https://code.visualstudio.com) with GitHub Copilot, or in [[CursorAI]], switch the assistant to agent mode, and ask — each reads the garden's bundled skill. With Copilot, the free tier limits how many agent requests you get each month.
	- ## Troubleshooting
		- `mise: command not found` — open a new terminal window, or run the activation line the install step printed.
		- "No supported AI agent was found" — install one from "Which AI agent?" above, then retry step 4. If yours is installed but not detected, name it: `mise run ask-my-agent-anything-about-me --tool <name>`.
		- The skill seems out of date — rebuild your tool's config: `mise run ask-my-agent-anything-about-me --generate`.
		- You do not want to pay — use [[GitHub/CoPilot]]'s free tier (see "Which AI agent?").