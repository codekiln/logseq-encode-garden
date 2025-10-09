# Conceptual overview of issues with using pnpm in devcontainers
- # Common Issues and Patterns
	- ## Store Path Problems
		- **Issue**: pnpm creates store inside project directory when host and container filesystems differ
		- **Root Cause**: pnpm uses hard links, which don't work across different filesystems
		- **Impact**: Breaks pnpm's efficiency and can cause permission issues
	- ## OS Compatibility Issues
		- **Issue**: Compiled dependencies vary between different OS versions
		- **Impact**: Dependencies compiled for one OS may not work in another
		- **Solution**: Separate store directories per OS version
	- ## Permission Problems
		- **Issue**: EACCES errors when creating symlinks in mounted volumes
		- **Common Error**: `EACCES: permission denied, symlink '../../../apps/kebricide' -> '/app/node_modules/.pnpm/node_modules/kebricide'`
		- **Cause**: File system permissions between host and container
- # Successful Patterns and Solutions
	- ## Pattern 1: Container-Only Store Directory
		- **Approach**: Set pnpm store directory within container filesystem
		- **Configuration**:
		  ```json
		  {
		  "postCreateCommand": "pnpm config set store-dir /home/vscode/.pnpm-store && pnpm install --frozen-lockfile"
		  }
		  ```
		- **Benefits**: Avoids cross-filesystem hard link issues
		- **Trade-off**: No shared cache between containers
	- ## Pattern 2: Shared Store with Volume Mounting
		- **Approach**: Mount host pnpm store into container
		- **Configuration**:
		  ```yaml
		  volumes:
		  - ${HOME}/.local/share/pnpm:/home/node/.local/share/pnpm:cached
		  ```
		- **Benefits**: Shared cache, reduced downloads
		- **Requirements**: Pre-create store directory on host
	- ## Pattern 3: Multi-Stage Docker Builds
		- **Approach**: Separate dependency installation and build stages
		- **Configuration**:
		  ```dockerfile
		  FROM node:20-slim AS base
		  ENV PNPM_HOME="/pnpm"
		  ENV PATH="$PNPM_HOME:$PATH"
		  RUN corepack enable
		  
		  FROM base AS deps
		  RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
		  
		  FROM base AS build
		  RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
		  RUN pnpm run build
		  ```
		- **Benefits**: Optimized image size, cached builds
	- ## Pattern 4: DevContainer Features Integration
		- **Approach**: Use official DevContainer features
		- **Configuration**:
		  ```json
		  {
		  "features": {
		  	"ghcr.io/devcontainers/features/node:1": {
		  		"version": "18",
		  		"packageManager": "pnpm"
		  	}
		  }
		  }
		  ```
		- **Benefits**: Standardized setup, maintained by community
	- ## Pattern 5: Corepack Integration
		- **Approach**: Use Node.js built-in corepack for pnpm management
		- **Configuration**:
		  ```dockerfile
		  FROM node:20-slim
		  ENV PNPM_HOME="/pnpm"
		  ENV PATH="$PNPM_HOME:$PATH"
		  RUN corepack enable
		  ```
		- **Benefits**: Version consistency, automatic pnpm installation
- # Searching for Examples of Repositories Using pnpm in Docker or DevContainers
	- ## Improved Search Strategy (Two-Phase Pipeline)
		- **Phase 1**: Find repositories with devcontainer configurations using code search API
		- **Phase 2**: Verify pnpm usage by cloning and examining files
		- **Why**: Separates discovery from verification, avoiding impossible single-query constraints
		- **Commands Used**:
			```bash
			# Phase 1: Find devcontainer repositories
			gh api -X GET search/code -f q='filename:devcontainer.json' -f per_page=100
			gh api -X GET search/code -f q='devcontainer.json corepack enable' -f per_page=50
			gh api -X GET search/code -f q='devcontainer.json "pnpm install"' -f per_page=20
			
			# Phase 2: Clone and verify pnpm usage
			gh repo clone REPO_NAME -- --depth 1
			find . -name "pnpm-lock.yaml" -o -name "pnpm-workspace.yaml" -o -name "package.json"
			```
	- ## Search Results Summary (Updated)
		- **Total repositories examined**: 50+ repositories with devcontainer configurations
		- **Repositories with confirmed pnpm + devcontainer usage**: 3 high-quality examples
		- **Repositories with 1000+ stars**: 1 (QwikDev/qwik with 20k+ stars)
		- **Repositories with 100+ stars**: 1 (p-s-dev/typescript-nestjs-langgraph-ollama)
		- **Key finding**: While few repositories combine pnpm with devcontainer, the ones that do follow excellent patterns
	- ## High-Quality Examples Found
		- [QwikDev/qwik](https://github.com/QwikDev/qwik) - The HTML-first framework (20k+ stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 1 (Container-Only Store) + Pattern 3 (Multi-Stage Docker Builds)
			- **Implementation**: 
				- Uses `corepack enable --install-directory ~/bin` in Dockerfile
				- Sets `pnpm config set store-dir /home/circleci/store` for container-only store
				- Uses `updateContentCommand: "corepack prepare & pnpm install"` in devcontainer.json
				- Comprehensive monorepo with workspace protocol (`"packageManager": "pnpm@10.14.0"`)
			- **Files**: [devcontainer.json](https://github.com/QwikDev/qwik/blob/main/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/QwikDev/qwik/blob/main/.devcontainer/Dockerfile) | [package.json](https://github.com/QwikDev/qwik/blob/main/package.json)
		- [p-s-dev/typescript-nestjs-langgraph-ollama](https://github.com/p-s-dev/typescript-nestjs-langgraph-ollama) - NestJS with LangGraph and Ollama (100+ stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 4 (DevContainer Features)
			- **Implementation**:
				- Uses `postCreateCommand: "corepack enable && corepack prepare pnpm@latest --activate && pnpm install"`
				- Leverages DevContainer features for Node.js setup
				- Sets `"packageManager": "pnpm@8.15.0"` in package.json
				- Custom Dockerfile with `ENV PNPM_HOME=/usr/local/share/pnpm` and `ENV PATH=$PNPM_HOME:$PATH`
			- **Files**: [devcontainer.json](https://github.com/p-s-dev/typescript-nestjs-langgraph-ollama/blob/main/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/p-s-dev/typescript-nestjs-langgraph-ollama/blob/main/.devcontainer/Dockerfile) | [package.json](https://github.com/p-s-dev/typescript-nestjs-langgraph-ollama/blob/main/package.json)
		- [jkomyno/pnpm-monorepo-template](https://github.com/jkomyno/pnpm-monorepo-template) - Opinionated Node.js monorepo with pnpm, turborepo, vitest (57 stars)
			- **Pattern**: Pattern 3 (Multi-Stage Docker Builds) + Pattern 5 (Corepack Integration) + Pattern 1 (Container-Only Store)
			- **Implementation**: 
				- Multi-stage Dockerfile with `RUN --mount=type=cache,id=pnpm-store,target=/root/.pnpm-store npm i -g pnpm@${PNPM_VERSION}`
				- Uses BuildKit cache mounts for pnpm store optimization
				- Comprehensive monorepo setup with workspace configuration
			- **Files**: [Dockerfile.pnpm](https://github.com/jkomyno/pnpm-monorepo-template/blob/main/Dockerfile.pnpm) | [package.json](https://github.com/jkomyno/pnpm-monorepo-template/blob/main/package.json)
	- ## Additional Examples (Smaller Repositories)
		- [nafnix/pnpm-devcontainer](https://github.com/nafnix/pnpm-devcontainer) - PNPM 开发容器 (0 stars)
			- **Pattern**: Pattern 1 (Container-Only Store Directory)
			- **Implementation**: Uses `pnpm config set store-dir /home/vscode/.pnpm-store` in postCreateCommand
			- **Files**: [devcontainer.json](https://github.com/nafnix/pnpm-devcontainer/blob/master/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/nafnix/pnpm-devcontainer/blob/master/.devcontainer/Dockerfile)
		- [p-buddy/pnpm-devcontainer-template](https://github.com/p-buddy/pnpm-devcontainer-template) - Template repository (0 stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 1 (Container-Only Store)
			- **Implementation**: Uses `RUN corepack enable` with `ENV PNPM_HOME="/pnpm"` and `ENV PATH="$PNPM_HOME:$PATH"`
			- **Files**: [devcontainer.json](https://github.com/p-buddy/pnpm-devcontainer-template/blob/main/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/p-buddy/pnpm-devcontainer-template/blob/main/.devcontainer/Dockerfile)
		- [aj007-art/ts-template](https://github.com/aj007-art/ts-template) - TypeScript starter with ESLint+Prettier, tsx, pnpm, devcontainer (0 stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 4 (DevContainer Features)
			- **Implementation**: Uses corepack for pnpm installation combined with DevContainer features
			- **Files**: [devcontainer.json](https://github.com/aj007-art/ts-template/blob/main/.devcontainer/devcontainer.json) *(No Dockerfile - uses base image)*
	- ## Anti-Patterns Found
		- **Mismatched Package Managers**: Some repositories have `pnpm install` in devcontainer.json but actually use npm/yarn (e.g., ant-design/ant-design)
		- **Missing Store Configuration**: Several repositories use pnpm without configuring store directory, leading to potential cross-filesystem issues
		- **Incomplete Corepack Setup**: Some repositories enable corepack but don't properly configure PNPM_HOME environment variable
- # Best Practices Summary (Updated with Real Examples)
	- ## Store Management
		- **Container-Only Store** (Recommended for most cases): Set `pnpm config set store-dir /path/in/container` to avoid cross-filesystem issues
		- **Shared Store with Volume Mounting**: Mount host pnpm store for efficiency in CI/CD environments
		- **Avoid Cross-Filesystem Store Locations**: Never use host-mounted directories as pnpm store without proper volume mounting
	- ## Installation Methods (Ranked by Quality)
		- **Corepack Integration** (Best Practice): Use `corepack enable` + `corepack prepare pnpm@latest --activate` for version consistency
		- **DevContainer Features**: Leverage `ghcr.io/devcontainers/features/node:1` with `packageManager: "pnpm"` option
		- **Manual Installation**: Only when corepack is not available, use `npm i -g pnpm@VERSION`
	- ## Environment Configuration
		- **PNPM_HOME**: Always set `ENV PNPM_HOME=/usr/local/share/pnpm` (or similar path)
		- **PATH Configuration**: Add `ENV PATH=$PNPM_HOME:$PATH` to make pnpm available globally
		- **Package Manager Field**: Always specify `"packageManager": "pnpm@VERSION"` in package.json
	- ## Build Optimization (Production-Ready Patterns)
		- **Multi-Stage Builds**: Separate dependency installation from application build
		- **BuildKit Cache Mounts**: Use `--mount=type=cache,id=pnpm,target=/pnpm/store` for Docker layer caching
		- **Frozen Lockfile**: Always use `--frozen-lockfile` for consistent, reproducible builds
	- ## Development Workflow
		- **PostCreateCommand**: Use `corepack enable && corepack prepare pnpm@latest --activate && pnpm install`
		- **UpdateContentCommand**: For monorepos, use `corepack prepare & pnpm install` to handle workspace updates
		- **OS Compatibility**: Handle different OS versions with separate store directories when needed
	- ## Monorepo Considerations
		- **Workspace Protocol**: Use `workspace:^` for local package references
		- **Store Optimization**: Configure store directory early in container lifecycle
		- **Parallel Installation**: Leverage pnpm's parallel installation capabilities with `--parallel` flag
- # Canonical Examples (Copy-Paste Ready)
	- ## Example 1: Simple DevContainer with Corepack (Recommended)
		- **Use Case**: Single-package projects, TypeScript/JavaScript applications
		- **devcontainer.json**:
		  ```json
		  {
		    "name": "Node.js with pnpm",
		    "image": "mcr.microsoft.com/devcontainers/typescript-node:1-22-bookworm",
		    "features": {
		      "ghcr.io/devcontainers/features/node:1": {
		        "version": "22",
		        "packageManager": "pnpm"
		      }
		    },
		    "postCreateCommand": "corepack enable && corepack prepare pnpm@latest --activate && pnpm install",
		    "customizations": {
		      "vscode": {
		        "extensions": [
		          "dbaeumer.vscode-eslint",
		          "esbenp.prettier-vscode"
		        ]
		      }
		    }
		  }
		  ```
		- **package.json** (add this field):
		  ```json
		  {
		    "packageManager": "pnpm@8.15.0"
		  }
		  ```
	- ## Example 2: Custom Dockerfile with Container-Only Store
		- **Use Case**: When you need full control over the environment
		- **Dockerfile**:
		  ```dockerfile
		  FROM mcr.microsoft.com/devcontainers/base:ubuntu
		  
		  # Install Node.js and setup pnpm
		  RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
		      && apt-get install -y nodejs
		  
		  # Configure pnpm environment
		  ENV PNPM_HOME=/usr/local/share/pnpm
		  ENV PATH=$PNPM_HOME:$PATH
		  
		  # Enable corepack and prepare pnpm
		  RUN corepack enable
		  RUN corepack prepare pnpm@latest --activate
		  
		  # Set container-only store directory
		  RUN mkdir -p /home/vscode/.pnpm-store
		  RUN pnpm config set store-dir /home/vscode/.pnpm-store
		  ```
		- **devcontainer.json**:
		  ```json
		  {
		    "name": "Custom Node.js with pnpm",
		    "build": {
		      "dockerfile": "Dockerfile"
		    },
		    "postCreateCommand": "pnpm install",
		    "remoteUser": "vscode"
		  }
		  ```
	- ## Example 3: Monorepo with Workspace Support
		- **Use Case**: Large projects with multiple packages, monorepos
		- **devcontainer.json**:
		  ```json
		  {
		    "name": "Monorepo with pnpm",
		    "image": "mcr.microsoft.com/devcontainers/typescript-node:1-22-bookworm",
		    "features": {
		      "ghcr.io/devcontainers/features/node:1": {
		        "version": "22",
		        "packageManager": "pnpm"
		      }
		    },
		    "updateContentCommand": "corepack prepare & pnpm install",
		    "postCreateCommand": "pnpm install",
		    "customizations": {
		      "vscode": {
		        "extensions": [
		          "dbaeumer.vscode-eslint",
		          "esbenp.prettier-vscode",
		          "ms-vscode.vscode-typescript-next"
		        ]
		      }
		    }
		  }
		  ```
		- **pnpm-workspace.yaml**:
		  ```yaml
		  packages:
		    - 'packages/*'
		    - 'apps/*'
		  ```
	- ## Example 4: Production Dockerfile with Multi-Stage Build
		- **Use Case**: Production deployments, CI/CD pipelines
		- **Dockerfile**:
		  ```dockerfile
		  FROM node:22-alpine AS base
		  ENV PNPM_HOME="/pnpm"
		  ENV PATH="$PNPM_HOME:$PATH"
		  RUN corepack enable
		  
		  FROM base AS deps
		  WORKDIR /app
		  COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
		  RUN --mount=type=cache,id=pnpm,target=/pnpm/store \
		      pnpm install --frozen-lockfile
		  
		  FROM base AS build
		  WORKDIR /app
		  COPY --from=deps /app/node_modules ./node_modules
		  COPY . .
		  RUN --mount=type=cache,id=pnpm,target=/pnpm/store \
		      pnpm run build
		  
		  FROM node:22-alpine AS runtime
		  WORKDIR /app
		  COPY --from=build /app/dist ./dist
		  COPY --from=build /app/package.json ./
		  RUN --mount=type=cache,id=pnpm,target=/pnpm/store \
              pnpm install --prod --frozen-lockfile
		  EXPOSE 3000
		  CMD ["node", "dist/index.js"]
		  ```
- # Common Anti-Patterns to Avoid (Updated)
	- **Mismatched Package Managers**: Having `pnpm install` in devcontainer.json but using npm/yarn in package.json
	- **Missing Store Configuration**: Using pnpm without configuring store directory, leading to cross-filesystem hard link issues
	- **Incomplete Corepack Setup**: Enabling corepack without properly configuring PNPM_HOME environment variable
	- **Cross-Filesystem Store Locations**: Binding project directory from host without considering filesystem differences
	- **Missing Package Manager Field**: Not specifying `"packageManager": "pnpm@VERSION"` in package.json
	- **Ignoring Permission Issues**: Not handling file system permissions in mounted volumes
	- **OS Version Inconsistencies**: Not handling different OS versions in compiled dependencies
	- **Missing Frozen Lockfile**: Not using `--frozen-lockfile` for consistent, reproducible builds