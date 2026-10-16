logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[Codex/Plugin]], [[Claude/Code/Plugin/Skills-Directory Plugin]]
- # How To Develop and Share a Team Plugin for ChatGPT and Claude
	- ## Overview
		- Develop and test the plugin against editable files on the author's computer before publishing or sharing a release. This local edit-and-test cycle is an expected authoring step in both Claude and ChatGPT/Codex.
		- Follow this order: create the source package, load the working files, change a file and verify the changed behavior, test the installed package, then publish or share it. Keep the reusable skills in one repository when supporting both hosts.
		- Claude Code can load the complete plugin directory directly. Local Codex can load skill directories directly; its marketplace workflow tests the complete plugin through a cached installation. A private local cache is an installation mechanism and does not require publishing to an account, workspace, or public directory.
		- Product behavior and documentation checked October 16, 2026.
	- ## Prerequisites
		- A local checkout accessible to the test host. Use Claude Code for Claude directory loading and a supported local Codex session for OpenAI skill discovery. Account plugins in a web chat do not provide access to the checkout's working files.
		- A representative input, an example of the desired output, and the reference material the workflow needs.
		- Plugin Creator and permission to use plugins in the intended ChatGPT workspace. Sharing and publishing to the workspace directory have separate permissions. [ChatGPT plugin authoring](https://learn.chatgpt.com/docs/build-plugins).
	- ## Steps
		- ### 1. Describe the workflow and request local source files
			- In Chat or Work, select Plugin Creator from the `@` menu. Describe the task, inputs, output, and how missing information should be handled. Attach a representative example. Ask for a local source package to edit and test before saving or publishing an account plugin.
			- Example brief:
				- > Build a local source package called Team Design Review in plugins/team-review so I can edit and test its files before publishing. Given a design document and our review checklist, draft a review containing the problem, proposed behavior, unresolved decisions, and questions for the author. Cite supporting sections. Mark missing information explicitly. Use the attached example to demonstrate the output. Stop after local testing; account upload and sharing come later.
			- Review the generated instructions and supporting files. If the workflow needs an existing app, name the app and the information or actions it should provide.
		- ### 2. Define repeatable local checks
			- Keep a familiar input and an input with missing information beside the source package, with the expected output for each. Reuse these checks after every change to a skill, reference, script, or tool.
			- During the direct-source tests below, edit a working file, reload the relevant component, and rerun a check that exercises that edit. Verify the source path as well as the result. Complete this cycle in each target host before testing a release installation.
		- ### 3. Keep a source package when developing in a repo
			- Save the generated source files at `plugins/team-review/` in the repository and edit that directory throughout development. If the creation chat has no filesystem access, download its source package into the checkout before continuing. An uploaded account plugin does not stay linked to the checkout.
			- For a portable OpenAI package, use this layout:
				- ~~~text
				  plugins/team-review/
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
		- ### 4. Test the editable plugin directory in Claude Code
			- Add `.claude-plugin/plugin.json` to the same package:
				- ~~~json
				  {
				    "name": "team-review",
				    "version": "0.1.0",
				    "description": "Review team design documents against a shared checklist."
				  }
				  ~~~
			- Keep the `skills/` tree shared and synchronize the identity and version in both manifests. Use provider-neutral instructions for the shared workflow. Convert reusable Claude commands and agent procedures into skills; keep host-specific features separate. [OpenAI's Claude plugin conversion guide](https://developers.openai.com/plugins/guides/submit-claude-plugin).
			- From the repo root, load the source directory for a Claude Code development session:
				- ~~~bash
				  claude --plugin-dir ./plugins/team-review
				  ~~~
			- This loads the directory as `team-review@inline`. Run `/reload-plugins` after edits, then invoke `/team-review:team-design-review`. Pass the directory itself to use the working files; a ZIP is a packaged build. [Claude development without a marketplace](https://code.claude.com/docs/en/plugins/create#develop-without-a-marketplace).
			- If automatic discovery is preferable, keep the source package itself at `.claude/skills/team-review/`, including `.claude-plugin/plugin.json` and its `skills/` directory. Launch Claude Code from the repo root and accept project trust. It loads as `team-review@skills-dir`; `/reload-plugins` reloads changes. Update the Codex symlink and marketplace paths below to this source location. Keep a single editable package, rather than copying it between both locations. See [[Claude/Code/Plugin/Skills-Directory Plugin]] and the [Claude loading reference](https://code.claude.com/docs/en/plugins/loading#plugins-shared-through-a-repository).
			- Test tools independently in both products. MCP provides a shared protocol, while connection settings, authentication, hooks, and app interfaces have host-specific behavior. A shared skill does not make those features interchangeable.
		- ### 5. Test the editable skill directory in local Codex
			- Expose each shared skill directory under the repo's `.agents/skills/`. Codex follows symlinked skill folders, so edits to the package's `SKILL.md`, references, and scripts remain edits to the files used by the discovered skill. This loads a plain skill; it does not activate the package's MCP configuration or hooks. [Codex local skill discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
			- From the repo root, create this link if the destination does not already exist:
				- ~~~bash
				  mkdir -p .agents/skills
				  ln -s ../../plugins/team-review/skills/team-design-review .agents/skills/team-design-review
				  realpath .agents/skills/team-design-review/SKILL.md
				  ~~~
			- The resolved path should end in `plugins/team-review/skills/team-design-review/SKILL.md` inside the current checkout. Relative symlink targets are resolved from `.agents/skills/`. If the package lives under `.claude/skills/team-review/`, use `../../.claude/skills/team-review/skills/team-design-review` as the target instead. Inspect any existing destination before changing it.
			- Disable the installed `team-review@team-plugins` plugin while testing the direct skill. In a trusted repo's `.codex/config.toml`, use:
				- ~~~toml
				  [plugins."team-review@team-plugins"]
				  enabled = false
				  ~~~
			- Also deselect account or workspace copies for the test chat where permitted. Repo configuration controls local-marketplace entries; it does not override workspace-managed installation state. Start a fresh local Codex chat in the checkout and explicitly select `team-design-review` from the skill picker. Restart Codex if discovery has not caught up.
			- Verify both the selected source path and behavior: temporarily add an instruction to the source skill to include `LOCAL-DEVELOPMENT-CHECK` in its review, run a representative review, and inspect which `SKILL.md` was loaded. The resolved file should be in the checkout, outside `~/.codex/plugins/cache/`. Remove the test instruction after verification. Reading a file on demand alone does not demonstrate that the host selected it as the skill.
			- In Claude, inspect the loaded plugin's origin in `/plugin` or `claude --plugin-dir ./plugins/team-review plugin list`, reload, and run the same temporary behavior check. Expect `@inline` for the directory flag or `@skills-dir` for automatic discovery. [Claude component verification](https://code.claude.com/docs/en/plugins/create#verify-your-plugin).
			- For MCP tools and hooks, verify their process and script paths separately. Rebuild compiled helpers and restart the relevant process after edits. A live `SKILL.md` does not establish that a running server has reloaded its code. Direct Codex skill discovery and these filesystem checks apply to supported local sessions; a web or cloud account installation does not read the checkout automatically.
		- ### 6. Test the packaged plugin through a local marketplace
			- After the direct-source checks pass, test installation and the full bundle through a private local marketplace. This catches packaging, component discovery, and startup problems before publishing. In Codex, this full-plugin test uses a cache even though the source files and catalog are local; direct skill loading above remains the path for editing skills in place.
			- A **local-marketplace plugin** is a plugin listed in a catalog read by a local client. The catalog can be one JSON file containing one entry. It makes the package discoverable; installation supplies the runtime copy. Add `.agents/plugins/marketplace.json` at the repo root:
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
			- Use `enabled = true` for the packaged-plugin test after disabling direct skill discovery for that test. Supported local Codex clients can install or refresh configured plugins during marketplace refresh. Restart the desktop app and verify the plugin in a new chat. [Repo plugin settings](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).
			- Local marketplace installation loads `~/.codex/plugins/cache/team-plugins/team-review/local/`. A local `source.path` and `enabled = true` do not turn that copy into a live link. Edit the source package, refresh or reinstall it, and test the installed result separately. See [[Codex/Plugin/Q/Does registering a local plugin copy it into a home-directory cache?]] and [How local marketplaces work](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work).
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
		- ### 7. Publish or share the tested release
			- Once local source tests and installed-package tests pass, save or update the account plugin from the tested source. Start a new chat, select it with `@`, and rerun the representative inputs. Check both Chat and Work if teammates use both.
			- Open the plugin's sharing settings and choose the intended people or groups. Include a sample prompt and the maintainer's name. Recipients install the plugin unless an administrator has installed it for them. Each person also needs access to required apps. [Testing and team sharing](https://learn.chatgpt.com/docs/build-plugins#share-the-plugin-with-your-team).
			- For GitHub-managed distribution, have a workspace administrator open **Admin → Plugins → Add → Import marketplace**, enter the repository URL, and select a branch or revision. Review the imported plugins and configure installation policy for the intended roles. Use **Sync now** to test an update; new marketplaces also sync daily. [Workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).
			- This workspace import supports Codex catalogs, Claude catalogs, and standalone Claude plugins. Imported packages declaring MCP servers are currently desktop-only, including packages whose server uses HTTPS. For web use, verify the supported app-connection route before sharing.
	- ## Troubleshooting
		- **Source edit does not appear:** edit the marketplace source, bump the package version, reinstall or refresh through the supported client flow, and start a new chat. The runtime uses a cached installation. See [[Codex/Plugin/Q/Does registering a local plugin copy it into a home-directory cache?]].
		- **Duplicate skill entries:** disable the installed copy while testing the source skill. For a packaged release test, temporarily move only the discovery symlink outside `.agents/skills/`, leaving its source directory in place, then start a fresh chat. Restore the link to resume local development.
		- **Teammate sees the listing but cannot use it:** check installation, workspace role policy, and the required app connection separately.
