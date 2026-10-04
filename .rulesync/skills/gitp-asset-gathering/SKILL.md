---
name: gitp-asset-gathering
description: >-
  Prepare a GitP episode from an exported WAV and a Making/Music/Log entry:
  create the garden episode, capture MicroFreak presets, enrich notes from MIDI
  and manuals, upload MP3 and presets to B2, and prepare a Gitpa publication PR.
  The human listens to one episode recording and merges the PR to publish.
targets: ["*"]
---

# Prepare a GitP episode

Read `pages/GitP___How To___Draft an Episode from Session Assets.md` for the
human workflow and `pages/GitP___How To___Prepare Podcast Metadata.md` for the
metadata commands. Start from the supplied Making/Music/Log entry and follow its
project and WAV pointers. Search existing notes before asking for a missing path.

## Create the episode and prepare audio

Read the Podcast/Episode entity definition and search for an existing episode.
Create or update the GitP episode under the show's namespace, linking the source
log entry and its pointers. Preserve human notes and publication identity. Do not
invent an air date for an unpublished episode. Record graph edits in today's journal.
Keep any technical file inventory on the session assets page and link it from the
episode; the episode page holds the description and listening/download links.

Use the exported WAV as the one episode recording. Convert it to MP3 without
changing the source WAV. Do not select among stems, assemble commentary, or ask
the human for time ranges, trims, or editorial assessments. Upload the MP3 to B2
under a stable episode path using the garden's configured credentials; never print
secrets. Verify uploaded bytes and media metadata against the local MP3.

## Capture saved presets

Read the MicroFreak preset entity rules and existing device workflow documentation
before device writes. Identify the saved slots used in this episode from the log,
MIDI, and any existing captures. A current slot's contents alone cannot establish
what was used in an older session. If the association cannot be established, ask
only for the missing slot identification and continue independent episode work.

Back up each identified preset before renaming. Use the documented episode naming
convention and device name limits. Protect any unsaved active sound, verify that
the slot still holds the captured sound, rename it, download it, and verify that
only intended metadata changed. Upload the exports to B2 and add labeled download
links to the episode page. Never rename unrelated presets or claim that an
unimplemented device command has run.

## Describe the session

Read the captured MIDI data, source log, and relevant MicroFreak and Launchpad
manual sections. Correlate MIDI CC numbers, values, and times with the documented
controls. Read preset metadata for oscillator type, category, and other supported
settings. Link each useful explanation to its source. Distinguish session events
from saved preset settings; omit unsupported historical claims. Audio filenames,
track names, and a preset's current name do not establish recording content.
Commentary transcription is not required for this workflow.

## Prepare the Gitpa publication PR

Use `mise run gitpa:episode:draft -- <project>` for the available metadata checks
and JSON export, then the Gitpa importer. Read the task documentation first. If
an edited session asset page already exists, use fresh output paths and transfer
checked facts without replacing human edits. Review proposed copy yourself.

Prepare the Gitpa episode page, media links, publication metadata, and feed changes
in a worktree. Run the relevant importer and feed checks, commit, push, and open a
PR. Include the episode title, a direct MP3 link, and the reason to listen: decide
whether to publish this recording. The human's remaining work is one listen and a
go/no-go decision. Leave the publication PR for the human to merge; CI publishes
after that merge. Do not substitute an AI listening assessment for this decision.

Some parts of this workflow still need automation, particularly device capture,
rename, and MIDI enrichment. Report a concrete missing capability if it blocks
completion; do not turn it into an extra human review checklist.
