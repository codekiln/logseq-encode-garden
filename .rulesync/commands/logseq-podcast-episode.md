---
targets:
  - '*'
description: Log a podcast episode using Person/Pod/YY/MM EpisodeTitle, ensure Person/Podcast page aliases, and add a journal entry for a specified date
argument-hint: Person (required); Show Name (required); Episode Title (required); Episode Date (required, YYYY/MM/DD); Journal Date (required, YYYY_MM_DD); Episode URL (optional); Notes/Highlights/Transcript (optional)
---
# Log a Podcast Episode in Logseq

This command creates or updates podcast pages using the podcast conventions for this garden:
- Episode page: `[[<Person>/Pod/<YY>/<MM> <EpisodeTitle>]]`
- Podcast show page: `[[<Person>/Podcast]]`
- Journal entry added to the date provided by the user (not necessarily today).

## Variables

- **Person** - **Required**: Host/person namespace (example: `Gergely Orosz` for `[[Person/Gergely Orosz]]`).
- **Show Name** - **Required**: Podcast/show title for aliases (example: `The Pragmatic Engineer Podcast`).
- **Episode Title** - **Required**: Episode title text.
- **Episode Date** - **Required**: `YYYY/MM/DD`.
- **Journal Date** - **Required**: `YYYY_MM_DD` (journal filename format).
- **Episode URL** - Optional: Canonical episode link.
- **Notes/Highlights/Transcript** - Optional: User-provided content.

## Conventions

- **Episode naming**
  - Link format: `[[<Person>/Pod/<YY>/<MM> <EpisodeTitle>]]`
  - File format: `pages/<Person>___Pod___<YY>___<MM> <EpisodeTitle>.md`
- **Podcast show page**
  - Page link: `[[<Person>/Podcast]]`
  - File: `pages/<Person>___Podcast.md`
  - Must include aliases:
    - `alias:: [[Podcast/<Show Name>]], [[<Person>/Pod <Show Name>]]`
- **Episode metadata**
  - `date-created:: [[YYYY/MM/DD]]`
  - `tags:: [[Podcast/Episode]]`
- **Podcast tag expectations**
  - If creating a new show page, add `tags:: [[Podcast]]`.

## Workflow

### Step 1: Normalize and validate inputs

- Parse required fields: Person, Show Name, Episode Title, Episode Date, Journal Date.
- Validate date formats:
  - Episode Date: `YYYY/MM/DD`
  - Journal Date: `YYYY_MM_DD`
- Derive:
  - `<YY>` from Episode Date year (last 2 digits)
  - `<MM>` from Episode Date month (2 digits)
  - Person namespace link: `[[Person/<Person>]]`

### Step 2: Ensure the show page exists and aliases are correct

- Target show page: `pages/<Person>___Podcast.md` (`[[<Person>/Podcast]]`).
- If it exists:
  - Ensure `alias::` includes both:
    - `[[Podcast/<Show Name>]]`
    - `[[<Person>/Pod <Show Name>]]`
  - If aliases are missing, update the existing `alias::` line (do not duplicate aliases).
- If it does not exist, create it with:
  - `alias:: [[Podcast/<Show Name>]], [[<Person>/Pod <Show Name>]]`
  - `tags:: [[Podcast]]`
  - `created-by:: [[Person/<Person>]]`
  - Body with at least:
    - `- # <Show Name>`
    - Optional short description block if the user provides one.

### Step 3: Create or update the episode page

- Target episode file:
  - `pages/<Person>___Pod___<YY>___<MM> <EpisodeTitle>.md`
- If page exists, update in place (do not duplicate sections).
- Required top attributes:
  - `date-created:: [[YYYY/MM/DD]]`
  - `tags:: [[Podcast/Episode]]`
- Episode page structure should include:

~~~markdown
date-created:: [[YYYY/MM/DD]]
tags:: [[Podcast/Episode]]

- # [<Episode Title>](<Episode URL>)
	- Podcast: [[<Person>/Podcast]]
	- Host: [[Person/<Person>]]
	- Episode date: [[YYYY/MM/DD]]
	- ## Notes
		- <user notes, if provided>
	- ## Highlights
		- <highlights, quotes, or key takeaways if provided>
	- ## Transcript
		- <transcript snippets or transcript link if provided>
~~~

- If `Episode URL` is missing, use:
  - `- # <Episode Title>` (without markdown link).
- Keep the notes/highlights/transcript sections present even if content is pending.

### Step 4: Update the specified journal page

- Journal file path: `journals/<Journal Date>.md`
- If the journal file does not exist, create it.
- Add a bullet linking the episode page:
  - `- [[<Person>/Pod/<YY>/<MM> <EpisodeTitle>]]`
- Prefer adding a short context note on the same bullet or child bullet, including the show page:
  - `[[<Person>/Podcast]]`

### Step 5: Deduplication and safety checks

- Do not create duplicate episode pages for the same person + `YY/MM` + title.
- Do not create duplicate alias entries on `[[<Person>/Podcast]]`.
- Preserve existing content in both pages; only append/update minimally.

## Report

- Confirm:
  - Show page created/updated: `[[<Person>/Podcast]]`
  - Episode page created/updated: `[[<Person>/Pod/<YY>/<MM> <EpisodeTitle>]]`
  - Journal page updated: `journals/<Journal Date>.md`
- Include file paths touched.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-page-naming-reference` - Namespace and filename conventions
- rule: `logseq-flavored-markdown` - Logseq markdown structure
- rule: `logseq-journal-updates` - Journal update requirements
