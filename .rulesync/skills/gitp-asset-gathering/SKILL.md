---
name: gitp-asset-gathering
description: >-
  Gather GitP session recordings and garden notes, assess candidates for podcast
  inclusion, and draft episode copy and an audio preparation plan. Use when a
  recording session should become a podcast draft, including before a release
  MP3 exists. Complements the gitpa episode mise tasks.
targets: ["*"]
---

# GitP asset gathering

Read `pages/GitP___How To___Draft an Episode from Session Assets.md` for the
human workflow and `pages/GitP___How To___Prepare Podcast Metadata.md` for the
later handoff. Start from the supplied date and project location; if one is
missing, search existing GitP session notes and project locations before asking.

## Gather

Find related garden notes and journal entries by date and project name. Inventory
the session's Ableton sets, audio files/stems, MIDI, and patch exports. Record
project-relative paths, format, duration when inspected, and source-note links in
`GitP/Session/YY/MM/DD Day/Session Assets`. Reuse an existing page and preserve its
notes; follow the garden's Logseq rules and record graph edits in today's journal.
A prepared MP3 is not required at this stage. Read original files without moving,
renaming, or overwriting them.

## Assess

Listen to available audio with supported playback or audio inspection tools.
Assess musical interest, intelligibility, recording quality, useful time ranges,
and duplication between stems and mixed output. Recommend include, edit, or omit
with a reason grounded in what was inspected. If listening is unavailable, say
which files remain unassessed and continue gathering and drafting from the notes;
do not claim a listening assessment from waveform statistics or filenames.

Distinguish source-note statements, observed recording content, and inference.
Ableton track names and filenames identify candidates, not their content or
suitability. Do not infer presets from names alone. Treat speech recognition as a
candidate transcript: check it against the recording before using it in public
copy, and omit hallucinated or unsupported speech.

## Draft

Write proposed title, description, and show notes, plus an audio selection/order
and edit/export plan on the session asset page. Keep source links and uncertainties
alongside the draft, outside proposed public copy. Use existing metadata as a
starting point without replacing human edits. Keep drafts unpublished and original
recordings local unless uploading or publishing is authorized by the conversation.

## Prepare the handoff

When chosen audio has been prepared as an MP3, read
`pages/GitP___mise___Task___episode___draft.md` and use
`mise run gitpa:episode:draft -- <project>` for deterministic checks and JSON.
If the session asset page already exists, select a fresh `--assets-page` and
`--output-dir`, then bring useful checked facts into the edited page without
replacing human edits. The task's description is a source-note proposal;
review the JSON against the drafted copy before import. Report any remaining
listening, audio preparation, or publication decisions with the draft.
