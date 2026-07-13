logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Docker/Compose/Q/What does the secrets key do?]]
- # In [[Docker/Compose]], is it ever appropriate or secure to use a build arg for a secret instead of BuildKit secrets?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Dockerfile `ARG` reference](https://docs.docker.com/reference/dockerfile/#arg) and [Build secrets](https://docs.docker.com/build/building/secrets/).
		- **Short answer:** No — a build `ARG` is never a secure way to pass a secret. Its value is baked into the image metadata and recoverable with `docker history`, so it leaks to anyone who can pull the image. Use BuildKit build secrets (`RUN --mount=type=secret=...`) for anything sensitive. Build args are appropriate only for **non-secret** build-time configuration.
		- ### Why a build arg is insecure for secrets
			- The Docker docs warn directly against it: build-time variable values are visible to any user of the image via `docker history`.
			- Even if you never reference the `ARG` in the final image, the value persists in the build cache and layer metadata of the stage where it was set.
			- `--build-arg` values can also show up in shell history and CI logs.
		- ### Why BuildKit secrets are the secure alternative
			- `RUN --mount=type=secret=id=mysecret,...` mounts the secret as a file (default `/run/secrets/<id>`) **only for the duration of that `RUN` step**.
			- The secret is not written to any image layer, not stored in image history, and not left in the build cache.
			- In Compose this is wired via a service's `build.secrets` referencing top-level `secrets` (see [[Docker/Compose/Q/What does the secrets key do?]]).
		- ### Narrow cases where a build arg is defensible
			- **Non-sensitive config** — versions, feature flags, base-image tags, locales. This is what `ARG` is for.
			- **Low-value or throwaway secrets** on a purely local image that is never pushed or shared — the leak surface is smaller, but the value is still in history, so this is "less bad," not secure.
			- A multi-stage build that consumes the arg only in an early stage and copies just the artifact forward reduces exposure in the **final** image, but the secret still lives in that intermediate stage's layers/cache. Not a substitute for BuildKit secrets.
		- **Bottom line:** treat "build arg for a secret" as a code smell. If the value must stay confidential, use a BuildKit secret; reserve `ARG` for configuration you would be comfortable printing in `docker history`.
