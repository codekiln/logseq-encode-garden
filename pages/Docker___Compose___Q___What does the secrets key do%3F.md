logseq-entity:: [[Logseq/Entity/Question]]
- # What does the `secrets` key do in [[Docker/Compose]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Compose file: secrets reference](https://docs.docker.com/reference/compose-file/secrets/) and [How to use secrets in Compose](https://docs.docker.com/compose/how-tos/use-secrets/).
		- **Short answer:** `secrets` lets you hand sensitive data (passwords, tokens, TLS keys) to a service as a read-only file mounted at `/run/secrets/<name>`, instead of baking it into the image or exposing it through environment variables and the compose file itself.
		- ### Two levels
			- **Top-level `secrets:`** declares each secret and where its value comes from.
			- **Service-level `secrets:`** grants a specific service access to declared secrets; only granted services can read them.
		- ### Where a secret's value comes from (top-level source)
			- `file:` — read the value from a file on the host.
			- `environment:` — read the value from an environment variable (Compose Spec).
			- `external: true` — the secret already exists in the platform (e.g. pre-created, Swarm) and Compose does not create it.
		- ### How a service consumes it
			- **Short syntax** grants access and mounts at the default path: `secrets: [db_password]` → available in the container as `/run/secrets/db_password`.
			- **Long syntax** overrides mount details: `source`, `target` (custom path/filename), `uid`, `gid`, `mode`.
		- ### Example
			- ~~~yaml
			  services:
			    db:
			      image: postgres
			      environment:
			        POSTGRES_PASSWORD_FILE: /run/secrets/db_password
			      secrets:
			        - db_password
			  secrets:
			    db_password:
			      file: ./db_password.txt
			  ~~~
		- ### Why use it
			- Keeps secrets out of image layers and out of `docker inspect`/env output.
			- The container reads the value from a file (many images support a `*_FILE` convention), so the plaintext never lands in the compose file or shell history.
