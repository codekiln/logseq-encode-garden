---
targets:
  - '*'
description: Logseq-Flavored Markdown (LFM) Book Import
---
# How a Book is tracked in this Logseq knowledge garden
This is an extension to logseq-flavored-markdown `logseq-flavored-markdown.mdc` for recording information about a book.

A book entry is a logseq page where the page title matches one of the following patterns:
- [[Book/Title]] (corresponds to `pages/Book___Title.md`)
- [[Person/Author/Book/Year/Title]] (corresponds to `pages/Person___Author___Book___Year___Title.md`)

### When to Create a Book Page

Book pages should be created for:
- Books you've read or are reading
- Books you want to reference or take notes on
- Books relevant to your areas of interest or study
- Books you want to annotate or extract quotes from

### Creating a Book Page

If you are asked to make an entry for a book, you should:

1. **Search First**
   - Search in `pages/Book___*.md` and in any file matching `pages/Person___*___Book___*___*.md` to find if the book already exists
   - If it already exists, then you should **update** the existing entry
   - A single book should not have more than one primary book page

2. **Create/Update Page**
   - For a general book reference, create it under `[[Book/Title]]` by default
   - For a book authored by a known person in your knowledge graph, use `[[Person/Author/Book/Year/Title]]` format
   - Add appropriate frontmatter using `:::` syntax (not `::`)
   - Include all available metadata:
     - `alias::` for alternative names/references
     - `created-by::` to link to author page(s)
     - `tags::` with relevant tags, including `[[Book]]`
     - `goodreads-link::` for Goodreads URL if available
     - `published::` for publication date if known
     - `isbn::` for ISBN if available

3. **Book Content Structure**
   - Start with a heading: `- # [Book Title](url-to-book)`
   - Include book cover image if available
   - Add a brief description or summary
   - Include table of contents or chapter notes as appropriate
   - Use bullet hierarchy for your notes and annotations
   - Group related annotations by chapter or theme
   - Add quotes using blockquote syntax: `- > Quote text`

4. **External Resources**
   - Link to related resources like:
     - Author's website
     - Publisher's page
     - Source code repository (for technical books)
     - Reviews or discussions
     - Related books or articles

5. **Journal Entry**
   - If the book page is new, make an entry in today's journal page that links to that book
   - Consider adding context about why you're adding this book to your knowledge garden

### Book Annotation Conventions

When annotating books:
1. **Hierarchy**:
   - Use bullet hierarchy to organize notes
   - Chapter headings as H2 (`- ## Chapter Title`)
   - Important concepts as H3 (`- ### Concept`)

2. **Quotes**:
   - Format direct quotes with blockquote: `- > Quote text`
   - Include page numbers when available: `- > Quote text (p. 42)`

3. **Personal Notes**:
   - Distinguish your thoughts from the book's content
   - Consider using a personal note indicator: `- **Note**: My thoughts about this...`

4. **Connections**:
   - Link to related concepts in your knowledge garden
   - Create links to authors, concepts, and related books

5. **Visual Elements**:
   - Add diagrams or images from the book when helpful
   - Use code blocks for code examples: ````source-code```

### Examples

<CORRECT_✅>
```markdown
alias:: [[The Art of Programming]], [[Person/Jane Doe/Book/2023/The Art of Programming]]
created-by:: [[Person/Jane Doe]]
goodreads-link:: https://www.goodreads.com/book/show/example-book
tags:: [[Book]], [[Programming]], [[Software Development]]
isbn:: 978-0123456789

- # [The Art of Programming](https://publisher.com/book)
  - ![Book Cover](../assets/art_of_programming_cover.jpg)
  - > "A comprehensive guide to programming principles and practices" - Publisher description
  - ## Chapter 1: Fundamentals
    - ### Core Concepts
      - Key points about programming fundamentals
      - > "Programming is the art of telling another human what one wants the computer to do." (p. 15)
    - ### Examples
      - ```python
        def hello_world():
            print("Hello, World!")
        ```
  - ## Chapter 2: Advanced Topics
    - Notes on advanced programming concepts
```
</CORRECT_✅>