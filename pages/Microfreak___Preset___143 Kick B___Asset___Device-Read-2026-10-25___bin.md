logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Kick B slot 143 capture
	- [Download the slot 143 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___143%20Kick%20B___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 143 over USB on October 25, 2026 with `mise run microfreak:download --slot 143`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `8eff1c5031b275c2439cacfbe64c802e28e3c8f65fdc68522a6e15a871805808`.
