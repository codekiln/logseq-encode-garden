alias:: [[Anthropic/App/Claude Code/Settings]], [[Claude/Code/Config]]
title:: Claude/Code/Settings
- # [Claude Code settings](https://code.claude.com/docs/en/settings)
	- > Configure Claude Code with hierarchical settings files, per-scope overrides, and environment variables.
	- `settings.json` is the file-based mechanism for configuring Claude Code. `/config` presents the same options as a tabbed interface, and `/config key=value` changes a single option without opening it. `/status` lists which settings sources actually loaded; `/doctor` reports entries that were rejected.
	- Keys below reflect Claude Code 2.1.233.
	- ## Configuration scopes
		- Settings come from four scopes. Each is a known path — Claude Code does not walk up the directory tree hunting for a `settings.json`.
		- **Managed** — deployed by IT as a file in a system location, through MDM or OS policy, or delivered from the server at sign-in. Applies to everyone in the organization or on the machine, and cannot be overridden from below.
		- **User** — `~/.claude/settings.json`, which resolves to `%USERPROFILE%\.claude` on Windows. Applies to every project on the machine and is not shared.
		- **Project** — `.claude/settings.json`, checked into source control and shared with everyone working in the repository.
		- **Local** — `.claude/settings.local.json`, personal to one person in one repository and kept out of git. Claude Code adds `**/.claude/settings.local.json` to the global excludes file — `core.excludesFile` if set, otherwise `$XDG_CONFIG_HOME/git/ignore` or `~/.config/git/ignore`.
		- Since 2.1.211 the local file lives at the git repository root, resolved through worktrees, so it covers every subdirectory. Older locations are still read. It stays in the starting directory in three cases: outside a git repository, when the repository root is the home directory, and in Agent SDK sessions.
		- Answering a permission prompt with "don't ask again" writes the rule to the local file. Those `allow` rules take effect without workspace trust, because the file is personal — but once the file is committed, workspace trust applies to it again.
		- ### Precedence
			- Highest to lowest: managed, command-line arguments, local, project, user.
			- Most keys are **replaced** by the highest-precedence scope that defines them rather than deep-merged. Permission `allow`, `ask`, and `deny` rules are the exception — they **merge**, so the effective set is the union across scopes and a project `deny` still binds when user settings only add `allow` entries.
			- A handful of other arrays merge and at least one array-valued key deliberately does not. That distinction, with worked examples, is the subject of the override page.
		- ### Managed settings locations
			- macOS: `/Library/Application Support/ClaudeCode/`
			- Linux and WSL: `/etc/claude-code/`
			- Windows: `C:\Program Files\ClaudeCode\`
			- Each directory holds `managed-settings.json` as the base plus optional `managed-settings.d/*.json` drop-in fragments, merged alphabetically on top: scalars override, arrays concatenate and de-duplicate, objects deep-merge. Numeric prefixes such as `10-telemetry.json` and `20-security.json` make the order explicit. Hidden `.*.json` files are ignored.
			- The Windows path `C:\ProgramData\ClaudeCode\managed-settings.json` **is no longer supported as of 2.1.75**. A policy deployed there has stopped taking effect and must move to `C:\Program Files\ClaudeCode\`.
			- Invalid entries in managed settings are stripped individually with a warning rather than discarding the file, so a single typo cannot switch off an organization's policy. Security-enforcing keys fail closed instead — an invalid `allowedMcpServers` enforces an empty allowlist and `allowManagedHooksOnly` is treated as `true` until fixed — while `requiredMinimumVersion` and `requiredMaximumVersion` fail open so startup is never blocked.
		- ### Example
			- ~~~json
			  {
			    "$schema": "https://json.schemastore.org/claude-code-settings.json",
			    "permissions": {
			      "allow": [
			        "Bash(npm run lint)",
			        "Bash(npm run test *)",
			        "Read(~/.zshrc)"
			      ],
			      "deny": [
			        "Bash(curl *)",
			        "Read(./.env)",
			        "Read(./.env.*)",
			        "Read(./secrets/**)"
			      ]
			    },
			    "env": {
			      "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
			      "OTEL_METRICS_EXPORTER": "otlp"
			    }
			  }
			  ~~~
	- ## When edits take effect
		- Most keys hot-reload. `permissions`, `hooks`, and credential helpers such as `apiKeyHelper` apply as soon as the file changes, and a `ConfigChange` hook fires on each detected change.
		- `model` and `outputStyle` are read once at startup. Use `/model` to switch model mid-session; `outputStyle` is part of the system prompt and is rebuilt on `/clear` or on restart.
	- ## Model and effort
		- `model` — override the default model. Takes an alias or a full model ID. Example: `"opus"` or `"claude-opus-5"`.
		- `fallbackModel` — models tried in order when the primary is overloaded or unavailable; `"default"` expands to the default model. Unlike most arrays this one does not merge across scopes — the highest-precedence file supplies the whole chain. Example: `["sonnet", "default"]`.
		- `effortLevel` — persisted reasoning effort on models that support it: `low`, `medium`, `high`, `xhigh`.
		- `alwaysThinkingEnabled` — set `false` to disable thinking. Absent or `true` enables it automatically on supported models.
		- `showThinkingSummaries` — request API-side thinking summaries and show them in the conversation and the transcript view.
		- `fastMode` — enable fast mode, which keeps the same model and speeds up output. `fastModePerSessionOptIn` set `true` stops it persisting between sessions.
		- `advisorModel` — model for the server-side advisor tool. Example: `"opus"`.
		- `agent` — run the main thread as a named agent, applying that agent's system prompt, tool restrictions, and model. Example: `"code-reviewer"`.
		- `switchModelsOnFlag` — when a message is flagged, switch to another model rather than pausing the session.
	- ## Permissions
		- `allow` — permission rules granting tool use without a prompt. Bash rules match by prefix, not regex. Example: `["Bash(git diff:*)", "Read"]`.
		- `ask` — rules that always prompt for confirmation, even when a broader `allow` would cover them. Example: `["Bash(git push:*)"]`.
		- `deny` — rules refusing tool use, also the way to keep sensitive files out of reach. Bash patterns are prefix matches and can be worked around, so do not lean on them as a security boundary. Example: `["WebFetch", "Bash(curl:*)", "Read(./.env)"]`.
		- `defaultMode` — permission mode a session opens in: `default` (`manual` is accepted as an alias), `plan`, `acceptEdits`, `auto`, `dontAsk`, or `bypassPermissions`.
		- `additionalDirectories` — directories outside the working tree that tools may reach. Example: `["../docs/"]`.
		- `disableBypassPermissionsMode` — set to `"disable"` to stop `bypassPermissions` mode being activated at all.
		- `disableAutoMode` — set to `"disable"` to stop auto mode being used. Also accepted as a top-level key.
		- Rules name tools, so the tool names and the per-tool rule syntax are what to look up when writing them — see [Identity and access management](https://code.claude.com/docs/en/iam).
		- ### Auto mode
			- `useAutoModeDuringPlan` — whether plan mode takes on auto mode semantics where auto mode is available. Default `true`.
			- `autoMode` — customize the auto mode classifier through `allow`, `soft_deny`, `hard_deny`, and `environment` arrays. Include the literal `"$defaults"` to inherit the built-in rules at that position. `classifyAllShell` set `true` suspends shell allow rules so every command is classified. Example: `{"soft_deny": ["$defaults", "Never run terraform apply"]}`.
		- ### Excluding sensitive files
			- `permissions.deny` is how files carrying API keys, secrets, and environment values are kept out of Claude Code's view. Matching files become invisible rather than merely unread.
			- ~~~json
			  {
			    "permissions": {
			      "deny": [
			        "Read(./.env)",
			        "Read(./.env.*)",
			        "Read(./secrets/**)",
			        "Read(./config/credentials.json)",
			        "Read(./build)"
			      ]
			    }
			  }
			  ~~~
			- This replaced the earlier `ignorePatterns` configuration.
	- ## Git attribution
		- `attribution` — attribution text for commits and pull requests. `commit` and `pr` each default to the standard Claude Code attribution, and an empty string hides that one. `sessionUrl` set `false` omits the session link from commits and PRs made through the web or Remote Control. Example: `{"commit": "", "pr": ""}`.
		- `includeCoAuthoredBy` — **deprecated**, superseded by `attribution`. Whether to include the `Co-Authored-By: Claude` byline in commits and pull requests. Default `true`.
		- `includeGitInstructions` — set `false` to leave the built-in commit and pull-request workflow instructions out of the system prompt. Default `true`.
	- ## Hooks
		- `hooks` — commands run at points in the session lifecycle, keyed by event name, each entry pairing a `matcher` with a list of hooks to run. Example: `{"PostToolUse": [{"matcher": "Write|Edit", "hooks": [{"type": "command", "command": "prettier --write \"$f\""}]}]}`.
		- Events include `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `UserPromptSubmit`, `SessionStart`, `SessionEnd`, `Stop`, `SubagentStart`, `SubagentStop`, `PreCompact`, `PostCompact`, `ConfigChange`, and `FileChanged`.
		- A hook is one of five types: `command` runs a shell command or, with `args`, an executable with no shell; `prompt` evaluates a condition with a small model; `agent` runs an agentic verifier; `http` POSTs the hook payload to a URL; `mcp_tool` calls a tool on a configured MCP server. `prompt`, `agent`, and `mcp_tool` are limited to the tool events.
		- Per-hook options worth knowing: `if` filters on permission-rule syntax so the hook only spawns for matching calls, `timeout` bounds it, `statusMessage` labels it in the spinner, `once` removes it after one run, and `async` / `asyncRewake` run it without blocking.
		- `disableAllHooks` — disable every hook, and status line execution with them.
		- `disableSkillShellExecution` — replace inline shell execution in skills and custom slash commands with a placeholder rather than running it.
		- Full event payloads, exit-code semantics, and JSON output fields are on the [hooks reference](https://code.claude.com/docs/en/hooks) and in the [hooks guide](https://code.claude.com/docs/en/hooks-guide).
	- ## Status line and output style
		- `statusLine` — a command whose output becomes the status line, receiving session context as JSON on stdin. `padding` insets it, `refreshInterval` re-runs it every N seconds on top of event-driven updates, and `hideVimModeIndicator` suppresses the built-in `-- INSERT --` marker for a script that renders vim mode itself. Example: `{"type": "command", "command": "~/.claude/statusline.sh"}`. See the [status line documentation](https://code.claude.com/docs/en/statusline).
		- `subagentStatusLine` — the same idea per subagent row in the agent panel.
		- `outputStyle` — output style adjusting the system prompt. Read at startup and rebuilt on `/clear`. Example: `"Explanatory"`. See the [output styles documentation](https://code.claude.com/docs/en/output-styles).
		- `prUrlTemplate` — URL template for the pull-request footer badge, with `{host}`, `{owner}`, `{repo}`, `{number}`, and `{url}` placeholders.
	- ## Skills, plugins, and MCP servers
		- `skillOverrides` — per-skill listing control keyed by skill name: `name-only` lists it without its description, `user-invocable-only` hides it from the model but keeps `/name` working, `off` hides it from both. Absent means on.
		- `disableBundledSkills` — remove the skills and workflows that ship with Claude Code. Plugins and project skills are unaffected.
		- `skillListingMaxDescChars` — per-skill description cap in the listing sent to the model. Default `1536`.
		- `skillListingBudgetFraction` — share of the context window reserved for the skill listing. Default `0.01`, meaning one percent.
		- `enabledPlugins` — map of `"plugin-id@marketplace-id"` to a boolean. Resolved per plugin across scopes, so a higher scope only overrides the plugins it names. Example: `{"formatter@anthropic-tools": true}`.
		- `extraKnownMarketplaces` — marketplaces to register for a repository, keyed by name, each with a `source`. Also spelled `additionalMarketplaces`; do not set both in one file.
		- `pluginConfigs` — per-plugin configuration, keyed by plugin ID, holding MCP server user config and non-sensitive option values.
		- `enableAllProjectMcpServers` — approve every MCP server declared in the project's `.mcp.json` automatically.
		- `enabledMcpjsonServers` / `disabledMcpjsonServers` — approve or reject named servers from `.mcp.json`. Example: `["memory", "github"]`.
		- `disableClaudeAiConnectors` — stop claude.ai MCP cloud connectors being fetched and connected. True in any scope wins, so a project can opt out but cannot opt a user back in.
	- ## Sandbox
		- `sandbox.enabled` — run Bash commands inside the sandbox. `failIfUnavailable` turns a sandbox that cannot start into a startup error rather than a warning and an unsandboxed run.
		- `sandbox.autoAllowBashIfSandboxed` — skip the permission prompt for commands that are running sandboxed anyway.
		- `sandbox.allowUnsandboxedCommands` — whether the `dangerouslyDisableSandbox` escape hatch is honoured at all. Default `true`.
		- `sandbox.network.allowedDomains` / `deniedDomains` — egress allowlist and blocklist, both accepting wildcards. Denied domains always win, and merge from every scope.
		- `sandbox.network.strictAllowlist` — deny unlisted hosts outright instead of prompting.
		- `sandbox.filesystem.allowWrite` / `denyWrite` / `denyRead` / `allowRead` — extra paths on top of those implied by `Edit(...)` and `Read(...)` permission rules.
		- `sandbox.excludedCommands` — commands that are never sandboxed.
		- Credential masking, SigV4 re-signing, and TLS termination also live under `sandbox`; see [sandboxing](https://code.claude.com/docs/en/sandboxing).
	- ## Session behaviour
		- `cleanupPeriodDays` — how long session transcripts are retained, counted from last activity. Default `30`, minimum `1`.
		- `autoCompactEnabled` — compact the conversation automatically as context fills. `autoCompactWindow` sets the window between 100,000 and 1,000,000 tokens, and `precomputeCompactionEnabled` builds the summary in the background before it is needed.
		- `fileCheckpointingEnabled` — snapshot files before edits so `/rewind` can restore them.
		- `plansDirectory` — directory for plan files, relative to the project root. Defaults to `~/.claude/plans/`.
		- `respectGitignore` — whether the file picker honours `.gitignore`. Default `true`; `.ignore` files are always honoured.
		- `fileSuggestion` — a command supplying `@`-mention file suggestions in place of the built-in picker.
		- `env` — environment variables applied to every session. Example: `{"FOO": "bar"}`.
		- `defaultShell` — shell for input-box `!` commands: `bash` or `powershell`. Defaults to `bash` everywhere.
		- `respondToBashCommands` — set `false` to add a `!` command's output to context without Claude responding to it.
		- `askUserQuestionTimeout` — idle time before Claude's questions auto-continue with whatever is selected: `60s`, `5m`, `10m`, or `never`. Defaults to `never`.
		- `dialogExpiry` — how long a dialog forwarded to a remote client, or a held cross-session message, waits before resolving to its no-action default. Default `5m`.
		- `showClearContextOnPlanAccept` — offer a "clear context" option in the plan-approval dialog. Default `false`.
		- `autoUpdatesChannel` — release channel for auto-updates: `latest`, `stable`, or `rc`. `minimumVersion` prevents a downgrade when switching to a slower channel.
		- `language` — preferred language for responses and voice dictation. Example: `"japanese"`.
		- `feedbackDrafts` — model-drafted feedback: `notify`, `quiet`, or `off`.
	- ## Memory
		- `autoMemoryEnabled` — whether Claude reads from and writes to the auto-memory directory for this project.
		- `autoMemoryDirectory` — custom auto-memory path, `~/` expanded. Ignored when set in a checked-in `.claude/settings.json`. Defaults to `~/.claude/projects/<sanitized-cwd>/memory/`.
		- `autoDreamEnabled` — background memory consolidation.
		- `claudeMdExcludes` — glob patterns or absolute paths of `CLAUDE.md` files to skip. Applies to user, project, and local memory, never to managed instructions. Arrays merge across scopes. Example: `["**/code/CLAUDE.md"]`.
	- ## Appearance and accessibility
		- `theme` — `auto`, `dark`, `light`, `light-daltonized`, `dark-daltonized`, `light-ansi`, `dark-ansi`, or `custom:<name>`.
		- `editorMode` — key bindings for the prompt input: `normal` or `vim`. `vimInsertModeRemaps` adds two-character INSERT-mode escapes, e.g. `{"jj": "<Esc>"}`.
		- `tui` — renderer: `fullscreen` for the flicker-free alternate screen with virtualized scrollback, `default` for the classic main-screen renderer.
		- `viewMode` — transcript view on startup: `default`, `verbose`, or `focus`. `defaultView` chooses `chat` or full `transcript`.
		- `verbose` — show full tool output rather than truncated summaries.
		- `preferredNotifChannel` — OS notification channel: `auto`, `iterm2`, `iterm2_with_bell`, `terminal_bell`, `kitty`, `ghostty`, or `notifications_disabled`.
		- `syntaxHighlightingDisabled` — turn off diff syntax highlighting.
		- `prefersReducedMotion` — reduce or disable animations.
		- `axScreenReader` — flat screen-reader-friendly output with no decorative borders or animations.
		- `showTurnDuration` / `showMessageTimestamps` / `terminalProgressBarEnabled` — per-turn duration, message arrival times, and OSC 9;4 progress sequences.
		- `terminalTitleFromRename` — whether `/rename` retitles the terminal tab. Default `true`.
		- `spinnerTipsEnabled`, `spinnerVerbs`, `spinnerTipsOverride` — spinner tips and verbs. `spinnerVerbs` takes `{"mode": "append" | "replace", "verbs": [...]}`.
		- `emojiCompletionEnabled` / `promptSuggestionEnabled` — the `:emoji:` typeahead and prompt suggestions.
		- `todoFeatureEnabled` — the todo and task-tracking panel.
		- `autoScrollEnabled` / `wheelScrollAccelerationEnabled` — follow new output to the bottom, and ramp wheel speed during fast scrolls. Both fullscreen only.
	- ## Voice
		- `voice` — hold-to-talk and tap-to-toggle dictation. `enabled` turns it on, `mode` is `hold` (the default) or `tap`, and `autoSubmit` submits the prompt when the key is released in hold mode.
		- `voiceEnabled` — older boolean toggle for the same feature.
	- ## Workflows and agents
		- `enableWorkflows` — whether the Workflows feature is available. `disableWorkflows` turns it off outright.
		- `workflowSizeGuideline` — advisory size for workflows Claude writes: `small` under 5 agents, `medium` under 15, `large` under 50, `unrestricted` for no guideline. A value here wins over the `/config` row, which is hidden while a settings file supplies the key.
		- `workflowKeywordTriggerEnabled` — whether the `ultracode` keyword opts a turn into a workflow. Default `true`.
		- `enableArtifact` — whether the Artifact tool is available. `disableArtifact` turns it off outright.
		- `worktree.symlinkDirectories` — directories symlinked from the main repository into worktrees to avoid duplicating them on disk. Nothing is symlinked by default. Example: `["node_modules"]`.
		- `worktree.sparsePaths` — paths to check out via sparse-checkout, which matters in a large monorepo.
		- `worktree.baseRef` — what new worktrees branch from: `fresh` from the remote default branch, or `head` from the current local HEAD so unpushed work is present.
		- `worktree.bgIsolation` — `worktree` blocks edits in the main checkout until a worktree is entered; `none` lets background sessions edit the working copy directly.
		- `teammateMode` — how spawned teammates run: `auto`, `tmux`, `iterm2`, or `in-process`.
		- `crossSessionInbound` — inbound peer messages from other sessions: `accept` delivers them, `hold` parks them for review, `refuse` opts out. Unset matches on the sending session's permission-mode class.
		- `isolatePeerMachines` — require explicit approval before a peer session on another machine can be reached.
		- `remoteControlAtStartup` — start the Remote Control bridge every session. `autoUploadSessions` mirrors sessions to claude.ai as view-only, and `disableRemoteControl` turns Remote Control off entirely.
		- `disableAgentView` — disable `claude agents`, `--bg`, `/background`, and the on-demand daemon.
		- `daemonColdStart` — with no background service running, `transient` spawns one for the login session and `ask` offers to install it persistently.
		- `inputNeededNotifEnabled` / `agentPushNotifEnabled` — push to mobile when a prompt is waiting, and allow proactive notifications.
	- ## Subagent configuration
		- Subagents are Markdown files with YAML frontmatter defining a specialized assistant's prompt and tool permissions.
		- **User subagents** live in `~/.claude/agents/` and are available in every project.
		- **Project subagents** live in `.claude/agents/` and can be shared with the team.
		- The `agent` setting runs the main thread as one of them. See the [subagents documentation](https://code.claude.com/docs/en/sub-agents).
	- ## Authentication helpers
		- `apiKeyHelper` — script executed in `/bin/sh` producing an auth value, sent as the `X-Api-Key` and `Authorization: Bearer` headers. Example: `/bin/generate_temp_api_key.sh`.
		- `awsAuthRefresh` — script that refreshes AWS authentication by modifying the `.aws` directory. Example: `aws sso login --profile myprofile`.
		- `awsCredentialExport` — script that prints AWS credentials as JSON. Both are described under [advanced credential configuration](https://code.claude.com/docs/en/amazon-bedrock).
		- `gcpAuthRefresh` — command that refreshes GCP authentication. Example: `gcloud auth application-default login`.
		- `otelHeadersHelper` — script that outputs OpenTelemetry headers.
		- `forceLoginMethod` — restrict login to `claudeai` for Claude subscription accounts, `console` for API billing accounts, or `gateway` for the cloud gateway device flow.
		- `forceLoginOrgUUID` — organization UUID, or a list of them, that an account must belong to. Requires `forceLoginMethod`.
	- ## Environment variables
		- Environment variables can be set in the shell or under the `env` key in `settings.json`, which is the way to apply a set of them to every session or roll them out to a team.
		- The full list, including Bedrock and Vertex region overrides, proxy configuration, and telemetry, is on the [environment variables reference](https://code.claude.com/docs/en/env-vars). The ones that come up in ordinary personal use:
		- `ANTHROPIC_API_KEY` — API key sent as the `X-Api-Key` header, mainly for SDK use. For interactive sessions, run `/login`.
		- `ANTHROPIC_AUTH_TOKEN` — value for the `Authorization` header, prefixed with `Bearer `.
		- `ANTHROPIC_MODEL` — model to use, equivalent to the `model` setting.
		- `ANTHROPIC_DEFAULT_OPUS_MODEL` / `ANTHROPIC_DEFAULT_SONNET_MODEL` / `ANTHROPIC_DEFAULT_HAIKU_MODEL` — which concrete model each alias resolves to. See [model configuration](https://code.claude.com/docs/en/model-config).
		- `CLAUDE_CODE_SUBAGENT_MODEL` — model used for subagents.
		- `MAX_THINKING_TOKENS` — thinking budget for the model.
		- `CLAUDE_CODE_MAX_OUTPUT_TOKENS` — maximum output tokens for most requests.
		- `BASH_DEFAULT_TIMEOUT_MS` / `BASH_MAX_TIMEOUT_MS` — default timeout for long-running bash commands, and the ceiling the model is allowed to set.
		- `BASH_MAX_OUTPUT_LENGTH` — characters of bash output before the middle is truncated.
		- `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR` — return to the original working directory after each Bash command.
		- `MCP_TIMEOUT` / `MCP_TOOL_TIMEOUT` — milliseconds allowed for MCP server startup and for MCP tool execution.
		- `MAX_MCP_OUTPUT_TOKENS` — token ceiling on MCP tool responses, with a warning past 10,000. Default 25,000.
		- `USE_BUILTIN_RIPGREP` — set `0` to use the system `rg` instead of the bundled one.
		- `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` — set `1` to stop terminal title updates.
		- `DISABLE_AUTOUPDATER` — set `1` to disable automatic updates. Takes precedence over the auto-update settings.
		- `DISABLE_COST_WARNINGS` — set `1` to silence cost warnings.
		- `DISABLE_TELEMETRY` / `DISABLE_ERROR_REPORTING` / `DISABLE_BUG_COMMAND` / `DISABLE_NON_ESSENTIAL_MODEL_CALLS` — individual opt-outs. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` sets the telemetry, error-reporting, bug-command, and auto-updater ones together.
	- ## Enterprise and policy settings
		- A large part of the schema exists for administrators deploying Claude Code across an organization, and is only honoured from managed settings. It is worth knowing these exist rather than enumerating them:
		- **Lockdown switches** — `allowManagedHooksOnly`, `allowManagedPermissionRulesOnly`, `allowManagedMcpServersOnly`, and `strictPluginOnlyCustomization` restrict hooks, permission rules, MCP servers, and customization surfaces to what managed settings define. `disableSideloadFlags` rejects the CLI flags that would otherwise bypass them.
		- **MCP allow and deny lists** — `allowedMcpServers` and `deniedMcpServers` gate servers by name, command, or URL pattern across every scope, with the denylist winning.
		- **Marketplace policy** — `strictKnownMarketplaces` (also spelled `allowedMarketplaces`), `blockedMarketplaces`, `disableCommandPluginSources`, and `pluginSuggestionMarketplaces` control which plugin sources may be added, checked before anything is downloaded.
		- **Model policy** — `availableModels`, `enforceAvailableModels`, and `modelOverrides` constrain which models users may select and map them onto provider-specific IDs.
		- **Version floor and ceiling** — `requiredMinimumVersion` and `requiredMaximumVersion` refuse to start an out-of-policy build.
		- **Managed instructions** — `claudeMd` injects organization-wide memory; `companyAnnouncements` shows a startup message; `pluginTrustMessage` appends organization context to the plugin trust warning.
		- **Policy helpers** — `policyHelper` and its per-OS variant compute managed settings at startup; `processWrapper` prefixes background processes with a corporate launcher; `forceRemoteSettingsRefresh` blocks startup until managed settings are freshly fetched.
		- **Credential handling** — the `sandbox.credentials` tree masks or denies credential files and environment variables, and re-signs AWS SigV4 requests at the proxy.
		- Deployment guidance is on the [IAM and access control](https://code.claude.com/docs/en/iam) page.
	- ## See also
		- [[Claude/Code/Settings/Override]] — what "override" means per key, and which values merge rather than replace.
		- [Identity and access management](https://code.claude.com/docs/en/iam) — the permission system and tool-specific rule syntax.
		- [Environment variables](https://code.claude.com/docs/en/env-vars) — the full variable reference.
		- [CLI reference](https://code.claude.com/docs/en/cli-reference) — flags and subcommands.
		- [Troubleshooting](https://code.claude.com/docs/en/troubleshooting) — auto-updater and configuration problems.
