logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Trance slot 3 capture
	- [Download the slot 3 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___003%20Trance___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 3 over USB on October 25, 2026 with `mise run microfreak:download --slot 3`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `09a16bb0f127df185a8ec15fcb250804766e89b33448edb0738de1a85c31714a`.
