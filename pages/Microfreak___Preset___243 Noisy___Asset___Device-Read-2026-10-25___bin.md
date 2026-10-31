logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Noisy slot 243 capture
	- [Download the slot 243 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___243%20Noisy___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 243 over USB on October 25, 2026 with `mise run microfreak:download --slot 243`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `1ea8f548ff1923aa8ef12880a947688f7f18bff6e02709c07dd9f29e1acf0a5d`.
