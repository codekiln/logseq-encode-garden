tags:: [[Diataxis/How To]]

- # How To Remove [[Docker/Volume]]s when using [[Docker/Compose]]
	- ## Goal
		- Remove all volumes managed by the current Docker Compose project while leaving external volumes and bind mounts intact.
	- ## Preconditions
		- Docker Engine ≥ 20.10 and Docker Compose plugin (v2) installed.
		- Terminal opened in the directory containing `docker-compose.yml`.
	- ## Procedure
		- ### 1. Stop & Remove Containers
			- ~~~bash
			  docker compose down
			  ~~~
		- ### 2. Remove Named & Anonymous Volumes
			- ~~~bash
			  docker compose down --volumes
			  ~~~
			- Deletes every volume created by this Compose project unless the volume is declared with `external: true`.
		- ### 3. Remove Orphan Containers (optional)
			- ~~~bash
			  docker compose down --volumes --remove-orphans
			  ~~~
			- Cleans up any containers left from previous runs that are no longer defined in the compose file.
		- ### 4. Verify Volume Removal
			- ~~~bash
			  docker volume ls
			  ~~~
			- Project-specific volumes should no longer appear in the list.
	- ## Troubleshooting
		- **Volume still exists** → Check the compose file for `external: true`; Compose will never delete external volumes.
		- **Avoid data loss** → Back up a volume before deletion:
			- ~~~bash
			  docker run --rm -v myvol:/data -v "$PWD":/backup alpine tar -czf /backup/myvol.tgz /data
			  ~~~
	- ## References
		- [Docker Compose CLI reference — down](https://docs.docker.com/compose/reference/down/)
		- [Compose file reference — volumes.external](https://docs.docker.com/compose/compose-file/compose-file-v3/#external)