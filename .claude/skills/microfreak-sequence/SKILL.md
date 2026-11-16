---
name: microfreak-sequence
description: >-
  Put a sequence that codekiln describes in words into a MicroFreak preset slot:
  notes, chords, rests, ties, accents, modulation tracks, patterns A and B, 1 to
  64 steps. Use when asked to put, write, program, change or check a sequence,
  pattern, arpeggio, bass line or riff in a MicroFreak preset or slot. Routes to
  the garden page Microfreak/Sequence/Write a sequence and the mise tasks
  microfreak:write-sequence and microfreak:verify-sequence.
---
# Write a described sequence into a MicroFreak preset

Read `pages/Microfreak___Sequence___Write a sequence.md` (the garden page `Microfreak/Sequence/Write a sequence`) and follow its Steps. It shows how to turn the request into a description file, with worked examples, how to pick the slot and the base sound, the commands, how to read the verify report, what pattern B needs, and what to tell codekiln.

The two commands it builds on, run from the garden root:

```sh
# preview: reads the base and prints what it would store, writes nothing
mise run microfreak:write-sequence "$TMPDIR/microfreak-seq/seq.yaml" --base 358
# write, play, record, download again and compare, step by step
mise run microfreak:verify-sequence "$TMPDIR/microfreak-seq/seq.yaml" --base 358 --slot N \
  --backup-dir "$TMPDIR/microfreak-seq/backup-1" --out-dir "$TMPDIR/microfreak-seq/verify"
```

Hold to these while you work:

- Keep description files, backups, recordings and reports outside the repository. The presets are codekiln's and the repository is public.
- Write to the slot codekiln names, or to an empty slot you checked. A slot that holds a preset needs `--backup-dir`, and codekiln needs to know where the backup is.
- Pattern B is written and checked by download; hearing it takes one press of B on the panel.

`pages/Microfreak___Sequence___Storage.md` describes how a preset stores the sequence, and `pages/Microfreak___Sequence___Research.md` lists the runs on the instrument behind the workflow.
