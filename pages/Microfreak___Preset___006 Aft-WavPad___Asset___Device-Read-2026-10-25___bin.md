logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Aft-WavPad slot 6 capture
	- [Download the slot 6 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___006%20Aft-WavPad___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 6 over USB on October 25, 2026 with `mise run microfreak:download --slot 6`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `25bd41e5ce7e418689c968eeb4db89fe31291918869cfc72147f8ef0b3bdf960`.
