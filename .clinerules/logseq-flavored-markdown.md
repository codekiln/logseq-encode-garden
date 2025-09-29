# Formatting Logseq-Flavored Markdown (LFM)

Note: these markdown rules are not itself in LFM (though it does contain examples of valid LFM)

### ⚠️ CRITICAL: DO NOT MODIFY FRONTMATTER TAGS ⚠️

- **NEVER** modify, add, or remove the `tags::` frontmatter item specifically
- The `tags::` frontmatter (e.g., `tags:: [[MyTagHere]], [[MySecondTagHere]]`) is strictly protected
- Even if you think a tag is missing or incorrect, DO NOT change the `tags::` frontmatter
- This restriction applies ONLY to the `tags::` frontmatter item, not to other page attributes
- Other page-level attributes may be modified when explicitly instructed to do so
- Do not confuse this instruction with inline tags in the document body (e.g., `#MyTag`)
- This is a strict requirement - modifying frontmatter tags will disrupt the user's categorization system

### Basic Structure

- Logseq uses a hierarchical bullet-point structure.
- TAB Indentation determines the relationship between parent and child blocks. 
- IMPORTANT: All content, including headings, must be prefixed with bullet points (`-`)
- IMPORTANT: Indentations should use the TAB character.
- Headings are created using `#`, with more `#` indicating deeper nesting
- Heading format: `- # Heading Text` (note the bullet point before the #)
- Content should be nested logically under the appropriate headings
  - H2 (##) should be "under" H1 (#)
  - H3 (###) should be "under" H2 (##)
  - ... 
  - H<n> should be "under H<n-1>
- DO NOT blank newlines in the document. Each line in the whole file should have content. At the very least, a line should contain a `-`.

#### Example

<CORRECT_✅>
~~~markdown

- # Main Topic
  - ## Overview
    - ### Basic Idea
      - Sub-detail A
    - Detail 2
- # Next Topic
  - First point under next topic

~~~
<CORRECT_✅>

The following example is incorrect because it lacks indentation, unordered list items, and puts newlines between headings:
<INCORRECT_❌>
~~~markdown

# Main Topic

## Overview

### Basic Idea
- Sub-detail A
- Detail 2

# Next Topic
- Another point

~~~
</INCORRECT_❌>


### Namespaces / Hierarchy

- Logseq supports namespaces using `/` to create hierarchical page structures.
- Namespaces help organize related content under broader categories.
- Pages with namespaces are stored as a single file but visually represented as a hierarchy.
- In the filesystem, Logseq replaces `/` with `___`, storing namespaced pages as single markdown files.
- It's important that you not invent namespace links that don't already exist, to avoid polluting the knowledge garden with duplicate content.

**Example:**

```markdown
[[Project/Tasks]]
[[Work/Meetings/2024]]
```

- The above will be interpreted as:

  - `Project` → `Tasks`
  - `Work` → `Meetings` → `2024`

- In the filesystem, these pages would be saved as:

  - `Project___Tasks.md`
  - `Work___Meetings___2024.md`

### **Special Formatting**

- **Bold:** `**bold text**`
- *Italic:* `*italic text*`
- `Inline code:` `` `code` ``
- Blockquotes: `> Quote`
- Code Blocks:
  ```markdown
  ~~~
  $> git describe --tags  
  ~~~
  ```

### Page-level attributes in Logseq

**CRITICAL: NEVER modify the `tags::` frontmatter item in any document.** The user has a specific tagging system that follows particular rules not documented here. Any modification to the `tags::` frontmatter will disrupt their categorization system. Always preserve existing frontmatter tags exactly as they appear.

Other page-level attributes may be modified when explicitly instructed to do so, but the `tags::` frontmatter must remain untouched.

Page-level attributes or Logseq Frontmatter 
- MUST occur as the first lines in the markdown file before an unordered list item
- MUST use kebob-case
- separation between key and value is with `:: `
- The `tags::` frontmatter item specifically **MUST NOT be modified, added, or removed** under any circumstances

<CORRECT_✅>
~~~markdown
tags:: [[Q]], [[nvm]], [[npx]]
other-attribute:: some value
- # Main Topic
...
~~~
<CORRECT_✅>

The following example is incorrect because it tries to put page level attributes as the first list item in the document: 
<INCORRECT_❌>
~~~markdown
- tags:: Q, topicA
- # Main Topic
...
~~~
</INCORRECT_❌>

The following example is incorrect because it does not use `:: ` to separate the key-value pairs:
<INCORRECT_❌>
~~~markdown
tags: Q, topicA
- # Main Topic
...
~~~
</INCORRECT_❌>



### Fenced Code Blocks Rule

- When nesting fenced code blocks in markdown, avoid using triple-backticks inside another triple-backtick block.
- Use triple-backticks for the outer markdown block and triple-tilde (`~~~`) for inner code blocks.
- This prevents rendering issues and aligns with the CommonMark spec.
- See also  which is a duplicate of this rule that also applies to .mdc files

**Example:**

```markdown
- Here's an example of the code:
  ~~~
  $> git describe --tags  
  ~~~
```

### There are no ordered list items in Logseq Flavored Markdown 
... but you can use numbers as the first item in an unordered list item.
REMEMBER to use TAB character for identing before the `-`

<INCORRECT_❌>
- # how to do something
  - subheading:
    1. do the first thing
    2. do the second thing
	  3. do the third thing
</INCORRECT_❌>


<CORRECT_✅>
- # how to do something
	- subheading:
	  - 1. do the first thing
	  - 2. do the second thing
	  - 3. do the third thing
</CORRECT_✅>