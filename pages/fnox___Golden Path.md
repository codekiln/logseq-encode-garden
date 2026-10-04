tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[fnox/How To/Use Apple Secure Enclave Touch ID]]

- # [[fnox]] [golden path](https://fnox.jdx.dev/guide/what-is-fnox#the-golden-path)
	- ## Overview
		- The **golden path** is the workflow [[fnox]] recommends for a team that already keeps secrets in a remote vault such as [[1Password]]: the vault stays the single source of truth, and each person reads from a personal encrypted cache on their own machine.
		- Upstream describes it in [What is fnox?](https://fnox.jdx.dev/guide/what-is-fnox#the-golden-path) and walks through it in [Connect a vault and cache locally](https://fnox.jdx.dev/guide/golden-path.html). Both were read from a local clone of [jdx/fnox](https://github.com/jdx/fnox) at commit `03e9aee` (2026-10-01).
	- ## Context
		- fnox can hold secrets as ciphertext in `fnox.toml`, as references into a vault, or as plain defaults. The golden path combines the second with local encryption.
		- Every vault read can need the vault's CLI, a network connection and an authentication prompt. The cache removes those from daily use.
		- Without a vault, fnox points to its [age quick start](https://fnox.jdx.dev/guide/quick-start) instead.
	- ## Key Principles
		- The vault is the source of truth. `fnox.toml` is committed and holds references, never secret material.
		- Each person's cache is encrypted to their own key. Nothing is shared except the vault, so onboarding means granting vault access and repeating the setup on the new machine.
		- The cache is a snapshot. It does not refresh on its own; sync again after a secret changes.
		- Only the machine-wide key setup changes when the key moves into hardware. Everything after it stays the same.
	- ## Mechanism
		- 1. One-time per machine: create a personal [age](https://github.com/FiloSottile/age) key and a global `sync-age` provider in `~/.config/fnox/config.toml`.
		- 2. Put secrets in the vault, then commit a provider and per-secret references in `fnox.toml`.
		- 3. Add `fnox.local.toml` to `.gitignore`.
		- 4. Run `fnox sync --provider sync-age --local-file`. fnox resolves each value from the vault, re-encrypts it to your age key and writes it to `fnox.local.toml`.
		- 5. From then on fnox finds the `sync` field on each secret first and decrypts locally, whether through `fnox exec`, `fnox get` or shell integration (`eval "$(fnox activate zsh)"`).
		- Any remote provider can stand in for 1Password. In CI the golden path does not apply: the job authenticates to the vault directly, for example with a service account token.
	- ## Examples
		- Hardening the key: the age key can live in Apple's Secure Enclave instead of a key file, see [[fnox/How To/Use Apple Secure Enclave Touch ID]]. Upstream also covers a YubiKey, a TPM and FIDO2 tokens in its [sync guide](https://fnox.jdx.dev/guide/sync#hardware-backed-decryption).
		- Preference for pairing [[fnox]] with a secret store is on [[My/Pref/Dev/Tool/Secrets/fnox]].
	- ## Misconceptions
		- The cache is not a replacement for the vault. A revoked or rotated secret stays readable from the cache until the next sync.
		- Cached values are not portable. Each is encrypted to one person's key, and a Secure Enclave key works on only one Mac.