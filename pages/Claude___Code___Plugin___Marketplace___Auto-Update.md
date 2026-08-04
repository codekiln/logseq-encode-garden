logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[Claude/Code/Plugin/Marketplace]], [[Claude/Desktop/Code]], [[Claude/Code/Plugin]]

- # Claude Code Plugin Marketplace Auto-Update
	- ## Overview
		- The use case: a team publishes a [[Claude/Code/Plugin]] to a **private** [[Claude/Code/Plugin/Marketplace]], and everyone consuming it through the [[Claude/Desktop/Code]] tab (Windows and macOS) should end up on each new version without manual steps.
		- Bottom line (as of [[2026-07-28 Tue]]): the marketplace file itself cannot declare auto-update, and the built-in per-marketplace auto-update is unreliable for third-party marketplaces — it refreshes the catalog but often fails to move installed plugins forward, silently. The dependable path is **version discipline in CI plus a small updater shipped in the marketplace**. On macOS that updater runs as a `SessionStart` hook; on Windows, where plugin hooks silently do nothing before Desktop v1.24012.9, the same script runs instead as a logon [[Claude/Desktop/Scheduled Task]] — a delivery path that does not depend on the app's hook system.
	- ## Three surfaces called "plugin controls"
		- Only some of these exist on the desktop Code tab; match the instruction to the surface.
		- | Surface | What it is | On desktop Code tab? |
		  | --- | --- | --- |
		  | `/plugin ...` slash commands | Interactive plugin manager inside the **terminal** `claude` | No — terminal CLI only |
		  | `claude plugin ...` CLI | The `claude` binary's non-interactive subcommands | Only if the terminal CLI is **separately installed**; shares `~/.claude` |
		  | Desktop plugin browser (GUI) | `+` / Customize → **Plugins**: tabs Discover, Installed, Marketplaces, Errors | Yes — this is the surface |
		- On desktop, users manage plugins through the **GUI**, admins through **managed settings JSON**, and automation through a **hook plus a script**. The desktop app registers marketplaces by hosted URL only, so a private marketplace is distributed via its git repo URL.
	- ## Mental model: an update is two moves
		- Claude Code (the engine under the desktop Code tab) keeps a marketplace in three places.
		- | Layer | Location | What it is |
		  | --- | --- | --- |
		  | **Catalog** | `~/.claude/plugins/marketplaces/<name>/` | A git clone of the marketplace repo. Holds `marketplace.json`. |
		  | **Installed plugin** | `~/.claude/plugins/cache/<name>/<plugin>/<version>/` | A frozen copy of the plugin at one version. |
		  | **Registry** | `~/.claude/plugins/installed_plugins.json` | Points each installed plugin at its active `installPath` and version. |
		- On Windows the base path is `%USERPROFILE%\.claude\plugins`.
		- An update must do both moves: **refresh the catalog** so the new version becomes visible, and **re-install the plugin** into a new `cache/.../<new-version>/` directory with the registry repointed. The common failure is move 1 happening while move 2 does not — the catalog advances and the running plugin stays put.
		- **Version resolution** (first one set wins): `version` in `plugin.json` → `version` in the marketplace entry → the git commit SHA. When the resolved version equals the installed one, the update is skipped. That resolution is the lever an author controls.
		- **Author control:** there is no `autoUpdate` field in the `marketplace.json` schema. The marketplace file cannot enable auto-update for the people who add it — that is an installer-side setting. What the author sets is the version numbers.
	- ## How updates get triggered on desktop
		- | Trigger | How (desktop) | Who |
		  | --- | --- | --- |
		  | Manual catalog refresh | Plugins → **Marketplaces** → the marketplace → **Update** | User (GUI) |
		  | Auto-update toggle | Plugins → **Marketplaces** → the marketplace → **Enable auto-update** (also in Desktop settings as of v1.24012.0, 2026-07-21) | User (GUI) |
		  | Policy auto-update | `"autoUpdate": true` per `extraKnownMarketplaces` entry in managed settings | Admin (JSON) |
		  | Forced update | A `SessionStart` hook shipped in the marketplace | Automation |
		- Third-party and local marketplaces do not auto-update by default; only official Anthropic ones do. To apply an update: the GUI **Update** button, a policy refresh, or a shipped hook. Changes reach a running session on its next launch.
	- ## Why built-in auto-update isn't enough
		- The toggle and the managed-settings flag both exist and are documented, but for third-party marketplaces the re-install move breaks in several overlapping ways. All of the following were open as of [[2026-07-28 Tue]]; the July Claude Code releases (v2.1.207–v2.1.212) fixed other plugin bugs but not these.
			- Catalog is fetched but never pulled, so the working tree never advances and the version bump is never seen locally. [#49410](https://github.com/anthropics/claude-code/issues/49410)
			- GitHub-sourced marketplaces are never `git pull`-ed, so upstream changes are never picked up. [#44276](https://github.com/anthropics/claude-code/issues/44276)
			- Third-party marketplaces are not pulled on session start the way official ones are. [#26744](https://github.com/anthropics/claude-code/issues/26744)
			- `autoUpdate` promotes the runtime version but does not rewrite `installed_plugins.json`, so bundled hooks stay pinned to the old path; it also runs before `SessionStart`. [#52218](https://github.com/anthropics/claude-code/issues/52218)
			- With `autoUpdate: true` the catalog advances but installed plugins never move, with no error. [#61854](https://github.com/anthropics/claude-code/issues/61854)
			- The frozen cache is read instead of the updated marketplace folder. [#17361](https://github.com/anthropics/claude-code/issues/17361)
		- Desktop-specific gaps:
			- The desktop app cannot register a local directory as a marketplace, so a hosted URL is required. [#52147](https://github.com/anthropics/claude-code/issues/52147)
			- Plugin hooks silently do nothing on Windows before Desktop **v1.24012.9**, which fixes it (per the [Cowork/Desktop changelog](https://claude.com/docs/cowork/changelog)). On an older Windows build the `SessionStart` updater does not run; macOS is unaffected.
		- The declare-it-in-config capability is filed but unshipped: [#10265](https://github.com/anthropics/claude-code/issues/10265) (auto-update flag in the definition file) and [#51350](https://github.com/anthropics/claude-code/issues/51350) (enable via settings.json).
		- Turning the toggle or policy on is worthwhile as a backstop, but on its own it does not meet the requirement today.
	- ## Recommended architecture
		- ### Layer 1 — Version discipline
			- Set an explicit `version` in each plugin's `plugin.json` and bump it (semver) on every release. A commit without a version bump delivers nothing to existing installs.
			- Automate the bump in CI (conventional-commits → a release bot that bumps `plugin.json`, syncs `marketplace.json`, and tags a release) so there is no manual step.
			- Trade-off: omitting `version` and falling back to the commit SHA makes every commit an update, which suits fast iteration but interacts badly with the fetch-not-pull bug and makes the deployed version hard to read at a glance. For a team marketplace, explicit semver is the safer default.
		- ### Layer 2 — Turn on the intended path (backstop)
			- Per user (GUI): Plugins → Marketplaces → the marketplace → **Enable auto-update**.
			- Fleet (managed settings, Team/Enterprise): the block below also removes the per-user add-marketplace step. The `managed-settings.json` location is OS-specific — see the [settings reference](https://code.claude.com/docs/en/settings).
			- ~~~json
			  {
			    "extraKnownMarketplaces": {
			      "your-marketplace": {
			        "source": { "source": "github", "repo": "your-org/your-marketplace" },
			        "autoUpdate": true
			      }
			    },
			    "enabledPlugins": {
			      "updater@your-marketplace": true
			    }
			  }
			  ~~~
		- ### Layer 3 — A shipped updater (the guarantee)
			- One small script does the pull-and-reinstall the background updater skips, with two delivery paths for the same script. Requirements: `git` and `node` on `PATH`.
			- | OS | Delivery | Why |
			  | --- | --- | --- |
			  | macOS | `SessionStart` hook shipped in an `updater` plugin | Hooks fire on macOS today |
			  | Windows | Logon Scheduled Task running the script from a fixed path | Plugin hooks silently do nothing on Windows before Desktop v1.24012.9 |
			- What the script does, in order:
				- Exits quietly if the marketplace clone has no `.git` (nothing to do).
				- Advances the catalog working tree with `git fetch` then `git reset --hard origin/<branch>`, working around the fetch-not-pull bug. It uses the user's own git credentials, so private-repo auth behaves exactly like their shell.
				- Reads `installed_plugins.json` (the registry) and the catalog's `marketplace.json`, and for each installed plugin from this marketplace compares the installed version to the catalog version.
				- When they differ, copies the fresh plugin files into a new `cache/<marketplace>/<plugin>/<version>/` directory and repoints the registry entry's `version` and `installPath` at it.
				- Writes the registry back only if something changed, and swallows all errors so it never blocks the session.
			- Coverage: this handles **relative-source** plugins (plugins living inside the marketplace repo), the common team layout. For `github`/`npm` plugin sources the files are not in the clone; cover those by installing the terminal CLI as a prerequisite and driving `claude plugin marketplace update` followed by `claude plugin update <plugin>` instead of the copy step.
			- macOS delivery — ship the script as a plugin hook. Package it in a bootstrap `updater` plugin in the same marketplace; installing the plugin activates the hook.
				- ~~~json
				  {
				    "name": "updater",
				    "version": "1.0.0",
				    "description": "Keeps marketplace plugins current on session start"
				  }
				  ~~~
				- ~~~json
				  {
				    "hooks": {
				      "SessionStart": [
				        {
				          "hooks": [
				            {
				              "type": "command",
				              "command": "node",
				              "args": ["${CLAUDE_PLUGIN_ROOT}/scripts/sync.mjs"]
				            }
				          ]
				        }
				      ]
				    }
				  }
				  ~~~
				- Validate with `claude plugin validate ./updater` before publishing. On Windows this hook installs cleanly but does not fire until Desktop v1.24012.9, so Windows uses the Scheduled Task meanwhile.
			- Windows delivery — logon Scheduled Task. Place the script at a fixed path (the plugin cache path changes each version, so a task must not point there) and register a per-user task that runs it at logon; IT can push both steps fleet-wide via MDM. The task updates the on-disk marketplace and registry, and the desktop app picks up the change on its next Code session launch. macOS needs no task; for the same interval behaviour on macOS, run the script from a LaunchAgent or cron.
	- ## Caveats
		- **Windows hooks.** The `SessionStart` hook silently does nothing on Windows before Desktop v1.24012.9 ([changelog](https://claude.com/docs/cowork/changelog)), so Windows uses the Scheduled Task and macOS uses the hook.
		- **One-session lag.** On macOS, version resolution runs before `SessionStart` hooks ([#52218](https://github.com/anthropics/claude-code/issues/52218)); the hook writes the fresh version to disk, and a session that already loaded the old one picks it up on next launch. The Windows Scheduled Task runs at logon, before any session, so it avoids this.
		- **MCP-bearing plugins.** Close and reopen the Code session to load the new version. Skills, commands, and agents are lighter but safest to pick up on relaunch.
		- **Private-repo auth.** The updater runs `git` with the user's normal credentials, so private pulls behave like their shell (`gh auth login`, or an SSH agent). If also relying on the background updater, set `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1` and configure a git credential helper.
		- **Distribution.** The desktop app registers marketplaces by hosted URL, so use the private git repo URL ([#52147](https://github.com/anthropics/claude-code/issues/52147)).
		- **Global updater switch.** If `DISABLE_AUTOUPDATER` is set anywhere, add `FORCE_AUTOUPDATE_PLUGINS=1` to keep plugin updates.
		- **Internal files.** The script writes `installed_plugins.json` and the cache, which are undocumented internals and can change between releases — keep it in the review loop.
	- ## Verifying a user is current
		- GUI: Plugins → **Installed** shows each plugin's version and **Marketplaces** shows the catalog. If Installed lags the catalog, hit **Update** and relaunch the session.
		- Scriptable: read `installed_plugins.json` and the catalog's `marketplace.json`, and for each plugin from the marketplace print its installed version beside its catalog version. Matching pairs are current; a mismatch means the re-install move did not land.
	- ## Review trigger
		- Re-verify against the current Claude Code and Desktop release before relying on this. Two milestones change the design:
			- **Fleet reaches Desktop v1.24012.9+** → plugin hooks fire on Windows, so Windows can drop the Scheduled Task and use the plugin hook like macOS.
			- **`autoUpdate: true` propagates to `installed_plugins.json`** → the shipped updater becomes optional and its registry writes can be retired entirely.
	- ## References
		- [Install plugins (Cowork/desktop GUI)](https://claude.com/docs/cowork/guide/plugins)
		- [Plugins overview](https://claude.com/docs/plugins/overview)
		- [Plugins reference — schema, versioning, cache](https://code.claude.com/docs/en/plugins-reference)
		- [Create & distribute a marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
		- [Discover & install — auto-update toggle, env vars](https://code.claude.com/docs/en/discover-plugins)
		- [Settings reference — managed settings paths](https://code.claude.com/docs/en/settings)
		- [Cowork/Desktop changelog](https://claude.com/docs/cowork/changelog)
