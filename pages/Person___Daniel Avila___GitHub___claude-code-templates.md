- # [Claude Code Templates (aitmpl.com)](https://github.com/davila7/claude-code-templates)
	- Repository: [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
	- Website: [aitmpl.com](https://aitmpl.com)
	- Documentation: [docs.aitmpl.com](https://docs.aitmpl.com)
	- Created by: [[Person/Daniel Avila]]
	- **Ready-to-use configurations for Anthropic's Claude Code.** A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.
	- **Note:** This is a community-maintained project, not an official Anthropic product.
- ## Overview
	- Claude Code Templates is a **CLI tool and marketplace** for configuring and monitoring Claude Code
	- Provides 100+ pre-built components including agents, commands, MCPs, settings, hooks, and skills
	- Includes interactive web interface for browsing and installing components
	- Offers additional development tools for analytics, monitoring, and diagnostics
- ## Components
	- | Component | Description | Examples |
	  | ---- | ---- | ---- |
	  | **🤖 Agents** | AI specialists for specific domains | Security auditor, React performance optimizer, database architect |
	  | **⚡ Commands** | Custom slash commands | `/generate-tests`, `/optimize-bundle`, `/check-security` |
	  | **🔌 MCPs** | External service integrations | GitHub, PostgreSQL, Stripe, AWS, OpenAI |
	  | **⚙️ Settings** | Claude Code configurations | Timeouts, memory settings, output styles |
	  | **🪝 Hooks** | Automation triggers | Pre-commit validation, post-completion actions |
	  | **🎨 Skills** | Reusable capabilities with progressive disclosure | PDF processing, Excel automation, custom workflows |
- ## Installation Methods
	- ### Interactive Installation
		- Browse and install interactively:
		  ```bash
		  npx claude-code-templates@latest
		  ```
	- ### Command Line Installation
		- Install complete development stack:
		  ```bash
		  npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes
		  ```
		- Install specific components:
		  ```bash
		  # Install agent
		  npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
		  
		  # Install command
		  npx claude-code-templates@latest --command performance/optimize-bundle --yes
		  
		  # Install setting
		  npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
		  
		  # Install hook
		  npx claude-code-templates@latest --hook git/pre-commit-validation --yes
		  
		  # Install MCP
		  npx claude-code-templates@latest --mcp database/postgresql-integration --yes
		  ```
- ## Additional Tools
	- ### 📊 Claude Code Analytics
		- Monitor AI-powered development sessions in real-time with live state detection and performance metrics
		- ```bash
		  npx claude-code-templates@latest --analytics
		  ```
	- ### 💬 Conversation Monitor
		- Mobile-optimized interface to view Claude responses in real-time with secure remote access
		- Local access:
		  ```bash
		  npx claude-code-templates@latest --chats
		  ```
		- Secure remote access via Cloudflare Tunnel:
		  ```bash
		  npx claude-code-templates@latest --chats --tunnel
		  ```
	- ### 🔍 Health Check
		- Comprehensive diagnostics to ensure your Claude Code installation is optimized
		- ```bash
		  npx claude-code-templates@latest --health-check
		  ```
	- ### 🔌 Plugin Dashboard
		- View marketplaces, installed plugins, and manage permissions from a unified interface
		- ```bash
		  npx claude-code-templates@latest --plugins
		  ```
- ## Related Concepts
	- [[Claude Code/Command/Slash/Docs/Comparison with Skills]]
	- [[Claude Code/Skill/Project]]
	- [[My/Dev/Tool/Pref/AI/Coding/Config/Management]]
- ## Links
	- **🌐 Browse Templates**: [aitmpl.com](https://aitmpl.com)
	- **📚 Documentation**: [docs.aitmpl.com](https://docs.aitmpl.com)
	- **💬 Community**: [GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
	- **🐛 Issues**: [GitHub Issues](https://github.com/davila7/claude-code-templates/issues)
- ## Attribution
	- This collection includes components from multiple sources:
	- **Agents Collection:**
		- **wshobson/agents Collection** by wshobson - Licensed under MIT License (48 agents)
	- **Commands Collection:**
		- **awesome-claude-code Commands** by hesreallyhim - Licensed under CC0 1.0 Universal (21 commands)
- ## License
	- MIT License - see the [LICENSE file](https://github.com/davila7/claude-code-templates/blob/main/LICENSE) for details

