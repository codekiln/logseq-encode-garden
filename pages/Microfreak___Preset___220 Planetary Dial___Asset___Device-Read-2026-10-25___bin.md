logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Planetary Dial slot 220 capture
	- [Download the slot 220 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___220%20Planetary%20Dial___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 220 over USB on October 25, 2026 with `mise run microfreak:download --slot 220`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `f02d40dfe38e37a99619b70ecfc933654f603dfebdc877920497177b7f8c0b7c`.
