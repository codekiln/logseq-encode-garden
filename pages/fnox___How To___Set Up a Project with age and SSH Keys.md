tags:: [[Diataxis/How To]]
logseq-entity:: [[Logseq/Entity/Diataxis/How To]]
see-also:: [[fnox/Golden Path]]

- # How to set up a project to use [[fnox]] with age and SSH keys
	- ## Overview
		- Commit secrets to a project as age ciphertext in `fnox.toml`, encrypted to each teammate's existing SSH public key, so anyone with a matching SSH private key can decrypt after a `git pull`.
		- Source: the [age provider guide](https://fnox.jdx.dev/providers/age), read from a local clone of [jdx/fnox](https://github.com/jdx/fnox) at commit `03e9aee` (2026-10-01). Commands are copied from that guide; the scenarios below have not been run.
	- ## How it works
		- Each value is encrypted with [age](https://github.com/FiloSottile/age) to a list of **recipients**, the public keys in the `age` provider's `recipients` array. A recipient can be an SSH public key (`ssh-ed25519` or `ssh-rsa`), a native `age1...` key, or an age plugin key.
		- Decrypting needs the **private** half of any one recipient. fnox looks for it in `FNOX_AGE_KEY`, then the provider's `identity`, then its `key_file`, then `FNOX_AGE_KEY_FILE`, then `age.txt` in the fnox config directory. For SSH keys, point `FNOX_AGE_KEY_FILE` at the private key.
		- The ciphertext stores which recipients it was encrypted to. Editing the `recipients` list changes nothing already encrypted until `fnox reencrypt` rewrites it. That one fact drives the add and retire scenarios.
	- ## Prerequisites
		- [fnox installed](https://fnox.jdx.dev/guide/installation) and the `age` CLI. fnox can encrypt to SSH recipients without it; install it with `brew install age` if you also want `age-keygen` for a CI key.
		- Every person has an SSH key of type `ed25519` or `rsa` (2048 bits minimum, 4096 recommended).
		- The SSH private key must **not** be passphrase-protected. Upstream says password-protected SSH keys are not supported; it advises a dedicated age identity or an age plugin instead of stripping the passphrase from your normal key. See [[fnox/How To/Use Apple Secure Enclave Touch ID]] for the plugin route on a Mac.
	- ## Steps
		- ### 1. Collect public keys
			- Each person sends the contents of their SSH public key. It is safe to share.
			- ~~~bash
			  cat ~/.ssh/id_ed25519.pub
			  ~~~
		- ### 2. List them as recipients
			- In the project's `fnox.toml`:
			- ~~~toml
			  [providers.age]
			  type = "age"
			  recipients = [
			    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGQs...",  # alice
			    "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBws...",  # bob
			  ]
			  ~~~
			- Recipients are public. Never paste a private key into this field.
		- ### 3. Point fnox at your private key
			- ~~~bash
			  export FNOX_AGE_KEY_FILE=~/.ssh/id_ed25519
			  ~~~
			- Add the line to your shell profile to keep it.
		- ### 4. Add a secret and check it
			- ~~~bash
			  fnox set DATABASE_URL --provider age   # prompts with hidden input
			  fnox check --all
			  fnox exec -- npm start
			  ~~~
			- The value lands in `fnox.toml` as ciphertext, safe to commit.
		- ### 5. Commit
			- ~~~bash
			  git add fnox.toml
			  git commit -m "Add encrypted development secrets"
			  git push
			  ~~~
	- ## Scenarios
		- ### A person adds a secret
			- Run `fnox set API_KEY --provider age`, then commit `fnox.toml`. fnox encrypts to the current recipient list, so everyone listed can read it after pulling. No re-encryption step.
			- Someone who is not yet in the list cannot read the new value either, until scenario B.
		- ### A new team member joins
			- 1. They send their SSH public key.
			- 2. An existing member who can already decrypt adds it to `recipients`.
			- 3. That member re-encrypts everything, previewing first:
			- ~~~bash
			  fnox reencrypt -p age --dry-run
			  fnox reencrypt -p age
			  ~~~
			- 4. They commit and push. The new member pulls, sets `FNOX_AGE_KEY_FILE`, and runs `fnox get DATABASE_URL`.
			- Without step 3 the new person's key is listed but every existing secret is still locked to the old set. Run it once per profile, for example `fnox reencrypt -p age -P staging -f`.
		- ### A team member leaves
			- 1. Delete their line from `recipients`.
			- 2. Run `fnox reencrypt -p age` with an identity that can still decrypt, then commit and push. New commits are then encrypted without them.
			- 3. **Rotate the underlying secrets.** Removing a recipient cannot revoke access to ciphertext already in git history, and the leaver's key still decrypts those old commits. Upstream says to rotate the secret if access must end. The re-encryption changes the wrapping, not the secret's value.
			- Rotation sequence for each secret: change it at its source, `fnox set` the new value, commit.
		- ### Someone loses their SSH key
			- The same as a departure for that key, then the same as a join for their replacement key. Until the old key is removed and secrets rotated, whoever holds the lost key can decrypt history.
		- ### CI needs access
			- Give CI its own age key, not a person's SSH key. Generate it with `age-keygen -o ci-age.txt`, add the `age1...` public key to `recipients`, run `fnox reencrypt -p age`, and store the secret key in the CI system as `FNOX_AGE_KEY`.
	- ## Troubleshooting
		- `no identity matched any of the recipients`: the private key in use is not the pair of any listed recipient. Compare your public key with the `recipients` array.
		- `failed to decrypt`: `FNOX_AGE_KEY` and `FNOX_AGE_KEY_FILE` are both unset and there is no `age.txt` in the fnox config directory, or the file is unreadable.
		- An inline `FNOX_AGE_KEY` overrides the provider's `identity` and `key_file`. Unset it if you meant to use an SSH key file.
		- SSH key rejected: confirm the type is `ed25519` or `rsa` and the key has no passphrase.
	- ## Related
		- [[fnox/Golden Path]]: the alternative where a vault is the source of truth and each person keeps a personal encrypted cache.
		- [[fnox]]
