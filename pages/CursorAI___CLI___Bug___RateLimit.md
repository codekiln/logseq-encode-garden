tags:: [[Bug]]

- ## [[Expected Behavior]]
	- in `cursor-agent`
		- if model runs out of rate limit
			- interactive [[TUI]] mode or [[CLI]] mode
				- it displays a warning in interactive mode and displays commands to switch models
				- it is easy to set an [[AI/Coding/Config]] such that it will always fall back to a model with rate limits available and display a warning
- ## [[Behavior/Observed]]
	- in `cursor-agent`
		- if model runs out of rate limit
			- interactive [[TUI]] mode
				- the agent does not respond and no error is displays
			- [[CLI]] mode
				- it displays a warning in interactive mode and exits with code 1
	- When trying to run cursor-agent in interactive mode, I've encountered times when the agent just wouldn't respond and it would not show an error.
	- To see the error, use `--exec --print`, which will show an [[Error]] like:
		- ```
		  S: Increase limits for faster responses claude-4.6-opus-high-thinking is not available in the slow pool. Please switch to auto or Auto.
		  💡 Command failed with exit code 1. Press Enter to fix.
		  ```
- ## [[Workaround]]
	- [[CLI]]
		- 1 - list models
			- [[CursorAI/CLI/list-models]]
				- ```
				  cursor-agent --list-models
				  Available models
				  
				  auto - Auto
				  composer-1.5 - Composer 1.5
				  composer-1 - Composer 1
				  gpt-5.3-codex - GPT-5.3 Codex
				  gpt-5.3-codex-low - GPT-5.3 Codex Low
				  gpt-5.3-codex-high - GPT-5.3 Codex High
				  gpt-5.3-codex-xhigh - GPT-5.3 Codex Extra High
				  gpt-5.3-codex-fast - GPT-5.3 Codex Fast
				  gpt-5.3-codex-low-fast - GPT-5.3 Codex Low Fast
				  gpt-5.3-codex-high-fast - GPT-5.3 Codex High Fast
				  gpt-5.3-codex-xhigh-fast - GPT-5.3 Codex Extra High Fast
				  gpt-5.2 - GPT-5.2
				  gpt-5.2-codex - GPT-5.2 Codex
				  gpt-5.2-codex-high - GPT-5.2 Codex High
				  gpt-5.2-codex-low - GPT-5.2 Codex Low
				  gpt-5.2-codex-xhigh - GPT-5.2 Codex Extra High
				  gpt-5.2-codex-fast - GPT-5.2 Codex Fast
				  gpt-5.2-codex-high-fast - GPT-5.2 Codex High Fast
				  gpt-5.2-codex-low-fast - GPT-5.2 Codex Low Fast
				  gpt-5.2-codex-xhigh-fast - GPT-5.2 Codex Extra High Fast
				  gpt-5.1-codex-max - GPT-5.1 Codex Max
				  gpt-5.1-codex-max-high - GPT-5.1 Codex Max High
				  opus-4.6-thinking - Claude 4.6 Opus (Thinking)  (current, default)
				  gpt-5.2-high - GPT-5.2 High
				  opus-4.6 - Claude 4.6 Opus
				  opus-4.5 - Claude 4.5 Opus
				  opus-4.5-thinking - Claude 4.5 Opus (Thinking)
				  sonnet-4.6 - Claude 4.6 Sonnet
				  sonnet-4.6-thinking - Claude 4.6 Sonnet (Thinking)
				  sonnet-4.5 - Claude 4.5 Sonnet
				  sonnet-4.5-thinking - Claude 4.5 Sonnet (Thinking)
				  gpt-5.1-high - GPT-5.1 High
				  gemini-3.1-pro - Gemini 3.1 Pro
				  gemini-3-pro - Gemini 3 Pro
				  gemini-3-flash - Gemini 3 Flash
				  gpt-5.1-codex-mini - GPT-5.1 Codex Mini
				  grok - Grok
				  
				  Tip: use --model <id> (or /model <id> in interactive mode) to switch.
				  ```
		- 2 - specify model id each time
			- `cursor-agent --print --exec --model <id> <prompt>`
		-
-