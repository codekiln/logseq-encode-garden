# Logseq proxy registry

Prefer `ghq-address` over a hardcoded path — it resolves fresh on whatever machine you run this on, so a row never goes stale. Only set `root` directly for a graph `ghq` doesn't manage.

Authoritative schema and column meanings: `.rulesync/skills/logseq-proxy/references/graph-registry.md`.

## Graphs

| graph_name | ghq-address | root | notes |
|------------|-------------|------|-------|
| logseq-garden | `github.com/codekiln/logseq-garden` | | Personal day-to-day garden; source of proxied entity and reading pages |

## How to add a row

1. `graph_name` must match the segment in `logseq://graph/<graph_name>?page=...` exactly.
2. Prefer `ghq-address` (e.g. `github.com/<org>/<repo>`) — the same address used as `ghq-address::` on that repo's `[[My/Repo/GitHub/<org>/<repo>]]` page, if one exists. It resolves via `ghq list --full-path --exact <ghq-address>` at sync time.
3. Only set `root` directly when the graph isn't a `ghq`-managed repo. If both are set, `ghq-address` wins.
4. If `ghq-address` resolves to nothing, the repo isn't cloned locally — stop and ask before cloning it.
