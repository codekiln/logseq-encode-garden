# nbb-logseq

`nbb-logseq` is the preferred runtime for deterministic Logseq graph scripts when available.

Relevant upstream facts:

- Repository: https://github.com/logseq/nbb-logseq
- It provides ClojureScript scripting on Node.js for Logseq.
- It bundles useful Logseq-adjacent libraries, including Datascript support.
- For file graphs, use it for querying, parsing, and validation.
- DB graphs can be written by scripts, but file graph mutation should still happen through normal Markdown edits unless a specific DB workflow is active.

## Install

Assume global CLI tools are managed by `mise`. Install `nbb-logseq` globally with:

```sh
mise use -g npm:@logseq/nbb-logseq@latest
```

This writes the tool to the global mise config and makes `nbb-logseq` available through mise shims.

One-off fallback when a global install is not appropriate:

```sh
npx -y @logseq/nbb-logseq .rulesync/skills/logseq-link-hygiene/scripts/resolve-wikilinks.cljs --changed <file>...
```

## Script contract

Run from the graph root. The script reads `pages/`, `journals/`, and the changed files passed after `--changed`.

Output is line-delimited JSON. Each line has:

- `link`
- `file`
- `status`
- `canonical`
- `candidates`

Statuses are:

- `canonical`
- `alias-match`
- `normalized-match`
- `date-link`
- `ambiguous`
- `unresolved`

The script is a checker. It does not edit files.
