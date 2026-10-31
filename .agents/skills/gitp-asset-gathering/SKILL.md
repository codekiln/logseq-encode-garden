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

## Research every referenced preset

Read the MicroFreak preset entity rules. Find every saved preset linked from the
session, including brief appearances and presets already present in the garden.
An existing page with only header metadata or an empty Notes heading still needs
research. Identify sounds from the source log, captured data and existing exports;
a name, category or slot number alone cannot establish the sound's settings.

Work from verified saved exports before considering a new device capture. Record
the export filename, capture date, computer-bank slot when relevant, and digest.
Check the payload against the available archive or factory source and cite the
decoder, parameter mapping and instrument manual used to interpret it. An archived
factory match establishes a baseline; it does not establish session-time settings
or unsaved edits. Do not change hardware to research existing exports.

Enrich each preset page upstream with these recognizable notes sections:

- **Saved export and provenance:** which saved bytes support the account, their
  date and identity, factory/archive relationship, and limits on session evidence.
- **Oscillator:** model, what its controls mean, and supported saved settings.
- **Filter:** type, relevant controls and supported saved settings.
- **Envelopes:** main and cycling envelope behavior and supported settings.
- **LFO:** shape, rate/sync behavior and supported settings.
- **Modulation matrix:** source, destination, signed amount and performance effect.
- **Performance and session context:** how to play the saved sound, and which
  changes were actually observed in the episode versus inferred from its baseline.

Use verified units or label normalized domains and raw values explicitly. State
uncertainty where a destination, conversion, firmware assumption or resource identity
is unsupported. Keep large raw numeric reports outside the graph; write the control
meaning and listening implications that help a reader. Cite substantive claims.
Describe an unidentified initialized patch plainly; do not invent a numbered saved
preset, export or default settings for it.

Run the repeatable source audit before publication:

```sh
mise run gitpa:preset:audit --episode 'GitP/A/Session/YY/MM/DD-Day' --check
```

The audit checks recorded evidence and topic coverage, not decoding accuracy or
listening quality. Resolve stubs and missing research for the selected episode;
report any unavailable evidence without filling it with guesses. Historical audits
are advisory and do not gate the whole site's deployment:

```sh
mise run gitpa:preset:audit --all --json > /tmp/gitp-preset-audit.json
```

When a new preset capture is part of the authorized task, follow the device
workflow: protect any unsaved active sound, back up the identified slot, verify it
still matches, and only then apply an authorized rename and download. Verify that
only intended metadata changed, upload the prepared export, and add its download
link. Missing slot identification leaves hardware unchanged while other preparation
continues.

## Describe the session

Correlate captured MIDI CC numbers, values, and times with the MicroFreak manual.
Use MIDI analysis in listener notes when it explains how chapters differ, naming
the controls exercised during each passage. A session-wide parameter inventory
is not useful listener context. Use preset metadata for oscillator type, category,
and supported settings, and read the Launchpad manual where relevant. Link useful
explanations to their sources. Distinguish recorded events from saved preset settings.

Export the full session as a standard MIDI file for DAW import, preserving notes
and controller changes and checking its tempo and alignment with the recording.
Upload it as an Asset/B2 page and add a direct download link to the episode.

## Prepare publication

Follow the metadata how-to to sync the session into Gitpa as an exact-name Logseq proxy.
Sync every referenced preset page into Gitpa after enriching it upstream. Sync
the episode’s audio and MIDI asset pages separately so the publication checkout
includes their metadata. Keep episode text in the source garden and publication
identity on the Gitpa proxy. Prepare a worktree PR with the public page and feed
changes, run the relevant sync and RSS checks, commit, and push.

The PR includes the episode title, a direct MP3 link, and the reason to listen:
decide whether to publish this recording. Leave the publication PR for the human
to merge after one listen and a go decision. CI publishes after the merge.

Automatic preset capture, renaming, and MIDI enrichment still need implementation.
Report the concrete missing capability if it prevents preparing the episode.
