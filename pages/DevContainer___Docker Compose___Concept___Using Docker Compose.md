tags:: [[DevContainer]], [[Docker]], [[Docker/Compose]], [[Diataxis/Explanation]]

- # Using Docker Compose with DevContainers Conceptual Overview
	- ## Overview
		- Dev Containers supports Docker Compose for managing multi-container development environments, allowing developers to reference existing `docker-compose.yml` files and extend them with development-specific configurations.
		- This enables seamless integration between production Docker Compose configurations and development container setups without modifying production files.
	- ## Context
		- Many projects already use Docker Compose to define their multi-container production environments.
		- Developers need to add development-specific configurations (like volume mounts, debugging capabilities, and extended runtime configurations) without altering production compose files.
		- Docker Compose's override mechanism provides a clean way to layer development configurations on top of production setups.
	- ## Key Principles
		- **Production File Preservation**: Never modify production `docker-compose.yml` files for development purposes.
			- Keep production and development configurations separate to avoid accidental changes to production environments.
		- **Sequential File Processing**: VS Code processes Docker Compose files in the order specified in `dockerComposeFile` array.
			- Later files override or supplement earlier configurations through Docker Compose's native merge behavior.
		- **Service Selection**: The `service` property in `devcontainer.json` specifies which service from the compose file to use as the dev container.
			- VS Code automatically starts or attaches to the specified service when reopening in a container.
		- **Workspace Mapping**: The `workspaceFolder` property defines where source code is mounted inside the container.
			- This typically corresponds to a volume mount defined in the compose file.
	- ## Mechanism
		- **Basic Configuration**:
			- Define `dockerComposeFile` and `service` properties in `devcontainer.json`:
				- ~~~json
				  {
				    "dockerComposeFile": "../docker-compose.yml",
				    "service": "service-name",
				    "workspaceFolder": "/workspace/path"
				  }
				  ~~~
		- **Using Override Files**:
			- Create development-specific override file (e.g., `.devcontainer/docker-compose.extend.yml`):
				- ~~~yaml
				  version: '3'
				  services:
				    your-service:
				      volumes:
				        - .:/workspace:cached
				      command: /bin/sh -c "while sleep 1000; do :; done"
				  ~~~
			- Reference both files in order in `devcontainer.json`:
				- ~~~json
				  {
				    "dockerComposeFile": [
				      "../docker-compose.yml",
				      "docker-compose.extend.yml"
				    ],
				    "service": "your-service",
				    "workspaceFolder": "/workspace"
				  }
				  ~~~
		- **Processing Order**:
			- 1. VS Code reads the base `docker-compose.yml` file
			- 2. VS Code applies configurations from `docker-compose.extend.yml` (or other override files)
			- 3. Later configurations override or supplement the primary composition
			- 4. The specified service is started or attached to
	- ## Examples
		- **Basic Multi-Container Setup**:
			- Base production `docker-compose.yml`:
				- ~~~yaml
				  version: '3'
				  services:
				    app:
				      image: node:18
				      ports:
				        - "3000:3000"
				    db:
				      image: postgres:15
				      environment:
				        POSTGRES_PASSWORD: secret
				  ~~~
			- Development override `.devcontainer/docker-compose.extend.yml`:
				- ~~~yaml
				  version: '3'
				  services:
				    app:
				      volumes:
				        - ..:/workspace:cached
				      command: /bin/sh -c "while sleep 1000; do :; done"
				      # Keep container alive for development
				  ~~~
			- DevContainer configuration `.devcontainer/devcontainer.json`:
				- ~~~json
				  {
				    "dockerComposeFile": [
				      "../docker-compose.yml",
				      "docker-compose.extend.yml"
				    ],
				    "service": "app",
				    "workspaceFolder": "/workspace",
				    "postCreateCommand": "npm install"
				  }
				  ~~~
		- **Service Networking**:
			- Services on the same Docker Compose network can access each other by service name:
				- The `app` service can connect to PostgreSQL at `db:5432`
			- Use `network_mode: service:db` for localhost access between services:
				- ~~~yaml
				  services:
				    app:
				      network_mode: service:db
				  ~~~
	- ## Best Practices
		- **Volume Mounts**:
			- Use bind mounts to map local source code into the container:
				- ~~~yaml
				  volumes:
				    - ..:/workspace:cached
				  ~~~
			- The `:cached` flag improves performance on macOS and Windows.
		- **Non-Root Users on Linux**:
			- Specify non-root users to prevent file permission issues:
				- ~~~yaml
				  user: "1000:1000"
				  ~~~
		- **Development Entry Points**:
			- Avoid production entry points that exit prematurely
			- Use sleep loops or long-running commands during development:
				- ~~~yaml
				  command: /bin/sh -c "while sleep 1000; do :; done"
				  ~~~
		- **Install Development Dependencies**:
			- Use `postCreateCommand` in `devcontainer.json` to install dependencies after container creation:
				- ~~~json
				  {
				    "postCreateCommand": "npm install && npm run setup"
				  }
				  ~~~
	- ## Misconceptions
		- **Override files replace the base file** → **False**. Override files supplement and extend the base configuration through Docker Compose's merge behavior.
		- **All services in the compose file are started** → **False**. Only the specified service and its dependencies are started.
		- **Production compose files must be modified for development** → **False**. Use override files to keep production configurations pristine.
		- **Volume mounts are automatic** → **False**. You must explicitly define volume mounts in your compose or override files.
	- ## Related
		- [[DevContainer]]
		- [[DevContainer/Docker Compose/How To/Create Override File]]
		- [[DevContainer/Feature/Concept/Docker Build Order]]
		- [[Docker/Compose/How To/Remove Volumes]]
