# MicroFreak tasks

File tasks for reading, writing and checking presets on an Arturia MicroFreak over USB. Run them from the garden root as `mise run microfreak:<task>`; `mise run microfreak:<task> --help` lists each task's flags. The documentation lives in the garden pages linked below.

| Task | What it does | Garden page |
| --- | --- | --- |
| `download` | Save one slot as a `.bin` file | [Microfreak/CLI/Preset metadata over USB](../../pages/Microfreak___CLI___Preset%20metadata%20over%20USB.md) |
| `upload` | Write a saved `.bin` to a slot and read it back | [Microfreak/CLI/Upload a preset](../../pages/Microfreak___CLI___Upload%20a%20preset.md) |
| `inspect` | Print a saved preset's named parameters, and with `--sequence` its patterns, as JSON | [Microfreak/CLI/Inspect a preset](../../pages/Microfreak___CLI___Inspect%20a%20preset.md) |
| `compare` | Compare the named parameters of two saved presets | [Microfreak/CLI/Preset metadata over USB](../../pages/Microfreak___CLI___Preset%20metadata%20over%20USB.md) |
| `empty-slots` | List the slots that hold no preset | [Microfreak/Sequence/Write a sequence](../../pages/Microfreak___Sequence___Write%20a%20sequence.md) |
| `write-sequence` | Write a described sequence into a preset file, a slot or both | [Microfreak/Sequence/Write a sequence](../../pages/Microfreak___Sequence___Write%20a%20sequence.md) |
| `verify-sequence` | Write a described sequence, play it, record it, download it again and compare | [Microfreak/Sequence/Write a sequence](../../pages/Microfreak___Sequence___Write%20a%20sequence.md) |
| `audition` | Play a slot's sequence and report the notes per step from MIDI out and the Zoom H5 | [Microfreak/CLI/Audition a sequence](../../pages/Microfreak___CLI___Audition%20a%20sequence.md) |
| `sync` | Preview or apply preset metadata to the garden's preset pages | [Microfreak/CLI/Preset metadata over USB](../../pages/Microfreak___CLI___Preset%20metadata%20over%20USB.md) |
| `refresh` | Read every slot and list presets that differ from their garden pages | [Logseq/Entity/Preset/Synth/Microfreak](../../pages/Logseq___Entity___Preset___Synth___Microfreak.md) |
| `pages` | Write decoded settings onto preset pages from saved reads | [Logseq/Entity/Preset/Synth/Microfreak](../../pages/Logseq___Entity___Preset___Synth___Microfreak.md) |
| `test` | Run the tests for all of these tasks | |

More context:

- [Microfreak/Sequence/Storage](../../pages/Microfreak___Sequence___Storage.md): where a preset keeps patterns A and B and what each step holds.
- [Microfreak/Sequence/Research](../../pages/Microfreak___Sequence___Research.md): the experiments behind the sequence tasks.
- [Microfreak/UG](../../pages/Microfreak___UG.md): the garden's copy of the MicroFreak user guide.

Python helpers live in [`lib/`](lib/). Tests use synthetic data; private preset exports, recordings and raw dumps stay out of this public repository.
