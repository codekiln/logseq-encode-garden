logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[Codex/Plugin]], [[Claude/Code/Plugin/Skills-Directory Plugin]]
- # How To Develop and Share a Team Plugin for ChatGPT and Claude
	- ## Overview
		- Turn a recurring team workflow into a plugin, test it in ChatGPT, and share it with teammates. If the team also uses Claude, keep the reusable skills in one repository and package them for both hosts.
		- Product behavior and documentation checked October 15, 2026.
	- ## Prerequisites
		- A representative input, an example of the desired output, and the reference material the workflow needs.
		- Plugin Creator and permission to use plugins in the intended ChatGPT workspace. Sharing and publishing to the workspace directory have separate permissions. [ChatGPT plugin authoring](https://learn.chatgpt.com/docs/build-plugins).
	- ## Steps
		- ### 1. Create the workflow in ChatGPT
			- In Chat or Work, select Plugin Creator from the `@` menu. Describe the task, inputs, output, and how missing information should be handled. Attach a representative example.
			- Example brief:
				- > Create a plugin called Team Design Review. Given a design document and our review checklist, draft a review containing the problem, proposed behavior, unresolved decisions, and questions for the author. Cite supporting sections. Mark missing information explicitly. Use the attached example to demonstrate the output.
			- Review the generated instructions and supporting files. If the workflow needs an existing app, name the app and the information or actions it should provide.
		- ### 2. Test and share the ChatGPT version
			- Start a new chat, select the plugin with `@`, and run a familiar example plus an example with missing information. Check both Chat and Work if teammates use both.
			- Open the plugin's sharing settings and choose the intended people or groups. Include a sample prompt and the maintainer's name. Recipients install the plugin unless an administrator has installed it for them. Each person also needs access to required apps. [Testing and team sharing](https://learn.chatgpt.com/docs/build-plugins#share-the-plugin-with-your-team).
		- ### 3. Keep a source package when developing in a repo
			- Ask Plugin Creator for the source files as well as the account plugin. For a portable OpenAI package, use this layout:
				- ~~~text
				  team-review/
				    plugin.json
				    skills/team-design-review/SKILL.md
				    skills/team-design-review/references/checklist.md
				  ~~~
			- A minimal root `plugin.json`:
				- ~~~json
				  {
				    "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
				    "name": "team-review",
				    "version": "0.1.0",
				    "description": "Review team design documents against a shared checklist.",
				    "author": { "name": "Example team" }
				  }
				  ~~~
			- Each `SKILL.md` starts with YAML `name` and `description`, followed by the workflow. Keep references and scripts inside the package. Portable packages discover `skills/` at its fixed location. OpenAI presentation settings belong under `extensions.com.openai`; older local clients can use a synchronized `.codex-plugin/plugin.json` compatibility manifest. [Package format](https://developers.openai.com/plugins/build/plugins#plugin-structure).
		- ### 4. Reuse the skills in Claude
			- Add `.claude-plugin/plugin.json` to the same package:
				- ~~~json
				  {
				    "name": "team-review",
				    "version": "0.1.0",
				    "description": "Review team design documents against a shared checklist."
				  }
				  ~~~
			- Keep the `skills/` tree shared and synchronize the identity and version in both manifests. Use provider-neutral instructions for the shared workflow. Convert reusable Claude commands and agent procedures into skills; keep host-specific features separate. [OpenAI's Claude plugin conversion guide](https://developers.openai.com/plugins/guides/submit-claude-plugin).
			- Test the Claude package with `claude --plugin-dir ./team-review`. For automatic Claude project discovery, place the package under `.claude/skills/team-review/` and trust the project. See [[Claude/Code/Plugin/Skills-Directory Plugin]].
			- Test tools independently in both products. MCP provides a shared protocol, while connection settings, authentication, hooks, and app interfaces have host-specific behavior. A shared skill does not make those features interchangeable.
		- ### 5. Expose the package through the repo
			- Store the package at `plugins/team-review/`. Add `.agents/plugins/marketplace.json` at the repo root:
				- ~~~json
				  {
				    "name": "team-plugins",
				    "interface": { "displayName": "Team plugins" },
				    "plugins": [
				      {
				        "name": "team-review",
				        "source": {
				          "source": "local",
				          "path": "./plugins/team-review"
				        },
				        "policy": {
				          "installation": "AVAILABLE",
				          "authentication": "ON_INSTALL"
				        },
				        "category": "Productivity"
				      }
				    ]
				  }
				  ~~~
			- The source path is relative to the repository root. To enable the plugin for a trusted project, add this to the repo's `.codex/config.toml`:
				- ~~~toml
				  [plugins."team-review@team-plugins"]
				  enabled = true
				  ~~~
			- Supported local Codex clients can install or refresh configured plugins during marketplace refresh. Restart the desktop app and verify the plugin in a new chat. Repository discovery, cached installation, and enabled state are separate. [Repo plugin settings](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).
			- For Claude teammates, add a catalog at the repository root's `.claude-plugin/marketplace.json` pointing at the same package:
				- ~~~json
				  {
				    "name": "team-plugins",
				    "owner": { "name": "Example team" },
				    "plugins": [
				      { "name": "team-review", "source": "./plugins/team-review" }
				    ]
				  }
				  ~~~
			- Teammates add the repository through `/plugin marketplace add <owner>/<repo>` in Claude Code, then run `/plugin install team-review@team-plugins`. Replace `<owner>/<repo>` with the team's actual GitHub repository. [Claude marketplace setup](https://code.claude.com/docs/en/plugin-marketplaces).
		- ### 6. Distribute updates to the workspace
			- For GitHub-managed distribution, have a workspace administrator open **Admin → Plugins → Add → Import marketplace**, enter the repository URL, and select a branch or revision. Review the imported plugins and configure installation policy for the intended roles. Use **Sync now** to test an update; new marketplaces also sync daily. [Workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).
			- This workspace import supports Codex catalogs, Claude catalogs, and standalone Claude plugins. Imported packages declaring MCP servers are currently desktop-only, including packages whose server uses HTTPS. For web use, verify the supported app-connection route before sharing.
	- ## Troubleshooting
		- **Source edit does not appear:** edit the marketplace source, bump the package version, reinstall or refresh through the supported client flow, and start a new chat. The runtime uses a cached installation. See [[Codex/Plugin/Q/Does registering a local plugin copy it into a home-directory cache?]].
		- **Fast skill iteration:** expose the shared skill directory through `.agents/skills/` while editing. Codex supports symlinked skill folders. Test the packaged plugin separately before release, and avoid loading both copies during the same verification session. [Local skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
		- **Teammate sees the listing but cannot use it:** check installation, workspace role policy, and the required app connection separately.
