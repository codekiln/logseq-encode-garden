---
name: gitp-asset-gathering
description: >-
  Prepare a GitP episode from an exported WAV and a Making/Music/Log entry:
  create the garden session episode, capture MicroFreak presets, enrich notes
  from MIDI and manuals, upload media, and prepare a Gitpa publication PR. The
  human listens to one recording and merges the PR to publish.
---
# Prepare a GitP episode

Read `pages/GitP___How To___Draft an Episode from Session Assets.md` for the
human workflow and `pages/GitP___How To___Prepare Podcast Metadata.md` for
publication preparation. Start with the supplied music-making log and follow its
project and exported WAV links. Search existing notes before asking for a path.

## Prepare the session and recording

Read the Podcast/Episode and Asset entity definitions. Create or update the
session episode under `GitP/A/Session/YY/MM/DD-Day`, linking its source log.
The episode has one H1 title, a first-child description, and a direct MP3 media
embed: `![Episode recording](https://…mp3)`. Keep the recording's asset page for
file metadata and its download URL. Record graph edits in today's journal.

Convert the exported WAV to MP3 without changing the source WAV. Upload it to
B2 using the garden's configured credentials and page-derived asset filename.
Verify uploaded bytes and media metadata against the local MP3.

## Capture presets and describe the session

Read the MicroFreak preset entity rules and device workflow. Identify saved slots
from the source log, captured MIDI, and existing captures. Ask for missing slot
identification when the available evidence cannot establish which presets were
used; continue the recording and page preparation.

Back up each identified preset before renaming. Protect any unsaved active sound,
verify the slot still matches the backup, apply the episode naming convention,
download it, and verify that only intended metadata changed. Upload the exports
and add labeled download links to the session page.

Correlate captured MIDI CC numbers, values, and times with the MicroFreak manual.
Use preset metadata for oscillator type, category, and supported settings, and
read the Launchpad manual where relevant. Link useful explanations to their
sources. Distinguish recorded events from saved preset settings.

## Prepare publication

Follow the metadata how-to to sync the session into Gitpa as an exact-name Logseq proxy.
Sync asset pages separately when their metadata is needed in Gitpa. Keep episode text in the source garden and publication
identity on the Gitpa proxy. Prepare a worktree PR with the public page and feed
changes, run the relevant sync and RSS checks, commit, and push.

The PR includes the episode title, a direct MP3 link, and the reason to listen:
decide whether to publish this recording. Leave the publication PR for the human
to merge after one listen and a go decision. CI publishes after the merge.

Automatic preset capture, renaming, and MIDI enrichment still need implementation.
Report the concrete missing capability if it prevents preparing the episode.
