---
targets:
  - '*'
description: Import a blog post, article, or essay into the knowledge garden using ENTITY/Blog|Article|Essay/YY/MM/slug convention with created-by and type tag
argument-hint: Source URL (optional); entity and slug can be prompted if omitted
---
# Import Blog Post, Article, or Essay

This command imports a **blog post**, **article**, or **essay** into the Logseq knowledge garden as a new page. Use it for any of these; the only difference is the type segment in the namespace: **Blog**, **Article**, or **Essay**. An article or essay is treated as a one-off post (same structure, same date namespacing). It follows the namespace convention **[[Entity/Type/YY/MM/slug]]** and uses standard frontmatter. See [[Logseq/Best Practice/Utilize Date Namespacing Under Entity Name]].

## Variables

- `{url}` - **Optional**: Source URL of the post. If omitted, the user will be prompted for the URL or content source.
- Entity (person, company, or technology), **type** (Blog, Article, or Essay), and slug are inferred from the source or prompted when not clear.

## Namespace Convention

- Use **`<person_or_company_or_technology>/<Type>/<YY>/<MM>/<slug>`** where **Type** is one of:
  - **Blog** – recurring or blog-style posts.
  - **Article** – one-off article (e.g. magazine, publication, standalone piece).
  - **Essay** – one-off essay (e.g. long-form, opinion, standalone piece).
- **YY** = two-digit year (e.g. `26` for 2026). **MM** = two-digit month (e.g. `02` for February).
- **Slug** = short, URL-friendly title (lowercase, hyphens, no special chars where possible).
- **File naming**: Convert namespace slashes to triple underscores for the filename (e.g. `Person___Simon Willison___Blog___26___02___Introducing Showboat.md` or `Person___Jane Doe___Article___26___02___My One-Off Piece.md`).

## Workflow

### Step 1: Identify Source, Entity, and Type

- If the user provided a URL, fetch or use the content to determine title and author/source.
- If no URL was provided, ask the user for the post URL or paste/content.
- Determine the **entity** that owns the piece:
  - **Person**: e.g. `Person/Simon Willison`, `Person/Zack Steinkamp`. Search first per `[[Logseq/Entity/person]]` (and **logseq-entity** skill / `logseq-person` router) to avoid duplicate person hubs; use the canonical person page name when linking.
  - **Company or technology**: e.g. `Anthropic`, `CrowdStrike`, `LangChain`, `FormalCo`, `InvariantLabsAI`. Use existing namespace if the entity already has pages in the garden; otherwise use a consistent, existing-style name.
- Choose **type**: **Blog**, **Article**, or **Essay**. Use Blog for blog-style or recurring posts; use Article or Essay for one-off pieces (article = e.g. magazine/publication; essay = e.g. long-form/opinion). When in doubt, use Blog or ask the user.

### Step 2: Determine YY/MM and Slug

- Use the post’s publication date for **YY** and **MM**. If no date is available, use the current date.
- Derive a short **slug** from the title (keep it readable and unique under that entity/Type/YY/MM).
- **Search the knowledge garden** for an existing page under that entity’s Blog, Article, or Essay namespace for the same piece (e.g. same URL or title). If found, update that page instead of creating a new one.

### Step 3: Create or Update the Page

- **Filename**: `pages/<Entity>___...___<Type>___YY___MM___Title or slug>.md` (each `/` in the namespace becomes `___`; **Type** is Blog, Article, or Essay).
- **Frontmatter** (follow existing precedents; do not add or remove `tags::` unless creating a new page and the rule specifies it):
  - `created-by:: [[Person/Full Name]]` when the piece is by a **person** and that person has or will have a person page. Omit for company/technology sources unless attributing to a specific person.
  - `tags::` Use **`[[Blog/Post]]`** for Blog, **`[[Article]]`** for Article, **`[[Essay]]`** for Essay. Include other topic tags only when they already exist in the garden or the user requests them; do not invent new tags.
  - Optional: `date-created::` set to the **entity’s** publication or creation date (e.g. `[[21/05]]` for May 2021). Follow the logseq-date-created-frontmatter rule: use the date the post/article/essay was created or published, not the date you added the page to the garden.
  - Optional: `alias::` if an alternative link form is useful (e.g. shorter or legacy namespace).
- **Body** (Logseq Flavored Markdown):
  - Start with a top-level heading and link to the original: `- # [Post Title](url)`
  - Add sections as appropriate, e.g. `- ## [[My Notes]]`, `- ## #Quotes`, `- ## Highlights`. Use TAB indentation; all content under bullet points.

### Step 4: Convert and Format Content

- If importing full post body or excerpts, follow the logseq-flavored-markdown and logseq-convert-from-md-to-lfm rules:
  - All content under bullet points with TAB indentation.
  - Headings as `- ##` or `- ###` under the main heading.
  - Blockquotes as `- > ...`. Code blocks with triple tildes `~~~` where appropriate.
- Prefer summarizing and linking over pasting entire articles unless the user asks for a full import. When in doubt, create a concise summary and link to the source.

### Step 5: Link from Person or Entity Page

- If the entity is a **person** with an existing person page, add a link to the new page under that person’s page (e.g. under a "Blog", "Articles", "Essays", or "Writing" section), using the canonical namespace link with the correct type: `[[Person/Full Name/Blog/YY/MM/slug]]`, `[[Person/Full Name/Article/YY/MM/slug]]`, or `[[Person/Full Name/Essay/YY/MM/slug]]`.
- If the entity is a **company or technology**, add or update a link from the relevant entity page if one exists.

### Step 6: Journal Entry (Optional)

- If the page is new, consider adding an entry in today’s journal linking to the new page (e.g. under [[Filed]] or a short note). Follow logseq-journal-updates and logseq-format-journal conventions; avoid repetitive "Imported ..." boilerplate.

## Related Rules and Conventions

- **logseq-person** (router): Search before creating person hubs; follow `[[Logseq/Entity/person]]`; use canonical `[[Person/...]]` title; one hub per human.
- **logseq-flavored-markdown**: Bullet prefix, TAB indent, no blank lines between content, headings under bullets.
- **Logseq Best Practice**: Use `ENTITY/Type/YY/MM/<POST>` (Type = Blog, Article, or Essay) for date namespacing and chronological order.
- **Frontmatter**: Do not modify, add, or remove the `tags::` frontmatter item on existing pages; when creating a new page, set `tags:: [[Blog/Post]]`, `[[Article]]`, or `[[Essay]]` to match the type, and any other tags the user or existing convention requires.
- **logseq-date-created-frontmatter**: Set `date-created::` to the entity’s publication/creation date, not the import date.

## Precedents (Examples from This Garden)

- Person blog: `[[Person/Simon Willison/Blog/26/02/Introducing Showboat and Rodney, so agents can demo what they've built]]`, `[[Person/Zack Steinkamp/blog/posts/2022-02-15-git-diff-amxd-max]]`, `[[Person/Fernando Lucktermberg/Blog/26/02/OpenClaw Hardened Deployment: A Non-Technical Companion Guide]]`
- Company/tech blog: `[[Anthropic/Blog/24/12/Building Effective Agents]]`, `[[CrowdStrike/Blog/26/02/What Security Teams Need to Know About OpenClaw]]`, `[[LangChain/Blog/25/10/Agent Frameworks v1.0]]`
- File naming: `Person___Simon Willison___Blog___26___02___Introducing Showboat and Rodney, so agents can demo what they've built.md`, `Anthropic___Blog___24___12___Building Effective Agents.md`

## Report

After completing the import, report:

- The page link (namespace form) and filename created or updated.
- The type used (Blog, Article, or Essay).
- Whether a person or entity page was updated with a link to the new post.
- Any optional journal entry added.
