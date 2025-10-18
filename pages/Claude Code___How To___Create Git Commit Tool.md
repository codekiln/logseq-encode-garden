tags:: [[Diataxis/How To]]

- # How to use [[Claude Code]] to build a [[CLI/Tool]] to create a [[git/commit]] according to a convention
	- ## Goal
		- Create a standalone command-line tool that generates git commits following the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#summary) based on prompts stored independently of the script.
		- The tool should work independently of Claude Code and can be used in any development workflow.
	- ## Preconditions
		- Claude Code ≥ v1.0 installed and in `PATH`
		- Python 3.8+ or Node.js 18+ for the CLI tool
		- Git repository initialized
		- Anthropic API key configured (for the standalone tool)
	- ## Approach Options
		- ### Option 1: Python-based CLI with llm-cli (Recommended)
			- Uses Simon Willison's `llm-cli` tool for LLM interactions
			- Leverages `uv` for tool management
			- Can be installed globally or run on-demand
		- ### Option 2: Node.js-based CLI with Claude API
			- Direct integration with Anthropic's Claude API
			- Can use `oclif` framework for CLI structure
			- Managed via `mise` tasks
		- ### Option 3: Claude Code-assisted development
			- Use Claude Code to help build the tool
			- Then extract the standalone script for independent use
	- ## Procedure: Option 1 - Python CLI with llm-cli
		- ### 1. Set up the development environment
			- Create a new project directory:
				- ~~~bash
				  mkdir conventional-commit-tool
				  cd conventional-commit-tool
				  ~~~
			- Initialize with `uv`:
				- ~~~bash
				  uv init
				  ~~~
			- Add dependencies to `pyproject.toml`:
				- ~~~toml
				  [project]
				  name = "conventional-commit-tool"
				  version = "0.1.0"
				  description = "Generate conventional commits using LLM"
				  dependencies = [
				      "click>=8.0.0",
				      "anthropic>=0.25.0",
				      "pydantic>=2.0.0",
				  ]
				  
				  [project.scripts]
				  conventional-commit = "conventional_commit_tool.cli:main"
				  ~~~
		- ### 2. Create the CLI structure
			- Create the main CLI module:
				- ~~~python
				  # conventional_commit_tool/cli.py
				  import click
				  import os
				  from pathlib import Path
				  from .commit_generator import ConventionalCommitGenerator
				  
				  @click.command()
				  @click.option('--prompt-file', '-p', 
				                help='Path to file containing commit prompt')
				  @click.option('--prompt', '-m', 
				                help='Direct commit prompt text')
				  @click.option('--dry-run', is_flag=True, 
				                help='Show commit message without executing')
				  @click.option('--scope', '-s', 
				                help='Optional scope for the commit')
				  def main(prompt_file, prompt, dry_run, scope):
				      """Generate conventional commits using LLM."""
				      generator = ConventionalCommitGenerator()
				      
				      if prompt_file:
				          with open(prompt_file, 'r') as f:
				              prompt_text = f.read().strip()
				      elif prompt:
				          prompt_text = prompt
				      else:
				          click.echo("Error: Must provide either --prompt-file or --prompt")
				          return
				      
				      commit_msg = generator.generate_commit(prompt_text, scope)
				      
				      if dry_run:
				          click.echo("Generated commit message:")
				          click.echo(commit_msg)
				      else:
				          # Execute git commit
				          os.system(f'git commit -m "{commit_msg}"')
				  
				  if __name__ == '__main__':
				      main()
				  ~~~
		- ### 3. Create the commit generator
			- ~~~python
			  # conventional_commit_tool/commit_generator.py
			  import anthropic
			  import os
			  from typing import Optional
			  
			  class ConventionalCommitGenerator:
			   def __init__(self):
			    self.client = anthropic.Anthropic(
			  	  api_key=os.getenv('ANTHROPIC_API_KEY')
			    )
			   
			   def generate_commit(self, prompt: str, scope: Optional[str] = None) -> str:
			    system_prompt = self._get_system_prompt()
			    
			    user_prompt = f"""
			    Generate a conventional commit message for the following changes:
			    
			    {prompt}
			    """
			    
			    if scope:
			  	  user_prompt += f"\n\nScope: {scope}"
			    
			    response = self.client.messages.create(
			  	  model="claude-3-5-sonnet-20241022",
			  	  max_tokens=150,
			  	  system=system_prompt,
			  	  messages=[{"role": "user", "content": user_prompt}]
			    )
			    
			    return response.content[0].text.strip()
			   
			   def _get_system_prompt(self) -> str:
			    return """
			    You are a git commit message generator that follows the Conventional Commits specification.
			    
			    The commit message should be structured as follows:
			    <type>[optional scope]: <description>
			    
			    Types:
			    - feat: A new feature
			    - fix: A bug fix
			    - docs: Documentation only changes
			    - style: Changes that do not affect the meaning of the code
			    - refactor: A code change that neither fixes a bug nor adds a feature
			    - perf: A code change that improves performance
			    - test: Adding missing tests or correcting existing tests
			    - chore: Changes to the build process or auxiliary tools
			    
			    Rules:
			    1. Use the imperative mood ("add" not "added" or "adds")
			    2. Don't capitalize the first letter
			    3. No dot (.) at the end
			    4. Keep the description under 72 characters
			    5. If scope is provided, include it in brackets
			    
			    Examples:
			    - feat(auth): add OAuth2 authentication
			    - fix(api): resolve user data retrieval issue
			    - docs: update README with installation steps
			    - refactor: simplify user validation logic
			    """
			  ~~~
		- ### 4. Create prompt templates
			- Create a `prompts/` directory with template files:
				- ~~~bash
				  mkdir prompts
				  ~~~
			- Example prompt file `prompts/feature.txt`:
				- ~~~text
				  Added new user authentication feature with OAuth2 support.
				  Includes login/logout functionality and session management.
				  Updated API endpoints to handle authentication tokens.
				  Added unit tests for authentication flow.
				  ~~~
			- Example prompt file `prompts/bugfix.txt`:
				- ~~~text
				  Fixed issue where user data was not being retrieved correctly.
				  The problem was in the database query that was missing proper joins.
				  Added error handling for cases where user data is not found.
				  ~~~
		- ### 5. Install and test the tool
			- Install in development mode:
				- ~~~bash
				  uv pip install -e .
				  ~~~
			- Test with a prompt file:
				- ~~~bash
				  conventional-commit --prompt-file prompts/feature.txt --dry-run
				  ~~~
			- Test with direct prompt:
				- ~~~bash
				  conventional-commit --prompt "Fixed login bug" --scope auth --dry-run
				  ~~~
		- ### 6. Make it globally available
			- Install globally using `uv`:
				- ~~~bash
				  uv tool install conventional-commit-tool
				  ~~~
			- Or add to `mise.toml` for project-specific use:
				- ~~~toml
				  [tasks.commit]
				  description = "Generate conventional commit"
				  run = "uvx conventional-commit-tool $@"
				  env = { ANTHROPIC_API_KEY = "op://vault/anthropic-key/credential" }
				  ~~~
	- ## Procedure: Option 2 - Node.js CLI with oclif
		- ### 1. Initialize oclif project
			- ~~~bash
			  npx oclif generate conventional-commit-tool
			  cd conventional-commit-tool
			  ~~~
		- ### 2. Add dependencies
			- ~~~bash
			  npm install @anthropic-ai/sdk
			  ~~~
		- ### 3. Create the main command
			- ~~~typescript
			  // src/commands/generate.ts
			  import {Command, Flags} from '@oclif/core'
			  import Anthropic from '@anthropic-ai/sdk'
			  import * as fs from 'fs'
			  import {execSync} from 'child_process'
			  
			  export default class Generate extends Command {
			   static description = 'Generate conventional commit message'
			   
			   static flags = {
			    'prompt-file': Flags.string({
			  	  char: 'p',
			  	  description: 'Path to file containing commit prompt',
			    }),
			    prompt: Flags.string({
			  	  char: 'm',
			  	  description: 'Direct commit prompt text',
			    }),
			    'dry-run': Flags.boolean({
			  	  description: 'Show commit message without executing',
			    }),
			    scope: Flags.string({
			  	  char: 's',
			  	  description: 'Optional scope for the commit',
			    }),
			   }
			   
			   async run() {
			    const {flags} = await this.parse(Generate)
			    
			    const anthropic = new Anthropic({
			  	  apiKey: process.env.ANTHROPIC_API_KEY,
			    })
			    
			    let promptText: string
			    
			    if (flags['prompt-file']) {
			  	  promptText = fs.readFileSync(flags['prompt-file'], 'utf8').trim()
			    } else if (flags.prompt) {
			  	  promptText = flags.prompt
			    } else {
			  	  this.error('Must provide either --prompt-file or --prompt')
			    }
			    
			    const systemPrompt = this.getSystemPrompt()
			    const userPrompt = this.buildUserPrompt(promptText, flags.scope)
			    
			    const response = await anthropic.messages.create({
			  	  model: 'claude-3-5-sonnet-20241022',
			  	  max_tokens: 150,
			  	  system: systemPrompt,
			  	  messages: [{role: 'user', content: userPrompt}],
			    })
			    
			    const commitMsg = response.content[0].text.trim()
			    
			    if (flags['dry-run']) {
			  	  this.log('Generated commit message:')
			  	  this.log(commitMsg)
			    } else {
			  	  execSync(`git commit -m "${commitMsg}"`, {stdio: 'inherit'})
			    }
			   }
			   
			   private getSystemPrompt(): string {
			    return `You are a git commit message generator that follows the Conventional Commits specification.
			    
			    The commit message should be structured as follows:
			    <type>[optional scope]: <description>
			    
			    Types:
			    - feat: A new feature
			    - fix: A bug fix
			    - docs: Documentation only changes
			    - style: Changes that do not affect the meaning of the code
			    - refactor: A code change that neither fixes a bug nor adds a feature
			    - perf: A code change that improves performance
			    - test: Adding missing tests or correcting existing tests
			    - chore: Changes to the build process or auxiliary tools
			    
			    Rules:
			    1. Use the imperative mood ("add" not "added" or "adds")
			    2. Don't capitalize the first letter
			    3. No dot (.) at the end
			    4. Keep the description under 72 characters
			    5. If scope is provided, include it in brackets`
			   }
			   
			   private buildUserPrompt(prompt: string, scope?: string): string {
			    let userPrompt = `Generate a conventional commit message for the following changes:
			    
			    ${prompt}`
			    
			    if (scope) {
			  	  userPrompt += `\n\nScope: ${scope}`
			    }
			    
			    return userPrompt
			   }
			  }
			  ~~~
		- ### 4. Build and install
			- ~~~bash
			  npm run build
			  npm install -g .
			  ~~~
	- ## Procedure: Option 3 - Claude Code-assisted development
		- ### 1. Use Claude Code to scaffold the project
			- Start Claude Code in your project:
				- ~~~bash
				  claude
				  ~~~
			- Ask Claude to help create the CLI tool:
				- > "Help me create a Python CLI tool that generates conventional commits using the Anthropic API. The tool should read prompts from files and generate commit messages following the Conventional Commits specification."
		- ### 2. Extract the standalone script
			- Once Claude Code has helped create the tool, extract the relevant files
			- Remove any Claude Code-specific dependencies
			- Test the standalone version
	- ## Usage Examples
		- ### Basic usage with prompt file
			- ~~~bash
			  conventional-commit --prompt-file prompts/feature.txt
			  ~~~
		- ### With scope specification
			- ~~~bash
			  conventional-commit --prompt "Fixed authentication bug" --scope auth
			  ~~~
		- ### Dry run to preview
			- ~~~bash
			  conventional-commit --prompt-file prompts/bugfix.txt --dry-run
			  ~~~
		- ### Using with mise task
			- ~~~bash
			  mise run commit --prompt-file prompts/feature.txt
			  ~~~
	- ## Integration with Development Workflow
		- ### Git hooks
			- Create a pre-commit hook that uses the tool
			- Store commit prompts in a `.commit-prompts/` directory
		- ### IDE integration
			- Add VS Code tasks for common commit types
			- Create snippets for prompt templates
		- ### CI/CD integration
			- Use the tool in automated commit generation
			- Validate commit messages in CI
	- ## Troubleshooting
		- **API key not found**: Ensure `ANTHROPIC_API_KEY` is set in environment
		- **Permission denied**: Make sure the script is executable (`chmod +x`)
		- **Git not found**: Ensure git is installed and in PATH
		- **Invalid commit format**: Check that the prompt is clear and specific
	- ## References
		- [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/#summary)
		- [llm-cli Documentation](https://llm.datasette.io/)
		- [oclif Framework](https://oclif.io/)
		- [Anthropic Claude API](https://docs.anthropic.com/claude/reference)
		- [mise Task Management](https://mise.jdx.dev/tasks/)