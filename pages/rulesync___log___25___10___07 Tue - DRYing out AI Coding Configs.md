# [[2025-10-07 Tue]]
	- ## How to [[DRY]] out [[AI/Coding/Config]]s
		- ### Thinking About [[rulesync/GitHub/Issue/25/09/Brainstorm needed - how to share some rules across repos, but not all i329]]
			- Rules, commands, subagents and other AI coding configurations need to be defined at different scopes. In general, there's a need for `public`, `team` and `private` scopes. In addition, within each of these, sub-scopes would be necessary for individual projects and specific technologies.
				- Here are some examples that illustrate why three high-level scopes—`public`, `team`, `private`—and their sub-scopes (per-technology and per-project) are all useful. They are grouped by scope, then shown a few sub-scope situations for each.
				- ### 1. PUBLIC SCOPE (usable by anyone, even outside the company)
					- "General Secure-Coding Rules"
						- Lint-style guardrails: *"Always sanitize user input before DB insertion."*
						- Works for every repo, language, and organisation; no sensitive data.
					- "Inclusive Language Checker" command
						- Shell-style command a developer can call: `check-inclusive-language`.
						- Prompts the AI to flag non-inclusive terms in docs or code comments.
					- "Open-Source License Explainer" subagent
						- User can ask: *"Is GPL-3 compatible with MIT for this file?"*
						- Perfectly safe to share with the broader open-source community.
					- Public • Technology sub-scope
						- A public FastAPI rule pack: *"When creating FastAPI endpoints, always return Pydantic models, never raw dicts."*
					- Public • Project sub-scope
						- Open-source SDK project: *"SDK must not depend on non-standard library modules."*
				- ### 2. TEAM SCOPE (shared only by the internal engineering org)
					- "Company Commit-Message Convention" rule
						- *"Always start commit messages with `[JIRA-ticket]`."*
					- "Standard Staging-Env Spin-Up" command
						- Command: `spin-up-staging`.
						- AI agent runs Terraform in a specific AWS account that only the team uses.
					- "Logging Style Enforcer" subagent
						- Looks at any log lines and rewrites them to match the org's `jsonlog` schema.
					- Team • Technology sub-scope
						- TypeScript CLI rule set: *"Disallow `console.log`; use our `logger.ts` wrapper."*
					- Team • Project sub-scope
						- "Mobile-App" subagent that knows the internal feature flag system used only by the mobile team.
				- ### 3. PRIVATE SCOPE (individual or very restricted use)
					- "Experimental Algorithm" rule
						- Describes proprietary heuristics for an upcoming product feature.
						- Only the inventor keeps this in her personal repo.
					- "Internal Metrics Dashboard" command
						- Command: `query-sales-funnel`. Hits an internal Grafana API with a secret token.
					- "Contract-Drafting" subagent
						- Personal-use GPT-based helper that loads the user's saved prompts and legal templates.
					- Private • Technology sub-scope
						- GPU-cluster optimisation rules the research team is experimenting with, hidden from everyone else.
					- Private • Project sub-scope
						- One-off migration script commands for a stealth project codenamed "Project Quartz".
				- ### Why the distinctions matter
					- Public vs. Team vs. Private keeps confidential knowledge isolated.
					- Technology sub-scopes avoid polluting every repo with rules that only apply to, say, FastAPI or React.
					- Project sub-scopes stop cross-talk (the "mobile" rules don't appear in the "data-pipeline" repo).
			- Let's elaborate a bit on specific recommendations for how teams and developers could use `rulesync` in a way that better honors the [[Software/Engineering/Principle/DRY]] (Don't Repeat Yourself).
				- ### [[Markdown/Frontmatter/Yaml]] `remote` Config Key
					- In the `.rulesync/{commands,rules,subagents,...}/*.md`'s yaml frontmatter, you could support a yaml key like `remote` which could have a pointer to where the command/rule/subagent definition was located:
						- Places with a risk of prompt injection
							- a webpage on the internet
							- a file in another github (or gitlab, or any SCM) repo
						- Places with mitigated risks of prompt injection
							- a local file outside of the repository
							- a pointer to a file within a
					- Then upon `rulesync generate`, it would pull in the rule file into the `targets`.
					- As indicated above, there are issues. Introducing a `remote` key may encourage less experienced engineers to open up their system to prompt injection.
				- ### Rulesync `include` Config Keys
					- `rulesync.jsonc` could support a config like the following
					- #### Proposed extension: rulesync.jsonc → "include" array
						- Top-level schema change:
							- ~~~
							  {
							  ...
							  "include": [<IncludeObject>, <IncludeObject>, ...]
							  }
							  ~~~
						- If `include` is absent or empty, current behaviour is unchanged.
						- Entries are evaluated **in array order**; each may add, merge or override files that ultimately flow into the local `.rulesync` workspace.
					- #### IncludeObject specification
						- ##### Required
							- `repo` (`string`): URI, URL, or relative path that resolves to a Git repository containing a `.rulesync` folder.
						- ##### Optional
							- `ref` (`string`): Git reference (commit SHA, tag, or branch). Default = repository default branch.
							- `subDir` (`string`): Path inside the repo where the root `.rulesync` directory lives if it is **not** at repo root.
							- `features` (`array<string>` | `"*"`): Subset of tool-agnostic "features" to import: `"rules"`, `"commands"`, `"ignore"`, `"mcp"`, `"subagents"`. Default = `"*"` (all recognised features).
							- `patterns` (`array<string>` | `Record<Feature,array<string>>`): Glob patterns (minimatch style) applied **after** `features` filtering. Shorthand array applies to every selected feature; map form lets you specify per-feature patterns.
								- Example:
									- ~~~
									  "patterns": {
									    "rules": ["**/fastapi/**", "!**/experimental/**"],
									    "commands": ["deploy-prod.md"]
									  }
									  ~~~
							- `select` (`Record<Feature,array<string>>`): Explicit file list (relative to the feature directory) that must be present. If `select` is provided for a feature, it overrides `patterns` for that feature.
							- `exclude` (`array<string>`): Additional glob exclusions applied last, across all chosen features.
							- `mode` (`"merge"` | `"override"`): merge – included files are added only when **no** equally-named file exists locally. override – included files replace conflicting local files. Default = "merge".
							- `rename` (`Record<string,string>`): Mapping `sourcePath → targetPath` (paths relative to their feature roots) for files that need to land under a different name locally.
							- `transform` (`string`): Command (executed with the file streamed to STDIN, transformed content from STDOUT) that post-processes each included file. Optional ‑ for advanced use only.
					- #### Resolution rules & precedence
						- 1. Iterate through `include` array in order.
						- 2. For each IncludeObject:
							- a. Clone or fetch `repo` at `ref`.
							- b. Identify the `.rulesync` directory (`/` by default or `subDir`).
							- c. Filter by `features`, then `patterns`, then `select`, then `exclude`.
							- d. For each remaining file, determine destination path (after optional `rename`).
							- e. Apply `transform` if present.
							- f. Place file into the local staging area, respecting `mode`.
						- 3. After all includes are processed, run the normal local generation / export logic.
					- #### Illustrative examples
						- ##### Example 1 – Pull in a public rule pack verbatim
							- ~~~
							  "include": [
							  {
							    "repo": "https://github.com/public-ai/rules-general.git",
							    "ref": "v1.0.3",
							    "mode": "merge"
							  }
							  ]
							  ~~~
						- ##### Example 2 – Cherry-pick FastAPI rules and two deployment commands from an internal repo
							- ~~~
							  "include": [
							  {
							    "repo": "git@github.com:mycorp/fastapi-rules.git",
							    "features": ["rules", "commands"],
							    "patterns": {
							      "rules": ["fastapi/**"],
							      "commands": ["deploy-staging.md", "deploy-prod.md"]
							    },
							    "exclude": ["**/legacy/**"],
							    "mode": "override"
							  }
							  ]
							  ~~~
						- ##### Example 3 – Rename and transform a private subagent definition
							- ~~~
							  "include": [
							  {
							    "repo": "../personal-ai-snippets",
							    "features": ["subagents"],
							    "select": { "subagents": ["draft-legalese.md"] },
							    "rename": { "draft-legalese.md": "private/draft-legalese.md" },
							    "transform": "sed 's/ACME_CORP/FOOBAR_INC/g'"
							  }
							  ]
							  ~~~
					- #### Error handling
						- Missing repo, unreachable ref, or absent `.rulesync` directory → hard error; generation stops.
						- `select` item not found → hard error.
						- Overwrite conflicts when `mode == "merge"` → warning; local file is kept.
						- `transform` exit code ≠ 0 → hard error for that file.
					- #### Compatibility note
						- The new `include` key is entirely additive. Existing projects without it run exactly as before.