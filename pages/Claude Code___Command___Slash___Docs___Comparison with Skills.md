- [Slash commands - Claude Docs](https://docs.claude.com/en/docs/claude-code/slash-commands#skills-vs-slash-commands)
- # Skills vs slash commands
	- **Slash commands** and **Agent Skills** serve different purposes in Claude Code
- ## Use slash commands for
	- **Quick, frequently-used prompts**
	- Simple prompt snippets you use often
	- Quick reminders or templates
	- Frequently-used instructions that fit in one file
	- **Examples**
	- `/review` → "Review this code for bugs and suggest improvements"
	- `/explain` → "Explain this code in simple terms"
	- `/optimize` → "Analyze this code for performance issues"
- ## Use Skills for
	- **Comprehensive capabilities with structure**
	- Complex workflows with multiple steps
	- Capabilities requiring scripts or utilities
	- Knowledge organized across multiple files
	- Team workflows you want to standardize
	- **Examples**
	- PDF processing Skill with form-filling scripts and validation
	- Data analysis Skill with reference docs for different data types
	- Documentation Skill with style guides and templates
- ## Key differences
	- | Aspect | Slash Commands | Agent Skills |
	  | ---- | ---- | ---- |
	  | **Complexity** | Simple prompts | Complex capabilities |
	  | **Structure** | Single .md file | Directory with SKILL.md + resources |
	  | **Discovery** | Explicit invocation (`/command`) | Automatic (based on context) |
	  | **Files** | One file only | Multiple files, scripts, templates |
	  | **Scope** | Project or personal | Project or personal |
	  | **Sharing** | Via git | Via git |
- ## Example comparison
	- ### As a slash command
	- ~~~
	  **# .claude/commands/review.md**
	  Review this code for:
	  - Security vulnerabilities
	  - Performance issues
	  - Code style violations
	  ~~~
	- Usage: `/review` (manual invocation)
	- ### As a Skill
	- ~~~
	  .claude/skills/code-review/
	  ├── SKILL.md (overview and workflows)
	  ├── SECURITY.md (security checklist)
	  ├── PERFORMANCE.md (performance patterns)
	  ├── STYLE.md (style guide reference)
	  └── scripts/
	    └── run-linters.sh
	  ~~~
	- Usage: "Can you review this code?" (automatic discovery)
	- The Skill provides richer context, validation scripts, and organized reference material
- ## When to use each
	- **Use slash commands**
	- You invoke the same prompt repeatedly
	- The prompt fits in a single file
	- You want explicit control over when it runs
	- **Use Skills**
	- Claude should discover the capability automatically
	- Multiple files or scripts are needed
	- Complex workflows with validation steps
	- Team needs standardized, detailed guidance
- Both slash commands and Skills can coexist. Use the approach that fits your needs. Learn more about [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills).
