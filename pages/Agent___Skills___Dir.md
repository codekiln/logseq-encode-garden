alias:: [[.agents/skills]]

- # [Skill Discovery Recommendations for Agentic Tool Implementors](https://agentskills.io/client-implementation/adding-skills-support#step-1-discover-skills) - `.agents/skills`
	- ## The Agent Skills Specification Recommendation of Where to Scan for Skills
		- > Most locally-running agents scan at least two scopes:
		    **Project-level** (relative to the working directory): Skills specific to a project or repository.**
		    **User-level** (relative to the home directory): Skills available across all projects for a given user.
		- > Within each scope, consider scanning both a **client-specific directory** and the **`.agents/skills/` convention**
		  | Scope | Path | Purpose |
		  | ---- | ---- | ---- |
		  | Project | `<project>/.<your-client>/skills/` | Your client’s native location |
		  | Project | `<project>/.agents/skills/` | Cross-client interoperability |
		  | User | `~/.<your-client>/skills/` | Your client’s native location |
		  | User | `~/.agents/skills/` | Cross-client interoperability |
		- > The `.agents/skills/` paths have emerged as a widely-adopted convention for cross-client skill sharing. While the Agent Skills specification does not mandate where skill directories live (it only defines what goes inside them), scanning `.agents/skills/` means skills installed by other compliant clients are automatically visible to yours, and vice versa.
		- > Some implementations also scan `.claude/skills/` (both project-level and user-level) for pragmatic compatibility, since many existing skills are installed there. Other additional locations include ancestor directories up to the git root (useful for monorepos), [XDG](https://specifications.freedesktop.org/basedir-spec/latest/) config directories, and user-configured paths.
	- ## [[My Notes]]
		- see [[Agent/Skills/Dir/Compatibility]] for notes on compatibility