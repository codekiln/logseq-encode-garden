# Access boundary
	- Sourcer's access model defines which repository identities may be cloned, updated, or exposed to automation. Everything else is out of scope for the tool and should be unreachable via `srcr` commands.
	- Parent concepts: [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/Config]] (install by default vs allow-only), [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]] (enforcement per command).
	- ## Why an access boundary exists
		- AI agents need **primary sources** — implementation code, not only summaries — to plan and refactor accurately.
		- Unrestricted access creates two classes of risk:
			- **Network prompt injection** — issue comments, PR threads, wiki pages, and even README edits on public hosts can carry instructions aimed at the agent.
			- **Filesystem exfiltration or sprawl** — agents that may read "anywhere" or clone to `/tmp` duplicate corpora, bypass audit, and waste API quota.
		- Whitelisting "all of GitHub" does not solve injection; allowed libraries still have untrusted adjacent surfaces on the hosting site.
		- Local materialization inside a declared corpus lets agents `rg` and read files without live hosting access.
	- ## Threat model (practical)
		- **In scope for Sourcer to mitigate**
			- Arbitrary clone URLs or identities chosen by an agent at runtime.
			- Accidental cloning of unrelated org repos on a shared laptop.
			- Ambiguous paths (`/tmp/foo`, random `~/projects`) that break reproducibility across sessions.
		- **Out of scope (requires other controls)**
			- Malicious code inside an already-allowed repository (supply chain; code review, signing).
			- Compromised git hosting credentials (SSH keys, PATs).
			- Insider edits to allowed repos (normal SCM governance).
			- Agent reading sensitive files inside an allowed clone (scope tool permissions separately).
	- ## Policy expression
		- Policies are declarative over canonical identity `provider/owner/repo`. There is no separate `[trust]` table.
		- **MVP**
			- `[sources]` entries are **allowed** and **installed by default** on `srcr install`.
			- No `[allow]` table; identities not in `[sources]` cannot be materialized.
		- **Phase 2**
			- `[allow]` — wildcard patterns that permit download without auto-install, e.g.:
				- ~~~toml
				  [allow]
				  "github.com/my-org/*" = true
				  "github.com/my-org/internal-*" = true
				  ~~~
			- `[sources]` with `install = false` — allowed and path-resolvable, not cloned until `srcr use`.
			- Deny-by-default for ad-hoc clone when identity matches neither `[sources]` nor `[allow]`.
		- Wildcards should match path segments predictably; document whether `*` crosses `/` boundaries.
		- Evaluation order for Phase 2: deny-wins vs allow-wins TBD (recommend default deny for ad-hoc `use`, explicit `[sources]` + `[allow]` only).
	- ## Enforcement points
		- `srcr install` (MVP) — materialize only `[sources]` entries with default install; fail closed on config errors (recommend **fail** with non-zero exit for CI and agents).
		- `srcr use <identity>` (Phase 2) — reject before any network or git operation if identity is not allowed; replaces defunct `srcr ensure`.
		- `srcr where` — resolves path without clone; JSON reports `allowed: false` so planners do not treat the tree as approved for fetch.
		- Future: read-only mode where agents may read existing allowed paths but cannot trigger clone.
	- ## JSON and fail-closed behavior
		- Access verdict surfaces in structured output (see [[Person/codekiln/GitHub/sourcer/Project/v0 AI Spec/CLI]]):
			- ~~~json
			  {
			    "uri": "github.com/evil/example",
			    "allowed": false,
			    "error": "identity not allowed by access policy"
			  }
			  ~~~
		- Agents should treat `allowed: false` as hard stop unless a human overrides policy.
		- Human CLI: print actionable message ("add identity to `[sources]` or pattern to `[allow]`" — Phase 2; break-glass flag only if product allows).
	- ## Pre-configured corpora for agents
		- [[DevContainer]] images and CI runners build a **fixed corpus** at image build time:
			- MVP: only identities in `[sources]` get cloned on `srcr install`.
			- Phase 2: `[allow]` may permit optional `srcr use` at runtime without baking into image.
			- Agent runtime has no credentials to reach arbitrary hosts if network is restricted.
		- Skills and prompts can say: "read dependencies under `~/sources` via `srcr where`" without embedding paths.
		- Aligns with overview motivation: repositories as **installable context packages** for agentic work.
	- ## Soft links vs hard dependencies
		- Sourcer supports **contextually related** repos — libraries you should read, platforms you integrate with, internal docs repos — without [[git submodules]].
		- Submodules remain appropriate when:
			- another repo at a pinned commit is a **build input**,
			- reproducibility must be encoded in the parent repo's history,
			- consumers must get exact SHAs on clone.
		- Sourcer fits when:
			- relationship is advisory ("onboarding set"),
			- pins can float on branches/tags acceptable for exploration,
			- multiple parent projects share the same cached clone under `root`.
	- ## Documentation vs source
		- [[llms.txt]] and domain allowlists reduce risk for **published docs** at a stable URL.
		- When docs live only in git, or research needs implementation truth, local allowed clone wins.
		- Access policy for repos does not remove the need to read code for edge cases.
	- ## Operational patterns
		- **MVP** — service repo `srcr.toml` lists `[sources]`; `srcr install` in CI and devcontainer builds.
		- **Phase 2 — org-wide baseline** — security publishes `allow.d/org.toml` fragment; projects include it.
		- **Phase 2 — project overlay** — `[sources]` for install set; `[allow]` for org wildcards without auto-install.
		- **Agent sandbox** — minimal `[sources]` list (3–10 repos); expand only via human-approved config PR.
		- **Shared laptop cache** — permissive `[allow]` for developer convenience (Phase 2), stricter merged policy for agent sandbox profile.
	- ## Relationship to shared cache
		- Access policy controls **what may enter** the shared corpus under `root`.
		- Once materialized, all workspaces benefit from single clone (see overview: shared local source cache).
		- Eviction and GC (future) must respect policy — disallowed paths should not be created in the first place.
	- ## Future access features (Phase 2 and beyond)
		- Signed policy bundles.
		- Per-source audit log (who cloned what, when).
		- Time-bound allow (`expires_at` on pattern).
		- Integration with [[DevContainer/Feature]] to inject `[allow]` without merging into developer global config.