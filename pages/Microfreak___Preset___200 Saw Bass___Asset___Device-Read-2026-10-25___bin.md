logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Saw Bass slot 200 capture
	- [Download the slot 200 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___200%20Saw%20Bass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 200 over USB on October 25, 2026 with `mise run microfreak:download --slot 200`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `e09624549b55a1fda405b7ff5a3388c3fcfaacebfe0ab79116b3bf5ad4ac9ad0`.
