logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[1Password/Dev/op/run]], [[1Password/Dev/CLI/Secret Reference]]

- # When using [[1Password/Environment]]s, is there an easy way to load a variable from a [[1Password]] secret?
	- ## [[AI Answer]]
		- **Short answer:** not inside the Environment itself, as of 2026-09-30. An Environment variable holds a literal value, and it cannot link to a field on a vault item. If you paste `op://vault/item/field` as the value, the mounted `.env` hands back that string, not the secret. The easy way to get both today is `op run`, which reads an Environment and a file of `op://` references in the same command.
		- ### What the docs and forum say
			- [[Answer/Official]] from [Environments — 1Password Developer](https://www.1password.dev/environments): variables are added by importing a `.env` or by typing a name and value, and "1Password Environments return values exactly as they are entered." The docs never mention references to vault items.
			- The MCP server's own guide describes `append_variables` the same way: each variable is a name, a value, and a `concealed` flag. Nothing takes an item reference.
			- On the 1Password Community, users have asked for this since the 2025 beta, so they don't have to keep the same API key in a vault item and in an Environment. One user reported that importing a `.env` of secret references stored the references as literal text. 1Password staff replied only that they passed the feedback on. ([Frustrations with .env File Handling and Environments](https://www.1password.community/developers-69/frustrations-with-env-file-handling-and-environments-in-1password-22335), [1Password Environments Beta is awesome](https://www.1password.community/developers-69/1password-environments-beta-is-awesome-23264))
		- ### Workaround: `op run` with both sources
			- [[Answer/Official]] from [op run — 1Password CLI reference](https://www.1password.dev/cli/reference/commands/run): `--environment` and `--env-file` can be passed together, and `op run` resolves the `op://` references in the file.
			- Keep the Environment for values that live only there, and put vault-backed ones in a committable file of references:
				- ~~~bash
				  # .env.refs — safe to commit, holds no secrets
				  OPENAI_API_KEY=op://Private/OpenAI/credential
				  GITHUB_TOKEN=op://Private/GitHub PAT/token
				  ~~~
				- ~~~bash
				  op run --environment <environment-id> --env-file .env.refs -- npm run dev
				  ~~~
			- Copy the Environment ID from the desktop app: Developer → View Environments → the Environment → Manage environment → Copy environment ID.
			- **Name clashes:** when a name appears in both sources, the Environment wins, then the env file, then the shell. Define each name in only one place, or the stale Environment copy silently overrides the vault item.
			- **What you give up:** this path goes through `op` and a biometric prompt, not the mounted named pipe. A process that just opens `.env`, like a `dotenv` loader, sees only the Environment's literal values.
		- ### Untested variant
			- Store `op://…` strings as the Environment's values, mount it, and run `op run --env-file .env -- <command>` against the mount. `op run` should resolve the references it reads from the pipe, which keeps one list of names in the Environment and the values in vault items. No source confirms this, so try it on a throwaway Environment first.
