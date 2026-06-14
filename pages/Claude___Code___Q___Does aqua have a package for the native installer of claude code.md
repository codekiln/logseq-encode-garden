tags:: [[Claude/Code]], [[Q]]
alias:: [[Anthropic/App/Claude Code/Q/Does aqua have a package for the native installer of claude code]]
logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[aqua]], [[mise/Backend/aqua]], [[Claude/Code]]
title:: Claude/Code/Q/Does aqua have a package for the native installer of claude code

- # Does [[aqua]] have a package for the native installer of [[Claude/Code]]?
- ## Answer
	- [[AI/Response]]
		- **Yes.** The canonical registry entry is **`anthropics/claude-code`** ([`pkgs/anthropics/claude-code/registry.yaml`](https://github.com/aquaproj/aqua-registry/blob/main/pkgs/anthropics/claude-code/registry.yaml) in [aquaproj/aqua-registry](https://github.com/aquaproj/aqua-registry)).
		- **What it installs:** the package is declared with **`type: http`**, not as an npm artifact. It downloads the **`claude`** raw binary from Anthropic’s **Google Cloud Storage** release bucket (`claude-code-releases/...`), i.e. the same **native binary distribution channel** used by the standalone installer story, not the `@anthropic-ai/claude-code` npm package.
		- **How [[mise]] wires it:** the upstream tool shortname `claude` lists `aqua:anthropics/claude-code` for **Linux and macOS**, with separate backends for the direct **HTTP** template and for **npm** on other targets; see [`registry/claude.toml`](https://github.com/jdx/mise/blob/main/registry/claude.toml) in [jdx/mise](https://github.com/jdx/mise).
		- **Platform caveat:** the aqua-registry file’s **`supported_envs`** for this package are **Darwin and Linux** in the published YAML; **Windows** is handled in mise via the **`http:claude`** / **`npm:@anthropic-ai/claude-code`** backends in that same `claude.toml`, not via the aqua stanza. So “aqua has the native-style package” is accurate for **macOS/Linux**; on **Windows**, use those other backends or install paths unless the registry gains Windows coverage later.