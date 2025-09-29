---
targets:
  - '*'
root: false
description: How to create a Diataxis Explanation page
globs: []
cursor:
  alwaysApply: false
  description: How to create a Diataxis Explanation page
---
# Diataxis Explanation Guide Format for Logseq

This rule provides guidance on creating Explanation documentation in Logseq following the Diataxis documentation framework principles.

<rule>
name: diataxis_explanation_format
description: Guidelines for creating effective Explanation documentation in Logseq following the Diataxis framework
filters:
  - type: file_path
    pattern: ".*Concept.*\\.md$|.*Explanation.*\\.md$"

actions:
  - type: suggest
    message: |
      # Creating Diataxis Explanation Documentation in Logseq

      ## Purpose
      
      Explanations are **understanding-oriented** guides that help users grasp concepts, ideas, and principles. They focus on building comprehension and insight rather than teaching specific skills or providing reference information.
      
      According to the Diataxis framework, Explanations:
      - Help users understand concepts, ideas, and principles
      - Build comprehension and insight
      - Focus on "why" and "how" rather than "what" or "when"
      - Provide context and reasoning behind decisions and approaches
      - Help users think about problems and solutions
      
      ## Key Principles
      
      1. **Focus on Understanding** - Help users grasp concepts and principles
      2. **Provide Context** - Explain the "why" behind concepts and decisions
      3. **Build Insight** - Help users think about problems and solutions
      4. **Use Examples** - Illustrate concepts with concrete examples
      5. **Address Misconceptions** - Clarify common misunderstandings
      6. **Link to Related Content** - Connect to tutorials, how-to guides, and reference material
      
      ## Structure for Logseq Explanation Documentation
      
      When creating Explanation documentation in Logseq, follow this structure using Logseq-Flavored Markdown (LFM):
      
      ```
      tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Explanation]]
      
      - # [Topic Name] Conceptual Overview
        - ## Overview
          - Brief, clear description of the concept or topic
          - What it is and why it matters
        - ## Context
          - Historical background or current relevance
          - Why this concept exists or is important
          - Related problems or challenges it addresses
        - ## Key Principles
          - Core ideas and fundamental concepts
          - Important distinctions and relationships
          - Guiding principles or philosophies
        - ## Mechanism
          - How the concept works in practice
          - Technical details and implementation approaches
          - Components and their interactions
        - ## Examples
          - Concrete examples that illustrate the concept
          - Code snippets, diagrams, or case studies
          - Real-world applications
        - ## Misconceptions
          - Common misunderstandings about the concept
          - Clarifications and corrections
          - What it is NOT
        - ## Related
          - Links to related pages: [[Page1]], [[Page2]]
      ```
      
      ## Naming Convention and File Paths
      
      Use the namespace pattern: `Topic/Subtopic/Concept/Specific Subject`
      
      **Note**: Following the official Diataxis framework, explanation titles should be able to be prefixed with "About". For example: "About Virtual Environments" or "About User Authentication". This reflects that explanations are _about_ a topic in the sense that they are _around_ it.
      
      Examples:
      - `[[Programming/Python/Concept/Virtual Environments]]` (About Virtual Environments)
      - `[[AI/Machine Learning/Concept/Overfitting]]` (About Overfitting)
      
      In Logseq, namespaces using `/` are translated into file paths using triple underscores `___`. For example:
      
      - The page `[[Programming/Python/Concept/Virtual Environments]]` will be stored as:
        `pages/Programming___Python___Concept___Virtual Environments.md`
      
      - The page `[[AI/Machine Learning/Concept/Overfitting]]` will be stored as:
        `pages/AI___Machine Learning___Concept___Overfitting.md`
      
      ## Required Tags
      
      **IMPORTANT**: All Diataxis Explanation pages MUST include the `[[Diataxis/Explanation]]` tag in the frontmatter.
      
      - If the page already has tags, add `[[Diataxis/Explanation]]` to the existing tags list
      - Example: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Explanation]]`
      - If the page has no tags yet, add: `tags:: [[Diataxis/Explanation]]`
      - Never remove existing tags when adding the Diataxis tag
      
      ## Language Guidelines
      
      - Use clear, accessible language
      - Explain concepts step by step
      - Use analogies and metaphors when helpful
      - Provide concrete examples
      - Address common questions and misconceptions
      - Link to related tutorials, how-to guides, and reference material
      - Focus on building understanding rather than providing instructions
      
      ## Explanation Writing Process
      
      1. **Identify the Core Concept**
         - What fundamental idea needs to be understood?
         - What misconceptions commonly arise?
         - What context is needed for comprehension?
      
      2. **Structure the Explanation**
         - Start with a clear overview
         - Provide necessary context
         - Explain key principles
         - Show how it works in practice
         - Include concrete examples
         - Address misconceptions
      
      3. **Test for Understanding**
         - Can someone new to the topic follow the explanation?
         - Are common misconceptions addressed?
         - Are examples clear and relevant?
         - Does it build toward deeper understanding?

examples:
  - input: |
      tags:: [[Python]], [[Programming]], [[Diataxis/Explanation]]
      
      - # Python Virtual Environments Conceptual Overview
        - ## Overview
          - Virtual environments are isolated Python environments that allow you to manage dependencies for different projects without conflicts.
        - ## Context
          - Python packages are installed globally by default, leading to version conflicts between projects.
          - Virtual environments solve this by creating isolated spaces with their own Python interpreter and package installations.
        - ## Key Principles
          - *Isolation* – Each environment has its own Python interpreter and packages
          - *Reproducibility* – Dependencies can be exactly specified and reproduced
          - *Project-specific* – Each project can have its own environment
        - ## Mechanism
          - Virtual environments create a directory with a Python interpreter and site-packages
          - The `venv` module creates environments: `python -m venv myenv`
          - Activation modifies PATH to use the environment's Python
          - `pip` installs packages into the active environment
        - ## Examples
          - ~~~bash
            # Create and activate a virtual environment
            python -m venv myproject
            source myproject/bin/activate  # On Unix/macOS
            pip install requests
            ~~~
        - ## Misconceptions
          - Virtual environments are only for large projects → **False**. Even small projects benefit from isolation.
          - You need to recreate environments frequently → **False**. Environments persist until deleted.
        - ## Related
          - [[Programming/Python/How To/Create Virtual Environment]]
          - [[Programming/Python/Ref/Pip Commands]]
    output: "Correctly formatted Diataxis Explanation in Logseq with proper tags"

metadata:
  priority: high
  version: 1.0
  related_rules: ["logseq-flavored-markdown.mdc"]
</rule>

## Implementation Guide

When implementing Diataxis Explanation documentation in Logseq, follow these steps:

1. **Identify the concept that needs explanation**
   - Focus on ideas that benefit from deeper understanding
   - Choose concepts that are commonly misunderstood
   - Ask: "What fundamental understanding will help users work more effectively?"

2. **Create the page with the proper namespace**
   - Use `Topic/Subtopic/Concept/Specific Subject` format
   - This will create a file at `
