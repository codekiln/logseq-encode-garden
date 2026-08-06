---
name: logseq-slides
description: >-
  Author or fix Logseq slideshow pages where top-level bullets are section
  titles (H2) and nested bullets are individual slides with bullet points and a
  16:9 image. Use when the user asks to build a slide deck/presentation in
  Logseq, add slides, or fix slide structure/image sizing. Do not use for
  ordinary page bullets or non-slide content.
metadata:
  short-description: 'Build Logseq slideshow pages (sections, slides, 16:9 images)'
---
# Logseq slides

Build slide decks where structure maps to Logseq's reveal.js export.

## Rules

Read [references/slide-structure.md](./references/slide-structure.md) before authoring. Key points:

- Each top-level unordered bullet (`-`) = a section title (rendered H2).
- Each nested bullet (`\t-`) = one slide; give it multiple `*` bullet points describing the topic.
- One image per slide, 16:9: up to `680px` wide for slides under 10 words, ~`400px` for slides with more than 10 words.
- Keep each slide self-contained: one image, clear bullets, one coherent message.
- Do NOT split a single slide by using `-` instead of `*` for its points — that creates extra slides.

See the EXAMPLE / COUNTER_EXAMPLE in the reference for the single-slide vs three-slide distinction.
