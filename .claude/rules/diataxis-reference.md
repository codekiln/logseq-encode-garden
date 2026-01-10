# Diataxis Reference Guide Format for Logseq

This rule provides guidance on creating Reference documentation in Logseq following the Diataxis documentation framework principles.

<rule>
name: diataxis_reference_format
description: Guidelines for creating effective Reference documentation in Logseq following the Diataxis framework
filters:
  - type: file_path
    pattern: ".*Ref.*\\.md$"

actions:
  - type: suggest
    message: |
      # Creating Diataxis Reference Documentation in Logseq

      ## Purpose
      
      Reference documentation provides **technical descriptions** of a product and how to use it effectively. Reference material is **information-oriented** and serves as a reliable source of truth.
      
      According to the Diataxis framework, Reference documentation:
      - Contains propositional or theoretical knowledge that users consult during practical work
      - Describes the product as succinctly and clearly as possible, in an orderly and systematic way
      - Is led by the structure and nature of the product it describes (unlike tutorials and how-to guides)
      - Provides users with certainty and confidence—firm platforms on which to stand while they work
      
      ## Key Principles
      
      1. **Describe and Only Describe** - Neutral description is the key imperative
      2. **Adopt Standard Patterns** - Reference material is most useful when consistent
      3. **Respect the Structure of the Product** - Mirror the logical organization of what you're documenting
      4. **Provide Examples** - Illustrate usage without falling into explanation or instruction
      5. **Be Austere** - Users consult reference material rather than read it from beginning to end
      6. **Be Authoritative** - No doubt or ambiguity; wholly reliable and definitive
      
      ## Structure for Logseq Reference Documentation
      
      When creating Reference documentation in Logseq, follow this structure using Logseq-Flavored Markdown (LFM):
      
      ```
      tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Reference]]
      
      - # [Topic Name] Reference
        - ## Overview
          - Brief, factual description of what this reference documents
          - Scope and boundaries of the reference material
        - ## Structure
          - How the reference is organized (if needed)
          - Any conventions used throughout the document
        - ## Core Components
          - ### Component 1
            - Precise, factual description
            - Technical specifications
            - Parameters, properties, or attributes
            - Examples of usage
          - ### Component 2
            - And so on...
        - ## Technical Details
          - Specifications, constraints, and requirements
          - Version information (if applicable)
          - Dependencies and relationships
        - ## Related References
          - Links to related reference pages: [[Page1/Ref/Topic]], [[Page2/Ref/Topic]]
      ```
      
      ## Naming Convention and File Paths
      
      Use the namespace pattern: `Topic/Subtopic/Ref/Specific Subject`
      
      Examples:
      - `[[API/Endpoints/Ref/Authentication]]`
      - `[[Unicode/Block/Ref/Symbols for Legacy Computing]]`
      
      In Logseq, namespaces using `/` are translated into file paths using triple underscores `___`. For example:
      
      - The page `[[API/Endpoints/Ref/Authentication]]` will be stored as:
        `pages/API___Endpoints___Ref___Authentication.md`
      
      - The page `[[Unicode/Block/Ref/Symbols for Legacy Computing]]` will be stored as:
        `pages/Unicode___Block___Ref___Symbols for Legacy Computing.md`
      
      ## Required Tags
      
      **IMPORTANT**: All Diataxis Reference pages MUST include the `[[Diataxis/Reference]]` tag in the frontmatter.
      
      - If the page already has tags, add `[[Diataxis/Reference]]` to the existing tags list
      - Example: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Reference]]`
      - If the page has no tags yet, add: `tags:: [[Diataxis/Reference]]`
      - Never remove existing tags when adding the Diataxis tag
      
      ## Language Guidelines
      
      - Use neutral, objective language
      - Focus on facts, not opinions or interpretations
      - Present information in a consistent format
      - Use present tense for descriptions
      - Be precise and unambiguous
      - Avoid instructional language ("do this," "follow these steps")
      - Separate description from explanation (link to explanation pages instead)
      
      ## Common Pitfalls to Avoid
      
      - Mixing reference with tutorials or how-to content
      - Including opinions, speculation, or marketing language
      - Using inconsistent formats or structures
      - Assuming auto-generated reference is sufficient documentation
      - Failing to update reference when the product changes

examples:
  - input: |
      tags:: [[Unicode]], [[Character Sets]], [[Diataxis/Reference]]
      
      - # Unicode Block Reference: Symbols for Legacy Computing
        - ## Overview
          - The Symbols for Legacy Computing block (U+1FB00–U+1FBFF) contains 128 characters
          - Added to Unicode in version 13.0 (2020)
          - Contains graphical characters for compatibility with legacy computing platforms
        - ## Structure
          - Characters are organized by visual similarity and original platform
          - Hexadecimal code points are used for precise identification
        - ## Core Components
          - ### Block Elements (U+1FB00–U+1FB3B)
            - 60 characters for block drawing and pixel art
            - Compatible with CP437 and similar encodings
            - Example: U+1FB00 '▘' BLOCK SEXTANT-1
          - ### Teletext Elements (U+1FB3C–U+1FB6F)
            - 52 characters for teletext/videotex graphics
            - Compatible with NAPLPS and similar standards
            - Example: U+1FB3C '🬼' BLOCK SEXTANT-121
        - ## Technical Details
          - All characters have East Asian Width property: Neutral (N)
          - General Category: Symbol, Other (So)
          - Bidirectional Class: Other Neutral (ON)
        - ## Related References
          - [[Unicode/Block/Ref/Block Elements]]
          - [[Unicode/Block/Ref/Geometric Shapes]]
    output: "Correctly formatted Diataxis Reference documentation in Logseq with proper tags"

metadata:
  priority: high
  version: 1.0
  related_rules: ["logseq-flavored-markdown"]
</rule>

## Implementation Guide

When implementing Diataxis Reference documentation in Logseq, follow these steps:

1. **Identify the subject that needs reference documentation**
   - Focus on technical aspects that users need to look up
   - Choose subjects that benefit from structured, factual documentation
   - Ask: "What information will users need to consult while working with this?"

2. **Create the page with the proper namespace**
   - Use `Topic/Subtopic/Ref/Specific Subject` format
   - This will create a file at `pages/Topic___Subtopic___Ref___Specific Subject.md`
   - The triple underscore `___` is how Logseq translates namespace hierarchies into file paths

3. **Add the required tags**
   - Always include `[[Diataxis/Reference]]` in the tags frontmatter
   - Place tags at the very top of the file, before any content
   - Format: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Reference]]`
   - Never remove existing tags when adding the Diataxis tag

4. **Follow the Logseq-Flavored Markdown format**
   - All content must be prefixed with bullet points (`-`)
   - Use proper indentation with TAB characters
   - No blank lines between bullet points
   - Use headings to create a clear structure

5. **Structure the content to mirror the product**
   - Organize reference material to reflect the logical structure of what you're documenting
   - Group related items together in a way that makes sense for the subject
   - Use consistent naming and formatting throughout

6. **Focus on description, not instruction**
   - Use neutral, factual language
   - Describe what things are, not how to use them
   - Provide examples that illustrate usage without instructing
   - Be comprehensive but concise

7. **Maintain consistency**
   - Use the same format for similar types of information
   - Present technical details in a standardized way
   - Create patterns that users can recognize and rely on
   - Be consistent with terminology and naming

8. **Review for accuracy and completeness**
   - Verify all technical details
   - Ensure the reference covers the full scope of the subject
   - Update when the underlying product changes

## The Diataxis Compass for Reference Documentation

The Diataxis framework provides a "compass" to help identify what type of documentation you're creating:

| If the content... | ...and serves the user's... | ...then it belongs to... |
|----|---|-----|
| informs cognition | theoretical knowledge        | reference                |

Reference documentation:
- Informs cognition (not action)
- Serves theoretical knowledge (not practical application)
- Is information-oriented (not task-oriented)
- Focuses on describing the product (not guiding the user)

Remember that good reference documentation serves as a reliable source of truth that users can consult whenever they need factual information about the product. It should be authoritative, structured, and focused on providing clear, accurate descriptions without distracting explanations or instructions.

## Characteristics of Good Reference Documentation

- **Austere**: One consults reference material rather than reads it from beginning to end
- **Authoritative**: No doubt or ambiguity; wholly reliable and definitive
- **Map-like**: Tells you what you need to know without having to explore for yourself
- **Structured**: Organized according to the logical structure of what it describes

## Real-World Analogy

Reference documentation is similar to information on food packaging or product specifications:
- Users expect standardized presentation of facts in a predictable format
- Information should be reliable, consistent, and clearly separated from marketing or instructional content
- The importance of reference is such that in many fields it's governed by standards or regulations
