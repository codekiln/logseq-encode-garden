# Graph registry (v1: ghq-resolved or local disk)

## Source of truth

**File:** `.rulesync/config/logseq-proxy.md` in the **active** Logseq garden repo (the one you are writing into).

Agents **must** read this file before resolving `logseq://graph/...` URLs. If a graph name is missing, **stop** and ask the user to add a row (do not guess paths).

## Schema

Each **graph** is one row in the **Graphs** table:

| Column | Required | Meaning |
|--------|----------|---------|
| `graph_name` | yes | String after `logseq://graph/` in the URL. Must match exactly (case-sensitive unless you standardize lowercase in your registry). |
| `ghq-address` | one of `ghq-address` / `root` | The `ghq` address for the graph's repo, e.g. `github.com/codekiln/logseq-encode-garden` — the same string used as `ghq-address::` on that repo's `[[My/Repo/GitHub/<org>/<repo>]]` page in this garden, if one exists. Resolve the actual on-disk path at sync time with `ghq list --full-path --exact <ghq-address>`; **never** hardcode the result into the registry. |
| `root` | one of `ghq-address` / `root` | Absolute path to the graph root: directory that contains `pages/` and `logseq/` (and usually `journals/`). Use this **only** when the graph is not a `ghq`-managed repo. If both columns are set, `ghq-address` takes precedence. |
| `notes` | no | Free text. |

## Resolving `root` at sync time

1. If `ghq-address` is set, run `ghq list --full-path --exact <ghq-address>`.
   - **One path returned** — that is `root` for this sync.
   - **No path returned** — the repo isn't cloned locally. **Stop and ask the user** before cloning it (per their global rule to ask before cloning new repos); do not guess a path or invent one.
   - **Multiple paths returned** — stop and ask the user to disambiguate.
2. Otherwise use the row's `root` value directly.
3. Validate: the resolved `root` must exist and contain `pages/` and `logseq/` before sync.

## Future: GitHub / git

If a graph exists on GitHub but has never been cloned locally, ask the user before cloning it, then either let `ghq-address` resolve it from then on, or set `root` if it ends up somewhere `ghq` doesn't track.
