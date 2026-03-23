tags:: [[Idea]]
date-created:: [[2026-03-23 Mon]]

- # Cron (or CI) lint for agentic coding tool permission and allow lists
	- Run scheduled checks across repos that contain configs for [[AI/Agent]]ic coding tools (editor agents, CLI coders, MCP servers, sandbox allowlists, etc.)
	- Goal: catch over-broad rules that slip in through approval fatigue — e.g. always-allow entire hostnames such as `github.com`, blanket network permissions, or “trust this path forever” patterns that are wider than intended
	- With enough repos and enough “Allow” clicks, at least one config will eventually accumulate a dumb rule; treat that as statistically inevitable, not a personal failure
	- Overly wide allowlists enlarge the attack surface for prompt injection and exfiltration: if fetch, browse, or shell is effectively unconstrained within a trusted-looking domain class, an agent can be steered into actions the operator thought they had gated
	- Lint policy examples (to encode in rules): deny-list glob domains; require scoped paths or repo-specific origins; flag new `always` / `*` / top-level registry keys; diff allowlists in PRs with noisy alerts
	- Implementation sketch: small script + cron or GitHub Action that parses known config formats (per tool), fails on patterns from a shared deny list, and optionally posts a summary
