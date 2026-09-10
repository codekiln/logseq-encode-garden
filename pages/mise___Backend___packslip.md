tags:: [[packslip]]

- # [packslip](https://mise.jdx.dev/dev-tools/backends/packslip.html) backend for mise
	- Installs tools from signed Packslip release manifests: mise verifies the publisher, selects the host-matching artifact, and can surface version-matched shell completions and agent skills declared in the release.
	- Preferred Tier 1 backend when a publisher ships Packslip manifests; otherwise use [[aqua]], GitHub, or another supported [[mise/Backend]].
	- Identifier form: `packslip:github.com/owner/repo` (GitHub host may be omitted: `packslip:jdx/hk`). Domain projects use a host/path that points at a signed release list.
	- Example: `mise use packslip:github.com/jdx/hk` records [[hk]] in `mise.toml`; the registry shorthand `mise use hk` also selects Packslip by default for current releases.
