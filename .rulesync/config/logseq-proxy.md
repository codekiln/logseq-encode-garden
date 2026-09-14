# Logseq proxy registry

Machine-local paths belong here. **Edit `root` values** for your computer; do not commit secrets.

Authoritative schema and column meanings: `.rulesync/skills/logseq-proxy/references/graph-registry.md` in `logseq-garden`.

## Graphs

| graph_name | root | dest_prefix | mirror_flat | github | notes |
|------------|------|-------------|-------------|--------|-------|
| logseq-garden | `~/ghq/github.com/codekiln/logseq-garden` | | false | codekiln/logseq-garden | Personal day-to-day garden; source of proxied entity pages |

## How to add a row

1. `graph_name` must match the segment in `logseq://graph/<graph_name>?page=...` exactly.
2. `root` must be the directory that contains `pages/` and `logseq/`.
3. Leave `dest_prefix` empty to use the default `Logseq/Proxy/<graph_name>/...` in the **destination** garden.
4. Set `mirror_flat` to `true` only if you intentionally want `pages/<Page>.md` at the top level (collision risk).

## v1 limitation

**GitHub** is documentation-only. Clone or pull the repo locally, point `root` at that clone, then run the proxy workflow.
