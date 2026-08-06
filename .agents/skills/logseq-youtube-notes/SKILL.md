---
name: logseq-youtube-notes
description: >-
  Format a YouTube video transcript inside a Logseq page into clean, navigable,
  timestamped Logseq-Flavored Markdown. Use when the user pastes a raw YouTube
  transcript, asks to organize/clean up video notes, add clickable
  {{youtube-timestamp}} headings, or structure a {{video ...}} block's notes. Do
  not use for non-video transcripts or for general LFM formatting (that is the
  logseq-lfm skill / logseq-core rule).
metadata:
  short-description: Clean and structure YouTube transcripts into timestamped LFM
---
# Logseq YouTube transcript notes

Turn a raw, AI-generated transcript under a `{{video ...}}` block into readable, chapter-structured LFM with clickable timestamps.

## Quick path

1. Confirm the page has the video block shape (`- ## [[Video]]` → `{{video URL}}` → notes nested underneath). Notes/headings MUST nest under the video block for timestamps to be clickable.
2. If you can reach the video, name the section headings after the video's chapters; otherwise group by topic with your best judgment (ask the user if unsure).
3. Reformat the transcript per [references/transcript-formatting.md](./references/transcript-formatting.md): timestamped section headings, subsections, cleaned quotes, semantic links.
4. Apply `logseq-core` LFM rules (bullets, TAB nesting, no blank lines, protected `tags::`).

## Always

- Headings carry timestamps: `### {{youtube-timestamp X}} Topic`, `####`/`#####` for subsections.
- Clean up AI transcription errors (spelling, tech names) using context; quote the transcript where useful.
- Only link `[[Page]]` / `#Tag` that already exist (see `pages/Index.md`); never invent pages — use the `logseq-link-hygiene` skill if unsure.
- No heading without bullet content under it; aim for chapter-sized sections (~90s+ each).

## Reference

- [references/transcript-formatting.md](./references/transcript-formatting.md) — full heading structure, before/after example, semantic-linking and content-formatting guidelines.
