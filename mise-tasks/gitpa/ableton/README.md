# Logseq to Ableton Live 11

`sync` reads an `Ableton Session` block and edits a copy of an existing Live 11 Set. The base supplies devices, tracks, internal object IDs and MIDI mapping structures.

```sh
mise run gitpa:ableton:sync -- \
  --page 'GitP/A/Session/26/10/29-Thu' \
  --output "$HOME/Documents/ableton/GitP/26.10.29 Project/26.10.29.als" \
  --fresh
```

The default prints the validated plan. Add `--apply` to write the new Set. An existing output path is always refused. `--base-template /path/to/base.als` overrides the declaration. `--garden /path/to/garden` selects another source graph.

`--fresh` clears recorded clips in Arrangement, Session and take lanes, automation envelopes, and locators. It resets playback to the beginning and disables looping. It also permits omitting unwanted tracks from the declaration; return tracks are retained. Without `--fresh`, existing musical content is preserved and track pruning or locator replacement is rejected.

## Declaration

```markdown
- Ableton Session
  spec-version:: 1
  live-version:: 11
  base-template:: /absolute/path/to/seed.als
  tempo:: 120
  time-signature:: 4/4
  intention:: Explore the contrast between Pattern A and Pattern B.
  - Tracks
    - Pattern A Audio
      track-key:: pattern-a-audio
      source-track-id:: 23
      type:: audio
      monitor:: auto
      arm:: false
      color:: 8
      audio-from:: AudioIn/External/M2
      audio-to:: AudioOut/Track.26/TrackIn
  - Scenes
    - Introduction
      scene-key:: introduction
      color:: 8
  - Locators
    - Introduction
      bar:: 1
    - Exploration
      beats:: 64
  - Controls
    - Arrangement Record
      action:: record
      cc:: 119
      channel:: 16
```

The optional `intention` property sets the Live Set annotation (Set Info Text). Omitting it preserves the seed annotation.

Use Logseq bullets with tab or space indentation. Properties belong beneath their bullet. Code fences are ignored. A page may contain one `Ableton Session` block anywhere in its outline.

A page-level `ableton-template:: [[GitP/A/Template/Pattern A and B]]` inherits that page's declaration. The episode's session properties override inherited properties. An episode's `Tracks`, `Scenes`, `Locators`, or `Controls` section replaces the entire inherited section with the same name. An omitted section is inherited. Inheritance cycles and duplicate properties are errors.

Track labels become names. `track-key`, `source-track-id`, and `type` are required; source IDs select existing tracks. Types are `audio`, `midi`, `return`, or `group`. The compiler retains device chains and does not create tracks or groups. Optional `monitor` is `in`, `auto`, or `off`; `arm` is `true` or `false`; color is a Live palette index. Native routing targets can be supplied through `audio-from`, `audio-to`, `midi-from`, and `midi-to`. Track output references must resolve to retained tracks.

Scenes rename existing scene slots in order; each requires a unique `scene-key`. Additional existing scene slots remain available. Locators use either one-based `bar` or zero-based quarter-note `beats`. This version supports 4/4 time.

Control actions are `record`, `set-locator`, `previous-locator`, and `next-locator`. CC values are 0–127; declared MIDI channels are 1–16. The compiler converts channels to Live's zero-based XML representation. It preserves keyboard assignments. Configure matching messages in the Launchpad Custom Mode and enable Remote on that MIDI input in Live.

Audio interface selection, MIDI port enablement and controller configuration are Live/device settings outside the Set. Open, save and reopen generated Sets in Live to validate the resulting template with the installed Live version.

## Tests

```sh
python3 -m unittest discover -s mise-tasks/gitpa/ableton/lib -p 'test_*.py' -v
```

## Seed maintenance

The tracked seed contains organizational groups Pattern A (30) and Pattern B (31). Its child tracks retain the performance bus routes. `lib/prepare_seed.py` is a constrained maintenance helper: it copies the observed empty GroupTrack30 from a Live-saved Set, allocates new global automation/object IDs for GroupTrack31, preserves local slot/send/lane IDs, and groups existing tracks21/22. It rejects device-bearing or automated source groups and unexpected identities. The page compiler only edits existing groups.

After modifying a seed, open, save and reopen it in Live before using it for episodes.
