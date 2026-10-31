logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # ArpZap slot 79 capture
	- [Download the slot 79 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___079%20ArpZap___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 79 over USB on October 25, 2026 with `mise run microfreak:download --slot 79`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `8cc5fef304473d060422ddd1aea102be7c1e128c3814525751b7bf66229c42c6`.
