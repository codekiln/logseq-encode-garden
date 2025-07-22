tags:: [[Diataxis/Explanation]]

- # COMPOSE_BAKE=true vs explicit Buildx/Bake
	- ## Overview
		- `COMPOSE_BAKE=true` makes `docker compose build` delegate image builds to **Buildx Bake**, gaining BuildKit speed without leaving the Compose UX.
	- ## Context
		- Developers favour a one-liner like `docker compose build`; CI pipelines need deterministic, cache-efficient, multi-platform builds and precise control.
	- ## Key Principles
		- **Ergonomics first** – favour the simplest command locally.
		- **Explicit in CI** – prefer repeatability and full control.
		- **Single source of truth** – reuse the same Compose or Bake definitions everywhere.
	- ## Mechanism
		- With the variable set, Compose converts each service’s *build* section into a Bake target and runs `docker buildx bake`.
		- Bake inherits BuildKit: parallel DAGs, cross-arch, secrets, and cache import/export.
		- Without the flag, Compose loops over services sequentially, missing cross-service cache and multi-arch output.
	- ## When to Use
		- ### Local Development
			- ✅ Instant speed-up; no new commands to learn.
			- ✅ Retains familiar `docker compose build`.
			- ⚠️ Occasional stale-image quirks after `docker compose up --build`.
		- ### Continuous Integration
			- ❌ **Skip `COMPOSE_BAKE=true`**; invoke Buildx/Bake directly.
			- ✅ Official Buildx/Bake actions expose caching, secrets, platforms, registry login.
			- ✅ Use an explicit `docker-bake.hcl`, or reuse `compose.yaml` via `docker buildx bake --files compose.yaml`.
	- ## Examples
		- ~~~bash
		  # Local workstation
		  COMPOSE_BAKE=true docker compose build
		  
		  # GitHub Actions snippet pushing to ECR
		  - uses: aws-actions/configure-aws-credentials@v4
		  - uses: aws-actions/amazon-ecr-login@v2
		  - uses: docker/setup-buildx-action@v3
		  - uses: docker/build-push-action@v6
		    with:
		      file: Dockerfile
		      platforms: linux/amd64,linux/arm64
		      push: true
		      tags: ${{ steps.login-ecr.outputs.registry }}/my-app:latest
		      cache-from: type=gha
		      cache-to: type=gha,mode=max
		  ~~~
	- ## Misconceptions
		- *“The flag is required for Buildx.”* → Buildx can be called directly; the flag is only a convenience wrapper.
		- *“Compose+Bake in CI is identical to direct Buildx.”* → Delegation hides flags and has open bugs; explicit Buildx remains more predictable.
	- ## Related
		- [Docker Compose build documentation](https://docs.docker.com/compose/compose-file/build/)
		- [Buildx Bake documentation](https://docs.docker.com/build/bake/)
		- [docker/build-push-action](https://github.com/docker/build-push-action)