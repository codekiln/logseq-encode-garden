# Listing proxied pages and graphs

Proxied pages are identified by the presence of **`logseq-url::`** (set by this skill). Use ripgrep from the **destination graph root** (repo with `pages/`).

## All proxied pages

~~~bash
rg -n 'logseq-url::' pages/ --glob '*.md'
~~~

Each hit is a proxied page (or a page that reused the property manually—treat as proxied).

## Pages proxied from a specific graph

The graph segment appears in the URL after `logseq://graph/`:

`logseq://graph/<graph_name>?page=...`

**Filter by graph name** (example: `logseq-encode-garden`):

~~~bash
rg -n 'logseq-url::.*logseq-encode-garden' pages/ --glob '*.md'
~~~

Or broader:

~~~bash
rg -n 'logseq://graph/logseq-encode-garden' pages/ --glob '*.md'
~~~

## Distinct source graphs

1. Run:

~~~bash
rg -o 'logseq://graph/[^?]+' pages/ --glob '*.md' | sort -u
~~~

2. Or read lines with `logseq-url::` and parse the path segment after `logseq://graph/` up to `?` or end of line.

## Agent-facing answers

- **“What Logseq pages are proxied?”** — List paths under `pages/` that contain `logseq-url::`, optionally showing the `logseq-url` value and `logseq-proxy-last-sync-date::` if present.
- **“What is proxied from graph X?”** — Filter as above.
- **”Which gardens do we proxy from?”** — Unique `graph` segments from all `logseq-url::` values.

Proxies mirror the source page's exact name, so they are scattered across `pages/` wherever that name naturally falls — there is no dedicated namespace to narrow the search to. Always search repo-wide.
