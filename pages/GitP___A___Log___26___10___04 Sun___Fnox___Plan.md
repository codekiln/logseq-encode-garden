# B2 access while working away from the Mac
	- Use [[fnox/Golden Path]] on the Mac where Codex and Claude already run. Keep each garden's Backblaze application keys in [[1Password]], and let fnox read an encrypted local copy during asset work. Creating or refreshing that copy requires 1Password authentication; using it can work while the Mac is unattended.
	- ## How it works
		- In each garden, `fnox.toml` names the 1Password item containing that garden's B2 credentials. Git tracks these references so every agent uses the same configuration.
		- After signing in to 1Password on the Mac, run `fnox sync` to create `fnox.local.toml`. This gitignored file holds the encrypted copy of the credentials.
		- Configure fnox to decrypt with an ordinary age key file on the Mac. Age uses a public key to encrypt the cache and a private key to open it. The private key file gives the local agent access without a Touch ID prompt.
		- When an agent runs an asset command through `fnox exec`, fnox decrypts the cached credentials and supplies them to that command. Codex and Claude use the same files and commands, including when their processes are controlled remotely. [Fnox's cache guide](https://fnox.jdx.dev/guide/sync.html) explains how `fnox.local.toml` takes precedence over vault reads.
	- ## B2 credentials
		- [[GitP/A/Log/26/10/04 Sun/Dvc for Knowledge Gardens/Plan]] proposes DVC for transferring selected assets between B2 and `assets/.remote/`. Fnox supplies the credentials; DVC handles the files.
		- DVC connects to B2 through B2's S3-compatible interface, which accepts the request format used by Amazon S3 clients. Configure DVC with the Backblaze endpoint. The storage remains in Backblaze, and this setup requires no AWS account or AWS CLI. [DVC's compatible-server configuration](https://doc.dvc.org/user-guide/data-management/remote-storage/amazon-s3#s3-compatible-servers-non-amazon) describes the endpoint setting.
		- For DVC, name the credential entries `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`: their values are the B2 application key ID and B2 application key. DVC expects these environment-variable names even when it connects to Backblaze. [Backblaze's integration guide](https://www.backblaze.com/docs/en/cloud-storage-get-started-with-a-backblaze-integration) documents this mapping.
	- ## Set up the Mac
		- Follow [[fnox/Golden Path]] to create an age key file and a global provider named `sync-age` in `~/.config/fnox/config.toml`. Use file-based decryption for the asset cache so commands can run while nobody is at the keyboard.
		- Protect the private key file with permissions that allow only the Mac account running the agents to read it. That account can recover the cached B2 credentials, so give the agents B2 keys limited to the garden assets they need.
		- Store each garden's B2 application key ID and application key in a 1Password vault item. Fnox's 1Password provider reads vault items through the `op` CLI; an existing 1Password Environment mount needs corresponding vault-item references for this setup.
		- [The garden fnox configuration](https://github.com/codekiln/logseq-encode-garden/blob/main/fnox.toml) defines an `assets` profile using the supplied B2 key ID and application-key references. Secret values remain in 1Password; missing credentials stop the command.
		- Add `fnox.local.toml` and `assets/.remote/` to `.gitignore`. Keep the bucket name and storage endpoint as ordinary project settings.
		- From that garden's checkout, authenticate to 1Password and create the cache:
			- ~~~sh
			  fnox --profile assets --no-defaults sync --provider sync-age --local-file
			  ~~~
		- The `assets` profile selects the garden's asset credentials. `--no-defaults` leaves unrelated top-level fnox secrets out of the command. The same Mac-wide age key can decrypt separate caches in each garden.
	- ## Run asset commands
		- Once the DVC remote and cache are configured, an agent can fetch or upload tracked assets:
			- ~~~sh
			  fnox --profile assets --no-defaults exec -- dvc pull
			  fnox --profile assets --no-defaults exec -- dvc push
			  ~~~
		- Agents should use the same garden asset mise tasks whether controlled locally or remotely. Each garden supplies its own bucket settings and credentials; the task names and arguments stay consistent.
	- ## Refresh access
		- After changing a B2 key, update its 1Password item and refresh the affected garden's cache while authenticated:
			- ~~~sh
			  fnox --profile assets --no-defaults sync --provider sync-age --local-file --force
			  ~~~
		- Fnox keeps using the cached value until the cache is refreshed. Revoking the old application key in Backblaze ends its storage access. [Fnox's refresh guide](https://fnox.jdx.dev/guide/sync.html#refreshing-the-cache) describes rereading the vault values.
	- ## Try it on one garden
		- DONE Set up [the garden vault references](https://github.com/codekiln/logseq-encode-garden/blob/main/fnox.toml) and the encrypted local cache on the Mac. B2 authorization identifies `logseq-encode-garden` as the key’s allowed bucket; the key has access throughout that bucket.
		- DONE Read credentials from fresh processes with the 1Password CLI blocked and the fnox daemon disabled. The reads used the age-encrypted cache and required no vault authentication.
		- DONE Upload, list, download, compare, replace, and delete a disposable file through the B2 API. The test used a unique name under `gitpa/tests/`; all versions created by the test were deleted.
		- DOING Apply [the tested fnox configuration](https://github.com/codekiln/logseq-encode-garden/blob/main/fnox.toml) to the [private knowledge garden](https://github.com/codekiln/logseq-garden) once its private recording bucket and application key exist. Supply that garden’s vault references so rough recordings remain in private storage.
			- DOING create a mise file task in the private knowledge garden which will use the Backblaze Administration logseq environment to create the appropriate keys and store them in 1password without exposing them to you or anyone using the op cli. Make it easy for me. Remember you have access to onepassword environments mcp as well as op cli. I already mounted `~/ghq/github.com/codekiln/logseq-garden/.env` with backblaze admin there.
			  id:: 6ac29dea-d7c5-4079-9cd0-ec0c7f6c699e
		- The Mac trial used the supplied vault references and a native age key file. DVC transfer and restore are the next trial in [[GitP/A/Log/26/10/04 Sun/Dvc for Knowledge Gardens/Plan]].