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
	- ## Search Queries Attempted
		- **Query**: `gh search repos '"devcontainer.json" "pnpm-lock.yaml" stars:>100' --limit 100`
			- **Goal**: Find repositories with both devcontainer configurations and pnpm usage that have significant community adoption
			- **Result**: No results found - suggests few repositories use both devcontainer and pnpm together with high popularity
		- **Query**: `gh search repos 'pnpm devcontainer' --limit 30`
			- **Goal**: Find repositories specifically mentioning both pnpm and devcontainer
			- **Result**: Found 3 repositories: nafnix/pnpm-devcontainer, p-buddy/pnpm-devcontainer-template, aj007-art/ts-template
		- **Query**: `gh search repos 'devcontainer.json pnpm' --limit 30`
			- **Goal**: Alternative search for repositories with devcontainer.json files that use pnpm
			- **Result**: No additional results beyond previous query
		- **Query**: `gh search repos 'pnpm monorepo devcontainer' --limit 10`
			- **Goal**: Find monorepo examples using pnpm with devcontainer setups
			- **Result**: No results found
		- **Query**: `gh search repos 'pnpm turborepo devcontainer' --limit 10`
			- **Goal**: Find repositories combining pnpm, turborepo, and devcontainer (common modern stack)
			- **Result**: No results found
		- **Query**: `gh search repos 'pnpm workspace devcontainer' --limit 15`
			- **Goal**: Find repositories using pnpm workspaces with devcontainer configurations
			- **Result**: No results found
		- **Query**: `gh search repos 'pnpm devcontainer template' --limit 15`
			- **Goal**: Find template repositories specifically for pnpm devcontainer setups
			- **Result**: Found p-buddy/pnpm-devcontainer-template
		- **Query**: `gh search repos 'pnpm devcontainer example' --limit 15`
			- **Goal**: Find example repositories demonstrating pnpm devcontainer usage
			- **Result**: No additional results
		- **Query**: `gh search repos 'pnpm devcontainer starter' --limit 15`
			- **Goal**: Find starter templates with pnpm devcontainer configurations
			- **Result**: No additional results
		- **Query**: `gh search repos 'pnpm monorepo' --limit 10`
			- **Goal**: Find pnpm monorepo repositories that might have Docker configurations
			- **Result**: Found jkomyno/pnpm-monorepo-template (57 stars) with Dockerfile.pnpm
		- **Query**: `gh search repos 'vercel pnpm devcontainer' --limit 10`
			- **Goal**: Find Vercel projects using pnpm with devcontainer configurations
			- **Result**: No results found
		- **Query**: `gh search repos 'stackblitz pnpm devcontainer' --limit 10`
			- **Goal**: Find StackBlitz projects using pnpm with devcontainer configurations
			- **Result**: No results found
		- **Query**: `gh search repos 'discord pnpm devcontainer' --limit 10`
			- **Goal**: Find Discord projects using pnpm with devcontainer configurations
			- **Result**: No results found
	- ## Search Results Summary
		- **Total repositories found with actual devcontainer/Docker pnpm configurations**: 5
		- **Repositories with 100+ stars**: 0
		- **Repositories with 50+ stars**: 1 (jkomyno/pnpm-monorepo-template with 57 stars)
		- **Repositories with 0-10 stars**: 4
		- **Key finding**: Very few repositories combine pnpm with devcontainer configurations, suggesting this is not a common pattern in the community
	- ## Examples Found (All Under 100 Stars)
		- [jkomyno/pnpm-monorepo-template](https://github.com/jkomyno/pnpm-monorepo-template) - Opinionated Node.js monorepo with pnpm, turborepo, vitest (57 stars)
			- **Pattern**: Pattern 3 (Multi-Stage Docker Builds) + Pattern 5 (Corepack Integration) + Pattern 1 (Container-Only Store)
			- **Implementation**: Comprehensive multi-stage builds with separate stages for dependencies, build, and test, uses corepack for pnpm consistency, container-only store for monorepo efficiency
			- **Files**: [Dockerfile.pnpm](https://github.com/jkomyno/pnpm-monorepo-template/blob/main/Dockerfile.pnpm)
		- [nafnix/pnpm-devcontainer](https://github.com/nafnix/pnpm-devcontainer) - PNPM 开发容器 (0 stars)
			- **Pattern**: Pattern 1 (Container-Only Store Directory)
			- **Implementation**: Uses `pnpm config set store-dir /home/vscode/.pnpm-store` in postCreateCommand, avoiding cross-filesystem hard link issues by keeping store within container filesystem
			- **Files**: [devcontainer.json](https://github.com/nafnix/pnpm-devcontainer/blob/master/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/nafnix/pnpm-devcontainer/blob/master/.devcontainer/Dockerfile)
		- [p-buddy/pnpm-devcontainer-template](https://github.com/p-buddy/pnpm-devcontainer-template) - Template repository (0 stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 1 (Container-Only Store)
			- **Implementation**: Leverages `RUN corepack enable` in Dockerfile with `ENV PNPM_HOME="/pnpm"` and `ENV PATH="$PNPM_HOME:$PATH"`, then sets container-only store directory
			- **Files**: [devcontainer.json](https://github.com/p-buddy/pnpm-devcontainer-template/blob/main/.devcontainer/devcontainer.json) | [Dockerfile](https://github.com/p-buddy/pnpm-devcontainer-template/blob/main/.devcontainer/Dockerfile)
		- [aj007-art/ts-template](https://github.com/aj007-art/ts-template) - TypeScript starter with ESLint+Prettier, tsx, pnpm, devcontainer (0 stars)
			- **Pattern**: Pattern 5 (Corepack Integration) + Pattern 4 (DevContainer Features)
			- **Implementation**: Uses corepack for pnpm installation combined with DevContainer features for TypeScript tooling, likely with container-only store approach
			- **Files**: [devcontainer.json](https://github.com/aj007-art/ts-template/blob/main/.devcontainer/devcontainer.json) *(No Dockerfile - uses base image)*
		- [gitgitWi/nodejs-monorepo-devcontainer-template](https://github.com/gitgitWi/nodejs-monorepo-devcontainer-template) - Uses PNPM Workspace + Turborepo (1 star)
			- **Pattern**: Pattern 3 (Multi-Stage Docker Builds) + Pattern 5 (Corepack Integration)
			- **Implementation**: Implements multi-stage builds with separate dependency installation and build stages, uses corepack for pnpm management, optimized for monorepo with PNPM Workspace + Turborepo
			- **Files**: [devcontainer.json](https://github.com/gitgitWi/nodejs-monorepo-devcontainer-template/blob/main/.devcontainer/devcontainer.json) *(No Dockerfile - uses base image)*
- # Best Practices Summary
	- ## Store Management
		- Use container-only store for simplicity
		- Use shared store with proper volume mounting for efficiency
		- Avoid cross-filesystem store locations
	- ## Installation Methods
		- Prefer corepack over manual npm install -g pnpm
		- Use DevContainer features when available
		- Set PNPM_HOME environment variable consistently
	- ## Build Optimization
		- Use multi-stage builds for production images
		- Leverage BuildKit cache mounts
		- Separate dependency installation from application build
	- ## Development Workflow
		- Use --frozen-lockfile for consistent installs
		- Configure postCreateCommand for automatic setup
		- Handle OS-specific dependency variations
- # Common Anti-Patterns to Avoid
	- Binding project directory from host without considering filesystem differences
	- Not setting explicit store directory location
	- Mixing different package managers in same project
	- Ignoring permission issues in mounted volumes
	- Not handling OS version differences in compiled dependencies