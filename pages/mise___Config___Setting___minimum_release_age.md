# [minimum_release_age mise setting](https://mise.jdx.dev/configuration/settings.html#minimum_release_age)
	- Type: `string`(optional)
	- Env: `MISE_MINIMUM_RELEASE_AGE`
	- Default: `None`
	  
	  Filter tool versions by release date to limit supply chain risk. Similar to Renovate's [minimum release age](https://docs.renovatebot.com/key-concepts/minimum-release-age/), this ensures newly published versions are ignored until they've been available for a configurable amount of time — giving the community time to discover compromised releases. This name matches pnpm's `minimumReleaseAge` setting, though mise accepts both relative durations and absolute cutoff dates.
	  
	  Supports:
	- Relative durations: `7d` (7 days ago), `90d` (90 days ago), `6m` (6 months ago), `1y` (1 year ago)
	- Absolute dates: `2024-06-01`, `2024-06-01T12:00:00Z`
	  
	  Example:
	  
	  ```
	  [settings]
	  minimum_release_age = "7d"  # only install versions released more than 7 days ago
	  ```
	  
	  Only affects backends that provide release timestamps (aqua, cargo, npm, pipx, and some core plugins). Versions without timestamps are included by default.