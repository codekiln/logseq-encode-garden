logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Brass 1 slot 189 capture
	- [Download the slot 189 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___189%20Brass%201___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 189 over USB on October 25, 2026 with `mise run microfreak:download --slot 189`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `eb55a86354cd146caa967f6c5ab40c8aa85e6b84c709163856a2f341811f4b0c`.
