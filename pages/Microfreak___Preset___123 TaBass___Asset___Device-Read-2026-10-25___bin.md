logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # TaBass slot 123 capture
	- [Download the slot 123 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___123%20TaBass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 123 over USB on October 25, 2026 with `mise run microfreak:download --slot 123`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4c0f43d92ef8c043b6de5d270f3b6e0031f27a60c9ebb1d933672821e0cfbded`.
