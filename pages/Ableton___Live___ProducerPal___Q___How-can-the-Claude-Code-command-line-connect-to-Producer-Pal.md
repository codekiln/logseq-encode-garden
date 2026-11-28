logseq-entity:: [[Logseq/Entity/Question]]
via:: [[GitP/A/Log/26/11/28-Sat]]

- # How can the [[Claude/Code]] command line connect to [[Ableton/Live/ProducerPal]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Claude Code · Producer Pal](https://producer-pal.org/installation/claude-code), [Ableton Live Agent Skills · Producer Pal](https://producer-pal.org/guide/skills) and [Ableton Live REST API · Producer Pal](https://producer-pal.org/guide/rest-api)
		- **Short answer:** register Producer Pal as an MCP server with `claude mcp add`, or install Producer Pal's Agent Skill. Either way the Producer Pal device has to be running in the open Live Set, and its server listens on port 3350.
		- ### MCP server through npx
			- The recommended way. It works whether Claude Code or Live starts first, and reconnects on its own. It needs Node.js 20 or later.
			- ~~~sh
			  claude mcp add producer-pal npx producer-pal@latest
			  ~~~
			- `--tools` keeps only the listed tool groups, such as `--tools core,clip,track`, and `--tools read-only` cuts the instructions the model receives by more than half. Flags for the server go after `--`: `claude mcp add producer-pal -- npx producer-pal@latest --tools read-only`.
			- For an agent that writes code which builds or parses Producer Pal data, the site suggests `--format json --notation midi-json`. Ordinary music-making keeps the defaults, which use fewer tokens.
		- ### MCP server over HTTP
			- Points Claude Code straight at the device's endpoint. The device must already be running, and it doesn't reconnect on its own.
			- ~~~sh
			  claude mcp add --transport http producer-pal http://localhost:3350/mcp
			  ~~~
		- ### Agent Skill
			- A skill folder, `producer-pal/`, with a `SKILL.md` and a small Node script, `ppal.mjs`, that calls the REST API. No MCP setup is needed.
			- ~~~sh
			  curl -L https://producer-pal.org/downloads/producer-pal-skill.zip -o /tmp/ppal-skill.zip
			  unzip -o /tmp/ppal-skill.zip -d ~/.claude/skills/
			  ~~~
			- A project's own `.claude/skills/` folder keeps the skill to that project.
			- The site recommends the skill for coding agents: it can choose its notation and toolset per request and re-read the tool schemas mid-session. An MCP client fixes the tool descriptions when a conversation starts.
		- ### After setup
			- MCP servers added with `claude mcp add` load when a session starts, so a running session doesn't see them. Start a new `claude` session, run `/mcp` to check the Producer Pal tools are listed, then ask it to connect to Ableton.
		- ### Without any setup
			- The REST API needs no MCP client: `GET http://localhost:3350/api/tools` lists the tools, and `POST http://localhost:3350/api/tools/<toolName>` with a JSON body calls one. A Claude Code session without Producer Pal configured can still reach Live this way with `curl`.
			- The MCP endpoint at `http://localhost:3350/mcp` also answers plain JSON-RPC requests, which is how a session without the tools built the `LPP CM8 Lights` and `LPP CM8 Paint` tracks for [[Launchpad/Custom/Idea/Control-Rendering-With-Ableton-and-MIDI]].
