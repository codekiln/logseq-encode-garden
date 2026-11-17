---
name: microfreak-patch
description: >-
  Put a sound the user describes in words into a MicroFreak preset slot:
  oscillator type and knobs, filter, envelopes, LFO, glide, bend range, scale,
  unison, chord mode, preset volume and the modulation matrix, with an optional
  sequence. Use when asked to make, program, change or check a patch, preset,
  sound, lead, bass, pad or stab on the MicroFreak. Routes to the garden page
  Microfreak/Patch/Write a patch and the mise tasks microfreak:write-patch and
  microfreak:probe.
targets: ["*"]
codexcli:
  short-description: Write a described patch into a MicroFreak preset slot
---

# Write a described patch into a MicroFreak preset

Read `pages/Microfreak___Patch___Write a patch.md` (the garden page `Microfreak/Patch/Write a patch`) and follow its Steps. They cover where to keep your files, how to write the request as a description file, how to pick the slot and the base, the preview, write and listen commands, and what to tell the user. Below the Steps, the page lists every description key, explains how to read musical words and gives worked examples. The page is the user's own note, so "I" and "me" there mean the user.

Run the tasks from the root of a garden checkout on current `main`: the checkout that `ghq list --full-path --exact github.com/codekiln/logseq-encode-garden` prints, after `git pull --ff-only`, or a worktree of `origin/main`. Each task runs the code of the checkout it is started from.

The commands it builds on:

```sh
# list the empty slots, reading only preset headers
mise run microfreak:empty-slots
# preview: reads the base and prints each setting it would change, writes nothing
mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359
# write the slot, backing up what it held
mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359 --slot N \
  --backup-dir "$TMPDIR/microfreak-patch/backup-1"
# play the slot and measure pitch, level and brightness through the Zoom H5
mise run microfreak:probe --slot N --no-write --script "$TMPDIR/microfreak-patch/script.yaml" \
  --output "$TMPDIR/microfreak-patch/report.json"
```

Hold to these while you work:

- Keep descriptions, backups, recordings and reports outside the repository. The repository is public, and the backups hold the user's presets.
- Write to the slot the user names, or to an empty slot you checked. A slot that holds a preset needs `--backup-dir`; tell the user where the backup is.
- Begin a description with `start: plain` unless the request builds on the base's own sound; the page lists what slot 359 holds.
- Settings without a measured conversion take 0–1 values. Say which value you chose for each of them.

For a sequence in the patch, the `sequence` key takes the format of `pages/Microfreak___Sequence___Write a sequence.md`. `pages/Microfreak___Patch___Storage.md` says what each stored setting means, and `pages/Microfreak___Patch___Research.md` lists the runs on the instrument behind it.
