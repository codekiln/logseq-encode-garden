logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Darkstream slot 12 capture
	- [Download the slot 12 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___012%20Darkstream___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 12 over USB on October 25, 2026 with `mise run microfreak:download --slot 12`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `8b284b55fd19e3539509f8d07a3e6fbec023598e364d0a027c92c8d742797d33`.
