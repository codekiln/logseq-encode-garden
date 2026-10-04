# Remote asset credentials
	- Use [[fnox/Golden Path]] with a separate encrypted cache and identity for each persistent remote host. Keep B2 application keys in a vault; commit references in each garden's `fnox.toml`; keep `fnox.local.toml` and `assets/.remote/` gitignored. A remote host decrypts its own cache without asking the Mac for Touch ID.
	- The remote host needs an independent way to obtain its initial credentials. A cache removes repeated vault authentication after setup; cache refresh still needs access to the vault. A dedicated noninteractive vault identity can automate refresh later.
	- Pair the credential plan with [[GitP/A/Log/26/10/04 Sun/Dvc for Knowledge Gardens/Plan]]. fnox supplies credentials to an asset command; DVC tracks and transfers asset content.
	- ## Golden path and SSH
		- [[fnox/How To/Set Up a Project with age and SSH Keys]] supports using an SSH public key as an age recipient. The matching private key must be readable on the decrypting host. The native integration reads a key file and parses an SSH identity; it does not query `ssh-agent`. SSH login or forwarding an unlocked SSH agent therefore does not, by itself, let fnox decrypt. [fnox age identity loading](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/crates/fnox-core/src/providers/age.rs#L372)
			- [[My Note]] I'm a bit confused why [[fnox/How To/Set Up a Project with age and SSH Keys]] is referenced here, as that page is about "Commit secrets to a project as age ciphertext in `fnox.toml`," which is the opposite of the [[fnox/Golden Path]] in which you " Run [`fnox sync`](https://fnox.jdx.dev/guide/sync.html) to encrypt a personal copy into the gitignored `fnox.local.toml` using a local provider such as age." Are you referencing it for your own benefit, so that you're aware of it while making a plan? If so, that's a bit against [[My/AI/Rule/No Recipe in the Cake]].
		- Password-protected SSH private keys are unsupported by the documented integration. Use a dedicated native age identity for the remote host, stored outside the checkout with access restricted to the host's user. Keep the Mac's SSH login key and Secure Enclave identity on the Mac. [Supported SSH keys and passphrase limitation](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/providers/age.md#ssh-key-support)
		- A personal cache is encrypted to the selected provider's recipients. Copying a Mac cache to a remote host works only when the remote host has an identity for a recipient already included in that ciphertext. A cache encrypted solely to the Mac's Secure Enclave remains tied to that Mac. [Cache recipients and hardware identities](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/guide/sync.md#hardware-backed-decryption)
			- [[My Note]] why would I copy a mac cache to a remote host? Did I mention this? Also, "A personal cache is encrypted to the selected provider's recipients" is the opposite of clarity; please review [[My/AI/Rule/Prune useless commandments]], as "selected provider's recipients" is clearly out of scope here. I don't even know what you mean by recipient here, as the point here is for me and my agents to develop.
		- Prefer a distinct provider named `sync-remote-age` for each remote host's local configuration. Provider definitions replace one another as a whole during config merging, so a personal cache provider should have a separate name from any provider used for committed team ciphertext. [Cache configuration merging](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/guide/sync.md#what-it-looks-like)
			- [[My Note]] "personal cache provider" is so ambiguous here, what are you talking about?
	- ## Daemon
		- [[fnox/Daemon]] can reduce repeated decryption during a remote session. Its cache lives in memory, is lost at restart or idle expiry, and is served over a local Unix socket to the same user. Running the daemon on the Mac does not make it a remote credential service. [Daemon security and cache behavior](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/guide/daemon.md#security-model)
		- A daemon cache miss still needs a working provider or local age identity. Enable the daemon only after unattended direct resolution succeeds. Clear the daemon after rotating a key; remote vault changes do not automatically invalidate cached values. [Daemon setup and cache misses](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/guide/daemon.md#enable-it)
	- ## Garden isolation
		- Give each garden its own B2 bucket, scoped application key and vault item. A shared public bucket can use separate enforced prefixes when the bucket's privacy policy fits every object. Keep private recordings in the private garden's bucket; a name prefix alone does not give an object a private visibility policy.
		- Use a read-only key for inspection and a separately scoped read/write key for normal asset work. Full CRUD needs read, list, upload and deletion capabilities. B2 application keys enforce bucket and optional file-prefix restrictions; fnox profiles only select configuration. [B2 application-key restrictions](https://www.backblaze.com/docs/en/cloud-storage-application-keys)
		- B2 S3 credentials map the application key ID to `AWS_ACCESS_KEY_ID` and the application key to `AWS_SECRET_ACCESS_KEY`. Bucket-restricted integrations may need `listAllBucketNames`, which exposes account bucket names. Confirm the chosen client works with the proposed capability set before granting access. [B2 S3 application keys](https://www.backblaze.com/docs/cloud-storage-s3-compatible-app-keys)
			- [[My Question]]
				- TODO What does AWS have to do with B2 specifically for my use cases? I'm struggling to see how this is relevant to my use cases, which don't involve AWS at all. Also, I'm not seeing anything about `AWS_ACCESS_KEY_ID` in backblaze's docs outside of specifically using the [[AWS/CLI]] [here](https://www.backblaze.com/docs/en/cloud-storage-use-cli-to-create-an-application)
		- `writeFiles` permits S3 deletion by object name, which creates a hide marker; `deleteFiles` permits deleting a specific version. Omitting `deleteFiles` from an upload key therefore does not enforce a complete ban on deletion. Use separate cleanup credentials for deleting retained versions, and choose retention and lifecycle rules to protect recoverability. [B2 S3 deletion permissions](https://www.backblaze.com/docs/cloud-storage-s3-compatible-app-keys#app-key-restrictions)
		- Scope the remote host to the gardens it needs. Any process running as the same user with access to the age identity and encrypted cache can recover that host's credentials. Garden isolation comes from separate keys and B2 permissions; placing several providers in one user's fnox configuration does not isolate untrusted processes from one another.
	- ## Reusable configuration
		- In each garden, keep the same `assets` profile and secret names. Store the bucket, endpoint, DVC object-store prefix and optional public-media base URL as nonsecret project settings. A private garden's public-media base URL stays absent.
		- The following template describes vault items to create or select; placeholders must be replaced with actual metadata before use. Vault and item names in a public repository are visible metadata, so choose names suitable for publication.
			- ~~~toml
			  # fnox.toml — references committed per garden
			  [providers.asset-vault]
			  type = "1password"
			  vault = "<asset-vault>"
			  [profiles.assets.secrets]
			  AWS_ACCESS_KEY_ID = { provider = "asset-vault", value = "<garden-b2-item>/key-id", if_missing = "error" }
			  AWS_SECRET_ACCESS_KEY = { provider = "asset-vault", value = "<garden-b2-item>/application-key", if_missing = "error" }
			  ~~~
		- Remote host configuration belongs outside git:
			- ~~~toml
			  # ~/.config/fnox/config.toml — host-specific provider
			  [providers.sync-remote-age]
			  type = "age"
			  recipients = ["<remote-host-public-age-recipient>"]
			  key_file = "~/.config/fnox/remote-age.txt"
			  ~~~
		- Start asset commands with an explicit profile and fail on missing credentials. `--no-defaults` excludes unrelated top-level secrets from the selected profile. The caller must also supply a clean environment if inherited AWS credentials or unrelated secret variables would be a concern.
			- ~~~sh
			  fnox --non-interactive --no-daemon --no-defaults --profile assets --if-missing error exec -- dvc pull
			  fnox --non-interactive --no-daemon --no-defaults --profile assets --if-missing error exec -- dvc push
			  ~~~
		- DVC pulls selected tracked content into `assets/.remote`; the checkout may hold only part of the remote collection. DVC content-addressed storage and a public named-media area need distinct prefixes. Deleting a local proxy does not delete the corresponding stored object. DVC garbage collection and public-object deletion need explicit cleanup commands and credentials.
	- ## Set up a persistent remote host
		- Generate a dedicated age identity on the remote host, with its private file accessible only to that user. Share the public recipient with the operator who can authenticate to the vault. Install compatible fnox and the asset client on the remote host.
		- On the operator's machine, use a separate clean checkout of the target garden and configure `sync-remote-age` with the remote public recipient. Age encryption needs the public recipient; the remote private identity remains on the remote host. Authenticate to the vault and create a cache for the asset profile:
			- ~~~sh
			  fnox --profile assets --no-defaults sync --provider sync-remote-age --local-file AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY
			  ~~~
		- Transfer only the resulting encrypted `fnox.local.toml` to that garden's remote checkout through an authenticated channel. The remote host's `sync-remote-age` provider points at the matching local private identity. Repeat for each authorized garden; use a different identity for a different remote host.
		- Test from a fresh remote session with vault authentication absent and daemon disabled. The remote asset command should resolve the cache, restart successfully and work without a Mac prompt. Validate a scratch object's upload, listing, download, checksum, replacement and deletion inside a temporary prefix before allowing work on existing assets.
		- Refresh the cache from its original vault references after rotation, then transfer the replacement ciphertext and clear any remote daemon cache. `fnox sync --local-file --force` reads the original source rather than reusing the old local sync value. [Refresh implementation](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/src/commands/sync.rs#L64)
	- ## Ephemeral remote agents
		- For a host that is recreated frequently, inject a narrowly scoped 1Password service-account token through the runner's secret store and let fnox resolve vault references directly. This makes vault refresh independent of Mac Touch ID, but adds a credential whose vault access must be restricted. [fnox unattended 1Password authentication](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/providers/1password.md#ci-and-automation)
			- [[My Note]] In my consumer plan, I do not have access to [[1Password Service Accounts]]. I know they can be used but they are useless to me. They are only available on 1Password Business and similar accounts.
		- An alternative is an encrypted cache delivered with a dedicated runner age identity through the runner's secret store. A ciphertext file and its private identity should travel through separately controlled channels. The runner still needs a credential delivery mechanism; storing the age private key beside ciphertext in a repository would erase the protection.
		- 1Password Environment mounts and fnox's 1Password CLI vault provider are different interfaces. The proposed vault path assumes suitable vault items exist; adopting fnox does not automatically convert an Environment mount into vault references.
	- ## Rotation and retirement
		- Rotate the underlying B2 application key when access must end. Removing an age recipient and reencrypting cannot revoke credentials already decrypted or old ciphertext already copied. Revoke the old B2 key, update the vault reference or value, replace authorized host caches and clear daemon caches. [Age recipient changes](https://github.com/jdx/fnox/blob/addc5d139e142e3270b8d43b276c852f84ef460a/docs/providers/age.md#usage-notes)
			- [[My Note]] I'm struggling with understanding why this paragraph is here and the perspective it is coming from, as I I'm not suggesting in any way using age in the committed assets; I'm only interested in using age for the gitignored local cache in `fnox.local.toml`.
		- Cache freshness needs an explicit routine: refresh after key rotation and before an extended unattended work period. A sync cache remains unchanged until refreshed; encryption does not impose an expiry on the B2 key.
	- ## Pilot
		- TODO Choose the initial persistent remote host, the asset vault and a bucket-scoped pilot key for `logseq-encode-garden`.
		- TODO Repeat the public-recipient cache test with the chosen remote host's native age identity before storing live credentials on that host.
		- TODO Run the scratch-prefix CRUD test through the selected DVC/B2 client and verify requests to another garden are denied.
		- TODO Test explicit Logseq links to `assets/.remote`, hidden-file search and partial-checkout behavior before using local proxies across the gardens.
		- TODO Choose B2 retention and cleanup rules, then repeat the same profile and cache setup for the private garden and other gardens.
	- ## Disposable test
		- A synthetic B2-shaped credential pair was synced to a cache using only a newly generated remote SSH public recipient. The remote private identity stayed in the simulated remote directory. The operator encrypted without a private identity.
		- A separate remote checkout decrypted the transferred cache through `fnox exec` with daemon disabled and the original provider deliberately made unusable. A fresh subprocess repeated the successful decryption; removing the cache caused the command to fail. The test used `fnox 1.36.0` and a passphrase-free disposable Ed25519 key; all disposable files were removed.
		- This demonstrates the cache-transfer mechanism locally. Native age identities, an actual remote host, real vault references, B2 capabilities and the selected asset client still need the pilot tests.
	- ## Source review
		- The local fnox repository was fetched to [v1.37.0 release — addc5d1](https://github.com/jdx/fnox/commit/addc5d139e142e3270b8d43b276c852f84ef460a). The age, sync, golden-path and daemon documentation is unchanged from the local checkout reviewed. The installed CLI reports `fnox 1.36.0`; its help exposes the command flags used in the examples. Live credential delivery and B2 access still need the pilot tests.