logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Obsidian/Q/Can a custom Obsidian plugin live in the same repository as its vault and be installed locally on desktop and iPhone?]], [[Obsidian/CLI]]

- # How can an [[Obsidian]] vault declare the community plugins it depends on and install them by script?
	- ## [[AI Answer]]
		- **Short answer:** The declaration half already exists — `.obsidian/community-plugins.json` is an array of enabled community plugin IDs that Obsidian itself writes, and committing it makes the plugin set part of the vault. The missing half is the fetch, and there are now four working ways to script it: the official CLI's `plugin:install` (Obsidian 1.12+), vendoring the plugin payloads into the repo, [[Nix]] + home-manager, or a ~20-line resolver against the public plugin registry.
		- ### 1. Official CLI — `obsidian plugin:install`
			- [[Answer/Official]] from [Obsidian CLI](https://obsidian.md/help/cli). The [[Obsidian/CLI]] added first-class plugin management: `plugins`, `plugin:install`, `plugin:uninstall`, `plugin:enable`, `plugin:disable`, `plugins:restrict`.
			- Loop the committed ID list through it:
				- ~~~bash
				  #!/usr/bin/env bash
				  set -euo pipefail
				  VAULT="${1:?vault name}"
				  obsidian vault="$VAULT" plugins:restrict off
				  jq -r '.[]' ".obsidian/community-plugins.json" | while read -r id; do
				    obsidian vault="$VAULT" plugin:install id="$id" enable
				  done
				  ~~~
			- `plugins:restrict off` matters: community plugins do not load while restricted mode is on, and that is otherwise a UI toggle.
			- **Constraints.** Requires the 1.12.7+ installer, a one-time **Settings → General → Command line interface** registration per machine, and a running app (the first command launches Obsidian). Desktop only — there is no CLI on iOS.
		- ### 2. Vendor the plugin payloads into the repo
			- Commit `.obsidian/plugins/<id>/{manifest.json,main.js,styles.css}` directly. Cloning the repo *is* the install; nothing is fetched and nothing is clicked.
			- This is the only approach that also covers iPhone/iPad, where the same tradeoffs apply as in [[Obsidian/Q/Can a custom Obsidian plugin live in the same repository as its vault and be installed locally on desktop and iPhone?]].
			- Cost: build output lives in the notes repo, and updates are a manual re-vendor. Pair it with approach 4 as the refresh script.
		- ### 3. [[Nix]] + home-manager (fully declarative)
			- The `programs.obsidian` home-manager module merged in [PR #6487](https://github.com/nix-community/home-manager/pull/6487) (May 2025) and covers vaults, community plugins with their settings, themes, CSS snippets, and hotkeys.
			- [karaolidis/nix-obsidian-extensions](https://github.com/karaolidis/nix-obsidian-extensions) supplies the packages: an overlay exposing `pkgs.obsidianPlugins` and `pkgs.obsidianThemes`, scraped daily from the official registry, consumed as a flake input and referenced by plugin ID.
			- This is the strongest coupling available — plugin set, plugin settings, and hotkeys all rebuild from one config — at the cost of adopting Nix for the machine.
		- ### 4. Resolve the registry yourself (headless, no Obsidian needed)
			- `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json` is the public registry. Each entry carries `id`, `name`, `author`, `description`, and `repo`, so an ID resolves to a GitHub slug, and the release assets are the three files Obsidian would have downloaded anyway.
				- ~~~bash
				  #!/usr/bin/env bash
				  set -euo pipefail
				  VAULT="${1:-.}"
				  registry=$(curl -fsSL https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json)
				  jq -r '.[]' "$VAULT/.obsidian/community-plugins.json" | while read -r id; do
				    repo=$(jq -r --arg id "$id" '.[] | select(.id==$id) | .repo' <<<"$registry")
				    [ -n "$repo" ] || { echo "not in registry: $id" >&2; continue; }
				    tag=$(gh api "repos/$repo/releases/latest" --jq .tag_name)
				    dir="$VAULT/.obsidian/plugins/$id"; mkdir -p "$dir"
				    for f in manifest.json main.js styles.css; do
				      curl -fsSL -o "$dir/$f" "https://github.com/$repo/releases/download/$tag/$f" || true
				    done
				  done
				  ~~~
			- `styles.css` is optional per plugin, hence the tolerant `|| true`. Use `gh api` rather than bare `curl` against the GitHub API so the 60-request-per-hour unauthenticated limit does not bite on a large plugin set.
			- Runs in CI and on a fresh machine before Obsidian is ever launched. Pin `tag` per plugin instead of `latest` to get lockfile behavior.
		- ### Other tools, and why they place lower
			- [obsidian-plugin-cli](https://github.com/obsidian-tools/obsidian-tools) — `obsidian-plugin install <id> -v <vault>`, installs from the registry or a GitHub slug, no running app required. Self-described alpha with expected breaking changes before 1.0.
			- [Community Install Manager](https://github.com/skilletron/obsidian-automatic-installation-of-plugins) — an in-vault plugin that reads `.obsidian/community-plugins-list.json` plus a settings map and installs on startup. It also applies per-plugin settings, which the CLI does not, but it has a bootstrap problem: that plugin itself must be placed by hand first, so it only pays off when combined with vendoring it.
			- The community has repeatedly asked for this as a built-in — see [a single button click to reinstall all community plugins](https://forum.obsidian.md/t/a-single-button-click-to-reinstall-all-community-plugins-after-cloning-pulling-git-repository-that-ignores-plugins/100826) — and `plugin:install` is the closest thing to an official resolution.
		- ### Recommended combination
			- Commit `.obsidian/community-plugins.json` as the declaration, and check in a `bootstrap` script implementing approach 4 so a fresh clone is one command with no Obsidian process and no clicking. Keep approach 1 as the on-machine path once Obsidian is running, and vendor payloads only for the plugins that must work on iOS.
