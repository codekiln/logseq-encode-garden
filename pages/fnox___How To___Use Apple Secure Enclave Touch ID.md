tags:: [[Diataxis/How To]]
logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[fnox/Golden Path]]

- # How to use Apple Secure Enclave Touch ID with [[fnox]]
	- ## Overview
		- Keep the [[fnox]] sync cache's age key inside Apple's Secure Enclave, so decrypting secrets on your Mac can require Touch ID instead of reading a key file from disk.
		- Source: the [Secure Enclave section of the fnox sync guide](https://fnox.jdx.dev/guide/sync#apple-secure-enclave-touch-id), read from a local clone of [jdx/fnox](https://github.com/jdx/fnox) at commit `03e9aee` (2026-10-01). The commands below are copied from that guide.
	- ## Prerequisites
		- A Mac with a Secure Enclave running macOS 14 or later.
		- [fnox installed](https://fnox.jdx.dev/guide/installation).
		- [[Brew]] to install the plugin.
		- A project already set up for `fnox sync`, as in [[fnox/Golden Path]].
	- ## Steps
		- ### 1. Install the plugin
			- [age-plugin-se](https://github.com/remko/age-plugin-se) must be on your `PATH`.
			- ~~~bash
			  brew install age-plugin-se
			  ~~~
		- ### 2. Generate a hardware-bound identity
			- ~~~bash
			  mkdir -p ~/.config/fnox
			  age-plugin-se keygen --access-control=any-biometry -o ~/.config/fnox/age-se.txt
			  ~~~
			- The command prints a public key beginning `age1se1...`. Copy it.
			- `--access-control` sets when the Secure Enclave asks for a fingerprint. fnox's guide names `any-biometry`, `any-biometry-or-passcode` and `none`, and lists more. If you want Touch ID on every decryption, use `any-biometry`; `none` skips the prompt.
		- ### 3. Point the sync provider at the identity
			- Put the recipient in the global config so every project on the machine reuses the key.
			- ~~~toml
			  # ~/.config/fnox/config.toml
			  [providers.sync-age]
			  type = "age"
			  recipients = ["age1se1..."]
			  key_file = "~/.config/fnox/age-se.txt"
			  ~~~
			- `age-se.txt` holds a reference to the key in the Secure Enclave, not the private key. Treat it like an identity file anyway.
		- ### 4. Unset `FNOX_AGE_KEY`
			- If `FNOX_AGE_KEY` is exported, unset it. It takes precedence over the provider's `key_file`.
		- ### 5. Sync
			- ~~~bash
			  fnox sync --provider sync-age --local-file
			  ~~~
			- `fnox get`, `fnox exec` and shell integration now decrypt the cache through the Secure Enclave. Whether a Touch ID prompt appears depends on the access control you chose in step 2.
		- ### 6. Re-sync an existing cache
			- A cache written earlier with a file-based age key is encrypted to that old key. Run the sync command from the [[fnox/Golden Path]] with `--force` to rewrite it: `fnox sync --provider sync-age --local-file --force`.
			- Unverified: fnox's docs describe `--force` for refreshing a stale cache, not for switching keys. Confirm that it replaces entries encrypted to the old key.
	- ## Troubleshooting
		- The key only decrypts on the Mac that generated it, so a cache synced here cannot be read from another machine. Run the setup on each machine.
		- Unverified: how fnox behaves when the Touch ID prompt is cancelled, or when the Mac has no enrolled fingerprint. The upstream docs do not say.
