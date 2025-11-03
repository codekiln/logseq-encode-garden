tags:: [[GitHub]], [[Claude Code]]

- # [Claude Code Plugins (wshobson/agents)](https://github.com/wshobson/agents)
	- Repository: [wshobson/agents](https://github.com/wshobson/agents)
	- Created by: [[Person/Seth Hobson]]
	- Stars: 14.5k+
	- **Intelligent automation and multi-agent orchestration for Claude Code.** A comprehensive production-ready system combining 84 specialized AI agents, 15 multi-agent workflow orchestrators, and 44 development tools organized into 62 focused, single-purpose plugins.
	- **Note:** This is a community-maintained project, not an official Anthropic product.
- ## Overview
	- Comprehensive collection of **84 specialized AI agents** designed to enhance Claude Code capabilities across the entire software development lifecycle
	- **63 plugins**, each introducing unique agents, commands, and skills to Claude Code
	- **47 specialized skills** distributed across 14 plugins, following Anthropic's progressive disclosure architecture
	- **15 multi-agent workflow orchestrators** for complex task coordination
	- **44 development tools** for various aspects of software development
	- Optimized for Claude models including Sonnet 4.5 and Haiku 4.5
- ## Architecture
	- ### Hybrid Model Orchestration
		- Strategic model assignment to balance performance and cost
		- **Haiku agents** for fast execution of deterministic tasks
		- **Sonnet agents** for complex reasoning and architecture
	- ### Progressive Disclosure
		- Skills follow Anthropic's progressive disclosure architecture
		- Skills are distributed across 14 plugins
		- Enables focused, targeted functionality
- ## Installation
	- ### Add the Marketplace
		- ```bash
		  /plugin marketplace add wshobson/agents
		  ```
	- ### Install Desired Plugins
		- ```bash
		  /plugin install [plugin-name]
		  ```
		- Replace `[plugin-name]` with the specific plugin you wish to install
		- Example: Install the Python development plugin
			- ```bash
			  /plugin install python-development
			  ```
		- Each installed plugin loads its specific agents, commands, and skills into Claude's context
- ## Components
	- ### Plugins (63 total)
		- Each plugin introduces unique agents, commands, and skills
		- Plugins cover a wide range of functionalities:
			- Development (Python, JavaScript, TypeScript, etc.)
			- Infrastructure (DevOps, cloud deployment, etc.)
			- Security (code auditing, vulnerability scanning, etc.)
			- And more specialized domains
	- ### Agents (84 total)
		- Specialized AI agents for specific tasks and domains
		- Organized by category and functionality
		- Each agent is tailored to perform specific development tasks
	- ### Skills (47 total)
		- Specialized skills distributed across 14 plugins
		- Following progressive disclosure architecture
		- Encompass areas such as:
			- Language development
			- Infrastructure
			- DevOps
			- Security
	- ### Multi-Agent Workflow Orchestrators (15 total)
		- Coordinate multiple agents for complex tasks
		- Enable intelligent automation across the development lifecycle
	- ### Development Tools (44 total)
		- Tools for various aspects of software development
		- Cover testing, deployment, monitoring, and more
- ## Documentation and Resources
	- **Plugin Reference:** Complete catalog of all 63 plugins
	- **Agent Reference:** Detailed information on all 84 agents, organized by category
	- **Agent Skills:** Descriptions of the 47 specialized skills with progressive disclosure
	- **Usage Guide:** Instructions on commands, workflows, and best practices
	- **Architecture Overview:** Insights into design principles and patterns
	- All resources accessible within the repository
- ## Use Cases
	- Enhance Claude Code environment with specialized capabilities
	- Enable intelligent automation throughout software development
	- Coordinate multiple agents for complex development tasks
	- Optimize workflow efficiency with targeted plugins
	- Balance performance and cost with hybrid model orchestration
- ## External Links
	- [GitHub Repository](https://github.com/wshobson/agents)
	- [Person/Seth Hobson]([[Person/Seth Hobson]]) - Creator and maintainer

