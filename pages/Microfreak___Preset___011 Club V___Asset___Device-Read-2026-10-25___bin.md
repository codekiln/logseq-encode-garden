logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Club V slot 11 capture
	- [Download the slot 11 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___011%20Club%20V___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 11 over USB on October 25, 2026 with `mise run microfreak:download --slot 11`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `d46d0d2639814a80c2d99b42dc181d291701a6d539d8d82516a43a0c1fbad547`.
