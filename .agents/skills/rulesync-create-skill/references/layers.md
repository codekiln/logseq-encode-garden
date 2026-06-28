# Three layers for a Rulesync skill

Progressive disclosure means **staging** what enters the model context: metadata first, core instructions when the skill matches, bundled files only when the task needs them.

## Level 1 — Discovery (YAML on `SKILL.md`)

- **Always-on cost**: frontmatter is what agents use to **select** among skills.
- **Rulesync**: keep `name` stable; set `targets` appropriately; add tool-specific blocks only when they change real behavior (for example `allowed-tools`, `short-description`).
- **Write `description` like a trigger spec**: concrete user intents, technologies, and boundaries (“use when…”, “do not use for…”).

## Level 2 — Core procedure (body of `SKILL.md`)

- Loaded **after** the skill is chosen; still shared with everything else in the window, so keep it **short and procedural**.
- Start with **quick start** or numbered default path.
- Tell the agent **when to open** each reference file or **when to run** each script so it does not preload “just in case.”
- Prefer **relative links** (`./references/foo.md`) so the skill stays portable across clones.

## Level 3 — Bundled resources (same directory)

Typical layout:

```text
.rulesync/skills/<skill-name>/
├── SKILL.md
├── references/     # long tables, API notes, rare branches
├── scripts/        # deterministic or token-heavy steps
└── assets/         # templates, static files for outputs
```

- **`references/`**: one topic per file when possible; filenames should signal when to load them.
- **`scripts/`**: document invocation, inputs, and what to trust in stdout or artifacts; execution can avoid loading entire source into context.
- **Precedence**: local skills under `.rulesync/skills/<name>/` override curated copies with the same name (see Rulesync declarative sources docs).

## Relation to the generic `skill-creator` skill

Upstream `skill-creator` (for example from `anthropics/skills`) is **general** skill authoring. This garden’s workflow is **Rulesync-shaped**: same directory model, plus `targets` and tool-specific YAML from Rulesync. Follow both: Rulesync file-format constraints here, token discipline from `skill-creator` where it does not conflict.
