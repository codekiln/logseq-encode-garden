---
targets:
  - '*'
description: Create a new Rulesync slash command through guided requirements elicitation
---

# Create Rulesync Command

This command guides you through creating a new Rulesync slash command by eliciting requirements, determining the command's purpose and name, and then creating the command file in `.rulesync/commands/`.

## Workflow

### Step 1: Requirements Elicitation

Ask the user the following questions to understand what the command should do:

1. **What is the primary purpose of this command?**
   - What problem does it solve?
   - What task should it help automate or guide?

2. **What should the command be called?**
   - Use kebab-case naming (e.g., `logseq-person`, `create-rulesync-command`)
   - Consider prefixing with a category if appropriate (e.g., `logseq-*`, `git-*`)
   - The command name should be descriptive and follow existing naming patterns

3. **Does the command need arguments?**
   - If yes, what arguments does it need?
   - What format should arguments be in?
   - Should there be an `argument-hint` to guide users?

4. **What is the target scope?**
   - Should it apply to all targets (`['*']`)?
   - Or specific targets (e.g., `['claudecode', 'cursor']`)?

5. **What are the key steps or workflow the command should guide?**
   - What are the main actions or decisions involved?
   - What should the AI do when executing this command?

6. **Are there any special considerations or constraints?**
   - Any formatting requirements?
   - Any dependencies on other commands or rules?
   - Any specific patterns to follow?

### Step 2: Review and Confirm

After gathering requirements, summarize:
- Command name
- Purpose/description
- Arguments (if any)
- Target scope
- Main workflow/steps

Ask the user to confirm or request changes before proceeding.

### Step 3: Create the Command File

Once confirmed, create the command file at `.rulesync/commands/{COMMAND_NAME}.md` with:

1. **Frontmatter**:
   - `targets:` array (from requirements)
   - `description:` string (from requirements)
   - `argument-hint:` (if arguments are needed)

2. **Content Structure**:
   - Title: `# {Command Name}`
   - Brief description of what the command does
   - **Variables** section (if arguments are used)
   - **Workflow** section with clear steps
   - **Report** section (if output is needed)
   - Any additional sections relevant to the command

3. **Formatting**:
   - Follow the format of existing commands in `.rulesync/commands/`
   - Use clear, actionable language
   - Include examples if helpful
   - Reference related rules or commands if applicable

### Step 4: Verify and Test

After creating the file:
- Read back the created command file to the user
- Confirm it matches their requirements
- Suggest any improvements if needed

## Example Interaction

**User**: `/create-rulesync-command`

**AI**: I'll help you create a new Rulesync command. Let me ask a few questions:

1. What is the primary purpose of this command?
2. What should it be called?
3. Does it need arguments?
...

**After requirements gathered**:

**AI**: Based on our discussion, I'll create a command called `{name}` that {description}. Here's what I understand:
- Purpose: {purpose}
- Arguments: {args or none}
- Targets: {targets}
- Workflow: {workflow}

Does this look correct? Should I proceed with creating the file?

## Notes

- Command files should be in `.rulesync/commands/` directory
- Use kebab-case for filenames
- Follow existing command patterns for consistency
- Commands should be clear, actionable, and well-documented
- Consider referencing related rules or commands when relevant

