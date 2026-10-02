logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[1Password/Environment/MCP]], [[Unix/Q/What is a named pipe in unix, and how do 1Password Environments use one to mount a .env?]]

- # What can I do with [[1Password]] in [[Claude/Desktop/Code]] vs [[Codex]] in the [[ChatGPT/App/Desktop]], as of 2026-09-30?
	- ## [[AI Answer]]
		- **Short answer:** For [[1Password/Environment]]s, the two are nearly the same. 1Password ships a plugin for each, and both plugins wrap the same local `1password-mcp` server with the same eight tools and the same `1password-environments` skill. The Claude plugin adds one thing the Codex plugin lacks: a hook that stops shell commands when a mounted `.env` is broken. The loud "1Password for Claude" launch in July 2026 was about something else, browser logins, and it is not aimed at the Code tab.
		- ### Side by side
			- | Capability                                    | [[Claude/Desktop/Code]] + 1Password          | [[Codex]] in [[ChatGPT/App/Desktop]] + 1Password |
			  | --------------------------------------------- | -------------------------------------------- | ------------------------------------------------ |
			  | 1Password-built plugin                        | [[1Password/GitHub/1password-claude-plugin]] | [[1Password/GitHub/1password-codex-plugin]]      |
			  | List, create, rename Environments             | ✓                                            | ✓                                                |
			  | See variable names, never values              | ✓                                            | ✓                                                |
			  | Append variables and placeholders             | ✓                                            | ✓                                                |
			  | Mount an Environment as a local `.env`        | ✓ macOS, Linux                               | ✓ macOS; Windows unclear                         |
			  | Import-and-mount skill                        | ✓ `1password-environments`                   | ✓ `1password-environments`                       |
			  | Hook that checks mounts before shell commands | ✓ `PreToolUse`                               | ✗ not shipped                                    |
			  | Install from the GitHub repo as a marketplace | ✓                                            | ✓                                                |
			  | `op` CLI and SSH agent in the terminal        | ✓                                            | ✓                                                |
			  | Agent browser logins through 1Password        | ~ macOS; for browser tasks, not Code tab     | ✗ none found                                     |
		- ### Environments: what is the same
			- Both plugins register `1password-mcp` ([[1Password/Environment/MCP]]) and expose `authenticate`, `list_environments`, `create_environment`, `rename_environment`, `list_variables`, `append_variables`, `create_local_env_file`, and `list_local_env_files`.
			- The agent sees Environment names, variable names, and mount paths. Values stay in 1Password. The desktop app asks for approval the first time a client touches an Environment.
			- Useful prompts are identical on both sides: "import `.env` into 1Password and mount it here", "add a placeholder for my OpenAI API key".
			- Outside the plugins, both apps run commands in a local shell, so `op run`, `op read`, [[1Password/Dev/CLI/Shell Plugin]]s, and the 1Password SSH agent behave the same way in either one.
		- ### Environments: what differs
			- **Mount check hook.** The Claude plugin's `PreToolUse` [[Claude/Code/Hook]] runs before every Bash command. It checks that each mounted `.env` exists, is a named pipe, and is switched on in 1Password, and blocks the command when one is not, so Claude can say "your staging mount is off" instead of your app failing with a missing key. The Codex plugin ships skills and MCP config but no hook. That gap comes from 1Password, not Codex: [[Codex/Hook]]s support `PreToolUse`, and Codex plugins can bundle `hooks/hooks.json`. 1Password's separate [agent-hooks](https://github.com/1Password/agent-hooks) repo lists Cursor, Claude Code, GitHub Copilot, and Windsurf, and does not list Codex.
			- **Windows.** The Claude plugin says mounts and the MCP server are macOS and Linux only. On Windows its skill switches to `op run --environment=<id> -- <command>` ([[1Password/Dev/op/run]]). The Codex plugin README claims macOS, Windows, and Linux. The Claude README also says "1Password Environments has no local `.env` mounts on Windows", so on a Windows ChatGPT desktop app, expect the listing and editing tools to work and mounting to fail until 1Password says otherwise.
			- **Turning the server on.** The Claude README points to a Labs experiment, **Settings → Labs → MCP Server** (feature flag `ai-local-mcp-server`). The Codex README points to **Settings → Developer**. These two 1Password READMEs contradict each other, and the likeliest reason is that the setting moved out of Labs. Check your own 1Password build.
			- **Install path.**
				- Code tab: `/plugin marketplace add 1Password/1password-claude-plugin`, then `/plugin install 1password@1password`. The Code tab uses the same plugin system as the CLI ([[Claude/Code/Plugin/Marketplace]]).
				- Codex: `codex plugin marketplace add 1Password/1password-codex-plugin`, then restart and turn the plugin on ([[Codex/Plugin]]). The OpenAI Plugin Directory listing is skills-only, because the directory refuses local stdio MCP servers, so installing from the directory gets the skill without the server. Install from GitHub to get both.
			- **Not a Claude Desktop extension.** The Claude repo's GitHub description says "Claude desktop extension (MCPB) for macOS", and that is out of date. The repo is now a Claude Code plugin with no `.mcpb` bundle, so it adds nothing to Claude Desktop's chat or Cowork tabs through [[Claude/Desktop/Extension]].
			- **Code tab's own env vars.** [[Claude/Desktop/Code]] also has a **Local** environment editor that Claude Desktop stores for you. That is Anthropic storage, not 1Password, and it works independently of the plugin.
		- ### Browser logins: the part the blog covers
			- The [1Password for Claude](https://1password.com/blog/1password-for-claude) launch (July 16, 2026) lets Claude sign in to websites without seeing the password. When Claude needs a login, 1Password asks you to approve with Touch ID, then injects the credential straight into the page, so it never enters Claude's context. The 1Password browser extension adds an **Agentic Mode** that locks the vault down to only the logins you approved. ([Help Net Security](https://www.helpnetsecurity.com/2026/07/17/1password-anthropic-claude-integration/), [Engadget](https://www.engadget.com/2216405/1password-anthropic-claude-integration/), [1Password Marketplace](https://marketplace.1password.com/integration/1password-for-claude))
			- It requires macOS, a paid Claude plan, the Claude desktop app with Claude's browser extension, and the 1Password desktop app with its browser extension. It targets Claude driving your browser, as in [[Claude/Cowork]], not the Code tab's terminal work. The Code tab's built-in [[Claude/Desktop/Code/Browser]] pane is not mentioned in any source found, so treat it as unsupported until tested.
			- The ChatGPT desktop app has no counterpart as of 2026-09-30. [[ChatGPT/Atlas]] shut down on August 9, 2026, after being folded into the desktop app. Search turned up no 1Password agentic-autofill integration for ChatGPT or Codex. The May 2026 1Password and OpenAI announcement ([1Password press](https://1password.com/press/2026/may/openai-codex-integration)) is the Environments MCP server described above.
		- ### Which to pick
			- For secrets in a repo on a Mac, either works. The Code tab has the edge because the hook catches broken mounts before a command runs.
			- For Claude or Codex to sign in to websites, only Claude has a 1Password integration today, and it lives in Claude's browser tasks rather than the Code tab.
		- ### Sources and gaps
			- Plugin facts come from the two repos' READMEs and file trees as of 2026-09-30.
			- The 1Password blog and docs sites were blocked from this research session, so the browser-login summary relies on press coverage, and the Labs-versus-Developer setting has not been checked against a running 1Password app.
