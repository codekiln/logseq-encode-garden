tags:: [[Conventional Commits]], [[gitmoji]]
alias:: [[Conventional Emoji Commits]]

- # Conventional Emoji Commits
	- ## Overview
		- A specification that blends [[gitmoji]] with [[Conventional Commits]]
		- Creates more expressive and standardized commit messages
		- Link: [Conventional Emoji Commits](https://conventional-emoji-commits.site/quick-summary/summary)
	- ## Core Format
		- ```
		  <emoji> <type>[optional scope]: <description>

		  [optional body]

		  [optional footer(s)]
		  ```
	- ## Primary Commit Types
		- `✨ feat`: New feature (MINOR version)
		- `🩹 fix`: Bug fix (PATCH version)
		- `🚨 BREAKING CHANGE`: API-breaking modifications (MAJOR version)
	- ## Additional Types
		- `📚 docs`: Documentation changes
		- `♻️ refactor`: Code refactoring
		- `🧪 test`: Adding or modifying tests
		- `🔧 build`: Build system or dependency changes
		- `🎨 style`: Formatting, missing semicolons, etc.
		- `⚡️ perf`: Performance improvements
	- ## Key Benefits
		- Visual indicators make commit history more readable
		- Compatible with semantic versioning
		- Supports automated changelog generation
		- Enhances team communication
	- ## Examples
		- ```
		  ✨ feat(auth): add OAuth2 support

		  Implements OAuth2 authentication flow for third-party logins

		  BREAKING CHANGE: removes legacy authentication endpoints
		  ```
		- ```
		  🩹 fix: resolve image upload bug in Safari
		  ```
	- ## Usage with Ticket References
		- For ticket-based projects, add the ticket reference as the last line:
		- ```
		  ✨ feat: implement user profile page

		  PD-12345 User Profile Implementation
		  ```
		- For non-ticket projects, this reference is optional
	- ## References
		- Extended documentation: [conventional_commits.md](https://github.com/codekiln/alits/blob/feature/story-1.1-foundation-core-package-setup/docs/dev/scm/conventional_commits.md)
		- See also: [[My/Dev/Tool/Pref/SCM]] for commit message preferences