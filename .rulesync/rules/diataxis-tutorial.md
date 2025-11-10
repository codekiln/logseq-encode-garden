---
root: false
targets:
  - '*'
description: ''
globs: ['{journals,pages}/*.md']
---
# How to create a Diataxis Tutorial page in the Knowledge Garden

# Diataxis Tutorial Guide Format for Logseq

This rule provides guidance on creating Tutorial documentation in Logseq following the Diataxis documentation framework principles.

<rule>
name: diataxis_tutorial_format
description: Guidelines for creating effective Tutorial documentation in Logseq following the Diataxis framework
filters:
  - type: file_path
    pattern: ".*Tutorial.*\\.md$"

actions:
  - type: suggest
    message: |
      # Creating Diataxis Tutorial Documentation in Logseq

      ## Purpose
      
      Tutorials are **learning-oriented** guides that provide a hands-on experience. A tutorial is a lesson that:
      - Takes the learner through meaningful, practical steps
      - Focuses on learning by doing
      - Builds confidence through successful completion
      - Minimizes explanation in favor of action
      
      ## Key Principles
      
      1. **Focus on Learning** - Help users acquire new skills through guided practice
      2. **Show Early Results** - Deliver visible achievements frequently
      3. **Minimize Explanation** - Keep focus on doing; link to explanations elsewhere
      4. **Ensure Success** - Every step must work reliably for every user
      5. **Be Concrete** - Use specific examples, avoid abstractions
      6. **Guide Completely** - Take full responsibility for the learner's success
      
      ## Structure for Logseq Tutorial Documentation
      
      When creating Tutorial documentation in Logseq, follow this structure using Logseq-Flavored Markdown (LFM):
      
      ```
      tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Tutorial]]
      
      - # Tutorial: [Learning Goal]
        - ## What You'll Create
          - Brief description of the end result
          - Screenshot or example of the finished product
        - ## Prerequisites
          - Required tools or knowledge
          - Setup steps if needed
        - ## Learning Goals
          - What skills they'll acquire
          - What they'll be able to do afterward
        - ## Steps
          - ### 1. First Achievement
            - Clear, concrete instructions
            - Expected results
            - What to notice
          - ### 2. Second Achievement
            - And so on...
        - ## What You've Learned
          - Recap of skills acquired
          - Next steps for practice
        - ## Related
          - Links to related pages: [[Page1]], [[Page2]]
      ```
      
      ## Naming Convention and File Paths
      
      Use the namespace pattern: `Topic/Subtopic/Tutorial/Learning Goal`
      
      Examples:
      - `[[Programming/Python/Tutorial/Build Your First Web App]]`
      - `[[PKM/Logseq/Tutorial/Create a Daily Notes Workflow]]`
      
      In Logseq, namespaces using `/` are translated into file paths using triple underscores `___`. For example:
      
      - The page `[[Programming/Python/Tutorial/Build Your First Web App]]` will be stored as:
        `pages/Programming___Python___Tutorial___Build Your First Web App.md`
      
      ## Required Tags
      
      **IMPORTANT**: All Diataxis Tutorial pages MUST include the `[[Diataxis/Tutorial]]` tag in the frontmatter.
      
      - If the page already has tags, add `[[Diataxis/Tutorial]]` to the existing tags list
      - Example: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Tutorial]]`
      - If the page has no tags yet, add: `tags:: [[Diataxis/Tutorial]]`
      - Never remove existing tags when adding the Diataxis tag
      
      ## Language Guidelines
      
      - Use "we" to establish teacher-learner relationship: "We will create..."
      - Use present tense and active voice
      - Provide clear expectations: "You will see..."
      - Point out important observations: "Notice that..."
      - Keep explanations minimal and link to reference material
      - Focus on concrete actions and results
      
      ## Tutorial Writing Process
      
      1. **Plan the Learning Journey**
         - Identify specific skills to be learned
         - Break down into small, achievable steps
         - Ensure each step produces visible results
      
      2. **Write the Tutorial**
         - Start with clear learning goals
         - Focus on concrete actions
         - Include expected results
         - Point out what to notice
      
      3. **Test the Tutorial**
         - Follow your own instructions exactly
         - Verify each step works reliably
         - Check that results match expectations
      
      4. **Review and Refine**
         - Remove unnecessary explanations
         - Add missing steps if needed
         - Ensure consistent success

examples:
  - input: |
      tags:: [[Python]], [[Web Development]], [[Diataxis/Tutorial]]
      
      - # Tutorial: Build Your First Flask Web App
        - ## What You'll Create
          - A simple web application that displays a greeting
          - Screenshot of finished application
        - ## Prerequisites
          - Python 3.8 or later installed
          - Basic familiarity with terminal/command prompt
        - ## Learning Goals
          - Create a basic Flask application
          - Run a local development server
          - Handle web requests
        - ## Steps
          - ### 1. Set Up Your Environment
            - Open your terminal
            - Create a new directory: `mkdir my-flask-app`
            - Move into it: `cd my-flask-app`
          - ### 2. Create Your First Route
            - Create app.py with this code:
              ~~~python
              from flask import Flask
              app = Flask(__name__)
              
              @app.route('/')
              def hello():
                  return 'Hello, World!'
              ~~~
            - Notice how we import Flask and create an application
          - ### 3. Run Your Application
            - In the terminal, run: `flask run`
            - You'll see a message that your server is running
            - Open http://localhost:5000 in your browser
        - ## What You've Learned
          - How to create a basic Flask application
          - How to define a route
          - How to run a development server
        - ## Related
          - [[Programming/Python/Tutorial/Add Database to Flask App]]
          - [[Programming/Web/How To/Deploy Flask to Production]]
    output: "Correctly formatted Diataxis Tutorial in Logseq with proper tags"

metadata:
  priority: high
  version: 1.0
  related_rules: ["logseq-flavored-markdown"]
</rule>

## Implementation Guide

When implementing Diataxis Tutorial documentation in Logseq, follow these steps:

1. **Plan the Learning Experience**
   - Identify what specific skills need to be learned
   - Break down into small, achievable steps
   - Ensure each step produces visible results
   - Focus on concrete actions over abstract concepts

2. **Create the page with the proper namespace**
   - Use `Topic/Subtopic/Tutorial/Learning Goal` format
   - This will create a file at `pages/Topic___Subtopic___Tutorial___Learning Goal.md`
   - The triple underscore `___` is how Logseq translates namespace hierarchies into file paths

3. **Add the required tags**
   - Always include `[[Diataxis/Tutorial]]` in the tags frontmatter
   - Place tags at the very top of the file, before any content
   - Format: `tags:: [[ExistingTag1]], [[ExistingTag2]], [[Diataxis/Tutorial]]`
   - Never remove existing tags when adding the Diataxis tag

4. **Structure the content**
   - Follow the Logseq-Flavored Markdown format
   - Use bullet points (`-`) for all content
   - Use proper indentation with TAB characters
   - Include all required sections (What You'll Create, Prerequisites, etc.)

5. **Write with the learner in mind**
   - Use "we" to establish the teacher-learner relationship
   - Keep explanations minimal
   - Focus on concrete actions and results
   - Point out what to notice
   - Provide clear expectations

6. **Test thoroughly**
   - Follow your own instructions exactly
   - Verify each step works reliably
   - Check that results match expectations
   - Test with different users if possible

Remember that a good tutorial:
- Takes full responsibility for the learner's success
- Provides a reliable, repeatable experience
- Builds confidence through early and frequent achievements
- Focuses on concrete actions over abstract concepts
