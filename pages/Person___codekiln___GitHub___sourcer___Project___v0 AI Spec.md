# Sourcer (`srcr`)
	- Sourcer (`srcr`) is a local source repository locator and cache for humans and AI agents.
	- Its purpose is to provide a predictable, policy-aware, machine-readable way to locate, clone, cache, and reason about source code repositories on disk.
	- At its core, Sourcer establishes a canonical mapping between repository identities and filesystem paths.
	- A repository such as:
		- ~~~
		  github.com/example/project
		  ~~~
	- maps by default to:
		- ~~~
		  ~/sources/github.com/example/project
		  ~~~
	- This creates a stable shared corpus of trusted repositories that both humans and AI systems can navigate without needing unrestricted access to external hosting providers or arbitrary filesystem locations.
	- ## Motivation
		- ### Make it easy to locate repositories
			- Both human and AI engineers should read the source code they are interfacing with. There should preferably one obvious way to get the source code and read it. This CLI defines and implements a slim convention for this. Skills can make use of this convention independently of whether they are using `srcr`. In addition to knowing where to find existing repositories, it helps to have a universal convention for where each new project should be located.
		- ### Pre-configure AI agents with access to repositories
			- AI agents suffer from prompt injection attacks. Allowing them to view anything on the internet is dangerous, yet to be productive they do need more context about other libraries than just what's in their pre-training. It's not wise to provide whitelisted access to github or other source code repositories for even trusted libraries may have github issues submited by a malicious actor whose comments contain hidden prompt injection attacks. `srcr` specifies a way that AI agents can be configured with access to source code without requiring access to the larger public internet. As long as the repositories exist on disk, they can use the source code. Instead of granting agents unrestricted access to all repositories on the internet or the entire local filesystem, Sourcer creates an explicit repository trust boundary. When working with [[DevContainer]]s, this can be done by pre-cloning libraries into the image.
		- ### Declare repositories that are contextually related to a project
			- For engineers onboarding onto a project, whether human or AI, it's helpful to know what other repositories are likely to be needed to work on the current project. To be productive and accurate in their plans, engineers need to assemble the full context in order to understand the current project and its dependencies.
			- [[git submodules]] have a place in software engineering when there's a hard functional dependency between repositories, but they are also rather heavyweight and not everyone understands how to use them without causing problems or confusion.
			- This project aims to present a convention that brings a project's soft links to other repositories to be ready at hand so that things that should likely be consulted and understood are readily available.
		- ### Web documentation is not as convenient as local access
			- Local source code can be searched and referenced in a more multidimensional and efficient way than remote websites.
			- The web documentation for libraries are useful to AI agents, particularly when combined with [[llms.txt]] and published at a particular domain that can be whitelisted in a network block to avoid prompt injection.
			- If documentation is only published in a source code repository, it's difficult to provide that to an AI agent without also exposing it to prompt injection attacks from public comments on the repository.
			- Documentation is a secondary source, though, and is usually slightly out of date relative to the implementation. When conducting research, it's important to go to the primary source, the repository itself.
		- ### In the agentic engineering era, repositories need to become installable context packages
			- Written documents are the new source code. The projects that one can do with AI are bound to the available context. For those who have published context that's rich for AI agents as source code repositories of text files, `srcr` provides a way to bring that context closer to AI agents in a trusted way.
	- ## Design Goals
		- ### Canonical Repository Identity
			- Every repository is identified by a normalized URI-like identity:
				- ~~~
				  <provider>/<owner>/<repository>
				  ~~~
			- Examples:
				- ~~~
				  github.com/example/project
				  gitlab.com/team/api
				  codeberg.org/person/tool
				  ~~~
			- This identity is the primary abstraction.
			- Filesystem layout, clone URLs, caching strategy, and trust policies are all derived from this canonical identity.
		- ### Be a light-weight [[Universal Installer]] or [[Meta Package Manager]] for [[SCM]] tools
			- Tools like [[aqua]] and [[asdf]] provide a centralized, [[Declarative]] ways to express dependencies from multiple [[Package Managers]]. In a similar way, `srcr` provides a centralized way to clone, update or remove repositories from multiple providers, whether that's [[Gitlab]], [[SourceHut]], [[Codeberg]], or [[GitHub]].
			- Like [[mise]], [[npm]] and similar tools, the config file for `srcr` should declare the desired disk state that the CLI executable should ensure. `srcr install` should bring the disk to match that desired state.
		- ### Predictable Local Paths
			- Repositories always resolve to deterministic local filesystem paths.
			- Default layout:
				- ~~~
				  ~/sources/
				  github.com/
				    owner/
				      repository/
				  ~~~
			- Example:
				- ~~~
				  ~/sources/github.com/example/project
				  ~~~
			- The location should never vary unpredictably based on runtime state.
			- Determinism is critical for automation and AI agents.
		- ### Shared Local Source Cache
			- Repositories cloned by one an AI or a human on disk becomes reusable for subsequent tasks.
			- Benefits include:
				- reduced duplicate cloning and fewer total API calls
					- sometimes agents will actually clone APIs to `/tmp` to look inside the source code. This is wasteful for libraries that are heavily used.
				- improved local searchability
					- for example, *being able to ripgrep across an entire org in github*
			- Sourcer is conceptually closer to a shared source corpus than a traditional package manager.
		- ### Explicit access boundary
			- Sourcer is designed around constrained repository access.
			- In the MVP, every identity listed in `[sources]` is **allowed** and **installed by default** when `srcr install` runs (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]]).
			- In Phase 2, optional `[allow]` patterns (including wildcards) can permit download without auto-install; see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Trust]].
		- ### Human and Agent Friendly
			- The command-line interface should work equally well for:
				- humans
				- shell scripts
				- CI systems
				- local automation
				- AI agents
			- Commands should support structured output from the beginning.
			- MVP agents and scripts rely on `srcr install`, `srcr where`, and `srcr status --json` (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]]).
			- Machine-readable interfaces are a first-class design requirement.
		- ### Compatibility with [[DevContainer]]s and related technologies like [[DevContainer/Feature]]s and [[GitHub Codespaces]]
			- DevContainers are typically created in a way that touches a single repository, and in many cases that's likely because people don't understand any way to bring more than one repository into a devcontainer. `srcr` aims to provide a sensible and easy way to do that in devcontainers.
			- In particular,
	- ## Configurable Layout
		- Although Sourcer provides a default layout convention, the storage root should be configurable.
		- Precedence order:
			- command-line flag
			- environment variable
			- configuration file
			- default
		- Example (MVP):
			- ~~~sh
			  srcr install --root /mnt/ssd/sources
			  ~~~
		- Example environment override:
			- ~~~sh
			  export SRCR_ROOT=/mnt/shared/sources
			  ~~~
		- Example configuration:
			- ~~~toml
			  root = "~/sources"
			  ~~~
		- Internally, repository identity should remain stable regardless of physical layout.
	- ## Non-Goals
		- Sourcer is not yet intended to:
			- ### Be Declarative Config That Can Be Imperatively Constructed
				- It would be nice to modify the config file one command at a time. For example, `srcr use <provider>/<owner>/<repo>` could modify the config file and get the repository locally in an idempotent way.
				- This would lend itself to [[DevContainer/Feature]]s because a slim feature description could wrap `srcr use <provider>/<owner>/<repo>` to declare a dependency on a particular repo without interfering with the developer's dotfiles version of the `srcr` config file, and the way `srcr install` reads the modified config could then become cached as a docker layer upon build.
			- replace Git
			- implement a full source control system
			- manage dependency graphs
			- replace package managers
			- perform builds
			- manage deployment pipelines
			- provide repository hosting
		- Its responsibility is repository location, access policy (allow + install), and local source materialization.
	- ## Phase 2
		- Phase 2 extends the MVP with ad-hoc materialization and richer access policy. See [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]] and [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]].
		- **`srcr use <identity>`** — materialize one repository by identity (replaces the defunct `srcr ensure`); may also imperatively update `srcr.toml` when config-mutating mode is enabled (see non-goals above).
		- **`[allow]`** — wildcard patterns that permit download without listing the repo in `[sources]` (no auto-install on `srcr install`).
		- **`install = false` on a `[sources]` entry** — allowed and path-resolvable, but not cloned until `srcr use`.
		- Example (Phase 2 preview):
			- ~~~sh
			  srcr use github.com/example/project --json
			  ~~~
		- Example output:
			- ~~~json
			  {
			    "uri": "github.com/example/project",
			    "path": "/home/user/sources/github.com/example/project",
			    "exists": true,
			    "cloned": false,
			    "allowed": true
			  }
			  ~~~
	- ## Design
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Design/Thinking]] — structured design-thinking workshop (empathy → test).
		- [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Mise]] — speculative mise-inspired repo conventions (Rust layout, CLI modules, tooling).
	- ## Example CLI
		- TBD pending design review — see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]].
	- ## Long-Term Possibilities
		- Potential future directions include:
			- migrate existing local repository locations that are outside of the convention to move them into a location that's matches the convention
			- repository metadata indexing
			- facilitating creation of [[llms.txt]] indexes for repositories and their files, e.g. [[AI Knowledge Gardening]] about source code repositories
			- garbage collection and eviction policies, for example, being able to set a two week expiration for a given repository and have that repository removed in two weeks
			- content-addressed repository snapshots, for example, [[GitHub/Action]] affordances that can publish a [[DevContainer/Feature]] proxy for a repository
		- These are intentionally outside the scope of the initial implementation.
	- ## Philosophy
		- Sourcer treats source repositories as durable local knowledge assets.
		- The system is designed around three assumptions:
			- repository identity should be canonical
			- trusted source code should be locally discoverable
			- AI agents require explicit structural boundaries
		- The result is a shared source repository layer that is understandable to both humans and machines.
	- ## Mise-compatible declaration model
		- Sourcer should deliberately mirror [[mise]] at the level of configuration shape and mental model, while remaining a separate tool with its own domain. Mise declares desired development tools in `[tools]`; Sourcer should declare desired local source repositories in `[sources]`. The basic form should be compact and obvious:
		- Example:
			- ~~~toml
			  [sources]
			  "github.com/example/project" = "main"
			  "github.com/example/library" = "v1.2.3"
			  "codeberg.org/person/tool" = "latest"
			  ~~~
		- In this model, the table key is the canonical source identity and the value is the requested ref. Provider defaults derive clone URLs, default path layout, and common behavior from the identity. For example, `github.com/example/project` resolves by convention to `https://github.com/example/project.git` and materializes by default at `~/sources/github.com/example/project`. This keeps the happy path as terse as mise while preserving Sourcer's core commitment to deterministic repository identity and predictable local paths.
		- The MVP should avoid imperative config mutation commands. Instead of `srcr use` or `srcr unuse`, the first version can be purely declarative: users edit `srcr.toml`, then run `srcr install`, `srcr status`, or `srcr where <source>`. That preserves a clean boundary between desired state and realized disk state, and it makes the project easier to reason about for humans, CI, devcontainers, and AI agents. The CLI shape can still be designed with future symmetry in mind, but the initial product can remain config-first.
		- The simple string form should be equivalent to a richer object form, used only when defaults are insufficient:
		- Example:
			- ~~~toml
			  [sources]
			  "github.com/example/project" = "main"
			  "github.com/example/private-tool" = { ref = "main", clone = "ssh" }
			  "internal.example.com/platform/tool" = { ref = "main", remote = "ssh://git@internal.example.com/platform/tool.git" }
			  ~~~
		- This gives Sourcer a progressive disclosure model: most sources look like mise tools, but unusual sources can specify details without requiring a separate table structure. The valid object keys should be intentionally small for the MVP, perhaps `ref`, `remote`, `clone`, and `path`, with `path` treated as an escape hatch rather than the normal mechanism. Provider defaults should do most of the work.
		- For editor affordances, Sourcer should publish a JSON Schema for `srcr.toml` even though the file is TOML. Many editors and language servers can associate schemas with TOML files through tooling such as Taplo, which supports JSON Schema-based validation and completions for TOML. That means the project can offer a schema URL and document editor setup so users get autocomplete for `[sources]`, object keys, allowed enum values such as `clone = "https" | "ssh"`, and warnings for misspelled options. This is important because the config file is the interface in the MVP.
		- A good MVP command surface would be small and declarative:
		- Example:
			- ~~~sh
			  srcr install
			  srcr status
			  srcr where github.com/example/project
			  srcr list
			  srcr doctor
			  ~~~
		- The symmetry with mise should be treated as a design constraint rather than an implementation dependency. Mise installs tools; Sourcer materializes source repositories. Mise can orchestrate Sourcer through tasks, but Sourcer should not need to be a mise plugin to feel mise-native. A project could simply declare `srcr` under mise's `[tools]`, then define a `sources:install` task that runs `srcr install`. That gives a one-command onboarding path while keeping Sourcer's own source declaration model clear and independent.