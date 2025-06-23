tags:: [[Diataxis/How To]]

- # How To wrap **rclone** with **1Password + mise**
	- ## Goal
		- Use `~/.config/rclone/rclone.env` to hold 1Password secret references, then call **rclone** through a **mise** task that runs `op run` so secrets are injected at runtime.
	- ## Preconditions
		- rclone ≥ 1.65 installed and in PATH.
		- A configured 1Password desktop app and CLI (`op`) with biometric unlock.
		- `mise` ≥ 2025.5 installed (`brew install mise`).
		- Your rclone remote names contain only letters, digits, or `_` so they map cleanly to env-vars.
	- ## Procedure
		- ### 1. Author the `rclone.env` file
			- Create the directory if needed: `mkdir -p ~/.config/rclone`
			- Add one variable per secret **using 1Password secret-reference URIs**:
			  ~~~env
			  # AWS remote called "s3prod"
			  RCLONE_CONFIG_S3PROD_TYPE=s3
			  RCLONE_CONFIG_S3PROD_PROVIDER=AWS
			  RCLONE_CONFIG_S3PROD_ACCESS_KEY_ID=op://DevVault/S3Prod/key_id
			  RCLONE_CONFIG_S3PROD_SECRET_ACCESS_KEY=op://DevVault/S3Prod/secret_key
			  # optional global flags
			  RCLONE_STATS=5s
			  ~~~
			- rclone reads any `RCLONE_*` or `RCLONE_CONFIG_<REMOTE>_*` variables just like CLI flags, so this completely avoids putting credentials in `rclone.conf`.
		- ### 2. Verify the env-file with `op run`
			- Test interactively:
			  ~~~bash
			  op run --env-file ~/.config/rclone/rclone.env -- \
			   rclone lsd s3prod:/
			  ~~~
			- `op run` resolves each `op://…` reference, exports the resulting plaintext, then executes the wrapped command.
		- ### 3. Create the **mise** task
			- Edit (or create) `~/.config/mise/config.toml`:
			  ~~~toml
			  [tasks.rclone]
			  desc = "rclone with 1Password-injected secrets"
			  run = [
			   "op run --env-file ~/.config/rclone/rclone.env -- rclone"
			  ]
			  ~~~
			- Because no templated args (`{{arg(...)}}`, etc.) are defined, any arguments passed to `mise rclone …` will automatically be forwarded to `rclone`.
		- ### 4. Use it
			- Copy a directory:
			  ```bash
			  mise rclone copy ~/projects s3prod:backup/projects --progress
			  ```
			- All secrets are fetched on-demand via Touch ID; nothing ever hits disk unencrypted.
	- ## Troubleshooting
		- **`op: item not found`** → check the vault/item names in each secret reference.
		- **`No accounts configured for use with 1Password CLI`** → unlock 1Password or run `op signin` if desktop integration is disabled.
		- **rclone reports missing credentials** → confirm the env-var names follow `RCLONE_CONFIG_<REMOTE>_<OPTION>` exactly.
	- ## References
		- [Load secrets into scripts](https://developer.1password.com/docs/cli/secrets-envvars/)
		- [Environment Variables](https://rclone.org/docs/#environment-variables) – rclone Documentation