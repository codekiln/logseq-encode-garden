- [[mise]] config
	- ```toml
	  [tasks.rulesync]
	  # https://github.com/dyoshikawa/rulesync/tree/main
	  description = "Node.js CLI tool to sync AI coding rules across multiple tools."
	  run = "npx rulesync $@"
	  ```	- **`rulesync` and `npx rulesync` are different tools on this machine, and a task written with `npx` gets the older one.** Measured [[2026-08-25 Tue]]: `rulesync` on `PATH` is 16.14.0, installed by [[mise]] from `"npm:rulesync" = "latest"`; `npx rulesync` is 8.15.0 from a cached copy. A `run = "npx rulesync $@"` task therefore bypasses the version mise pins.
	- Use `mise exec -- rulesync generate` so the pinned tool runs. `.rulesync/skills/readwise-skills-sync/scripts/sync.sh` already does.
	- **`latest` is not a pin.** The version moves whenever mise reinstalls, so a version-specific behaviour is not something to rely on without reading it back. 16.14.0 stops at the first rule source carrying no frontmatter and writes zero rules; in [[My/Knowledge/Garden/logseq-encode-garden]] both sources under `.rulesync/rules/` have frontmatter, so that failure does not apply here.
