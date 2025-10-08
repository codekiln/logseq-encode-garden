---
description: ''
---
# Diataxis How-To Guide Format for Logseq

This rule provides guidance on creating How-To guides in Logseq following the Diataxis documentation framework principles.

<rule>
name: diataxis_how_to_format
description: Guidelines for creating effective How-To guides in Logseq following the Diataxis framework
filters:
  - type: file_path
    pattern: ".*How To.*\\.md$"

actions:
  - type: suggest
    message: |
      # Creating Diataxis How-To Guides in Logseq

      ## Purpose
      
      How-to guides are **directions** that guide the reader through solving a specific problem or achieving a concrete result. They are **goal-oriented** and focused on practical tasks.
      
      According to the Diataxis framework, How-To guides:
      - Address real-world problems and tasks
      - Guide the reader's actions toward a specific goal
      - Assume the reader knows what they want to achieve
      - Focus on practical steps rather than conceptual understanding

      See @Diataxis___How To.md and @Diataxis___How To___Create a How To.md for more detailed information in the knowledge base about how-to guides.
      
      ## Key Principles
      
      1. **Focus on tasks or problems** - Address real-world needs
      2. **Assume competence** - The reader knows what they want to achieve
      3. **Action-oriented** - Provide clear, executable steps
      4. **No digressions** - Avoid explanations, teaching, or reference material
      5. **Practical over complete** - Usability is more important than covering every possibility
      6. **Describe a logical sequence** - Steps should flow naturally in a meaningful order
      7. **Pay attention to naming** - Titles should clearly state what the guide helps accomplish
      
      ## Structure for Logseq How-To Guides
      
      When creating a How-To guide in Logseq, follow this structure using Logseq-Flavored Markdown (LFM):
      
      ```
      tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/How To]]
      
      - # How To [Specific Task]
        - ## Overview
          - Brief description of what this guide helps accomplish
          - Who it's for and when they might need it
        - ## Prerequisites
          - What the reader needs before starting
          - Tools, knowledge, or resources required
        - ## Steps
          - ### 1. First Step
            - Details and guidance
            - Screenshots or examples if helpful
          - ### 2. Second Step
            - And so on...
        - ## Troubleshooting
          - Common issues and their solutions
        - ## Related
          - Links to related pages: [[Page1]], [[Page2]]
      ```
      
      ## Naming Convention and File Paths
      
      Use the namespace pattern: `Topic/Subtopic/How To/Specific Task`
      
      Examples:
      - `[[Programming/Python/How To/Set Up a Virtual Environment]]`
      - `[[PKM/Logseq/How To/Create a Template]]`
      
      In Logseq, namespaces using `/` are translated into file paths using triple underscores `___`. For example:
      
      - The page `[[Programming/Python/How To/Set Up a Virtual Environment]]` will be stored as:
        `pages/Programming___Python___How To___Set Up a Virtual Environment.md`
      
      - The page `[[PKM/Logseq/How To/Create a Template]]` will be stored as:
        `pages/PKM___Logseq___How To___Create a Template.md`
      
      ## Required Tags
      
      **IMPORTANT**: All Diataxis How-To pages MUST include the `[[Diataxis/How To]]` tag in the frontmatter.
      
      - If the page already has tags, add `[[Diataxis/How To]]` to the existing tags list
      - Example: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/How To]]`
      - If the page has no tags yet, add: `tags:: [[Diataxis/How To]]`
      - Never remove existing tags when adding the Diataxis tag
      
      ## Research Process
      
      If creating a How-To guide on a topic that requires research:
      
      1. Add a `- ### Research` section containing findings
      2. Clearly indicate uncertain information
      3. Ask the human collaborator specific questions to clarify scope
      4. Co-author the guide with the human, one section at a time
      
      ## Language Guidelines
      
      - Use conditional imperatives: "If you want X, do Y"
      - Start with clear action verbs: "Install", "Configure", "Create", etc.
      - Use present tense and active voice
      - Keep sentences concise and focused on the action
      - Avoid unnecessary explanations - link to explanation pages instead

examples:
  - input: |
      tags:: [[Python]], [[macOS]], [[Installation]], [[Diataxis/How To]]
      
      - # How To Install Python on macOS
        - ## Overview
          - This guide walks you through installing Python on macOS
          - For developers and users who need Python for their projects
        - ## Prerequisites
          - macOS 10.15 or later
          - Admin access to your computer
        - ## Steps
          - ### 1. Check Existing Installation
            - Open Terminal
            - Run `python --version` or `python3 --version`
          - ### 2. Install Homebrew (if not installed)
            - Run `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
          - ### 3. Install Python via Homebrew
            - Run `brew install python`
        - ## Troubleshooting
          - If you see "command not found": Ensure Homebrew is in your PATH
        - ## Related
          - [[Programming/Python/How To/Set Up a Virtual Environment]]
          - [[Programming/Tools/Homebrew]]
    output: "Correctly formatted Diataxis How-To guide in Logseq with proper tags"

metadata:
  priority: high
  version: 1.0
  related_rules: ["logseq-flavored-markdown.mdc"]
</rule>

## Implementation Guide

When implementing a Diataxis How-To guide in Logseq, follow these steps:

1. **Identify a specific task or problem** that needs solving
   - Focus on concrete, practical goals
   - Choose tasks that are meaningful to users
   - Ask: "What specific problem does this guide help solve?"

2. **Create the page with the proper namespace**
   - Use `Topic/Subtopic/How To/Specific Task` format
   - This will create a file at `pages/Topic___Subtopic___How To___Specific Task.md`
   - The triple underscore `___` is how Logseq translates namespace hierarchies into file paths

3. **Add the required tags**
   - Always include `[[Diataxis/How To]]` in the tags frontmatter
   - Place tags at the very top of the file, before any content
   - Format: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/How To]]`
   - Never remove existing tags when adding the Diataxis tag

4. **Follow the Logseq-Flavored Markdown format**
   - See [logseq-flavored-markdown.mdc](mdc:.cursor/rules/logseq-flavored-markdown.mdc) for detailed formatting rules
   - Remember all content must be prefixed with bullet points (`-`)
   - Use proper indentation with TAB characters
   - No blank lines between bullet points

5. **Structure the content**
   - Start with a clear title: `- # How To [Specific Task]`
   - Include all required sections (Overview, Prerequisites, Steps, etc.)
   - Make steps sequential and logical
   - Number steps for clarity: `- ### 1. First Step`

6. **Focus on action and guidance**
   - Use imperative language: "Run", "Click", "Enter", etc.
   - Provide enough context for each step
   - Include expected outcomes where helpful
   - Use conditional imperatives: "If you want X, do Y"

7. **Omit unnecessary information**
   - Link to explanations rather than including them
   - Keep reference material separate
   - Focus on the task at hand
   - Remember: How-To guides are about doing, not understanding

8. **Test the guide**
   - Follow your own instructions to verify accuracy
   - Update as needed based on feedback

## The Diataxis Compass for How-To Guides

The Diataxis framework provides a "compass" to help identify what type of documentation you're creating:

| If the content... | ...and serves the user's... | ...then it belongs to... |
|-------------------|------------------------------|--------------------------|
| informs action    | application of skill         | a how-to guide           |

How-To guides:
- Inform action (not cognition)
- Serve the application (not acquisition) of skill
- Are goal-oriented (not learning-oriented)
- Focus on practical tasks (not theoretical understanding)

Remember that a good How-To guide serves as a reliable reference that users can return to whenever they need to accomplish the specific task. It should be clear, concise, and focused on helping the user achieve their goal with minimal distractions.
