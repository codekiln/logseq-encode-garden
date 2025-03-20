tags:: [[CLI/Tool]], [[Secrets]]
- # [[dotenv-org/vault]]
	- ## Overview
		- Extension of [[dotenv]] that adds encrypted vault capabilities
		- Allows secure sharing and syncing of [[EnvVar/.env]] files across teams and environments
		- Integrated with various language ecosystems (Node.js, Python, etc.)
	- ## Key Features
		- ### Environment Management
			- Secure encryption of environment variables
			- Multiple environment support (development, production, etc.)
			- Version history and backup of `.env` files
			- Team-based access controls
		- ### Workflow
			- Local development using standard `.env` files
			- Build process encrypts to `.env.vault`
			- Deployment using `DOTENV_KEY` for decryption
			- Graceful fallback to standard [[dotenv]] when `DOTENV_KEY` not set
	- ## Usage
		- ### Basic Setup
			- ~~~bash
			  # Initialize new vault
			  npx dotenv-vault new
			  
			  # Login to dotenv.org
			  npx dotenv-vault login
			  
			  # Push/pull .env changes
			  npx dotenv-vault push
			  npx dotenv-vault pull
			  ~~~
		- ### Deployment
			- ~~~bash
			  # Build encrypted .env.vault
			  npx dotenv-vault build
			  
			  # Get deployment key
			  npx dotenv-vault keys
			  
			  # Set on infrastructure (e.g. Heroku)
			  heroku config:set DOTENV_KEY="dotenv://:key_1234@dotenv.org/vault/.env.vault?environment=production"
			  ~~~
	- ## Best Practices
		- Never commit `.env` files to version control
		- Always commit `.env.vault` files (they're encrypted)
		- Never share `DOTENV_KEY` through insecure channels
		- Use different keys for different environments
	- ## Integration with [[mise]]
		- Potential integration path through backend support
		- Could provide native support for encrypted environment variables
		- Alternative to direct secret manager integrations
	- ## Links
		- [GitHub Repository](https://github.com/dotenv-org/dotenv-vault)
		- [Documentation](https://www.dotenv.org/docs/) 